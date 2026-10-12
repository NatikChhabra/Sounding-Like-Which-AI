"""Stratified random sample of arXiv abstracts, 2015-01 to 2026-09, via the arXiv API.

For each (field, month): one random window of WINDOW[field] consecutive days, up to 400 papers whose
PRIMARY category is in the field. Window length scales with field size so cells reach ~150 papers.
Resumable: finished cells are listed in done.txt. Usage: python fetch_arxiv.py OUT_DIR
"""
import calendar, json, random, sys, time, urllib.error, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

API = "http://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
WINDOW = {"cs": 2, "math": 3, "astro-ph": 4, "cond-mat": 4, "stat": 6, "eess": 6, "q-bio": 12, "econ": 15}
MONTHS = [(y, m) for y in range(2015, 2027) for m in range(1, 13) if (y, m) <= (2026, 9)]


def query(field, start, end):
    q = f"cat:{field}.* AND submittedDate:[{start}0000 TO {end}2359]"
    url = API + "?" + urllib.parse.urlencode({"search_query": q, "max_results": 400,
                                               "sortBy": "submittedDate", "sortOrder": "ascending"})
    for attempt in range(8):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                return ET.fromstring(r.read())
        except (urllib.error.URLError, TimeoutError, ET.ParseError):
            time.sleep(15 * (attempt + 1))
    return None  # caller skips the cell without marking it done; a rerun retries it


def main(out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    done_f = out / "done.txt"
    done = set(done_f.read_text().split()) if done_f.exists() else set()
    rng = random.Random(20221130)
    plan = [(f, y, m, rng.randint(1, calendar.monthrange(y, m)[1])) for f in WINDOW for y, m in MONTHS]
    with (out / "sample.jsonl").open("a", encoding="utf-8") as fo:
        for field, y, m, d0 in plan:
            cell = f"{field}|{y}-{m:02d}"
            if cell in done:
                continue
            last = calendar.monthrange(y, m)[1]
            d0 = min(d0, max(1, last - WINDOW[field] + 1))
            d1 = min(last, d0 + WINDOW[field] - 1)
            root = query(field, f"{y}{m:02d}{d0:02d}", f"{y}{m:02d}{d1:02d}")
            if root is None:
                print(cell, "FAILED, will retry on rerun", flush=True)
                continue
            n = 0
            for e in root.iterfind("a:entry", NS):
                prim = e.find("x:primary_category", NS)
                prim = prim.get("term") if prim is not None else ""
                if not prim.startswith(field + "."):
                    continue  # cross-list from another field
                fo.write(json.dumps({
                    "id": e.findtext("a:id", "", NS).rsplit("/abs/", 1)[-1],
                    "field": field, "primary": prim, "published": e.findtext("a:published", "", NS),
                    "title": " ".join(e.findtext("a:title", "", NS).split()),
                    "abstract": " ".join(e.findtext("a:summary", "", NS).split()),
                }) + "\n")
                n += 1
            fo.flush()
            with done_f.open("a") as f:
                f.write(cell + "\n")
            print(cell, n, flush=True)
            time.sleep(3.1)  # arXiv API terms: max 1 request / 3 s


if __name__ == "__main__":
    main(sys.argv[1])
