# Pre-release repository audit (before the v1.0 Zenodo archive)

Audited: `main` at `c1a5193` (in sync with `origin/main`, 46 commits), plus the working tree as found on
2026-10-13 from 14:26 to about 14:45 IST. During the audit another session was changing the working tree: it
regenerated `results/numbers.tex` and the figures, added a `genlen` job and `paper/build.ps1`, and edited
`main.tex`. Each finding below says whether it applies to HEAD, to the working tree, or to both. The audit
edited no file except this report.

**Checks that passed:** `py_compile` on all 12 `code/*.py`. Self-tests: `features.py` printed "features ok",
`mso.py` printed "mso ok", and every `fmt` assert in `make_numbers.py` passed (imported, `main()` not called).
`make_numbers.missing()` returns `[]`. Every job name in `run_all.ps1` exists in the `jobs` dict, and every
script's argv matches its call. Every README number matches `numbers.tex`: 131,448; 9.2; 25.4 (23.2–27.7); 7.5;
ρ 0.83 with n = 18; 2.3 vs 4.2; 63.7 vs 8.0. The ORCID checksum is valid. The GitHub repo is public, and the
MIT licence is detected. The Hansard Zenodo record (17351233, CC BY 4.0, `corpus_1998_to_2025.parquet`), the
PERSUADE repo, and the licences of the HF datasets `liamdugan/raid` (MIT) and `WxWx/ChatGPT-Detector-Bias`
(MIT) were all confirmed. No secrets or API tokens were found.

---

## BLOCKING (fix before tagging v1.0)

### B1. The committed paper shows a stale "No dash features" result
`results/numbers.tex` at HEAD was last generated in `0a878f5`. That was before `f344b02` re-ran the dash
ablation with the encoding fix. As a result, Table 2's row "No dash features" reads **25.4 (23.2–27.7)**,
which is identical to the primary row: it is the pre-fix value. Regenerating from the committed CSV/JSON gives
**26.1 (23.9–28.3)**. Of the 255 `\R{}` keys used in `main.tex`, these 3 are the only ones that differ. In
total, 264 entries of `numbers.tex` are stale, all `arxiv_nodash_*`. Both `paper/main.pdf` and
`paper/preprint.pdf` (built 14:25) still print 25.4. Round 4 had asked for "re-run `nodash` and
`make_numbers`" (`round4_verification.md` M1). Only the first step was done.
- *State:* the working tree's `numbers.tex` (14:36) now matches a fresh regeneration byte for byte, but it is
  uncommitted and the PDFs are older than it.
- **Fix:** `powershell -File paper\build.ps1`. Check that the PDF row reads `26.1 | 23.9–28.3`. Then commit
  `results/numbers.tex`. To stop this recurring, add the assert round 4 suggested to `nodash()` in
  `code/analysis.py`, after the `EXCLUDE` line:
  `assert "pun:\u2014".startswith(mso.EXCLUDE) and "pun:\u2013".startswith(mso.EXCLUDE)`.

### B2. Release-relevant work is uncommitted or untracked
`git status` lists:
- **Modified:** `code/analysis.py` (new `generator_lengths`/`genlen` job), `code/figures.py`, all 5 figure PDFs,
  `paper/main.tex` (preprint switch and named author block), `results/numbers.tex`.
- **Untracked:** `paper/preprint.tex`, `paper/build.ps1`, `results/arxiv_generator_lengths.csv`,
  `paper/reviews/prerelease_*.md`.

A tag on the current HEAD would archive the stale numbers, with no named-preprint build and no build script.
- **Fix:** once the other pre-release sessions finish, commit everything as AI-written commits, then tag.
  Also add `"genlen"` to the analysis loop in `code/run_all.ps1`. It needs `llm_arxiv_old` and should go after
  `"vintage"`. Otherwise `results/arxiv_generator_lengths.csv` (if the paper cites it) is not produced by the
  documented pipeline. Then run `make_numbers.missing()` again.

### B3. The disclosure promises an author read-through "before release"
- `paper/AI_DISCLOSURE.md`: "The author will read the final paper before release; this line will be updated, in
  a `HUMAN-EDIT:` commit, when that is done."
- `main.tex` l. 604: "the human author(s) will read the final paper before release".
- `PLAN.md`: lists "Final read-through by the author" *before* "Release v1.0 … Zenodo".

