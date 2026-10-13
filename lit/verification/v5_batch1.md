# Citation verification v5, batch 1 (21 keys)

Checked 2026-10-13. Sources used: arXiv abstract pages and PDFs (full text extracted locally), ACL Anthology, PMLR, ICLR proceedings (including its BibTeX), AAAI OJS, the IZA PDF and IZA BibTeX, Springer page metadata (fetched with curl), Europe PMC and PMC full text, Crossref, Semantic Scholar, the Hugging Face model cards and API, Google's Gemma release log, the PERSUADE 2.0 GitHub README, and the University of Memphis repository. ScienceDirect and science.org returned 403. For those papers the abstract came from an institutional or index copy, as noted under each key.

The input file mangles the second Fast-DetectGPT sentence: the `%` characters dropped text. main.tex l.352-357 is intact, and that is the version I checked.

---

## anderson2024homog
**Sentence:** "Writing or ideating with instruction-tuned models reduces content diversity across users \citep{padmakumar2024, doshi2024, anderson2024homog}"

**Verdict: SUPPORTED.** The arXiv abstract (2402.01536) describes a user study with 36 participants. Ideas produced with ChatGPT were less semantically distinct across users than ideas produced with an alternative creativity-support tool. ChatGPT is instruction-tuned, and the task is ideation, which the sentence's "or ideating" covers.

**Bib:** Crossref matches the authors (Anderson, Shah, Kreminski), the container title "Creativity and Cognition", pp. 413-425, and the date of June 2024. OK. Optional: use the fuller booktitle "Proceedings of the 16th Conference on Creativity \& Cognition".

**Fix:** none.

## anderson2025spoken
**Sentences:** (1) "LLM-associated words have become more frequent in unscripted speech \citep{yakura2024, anderson2025spoken}"; (2) "LLM-associated vocabulary has grown in human speech \citep{yakura2024, anderson2025spoken}"

**Verdict: SUPPORTED for both.** The AIES abstract reports a moderate but significant rise after 2022 in words commonly associated with LLMs. The data are 22.1M words of unscripted speech from science and technology podcasts. The baseline synonyms show no shift, and the authors leave causation open. Neither sentence claims causation.

**Bib:** Crossref matches: Proc. AAAI/ACM Conf. on AI, Ethics, and Society 8(1):179-191, published online 15 Oct 2025, first author Bryce Anderson. OK.

**Fix:** none.

## askitas2025
**Sentence:** "\citet{askitas2025} finds an abrupt stylometric shift in economics working-paper abstracts in 2023 with an event-study design and a classifier."

**Verdict: SUPPORTED.** Evidence is the abstract on PDF p.3. The data are IZA DP economics working-paper abstracts, and the shift follows ChatGPT-3.5 in March 2023. The event-study regressions with fixed effects and placebo checks find the shift abrupt and persistent. A classifier trained on GPT-optimised variants flags a growing share of post-March 2023 abstracts.

**Bib:** The title, the author (Nikos Askitas), 2025 and DP No. 18062 are correct. **Error:** `institution = {IZA Network @ LISER}` matches neither the PDF nor IZA's own BibTeX, which gives "Institute of Labor Economics (IZA)", Bonn, Aug 2025. The paper also circulates as CESifo WP 12069. I found no journal version.

**Fix (bib):** `institution = {Institute of Labor Economics (IZA)}, address = {Bonn}, month = aug`.

## bao2024fastdetectgpt
**Sentences:** (1) "Zero-shot detectors use token-likelihood statistics \citep{hans2024binoculars, bao2024fastdetectgpt}"; (2) "the analytic Fast-DetectGPT criterion \citep{bao2024fastdetectgpt} computed with GPT-2 small ... larger scoring models, as in the original method, may not."

**Verdict (1): SUPPORTED.** The criterion is a conditional probability curvature. Per §2 and Algorithm 1, it compares the passage's token log-probabilities under a scoring model with those of sampled alternatives.

**Verdict (2): SUPPORTED.** Appendix B, "Analytical solution of conditional probability curvature", is the analytic criterion. The original method scores with larger models: Neo-2.7B in the black-box setting, with GPT-J sampling (Table 2 caption, §4). Its smallest scorer is GPT-2 in the gpt2-xl 1.5B variant (Table 4). Every model in the paper is therefore larger than GPT-2 small, so the contrast holds.

**Bib:** Matches ICLR's official BibTeX exactly: authors, title, pages 24814-24836, editors, URL. OK.

**Fix:** none.

## bentley2026
**Sentence:** "\citet{bentley2026} track a composite LLM-associated style index alongside vocabulary-complexity measures in arXiv abstracts"

**Verdict: SUPPORTED.** The arXiv abstract (2606.27052) covers millions of arXiv abstracts from 2010 to 2025. It tracks a composite LLM-associated style index together with vocabulary size and the Heaps' and Zipf's exponents, and says the index's link to the vocabulary-based complexity measures flattens after 2022.

