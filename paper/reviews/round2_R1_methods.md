# ARR Review, Round 2: Reviewer 1 (methods, identification, statistics)

**Paper:** "After the Delve Fades: Scientific Abstracts Keep Moving Toward LLM Style"
**Track:** Homogenization and knowledge collapse in LLMs
**Reviewer expertise:** computational social science, observational time series and causal inference, statistical learning.

**What I examined**
- `paper/main.tex` and the compiled PDF.
- `results/numbers.tex` and the raw result files in `results/`.
- All of `code/` (`analysis.py`, `mso.py`, `features.py`, `fetch_arxiv.py`, `build_sources.py`, `generate.py`, `claude_prompts.py`, `perplexity.py`, `make_numbers.py`).
- `preregistration.md`, and my own round-1 review with the authors' response plan.
- Read-only reanalyses of the cached features in `F:\research-data`. I imported the authors' own `mso.py` and `analysis.py` and used the same seed. My refit reproduces the primary instrument exactly: overall MSO 22.83% and pre-ChatGPT MSO 9.23%, identical to `arxiv_instrument.json` and `arxiv_baseline_pre2022.csv`. Every number below that is not in the paper comes from those runs. The scripts are in my scratch folder, not in the project.

---

## Summary

The paper defines Machine-Style Overlap (MSO) as the share of a genre's documents that a calibrated classifier places on the LLM side of a likelihood-ratio-one boundary. The classifier is trained on pre-ChatGPT human text against text from 14 reference generators, using features that exclude content words: function words, POS trigrams, dependency labels, punctuation, sentence and word length, and MTLD. The main claims are:

- **Baseline (H1).** 9.2% of pre-ChatGPT arXiv abstracts were already in the region, varying by archive from 4.5% (astro-ph) to 15.7% (econ).
- **Shift (H2).** MSO rose to 45.0% in 2026. The June-2025 interrupted-time-series (ITS) gap is 25.7 pp (CI 23.4–28.0). It survives threshold, notation, topic, length and dash checks, and is absent at two placebo breaks and in a "drift placebo" that uses a 2015–2018 instrument.
- **Comparison genre (H3).** Australian Hansard did not move measurably (1.7 pp), and the arXiv–Hansard difference is 30.6 pp.
- **Field gradient (H4).** The gap is largest in q-bio and cs and smallest in math and astro-ph.
- **Marker words.** Marker words peaked in 2024 and receded while MSO kept rising.
- **Generator set.** The 2026 trajectory depends on the generator set.
- **Dispersion.** Stylistic dispersion has declined steadily since 2015.
- **Learner essays (H5).** In PERSUADE, ELL essays are *less* machine-like than non-ELL essays. A perplexity instrument reproduces the TOEFL bias reported by Liang et al. on Liang's own data, which the paper reads as "detector bias depends on the population, not on non-native authorship".

The revision is a large improvement over round 1:
- The sampler bug is fixed.
- LaTeX dashes and math are normalised.
- Length, notation, topic and dash checks are in place.
- Generator-set sensitivity is reported openly.
- A drift placebo now exists.
- The Bayes-error language is appropriately hedged.

**I verified that the core arXiv shift is real and robust to the composition confounds I raised in round 1** (see "Reanalyses" below). The remaining problems concern three things:
1. What the shift is measured *against*: the LLM side of the instrument is partly post-treatment.
2. The two headline narrative claims built on it: "marker words understate the shift" and "keeps moving".
3. The comparison genre, the dispersion and learner side-results, and several reporting and code–text mismatches.

---

## Strengths

