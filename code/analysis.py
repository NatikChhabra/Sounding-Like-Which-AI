"""All tables and figures. Usage: python analysis.py DATA_DIR {essay|arxiv|hansard|all}

Writes results/<genre>_*.csv|json. Every number in the paper must come from these files.
"""
import json, sys
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy.stats import spearmanr
from sklearn.metrics import cohen_kappa_score, roc_auc_score

import features
import mso

OUT = Path(__file__).resolve().parent.parent / "results"
CHAT = lambda m: not str(m).startswith("raid-") or str(m).endswith(("-chat", "chatgpt", "gpt4"))


def save(name, obj):
    OUT.mkdir(exist_ok=True)
    if isinstance(obj, pd.DataFrame):
        obj.to_csv(OUT / f"{name}.csv", index=False)
    else:
        (OUT / f"{name}.json").write_text(json.dumps(obj, indent=2, default=float))
    print(f"--- {name}\n{obj if isinstance(obj, pd.DataFrame) else json.dumps(obj, indent=1, default=float)}")


def region(human, llm, genre):
    """Train the MSO instrument on chat-model text; return scorer + diagnostics shared by all genres."""
    llm = llm[llm.model.map(CHAT)]
    X, y, groups, L = mso.training_set(human, llm)
    auc, p_cv = mso.cv_auc(X, y, groups)
    n_h = int((y == 0).sum())
    per = []
    for (m, pk), idx in L.reset_index(drop=True).groupby(["model", "prompt"]).groups.items():
        yy = np.r_[np.zeros(n_h), np.ones(len(idx))]
        pp = np.r_[p_cv[:n_h], p_cv[n_h + np.asarray(idx)]]
        per.append({"model": m, "prompt": pk, "n": len(idx), "auc": roc_auc_score(yy, pp)})
    save(f"{genre}_separability", pd.DataFrame(per))
    score, vec, keep, model = mso.fit(X, y)
    up, down = mso.top_features(vec, keep, model)
    save(f"{genre}_features_llm_typical", up)
    save(f"{genre}_features_human_typical", down)

    # robustness: second instrument (gradient boosting) and leave-one-model-out regions
    score_gb = mso.fit(X, y, kind="gbm")[0]
    scored = human[human.pool == "score"]
    pa, pb = score(list(scored.f)), score_gb(list(scored.f))
    a, b = pa >= 0.5, pb >= 0.5
    lomo = []
    for m in sorted(llm.model.unique()):
        Xm, ym, _, _ = mso.training_set(human, llm, exclude_model=m)
        s_m = mso.fit(Xm, ym)[0]
        held = llm[llm.model == m]
        lomo.append({"held_out_model": m, "recall_on_unseen_model": float((s_m(list(held.f)) >= 0.5).mean()),
                     "mso_scored_humans": float((s_m(list(scored.f)) >= 0.5).mean())})
    save(f"{genre}_lomo", pd.DataFrame(lomo))
    save(f"{genre}_instrument", {
        "cv_auc_all": auc, "n_train_per_class": n_h,
        "mso_logreg": float(a.mean()), "mso_gbm": float(b.mean()),
        "kappa_logreg_vs_gbm": float(cohen_kappa_score(a, b)),
        "spearman_scores_logreg_vs_gbm": float(spearmanr(pa, pb).statistic),
        "share_flagged_by_both": float((a & b).mean())})
    return score