**Bib:** Authors, title, 2026 and eprint are correct. v1 is dated 25 Jun 2026 and has no journal-ref. I found no published version. OK.

**Fix:** none.

## berbersardinha2024
**Sentence:** "LLM text differs systematically from human text in lexico-grammatical features \citep{reinhart2025, munozortiz2024, berbersardinha2024, herbold2023}"

**Verdict: SUPPORTED.** The abstract (FAPESP index copy, via search; ScienceDirect returned 403) compares GPT texts with human written and spoken texts on Biber's (1988) five dimensions. Those dimensions are lexico-grammatical. It finds significant disparities, and a discriminant analysis separates AI texts easily.

**Bib:** Crossref matches: sole author Tony Berber Sardinha, Applied Corpus Linguistics 4(1), 100083, April 2024. OK.

**Fix:** none.

## brooks2024
**Sentences:** (1) traces of LLM-assisted writing in "encyclopedias"; (2) the pre-ChatGPT LLM share is used "to calibrate thresholds \citep{brooks2024}"; (3) "classifier- and detector-based studies label documents \citep{..., brooks2024, ...}"

**Verdict: SUPPORTED for all three.** The ACL Anthology abstract reports these points:
- (1) Detectors flag over 5% of new English Wikipedia articles.
- (2) GPTZero and Binoculars thresholds are set to a 1% false-positive rate on articles from before GPT-3.5.
- (3) It is a detector-based study that labels individual articles.

**Bib:** Matches the Anthology record: WikiNLP 2024, pp. 67-79, Brooks, Eggert, Peskoff. OK.

**Fix:** none.

## casal2023
**Sentences:** (1) "readers are poor at telling human from machine text \citep{clark2021, jakesch2023, casal2023}"; (2) "Readers misjudge machine text \citep{clark2021, jakesch2023, casal2023, gao2023}."

**Verdict: SUPPORTED for both.** The abstract (Univ. of Memphis repository, digitalcommons.memphis.edu/facpub2/10) reports 72 reviewers from applied-linguistics journals. Their overall rate of correct identification of AI versus human research abstracts was 38.9%.

**Bib:** Crossref matches: Casal and Kessler, RMAL 2(3), 100068, Dec 2023. OK.

**Fix:** none.

## chakraborty2024
**Sentence:** zero-shot detectors "need more text as machine and human distributions converge \citep{chakraborty2024}"

**Verdict: SUPPORTED.** The PMLR abstract says detection gets harder as machine text nears human quality but stays possible with enough data. It derives sample-complexity bounds in terms of sample size or sequence length.

**Bib:** Matches PMLR v235: ICML 2024, pp. 6093-6115, title with the "Position:" prefix, first author Chakraborty. OK.

**Fix:** none.

## chang2026
**Sentence:** "\citet{chang2026} show that PubMed, Wikipedia and Stack Exchange text became more predictable to small language models over 2014--2024, a trend that began before generative AI"

**Verdict: SUPPORTED.** The Springer abstract (dc.description meta) covers human writing in all three sources over 2014-2024. Perplexity and Binoculars under OPT-125M, GPT-2 and Llama-3.2 show it becoming more machine-predictable, and the abstract says the trend predates widespread generative-AI adoption. "Small" fits OPT-125M and GPT-2. The abstract does not give the Llama-3.2 size.

**Bib:** Matches Springer metadata: Scientometrics 131(3):1635-1654, March 2026 (online 9 Mar 2026), sole author Eunsuk Chang. OK.

**Fix:** none.

## clark2021
**Sentences:** (1) "readers are poor at telling human from machine text"; (2) "Readers misjudge machine text".

**Verdict: SUPPORTED for both.** The ACL Anthology abstract says untrained evaluators told GPT-3 text from human text at about chance. Training raised accuracy only to about 55%, and the gain was not significant across domains.

**Bib:** Matches the Anthology record: ACL-IJCNLP 2021, pp. 7282-7296, first author Clark. OK.

**Fix:** none.

## crossley2024persuade
**Sentence:** "PERSUADE~2.0 \citep{crossley2024persuade}, N pre-ChatGPT essays by US students in grades 6--12 on K prompts, with English-language-learner (ELL) status and a holistic score."

**Verdict: SUPPORTED.**
- The PERSUADE 2.0 README describes over 25,000 argumentative essays by US students in grades 6-12, on 15 prompts.
- Version 2.0 adds holistic scores to every essay and carries demographic data for each writer.
- ELL status is documented in the PERSUADE 1.0 article (PMC9767095, "Participants" section), for a sub-sample of n = 24,787.
- The essays are pre-ChatGPT: the 1.0 article was received in Feb 2022, and the corpus was the basis of the 2021-22 Kaggle competition.

