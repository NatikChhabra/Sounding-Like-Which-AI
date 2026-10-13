# Pre-release audit round 7: final verification

Commit checked: `602d151` (fresh clone of the public repository). I edited no project file except this report and
pushed nothing. Clone, logs, renders and scripts are in the session scratchpad. This is an AI check; no human has
reviewed it.

Note: while this check ran, `origin/main` (GitHub) and the local repository moved to `6f62a89` ("Pre-release audit
round 7 (part 1)"). Everything below refers to `602d151` unless marked. I ran only light checks on `6f62a89` (listed
at the end).

## Blocking

### B1. The pre-rewrite commits, including the withheld Hansard P2 revisions, are still public on GitHub
- The rewritten history is clean (see Verified). GitHub still serves the old, unreachable commits by SHA, though:
  - `https://github.com/NatikChhabra/Sounding-Like-Which-AI-/commit/<sha>` returns 200 for `5f285c4`, `a2372da`,
    `5720997` and `cde9132`, and also for the short SHA `5f285c4`. A made-up SHA returns 404.
  - `/raw/a2372da8f9a6440d7af535b754a205a8131adbc4/data/generated/llm_hansard.jsonl.gz` redirects (302) to
    raw.githubusercontent.com, which returns 200 with Content-Length 2,076,911. That is the file with 3,630 rows,
    1,202 of them P2 revisions of real speeches. `5f285c4` holds the same rows.
  - `cde9132` and the other old commits listed in `prerelease3_package.md` still contain the local Windows username.
- These SHAs are easy to find:
  - `paper/reviews/prerelease3_package.md` lines 22–23 (in HEAD) name `5f285c4` and `a2372da` as the commits that
    contain the 1,202 P2 rows.
  - The public Events API (`api.github.com/repos/NatikChhabra/Sounding-Like-Which-AI-/events`) lists the old SHAs
    in its PushEvents (`head 5f285c4…`, `before a2372da…`, `head 0795e4b…`).
- This contradicts the Ethics statement ("we do not release the LLM revisions of speeches (P2)") and the README and
  AI_DISCLOSURE accounts of the rewrite. Hansard is CC BY-NC-ND, and the purpose of the rewrite was to stop releasing
  these adaptations.
- Fix (owner only): ask GitHub Support to remove cached views and unreachable objects for this repository. The
  purge request recommended in `prerelease3_package.md` line 52 has evidently not taken effect. Alternatively,
  delete and recreate the repository. Once the purge is done, the old SHAs in the review files can stay as history,
  but see M5.

## Important

None.

## Minor

### M1. Figure 2a: the ChatGPT line still runs through the legend text
At 800 dpi on p. 8, the vertical line crosses "(incl. gpt-oss)" and "5.5)". Round 6 added `framealpha=1`
(`code/figures.py:154`). That has no effect because `legend.frameon` is `False` in rcParams (`figures.py:24`), so no
legend frame is drawn. Fix: pass `frameon=True, facecolor="white", edgecolor="none"`, as Figure 1 already does
(`figures.py:42–43`).

### M2. Figure 2b: label collisions remain (round-6 item M8)
The 2026 model's open circle still touches the top of the shortened "Granite 4.2" label. The ρ annotation
("… (n = 15)") runs past the right spine. Nothing is clipped. Fix: place the Granite 4.2 label below or to the left
of its point (for example offset `(3, -7)`, as for Gemma 4), and break the ρ line in two.

### M3. Appendix page 15: large blank gaps around "F Field results" (fixed in `6f62a89`)
In `preprint.pdf` and `main.pdf` at `602d151`, the left column of p. 15 has two large white gaps, above and below
the heading. The log shows 23 "Underfull \vbox … while \output is active" warnings. This is a regression from
`9542943`, whose page 15 is filled. The preprint also grew from 16 to 17 pages, with Figure 4 alone on p. 17. The
committed `preprint.pdf` at `6f62a89` no longer has the gaps.

### M4. "Changed nothing else" is slightly too strong (AI_DISCLOSURE.md lines 39–41; README lines 46–49)
Comparing the 53 old commits with the 53 new ones pair by pair:
- In the two rewritten commits (`5bfef10`, `2bc5f4f`), the rewrite deleted `data/generated/llm_hansard.jsonl.gz`
  outright. Those commits therefore lost the P1/P3 speech generations too, not only the P2 rows. The file reappears
  in `ee03728`.
