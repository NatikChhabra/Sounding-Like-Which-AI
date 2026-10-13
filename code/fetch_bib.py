"""Resolve every citation against Crossref (DOI) or the arXiv API; write paper/references.bib and
lit/CITATIONS.md (the human verification checklist). Nothing is typed by hand.
Usage: python fetch_bib.py lit/citations.txt
"""
import html, re, sys, time, urllib.parse, urllib.request
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


def bib_entry(key, url):
    """Raw BibTeX served by the official venue page (ACL Anthology, NeurIPS/ICLR proceedings, PMLR)."""
    import html
    bib = get(url).strip()
    if not bib.startswith("@"):  # PMLR embeds the BibTeX in the paper's HTML page
        m = re.search(r"(@\w+\{[^@]*?\n\})", html.unescape(re.sub(r"<[^>]+>", "", bib)))
        if not m:
            raise ValueError(f"no BibTeX at {url}")
        bib = m.group(1).strip()
    bib = re.sub(r"^@(\w+)\s*\{[^,]*,", lambda m: f"@{m.group(1)}{{{key},", bib, count=1)
    bib = re.sub(r"(?<!\\)&", r"\\&", bib)
    title = re.search(r"(?<![a-z])title\s*=\s*[{\"](.+?)[}\"],", bib, re.S)
    year = re.search(r"year\s*=\s*[{\"]?(\d{4})", bib)
    return bib, (title.group(1) if title else "?"), (year.group(1) if year else "?"), url.rsplit(".bib", 1)[0]


def manual_entry(key, _):
    """Entry from lit/manual.bib (only for works without DOI/arXiv id; fields checked on the official listing)."""
    text = (ROOT / "lit/manual.bib").read_text(encoding="utf-8")
    m = re.search(r"(@\w+\{" + re.escape(key) + r",.*?\n\})", text, re.S)
    if not m:
        raise ValueError(f"{key} not in lit/manual.bib")
    bib = m.group(1)
    title = re.search(r"(?<![a-z])title\s*=\s*\{(.+?)\},", bib).group(1)
    url = re.search(r"url\s*=\s*\{(.+?)\}", bib).group(1)
    return bib, title, re.search(r"year\s*=\s*\{(\d{4})", bib).group(1), url


def arxiv_entry(key, aid):
    e = ET.fromstring(get("http://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": aid})))
    e = e.find("a:entry", NS)
    title = " ".join(e.findtext("a:title", "", NS).split())
    if not title or title == "Error":
        raise ValueError(f"arXiv id {aid} not found")
    authors = " and ".join(a.findtext("a:name", "", NS) for a in e.iterfind("a:author", NS))
    # an explicitly versioned id (e.g. 2409.01754v4) cites that version, so use its date
    year = e.findtext("a:updated" if re.search(r"v\d+$", aid) else "a:published", "", NS)[:4]
    bib = (f"@misc{{{key},\n  title = {{{title}}},\n  author = {{{authors}}},\n  year = {{{year}}},\n"
           f"  eprint = {{{aid}}},\n  archivePrefix = {{arXiv}},\n  url = {{https://arxiv.org/abs/{aid}}}\n}}")
    time.sleep(3)
    return bib, title, year, f"https://arxiv.org/abs/{aid}"


PROPER = {"Wikipedia", "Australian", "English", "Hansard", "Parliamentary", "Debates", "Bayes", "Korean",
          "Binoculars", "Coevolution"}


# Titles whose fetched form loses capitals after "?" or a braced colon under acl_natbib, or has Unicode quotes
# (wording checked against the source records; lit/verification/batch7_bib.md)
TITLES = {
    "juzek2025": r"Why Does {C}hat{GPT} ``Delve'' So Much? {E}xploring the Sources of Lexical Overrepresentation in Large Language Models",
    "khan2026": r"Who Gets Seen in the Age of {AI}? {A}doption Patterns of Large Language Models in Scholarly Writing and Citation Outcomes",
    "reinhart2025": r"Do {LLMs} Write Like Humans? {V}ariation in Grammatical and Rhetorical Styles",
    "sun2025": r"Are We in the {AI}-Generated Text World Already? {Q}uantifying and Monitoring {AIGT} on Social Media",
    "gray2024": r"{ChatGPT} ``Contamination'': {E}stimating the Prevalence of {LLMs} in the Scholarly Literature",
    "chang2026": r"Human Writing and Machine Patterns: {A}nalyzing a Decade of Convergence",
    "mccarthy2010": r"{MTLD}, vocd-{D}, and {HD-D}: {A} Validation Study of Sophisticated Approaches to Lexical Diversity Assessment",
    "dugan2024raid": r"{RAID}: {A} Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors",
    "geng2025": r"{Human-LLM} Coevolution: {E}vidence from Academic Writing",
    "bao2024fastdetectgpt": r"{Fast-DetectGPT}: {E}fficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature",
    "pillutla2021": r"{MAUVE}: {M}easuring the Gap Between Neural Text and Human Text using Divergence Frontiers",
    "clark2021": r"All That{'}s {`}{H}uman{'} Is Not Gold: {E}valuating Human Evaluation of Generated Text",
    "zheng2023judging": r"Judging {LLM}-as-a-Judge with {MT-Bench} and {Chatbot} {Arena}",
}


