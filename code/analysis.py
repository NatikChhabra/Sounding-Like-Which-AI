"""All tables and figures. Usage: python analysis.py DATA_DIR JOB   (JOB: see `jobs` at the bottom, or "all")

Writes results/<name>.csv|json. Every number in the paper comes from these files via make_numbers.py.
"""
import json, re, sys
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy.stats import chi2_contingency, norm, pointbiserialr, spearmanr
from sklearn.metrics import cohen_kappa_score, roc_auc_score

import features
import mso

OUT = Path(__file__).resolve().parent.parent / "results"
CHAT = lambda m: not str(m).startswith("raid-") or str(m).endswith(("-chat", "chatgpt", "gpt4"))
FRONTIER = "claude-opus-5.5"
T0 = pd.Period("2022-12", "M")      # first month after ChatGPT's release (2022-11-30)
EVAL = pd.Period("2025-06", "M")    # evaluation month, fixed in code before any time-series result (commit 50e2a17)
CUTOFF = pd.Timestamp("2022-11-30")
# Marker words, only from verified sources: Kobak et al. 2025, Gray 2024, Yakura et al. 2024.
MARK = r"\b(delv(e|es|ed|ing)|underscor(e|es|ed|ing)|showcas(e|es|ed|ing)|meticulous(ly)?|intricate|" \
       r"intricac(y|ies)|commendabl(e|y)|boast(s|ed|ing)?)\b"
LLM_TOPIC = r"\b(LLMs?|large language models?|language models?|GPT[-\d]*|ChatGPT|chatbots?|generative AI)\b"


def save(name, obj):
    OUT.mkdir(exist_ok=True)
    if isinstance(obj, pd.DataFrame):
        obj.to_csv(OUT / f"{name}.csv", index=False)
    else:
        (OUT / f"{name}.json").write_text(json.dumps(obj, indent=2, default=float))
    print(f"--- {name}\n{obj if isinstance(obj, pd.DataFrame) else json.dumps(obj, indent=1, default=float)}")


def ci_row(group, p, t=0.5):
    return {"group": group, "n": len(p), **dict(zip(["mso", "lo", "hi"], mso.mso(np.asarray(p) >= t)))}


# ----------------------------------------------------------------------------------------- instrument
def region(human, llm, name, lomo_runs=True):
    """Train the MSO instrument on chat-model text; return (logreg scorer, gbm scorer) + diagnostics."""
    llm = llm[llm.model.map(CHAT)]
    X, y, groups, L = mso.training_set(human, llm)
    auc, p_cv = mso.cv_auc(X, y, groups)
    n_h = int((y == 0).sum())
    per = []
    for (m, pk), idx in L.reset_index(drop=True).groupby(["model", "prompt"]).groups.items():
        yy = np.r_[np.zeros(n_h), np.ones(len(idx))]
        pp = np.r_[p_cv[:n_h], p_cv[n_h + np.asarray(idx)]]
        per.append({"model": m, "prompt": pk, "n": len(idx), "auc": roc_auc_score(yy, pp)})
    save(f"{name}_separability", pd.DataFrame(per))
    score, vec, keep, model = mso.fit(X, y, groups=groups)
    up, down = mso.top_features(vec, keep, model)
    save(f"{name}_features_llm_typical", up)
    save(f"{name}_features_human_typical", down)
    score_gb = mso.fit(X, y, kind="gbm", groups=groups)[0]
    scored = human[human.pool == "score"]
    pa, pb = score(list(scored.f)), score_gb(list(scored.f))
    a, b = pa >= 0.5, pb >= 0.5
    if lomo_runs:
        lomo = []
        for m in sorted(llm.model.unique()):
            Xm, ym, gm, _ = mso.training_set(human, llm, exclude_model=m)
            s_m = mso.fit(Xm, ym, groups=gm)[0]
            held = llm[llm.model == m]
            lomo.append({"held_out_model": m, "recall_on_unseen_model": float((s_m(list(held.f)) >= 0.5).mean()),
                         "mso_scored_humans": float((s_m(list(scored.f)) >= 0.5).mean())})
        save(f"{name}_lomo", pd.DataFrame(lomo))
    save(f"{name}_instrument", {
        "cv_auc_all": auc, "n_train_per_class": n_h, "n_generators": int(llm.model.nunique()),
        "mso_logreg": float(a.mean()), "mso_gbm": float(b.mean()),
        "kappa_logreg_vs_gbm": float(cohen_kappa_score(a, b)),
        "spearman_scores_logreg_vs_gbm": float(spearmanr(pa, pb).statistic),
        "share_flagged_by_both": float((a & b).mean())})
    return score, score_gb


