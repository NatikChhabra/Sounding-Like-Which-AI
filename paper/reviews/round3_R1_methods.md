# ARR Review, Round 3: Reviewer 1 (methods, identification, statistics)

**Paper (v3):** "Sounding Like Which AI? Machine-Style Overlap of arXiv Abstracts with Language Models of Different Vintages"
**Previous title (v2):** "After the Delve Fades: Scientific Abstracts Keep Moving Toward LLM Style"
**Reviewer expertise:** computational social science, observational time series and causal inference, statistical learning.

**What I examined**
- `paper/main.tex` (687 lines), the compiled `paper/main.pdf` (13 pp.; text extracted, Figures 1 and 2 rendered).
- `results/numbers.tex` and the raw files behind every number I quote below.
- `code/analysis.py` in full. This includes the new `vintage()`, `vintage_sets()`, `marker_series()`, `mined_markers()`, `source_texts()`, `load_old()`, `vintage_summary()`, `placebo_grid()`, `robustness_v3()`, `robustness_v4()`, `block_bootstrap()`, `_pre_fit()`/`gap_vs()` and `nonparam_gap()`. Also `code/mso.py`, `code/features.py`, `code/generate.py`, `code/make_numbers.py`, `code/build_sources.py`, `code/run_v4*.ps1`.
- `preregistration.md` (deviations 1–12), my round-2 review and the round-2 AC meta-review.
- **Read-only reanalyses.** I imported the authors' `mso.py` and `analysis.py` against `F:\research-data`, with the feature cache patched to be read-only and `save()` disabled; nothing in the project or data directory was written. The script is in my scratch folder. At seed 0 my refits reproduce the published single-generator values exactly (for example Gemma 3 at 31.6% → 29.5%, Granite 4.2 at 25.4% → 33.0%, and the 2026 model at 29.3% → 39.2%).

---

## Summary of the revision

The paper is reframed around a new question: which LLMs define "LLM style"? The main additions are:
- **Pre-ChatGPT-data region.** A region built from generators whose pretraining data predate ChatGPT: RAID GPT-4 and Llama-2-70B-chat, plus locally run Llama-2-Chat 7B and Vicuna 7B. Its June-2025 trend gap is 7.7 pp (4.7–10.6). The paper calls this the "identified" part of the 25.7 pp shift.
- **Single-generator regions.** Nineteen regions, each built from one generator on the title-only task. From 2025 to 2026, MSO fell under all 14 generators released before August 2025 and rose under 4 of the 5 released since. Two of the rises (Granite 4.2, Qwen 3.5) contrast with falls under their predecessors in the same family.
- **Mined marker words.** Words mined from each generator's own outputs, which "behave like their style regions until 2025".
- **Robustness additions:** a placebo grid, pre-trend variants, a block bootstrap, three drift-placebo origins, Holm correction with a cs–math contrast, implied prevalence via the mixture identity, length-standardised baselines, length-fixed dispersion with a bootstrap, and GPT-2 perplexity.

This is a substantive, mostly well-executed revision. It takes my central round-2 objection (W1: a post-treatment instrument) seriously and builds the design I asked for. The headline 25.7 pp shift remains robust. I tried again to break it, this time on revision censoring, and could not.

My remaining concerns have moved. They now concern **what the vintage analysis can identify**:
- the "identified" pre-ChatGPT-data gap is real: it passes a region-specific drift placebo that I ran and that the paper should add. But it is small, it rests mostly on RAID's GPT-4 outputs, and by 2026 it had fallen to 4.7 pp above trend. It is described with more confidence and generality than it supports.
- the 2026 "fading as models age" claim is a single calendar-year transition that the paper's own primary fixed reference set does not show.

They also concern **a set of new, verifiable errors in the rendered paper**:
- two macro-formatting bugs that print values multiplied by 100;
- a false sentence in §6.5;
- a false figure caption.

---

## 1. Status of my round-2 weaknesses

