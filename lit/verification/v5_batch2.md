# Citation verification v5, batch 2

Checked 2026-10-13. Sources: arXiv abstract, HTML and PDF pages; PMLR; ACL Anthology; ICLR proceedings (including its BibTeX); PMC; Crossref and OpenAlex metadata; Zenodo API; GitHub API; Hugging Face API; ScienceDirect and nature.com, read in a browser.

Three sources could not be opened directly. science.org (Cloudflare) and openreview.net (bot check) showed bot checks, which were not bypassed. pnas.org returned 403. For these, the arXiv author version (Kusumegi), the COLM accepted-papers list (Liang mapping) and PMC/Crossref (Jakesch) were used instead.

The batch input truncated some sentences, so they were checked against the full text in `paper/main.tex` (l.242, l.522-526, l.580-583).

---

## hans2024binoculars

**Sentence:** "Zero-shot detectors use token-likelihood statistics \citep{hans2024binoculars, bao2024fastdetectgpt}, ..."

**Verdict: SUPPORTED.** Binoculars is zero-shot, needing no training data (abstract). Its score is the ratio of log-perplexity under one model, which is the mean negative log-likelihood of the observed tokens, to the cross-perplexity between two models' next-token distributions (arXiv 2401.12070, §3.1 Eq. 2-3 and §3.3 Eq. 4). That is a token-likelihood statistic.

**Bib:** Correct: ICML 2024, PMLR 235:17519-17537, first author Hans, 8 authors (checked on the PMLR page).

**Fix:** none.

## herbold2023

**Sentence:** "LLM text differs systematically from human text in lexico-grammatical features \citep{reinhart2025, munozortiz2024, berbersardinha2024, herbold2023} ..."

**Verdict: SUPPORTED.** The abstract (penultimate sentence) says ChatGPT essays show linguistic characteristics that differ from human essays. Results/Table 3 (PMC10616290) give the detail. ChatGPT uses more nominalizations and more clauses per sentence, and fewer modals and epistemic markers. ChatGPT-4 also uses fewer discourse markers. MTLD differs from humans in both directions: it is lower for ChatGPT-3 and higher for ChatGPT-4.

**Bib:** Title, authors (first author Herbold), Sci. Rep. 13(1), 2023 are correct. The article number is missing; add `pages={18617}` (Crossref).

**Fix:** bib only (optional).

## holzwarth2026

**Sentence:** "Excess-vocabulary methods compare word frequencies with a counterfactual extrapolated from pre-LLM years \citep{kobak2025, holzwarth2026, lee2026}; ..."

**Verdict: SUPPORTED.** The expected human frequency comes from extrapolating a linear regression fitted to 2018-2022 (arXiv HTML, Results; Methods "Standard errors"). The paper describes the expected frequency as obtained "by extrapolating the regression line".

**Bib:** Title, three authors (first author Holzwarth), 2026 and eprint 2608.10715 match arXiv (v1 11 Aug 2026). There is no journal-ref, so it is a preprint only, and no published version was found.

**Fix:** none.

## jakesch2023

**Sentences:**
1. "readers are poor at telling human from machine text \citep{clark2021, jakesch2023, casal2023}"
2. "Readers misjudge machine text \citep{clark2021, jakesch2023, casal2023, gao2023}."

**Verdict: SUPPORTED (both).** In six experiments (N = 4,600), participants could not detect AI-generated self-presentations (abstract, 4th sentence; PMC10089155). Accuracy was about 50-52%. The judgments rest on flawed heuristics (abstract, 5th sentence). Note: the texts are short self-presentations (profiles), which is fine for these general claims.

**Bib:** Correct: PNAS 120(11), 2023, first author Jakesch. Optionally add `pages={e2208839120}`.

**Fix:** none (optional article number).

## jiang2023mistral

**Sentence (Table 1 caption, l.242):** "Other dates: \citet{jiang2023mistral, llama31card, ...}". The row this supports is "Mistral 7B Instruct v0.3 & 2024-05" (l.223).

**Verdict: PARTLY.** The Mistral 7B paper (arXiv 2310.06825, v1 10 Oct 2023) describes Mistral 7B and its Instruct model. It cannot source the release month of **v0.3**, which came seven months after the paper. The month itself is correct: the Hugging Face repo `mistralai/Mistral-7B-Instruct-v0.3` was created 2024-05-22 (HF API `createdAt`). The model card states no release date and no data cutoff, and the table correctly gives no cutoff.