def essay(data):
    human, llm = mso.load(data, "essay")
    score = region(human, llm, "essay")
    s = human[human.pool == "score"].copy()
    s["p"] = score(list(s.f))
    s["in_region"] = (s.p >= 0.5).astype(int)
    rows = [{"group": "all", "n": len(s), **dict(zip(["mso", "lo", "hi"], mso.mso(s.p)))}]
    for g, d in s.groupby("group"):
        rows.append({"group": g, "n": len(d), **dict(zip(["mso", "lo", "hi"], mso.mso(d.p)))})
    for g, d in s.groupby("grade"):
        rows.append({"group": f"grade {g}", "n": len(d), **dict(zip(["mso", "lo", "hi"], mso.mso(d.p)))})
    save("essay_mso_by_group", pd.DataFrame(rows))
    # ELL effect adjusted for essay prompt (topic/task) and grade
    s["ell"] = (s.group == "ELL").astype(int)
    fit = smf.logit("in_region ~ ell + C(title) + C(grade)", data=s).fit(disp=0)
    ci = fit.conf_int().loc["ell"]
    save("essay_ell_adjusted", {"odds_ratio": float(np.exp(fit.params["ell"])),
                                "or_lo": float(np.exp(ci[0])), "or_hi": float(np.exp(ci[1])),
                                "p_value": float(fit.pvalues["ell"]), "n": int(fit.nobs)})
    # continuous margin (more power than the rare thresholded event). Calibrated probabilities pile up at
    # exactly 0, so use the uncalibrated logistic decision score instead; standardized to SD units of the
    # scored humans. Model: margin ~ ELL + prompt + grade, robust (HC3) errors.
    from sklearn.feature_extraction import DictVectorizer
    X, y, _, _ = mso.training_set(human, llm[llm.model.map(CHAT)])
    vec = DictVectorizer(sparse=False)
    Xv = np.nan_to_num(vec.fit_transform(X))
    kp = (Xv != 0).mean(0) >= 0.01
    lin = mso.make_pipeline(mso.StandardScaler(), mso.LogisticRegression(C=0.1, max_iter=3000)).fit(Xv[:, kp], y)
    s["lp"] = lin.decision_function(np.nan_to_num(vec.transform(list(s.f)))[:, kp])
    s["lp"] = (s.lp - s.lp.mean()) / s.lp.std()
    ols = smf.ols("lp ~ ell + C(title) + C(grade)", data=s).fit(cov_type="HC3")
    ci = ols.conf_int().loc["ell"]
    save("essay_ell_continuous", {"ell_coef_sd": float(ols.params["ell"]), "coef_lo": float(ci[0]),
                                  "coef_hi": float(ci[1]), "p_value": float(ols.pvalues["ell"]), "n": int(ols.nobs)})
    # seed stability: re-draw the balanced training sample 10 times
    rows, keep_seed = [], mso.SEED
    for seed in range(10):
        mso.SEED = seed
        X, y, _, _ = mso.training_set(human, llm[llm.model.map(CHAT)])
        ps = mso.fit(X, y)[0](list(s.f))
        d = s.assign(in_region=(ps >= 0.5).astype(int))
        f = smf.logit("in_region ~ ell + C(title) + C(grade)", data=d).fit(disp=0)
        rows.append({"seed": seed, "mso_all": d.in_region.mean(), "mso_ell": d[d.ell == 1].in_region.mean(),
                     "mso_nonell": d[d.ell == 0].in_region.mean(), "odds_ratio": float(np.exp(f.params["ell"])),
                     "p_value": float(f.pvalues["ell"])})
    mso.SEED = keep_seed
    seeds = pd.DataFrame(rows)
    save("essay_seed_stability", {"n_seeds": len(seeds), **{f"{c}_{st}": float(getattr(seeds[c], st)())
                                  for c in ("mso_all", "mso_ell", "mso_nonell", "odds_ratio") for st in ("min", "median", "max")},
                                  "share_seeds_p_below_05": float((seeds.p_value < 0.05).mean()),
                                  "share_seeds_ell_lower": float((seeds.mso_ell < seeds.mso_nonell).mean())})
    # robustness 1: does the ELL contrast survive other thresholds?
    save("essay_thresholds", pd.DataFrame([
        {"group": f"{g}@{t}", "n": len(d), "mso": float((d.p >= t).mean())}
        for t in (0.4, 0.5, 0.6) for g, d in [("all", s), *s.groupby("group")]]))
    # robustness 2: a different instrument (sentence embeddings). Essays share prompts across groups,
    # so topic cannot drive the ELL contrast here; for arXiv it could, so we use it for essays only.
    from sentence_transformers import SentenceTransformer
    from sklearn.model_selection import train_test_split
    enc = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")
    emb = lambda texts: enc.encode([features.clean(t) for t in texts], batch_size=64, show_progress_bar=False)
    L = llm[llm.model.map(CHAT)]
    H = human[human.pool == "train"].sample(n=len(L), random_state=mso.SEED)
    X = np.vstack([emb(H.text.tolist()), emb(L.text.tolist())])
    y = np.r_[np.zeros(len(H)), np.ones(len(L))]
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=mso.SEED, stratify=y)
    from sklearn.calibration import CalibratedClassifierCV
    from sklearn.linear_model import LogisticRegression
    clf = CalibratedClassifierCV(LogisticRegression(C=1.0, max_iter=3000), method="isotonic", cv=5).fit(Xtr, ytr)
    pe = clf.predict_proba(emb(s.text.tolist()))[:, 1]
    rows = [{"group": "all", "n": len(s), **dict(zip(["mso", "lo", "hi"], mso.mso(pe)))}]
    rows += [{"group": g, "n": int((s.group == g).sum()), **dict(zip(["mso", "lo", "hi"], mso.mso(pe[s.group == g])))}
             for g in ("ELL", "non-ELL")]
    save("essay_embedding_instrument", pd.DataFrame(rows))
    save("essay_embedding_auc", {"heldout_auc": roc_auc_score(yte, clf.predict_proba(Xte)[:, 1])})
    # secondary: Liang et al. 2023 human essays (TOEFL vs US college essays), out-of-domain
    lg = pd.read_json(Path(data) / "learner/liang_toefl_all_data.json")
    lg = lg[(lg.kind == "Human-Written") & lg.name.isin(["Real TOEFL", "Real College Essays"])]
    lg["p"] = score(features.extract(lg.text.tolist()))
    save("essay_liang", pd.DataFrame([{"group": g, "n": len(d), **dict(zip(["mso", "lo", "hi"], mso.mso(d.p)))}
                                      for g, d in lg.groupby("name")]))