1. **A useful estimand.** Reframing the pre-period "LLM share" of prevalence studies as an overlap quantity is sensible. The classify-and-count framing (Forman 2008) is correct, and §3 now states that a finite classifier's flag rate is not a bound on the Bayes quantity.
2. **The core arXiv shift is robust. I tried to break it and could not.** Using the authors' instrument:

   | Check | June-2025 gap (pp) |
   |---|---|
   | Equal weight per archive | 26.9 (24.2–29.6) |
   | Reweighted to the pre-period mix of *primary subcategory* (cs.CL, cs.LG, cs.CV, math.PR, …) | 23.8 (21.9–25.8) |
   | Never-revised papers only, so the text is v1 in every period and the revision selection near the break is neutralised | 25.8 (23.4–28.2) |
   | Reweighted to the pre-period submission-hour (UTC) mix within archive, a crude author-region proxy | 25.6 (23.3–27.8) |

   - **Rises within subcategories:** cs.DS from 3.6% before ChatGPT to 32.1% in 2026, cs.IT from 5.9% to 36.4%, math.AP from 6.7% to 19.1%, so the rise is not a cs.CL/cs.LG composition story.
   - **Training-draw variance is small:** with seeds 1–4 the gap is 25.5–27.2.
   - **Placebo breaks:** over 54 fake break dates from 2017-01 to 2021-06, the arXiv placebo gaps range from −1.5 to +4.6 pp, and only 2% have p<0.05.
3. **The drift placebo is the right design.** It reproduces the main design's asymmetry: in-distribution before the boundary and out-of-distribution after it. It is also conservative in one respect: the LLM side still contains P1 and P2 texts seeded from 2019–2022 abstracts, which should *favour* a spurious gap, yet it finds −0.5 pp.
4. **Instrument sensitivity does not explain the Hansard null.** In my cross-validated check, LLM revisions of human drafts (P2) are recalled *more* often by the Hansard instrument (75.5%) than by the arXiv instrument (62.7%).
5. **Transparency.** Numbers are inserted from result files by macro (with one formatting bug, below). The paper includes the held-out-generator table, the generator-set table, an honest deviation list, H5 reported as unsupported, and a candid AI-use statement.
6. **The held-out 2026-model result is valuable on its own:** recall is 20.7% on abstracts and 35.3% on essays. It matters for detection research beyond this paper.

---

## Weaknesses (most severe first)

### W1. The LLM side of the instrument is partly post-treatment, so the headline gap mixes "humans moved toward LLMs" with "later LLMs learned from later humans".

An ITS needs an instrument fixed before treatment. Here only the human side is pre-treatment. Several generators were trained on data that overlap the outcome period:
- Qwen3, Gemma 3, gpt-oss, Phi-4 and Granite 3.3 (2024–2025 releases).
- Above all Claude Opus 5.5 (2026), whose pretraining almost certainly contains 2023–2025 arXiv abstracts.

If abstract style changed after 2022 for *any* reason, models trained on those abstracts reproduce the change. A region built from them then captures post-2022 human text more readily. This bias runs in the direction of the finding and is not separable from the paper's interpretation. The paper's own reading of §6.5, "abstracts moving away from 2023-era LLM style toward the style of later models", is observationally equivalent to "later models' style moved toward recent abstracts".

The paper's own numbers bear this out:
- **The RAID-only region is the only one whose generators largely predate post-ChatGPT human writing** (GPT-4 and ChatGPT with 2021 cutoffs, and 2023 chat models). It gives a gap of **5.9 pp (2.8–8.9)**, and MSO falls from 17.2% in 2025 to 10.9% in 2026.
- **The gap grows with how recent the generators are:** RAID 5.9 → all-but-2026 22.7 → all 25.7 → local 29.1 → local+2026 model 32.3.
- **The 2026 continuation that gives the paper its title rests on one generator.** That generator was:
  - added after a preliminary run showed a decline;
  - run without decoding control, in batches of 50 prompts per agent context (`claude_prompts.py`), so its outputs are not independent draws;
  - the same system that drafted the paper.
- **The drift placebo answers a different question.** It shows that the modern-generator region does not reward 2019–2022 abstracts over 2015–2018 ones. It cannot test post-2022 human text that is in those models' training data.

**Fix.**
- Define a pre-specified **pre-treatment region** from instruction-tuned generators whose training cutoff is at or before 2022. Examples are RAID's ChatGPT and GPT-4, text-davinci-003, FLAN-T5/OPT-IML, and LLaMA-1-based Alpaca/Vicuna. Make its gap the primary identified estimate.
- Present the regions that include later generators as descriptive, "vintage-matched" measurements.
- Add a vintage curve: single-generator regions, with each generator's yearly capture of human abstracts plotted against its training cutoff. If capture peaks at the cutoff, the recency mechanism is confirmed.
- Put the generator-set range (5.9–32.3 pp) in the abstract next to 25.7.
- Regenerate the 2026-model texts with one prompt per call and logged decoding settings, or demote them to a sensitivity analysis.

