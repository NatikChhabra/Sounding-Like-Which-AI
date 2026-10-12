# ARR Review — Reviewer 2 (machine-generated text detection / stylometry)

**Submission:** "Sounding Like AI Before AI: Machine-Style Overlap in Human Writing"

I read `main.tex` with every `\R{}` macro resolved against `results/numbers.tex`, the code in `code/`, `preregistration.md`, and the result files. Using the authors' own `mso.training_set`/`mso.fit` and their cached features, I refit the arXiv instrument and reproduced the headline numbers exactly: 21.5% overall MSO, a 9.4% pre-ChatGPT baseline, and the same yearly series. The additional analyses I cite below ("my re-analysis") come from that refit. I did not change any project file.

---

## Summary

The paper defines Machine-Style Overlap (MSO): the share of a genre's human documents that a calibrated classifier, trained on balanced pre-ChatGPT human text versus LLM text, assigns P(LLM) ≥ 0.5. The classifier uses "topic-robust" stylometric features: function-word rates, coarse POS trigrams, dependency labels, punctuation, sentence-length mean/SD, word length and MTLD. The paper argues that the pre-LLM value of MSO is "the human half of a Bayes error" and therefore a population property rather than estimator noise. It reports:

- a 9.4% pre-2022 baseline in 159k arXiv abstracts, ranging from 4.7% (astro-ph) to 16.2% (econ);
- a post-2022 excess of 22.5 points over the pre-trend at June 2025, against 1.4 points in Australian Hansard;
- a dose ordering of cs > astro-ph > math;
- marker words that rise and recede while MSO keeps rising;
- base RAID models that fall in the region far less often than chat models;
- ELL essays in PERSUADE 2.0 that fall in the region less often than non-ELL essays (1.2% vs 3.4%), described as "the opposite" of the bias of perplexity-based detectors.

## Strengths

1. The question is a good one. It reframes the non-zero pre-ChatGPT "AI share" that prevalence studies report (Liang et al. 2024; Lin & Zhu 2025; Brooks et al. 2024; Sun et al. 2025) as something to study rather than subtract. The field-level breakdown of that baseline is useful descriptive data.
2. The pipeline is unusually transparent. Every number is macro-generated, the code is small and readable, and the results reproduce exactly from the cached features. The train/score split keeps prompt seeds and training documents out of the measured set, and cross-validation is grouped by source document and by speaker.
3. Several design choices are sound and often missing from this literature: a three-prompt LLM side that includes revision (P2) and evasion (P3) prompts, leave-one-generator-out recall, placebo break dates, and a control genre.
4. The leave-one-out result for the 2026 frontier model (20.9% recall when held out, against 94.6% for GPT-4) is an honest and important negative finding. It shows that "LLM style" is a moving target, and the paper reports it.
5. The writing is clear and the limitations section is candid about authorship agnosticism.

## Weaknesses (most severe first)

### W1. The post-2022 trajectory, and the "markers recede but MSO does not" contrast, is an artifact of which generators define the region.

The paper itself says that adding the frontier model reversed a 2026 decline (§5.3, "In a preliminary run without the frontier model, arXiv MSO appeared to fall in 2026"). I checked how far this goes by refitting the instrument with three generator sets:

| Generator set defining L | pre-2022 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| All chat (paper) | 9.4 | 10.7 | 16.8 | 25.4 | 36.4 | **40.7** |
| Without Claude | 7.8 | 9.3 | 15.1 | 24.1 | 33.7 | **31.2** |
| RAID chat models only (ChatGPT, GPT-4, Cohere-chat, Llama-2-chat, Mistral-chat, MPT-chat) | 6.6 | 7.7 | 11.0 | 15.3 | 15.7 | **9.8** |

With a region defined by the 2023 commercial models, MSO peaks in 2024–25 and falls back almost to its 2022 level in 2026. That is the same rise-and-fall shape the paper reports for marker words (marker share 1.1% → 5.4% → 4.2% → 1.6%). So "lexical markers recede while style overlap persists" is not a finding about human writing. It is what happens when one measure is updated with a 2026 generator and the other (a fixed 8-word list from 2024 papers) is not. The more parsimonious reading of both series is generator turnover: newer models no longer write "delve", and no longer write in the 2023 ChatGPT register. That reading needs no author avoidance of markers (§5.4) and no "underlying register remained" (Discussion).