- All other differences are the username redactions: `code/run_v4.ps1` and `code/queues/run_v4.ps1` in 8 commits,
  and `prerelease_repo.md` and `prerelease2_ethics.md` in 3 commits.

Suggested wording: "removed the speech-generation file from the two commits that held the revisions, and the
username from file paths; nothing else changed."

### M5. HEAD files cite 14 commit ids that are not in the public history
The files cite `5f285c4`, `a2372da`, `0795e4b`, `cde9132`, `1012d6b`, `0a878f5`, `74837a7`, `f344b02`, `67594ce`,
`74902b3`, `c1a5193`, `80e1355`, `c63ada2` and `0ec57b6`. They appear in `paper/reviews/*.md`,
`lit/verification/v6_changed_sentences.md` and the docstring of `code/queues/invalidate_changed.py`. All are
pre-rewrite ids. The README promises unchanged ids only for the paper and the analysis plan, which holds. A one-line
note in `paper/reviews/` would make this clear, for example: "review reports written before 2026-10-13 cite
pre-rewrite commit ids". After B1 is fixed, these ids will no longer resolve on GitHub.

### M6. CITATION.cff says `version: "v1.0"`, but no tag exists
The README says v1.0 "will be tagged after the author's read-through". This is harmless if the tag is created before
anyone cites the repository. Otherwise, drop the field until the tag exists.

## Verified

**1. History (fresh clone)**
- HEAD is `602d151`. The history has 55 commits, a single branch and no tags.
- No commit's `data/generated/llm_hansard.jsonl.gz` has a `"prompt": "P2"` row. The file exists from `ee03728` on,
  with 2,428 rows (P1 and P3 only) in all 7 commits that contain it.
- `data/generated/hansard_p2_rows.csv.gz` holds only `src_id, model, prompt` for 1,202 rows, with no text.
- "<user>" appears in none of the 1,009 blobs of any commit, checked case-insensitively. The check also covered
  gzip-decompressed files, decompressed PDF streams, PDF metadata and text, and PNG zTXt/iTXt chunks. It is also
  absent from path names, author and committer fields (all `NatikChhabra <…noreply.github.com>`) and every commit
  message.
- Every commit id cited in `paper/main.tex` (`ef4fa21`), `preregistration.md` (`ef4fa21`, `f586d6c`, `c11d3ce`,
  `50e2a17`, `01ef90f`, `fd8a23b`) and `paper/AI_DISCLOSURE.md` (`6675865`) exists in the history. README.md and
  PLAN.md cite no ids.
- These ids are also ancestors of the pre-rewrite head `5720997`, which is still in the local object store. So they
  are unchanged by the rewrite, as claimed.
- Times match the text:
  - `ef4fa21` is 2026-10-12 07:53 IST.
  - `f586d6c` (15:35:31) to `c11d3ce` (15:37:49) is "two minutes".
  - `f586d6c` to `01ef90f` (15:44:42, Claude abstracts merged) is "nine minutes".
  - `6675865` ("Strip BOM") is the only commit without "(AI-written)". There are 54 Co-Authored-By trailers and no
    HUMAN-EDIT commits.
- Pre-rewrite history: exactly two commits (`5f285c4`, `a2372da`) held the 1,202 P2 rows, as the README and
  AI_DISCLOSURE state.

**2. Build**
- `paper/build.ps1` in the clone (with the repo `.venv` linked) printed `missing keys: []`, rebuilt all 5 figures,
  `main.pdf` and `preprint.pdf`, and exited 0.
- These are identical to the committed files: `preprint.pdf` and the 5 figure PDFs byte for byte, and
  `results/numbers.tex` after line-ending normalisation (git blob hash equal). `git status` was clean.
  `main.pdf` is git-ignored.
- LaTeX log (`--keep-logs`, both documents):
  - 0 overfull boxes, 0 undefined references or citations, 0 multiply-defined labels, 0 "Missing character".
  - The BibTeX `.blg` has no warnings.
  - Other messages: underfull hboxes (85 in the body, 105 in the bibliography), 23 underfull vboxes (see M3), an
    `inputenc` "ignored with utf8 based engines" note, and a tectonic note about invalid UTF-8 in the bundled
    `lineno.sty`. None of these matter.