**Bib:** Title, 18 authors (first author A. Q. Jiang) and 2023 are correct. It is arXiv only; no peer-reviewed version exists.

**Proposed fix:** Keep jiang2023mistral for the model and add a source for the v0.3 date, e.g. a new entry `@misc{mistral7bv03card, title={Mistral-7B-Instruct-v0.3}, author={{Mistral AI}}, year={2024}, howpublished={\url{https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3}}}`. Then change the caption to "Other dates: \citet{jiang2023mistral, mistral7bv03card, llama31card, ...}". If the date stays unsourced, the paper is no worse than now, but the citation does not cover it.

## jiang2024

**Sentence:** "... although detectors trained on a large writing assessment showed no such bias \citep{jiang2024} ..."

**Verdict: SUPPORTED.** On the ScienceDirect abstract and highlights, the detectors were built on GRE writing-assessment data from e-rater linguistic features and perplexity features. They reached near-perfect accuracy. In the authors' words they showed "no evidence of bias disadvantaging non-native English speakers" (abstract, 5th sentence; highlight 3).

**Bib:** Correct: Computers & Education 217, 105070, Aug 2024, first author Yang Jiang, 4 authors (Crossref).

**Fix:** none.

## juzek2025

**Sentence:** "... preference tuning reduces output diversity \citep{kirk2024, wu2025monoculture} and plausibly produces LLM-overused words \citep{juzek2025}."

**Verdict: SUPPORTED.** The Anthology abstract finds no evidence that architecture, algorithms or training data cause the overuse. Model testing is consistent with RLHF playing a role, but the evidence is inconclusive. "Plausibly" matches this hedge.

**Bib:** Correct: COLING 2025, pp. 6397-6411, first author Juzek, https://aclanthology.org/2025.coling-main.426/. The input file's link was "?"; the Anthology URL above is the right one.

**Fix:** none.

## katz2023scidata

**Sentence:** "\emph{Parliamentary speech:} Australian House of Representatives Hansard \citep{katz2023scidata, katz2025hansard}, up to 150 spoken speeches per month, January 2015 to July 2025 ..."

**Verdict: SUPPORTED.** Per the Introduction and Methods (nature.com), the database has one file per House of Representatives sitting day, 2 March 1998 to 8 September 2022. The paper also documents how interjections and Question Time are parsed, which supports filtering to spoken speeches. The 150-per-month sample and the 2015 start are the paper's own design.

**Bib:** Correct: Scientific Data 10, 567 (2023), Katz & Alexander (Crossref).

**Fix:** none.

## katz2025hansard

**Sentence:** same as katz2023scidata.

**Verdict: SUPPORTED.** The Zenodo record 17351233 (published 2025-10-14, CC BY 4.0) describes House of Representatives proceedings from 2 March 1998 to **31 July 2025**, parsed from the parliament's XML. This matches "to July 2025". The release notes mention corrected interjection and question flags.

**Bib:** Correct (title, Katz & Alexander, 2025, DOI).

**Fix:** none.

## khan2026

**Sentence:** "... classifier- and detector-based studies label documents \citep{lin2025, brooks2024, sun2025, khan2026}."

**Verdict: SUPPORTED (with a caveat).** The J. Informetrics abstract (via OpenAlex) describes over 230,000 Scopus CS articles from 2021-2025, each scored with the Binoculars zero-shot detector. The abstract reports results both on the score and on "its binary classification". Caveat: the authors stress that the score measures stylistic AI-likeness, not confirmed AI use (abstract, 4th sentence). Grouping it under prevalence studies is therefore acceptable but slightly generous. No change is needed because the sentence claims only that it labels documents.

**Bib:** Correct per Crossref: J. Informetrics 20(4), 101869, Dec 2026, first author **Farhan Kamrul** Khan. OpenAlex lists "Fahad Khan", which is an OpenAlex error; the bib follows Crossref. This replaces the earlier arXiv entry (khan2025); no `khan2025` is left in main.tex or references.bib.

**Fix:** none.

## kirk2024

**Sentence:** "... preference tuning reduces output diversity \citep{kirk2024, wu2025monoculture} ..."

**Verdict: SUPPORTED.** The abstract (ICLR proceedings page) reports that RLHF "significantly reduces output diversity compared to SFT".

**Bib:** Matches the official ICLR 2024 BibTeX: authors, editors, pp. 20620-20653, year 2024, URL.

**Fix:** none.

## kobak2025