### W2. The marker-word versus MSO contrast compares different generator vintages, so the title claim is not established.

Marker words (*delve*, *intricate*, *showcase*) were identified from 2023–2024 ChatGPT output. The MSO series they are compared with is dominated by 2024–2026 generators. The like-for-like comparison is the 2023-era region (RAID-only) against 2023-era markers, and there **both rise and then recede**: markers go 1.1 → 5.3 → 1.5%, RAID-only MSO goes 7.1% (2022) → 14.9% (2024) → 17.2% (2025) → 10.9% (2026). The paper notes this in §6.5 ("retracing the marker-word curve"), but the abstract, title and §6.4 still conclude that "marker-word counts understate how far scientific abstracts have moved toward LLM style".

What the data support is narrower: abstracts receded from *2023-era* LLM style in both lexical and stylistic terms, and they overlap increasingly with *current* models' style, for which W1 gives a competing explanation.

**Fix.**
- Retitle, or qualify "keep moving".
- In §6.4, compare markers against the RAID-only region.
- Derive marker words from the same 2024–2026 generators (excess-vocabulary on your own LLM sample) and track them alongside the vintage-matched region.

### W3. The comparison genre fails its own placebo tests, and several Hansard results are omitted.

- **Unreported placebo failures.** `hansard_its.json` contains the Hansard placebo results, and the paper does not report them:
  - break at 2019-11: gap −2.5 pp, **p=0.010**;
  - break at 2020-11: gap −2.8 pp, **p<0.001**.
- **The failures are systematic.** Over 54 fake breaks (2017-01 to 2021-06), **54% of Hansard placebo gaps have p<0.05**, ranging from −5.5 to +0.1 pp. The Hansard ITS standard errors are therefore anti-conservative. A gap of 1.7 pp with a CI of −0.6 to 4.0 cannot be called "did not move measurably" when pre-period noise produces ±5 pp "effects".
- **Possible cause.** Newey–West lags are applied by row, but Hansard has 92 non-contiguous months over a 126-month span. Only three months of 2025 exist, while the evaluation month is 2025-06.
- **Unreported significant Hansard results:**
  - At threshold 0.6, the Hansard gap is **1.8 pp (CI 0.3–3.2), p=0.018**.
  - The Hansard **marker-word gap is 1.6 pp, p=0.011**.
  - On a relative scale, Hansard yearly MSO went from about 5.4% before ChatGPT to 7.4% in 2024 (+37%).
- **Classifier agreement is low for Hansard.** κ between the logistic and gradient-boosted instruments is **0.27** (`hansard_instrument.json`), against 0.65 for arXiv. The Hansard ITS was never run with the gradient-boosted instrument.
- **H3 survives.** A 30.6 pp difference is not threatened by these problems, and Strength 4 shows that sensitivity is not the cause. But the Hansard half of the narrative is overstated, and the CI of the difference inherits the anti-conservative standard error.

**Fix.**
- Report the Hansard placebos.
- Base Hansard inference on the empirical placebo distribution (a permutation over break dates), or on standard errors that respect calendar gaps.
- Report Hansard at all three thresholds, with markers and with the gradient-boosted instrument.
- Describe Hansard as having "moved little in absolute terms, with a small, threshold-dependent rise", not as "did not move".

### W4. The dispersion result (§6.7) is largely a length artefact.

Features are per-token rates, and their sampling variance falls with document length. Median abstract length rose from 149 to 176 words, so the mean distance to the centroid falls mechanically. I reproduced the paper's series exactly (34.20 → 31.94 → 30.86) and then held length fixed:

| Sample | 2015 | 2022 | 2026 |
|---|---|---|---|
| Abstracts of ≥250 words, all truncated to exactly 250 (300 per year) | 37.33 | 36.88 | **37.33** (no decline) |
| Abstracts of 140–179 words (1,000 per year) | 33.52 | 32.56 | 32.17 (about 40% of the reported decline) |