**3. Paper (all 17 pages of preprint.pdf read)**
- I checked every sentence changed in the round-6 commits (`git diff 9542943 602d151 -- paper/main.tex`; `7f5fc99`
  and `a2ddcae` are the post-rewrite ids of `5720997` and `fd61781`) against `results/`. All hold:
  - **Abstract:** 7.5 pp; 3.5 pp for `old_open_p1`, which is Llama-2-Chat 7B and Vicuna on P1. ρ = 0.79 with
    n = 18; 0.66 with n = 15. "Mostly rose then fell" holds for 17 of the 19 single regions; the 2026 model was
    still rising, and Cohere peaked in 2023Q2. "Essay scores explain most of this": the odds ratio goes from 0.55 to
    0.87 (about 77% of the log-odds) and the margin from −0.37 to −0.12.
  - **Intro (4) and (5):**
    - GPT-4's single-generator gap (11.4) is the largest in the pre-ChatGPT-data region (5.5, 3.7, 1.4).
    - Mined-marker shares fell for 17 of 19 generators (`arxiv_vintage_summary.json`).
  - **§6.3:**
    - The range 23.5–29.1 covers every threshold, sample and trend variant in Table 2. Gradient-boosted trees give
      29.5 (`robustness_v7.gbm_main`).
    - The family ablations give 22.9 (closed-class words) to 26.6 (POS trigrams). Dependencies (25.0), punctuation
      (25.7) and sentence statistics (25.4) fall inside the range.
  - **§6.4:**
    - Three quarters RAID: 900 of 1,200 capped training texts.
    - Every single region except Cohere's rose from 2022 to 2025.
    - Every region except the 2026 model fell from 2026Q2 to 2026Q3, both unweighted and field-weighted
      (`n_fell_last_quarter` = 18).
    - Bootstrap 0.64–0.86. Seeds 0.79–0.85. Equal sizes 0.73–0.84; without the three new models 0.66–0.77 and
      0.57–0.76. Permutation p = 0.010. Partial correlations 0.56 and 0.37.
    - `robustness_v8` caps every single region at 150, as described.
    - Gemma 4 and Granite 4.2 peaked before release, and Qwen3.5 in its release quarter.
    - Annual change: 15 of 19 fell, and the 4 that rose are named correctly. Every change except Gemma 4's is 5/5
      and 10/10 with a CI that excludes 0.
    - In all three same-family pairs the newer model's change was higher, and the Gemma intervals overlap.
    - The 14-generator series: 12 regions fell. Without the 2026 model, 37.9 → 36.8.
    - `local_p1` is "not a stable change": CI −0.3 to 1.9 pp, same sign in 2 of 5 seeds.
    - `old_open_all` 12.5. `gap_to_eval` 13.1, 7.6 and 22.7.
  - **§6.5:**
    - Mined shares rose from 2022 to 2025 for all 19 generators and fell in 2026 for 17. Only Granite 4.2
      (33.6 → 35.6) and the 2026 model (49.4 → 57.4) kept rising.
    - Marker peaks were earlier for 7 generators, later for 6 and the same for 5.
  - **§6.6:** "same eight generators" means the 7 local models plus the 2026 model. 32.1 − 1.3 = 30.8, reported as
    30.7 from unrounded values.
  - **Discussion:** 3 of the 4 2026 generators peaked in 2026 or were still rising.
  - **Conclusion:** the pre-ChatGPT-data region rose from 6.5% to 17.9%, against 11.1% to 40.6% overall.
  - **Limitations:**
    - Median lengths: 102–250 in the pre-ChatGPT-data region (GPT-4 110, Llama-2 7B 105). 90–134 for the other RAID
      models (ChatGPT 121, Cohere 129). 138.5–186 for the 10 local 2024–2026 models.
    - 17.9% of 2015 abstracts fall in the 2026 model's region, against a maximum of 8.3% for any other generator
      (Cohere).
  - **Table 1:** the vintage-only models have P1–P3 (150 each), but only P1 is used except in `old_open_all`, so
    "mainly P1" is right.
  - **Tables 4–5:** labels are consistent with Table 1. Table 5 is in release order. "Recurs" equals
    `peak_boot_share`. RAID seeds redraw the 450 texts (`mso.training_set` samples with `random_state=SEED`).
  - **Appendix A:** times match the git log (see 1).
  - **Appendix E:** the peak-quarter groupings are correct. From 2025Q4, only gpt-oss (+3.9), Granite 4.2 (+2.9),
    the 2026 model (+7.2) and Qwen3.5 (+0.43) rose.
  - **Appendix F:** 44.4% and 8.2%.
  - Newey–West uses `maxlags=6`. The relative gap is the excess divided by the trend.
  - Ethics: the 11,730 local texts are 3,150 arXiv + 2,250 vintage + 3,150 essays + 3,180 Hansard (2,128 released
    and 1,052 withheld local P2).
