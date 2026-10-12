"""Keep RAID (Dugan et al. 2024, MIT) abstracts with no adversarial attack, all generators.

Downloads the 10 HF parquet shards one at a time, filters, deletes each shard.
Usage: python fetch_raid.py OUT.jsonl
"""
import json, subprocess, sys, tempfile
from pathlib import Path

import pyarrow.compute as pc
import pyarrow.parquet as pq

BASE = "https://huggingface.co/api/datasets/liamdugan/raid/parquet/raid/train/{}.parquet"
COLS = ["id", "source_id", "model", "decoding", "repetition_penalty", "attack", "domain", "title", "generation"]


def download(url, path):
    # curl resumes (-C -) across the dropped connections urllib gave up on
    for _ in range(50):
        if subprocess.run(["curl.exe", "-sSL", "-C", "-", "--retry", "5", "-o", str(path), url]).returncode == 0:
            return
    raise RuntimeError(url)


def main(out):
    out = Path(out)
    done_f = out.with_suffix(".done")
    done = set(done_f.read_text().split()) if done_f.exists() else set()
    with out.open("a", encoding="utf-8") as f:
        for i in range(10):
            if str(i) in done:
                continue
            tmp = Path(tempfile.gettempdir()) / f"raid_{i}.parquet"
            download(BASE.format(i), tmp)
            t = pq.read_table(tmp, columns=COLS)
            t = t.filter(pc.and_(pc.equal(t["domain"], "abstracts"), pc.equal(t["attack"], "none")))
            for r in t.to_pylist():
                if r["model"] == "human":
                    continue  # RAID's human abstracts aren't dated; we use our own arXiv sample
                f.write(json.dumps({
                    "id": "raid:" + r["id"], "src_id": "raid:" + str(r["source_id"]), "genre": "arxiv",
                    "model": "raid-" + r["model"], "prompt": f"raid-{r['decoding']}-rp{r['repetition_penalty']}",
                    "title": r["title"], "text": r["generation"]}) + "\n")
            tmp.unlink()
            f.flush()
            with done_f.open("a") as d:
                d.write(f"{i}\n")
            print("shard", i, "kept", t.num_rows, flush=True)


if __name__ == "__main__":
    main(sys.argv[1])