| # | Round-2 weakness | Status | Evidence in v3 | What is still missing |
|---|---|---|---|---|
| W1 | The LLM side is partly post-treatment | **Mostly fixed** | §5 "Vintage" and §6.4 build a pre-ChatGPT-data region (7.7 pp, 4.7–10.6; `arxiv_vintage.csv` `pre2022data_matched`) and a single-generator vintage design. The abstract now gives 7.7 next to 25.7. Three 2026 open models with logged decoding (`generate.py`: T=0.8, fixed seeds, `think=False`) replicate the 2026-model rise (open2026_p1: 29.3 → 35.5%). Later-generator regions are now presented as descriptive ("we cannot tell whether…", §6.4 last paragraph). | (i) The paper gives the "identified" region no drift placebo of its own. My run shows it passes one (§3b), so add it. Its controlled local-only variant (3.5 pp) is small, and the identified component had shrunk to 4.7 pp above trend by 2026. (ii) **No vintage curve against training cutoff** (my round-2 Q1). Table 1 gives cutoffs for only 8 of 19 generators, and the rise/fall pattern is cut by *release* month, not cutoff (§3c). (iii) The 2026-model texts were not regenerated; they are demoted in effect, which is acceptable now that open models replicate the result. |
| W2 | The marker-word vs MSO contrast mixes vintages | **Mostly fixed** | The title no longer says "keep moving". Mined, vintage-matched marker words (`mined_markers`) are compared with their own regions (§6.5). The "markers understate the shift" claim is gone. | §6.5 contains a factual error (N2). Also, mined "markers" with 2021 base rates of 17–62% (`arxiv_vintage.csv` m2021; for example Llama-2 at 49.4% and the 2026 model at 43.3%) are not markers in Kobak's sense. They are common academic words, and their dynamics mostly mirror secular vocabulary change. |
| W3 | The comparison genre fails its placebos; results omitted | **Mostly fixed** | Placebo grid reported: 17.6% of 34 breaks give p<0.05 (`robustness_v3.hansard_placebo_grid`). Threshold-0.6 gap reported: 1.6 pp (0.2–3.0). Pre-trend range −2.8 to 2.8. The 2022 change of government is noted. The wording is now "changed much less than abstracts". | HAC lags are still by row over non-contiguous months, and the Hansard block bootstrap resamples by row too. The Hansard marker gap (1.6 pp, p=0.011, `hansard_its.json` marker) is still unreported. No GBM-instrument ITS. The arXiv−Hansard CI (30.2, 27.7–32.7) still uses the anti-conservative Hansard SE. These are minor now that the claim is softened. |
| W4 | Dispersion is a length artefact | **Fixed in substance, broken in rendering** | §6.7 now uses the first 150 words of ≥150-word abstracts (`robustness_v3` → `arxiv_len150_dispersion*`). Pre-trend −0.11/yr; 2025 gap +0.05 (bootstrap −0.36 to 0.51). The homogenization claim is withdrawn and the result is reported as a null. | **The PDF prints the CI as "−35.9 to 50.8"** for an estimate of 0.05 (N1). Archive mix is not held fixed, and the ≥150-word subset is a time-varying selection, since abstracts lengthen. Within-archive dispersion was not done. |
| W5 | H1 heterogeneity and the H4 ordering are confounded by length and detectability | **Partly fixed** | Length-standardised baselines: astro-ph 6.1, econ 13.9 (`arxiv_baseline_lenstd.csv`). cs−math contrast 27.6 (22.3–33.0). Holm correction. | Math's standardised baseline (6.7%, versus 9.0% raw) makes it the second-lowest field; the text does not say so. **Field-specific sensitivity is still uncorrected.** The implied-prevalence calculation uses one pooled TPR (0.838) for every field, although P2 recall varies from 0.48 (astro-ph) to 0.76 (q-bio) (my round-2 reanalysis). Holm on p-values of order 10⁻²⁰–10⁻¹⁰⁷ is decorative. |
| W6 | ITS specification and inference | **Partly fixed** | Pre-trend variants: quadratic 27.0, from 2019 27.5, to 2020 25.7. Nonparametric gap 26.5. Block bootstrap 23.6–27.5. Yearly residuals 6.6 / 16.2 / 28.7 / 32.5 pp (`arxiv_event.csv`). Extreme p-values are now printed as "<0.001". | No pointwise CIs on the event study. No cluster bootstrap (only disclosed in Limitations). **The astro-ph negative level shift is still unexplained**: −3.8 pp, p=0.002 (`arxiv_its.json` astro-ph). There is also an unexplained econ level shift of +10.8 pp (p<0.001). The block bootstrap pools residuals from a misspecified, curved post-segment with pre-period residuals and ignores the WLS weights. Its CI is *narrower* than the HAC CI, which should be a warning sign rather than a reassurance. |
| W7 | Residual confounds (writing tools, author population, lexical leakage through function words) | **Not fixed** | Limitations mentions authorship and subfield change. | No feature decomposition of the shift. No ablation of LLM-favoured closed-class words (*across*, *within*, *through*). No author panel. Non-LLM writing assistants (Grammarly, Writefull, DeepL Write) are not discussed. |
| W8 | Learner and perplexity analyses | **Mostly fixed** | GPT-2 rerun: ELL OR 0.47, and 0.66 (0.52–0.85) after proficiency adjustment. TOEFL 63.7% vs US 8th grade 8.0% (`essay_*_gpt2`). Claim scoped to "in these data". Cut to one abstract sentence. | Note that under GPT-2 the ELL effect **survives** the proficiency adjustment, unlike the style instrument. "Most of the difference is proficiency" is true for the style instrument only and should say so. |
| W9 | Code–text mismatches and data integrity | **Partly fixed** | "8.00" is fixed, the TODO is gone, the 2026 months are labelled, and the §6.5 description is rewritten. | (1) "The overall series weights the eight archives about equally" (§4) is still false in the pre-period. Scored econ abstracts are 25 of 3,550 in 2015 (0.7%) and 975 of 11,727 in 2026 (8.3%); cs is 455 against math 862 in 2015. `monthly()` weights documents. (2) **113 Hansard generations still have `src_id = NaN`**, and llama3.1 and qwen3 still have 469 and 463 rows (`llm_hansard.jsonl`, checked today). (3) Deviation 9 in `preregistration.md` says the pre-ChatGPT region uses "RAID GPT-4 and ChatGPT"; the paper uses GPT-4 and Llama-2-70B, with ChatGPT only as a sensitivity check. |
| W10 | Uncertainty understates generator-set variation | **Mostly fixed** | The abstract reports 25.7 and 7.7 together. | No between-set summary. Single-region levels are highly sensitive to the 150-document human draw (§3c, R2). |

---

## 2. Verification of the new analyses against the code

### 2a. Generator-vintage design (`vintage`, `vintage_sets`, `load_old`, `training_set`)