The same issue undermines the claim that the pre-LLM baseline is "a population property". The baseline moves from 6.6% to 9.4% depending on which generators are included, and the definition uses an equal-weight mixture over generators that the researchers chose and changed mid-study.

**Fix:**
- Make generator composition a first-class axis of the analysis. Report the full time series and the excess under (a) RAID-only, (b) local-only, (c) the paper's set, and (d) each frontier model alone. Treat the spread as the main uncertainty.
- Re-run the marker analysis with a marker list updated in the same way, e.g. Kobak et al.'s full excess-vocabulary method applied to 2025–26 data, or markers mined from the frontier-model generations themselves.
- Rewrite §5.4 and the Discussion so they do not attribute the divergence to human behaviour unless it survives these checks.

### W2. Novelty against detector false-positive rates and against Liang et al.'s α is overstated. MSO is unadjusted classify-and-count.

Operationally, MSO(S) is the positive rate of a fixed binary classifier on population S. On pre-LLM text that is the classifier's false-positive rate, which every prevalence paper already reports or calibrates against (Brooks et al. 2024 fix a 1% FPR on pre-GPT-3.5 Wikipedia). Under the standard mixture S_t = (1−α)H₀ + αL, MSO(S_t) = FPR + α(TPR − FPR). The post-2022 "excess" is therefore α scaled by (TPR − FPR): Forman's (2008) adjusted classify-and-count, with the adjustment left out.

The only content of MSO that is not a rescaled prevalence is drift in H_t itself, and the paper explicitly declines to identify that ("we do not separate them"). The Bayes-error argument does not rescue the construct, for three reasons:

1. The identity MSO(H₀) = Bayes FPR holds only for the true densities p_L and p_H₀ under φ. Here p_L is an equal-weight mixture of researcher-chosen generators and prompts, so the "population" in question is partly the authors' construction.
2. A finite-sample classifier's FPR is not a bound on the Bayes FPR in either direction. A classifier that always predicts "human" has FPR = 0. The pre-registration's claim that a weaker classifier "gives a conservative estimate" is wrong. Only the *total* error is bounded below by the Bayes error.
3. "Estimator noise would be uniform across fields" (§5.2) is a straw man. A fixed classifier's FPR varies across subpopulations whenever covariates differ. This is exactly the detector-bias literature (Liang et al. 2023; Park et al. 2026). A χ² test rejecting uniformity is the expected outcome under either interpretation.

**Fix:**
- State the mixture identity explicitly and report the implied α = (MSO − FPR)/(TPR − FPR), using LOMO TPRs, next to Liang et al. (2024) and Kobak et al. (2025) for cs and math. If the implied α is implausible, that is informative about H_t drift. This is the one way to make the "overlap" estimand carry information that prevalence does not.
- Drop "population property" or qualify it as "property of the two populations *given φ, the generator mixture and the classifier family*".
- Replace the uniformity straw man with a substantive test: does the field-level baseline predict anything external, such as post-2022 uptake, author L1, or an independent register measure?

### W3. The features are not topic-robust, and length and LaTeX are uncontrolled confounds.

