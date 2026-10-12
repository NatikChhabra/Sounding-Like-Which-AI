# Pre-registration: Machine-Style Overlap in human writing, 2015–2026

Status: DRAFT (to be frozen with a Zenodo DOI before the full data run). Written by Claude (AI); verified by the author.

## 1. Construct

**Machine-Style Overlap (MSO).** For a genre G and period t, MSO is the share of human-written documents in G
whose style is at least as typical of LLM output as of human writing:

    MSO(G, t) = P_{x ~ H(G,t)} [ p_L(x) >= p_H0(x) ]

where H0 is the pre-ChatGPT human distribution (documents dated before 2022-11-30), L is LLM output for the
same genre and topics, and x is a vector of topic-robust style features. With balanced priors this is the
share of human documents that a calibrated Bayes classifier assigns P(LLM | x) >= 0.5. We estimate it with
calibrated classifiers, which give a conservative estimate (a weaker classifier separates less and so reports
more overlap). MSO(G, pre-2022) is the **baseline overlap**: how much human writing already "sounded like AI"
before AI writing was widely available.

Term search (lit/03_term_search.md) found no prior use of "machine-style overlap". Closest related constructs:
homogenization (Sourati et al. 2026), convergence measured by LM predictability (Chang 2026), AI-likeness
via detectors (Khan et al. 2025), LLM style index (Bentley et al. 2026).

## 2. Hypotheses
- **H1 (baseline):** MSO(arXiv, 2015–2021) > 0 and differs across fields; i.e. some human writing already
  occupied the LLM style region before LLMs. (Descriptive; no direction for field differences.)
- **H2 (shift):** In arXiv abstracts, MSO after 2022-11-30 exceeds the value predicted by the 2015–2022 linear
  trend (segmented regression, monthly).
- **H3 (control):** The post-2022 deviation in H2 is larger than in parliamentary speech (Australian Hansard),
  a genre with lower exposure to LLM writing.
- **H4 (dose):** The deviation is larger in fields with higher reported LLM uptake (cs) than lower (math).
- **H5 (misclassification):** Non-native learner essays have higher MSO than native-speaker essays of the same
  task type.

## 3. Data
- Human, treatment: arXiv abstracts (OAI-PMH, v1 submission date), monthly stratified sample by top-level field.
- Human, control: Australian Hansard 1998–2025 (Zenodo, CC BY 4.0).
- LLM: 5 local open models (Llama 3.1 8B, Qwen3 8B, Gemma 3 12B, Mistral 7B, gpt-oss 20B) x 3 prompt styles
  (generate from title; polish a human draft; "write naturally, avoid AI clichés"), prompts built from
  pre-2022 human documents only. Plus RAID abstracts subset (commercial-model outputs).
- Learner: Liang et al. 2023 TOEFL essays; ELLIPSE.

## 4. Features (topic-robust by design)
Function-word relative frequencies; POS-tag trigram frequencies; sentence-length mean and SD; MTLD lexical
diversity; punctuation rates (incl. em dash, colon, semicolon); paragraph/list structure. Content words are
excluded. Marker-word frequencies are analysed separately, never as an MSO feature.

## 5. Analysis
- Classifiers: L2 logistic regression (primary, isotonic-calibrated) and gradient boosting (robustness),
  trained on H0 (pre-2022) vs L, 5-fold CV; report AUC per model x prompt.
- MSO time series scored by the frozen classifier; segmented regression with Newey-West errors;
  placebo break dates at 2019-11 and 2020-11; leave-one-model-out region definitions.
- Sensitivity: thresholds 0.4/0.5/0.6; embedding-based classifier; excluding any one LLM.
- Wording rule: results are "consistent with" LLM influence; no causal claim.

## Deviations from this plan (logged as they happen)
Honesty note: this plan was committed to the project's git repository (commit ef4fa21, 2026-10-12) before any
MSO value was computed. Git timestamps are self-reported, so this is weaker than a third-party registry.
1. **Learner data.** ELLIPSE could not be downloaded (Git LFS); PERSUADE 2.0 (ELL vs non-ELL on identical
   prompts) is the primary learner contrast instead. The public Liang et al. release contains TOEFL and US
   *college* essays, not the 8th-grade essays described in their paper; it is used as a secondary,
   out-of-genre check only.
2. **arXiv sampling.** Full OAI-PMH harvesting was infeasible (~40 h), so abstracts were drawn as a
   stratified random sample via the arXiv API: one random window per field-month, 8 fields, 2015-01 to 2026-09.
3. **LLM side.** RAID abstracts are restricted to chat/instruction-tuned generators for the main region;
   base models are analysed separately.
4. **Added diagnostics (not in the plan):** agreement between the two classifiers on which documents are in
   the region (Cohen's kappa, Spearman), and recall on held-out (unseen) models.
6. **Hansard identifiers (bug fix, before any Hansard result).** The corpus field `uniqueID` identifies the
   speaker, not the speech. Speeches are now keyed by date + order, and cross-validation groups by speaker.
   Some speakers' speeches were sampled more than once as generation seeds; all generations are kept.
5. **Pilot run.** An essay analysis was run once on partial generations (3 of 5 models) to test the code.
   No analysis choices were changed after seeing it.

## 6. Self-test
The paper's own text is scored by the same pipeline and compared with human-written cs.CL abstracts.
