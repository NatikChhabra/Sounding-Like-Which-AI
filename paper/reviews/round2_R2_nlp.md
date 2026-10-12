# ARR Review, Round 2: Reviewer 2 (machine-generated text detection, stylometry, LLM homogenization)

**Submission:** "After the Delve Fades: Scientific Abstracts Keep Moving Toward LLM Style"
**Track:** Homogenization and knowledge collapse in LLMs (ACL 2027)

I read the compiled PDF, `main.tex` with the `\R{}` values in `results/numbers.tex`, the code in `code/`, the result files and my round-1 review. I also ran a read-only re-analysis with the project venv. It used the authors' `mso.training_set`/`mso.fit` and their cached features, and all scripts stayed in my own scratch folder. My refit of the RAID-only region reproduces the paper's yearly series exactly (6.4% before ChatGPT, then 17.2% in 2025 and 10.9% in 2026). The numbers marked "my re-analysis" below come from the same pipeline, with the training set restricted to subsets of generators or prompts.

---

## Summary

The paper defines Machine-Style Overlap (MSO). It is the share of a genre's documents that a calibrated classifier places at P(LLM) ≥ 0.5. The classifier uses content-word-free style features (closed-class word rates, coarse POS trigrams, dependency labels, punctuation, sentence-length mean/SD, word length, MTLD) and is trained on balanced pre-ChatGPT human text against an equal-weight mixture of 14 chat generators. Seven are local open-weight models, six are RAID 2023 chat models, and one is "Claude Opus 5.5", produced through agent sub-sessions of the system that also drafted the paper.

Main findings, from 131k stratified arXiv abstracts (2015–2026):

- MSO is 9.2% before ChatGPT, ranging by field from 4.5% (astro-ph) to 15.7% (econ).
- It rises to 45.0% in 2026, a June-2025 trend gap of 25.7 pp.
- The gap survives threshold, no-math, no-LLM-topic, length-reweighting and no-dash variants, and is absent under two placebo break dates and a drift placebo.
- Australian Hansard shows no measurable gap (1.7 pp) when its region is built from the same 8 generators.
- A fixed 8-word marker list peaks in 2024 and returns almost to trend in 2026.
- A region built only from RAID's 2023 models also turns down in 2026, while regions that include 2024–2026 models keep rising.

Secondary results:

- Chat tuning moves base models further into the region.
- Feature-space dispersion declines steadily from 2015, with no break at ChatGPT.
- PERSUADE ELL essays are *less* often in the region (H5 not supported), mostly because of proficiency.
- A Qwen2.5-0.5B perplexity instrument reproduces Liang et al.'s TOEFL false-positive bias (42.9% vs 3.4% for US 8th-grade essays), but flags PERSUADE ELL essays *less* than non-ELL essays. From this the paper concludes that detector bias "depends on the population, not on non-native authorship."

## Assessment of the revision

This is a substantially better paper than round 1, and most of my round-1 requests were addressed in good faith:

- LaTeX and dash normalisation (`features.delatex`), plus a no-dash ablation.
- A no-math subset and a length-reweighted series.
- A generator-set table and figure.
- The same generator set for arXiv and Hansard in the control comparison.
- Held-out-generator recall in an appendix.
- Held-out (LOMO) numbers for chat models in the base-vs-chat comparison.
- H5 reported as not supported.
- A proficiency adjustment and a perplexity instrument on the same essays.
- The self-test removed.
- "Pre-registered" softened to "analysis plan committed before results".
- Forman (2008), Khan et al. (2025), Shaib et al. (2024), Binoculars, Fast-DetectGPT, Herbold et al. and Berber Sardinha added.

The drift placebo is a particularly good addition. It is the right test for "the instrument simply ages", and it comes out clean.

What remains is mostly about **interpretation**. The paper's two headline narratives are the title/abstract claim that abstracts "keep moving toward LLM style" after the delve fades, and the claim that the generator-set result shows writing "moving away from 2023-era LLM style toward the style of later models". My re-analysis shows that both depend on a confound the paper does not discuss: *prompt task* is confounded with *model vintage* in the generator-set comparison. I also find that a lexical method updated to the same generators reproduces the "keeps rising" pattern, which weakens the claim that marker-word methods as such understate the shift.

