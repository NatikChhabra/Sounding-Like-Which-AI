# Pre-release methods audit 2 (statistics, causal inference, NLP measurement)

Scope: `paper/main.tex` as of 2026-10-13 15:02 (it was being edited during this audit, so passages are quoted
rather than cited by line number), `paper/preprint.pdf` (15:02 build), `code/analysis.py`, `code/mso.py`,
`code/features.py`, `code/build_sources.py`, `code/fetch_arxiv.py`, `code/generate.py`, `results/*`, and the
earlier reviews in `paper/reviews/`. Nothing in the project was edited except this file.

I re-ran the single-generator regions from the working data (`F:\research-data`) in a scratchpad (scripts in
`<scratchpad>/rev2m/`), reading the raw data and writing nothing to it. Seed 0 reproduces
`arxiv_vintage_quarterly.csv` exactly (max |diff| 1e-16), and the peaks match. Every check below that is new in
this round uses those doc-level scores.

**Verdict.** I found no code bug that changes a reported number, and no blocking validity problem in the headline
result. The ρ = 0.83 peak correlation holds up under every perturbation I tried. Five interpretive claims in the
vintage, marker and Discussion sections are contradicted or unsupported by the paper's own data (I1–I5). The
trend-gap estimand also has a specification problem that biases the vintage comparison (I6). Each fix is a
short text change, plus at most one cheap re-run.

---

## Checks that PASSED (new this round; the paper may cite them)

| Check | Result |
|---|---|
| Seeds of LLM prompts in the score pool (all three LLM files, RAID) | 0 of 5,850 local/2026 seeds are in the score pool; RAID ids are disjoint |
| Isotonic ties at the 0.5 threshold, single-generator regions | ≤0.08% of documents have p = 0.5; `>=` and `>` give the same MSO |
| ρ(release, peak) across 5 human-draw seeds | 0.79–0.84 |
| ρ across 10 LLM-side 80% subsamples (seed 0) | 0.71–0.85 (median 0.81); every 2025→2026 sign is the same in 10/10 |
| ρ under a joint document bootstrap within quarters (1,000 draws) | median 0.78, 95% interval 0.65–0.87 |
| ρ excluding the eight 2023 models (n = 10) | 0.82 (p = 0.003). The correlation is not just "2023 vs later" |
| ρ with equal field weights within each quarter | 0.81 |
| ρ with each quarter reweighted to the 2023 abstract-length distribution | 0.83, so human abstract lengthening does not drive the peak ordering |
| Main gap with equal field weights / pre-period field weights | 26.7 (24.0–29.3) / 24.4 (22.3–26.5), vs 25.4 primary |
| 2025→2026 single-generator changes with equal field weights | all 19 signs unchanged |

Note for the authors: field composition is far from equal. In 2015 eess is 1.5% and econ 0.7% of scored
abstracts, while astro-ph, cond-mat and math are 22–24% each. By 2022 eess is 16%. A 2-day cs window that falls on a
weekend gives far fewer than 200 papers. The headline survives this (row above), but the Data section's phrase
"smaller fields (economics in particular)" understates how much the mix changes, and the pre-trend slope partly
reflects it: 0.47 pp/yr pooled vs 0.29–0.30 with fixed field weights.

---

## IMPORTANT

### I1. The Discussion's two readings of the late peaks ignore that three 2026 models peaked before or at release
- **Evidence.** `arxiv_vintage_quarterly.csv` with `RELEASE`:
  - Gemma 4 (released 2026.42) peaked in 2025Q4, two quarters before release.
  - Granite 4.2 (2026.65) peaked in 2026Q2, before release.
  - Qwen3.5 (2026.17) peaked in 2026Q1, the release quarter.
  - These peaks are stable: 10/10 LLM subsamples, and 0.68–0.81 modal in the document bootstrap (Gemma 4 2026Q1 in 30%).
- **The problem.** The Discussion says: "Our data cannot say why abstracts in 2026 resemble the newest models:
  authors may use those models, or the models may have learned from recent abstracts." For these three models
  the first reading is impossible as a cause of the peak timing: no author used Gemma 4 in 2025Q4. The data
  therefore can partly say why.
