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
    # secondary: Liang et al. 2023 human essays (TOEFL vs US college essays), out-of-domain
    lg = pd.read_json(Path(data) / "learner/liang_toefl_all_data.json")
    lg = lg[(lg.kind == "Human-Written") & lg.name.isin(["Real TOEFL", "Real College Essays"])]
    lg["p"] = score(features.extract(lg.text.tolist()))
    save("essay_liang", pd.DataFrame([{"group": g, "n": len(d), **dict(zip(["mso", "lo", "hi"], mso.mso(d.p)))}
                                      for g, d in lg.groupby("name")]))


if __name__ == "__main__":
    data, which = sys.argv[1], sys.argv[2]
    {"essay": essay}[which](data)
