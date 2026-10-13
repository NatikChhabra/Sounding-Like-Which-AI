# Pre-release numbers-and-claims audit (final)

Scope: every typed number, count, ordering, superlative or quantifier in `paper/main.tex`, the direction of every
comparative claim built on `\R{}` values, abstract/contributions/discussion/conclusion against the body, Figure 2 and
Table 2 against `results/`, and the preregistration and AI disclosure against the appendix and AI Use section.

How it was checked: `numbers.tex` was regenerated in memory with `code/make_numbers.py` logic and compared with the
committed file. `main.tex` was rendered with every `\R{}` replaced by its printed value. Typed claims were then checked
against `results/*.csv|json`, `code/analysis.py`, `code/mso.py`, `code/figures.py`, `code/generate.py` and
`code/claude_prompts.py`. Nothing outside this report was edited.

---

## A. WRONG (fix before release)

### W1. Table 2 "No dash features" row shows stale, pre-fix values (line 404)
- `results/numbers.tex` (written 09:20) is older than the dash-ablation re-run (`arxiv_nodash_*`, written 09:48 to
  09:50, after the encoding fix in commit f344b02). Regenerating gives 266 changed entries, all `arxiv_nodash_*`.
  Three of them are printed in the paper:
  - `arxiv_nodash_its.all.excess`: printed **25.4**, the current result is **26.1**.
  - `excess_lo`: printed **23.2**, the current result is **23.9**.
  - `excess_hi`: printed **27.7**, the current result is **28.3**.
- The printed values match the primary row exactly (25.4, 23.2 to 27.7), as you would expect from an ablation that
  removed almost nothing.
- **Fix:** run `python code/make_numbers.py`, then recompile `main.tex` and `preprint.tex`. Table 2 then reads
  26.1 (23.9 to 28.3). The text range on lines 352 to 353 (23.5 to 29.1) still holds.
- This also matters for the AI Use claim (line 604) that every number is inserted from the analysis outputs. That is
  true of the mechanism, but the current PDF does not match the current outputs.

### W2. Abstract (lines 41 to 42) and Discussion (line 539): "under the newest generators ... it peaked in 2026 or was still rising"
- Gemma 4 was released 2026-06 and is the second-newest open model. Its peak was **2025Q4**
  (`arxiv_vintage_quarterly.csv`), and the body itself calls it "the clearest exception" (line 458).
- The claim holds for 3 of the 4 generators from 2026: Qwen3.5 (2026Q1), Granite 4.2 (2026Q2) and the 2026 model
  (still rising in 2026Q3).
- **Fix (abstract):** "under three of the four 2026 generators, including two open models run with logged decoding,
  it peaked in 2026 or was still rising."
- **Fix (line 539):** "under three of the four newest it peaked in 2026 or was still rising."

### W3. Lines 473 to 475: "The three 2026 open models, run with logged decoding, rose with the 2026 model (28.9% to 34.9%)"
- On its own, Gemma 4 **fell**: -0.9 pp, CI -1.8 to 0.1. Only the pooled `open2026_p1` region rose (28.9 to 34.9).
- **Fix:** "A region pooling the three 2026 open models, run with logged decoding, also rose (28.9% to 34.9% on annual
  means), so ..."

### W4. Lines 436 to 437: the variant descriptions are wrong
- `arxiv_vintage.pre2022data` (8.6 pp) and `pre2022data_plus_chatgpt` (7.4 pp) are **RAID-only** sets. In
  `analysis.vintage_sets`, `raid_pre` contains RAID GPT-4 and Llama-2-70B-chat only, and
  n_llm = 10,596 = 3,532 + 7,064. Neither set contains Llama-2-Chat 7B or Vicuna 7B, and both keep the summary-style
  outputs.
- The text presents each one as a one-change variant of the matched region.
- **Fix:** "Variants agree: the RAID models alone with summary-style outputs kept (8.6 pp), the same with RAID ChatGPT
  added (7.4 pp), or only the two small local models ... (3.5 pp ...)."

### W5. Appendix deviation (5), line 760: the second cleaning fix is attributed to the wrong review round
- The appendix places both cleaning fixes "after the second review".
- `preregistration.md` item 9 (round 2) contains only the "Title:" line fix. Item 10a (round 3) contains the second
  fix (keyword lines, word-count notes, inline labels). The git log agrees: cde9132 is the Title fix, and 0a878f5 is
  "Paper v4 after review round 3: second cleaning fix".
- **Fix:** in (5), write "a cleaning fix (whole "Title:" lines in LLM outputs are now dropped), after which every
  analysis was re-run". In (5b), add "a second cleaning fix (keyword lines, word-count notes and inline labels), with
  a full re-run; a fix to the dash-ablation feature names (re-run); field-specific detection rates".

