# ARR Review — Reviewer 1 (methods / identification)

**Paper:** "Sounding Like AI Before AI: Machine-Style Overlap in Human Writing"
**Reviewer expertise:** computational social science, causal inference with observational time series, statistical learning.
**Materials examined:** `paper/main.tex` and the compiled PDF, `results/numbers.tex` and every raw file in `results/`, all of `code/`, and `preregistration.md`. I also ran a few read-only reanalyses on the authors' cached features in `F:\research-data`, using the authors' own `mso.py` with the same seeds. My scripts are in my scratchpad and I can share them. Where I quote a number that is not in the paper, it comes from those runs.

---

## Summary

The paper defines Machine-Style Overlap (MSO): the share of a genre's documents for which a calibrated classifier, trained on balanced pre-ChatGPT human text and LLM text and using "topic-robust" style features (function words, POS trigrams, dependency labels, punctuation, sentence and word length, MTLD), gives P(LLM) ≥ 0.5. The paper argues that for pre-LLM text MSO is "the human half of a Bayes error" and is therefore a property of the population, not estimator noise. Its main empirical claims are:

- H1: about 9.4% of pre-2022 arXiv abstracts are "in the LLM region", ranging from 4.7% (astro-ph) to 16.2% (econ).
- H2: an interrupted-time-series excess of +22.5 points over the pre-2022 trend at June 2025.
- H3: an Australian Hansard control that moved only +1.4 points, giving a difference of 21.1 points.
- H4: a field "dose" ordering, cs highest and math lowest.
- Marker words such as *delve* peaked and receded while MSO kept rising.
- "Chat tuning makes the style."
- H5: English-language learners (PERSUADE 2.0) are *less* machine-like than their peers.
- A "self-test": 20.7% of the paper's own AI-drafted paragraphs fall in the region, against 59.1% of human cs abstracts from 2026.

The question matters and the pipeline is unusually transparent: numbers are inserted by macro, there is a pre-registration, and there is an AI-use statement. That transparency is what let me find the problems below. In its current form, though, the design does not identify what the paper claims. The time-series excess is confounded by a sampling artefact that I verified in the data, by covariate shift under a frozen classifier, and by which generators were included. The "Bayes error" framing does not hold for the estimator used. The control is not comparable. Several secondary claims are selectively reported or rest on a numerically wrong standard error.

---

## Strengths

1. **Useful reframing.** Asking how much human text overlaps with LLM style, as opposed to how much was LLM-produced, is a real contribution. It also explains the pre-period "LLM share" that prevalence studies treat as nuisance.
2. **Transparency.** Every number comes from a results file through `\R{}`. The code is short and readable, the pre-registration and its deviations are public, and the AI-use disclosure is candid. Few submissions allow a reviewer to audit this deeply.
3. **Train/score separation.** The train pool and score pool are disjoint, and prompts are seeded only from the train pool (`build_sources.py`), which avoids the obvious leakage.
4. **Leave-one-generator-out (LOMO) analysis.** This is the right diagnostic. Its most striking result is that a held-out 2026 frontier model is recalled only 20.9% of the time against 94.6% for GPT-4, and that result is interesting in its own right.
5. **Honest flagging of fragility in the learner analysis.** The seed-stability analysis (OR p<0.05 in only 3 of 10 draws) is reported rather than hidden.
6. **Separation by prompt type.** The finding that P2 (LLM revision of a human draft) is the hardest case is useful and correctly emphasised.

---

## Weaknesses (most severe first)

### W1. The arXiv sampler truncates high-volume cells, and this creates a composition shift that coincides with the post-period. (Verified bug.)

`fetch_arxiv.py` requests at most `max_results=400` per field-month window and sorts by `submittedDate` **ascending**. The window lengths are fixed for the whole 2015–2026 period (cs = 2 days). Once a window holds more than 400 entries (including cross-lists, which are dropped afterwards), the sample keeps only the *earliest-submitted* papers. I checked `arxiv/sample.jsonl`:

- **Days actually covered by a cs window:** 2.00 every year through 2023, then 1.67 in 2024, 1.58 in 2025 and **1.00 in 2026**. Math falls to 2.56 days in 2026.
- **Share of the cs sample submitted 00:00–12:00 UTC:** 0.41–0.44 in 2015–2019, about 0.49–0.54 in 2020–2025, and **0.72 in 2026**. Because the cap keeps the earliest submissions, the late-period cs sample is increasingly made up of early-UTC submitters, which mostly means authors in East and South Asian time zones.

