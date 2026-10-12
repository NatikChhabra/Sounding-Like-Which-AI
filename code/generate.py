"""Generate LLM text with local models via Ollama, from prompts built on pre-2022 human documents.

Input: a parquet of source docs with columns id, genre, title, text (pre-2022 human only).
Output: appends JSON lines {src_id, genre, model, prompt, text} -- resumable (skips done pairs).
Usage: python generate.py SOURCES.parquet OUT.jsonl [n_per_cell]
"""
import json, sys, urllib.request, zlib
from pathlib import Path

import pandas as pd

MODELS = ["llama3.1:8b", "qwen3:8b", "gemma3:12b", "mistral:7b", "gpt-oss:20b"]
URL = "http://127.0.0.1:11434/api/chat"

# P1 = write from scratch, P2 = polish a human draft (AI-assisted writing), P3 = asked to sound human.
PROMPTS = {
    "arxiv": {
        "P1": "Write the abstract for a research paper titled \"{title}\". About {n} words. Output only the abstract.",
        "P2": "Improve the writing of this research abstract. Keep the content. Output only the revised abstract.\n\n{text}",
        "P3": "Write the abstract for a research paper titled \"{title}\". About {n} words. Write plainly, like a "
              "busy researcher would; avoid typical AI phrasing. Output only the abstract.",
    },
    "hansard": {
        "P1": "Write a speech by a member of the Australian Parliament in a debate on \"{title}\". About {n} words. "
              "Output only the speech.",
        "P2": "Improve the wording of this parliamentary speech. Keep the content. Output only the revised speech.\n\n{text}",
        "P3": "Write a speech by a member of the Australian Parliament in a debate on \"{title}\". About {n} words. "
              "Make it sound like a real spoken speech, not AI writing. Output only the speech.",
    },
    "essay": {
        "P1": "Write an argumentative essay by a US high-school student responding to this prompt: \"{title}\". "
              "About {n} words. Output only the essay.",
        "P2": "Improve the writing of this student essay. Keep the content. Output only the revised essay.\n\n{text}",
        "P3": "Write an argumentative essay by a US high-school student responding to this prompt: \"{title}\". "
              "About {n} words. Make it sound like a real student wrote it, not AI. Output only the essay.",
    },
}


def chat(model, prompt, seed):
    body = {"model": model, "stream": False, "messages": [{"role": "user", "content": prompt}],
            "options": {"temperature": 0.8, "seed": seed, "num_predict": 1200}}
    if model.startswith("qwen3"):
        body["think"] = False
    if model.startswith("gpt-oss"):
        body["think"] = "low"
    req = urllib.request.Request(URL, json.dumps(body).encode(), {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.loads(r.read())["message"]["content"].strip()


def main(src, out, n_per_cell=200):
    src = pd.read_parquet(src)
    out = Path(out)
    done = set()
    if out.exists():
        for line in out.open(encoding="utf-8"):
            r = json.loads(line)
            done.add((r["src_id"], r["model"], r["prompt"]))
    with out.open("a", encoding="utf-8") as f:
        for model in MODELS:  # model-outer loop so each model loads into VRAM once
            for pk in ("P1", "P2", "P3"):
                # each (model, prompt) cell gets its own disjoint-ish random draw of sources
                cell = src.sample(n=min(n_per_cell, len(src)), random_state=zlib.crc32(f"{model}{pk}".encode()))
                for i, row in enumerate(cell.itertuples()):
                    if (row.id, model, pk) in done:
                        continue
                    words = min(len(row.text.split()), 250)
                    prompt = PROMPTS[row.genre][pk].format(title=row.title, n=round(words, -1), text=row.text)
                    text = chat(model, prompt, seed=i)
                    f.write(json.dumps({"src_id": row.id, "genre": row.genre, "model": model,
                                        "prompt": pk, "text": text}) + "\n")
                    f.flush()
                print(f"{model} {pk} done", flush=True)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 200)
