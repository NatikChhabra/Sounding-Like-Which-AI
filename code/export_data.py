"""Write the release data folder: every LLM generation used in the paper, and the exact samples and train/score
splits (ids only for human documents, so third-party texts are not redistributed).
Usage: python export_data.py DATA_DIR OUT_DIR
"""
import gzip, shutil, sys
from pathlib import Path

import pandas as pd


def main(data, out):
    data, out = Path(data), Path(out)
    gen, ids = out / "generated", out / "samples"
    gen.mkdir(parents=True, exist_ok=True)
    ids.mkdir(parents=True, exist_ok=True)
    for f in ("llm_arxiv.jsonl", "llm_arxiv_old.jsonl", "llm_hansard.jsonl", "llm_essay.jsonl"):
        with open(data / f, "rb") as src, gzip.open(gen / (f + ".gz"), "wb", compresslevel=9) as dst:
            shutil.copyfileobj(src, dst)
    for name in ("arxiv_v2", "arxiv"):  # the second (v1) sample seeded the original generators
        a = pd.read_json(data / name / "sample.jsonl", lines=True)
        cols = [c for c in ("id", "field", "primary", "published", "updated") if c in a]
        a[cols].to_csv(ids / f"{name}_sample_ids.csv.gz", index=False, compression="gzip")
    for g in ("arxiv", "hansard", "essay"):
        h = pd.read_parquet(data / f"human_{g}.parquet")
        cols = [c for c in ("id", "date", "group", "grp", "pool", "score", "grade", "title") if c in h]
        if g == "essay":  # PERSUADE fields beyond ids stay with the source dataset
            cols = [c for c in ("id", "group", "pool") if c in h]
        h[cols].to_csv(ids / f"{g}_split.csv.gz", index=False, compression="gzip")
    print("wrote", sorted(p.name for p in out.rglob("*.gz")))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