## Strengths

1. **A clear, well-posed estimand with honest framing.** §3 now states plainly that MSO is a classify-and-count flag rate (Forman 2008). It does not claim that a finite classifier bounds the Bayes quantity, and it treats MSO as instrument-dependent. That is the correct position, and it is better than most of the prevalence literature, which subtracts the pre-period "AI share" as noise without comment.
2. **The core arXiv result is robust.** A post-2022 rise of about 25 pp over trend survives every variant in Table 1, two placebo dates, an out-of-sample drift placebo, a no-LLM-topic subset and a comparison genre built from the same generators. I checked one more thing the authors did not: equal field weighting. The "all" series pools fields whose shares change over time (econ+eess go from 2% of 2015 documents to 21% in 2022). Equal-field yearly means are 9.5% (2015), 11.8% (2022), 41.7% (2025) and 45.3% (2026), essentially the same as the pooled series. I consider the existence and size of the post-ChatGPT movement established *for this instrument family*.
3. **Generator dependence is reported rather than hidden.** Table 1 and Figure 3 make the dependence on the reference set visible (RAID-only gap 5.9 pp vs local+frontier 32.3 pp). §6.5 also admits that the 2026 model was added after a preliminary run. Few papers in this area would report this.
4. **The LOMO result is important for the detection community.** The 2026 model has 20.7% held-out recall on abstracts and 21.3% on Hansard, against 59–95% for the other generators. This is direct evidence that a region built from older or smaller models does not cover current frontier output, and it is worth publishing on its own.
5. **The learner analysis is now careful.** It uses three instruments, a proficiency adjustment (OR 0.53 → 0.82), seed stability, the counts behind the thresholded effect (15/666), and an explicit statement that H5 failed. The perplexity replication on Liang et al.'s own released essays is a useful sanity check.
6. **Transparency.** Numbers are macro-generated, the code is small and readable, and the AI-use statement is unusually specific, including the fact that the drafting system also generated reference data.

## Weaknesses (most severe first)

### W1. The generator-set result confounds model vintage with prompt task, so "moving from 2023-era to later LLM style" is not warranted as stated.

The paper interprets the divergence in Figure 3 (RAID-only falls in 2026, regions with newer models keep rising) as abstracts "moving away from 2023-era LLM style toward the style of later models" (§6.5, Discussion). But the RAID set differs from the local and frontier sets in much more than vintage:

- **Task.** RAID's abstracts were generated only from a title (comparable to P1). There is no revision prompt (P2) and no evasion prompt (P3). The local and frontier sets are two-thirds P2/P3.
- **Register.** Many RAID chat outputs are third-person paper summaries rather than abstracts. 68% of ChatGPT, 83% of GPT-4 and 76% of Llama-chat RAID "abstracts" open with a paper-level framing ("In the paper '...'", "This paper ..."). The 20 words most over-represented in RAID chat outputs relative to pre-2022 human abstracts (log doc-frequency ratio, my re-analysis) are *titled, academic, concludes, discusses, abstract, explores, presents, contributes, …*. That is a summary-of-a-paper register, not an "era" of LLM style.
- **Decoding.** RAID uses greedy and sampling decoding, with and without repetition penalty. The local models use temperature 0.8 Ollama defaults, which are 4-bit-quantised builds unless stated otherwise. The 2026 model was run with uncontrolled decoding.

I separated task from vintage by refitting the region on prompt subsets (yearly MSO among scored abstracts; same code and caps as the paper):

