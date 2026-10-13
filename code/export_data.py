"""Write the release data folder: every LLM generation used in the paper, and the exact samples and train/score
splits (ids only for most human documents, so third-party texts are not redistributed). Output is deterministic
(gzip timestamps fixed), so re-running it does not change the committed files.
Usage: python export_data.py DATA_DIR OUT_DIR
"""
import gzip, json, sys
from pathlib import Path

import pandas as pd


def gz_write(path, data: bytes):
    with open(path, "wb") as raw, gzip.GzipFile(fileobj=raw, mode="wb", compresslevel=9, mtime=0, filename="") as g:
        g.write(data)


def gz_csv(df, path):
    gz_write(path, df.to_csv(index=False).encode("utf-8"))


def main(data, out):
    data, out = Path(data), Path(out)
    gen, ids = out / "generated", out / "samples"
    gen.mkdir(parents=True, exist_ok=True)
    ids.mkdir(parents=True, exist_ok=True)
    for f in ("llm_arxiv.jsonl", "llm_arxiv_old.jsonl", "llm_essay.jsonl"):
        gz_write(gen / (f + ".gz"), (data / f).read_bytes())
    # Hansard text (aph.gov.au) is CC BY-NC-ND: revisions of real speeches (P2) are adaptations, so only their
    # keys are released; the line-level filter keeps the other rows byte-identical
    lines = (data / "llm_hansard.jsonl").read_bytes().splitlines(keepends=True)
    p2 = [json.loads(l) for l in lines if json.loads(l)["prompt"] == "P2"]
    gz_write(gen / "llm_hansard.jsonl.gz", b"".join(l for l in lines if json.loads(l)["prompt"] != "P2"))
    if p2:  # a data folder rebuilt from this release has no P2 rows; keep the released list then
        gz_csv(pd.DataFrame(p2)[["src_id", "model", "prompt"]], gen / "hansard_p2_rows.csv.gz")
    for name in ("arxiv_v2", "arxiv"):  # the second (v1) sample seeded the original generators
        src = data / name / "sample.jsonl"
        if src.exists():
            a = pd.read_json(src, lines=True)
            cols = [c for c in ("id", "field", "primary", "published", "updated") if c in a]
            gz_csv(a[cols], ids / f"{name}_sample_ids.csv.gz")
    for g in ("arxiv", "hansard", "essay"):
        h = pd.read_parquet(data / f"human_{g}.parquet")
        cols = [c for c in ("id", "date", "group", "grp", "pool", "title") if c in h]
        if g == "essay":  # PERSUADE fields beyond ids stay with the source dataset
            cols = ["id", "group", "pool"]
        gz_csv(h[cols], ids / f"{g}_split.csv.gz")
    # source abstracts of generations seeded from the first sample but absent from the analysed corpus
    # (arXiv metadata is CC0); analysis.source_texts falls back to this file when the first sample is not present
    v1 = data / "arxiv" / "sample.jsonl"
    if v1.exists():
        llm = pd.concat([pd.read_json(data / f, lines=True) for f in ("llm_arxiv.jsonl", "llm_arxiv_old.jsonl")])
        used = set(llm.src_id.str.replace(r"v\d+$", "", regex=True))
        human = set(pd.read_parquet(data / "human_arxiv.parquet").id)
        a = pd.read_json(v1, lines=True)
        a["id"] = "arxiv:" + a.id.str.replace(r"v\d+$", "", regex=True)
        a = a[a.id.isin(used - human)].drop_duplicates("id")[["id", "title", "abstract"]]
        gz_write(ids / "arxiv_v1_seed_sources.jsonl.gz", a.to_json(orient="records", lines=True).encode("utf-8"))
    print("wrote", sorted(p.name for p in out.rglob("*.gz")))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