- **Length.** The code comment claims 250-word truncation means "length can't drive results". But only 6–9% of abstracts exceed 250 words (mean 153–174). In my re-analysis, pre-2022 MSO falls monotonically with abstract length: 13.8% (≤100 words), 11.5%, 8.3%, 5.2%, 3.9% (>250 words). Field means differ widely (math 122 words, astro-ph 208), so part of the field gradient in Fig. 2 is a length gradient. Abstract length also drifts upward over time (153 → 174 words). That biases the time series downward, but differently by field. The same applies to RAID base-vs-chat lengths: GPT-2 averages 262 words and MPT 278, against 98–141 for most chat models.
- **LaTeX.** Raw arXiv abstracts keep `$…$` math. That math is present in 57% of math, 53% of astro-ph, 11% of cs and 8% of econ abstracts, but in only 1–13% of P1/P3 LLM generations. Within every field, abstracts with math are less often in the region (cs 13.8% vs 6.9%; econ 16.8% vs 7.6%). The paper's lowest-baseline and lowest-excess fields (astro-ph, math) are exactly the LaTeX-dense ones. So the "dose" ordering, which is presented as matching Liang et al.'s uptake ordering, is partly confounded by notation density.
- **Encoding asymmetry in the top features.** The 2nd and 3rd most LLM-typical arXiv features are Unicode em dash and en dash (`pun:—`, `pun:–`). Not one of the 159k human abstracts contains them, because arXiv authors write LaTeX `---`/`--`. The cleaning step maps curly quotes and non-breaking hyphens to ASCII but does not map `---` → `—`. Meanwhile 49–56% of gpt-oss and 16–29% of Gemma abstracts contain Unicode dashes. The instrument therefore learns a typesetting convention, not a style. It is also blind to the best-known LLM marker in human abstracts: LaTeX dashes rise from 4.6% of abstracts (2015–24) to 7.7% (2025) and 12.0% (2026). The essay instrument has the same issue: `pun:—` ranks 2nd, `'s`/`'re` are LLM-typical, and `nt` (apostrophe-less "dont") is human-typical. Those are orthography and keyboard features, not register.
- **MTLD is the single strongest feature** in all three genres. It depends on terminology repetition, which depends on topic and field. "No content words" does not make a feature topic-robust.

**Fix:**
- Normalise `---`/`--` to Unicode dashes, or drop all dash features.
- Strip or placeholder LaTeX math in both classes and re-run.
- Length-match LLM and human texts by subsampling within length bins, or add length as a covariate and report MSO stratified by length decile.
- Report field results after these controls.
- Add an ablation table removing each feature family (punctuation, scalars, function words, POS, dependencies) and show which conclusions survive.

### W4. The Hansard control is not a control: it uses a different instrument built from a different, weaker generator set.

The paper describes the LLM side as "a broad set of open-weight and commercial generators". But `hansard_lomo.csv` and `essay_lomo.csv` show that Hansard and essays use only five 7–20B local models: no RAID, no commercial model, no frontier model. (The paper also says seven local models, but Phi-4 and Granite 3.3 appear in no result file; see W8.) The paper's own §5.3 argument, that "an overlap measure defined only by older models will understate recent movement", applies with full force to Hansard. Hansard's null excess (1.4 points, CI −0.2 to 3.1) may simply mean that small local models do not represent whatever LLM help parliamentarians' speechwriters use. Prepared parliamentary speeches are often written in advance, so "spoken" does not mean unexposed.

The arXiv-minus-Hansard difference (21.1 points) also compares two classifiers with different separability (AUC 0.934 vs 0.977) and different baselines (9.4% vs 3.7%). An excess measured in percentage points is not comparable across instruments with different floors.

**Fix:**
- Build every genre's region from the same generator families, including at least two commercial chat models via API (e.g. GPT-4o-class, Gemini-class) with logged decoding parameters.
- Better still, add a control that shares the arXiv instrument: a less-exposed *written scholarly* population (e.g. pre-print categories or journals with strict LLM policies), or a randomised placebo region trained on a random split of pre-2022 human text.
- Express excess on a scale comparable across instruments, e.g. relative to baseline or in logit units.

### W5. The base-vs-chat analysis is partly in-sample and confounded by prompt template, decoding and length.

The chat RAID generators are in the training set (up to 450 documents each). Their "share in region" in `arxiv_base_vs_chat.csv` (e.g. 86.9% for Mistral-chat) is computed on all 7,064 documents, including the training documents. The out-of-sample LOMO figure is 82.8%. The qualitative gap probably survives, but it must be reported out-of-sample.

