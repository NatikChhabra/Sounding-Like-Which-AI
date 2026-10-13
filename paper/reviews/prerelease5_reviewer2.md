# ARR review: "Sounding Like Which AI? Machine-Style Overlap of arXiv Abstracts with Language Models of Different Vintages"

Reviewer 2 (LLM-text detection, corpus linguistics, causal inference with time series). I read the anonymous PDF (16 pp.; main text ends at the bottom of p. 8), main.tex, results/*.csv|json and code/analysis.py, mso.py, features.py. Where I quote a number that is not in the paper, I computed it from the existing results files. The exact recipe is given so the authors can reproduce it.

---

## 1. Summary

The paper defines Machine-Style Overlap (MSO): the share of documents that a calibrated, class-balanced classifier on content-word-free style features (closed-class word rates, coarse POS trigrams, dependency labels, punctuation, sentence/word length, MTLD) places at likelihood ratio >= 1 for "LLM output" versus "pre-ChatGPT human writing in the same genre". The authors argue that it is the flag rate of the Bayes classifier, so on pre-ChatGPT text it is that classifier's FPR. They track it in 131k stratified arXiv abstracts (2015–Sep 2026). Results:

- (H1) Pre-ChatGPT MSO is 9.2% and differs by field.
- (H2/H4) An interrupted time series gives a June-2025 gap of 25.4 pp above the pre-trend, larger in cs than in math. The paper reports placebo breaks, drift placebos with instruments trained only on early years, and many specification variants.
- (Exploratory, the title) Regions defined by generators of different "vintages". Against a region built from generators whose pretraining data predate ChatGPT, the gap is 7.5 pp (3.5 pp for the two locally run ones). Single-generator regions "rise then fall", and the peak quarter correlates with release date (Spearman 0.79, n = 18; 0.66 without three 2026 models added post hoc).
- Secondary results: marker words rise then fall; dispersion is flat once length is fixed; Hansard shows no clear change; and in PERSUADE, English-language learners fall in the region less often than peers, largely explained by holistic score.

The study is disclosed as conducted and drafted by an AI agent, with a plan committed before results.

## 2. Strengths

1. **Unusually careful time-series design for this literature.** The design has a pre-specified evaluation month (fixed in code) and a 34-break placebo grid whose rejection rate (8.8%) is close to nominal, plus a 30-month-horizon grid. The drift placebos are the right control for instrument ageing: instruments trained only on 2015–16/17/18 and evaluated 41–65 months later, before ChatGPT. Nonparametric and quadratic/shortened pre-trends, fixed field weights, no-LaTeX, no-LM-terms, length reweighting, feature-family ablations, threshold 0.4/0.6 and a never-revised check all land between 22.9 and 29.1 pp. The H2 headline is robust to everything I would have asked for on the time-series side.
2. **Honest reporting of negative and awkward results.** H5 is reported as not supported. The first vintage test (release vs 2025-to-2026 change from 2025Q4, rho = 0.18) is disclosed, as are the post-hoc 2026 models, the shared 2026Q3 fall and the 2026 aggregate rise depending on the drafting model. The Hansard placebo failure is reported.
3. **The vintage question is genuinely new and important.** "LLM style" is defined by whichever models are the reference, and recent models are trained on recent writing. Prevalence studies mostly ignore this. Showing that a fixed reference can make the shift look like it is receding is a useful warning for the marker-word literature.
4. **Feature design limits topic leakage.** It drops content words and normalises LaTeX/Unicode dashes. The dash finding is a nice example of an encoding artefact that would otherwise separate the classes.
5. **Reproducibility.** Every number enters the paper through a macro from a results file, and the code is short and readable.

## 3. Weaknesses and probes

### (a) Is MSO a well-defined, useful estimand distinct from detector false-positive rates?

*Well-defined: yes, but only conditional on many researcher choices that the abstract hides.* Eq. (1) fixes the following:
- the feature map phi;
- the generator set, its equal weights (implemented as a 450-text cap per generator), the prompt mix and the decoding;
- the human reference, a pooled 2015–Nov 2022 sample whose field mix itself drifts (eess 1.5% to 16.2%);
- equal priors and truncation at 250 words.

Given these, MSO is the flag rate of one specific detector at its LR = 1 threshold. After ChatGPT it is that detector's flag rate on new data. The conceptual difference from "detector FPR" is interpretive: the paper declines to call pre-period flags errors and declines to subtract them. That is a legitimate, clearly stated choice, but it is a reframing rather than a new quantity.

The Bayes-classifier framing adds little in practice, for three reasons:
- The instruments are explicitly not Bayes (§3 concedes the flag rate bounds nothing).
- Single-generator instruments train on 150 LLM vs 150 human texts. The local single regions share the identical 150 human training abstracts, because `training_set` samples `H` with `random_state=0` and the same `n`.
- Logistic regression and GBM disagree badly at the document level: kappa 0.31 for Vicuna, 0.40 for GPT-4 and 0.48 for the pre-ChatGPT-data region. Logistic regression vs GBM MSO is 5.1% vs 10.4% for Vicuna.

*Useful:* as a within-study time series with a frozen instrument, yes. As a cross-study or cross-region quantity, much less. Its level ranges from 4.4% to 15.3% by field and from about 1% to 18% across single-generator regions in 2015. Because it is a thresholded share, its changes are not on a common scale across regions with different baselines. This matters for the vintage comparison (point (d) below).

*Request (cheap):* state in §3 that MSO is indexed by (phi, reference set incl. prompts, human reference period), and write it as MSO_{phi,R}.

*Also cheap:* report the main gap without P2 next to the headline. Revision outputs keep human content and pull the boundary towards human text. The no-P2 gap is 17.9 vs 25.4 pp, and the no-P2 2015 MSO is 6.7% vs 7.8%. So about 30% of the headline gap depends on including LLM-revised human drafts in the "LLM" class. The abstract does not say so.

### (b) Do the ITS trend gap and its placebos support the headline?

Yes, descriptively. I have no serious objection to "by June 2025 arXiv MSO stood 25.4 pp above its pre-ChatGPT trend". Residual concerns are minor:

- **The placebo grid tests the ITS machinery, not the instrument.** The main instrument's human pool spans the whole pre-period, so pre-period placebo breaks are evaluated in-distribution. The paper's drift placebos handle this correctly. However, three drift instruments is a small sample, and the largest gap (6.5 pp, p = 0.061) is 25.6% of the headline. That is slightly more than "no more than a quarter" (Contribution 3).
- **The 95% CIs exclude instrument variation and field-month clustering** (acknowledged). The defensible range across reference sets and specifications is roughly 17.9 to 29.1 pp. The abstract gives only the point estimate. The trend gap for the GBM instrument is not reported anywhere, even though GBM is the paper's second classifier family (§5, Limitations). See check C4.
- **Pre-trend composition.** Pooled pre-ChatGPT slope is 0.47 pp/yr. With equal field weights (mean of the eight field series in `arxiv_monthly_by_field.csv`, OLS on 2015-01..2022-11) it is 0.27 pp/yr. About half of the pre-trend is therefore field mix. This does not threaten H2 (equal-field gap 26.7 pp), but it weakens the Related-Work sentence aligning "our pre-ChatGPT slope" with Chang (2026).
- **The H3 contrast (30.7 pp, CI 28.3–33.2) is computed against a series that fails its own placebo grid (23.5%).** The text calls Hansard weak. Appendix G still reads it as evidence that speech "changed much less in style". The supportable reading is "no detectable change"; nothing validates Hansard as a control.

### (c) Does the vintage analysis (§6.4) match its exploratory status?

This is my main concern. The analysis gives the paper its title, and the abstract, Contribution 4, the Discussion and the Conclusion all lean on it.

1. **Output length is a confound the paper does not address.** P1 asks for "About {n} words", with n set from the source abstract. Generators differ in length compliance: medians run from 90 (MPT) and 102 (Vicuna) to 176 (Qwen3.5) and 186 (Granite 4.2), from `arxiv_generator_lengths.csv`. Newer generators write longer: Spearman(release, median length) = 0.70, n = 18. Human abstracts also grew longer, with a median of 149 words in 2015, 167 in 2022, 169 in 2025 and 176 in 2026 (`arxiv_length_by_year.csv`). The features include mean/sd sentence length, MTLD and per-token rates whose noise depends on length. Generators that write longer therefore plausibly define regions that later, longer abstracts enter later. From `arxiv_vintage_quarterly.csv` + `arxiv_generator_lengths.csv` + `RELEASE`:
   - Spearman(median output length, peak quarter) = **0.73** (n = 18), against 0.79 for release date.
   - Among the 15 generators chosen before the pattern was seen: rho(release, peak) = 0.66 and rho(length, peak) = **0.67**. The partial rank correlation of release with peak given length is **0.37 (p = 0.17)**.
   - Among the 12 locally run generators (identical prompts), rho(release, peak) = 0.89 and the partial correlation given length is 0.69 (p = 0.01). The vintage signal therefore partly survives on matched prompts, but it is not separable from length in the analysis as reported.
   - The same-family evidence lines up with length too. The two pairs with separated intervals have a newer model that writes longer (Granite 138.5 to 186; Qwen 168.5 to 176.5). The Gemma pair, where the newer model writes shorter (159.5 to 147), is the one whose intervals overlap.

   The Limitations list the length ranges but never connect them to the peak correlation.

2. **The effective n is far below 18.** The 18 regions score the same abstracts. The 13 local or 2026-model single regions share the same 150 human training abstracts, and the RAID regions share the same 450. The peaks fall into three clusters (2023 models mostly 2025Q1–Q3; 2024 models 2025Q2–Q3; 2025–26 models 2025Q4–2026Q2), and peak quarters are tied. The p < 0.001 treats 18 independent pairs. The document bootstrap (0.64–0.86) holds the instruments fixed. The five human-training-sample draws were used only for the sign of the 2025-to-2026 change, not for the peak quarters or rho.

3. **Forking paths.** The peak-quarter statistic was chosen after the pre-declared vintage statistic (release vs 2025-to-2026 change) gave 0.67 on annual means but 0.18 from 2025Q4. Three generators were added after the pattern was seen. Their inclusion raises rho from 0.66 to 0.79. The abstract and the Figure 2b annotation report 0.79.

   In fairness, the seven 2024–25 generators chosen in advance give rho = 0.84 (p = 0.02), so the within-recent-models pattern is not created by the additions.

4. **"Rose and then fell" is not true for all of them.**
   - Cohere's region fell from 2022 to 2025 (10.6% to 9.2%) and has a *negative* trend gap (-2.7 pp). §6.4 says so; the abstract's "all but the newest rose and then fell" does not.
   - Vicuna's region moved by 1.4 pp in total, and its 2026Q3 value (2.7%) is below its 2023Q1 value (4.6%). A "peak" of a series that barely moved is not informative about timing.
   - "The newest" is ambiguous. Granite 4.2 is the most recently released dated generator, and its overlap rose from 2025 to 2026. The intended meaning is "the 2026 model (Claude Opus 5.5)".

5. **The single shared last-quarter fall.** All 18 dated regions fell from 2026Q2 to 2026Q3 (`n_fell_last_quarter = 18`). Only the drafting model's region did not. The two 2026Q2 peaks (gpt-oss, Granite 4.2) are therefore defined by this shared drop, as the caption concedes. Dropping 2026Q3 or truncating at 2026Q1 leaves rho at 0.785, so rho does not depend on it. The interpretive claim "under three of the four 2026 generators it peaked in 2026 or was still rising" does lean on it. The random-window sampler also gives quarter-to-quarter field-mix swings (e.g. econ 86 to 148 per month in 2026). Whether the shared 2026Q3 fall survives equal field weights is untested (check C3).

6. **The cross-region comparisons use percentage points.** "Smaller" (7.5 vs 20.3 pp) compares thresholded shares from regions with different baselines and tightness. On the logit scale (2022 to 2025 yearly MSO from `arxiv_vintage.csv`):

   | Region | Logit change, 2022 to 2025 |
   |---|---|
   | All 14 generators | 1.71 |
   | Title-only 2024–25 open models | 2.10 |
   | Pre-ChatGPT-data region | 1.14 |
   | Two local pre-ChatGPT-data models | 0.79 |
   | **The 2026 model** | **0.76** |
   | RAID GPT-4 alone | 1.71 |

   So the direction "smaller towards older generators" holds against the 2024–25 open models. It is not a general ordering by vintage: on this scale, writing moved towards GPT-4 as much as towards the 14-generator region, and more than towards the 2026 model.

### (d) Does the pre-ChatGPT-data region claim survive the RAID-prompt imbalance?

Partly, and it rests mainly on GPT-4.
- After the 450-per-generator cap, 75% of the region's training texts come from RAID (GPT-4 and Llama-2-Chat 70B).
- Single-generator gaps are GPT-4 11.4 pp, Llama-2-Chat 70B 5.5, Llama-2-Chat 7B 3.7 and Vicuna 1.4 (CI 0.3–2.6). The 7.5 pp is carried mostly by GPT-4, under RAID's prompt and decoding.
- Llama-2-Chat 70B's RAID outputs have a median of 250 words, which equals the truncation length, so that region is also a length region.

Two further points:

- **Prompt mix matters, in a direction the paper does not report.** The two local pre-ChatGPT-data models pooled over *all three prompts* (`arxiv_vintage.csv`, group `old_open_all`) give **12.5 pp (CI 8.7–16.2)**. The seven 2024–25 local models over all three prompts (`arxiv_gensets_its.json`, `local`) give 29.3 pp. The main text says "on our own prompts that part is small". That is true only for title-only prompts. On all prompts, the old-vintage gap is about 43% of the new-vintage gap, against 17% on P1. Report both, since the headline uses all prompts.
- **"Could not have learned it" is stronger than §6.4's own "unlikely".** gpt-4-0613 and Llama-2-Chat were post-trained during 2023. Vicuna is distilled from user-shared ChatGPT conversations. The parenthetical "(Vicuna imitates ChatGPT's conversational style, not its abstracts)" is unsupported: ShareGPT contains abstract-writing and polishing requests, and no evidence is given either way.

Net: "part of the shift points towards generators unlikely to have learned it from post-ChatGPT writing" survives. "Present but small on our own prompts" does not survive as stated (see the all-prompt number). The magnitude is a GPT-4/RAID result.

### (e) The essay/learner claims

- The abstract generalises to "English learners" from US grade 6–12 PERSUADE ELL students. The result rests on **15 in-region learner essays**, with adjusted OR 0.55 (CI 0.32–0.95).
- **"Mostly because of proficiency."**
  - After adding the holistic score, the OR is 0.87 (CI 0.50–1.52). That interval contains both 1 and the unadjusted 0.55, so the binary analysis cannot show attenuation.
  - The continuous margin attenuates from -0.37 to -0.12 SD, which does support "largely".
  - The holistic score is a rater's quality judgement correlated with fluency and lexical diversity, which are the region's features. It is partly a measure of the same construct, not an independent proficiency measure. "Largely tracks essay score" is what was shown.
- **The out-of-genre check points the other way and is not mentioned where the claim is made.** Appendix A(2) says the PERSUADE-trained *style* instrument places **34.1% of TOEFL (non-native) essays vs 5.7% of US 8th-grade essays** in the region. The Limitations mention only that the *perplexity* instrument reverses between learner populations. The style instrument shows the same population dependence. This is out of genre and confounded, but it means the abstract's general statement about English learners is not supported beyond PERSUADE.

### (f) Limitations / Ethics / Acknowledgements: what a chair would object to

1. **No human has read or verified the submitted text.** The disclosure says "no human has edited the text", "Citations were not checked by a human; the human author(s) will read the final paper before release". It also says "Full responsibility for the content, including the citations ... lies with the human author(s)". A chair will read this as authors taking responsibility for a paper they state they have not read. ACL's publication-ethics and AI-assistance policies put verification on the authors. This is a desk-reject or ethics-flag risk independent of the science. Before submission, a human author must read the paper and verify at least the citations. Many are 2026 preprints with arXiv IDs a reviewer cannot easily check: 2606.27052, 2608.26710, 2608.05576, 2609.07447. Then rewrite the sentence in the past tense ("The human author(s) read the full paper and checked every citation before submission").
2. **"Acknowledgements" in the review version.** ARR asks that acknowledgements be omitted from anonymous submissions, while ACL policy requires AI-use disclosure. Retitle the section "AI Use Disclosure" so it is not removed or flagged. Its content is not deanonymising.
3. **The pre-registration claim cannot be verified.** "Committed to version control before any result was computed" is in the contributions paragraph. The commit is withheld, it sits in the authors' own repository, and the Limitations concede it was never frozen with a third party. Either give an anonymised timestamped artefact (e.g. an anonymous mirror with the plan's commit date) or soften the main-text wording (rewrite R15).
4. **Conflict of interest with the 2026 model.** The drafting system is also a reference generator. Its sub-agent sessions produced 50 prompts each without decoding control. The 2026 aggregate rise depends on it, and its region is the least distinct (17.9% of 2015 abstracts). The paper discloses all of this, which is good. It does not say what context the sub-agent sessions had: did their system or session context include the project or study goal? State it in §4 or Limitations, in one line.
5. **Title and framing.** The title centres the exploratory, post-review analysis. A chair may ask that confirmatory and exploratory results be distinguishable from the title and abstract alone. At minimum, the abstract should give the pre-chosen-set correlation (R1).
6. **Data provenance.** The 8th-grade essays derive from Hewlett ASAP (Kaggle competition rules). The paper releases only aggregates, which is correct. Say "used under the competition's research terms" rather than relying on a README badge. The Hansard CC BY-NC-ND handling and the share-alike release of PERSUADE revisions are fine.
7. **Missing limitations.** These sections do not count toward the 8 pages, so adding them is free:
   - generator output length as a confound of the vintage/peak analysis (see (c)1);
   - single-generator regions use the same 150 human training abstracts;
   - logistic regression vs GBM disagreement on single-generator regions (kappa 0.31–0.48);
   - cross-region comparisons in pp across regions with different baselines;
   - the all-prompt old-model gap (12.5 pp).

## 4. Cheap, decisive checks (existing pipeline, no new generation)

- **C1 (length, decisive for the title claim).** In `vintage_quarterly`, before `pd.Series(hit).groupby(q).mean()`, weight each scored abstract by w = p_pre(length bin) / p_quarter(length bin). Use 10-word bins of the cleaned, truncated length, with p_pre from 2015–2022 scored abstracts. Recompute the peaks and rho (all 18, and the 15 pre-chosen). Alternatively score abstracts cut to their first 150 words (as in Appendix H). Report rho and the partial rank correlation of release with peak given generator median length (I get 0.56, n = 18, and 0.37, n = 15, from existing files). If rho stays at 0.6 or above after length weighting, the title claim is much safer.
- **C2 (dependence).** Rerun `vintage_quarterly` for each of the five human-training-sample draws already used in `arxiv_vintage_uncertainty.csv`. Report rho for each draw.
- **C3 (shared 2026Q3 fall).** Recompute the quarterly single-generator series with equal field weights (mean of per-field quarterly means). Report how many regions still fall from 2026Q2 to 2026Q3.
- **C4 (instrument family).** `segmented(monthly(...))` with `mso.fit(..., kind="gbm")` for the main 14-generator region gives the GBM trend gap, one refit. Optionally do the same for the 18 single regions' peaks.
- **C5 (already computed, just report).** Report `old_open_all` (12.5 pp) beside `local` all-prompt (29.3 pp). Report logit-scale 2022-to-2025 changes for the vintage regions (one line or a column in Appendix E).

## 5. Claims stronger than the evidence, with copy-ready rewrites

All rewrites are the same length or shorter (checked by character count) unless marked. Net change is negative, so page 8 will not overflow. New numbers need `\R` macros: 0.66 = `arxiv_vintage_peak.rho_no_new` (exists); 6.5 = drift 2016 gap (exists); 0.73 = new key `rho_length` to add in `vintage_peak()`.

**R1. Abstract (vintage).**
- Quote: "Against single generators, overlap with all but the newest rose and then fell, peaking later for later generators (exploratory rank correlation 0.79, n = 18)."
- Limits: Cohere fell from 2022 to 2025 and has a negative gap. "Newest" is ambiguous (Granite 4.2 rose). 0.79 includes three post-hoc models (0.66 without). Length predicts peaks as well (0.67 vs 0.66 on the 15).
- Rewrite: "Single-generator overlap mostly rose then fell, peaking later for later, longer-writing generators (exploratory rank correlation 0.66, n = 15 pre-chosen)."

**R2. Abstract (consequence).**
- Quote: "A fixed reference set, like a fixed list of marker words such as delve, can therefore show the shift receding while writing keeps moving."
- Limits: "writing keeps moving" is measured only against newer generators, which may have learned from recent writing (§6.4's own caveat). The one region immune to that, the pre-ChatGPT-data region, fell in 2026 (17.9% to 11.9%).
- Rewrite: "A fixed reference set, like a fixed marker list such as delve, can thus show the shift receding while overlap with newer models rises."

**R3. Abstract (learners).**
- Quote: "In student essays, English learners' writing is less machine-like than their peers', mostly because of proficiency."
- Limits: US grade 6–12 PERSUADE only; 15 in-region learner essays. The OR with score is 0.87 (CI 0.50–1.52). The holistic score is a quality rating, not proficiency. The style instrument flags TOEFL non-native essays at 34.1% vs 5.7% for US 8th-grade essays out of genre.
- Rewrite: "In US school essays, learners' writing falls in the region less often than peers', largely tracking essay scores."

**R4. Contribution (3).**
- Quote: "Placebo dates and instruments trained on earlier years give gaps no more than a quarter as large (§6.3)."
- Limits: the largest drift gap is 6.5/25.4 = 25.6%.
- Rewrite: "Placebo dates and instruments trained on earlier years give gaps of at most 6.5 pp (§6.3)."

**R5. Contribution (4).**
- Quote: "The shift is present, though smaller, against generators that are unlikely to have learned it from post-ChatGPT writing; overlap with a single generator tends to peak later for more recent generators, so the trajectory depends on the reference's vintage (§6.4)."
- Limits: the pre-ChatGPT-data gap is carried by GPT-4 (11.4 pp; Vicuna 1.4). "Smaller" holds in pp, but on the logit scale it is not smaller than towards the 2026 model. Peak timing is confounded with output length.
- Rewrite: "The shift is present, though smaller and carried mainly by GPT-4, against generators unlikely to have learned it from post-ChatGPT writing; single-generator overlap tends to peak later for newer, longer-writing generators (§6.4)."

**R6. Contribution (5).**
- Quote: "parliamentary speech changed little; and, contrary to our plan, English learners' essays are less machine-like than their peers'."
- Limits: Hansard fails its placebo grid, and its nonparametric gap ranges from -3.2 to 3.1 pp. The learner limits are as in R3.
- Rewrite: "parliamentary speech showed no clear gap; and, contrary to our plan, US learners' essays fall in the region less often."

**R7. §6.4.**
- Quote: "(Vicuna imitates ChatGPT's conversational style, not its abstracts)"
- Limits: no evidence about ShareGPT content is given.
- Rewrite: "(Vicuna was tuned on user-shared ChatGPT chats)"

**R8. §6.4.**
- Quote: "Part of the shift therefore points towards generators that could not have learned it from recent abstracts, though on our own prompts that part is small."
- Limits: these models were post-trained in 2023, and §6.4 itself says "unlikely". On all three of our prompts the two local old models give 12.5 pp (CI 8.7–16.2), which is not small.
- Rewrite: "Part of the shift therefore points towards generators unlikely to have learned it from recent abstracts; on our title-only prompts that part is small."

**R9. §6.4 (correlation).**
- Quote: "The rank correlation between release date and peak quarter is 0.79 (n = 18, p<0.001; the 2026 model is excluded because its release month is not public)."
- Limits: the p-value assumes 18 independent pairs (shared human training sample, shared scored documents, tied quarters). Output length gives 0.73.
- Rewrite: "Release date and peak quarter have rank correlation 0.79 (n = 18; 2026 model excluded), but output length predicts peaks about as well (0.73)."

**R10. §6.4 (same-family pairs).** Keep the sentence. Add to Limitations, which costs no page space: "In the two same-family pairs with separated intervals, the newer model also writes longer; in the Gemma pair it writes shorter."

**R11. §7 Discussion.**
- Quote: "Detectors, prevalence estimators and marker lists built on a fixed set of models may therefore understate recent change unless the reference is refreshed."
- Limits: one-sided. By the paper's own argument, a refreshed reference may rise because the models learned from recent writing.
- Rewrite: "Detectors, prevalence estimators and marker lists built on fixed models may understate recent change; refreshed ones may mistake models' learning for it."

**R12. §7 Discussion.**
- Quote: "Either way, recent LLMs and recent scientific writing can no longer serve as independent references for each other,"
- Limits: inferred from an exploratory, length-confounded correlation.
- Rewrite: "Either way, recent LLMs and recent scientific writing may no longer be independent references for each other,"

**R13. §8 Conclusion.**
- Quote: "so studies of LLM influence on writing should report the vintage of their reference models and update it."
- Limits: "update it" contradicts §6.4's point that only old-vintage references avoid the who-learned-from-whom problem.
- Rewrite: "so studies of LLM influence on writing should report their reference models' vintage and compare several."

**R14. §6.3 (zero-shot baseline).**
- Quote: "A zero-shot detector (Fast-DetectGPT, Bao et al., 2024, with GPT-2 small) separates our human and LLM abstracts poorly (AUC 0.737) and does not track the shift (Appendix D)."
- Limits: one small scoring model. Appendix D itself says larger scorers might track it.
- Rewrite: "A zero-shot detector (Fast-DetectGPT, Bao et al., 2024) with GPT-2 small as scorer separates our abstracts poorly (AUC 0.737) and misses the shift (Appendix D)."

**R15. §1 (pre-registration).**
- Quote: "Our analysis plan was committed to version control before any result was computed (Appendix A)."
- Limits: the commit is unverifiable to reviewers and sits in the authors' own repository (Limitations).
- Rewrite: "Our analysis plan was committed to our repository before any result was computed (Appendix A)."

**R16. §2 Related Work.** (+4 characters; offset by R4, R7 and R14.)
- Quote: "our pre-ChatGPT slope points the same way."
- Limits: the equal-field-weight pre-slope is 0.27 vs 0.47 pp/yr.
- Rewrite: "our pre-ChatGPT slope (half field mix) agrees."

**R17. Appendix G** (appendix, not page-limited).
- Quote: "We read Hansard as evidence that parliamentary speech changed much less in style than abstracts."
- Limits: 23.5% placebo rejections.
- Rewrite: "We read Hansard as showing no clear change, not as a validated control."

**R18. Limitations (add; free).** "Generator output length rises with release date (rank correlation 0.70) and predicts peak quarter about as well as release date; the vintage pattern is not separated from length. Single-generator regions share one 150-abstract human training sample. The two local pre-ChatGPT-data models give 12.5 pp over all three prompts." Also replace "a perplexity instrument reverses its bias between two learner populations" with "the style and perplexity instruments both flag TOEFL essays far more often than US 8th-grade essays, so the learner result is specific to PERSUADE".

**R19. AI-use section (required before submission, see (f)1).**
- Quote: "Citations were not checked by a human; the human author(s) will read the final paper before release."
- Rewrite, once true: "A human author read the full paper and checked every citation before submission."

## 6. Minor and presentation

- Figure 2b: the x-axis has no 2023 tick, although eight points sit there. The printed "Spearman rho = 0.79" should add "(0.66 without the three 2026 open models)" or mark those points. The Granite 4.2 label overlaps the 2026-model circle.
- Figure 2a: the RAID line keeps summary-style outputs, unlike every single region. Either filter it or move it to the appendix. It currently needs a caption caveat to be read correctly.
- §3: "an equal-weight mixture over a reference set of generators and prompting styles". State that P2 outputs are LLM-revised human drafts, so P_LLM includes human content by construction.
- §6.3: the implied-prevalence levels (42.1% cs) are about 2.4 times Liang et al.'s. Say explicitly that this gap suggests the "nothing else changed" assumption fails, rather than only noting the shared ordering.
- §6.4 is dense: two dozen numbers in about 90 lines. Moving the peak-quarter list into Table 5's caption would free space for the length caveat.
- Table 1: "Released 2026" for the 2026 model, but the release month is "not public". Say "2026 (month undisclosed)".

## 7. Scores

| Score | Value (1–5) |
|---|---|
| Soundness | **3 (Acceptable)** |
| Excitement | **3 (Interesting)** |
| Overall assessment | **3 (Findings)** |
| Reviewer confidence | 4 |
| Reproducibility | 4 |
| Ethics flag | Yes (AI-use statement, item (f)1) |

The H2/H4 time-series result is strong and would, on its own, merit Soundness 4. The title result is exploratory, post hoc in both its statistic and three of its points, and confounded with output length, yet the abstract, Contribution 4, the Discussion and the Conclusion present it as a finding.

**What would raise each by one point:**
- **Soundness 3 to 4:**
  - Run C1 (length-weighted peaks) and C2 (rho across human-sample draws), and report the outcome whichever way it goes.
  - Apply R1, R2, R5, R8, R9 and R18.
  - Report the all-prompt old-model gap and the GBM trend gap (C4, C5).
- **Excitement 3 to 4:**
  - Show that the vintage ordering survives length control (C1) and does not depend on the pp scale (C5 logit column).
  - Give a continuous counterpart of MSO, e.g. the mean calibrated log-LR per month, from the scores the pipeline already produces. This would show that the rise-then-fall is a movement of the distribution rather than threshold geometry.
- **Overall 3 to 4:**
  - Make the soundness fixes above.
  - Make the confirmatory/exploratory split visible in the title and abstract.
  - Resolve (f)1: a human must read the paper and verify citations before submission, and the disclosure must say so.

## Top items

1. Output length confounds the vintage/peak result. Spearman(length, peak) is 0.73 against 0.79 for release; among the 15 pre-chosen generators, the partial rho of release given length is 0.37 (p = 0.17). Run C1 and add the R18 limitation.
2. Abstract overclaims on vintage. It says "all but the newest rose and then fell", but Cohere fell and Vicuna barely moved. It reports 0.79 although 0.66 is the pre-chosen value. "Writing keeps moving" is measured only against newer models (R1, R2).
3. Pre-ChatGPT-data region: mostly GPT-4 under RAID's prompt, and "small on our own prompts" holds only for title-only prompts. All prompts give 12.5 pp (R5, R8, C5).
4. Learner claim: US PERSUADE only, 15 essays, and "proficiency" is really the holistic score. The style instrument flags TOEFL essays far more than US 8th-grade essays, so the claim does not generalise (R3, R6, R18).
5. Chair-level: the disclosure states that no human has read the paper or checked its citations while assigning full responsibility to the humans. Fix this before submission (R19). Also retitle "Acknowledgements" for the review version and soften the unverifiable pre-registration wording (R15).