### W6. Universal "later generator, later peak" statements are stronger than the body (lines 82 to 83, 449, 478 to 479, 561 to 562; Fig. 2 caption line 490)
- The body reports a rank correlation of 0.83 and names an exception. The ordering is not monotone:
  - Gemma 4 (2026-06) peaked in 2025Q4, before gpt-oss (2025-08), which peaked in 2026Q2.
  - Vicuna (2023-08) peaked in 2024Q3, before RAID GPT-4 (2023-06), which peaked in 2025Q2.
  - Mistral 7B v0.3 (2024-05) peaked in 2025Q3, after Phi-4 (2024-12), which peaked in 2025Q2.
- **Fix:** use "tends to" (as the Discussion already does on line 539):
  - line 82: "overlap with each generator tends to peak later the more recent the generator";
  - line 449: "the turning point tends to come later for later generators";
  - line 478: "Because overlap tends to turn down later the more recent the generator";
  - line 561: "Overlap with each generator tended to peak later the more recent the generator";
  - caption line 490: "Overlap with later generators tends to peak later."

### W7. Line 84 (contribution 5) and line 501: mined markers "rise with its style region until 2025" / "behave like their style regions until 2025"
- Every generator's mined-marker share rose from 2022 to 2025. That part is verified.
- Cohere's style region, however, **fell**: 10.3% to 9.3%, while its markers rose from 31.7% to 39.8%. Line 448 says
  so itself.
- **Fix (line 84):** "marker words mined from each generator rise until 2025, and most fall in 2026".
- **Fix (line 501):** "behave like their style regions until 2025 (except Cohere's, whose style overlap did not rise):
  ..."

---

## B. IMPRECISE (minor; recommended)

| # | Line | Statement | Finding | Fix |
|---|---|---|---|---|
| M1 | 457 to 458 | "Peak quarters of flat-topped series (Gemma 3, Granite 3.3) are unstable" | Qwen3 is flatter than either: 22.7 / 22.8 / 22.9 in 2025Q2 to Q4, a 0.2 pp spread, yet it is cited as a 2025Q4 peak on line 451. Llama 3.1 (23.1 / 23.7 / 23.6) and Mistral (23.8 / 24.2 / 23.7) are also flat-topped. | "(Gemma 3, Granite 3.3, Qwen3)" |
| M2 | 186 to 187 | Never-revised restriction "leaves yearly MSO unchanged" | 2025 and 2026 match (40.7 vs 40.6, 44.7 vs 44.7). However, 2022 is 10.5 vs 11.1 and 2024 is 27.0 vs 27.8 (`robustness_v5.never_revised`). | "leaves 2025 and 2026 MSO unchanged (and moves 2022 and 2024 by under 1 pp)" |
| M3 | 554 | "Every instrument we tried flags non-learner essays more often" | Verified for style logreg (2.3 vs 4.2), embeddings (5.3 vs 10.0), Qwen perplexity (7.1 vs 15.6) and GPT-2 perplexity (15.5 vs 30.6). No ELL breakdown exists for the essay GBM instrument or the LOMO instruments. | "All four instruments we report flag ..." |
| M4 | 468 to 469 | "only Granite shows a clear rise against a fall" | True only from 2025Q4. On annual means, Qwen3.5 rose +2.4 pp (CI 1.3 to 3.3) while Qwen3 fell -3.7 pp. | Start the sentence "Measured from 2025Q4, only Granite ..." |
| M5 | 747 to 751 | Liang essays "are used only for the perplexity replication" | The next sentence reports style-instrument results on them (34.1 / 5.7 / 51.4%). | "used only for out-of-genre checks" |
| M6 | 743 to 765 | Deviation appendix vs `preregistration.md` | Missing from the appendix: the per-generator cap of 450 (prereg 8, a round-1 change; line 208 presents it without a note; the `mso.py` comment "(pre-registered)" contradicts the prereg); RAID restricted to chat models with base models analysed separately (prereg 3); Hansard speaker-id bug fix (prereg 5); the essay pilot run (prereg 6); event study, implied prevalence, revision-overlap check and length-standardised baselines (prereg 9, all used in the body); field-specific detection rates (prereg 10a, used at line 388). | Add these to (4), (5) and (5b), or add one line: "the full list is in preregistration.md". |
| M7 | 743 to 744 (preprint build) | "the commit will be identified after review" | The preprint is not anonymous. The commit is ef4fa21, dated 2026-10-12. | Under `\PREPRINT`, name ef4fa21. |

---