T0 = pd.Period("2022-12", "M")      # first month after ChatGPT's release (2022-11-30)
EVAL = pd.Period("2025-06", "M")    # common evaluation month (Hansard ends 2025-07)


def monthly(s, by=None):
    keys = [s.date.dt.to_period("M")] + ([s[by]] if by else [])
    m = s.groupby(keys).agg(n=("p", "size"), mso=("in_region", "mean")).reset_index()
    return m.rename(columns={"date": "month"})


def segmented(m, t0=T0, until=None):
    """Interrupted time series on monthly MSO: level shift `post` + slope change `t_post` at t0.
    Weighted by n (MSO is a proportion); Newey-West (HAC, 6 lags) errors."""
    m = m[m.month <= until] if until is not None else m
    d = pd.DataFrame({"y": m.mso.values, "w": m.n.values,
                      "t": [(p - t0).n for p in m.month]})
    d["post"] = (d.t >= 0).astype(int)
    d["t_post"] = d.t * d.post
    fit = smf.wls("y ~ t + post + t_post", data=d, weights=d.w).fit(cov_type="HAC", cov_kwds={"maxlags": 6})
    h = (EVAL - t0).n
    ex = fit.t_test(f"post + {h} * t_post")
    lo, hi = np.asarray(ex.conf_int()).ravel()
    return {"pre_slope_per_year": 12 * fit.params["t"], "pre_slope_p": fit.pvalues["t"],
            "level_shift": fit.params["post"], "level_shift_p": fit.pvalues["post"],
            "slope_change_per_year": 12 * fit.params["t_post"], "slope_change_p": fit.pvalues["t_post"],
            f"excess_at_{EVAL}": float(np.asarray(ex.effect).ravel()[0]), "excess_lo": lo, "excess_hi": hi,
            "excess_se": float(np.asarray(ex.sd).ravel()[0]), "months": len(d)}


