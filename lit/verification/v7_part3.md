# Citation verification v7, part 3 (18 keys)

Independent check made on 2026-10-13 against paper/main.tex and paper/references.bib. I formed each verdict from primary sources (arXiv abs/HTML, ACL Anthology, PMLR, NeurIPS/ICLR proceedings, Crossref, IZA/RePEc, Hugging Face, ai.google.dev). Only afterwards did I compare against the earlier lit/verification reports, and I found no disagreements.

Summary: 18 keys checked. All citing sentences are SUPPORTED. No entry has a metadata error that changes what the reader sees. Three entries have optional cosmetic fixes: kirk2024, gemmareleases and forman2008.

---

## askitas2025
**Bib:** OK. Title, author (Nikos Askitas), IZA Discussion Paper No. 18062, 2025, Bonn and URL all match docs.iza.org and IDEAS/RePEc (dated August 2025; a CESifo WP 12069 version also exists).
**Citing sentence (l.82):** "\citet{askitas2025} finds an abrupt stylometric shift in economics working-paper abstracts in 2023 with an event-study design and a classifier."
**Verdict:** SUPPORTED. The paper finds a stylistic break in IZA DP (economics working-paper) abstracts after the March 2023 ChatGPT-3.5 release. Event-study regressions show it is "abrupt, persistent" (RePEc abstract), and an ML classifier flags a growing share of post-March-2023 texts.

## brooks2024
**Bib:** OK. Title, authors (Brooks, Eggert, Peskoff), WikiNLP 2024 workshop proceedings, pp. 67-79 and DOI 10.18653/v1/2024.wikinlp-1.12 all match Crossref and the ACL Anthology.
**Citing sentences:**
- l.47-49: traces of LLM-assisted writing in "...encyclopedias". SUPPORTED: AI-generated content is flagged in over 5% of new English Wikipedia articles.
- l.56: pre-ChatGPT "LLM share" is used "to calibrate thresholds". SUPPORTED: "thresholds calibrated to achieve a 1% false positive rate on pre-GPT-3.5 articles".
- l.81: "classifier- and detector-based studies label documents". SUPPORTED: the study uses the GPTZero and Binoculars detectors.

## clark2021
**Bib:** OK. Title, six authors in order, ACL-IJCNLP 2021 Vol. 1, pp. 7282-7296 and DOI all match Crossref and the Anthology.
**Citing sentence (l.101):** "Readers misjudge machine text".
**Verdict:** SUPPORTED. Untrained evaluators "distinguished between GPT3- and human-authored text at random chance level."

## forman2008
**Bib:** OK. Title, author, *Data Mining and Knowledge Discovery* 17(2):164-206, 2008 and DOI 10.1007/s10618-008-0097-y match Crossref. Minor: `month=jun` is the online date (2008-06-10); the print issue is October 2008. This is harmless.
**Citing sentences:**
- l.64: MSO is "a classify-and-count quantity \citep{forman2008}".
- l.122-123: MSO "is the flag rate of the Bayes-optimal classifier, that is, classify-and-count with a calibrated threshold".
**Verdict:** SUPPORTED. Forman names "classify and count" (CC) as the naive quantifier: train a classifier, apply it to the test set and count the items predicted positive. The paper's use (the flag rate at a fixed, calibrated threshold) matches this definition. Springer's full text is paywalled (the redirect needs login), so I took the definition from the Crossref abstract plus quantification surveys that quote Forman (Wikipedia "Quantification (machine learning)"; arXiv 1602.08780). Forman also shows that CC is biased as a prevalence estimator. The paper does not use MSO as a prevalence estimate, so there is no conflict.
**Optional fix:** none needed.