| Region built from | pre-ChatGPT | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| RAID chat (2023 models, title-only) | 6.4 | 7.1 | 10.8 | 14.9 | 17.2 | **10.9** |
| Local 7, P1 only (title-only) | 3.6 | 4.7 | 9.1 | 17.2 | 28.9 | **29.6** |
| Local 7, P3 only (title-only, "avoid AI phrasing") | 4.8 | 6.2 | 10.9 | 20.1 | 33.2 | **38.4** |
| Local 7, P2 only (revise a human draft) | 14.7 | 17.1 | 25.2 | 37.0 | 51.9 | **59.9** |
| Local 7, all prompts | 8.8 | 9.9 | 16.6 | 28.2 | 42.4 | **48.3** |
| 2026 model only, P1+P3 | 13.5 | 12.3 | 12.6 | 15.2 | 22.6 | **36.4** |
| 2026 model only, P2 | 35.4 | 37.3 | 41.7 | 47.7 | 59.8 | **70.0** |
| 2026 model only, all | 20.3 | 19.2 | 21.8 | 26.7 | 41.0 | **58.2** |

Several conclusions follow:

- **(a)** Holding the task fixed at title-only generation, the 2024–25 open models do *not* "keep rising". They plateau from 2025 to 2026 (28.9 → 29.6). The 2026 continuation in the paper's local regions comes mainly from the revision and evasion prompts.
- **(b)** The most defensible reading of Figure 3 is therefore "2025–26 abstracts increasingly resemble LLM-*revised* human drafts and plain-register output, not title-to-abstract generations". That is a more specific and, I think, more interesting claim than "later-model style", and it fits the revision-dominated adoption that Lin & Zhu (2025) and Liang et al. describe.
- **(c)** A genuine vintage signal does exist. The 2026-model title-only region is flat from 2021 to 2024 (12–15%) and then rises sharply in 2025–26 (22.6 → 36.4), while RAID title-only falls. This is the paper's best evidence for vintage, but it rests on one model generated without decoding control (W4).
- **(d)** All of this is also exactly what *generator turnover in authors' actual tool use* would produce, with no change in human style. Authors who used ChatGPT-3.5 in 2023 and newer assistants in 2025–26 would empty a 2023 region and fill a current one. The paper says MSO is "agnostic to authorship", but the title ("Scientific Abstracts Keep Moving Toward LLM Style") and the phrase "abstracts moving away from 2023-era LLM style" read as claims about writing style, not about which tools are in use.

**Fix:**
- Add the prompt-stratified regions above, or equivalent, to Table 1 and Figure 3.
- Compare vintages only at fixed task, e.g. RAID vs local-P1 vs 2026-P1. Ideally regenerate RAID's titles with the local models and the P1 template so that only the model differs.
- Rewrite §6.5 and the Discussion to say that the 2026 continuation is carried by revision-style and 2026-model regions.
- Change the title and abstract so they do not imply a change in human style that the design cannot separate from tool turnover. For example: "…abstracts increasingly resemble current-LLM revisions".

### W2. The marker-word comparison is not like-for-like, and a lexical method updated to the same generators shows the same pattern as MSO.

§6.4 and the abstract conclude that "marker-word counts therefore understate how far scientific abstracts have moved toward LLM style". But the comparison pits a *fixed 2024 list of 8 words mined from ChatGPT-era text* against a *style region rebuilt with a 2026 model*. W1 already shows that a 2023-defined style region turns down in 2026 just as the 8-word list does.

I ran the matched lexical comparison. For each generator family I mined the 20 words most over-represented (by document frequency, ≥3% of generations) relative to the pre-2022 human training pool, using P1+P3 outputs only. I then tracked the share of scored abstracts containing at least one of them:

| Markers mined from | pre-ChatGPT | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| RAID chat | 10.9 | 13.9 | 16.8 | 19.8 | 20.3 | 15.3 |
| Local 7 (P1+P3) — list contains *delves, underscores, showcasing, intricate, paving, avenues* | 4.9 | 7.0 | 11.0 | 18.5 | 22.2 | 13.7 |
| 2026 model (P1+P3) — *roughly, fewer, alone, grows, depends, gives, little, poorly, …* | 23.5 | 23.5 | 23.8 | 23.2 | 26.5 | **34.7** |