The archive mix also shifts in the same window: astro-ph and math fall from 47% of the sample in 2015 to 28% in 2026. The claim that "abstracts have grown stylistically more uniform" since 2015 is therefore not supported. On the theme track, this is the paper's only direct homogenization measure.

**Fix.** Compute dispersion on length-matched (or fixed-length) samples within archive, with bootstrap CIs. Otherwise drop the section, or report it as null.

### W5. H1 field heterogeneity and the H4 "dose" ordering are confounded with length and with field-specific sensitivity.

**Length.** Pre-ChatGPT MSO falls steeply with abstract length: **13.8% in the shortest quintile (median 86 words) against 4.5% in the longest (247 words)**. After standardising each archive to the common length distribution, the baselines are:

| Archive | Raw baseline | Length-standardised |
|---|---|---|
| astro-ph | 4.5% | 6.3% |
| math | 9.0% | 6.8% |
| econ | 15.7% | 14.5% |

Math becomes one of the two lowest fields. The χ² test on n=37,512 is uninformative about mechanism, and the paper's list of explanations ("the writing, classifier fit, or both") omits length.

**Field sensitivity.** Cross-validated recall of LLM revisions of human drafts (P2) by source archive: astro-ph 0.48, math 0.57, econ 0.58, cond-mat 0.61, stat 0.68, eess 0.70, cs 0.73, q-bio 0.76. The archives with the largest gaps are the ones where the instrument detects LLM revision best. Correcting crudely for this, as gap/(recall − baseline FPR), the ordering survives (cs about 62 against math about 22), but the magnitudes compress. Comparing raw percentage-point gaps across fields mixes adoption with detectability, and the comparison with prevalence-study rankings needs this caveat.

**Fix.**
- Report length-standardised baselines.
- Report sensitivity-corrected field gaps, for example by injecting known fractions of P2 revisions into held-out pre-period abstracts per archive.
- Formally test H4 as a cs − math difference.

### W6. ITS specification and inference.

- **The linear post-segment does not fit.** The post-period is clearly curved (yearly 17.4, 27.7, 40.6, 45.0). The June-2025 linear gap is 25.7, while the non-parametric observed-minus-extrapolated-trend values are 6.2, 16.1, 28.6 and 32.6 pp for 2023–2026. The direction is conservative, but the headline depends on an arbitrary evaluation month, which deviation 6 admits was not in the plan.
- **A negative break needs explaining.** astro-ph has a significant **negative** level shift at December 2022 (−3.5 pp, p=0.001). It persists among never-revised papers (−3.3 pp, p=0.012), so it is not caused by the revision exclusion. That is either misspecification or a real discontinuity unrelated to LLMs, and the paper should investigate it.
- **Revision selection near the break is concentrated at the end of the pre-trend.** The exclusion rule drops 22.1% of 2022 and 7.8% of 2021 papers, against <1% for 2015–2018. My never-revised reanalysis shows this does not matter for the overall gap, but it should be reported.
- **Excessive precision.** p-values such as 10⁻¹¹⁰ convey false precision for a model-based extrapolation whose dominant uncertainty, the generator set, is excluded by construction.
- **Clustering.** The baseline CI ignores the archive-month cluster design. A cluster bootstrap gives 8.87–9.61 against the reported 8.9–9.5. This is small but should be fixed.

**Fix.**
- Show an event-study plot of monthly observed-minus-counterfactual values with pointwise CIs.
- Report yearly non-parametric gaps as the primary summary and the linear-fit gap as a secondary one.
- Drop the extreme p-values.
- Use cluster bootstraps.
- Discuss the astro-ph break.

### W7. Remaining confounds that the checks cannot reach.

The added checks cover topic, through a regex for LLM terms, along with notation, length and dashes, and my reanalyses add subcategory, revision and submission hour. Three confounds remain:

1. **Non-LLM writing tools adopted in the same window.** Grammarly, DeepL Write, Writefull and Overleaf assistants partly use LLMs, so "LLM style" here includes "AI-assisted editing".
2. **Author-population change**, including country and career stage. Submission hour is only a crude proxy.
3. **Closed-class features still carry lexical markers.** In my decomposition of the 2015–2022 → 2025–2026 shift on the linear logit, the largest contributors are MTLD, comma rate, a falling rate of *of*, adverbial clauses (*advcl*), hyphens, falling *is* and *are*, and a rising **fw:across**. *Across* is a well-known LLM-favoured word that enters through the "function word" channel. This is not fatal, since the shift is spread over many features, but "content-word-free" does not mean "marker-free".