- **Correct:** P1-only for local and 2026 generators, and RAID as is. OLD and NEW models are excluded from every non-vintage set (`new = chat[~chat.model.isin(OLD + NEW)]`). Seeds come from `seed_arxiv.parquet`, which is the train pool. No seed document is ever scored: I checked that every `src_id` in `llm_arxiv.jsonl` is in the train pool or absent from the v2 sample, and all 2,250 vintage-only generations are train-pool seeded. **No leakage found.**
- **Training-set size differs by generator.** `training_set` balances the human side to the LLM side and caps each generator at `PER_MODEL=450`. The consequences:
  - Every local single-generator region is trained on **150 LLM vs 150 human** documents, and every one uses the *same* 150 human abstracts (same seed and same n).
  - RAID single regions use 450 vs 450.
  - In `pre2022data_matched`, RAID GPT-4 and Llama-2-70B contribute 450 each and the two local models 150 each, so the region is 75% RAID. That contradicts §3's "equal-weight mixture over a reference set". It also means the "matched task" claim rests mostly on RAID's prompt and decoding, not on the controlled local runs. The local-only version (`old_open_p1`) gives 3.5 pp (1.5–5.5).
  - With several hundred features and C=0.1, a 150/150 classifier is a high-variance instrument. My seed reruns, which redraw the 150 human documents, move single-region *levels* a lot:
    - Granite 3.3 in 2025: 15.7–28.8%.
    - Qwen3 in 2025: 17.8–28.0%.
    - Qwen3.5 in 2025: 14.4–21.4%.

    The *signs* of the 2025→2026 changes are stable for every generator except **Gemma 4, whose change ranges from −1.1 to +0.5 pp** across five draws (§3c). No interval in the paper reflects this.
- **Summary-register filter.** `SUMMARY` drops RAID texts containing "titled", "the authors" or a leading "the paper/article/study". It is applied only to RAID in the matched set, which is reasonable. The 5.4% share quoted in the text is `pre2022data.summary_register_share`, which is correct.
- **`vintage_summary`** counts falls as `y2026 < y2025` with no tolerance, so a −0.8 pp change counts as a fall (Gemma 4). Given the instrument variance above, a tie band (for example |Δ| < 1 pp) should be reported.

### 2b. Mined markers (`mined_markers`, `marker_series`, `source_texts`)

- The log-odds of document frequency against the generator's own prompt sources is a sensible topic control. `PROMPT_WORDS` removes prompt echoes, and the assertion that ≥90% of sources are found is good practice.
- **Two issues:**
  1. With `min_df=0.05` and 150 outputs, a word needs about 8 occurrences to qualify, and the +1e-3 smoothing gives words absent from the 150 sources very large log-ratios. The resulting lists are ordinary vocabulary with base rates of 17–62% of abstracts (m2021). Their 2022→2025 rise is therefore partly secular vocabulary drift, and there is no pre-trend adjustment in the "rose from 2022 to 2025" statement.
  2. `marker_gap` is an ITS gap, but the text uses only raw yearly shares.
- The marker columns for `all` and `all_no_revision`, and for `pre2022data` and `pre2022data_abstract_register`, are identical to four decimals. I believe this is because the top-20 lists coincide, not a bug. Please confirm by printing `marker_words` from `arxiv_vintage_its.json`.

### 2c. Placebo grid (`placebo_grid`)

- **Correct as described:** 34 breaks, every second month from 2016-06 to 2021-12, each evaluated 12 months later. 3/34 (8.8%) have p<0.05, against an expected 1.7, binomial p≈0.24. The largest gap is 2.9 pp.
- **Horizon mismatch.** The real gap is evaluated **30 months** after the break; the placebos at **12**. Extrapolation error grows with horizon, so the grid understates what a spurious 30-month gap looks like. In round 2, with evaluation at June 2022 (horizons of 12–66 months), I found a maximum of 4.6 pp. Re-run the grid with a 30-month horizon for breaks up to 2020-05.

### 2d. Pre-trend variants and nonparametric gaps (`_pre_fit`, `gap_vs`)

- Correct. WLS with √n weights; the January–June 2025 mean minus the extrapolated trend.
- Table 2 labels these rows "Nonparametric", but they still extrapolate a parametric pre-trend. "Model-free post-period" would be more accurate.
- The values (26.5 / 27.0 / 27.5 / 25.7) are reproduced from `robustness_v4.json`.

### 2e. Block bootstrap (`block_bootstrap`)

- It resamples *unweighted* residuals from one residual vector covering the pre- and post-periods, then refits with weights.
- The post-period residuals come from a linear fit to a clearly curved segment, so they are systematic, not noise. Months with about 3× different n (about 300 docs/month in 2015 against about 1,100 in 2023+) are treated as exchangeable.
- The resulting CI (23.6–27.5) is narrower than HAC (23.5–27.9). Neither CI is wrong enough to matter for a 25.7 pp effect, but the block bootstrap adds no independent evidence.
- Hansard uses the same row-based blocks over 92 non-contiguous months.

### 2f. Drift placebos (`robustness_v4`, `drift_placebo`)

- **Implemented as described.** The train pool is truncated at Y; humans of all pre-ChatGPT years are scored; the break is the following January; the gap is evaluated in June 2022.
- **Results:**
  - to-2016: **+6.8 pp, CI 0.5–13.1, p=0.035**;
  - to-2017: **−2.5 pp, CI −4.5 to −0.4, p=0.017**;
  - to-2018: −1.2 pp, p=0.126.
- **Two of three drift placebos are significant at 5%, in opposite directions.** This is evidence that, at 41–65-month horizons, either instrument ageing is real or the HAC intervals are too narrow. Either way, the paper's statement that drift is "about a quarter of the observed gap at most" is a bound from three draws.
- That bound is fine for the 25.7 pp headline, which is 3.8× the largest drift placebo. It cannot be carried over to the 7.7 pp "identified" gap, which is measured with a different instrument and needs its own placebo. I ran one (§3b): it passes.
- Contribution (3) says drift gaps are "at most a quarter as large". In fact 6.8/25.7 = 0.26.