The aggregate series is therefore built from a design-driven mixture whose author-region composition changes exactly in the treatment period, and most sharply in 2026, the year behind the claim that "the rise continues". The same problem distorts the "all" estimand:

- The cs sample share grows from 11.8% (2015) to 25% (2021) and then stays flat around 23–25%, while true arXiv cs volume kept growing. So the "all" series weights fields neither by population nor by a fixed standard.
- Standardising to the 2015–2021 field mix, which I computed from `arxiv_monthly_by_field.csv`, changes the yearly MSO from 36.4% to 33.5% in 2025 and from 40.7% to 38.2% in 2026.
- The paper says the sample is "stratified random" with "window length scaled to field size". That is not true after the cap binds.

**Fix.**
- Paginate every window to exhaustion, or use the bulk arXiv metadata snapshot (Kaggle/OAI dump), which avoids the 40-hour harvest the deviation log cites.
- Post-stratify to true field × month submission counts, and report both population-weighted and fixed-mix series.
- Show that results are invariant to submission hour, or reweight on it.

### W2. A frozen classifier under covariate shift is not an interrupted-time-series design. The placebo tests cannot detect this.

The region is trained on 2015–2022 human text and then applied to 2023–2026 text. Any drift in the human style distribution moves documents in score space, whether or not it has anything to do with LLMs. Examples include author composition (the non-native share and country mix; see W1), subfield mix (the rise of LLM-topic papers, named systems and benchmarks), length, and formatting conventions. A discriminative linear model extrapolates, so out-of-distribution human text is not guaranteed to stay on the human side. The paper's own evidence shows how strong this effect is:

- The essay instrument puts **34.1% of TOEFL essays and 51.4% of US college essays** in the region, against 3.2% of in-genre essays (`essay_liang.csv`). Out-of-distribution human text lands in the "LLM region" at 10–16× the in-distribution rate. The paper calls this "near chance". It is evidence that the instrument flags distribution shift.
- **The placebos are uninformative about this.** The 2019-11 and 2020-11 placebo breaks are scored with a classifier trained on the *whole* pre-period, so the placebo months are in-distribution by construction.
- **I ran the correct placebo.** I trained the same pipeline on 2015–2018 human text only and placed a fake break at 2019-01. The excess at 2022-10 is **+3.0 points (95% CI −0.1 to 6.2, p=0.058)**, with a visible jump at the training boundary: 8.9% in 2018, 10.6% in 2019. Pure drift over four pre-LLM years produces a non-trivial excess. The post-period is a 31–45-month extrapolation under faster drift.
- **Reassuring check, which the authors should add.** A crude topic split does *not* explain the rise. Among cs abstracts that never mention LLMs, ChatGPT, GPT-4 or prompting, MSO rises from 13.9% (2022) to 59.5% (2026), about the same as the rise for LLM-topic abstracts. This is in the authors' favour, but it rules out only one confound.

**Fix.**
- Run rolling-origin placebos with the classifier frozen at earlier dates, for example train ≤2017 and test 2018–2022, and so on. Report the distribution of "excess" values that drift alone produces, and judge the post-2022 excess against that distribution, not against zero.
- Add an author-panel design: authors with first-author abstracts in both periods, with author fixed effects. This is the cleanest control for composition.
- Reweight the post-period to the pre-period covariate distribution (field, subfield, length, submission hour, and country proxies where available).
- Add the non-LLM-topic analysis at the subfield level, using arXiv primary categories such as cs.CL, cs.LG and cs.CV.

### W3. "MSO is the human half of a Bayes error" does not hold for the estimator used, and the estimand is not a property of the population.

The identity FPR = MSO(H0) holds for the Bayes classifier η(x) on the true distributions. What is computed is different:

