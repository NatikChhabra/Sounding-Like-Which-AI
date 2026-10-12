"""Keep RAID (Dugan et al. 2024, MIT) abstracts with no adversarial attack, all generators.

Downloads the 10 HF parquet shards one at a time, filters, deletes each shard.
Usage: python fetch_raid.py OUT.jsonl
"""
import json, sys, tempfile, urllib.request
from pathlib import Path

import pyarrow.compute as pc
import pyarrow.parquet as pq

BASE = "https://huggingface.co/api/datasets/liamdugan/raid/parquet/raid/train/{}.parquet"
COLS = ["id", "source_id", "model", "decoding", "repetition_penalty", "attack", "domain", "title", "generation"]


def main(out):
    out = Path(out)
    with out.open("w", encoding="utf-8") as f:
        for i in range(10):
            tmp = Path(tempfile.gettempdir()) / f"raid_{i}.parquet"
            urllib.request.urlretrieve(BASE.format(i), tmp)
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
            print("shard", i, "kept", t.num_rows, flush=True)


if __name__ == "__main__":
    main(sys.argv[1])