### 2g. Implied prevalence (`robustness_v4["implied"]`)

- **Identity applied correctly:** α = (MSO_t − FPR_g)/(TPR − FPR_g), with FPR_g the field's pre-period mean and TPR the pooled cross-validated recall (0.838) or the LOMO mean (0.801).
- **Three caveats:**
  1. FPR_g should be the *extrapolated trend* for year t, not the pre-period mean. For cs in 2024 this moves α from 42.0% to 38.9% (math from 7.9% to 7.5%; my calculation from `arxiv_monthly_by_field.csv`).
  2. The TPR is pooled over generators, prompts *and fields*. Field-specific detectability (W5) biases math α downward relative to cs.
  3. The comparison with Liang et al.'s 17.5% / 4.9% mixes documents with sentences and calendar-2024 means with February 2024.

  The paper states the third caveat and the mixture-identity limits fairly. The first two should be added.

### 2h. Length-fixed dispersion (`robustness_v3` → `dispersion`)

- Correct in code. Features are recomputed on the first 150 words. 1,200 documents per year are sampled from ≥150-word abstracts. Standardisation uses pre-ChatGPT documents in that sample. The bootstrap resamples within year and refits the 2015–2022 linear trend in each replicate.
- **The rendered CI is wrong by a factor of 100** (N1).
- The ≥150-word subset is a time-varying selection, and archive shares are not held fixed.

### 2i. Holm and cs−math (`robustness_v3`)

- Correct. The cs−math SE treats the two archives as independent, which is right for the sampling component and ignores the shared instrument.
- The H4 contrast (27.6, 22.3–33.0) is now properly reported.

---

## 3. Are the headline claims supported?

### (a) 25.7 pp trend gap: **supported, as a descriptive overlap with the 14-generator reference**

It reproduces (`arxiv_its.json` all: 0.2567, 0.2347–0.2787). It is stable across all of the following:
- thresholds (23.6–27.2);
- notation, topic, length and dash variants (24.1–29.3);
- pre-trend shape and window (25.7–27.5);
- my round-2 equal-archive, subcategory, never-revised and submission-hour reweightings.

**A new check this round: revision censoring.** The API returns the *latest* version, and later years have had less time to be revised. In the sample, 41.5% of 2024 papers carry a version >1, against 38.6% of 2025 papers and 24.0% of 2026 papers; in 2026Q3 the figure is 14%. If LLM-polished revisions inflate MSO, recent years are understated.

Restricting to never-revised (v1) papers leaves the 2025→2026 single-generator changes essentially unchanged; table in §6, R1. So revision censoring does not drive either the headline or the 2026 pattern. Please report this check; it is cheap and it pre-empts an obvious objection.

The causal reading ("because of ChatGPT") is still not claimed, which is correct.

### (b) Pre-ChatGPT-data gap as the "identified" part: **non-zero, but smaller, more fragile and more transient than the text implies**

The design is right. The region rules out one channel: models learning from post-ChatGPT *abstracts*. It does **not** identify a causal effect; it is still an ITS against a linear pre-trend.

1. **The region-specific drift placebo passes, and the paper should report it.**
   - The paper offers only the 14-generator drift placebos. The largest (+6.8 pp) is close to the 7.7 pp matched gap, so a reader cannot tell from the paper whether instrument ageing could produce the matched gap.
   - I ran the region's own placebos with the authors' code. The matched region was retrained with human training documents up to Y, the break placed the following January, and the gap evaluated at June 2022. The results:
     - Y=2016: **+1.2 pp (−2.6 to 5.0), p=0.53**;
     - Y=2017: **−1.6 pp (−3.1 to −0.0), p=0.049**;
     - Y=2018: **−1.8 pp (−3.1 to −0.4), p=0.009**.
   - Ageing in this region is small and, if anything, negative, so the 7.7 pp gap is not a drift artefact. Note, though, that two of three placebo gaps again have p<0.05: the HAC intervals are too narrow at long horizons in this design too.
   - **Caveats that remain:**
     - The only fully controlled variant (Llama-2-Chat 7B + Vicuna, local, logged decoding) gives **3.5 pp (1.5–5.5)**.
     - The 7.7 is carried mostly by RAID GPT-4 (single region 11.5 pp; three-quarters of the matched training texts are RAID).
2. **The identified component largely reversed in 2026.**
   - Matched-region yearly MSO is 6.6 → 10.2 → 15.6 → 18.2 → **12.2%** (2022–2026).
   - Its yearly residuals from its own linear pre-trend are within ±0.5 pp through 2022, then **3.7, 8.8, 11.0 and 4.7 pp** in 2023–2026 (my rerun at seed 0, which reproduces the published series and gap exactly).
   - The 2025→2026 fall (−5.5 to −6.5 pp across five training draws) is robust.
   - The ITS "gap" evaluated at June 2026 would still be 8.5 pp, only because the linear post-segment cannot bend. This is a concrete example of why the evaluation-month summary misleads for curved post-periods.
   - "Part of the shift is toward the style of pre-2023 LLMs" is true for 2023–2025. By 2026 that part is under 5 pp. The abstract should say so.
3. **"Training data predate ChatGPT" is literally false for two of the four generators.**
   - The Llama 2 paper the authors cite for the September 2022 cutoff states that the *tuning* data run to July 2023.
   - Vicuna is fine-tuned on ShareGPT, which consists of user-shared ChatGPT conversations from 2023 (Table 1, note d).
   - The abstract ("generators whose training data predate ChatGPT"), §1 and §6.4 ("cannot reflect models that learned from post-ChatGPT writing") should say "*pretraining* data", and should say that the style these models emit was shaped by 2023 instruction data. For Vicuna, that data is ChatGPT output, which is itself the "treatment".
   - What the region excludes is learning from post-ChatGPT *human abstracts*. That is the claim to make.