- **The threshold is set by a coarsened classifier.** The region is defined by an isotonic-calibrated L2 logistic model (C=0.1) on a hand-built feature map, with 250-word truncation. Calibration makes P(L | s(x)) ≈ s(x). It does not make s(x) ≈ η(x). Thresholding a coarsened score at 0.5 gives the false-positive rate (FPR) *of that classifier*.
- **The Bayes bound does not split into halves.** The Bayes error lower-bounds the *total* error of any classifier. It does not bound either half. A finite classifier's FPR can be above or below the Bayes FPR, so MSO is neither a lower nor an upper bound on the Bayes human half. The pre-registration's statement that a weaker classifier is "conservative" is also incorrect for one half of the error.
- **The quantity depends on the researcher's design of L.** That design includes the generator set, the prompt mix (P1/P2/P3), the RAID decoding settings (greedy and sampling, with and without repetition penalty), the 450-per-generator cap, the 50/50 prior, φ, and the truncation length. LOMO shows that overall MSO ranges from **18.6% to 22.7%** depending on which single generator is dropped (`arxiv_lomo.csv`). That spread is about eight times the width of the reported baseline bootstrap CI (9.1–9.6).
- **The claim that "prevalence studies that subtract a pre-period share remove exactly this quantity" is wrong as stated.** The pre-period α̂ of Liang et al.'s mixture estimator is a misspecification bias of a word-frequency mixture model. It is not the FPR of a style classifier.
- **The H1 argument is a non-sequitur.** "Estimator noise would be uniform across fields" is false. The FPR of a finite classifier differs across subpopulations whenever their feature distributions differ. I find MSO depends strongly on abstract length: pre-2022 MSO is **14.1% for ≤100 words, 11.9% for 100–150, 8.0% for 150–200, 5.1% for 200–250 and 4.2% for >250**. Astro-ph has the longest abstracts (median 213 words) and the lowest MSO, so the field ranking that H1 rests on is partly a length effect. A χ² test with n = 45,909 rejects uniformity trivially.

**Fix.** Recast MSO as an *instrument-relative* overlap: MSO(G, S; φ, L, f). Drop "population property" and "human half of a Bayes error" from the abstract and contributions, or support them with evidence that the estimate converges:
- MSO as a function of training size and model capacity (logistic regression → gradient boosting → a fine-tuned encoder), approaching a plateau;
- bounds, for example on the Bayes FPR via plug-in divergence estimates.

In addition:
- Propagate instrument uncertainty into every CI (resampling over seeds × generator subsets × prompt mixes) and over the window clusters. The paper itself promises to "treat their spread as part of the uncertainty", but no reported CI does so.
- Report H1 standardised for length.

### W4. The 2026 conclusion depends on one generator added after a disliked result, run under uncontrolled conditions.

The paper says that "in a preliminary run without the frontier model, arXiv MSO appeared to fall in 2026; with it, the rise continues." This is a textbook forking path. I reproduced it:

| Region | 2025 MSO | 2026 MSO |
|---|---|---|
| Without the frontier model | 33.2% | **31.1%** (falls) |
| With the frontier model | 36.1% | 40.7% |

Adding the frontier model changes the 2026 value by about 10 points but the 2015–2022 values by only 1–3 points. The arXiv time series therefore reflects which generators are in the region at least as much as how human writing changed. Further problems:

- The frontier model's abstracts were produced by "sub-agent sessions" in batches of 50 prompts per context (`claude_prompts.py`), with no temperature or seed control and an unknown system prompt. Fifty generations sharing one context are not independent draws.
- The same model family drafted the paper (see W10).
- **Generator-vintage confound.** If held-out frontier-model text is recalled at only 21%, MSO is not monotone in LLM use. When authors switch from 2023-era models to newer ones, MSO can *fall* while LLM use rises. The H2–H4 effects are therefore not interpretable as the magnitude of "human writing becoming machine-like".

**Fix.**
- Fix the generator set in a frozen pre-registration addendum before rerunning.
- Report every time-series result with and without each generator, as LOMO time series rather than only LOMO overall MSO.
- Consider vintage-specific regions: a 2023-era region and a 2025-era region, each tracked over time.
- Mark 2026 as exploratory.
- Generate the frontier-model texts through the API with logged decoding parameters and one prompt per call.

### W5. The Hansard control is not a credible comparison.