# ----------------------------------------------------------------------------------------- essays
def essay(data):
    human, llm = mso.load(data, "essay")
    score, _ = region(human, llm, "essay")
    s = human[human.pool == "score"].copy()
    s["p"] = score(list(s.f))
    s["in_region"] = (s.p >= 0.5).astype(int)
    s["ell"] = (s.group == "ELL").astype(int)
    # grade bands: grade 12 alone is almost all ELL with zero events (quasi-separation)
    s["band"] = pd.cut(s.grade, [0, 8, 10, 12], labels=["6-8", "9-10", "11-12"]).astype(str)
    rows = [ci_row("all", s.p)] + [ci_row(g, d.p) for g, d in s.groupby("group")] + \
           [ci_row(f"grades {b}", d.p) for b, d in s.groupby("band")]
    save("essay_mso_by_group", pd.DataFrame(rows))
    save("essay_ell_counts", {"ell_in_region": int(s[s.ell == 1].in_region.sum()), "n_ell": int(s.ell.sum()),
                              "n_prompts": int(s.title.nunique())})
    form = "in_region ~ ell + C(title) + C(band)"
    fit = smf.logit(form, data=s).fit(disp=0)
    fit2 = smf.logit(form + " + C(score)", data=s).fit(disp=0)  # adjusted for holistic proficiency score
    out = {}
    for tag, f in (("", fit), ("_prof", fit2)):
        ci = f.conf_int().loc["ell"]
        out |= {f"odds_ratio{tag}": float(np.exp(f.params["ell"])), f"or_lo{tag}": float(np.exp(ci[0])),
                f"or_hi{tag}": float(np.exp(ci[1])), f"p_value{tag}": float(f.pvalues["ell"])}
    save("essay_ell_adjusted", out | {"n": int(fit.nobs)})
    # continuous margin: uncalibrated logistic decision score (calibrated p piles up at 0), SD units;
    # classical HC1 errors (HC3 with many fixed effects understated the SE in v1).
    from sklearn.feature_extraction import DictVectorizer
    X, y, _, _ = mso.training_set(human, llm[llm.model.map(CHAT)])
    vec = DictVectorizer(sparse=False)
    Xv = np.nan_to_num(vec.fit_transform(X))
    kp = mso._mask(vec, Xv)
    lin = mso.make_pipeline(mso.StandardScaler(), mso.LogisticRegression(C=0.1, max_iter=3000)).fit(Xv[:, kp], y)
    s["lp"] = lin.decision_function(np.nan_to_num(vec.transform(list(s.f)))[:, kp])
    s["lp"] = (s.lp - s.lp.mean()) / s.lp.std()
    out = {}
    for tag, f in (("", "lp ~ ell + C(title) + C(band)"), ("_prof", "lp ~ ell + C(title) + C(band) + C(score)")):
        o = smf.ols(f, data=s).fit(cov_type="HC1")
        ci = o.conf_int().loc["ell"]
        out |= {f"ell_coef_sd{tag}": float(o.params["ell"]), f"coef_lo{tag}": float(ci[0]),
                f"coef_hi{tag}": float(ci[1]), f"p_value{tag}": float(o.pvalues["ell"])}
    save("essay_ell_continuous", out)
    # seed stability of the thresholded contrast
    rows, keep_seed = [], mso.SEED
    for seed in range(10):
        mso.SEED = seed
        X, y, g, _ = mso.training_set(human, llm[llm.model.map(CHAT)])
        d = s.assign(in_region=(mso.fit(X, y, groups=g)[0](list(s.f)) >= 0.5).astype(int))
        f = smf.logit(form, data=d).fit(disp=0)
        rows.append({"mso_ell": d[d.ell == 1].in_region.mean(), "mso_nonell": d[d.ell == 0].in_region.mean(),
                     "odds_ratio": float(np.exp(f.params["ell"])), "p_value": float(f.pvalues["ell"])})
    mso.SEED = keep_seed
    seeds = pd.DataFrame(rows)
    save("essay_seed_stability", {"n_seeds": len(seeds), **{f"{c}_{st}": float(getattr(seeds[c], st)())
                                  for c in ("mso_ell", "mso_nonell", "odds_ratio") for st in ("min", "median", "max")},
                                  "share_seeds_p_below_05": float((seeds.p_value < 0.05).mean()),
                                  "share_seeds_ell_lower": float((seeds.mso_ell < seeds.mso_nonell).mean())})
    save("essay_thresholds", pd.DataFrame([{"group": f"{g}@{t}", "n": len(d), "mso": float((d.p >= t).mean())}
                                           for t in (0.4, 0.5, 0.6) for g, d in [("all", s), *s.groupby("group")]]))
    # second instrument: sentence embeddings (topic is held fixed by prompt within the ELL contrast)
    from sentence_transformers import SentenceTransformer
    from sklearn.calibration import CalibratedClassifierCV
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    enc = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")
    emb = lambda texts: enc.encode([features.clean(t) for t in texts], batch_size=64, show_progress_bar=False)
    L = llm[llm.model.map(CHAT)]
    H = human[human.pool == "train"].sample(n=min(len(L), (human.pool == "train").sum()), random_state=mso.SEED)
    X = np.vstack([emb(H.text.tolist()), emb(L.text.tolist())])
    y = np.r_[np.zeros(len(H)), np.ones(len(L))]
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=mso.SEED, stratify=y)
    clf = CalibratedClassifierCV(LogisticRegression(C=1.0, max_iter=3000), method="isotonic", cv=5).fit(Xtr, ytr)
    pe = clf.predict_proba(emb(s.text.tolist()))[:, 1]
    save("essay_embedding_instrument", pd.DataFrame([ci_row("all", pe)] +
                                                    [ci_row(g, pe[(s.group == g).values]) for g in ("ELL", "non-ELL")]))
    save("essay_embedding_auc", {"heldout_auc": roc_auc_score(yte, clf.predict_proba(Xte)[:, 1])})
    # Liang et al. 2023 human essays, out of genre (reported as such, not as a learner test)
    lg = liang_essays(data)
    pl = score(features.extract(lg.text.tolist()))
    save("essay_liang", pd.DataFrame([ci_row(g, pl[(lg.name == g).values]) for g in sorted(lg.name.unique())]))