A DOI archive of v1.0 that still says this is a permanent, self-contradicting record.
- **Fix (either):**
  - (a) The author reads the paper first and records it in a `HUMAN-EDIT:` commit that updates the
    `AI_DISCLOSURE.md` line and the paper sentence (e.g. "The author read the final paper on 2026-10-DD; edits,
    if any, are `HUMAN-EDIT:` commits; citations were not checked by a human").
  - (b) Reword both places to "The author has not yet read the final paper; this archive (v1.0) predates that
    read-through", and reorder `PLAN.md`.

---

## IMPORTANT (fix before release if at all possible)

### I1. README reproduction steps do not say where the downloaded files go
`build_sources.py` and `analysis.py` expect exact names under `DATA` that the README never gives. Add this to
the README "Download first" bullet:

| Put at `DATA\…` | From |
|---|---|
| `hansard_au\corpus_1998_to_2025.parquet` | Zenodo record 17351233 |
| `learner\persuade_2.0_train.csv` | PERSUADE 2.0 training CSV (Google Drive link in the corpus README) |
| `learner\liang_toefl_all_data.json` | `all_data.json` from HF `WxWx/ChatGPT-Detector-Bias` |
| `learner\liang_us8th.json` | `Data_and_Results/Human_Data/HewlettStudentEssay_real_88/data.json` from the authors' GitHub repo |

The pipeline is also Windows-only (`py` launcher, PowerShell, `curl.exe` in `fetch_raid.py`). Say so in one
line.

### I2. Dependencies are not pinned, and one listed package is unused
- `pymupdf` is in the README install line, but no code imports it (it was used only by review sessions).
  Remove it.
- No versions are pinned. Add `requirements.txt` with the versions that produced the results (from `.venv`,
  Python 3.12.10): pandas 3.0.6, pyarrow 26.0.0, numpy 2.5.4, scipy 1.18.1, scikit-learn 1.9.1,
  statsmodels 0.15.0, spacy 3.8.16 (+ en_core_web_sm 3.8.0), matplotlib 3.11.2, transformers 5.19.0,
  torch 2.14.1 (CPU), sentence-transformers 6.1.0. The best route is `.venv\Scripts\pip freeze > requirements.txt`.
- Change the README install line to `pip install -r requirements.txt`.
- Also record the Ollama version and the model digests (`ollama list`) in the README. Fixed seeds do not make
  the output identical across Ollama versions or hardware.

### I3. `run_all.ps1 -Stage paper` overwrites the verified bibliography
The `paper` stage runs `fetch_bib.py`, which re-downloads every entry from Crossref, arXiv and venues and
rewrites `paper/references.bib` and `lit/CITATIONS.md`. That is not deterministic. A failed lookup is
silently dropped from the .bib (only flagged in CITATIONS.md), so a reader who runs the documented pipeline
can undo the two-pass citation verification. The stage also builds only the anonymous `main.tex`.
- **Fix:** remove the "bibliography" step from the default `paper` stage, or move it to an opt-in `-Stage bib`.
  Replace the compile step with `& (Join-Path $root "paper\build.ps1")`.

### I4. The results cannot be reproduced from public sources alone, and the README implies they can
The README says "the scripts rebuild them from public sources". In fact:
- The arXiv API sample drifts: new versions, withdrawals, and window contents that change.
- The Claude Opus 5.5 texts cannot be regenerated (no decoding control).
- Ollama outputs change with version and hardware.
- `vintage()` uses the v1 sample `DATA\arxiv\sample.jsonl`, which the current `fetch_arxiv.py` does not
  produce.

The LLM files are small: `llm_arxiv.jsonl` 4.4 MB, `llm_arxiv_old.jsonl` 2.6 MB, `llm_hansard.jsonl` 6.6 MB,
`llm_essay.jsonl` 7.3 MB.
- **Fix (recommended):** deposit a separate Zenodo *dataset* and link it with `isSupplementedBy`. Contents: the
  LLM generations, `arxiv_v2/sample.jsonl` and `arxiv/sample.jsonl` (arXiv metadata, CC0), and the
  RAID-derived files (MIT). Note that `llm_essay.jsonl` P2 rows are revisions of PERSUADE essays and fall under
  CC BY-NC-SA 4.0, so either deposit them under that licence or leave them out.
- **Minimum:** reword the README to "the scripts rebuild them from public sources; exact reproduction needs the
  generated texts and the arXiv sample, which are [archived at … / available on request]".

### I5. One commit carries no provenance label
`6675865 "Strip BOM"` (2026-10-12 14:34) has no "(AI-written)", no `Co-Authored-By` trailer and no
`HUMAN-EDIT:` prefix. It also did more than strip a BOM: it changed `code/analysis.py` (BOM),
`results/essay_ell_continuous.json` (BOM) and regenerated `results/numbers.tex` (+448/−65 lines). This
contradicts the claim in `AI_DISCLOSURE.md` and the README that AI-written commits say so and human edits are
`HUMAN-EDIT:` commits. History is public, so do not rewrite it.
- **Fix:** add a line under "How to audit it" in `AI_DISCLOSURE.md`: "One early commit (6675865, 'Strip BOM')
  lacks the label by mistake; it was made by the AI system and removed byte-order marks and regenerated
  `numbers.tex`." Change "made by the AI system" if that is not true.

### I6. README findings are stronger than the paper
- The ρ = 0.83 release-date/peak correlation is "exploratory and was chosen after a first one" (paper l. 454;
  prereg deviation 10a), but the README presents it as a headline. **Fix:** "...the later the turn
  (exploratory, chosen after a weaker first analysis: Spearman ρ = 0.83, n = 18)".
- "robust to trend specification, …" leaves out what the paper reports: the gap is smaller without the 2026
  model (22.2 pp) and without revision texts (17.9 pp). **Fix:** append "; smaller (18–22 pp) when the
  generators closest to human abstracts are left out".
- Fast-DetectGPT: the paper limits this result to "with GPT-2 small; larger scoring models … may not [miss
  it]". **Fix:** "...computed with GPT-2 small, does not see the shift (larger scoring models might)".