1. **Different instruments with different sensitivity.** The Hansard region is far tighter: CV AUC 0.977 against 0.934 for arXiv, and per-generator AUCs for P1/P3 of 0.995–0.9997. With a 3.7% baseline against 9.4%, a given LLM exposure moves Hansard MSO less *by construction*. Subtracting absolute excesses across two different classifiers on two different scales (`control_difference.json`) is not a difference-in-differences.
2. **It shares none of arXiv's confounds.** Field mix, author nationality, sampler truncation and topic drift do not apply to Hansard, so the control cannot rule them out. The only thing it controls for is a generic tendency of classifiers to drift, and even that is instrument-specific.
3. **Its own composition changes at the break.** The May 2022 federal election changed the government and brought in many new members six months before T0. Speaker turnover is a first-order shift for a speaker-level style instrument.
4. **Exposure.** "Spoken speech" in Hansard includes prepared and read speeches, often staff-drafted, and Hansard reporters edit the transcripts. It is not an unexposed genre.
5. **Data issues.**
   - Hansard has 92 non-contiguous months (parliamentary recesses), but the Newey–West lags are applied by row order.
   - Only 3 months of 2025 exist, while the evaluation month is 2025-06.
   - Hansard itself shows a significant slope change (+0.54 pts/yr, p=0.049) and a relative rise of roughly 40% (about 3.9% to 5.6%). The paper describes this as "moved far less".
   - The pre-registration specified Hansard 1998–2025. The paper uses 2015+, and this change is not logged as a deviation.

**Fix.**
- Calibrate each genre's sensitivity by injecting known fractions (1%, 5%, 10%) of P2-revised documents into held-out pre-period text, and report each excess in "equivalent-contamination" units.
- Compare effects on the logit scale or as relative risk.
- Add speaker fixed effects for Hansard, or restrict to members who served across the break.
- Find a within-arXiv control that shares the arXiv confounds. One option is the cleaned abstracts of the same paper's v1 against a later version (see W8f).

### W6. Some top features are encoding artefacts, which breaks measurement invariance.

The strongest LLM-typical features are `pun:—` (coefficient 1.02) and `pun:–` (0.92) (`arxiv_features_llm_typical.csv`).

- **No human abstract has these characters.** I counted: **0.0% of human arXiv abstracts contain a Unicode em or en dash in any year 2015–2026**, because arXiv abstracts are LaTeX source. Among generators, 51% of gpt-oss and 24% of gemma3 abstracts contain one. These features separate LLM text by encoding, not style, and they inflate the AUCs that support the separability claims.
- **Humans write the same choice differently, and the instrument cannot see it.** Human authors write dashes as `--` or `---`. The share of human abstracts with a LaTeX dash is flat at about 4.5–5% through 2024, then rises to **7.7% in 2025 and 12.0% in 2026**. That is plausibly LLM-influenced dash use, but the `PUNCT` list in `features.py` counts only a single `-`.
- **Other encoding asymmetries.** About 30% of human abstracts contain `$...$` math, and LLM outputs encode math differently. The other features I would expect to be affected by encoding or naming conventions are `PROPN_PROPN_*` trigrams (capitalised method and benchmark names, which grow after 2022) and the asymmetric `pun:(` (human-typical) against `pun:)` (LLM-typical).

**Fix.**
- Normalise dashes in both populations to one representation (LaTeX → Unicode or the reverse).
- Replace math spans with a placeholder token in both populations.
- Add a measurement-invariance check: features whose human-side support is zero should be removed.
- Rerun everything, and report how the AUCs and the excess change.

### W7. Specification and inference in the ITS.

- **The linear post-segment is misspecified.** Yearly MSO accelerates (+6.0, +8.7, +11.0 and +4.3 points per year from 2023 to 2026), and the marker series rises then falls. A single linear post-slope cannot represent either shape. Symptoms of the misspecification:
  - significant **negative** level shifts at December 2022 in astro-ph (−2.5 pts, p=0.008) and cond-mat (−2.5 pts, p=0.050), which make no sense as treatment effects;
  - a marker "excess" of 1.9 points that comes from a line fitted to a hump.
- **The headline "excess at 2025-06" is a 31-month extrapolation** of a 2015–2022 linear trend, and its CI does not include trend-model uncertainty, for example from alternative pre-trend functional forms.
- **CIs ignore both the cluster design and instrument variance.** Sampling is in field-month windows, but the bootstraps treat documents as independent, and the instrument variance from W3 is left out.
- **Unreported results and missing controls.** Placebo slope changes are not reported (2019-11: +0.35 pts/yr, p=0.14). Seasonality, such as conference-deadline cycles in cs, is not modelled.

**Fix.**
- Use an event-study specification with yearly or quarterly post-period indicators.
- Report observed minus counterfactual with uncertainty from a block bootstrap over field-month clusters, crossed with instrument resampling.
- Show sensitivity to quadratic or spline pre-trends and to the pre-trend window.
- Report all placebo parameters.