**Sentences:**
1. "Corpus studies find traces of LLM-assisted writing in abstracts, ... \citep{kobak2025, ...}"
2. "Excess-vocabulary methods compare word frequencies with a counterfactual extrapolated from pre-LLM years \citep{kobak2025, ...}"

**Verdict: SUPPORTED (both).**
1. The abstract covers more than 15M PubMed abstracts and puts at least 13.5% of 2024 abstracts as LLM-processed.
2. The counterfactual is a linear extrapolation of the 2021 and 2022 frequencies (arXiv 2406.07016, §2.1 and §4.3).

**Bib:** Correct: Sci. Adv. 11(27), 2025, first author Kobak, 4 authors. Optionally add the article number `pages={eadt3813}` (Crossref).

**Fix:** none (optional article number).

## krishna2023

**Sentence:** "detectors can be evaded \citep{sadasivan2025, krishna2023, dugan2024raid}"

**Verdict: SUPPORTED.** DIPPER paraphrases evade watermarking, GPTZero, DetectGPT and OpenAI's classifier. For example, DetectGPT falls from 70.3% to 4.6% at 1% FPR (arXiv 2303.13408 abstract).

**Bib:** Correct: NeurIPS 36 (2023), pp. 27469-27500, DOI 10.52202/075280-1195, first author Krishna (Crossref).

**Fix:** none.

## kusumegi2025

**Sentence:** "LLM adoption also changes how much scientists write \citep{kusumegi2025}."

**Verdict: SUPPORTED.** The source is the author version, arXiv 2601.13187, whose journal-ref is Science 390(6779):1240-1243. Scientists who use LLMs to draft manuscripts produce substantially more papers, 23.7-89.3% more depending on field and author background (abstract, 2nd-3rd sentences). The sentence is accurate, though "how much" reads as volume of text while the paper measures number of papers. Optional precision: "...changes how many papers scientists produce \citep{kusumegi2025}."

**Bib:** Correct: Science 390(6779), 1240-1243, 18 Dec 2025, first author Kusumegi, 6 authors (Crossref).

**Fix:** optional wording only.

## lee2026

**Sentence:** "Excess-vocabulary methods compare word frequencies with a counterfactual extrapolated from pre-LLM years \citep{kobak2025, holzwarth2026, lee2026}"

**Verdict: SUPPORTED.** The abstract defines excess vocabulary as frequency above the pre-2023 trend. In the Methods (PDF), a least-squares line is fitted through the 2018-2022 base years and extrapolated to the target year.

**Bib:** Title, single author Aron Lee, 2026 and eprint 2609.07447 match (v1 7 Sep 2026). The arXiv comment calls it a working paper; it is not peer reviewed.

**Fix:** none. It is the third of three citations, so it is not load-bearing.

## li2024mage

**Sentence:** "Detectors transfer unevenly to unseen generators \citep{pu2023zeroshot, li2024mage}, ..."

**Verdict: SUPPORTED.** The abstract says detectors struggle on out-of-distribution data. The "Unseen Models" testbed (arXiv 2305.13242, §5.1, Table 3) shows uneven transfer:
- Longformer stays high: AvgRec 86.6%, AUROC 0.95.
- FastText degrades: AvgRec 78.8% to 68.6%.
- GLTR and DetectGPT are weak throughout.

**Bib:** Correct: ACL 2024 (Long), pp. 36-53, DOI 10.18653/v1/2024.acl-long.3, first author Yafu Li, 9 authors (Crossref). The input file's link was "?"; use https://aclanthology.org/2024.acl-long.3/. The arXiv preprint had an earlier title ("Deepfake Text Detection in the Wild"), but the bib correctly uses the published one.

**Fix:** none.

## liang2023detectors

**Sentences:**
1. "some detectors have flagged non-native writers' human text as AI-generated at high rates \citep{liang2023detectors}"
2. "Zero-shot detectors use token-likelihood statistics ..., need more text ..., and have flagged non-native writing \citep{liang2023detectors}, although ..."
3. (l.522-524) "A GPT-2 perplexity instrument flags X% of TOEFL essays but Y% of US 8th-grade essays, reproducing the bias reported by \citet{liang2023detectors}, ..."
4. (l.580-583) "RAID and the Hugging Face release of \citet{liang2023detectors}, MIT; their US 8th-grade essays come from the authors' GitHub repository, which states no licence, and derive from the Hewlett Foundation ASAP data, ..."