- "2026-model texts were produced from the prompt batches written by `claude_prompts.py`" is ambiguous, because
  the README also lists three 2026 *open* models. **Fix:** "The Claude Opus 5.5 ('2026 model') texts were…".

### I7. The licence for non-code content is unstated, and the paper's ethics wording does not match the repo
- `LICENSE` covers "code only", and the README says only "Code is MIT-licensed". The paper source, figures,
  `results/`, reviews and lit notes have no licence. A Zenodo record carries one licence.
- **Fix:** add to the README: "Paper text, figures, results and documentation: CC BY 4.0 (or MIT; author's
  choice). Results in `results/essay_*` are aggregate statistics computed from PERSUADE 2.0 (CC BY-NC-SA 4.0)."
- The Ethics Statement (`main.tex` l. 587) says PERSUADE's "share-alike terms apply to derived data we
  release". This repo releases no derived per-document data. Either release it (see I4) or reword to
  "...would apply to any derived data; we release only aggregate results".

### I8. Version identity is inconsistent
| Where | Says |
|---|---|
| `CITATION.cff` | `version: "v5"` |
| README | "preprint version v5" |
| `PLAN.md` | "Release v1.0" |

Once `.zenodo.json` exists, Zenodo ignores `CITATION.cff` completely (help.zenodo.org, "Zenodo JSON file").
GitHub's "Cite this repository" still uses `CITATION.cff`, so the two must agree.
- **Fix in `CITATION.cff`:**
  - `version: "v1.0"`
  - `date-released:` set to the actual tag date
  - replace `message:` with `"If you use this code or these results, please cite it as below."`; the current
    message says "cite the paper as below" but there is no `preferred-citation` block
  - optionally add
    ```yaml
    preferred-citation:
      type: unpublished
      title: "Sounding Like Which AI? Machine-Style Overlap of arXiv Abstracts with Language Models of Different Vintages"
      authors:
        - family-names: Chhabra
          given-names: Natik
          orcid: "https://orcid.org/0009-0004-8786-7703"
      year: 2026
      notes: "Preprint, version v5"
    ```
  - after Zenodo mints the DOI, add `doi:` (concept DOI) in a follow-up commit
- **Fix in the README:** "**Status:** release v1.0 (paper version v5); preprint, not peer reviewed".

### I9. No PDF in the archive
`.gitignore` has `paper/*.pdf`. The Zenodo GitHub integration archives the tag's source zip only, so the DOI
record would contain no readable paper and need Tectonic to view.
- **Fix:** after B1, `git add -f paper/preprint.pdf`, or add `!paper/preprint.pdf` to `.gitignore`. The named
  preprint is the right one to archive. Keep `main.pdf` (anonymous review build) out.