def essay_perplexity(data):
    """Perplexity-detector instrument on the SAME essays (log-perplexity under a small LM, computed by
    perplexity.py), calibrated on the same human-vs-LLM training set: who does it flag?"""
    from sklearn.calibration import CalibratedClassifierCV
    from sklearn.linear_model import LogisticRegression
    human, llm = mso.load(data, "essay")
    import perplexity
    T = perplexity.TAG
    ppl = pd.read_json(Path(data) / f"ppl_essay{T}.jsonl", lines=True).set_index("id").logppl
    llm = llm[llm.model.map(CHAT)]
    _, _, _, L = mso.training_set(human, llm)
    H = human[human.pool == "train"].sample(n=len(L), random_state=mso.SEED)
    Xtr = np.r_[ppl.reindex(H.id).values, ppl.reindex(L.id).values].reshape(-1, 1)
    ytr = np.r_[np.zeros(len(H)), np.ones(len(L))]
    ok = ~np.isnan(Xtr.ravel())
    clf = CalibratedClassifierCV(LogisticRegression(), method="isotonic", cv=5).fit(Xtr[ok], ytr[ok])
    s = human[human.pool == "score"].copy()
    s["lp"] = ppl.reindex(s.id).values
    s = s.dropna(subset=["lp"])
    s["p"] = clf.predict_proba(s[["lp"]].values)[:, 1]
    s["flag"] = (s.p >= 0.5).astype(int)
    s["ell"] = (s.group == "ELL").astype(int)
    s["band"] = pd.cut(s.grade, [0, 8, 10, 12], labels=["6-8", "9-10", "11-12"]).astype(str)
    f = smf.logit("flag ~ ell + C(title) + C(band)", data=s).fit(disp=0)
    ci = f.conf_int().loc["ell"]
    save(f"essay_perplexity_instrument{T}", pd.DataFrame([ci_row(g, d.p) for g, d in [("all", s), *s.groupby("group")]]))
    save(f"essay_perplexity_adjusted{T}", {"odds_ratio": float(np.exp(f.params["ell"])), "or_lo": float(np.exp(ci[0])),
                                       "or_hi": float(np.exp(ci[1])), "p_value": float(f.pvalues["ell"]),
                                       "mean_logppl_ell": float(s[s.ell == 1].lp.mean()),
                                       "mean_logppl_nonell": float(s[s.ell == 0].lp.mean())})
    # Liang et al. (2023) original contrast, out of genre: TOEFL essays vs US 8th-grade essays
    lg = liang_essays(data)
    lp = np.array(perplexity.scorer()(lg.text.tolist()))
    pl = clf.predict_proba(lp.reshape(-1, 1))[:, 1]
    save(f"essay_liang_perplexity{T}", pd.DataFrame([{**ci_row(g, pl[(lg.name == g).values]),
                                                  "mean_logppl": float(np.nanmean(lp[(lg.name == g).values]))}
                                                 for g in sorted(lg.name.unique())]))


def liang_essays(data):
    """Human essays released by Liang et al. (2023): TOEFL and US college essays (HF copy) plus the US 8th-grade
    essays (authors' GitHub repository)."""
    lg = pd.read_json(Path(data) / "learner/liang_toefl_all_data.json")
    lg = lg[(lg.kind == "Human-Written") & lg.name.isin(["Real TOEFL", "Real College Essays"])][["name", "text"]]
    us8 = pd.DataFrame({"name": "Real US 8th grade",
                        "text": [r["document"] for r in json.loads((Path(data) / "learner/liang_us8th.json").read_text(encoding="utf-8"))]})
    return pd.concat([lg, us8], ignore_index=True)


# ----------------------------------------------------------------------------------------- time series
def monthly(s, col="in_region", by=None, w=None):
    keys = [s.date.dt.to_period("M")] + ([s[by]] if by else [])
    s = s.assign(_w=1.0 if w is None else s[w])
    g = s.groupby(keys)
    m = g.apply(lambda d: pd.Series({"n": len(d), "mso": np.average(d[col], weights=d._w)}), include_groups=False)
    return m.reset_index().rename(columns={"date": "month"})


def segmented(m, t0=T0, eval_at=EVAL, until=None):
    """Interrupted time series on a monthly share: level shift `post` + slope change `t_post` at t0.
    Weighted by n; Newey-West (HAC, 6 lags) errors. Excess = fitted post-t0 minus extrapolated trend at eval_at."""
    m = m[m.month <= until] if until is not None else m
    d = pd.DataFrame({"y": m.mso.values, "w": m.n.values, "t": [(p - t0).n for p in m.month]})
    d["post"] = (d.t >= 0).astype(int)
    d["t_post"] = d.t * d.post
    fit = smf.wls("y ~ t + post + t_post", data=d, weights=d.w).fit(cov_type="HAC", cov_kwds={"maxlags": 6})
    ex = fit.t_test(f"post + {(eval_at - t0).n} * t_post")
    lo, hi = np.asarray(ex.conf_int()).ravel()
    return {"pre_slope_per_year": 12 * fit.params["t"], "pre_slope_p": fit.pvalues["t"],
            "level_shift": fit.params["post"], "level_shift_p": fit.pvalues["post"],
            "slope_change_per_year": 12 * fit.params["t_post"], "slope_change_p": fit.pvalues["t_post"],
            "excess": float(np.asarray(ex.effect).ravel()[0]), "excess_lo": lo, "excess_hi": hi,
            "excess_se": float(np.asarray(ex.sd).ravel()[0]), "excess_p": float(np.asarray(ex.pvalue).ravel()[0]),
            "months": len(d)}


def placebo(m):
    """Fake break dates inside the pre-LLM period (same frozen instrument)."""
    pre = m[m.month < T0]
    out = []
    for fake in ("2019-11", "2020-11"):
        r = segmented(pre, t0=pd.Period(fake, "M"), eval_at=pd.Period("2022-06", "M"))
        out.append({"fake_break": fake, "level_shift": r["level_shift"], "level_shift_p": r["level_shift_p"],
                    "slope_change_per_year": r["slope_change_per_year"], "slope_change_p": r["slope_change_p"],
                    "excess": r["excess"], "excess_p": r["excess_p"]})
    return out


def yearly(s, cols):
    yr = s.groupby(s.date.dt.year)[cols].mean().reset_index()
    yr["n"] = s.groupby(s.date.dt.year).size().values
    return yr.rename(columns={"date": "group"}).assign(group=lambda d: d.group.astype(str))


