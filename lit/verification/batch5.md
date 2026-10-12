# Citation verification, batch 5

Checked on 2026-10-13 against arXiv abstract pages and PDFs, Crossref, the ACL Anthology, NeurIPS/ICLR proceedings, the TMLR paper listing (jmlr.org/tmlr/papers) and PMC. Line numbers refer to `paper/main.tex`.

| Key | Verdict | Bib action |
|---|---|---|
| pillutla2021 | SUPPORTED | Upgrade to NeurIPS 2021 |
| rallapalli2026 | PARTIALLY SUPPORTED | None |
| reinhart2025 | SUPPORTED | None |
| sadasivan2023 | SUPPORTED | Upgrade to TMLR 2025 (published title is longer) |
| shaib2024 | SUPPORTED | Upgrade to EMNLP 2024 |
| shumailov2024 | SUPPORTED | None |
| sourati2025 | SUPPORTED | Upgrade to Nature Human Behaviour 2026 |
| sun2025 | SUPPORTED | Upgrade to ACL 2025 (bib year currently 2024) |
| wu2025monoculture | SUPPORTED | Upgrade to ICLR 2025 (bib year currently 2024) |
| yakura2024 | SUPPORTED, but only by v4 (2026) | Pin the version or year; see below |
| yang2026coverage | SUPPORTED | None (arXiv only) |

---

## pillutla2021

**Where it is cited:** l.105. "Distribution-level comparisons such as MAUVE \citep{pillutla2021} and coverage frameworks \citep{yang2026coverage} evaluate models against human text."

**Source:** arXiv:2102.01454 (v3, 23 Nov 2021). MAUVE compares the distribution of a text-generation model's output with the distribution of human-written text using divergence frontiers.

**Verdict: SUPPORTED.** The source describes MAUVE as a measure of "the gap between neural text and human text" (from the title).

**Bibliographic data:** Title and all 7 authors match. Year 2021 is correct. The bib currently has `@misc` (arXiv), but a peer-reviewed version exists. Verified on proceedings.neurips.cc:
- Advances in Neural Information Processing Systems 34 (NeurIPS 2021, oral), pp. 4816--4828.
- https://proceedings.neurips.cc/paper/2021/hash/260c2432a0eecc28ce03c10dadc078a4-Abstract.html

**Wording:** No change needed.

---

## rallapalli2026

**Where it is cited:** l.104. "...but genre explains more stylistic variance than source \citep{rallapalli2026}, so any overlap measure must be genre-specific."

**Source:** arXiv:2604.14111 (v1, 15 Apr 2026). The paper compares Biber features of human text and of text from 11 LLMs across 8 genres and 4 decoding strategies. Its second finding is that genre exerts "a stronger influence on stylistic features than the source itself."

**Verdict: PARTIALLY SUPPORTED.** The direction of the claim is right, but the paper does not decompose variance or report variance explained. The evidence is PCA and hierarchical clustering, where texts "of the same genre tend to cluster together irrespective of the source." "Explains more stylistic variance" therefore states a quantitative result the paper does not report.

**Bibliographic data:** Title, all 7 authors and the year match. There is no journal reference, so it is arXiv-only.

**Proposed wording (l.104):**
> but genre shapes stylistic features more strongly than source does \citep{rallapalli2026}, so any overlap measure must be genre-specific.

---

## reinhart2025

**Where it is cited:** l.102. "LLM text differs systematically from human text in lexico-grammatical features \citep{reinhart2025, munozortiz2024, berbersardinha2024, herbold2023}."

**Source:** PNAS 122(8), e2422455122, published 18 Feb 2025 (verified via Crossref and the arXiv:2410.16107 journal-ref). The authors built parallel human and LLM corpora (Llama 3 and GPT-4o variants) and applied Biber's lexical, grammatical and rhetorical features. They found systematic differences between LLMs and humans that are larger in instruction-tuned models.

**Verdict: SUPPORTED.** The abstract reports "systematic differences between LLMs and humans."

**Bibliographic data:** Title, all 7 authors, journal, volume 122, issue 8, year 2025 and DOI 10.1073/pnas.2422455122 all match Crossref. No change needed.

**Wording:** No change needed.

---

## sadasivan2023

**Where it is cited:**
- l.49: "...detectors can be evaded \citep{sadasivan2023, krishna2023, dugan2024raid}..."
- l.113: "Zero-shot detectors ... can be evaded \citep{sadasivan2023, krishna2023, dugan2024raid}..."