## C. CANNOT VERIFY from the authors' files

| # | Line | Statement | Note |
|---|---|---|---|
| C1 | 240 to 242, 458, 472 | Qwen3.5 released 2026-Q1; Gemma 4 released 2026-06 with a Jan 2025 cutoff; Granite 4.2 released 2026-08 | These match `analysis.RELEASE` (2026.17, 2026.42, 2026.65) and the figure. They are external facts I cannot check offline. |
| C2 | 570 | "older models write shorter abstracts" | No result file contains generator output lengths. |
| C3 | 429 to 430, 700 | Instruction-tuning data of the 2023 models; GPT-2 training data predating the TOEFL essays' release | External. Both are hedged in the text. |
| C4 | 194 | Hansard "January 2015 to July 2025" | `hansard_monthly.csv` starts in 2015-02, probably because Parliament has no January sittings. The data directory is not in the repository. |
| C5 | 222 to 224 | RAID snapshot names (gpt-4-0613, gpt-3.5-turbo-0613) | Not recorded in the results. They match the code comment. |

---

## D. VERIFIED

### Typed numbers, counts and orderings
| Line | Claim | Source and check |
|---|---|---|
| 70, 76 to 77 | 19 generators, 2023 to 2026; 4 with pre-ChatGPT data (GPT-4, Llama-2-70B-chat, Llama-2-Chat 7B, Vicuna); 4 from 2026 (Qwen3.5, Gemma 4, Granite 4.2, Claude) | `arxiv_vintage_summary.n_single` = 19; `RELEASE` |
| 78 to 80 | More in cs than math; placebo and drift gaps "about a quarter as large or smaller" | Max placebo 3.2 pp (5.8 pp at 30 months), max drift 6.5 pp. 6.5 / 25.4 = 0.26 and 5.8 / 25.4 = 0.23 |
| 89 to 91 | H1 to H5 wording | Matches `preregistration.md` §2 |
| 177 to 180 | 8 archives; Jan 2015 to Sep 2026; up to 200 per field-month | `arxiv_monthly_by_field.csv` runs 2015-01 to 2026-09 with max n = 200; `corpus_stats.arxiv_n_fields` = 8 |
| 180 to 181 | Economics small, more so in early years | Econ n: 25 (2015) to 248 (2021), against about 800 to 1,000 for large fields |
| 194 | Up to 150 speeches per month | `hansard_monthly.n` max = 150 |
| 196 | Grades 6 to 12 | `essay_mso_by_group` grade groups 6-8, 9-10, 11-12 |
| 201, 572 | 3 prompt styles × 150; single regions use 150 texts (450 for RAID) | `corpus_stats.arxiv_n_llm_local` = 3,600 = 8 × 450; n_llm = 150; `PER_MODEL` = 450 cap |
| 204 to 205 | Temperature 0.8, fixed seeds; batches of 50 prompts | `generate.py` L43; `claude_prompts.py` `batch=50` |
| 207 to 211 | 6 RAID models; 14 generators capped at 450; 5 further models (2 old, 3 from 2026, paired with 2025 families Gemma 3, Granite 3.3, Qwen3); Hansard and essays use 7 local + 2026 model | `arxiv_instrument.n_generators` = 14; `hansard/essay_instrument.n_generators` = 8; `mso.PER_MODEL` |
| Table 1 | Release months: Mistral v0.3 2024-05, Llama 3.1 2024-07, Phi-4 2024-12, Gemma 3 2025-03, Granite 3.3 and Qwen3 2025-04, gpt-oss 2025-08, Llama-2-Chat 2023-07, Vicuna 2023-08 | Consistent with `analysis.RELEASE` and the figure's year colours. Cutoffs (GPT-4 Sep 2021, Llama 2 Sep 2022, Llama 3.1 Dec 2023, Phi-4 Jun 2024, Gemma 3 Aug 2024, gpt-oss Jun 2024) match the developers' published statements as far as I know. |
| 262, 268, 270, 281, 285 to 288 | 250-word cap; 1% feature filter; C = 0.1, isotonic calibration; Newey-West with 6 lags; 12-month blocks; placebo grid Jun 2016 to Dec 2021 every 2 months, evaluated +12; drift gaps 41 to 65 months | `features.MAX_WORDS`, `mso._mask`, `mso.make_model`, `analysis.segmented`, `block_bootstrap`, `placebo_grid` |
| 301 | 20 mined words, smoothed log ratio | `mined_markers(k=20)` |
| 326 to 327 | MTLD is the top LLM-typical feature; human side shows conj, amod, mean sentence length | `arxiv_features_*_typical.csv` |
| 345 | Yearly MSO min in 2016 (7.3) and max in 2020 (10.2) over 2015 to 2021 | `arxiv_yearly.csv` |
| 347 to 348 | Monthly series roughly flat since late 2025 | Oct 2025 to Sep 2026 values lie between 42.0 and 48.0 |
| 352 to 353 | Range 23.5 (threshold 0.6) to 29.1 (no math) | All threshold, sample and trend rows of Table 2 fall in this range (including the corrected dash row, 26.1) |
| 356 to 359 | MTLD is the strongest feature (coefficient 1.30); ablation range 22.9 to 26.6 | `arxiv_ablation.csv` |
| 361 to 363 | 600 abstracts per year; Fast-DetectGPT rate does not rise; GPT-2 small | `arxiv_fastdetect.csv` (all n = 600; post-2022 values 11.0, 10.3, 7.3, 5.3); `fastdetect()` uses `gpt2` |
| 364 to 368 | 34 breaks, 8.8%, 3.2 pp; 30-month version 8.3%, 5.8 pp | `robustness_v3`, `robustness_v5` |
| 369 to 372 | Three drift gaps; the positive one is the 2016 instrument; 65 months; two-year trend; "about a quarter" | 6.5 / 25.4 = 26% |
| 373 | Residuals within ±1 pp through 2022 | `arxiv_event.csv` max \|resid\| = 0.60 pp |
| 375 to 379 | cs largest, q-bio second; math smallest, astro-ph second smallest; all 8 Holm p < 0.001 | `arxiv_its` fields; `robustness_v3.field_holm` max = 1.9e-10 |
| 385 | 17.5% and 4.9% (Liang et al., Feb 2024, abstract sentences) | `lit/verification/batch6_v3.md` |
| 385 to 386 | Implied shares are larger, same ordering | 42.1 > 17.5 and 7.8 > 4.9 |
| 389 to 390 | Lower math TPR raises the implied math share | α = (MSO − FPR) / (TPR − FPR) |
| 439 to 440 | "Three quarters" of training texts from RAID | Cap of 450 each: RAID 900 of 1,200 |
| 447 to 448 | Rose 2022 to 2025 under every generator except Cohere | Cohere -0.9 pp; all others positive |
| 450 to 452 | Peak quarters: 2023 models 2024Q3 to 2025Q2; 2024 models 2025Q2 to Q3; Gemma 3, Granite 3.3, Qwen3 2025Q4; gpt-oss, Qwen3.5, Granite 4.2 2026Q1 to Q2; 2026 model rising in 2026Q3 | `arxiv_vintage_quarterly.csv`; `peak` equals the argmax for all 19 |
| 453 to 454 | ρ = 0.83, n = 18, p < 0.001; 2026 model excluded | Recomputed independently: 0.8267, p = 2.3e-5 |
| 455 to 457 | 0.66 annual, 0.22 (p = 0.375) from 2025Q4; computed first | `arxiv_vintage_release_corr`; prereg 10a |
| 459 to 462 | 15 of 19 fell; gpt-oss, Qwen3.5, Granite 4.2 and the 2026 model rose | `arxiv_vintage_summary` |
| 463 to 466 | Every bootstrap CI excludes 0 and all 5 seeds share a sign, except Gemma 4 (4 of 5 seeds; CI -1.8 to 0.1) | `arxiv_vintage_uncertainty.csv` |
| 467 to 468 | From 2025Q4 only gpt-oss (+3.9), Granite 4.2 (+2.9) and the 2026 model (+7.2) rose; Qwen3.5 flat (+0.4) | `change_q4` |
| 468 to 469 | The newer model fared better in all 3 family pairs | Gemma, Granite and Qwen, both annually and from Q4 |
| 472 | gpt-oss peaked late, Gemma 4 peaked early | 2026Q2 and 2025Q4 |
| 477 to 478 | 14-generator series rose in 2026; 12 of 14 single regions fell; carried by gpt-oss and the 2026 model | Of the 14 main generators, only gpt-oss and Claude rose. `arxiv_gensets.no_frontier` fell from 37.9 to 36.8. |
| 496 to 497; Fig. 1c | Published-marker share peaks in 2024 | `arxiv_yearly.marker`: 2024 = 5.33 is the maximum |
| 501 to 507 | Mined markers rose 2022 to 2025 for every generator; fell for 17 of 19, including gpt-oss and Qwen3.5; rose only for Granite 4.2 and the 2026 model | `arxiv_vintage.csv` m2022, m2025, m2026 |
| 508 | The 2026 model's words include substantial, comparable, implications, whose | `arxiv_vintage_its.json` |
| 540 | "including two whose style overlap kept rising" | `n_style_rose_marker_fell` = 2 |
| 567 to 569 | Four generators from 2026; pre-ChatGPT-data region has 4 generators, 3 on Llama 2 | `RELEASE`; `PRE2022_DATA` + `OLD` |
| 575 | Two of the eight fields are physics | astro-ph, cond-mat |
| 580 | 2022 change of government about six months before ChatGPT | Election 21 May 2022; ChatGPT 30 Nov 2022 |
| 652 | Hansard nonparametric gap -3.2 to 3.1 across specifications | `robustness_v4.hansard_pretrend` min and max |
| 663 | Dispersion "falls steadily" | `arxiv_dispersion.csv` decreases every year |
| 665 | 1,200 per year | `arxiv_len150_dispersion.n` |
| 669 | "about three years" | 0.358 / 0.108 = 3.3 years of trend |
| 680 | Lower and p < 0.05 in all 10 draws | `essay_seed_stability`: share_seeds_p_below_05 = 1.0, n_seeds = 10 |
| 752 | 2026-model texts merged two minutes after the preliminary run | prereg 7: 15:35 f586d6c, then 15:37 c11d3ce |
| 758 | "other 16 generators" | 19 − 3 |