def timeseries(data, genre, by_field=False, tag="", drop_models=(), lomo_runs=True):
    human, llm = mso.load(data, genre)
    llm = llm[~llm.model.isin(drop_models)]
    name = genre + tag
    score, score_gb = region(human, llm, name, lomo_runs)
    s = human[human.pool == "score"].copy()
    s["p"] = score(list(s.f))
    s["in_region"] = (s.p >= 0.5).astype(int)
    s["marker"] = s.text.str.contains(MARK, case=False, regex=True).astype(int)
    m = monthly(s)
    save(f"{name}_monthly", m)
    pre = s[s.date < CUTOFF]
    base = [ci_row("all", pre.p)]
    tests = {"all": {**segmented(m), "placebo": placebo(m)}}
    s["in_04"], s["in_06"] = (s.p >= 0.4).astype(int), (s.p >= 0.6).astype(int)
    for t in ("04", "06"):
        tests[f"threshold_{t}"] = segmented(monthly(s, f"in_{t}"))
    save(f"{name}_yearly", yearly(s, ["in_region", "in_04", "in_06", "marker"]).rename(columns={"in_region": "mso"}))
    if by_field:
        mf = monthly(s, by="group")
        save(f"{name}_monthly_by_field", mf)
        for g, d in mf.groupby("group"):
            tests[g] = segmented(d)
        pre = pre.assign(p_gb=score_gb(list(pre.f)))
        base += [{**ci_row(g, d.p), "mso_gbm": float((d.p_gb >= 0.5).mean())} for g, d in pre.groupby("group")]
        chi2, pv, dof, _ = chi2_contingency(pd.crosstab(pre.group, pre.in_region))
        tests["baseline_field_heterogeneity"] = {"chi2": chi2, "dof": dof, "p": pv}
        # confound checks (reviewers): math notation, length, LLM-related topics
        s["has_math"] = s.text.str.contains(r"\$", regex=True)
        s["n_words"] = s.text.str.split().str.len()
        s["llm_topic"] = s.text.str.contains(LLM_TOPIC, case=False, regex=True)
        nm = s[~s.has_math]
        tests["no_math"] = segmented(monthly(nm))
        base += [{**ci_row(f"nomath {g}", d.p)} for g, d in nm[nm.date < CUTOFF].groupby("group")]
        tests["no_llm_topic"] = segmented(monthly(s[~s.llm_topic]))
        bins = pd.qcut(pre.text.str.split().str.len(), 5, retbins=True)[1]
        bins[0], bins[-1] = -np.inf, np.inf
        s["lbin"] = pd.cut(s.n_words, bins, labels=False)
        target = s[s.date < CUTOFF].lbin.value_counts(normalize=True)
        cur = s.groupby([s.date.dt.to_period("M"), "lbin"]).size() / s.groupby(s.date.dt.to_period("M")).size()
        s["lw"] = [target[b] / cur[(d, b)] for d, b in zip(s.date.dt.to_period("M"), s.lbin)]
        tests["length_adjusted"] = segmented(monthly(s, w="lw"))
        save(f"{name}_length_by_year", s.groupby(s.date.dt.year).n_words.median().reset_index()
             .rename(columns={"date": "group", "n_words": "median_words"}).assign(group=lambda d: d.group.astype(str)))
    dispersion(s, name)
    save(f"{name}_marker_monthly", monthly(s, "marker"))
    tests["marker"] = segmented(monthly(s, "marker"))
    save(f"{name}_marker_vs_mso", {"corr_marker_inregion": float(pointbiserialr(s.marker, s.in_region).statistic),
                                   "share_inregion_with_marker": float(s[s.in_region == 1].marker.mean()),
                                   "share_outregion_with_marker": float(s[s.in_region == 0].marker.mean())})
    base_llm = llm[~llm.model.map(CHAT)]
    if len(base_llm):  # base (non-chat) generators vs a chat-defined region (chat shares are in-sample)
        pb = score(list(base_llm.f))
        save(f"{name}_base_models", pd.DataFrame([{"group": mm, "n": int((base_llm.model == mm).sum()),
                                                    "share_in_region": float((pb[(base_llm.model == mm).values] >= 0.5).mean())}
                                                   for mm in sorted(base_llm.model.unique())]))
    save(f"{name}_baseline_pre2022", pd.DataFrame(base))
    save(f"{name}_its", tests)
    return tests


def dispersion(s, name, per_year=1500, n_boot=300):
    """Homogenization check: per-year stylistic dispersion of human documents = mean Euclidean distance to
    the year's centroid in the feature space standardized on pre-ChatGPT documents (same per-year n)."""
    from sklearn.feature_extraction import DictVectorizer
    smp = s.groupby(s.date.dt.year, group_keys=False).apply(
        lambda d: d.sample(n=min(per_year, len(d)), random_state=mso.SEED))
    vec = DictVectorizer(sparse=False)
    X = np.nan_to_num(vec.fit_transform(list(smp.f)))
    X = X[:, (X != 0).mean(0) >= 0.01]
    pre = (smp.date < CUTOFF).values
    mu, sd = X[pre].mean(0), X[pre].std(0) + 1e-9
    Z = (X - mu) / sd
    years = smp.date.dt.year.values
    ys = sorted(set(years))
    disp = lambda z: float(np.linalg.norm(z - z.mean(0), axis=1).mean())
    rng = np.random.default_rng(mso.SEED)
    boot = np.array([[disp(Z[years == y][rng.integers(0, (years == y).sum(), (years == y).sum())]) for y in ys]
                     for _ in range(n_boot)])
    pre_y = [y for y in ys if y <= 2022]

    def gap(v, at):  # observed minus linear 2015-2022 trend, extrapolated to year `at`
        b = np.polyfit(pre_y, v[:len(pre_y)], 1)
        return v[ys.index(at)] - np.polyval(b, at)
    point = np.array([disp(Z[years == y]) for y in ys])
    rows = [{"group": str(y), "n": int((years == y).sum()), "dispersion": point[i],
             "lo": float(np.percentile(boot[:, i], 2.5)), "hi": float(np.percentile(boot[:, i], 97.5))}
            for i, y in enumerate(ys)]
    save(f"{name}_dispersion", pd.DataFrame(rows))
    g = {}
    for at in (2025, 2026):
        bg = [gap(b, at) for b in boot]
        g[f"gap_{at}"] = {"est": gap(point, at), "ci_lo": float(np.percentile(bg, 2.5)),
                          "ci_hi": float(np.percentile(bg, 97.5)), "trend_per_year": float(np.polyfit(pre_y, point[:len(pre_y)], 1)[0])}
    save(f"{name}_dispersion_trend", g)


GENSETS = {  # which generators define the LLM region
    "all": lambda m: True,
    "no_frontier": lambda m: m != FRONTIER,
    "local": lambda m: not m.startswith("raid-") and m != FRONTIER,
    "local_frontier": lambda m: not m.startswith("raid-"),
    "raid": lambda m: m.startswith("raid-"),
}