- **The missing reading.** Open models released in 2025–26 are post-trained largely on synthetic data from the
  commercial models that authors actually use. Under this reading, release date proxies the commercial-model
  style of the time, and both the open model and the abstracts converge on it.
- **Fix (text).** Replace the sentence with: "For three of the 2026 open models overlap peaked before or in the
  quarter of their release, so their late peaks cannot come from authors using them. They fit models that learned
  from recent writing, or open models and authors converging on the style of the commercial models in use at the
  time, which we did not run."
- **Fix (code).** Add `release_before_peak` to `vintage_peak()` so the count is a macro.

### I2. "Release date sorts them better [than cutoff], consistent with … post-training" is unsupported
- **Evidence.** The 9 generators with a stated cutoff (Table 1) are GPT-4, Llama-2-70B, Llama-2-7B, Vicuna,
  Llama 3.1, Phi-4, Gemma 3, gpt-oss and Gemma 4. On these, ρ(cutoff, peak) = 0.72 (p = 0.03) and
  ρ(release, peak) = 0.75 (p = 0.02).
- **The problem.** The two orderings cannot be told apart. The text's evidence is two anecdotes (gpt-oss and Gemma 4).
- **Fix (text).** "On the nine generators with a stated cutoff, cutoff and release date order the peaks about
  equally well (ρ = 0.72 and 0.75), so we cannot separate post-training from pretraining-data recency." Compute
  both values in `vintage_peak()`.

### I3. "Lexical markers turned earlier" is contradicted by quarterly data
- **Where.** Discussion: "Lexical markers turned earlier"; §Markers: "lexical measures turned down before stylistic ones".
- **Evidence.** I computed the quarterly share of abstracts that contain each generator's own mined words (from
  `arxiv_vintage_its.json`) and compared its peak with the style peak:

  | Marker peak vs style peak | n | Generators |
  |---|---|---|
  | Earlier | 7 | gpt-oss, Granite 3.3, Mistral, Phi-4, Qwen3.5, Qwen3, RAID GPT-4 |
  | **Later** | 8 | Gemma 4, Llama-2-7B, ChatGPT, Cohere, Llama-2-70B, Mistral-chat, MPT, Vicuna |
  | Same | 4 | |

  For the 2023 models, markers peaked **after** style (e.g. Vicuna: style 2024Q3, markers 2025Q2).
- **What survives.** The annual 2026 comparison holds for gpt-oss and Qwen3.5 only. "Including two whose style
  overlap kept rising" also still counts Qwen3.5, which peaked in 2026Q1 (round-4 m1, unfixed).
- **Fix (text).** "For gpt-oss and Qwen3.5, mined-marker shares fell in 2026 while style overlap rose, so a falling
  marker share need not mean that writing stopped moving. Across all generators, quarterly marker and style peaks
  show no consistent order." Delete "Lexical markers turned earlier".

### I4. The "turn down" of the late generators rests on a final quarter that drops for every instrument
- **Evidence.** From 2026Q2 to 2026Q3, overlap falls under all 18 non-2026-model single regions. It falls in every
  field except astro-ph: cs −2.7, econ −3.0, math −2.2, stat −2.1 pp (mean over regions). Field shares barely
  move between the two quarters.
- **Why it matters.** For gpt-oss (39.9→37.5) and Granite 4.2 (34.1→32.0), this common-mode last-quarter drop
  is the whole "turn". The abstract says overlap "rises and then falls" for each single generator, and §6.4 says
  "rises and then turns down".
- **Statistical consequence.** All instruments score the same documents, so their quarterly errors are
  correlated. The asymptotic p for ρ assumes 18 independent points.
- **Fix (text).**
  - "…overlap rose and then turned down under all generators but the 2026 model; for gpt-oss and Granite 4.2 the
    turn is a single final quarter in which overlap fell under every reference except the 2026 model."
  - Report the bootstrap interval for ρ (0.65–0.87) instead of, or next to, "p<0.001".