(Mean counts per abstract show the same shapes.)

Words mined from the 2026 model are flat through 2024 and then rise sharply in 2025–26, tracking the 2026-model style region. Updated lexical markers therefore also "keep moving". This is a crude list: it has a high baseline and some topical words. Even so, it shows that the contrast in §6.4 is mainly between generator *vintages*, not between *lexical and stylistic* measurement. The paper's claim is supported only where generator and prompt are held fixed. For the local-7 P1+P3 set, mined markers fall from 22.2 to 13.7 in 2026 while the matched style region still edges up (30.4 → 32.6). That *matched* version is the version the paper should present. It is a narrower and more defensible form of the "after the delve fades" claim.

Two further points:

- The lexical half of the story is not new. Geng & Trotta (2025), already cited, show that "delve" and other publicised words fell after early 2024 while other ChatGPT-preferred words (e.g. *significant*) kept rising. §6.4 should credit them for the lexical decline-with-persistence pattern and position MSO's contribution relative to it.
- Point-biserial r = 0.12 between marker and region "mostly pick out different documents" is expected, because the marker rate is about 1–5%. Report overlap conditional on base rates (e.g. lift or odds ratio) instead.

**Fix:**
- Replace the fixed-list comparison with matched comparisons: markers mined from each generator set vs MSO from the same set.
- Credit Geng & Trotta.
- Drop "marker-word counts understate…" from the abstract, or qualify it as "fixed marker lists built from 2023-era models understate…". That qualified statement is true and is the actual finding.

### W3. Is MSO more than a detector flag rate? The prevalence link is still missing.

§3 now concedes that MSO is classify-and-count. Its distinctive content is therefore (i) the pre-period level and its field structure, and (ii) post-period movement that prevalence cannot explain. Neither is pinned down:

- (i) is explicitly left uninterpretable ("may reflect the writing, classifier fit that varies by field, or both"). The GBM and logreg baselines also differ by a factor of 2 in astro-ph (2.0% vs 4.5%) and math (5.1% vs 9.0%).
- For (ii), round 1 asked for the mixture identity MSO(S_t) = FPR + α(TPR − FPR), so that one can see whether the rise exceeds what plausible prevalence implies. This was not done.

A back-of-envelope version is informative. With FPR = the field's pre-period MSO and TPR = 0.84 (mean LOMO recall of the 13 non-2026 generators), cs implies α ≈ 0.41 in 2024 and α ≈ 0.67 in 2025. Liang et al. (2024b) estimate roughly 17–18% LLM-modified cs abstracts by early 2024. With the 2026 model's held-out recall (0.21) as TPR, the 2025 cs value implies α > 1, which is impossible.

So the MSO rise is either far larger than published prevalence, which would be evidence of human style adoption or detector drift and is precisely the information MSO could add, or it is not interpretable as prevalence at all. Either answer would make the paper sharper. As written, a skeptical reader can treat MSO as "yet another detector's positive rate with a pre-period", in the line of Khan et al. (2025), Askitas (2025) and Kusumegi et al. (2026).

**Fix:**
- Add a short subsection that reports implied α under a range of TPRs (LOMO min/mean, in-sample) by field and year, and compares it with Liang et al. (2024b) and Kobak et al. (2025).
- State which of the two readings the data favour.
- Add one off-the-shelf detector series on the same arXiv sample (Binoculars or Fast-DetectGPT flag rate by year at a pre-period-calibrated threshold) as a baseline. Without that, a reviewer cannot tell what the content-word-free stylometric instrument buys over a standard zero-shot detector.

### W4. The 2026 reference model is uncontrolled and is the paper's own drafting system.

The 2026-model texts drive the abstract's "keeps rising" claim. They also provide the only evidence for vintage that is not confounded with task (W1c). But they were produced by agent sub-sessions in batches of 50 prompts, with no decoding control, no fixed or disclosed system prompt, possible within-batch dependence, and no API snapshot. My checks raise three concrete issues:

