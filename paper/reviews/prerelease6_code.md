# Pre-release audit 6: code review of the vintage analysis

Reviewer: statistician / Python reviewer (AI session). Commit reviewed: 0ec57b6.
Scope: `code/analysis.py` (`vintage_sets`, `vintage`, `vintage_quarterly`, `vintage_peak`, `robustness_v5`,
`robustness_v6`, `robustness_v7`, `segmented`, `nonparam_gap`, `RELEASE`, `PRETRAIN_CUTOFF`) and the parts of
`code/mso.py` they call (`training_set`, `fit`, `SEED`). Also checked: `generator_lengths` (feeds `vintage_peak`)
and the job order in `code/run_all.ps1`.

Method: line-by-line reading, then re-execution from a scratch copy of `code/` and `results/` (the repository and
`F:\research-data` were never written; the scratch `mso.cached_features` was patched to raise instead of appending to
the raw-data feature caches, and it never fired). Every check below was run on the real data, not on toy inputs,
except the two synthetic unit checks marked as such.

## Bugs that change a reported number

None found. Every vintage number the paper cites from `arxiv_vintage_quarterly`, `arxiv_vintage_peak`,
`arxiv_vintage_peak_boot`, `arxiv_vintage_release_corr`, `arxiv_vintage_uncertainty` (single regions),
`arxiv_generator_lengths`, `robustness_v6` and `robustness_v7` was reproduced exactly (byte-identical result files,
or agreement to 1e-16), and the independent re-implementations below agree with the code's outputs.

## Bugs that do not change a reported number

1. **`run_all.ps1` runs `vpeak` before `genlen`.** `vintage_peak` reads `results/arxiv_generator_lengths.csv`
   (analysis.py:581), which only `generator_lengths` (job `genlen`) writes, and `run_all.ps1:36` lists
   `"vquarter", "vpeak", "genlen"`. On an empty `results/` the pipeline stops with `FileNotFoundError`; on the
   committed `results/` `vpeak` silently uses whatever lengths file is already there (today that file is current:
   `genlen` re-run in scratch is byte-identical, so no number changes). Fix: put `"genlen"` before `"vpeak"`.

2. **`run_all.ps1` never runs `robust6` or `robust7`.** Both jobs exist in `jobs` (analysis.py:1111) but are absent
   from `run_all.ps1:35-36` and from every script in `code/queues/`, while the README says `run_all.ps1` "runs the
   pipeline in order". The paper cites 20 numbers from them (`robustness_v6.*`: 11; `robustness_v7.*`: 9: the
   training-draw range of rho, the length- and field-weighted rho, and the gradient-boosted-trees gap). The
   documented pipeline therefore does not regenerate them. Re-running both in scratch reproduces the committed files
   byte for byte, so the numbers are right. Fix: append `"robust6", "robust7"` after `"robust5"`. `robust6` needs
   `arxiv_monthly_by_field.csv` from `arxiv`; `robust7` has no file dependency.

3. **"Seeds" counts the estimate's own draw.** In `robustness_v5` the estimate is `ch[0]` (seed 0), and
   `n_seeds_same_sign = sum(sign(c) == sign(ch[0]) for c in ch)` (analysis.py:792) includes seed 0, so a 5/5 in
   Table `tab:peaks` means the estimate plus 4 agreeing redraws, and Gemma 4's 4/5 means 3 of 4 redraws agree. The
   caption says "draws of the human training sample (of 5) ... whose change has the same sign as the estimate",
   which suggests 5 independent checks. No number is wrong. Fix: either say "of 5, including the estimate's own draw"
   or count over seeds 1-4 ("of 4"). (`n_sub_same_sign` has no such issue: subsamples 0-9 are all refits.)

4. **"Draws of the human training sample" also redraw the generator texts for RAID regions.** `mso.training_set`
   caps each generator at `PER_MODEL=450` with `g.sample(..., random_state=SEED)` (mso.py:84). For the six RAID
   single regions (2,371-6,545 texts each) a new seed therefore draws a different 450 generator texts as well as a
   new human sample. For the local models (150 texts) the seed only permutes them. This applies to the seed columns
   of `arxiv_vintage_uncertainty` and to `robustness_v7.seeds.*` ("five draws of the human training sample", main
   text). The numbers are correct for what the code does. Fix the wording ("training draws (human sample and, for
   RAID, the 450 generator texts)"), or hold the generator sample at `random_state=0` while varying the human one.

5. **`CUTOFF` vs `T0` boundary on 30 November 2022.** "Pre-ChatGPT" is `date < 2022-11-30` (excludes 30 November)
   in `robustness_v7`'s length target `p_pre` and in `timeseries`' `pre`, but the monthly series and `segmented` put all
   of 2022-11 in the pre-period (`T0 = 2022-12`). 68 scored abstracts are dated 30 November 2022. This is negligible
   for the 10-word-bin target distribution (68 of the 2015-2022 scored documents), and no rounded number moves.
   Noted for consistency only.