def gensets(data, genre="arxiv"):
    """Sensitivity of the series to the generator set defining the region (no LOMO)."""
    human, llm = mso.load(data, genre)
    rows, out = [], {}
    for k, keep in GENSETS.items():
        sub = llm[llm.model.map(keep)]
        if sub.empty:
            continue
        score, _ = region(human, sub, f"{genre}_gs_{k}", lomo_runs=False)
        s = human[human.pool == "score"].copy()
        s["in_region"] = (score(list(s.f)) >= 0.5).astype(int)
        r = segmented(monthly(s))
        out[k] = r
        yr = s.groupby(s.date.dt.year).in_region.mean()
        rows.append({"group": k, "n_generators": int(sub[sub.model.map(CHAT)].model.nunique()),
                     **{f"y{y}": float(v) for y, v in yr.items()}, "excess": r["excess"],
                     "excess_lo": r["excess_lo"], "excess_hi": r["excess_hi"]})
    save(f"{genre}_gensets", pd.DataFrame(rows))
    save(f"{genre}_gensets_its", out)


def drift_placebo(data, genre="arxiv"):
    """Out-of-sample placebo for instrument drift: train the region on 2015-2018 humans only, then test for
    an 'excess' at mid-2022 over the 2015-2018 trend, i.e. before any LLM writing assistance."""
    human, llm = mso.load(data, genre)
    h = human.copy()
    h.loc[(h.pool == "train") & (h.date >= "2019-01-01"), "pool"] = "unused"
    score, _ = region(h, llm, f"{genre}_drift", lomo_runs=False)
    s = h[(h.pool == "score") & (h.date < CUTOFF)].copy()
    s["in_region"] = (score(list(s.f)) >= 0.5).astype(int)
    save(f"{genre}_drift_placebo", segmented(monthly(s), t0=pd.Period("2019-01", "M"), eval_at=pd.Period("2022-06", "M")))


# ----------------------------------------------------------------------------------------- v3: generator vintage
# Pretraining data predate ChatGPT's release, per primary sources: GPT-4 (gpt-4-0613; GPT-4 report: Sep 2021) and
# RAID's Llama-2-70b-chat (Llama 2 model card: Sep 2022). ChatGPT (gpt-3.5-turbo-0613) only as a sensitivity set,
# since its cutoff is documented only by secondary sources.
PRE2022_DATA = ("raid-gpt4", "raid-llama-chat")
# Open models whose pretraining data predate ChatGPT, run locally on the same prompts (added after review round 2;
# kept out of every other analysis): Llama 2 chat (pretraining cutoff Sep 2022) and Vicuna (Llama + ShareGPT).
OLD = ("llama2:7b", "vicuna:7b")
NEW = ("gemma4:12b", "qwen3.5:9b", "granite4.2:8b")  # 2026 open models with logged decoding (vintage analysis only)
# RAID chat outputs often summarise the paper instead of writing its abstract ("In the paper titled ...")
SUMMARY = re.compile(r"\btitled\b|\bthe authors\b|^\s*(in )?the (paper|article|study)\b", re.I)


def load_old(data, llm):
    """Append the vintage-only open models (OLD and NEW; separate file, separate feature cache)."""
    f = Path(data) / "llm_arxiv_old.jsonl"
    if not f.exists():
        return llm
    o = pd.read_json(f, lines=True)
    o["id"] = o.src_id + "|" + o.model + "|" + o.prompt
    o["id"] = o.id + "|" + o.groupby("id").cumcount().astype(str)
    mso.cached_features(o, Path(data) / "feat_llm_arxiv_old.jsonl")
    return pd.concat([llm, o], ignore_index=True)
WORD = re.compile(r"[a-z]+")


PROMPT_WORDS = {"title", "titled", "abstract", "paper", "academic", "authors"}  # echo the prompt, not style


def mined_markers(llm_texts, human_texts, k=20, min_df=0.05):
    """Words most over-represented in LLM output vs the human abstracts its prompts were built from (smoothed
    log-odds of document frequency). Topic-matched, so the lexical comparison uses markers of the SAME generators
    that define the style region rather than topic words of the prompt set."""
    def df(texts):
        c = pd.Series([w for t in texts for w in set(WORD.findall(t.lower()))]).value_counts()
        return c / len(texts)
    a, b = df(llm_texts), df(human_texts)
    words = a[(a >= min_df) & ~a.index.isin(PROMPT_WORDS)].index
    lo = np.log((a[words] + 1e-3) / (b.reindex(words).fillna(0) + 1e-3))
    return list(lo.sort_values(ascending=False).index[:k])


def source_texts(data, human):
    """id -> human source text for every generation: our arXiv sample plus RAID's own human abstracts."""
    pool = dict(zip(human.id, human.text))
    raid = Path(data) / "raid_arxiv_human.jsonl"
    if raid.exists():
        r = pd.read_json(raid, lines=True)
        pool |= dict(zip(r.src_id, r.text)) | dict(zip(r.id, r.text))
    return pool


def marker_series(sub, s0, pool):
    """Monthly share of scored abstracts using >=1 of the set's topic-matched mined markers."""
    src = [pool[i] for i in sub.src_id.unique() if i in pool]
    assert len(src) >= 0.9 * sub.src_id.nunique(), f"only {len(src)} of {sub.src_id.nunique()} sources found"
    words = mined_markers(sub.text.tolist(), src)
    pat = re.compile(r"\b(" + "|".join(map(re.escape, words)) + r")\b", re.I)
    mk = s0.text.map(lambda t: bool(pat.search(t))).astype(int)
    return words, len(src), mk


def nonparam_gap(m, start="2025-01", end="2025-06"):
    """Mean observed monthly value in [start, end] minus the extrapolated linear pre-ChatGPT trend (WLS)."""
    pre = m[m.month < T0]
    t = np.array([(p - T0).n for p in pre.month])
    b = np.polyfit(t, pre.mso, 1, w=np.sqrt(pre.n))
    win = m[(m.month >= pd.Period(start, "M")) & (m.month <= pd.Period(end, "M"))]
    tw = np.array([(p - T0).n for p in win.month])
    return float((win.mso - np.polyval(b, tw)).mean())


