# Citation verification, batch 2

Keys: crossley2024persuade, doshi2024, dugan2024raid, forman2008, gao2023, geng2024, geng2025, gerstgrasser2024, gray2024, hans2024binoculars

Sources were checked on 2026-10-13: arXiv abstract and HTML pages, ACL Anthology, PMLR, Crossref API, PMC, the PERSUADE GitHub and Zenodo pages, and the Gray PDF (full text). Line numbers refer to paper/main.tex.

---

## crossley2024persuade

**Citing sentence (l.164-166):** "PERSUADE 2.0 \citep{crossley2024persuade}: N argumentative essays by US students in grades 6--12 on K prompts, written before 2020, with English-language-learner (ELL) status and a holistic quality score for each essay."

**Source:**
- Crossref, Zenodo 8221504 and the GitHub repo scrosseye/persuade_corpus_2.0 all describe it as "over 25,000 argumentative essays" by US students in grades 6-12, written for 15 prompts.
- Holistic essay scores are included in 2.0 (GitHub README).
- ELL status is among the demographic variables. The PERSUADE 1.0 paper (PMC9767095) reports English Language Learner status for n = 24,787. The project's own loader (code/build_sources.py) reads the `ell_status` and `holistic_essay_score` columns.
- **"Written before 2020" could not be verified.** Neither the 1.0 paper (PMC full text), the 2.0 Zenodo/GitHub pages nor any other source found gives a collection period. What is verifiable: the corpus was the basis of the Kaggle Feedback Prize "hosted by Kaggle in the winter of 2021-2022" (PERSUADE 1.0 GitHub), so the essays predate ChatGPT. The `2019-01-01` date in build_sources.py is an assumption made in the code, not something the source states.

**Verdict:** PARTIALLY SUPPORTED. Everything except "written before 2020" is supported.

**Bibliography:**
- Crossref matches the bib entry: title, journal (Assessing Writing), vol. 61, article 100865, 2024, DOI 10.1016/j.asw.2024.100865.
- The author order in the bib (Crossley, Tian, Baffour, Franklin, Benner, Boser) matches Crossref and Semantic Scholar. The GitHub README lists Baffour before Tian, but the publisher's order should take precedence. OK.

**Proposed wording:** replace "written before 2020," with "written before ChatGPT (the corpus was released for a Kaggle competition in 2021)," or give a collection period only if it can be found in the full text of the 2.0 article.

---

## doshi2024

**Citing sentence (l.94-95):** "Writing with instruction-tuned models reduces content diversity \citep{padmakumar2024, doshi2024, anderson2024homog}".

**Source:** an online experiment in which some writers received story ideas from an LLM. The stories written with AI ideas are "more similar to each other than stories by humans alone" (Crossref abstract). The paper calls this a loss of collective novelty.

**Verdict:** SUPPORTED. Doshi and Hauser's setting is writers who received LLM story ideas, not writers co-writing with the model. The sentence is still a fair summary of the group of three citations.

**Bibliography:**
- Crossref confirms the bib: title, authors (Anil R. Doshi, Oliver P. Hauser), Science Advances 10(28), 2024 (12 July), DOI 10.1126/sciadv.adn5290.
- Optional: add the article number eadn5290.

**Wording change:** none required.

---

## dugan2024raid

**Citing sentences:**
1. l.49 and l.113: "detectors can be evaded \citep{sadasivan2023, krishna2023, dugan2024raid}".
2. l.179-181: "we add the RAID generations without adversarial attacks \citep{dugan2024raid} from six chat models (GPT-4, ChatGPT, and chat versions of Cohere, Llama, Mistral and MPT) and, for one analysis only, five base models."

**Source:** The abstract says "current detectors are easily fooled by adversarial attacks". RAID covers 11 models.
- Chat models: ChatGPT, GPT-4, Cohere chat, Mistral 7B chat, MPT 30B chat and LLaMA 2 70B. RAID's LLaMA 2 70B is the chat model; its Table 5 labels it "llama-c".
- Base models: GPT-2 XL, GPT-3, Cohere, Mistral 7B and MPT 30B, which gives five.
- RAID includes a non-attacked split.

**Verdict:** SUPPORTED, for both uses.