### Direction of comparative `\R{}` claims (all correct)
| Claim | Values |
|---|---|
| Gap smaller vs pre-ChatGPT-data generators | 7.5 < 25.4 |
| Smaller without the 2026 model / without P2 | 22.2 and 17.9 < 25.4 |
| 2026 model hard to recognise | Recall 20.7%, against 59.6 to 95.6% for the others |
| Pre-ChatGPT-data region 2022 → 2024 → 2025 rise, then fall in 2026 | 6.5 → 15.5 → 17.9 → 11.9 |
| Region vs local_p1 | 7.5 vs 20.3 |
| arXiv exceeds Hansard | By 30.7 (CI 28.3 to 33.2) |
| ELL lower | 2.3 vs 4.2; OR 0.55 → 0.87 |
| TOEFL vs 8th grade | 63.7 vs 8.0; Qwen 41.8 vs 3.4 |
| Learner essays less predictable | log-ppl 3.74 vs 3.43 |
| logreg ≈ gbm | 22.8 vs 22.6 |
| Kappa moderate / low | 0.64 / 0.26, 0.29 |
| Hansard relative gap far below arXiv | 0.22 vs 2.09; logit 0.21 vs 1.47 |
| Never-revised 2025 and 2026 | 40.7 vs 40.6; 44.7 vs 44.7 |
| Fast-DetectGPT not rising | 8.3 → 11.3 → 5.3 |
| Marker vs MSO overlap | r = 0.12; 5.9 vs 1.4 |
| Dispersion gap CI spans 0 | -0.36 to 0.51 |
| Baseline astro-ph lowest, econ highest; no-math ordering similar | 4.4 to 15.3; no-math 5.75 to 15.9, cs and stat next in both |