### W8. Code–paper mismatches and reporting errors.

**a. The described data do not exist in the results.** The paper describes "Seven open-weight models (… Phi-4 14B, Granite 3.3 8B)". No results file contains Phi-4 or Granite: `*_lomo.csv` and `*_separability.csv` list five local models plus the frontier model and RAID. The Data section describes data that were not used.

**b. The grouped-CV claim is false in two places.**
- For Hansard, `training_set` groups human documents by `grp` (the *speaker*) and LLM documents by `src_id` (the *speech* key `hansard:date:order`). A P2 revision and its source speech therefore have different group labels and can fall into different folds.
- In all genres, `CalibratedClassifierCV(cv=5)` uses ungrouped stratified folds, so the isotonic map that *defines the 0.5 threshold* is fitted without grouping.

**c. Hard-coded numbers.** The text contains literals: "159,102", "seven", "8 fields", "150", "450". This contradicts "every number in this paper is inserted automatically."

**d. Missing appendix.** Appendix A is a red `\TODO`, and the main text cites it for the LOMO evidence.

**e. Latest-version abstracts are dated by v1.** Every arXiv id carries a version suffix, and 42% of pre-cutoff abstracts are v2 or later. The API returns the *latest* abstract text but the v1 date, so some "pre-LLM" training and baseline abstracts are post-2022 revisions. My coarse check found v2+ abstracts about 1–2 points more in-region, with no significant 2021–22 interaction (p=0.73), so the bias seems small. The design is still wrong for a paper whose central object is the *pre-LLM* baseline. Record `updated` and restrict H0 to abstracts last revised before 2022-11-30.

**f. Prompt count.** "15 prompts". The PERSUADE table used has 14.

**g. Coverage of arXiv.** The "8 fields" exclude all of physics (hep-*, quant-ph, gr-qc, nucl-*, physics.*, math-ph), which is a large share of arXiv. "arXiv abstracts" in the title and abstract overstates what was sampled.

**h. A Discussion claim contradicts the paper's own results.** "Formal, noun-heavy registers were closest to what instruction-tuned models produce." In the paper's own feature table, `dep:amod` and `ADJ_ADJ_NOUN` are the most *human*-typical features, and the longest, densest field (astro-ph) has the lowest MSO.

**i. Pre-registration deviations that are not logged.**
- The pre-registration is still "DRAFT"; it was never frozen with a DOI.
- H5's direction was reversed (see W9).
- The self-test comparison changed from cs.CL to all cs.
- The Hansard window changed from 1998 to 2015.
- The embedding-instrument and threshold (0.4/0.6) sensitivity analyses were dropped for arXiv.
- The deviation items are numbered out of order (6, 7, 5), which suggests they were edited after the fact.

### W9. The learner analysis (H5).

**1. The pre-registered hypothesis was the opposite.** H5 predicted that learners would have *higher* MSO. The paper labels the section "(H5)" and presents the reverse as a finding without saying the hypothesis was not supported. That must be stated plainly.

**2. Rare events and quasi-separation.** Only **8 of 666 ELL essays** are in the region. The logit has 14 prompt and 6 grade fixed effects. Grade 12 contains 114 ELL and 5 non-ELL essays and **zero** events, so its coefficient is quasi-separated. ELL status is also concentrated in three prompts: 22–24% ELL against 3–7% in the others. The unadjusted 1.2% against 3.4% contrast is therefore confounded by prompt and grade. Use Firth or exact logistic regression, and report prompt-stratified contrasts.

**3. The continuous-margin CI is numerically wrong (verified).** The paper reports a coefficient of −0.31 with a 95% CI of [−0.32, −0.29]. I reproduced the model exactly:

| Variance estimator | SE |
|---|---|
| Classical (non-robust) | 0.044 |
| HC1 | 0.047 |
| HC3 (as used in the paper) | 0.0076 |

R² is only 0.049 and the residual SD is 0.98, so an SE of 0.0076 is impossible for a group of n=666. The HC3 result is a numerical failure, probably from leverage near 1 in the sparse grade cells. The correct CI is about **[−0.40, −0.21]**. The sign survives, as it does after adjusting for truncated length (−0.28), but the reported precision is off by a factor of six. This also means the authors' code checks did not catch an implausible output.