- Add to the README: "Named preprint: `paper/preprint.pdf` (`tectonic paper/preprint.tex`); anonymous review
  build: `main.tex`; `paper/build.ps1` rebuilds numbers, figures and both PDFs."

### I10. The paper's deviations appendix does not match the named preprint and the prereg
- `main.tex` l. 743: "(the commit will be identified after review)". In the named preprint, wrap it:
  `\ifdefined\PREPRINT (commit \texttt{ef4fa21}, 2026-10-12)\else (the commit will be identified after review)\fi`.
- Paper item (5) places *both* cleaning fixes after review round 2. Prereg deviations 9 and 10a place the
  second one in round 3. Move "keyword lines, word-count notes and inline labels" into item (5b).
- The dash-ablation bug fix (prereg 10a) is missing from the paper appendix. Add it to (5b).

### I11. `python analysis.py DATA all` runs jobs in a broken order
`all` runs the jobs in dict order:
- `vpeak` runs before `vquarter`, so it reads last run's `arxiv_vintage_quarterly.csv`, or crashes on a clean
  `results/`.
- `vmarkers` re-runs work already done.
- `genlen` and `robust4` come before jobs they do not need, which is harmless.

The docstring advertises `all`.
- **Fix:** delete `or "all"` from the module docstring and the `for j in (jobs if which == "all" …)` branch.
  Make `run_all.ps1` the only full-pipeline entry point.

---

## MINOR / NITS

1. **Hard-coded absolute paths** (they break for anyone else):
   - every `code/queues/*.ps1` uses `F:\downloads\Outreach and other plans\research-paper\…` and
     `F:\research-data`. Historical, so fine.
   - `code/queues/run_v4.ps1:4` calls `C:\Users\<user>\AppData\Local\Temp\claude\…\scratchpad\invalidate_title.py`.
     That script (feature-cache invalidation after the "Title:" cleaning fix) is not in the repo, so "the
     exact batches used" is not fully true. Add a comment in `run_v4.ps1` or a sentence in the README, and
     ideally add the script as `code/queues/invalidate_title.py`. The path also exposes the Windows username.
   - `paper/build.ps1` (new) falls back to `F:\tools\tectonic\tectonic.exe`. Fine as a fallback; mention
     "tectonic on PATH".
   - `run_all.ps1` usage comment says `-Data F:\research-data` but the README says `D:\research-data`. Pick one,
     e.g. `C:\data\mso`.
2. **Orphan result files** that no current code produces and the paper does not use:
   - `results/selftest.json` and `results/arxiv_selftest_{features_human_typical,features_llm_typical,instrument,lomo,separability}.*`,
     from the dropped self-test (`02bde27`)
   - the 11 `results/arxiv_nofrontier_*` files (`81cb700`, v2; no job writes `_nofrontier` any more)

   Delete them, or add "results from earlier versions, kept for the record" to the README.
3. **Leftover/debug code:**
   - `analysis.py:517` has a `# ponytail:` tool-convention comment. Reword to `# note:`.
   - `analysis.py:901`'s comment says "escapes", but the line uses literal dash characters. Write
     `"pun:\u2014", "pun:\u2013"` to match.
   - `analysis.py` module docstring says "All tables and figures"; the figures are in `figures.py`.
   - `analysis.py:424` `WORD = …` is glued to the previous function (missing blank lines).
   - `perplexity.py:14`: a stray `import os` after the third-party imports.
   - `fetch_bib.py:27`: a duplicate `import html` inside `bib_entry`.
   - `figures.py` catches `FileNotFoundError` and prints "skip", so the "figures" step can never fail.
     Acceptable, but `build.ps1` users should look for "skip" in the output.
4. **`lit/verification/_v5_*_input.md`:** keeping them is reasonable and useful. They are the exact inputs the
   verifier sessions saw (paper sentence + title + link), so a reader can check what was verified. Rename
   without the leading underscore (e.g. `v5_batch1_input.md`) or add a one-line `lit/verification/README.md`
   saying so. The inputs for batches 1–3 of the first pass were not kept (they sit in
   `F:\research-data\_old_in*.md`); add them, or say so.
5. **`paper/reviews/RESPONSE_PLAN.md`:** every box is unticked although the work was done. Add a header line:
   "historical plan; boxes were not updated".
6. **`lit/CITATIONS.md` header:** says the author "opens every link … and ticks the box". No box is ticked,
   consistent with "author has not checked citations". Leave it, or append "(not yet done; see
   AI_DISCLOSURE.md)".