- The abstract is 197 words with \R values substituted (≤ 200).
- `main.pdf`: the Conclusion ends on p. 8 and Limitations starts on p. 9.
- `main.pdf` is anonymous:
  - It shows "Anonymous ACL submission", the human author is "author(s)", and Appendix A reads "the commit will be
    identified after review".
  - The text has none of Natik, Chhabra, NatikChhabra, ORCID, 0009-, Bilaspur, India, ef4fa21, the repo URL or
    <user>, and the raw bytes have none of these strings either.
  - The PDF metadata is empty.
  - No link annotation points to the author's GitHub. All links go to third-party DOIs, model cards and similar.

**4. Release metadata**
- README "Main findings": every number and claim matches the paper and `results/`:
  - 131,448; 9.2%; 25.4 (23.2–27.7); 22.2; 17.9; 7.5; 3.5; 12.5; 13.1; 22.7.
  - ρ 0.79 (0.79–0.85; 0.73–0.84), 0.84, 0.81, 0.82, 0.73, 0.66 with n = 15. "Chosen before the pattern was seen"
    matches Appendix A(5) and the round-6 review.
  - The Fast-DetectGPT flag rate falls after 2022: 11.3% → 5.3%.
  - 2.3% vs 4.2%; 63.7% vs 8.0%.
- `.zenodo.json` is valid JSON. Its creators, ORCID, licence description and AI-use note are consistent with the
  README and `data/README.md`.
- `CITATION.cff` is valid YAML and conforms to CFF 1.2.0. It has the required `cff-version`, `message`, `title` and
  `authors`. The licences are valid SPDX ids. `preferred-citation` has type `article`, status `preprint` and an
  integer `year`. The ORCID check digit is valid.
- The venv's Python is 3.12.10, as the README states.

**5. Figures and tables (pages 4, 6, 8, 14, 15, 16 and 17 rendered at 140 dpi; zooms at 400–800 dpi)**
- Table 1 and Tables 2–5: no clipping or overlap, and the values match the text and `results/`.
- Figure 1:
  - The legend's white frame hides the ChatGPT line.
  - Panel (c) peaks in 2024, as the caption says.
- Figure 2: the data match the CSVs:
  - Panel (a): the 2026 model starts at 17.9% in 2015 and ends at 39.2%. `local_p1` ends at 29.0%, the 2026 open
    models at 34.9% and gpt-oss at 38.5%.
  - Panel (b): all 19 peaks and the `RELEASE` dates match. The unlabelled green points are Gemma 3, Granite 3.3 and
    Qwen3.
  - Overlaps are listed under M1 and M2.
- Figure 3: n and the values match the text (astro-ph 4.4, econ 15.3; gaps for cs 38.1, q-bio 36.2, math 10.5,
  astro-ph 13.7).
- Figure 4: the values match Appendix I (2.3/4.2, 5.3/10.0, 15.5/30.6), as do the n values.

**Light checks on `6f62a89` (outside the requested scope)**
- Its diff from `602d151` contains no "<user>".
- The committed `preprint.pdf` has an abstract of 199 words, the Conclusion on p. 8 and the p. 15 gaps fixed.
- Figures are unchanged, so M1 and M2 persist.
- Not rebuilt.

## Counts
Blocking 1 · Important 0 · Minor 6