4. **The set definition was chosen after seeing results.**
   - The analysis was added after review. ChatGPT was excluded from the main set on documentation grounds, and the summary filter was added. The headline set (`matched`, 7.7) sits mid-range among six definitions (3.5, 7.2, 7.4, 7.7, 8.6, 12.2).
   - This is not damning, but "identified" and "the only comparison free of that ambiguity" should be softened to "a comparison not open to the reverse-learning explanation".
   - Show all six definitions in one small table.

### (c) The 2026 pattern: **descriptively correct, but the partition is post hoc and the interpretation is under-tested**

I verified every number in §6.4 against `arxiv_vintage.csv`. All 14 pre-August-2025 single regions fell; gpt-oss, Qwen3.5, Granite 4.2 and the 2026 model rose; Gemma 4 fell by 0.9 pp. My seed reruns show the signs are stable for all generators except Gemma 4, and unchanged on never-revised papers. The problems are these:

1. **The August-2025 cut is chosen to put gpt-oss (released 5 August 2025) on the "new" side.** A pre-specified split by release year reads differently: "14 of 15 pre-2026 generators fell, 3 of 4 2026 generators rose".
2. **Release date is the wrong axis for the paper's own mechanism.** The paper's mechanism is about *training data*. Where cutoffs are known, they do not line up with the pattern:
   - Gemma 4 has the latest stated cutoff among the 19 (January 2025, Table 1), yet it fell.
   - Gemma 3 (August 2024) and Phi-4 (June 2024) fell.
   - The gpt-oss model card, as I recall, states a June 2024 knowledge cutoff (please verify; Table 1 leaves it blank), yet gpt-oss rose most strongly of the open models (+9.0 to +11.2 pp across my reruns).

   If those cutoffs hold, the 2026 risers are not distinguished by fresher pretraining data. More plausibly they share a post-training style: reasoning-style RL, or synthetic-data-heavy tuning. That is a third explanation alongside "authors use the newest models" and "the newest models learned from recent abstracts", and the paper's dichotomy omits it. The vintage curve against cutoff that I asked for in round 2 is still the missing analysis.
3. **Within-family evidence is n=3, and one family runs against the claim.**
   - Granite 3.3→4.2 (−2.7 vs +7.6) and Qwen3→3.5 (−3.7 vs +2.3) are clean and robust in my reruns: Granite 4.2 +4.8 to +7.6, Qwen3.5 +0.6 to +3.4.
   - Gemma 3→4 (−2.0 vs −0.9) does not fit the claim. "Fell less" is within instrument noise: my reruns give Gemma 4 between −1.1 and +0.5.
   - State it as "2 of 3 families".
4. **No uncertainty is attached to any 2025→2026 change.** The sampling SE of a difference of two proportions near 0.2 with n≈14,700 and 11,700 is about 0.5 pp, and instrument variance is larger (see 2a). Report per-generator Δ with a bootstrap CI and a seed range, and use a tie band.

### (d) "A fixed reference set shows the shift fading as its models age": **not supported**

This sentence, in the abstract and in §6.4 ("Any reference set that is not refreshed will show the shift fading as its models age"), is the paper's most general claim and its weakest.

1. **The paper's own primary fixed reference set does not fade.** The 14-generator region rose from 40.7% (2025) to 44.9% (2026), and its residual from trend rose from 28.7 to 32.5 pp (`arxiv_yearly.csv`, `arxiv_event.csv`). The monthly series is flat from late 2025, which is "stopped rising", not "fading".
   - **Twelve of its 14 constituent single-generator regions fell in 2026, yet the pooled region rose.** So the explanation "it flattened in 2026 because most of its 14 generators are older than the abstracts it now measures" (§6.4) is contradicted by the paper's own numbers. A pooled region is not an average of single regions.
   - The likely driver is the 2026 model's near-human P2 revisions: AUC 0.674 (`arxiv_separability.csv`), which pull the pooled boundary toward human text, as the round-2 AC noted (N18).
2. **The pattern is a calendar-time effect, not an age effect.**
   - If regions faded *as their models aged*, the 2023 RAID models would have started fading in 2024 or 2025. Instead every RAID single region rose through 2025 (GPT-4: 8.2 → 14.4 → 20.2%) and fell only in 2026.
   - Over the same year, models only months old in 2025 (Qwen3, Gemma 3, Granite 3.3) fell too.
   - All older generators turning down in the same calendar year, whatever their age, is a **period effect**: 2026 abstracts differ from 2025 abstracts in a direction away from pre-mid-2025 model style. The data contain exactly one such transition, so a general law about ageing references cannot be estimated from them.
3. **Fixed marker lists.** The published-marker series peaks in 2024, a year *earlier* than the style regions, and the mined-marker series fall in 2026 for 17 of 19 generators. This is consistent with markers tracking public awareness (Geng & Trotta) rather than model age. That reading is just as compatible with the data.

**Suggested rewording:** "In 2026, overlap fell against every generator released before August 2025 and rose against most newer ones; a reference set that is not refreshed can therefore understate recent change."

---

## 4. New problems introduced by the revision (most serious first)

**N1. Two macro-formatting bugs print wrong numbers in the PDF.**