# Article numbers missing from Crossref's BibTeX (checked on the publisher pages; lit/verification/v5_batch*.md)
PAGES = {"gao2023": "75", "herbold2023": "18617", "jakesch2023": "e2208839120", "kobak2025": "eadt3813",
         "munozortiz2024": "265", "reinhart2025": "e2422455122"}


def retitle(key, bib):
    if key in PAGES and not re.search(r"pages\s*=", bib):
        bib = re.sub(r"^(@\w+\{[^,]+,)", lambda m: m.group(1) + " pages={" + PAGES[key] + "},", bib, count=1)
    if key not in TITLES:
        return bib
    # braced (Crossref, arXiv) or quoted (ACL Anthology) title field
    return re.sub(r'(?<![a-z])title\s*=\s*(?:\{(?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*\}|"[^"]*"),',
                  lambda m: "title = {" + TITLES[key] + "},", bib, count=1)


def tidy(bib):
    """ACL's style lower-cases titles: brace acronyms (>=2 capitals, e.g. ChatGPT, LLMs, AI) and proper nouns so
    they survive; give page ranges a LaTeX en dash."""
    def keep(w):  # acronym (>=2 capitals), model size such as 7B, or proper noun
        return (len(re.findall(r"[A-Z]", w)) >= 2 or re.search(r"\d[A-Z]", w) is not None
                or w.strip(".,:;?!()") in PROPER)

    def brace(w):
        if "{" in w or not keep(w):
            return w
        if "-" in w:  # AI-Associated -> {AI}-Associated, so the style still lowercases "associated"
            return "-".join("{" + p + "}" if keep(p) else p for p in w.split("-"))
        return "{" + w + "}"

    def protect(m):
        return m.group(1) + "".join(brace(w) for w in re.split(r"(\s+)", m.group(2))) + m.group(3)
    # title = {...} with at most one level of nested braces; works for one-line (Crossref) and multi-line entries
    bib = re.sub(r"((?<![a-z])title\s*=\s*\{)((?:[^{}]|\{[^{}]*\})*)(\})", protect, bib)
    bib = html.unescape(bib)  # Crossref sometimes returns HTML entities (Computers &amp; Education)
    bib = re.sub(r"(?<!\\)&", r"\\&", bib)  # arXiv titles can contain a bare & (e.g. the gpt-oss model card)
    bib = bib.replace("Mcfarland", "McFarland").replace("’", "'")  # PMLR author list; curly apostrophes vanish
    bib = bib.replace("ő", r"{\H{o}}")  # the Times font has no ő glyph (Emőke would print as "Emke")
    # Crossref writes month=July/June, which BibTeX does not know (the month is then dropped); use its macros
    bib = re.sub(r"month\s*=\s*([A-Z][a-z]+)\b", lambda m: "month=" + m.group(1)[:3].lower(), bib)
    # initials need a full stop ("Christopher D Manning" -> "Christopher D. Manning")
    bib = re.sub(r"(author\s*=\s*\{)([^}]*)\}",
                 lambda m: m.group(1) + re.sub(r"(?<=[\s{])([A-Z])(?=\s)", r"\1.", m.group(2)) + "}", bib)
    # year ranges in titles get an en dash (1998-2022 -> 1998--2022)
    bib = re.sub(r"((?<![a-z])title\s*=\s*\{[^\n]*?\d{4})-(\d{4})", r"\1--\2", bib)
    if "International Conference on Learning Representations" in bib:  # OpenReview gives volume = year
        bib = re.sub(r"\s*volume\s*=\s*\{\d{4}\},?", "", bib)
    return re.sub(r"(pages\s*=\s*\{\s*\d+)\s*[–—-]+\s*(\d+)", r"\1--\2", bib)


def main(src):
    bibs, rows = [], []
    for line in Path(src).read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        key, ident = line.split()[:2]
        kind, val = ident.split(":", 1)
        try:
            bib, title, year, url = {"doi": doi_entry, "arxiv": arxiv_entry, "bib": bib_entry,
                                     "manual": manual_entry}[kind](key, val)
            bibs.append(tidy(retitle(key, bib)))
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