def vintage_sets(llm):
    chat = llm[llm.model.map(CHAT)]
    p1 = chat[(chat.prompt == "P1") | chat.model.str.startswith("raid-")]
    sets = {f"single:{g}": p1[p1.model == g] for g in sorted(p1.model.unique())}
    old, raid_pre = chat[chat.model.isin(OLD)], chat[chat.model.isin(PRE2022_DATA)]
    new = chat[~chat.model.isin(OLD + NEW)]  # every set below except the vintage-only ones is as before
    raid_pre_c = chat[chat.model.isin(PRE2022_DATA + ("raid-chatgpt",))]
    sets |= {"pre2022data": raid_pre, "pre2022data_plus_chatgpt": raid_pre_c,
             "pre2022data_abstract_register": raid_pre[~raid_pre.text.str.contains(SUMMARY)],
             "raid_all": new[new.model.str.startswith("raid-")],
             "local_p1": p1[~p1.model.str.startswith("raid-") & (p1.model != FRONTIER) & ~p1.model.isin(OLD + NEW)],
             "frontier_p1": p1[p1.model == FRONTIER],
             "all_no_revision": new[new.prompt != "P2"],
             "all": new}
    if chat.model.isin(NEW).any():
        sets |= {"open2026_p1": p1[p1.model.isin(NEW)], "all2026_p1": p1[p1.model.isin(NEW + (FRONTIER,))]}
    if len(old):
        sets |= {"old_open_p1": old[old.prompt == "P1"], "old_open_all": old,
                 "pre2022data_matched": pd.concat([old[old.prompt == "P1"], raid_pre[~raid_pre.text.str.contains(SUMMARY)]])}
    return sets


def vintage(data, markers_only=False):
    """Per-generator-vintage regions on a matched task: each local/2026 generator on title-only prompts (P1), RAID
    generators (title-based) as they are, plus a region from generators whose training data predate ChatGPT.
    markers_only: recompute the marker columns and keep the (expensive) style regions from the last full run."""
    human, llm = mso.load(data, "arxiv")
    llm = load_old(data, llm)
    pool = source_texts(data, human)
    s0 = human[human.pool == "score"].copy()
    old = pd.read_csv(OUT / "arxiv_vintage.csv").set_index("group") if markers_only else None
    old_its = json.loads((OUT / "arxiv_vintage_its.json").read_text()) if markers_only else {}
    rows, its = [], {}
    for name, sub in vintage_sets(llm).items():
        s = s0.copy()
        words, n_src, s["mk"] = marker_series(sub, s0, pool)
        mm = monthly(s, "mk")
        rm = segmented(mm)
        if markers_only:
            row = old.loc[name].to_dict() | {"group": name}
            r = old_its[name]["style"]  # ponytail: markers_only needs every set in the last full run
        else:
            score, _ = region(human, sub, f"arxiv_v_{name.replace(':', '_')}", lomo_runs=False)
            s["in_region"] = (score(list(s.f)) >= 0.5).astype(int)
            m = monthly(s)
            r = segmented(m)
            yr = s.groupby(s.date.dt.year).in_region.mean()
            row = {"group": name, "n_llm": len(sub), "gap": r["excess"], "gap_lo": r["excess_lo"],
                   "gap_hi": r["excess_hi"], "gap_nonparam": nonparam_gap(m),
                   **{f"y{y}": float(v) for y, v in yr.items()}}
        yr_m = s.groupby(s.date.dt.year).mk.mean()
        row |= {"marker_gap": rm["excess"], "marker_gap_lo": rm["excess_lo"], "marker_gap_hi": rm["excess_hi"],
                "marker_n_sources": n_src, "summary_register_share": float(sub.text.str.contains(SUMMARY).mean()),
                **{f"m{y}": float(v) for y, v in yr_m.items()}}
        rows.append(row)
        its[name] = {"style": r, "markers": rm, "marker_words": words}
    save("arxiv_vintage", pd.DataFrame(rows))
    save("arxiv_vintage_its", its)


def placebo_grid(m, start="2016-06", end="2021-12", eval_months=12):
    """Every 2 months: fake break; share of fake breaks whose 'gap' (eval_months later) has p < 0.05."""
    pre = m[m.month < T0]
    out = []
    for f in pd.period_range(start, end, freq="M")[::2]:
        r = segmented(pre, t0=f, eval_at=min(f + eval_months, T0 - 1))
        out.append({"break": str(f), "gap": r["excess"], "p": r["excess_p"]})
    g = pd.DataFrame(out)
    return {"n_breaks": len(g), "share_p_below_05": float((g.p < 0.05).mean()),
            "median_abs_gap": float(g.gap.abs().median()), "max_abs_gap": float(g.gap.abs().max())}