The essay and prompt counts are the paper's own macros and are not checked here.

**Bib:** Crossref matches: Assessing Writing vol. 61, 100865, July 2024, author order Crossley, Tian, Baffour, Franklin, Benner, Boser. The GitHub README lists Baffour second, but the publisher's order should be used. OK.

**Fix:** none.

## doshi2024
**Sentence:** "Writing or ideating with instruction-tuned models reduces content diversity across users"

**Verdict: SUPPORTED.** The abstract (Europe PMC, PMC11244532) describes an online experiment in which writers received story ideas from an LLM. The resulting stories were more similar to one another than stories written without AI.

**Bib:** Crossref matches: Science Advances 10(28), eadn5290, 2024, Doshi and Hauser. OK.

**Fix:** none.

## dugan2024raid
**Sentences:** (1) "detectors can be evaded \citep{sadasivan2025, krishna2023, dugan2024raid}"; (2) "the RAID generations without adversarial attack \citep{dugan2024raid}, written from titles of arXiv papers by six 2023 chat models."

**Verdict (1): SUPPORTED.** The abstract (last sentence) says current detectors are easily fooled by adversarial attacks, sampling variations and unseen generators.

**Verdict (2): SUPPORTED.** The evidence:
- §3.3 and Table 2 show that Abstracts-domain prompts are filled with the human paper's title.
- App. D says the abstracts are scraped from arXiv with titles and filtered to papers from 2023 or later.
- Table 3 is the "base dataset without adversarial attacks".
- App. E.2 lists six chat models: gpt-4-0613, gpt-3.5-turbo-0613, Llama-2-70b-chat, Mistral-7B-Instruct-v0.1, mpt-30b-chat, and Cohere command via co.chat(). All six are 2023 checkpoints or releases.

**Bib:** Matches the Anthology/Crossref record: ACL 2024 long papers, pp. 12463-12492, eight authors with Dugan first. OK.

**Fix:** none.

## forman2008
**Sentences:** (1) "a classify-and-count quantity \citep{forman2008}"; (2) "classify-and-count \citep{forman2008} with a calibrated threshold."

**Verdict: SUPPORTED for both, for the term only.** Forman's DMKD paper defines the quantification task and uses "classify and count" for the naive count of positive predictions. It then proposes adjusted variants and threshold-selection policies. Evidence is the abstract (third-party reproduction) and later quantification reviews that credit the term to Forman; Springer's full text is paywalled. The Bayes-FPR equivalence is the paper's own claim and is not attributed to Forman.

**Bib:** Crossref matches: DMKD 17(2):164-206, 2008, sole author George Forman. The bib's `month=June` is the online date; the print issue is Oct 2008. Harmless.

**Fix:** none.

## gao2023
**Sentence:** "Readers misjudge machine text \citep{clark2021, jakesch2023, casal2023, gao2023}."

**Verdict: SUPPORTED.** The abstract and Results (PMC10133283) describe four blinded reviewers. They caught 68% of ChatGPT abstracts, so they missed 32%, and they wrongly labelled 14% of original abstracts as generated. They also reported that the two were hard to tell apart.

**Bib:** Title, authors, npj Digital Medicine 6(1), 2023 and DOI are correct. **Minor omission:** the article number 75 is missing.

**Fix (bib):** add `pages={75}`.

## gemma3card
**Use:** a source for the table's Gemma 3 12B row: released 2025-03, cutoff Aug 2024.

**Verdict: SUPPORTED, with one caveat.** The card states the August 2024 knowledge cutoff and lists a 12B model. **The card itself gives no release date.** Google's Gemma release log (ai.google.dev/gemma/docs/releases) gives 10 March 2025 for the release of Gemma 3 in 1B, 4B, 12B and 27B, so "2025-03" is correct but is not sourced from the cited card.

**Bib:** Title, organisation and 2025 are correct. Optional: the card's own citation uses author "Gemma Team" and publisher Google DeepMind, and a technical report exists (Gemma Team 2025, arXiv 2503.19786).

**Fix:** none required. Optional: add the release-log URL to `howpublished`, or cite the Gemma 3 technical report for the date.

## gemma4card
**Use:** a source for the table's Gemma 4 12B row: released 2026-06, cutoff Jan 2025.

**Verdict: SUPPORTED, with the same caveat.** The HF card states a pre-training data cutoff of January 2025. **The card gives no release date.** Google's release log gives 3 June 2026 for the release of "Gemma 4 12B Unified", which matches 2026-06. Secondary coverage agrees.

**Bib:** Organisation and 2026 are correct. **Minor:** the card names the model "Gemma 4 12B Unified".

**Fix (optional bib):** `title = {Gemma 4 12{B} Unified Model Card}`.