- **Light revisions.** 54% of the 2026 model's P2 revisions retain more than 30% of the source abstract's word 6-grams, against 1–5% for most local models (Qwen3 is similar at 41%). This explains its P2 separability of 0.67 AUC. A region trained on near-copies of human abstracts with a "1" label inflates every level. The 2026-model-only region puts 20.3% of pre-ChatGPT abstracts, and its P2-only region 35.4%, on the LLM side.
- **Memorisation.** Prompts use titles of real pre-2022 arXiv papers. At least one title-only P1 output reproduces its source abstract almost verbatim (88% 6-gram overlap; "Learning meaningful and compact representations with disentangled semantic aspects…"). Others are recognisable paraphrases (e.g. PolyGen). This is rare (≤1% above 0.6 overlap), but the frontier model's "LLM" class partly contains recalled human text.
- **Unknown context.** The paper does not say what context the sub-agents had. If they knew the study's goal or saw other prompts, their outputs are not a sample of the model's ordinary behaviour.

**Fix:**
- Generate the 2026-model set (and ideally one or two other current commercial models, e.g. GPT- and Gemini-class) through the API, with logged model ID, temperature and system prompt.
- Disclose the exact sub-agent instructions for the current set.
- Filter generations whose 6-gram overlap with the source exceeds a threshold, for P1/P3 and for P2 alike.
- Until then, present every 2026-model result as exploratory and do not let the title rest on it.

### W5. The perplexity replication is reasonable, but the "population, not non-native authorship" claim overreaches and is less novel than presented.

The instrument is a single-feature, isotonically calibrated threshold on Qwen2.5-0.5B log-perplexity, trained on PERSUADE human vs LLM essays. On Liang et al.'s released essays it flags 42.9% of TOEFL essays against 3.4% of US 8th-grade essays. That qualitatively reproduces Liang et al. (their seven detectors averaged about 61% on TOEFL and were near zero on 8th-grade essays). Good. Concerns:

1. **Novelty.** Liang et al. (2023) already attributed the bias to low perplexity from constrained vocabulary rather than to L1 status. They showed that enriching vocabulary removes it. Jiang et al. (2024) examined detector fairness for native vs non-native GRE writers in a large-scale assessment. "Detector bias depends on the population" is therefore the existing mechanistic account. The new element is the *within-PERSUADE* reversal, and that is what the paper should claim.
2. **The reversal is not proficiency-adjusted for the perplexity instrument.** It is adjusted only for the style instrument. Spelling errors inflate subword perplexity, so the ELL perplexity gap (3.29 vs 3.02) may be largely orthographic. Re-run the perplexity contrast with the holistic score covariate and on spell-normalised text.
3. **Possible contamination.** Qwen2.5 (2024) post-dates the public release of both PERSUADE 2.0 and Liang et al.'s essays. Memorised documents get lower perplexity, which pushes them toward being flagged, possibly unequally across sets. Repeat with a scorer whose training data predate 2022 (GPT-2, Pythia, OPT), and with a standard zero-shot detector (Binoculars) rather than raw perplexity.
4. **Generalisation.** "Not on non-native authorship as such" is a population-level generalisation from two datasets with different genres, prompts, lengths and an out-of-genre threshold for TOEFL. Rephrase to "in these two learner populations the bias has opposite signs, tracking predictability rather than L1 status."

### W6. Feature design: topic robustness is improved but still asserted rather than shown, and the dispersion result is length-confounded.

