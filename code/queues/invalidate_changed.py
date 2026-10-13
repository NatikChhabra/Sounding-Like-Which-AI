"""Drop cached features / perplexities of every text whose cleaned form differs between the previous cleaning
(_MD as of commit 1012d6b) and the current features.clean. Backs up each changed cache first."""
import json, re, sys
from pathlib import Path

sys.path.insert(0, r"F:\downloads\Outreach and other plans\research-paper\code")
import pandas as pd
import features

D = Path(sys.argv[1])
OLD_MD = [(re.compile(r"\*\*|__|`|^#+\s*", re.M), ""),
          (re.compile(r"(?<![\w*])\*(?=\S)([^*\n]+?)(?<=\S)\*(?![\w*])"), r"\1"),
          (re.compile(r"^\s*title\s*:.*$", re.I | re.M), ""),
          (re.compile(r"^\s*(abstract|speech|essay)\s*:\s*", re.I | re.M), ""),
          (re.compile(r"^\s*([-*•]|\d+[.)])\s+", re.M), "")]


def old_clean(t):
    t = features.delatex(features.unwrap(t))
    for p, r in OLD_MD:
        t = p.sub(r, t)
    return " ".join(t.split()[:features.MAX_WORDS])


changed = lambda t: old_clean(t) != features.clean(t)


def llm_ids(f, strip):
    d = pd.read_json(f, lines=True)
    if strip:
        d["src_id"] = d.src_id.str.replace(r"v\d+$", "", regex=True)
    d["id"] = d.src_id + "|" + d.model + "|" + d.prompt
    d["id"] = d.id + "|" + d.groupby("id").cumcount().astype(str)
    return set(d.id[d.text.map(changed)])


bad = set()
for g in ("arxiv", "hansard", "essay"):
    bad |= llm_ids(D / f"llm_{g}.jsonl", g == "arxiv")
    h = pd.read_parquet(D / f"human_{g}.parquet")
    hb = set(h.id[h.text.map(changed)])
    print(g, "human changed:", len(hb))
    bad |= hb
bad |= llm_ids(D / "llm_arxiv_old.jsonl", False)
r = pd.read_json(D / "raid_arxiv.jsonl", lines=True)
bad |= set(r.id[r.text.map(changed)])
print("changed texts:", len(bad))

(D / "cache_backup2").mkdir(exist_ok=True)
for cache in sorted(D.glob("feat_*.jsonl")) + sorted(D.glob("ppl_essay*.jsonl")):
    lines = cache.read_text(encoding="utf-8").splitlines()
    keep = [ln for ln in lines if json.loads(ln)["id"] not in bad]
    if len(keep) < len(lines):
        (D / "cache_backup2" / cache.name).write_text("\n".join(lines) + "\n", encoding="utf-8")
        cache.write_text("\n".join(keep) + ("\n" if keep else ""), encoding="utf-8")
    print(cache.name, len(lines), "->", len(keep))
