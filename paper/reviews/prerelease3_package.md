# Pre-release audit 3: release package (data, licences, metadata, history)

Audited 2026-10-13 against commit `0795e4b` (= `origin/main` = public GitHub `HEAD`, checked with `git ls-remote`).
Method: fresh `git clone` of the local repository into a scratch folder; every check below ran on that clone.
The working data folder `F:\research-data` was only read. No project file was changed except this report.
Tools: the project `.venv` (pandas 3.0.6) and a scratch venv with `cffconvert` 2.0.0 and `pypdf`; `pdftotext`;
Zenodo's licence vocabulary API; the ORCID public API; the GitHub REST API (read-only).

Counts: **2 Blocking, 3 Important, 11 Minor**, plus a list of what was verified.

---

## Blocking

### B1. The withheld Hansard P2 revisions are still in the public git history
README.md ("the revisions of real speeches are not released"), data/README.md ("The P2 revisions of real speeches are
left out, as Hansard text may not be adapted"), the paper's Ethics Statement ("we do not release the LLM revisions of
speeches (P2)") and `.zenodo.json` all say these texts are not released. They are still public on GitHub in two commits:

| Commit (public) | File | Blob | Rows | P2 rows |
|---|---|---|---|---|
| [pre-rewrite commit] | `data/generated/llm_hansard.jsonl.gz` | `[removed blob]` | 3,630 | **1,202** |
| [pre-rewrite commit] | `data/generated/llm_hansard.jsonl.gz` | `[removed blob]` | 3,630 | **1,202** |
| `0795e4b` (HEAD) | same file | `f4dbfa60…` | 2,428 | 0 |

The 1,202 rows are by model llama3.1 156, qwen3 155, mistral 150, gpt-oss 150, claude-opus-5.5 150, phi4 150,
granite3.3 150 and gemma3 141, matching `hansard_p2_rows.csv.gz`. They are near-copies of the speeches, not loose
paraphrases: `results/revision_overlap.csv` shows the 2026 model keeping a median 26% of the source speech's word
6-grams (35% of its revisions keep more than 30%). No other file in the history holds third-party full texts: the old
`hansard_split`, `essay_split` and `arxiv_split` files have the same columns as now, and old `llm_essay` and `llm_arxiv`
texts are identical to the current ones. A Zenodo archive of a release tag holds only that tag's tree, so the DOI
record itself would be clean. The public GitHub repository is not. The repository is new (created 2026-10-13T08:08Z)
with 0 forks and 0 stars, so rewriting its history now costs little.

**Fix (author runs this; it rewrites history and force-pushes):**
```
# 1. Work in a fresh mirror, not in the working copy
git clone --mirror https://github.com/NatikChhabra/Sounding-Like-Which-AI-.git sl-mirror.git
cd sl-mirror.git
py -3.12 -m pip install git-filter-repo
printf '[removed blob]\n[removed blob]\n' > ../p2-blobs.txt
# optional, same pass: scrub the Windows username (see M9)
printf '<user>==>USER\n' > ../names.txt
git filter-repo --strip-blobs-with-ids ../p2-blobs.txt --replace-text ../names.txt
# 2. Check: no commit may contain a P2 row
for c in $(git rev-list --all); do git show $c:data/generated/llm_hansard.jsonl.gz 2>/dev/null | gzip -dc | grep -c '"prompt": *"P2"'; done | sort | uniq -c   # must print only 0s
git remote add origin https://github.com/NatikChhabra/Sounding-Like-Which-AI-.git
git push --force origin main
# 3. In the working copy: commit or stash local work first, then
git fetch origin && git reset --hard origin/main
```
Then ask GitHub Support to purge cached views of the old commits [pre-rewrite commit] and [pre-rewrite commit] (GitHub Docs, "Removing
sensitive data from a repository"). Until GitHub runs garbage collection, an old commit stays reachable by its full SHA.
Only [pre-rewrite commit], [pre-rewrite commit] and `0795e4b` get new SHAs. `6675865` and every hash cited in `paper/AI_DISCLOSURE.md` are
older and do not change. `paper/reviews/prerelease2_ethics.md` and `prerelease2_repro.md` cite [pre-rewrite commit], which will
no longer resolve.

The README says "The git history is the complete record of changes to the files". To keep that true, add to README.md
("How this was made") and to `paper/AI_DISCLOSURE.md` ("How to audit it"):
> On 2026-10-13 the public history was rewritten once to remove the LLM revisions of Hansard speeches (P2), which had
> been committed by mistake in two commits (the former [pre-rewrite commit] and [pre-rewrite commit]). No other content changed. Review
> reports written before the rewrite cite the old commit ids.

### B2. Release gate: no author read-through or HUMAN-EDIT commit yet
At `0795e4b` the release package says the author has not yet read or approved the paper. README: "pre-release draft:
not yet read or approved by the author … v1.0 will be tagged after the author's read-through". Paper Acknowledgements
(preprint p. 9): "the human author will read the final paper before release". AI_DISCLOSURE: "zero `HUMAN-EDIT:`
commits". `git log --all` confirms 0 commits containing `HUMAN-EDIT`. As long as nobody tags a release, these
statements are consistent. A GitHub release cut now would make Zenodo archive, under a permanent DOI, a paper whose
own text promises a read-through that has not happened, and the Acknowledgements sentence would become false.
**Fix:** do not create the GitHub release until PLAN.md "Remaining" items 1–4 are done. That means at least one
`HUMAN-EDIT:` commit recording the read-through, AI-use statements in the past tense in `main.tex`,
`AI_DISCLOSURE.md` and the README status line, a rebuilt `preprint.pdf`, and `date-released` set in `CITATION.cff`.
Re-run checks 4 and 6 of this report after that commit.

---

## Important

### I1. `.zenodo.json` gives the whole deposit one CC BY 4.0 licence, which over-grants rights
`"license": "cc-by-4.0"` is a valid Zenodo id, but Zenodo applies it to the whole deposit. The deposit-metadata docs
say the selected licence "applies to all files in this deposition", and the field is a single string. When
`.zenodo.json` exists, Zenodo uses only that file and ignores `CITATION.cff` (Zenodo docs, "zenodo.json"). The record
badge and the DataCite/OpenAIRE rights field would therefore say CC BY 4.0 for content that is CC BY-NC-SA 4.0
(`llm_essay.jsonl.gz`, `essay_split.csv.gz`), CC BY-NC 4.0 (`llm_hansard.jsonl.gz`), CC BY-NC-ND 4.0 Parliament of
Australia text (the Hansard opening sentences in `hansard_split.csv.gz`) and MIT (code). The sentence in the
description ("The record-level licence below applies only where no other licence is stated") does not carry over to
harvested metadata. GitHub separately labels the whole repository "MIT License" from `LICENSE`, but the README
corrects that on the same page.
**Fix (smallest):** in `.zenodo.json` replace
```
  "license": "cc-by-4.0",
```
with
```
  "license": "other-nc",
```
(`other-nc` = "Other (Non-Commercial)", confirmed as a valid id at `https://zenodo.org/api/vocabularies/licenses/other-nc`).
In the description, replace "The record-level licence below applies only where no other licence is stated." with
"The record is labelled non-commercial because some parts are; each part's own licence is listed above and in
data/README.md, and the code (MIT) and the paper and generated abstracts (CC BY 4.0) may be reused commercially."
Alternative: keep `cc-by-4.0` and move the NC/ND files (`llm_hansard`, `llm_essay`, `essay_split`, `hansard_split`)
into a separate Zenodo dataset record licensed `cc-by-nc-sa-4.0`/`cc-by-nc-nd-4.0`. That is cleaner but more work.

### I2. `code/export_data.py` crashes on a data folder rebuilt from the release (documented path), and the paper stage overwrites `data/`
Following the README ("unpack `data/generated/*.gz` into the data folder") leaves `llm_hansard.jsonl` with no P2 rows.
`export_data.py` then builds `pd.DataFrame([])[["src_id","model","prompt"]]` and raises
`KeyError: "None of [Index(['src_id', 'model', 'prompt'] …)] are in the [columns]"`. Reproduced in a scratch folder
with the four unpacked generation files and the three `human_*.parquet`. `run_all.ps1 -Stage paper` and the default
`all` call this step last, so the documented pipeline ends in `throw "export release data failed"`. The same step
writes into the repository's own `data/` folder, so a user who regenerated texts would silently overwrite the
committed release files.
**Fix** (`code/export_data.py`, replace the `gz_csv(pd.DataFrame(p2)…` line):
```python
    if p2:  # a data folder rebuilt from this release has no P2 rows; keep the committed list
        gz_csv(pd.DataFrame(p2)[["src_id", "model", "prompt"]], gen / "hansard_p2_rows.csv.gz")
```
In `code/run_all.ps1`, write the export to a scratch folder unless asked:
```powershell
    Step "export release data" { & $py export_data.py $Data (Join-Path $Data "release_export") }  # copy to data\ by hand to update the release
```
I checked that the export is byte-identical when run on the full working folder (see Verified), so neither change
affects the committed files.

### I3. Personal data beyond name and ORCID in permanently archived files
- `PLAN.md:35`: "Ask the EACL 2027 SRW chairs whether a secondary-school student may be first author". This
  publishes that the author is a secondary-school student, and may imply a minor, in a permanent Zenodo record.
- `paper/main.tex:23` and `paper/preprint.pdf` p. 1: "Independent researcher, Bilaspur, India" (city of residence).

It is the author's choice to publish these, but they should be deliberate, because a Zenodo version cannot be deleted.
The commit identity is already the GitHub noreply address (`213114435+NatikChhabra@users.noreply.github.com`, all 49
commits). That is good.
**Fix (if the author agrees):** in PLAN.md replace that line with `- [ ] Ask the EACL 2027 SRW chairs about
first-author eligibility (before 2026-11-06)`. In `main.tex` use `Independent researcher` (ACL needs an
affiliation, not a city), then rebuild. Doing this before B1's rewrite keeps the city out of the archived tag. It stays
in older commits unless it is also added to `names.txt`.

---

## Minor

**M1. 12 exact-duplicate generations in `llm_hansard.jsonl.gz`.** 24 rows form 12 identical pairs (same model,
prompt and text). All are P1 with no `src_id` (llama3.1 ×8, qwen3 ×2, gemma3 ×2; for example rows 11/750 and
17/751). They look like a queue re-run appending the same outputs. The working file has 17 such pairs (5 more among
the withheld P2 rows). No code de-duplicates them (`analysis.py` has no `drop_duplicates`), so they enter the Hansard
instrument twice. The effect on a secondary result is negligible. Fix: add to data/README.md Notes:
"`llm_hansard.jsonl.gz` contains 12 duplicated P1 rows without `src_id` (a queue re-run); they were analysed as they
are."

**M2. data/README says generations use unversioned arXiv ids, but 2,700 of 3,600 `llm_arxiv` rows are versioned.**
`src_id` ends in `vN` for claude-opus-5.5, gemma3, gpt-oss, llama3.1, mistral and qwen3 (450 each, for example
`arxiv:1810.07468v1`). It is unversioned for granite3.3, phi4 and all of `llm_arxiv_old`. The code strips versions
(`analysis.py:979`, `export_data.py:52`), so results are unaffected. Fix: in data/README.md replace "Split files and
generations use `arxiv:` plus the unversioned id." with "Split files, `llm_arxiv_old` and the seed-source file use
`arxiv:` plus the unversioned id; in `llm_arxiv` six models' `src_id` keep the version suffix (`v1`, …), which the
code strips before matching."

**M3. `CITATION.cff` licence list is incomplete and has no release date.** It validates against CFF 1.2.0
(`cffconvert --validate`: "valid according to schema version 1.2.0"). However, `license` lists MIT, CC-BY-4.0,
CC-BY-NC-4.0 and CC-BY-NC-SA-4.0 and omits CC0-1.0 (`hansard_p2_rows`, arXiv ids) and CC-BY-NC-ND-4.0 (Hansard opening
sentences). `date-released` is missing. Zenodo ignores this file (I1), but GitHub's "Cite this repository" uses it.
Fix: add `  - CC0-1.0` and `  - CC-BY-NC-ND-4.0` under `license:` and, at release, `date-released: "YYYY-MM-DD"`.
After the DOI exists, add `doi:` to `preferred-citation`.

**M4. README "against 22.1 pp for recent open models" is ambiguous.** 22.1 is `arxiv_vintage.local_p1.gap_nonparam`,
which the paper calls "the 2024–2025 open models". The 2026 open models give 21.7 (`open2026_p1.gap_nonparam`).
Fix: README "Main findings", bullet 2: "against 22.1 pp for open models released in 2024–2025".

**M5. Third-party LaTeX files are not covered by the licence statements.** `paper/acl.sty` (ACL style files),
`paper/acl_natbib.bst` (header: "Modifications Copyright 2002–23, Norman Gray, and distributed under the terms of the
LPPL") and `paper/acl_latex.tex` (the ACL template example, which no build file uses) would fall under README "Code:
MIT". Fix: delete `paper/acl_latex.tex` (`git rm paper/acl_latex.tex`) and add to README "Licences": "- `paper/acl.sty`
and `paper/acl_natbib.bst` are the ACL style files (github.com/acl-org/acl-style-files) under their own terms (the
`.bst` under the LPPL)."

**M6. PLAN.md points to a file that does not exist, and its audit glob is too narrow.** `lit/HUMAN_CITATION_CHECK.md` is
not in the repository; it is meant to be created by the author. "Five pre-release audit rounds
(`paper/reviews/prerelease_*.md`)" does not match `prerelease2_*.md` or `prerelease3_*.md`. Fix: "(`lit/HUMAN_CITATION_CHECK.md`,
to be created, `HUMAN-EDIT:` commit)" and "Pre-release audit rounds (`paper/reviews/prerelease*.md`)".

**M7. AI_DISCLOSURE says it and the paper "say the same thing", but it adds facts not in the paper.** These are
"gave standing permission for downloads and setup", "several of which the AI system made while working unattended
under an instruction to continue" and "approved making the repository public". There is no contradiction; the file
has more detail. Fix: replace the first sentence with "This file expands the paper's 'Acknowledgements: AI Use and
Authorship' section; if they ever conflict, the paper's section is authoritative."

**M8. README says "AI-written commits say so", but one does not.** `6675865` ("Strip BOM") has no "(AI-written)"
label and no `Co-Authored-By` trailer; the other 48 commits have both. AI_DISCLOSURE already reports this. Fix: README,
after "AI-written commits say so": "(one early commit, `6675865`, lacks the label; see the disclosure)". If B1's
rewrite runs anyway, this commit is not rewritten, so the note stays valid.

**M9. Windows username "<user>" in tracked files.**
- HEAD: `paper/reviews/prerelease_repo.md:211` and `paper/reviews/prerelease2_ethics.md:230`. Both quote the old
  path in an audit finding, and neither file contains a live path.
- History only: `code/run_v4.ps1` in `cde9132`, `1012d6b`, `0a878f5`, `74837a7` and `f344b02`;
  `code/queues/run_v4.ps1` in `67594ce`, `74902b3` and `c1a5193` (a `C:\Users\<user>\AppData\Local\Temp\claude\…`
  scratch path). HEAD's `code/queues/run_v4.ps1` is clean.

Other absolute paths are `F:\…` and contain no username (the `code/queues/*.ps1` records, the `paper/build.ps1`
tectonic fallback `F:\tools\tectonic`, and the README example `D:\research-data`). This is low sensitivity. Fix: the
optional `--replace-text` in B1 removes all occurrences. Without the rewrite, accept it.

**M10. Some released Hansard P1/P3 speeches quote the Hansard remark used in their prompt.** Of the 900 released rows
whose `src_id` is a speech id, 44 contain 8 or more consecutive words of that remark and 3 contain 15 or more (maximum
16), despite "Do not reuse the remark's wording". The 1,448 speaker-id rows cannot be mapped. These are short quotes
of public text, so the risk is low. Fix: data/README.md, `llm_hansard` row: append "; a few outputs quote up to 16
words of the prompt's opening sentence verbatim".

**M11. Reproduction instructions skip a necessary step.** "To reproduce the analyses exactly … unpack
`data/generated/*.gz` into the data folder" does not say to skip the `generate` stage. Running `run_all.ps1` with the
default `-Stage all` would call `generate.py`, which resumes and generates the missing Hansard P2 rows afresh (needs
Ollama). The data stage also builds `seed_arxiv.parquet` from the v2 sample, while six of the original generators were
seeded from the first sample, so regenerated arXiv texts would use different source documents. Fix: replace the README
sentence with "To reproduce the analyses exactly rather than regenerate the texts, unpack `data/generated/*.gz` (as
`llm_*.jsonl`) into the data folder and run the stages `data`, `perplexity`, `analysis` and `paper` one at a time,
not `generate` or `all`. Regenerating also needs the first arXiv sample (`data/samples/arxiv_sample_ids.csv.gz`,
`fetch_arxiv.py ids … "$Data\arxiv"`), which seeded six of the original generators."

---

## Verified (no defect)

**1. Files.** Every file named in README.md and data/README.md exists in the fresh clone. The only exceptions are
external downloads and the future `lit/HUMAN_CITATION_CHECK.md` (M6). All 11 files under `data/` are documented
(generated: 5, samples: 6).

**2. Data claims** (decompressed and counted):
- `llm_hansard.jsonl.gz`: 2,428 rows, prompts P1 1,217 / P3 1,211, **0 P2**. Columns `src_id, genre, model, prompt, text`.
- `hansard_p2_rows.csv.gz`: **1,202** rows, columns `src_id, model, prompt`, all P2; 150 rows are claude-opus-5.5.
- Speaker-id `src_id`: **2,167** in total (1,448 released + 719 withheld) ✓. Rows with no `src_id`: **113** (80 released + 33 withheld) ✓.
- `hansard_split.csv.gz`: 13,725 rows, **402** empty `group` (party) ✓. Opening sentences are at most 251 characters,
  none is a whole speech, and all are prefixes of the speech text up to whitespace.
- `arxiv_v1_seed_sources.jsonl.gz`: **434** rows (`id, title, abstract`) ✓. All 5,488 arXiv generation sources are
  covered by `arxiv_split` ∪ seed sources.
- `llm_arxiv` 3,600 (8 models × P1/P2/P3 × 150), `llm_arxiv_old` 2,250 (5 × 3 × 150), `llm_essay` 3,600. No empty
  texts.
- `arxiv_split` 131,448 rows (train 39,829 / score 91,619), all in the v2 sample. `essay_split` 14,797 (ELL 1,330).
  Every essay generation's `src_id` is in `essay_split`. `*_sample_ids` ids are all versioned and unique.
- The paper's "11,730 texts" of local generation = 3,150 + 2,250 + 3,150 + 3,180 ✓.

**3. Determinism.** `python code/export_data.py F:/research-data <scratch>`, run from `code/` with the project venv,
wrote 11 files, and all **11 are byte-identical** (`cmp`) to the committed `data/` files.

**4. Licence metadata.**
- `LICENSE` is MIT, scoped to code.
- `CITATION.cff` is valid CFF 1.2.0 (M3 aside).
- `.zenodo.json` parses, uses only valid legacy deposit keys (`creators, description, keywords, language, license,
  notes, title, upload_type`), `upload_type: software` is valid, `language: eng` is ISO 639-3, and `cc-by-4.0` is a
  valid id (`/api/vocabularies/licenses/cc-by-4.0`) but has the wrong scope (I1).
- ORCID `0009-0004-8786-7703` has a valid checksum (3) and resolves to Natik Chhabra. `version` is absent, so Zenodo
  takes it from the tag (fine).
- Licence statements agree across README.md, data/README.md, the Ethics Statement and the `.zenodo.json`
  description: arXiv CC0; Hansard CC BY-NC-ND 4.0 via Katz & Alexander CC BY 4.0; PERSUADE CC BY-NC-SA with
  share-alike on the essay data; RAID and Liang HF MIT; the US 8th-grade essays not redistributed; speech
  generations CC BY-NC without P2. Model licences check out: Gemma 4 12B, Qwen3.5 9B and Granite 4.2 8B are Apache 2.0
  on Hugging Face, consistent with "the others: Apache 2.0 or MIT".

**5. README numbers.** Every number in "Main findings" matches `results/numbers.tex` and the raw CSVs:

| README value | Source key |
|---|---|
| 131,448 | `corpus_stats.arxiv_n_docs` |
| 9.2 | `arxiv_baseline_pre2022.all.mso` |
| 25.4 (23.2–27.7) | `arxiv_its.all.excess` / `_lo` / `_hi` |
| 22.2 | `arxiv_gensets_its.no_frontier.excess` |
| 17.9 | `arxiv_vintage.all_no_revision.gap` |
| 7.5 | `arxiv_vintage.pre2022data_matched.gap` |
| 11.9 | `…gap_nonparam` |
| 22.1 | `arxiv_vintage.local_p1.gap_nonparam` (M4) |
| 0.79, n = 18 | `arxiv_vintage_peak.rho`, `.n` |
| 0.64–0.86 | `arxiv_vintage_peak_boot.rho_lo` / `_hi` |
| 2.3 vs 4.2 | `essay_mso_by_group` (ELL 0.0225 vs non-ELL 0.0420) |
| 63.7 vs 8.0 | `essay_liang_perplexity_gpt2` (TOEFL 0.637 vs US 8th 0.0795) |

`requirements.txt` pins match the installed venv (torch is the `+cpu` build of 2.14.1). `run_all.ps1` stages match the
README apart from M11. `analysis.py` handles a data folder without Hansard P2 rows (`revision_overlap` simply has no
Hansard rows).

**6. PDFs.**
- `paper/preprint.pdf` (tracked) is the current build. It is identical to the working-copy file; its abstract
  matches `main.tex` word for word, including "0.79, n = 18"; it has the heading "Acknowledgements: AI Use and
  Authorship"; and it contains sentences first added in `0795e4b` (for example "Instrument ageing can thus produce
  gaps", "which may flatter its held-in recall").
- `paper/main.pdf` is **not tracked** (`.gitignore`: `paper/*.pdf`, `!paper/preprint.pdf`) and never was in the
  history (only `preprint.pdf` and `paper/figures/*.pdf` were). The local copy is anonymous anyway: no
  "Chhabra"/"Natik"/ORCID/GitHub URL/"Bilaspur" in its text; its metadata has only `/Creator: LaTeX with hyperref`
  and `/Producer: xdvipdfmx`, with no `/Author` and no XMP.

**7. Secrets.** There are no API keys, tokens or passwords of the author's in tracked files. The only "password"
strings are the public test-ZIP passwords that the ELLIPSE and PERSUADE maintainers publish
(`lit/04_data_venues.md:52–53`). No e-mail addresses appear outside bibliographies.

**8. AI disclosure.** PLAN.md and `paper/AI_DISCLOSURE.md` agree with the paper's Acknowledgements on every point the
paper makes: topic, constraints and plan approval by the author; plan, code, analyses and all text by the AI system;
"no human has edited the text"; citations AI-checked in two passes and not by a human; the author takes
responsibility; no AI author. Both agree with the repository state (0 `HUMAN-EDIT:` commits). PLAN's "12 local open
models" (7 + 5) and "four rounds of simulated peer review" (round1–round4) are correct.