`make_numbers.fmt` multiplies by 100 any leaf that `startswith` or `endswith` an element of `PCT`, and `PCT` contains `"lo"` and `"hi"`. As a result:
- **§6.7:** "in 2025 lies 0.05 above that trend (bootstrap CI **−35.9 to 50.8**)". The true CI is −0.36 to 0.51 (`arxiv_len150_dispersion_trend.json`: `ci_lo`/`ci_hi` end in "lo"/"hi" and are scaled by 100; `est` is not).
- **§6.6:** "on the logit scale **27.7 against 149.0**". The true values are 0.28 and 1.49 (`logit_gap` starts with "lo").

The self-test asserts in `make_numbers.py` do not cover these keys. Fix this by matching whole leaf names, and add asserts for `ci_lo`, `ci_hi` and `logit_gap`. Then grep `numbers.tex` for any other key whose leaf starts with "lo" or "hi" or ends with them.

**N2. False sentence in §6.5.** "In 2026 the share fell for 17 of the 19 generators … it kept rising only for the 2026 model." Seventeen of 19 falling means two rose. The other is **Granite 4.2**, from 34.4% to 35.6% (`arxiv_vintage.csv` single:granite4.2:8b m2025/m2026). This also changes the interpretation: for Granite 4.2, as for the 2026 model, lexical and style measures *both* rose.

**N3. False caption on Figure 2.** "Overlap fell against every generator except the two newest." Panel (b) and the text show rises for **four** generators: gpt-oss, Granite 4.2, Qwen3.5 and the 2026 model. One of the two newest by release month (Gemma 4, 2026-05) *fell*.

**N4. The pre-ChatGPT-data region is overclaimed** (§3b). "Identified", "the only comparison free of that ambiguity", and "training data predate ChatGPT" all go too far. The paper also omits that the component fell to under 5 pp above trend in 2026, and it lacks the region-specific drift placebo, which, to the authors' benefit, passes.

**N5. The general ageing claim** (§3d) appears in the abstract, §6.4 and the Discussion ("the rise and fall of *delve* is mostly what any fixed word list or reference set would show as its models age").

**N6. The revision-exclusion rates are quoted selectively.** §4 cites 0.5% for 2016 and 7.8% for 2021 but omits **24.2% for 2022**, the year adjacent to the break (`robustness_v4.revision_exclusion_share.y2022`). The trend-to-2020 variant (25.7) shows this does not matter for the headline. Quote 2022 anyway, and cite that variant as the check.

**N7. Instrument-capacity heterogeneity across single regions** (§2a). Regions built on 150 vs 150 documents (local) and 450 vs 450 (RAID) differ in variance and in their pre-period levels: 2015 FPRs range from 0.8% (Phi-4) to 17.9% (the 2026 model). Comparisons of *levels* across generators in Figure 2a are not meaningful. Comparisons of *changes* are, with the caveats above. Say so in the caption.

**N8. Inconsistent "equal-weight mixture" description.** §3 defines P_LLM as an equal-weight mixture over generators. The matched region is 75% RAID, and the main region gives a single RAID generator (up to 7,064 texts, capped at 450) the same weight as one local model's three prompts. The latter is fine, but the matched region should be described accurately.

**N9. Smaller items.**
- Contribution (3): "at most a quarter as large"; the actual ratio is 0.26.
- Contribution (5) and §6.5 say mined markers "rise with its style region until 2025", without a pre-trend adjustment.
- Table 2 "Nonparametric" (see 2d).
- The intro credits the vintage analysis to "after review" while Appendix B(5) lists it. That is consistent, but `preregistration.md` deviation 9 names the wrong generators (W9).
- The Limitations say "four generators are from 2026"; Table 1 lists four (Claude, Qwen3.5, Gemma 4, Granite 4.2), which is correct. But the abstract says "five released since [August 2025]", which includes gpt-oss. The two counts are both right but invite confusion.

---

## 5. Numbers verified against the result files (seventeen-plus checks)

All of these match after `make_numbers` formatting unless marked.

