"""Mean token log-likelihood of each (cleaned, 250-word) essay under a small causal LM: the statistic behind
perplexity-based AI-text detectors. Resumable cache: DATA/ppl_essay.jsonl {id, logppl}.
Usage: python perplexity.py DATA_DIR
"""
import json, sys
from pathlib import Path

import pandas as pd
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

import features

MODEL = "Qwen/Qwen2.5-0.5B"


def scorer():
    """Returns f(texts) -> list of mean token negative log-likelihoods (same cleaning as the main run)."""
    torch.set_num_threads(6)
    tok = AutoTokenizer.from_pretrained(MODEL)
    lm = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.float32).eval()

    def f(texts):
        out = []
        with torch.no_grad():
            for t in texts:
                ids = tok(features.clean(t), return_tensors="pt", truncation=True, max_length=512).input_ids
                out.append(lm(ids, labels=ids).loss.item() if ids.shape[1] >= 5 else float("nan"))
        return out
    return f


def main(data):
    data = Path(data)
    human = pd.read_parquet(data / "human_essay.parquet")
    llm = pd.read_json(data / "llm_essay.jsonl", lines=True)
    llm["id"] = llm.src_id + "|" + llm.model + "|" + llm.prompt
    llm["id"] = llm.id + "|" + llm.groupby("id").cumcount().astype(str)  # same ids as mso.load
    docs = pd.concat([human[["id", "text"]], llm[["id", "text"]]], ignore_index=True)
    out = data / "ppl_essay.jsonl"
    done = set(pd.read_json(out, lines=True).id) if out.exists() else set()
    docs = docs[~docs.id.isin(done)]
    torch.set_num_threads(6)
    tok = AutoTokenizer.from_pretrained(MODEL)
    lm = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.float32).eval()
    with out.open("a", encoding="utf-8") as f, torch.no_grad():
        for i, (did, text) in enumerate(zip(docs.id, docs.text)):
            ids = tok(features.clean(text), return_tensors="pt", truncation=True, max_length=512).input_ids
            if ids.shape[1] < 5:
                continue
            loss = lm(ids, labels=ids).loss.item()  # mean negative log-likelihood per token
            f.write(json.dumps({"id": did, "logppl": loss}) + "\n")
            if i % 500 == 0:
                f.flush()
                print(i, "/", len(docs), flush=True)


if __name__ == "__main__":
    main(sys.argv[1])