- **The LaTeX/encoding normalisation is now correct and well tested.** The `delatex` unit tests cover `---`/`--`, math, `\emph`, `~` and `\cite`. Whitespace from arXiv hard-wrapping is collapsed by `clean`. I found no remaining encoding asymmetry in the top features. Dash features no longer appear among the most LLM-typical arXiv features, and the no-dash ablation is unchanged (26.2 pp).
- **MTLD dominates.** Its coefficient (1.25) is twice that of any other feature, and it is the top LLM-typical feature in all three genres. MTLD depends on terminology repetition, which depends on field and topic, and it is unstable on short texts. Hyphen rate (`pun:-`, LLM-typical) also partly tracks compound terminology. "Content-word-free" is not the same as "topic-robust". The drift placebo and the no-LLM-topic subset help, but a **feature-family ablation** (drop scalars incl. MTLD; drop POS; drop dependency; drop function words; drop punctuation) was requested in round 1 and is still missing. It is cheap and would show which conclusions rest on lexical diversity alone. This matters for interpretation: if MSO mostly measures "fluent, lexically diverse writing", as the essay analysis itself concludes, then part of the arXiv rise could be general fluency gains from any writing tool (Grammarly, DeepL, editing services), not LLM style specifically.
- **Dispersion (§6.7) is confounded with length.** Features are per-token rates. Longer documents give less noisy rates, so mean distance to the centroid falls mechanically as abstracts lengthen. Median length grew from 149 to 176 words over the same period in which dispersion fell from 34.2 to 30.9. Recompute dispersion on fixed-length windows (e.g. the first 120 words of every abstract ≥120 words) before interpreting "steady homogenization". This is the paper's only direct homogenization measure for the theme track, so it should be solid.

### W7. The generator set does not represent what arXiv authors use.

The seven local models are 7–20B, probably 4-bit-quantised Ollama builds. RAID's are 2023 models. The only current commercial-grade model is W4's. The authors of 2025–26 arXiv abstracts mostly use GPT-4o/GPT-5-class, Gemini, Claude and DeepSeek assistants, along with editing tools.

The paper's own conclusion ("Measuring that shift requires reference generators as current as the writing being measured") argues for at least two controlled current commercial models. Without them, the level of MSO and the 2026 trajectory are statements about this particular mixture. Report quantisation and model tags, and add API models (W4).

### W8. Remaining presentation and completeness issues.

- **Incomplete submission.** The AI Use section still contains a visible red "[TODO: confirm after the author's spot-check]". It must be resolved, and the spot-check must actually be done, before the claim is printed.
- "For each of **8.00** archives" (§4): a macro formatting bug (`corpus_stats.arxiv_n_fields`).
- Bibliography encoding: "All thats human is not gold" is missing its apostrophe, and "Digitization of the Australian Parliamentary Debates, 19982022" is missing its en dash.
- Liang et al. (2024b) is cited as a preprint. It has a peer-reviewed version (COLM 2024); please cite that.
- The ITS fits a *linear* post-period slope through September 2026, but the series visibly bends in 2025–26 and the 2026 RAID series reverses. Report the observed June-2025 window mean next to the fitted gap, or use a piecewise post-trend, so that the headline does not depend on extrapolating a misspecified line.
- §6.6 base vs chat: base outputs are about twice as long (GPT-2 median 279 words, MPT 311 vs 90–134 for most chat models). They also come from a continuation template, so "chat tuning amplifies the style" should stay "indicative", as the text says. The section title states it as a finding.
- The H4 sentence ("same high-CS, low-mathematics ordering that prevalence studies report") is fine, but q-bio has the largest gap and is not among the fields in Liang et al. (2024b). Say so.

## Missing references (verified)

- **Askitas, N. (2025).** *The Behavioral Signature of GenAI in Scientific Communication.* IZA Discussion Paper 18062. https://docs.iza.org/dp18062.pdf. It uses economics working-paper abstracts, stylometric shifts after ChatGPT, a classifier that flags a growing "GPT-like" share, and an event study with placebo checks. This is the closest prior design to §6.3, including the econ field. I requested it in round 1 and it is still not cited.
- **Kusumegi, Yang, Ginsparg, de Vaan, Stuart, Yin (2026).** *Scientific production in the era of Large Language Models.* arXiv:2601.13187. https://arxiv.org/abs/2601.13187. It covers about 2.1M arXiv-family preprints and LLM-adopter identification, with consequences for writing complexity. It is directly relevant to the arXiv population and to the "fluent but not better" reading of MSO.
- **Jiang, Hao, Fauss, Li (2024).** *Detecting ChatGPT-generated essays in a large-scale writing assessment: Is there a bias against non-native English speakers?* Computers & Education 105070. https://doi.org/10.1016/j.compedu.2024.105070. It is the main follow-up to Liang et al. (2023) on native vs non-native fairness of detectors, and it is necessary context for §6.8's population claim.
- (Already cited, but its finding should be credited in §6.4.) **Geng & Trotta (2025)**, Findings of ACL. https://arxiv.org/abs/2502.09606. "Delve" and other publicised words fell after early 2024 while other ChatGPT-preferred words kept rising.