**Source:** arXiv:2303.11156 (v4, 17 Jan 2025). A recursive paraphrasing attack against watermarking, neural, zero-shot and retrieval-based detectors "can significantly reduce detection rates."

**Verdict: SUPPORTED** at both sites. The source covers zero-shot detectors explicitly, so the l.113 context also fits.

**Bibliographic data:** The authors (5) match. A peer-reviewed version exists, verified on the official TMLR paper listing (jmlr.org/tmlr/papers):
- Published title: "Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks". This is longer than the bib title.
- Transactions on Machine Learning Research, January 2025.
- OpenReview: https://openreview.net/forum?id=OOgsAZdFOt. I could not open the forum page itself because of a bot check; the ID comes from the TMLR listing.

If the bib cites TMLR, use the full published title and year 2025. The key name can stay.

**Wording:** No change needed.

---

## shaib2024

**Where it is cited:** l.103. "...and in recurring part-of-speech templates \citep{shaib2024}."

**Source:** The paper defines syntactic templates "(e.g., strings comprising parts-of-speech)". Models produce templated text in downstream tasks at a higher rate than human reference texts, and 76% of the templates in model text are found in pre-training data, against 35% for human text.

**Verdict: SUPPORTED.**

**Bibliographic data:** Title, the 4 authors and the year match. The bib has `@misc` arXiv:2407.00211, but a peer-reviewed version exists. Verified on the ACL Anthology:
- Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP 2024), Miami, pp. 6416--6431.
- DOI 10.18653/v1/2024.emnlp-main.368
- https://aclanthology.org/2024.emnlp-main.368/

**Wording:** No change needed.

---

## shumailov2024

**Where it is cited:** l.417. "Model collapse under recursive training is documented in controlled settings \citep{shumailov2024}, but accumulating real data limits it \citep{gerstgrasser2024}."

**Source:** Nature 631(8022):755--759, published 24 Jul 2024 (Crossref; full text on PMC11269175). Collapse is shown in controlled experiments with OPT-125m fine-tuned on wikitext2 over generations, and with VAEs and GMMs. The paper describes collapse as "irreversible defects" in which the tails of the distribution disappear.

**Verdict: SUPPORTED.** "Controlled settings" is accurate. The paper itself also notes that keeping 10% of the original data reduces the degradation, which is consistent with the second half of the sentence.

**Bibliographic data:** All fields (title, 6 authors, Nature, 631, 8022, 755--759, 2024, DOI 10.1038/s41586-024-07566-y) match Crossref. No change needed.

**Wording:** No change needed.

---

## sourati2025

**Where it is cited:** l.95. "LLM rewriting compresses stylistic variance \citep{sourati2025}."

**Source:** arXiv:2502.11266 (v2, 24 Aug 2026). The study uses 7 datasets and more than 880k texts. When LLMs polish or rewrite text, they keep the content but "homogenize writing styles," which reduces writing-complexity variance by 21--50% (p ≤ .05).

**Verdict: SUPPORTED.**

**Bibliographic data:** The 10 authors match. A peer-reviewed version exists, verified via Crossref for the DOI and the arXiv journal-ref. nature.com itself redirected to a login page.
- Title: "The shrinking landscape of linguistic diversity in the age of large language models", in sentence case.
- Journal: Nature Human Behaviour, published online 24 Aug 2026. Crossref shows no volume or issue yet.
- DOI: 10.1038/s41562-026-02550-0

Update the bib to `@article` with year 2026 and this DOI. The key can stay.

**Wording:** No change needed.

---

## sun2025

**Where it is cited:** l.86. "...classifier- and detector-based studies label documents \citep{lin2025, brooks2024, sun2025, khan2025}. All target the share of text produced with LLM help."

**Source:** The authors collected about 2.4M posts from Medium, Quora and Reddit, selected the best detector (OSM-Det) on their AIGTBench benchmark, and applied it to the posts. They report an "AI Attribution Rate" for each platform from Jan 2022 to Oct 2024; for example, Medium rose from 1.77% to 37.03%.

**Verdict: SUPPORTED.** This is a detector-based prevalence study.

**Bibliographic data:** Title and the 8 authors match. The bib year is 2024 (arXiv v1, Dec 2024), while the key says 2025. A peer-reviewed version exists, verified on the ACL Anthology:
- Proceedings of the 63rd Annual Meeting of the ACL (Volume 1: Long Papers), ACL 2025, Vienna, July 2025, pp. 22975--23005.
- DOI 10.18653/v1/2025.acl-long.1120
- https://aclanthology.org/2025.acl-long.1120/