7. **`preregistration.md`:**
   - deviation "10a" is listed before "10". Renumber 10a→10 and 10→11, and so on.
   - the header now says "approved by the author", while the original commit `ef4fa21` said "verified by the
     author". It is outside sections 1–6, so not a violation, but the deviation log could mention it.
   - **Consistent with the git log:** ef4fa21 07:53 before the first result (cff4c35 09:08, f7b53b9 10:48);
     EVAL fixed in 50e2a17 (verified: `EVAL = 2025-06` in that commit); fd8a23b 15:32, f586d6c 15:35,
     c11d3ce 15:37; the 0.66/0.22/0.83 values match `arxiv_vintage_release_corr.json` and
     `arxiv_vintage_peak.json`.
8. **"The git history is the complete record"** (README and AI_DISCLOSURE.md): some steps lived only in the data
   folder: the invalidation script, cache backups, and the first-pass verification inputs. Soften to "the
   complete record of changes to the files in this repository".
9. **Personal data:** the named preprint's author block says "Independent researcher, Bilaspur, India"
   (author's choice; the city is optional). `lit/04_data_venues.md` lists the PERSUADE and ELLIPSE test-zip
   passwords. These are published in the corpora's own READMEs, so this is harmless. Nothing else sensitive was
   found. File sizes are fine (largest tracked file: `numbers.tex`, 1.1 MB).
10. **`main.tex` AI section** in the named preprint says "the human author(s)". Fine in the review build; in the
    preprint, "the author" reads better (`\ifdefined\PREPRINT`).
11. **`PLAN.md` "Remaining":** tick the release item after tagging, and add "deposit generated texts (I4)" if
    adopted.
12. **`CITATION.cff` is valid against cff 1.2.0:** the required `cff-version`, `message`, `title`, `authors` are
    present; the ORCID is a URL; `license: MIT` is valid SPDX; `date-released` is a valid date. Only the
    content issues in I8 remain.

---

## Proposed `.zenodo.json` (repository root)

Field names were checked against Zenodo's deposit-metadata documentation (developers.zenodo.org,
"Representation → Deposit metadata") and the GitHub help page (help.zenodo.org/docs/github/describe-software/zenodo-json).
Every top-level key is in the documented list. Every `relation` is in the allowed vocabulary. Creators use only
`name` / `orcid` / `affiliation`. The JSON parses.