More importantly, RAID base models receive a continuation template ("The following is the full text of the abstract…from arxiv.org:") and fully random sampling, while chat models receive an instruction template. Base outputs are also about twice as long. Every one of these differences moves MSO. The ordering also does not cleanly support "chat tuning makes the style": base MPT reaches 56.2%, above RAID's GPT-3 (44.5%) and Cohere "command" (39.8%), which are API models of at least partly instruction-tuned lineage. The sentence "What humans hear as 'sounding like AI' is largely a product of instruction and preference tuning" has no human-perception data behind it.

**Fix:**
- Use LOMO numbers for chat models.
- Restrict the comparison to matched decoding (sampling with repetition penalty), length-matched outputs, and base/chat pairs from the same family (Mistral, MPT, and ideally Llama-3 base/instruct and OLMo-2 base/SFT/DPO checkpoints, which isolate SFT from preference tuning).
- Remove the perception claim.

### W6. The learner result is predetermined by the feature set, contradicts the pre-registered hypothesis, and is not compared with the instrument it claims to contradict.

- The pre-registration states **H5: "Non-native learner essays have higher MSO than native-speaker essays."** The paper reports the opposite under the label "H5" without saying that the pre-registered prediction failed. This must be disclosed.
- The essay region's top LLM-typical features are MTLD, the em dash and word length. Its top human-typical features are sentence-length SD and apostrophe-less "nt". Those are proficiency and typing measures, so an instrument built on lexical sophistication will place less proficient writers further from LLM output by construction. Liang et al. (2023) themselves showed the mirror image: raising TOEFL essays' lexical sophistication lowers perplexity-detector false positives. The result is the expected sign, not a reversal.
- "The opposite of the bias reported for perplexity-based detectors" compares different instruments (style classifier vs commercial perplexity detectors), different populations (US grade 6–12 ELLs vs Chinese TOEFL test-takers) and different genres. Your own out-of-genre check does not support the framing: the essay instrument puts **34.1% of Liang's TOEFL essays** in the region, ten times the in-genre baseline of 3.2%, and 51.4% of college essays. Describing those as "near chance" is wrong; they show the instrument breaks out of genre.
- The thresholded effect rests on 8 ELL essays in the region (1.2% of 666). It reaches p < 0.05 in 3 of 10 training draws.

**Fix:**
- Run a perplexity-based detector (Binoculars, Fast-DetectGPT) on the same PERSUADE ELL/non-ELL essays, adjusting for prompt and grade. Only a within-population, two-instrument comparison can show "same text, opposite verdicts".
- Report H5 as disconfirmed.
- Add a proficiency covariate (PERSUADE provides holistic scores) to show whether any ELL effect remains beyond proficiency.

### W7. Frontier-model data are not a controlled sample, and the study's integrity around them needs work.

The 2026 "frontier model" texts were produced by agent sub-sessions answering batches of 50 prompts each. There is no temperature or seed control, no fixed system prompt, no API snapshot, and possible within-batch stylistic dependence. This is the same model family that drafted the paper. Its separability is also strikingly low: AUC 0.69 for P2 and 0.84 for P1. With equal weighting, its 450 texts pull the region boundary toward human text and raise everyone's MSO; the overall baseline goes from 7.8% to 9.4%.

The pre-registration is marked "DRAFT (to be frozen with a Zenodo DOI)". Its deviation log says the frontier model was added "before the final run" and that "no analysis choice was changed" after pilots. Yet the paper says a preliminary run *without* the frontier model showed a 2026 decline and the frontier model was then added. These two accounts are inconsistent, and the paper still calls the June-2025 excess "the pre-registered quantity".

**Fix:**
- Generate frontier-model text through the API with logged parameters.
- Report all results with and without it (see W1).
- Freeze and link the pre-registration, or stop calling quantities pre-registered.
- Reconcile the deviation log with §5.3.

### W8. Factual inconsistencies and an incomplete submission.

- §4 says seven local open-weight models, including Phi-4 and Granite 3.3. `generate.py` lists five, and no result file contains Phi-4 or Granite.
- Appendix A is a red `\TODO`. The LOMO table the main text points to does not exist in the paper.
- "Bars are 95% intervals" in Fig. 2: the per-field excess CIs come from WLS with HAC errors on monthly cells as small as about 20 documents (econ), which is worth a sentence.
- §5.1 "the region generalises to generators it never saw" is contradicted by the 20.9% frontier recall two sections later.

