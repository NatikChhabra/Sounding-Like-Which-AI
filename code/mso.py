"""Machine-Style Overlap (MSO) estimation.

MSO = share of human documents whose calibrated P(LLM | style) >= 0.5 under a classifier trained on a
BALANCED set of pre-2022 human docs (train pool) vs LLM docs, i.e. docs at least as typical of LLM output
as of pre-2022 human writing (likelihood ratio >= 1). 0 = fully separable; ~0.5 = indistinguishable.
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.calibration import CalibratedClassifierCV
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GroupKFold, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

import features

SEED = 0


def load(data, genre):
    """Human table + LLM table (with features cached to disk, since spaCy is the slow step)."""
    data = Path(data)
    human = pd.read_parquet(data / f"human_{genre}.parquet")
    llm = pd.read_json(data / f"llm_{genre}.jsonl", lines=True)
    llm["id"] = llm.src_id + "|" + llm.model + "|" + llm.prompt
    llm["id"] = llm.id + "|" + llm.groupby("id").cumcount().astype(str)  # unique even if a source repeats
    extra = data / f"raid_{genre}.jsonl"  # commercial-model outputs, if available
    if extra.exists():
        r = pd.read_json(extra, lines=True)
        llm = pd.concat([llm, r[["id", "src_id", "genre", "model", "prompt", "text"]]], ignore_index=True)
    cached_features(human, data / f"feat_human_{genre}.jsonl")
    cached_features(llm, data / f"feat_llm_{genre}.jsonl")
    return human, llm


def cached_features(df, cache):
    """Adds column f; spaCy runs only on ids not already in the cache file."""
    have = {}
    if cache.exists():
        for line in cache.open(encoding="utf-8"):
            r = json.loads(line)
            have[r["id"]] = r["f"]
    todo = df[~df.id.isin(have)]
    if len(todo):
        with cache.open("a", encoding="utf-8") as f:
            for i, ft in zip(todo.id, features.extract(todo.text.tolist())):
                have[i] = ft
                f.write(json.dumps({"id": i, "f": ft}) + "\n")
    df["f"] = df.id.map(have)
    return df


def make_model(kind="logreg"):
    if kind == "logreg":
        base = make_pipeline(StandardScaler(), LogisticRegression(C=0.1, max_iter=3000))
    else:
        base = HistGradientBoostingClassifier(max_iter=300, learning_rate=0.05, random_state=SEED)
    return CalibratedClassifierCV(base, method="isotonic", cv=5)


def training_set(human, llm, exclude_model=None):
    """Balanced: equal numbers of pre-2022 human (train pool) and LLM docs."""
    L = llm if exclude_model is None else llm[llm.model != exclude_model]
    H = human[human.pool == "train"]
    H = H.sample(n=min(len(H), len(L)), random_state=SEED)
    L = L.sample(n=len(H), random_state=SEED)
    X = list(H.f) + list(L.f)
    y = np.r_[np.zeros(len(H)), np.ones(len(L))]
    # a polished text shares a group with its human source; Hansard groups are speakers
    groups = list(H.grp if "grp" in H else H.id) + list(L.src_id)
    return X, y, groups, L


def fit(X, y, kind="logreg"):
    vec = DictVectorizer(sparse=False)
    Xv = np.nan_to_num(vec.fit_transform(X))
    keep = (Xv != 0).mean(0) >= 0.01  # drop features present in <1% of training docs
    model = make_model(kind).fit(Xv[:, keep], y)
    return lambda F: model.predict_proba(np.nan_to_num(vec.transform(F))[:, keep])[:, 1], vec, keep, model


def cv_auc(X, y, groups, kind="logreg"):
    vec = DictVectorizer(sparse=False)
    Xv = np.nan_to_num(vec.fit_transform(X))
    Xv = Xv[:, (Xv != 0).mean(0) >= 0.01]
    p = cross_val_predict(make_model(kind), Xv, y, groups=groups, cv=GroupKFold(5), method="predict_proba")[:, 1]
    return roc_auc_score(y, p), p


def mso(p, n_boot=2000, seed=SEED):
    """Point estimate and 95% bootstrap CI of the share with P(LLM) >= 0.5."""
    hit = (np.asarray(p) >= 0.5).astype(float)
    if len(hit) == 0:
        return np.nan, np.nan, np.nan
    rng = np.random.default_rng(seed)
    boots = rng.choice(hit, (n_boot, len(hit))).mean(1)
    return hit.mean(), *np.percentile(boots, [2.5, 97.5])


def top_features(vec, keep, model, k=15):
    """Mean standardized logistic coefficients across calibration folds (+ = LLM-typical)."""
    coefs = np.mean([c.estimator[-1].coef_[0] for c in model.calibrated_classifiers_], 0)
    names = np.array(vec.feature_names_)[keep]
    order = np.argsort(coefs)
    return (pd.DataFrame({"feature": names[order[::-1][:k]], "coef": coefs[order[::-1][:k]]}),
            pd.DataFrame({"feature": names[order[:k]], "coef": coefs[order[:k]]}))


if __name__ == "__main__":
    assert mso([0.9, 0.1, 0.6, 0.2])[0] == 0.5
    lo, hi = mso([1.0] * 50 + [0.0] * 50)[1:]
    assert lo < 0.5 < hi
    print("mso ok")