Update the bib to `@inproceedings` with year 2025.

**Wording:** No change needed.

---

## wu2025monoculture

**Where it is cited:** l.95--96. "...preference tuning reduces output diversity \citep{kirk2024, wu2025monoculture} and plausibly produces LLM-overused words \citep{juzek2025}."

**Source:** The paper defines "generative monoculture," a narrowing of output diversity relative to the training data, and demonstrates it in book reviews and code. The abstract attributes the root causes to alignment ("likely embedded within the LLM's alignment processes"). The body supports the RLHF link directly, stating "Takeaway 3: RLHF Hurts Diversity the Most" from a comparison of Llama-2-chat with its base and SFT counterparts.

**Verdict: SUPPORTED.** The causal claim is hedged in the source ("likely"; "we conjecture"), but the empirical result that RLHF-tuned models are less diverse is reported. The sentence is acceptable because kirk2024 shares the load.

**Bibliographic data:** Title and the 3 authors match. The bib year is 2024 (arXiv v1, Jul 2024), while the key says 2025. A peer-reviewed version exists, verified on iclr.cc and proceedings.iclr.cc:
- ICLR 2025 (poster).
- https://proceedings.iclr.cc/paper_files/paper/2025/hash/5178b2f2d7c44aa390c0777dc77b3f0c-Abstract-Conference.html
- https://iclr.cc/virtual/2025/poster/27717

Update the bib to `@inproceedings`, ICLR 2025, year 2025.

**Wording:** No change needed. For a stricter version: "preference tuning is associated with reduced output diversity".

---

## yakura2024

**Where it is cited:**
- l.47: "...LLM-favoured words have entered unscripted speech \citep{yakura2024, anderson2025spoken}."
- l.97: "Humans adopt LLM vocabulary in speech \citep{yakura2024, anderson2025spoken}..."
- l.219--221: marker list "(delve, underscore, showcase, meticulous, intricate, intricacies, commendable, boast; \citealp{kobak2025, gray2024, yakura2024})."

**Source (current version, arXiv:2409.01754v4, 16 Jul 2026):**
- The authors analysed 737,083 hours from 824,634 podcast episodes, screened for spontaneous speech, and replicated the result on 360,445 academic YouTube talks.
- A preregistered experiment (N = 496) found that participants adopted the chatbot's words.
- The abstract names "delve, showcase, boast, intricacies and meticulous". "Underscore" also appears in the appendix ranking.

**Marker check:**
- **"boast": CONFIRMED in v4.** It appears in the abstract and in the results ("boast, meticulous, and showcase maintain a sustained uptake").
- **"intricacies": CONFIRMED in v4.** It appears in the abstract and in the Results.

**Version caveat:** v1 (3 Sep 2024) differs substantially.
- It had 6 authors.
- Its data was about 280k academic YouTube transcripts, not unscripted podcasts.
- Its highlighted words are delve, realm, meticulous and adept.
- **"boast" and "intricacies" do not appear anywhere in the v1 text** (checked by full-text search of the v1 PDF).

The bib author list already matches v4, which has 10 authors, but the year is 2024. A reader who resolves "Yakura et al. 2024" to v1 will find neither marker word and no podcast or unscripted-speech analysis.

**Verdict: SUPPORTED** at all three sites, but only by v4. The citation must point to v4.

**Bibliographic data:**
- v4 title: "Empirical Evidence of Large Language Model's Influence on Human Spoken Communication". The capitalisation differs from the bib; the words are the same.
- No peer-reviewed version was found; the arXiv journal-ref is blank.
- Required fix: set year = {2026} (or note "arXiv:2409.01754v4, version of 16 Jul 2026") so the cited content is the one checked. The key can stay `yakura2024`.

**Wording:** No change needed in main.tex once the bib entry is pinned to v4.

---

## yang2026coverage

**Where it is cited:** l.105--106. "...and coverage frameworks \citep{yang2026coverage} evaluate models against human text..."

**Source:** arXiv:2608.05576 (v1, 6 Aug 2026). The paper proposes a human-grounded coverage framework with two metrics, LLM-Cov and In-Boundary Rate. These use the empirical distribution of human writing on a topic to measure how broadly LLM outputs cover it. It finds LLM output to be plausible but narrow.

**Verdict: SUPPORTED.**

**Bibliographic data:** Title, the 3 authors (Zini Yang, Emily Wenger, Richard So) and the year 2026 match. No journal-ref, so it is arXiv-only. No change needed.

**Wording:** No change needed.
