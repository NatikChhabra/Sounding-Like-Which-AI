# Citation verification: batch 1

Checked on 2026-10-13 against the arXiv abstract pages, ACL Anthology, PMLR, ICLR proceedings, AAAI OJS, Crossref metadata, and author/institutional repositories. Elsevier (ScienceDirect), ACM DL and Springer landing pages returned 403 or login redirects. For those, Crossref gave the bibliographic data and the abstract came from an institutional repository (Casal), a FAPESP mirror (Berber Sardinha), arXiv (Anderson 2024), or a search-index copy of the Springer abstract plus the author's GitHub README (Chang).

Summary:

| key | verdict | bib fix needed |
|---|---|---|
| anderson2024homog | PARTIALLY SUPPORTED | none (optional: fuller booktitle) |
| anderson2025spoken | PARTIALLY SUPPORTED | yes: published at AIES 2025 |
| bao2024fastdetectgpt | PARTIALLY SUPPORTED | yes: ICLR 2024, year 2024 |
| bentley2026 | SUPPORTED | none (arXiv only) |
| berbersardinha2024 | SUPPORTED | none |
| brooks2024 | SUPPORTED | yes: WikiNLP 2024 (ACL Anthology) |
| casal2023 | SUPPORTED | none |
| chakraborty2024 | PARTIALLY SUPPORTED | yes: ICML 2024 (PMLR 235), title has "Position:" prefix |
| chang2026 | SUPPORTED | none |
| clark2021 | SUPPORTED | yes: ACL-IJCNLP 2021 |

---

## anderson2024homog

**Citing sentence (main.tex l.94-95):** "Writing with instruction-tuned models reduces content diversity \citep{padmakumar2024, doshi2024, anderson2024homog}"

**Source:** Anderson, Shah, Kreminski, "Homogenization Effects of Large Language Models on Human Creative Ideation", C&C '24 (ACM), pp. 413-425, DOI 10.1145/3635636.3656204 (Crossref). arXiv 2402.01536 says "Accepted to C&C 2024".

**What it shows:** a 36-participant study of creative *ideation* (generating ideas, not writing prose). Participants using ChatGPT produced ideas that were less semantically distinct across users than those using an alternative creativity support tool. Evidence: "different users tended to produce less semantically distinct ideas with ChatGPT".

**Verdict: PARTIALLY SUPPORTED.** The homogenization finding is correct. But the task is ideation, not writing, and the effect is between users, not within a single text.

**Bib:** Title, authors, year, DOI and pages match Crossref. Optional: set booktitle to "Proceedings of the 16th Conference on Creativity & Cognition".

**Proposed wording:** "Writing or ideating with instruction-tuned models reduces content diversity across users \citep{padmakumar2024, doshi2024, anderson2024homog}"

---

## anderson2025spoken

**Citing sentences:**
- l.47: "LLM-favoured words have entered unscripted speech \citep{yakura2024, anderson2025spoken}"
- l.97: "Humans adopt LLM vocabulary in speech \citep{yakura2024, anderson2025spoken}"

**Source:** Anderson, Galpin, Juzek, "Model Misalignment and Language Change: Traces of AI-Associated Language in Unscripted Spoken English", arXiv 2508.00238. The paper builds a 22.1M-word corpus of conversational science and technology podcasts. Evidence: "a moderate yet significant increase in the usage of these words post-2022". Synonym baselines did not shift. The authors explicitly leave open whether the change is natural language change or driven by AI.

**Verdict: PARTIALLY SUPPORTED.**
- "Entered" overstates the finding: these are ordinary English words, and the paper shows only that they became more frequent.
- "Humans adopt" asserts a causal adoption that this paper leaves open. yakura2024 may support adoption more directly (not checked in this batch).
- The domain is science and technology podcasts, not speech in general.

**Bib:** Authors, title and year are correct. The work has a peer-reviewed version: *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society* (AIES 2025), Vol. 8 No. 1, pp. 179-191, DOI 10.1609/aies.v8i1.36540 (verified on ojs.aaai.org/index.php/AIES/article/view/36540). Change the entry to @inproceedings with this venue and DOI.

**Proposed wording:**
- l.47: "LLM-associated words have become more frequent in unscripted speech \citep{yakura2024, anderson2025spoken}"
- l.97: "LLM-associated vocabulary has grown in human speech \citep{yakura2024, anderson2025spoken}" (keep "Humans adopt" only if yakura2024 shows adoption directly).

---

## bao2024fastdetectgpt