```json
{
  "upload_type": "software",
  "title": "Sounding Like Which AI? Machine-Style Overlap of arXiv Abstracts with Language Models of Different Vintages: code, results and paper source",
  "version": "v1.0",
  "creators": [
    {
      "name": "Chhabra, Natik",
      "orcid": "0009-0004-8786-7703",
      "affiliation": "Independent researcher"
    }
  ],
  "description": "<p>Code, analysis outputs, LaTeX source and audit trail for the preprint <em>Sounding Like Which AI? Machine-Style Overlap of arXiv Abstracts with Language Models of Different Vintages</em> (paper version v5, not peer reviewed).</p><p>Studies of LLM-assisted writing estimate how much text was produced with LLM help. This study asks how much writing, whoever wrote it, falls on the LLM side of a stylistic boundary, and which LLMs define that side. It defines <strong>Machine-Style Overlap</strong> (MSO): the share of documents that a calibrated classifier on content-word-free style features judges at least as likely to be LLM output as pre-ChatGPT human writing. In 131,448 arXiv abstracts (2015&ndash;2026), MSO was 9.2% before ChatGPT and by June 2025 stood 25.4 percentage points (95% CI 23.2&ndash;27.7) above its pre-ChatGPT trend, far beyond placebo and instrument-drift gaps. Against generators whose pretraining data predate ChatGPT, the gap is smaller but clear (7.5 points). Against one generator at a time, overlap rises and then turns down, and the later a generator was released, the later the turn (exploratory rank correlation 0.83 across 18 generators); under the newest generators it peaked in 2026 or was still rising. A reference set that is not refreshed, like a fixed list of marker words such as <em>delve</em>, will eventually show the shift receding. In student essays, English learners' writing is less machine-like than their peers', even under a GPT-2 perplexity instrument that reproduces a published bias against TOEFL essays.</p><p><strong>Contents.</strong> <code>code/</code>: data pipeline and every analysis (<code>run_all.ps1</code> runs it in order; <code>queues/</code> keeps the exact batches used). <code>results/</code>: every table the analyses write; <code>numbers.tex</code> inserts each result into the paper. <code>paper/</code>: manuscript source, figures, AI disclosure, simulated review rounds. <code>preregistration.md</code>: analysis plan committed before any result, with the full deviation log. <code>lit/</code>: literature notes and citation-verification reports. Raw and intermediate data are not included; the scripts rebuild them from public sources (arXiv API; Australian Hansard, doi:10.5281/zenodo.17351233; PERSUADE 2.0; the essays of Liang et al. 2023; RAID).</p><p><strong>AI use.</strong> The study was carried out by an AI system (Claude Opus 5.5, Anthropic, used as an agent through Claude Code) under the author's direction: it wrote the code, ran the analyses and drafted the text. The author chose the topic and constraints and is responsible for the content. No AI system is listed as a creator. Details are in <code>paper/AI_DISCLOSURE.md</code> and in the git history (AI-written commits are labelled; human edits are commits starting <code>HUMAN-EDIT:</code>).</p>",
  "access_right": "open",
  "license": "mit",
  "language": "eng",
  "keywords": [
    "machine-style overlap",
    "LLM-generated text",
    "stylometry",
    "scientific writing",
    "arXiv",
    "computational linguistics",
    "AI-assisted writing",
    "AI-conducted research"
  ],
  "related_identifiers": [
    {"identifier": "10.5281/zenodo.17351233", "relation": "references", "resource_type": "dataset"},
    {"identifier": "10.1016/j.asw.2024.100865", "relation": "references", "resource_type": "publication-article"},
    {"identifier": "10.1016/j.patter.2023.100779", "relation": "references", "resource_type": "publication-article"},
    {"identifier": "10.18653/v1/2024.acl-long.674", "relation": "references", "resource_type": "publication-conferencepaper"}
  ],
  "notes": "AI authorship disclosure: the code, analyses and all text of this release (paper, README, analysis plan, reviews) were produced by Claude Opus 5.5 (Anthropic) acting as an agent under the author's direction; simulated peer review and citation verification were done by separate sessions of the same model family, and citations have not been checked by a human. See paper/AI_DISCLOSURE.md. Licences: code is MIT (LICENSE). Each dataset keeps its own licence (arXiv metadata CC0; Australian Hansard CC BY 4.0; PERSUADE 2.0 CC BY-NC-SA 4.0; RAID and the Hugging Face release of Liang et al. 2023 MIT); no third-party texts are redistributed here."
}
```

**Notes on the fields:**
- **`upload_type: software`, no `publication_type`.** The archive is a code-and-results repository.
  `publication_type` is valid only when `upload_type` is `publication`, and the GitHub integration is meant for
  software records. If a citable *paper* record is wanted, upload `preprint.pdf` manually as a separate record
  (`upload_type: publication`, `publication_type: preprint`). Link the two with `isSupplementedBy` /
  `isSupplementTo` in a v1.0.1 `.zenodo.json`. Do not add placeholder identifiers now.
- **`license: "mit"`.** Lowercase, as in Zenodo's own `.zenodo.json` example. A record holds one licence, so
  state the licence of the non-code files in the README (I7) and in `notes`. If the README adopts CC BY 4.0 for
  the paper, add that to `notes`.
- **`orcid`** takes the bare iD, not the URL (unlike `CITATION.cff`). Checksum verified.
- **`version: "v1.0"`** overrides the tag name. Keep the tag `v1.0` so the two match.
- **AI authorship.** Zenodo has no AI-contribution field. Disclose in `description` and `notes`, as above.
  Do **not** add Claude to `creators`: it would be listed as an author, against ACL/arXiv/COPE policy and the
  repo's own disclosure. Listing it under `contributors` (type `Other`) would be valid schema, but it reads as
  credit and is unnecessary. Prefer the notes.
- **Do not add:**
  - `publication_date` (defaults to the release date)
  - the GitHub URL as a related identifier (Zenodo adds `isSupplementTo` to the tag automatically)
  - `communities`, unless a community has agreed
  - the `type` key inside creators, which appears in the help-page example but is not in the documented
    deposit schema
- **Precedence.** With `.zenodo.json` present, Zenodo ignores `CITATION.cff`. Keep the two consistent (title,
  author, version, licence), as I8 requires.
- **Before tagging:** enable the repository at zenodo.org/account/settings/github, and commit `.zenodo.json`
  first. The tag must contain it.