### I5. The typed peak-quarter lists are less stable than the text admits
- **Where.** The text gives exact peak quarters by group ("in 2025Q2–Q3 under the 2024 models", "2025Q4 under
  Gemma 3, Granite 3.3 and Qwen3"). It calls only Gemma 3, Granite 3.3 and Qwen3 unstable.
- **Evidence.** No top quarter beats the runner-up by more than z = 1.7 (independent binomial SE).
- **Modal share in the document bootstrap:**
  - Below 0.5: RAID GPT-4 0.41, Qwen3 0.43, Llama 3.1 0.45, Gemma 3 0.47.
  - 0.5: Mistral, Llama-2-70B.
- **Across LLM subsamples:**
  - Phi-4 peaks in 2025Q4 in 6 of 10 runs (the text says 2025Q2).
  - Llama 3.1 peaks in 2025Q3 in 6 of 10.
  - RAID GPT-4 peaks in 2025Q1, Q3 or Q4.
- **Fix (text).**
  - Give ranges: "2023 models 2024Q3–2025Q3; 2024 models 2025Q1–Q4; Gemma 3, Granite 3.3, Qwen3 2025Q2–2026Q1;
    gpt-oss, Qwen3.5, Granite 4.2 2026Q1–Q2".
  - Change "Peak quarters of flat-topped series (…) are unstable" to "Individual peak quarters are uncertain by
    about one quarter (Appendix X); the rank correlation is not (bootstrap 0.65–0.87; 0.79–0.84 over training
    draws; 0.71–0.85 over subsamples of generator outputs)".
- **Fix (code, about 20 lines).** Add a bootstrap within quarters to `vintage_quarterly()`, resampling document
  indices jointly for all regions (the sketch is in `rev2m/peaks.py`, section 3).

### I6. The June-2025 trend gap depends on data after June 2025, which biases the vintage comparison
- **Code.** `segmented()` fits one linear post-segment through September 2026 and reads it at June 2025.
  - For S-shaped or hump-shaped post-periods, that number changes as later data arrive and is not a
    well-defined estimand.
  - Under misspecification the HAC CI is not valid.
- **Evidence, main series.** The fit ending at EVAL gives **27.5** (25.6–29.3) instead of 25.4. Ending at
  2025-12 gives 27.4. This is conservative and harmless for H2.
- **Evidence, vintage regions** (`arxiv_vintage.csv`, `gap` vs `gap_nonparam`, the mean observed Jan–Jun 2025
  value minus the trend). The bias depends on the shape:

  | Region | Shape | ITS gap | Nonparametric gap |
  |---|---|---|---|
  | `pre2022data_matched` | hump | 7.5 | **11.9** |
  | `old_open_p1` | hump | 3.5 | 6.6 |
  | Llama-2-7B | hump | 3.7 | 7.5 |
  | `local_p1` | rising | 20.3 | 22.1 |
  | 2026 model | rising | 14.2 | 10.9 |
  | gpt-oss | rising | 22.3 | 20.3 |

  The headline contrast "7.5 vs 20.3" (ratio 0.37) becomes 11.9 vs 22.1 (ratio 0.54). The abstract's "smaller
  but clear (7.5)" understates the pre-ChatGPT-data shift by about 40% relative to the newer region.
- **Fix (one argument, already in the code).** In `vintage()` and `timeseries()`, report
  `segmented(m, until=EVAL)` as the primary or as a robustness row, or state the gap as the nonparametric value
  already computed (`gap_nonparam`). At minimum add one sentence: "Because overlap with older generators peaked
  in 2025, a linear post-trend fitted through 2026 understates their June-2025 gap (nonparametric: 11.9 vs 22.1 pp)."

---

## MINOR

- **m1. Abstract, "will eventually show the shift receding".** This is a forecast from ≤3 quarters of 2026 data,
  and the 14-generator set still rose in 2026. Use "can show" or "would eventually show if the pattern persists".
- **m2. Seed-variation design.** `robustness_v5` varies only the human training draw (`mso.SEED` changes `H`;
  the 150 LLM texts are fixed). The text's "five draws of the human training sample" is accurate, but the
  dominant instrument variance with 150 generator texts is on the LLM side. My 10 subsamples at 80% leave every
  sign unchanged; add one sentence saying so, or add the subsampling loop (`rev2m/llmsub.py`).
- **m3. RAID single regions still mix registers** (round-4 m10, not fixed). Summary-register shares are ChatGPT
  31%, Cohere 33%, Mistral-chat 21% and MPT 16%. The mined markers for these regions are summary words
  (*concludes, discusses, summary, summarized, overview, you*). The only exception to "rose 2022–2025" (Cohere) is
  the region most affected. Either apply `SUMMARY` to the `single:raid-*` sets in `vintage_sets` (one line:
  `p1 = p1[~(p1.model.str.startswith("raid-") & p1.text.str.contains(SUMMARY))]`) and re-run `vintage`,
  `vquarter` and `vpeak`, or add the shares to Limitations.
- **m4. Training size differs by vintage.** RAID single regions train on 450+450 texts and local regions on
  150+150, so instrument precision is confounded with vintage group. The ρ excluding the 2023 models (0.82,
  n = 10) shows this does not drive the result; say so in one clause.
- **m5. Seasonality.** Pre-period residuals by quarter are Q1 −0.44, Q2 +0.52, Q3 +0.25 and Q4 −0.34 pp (F-test
  p = 0.08). This is the same order as most top-two peak margins (0.1–0.9 pp). It is harmless for ρ, but it is
  one more reason to quote peaks as ranges (I5).
- **m6. Equal-weight claim for the pre-ChatGPT-data region.** §3 defines P_LLM as an equal-weight mixture over
  generators. In `pre2022data_matched`, the capped mix is GPT-4 450, Llama-2-70B 450, Llama-2-7B 150 and Vicuna
  150, so the weights are 37.5/37.5/12.5/12.5. The text's "three quarters from RAID" says this; add "not equally
  weighted" in §4 Vintage.
- **m7. Data section on composition.** Add the field-share range (e.g. eess 1.5% in 2015 vs 16% in 2022) and the
  fixed-field-weight gap (26.7, CI 24.0–29.3) to Table 2. The latter needs about 5 lines from
  `arxiv_monthly_by_field.csv`: pivot, average over fields, then `segmented`.
- **m8. 2026-model session batching.** The 50-prompt sessions can make outputs within a session correlated.
  CV and calibration folds group by source document, not by session, so held-out recall and calibration for the
  2026 model may be optimistic. Add the session id to `grp` in `mso.training_set`, or mention it in Limitations.

---

## Exact text replacements (copy-ready)

1. §6.4: "Known pretraining cutoffs do not sort the generators: gpt-oss (cutoff June 2024) peaked late while
   Gemma 4 (January 2025) peaked early. Release date sorts them better, consistent with an effect of recent
   post-training more than of pretraining-data recency."
   → "On the nine generators with a stated pretraining cutoff, cutoff and release date order the peaks about
   equally well (rank correlations 0.72 and 0.75), so we cannot separate the recency of post-training from that
   of pretraining data."
2. §Markers: "For these generators, lexical measures turned down before stylistic ones, so…"
   → "Under gpt-oss and Qwen3.5 the mined-marker share fell in 2026 while style overlap rose, so…"
3. Discussion: "Lexical markers turned earlier: words mined from most generators, including two whose style
   overlap kept rising, fell in 2026, so…"
   → "Words mined from most generators fell in 2026, including those of gpt-oss, whose style overlap kept
   rising, so…"
4. Discussion: "Our data cannot say why abstracts in 2026 resemble the newest models: authors may use those
   models, or the models may have learned from recent abstracts."
   → see I1.
5. §6.4: after the ρ sentence add "(document-bootstrap interval 0.65–0.87; 0.82 without the 2023 models)", and
   replace the instability sentence as in I5.