**4. Confounding with proficiency.** The LLM-typical features for essays are MTLD, word length, em dash and commas; the human-typical ones are sentence-length SD and contractions. The instrument is largely a writing-proficiency detector, so "ELLs are less machine-like" may simply mean "lower-proficiency writing is less like fluent LLM prose." ELL essays are also shorter (median 325 words against 391; 28% against 18% under 250 words). PERSUADE includes holistic scores. Condition on them, or match on score, before interpreting the result as an ELL effect.

**5. The detector comparison is not like-for-like.** The paper says the result is the opposite of the perplexity-detector bias. Liang et al. studied adult TOEFL test-takers with commercial detectors. This paper studies US school ELL designations with a different instrument. No perplexity-based detector was run on PERSUADE, so the "opposite" claim has no same-data comparison. Run at least one perplexity-based score (GPT-2 perplexity, DetectGPT or Binoculars) on the same essays and show the two instruments disagree on the same documents.

### W10. The self-test is circular and uninformative, and its conclusion does not follow.

- The drafting model is one of the training generators. Its held-out recall is 20.9%, and the paper's paragraphs come in at 20.7% in-region. The self-test restates the LOMO result: the instrument barely detects this model.
- Paper paragraphs are not abstracts. The paper concedes this and then draws the conclusion anyway: "most 2026 computer-science abstracts read as more machine-like than an AI-drafted paper about them." Comparing 59.1% of one population with 20.7% of another does not support a claim about "most" abstracts relative to the paper.
- `selftest.json` (15:54) predates the final `main.tex` (15:55), so the scored text is not the submitted text.
- `latex_paragraphs` replaces every `\R{}` number with "X", which changes punctuation and POS rates.
- The pre-registration specified a comparison with cs.CL. The paper uses all of cs, and this deviation is not logged.

**Fix.** Remove the self-test, or move it to an appendix as an anecdote with the LOMO caveat stated.

### W11. Selective reporting in secondary claims.

- **"Chat tuning makes the style."** The paper cites the two base models with the *lowest* in-region shares (GPT-2 30.1% and base Mistral 23.8%) and omits the others in `arxiv_base_vs_chat.csv`:

  | Base model | In-region share |
  |---|---|
  | MPT | **56.2%** |
  | GPT-3 | **44.5%** |
  | Cohere | **39.8%** |

  All base models are 2.5–6× the human baseline. The chat-model shares are *in-sample* (mistral-chat 86.9% in-sample against 82.8% held out). To my knowledge RAID's "gpt3" is text-davinci-003 and "cohere" is Cohere *command*, both instruction-tuned, so the `CHAT` lambda may misclassify them as base models. Base and chat outputs in RAID also differ in prompt format and in degenerate greedy decoding, which confounds "chat tuning". Fix: report all base models, use held-out (LOMO) recall for chat models, verify the RAID model identities, and soften the claim.
- **Markers.** "Weakly related (r=0.11)" hides the fact that marker words are **3.8× as common** inside the region as outside it (5.7% against 1.5%). The point-biserial r is small because markers are rare. The marker excess at 2025-06 is still significantly positive (CI 0.8–2.9), which the text omits. By 2026 the marker share (about 1%) is *below* the extrapolated pre-trend. Generator change (newer models avoid *delve*), which the paper's own frontier-model result supports, explains that at least as well as author avoidance. The paper offers only author avoidance.
- **Multiplicity.** The paper reports 8 field ITS fits, 2 placebos × 2 parameters, the aggregate, markers, Hansard, the control, the thresholded and continuous ELL tests, 10 seeds, 3 thresholds and 2 out-of-genre sets, with no correction or pre-specified hierarchy. The arXiv headline survives any correction. Several secondary claims are borderline: the ELL logit (p=0.045), Hansard's slope change (p=0.049) and some field level shifts. H4 (cs > math) is pre-registered but never formally tested as a contrast. Fix: report the H4 contrast with a CI, apply Holm or BH within families, and label secondary analyses as such.

---

## Questions to authors