**Citing sentence (l.112):** "Zero-shot detectors use perplexity-based statistics \citep{hans2024binoculars, bao2024fastdetectgpt}"

**Source:** Bao, Zhao, Teng, Yang, Zhang, "Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature". The detection statistic is "conditional probability curvature": a normalized gap between the passage's token log-likelihood and that of sampled alternative tokens. It is likelihood-based, but it is not perplexity. Binoculars (the co-citation) does use perplexity/cross-perplexity.

**Verdict: PARTIALLY SUPPORTED.** "Perplexity-based" fits Binoculars but not Fast-DetectGPT.

**Bib:** The title and authors are correct. The year in the bib is 2023 (arXiv v1), but the key says 2024. Published version: ICLR 2024 (International Conference on Learning Representations), https://proceedings.iclr.cc/paper_files/paper/2024/hash/6b8c6f846c3575e1d1ad496abea28826-Abstract-Conference.html (verified). Change to @inproceedings, booktitle ICLR, year 2024.

**Proposed wording:** "Zero-shot detectors use token-likelihood statistics such as perplexity ratios and probability curvature \citep{hans2024binoculars, bao2024fastdetectgpt}"

---

## bentley2026

**Citing sentence (l.87-88):** "\citet{bentley2026} track an LLM-associated style index for arXiv abstracts built from a few markers"

**Source:** Bentley, Vidiella, Ruck, Dutta, Li, Valverde, "Human--LLM Collaboration Is Transforming Complexity Metrics in Scientific Texts", arXiv 2606.27052 (v1, 25 Jun 2026; no journal-ref). The abstract describes a "composite LLM-associated style index" over arXiv abstracts. The full text defines it as LLM_index = z_dash + z_significant + z_crucial + z_showcase. These are four standardized monthly rates: dashes, plus the words "significant", "crucial" and "showcase". It is computed on v1 abstracts from 2014 onward.

**Verdict: SUPPORTED.** "Built from a few markers" is accurate (four components).

**Bib:** Title, authors, year and eprint all match. No peer-reviewed version found.

---

## berbersardinha2024

**Citing sentence (l.102-103):** "LLM text differs systematically from human text in lexico-grammatical features \citep{reinhart2025, munozortiz2024, berbersardinha2024, herbold2023}"

**Source:** Berber Sardinha, "AI-generated vs human-authored texts: A multidimensional comparison", *Applied Corpus Linguistics* 4(1), 100083, 2024, DOI 10.1016/j.acorp.2023.100083 (Crossref). The paper compares GPT texts with human written and spoken texts on Biber's (1988) five dimensions, which are lexico-grammatical. It finds significant differences, and a discriminant analysis separates the two groups. Evidence (abstract via FAPESP mirror): "AI-generated texts generally failed to exhibit resemblance to their human counterparts".

**Verdict: SUPPORTED.**

**Bib:** Correct.

---

## brooks2024

**Citing sentences:**
- l.44-47: corpus studies find traces of LLM-assisted writing in "...encyclopedia articles \citep{..., brooks2024}"
- l.55-57: the small pre-ChatGPT "LLM share... which several studies calibrate away as estimator error \citep{liang2024mapping, lin2025, brooks2024}"
- l.85-86: "classifier- and detector-based studies label documents \citep{lin2025, brooks2024, sun2025, khan2025}"

**Source:** Brooks, Eggert, Peskoff, "The Rise of AI-Generated Content in Wikipedia". The authors use GPTZero and Binoculars and calibrate thresholds to a 1% false-positive rate on pre-GPT-3.5 articles. They find over 5% of new English Wikipedia articles flagged. Evidence: the paper reports thresholds "calibrated to achieve a 1% false positive rate on pre-GPT-3.5 articles".

**Verdict: SUPPORTED** for all three uses.
- Wikipedia counts as encyclopedia articles.
- Detector-based labelling is what the paper does.
- Treating pre-release flags as false positives is calibrating that share away as estimator error.
- Minor: the paper's cutoff is the GPT-3.5 release, not ChatGPT itself. This is close enough for "pre-ChatGPT"; no change needed.

**Bib:** Title, authors and year are correct. Published version: *Proceedings of the First Workshop on Advancing Natural Language Processing for Wikipedia* (WikiNLP 2024, co-located with EMNLP 2024), pp. 67-79, ACL. Anthology https://aclanthology.org/2024.wikinlp-1.12/, DOI 10.18653/v1/2024.wikinlp-1.12 (verified). Change to @inproceedings.

---

## casal2023