**Evidence:** arXiv 2304.02819v3 Results, and the Patterns article. Seven off-the-shelf detectors had an average false-positive rate of 61.22% on 91 TOEFL essays and near-perfect accuracy on 88 US 8th-grade essays. The detectors were Originality.AI, Quill.org, Sapling, OpenAI, Crossplag, GPTZero and ZeroGPT. The 8th-grade essays are "sourced from the Hewlett Foundation's ASAP dataset" (Results, first subsection). The paper says it focuses on perplexity-based and supervised methods, and that most assessed detectors use GPT-2 as their backbone.

**Verdicts:**
1. SUPPORTED.
2. **PARTLY.** The sentence's grammatical subject makes this a claim about *zero-shot* detectors. Liang et al. tested commercial off-the-shelf detectors of mixed or undisclosed type (perplexity-based and supervised), not specifically zero-shot detectors. They do tie the bias to low perplexity.
3. SUPPORTED for the attributed part: Liang reports high FPR on TOEFL and near-zero on 8th-grade essays. The paper's own X and Y values were not checked, since they are the paper's own results.
4. **PARTLY.**
   - The HF dataset `WxWx/ChatGPT-Detector-Bias` has `license: mit` in its card. Its `all_data.json` holds 749 texts and contains no 8th-grade set. Both are correct.
   - The GitHub repo has the 8th-grade set at `Data_and_Results/Human_Data/HewlettStudentEssay_real_88`. Correct.
   - The Hewlett ASAP origin is correct.
   - "which states no licence" is inaccurate. The repo has no LICENSE file (GitHub API `license: null`), but its README shows an "MIT license" badge.

**Bib:** Correct: Patterns 4(7), 100779, July 2023, first author W. Liang, 5 authors (Crossref).

**Proposed fixes:**
- Sentence 2: "Zero-shot detectors use token-likelihood statistics \citep{hans2024binoculars, bao2024fastdetectgpt} and need more text as machine and human distributions converge \citep{chakraborty2024}; off-the-shelf detectors have flagged non-native writing \citep{liang2023detectors}, although ..."
- Sentence 4: "... their US 8th-grade essays come from the authors' GitHub repository, which has no licence file (its README shows an MIT badge), and derive from the Hewlett Foundation ASAP data, ..."

## liang2024mapping

**Sentences:**
1. "Corpus studies find traces of LLM-assisted writing in abstracts, ... \citep{..., liang2024mapping, ...}"
2. "Prevalence estimators report a small ``LLM share'' for text written before ChatGPT, which studies treat as consistent with false positives \citep{liang2024mapping}, ..."
3. "distributional methods fit a mixture of human and LLM word distributions \citep{liang2024mapping, ...}"
4. "This is the high-CS, low-mathematics ordering that prevalence studies report \citep{liang2024mapping}."

**Verdict: SUPPORTED (all four).** Evidence is from arXiv 2404.01268v1.
1. The paper estimates LLM modification in abstracts and introductions.
2. §5.1 gives Nov 2022 estimates of 2.3-3.1% and calls them "consistent with the false positive rate reported in" the validation section. The earlier "calibrate away" overstatement is now fixed.
3. The framework is a mixture (1-α)P + αQ with α estimated by maximum likelihood.
4. In Feb 2024, CS abstracts were the highest at 17.5% and Mathematics the lowest at 4.9%.

**Bib:** Correct: COLM 2024, 14 authors, first author W. Liang. The COLM accepted-papers page links the title to OpenReview id YX7QnhxESU, which matches the bib URL. OpenReview itself was behind a bot check and was not opened. A later journal version exists with different numbers (Nature Human Behaviour 9:2599-2609, 2025). Keep COLM because the numbers cited match the COLM version.

**Fix:** none.

## liang2024monitoring

**Sentences:**
1. "traces of LLM-assisted writing in ... peer reviews"
2. "distributional methods fit a mixture of human and LLM word distributions"

**Verdict: SUPPORTED (both).** The source (PMLR abstract; arXiv 2403.07183 §3.1, §3.3) estimates 6.5-16.9% of review text at ICLR 2024, NeurIPS 2023, CoRL 2023 and EMNLP 2023 as substantially LLM-modified. Documents are assumed to come from a mixture (1-α)P + αQ, with α estimated by MLE. The vocabulary is adjectives, i.e. word distributions.

**Bib:** Correct: ICML 2024, PMLR 235:29575-29620, first author W. Liang.

**Fix:** none.