## Risks (not bugs; the code does what it says)

- **Training size differs by vintage, and it moves the correlation.** Single regions use 150 human + 150 LLM texts
  for every local model but 450 + 450 for every RAID model (the `PER_MODEL` cap applied to a single generator), and
  all six RAID models are 2023 models. Pandas sampling is prefix-consistent (`RandomState.choice` without
  replacement takes a permutation prefix), so all 19 single regions share the same 150 human training abstracts, and
  the RAID regions add 300 more. Refitting only the six RAID regions at 150 + 150 (seed 0) moves three peaks
  (ChatGPT 2025Q1 to 2025Q2, MPT 2025Q1 to 2025Q2, Cohere 2023Q2 to 2023Q4). rho changes from 0.785 to 0.731, and
  rho without the 2026 open models from 0.662 to 0.567. 0.567 is below the reported training-draw range
  (0.66-0.77). The paper discloses the size difference ("Single-generator regions rest on 150 texts each (up to 450
  for RAID models), so instrument precision differs by vintage") but reports no size-matched correlation. A
  size-matched sensitivity (RAID capped at 150, five draws) would show whether the 15-generator correlation depends
  on it.
- **Spearman p-values are asymptotic.** `rho_no_new_p` (cited as 0.007) uses scipy's t-approximation with heavy ties
  (15 generators, 7 distinct peak quarters). A 200,000-draw permutation test gives p = 0.0088 (n = 15) and
  p = 0.0002 (n = 18). Both p-values also treat the estimated peaks as fixed and the generators as independent.
  The bootstrap and seed ranges partly address this, and the paper calls the analysis exploratory. Consider
  reporting the permutation p (0.009).
- **The partial correlation has no test.** It is computed correctly (see Verified). Under the usual t-test with
  n - 3 df, p = 0.020 (n = 18, partial 0.56) and p = 0.19 (n = 15, partial 0.37). This agrees with the paper's
  reading ("vintage and output length cannot be separated").
- **`peak_by_release` compares the quarter start with a day-level release date.** Qwen3.5 (released 2026.12, peak
  2026Q1) therefore counts as "peak by release" although most of its peak quarter follows its release. The paper
  states this case correctly ("Qwen3.5 in its release quarter"), and `n_peak_by_release` is not cited. Also, the
  RAID release months are approximate (documented in the Table 1 caption). `rho_raid_tied` covers this.
- **The peak bootstrap is conditional on the fitted instrument.** Training uncertainty enters only through the
  seed and subsample checks. This is correct as described in the paper. The human training pool (2015-2022-11-29)
  is disjoint from the 2023+ scored documents, so the conditional bootstrap is valid.
- Outside the listed functions, noticed in passing: (a) `mso.cv_auc` uses `make_model(kind)` with ungrouped inner
  calibration folds (`cv=5`), whereas `mso.fit` groups them. This affects the separability AUCs and
  `robustness_v5.tpr_by_field`, not the peaks. (b) `timeseries`' `length_adjusted` test bins raw
  `text.str.split()` lengths (LaTeX and wrappers included, no 250-word cap) into quintiles, unlike `robustness_v7`,
  which bins exactly what the classifier sees. (c) `mso.mso(..., seed=SEED)` binds the default seed at import, so it
  ignores later changes to `mso.SEED`. It is not used in the vintage path. (d) NaN MTLD is imputed as 0 by
  `nan_to_num`. This affects 1 human arXiv document.

## Verified

- **Seed 0 of `robustness_v7` reproduces `arxiv_vintage_quarterly.csv`.** All 19 single-region peaks agree
  (`arxiv_vintage_peak_checks.peak` = `arxiv_vintage_quarterly.peak`), and `robustness_v7.seed0`
  (rho 0.7851, 0.6616) equals `arxiv_vintage_peak` (rho, rho_no_new). A full scratch re-run of `robust7`
  (5 seeds + GBM) gave robustness_v7.json and arxiv_vintage_peak_checks.csv byte-identical to the committed files.
- **Quarterly series recomputed independently.** With `training_set`/`fit` at SEED 0 on the 2023+ scored abstracts,
  every `mso_YYYYQn` of all 19 regions matches the file to at most 9.7e-17. The annual 2025-to-2026 changes equal
  both `arxiv_vintage.y2026 - y2025` and `arxiv_vintage_uncertainty.change_seed0` for all 19 regions.
- **Scratch re-runs of the jobs are byte-identical to the committed files:** `vquarter` (`arxiv_vintage_quarterly.csv`,
  `arxiv_vintage_peak_boot.json`, `arxiv_vintage_release_corr.json`), `vpeak` (`arxiv_vintage_peak.json`), `robust6`
  (`robustness_v6.json`) and `genlen` (`arxiv_generator_lengths.csv`).
