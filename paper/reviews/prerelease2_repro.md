# Pre-release audit 2: reproducibility from the public repository

Auditor: AI reproducibility check (Claude Opus 5.5), 2026-10-13. Fresh clone of
https://github.com/NatikChhabra/Sounding-Like-Which-AI-.git at `5f285c4` in a scratch folder. Packages from the
existing venv (linked into the clone as `.venv` with a directory junction, removed afterwards; nothing installed).
`F:\research-data` was used read-only: analysis jobs ran through a wrapper that asserted no feature cache would be
appended to, and the sizes and mtimes of every `*.jsonl`/`*.parquet` in the data folder were identical before and
after. Nothing in the working repository was changed except this file.

## Summary

| Check | Result |
|---|---|
| `code/features.py` self-test | pass (`features ok 35 features in doc 1`) |
| `make_numbers.py` asserts + rebuild | asserts pass; output deterministic across runs; **but differs from the committed `results/numbers.tex` (F1)** |
| Re-run `vsummary`, `vpeak`, `genlen`, `control`, `robust3` in the clone | all 14 result files rewritten, **byte-identical** to the committed ones (`git diff --stat results/` empty) |
| `analysis.py` writes to the clone | yes: `OUT = <clone>\results` (checked at run time) |
| `data/generated/*.gz` vs `F:\research-data\llm_*.jsonl` | all four **byte-identical** (same line counts and SHA-256) |
| `data/samples/*.csv.gz` vs data folder | ids, order, pools, dates, titles, fields all match (after the documented id mapping) |
| Paper build in the clone (`paper\build.ps1`) | builds; `missing keys: []`; no errors/overfull/undefined lines |
| Built `preprint.pdf` vs committed | extracted text identical (15 pages); every page renders pixel-identical at 100 dpi; bytes differ only through timestamps |
| Built `main.pdf` vs working-copy `main.pdf` | extracted text identical |
| Regenerated figures vs committed | render identical; bytes identical after stripping `CreationDate`/`ModDate`/`/ID` |
| README newcomer path | **blocked for the vintage analysis and the data export (F2)**; smaller gaps F3-F7 |

## Findings

### F1 (minor, fix before tagging): committed `results/numbers.tex` is stale
Running `make_numbers.py` in a fresh clone changes `results/numbers.tex`:
`results/numbers.tex | 744 ---` (744 deletions, 0 insertions). The deleted macros all come from results files that
commit `5f285c4` deleted but that were still present when `numbers.tex` was last generated:
`arxiv_nofrontier_*` (11 files, 522 lines), `arxiv_selftest_*` (5 files, 217 lines), `selftest.json` (5 lines).
`git log --diff-filter=D` confirms the 19 files were deleted in `5f285c4`. No `\R{}` key in `paper/*.tex` uses them,
so every number in the PDF is unaffected, and every surviving line is unchanged. The working copy has the same
stale file (`git status` clean there), so the paper was not rebuilt after the deletion.
Effect: every newcomer's first build dirties `git status`, and the "determinism" check fails.
**Fix:** run `paper\build.ps1` (or `python code\make_numbers.py`) in the working repo and commit the new
`results/numbers.tex` (md5 of the regenerated file in the clone: `0abfebde147d6d14692b1e42739ae19a`).

### F2 (major for a newcomer): the v1 arXiv sample (`DATA\arxiv\sample.jsonl`) is required but nothing creates it
- `analysis.py:446` (`source_texts`) reads `DATA\arxiv\sample.jsonl` to find the source abstracts of the original
  generators; `marker_series` then asserts that >= 90% of each set's sources are found.
- `export_data.py:19` reads `DATA\arxiv\sample.jsonl` unconditionally.
- `run_all.ps1` only runs `fetch_arxiv.py "$Data\arxiv_v2"`; the v1 sampler (an earlier version of
  `fetch_arxiv.py`) is not in the repository, and the release ships only ids (`data/samples/arxiv_sample_ids.csv.gz`).

Evidence: share of P1 source ids (version suffix stripped) that are in `human_arxiv.parquet` without the v1
sample: claude-opus-5.5 0.760, gemma3:12b 0.860, gpt-oss:20b 0.853, llama3.1:8b 0.820, mistral:7b 0.840,
qwen3:8b 0.800 (granite3.3 and phi4 1.000). Overall, 434 of 3,464 `llm_arxiv` source ids are only in the v1 sample.
So on a newcomer's machine `analysis.py DATA vintage` fails with
`AssertionError: only N of 150 sources found`, and with it `vsummary`, `vquarter`, `vpeak`, the vintage figure and
the headline "0.83, n = 18" result; the `paper` stage of `run_all.ps1` then crashes in `export_data.py`.
**Fix (smallest):** add an id mode to `fetch_arxiv.py` (arXiv API `id_list=`, 100 ids per request, 3 s apart)
that rebuilds `DATA\arxiv\sample.jsonl` (id, field, primary, published, title, abstract) from
`data/samples/arxiv_sample_ids.csv.gz`, and call it in the `data` stage of `run_all.ps1`. The same mode applied to
`arxiv_v2_sample_ids.csv.gz` also gives the exact v2 sample (see F3). Alternatively make `export_data.py` skip a
missing v1 file and state in the README that `vintage` needs it.