**Bibliography:**
- The bib is an arXiv @misc. The work is peer-reviewed: Proceedings of the 62nd Annual Meeting of the ACL (Volume 1: Long Papers), ACL 2024, Bangkok, pp. 12463-12492. DOI 10.18653/v1/2024.acl-long.674. Anthology URL https://aclanthology.org/2024.acl-long.674/.
- The author order differs. The Anthology has "... Filip Trhlík, Andrew Zhu, Josh Magnus Ludan, Hainiu Xu ...", while arXiv and the bib have "... Trhlik, Josh Magnus Ludan, Andrew Zhu ...". When switching to the ACL version, use the Anthology order and the accent in "Trhl{\'i}k".

**Wording change:** none required. Update the bib to the ACL 2024 version.

---

## forman2008

**Citing sentences:**
- l.62: "a classify-and-count quantity \citep{forman2008}".
- l.130: "classify-and-count \citep{forman2008} with a calibrated threshold."

**Source:** The paper is Forman's DMKD article on quantification, which is estimating class counts or prevalence in a test set. It names the naive "classify and count" (CC) method and proposes adjusted versions of it. Secondary sources confirm this, among them the Wikipedia article on quantification, which cites this paper. The full text is paywalled and I could not read it directly.

**Verdict:** SUPPORTED. The paper is cited for the term "classify and count", which is correct. Forman shows that CC is biased when class priors shift. The paper does not claim otherwise; it treats MSO as a definition, not an unbiased estimator.

**Bibliography:**
- Crossref confirms the bib: "Quantifying counts and costs via classification", George Forman, Data Mining and Knowledge Discovery 17(2):164-206, 2008, DOI 10.1007/s10618-008-0097-y.
- Optional: the term first appeared in Forman (2005, ECML), but citing the 2008 journal paper is standard.

**Wording change:** none.

---

## gao2023

**Citing sentence (l.111):** "linguists and scientific reviewers misclassify abstracts \citep{casal2023, gao2023}."

**Source:** The abstract (Crossref) says blinded human reviewers "correctly identified 68% of generated abstracts ... but incorrectly identified 14% of original abstracts as being generated." The abstracts are medical research abstracts.

**Verdict:** SUPPORTED.

**Bibliography:**
- Crossref confirms the bib: title, all seven authors, npj Digital Medicine 6(1), 2023 (26 April), DOI 10.1038/s41746-023-00819-6.
- Add the article number 75 (`pages={75}`), which is currently missing.

**Wording change:** none required. Optionally write "medical researchers" for precision.

---

## geng2024

**Citing sentence (l.84-85):** "distributional methods fit a mixture of human and LLM word distributions \citep{liang2024mapping, liang2024monitoring, liang2025widespread, geng2024}".

**Source:** The paper models observed word frequency as a share eta of LLM-affected abstracts. Its Eq. 3 gives the observed frequency as the baseline frequency plus eta times the baseline times the LLM change rate, and eta is estimated by OLS on GPT-3.5-revised abstracts (arXiv HTML v2). In effect this is a two-component mixture of word frequencies.

**Verdict:** SUPPORTED. It is a word-frequency mixture estimated by regression rather than by MLE like Liang et al., but it is fairly grouped with them.

**Bibliography:**
- Title, authors (Mingmeng Geng, Roberto Trotta) and arXiv ID 2404.08627 are correct.
- v1 is dated 12 Apr 2024 and v2 8 Nov 2024. No journal-ref is given.
- It was only an ICML 2024 workshop poster (Next Generation of AI Safety), not archival proceedings. Keeping the arXiv entry is correct.

**Wording change:** none.

---

## geng2025

**Citing sentences:**
1. l.90-91: "authors react to publicised markers \citep{geng2025}, so lexical markers are a moving target."
2. l.97-98: "Humans adopt LLM vocabulary in speech \citep{yakura2024, anderson2025spoken} and academic writing \citep{geng2025, lin2025}."
3. l.320-321: "consistent with authors avoiding publicised markers \citep{geng2025}."

**Source:** The abstract reports "a marked drop in the frequency of several words previously identified as overused" (e.g. *delve*) after publicity in early 2024, while words like *significant* keep rising. The paper explains this as authors adapting their LLM use, e.g. "by selecting outputs or applying modifications to the LLM outputs". It does not claim that authors pick up LLM vocabulary independently of using LLMs.