## geng2024
**Sentence:** "distributional methods fit a mixture of human and LLM word distributions \citep{liang2024mapping, liang2024monitoring, liang2025widespread, geng2024}"

**Verdict: SUPPORTED, with a nuance.** §4.1, Eq. (3) of the arXiv PDF models observed word frequency as a mixture. A proportion η of abstracts uses LLM-modified frequencies and the rest uses the counterfactual human frequency, which comes from the pre-ChatGPT average (Eq. 4). η is then estimated across an adaptive word set by least squares (§4.2-4.3) and calibrated on simulated admixtures. This is a mixture of human and LLM word frequencies. Unlike Liang et al., it uses a least-squares fit on selected words rather than a likelihood over the whole vocabulary distribution. That is within the sentence's wording.

**Bib:** Authors, title and arXiv 2404.08627 (v2, 8 Nov 2024) are correct. I found no archival peer-reviewed version; there is only an ICML 2024 workshop listing. Keep arXiv. OK.

**Fix:** none.

## geng2025
**Sentences:** (1) "...in excluding content words from the features, since authors react to publicised markers \citep{geng2025}"; (2) "academic authors adapt their LLM use once overused words are publicised \citep{geng2025}"

**Verdict: SUPPORTED for both.** The ACL Anthology abstract reports a marked drop in several words flagged as overused by ChatGPT, such as "delve", beginning soon after they were pointed out in early 2024. It infers that some authors have adapted their LLM use. Other words, such as "significant", kept rising. Sentence (1) uses this only as motivation, which is fine.

**Bib:** Matches the Anthology/Crossref record: Findings of ACL 2025, pp. 12689-12696, Geng and Trotta. OK.

**Fix:** none.

## gerstgrasser2024
**Sentences:** (1) "Models trained on their own outputs degrade when synthetic data replace real data \citep{shumailov2024} but not when the two accumulate \citep{gerstgrasser2024}."; (2) "...the recursive dynamics studied in model-collapse work \citep{shumailov2024, gerstgrasser2024}"

**Verdict: SUPPORTED for both.** The abstract (arXiv 2404.01413v2) confirms that replacing real data with synthetic data tends toward collapse. Accumulating successive synthetic generations alongside the original real data avoids it, across LM pretraining, diffusion models and VAEs.

**Bib:** 14 authors, first author Gerstgrasser, which matches the OpenReview author list. The venue is COLM 2024 (papers.cool venue tag "COLM.2024" for OpenReview id 5B2K4LRgmz). OK.

**Fix:** none.

## granitecards
**Use:** a source for the table rows Granite 3.3 8B (2025-04, no cutoff) and Granite 4.2 8B (2026-08, no cutoff).

**Verdict: SUPPORTED.**
- The Granite-3.3-8B-Instruct card gives a release date of April 16th, 2025.
- The Granite-4.2-8B card gives a release date of August 25, 2026.
- Neither card states a training-data cutoff, which matches the blank cutoff cells.

**Bib:** IBM Granite Team, 2026. **Minor:** `url` points only to the 4.2 card, and `howpublished` points to the org page.

**Fix (optional bib):** list both card URLs, `https://huggingface.co/ibm-granite/granite-3.3-8b-instruct` and `https://huggingface.co/ibm-granite/granite-4.2-8b`.

---

## Summary

| Key | Verdict | Needs fix? |
|---|---|---|
| anderson2024homog | SUPPORTED | No |
| anderson2025spoken | SUPPORTED (both) | No |
| askitas2025 | SUPPORTED | Yes, bib: institution should be "Institute of Labor Economics (IZA)", Bonn |
| bao2024fastdetectgpt | SUPPORTED (both) | No |
| bentley2026 | SUPPORTED | No |
| berbersardinha2024 | SUPPORTED | No |
| brooks2024 | SUPPORTED (all 3) | No |
| casal2023 | SUPPORTED (both) | No |
| chakraborty2024 | SUPPORTED | No |
| chang2026 | SUPPORTED | No |
| clark2021 | SUPPORTED (both) | No |
| crossley2024persuade | SUPPORTED | No |
| doshi2024 | SUPPORTED | No |
| dugan2024raid | SUPPORTED (both) | No |
| forman2008 | SUPPORTED (both, for the term) | No |
| gao2023 | SUPPORTED | Minor bib: add `pages={75}` |
| gemma3card | SUPPORTED (cutoff on card; release date only in Google release log) | Optional: source the release date |
| gemma4card | SUPPORTED (cutoff on card; release date only in Google release log) | Optional: title "Gemma 4 12B Unified" |
| geng2024 | SUPPORTED (least-squares mixture of word frequencies) | No |
| geng2025 | SUPPORTED (both) | No |
| gerstgrasser2024 | SUPPORTED (both) | No |
| granitecards | SUPPORTED | Optional: add the Granite 3.3 card URL |