def robustness_v3(data):
    """Placebo grids for both genres, event study, field tests (Holm; cs vs math), length-standardised field
    baselines, length-fixed dispersion, revision overlap with sources."""
    from statsmodels.stats.multitest import multipletests
    out = {}
    for genre in ("arxiv", "hansard"):
        m = pd.read_csv(OUT / f"{genre}_monthly.csv")
        m["month"] = pd.PeriodIndex(m.month, freq="M")
        out[f"{genre}_placebo_grid"] = placebo_grid(m)
        pre = m[m.month < T0]
        t = np.array([(p - T0).n for p in pre.month])
        b = np.polyfit(t, pre.mso, 1, w=np.sqrt(pre.n))
        m["resid"] = m.mso - np.polyval(b, [(p - T0).n for p in m.month])
        ev = m.groupby(m.month.dt.year).apply(lambda d: pd.Series({
            "resid": np.average(d.resid, weights=d.n), "n": d.n.sum()}), include_groups=False).reset_index()
        save(f"{genre}_event", ev.rename(columns={"month": "group"}).assign(group=lambda d: d.group.astype(str)))
    its = json.loads((OUT / "arxiv_its.json").read_text())
    fields = ["astro-ph", "cond-mat", "cs", "econ", "eess", "math", "q-bio", "stat"]
    p = [its[f]["excess_p"] for f in fields]
    out["field_holm"] = dict(zip(fields, multipletests(p, method="holm")[1].tolist()))
    a, b = its["cs"], its["math"]
    d = a["excess"] - b["excess"]
    se = (a["excess_se"] ** 2 + b["excess_se"] ** 2) ** 0.5
    out["cs_minus_math"] = {"diff": d, "lo": d - 1.96 * se, "hi": d + 1.96 * se, "p": float(2 * norm.sf(abs(d / se)))}
    save("robustness_v3", out)
    # length-standardised pre-ChatGPT baselines by field (reweight to the overall pre-period length distribution)
    human, llm = mso.load(data, "arxiv")
    score, _ = region(human, llm[llm.model.map(CHAT)], "arxiv_lenstd", lomo_runs=False)
    pre = human[(human.pool == "score") & (human.date < CUTOFF)].copy()
    pre["in_region"] = (score(list(pre.f)) >= 0.5).astype(int)
    pre["lbin"] = pd.qcut(pre.text.str.split().str.len(), 5, labels=False, duplicates="drop")
    target = pre.lbin.value_counts(normalize=True)
    rows = []
    for g, d in pre.groupby("group"):
        w = d.lbin.map(target / d.lbin.value_counts(normalize=True))
        rows.append({"group": g, "mso_lenstd": float(np.average(d.in_region, weights=w)),
                     "median_words": float(d.text.str.split().str.len().median())})
    save("arxiv_baseline_lenstd", pd.DataFrame(rows))
    # dispersion with length fixed: abstracts of >= 150 words, features recomputed on the first 150 words
    s = human[(human.pool == "score")].copy()
    s = s[s.text.str.split().str.len() >= 150]
    smp = s.groupby(s.date.dt.year, group_keys=False).apply(lambda d: d.sample(n=min(1200, len(d)), random_state=mso.SEED))
    smp = smp.assign(f=features.extract([" ".join(t.split()[:150]) for t in smp.text]))
    dispersion(smp, "arxiv_len150")


def _pre_fit(m, start=None, end=None, deg=1):
    pre = m[m.month < T0]
    pre = pre[(pre.month >= pd.Period(start, "M")) if start else slice(None)]
    pre = pre[(pre.month <= pd.Period(end, "M")) if end else slice(None)]
    t = np.array([(p - T0).n for p in pre.month])
    return np.polyfit(t, pre.mso, deg, w=np.sqrt(pre.n))


def gap_vs(m, b, start="2025-01", end="2025-06"):
    """Mean observed share in [start, end] minus the extrapolated pre-ChatGPT trend b (nonparametric gap)."""
    win = m[(m.month >= pd.Period(start, "M")) & (m.month <= pd.Period(end, "M"))]
    return float((win.mso - np.polyval(b, [(p - T0).n for p in win.month])).mean())