## Questions for the authors

1. Can you add prompt-stratified regions (P1/P2/P3 separately, per vintage) to Table 1? Does the "keeps rising" result survive when vintages are compared at a fixed task?
2. What exactly did the 2026-model sub-agents receive (system prompt, project context, batch composition)? Were any of them aware of the study's purpose?
3. What implied α does the June-2025 gap correspond to under the mixture identity, by field? How does it compare with Liang et al. (2024b)?
4. What does a Binoculars or Fast-DetectGPT flag-rate series look like on the same arXiv sample?
5. Which conclusions survive dropping MTLD (or all scalar features)?
6. Does the perplexity ELL contrast survive the holistic-score covariate, spell normalisation and a pre-2022 scorer LM?
7. Does dispersion still decline on fixed-length windows?
8. Were the Ollama models run at default quantisation? Which exact tags and digests were used?

## Scores

- **Soundness: 3 / 5.** The central empirical result, a large post-ChatGPT movement of arXiv abstracts into an LLM-style region absent in placebos and in Hansard, is now well supported. The interpretive claims built on it are not: "keeps moving", "2023-era to later style" and "markers understate" rest on a generator comparison confounded by prompt task, on one uncontrolled frontier generator, and on an unmatched lexical baseline.
- **Excitement: 3 / 5.** Useful descriptive data, a candid treatment of instrument dependence, and a LOMO finding that matters for detection. The construct remains close to a detector flag rate, and the most interesting possible contribution (the gap between MSO and plausible prevalence) is not yet made.
- **Overall assessment: 3 / 5** (Findings-level once the required changes below are made; main-conference with the matched analyses and a controlled current-model set).
- **Reviewer confidence: 4 / 5.** I re-ran the region-subset and marker-mining analyses with the authors' code and cached features.

## Required changes for acceptance

1. **Separate vintage from task (W1).** Add prompt-stratified generator-set results. Compare vintages at fixed task. Rewrite §6.5, the Discussion, the abstract and the title so that the 2026 continuation is attributed to what the data show: revision-style regions and the 2026 model, not a general "later-model style". Acknowledge tool turnover as an equally consistent explanation.
2. **Matched marker comparison (W2).** Compare MSO with markers mined from the *same* generator set. Present the local-set matched contrast as the evidence for "style persists while markers fade". Credit Geng & Trotta (2025). Qualify the abstract to "fixed, 2023-era marker lists understate…".
3. **Relate MSO to prevalence (W3).** Report implied α by field and year under a range of TPRs, compare it with published prevalence, and add one standard zero-shot detector series on the same arXiv sample.
4. **Control or demote the 2026 model (W4).** Use API generation with logged parameters, filter near-copies and memorised outputs, and disclose the sub-agent instructions. Otherwise mark all 2026-model-dependent results as exploratory and keep them out of the title.
5. **Perplexity claim (W5).** Adjust the perplexity contrast for proficiency, check spelling and contamination with a pre-2022 scorer, cite Jiang et al. (2024), and narrow "detector bias depends on the population, not on non-native authorship" to what two datasets support.
6. **Feature checks (W6).** Add a feature-family ablation (at minimum without MTLD/scalars), and recompute dispersion on fixed-length windows.
7. **Completeness (W8).** Remove the TODO and complete the citation spot-check, fix "8.00 archives" and the bibliography encoding, cite Askitas (2025) and Kusumegi et al. (2026), and report observed window means next to the linear-ITS gap.