- **Joint document bootstrap.** It resamples within quarters with the same draws for every region, the quarters
  sort chronologically as strings, argmax and `idxmax` both take the first maximum, and the bootstrap rho on
  quarter indices equals the rho on decimal quarters (monotone map). Re-implemented: `peak_boot_share` matches
  exactly, and rho median/2.5%/97.5% = 0.777/0.641/0.863. `peak_boot_lo/hi` are the 10th/90th percentiles
  (`method="lower"/"higher"`), as the caption says ("80% range"). No bootstrap rho is NaN.
- **Spearman partial correlation is correct.** It is the Pearson correlation of OLS residuals of ranks on the rank
  of length, with ranks recomputed within each subset. It matches the closed form
  (r_xy - r_xz r_yz)/sqrt((1-r_xz^2)(1-r_yz^2)) on Spearman coefficients (0.558469 and 0.373796) and an lstsq
  re-implementation.
- **Other `vintage_peak` outputs.** rho, rho_no_new (and p), rho_no2023 (n = 10: `release >= 2024` drops the six
  RAID models plus Llama-2-7B and Vicuna), rho_raid_tied (all `raid-` set to 2023.5), rho_cutoff and
  rho_release_on_cutoff_set (n = 9), rho_length and rho_release_length all recomputed. Quarter-start or quarter-
  midpoint coding gives the same rho. NaN handling is right: only the 2026 model drops (no release month), and
  `n_fell_last_quarter` = 18/18 matches "fell under every other generator".
- **Length reweighting (`robustness_v7`).** It uses 10-word bins of `len(features.clean(t).split())` capped at 250,
  which is exactly the text the classifier sees (`features.extract` runs spaCy on `clean(t)`, cut to `MAX_WORDS=250`).
  The target is the pre-ChatGPT scored distribution, and the weights are `p_pre(b)/p_q(b)`. An independent
  post-stratification (bin means weighted by `p_pre`, renormalised over bins present) gives identical peaks for all
  19 regions and rho 0.8447 / 0.7462.
- **Field weighting.** `robustness_v7` uses an equal-weight mean over fields within each quarter (smallest
  field-quarter cell: econ, 180 abstracts). Re-implemented with identical peaks: rho 0.8143, and 18/18 fell in the
  last quarter. `robustness_v6`: weights renormalise over the fields present in each month, string-month
  comparison with `str(T0)` is safe for zero-padded "YYYY-MM", and the result is byte-identical.
- **Seeds 1-4 recomputed outside `robustness_v7`.** rho = 0.8410, 0.8259, 0.7955, 0.8469 and rho_no_new = 0.7468,
  0.7276, 0.6744, 0.7732, all equal to the file. `mso.SEED` is reset to 0 in a `finally` in both `robustness_v5` and
  `robustness_v7`. Scoring does not depend on `SEED`. The GBM fit after the loop uses `random_state=0`, and each job
  runs in its own process.
- **`robustness_v5` single regions.** Seed min/max and `n_seeds_same_sign` reproduce for all 19 regions from
  independently computed seed 1-4 hits. The 80% generator-subsample refits reproduce `sub_change_min/max` and
  `n_sub_same_sign`.
- **No leakage.** The train and score pools are disjoint (0 shared ids, no duplicate ids), and the train pool ends
  2022-11-29. Every local-model LLM source is a train-pool document (5,401) or a v1 source absent from the human
  table (449). None is a scored document. RAID sources are RAID's own abstracts. Calibration folds group each LLM text
  with its human source (`grp`).
- **Feature cache is current.** 1,000 random documents (400 single-region LLM texts, 300 scored and 300 training
  abstracts) re-extracted with the current `features.py` give features identical to the cached ones.
- **`segmented` / `nonparam_gap`.** Synthetic check: a series with a level shift of 0.02 and a slope change of
  0.003/month returns excess 0.10997 (truth 0.11), to-eval 0.10998, nonparametric 0.10245 (truth 0.1025).
  `(EVAL - T0).n` = 30, and the first post month has t = 0. `np.polyfit(w=sqrt(n))` is WLS with weights n.
- **Quarters.** 2023Q1-2026Q3 are all present (3,097-4,090 abstracts each). The data end on 2026-09-30, with no
  2026Q4 documents, so `mso_2026Q3` is a complete quarter.
- **`RELEASE` / `PRETRAIN_CUTOFF`.** Each decimal value falls inside the month given in Table 1 (for example
  2026.42 = early June 2026 for Gemma 4, 2024.95 = December 2024 for Phi-4, and cutoffs at mid-month: 2021.71 =
  September 2021). Every single region except the 2026 model has a release entry (18), and 9 have a cutoff,
  matching `n` and `n_cutoff`.
- **`vintage_sets`.** RAID summary-register outputs are dropped from single regions only for `raid-` models. The
  `CHAT` filter keeps the six RAID chat models (base `raid-cohere` excluded). "Main 14-generator region" in
  `robustness_v7` = 8 local/2026 + 6 RAID chat models, the same as `timeseries('arxiv')`.