**Verdict:**
- (1) SUPPORTED.
- (3) SUPPORTED.
- (2) PARTIALLY SUPPORTED. Geng and Trotta show authors adapting how they use LLMs, not humans adopting LLM vocabulary in their own writing. Placed next to the speech studies, the sentence implies human uptake of LLM vocabulary, which this paper does not claim.

**Bibliography:**
- The bib is an arXiv @misc (2502.09606). The work is peer-reviewed: Findings of the Association for Computational Linguistics: ACL 2025 (Vienna), pp. 12689-12696. DOI 10.18653/v1/2025.findings-acl.657. URL https://aclanthology.org/2025.findings-acl.657/.
- Title and authors match.

**Proposed wording (l.97-98):** "Humans adopt LLM vocabulary in speech \citep{yakura2024, anderson2025spoken} and academic writing \citep{lin2025}, and academic authors adapt their LLM use once overused words are publicised \citep{geng2025}." The lin2025 support is not verified in this batch.

---

## gerstgrasser2024

**Citing sentence (l.416-417):** "Model collapse under recursive training is documented in controlled settings \citep{shumailov2024}, but accumulating real data limits it \citep{gerstgrasser2024}."

**Source:** The paper finds that "accumulating the successive generations of synthetic data alongside the original real data avoids model collapse". Replacing real data leads to collapse. For linear models, the test error under accumulation has a finite upper bound.

**Verdict:** PARTIALLY SUPPORTED (wording only). The mechanism is keeping the original real data while synthetic data accumulate, not "accumulating real data". "Limits" is also weaker than the paper's "avoids".

**Bibliography:**
- Title and the arXiv ID 2404.01413 (v2, 29 Apr 2024) match the 14 authors in the bib.
- Peer-reviewed version: Conference on Language Modeling (COLM) 2024. OpenReview id 5B2K4LRgmz, according to the NSF PAR record 10616583 and the OpenReview COLM.2024 listing on papers.cool. The official OpenReview page was behind a bot check and I could not open it; confirm at https://openreview.net/forum?id=5B2K4LRgmz.
- The COLM author order differs: Rafailov, Korbak, Sleight, Agrawal, Hughes, Pai ...
- There was also an ICML 2024 DMLR workshop poster.

**Proposed wording:** "...but is avoided when synthetic data accumulate alongside the original real data instead of replacing it \citep{gerstgrasser2024}."

---

## gray2024

**Citing sentence (l.218-221):** marker words *delve, underscore, showcase, meticulous, intricate, intricacies, commendable, boast*, cited to \citealp{kobak2025, gray2024, yakura2024}.

**Source (full PDF checked):** Gray's indicator terms include "commendable", "meticulous" and "intricate". The full text never mentions *delve*, *underscore*, *showcase*, *intricacies* or *boast*.

**Verdict:** SUPPORTED as part of the joint citation. Gray supplies three of the eight words; the others must come from kobak2025 or yakura2024, which were not checked here.

**Bibliography:**
- Title, sole author Andrew Gray, arXiv 2403.16887 and 2024 (v1, 25 Mar 2024) are correct.
- No peer-reviewed version was found. arXiv lists no journal-ref.

**Wording change:** none, provided kobak2025 and yakura2024 cover the other five words.

---

## hans2024binoculars

**Citing sentence (l.112):** "Zero-shot detectors use perplexity-based statistics \citep{hans2024binoculars, bao2024fastdetectgpt}".

**Source:** Binoculars scores text by "the ratio of perplexity to cross-perplexity" (arXiv HTML v3, Eq. 4) and "operates entirely in a zero-shot setting".

**Verdict:** SUPPORTED.

**Bibliography:**
- Title, the 8 authors and 2024 match.
- The bib is an arXiv @misc. The peer-reviewed version is Proceedings of the 41st International Conference on Machine Learning (ICML 2024), PMLR 235:17519-17537. URL https://proceedings.mlr.press/v235/hans24a.html. There is no DOI.

**Wording change:** none. Update the bib to the ICML 2024 version.