**Fix:** correct the generator list, add the appendix table, and qualify the generalisation claim.

### W9. The self-test overclaims.

"By this measure, most 2026 computer-science abstracts read as more machine-like than an AI-drafted paper about them" rests on 29 out-of-genre paragraphs. They are LaTeX-stripped, so the paper's own dashes (`--`) never register as the top LLM feature. They are scored by an instrument whose recall on the drafting model's own family is 21%. This is not a finding.

**Fix:** remove it, or move it to an appendix without the comparative sentence.

### W10. Title and framing promise human perception, which the paper does not measure.

"Sounding like AI", "what humans hear", and "Whether text 'sounds like AI'…" in the abstract all refer to a classifier's output. The paper collects no human judgements (it says so), and nothing shows that MSO correlates with reader perception.

**Fix:** retitle around the measured construct, or add a small perception study showing that MSO predicts human "AI-sounding" ratings.

### W11. On the name.

"Machine-Style Overlap" is free as a phrase; the authors' own term search found zero hits. But "overlap" suggests a symmetric distributional overlap coefficient (Bhattacharyya, OVL), and the construct is a one-sided, thresholded positive rate. The authors' term search recommended "machine-indistinguishable share" for this reason, and it is the more accurate name. More importantly, the construct already exists under other names: "AI-likeness"/"AI-ness" (Khan et al. 2025; Mizumoto 2026), "convergence" (Chang 2026), and a "GPT-like share" from a stylometric classifier (Askitas 2025).

**Fix:** either justify the term against these explicitly, or adopt the descriptive name and position the contribution as the baseline decomposition rather than a new construct.

## Missing references (verified)

- **Khan, Ibrahim, Aldahoul, Rahwan, Zaki (2025).** *Who Gets Seen in the Age of AI? Adoption Patterns of Large Language Models in Scholarly Writing and Citation Outcomes.* https://arxiv.org/abs/2509.08306. Tracks zero-shot-detector "AI-likeness" in 230k CS articles from 2021–2025, with a pre-ChatGPT baseline. Same design with a perplexity-type instrument; must be cited and compared.
- **Askitas (2025).** *The Behavioral Signature of GenAI in Scientific Communication.* IZA DP 18062. https://ideas.repec.org/p/iza/izadps/dp18062.html. Economics abstracts; stylometric shift in word length, TTR and readability; a classifier flagging a growing "GPT-like" share; event study with placebos. Very close to this paper's arXiv analysis, including its econ field.
- **Shaib, Elazar, Li, Wallace (2024).** *Detection and Measurement of Syntactic Templates in Generated Text.* EMNLP 2024. https://aclanthology.org/2024.emnlp-main.368. POS-sequence templates characterise LLM output, and 76% of model templates already occur in pre-training data. This directly bears on the POS-trigram features and on "pre-LLM human text already in the region".
- **Hans et al. (2024).** *Spotting LLMs With Binoculars.* ICML 2024. https://proceedings.mlr.press/v235/hans24a.html. The obvious perplexity-family instrument to run alongside MSO, in all genres and especially for the learner claim.
- **Bao et al. (2024).** *Fast-DetectGPT.* ICLR 2024. https://arxiv.org/abs/2310.05130. Second perplexity-curvature baseline.
- **Chakraborty et al. (2024).** *Position: On the Possibilities of AI-Generated Text Detection.* ICML 2024. https://proceedings.mlr.press/v235/chakraborty24a.html. Relates detectability to total-variation distance; it is the formal background for the "Bayes error" argument.
- **Forman (2008).** *Quantifying counts and costs via classification.* Data Mining and Knowledge Discovery 17(2). https://doi.org/10.1007/s10618-008-0097-y. Classify-and-count vs adjusted classify-and-count; needed to relate MSO to prevalence (W2).
- **Mizumoto (2026).** *Corpus-informed AI-likeness screening for L2 writing.* Applied Corpus Linguistics 6(3):100223. https://doi.org/10.1016/j.acorp.2026.100223. AI-likeness of L2 writing, relevant to the learner result.
- **Berber Sardinha (2024).** *AI-generated vs human-authored texts: A multidimensional comparison.* Applied Corpus Linguistics 4(1). https://doi.org/10.1016/j.acorp.2023.100083. A Biber-MD comparison; should sit next to Reinhart et al. (2025).
- **Herbold et al. (2023).** *A large-scale comparison of human-written versus ChatGPT-generated essays.* Scientific Reports 13:18617. https://doi.org/10.1038/s41598-023-45644-9. Linguistic-feature differences in student essays, relevant to the essay instrument.

