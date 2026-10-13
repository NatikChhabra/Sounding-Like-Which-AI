# Pre-registration: Machine-Style Overlap in human writing, 2015–2026

Status: analysis plan committed to this repository on 2026-10-12 (commit ef4fa21) before any result was computed.
It was never registered with a third party and was not frozen with a DOI as originally intended. Sections 1-6 are
kept as committed (one retracted sentence is marked); all later changes are listed under "Deviations". Written by
Claude (AI) at the author's request; approved by the author.

## 1. Construct

**Machine-Style Overlap (MSO).** For a genre G and period t, MSO is the share of human-written documents in G
whose style is at least as typical of LLM output as of human writing:

    MSO(G, t) = P_{x ~ H(G,t)} [ p_L(x) >= p_H0(x) ]

where H0 is the pre-ChatGPT human distribution (documents dated before 2022-11-30), L is LLM output for the
same genre and topics, and x is a vector of topic-robust style features. With balanced priors this is the
share of human documents that a calibrated Bayes classifier assigns P(LLM | x) >= 0.5. We estimate it with
calibrated classifiers. [RETRACTED after review: "which give a conservative estimate (a weaker classifier
separates less and so reports more overlap)" is false; a finite classifier's flag rate is neither an upper nor a
lower bound on the Bayes quantity.] MSO(G, pre-2022) is the **baseline overlap**: how much human writing already "sounded like AI"
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

## Deviations from this plan (in order; times from the git log)
Honesty note: this plan was committed to the project's git repository (commit ef4fa21, 2026-10-12 07:53 IST)
before any MSO value was computed. Git timestamps are self-reported, so this is weaker than a third-party registry.
1. **arXiv sampling.** Full OAI-PMH harvesting was infeasible (~40 h), so abstracts were drawn as a
   stratified random sample via the arXiv API: one random window per archive-month, 8 archives (cs, math, stat, eess, q-bio, econ, astro-ph, cond-mat),
   2015-01 to 2026-09. The first sampler kept only the first 400 results per window; it was replaced after
   review round 1 by one that fetches every paper in the window and samples 200 at random. The overall series
   therefore weights the eight archives about equally, not by submission volume. Because the API returns the
   latest version, pre-ChatGPT papers whose latest version postdates ChatGPT are excluded.
2. **Learner data.** ELLIPSE could not be downloaded (Git LFS); PERSUADE 2.0 (ELL vs non-ELL on identical
   prompts) is the primary learner contrast. Liang et al.'s TOEFL and US college essays (Hugging Face release)
   and their US 8th-grade essays (distributed in the authors' GitHub repository, found after review round 1)
   are used only for an out-of-genre perplexity replication.
3. **LLM side.** RAID abstracts are restricted to chat/instruction-tuned generators for the main region;
   base models are analysed separately.
4. **Added diagnostics (not in the plan):** agreement between the two classifiers on which documents are in
   the region (Cohen's kappa, Spearman), and recall on held-out (unseen) generators.
5. **Hansard identifiers (bug fix, before any Hansard result).** The corpus field `uniqueID` identifies the
   speaker, not the speech. Speeches are now keyed by date + order, and cross-validation groups by speaker.
   Generations made before the fix carry speaker-style source ids; they still group by speaker.
6. **Pilot runs.** An essay analysis was run once on partial generations (3 of 5 models) to test the code;
   no analysis choice was changed after it. An arXiv pilot (RAID plus about 30% of the local generations) tested
   the pipeline at scale; see 7. A preliminary arXiv run (5 local models + RAID) was committed at 15:35 (f586d6c).
7. **More generators (decided after the arXiv pilot; texts merged after the preliminary run).** Phi-4 14B and Granite 3.3 8B (the generation
   script gained a model-list argument at 15:32, fd8a23b) and the 2026 model Claude Opus 5.5, whose prompt
   batches were committed at 15:37 (c11d3ce), two minutes after the preliminary arXiv results. The decision
   to add all three was stated in the working conversation after the arXiv pilot run on partial data (RAID plus
   about 30% of the local generations) and before the preliminary run with all five local models. The git
   record cannot show this, and the pilot may have informed the decision. The 2026 model's texts were produced by sub-agent sessions answering
   50 prompt instances each, with no temperature or seed control. Phi-4 and Granite were described in paper v1
   but first used in v2. Each generator is capped at 450 texts so no single source dominates the region.
8. **Review round 1 (2026-10-12) changes:** arXiv sampler replaced (see 1); LaTeX and encoding normalisation;
   grouped calibration; per-generator cap; Claude, Phi-4 and Granite added to all genres; generator-set, drift,
   math, topic, length, threshold and dash analyses; proficiency adjustment; perplexity instrument;
   dispersion; the self-test (section 6) dropped as circular; Hansard restricted to 2015-2025.
9. **Review round 2 (2026-10-13) changes:** generator-vintage analysis on a matched title-only task; a region
   from generators whose training data predate ChatGPT (RAID GPT-4 and ChatGPT, and two locally run open
   models, Llama 2 chat and Vicuna, added for this purpose only); three 2026 open models (Qwen3.5 9B, Gemma 4 12B,
   Granite 4.2 8B), added for the vintage analysis only after the single-generator pattern of the other 16
   generators had been seen (post hoc); vintage-matched, topic-matched mined marker
   words; placebo grids for both genres; event study; pre-trend shape and window sensitivity; block bootstrap;
   drift placebos at three origins; Holm correction across archives and a cs-minus-math contrast (H4);
   length-standardised baselines and length-fixed dispersion; GPT-2 perplexity to rule out training-data
   contamination; revision-overlap check; implied prevalence via the mixture identity. Cleaning fix found
   while adding generators: lines of the form "Title: ..." in LLM outputs (mostly Mistral 7B; 13% of local arXiv
   and 18% of LLM essay texts) had only their label removed, leaving the echoed title glued to the first
   sentence; the whole line is now dropped and every analysis was re-run.
10. **Not run:** the plan's embedding-based classifier for arXiv (run for essays only).
11. **Outcomes.** H5 not supported (opposite direction). The evaluation month (June 2025) was fixed in code
    (commit 50e2a17), not in this plan. The plan named cs.CL for one comparison; all of cs is used.
12. **Never frozen.** The plan was intended to be frozen with a DOI; it was not. "Pre-registered" is therefore
    not used in the paper.

## 6. Self-test (dropped; see deviation 8)
The paper's own text is scored by the same pipeline and compared with human-written cs.CL abstracts.
