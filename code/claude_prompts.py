"""Write prompt batches for a frontier model (Claude) that cannot be run through Ollama.
Same prompt templates, same per-cell sampling rule as generate.py (crc32 seed of model+prompt), so the
Claude cell is drawn exactly like every local-model cell. Agents answer each prompt and write
{src_id, genre, model, prompt, text} lines; merge_claude() appends them to llm_<genre>.jsonl.
Usage: python claude_prompts.py DATA_DIR GENRE [n_per_cell] [batch_size]
       python claude_prompts.py DATA_DIR GENRE --merge
"""
import json, sys, zlib
from pathlib import Path

import pandas as pd

from generate import PROMPTS

MODEL = "claude-opus-5.5"


def make(data, genre, n=150, batch=50):
    src = pd.read_parquet(Path(data) / f"seed_{genre}.parquet")
    out = Path(data) / "claude_batches" / genre
    out.mkdir(parents=True, exist_ok=True)
    items = []
    for pk in ("P1", "P2", "P3"):
        cell = src.sample(n=min(n, len(src)), random_state=zlib.crc32(f"{MODEL}{pk}".encode()))
        for row in cell.itertuples():
            words = min(len(row.text.split()), 250)
            items.append({"src_id": row.id, "genre": genre, "model": MODEL, "prompt": pk,
                          "instruction": PROMPTS[genre][pk].format(title=row.title, n=round(words, -1), text=row.text)})
    for i in range(0, len(items), batch):
        with (out / f"prompts_{i // batch:02d}.jsonl").open("w", encoding="utf-8") as f:
            f.writelines(json.dumps(x) + "\n" for x in items[i:i + batch])
    print(len(items), "prompts in", -(-len(items) // batch), "batches ->", out)


def merge(data, genre):
    d = Path(data) / "claude_batches" / genre
    rows = []
    for f in sorted(d.glob("answers_*.jsonl")):
        for line in f.open(encoding="utf-8"):
            r = json.loads(line)
            assert r["model"] == MODEL and r["text"].strip(), f
            rows.append({k: r[k] for k in ("src_id", "genre", "model", "prompt", "text")})
    with (Path(data) / f"llm_{genre}.jsonl").open("a", encoding="utf-8") as f:
        f.writelines(json.dumps(r) + "\n" for r in rows)
    print("merged", len(rows))


if __name__ == "__main__":
    if "--merge" in sys.argv:
        merge(sys.argv[1], sys.argv[2])
    else:
        make(sys.argv[1], sys.argv[2], *(int(a) for a in sys.argv[3:5]))