| Paper text (v3) | Value printed | Source and key | Raw value |
|---|---|---|---|
| arXiv documents | 131,448 | `corpus_stats.arxiv_n_docs` | 131448 |
| Pre-ChatGPT MSO | 9.2% (8.9–9.5) | `arxiv_baseline_pre2022.csv` all | 0.0921 (0.0891–0.0949) |
| Trend gap | 25.7 (23.5–27.9) | `arxiv_its.json` all | 0.2567 (0.2347–0.2787) |
| Block bootstrap | 23.6–27.5 | `robustness_v4.arxiv_block_bootstrap` | 0.2358–0.2748 |
| Relative gap | 2.14× | `robustness_v4.arxiv_pretrend.relative_gap` | 2.142 |
| Threshold 0.6 / no-math | 23.6 / 29.3 | `arxiv_its.json` | 0.2359 / 0.2934 |
| Placebo grid | 34 breaks, 8.8%, max 2.9 | `robustness_v3.arxiv_placebo_grid` | 34, 0.0882, 0.0287 |
| Drift placebos | 6.8, −2.5, −1.2 | `robustness_v4.drift_to_2016/2017`, `arxiv_drift_placebo` | 0.0678, −0.0247, −0.0121 |
| Yearly residuals 2023–26 | 6.6 / 16.2 / 28.7 / 32.5 | `arxiv_event.csv` | 0.0656 / 0.1622 / 0.2869 / 0.3247 |
| Field gaps q-bio / cs / math / astro-ph | 36.8 / 38.4 / 10.7 / 13.9 | `arxiv_its.json` | 0.3681 / 0.3837 / 0.1073 / 0.1388 |
| cs − math | 27.6 (22.3–33.0) | `robustness_v3.cs_minus_math` | 0.2764 (0.2226–0.3302) |
| Implied α cs / math 2024 | 42.0 / 7.9 (LOMO 44.3 / 8.3) | `robustness_v4.implied` | 0.4198 / 0.0785 (0.4431 / 0.0826) |
| Length-standardised astro-ph / econ | 6.1 / 13.9 | `arxiv_baseline_lenstd.csv` | 0.0609 / 0.1392 |
| Matched pre-ChatGPT region | 6.6 / 15.6 / 18.2 / 12.2%; gap 7.7 (4.7–10.6) | `arxiv_vintage.csv` pre2022data_matched | 0.066 / 0.156 / 0.182 / 0.122; 0.0766 (0.0472–0.1060) |
| Variants | 8.6 / 7.2 / 3.5 (1.5–5.5) | same, pre2022data / plus_chatgpt / old_open_p1 | 0.0861 / 0.0723 / 0.0347 (0.0149–0.0546) |
| Summary-register share | 5.4% | `pre2022data.summary_register_share` | 0.0540 |
| 15 of 19 fell; 4 rose | 15 / 19 | `arxiv_vintage_summary.json` | 15, 19, rose = claude, gpt-oss, granite4.2, qwen3.5 |
| gpt-oss; 2026 model | 29.4→38.5; 29.3→39.2 | `arxiv_vintage.csv` | 0.294→0.385; 0.293→0.392 |
| Granite 3.3/4.2; Qwen3/3.5 | 22.4→19.7, 25.4→33.0; 22.4→18.7, 21.2→23.5 | same | match |
| Open 2026 models | 29.3→35.5 | open2026_p1 | 0.293→0.355 |
| Mined markers, pre-ChatGPT set | 17.4→34.9 | pre2022data_matched m2022/m2025 | 0.1744 / 0.3489 |
| Mined markers, 2026 model | 49.1→57.5 | single:claude m2025/m2026 | 0.4914 / 0.5746 |
| **"kept rising only for the 2026 model"** | — | single:granite4.2 m2025/m2026 | **0.3435 → 0.3564: also rose (N2)** |
| Hansard gap; threshold 0.6 | 1.8 (−0.3 to 3.9); 1.6 (0.2–3.0) | `hansard_its.json` | 0.0178 (−0.0032–0.0388); 0.0158 (0.0017–0.0299) |
| arXiv − Hansard | 30.2 (27.7–32.7), arXiv 32.0 | `control_difference.json` | 0.3023 (0.2775–0.3270), 0.3200 |
| **Logit gaps** | **27.7 vs 149.0** | `robustness_v4.*_pretrend.logit_gap` | **0.277 vs 1.490 (N1)** |
| **Dispersion 2025 gap** | **0.05 (CI −35.9 to 50.8)** | `arxiv_len150_dispersion_trend.gap_2025` | **0.046 (−0.359 to 0.508) (N1)** |
| Revision exclusion 2016 / 2021 | 0.5 / 7.8 | `robustness_v4.revision_exclusion_share` | 0.0051 / 0.0780 (2022: 0.2422, not quoted) |
| GPT-2 TOEFL / 8th grade | 63.7 / 8.0 | `essay_liang_perplexity_gpt2.csv` | 0.637 / 0.080 |
| Held-out 2026 model, arXiv / essays | 20.4 / 36.4 | `arxiv_lomo.csv`, `essay_lomo.csv` | 0.2044 / 0.3644 |

---

## 6. Reanalyses run for this review

All use the authors' code with read-only data access. Seed 0 reproduces the published values.

**R1. Seed stability and revision censoring of the 2025→2026 single-region changes.** Five redraws of the human training sample (`mso.SEED` 0–4). "NR" means never-revised (v1-only) papers, seed 0.

| Region | 2025→2026, seed 0 (pp) | Range over seeds 0–4 (pp) | 2025 level range (%) | Never-revised, seed 0 (pp) |
|---|---|---|---|---|
| gemma3:12b | −2.0 | −3.0 to −0.5 | 26.7–31.6 | −1.9 |
| gemma4:12b | −0.9 | **−1.1 to +0.5** | 14.5–19.2 | −1.0 |
| qwen3:8b | −3.7 | −3.7 to −2.4 | 17.8–28.0 | −4.0 |
| qwen3.5:9b | +2.4 | +0.6 to +3.4 | 14.4–21.4 | +2.5 |
| granite3.3:8b | −2.6 | −3.6 to −1.8 | 15.7–28.8 | −3.2 |
| granite4.2:8b | +7.6 | +4.8 to +7.6 | 16.1–25.4 | +7.8 |
| gpt-oss:20b | +9.0 | +9.0 to +11.2 | 27.3–33.6 | +9.8 |
| claude-opus-5.5 | +9.9 | +9.4 to +12.9 | 26.1–29.3 | +10.7 |
| raid-gpt4 | −3.9 | −4.3 to −3.5 | 13.2–21.2 | −4.6 |
| llama2:7b | −5.2 | −5.2 to −3.2 | 8.2–15.4 | −5.7 |
| mistral:7b | −4.3 | −4.6 to −3.7 | 14.3–25.9 | −5.0 |
| pre2022data_matched | −6.0 | −6.5 to −5.5 | 15.9–18.6 | −6.6 |
| open2026_p1 | +6.1 | +4.1 to +7.0 | 22.3–29.3 | +6.6 |

How to read this:
- **The signs are robust** for every region except Gemma 4.
- **The levels are not.** The 2025 level of a 150/150 single-generator region moves by up to 13 pp with the human training draw.
- **Revision censoring changes nothing.** Restricting to never-revised papers leaves every change within 1 pp.