## liang2025widespread

**Sentences:**
1. "traces of LLM-assisted writing in ... press releases"
2. "distributional methods fit a mixture ..."

**Verdict: SUPPORTED (both).**
1. The abstract (arXiv 2502.09747) covers consumer complaints, corporate press releases (up to 24%), job postings and UN press releases (about 14%).
2. It applies the authors' earlier population-level framework (Introduction; Supplementary "Data Split, Model Fitting, and Evaluation"), which is the same mixture estimator as liang2024monitoring. The paper itself only references that method; it does not restate the mixture.

**Bib:** Correct: Patterns 6(12), 101366, Dec 2025, first author W. Liang, 6 authors (Crossref).

**Fix:** none.

## lin2025

**Sentences:**
1. "... subtract as baseline misclassification \citep{lin2025}"
2. "classifier- and detector-based studies label documents \citep{lin2025, ...}"
3. "... adoption of LLM revision varies across disciplines and author groups \citep{lin2025}."

**Verdict: SUPPORTED (all three).** Evidence is from arXiv 2504.13629 (HTML).
1. §3.2 attributes the stable pre-release level to misclassification and subtracts the pre-Nov-2022 average adoption rate.
2. §2.1 describes fine-tuned all-mpnet-base-v2 classifiers that score each article's abstract.
3. The abstract reports disparities in adoption across disciplines, gender, native-language status and career stage.

**Bib:** Correct: Lin & Zhu, 2025, arXiv 2504.13629. Only v1 exists, with no journal-ref, and no published version was found (search, RePEc).

**Fix:** none.

## llama31card

**Sentence (Table 1 caption):** "Other dates: \citet{..., llama31card, ...}". The row it supports is "Llama 3.1 8B & 2024-07 & Dec 2023".

**Verdict: SUPPORTED.** The model card gives "Model Release Date: July 23, 2024" and a pretraining data cutoff of December 2023 (Data Freshness section).

**Bib:** Acceptable (`{Meta}`, 2024, GitHub URL).

**Fix:** none.

## mccarthy2010

**Sentence:** "... mean word length and MTLD lexical diversity \citep{mccarthy2010}, computed with spaCy~3.8 ..."

**Verdict: SUPPORTED.** This is the standard validation reference for MTLD, which it validates alongside vocd-D and HD-D.

**Bib:** Correct: Behavior Research Methods 42(2):381-392, 2010, McCarthy & Jarvis (Crossref). The input file shows the title truncated as "{MTLD", but this is an extraction artifact; the .bib title is complete.

**Fix:** none.

---

## Summary table

| Key | Verdict | Needs fix? |
|---|---|---|
| hans2024binoculars | SUPPORTED | No |
| herbold2023 | SUPPORTED | Optional bib: add `pages={18617}` |
| holzwarth2026 | SUPPORTED | No (arXiv preprint) |
| jakesch2023 | SUPPORTED (both) | Optional bib: add `pages={e2208839120}` |
| jiang2023mistral | PARTLY: does not source the v0.3 release month (2024-05; HF repo created 2024-05-22) | Yes: add a v0.3 model-card citation to the caption |
| jiang2024 | SUPPORTED | No |
| juzek2025 | SUPPORTED | No |
| katz2023scidata | SUPPORTED | No |
| katz2025hansard | SUPPORTED | No |
| khan2026 | SUPPORTED (it measures AI-likeness, not confirmed use) | No (no stale `khan2025` left in main.tex or the .bib) |
| kirk2024 | SUPPORTED | No |
| kobak2025 | SUPPORTED (both) | Optional bib: add `pages={eadt3813}` |
| krishna2023 | SUPPORTED | No |
| kusumegi2025 | SUPPORTED | Optional wording: "how many papers scientists produce" |
| lee2026 | SUPPORTED | No (working paper) |
| li2024mage | SUPPORTED | No |
| liang2023detectors | S1 SUPPORTED; S2 PARTLY (not specifically zero-shot detectors); S3 SUPPORTED; S4 PARTLY (GitHub README shows an MIT badge, so "states no licence" is inaccurate) | Yes: reword S2 and S4 |
| liang2024mapping | SUPPORTED (all four) | No |
| liang2024monitoring | SUPPORTED (both) | No |
| liang2025widespread | SUPPORTED (both) | No |
| lin2025 | SUPPORTED (all three) | No |
| llama31card | SUPPORTED | No |
| mccarthy2010 | SUPPORTED | No |
