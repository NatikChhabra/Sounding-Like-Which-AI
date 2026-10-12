# Citation verification, batch 4

Checked 2026-10-13 against arXiv abstract and HTML full-text pages, Crossref, OpenAlex, PMLR, the ICLR 2024 virtual site, the COLM 2024 accepted-papers list, and the GitHub and Hugging Face data releases. Line numbers refer to `paper/main.tex`.

Summary

| Key | Verdict |
|---|---|
| liang2023detectors | SUPPORTED for the citations themselves; the line 500 factual claim about the release is WRONG |
| liang2024mapping | PARTIALLY SUPPORTED (line 57 "calibrate away" is wrong for this paper); line 284 ordering is SUPPORTED |
| liang2024monitoring | SUPPORTED |
| liang2025widespread | SUPPORTED |
| lin2025 | SUPPORTED at line 57 and line 86; PARTIALLY SUPPORTED at line 98 |
| mccarthy2010 | SUPPORTED |
| mizumoto2026 | NOT SUPPORTED at line 115 |
| munozortiz2024 | SUPPORTED |
| padmakumar2024 | SUPPORTED |
| park2026 | PARTIALLY SUPPORTED at line 50; NOT SUPPORTED for "concentrated on non-native writing" at line 115 |

---

## liang2023detectors

Source: Liang, Yuksekgonul, Mao, Wu, Zou, "GPT detectors are biased against non-native English writers", *Patterns* 4(7):100779, July 2023, doi:10.1016/j.patter.2023.100779 (arXiv:2304.02819). Data: github.com/Weixin-Liang/ChatGPT-Detector-Bias; HF `WxWx/ChatGPT-Detector-Bias`.

How the paper uses it:
- L50: detectors "have flagged non-native writers' human text as AI-generated at high rates".
- L115: detectors "have produced false positives concentrated on non-native writing".
- L167: the study's population is TOEFL.
- L387: a detector bias is "reported for TOEFL essays".
- L449: the data are released under the MIT licence.
- L500: "the \citet{liang2023detectors} release lacks the 8th-grade essays".

What the source shows: seven detectors had an average false-positive rate of 61.22% on 91 TOEFL essays and "near-perfect accuracy" on 88 US 8th-grade essays (Hewlett ASAP). The TOEFL essays came from a Chinese educational forum.

Verdict:
- L50, L115, L167, L387: SUPPORTED.
- L449: SUPPORTED with a caveat. The README badge and the HF dataset card both say MIT, but the GitHub repo has no LICENSE file, and the GitHub API reports `license: null`.
- **L500: NOT ACCURATE.** The authors' GitHub release does contain the 8th-grade essays, in `Data_and_Results/Human_Data/HewlettStudentEssay_real_88/data.json`, whose `name.json` reads `"US 8th grade essay"`. The paper used the Hugging Face copy (`WxWx/ChatGPT-Detector-Bias`, per the project README). That copy's `all_data.json` holds 749 texts and has no 8th-grade set: its human sets are only Real TOEFL, Real College Essays and Real CS224N. So the statement is true of the HF copy, not of "the release".

Bibliographic data: correct (title, five authors, Patterns 4(7) 100779, 2023, DOI).