### Figures and Table 2
- **Fig. 2(b):** `figures.py` draws the peaks from `arxiv_vintage_quarterly.csv` and the ρ label from
  `arxiv_vintage_peak.json`. `vintage.pdf` (09:54) is newer than both input files (09:20). There are 18 filled points
  plus 1 open circle (the 2026 model, peak 2026Q3, the last quarter).
- **Fig. 2(a):** draws from `arxiv_vintage.csv`. The sets are pre2022data_matched, raid_all, local_p1, gpt-oss,
  open2026_p1 and frontier_p1.
- **Table 2:** every row matches its result file **except "No dash features" (W1)**. The placebo rows are evaluated
  in June 2022 (`placebo()`, `drift_placebo`). The drift-to-2018 row comes from `arxiv_drift_placebo.json`.

### Preregistration and AI disclosure vs paper
- **Appendix deviations:** (1), (2), (3), (6) and (7) agree with prereg items 1, 2, 7, 10, 11 and 12. Item (5)
  disagrees on the cleaning-fix round (W5). Several prereg items are omitted (M6).
- **`AI_DISCLOSURE.md` vs the AI Use section:** they agree on all of the following:
  - the human's role and the approvals;
  - the AI's role;
  - the 2026-model texts coming from the same system, in batches of 50 with no decoding control;
  - simulated review by the same model family;
  - two citation-verification passes, one removed citation, and published versions replacing preprints;
  - citations not checked by a human, with the human reading the paper before release;
  - numbers inserted automatically, with a few counts typed;
  - no AI author.
- Minor omissions in the paper section, none of them contradictions: "no budget"; the AI's literature search and data
  collection; approval of downloads and public actions.