**Citing sentences:**
- l.48: "readers are poor at telling human from machine text \citep{clark2021, jakesch2023, casal2023}"
- l.111: "linguists and scientific reviewers misclassify abstracts \citep{casal2023, gao2023}"

**Source:** Casal and Kessler, "Can linguists distinguish between ChatGPT/AI and human writing?: A study of research ethics and academic publishing", *Research Methods in Applied Linguistics* 2(3), 100068, 2023, DOI 10.1016/j.rmal.2023.100068 (Crossref; University of Memphis repository). In the study, 72 reviewers for applied-linguistics journals judged AI- and human-written research abstracts. Evidence: "overall positive identification rate of only 38.9%".

**Verdict: SUPPORTED.** At l.111, Casal covers "linguists" and gao2023 covers "scientific reviewers"; the pairing is fine.

**Bib:** Correct. One secondary source gives the issue as 2(2), but Crossref and the institutional repository both give 2(3), which matches the bib.

---

## chakraborty2024

**Citing sentence (l.112-114):** zero-shot detectors "face limits that grow as distributions converge \citep{chakraborty2024}"

**Source:** Chakraborty, Bedi, Zhu, An, Manocha, Huang, "On the Possibilities of AI-Generated Text Detection" (arXiv 2304.04736). The paper's thesis is *optimistic*: detection is possible unless the human and machine distributions are identical over their whole support. It derives sample-complexity bounds showing that more samples or longer sequences are needed as machine text approaches human text. Evidence (PMLR abstract): detection "becomes harder as it nears human quality".

**Verdict: PARTIALLY SUPPORTED.** "Limits that grow" could be read as "detection becomes impossible", which the paper argues against (it was written as a rebuttal to impossibility claims). The accurate statement is about rising sample requirements.

**Bib:** Authors are correct. The year in the bib is 2023 (arXiv), but the key says 2024. Published version: "Position: On the Possibilities of AI-Generated Text Detection", *Proceedings of the 41st International Conference on Machine Learning* (ICML 2024), PMLR 235:6093-6115, https://proceedings.mlr.press/v235/chakraborty24a.html (verified). Change to @inproceedings with the "Position:" title, ICML 2024, PMLR 235, pp. 6093-6115.

**Proposed wording:** "...can be evaded \citep{...}, need more text to succeed as machine and human distributions converge \citep{chakraborty2024}, and have produced false positives..."

---

## chang2026

**Citing sentence (l.88-89):** "\citet{chang2026} analyse a decade of convergence between human writing and machine patterns"

**Source:** Eunsuk Chang, "Human writing and machine patterns: analyzing a decade of convergence", *Scientometrics* 131(3), 1635-1654, 2026, DOI 10.1007/s11192-026-05589-y (Crossref). Springer's page redirected to login, so I could not read it there. A search-index copy of the abstract and the author's GitHub README (eunsuk-c/perplexity) give the content: about 111K documents from PubMed, Wikipedia and Stack Exchange, sampled from 2014 to 2024. The paper measures perplexity and Binoculars scores under OPT-125M, GPT-2 and Llama-3.2, plus sentence length and type-token ratio. Human writing becomes more predictable to these models over time.

**Verdict: SUPPORTED.** The sentence restates the title.

Optional, for a sharper contrast with your work: "\citet{chang2026} show that PubMed, Wikipedia and Stack Exchange text became more predictable to small language models over 2014--2024". The search-index abstract also says the trend predates widespread generative AI. I could not confirm that point on the official page, so check it in the full text before you rely on it.

**Bib:** Correct per Crossref.

---

## clark2021

**Citing sentences:**
- l.48: "readers are poor at telling human from machine text \citep{clark2021, ...}"
- l.110: "Untrained readers judge GPT-3 text at chance \citep{clark2021}"

**Source:** Clark, August, Serrano, Haduong, Gururangan, Smith, "All That's 'Human' Is Not Gold: Evaluating Human Evaluation of Generated Text". Untrained evaluators distinguished GPT-3 from human text at chance level across stories, news and recipes. Training raised accuracy only to about 55%.

**Verdict: SUPPORTED.**

**Bib:** Title, authors and year are correct. Published version: *Proceedings of the 59th Annual Meeting of the ACL and the 11th IJCNLP (Volume 1: Long Papers)*, ACL-IJCNLP 2021, pp. 7282-7296, Anthology https://aclanthology.org/2021.acl-long.565/, DOI 10.18653/v1/2021.acl-long.565 (verified). Change to @inproceedings.