**Fix.**
- Report a feature-level decomposition of the shift.
- Run an ablation dropping closed-class words with known LLM overuse (*across*, *within*, *through*, *while*).
- Run an author-panel analysis: the same first authors before and after, with author fixed effects. This is feasible from arXiv metadata, and it is the cleanest composition control.

### W8. The learner and perplexity analyses overreach and are off-theme.

1. **Possible pretraining contamination.** Qwen2.5-0.5B (2024) was very likely trained on PERSUADE (released through the Kaggle Feedback Prize competitions in 2021–2022), on Liang et al.'s TOEFL release (2023), and possibly on the US 8th-grade essays, which appear to come from the public Kaggle ASAP set. Differential memorisation lowers perplexity and directly affects which groups get "flagged".
   **Fix:** replicate with a model whose training cutoff predates all three releases, such as GPT-2 or Pythia.
2. **The generalisation is not identified.** "Detector bias depends on the population, not on non-native authorship" rests on two samples (n=91 and n=88) that differ in genre, task, length, era and proficiency, and on one 0.5B scoring model. The proposed mechanism ("predictable, formulaic text") is measured only by perplexity itself, so the explanation is circular.
3. **Adjusting for proficiency is adjusting for a mediator.** The OR moves from 0.53 to 0.82, and its CI (0.47–1.43) contains the unadjusted estimate. That supports "partly", not "mostly". The continuous margin (−0.37 → −0.12 SD) is the better evidence and should be the one stated.
4. **Focus.** The analysis takes three sentences of the abstract in a paper about homogenization of scientific writing.

**Fix.** Move the learner and perplexity analyses to an appendix or a companion paper, and reword the claim as "is not a fixed property of non-native authorship".

### W9. Code–text mismatches and data-integrity issues.

1. **"So every archive-month has the same design weight" is false.** Cells hold between about 5 documents per month (econ, 2015) and 200 (cs and math after 2020). `monthly()` weights documents, not cells, and the archive mix shifts substantially (eess from 1.5% to 15%, econ from 0.8% to 8.3%, astro-ph and math from 47% to 28%). The equal-archive series gives 26.9 pp, so the consequence is small, but the text must match the estimator. Either implement the design weights that the response plan promised ("equal field weights for 'all' series") or correct the sentence.
2. **"For each of 8.00 archives"** (§4). `make_numbers.fmt` does not treat `arxiv_n_fields` as an integer.
3. **The AI-use statement still contains `\TODO{confirm after the author's spot-check}`.** That sentence asserts a human citation check which the TODO says has not been confirmed. It must not be submitted in this state.
4. **113 Hansard generations have `src_id = NaN`** in `llm_hansard.jsonl`: 38 from llama3.1, 26 from qwen3, 22 from gemma3, 18 from mistral and 9 from gpt-oss, 33 of them P2 revisions. For these rows, speaker grouping in cross-validation and calibration fails, and the rule "seed documents are never measured" (`build_sources.py`) cannot be enforced. The feature cache holds 113 lines with a NaN id. Some local generators also have more than 450 Hansard rows (llama 469, qwen 463), against "150 times each".
   **Fix:** regenerate or drop these rows.
5. **Some promised analyses are missing or undated:**
   - The pre-registration promised an embedding-classifier sensitivity analysis for arXiv; it was run only for essays.
   - The gradient-boosted instrument is never used for any ITS.
   - Deviation 4 lists the drift placebo as "added after review", but the paper does not state when each robustness check was specified relative to seeing results.
6. **Inconsistent §6.5 wording.** It says "regions that include 2024–2026 models keep rising" and "without the 2026 model the series levels off (38.1% to 37.2%)". But the local-only region, which has no 2026 model, *rises* (42.4% → 48.3%), and the no-frontier region, which *includes* the 2024–2025 local models, levels off. The difference is driven by including RAID's 2023 models against including the 2026 model. The abstract's sentence ("regions that include current models show it continuing") is inaccurate for the same reason.
7. **2026 covers January–September only**, and the yearly comparison with full-year 2025 does not say so.