def placebo(m):
    """Fake break dates inside the pre-LLM period; should show no excess."""
    pre = m[m.month < T0]
    out = []
    for fake in ("2019-11", "2020-11"):
        f = pd.Period(fake, "M")
        d = pre.copy()
        d2 = pd.DataFrame({"y": d.mso.values, "w": d.n.values, "t": [(p - f).n for p in d.month]})
        d2["post"] = (d2.t >= 0).astype(int)
        d2["t_post"] = d2.t * d2.post
        fit = smf.wls("y ~ t + post + t_post", data=d2, weights=d2.w).fit(cov_type="HAC", cov_kwds={"maxlags": 6})
        out.append({"fake_break": fake, "level_shift": fit.params["post"], "level_shift_p": fit.pvalues["post"],
                    "slope_change_per_year": 12 * fit.params["t_post"], "slope_change_p": fit.pvalues["t_post"]})
    return out


def timeseries(data, genre, by_field=False):
    human, llm = mso.load(data, genre)
    score = region(human, llm, genre)
    s = human[human.pool == "score"].copy()
    s["p"] = score(list(s.f))
    s["in_region"] = (s.p >= 0.5).astype(int)
    m = monthly(s)
    save(f"{genre}_monthly", m)
    pre = s[s.date < "2022-11-30"]
    base = [{"group": "all", "n": len(pre), **dict(zip(["mso", "lo", "hi"], mso.mso(pre.p)))}]
    tests = {"all": {**segmented(m), "placebo": placebo(m)}}
    if by_field:
        mf = monthly(s, "group")
        save(f"{genre}_monthly_by_field", mf)
        for g, d in mf.groupby("group"):
            tests[g] = segmented(d)
        for g, d in pre.groupby("group"):
            base.append({"group": g, "n": len(d), **dict(zip(["mso", "lo", "hi"], mso.mso(d.p)))})
        # is the baseline structured (differs by field) rather than uniform noise?
        tab = pd.crosstab(pre.group, pre.in_region)
        from scipy.stats import chi2_contingency
        chi2, pv, dof, _ = chi2_contingency(tab)
        tests["baseline_field_heterogeneity"] = {"chi2": chi2, "dof": dof, "p": pv}
    # base (non-chat) RAID generators: does a region defined by chat models also capture them?
    base_llm = llm[~llm.model.map(CHAT)]
    if len(base_llm):
        pb = score(list(base_llm.f))
        rows = [{"group": m, "n": int((base_llm.model == m).sum()), "share_in_region": float((pb[base_llm.model.values == m] >= 0.5).mean())}
                for m in sorted(base_llm.model.unique())]
        chat = llm[llm.model.str.startswith("raid-") & llm.model.map(CHAT)]
        pc = score(list(chat.f))
        rows += [{"group": m, "n": int((chat.model == m).sum()), "share_in_region": float((pc[chat.model.values == m] >= 0.5).mean())}
                 for m in sorted(chat.model.unique())]
        save(f"{genre}_base_vs_chat", pd.DataFrame(rows))
    save(f"{genre}_baseline_pre2022", pd.DataFrame(base))
    save(f"{genre}_its", tests)
    return tests


def control():
    """H3: arXiv excess minus Hansard excess at the common evaluation month (independent samples)."""
    a = json.loads((OUT / "arxiv_its.json").read_text())["all"]
    h = json.loads((OUT / "hansard_its.json").read_text())["all"]
    k = f"excess_at_{EVAL}"
    diff = a[k] - h[k]
    se = (a["excess_se"] ** 2 + h["excess_se"] ** 2) ** 0.5
    from scipy.stats import norm
    save("control_difference", {"arxiv_excess": a[k], "hansard_excess": h[k], "difference": diff,
                                "lo": diff - 1.96 * se, "hi": diff + 1.96 * se, "p": 2 * norm.sf(abs(diff / se))})


if __name__ == "__main__":
    data, which = sys.argv[1], sys.argv[2]
    jobs = {"essay": lambda: essay(data), "arxiv": lambda: timeseries(data, "arxiv", by_field=True),
            "hansard": lambda: timeseries(data, "hansard"), "control": control}
    for j in (jobs if which == "all" else [which]):
        jobs[j]()