Also: Chang (2026) is cited, but the related-work sentence does not say what it measures. If, as the authors' notes indicate, it tracks LM-predictability over a decade, it is the perplexity counterpart of this paper and must be compared quantitatively, not in one clause.

## Questions for the authors

1. What is the time series under a RAID-only region and a frontier-only region (W1)? Does any conclusion in §5.3–5.4 survive across all of them?
2. Which α does the June-2025 excess imply under the mixture identity, and how does it compare with Liang et al. (2024) for cs?
3. Do the field ordering and the dose result survive after LaTeX stripping, dash normalisation and length matching?
4. Why were Phi-4 and Granite 3.3 described but not used? Were they generated and then dropped, and if so, why?
5. What are the exact conditions under which the frontier-model texts were produced (system prompt, batching, number of sub-agents, any instructions beyond the prompt)?
6. Does the ELL effect survive conditioning on PERSUADE holistic score? What does Binoculars say about the same essays?
7. Why are Hansard and essay regions built without any commercial model, when §5.3 argues that this understates movement?
8. Was the pre-registration frozen anywhere external before the arXiv run? If not, which analyses were decided after the pilot?

## Scores

- **Soundness: 2 / 5.** Several headline claims depend on uncontrolled choices: generator composition, encoding, length, and a cross-instrument control. The learner claim reverses a pre-registered hypothesis without saying so.
- **Excitement: 3 / 5.** The baseline decomposition is a useful idea and the descriptive data are interesting, but the construct is close to existing detector-rate and "AI-likeness" measures.
- **Overall assessment: 2 / 5.** Resubmit after major revisions.
- **Reviewer confidence: 4 / 5.** I re-ran parts of the analysis with the authors' code and data.

## Required changes for acceptance

1. **Generator-set sensitivity.** Report every headline result (baseline, excess, field dose, marker contrast, ELL) under at least RAID-only, local-only, all-but-frontier and full regions. Rewrite the marker-vs-MSO and "register remained" claims unless they hold across these sets.
2. **Relate MSO formally to prevalence** via the mixture identity / adjusted classify-and-count. Report implied α. Remove the "conservative estimate", "population property" and "noise would be uniform" arguments, or correct them.
3. **Confound controls.** Dash and LaTeX normalisation, length matching or stratification, and a feature-family ablation. Re-report the field ordering and dose result.
4. **A common-instrument control.** Use the same generator families for all genres, and add a control or placebo that shares the arXiv instrument.
5. **Learner analysis.** Run a perplexity-based detector on the same PERSUADE essays, add a proficiency covariate, report H5 as disconfirmed, and drop "opposite of the bias" unless the within-population comparison shows it. Correct "near chance" for the Liang essays.
6. **Base vs chat.** Use out-of-sample shares, matched decoding, prompt and length, and same-family pairs. Remove the perception claim.
7. **Integrity.** Use controlled API generation for the frontier model or clearly demote it. Freeze the pre-registration or stop calling quantities pre-registered. Reconcile the deviation log with §5.3. Fix the seven-vs-five generator statement. Fill Appendix A.
8. **Framing.** Retitle or qualify "sounding like AI". Remove the self-test comparison sentence. Cite and differentiate Khan et al. 2025, Askitas 2025, Shaib et al. 2024 and Chang 2026, plus the detection baselines above.