### F3 (moderate): re-fetching the arXiv sample by id is promised but not provided
README: "Re-fetching arXiv abstracts by id (`data/samples/`) returns their current version." No script fetches by id.
`fetch_arxiv.py` re-runs the stratified sampler (seeded windows, `random.Random(cell)` draws), which gives the same
ids only if the API returns exactly the same window listing as on 2026-10-12 (withdrawn papers, category changes or
API ordering changes alter the draw). It also takes many hours (1,128 field-months, 3 s per request), which the
README does not say. **Fix:** same id mode as F2; in the README, say "use `fetch_arxiv.py --ids
data\samples\arxiv_v2_sample_ids.csv.gz DATA\arxiv_v2` to get the exact sample; the sampler itself may differ".

### F4 (minor): spaCy model version not pinned
All features come from `en_core_web_sm`; the venv has `en_core_web_sm 3.8.0`, but README/requirements say only
`python -m spacy download en_core_web_sm`, which installs whatever is compatible at the time. A different model
version changes POS/dependency features and hence every number. **Fix:** in README and `requirements.txt`, pin
`python -m spacy download en_core_web_sm-3.8.0 --direct` (or add the wheel URL
`en_core_web_sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl`
to `requirements.txt`). Also note that `torch` in the venv is `2.14.1+cpu`; the plain `torch==2.14.1` pin is fine
on Windows (PyPI wheel is CPU), but say "CPU build used" for clarity.

### F5 (minor, documentation): Hansard `src_id` is not always a document id
`data/README.md` says `src_id` is "the human document a prompt was built from". In `llm_hansard.jsonl`
(3,630 rows), 2,167 rows from gemma3, gpt-oss, llama3.1, mistral and qwen3 carry speaker-style ids
(e.g. `hansard:Abbott1957`; 95% match a current `grp` value) and 113 rows have a null `src_id`; only 37% of distinct
Hansard source ids are current document ids. These generators also have 141-158 rows per prompt instead of 150, and
872 duplicated (src_id, model, prompt) triples. This is the documented deviation 5 of `preregistration.md` and was
raised in review rounds 2-3, so it is not new, but a data user cannot know it from the release. A side effect:
`revision_overlap` silently covers only 3 of 8 Hansard generators (claude, granite3.3, phi4; not cited in the paper).
**Fix:** add one sentence to `data/README.md` ("Hansard generations made before the identifier fix
(preregistration deviation 5) carry the speaker id, or no id (113 rows), in `src_id`; cells are not exactly 150").

### F6 (minor, documentation): id formats in `data/samples/` differ between files
`arxiv_split.csv.gz` ids are `arxiv:<id>` without version; `arxiv_*_sample_ids.csv.gz` ids are bare with a version
suffix (`1501.02046v1`). The mapping is exact (100% of split ids are in the v2 sample after
`"arxiv:" + id.removesuffix(vN)`; no duplicate keys), but undocumented. 402 Hansard rows have an empty `group`
(party unknown). **Fix:** one line each in `data/README.md`.

### F7 (cosmetic): builds are not byte-reproducible
Every build rewrites all five `paper/figures/*.pdf` and `paper/preprint.pdf` with new timestamps, so a rebuild
always dirties `git status` even when nothing changed (verified: content identical). Likewise the `paper` stage of
`run_all.ps1` re-gzips `data/generated/*.gz` with a new gzip mtime. **Fix (optional):**
`fig.savefig(..., metadata={"CreationDate": None})` in `figures.py`, `SOURCE_DATE_EPOCH` for tectonic, and
`gzip.GzipFile(..., mtime=0)` in `export_data.py`.

### Other notes (no action needed)
- `paper/build.ps1` falls back to `F:\tools\tectonic\tectonic.exe`; for anyone else tectonic must be on PATH, which
  the README's "compiles with Tectonic" covers. It also requires `.venv` at the repository root, as the README's
  venv commands create.
- `requirements.txt` covers every third-party import in `code/*.py` (matplotlib, numpy, pandas, pyarrow, sklearn,
  scipy, sentence_transformers, spacy, statsmodels, torch, transformers); installed versions match the pins exactly.
  Implicit downloads (HF models `Qwen/Qwen2.5-0.5B`, `gpt2`, `sentence-transformers/all-MiniLM-L6-v2`; RAID shards via
  `curl.exe`) happen automatically; the README could list them for offline users.
- The Ollama version (0.40.3) could not be confirmed from `ollama_serve.log`.
- `run_all.ps1` job order satisfies every file dependency checked (`control` after `gensets`/`hansard`,
  `vpeak` after `vquarter`, `robust3`/`robust4` after `arxiv`).

## Commands used (in the clone)
```
python code/features.py
python code/make_numbers.py                       # twice; identical md5 both times
python analysis.py F:\research-data vsummary|vpeak|control|genlen|robust3   (via read-only guard wrapper)
git diff --stat results/                          # empty after restoring numbers.tex
powershell -File paper\build.ps1                  # 12 s; missing keys: []
pymupdf text extraction + per-page pixmap comparison of committed vs built PDFs
```
