"""One-off: drop cached features / perplexities of texts whose cleaning changed with the 'Title:' line fix."""
import json, re, sys
from pathlib import Path

import pandas as pd

D = Path(sys.argv[1])
TITLE = re.compile(r"^\s*title\s*:", re.I | re.M)
changed = lambda t: bool(TITLE.search(t.replace("**", "")))


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
    bad |= set(h.id[h.text.map(changed)])
bad |= llm_ids(D / "llm_arxiv_old.jsonl", False)
r = pd.read_json(D / "raid_arxiv.jsonl", lines=True)
bad |= set(r.id[r.text.map(changed)])
print("changed texts:", len(bad))

for cache in sorted(D.glob("feat_*.jsonl")) + sorted(D.glob("ppl_essay*.jsonl")):
    lines = cache.read_text(encoding="utf-8").splitlines()
    keep = [ln for ln in lines if json.loads(ln)["id"] not in bad]
    if len(keep) < len(lines):  # backup first; caches are regenerable but slow
        (D / "cache_backup").mkdir(exist_ok=True)
        (D / "cache_backup" / cache.name).write_text("\n".join(lines) + "\n", encoding="utf-8")
        cache.write_text("\n".join(keep) + ("\n" if keep else ""), encoding="utf-8")
    print(cache.name, len(lines), "->", len(keep))