### W10. Uncertainty reporting understates the dominant source of variation.

§3 discloses that CIs exclude instrument variation, which is good. But the abstract still reports "25.7 pp" as if it were a fixed population quantity. Training-draw variance is negligible (±1 pp in my seed reruns). The generator-set variance (5.9–32.3 pp) is about 12 times the width of the reported sampling CI.

**Fix.** Report the headline as a range across pre-specified generator sets, or as a mean with between-set variance, and put that range in the abstract.

---

## Questions for the authors

1. What are the training-data cutoffs of each generator? Does a single-generator region's capture of human abstracts peak near that generator's cutoff?
2. Was the frontier model given any system prompt or tool access (for example, web search) during generation? How many sessions were there, and were batches of 50 prompts answered in one context?
3. Why does astro-ph show a significant negative level shift at December 2022?
4. Why are the Hansard placebo results, the threshold-0.6 result and the marker result not reported? How do the Hansard placebo results change with HAC lags defined on calendar time?
5. Can you reproduce the perplexity results with a model trained before PERSUADE, the TOEFL essays and ASAP were public?
6. Can you run an author-panel version of H2, with first-author fixed effects?
7. When was each Table 1 robustness check specified, relative to seeing the primary result?

---

## Numbers verified against raw result files

All of the following match the result files after `make_numbers` formatting.

| Paper text | Value in paper | Source file and key | Raw value |
|---|---|---|---|
| Pre-ChatGPT arXiv MSO | 9.2% (8.9–9.5) | `arxiv_baseline_pre2022.csv` all | 0.0923 (0.0895–0.0951) |
| astro-ph, cs, econ baselines | 4.5 / 13.0 / 15.7 | same file | 0.0448 / 0.1305 / 0.1568 |
| Yearly MSO, 2022–2026 | 11.1 / 17.4 / 27.7 / 40.6 / 45.0 | `arxiv_yearly.csv` | 0.1109 / 0.1741 / 0.2773 / 0.4064 / 0.4499 |
| Trend gap | 25.7 (23.4–28.0) | `arxiv_its.json` all.excess | 0.2569 (0.2343–0.2795) |
| Drift placebo | −0.5 (−1.9 to 0.9), p=0.489 | `arxiv_drift_placebo.json` | −0.00505 (−0.0194 to 0.0093), 0.489 |
| Hansard gap | 1.7 (−0.6 to 4.0) | `hansard_its.json` all | 0.0169 (−0.0058 to 0.0397) |
| arXiv − Hansard | 30.6 (27.9–33.3) | `control_difference.json` | 0.3061 (0.2794–0.3328) |
| Field gaps q-bio / cs / math / astro-ph | 37.9 / 37.4 / 10.4 / 14.3 | `arxiv_its.json` | 0.379 / 0.374 / 0.104 / 0.143 |
| Generator-set gaps | 22.7 / 29.1 / 5.9 | `arxiv_gensets_its.json` | 0.2271 / 0.2906 / 0.0586 |
| RAID-only 2025 → 2026; no-frontier; local+frontier 2026 | 17.2 → 10.9; 38.1 → 37.2; 57.6 | `arxiv_gensets.csv` | matches |
| Held-out 2026-model recall (arXiv / essays) | 20.7 / 35.3 | `arxiv_lomo.csv`, `essay_lomo.csv` | 0.2067 / 0.3533 |
| Markers | 1.1 → 5.3 → 1.5; r=0.12; 5.9 vs 1.4 | `arxiv_yearly.csv`, `arxiv_marker_vs_mso.json` | matches |
| ELL | 2.3 vs 4.3; OR 0.53 (0.31–0.92); 0.82 (0.47–1.43) | `essay_mso_by_group.csv`, `essay_ell_adjusted.json` | matches |
| Perplexity | 7.4 vs 16.0; OR 0.46; TOEFL 42.9% (2.68); US 8th grade 3.4% (3.34) | `essay_perplexity_*.json/csv`, `essay_liang_perplexity.csv` | matches |
| Dispersion | 34.20 / 31.94 / 30.86 | `arxiv_dispersion.csv` | matches |
| κ; classifier-family MSO | 0.65; 22.8 vs 22.7 | `arxiv_instrument.json` | 0.646; 0.2283 / 0.2271 |