**R2. Revision status and MSO (main 14-generator instrument, seed 0; reproduces `arxiv_yearly.csv` exactly).**

| | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|
| Revised (version >1) | 12.7% | 19.2% | 28.9% | 40.4% | 44.9% |
| Never revised | 10.4% | 16.5% | 27.0% | 40.9% | 44.9% |

Revised papers sit 2–3 pp higher in 2022–2024 and equal afterwards, so the falling revision share in 2025–2026 cannot explain the 2026 pattern.

**R3. Pre-ChatGPT-data (matched) region, seed 0.**
- ITS gap: 7.7 (4.7–10.6), reproduced exactly.
- Yearly residuals from its own pre-trend: within ±0.5 pp for 2015–2022, then 3.7 / 8.8 / 11.0 / 4.7 pp for 2023–2026.
- ITS gap if evaluated at June 2026: 8.5.
- Region-specific drift placebos: +1.2 (p=0.53) to 2016, −1.6 (p=0.049) to 2017, and −1.8 (p=0.009) to 2018.

**R4. Implied prevalence with a trend-based FPR:** cs 2024 at 38.9% (vs 42.0), math 2024 at 7.5% (vs 7.9).

**R5. Revision share by submission year** (version >1 in `arxiv_v2/sample.jsonl`): 2015–2024 between 40.2% and 42.1%, 2025 at 38.6%, 2026 at 24.0% (2026Q3: 14.0%).

**R6. Archive composition of scored abstracts:** econ 25/3,550 (2015) → 975/11,727 (2026); cs 455 vs math 862 in 2015.

---

## 7. Questions for the authors

1. What are the stated knowledge cutoffs of gpt-oss, Qwen3/3.5, Granite 3.3/4.2, Mistral 7B v0.3 and the 2026 model? Does the 2025→2026 change sort by cutoff better than by release month?
2. Please add the matched region's own drift placebos to Table 2. My attempt (R3) passes. Also, which part of the matched gap survives if RAID outputs are reweighted to equal weight with the local generators?
3. Why does the pooled 14-generator region rise in 2026 when 12 of its 14 single-generator regions fall? Which generators' texts are nearest the moved boundary?
4. Will you re-run the placebo grid at the 30-month horizon of the real gap?
5. What explains the astro-ph (−3.8 pp) and econ (+10.8 pp) level shifts at December 2022?

---

## 8. Scores

- **Soundness: 3.5 / 5.**
  - The headline shift is well supported and survives everything I and the authors have thrown at it, now including revision censoring.
  - The vintage design is the right one and is mostly correctly implemented, with no leakage.
  - Points are deducted for:
    - the over-reading of the pre-ChatGPT-data gap as "identified", given that it is mostly RAID GPT-4, has no reported region-specific placebo and had fallen below 5 pp above trend by 2026;
    - the unsupported "fading as models age" generalisation;
    - three demonstrably false statements in the rendered paper (N1–N3).
- **Excitement: 4 / 5.** "Which AI does writing sound like, and does the answer depend on the model's vintage?" is a genuinely new and useful framing for the homogenization track. The single-generator 2026 split, replicated with logged-decoding open models, is the most interesting result in the paper.
- **Overall assessment: 3.5 / 5.** Borderline main conference / strong Findings. With N1–N5 fixed and the claims in §3b and §3d narrowed, I would support main-conference acceptance.
- **Confidence: 4 / 5.** I read all the analysis code, reproduced the vintage results at seed 0 and ran the reanalyses above. I did not check the cited cutoff dates beyond Table 1.

---

## 9. The five most important changes, in order of impact

1. **Narrow the two vintage claims to what the data show.**
   - Drop "a fixed reference set shows the shift fading as its models age" and the parallel Discussion sentence about *delve*. Replace them with the period-specific statement in §3d.
   - Acknowledge that the 14-generator fixed set rose in 2026, and remove the incorrect explanation of why it "flattened".
   - Describe the pre-ChatGPT-*pretraining*-data region as excluding the reverse-learning channel, not as "identified".
   - Report its own drift placebos, which pass (R3), next to the controlled local-pair estimate (3.5 pp).
   - Say that the component had fallen from 11.0 to 4.7 pp above trend by 2026.
2. **Fix the false statements in the rendered paper:**
   - the `make_numbers.fmt` "lo"/"hi" bug (dispersion CI, logit gaps), with asserts and a grep of all affected keys;
   - the §6.5 marker sentence (Granite 4.2);
   - the Figure 2 caption;
   - "at most a quarter";
   - the archive-weighting sentence in §4;
   - "training data" → "pretraining data".
3. **Put uncertainty on the vintage design:**
   - per-generator 2025→2026 Δ with bootstrap CIs and a seed range (the human training draw), with a tie band;
   - drift placebos for the matched region (Table 2);
   - the placebo grid at a 30-month horizon;
   - a small table of all six pre-ChatGPT-data region definitions.
4. **Add the cutoff axis.**
   - Fill Table 1's cutoffs from model cards, flagging gpt-oss.
   - Plot the 2025→2026 Δ, and each region's yearly capture curve, against training cutoff, as well as against release month.
   - Discuss post-training style (reasoning RL, synthetic data) as a third explanation alongside "authors use new models" and "models learned from new abstracts".
5. **Close the remaining round-2 items:**
   - the never-revised check (report it; it helps you);
   - astro-ph and econ level shifts;
   - a field-specific TPR and trend-based FPR in the implied-prevalence calculation;
   - the 113 NaN-source Hansard generations and over-quota rows;
   - a feature-level decomposition of the 2015–22 → 2025–26 shift, with an ablation of LLM-favoured function words.