def block_bootstrap(m, n_boot=2000, block=12, seed=0):
    """Moving-block residual bootstrap of the ITS trend gap (keeps within-year autocorrelation)."""
    rng = np.random.default_rng(seed)
    t = np.array([(p - T0).n for p in m.month])
    X = np.c_[np.ones_like(t), t, t >= 0, t * (t >= 0)].astype(float)
    w = np.sqrt(m.n.values)
    beta, *_ = np.linalg.lstsq(X * w[:, None], m.mso.values * w, rcond=None)
    fitted, res = X @ beta, m.mso.values - X @ beta
    e = (EVAL - T0).n
    out = []
    for _ in range(n_boot):
        starts = rng.integers(0, len(res) - block + 1, size=len(res) // block + 1)
        r = np.concatenate([res[s:s + block] for s in starts])[:len(res)]
        b, *_ = np.linalg.lstsq(X * w[:, None], (fitted + r) * w, rcond=None)
        out.append(b[2] + e * b[3])
    return {"excess": float(beta[2] + e * beta[3]), "lo": float(np.percentile(out, 2.5)),
            "hi": float(np.percentile(out, 97.5))}


def robustness_v4(data):
    """Pre-trend shape/window sensitivity, block bootstrap, drift placebos at several origins, relative/logit
    scale for arXiv vs Hansard, implied LLM-prevalence (mixture identity), revision-exclusion rates."""
    out = {}
    for genre in ("arxiv", "hansard"):
        m = pd.read_csv(OUT / f"{genre}_monthly.csv")
        m["month"] = pd.PeriodIndex(m.month, freq="M")
        lin = _pre_fit(m)
        trend = float(np.polyval(lin, (EVAL - T0).n))
        its = json.loads((OUT / f"{genre}_its.json").read_text())["all"]
        lg = lambda q: np.log(q / (1 - q))
        out[f"{genre}_pretrend"] = {
            "linear_2015": gap_vs(m, lin), "quadratic_2015": gap_vs(m, _pre_fit(m, deg=2)),
            "linear_2017": gap_vs(m, _pre_fit(m, start="2017-01")),
            "linear_2019": gap_vs(m, _pre_fit(m, start="2019-01")),
            "linear_to_2020": gap_vs(m, _pre_fit(m, end="2020-12")),  # pre-period without 2021-22 (N9)
            "trend_at_eval": trend, "relative_gap": its["excess"] / trend,
            "logit_gap": float(lg(trend + its["excess"]) - lg(trend))}
        out[f"{genre}_block_bootstrap"] = block_bootstrap(m)
    # drift placebos: instrument trained on human abstracts up to year Y only, fake break the following January
    human, llm = mso.load(data, "arxiv")
    for y in (2016, 2017):
        h = human.copy()
        h.loc[(h.pool == "train") & (h.date >= f"{y + 1}-01-01"), "pool"] = "unused"
        score, _ = region(h, llm, f"arxiv_drift{y}", lomo_runs=False)
        sc = h[(h.pool == "score") & (h.date < CUTOFF)].copy()
        sc["in_region"] = (score(list(sc.f)) >= 0.5).astype(int)
        out[f"drift_to_{y}"] = segmented(monthly(sc), t0=pd.Period(f"{y + 1}-01", "M"), eval_at=pd.Period("2022-06", "M"))
    # implied prevalence: MSO_t = FPR + alpha (TPR - FPR)  =>  alpha = (MSO_t - FPR) / (TPR - FPR)
    X, yv, groups, _ = mso.training_set(human, llm[llm.model.map(CHAT)])
    _, p_cv = mso.cv_auc(X, yv, groups)
    tpr_cv = float((p_cv[yv == 1] >= 0.5).mean())
    tpr_lomo = float(pd.read_csv(OUT / "arxiv_lomo.csv").recall_on_unseen_model.mean())
    base = pd.read_csv(OUT / "arxiv_baseline_pre2022.csv").set_index("group").mso
    f = pd.read_csv(OUT / "arxiv_monthly_by_field.csv")
    f["year"] = f.month.str[:4].astype(int)
    f = f.assign(k=f.mso * f.n).groupby(["group", "year"])[["k", "n"]].sum()
    out["implied"] = {"tpr_cv": tpr_cv, "fpr_cv": float((p_cv[yv == 0] >= 0.5).mean()), "tpr_lomo_mean": tpr_lomo}
    for g in ("cs", "math", "stat", "econ"):
        for y in (2023, 2024, 2025, 2026):
            q = f.loc[(g, y)]
            q = q.k / q.n
            out["implied"][f"{g}_{y}_alpha_cv"] = (q - base[g]) / (tpr_cv - base[g])
            out["implied"][f"{g}_{y}_alpha_lomo"] = (q - base[g]) / (tpr_lomo - base[g])
    # N9: share of sampled pre-ChatGPT papers excluded because their latest version postdates ChatGPT
    a = pd.read_json(Path(data) / "arxiv_v2" / "sample.jsonl", lines=True)
    pub = pd.to_datetime(a.published).dt.tz_localize(None)
    upd = pd.to_datetime(a.updated).dt.tz_localize(None)
    pre = pub < CUTOFF
    ex = (upd[pre] >= CUTOFF).groupby(pub[pre].dt.year).mean()
    out["revision_exclusion_share"] = {f"y{k}": float(v) for k, v in ex.items()}
    save("robustness_v4", out)


def revision_overlap(data):
    """Share of each generator's revision (P2) outputs that keep >30% of the source's word 6-grams."""
    rows = []
    for genre in ("arxiv", "hansard", "essay"):
        human = pd.read_parquet(Path(data) / f"human_{genre}.parquet").set_index("id").text
        llm = pd.read_json(Path(data) / f"llm_{genre}.jsonl", lines=True)
        if genre == "arxiv":
            llm["src_id"] = llm.src_id.str.replace(r"v\d+$", "", regex=True)
        p2 = llm[(llm.prompt == "P2") & llm.src_id.isin(human.index)]
        grams = lambda t: {tuple(w[i:i + 6]) for w in [t.lower().split()] for i in range(len(w) - 5)}
        for g, d in p2.groupby("model"):
            keep = [len(grams(o) & grams(human[s])) / max(1, len(grams(human[s]))) for o, s in zip(d.text, d.src_id)]
            rows.append({"group": f"{genre}:{g}", "n": len(d), "share_over_30pct": float(np.mean(np.array(keep) > 0.3)),
                         "median_retained": float(np.median(keep))})
    save("revision_overlap", pd.DataFrame(rows))


def nodash(data):
    """Ablation: drop every dash feature so punctuation typography cannot drive MSO."""
    mso.EXCLUDE = ("pun:â€”", "pun:â€“", "pun:-")
    try:
        timeseries(data, "arxiv", True, "_nodash", (), False)
    finally:
        mso.EXCLUDE = ()


def control():
    """arXiv vs parliamentary speech, each with the region defined by the SAME generator set (local + frontier),
    excess at the common evaluation month; independent-samples z test."""
    a = json.loads((OUT / "arxiv_gensets_its.json").read_text())["local_frontier"]
    h = json.loads((OUT / "hansard_its.json").read_text())["all"]
    diff = a["excess"] - h["excess"]
    se = (a["excess_se"] ** 2 + h["excess_se"] ** 2) ** 0.5
    save("control_difference", {"arxiv_excess": a["excess"], "hansard_excess": h["excess"], "difference": diff,
                                "lo": diff - 1.96 * se, "hi": diff + 1.96 * se, "p": 2 * norm.sf(abs(diff / se))})


def corpus_stats(data):
    d = Path(data)
    st = {}
    for g in ("arxiv", "hansard", "essay"):
        h = pd.read_parquet(d / f"human_{g}.parquet")
        l = pd.read_json(d / f"llm_{g}.jsonl", lines=True)
        st |= {f"{g}_n_docs": len(h), f"{g}_n_train": int((h.pool == "train").sum()),
               f"{g}_n_score": int((h.pool == "score").sum()), f"{g}_n_llm_local": len(l),
               f"{g}_n_generators_local": int(l.model.nunique())}
    st["arxiv_n_fields"] = int(pd.read_parquet(d / "human_arxiv.parquet").group.nunique())
    save("corpus_stats", st)


if __name__ == "__main__":
    data, which = sys.argv[1], sys.argv[2]
    jobs = {"corpus": lambda: corpus_stats(data), "essay": lambda: essay(data),
            "essay_perplexity": lambda: essay_perplexity(data),
            "arxiv": lambda: timeseries(data, "arxiv", by_field=True), "hansard": lambda: timeseries(data, "hansard"),
            "gensets": lambda: gensets(data), "drift": lambda: drift_placebo(data), "nodash": lambda: nodash(data),
            "vintage": lambda: vintage(data), "vmarkers": lambda: vintage(data, markers_only=True), "robust4": lambda: robustness_v4(data), "robust3": lambda: robustness_v3(data),
            "overlap": lambda: revision_overlap(data),
            "control": control}
    for j in (jobs if which == "all" else [which]):
        jobs[j]()
