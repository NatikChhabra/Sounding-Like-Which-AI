"""Build one human-text table per genre with a fixed train/score split.

pool == "train": pre-2022-11-30 human docs used to (a) train the style classifier as the human side and
(b) seed LLM generation prompts. pool == "score": everything else; MSO is only ever measured on these,
so no document is both a training example/prompt source and a measured document.
Usage: python build_sources.py {essay|arxiv|hansard} DATA_DIR
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

CUTOFF = pd.Timestamp("2022-11-30")


def split(df, frac=0.5, seed=0):
    rng = np.random.default_rng(seed)
    pre = df["date"] < CUTOFF
    df["pool"] = np.where(pre & (rng.random(len(df)) < frac), "train", "score")
    return df


def essay(d):
    p = pd.read_csv(d / "learner/persuade_2.0_train.csv",
                    usecols=["essay_id", "full_text", "prompt_name", "ell_status", "grade_level"])
    p = p.drop_duplicates("essay_id").dropna(subset=["full_text"])
    p = p[p.ell_status.isin(["Yes", "No"])]
    return split(pd.DataFrame({
        "id": "persuade:" + p.essay_id.astype(str), "genre": "essay", "title": p.prompt_name,
        "text": p.full_text, "date": pd.Timestamp("2019-01-01"),  # PERSUADE essays are pre-2020
        "group": np.where(p.ell_status == "Yes", "ELL", "non-ELL"), "grade": p.grade_level}))


def arxiv(d):
    a = pd.read_json(d / "arxiv/sample.jsonl", lines=True).drop_duplicates("id")
    return split(pd.DataFrame({
        "id": "arxiv:" + a.id, "genre": "arxiv", "title": a.title, "text": a.abstract,
        "date": pd.to_datetime(a.published).dt.tz_localize(None), "group": a.field}))


def hansard(d, per_month=150, seed=0):
    h = pd.read_parquet(d / "hansard_au/corpus_1998_to_2025.parquet",
                        columns=["date", "body", "uniqueID", "order", "interject", "q_in_writing", "partyAbbrev"])
    h = h[(h.interject.astype(str) != "1") & (h.q_in_writing.astype(str) != "1")]  # spoken speeches only
    h["date"] = pd.to_datetime(h.date)
    h = h[(h.date >= "2015-01-01") & (h.body.str.split().str.len() >= 50)]
    h = h.groupby(h.date.dt.to_period("M"), group_keys=False).apply(
        lambda g: g.sample(n=min(per_month, len(g)), random_state=seed))
    # no debate titles in this corpus: the opening sentence stands in as the topic cue for prompts
    first = h.body.str.split(r"(?<=[.?!])\s", n=1, regex=True).str[0].str.split().str[:30].str.join(" ")
    # uniqueID in this corpus identifies the SPEAKER, not the speech: the speech id is date + order,
    # and the speaker becomes `grp` so cross-validation never splits one speaker across folds.
    sid = "hansard:" + h.date.dt.strftime("%Y-%m-%d") + ":" + h.order.astype(str)
    return split(pd.DataFrame({
        "id": sid, "genre": "hansard", "title": first, "text": h.body, "date": h.date,
        "group": h.partyAbbrev.astype(str), "grp": ("hansard:" + h.uniqueID.astype(str)).where(h.uniqueID.notna(), sid)}))


if __name__ == "__main__":
    genre, d = sys.argv[1], Path(sys.argv[2])
    df = {"essay": essay, "arxiv": arxiv, "hansard": hansard}[genre](d)
    df = df[df.text.str.split().str.len() >= 50]  # too-short texts carry little style signal
    assert df.id.is_unique, "document ids must be unique (feature cache is keyed by id)"
    if "grp" not in df:
        df["grp"] = df.id
    df.to_parquet(d / f"human_{genre}.parquet", index=False)
    df[df.pool == "train"].to_parquet(d / f"seed_{genre}.parquet", index=False)
    print(genre, len(df), "docs;", (df.pool == "train").sum(), "train pool")
    print(df.groupby(["pool", "group"]).size().to_string())
