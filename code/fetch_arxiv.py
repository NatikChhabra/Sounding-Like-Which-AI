"""Stratified random sample of arXiv abstracts, 2015-01 to 2026-09, via the arXiv API.

For each (field, month): one random window of WINDOW[field] consecutive days. ALL papers in the window are
fetched (paginated), papers whose primary category is outside the field are dropped, and PER_CELL papers are
drawn uniformly at random, so every field-month cell has the same design weight and no part of the window is
favoured (v1 of this script kept only the first 400 results, which truncated recent cs windows to papers
submitted early in the day). Both the v1 submission date (`published`) and last-revision date (`updated`)
are recorded. Resumable via done.txt. Usage: python fetch_arxiv.py OUT_DIR
"""
import calendar, json, random, sys, time, urllib.error, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

API = "http://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom",
      "o": "http://a9.com/-/spec/opensearch/1.1/"}
WINDOW = {"cs": 2, "math": 3, "astro-ph": 4, "cond-mat": 4, "stat": 6, "eess": 6, "q-bio": 12, "econ": 15}
MONTHS = [(y, m) for y in range(2015, 2027) for m in range(1, 13) if (y, m) <= (2026, 9)]
PER_CELL, PAGE = 200, 500


def query(field, start, end, offset):
    q = f"cat:{field}.* AND submittedDate:[{start}0000 TO {end}2359]"
    url = API + "?" + urllib.parse.urlencode({"search_query": q, "start": offset, "max_results": PAGE,
                                               "sortBy": "submittedDate", "sortOrder": "ascending"})
    for attempt in range(8):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                return ET.fromstring(r.read())
        except (urllib.error.URLError, TimeoutError, ET.ParseError):
            time.sleep(15 * (attempt + 1))
    return None


def fetch_window(field, start, end):
    """All entries in the window (list of dicts) or None if the API kept failing."""
    rows, offset, total = [], 0, None
    while total is None or offset < total:
        root = query(field, start, end, offset)
        time.sleep(3.1)  # arXiv API terms: max 1 request / 3 s
        if root is None:
            return None
        total = int(root.findtext("o:totalResults", "0", NS))
        entries = root.findall("a:entry", NS)
        if not entries and offset < total:
            return None  # API returned an empty page mid-window: treat as failure, retry cell later
        for e in entries:
            prim = e.find("x:primary_category", NS)
            prim = prim.get("term") if prim is not None else ""
            if prim.startswith(field + "."):
                rows.append({"id": e.findtext("a:id", "", NS).rsplit("/abs/", 1)[-1], "field": field,
                             "primary": prim, "published": e.findtext("a:published", "", NS),
                             "updated": e.findtext("a:updated", "", NS),
                             "title": " ".join(e.findtext("a:title", "", NS).split()),
                             "abstract": " ".join(e.findtext("a:summary", "", NS).split())})
        offset += PAGE
    return rows


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
            rows = fetch_window(field, f"{y}{m:02d}{d0:02d}", f"{y}{m:02d}{d1:02d}")
            if rows is None:
                print(cell, "FAILED, will retry on rerun", flush=True)
                continue
            pick = random.Random(f"{cell}").sample(rows, min(PER_CELL, len(rows)))
            fo.writelines(json.dumps(r) + "\n" for r in pick)
            fo.flush()
            with done_f.open("a") as f:
                f.write(cell + "\n")
            print(cell, len(rows), "->", len(pick), flush=True)


if __name__ == "__main__":
    main(sys.argv[1])