## gemmareleases
**Bib:** EXISTS. The page is "Gemma releases | Google AI for Developers" (ai.google.dev/gemma/docs/releases). The page names no author; the bib uses `{Google DeepMind}`, which is acceptable for a corporate misc entry.
**Citing sentence:** Table 1 caption, "Other dates: ... gemmareleases".
**Release-month checks:**
- Gemma 3 12B, 2025-03: SUPPORTED. The page lists "March 10, 2025: Gemma 3 in 1B, 4B, 12B, and 27B sizes".
- Gemma 4 12B, 2026-06: SUPPORTED. The page lists "June 3, 2026: Gemma 4 12B Unified", the only 12B Gemma 4 entry. The first Gemma 4 release on 31 March 2026 had no 12B.
**Optional fix:** `author = {{Google}}` matches the page owner more literally. Not required.

## granitecards
**Bib:** EXISTS. Both HF cards exist under ibm-granite: granite-3.3-8b-instruct and granite-4.2-8b. Both list the developer as "Granite Team, IBM" and the licence as Apache 2.0.
**Citing sentence:** Table 1 caption, "Other dates".
**Checks:**
- Granite 3.3 8B, 2025-04: SUPPORTED ("Release Date: April 16th, 2025").
- Granite 4.2 8B, 2026-08: SUPPORTED (Release Date "August 25, 2026"; 8B per the Model Summary).
- Cutoff column is blank for both: correct, because neither card states a training-data cutoff.

## holzwarth2026
**Bib:** OK. Title, authors in order (Holzwarth, González-Márquez, Kobak), arXiv 2608.10715 (v1 11 Aug 2026) and year 2026 all match.
**Citing sentence (l.78-79):** "Excess-vocabulary methods compare word frequencies with a counterfactual extrapolated from pre-LLM years \citep{kobak2025, holzwarth2026, lee2026}".
**Verdict:** SUPPORTED. The expected frequency is a linear extrapolation: "We fit a linear regression to the five-year period (2018–2022)."

## juzek2025
**Bib:** OK. Title, authors (Juzek, Ward), COLING 2025, editors, Abu Dhabi, January 2025 and pp. 6397-6411 all match the ACL Anthology.
**Citing sentence (l.88-89):** "Preference tuning ... plausibly produces LLM-overused words \citep{juzek2025}".
**Verdict:** SUPPORTED. The hedge fits the source: "While the model testing is consistent with RLHF playing a role". The source rules out architecture, algorithm and training data, and it leaves the role of RLHF tentative. "Plausibly" matches that degree of certainty.

## kirk2024
**Bib:** OK. Title, seven authors in order, ICLR 2024, editors and pp. 20620-20653 match the official ICLR proceedings BibTeX. That BibTeX also has `volume = {2024}`, which the bib omits (cosmetic).
**Citing sentence (l.88):** "Preference tuning reduces output diversity \citep{kirk2024, ...}".
**Verdict:** SUPPORTED: "RLHF significantly reduces output diversity compared to SFT".

## lee2026
**Bib:** OK. Title, single author Aron Lee, arXiv 2609.07447 (v1 7 Sep 2026) all match.
**Citing sentence (l.79):** excess-vocabulary methods with a counterfactual from pre-LLM years.
**Verdict:** SUPPORTED. The source defines excess vocabulary as "a word's frequency above its pre-2023 trend".

## liang2024monitoring
**Bib:** OK. Title, twelve authors in order, ICML 2024 (PMLR 235) and pp. 29575-29620 match PMLR. PMLR spells "Mcfarland"; the bib has "McFarland", which is the correct spelling.
**Citing sentences:**
- l.47-48: traces in "peer reviews". SUPPORTED: 6.5% to 16.9% of review text at ICLR, NeurIPS, CoRL and EMNLP was substantially LLM-modified.
- l.80: "distributional methods fit a mixture of human and LLM word distributions". SUPPORTED: the method is a maximum-likelihood mixture over word-occurrence distributions estimated from expert-written and AI-generated reference texts.

## mccarthy2010
**Bib:** OK. Title, authors (McCarthy, Jarvis), *Behavior Research Methods* 42(2):381-392, May 2010 and DOI 10.3758/BRM.42.2.381 match Crossref.
**Citing sentence (l.226):** "lexical diversity (MTLD; \citealp{mccarthy2010})".
**Verdict:** SUPPORTED. This is the standard validation reference for MTLD.

