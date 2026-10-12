"""Resolve every citation against Crossref (DOI) or the arXiv API; write paper/references.bib and
lit/CITATIONS.md (the human verification checklist). Nothing is typed by hand.
Usage: python fetch_bib.py lit/citations.txt
"""
import re, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NS = {"a": "http://www.w3.org/2005/Atom"}


def get(url, accept=None):
    req = urllib.request.Request(url, headers={"Accept": accept} if accept else {})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8")


def doi_entry(key, doi):
    bib = get("https://doi.org/" + doi, "application/x-bibtex").strip()
    bib = re.sub(r"^@(\w+)\{[^,]*,", lambda m: f"@{m.group(1)}{{{key},", bib, count=1)
    bib = re.sub(r"(?<!\\)&", r"\\&", bib)  # Crossref leaves bare & (e.g. series={C&C '24}); LaTeX needs \&
    title = re.search(r"title\s*=\s*\{(.+?)\},", bib, re.S)
    year = re.search(r"year\s*=\s*\{?(\d{4})", bib)
    return bib, (title.group(1) if title else "?"), (year.group(1) if year else "?"), "https://doi.org/" + doi


def arxiv_entry(key, aid):
    e = ET.fromstring(get("http://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": aid})))
    e = e.find("a:entry", NS)
    title = " ".join(e.findtext("a:title", "", NS).split())
    if not title or title == "Error":
        raise ValueError(f"arXiv id {aid} not found")
    authors = " and ".join(a.findtext("a:name", "", NS) for a in e.iterfind("a:author", NS))
    year = e.findtext("a:published", "", NS)[:4]
    bib = (f"@misc{{{key},\n  title = {{{title}}},\n  author = {{{authors}}},\n  year = {{{year}}},\n"
           f"  eprint = {{{aid}}},\n  archivePrefix = {{arXiv}},\n  url = {{https://arxiv.org/abs/{aid}}}\n}}")
    time.sleep(3)
    return bib, title, year, f"https://arxiv.org/abs/{aid}"


def main(src):
    bibs, rows = [], []
    for line in Path(src).read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        key, ident = line.split()[:2]
        kind, val = ident.split(":", 1)
        try:
            bib, title, year, url = (doi_entry if kind == "doi" else arxiv_entry)(key, val)
            bibs.append(bib)
            rows.append(f"- [ ] `{key}` ({year}) [{title}]({url})")
        except Exception as ex:  # unresolvable = must not be cited
            rows.append(f"- [ ] `{key}` **FAILED TO RESOLVE ({ident}): {ex}** — do not cite until fixed")
        print(rows[-1], flush=True)
    (ROOT / "paper").mkdir(exist_ok=True)
    (ROOT / "paper/references.bib").write_text("\n\n".join(bibs) + "\n", encoding="utf-8")
    (ROOT / "lit/CITATIONS.md").write_text(
        "# Citation verification checklist\n\nEach entry was resolved automatically from its DOI or arXiv id. "
        "Before submission the author opens every link, confirms the paper says what our text claims, and ticks "
        "the box.\n\n" + "\n".join(rows) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1])