Required rewording, L500:
> ...the Hugging Face copy of the \citet{liang2023detectors} data lacks the US 8th-grade essays (they are distributed only in the authors' GitHub repository), so it is used only as an out-of-genre check...

Also note that the 8th-grade essays are in fact obtainable. The deviation's rationale therefore weakens, and the authors may want to either use them or explain why not.

## liang2024mapping

Source: Liang, Zhang, Wu, Lepp, Ji, Zhao, Cao, Liu, He, Huang, Yang, Potts, Manning, Zou, "Mapping the Increasing Use of LLMs in Scientific Papers", arXiv:2404.01268 (v1 only, 1 Apr 2024).

How the paper uses it:
- L46: a corpus study finding traces of LLM-assisted writing in scientific abstracts.
- L57: the small pre-ChatGPT "LLM share" is one that "several studies calibrate away as estimator error".
- L85: a distributional method that fits a mixture of human and LLM word distributions.
- L284: "the same high-CS, low-mathematics ordering that prevalence studies report".

Check:
- L46, L85: SUPPORTED. The paper uses a population-level distributional framework on abstracts and introductions.
- L284: SUPPORTED. In Feb 2024, CS abstracts were at 17.5%, the highest, and Mathematics at 4.9%, the lowest. The abstract describes CS as having the "largest and fastest growth". Fields covered: CS, EESS, Math, Physics, Statistics, bioRxiv, Nature.
- L57: PARTIALLY SUPPORTED / overstated. The paper reports non-zero pre-ChatGPT estimates for Nov 2022 (CS 2.3%, EESS 2.9%, Math 2.4%, Nature 3.1%). It treats them as a "pre-ChatGPT reference point" and says they "are consistent with the false positive rate reported in" §4.2. Its validation on Jan–Nov 2022 papers reports estimation error under 3.5%. However, it does **not** subtract, calibrate or adjust for this value: every month is estimated independently and reported as an absolute level. "Interpret as false positives" is accurate; "calibrate away" is not.

Bibliographic data: title, authors and year are correct.
- Peer-reviewed version: **COLM 2024** (First Conference on Language Modeling). The title is on colmweb.org/2024/AcceptedPapers.html. OpenReview id YX7QnhxESU comes from an aggregator; OpenReview itself was behind a bot challenge, so that id is not verified on OpenReview.
- An extended journal version exists, with different numbers (larger corpus to Sept 2024): Liang et al., "Quantifying large language model usage in scientific papers", *Nature Human Behaviour* 9(12):2599–2609, 2025, doi:10.1038/s41562-025-02273-8 (verified on Crossref).
- Recommend citing the COLM 2024 version: `@inproceedings{..., booktitle={First Conference on Language Modeling (COLM)}, year={2024}}`.

Required rewording, L55–57. Wording that is accurate for this key and for lin2025; brooks2024 was not checked in this batch:
> ...the small ``LLM share'' that prevalence estimators report for text written before ChatGPT, which studies treat as false positives \citep{liang2024mapping} or subtract as baseline classification error \citep{lin2025}.

Add brooks2024 back only if its own check confirms it does one of these.

## liang2024monitoring

Source: Liang, Izzo, Zhang, Lepp, Cao, Zhao, Chen, Ye, Liu, Huang, McFarland, Zou, "Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews", arXiv:2403.07183.

How the paper uses it:
- L46: traces of LLM writing in peer reviews.
- L85: a distributional mixture method.

Verdict: SUPPORTED. The paper uses a maximum-likelihood mixture over expert-written and AI-generated reference texts, and estimates "between 6.5% and 16.9%" of peer-review text at ICLR 2024, NeurIPS 2023, CoRL 2023 and EMNLP 2023.

Bibliographic data: correct.
- Published version: **ICML 2024**, *Proceedings of the 41st International Conference on Machine Learning*, PMLR 235:29575–29620, https://proceedings.mlr.press/v235/liang24b.html (verified on the PMLR page). Recommend `@inproceedings` with that venue.

## liang2025widespread

Source: Liang, Zhang, Codreanu, Wang, Cao, Zou, "The Widespread Adoption of Large Language Model-Assisted Writing Across Society", arXiv:2502.09747.

How the paper uses it:
- L46: traces of LLM writing in press releases.
- L85: a distributional mixture method.

Verdict: SUPPORTED. The paper applies the population-level framework to consumer complaints, corporate press releases, job postings and UN press releases, estimating up to 24% of corporate press releases.

Bibliographic data: correct.
- Published version: *Patterns* 6(12):101366, 2025, doi:10.1016/j.patter.2025.101366 (Crossref: same six authors, title in sentence case). Recommend citing the journal version.

## lin2025

Source: Cong William Lin, Wu Zhu, "Divergent LLM Adoption and Heterogeneous Convergence Paths in Research Writing", arXiv:2504.13629 (v1, 18 Apr 2025). No peer-reviewed version found (arXiv, RePEc).

How the paper uses it:
- L57: the pre-ChatGPT share is "calibrated away as estimator error".
- L86: a classifier-based study that labels documents.
- L98: humans adopt LLM vocabulary in academic writing.

Check:
- L57: SUPPORTED. Section 3.2 attributes the stable pre-release level "primarily ... to misclassification by the model". The authors "adjusted the raw values by subtracting the average adoption rate observed before November 2022", so the metric averages zero before ChatGPT. This is baseline subtraction, which "calibrate away" fairly describes.
- L86: SUPPORTED. The study uses fine-tuned classifiers (all-mpnet-base-v2) on more than 627k arXiv abstracts.
- L98: PARTIALLY SUPPORTED. The paper measures *adoption of LLM revision* by classifier and finds the style of adopters' writing converges. It does not show that humans adopt LLM vocabulary in their own unassisted writing; the convergence it measures is in classifier-flagged, LLM-revised text.

Bibliographic data: correct (title, authors, 2025, eprint).

Suggested rewording, L97–98:
> Humans adopt LLM vocabulary in speech \citep{yakura2024, anderson2025spoken} and academic writing \citep{geng2025}, and adoption of LLM revision in research writing varies across disciplines and author groups \citep{lin2025}.

This assumes geng2025 supports the vocabulary claim; that key is checked in another batch.

## mccarthy2010

Source: McCarthy & Jarvis, "MTLD, vocd-D, and HD-D: A validation study of sophisticated approaches to lexical diversity assessment", *Behavior Research Methods* 42(2):381–392, 2010, doi:10.3758/BRM.42.2.381.

How the paper uses it: L200 cites it for MTLD lexical diversity.

Verdict: SUPPORTED. This is the standard reference for MTLD and its validation.

Bibliographic data: correct (verified on Crossref).

## mizumoto2026

Source: Atsushi Mizumoto, "Corpus-informed AI-likeness screening for L2 writing: A proof-of-concept field test and two flagged cases", *Applied Corpus Linguistics* 6(3):100223, Dec 2026, published online 14 June 2026, doi:10.1016/j.acorp.2026.100223. The abstract was read via OpenAlex; ScienceDirect returned 403.

How the paper uses it: L115, detectors "have produced false positives concentrated on non-native writing \citep{liang2023detectors, park2026, mizumoto2026}".

Verdict: **NOT SUPPORTED.** The study field-tests a corpus-informed screening prototype on 142 L2 students' essays. Two essays were flagged, and follow-up interviews showed that both students *had* used ChatGPT, prompting it to insert deliberate errors. The flags were therefore true positives, not false positives. The study states it "does not estimate sensitivity, specificity, or false negative rates". It mentions "fairness risks in multilingual settings" only as background.

Bibliographic data: correct.

Required change: remove mizumoto2026 from L115. To keep it, cite it for what it does, for example:
> ...and interpretable, corpus-informed screening has been proposed for L2 writing as an alternative to black-box detectors \citep{mizumoto2026}.

## munozortiz2024

Source: Muñoz-Ortiz, Gómez-Rodríguez, Vilares, "Contrasting Linguistic Patterns in Human and LLM-Generated News Text", *Artificial Intelligence Review* 57(10), article 265, 2024, doi:10.1007/s10462-024-10903-2.

How the paper uses it: L103, "LLM text differs systematically from human text in lexico-grammatical features".

Verdict: SUPPORTED. The paper compares human news text with output from six LLMs on morphological, syntactic, psychometric and sociolinguistic features. It finds human text has more varied sentence lengths and a different mix of dependency types, and that LLM output contains more auxiliaries, numbers and pronouns.

Bibliographic data: correct. The entry lacks an article number; add `pages={265}` (Crossref article-number 265).

## padmakumar2024

Source: Vishakh Padmakumar, He He, "Does Writing with Language Models Reduce Content Diversity?", arXiv:2309.05196.

How the paper uses it: L94, "Writing with instruction-tuned models reduces content diversity".

Verdict: SUPPORTED. Co-writing with InstructGPT reduced diversity; co-writing with base GPT-3 did not. The wording "instruction-tuned" correctly captures that distinction.

Bibliographic data: title and authors are correct. The bib year is 2023, the arXiv v1 year, while the key says 2024.
- Published version: **ICLR 2024**, poster at https://iclr.cc/virtual/2024/poster/19056 (verified). Recommend `@inproceedings{padmakumar2024, ..., booktitle={The Twelfth International Conference on Learning Representations (ICLR)}, year={2024}}`.

## park2026

Source: Hyeonchu Park, Gahye Jeong, Bugeun Kim, "Style as a Confound: False Positives in AI Detection of Non-Native Academic Writing", arXiv:2608.26710 (v1, 27 Aug 2026; the arXiv comment reads "Presented in EMNLP 2026").

How the paper uses it:
- L50: detectors "have flagged non-native writers' human text as AI-generated at high rates".
- L115: false positives are "concentrated on non-native writing".

What the source shows: the study has 135,389 pairs of non-native manuscripts and their native-edited versions from an editing service. It contains **no native-authored originals**. On pre-ChatGPT originals, false-positive rates across 13 detectors range from 0.0% to 100% (for example Binoculars 0.0%, Fast-DetectGPT 25.2%, RADAR 88.3%, RoBERTa 93.1%). Native editing raised the rate for some detectors and lowered it for others. The conclusion is that professional editing style is "a key confounding variable" in detector outputs.

Verdict:
- L50: PARTIALLY SUPPORTED. High rates hold for some detectors only. Suggest "...and some detectors have flagged...".
- L115: NOT SUPPORTED for "concentrated on non-native writing". The study makes no comparison with native writers, and its message is that style, not nativeness, drives the scores.

Bibliographic data: correct as an arXiv entry. EMNLP 2026 is not yet in the ACL Anthology (the events/emnlp-2026 page returns 404), so the venue is unverified. Keep the arXiv citation, and update to the Anthology entry once it appears.

Required rewording, L114–115, combined with the mizumoto2026 fix:
> ...face limits that grow as distributions converge \citep{chakraborty2024}, and have produced false positives concentrated on non-native writing \citep{liang2023detectors}; on non-native academic manuscripts, false-positive rates range from 0\% to 100\% across detectors and shift with professional editing \citep{park2026}.