The only rendering error is "8.00 archives" (W9.2).

## Reanalyses run for this review

All use the authors' own code, seed 0, and read-only access to the data.

| Analysis | Result |
|---|---|
| Refit of the primary instrument | Reproduces 22.83% / 9.23% exactly |
| Equal-archive-weight series | Gap 26.9 (24.2–29.6) |
| Reweighting to the pre-period primary-subcategory mix | 23.8 (21.9–25.8) |
| Never-revised papers only | 25.8 (23.4–28.2) |
| Submission-hour reweighting | 25.6 (23.3–27.8) |
| Seeds 1–4 | Gap 25.5 / 27.0 / 26.4 / 27.2 |
| Placebo distribution over 54 breaks | arXiv: 2% with p<0.05, max \|gap\| 4.6; Hansard: **54% with p<0.05**, max \|gap\| 5.5 |
| Pre-period MSO by length quintile | 13.8 / 11.4 / 10.0 / 6.4 / 4.5% |
| Length-standardised field baselines | astro-ph 6.3, math 6.8, cond-mat 7.8, eess 10.3, q-bio 10.6, stat 11.3, cs 13.4, econ 14.5 |
| Dispersion with length held fixed | Flat (≥250 words) or about 40% of the reported decline (140–179 words) |
| P2 cross-validated recall | arXiv 0.627, Hansard 0.755; by archive 0.48 (astro-ph) to 0.76 (q-bio) |
| Non-parametric yearly gaps | 6.2 / 16.1 / 28.6 / 32.6 pp for 2023–2026 |
| Cluster-bootstrap baseline CI | 8.87–9.61 |
| astro-ph level shift among never-revised papers | −3.3 pp, p=0.012 |

---

## Scores

- **Soundness: 3 / 5.** The core arXiv shift is well supported and survives every composition check I could devise. The identification of *what* it is a shift toward (W1, W2), the comparison-genre inference (W3) and the dispersion claim (W4) are not.
- **Excitement: 3.5 / 5.** The overlap estimand and the generator-vintage finding are interesting and on-theme. The narrative headline overstates what is identified.
- **Overall assessment: 3 / 5** (Findings-level as it stands; main-conference level if W1–W4 are addressed).
- **Confidence: 4 / 5.** I read all the code, reran the primary instrument and checked the main numbers.

---

## Required changes for acceptance

1. **Pre-treatment region (W1).**
   - Add a pre-specified region built from generators with training cutoffs at or before 2022, and report its gap as the identified estimate.
   - Present later-generator regions as vintage-matched descriptions.
   - Put the generator-set range in the abstract.
   - Discuss the training-data recency mechanism explicitly.
2. **Marker-word claim (W2).** Reword the title, abstract and §6.4 so they no longer claim that marker words understate the shift, unless a vintage-matched comparison supports it. The like-for-like comparison currently shows both receding.
3. **Hansard (W3).**
   - Report the Hansard placebos, the threshold-0.6 and marker results, and gradient-boosted results.
   - Use placebo-calibrated or calendar-aware inference.
   - Soften "did not move measurably".
4. **Dispersion (W4).** Redo §6.7 on length-matched samples, or remove the homogenization claim.
5. **Baselines and field gaps (W5).** Report length-standardised baselines and sensitivity-corrected field gaps, and test H4 formally.
6. **Fix the code–text mismatches (W9):**
   - the design-weight sentence, or implement the weights;
   - "8.00";
   - the leftover TODO in the AI-use statement;
   - the 113 NaN-source Hansard generations;
   - the §6.5 and abstract description of which regions "continue";
   - mark 2026 as January–September.
7. **Learner analysis (W8).** Rerun the perplexity analysis with an uncontaminated, pre-2021 scoring model. Narrow the claim to "not a fixed property of non-native authorship", and move it out of the abstract.
8. **Robustness in the paper (strengths and W7).** Add the subcategory-reweighted, never-revised, equal-archive and placebo-distribution analyses, which strengthen the paper. Add a feature-level decomposition of the shift.