## openai2025gptoss
**Bib:** OK. Title "gpt-oss-120b & gpt-oss-20b Model Card", arXiv 2508.10925 (v1 8 Aug 2025) and year 2025 match. arXiv lists Sandhini Agarwal plus 123 others; the corporate author "OpenAI" is how the card presents itself and is acceptable.
**Citing sentence:** Table 1 caption, "Other dates"; Table 1 row "gpt-oss 20B | 2025-08 | Jun 2024".
**Checks:**
- Release month 2025-08: SUPPORTED (August 2025 release; HF collection dated 7 Aug 2025; card dated 8 Aug 2025).
- Cutoff Jun 2024: SUPPORTED: "Our model has a knowledge cutoff of June 2024."
- Parameters: 20.9B total, 3.6B active ("20B" in the paper is the model's name). Licence: Apache 2.0 plus the gpt-oss usage policy. The paper makes no claim about either.

## pillutla2021
**Bib:** OK. It is identical to the official NeurIPS 2021 BibTeX: seven authors, vol. 34, pp. 4816-4828.
**Citing sentence (l.97):** "Distribution-level comparisons ... evaluate models against human text".
**Verdict:** SUPPORTED. MAUVE "directly compares the learnt distribution from a text generation model to the distribution of human-written text".

## rallapalli2026
**Bib:** OK. Title, seven authors in order and arXiv 2604.14111 (v1 15 Apr 2026) match.
**Citing sentence (l.95-96):** "texts cluster by genre more than by source".
**Verdict:** SUPPORTED. PCA section: "texts from same genre tend to cluster together irrespective of the source". The study covers 67 Biber features, 8 genres and 11 LLMs. Caveat: the conclusion rests on visual inspection of PCA plots, not a formal test. The paper's wording is no stronger than the source's.

## shumailov2024
**Bib:** OK. Title, six authors, *Nature* 631(8022):755-759, July 2024 and DOI 10.1038/s41586-024-07566-y match Crossref.
**Citing sentence (l.428):** recent LLMs and recent writing "may no longer be independent references ... a precondition for the recursive dynamics studied in model-collapse work ... but not evidence of them."
**Verdict:** SUPPORTED. The source studies training on recursively generated data, and the sentence is suitably hedged.

## touvron2023llama2
**Bib:** OK. Title, all 68 authors in correct order, arXiv 2307.09288 (v1 18 Jul 2023) and year 2023 match.
**Citing sentence:** Table 1 footnote b, giving the "Sep 2022" cutoff for Llama-2-Chat 70B, Llama-2-Chat 7B and (via the base model) Vicuna 7B v1.5.
**Verdict:** SUPPORTED. The model card (Data Freshness) says: "The pretraining data has a cutoff of September 2022". The same line adds that some tuning data runs to July 2023. That does not conflict, because the column is defined as the pretraining-data cutoff. Release 2023 / 2023-07: consistent with the 18 July 2023 release (training "between January 2023 and July 2023"). For Vicuna, Touvron documents only the base model's cutoff. The caption already says that Vicuna's fine-tuning data are ChatGPT conversations, so this is handled.

## yang2026coverage
**Bib:** OK. Title, authors (Zini Yang, Emily Wenger, Richard So) and arXiv 2608.05576 (v1 6 Aug 2026) match.
**Citing sentence (l.97):** "Distribution-level comparisons ... evaluate models against human text".
**Verdict:** SUPPORTED. Its LLM-Cov and IBR metrics measure LLM output against the empirical distribution of human responses.

---

## Optional cosmetic fixes (copy-ready)
- kirk2024: add `volume = {2024},` to match the ICLR proceedings BibTeX.
- gemmareleases: `author = {{Google}},`. The page names no author, so this is optional.
- forman2008: `month=jun` is the online date; the print issue is October 2008. Leave it or drop `month`.

## Comparison with earlier reports
I read the earlier reports only after reaching my verdicts and found no disagreements. v5_followup marked the Vicuna release month as uncited; that claim belongs to vicuna15card, which is outside this set. v6_changed_sentences notes that forman2008 keeps the ISSN `1573-756X`; that ISSN is correct.