1. How many arXiv field-month windows hit the 400-result cap? What do the main results look like after paginating, or with the bulk metadata snapshot and population weights?
2. Using a classifier frozen at 2017 or 2018, what "excess" does pure pre-LLM drift produce over horizons of 31–45 months? How does that compare to 22.5 points?
3. How do the arXiv AUCs and MSO change once Unicode dashes are normalised and math is masked in both populations?
4. Can you show MSO for a panel of the same authors before and after 2022?
5. What is the excess at 2025-06 when each generator is left out, especially the frontier model? Was the decision to add that model made before or after seeing the 2026 decline? The paper's wording implies after.
6. How do you justify an absolute difference in excess across two instruments with different AUCs and baselines? What does the injection-based sensitivity calibration show?
7. Why does HC3 give an SE six times smaller than HC1 or the classical SE in `essay_ell_continuous`? Which observations have leverage near 1?
8. Does the ELL effect survive conditioning on PERSUADE holistic scores?
9. Which RAID models do you treat as "base", and are `gpt3` and `cohere` actually instruction-tuned?
10. Were the Phi-4 and Granite generations used in any reported number? If not, why does the paper describe seven models?
11. How were the 2026 frontier-model batches produced (system prompt, context sharing, retries)? Were any generations filtered?

---

## Scores

| Criterion | Score | Comment |
|---|---|---|
| Soundness | **2 / 5** | The core identification is threatened by a verified sampling artefact, frozen-classifier drift, generator dependence and encoding artefacts. Several reported quantities are wrong or selectively reported. |
| Excitement | **3 / 5** | The question and the construct are interesting and the frontier-model observation is a genuine finding, but the strong framings ("population property", "Bayes error", "learners least machine-like") are not supported. |
| Overall assessment | **2 / 5** | Resubmit next cycle. The issues need new data collection and reanalysis, not edits to the text. |
| Confidence | **4 / 5** | I read the full code and results and reproduced the key quantities on the authors' data. |

---

## Required changes for acceptance

1. **Fix the arXiv sampling.** Remove the 400-cap truncation by paginating or using the bulk snapshot, post-stratify to true field-month volumes, and show robustness to submission hour.
2. **Replace the in-sample placebos** with rolling-origin placebos using classifiers frozen at earlier dates, and judge the post-2022 excess against the resulting drift distribution.
3. **Add composition controls:** an author-panel or fixed-effects analysis, reweighting to the pre-period distribution of field, subfield, length and submission hour, and the non-LLM-topic subfield analysis.
4. **Normalise encoding artefacts** (Unicode against LaTeX dashes, math spans), remove features with zero human support, and rerun everything.
5. **Reframe MSO as instrument-relative.** Remove or substantiate the "human half of a Bayes error" and "population property" claims with evidence that the estimate converges or with bounds, and correct the statement about prevalence-study subtraction.
6. **Propagate instrument uncertainty** (seeds × generator subsets × prompt mixes) and cluster-sampling uncertainty into every CI. Report LOMO *time series*, not only overall MSO.
7. **Pre-specify and freeze the generator set**, regenerate frontier-model text under logged, per-call decoding, and report 2026 as exploratory with results with and without each generator.
8. **Replace the absolute-difference Hansard control** with sensitivity-calibrated (injection) comparisons on a common scale. Address the 2022 speaker turnover and the HAC handling of gappy months, or demote Hansard to a descriptive comparison.
9. **Use an event-study or flexible post-period specification.** Report all placebo parameters and pre-trend sensitivity.
10. **Fix the learner analysis:**
    - state that pre-registered H5 was not supported;
    - correct the continuous-margin SE (HC1 or cluster-by-prompt);
    - use Firth logistic regression;
    - condition on holistic proficiency scores;
    - run a perplexity-based detector on the same essays before claiming the result is the opposite of detector bias;
    - correct "near chance" for the TOEFL and college essays.
11. **Report all base models in the chat-tuning analysis**, use held-out recall for chat models, verify the RAID model identities, and soften the claim.
12. **Correct the marker narrative:** report the significant 2025 excess and the 3.8× in-region enrichment, and discuss generator change as an alternative explanation.
13. **Remove the self-test**, or move it to an appendix with the LOMO caveat.
14. **Fix the mismatches:**
    - the seven-model claim against the five models actually used;
    - grouped CV for Hansard (shared keys) and in the calibration step;
    - hard-coded numbers;
    - the missing Appendix A;
    - latest-version abstracts (restrict H0 by the `updated` date);
    - the prompt count;
    - the "noun-heavy" claim;
    - the scope of "arXiv" (8 non-physics fields).
15. **Freeze the pre-registration** and log every deviation listed in W8(i). Apply multiplicity control within families and test H4 as a formal contrast.
