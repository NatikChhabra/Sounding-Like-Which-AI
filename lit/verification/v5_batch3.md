# Citation verification, v5 batch 3

Scope: 23 keys from `_v5_batch3_input.md`. Each key gets a verdict for each citing sentence, where the evidence is in the source, a check of its `references.bib` entry, and a proposed fix where needed. Table rows are from `main.tex` l.214-243 (Table `tab:gens`).

---

## munozortiz2024
- **Claim:** LLM text differs systematically from human text in lexico-grammatical features.
- **Verdict:** SUPPORTED.
- **Evidence:** The abstract compares human news with six LLMs on morphological, syntactic, psychometric and sociolinguistic measures. Humans show more varied sentence length and vocabulary and use dependency and constituent types differently. LLMs use more numbers, symbols, auxiliaries and pronouns. The final sentence says LLM–human differences are larger than differences between LLMs. (Read via arXiv 2308.09067, which carries the AIR journal reference.)
- **Bib:** Correct: Muñoz-Ortiz et al., *Artificial Intelligence Review* 57(10), 2024, DOI matches. Minor: the article number (265) is missing; consider adding `pages={265}`.
- **Fix:** None.

## openai2023gpt4
- **Claim:** Footnote a of the table gives a Sep 2021 pretraining cutoff for GPT-4 (gpt-4-0613).
- **Verdict:** SUPPORTED.
- **Evidence:** Section 5 (Limitations) says most of GPT-4's pre-training data cuts off in September 2021. Footnote 10 there adds that pre- and post-training data contain a small amount of more recent data. Caveat: the report describes the March 2023 GPT-4, not the 0613 snapshot. OpenAI's API docs give the same cutoff for 0613, but the report does not name that snapshot.
- **Bib:** OK: author "OpenAI", 2023, arXiv 2303.08774. There is no peer-reviewed version, so @misc is appropriate.
- **Fix:** None needed. Optional: "Sep 2021$^a$" could note "most data".

## openai2025gptoss
- **Claim:** "Other dates" sources the release month (2025-08) and the Jun 2024 cutoff for gpt-oss 20B.
- **Verdict:** SUPPORTED.
- **Evidence:** The model card's title page is dated August 5, 2025. Section 2 (model training, "Data" paragraph) states a knowledge cutoff of June 2024.
- **Bib:** OK: OpenAI, 2025, arXiv 2508.10925, title matches.
- **Fix:** None.

## padmakumar2024
- **Claim:** Writing with instruction-tuned models reduces content diversity across users.
- **Verdict:** SUPPORTED.
- **Evidence:** The abstract reports that writing with InstructGPT, but not GPT-3, significantly reduced diversity. Essays by different authors became more similar, and the reduction came mainly from the model-contributed text.
- **Bib:** OK: Padmakumar & He, ICLR 2024 proceedings, title matches.
- **Fix:** None.

## park2026
- **Claim:** False-positive rates on non-native manuscripts vary widely.
- **Verdict:** SUPPORTED.
- **Evidence:** The abstract reports human-text FPRs from 0% to 100% across 13 detectors. Section 4.1 and Table 3 ("orig" column) show this range is for the original non-native manuscripts (pre-ChatGPT 2018–2022 subset) at a fixed 0.5 threshold (Appendix C). Section 6 notes that absolute FPRs depend on the threshold.
- **Bib:** OK: Park, Jeong, Kim, 2026, arXiv 2608.26710 (submitted 27 Aug 2026). Still a preprint.
- **Fix:** None.

## phi4card
- **Claim:** "Other dates" sources the release month (2024-12) and the Jun 2024 cutoff for Phi-4 14B.
- **Verdict:** SUPPORTED.
- **Evidence:** The HF model card gives a release date of 12 Dec 2024 and says public data runs to June 2024. It lists the model as 14B parameters.
- **Bib:** OK: Microsoft, 2024, HF URL. Optional: the Phi-4 Technical Report (Abdin et al., arXiv 2412.08905) is the citable document.
- **Fix:** None.

## pillutla2021
- **Claim:** Distribution-level comparisons evaluate models against human text.
- **Verdict:** SUPPORTED.
- **Evidence:** The abstract says MAUVE compares a generation model's learned distribution with the distribution of human text, using divergence frontiers.
- **Bib:** OK: Pillutla et al., NeurIPS 34, 2021. The page numbers were not checked: the proceedings page does not list them.
- **Fix:** None.

## pu2023zeroshot
- **Claim:** Detectors transfer unevenly to unseen generators.
- **Verdict:** SUPPORTED.
- **Evidence:** The abstract reports that no detector generalizes to all generators. The one consistent transfer is from medium-sized models to their larger versions.
- **Bib:** OK: Pu et al., Findings of EMNLP 2023, pp. 4799–4808, DOI matches. The input file gave no link; the ACL Anthology entry is 2023.findings-emnlp.318.
- **Fix:** None.

## qwen35card
- **Claim:** "Other dates" sources the release month (2026-03) for Qwen3.5 9B.
- **Verdict:** PARTLY / CANNOT VERIFY from the cited source.
- **Evidence:** The HF card gives no explicit release date. Its suggested BibTeX dates the Qwen3.5 family to February 2026. The HF repo was created 27 Feb 2026. Secondary catalogues (DataLearner, NVIDIA/Vultr docs) give a public release of 2 Mar 2026, which matches "2026-03", but the cited card does not state it.
- **Bib:** Author "Qwen Team", 2026, HF URL, which is fine. The card asks to be cited as "Qwen3.5: Towards Native Multimodal Agents" (Qwen blog, qwen.ai/blog?id=qwen3.5). Consider using that title or adding the blog URL.
- **Fix:** Keep 2026-03, but source it from the release post or HF release, or change the table to "2026-02/03". Minimal option: leave the table and add "release month from the HF release" to the caption.

## rallapalli2026
- **Claim:** Texts cluster by genre more than by source.
- **Verdict:** SUPPORTED.
- **Evidence:** The abstract (2nd finding) says genre influences stylistic features more strongly than source does. Section 4.2 (PCA of genre-by-source means, Fig. 6) says texts of the same genre cluster together regardless of source. Nuance: Section 4.3 and the Introduction say instruction-tuned models often cluster apart from human and base-model text within a genre. That does not contradict the cited claim.
- **Bib:** OK: Rallapalli et al., 2026, arXiv 2604.14111. No venue is listed, so it is still a preprint.
- **Fix:** None.

## reinhart2025
- **Claim:** LLM text differs systematically from human text in lexico-grammatical features.
- **Verdict:** SUPPORTED.
- **Evidence:** The abstract (arXiv 2410.16107 = the PNAS paper) uses Biber's features on parallel human and LLM corpora. It reports systematic LLM–human differences that are larger for instruction-tuned models.
- **Bib:** OK: Reinhart et al., PNAS 122(8), 2025, DOI matches. Minor: the article number e2422455122 is missing.
- **Fix:** None.

## sadasivan2025
- **Claim:** Detectors can be evaded.
- **Verdict:** SUPPORTED.
- **Evidence:** The abstract says recursive paraphrasing sharply lowers detection rates for watermarking, neural, zero-shot and retrieval-based detectors, with only slight loss of text quality.
- **Bib:** OK: the full TMLR title matches mlanthology's TMLR 2025 listing; Sadasivan et al., TMLR 2025.
- **Fix:** None.

## shaib2024
- **Claim:** LLM text differs from human text in recurring part-of-speech templates.
- **Verdict:** SUPPORTED.
- **Evidence:** The abstract defines syntactic templates as POS sequences. It finds models produce templated text more often than human reference texts do.
- **Bib:** OK: Shaib et al., EMNLP 2024, pp. 6416–6431, DOI matches.
- **Fix:** None.

## shumailov2024
- **Claim (s1):** Models trained on their own outputs degrade when synthetic data replace real data.
  - **Verdict:** SUPPORTED. The abstract says indiscriminate training on generated content causes irreversible defects, with the tails of the distribution disappearing. The LLM experiment (OPT-125m, "Language Models" section, Fig. 11) has a no-original-data setting that degrades. The 10%-original-data setting degrades only slightly. Note: even with 10% preserved there is minor degradation, so "replace" is a fair contrast and not an overstatement.
- **Claim (s2):** These are the recursive dynamics studied in model-collapse work.
  - **Verdict:** SUPPORTED.
- **Bib:** OK: Shumailov et al., *Nature* 631(8022):755–759, 2024, DOI matches.
- **Fix:** None.

## sourati2025
- **Claim:** LLM rewriting compresses stylistic variance.
- **Verdict:** SUPPORTED.
- **Evidence:** The abstract of arXiv v2, which matches the NHB version, says LLM rewriting keeps content but homogenizes style. It reports writing-complexity variance falling by a significant 21–50% across datasets and models.
- **Bib:** Mostly OK: Sourati et al., *Nature Human Behaviour*, DOI matches, published online 24 Aug 2026, year 2026. The key says 2025 but the entry says 2026, which is harmless. Volume and pages are not yet assigned.
- **Fix:** None.

## sun2025
- **Claim:** Classifier- and detector-based studies label documents.
- **Verdict:** SUPPORTED.
- **Evidence:** The abstract describes training detectors on AIGTBench and applying the best one (OSM-Det) to about 2.4M Medium, Quora and Reddit posts. It then tracks an "AI attribution rate" over time.
- **Bib:** OK: Sun et al., ACL 2025 (long), pp. 22975–23005, DOI matches.
- **Fix:** None.

## sun2025idiosyncrasies
- **Claim:** Individual models have distinctive, identifiable output patterns.
- **Verdict:** SUPPORTED.
- **Evidence:** The abstract reports 97.1% accuracy for five-way source-LLM classification. The patterns are rooted in word-level distributions and persist after rewriting.
- **Bib:** OK: Sun et al., ICML 2025, PMLR 267:57854–57885.
- **Fix:** None.

## touvron2023llama2
- **Claim:** Footnote b gives a Sep 2022 pretraining cutoff for Llama-2-Chat and Vicuna v1.5 (Llama 2 base); Llama 2 released 2023-07.
- **Verdict:** SUPPORTED.
- **Evidence:** The Model Card in Appendix A.7 says pretraining data cuts off in September 2022, with some tuning data as recent as July 2023. The arXiv v1 is dated 18 Jul 2023.
- **Bib:** OK: Touvron et al., 2023, arXiv 2307.09288. There is no peer-reviewed version.
- **Fix:** None.

## wu2025monoculture
- **Claim:** Preference tuning reduces output diversity.
- **Verdict:** SUPPORTED.
- **Evidence:** The abstract (last sentence) places the root causes in alignment processes. Section 5, Takeaway 3 ("RLHF Hurts Diversity the Most") compares pretrained Llama-2, SFT Vicuna-13b and RLHF Llama-2-chat on review sentiment diversity. RLHF is the least diverse.
- **Bib:** OK: Wu, Black, Chandrasekaran, ICLR 2025; the PDF header confirms the conference version.
- **Fix:** None.

## yakura2024
- **Claim (s1):** LLM-associated words have become more frequent in unscripted speech.
  - **Verdict:** SUPPORTED. The abstract and main text use 737k hours from about 825k podcast episodes, filtered for spontaneous speech. They report abrupt rises in ChatGPT-associated words such as "delve" after ChatGPT's release.
- **Claim (s2):** LLM-associated vocabulary has grown in human speech.
  - **Verdict:** SUPPORTED. Appendix B replicates the finding on YouTube academic talks, which are mostly prepared speech.
- **Bib:** OK as a preprint: Yakura et al., arXiv 2409.01754v4 (16 Jul 2026); the author list matches v4. No journal version was found. The key says 2024 but the entry says 2026, which is harmless; arXiv v1 is from 2024.
- **Fix:** None.

## yang2025qwen3
- **Claim:** "Other dates" sources the release month (2025-04) for Qwen3 8B (with Granite 3.3).
- **Verdict:** PARTLY.
- **Evidence:** The report identifies the Qwen3 dense models, including 8B, but does not state a release date. arXiv v1 is dated 14 May 2025. The 2025-04 month matches the HF repo Qwen/Qwen3-8B, created 27 Apr 2025, and the public launch of 29 Apr 2025, but the report does not state it.
- **Bib:** OK: Yang et al., 2025, arXiv 2505.09388. There is no peer-reviewed version.
- **Fix:** Optional: add the HF card (huggingface.co/Qwen/Qwen3-8B) as the date source, or accept it as is, since the caption says "Other dates" in general.

## yang2026coverage
- **Claim:** Distribution-level comparisons evaluate models against human text.
- **Verdict:** SUPPORTED.
- **Evidence:** The abstract proposes the LLM-Cov and IBR metrics, which measure LLM output breadth against the empirical distribution of human writing on the same topic.
- **Bib:** OK: Yang, Wenger, So, 2026, arXiv 2608.05576. Still a preprint.
- **Fix:** None.

## zheng2023judging
- **Claim:** Footnote d says Vicuna 7B v1.5 is "Llama 2 fine-tuned on user-shared ChatGPT conversations".
- **Verdict:** PARTLY.
- **Evidence:** Appendix E (Vicuna training) describes Vicuna as a fine-tuned **LLaMA** (v1) base trained on about 125K user-shared ShareGPT ChatGPT conversations. The paper does not mention Llama 2 or v1.5. The Llama 2 base for v1.5 comes from the lmsys/vicuna-7b-v1.5 HF card, which cites this paper for its training details. Separately, the HF repo was created 29 Jul 2023; the table's 2023-08 is plausibly the public release month, but it was not checked against a source.
- **Bib: needs fix.** The entry is an arXiv @misc, but the paper was published at **NeurIPS 2023, Datasets and Benchmarks Track** (arXiv comments field). Suggested change: `@inproceedings{zheng2023judging, ..., booktitle={Advances in Neural Information Processing Systems 36 (Datasets and Benchmarks Track)}, year={2023}}`.
- **Fix (caption):** "$^d$Llama~2 fine-tuned on user-shared ChatGPT conversations (training recipe: \citealp{zheng2023judging}; base model per the lmsys/vicuna-7b-v1.5 model card)". Shorter alternative: "$^d$fine-tuned from Llama~2 with the Vicuna recipe of training on user-shared ChatGPT conversations \citep{zheng2023judging}."

---

## Summary table

| Key | Verdict | Needs fix? |
|---|---|---|
| munozortiz2024 | SUPPORTED | No (optional: add article no. 265) |
| openai2023gpt4 | SUPPORTED | No |
| openai2025gptoss | SUPPORTED | No |
| padmakumar2024 | SUPPORTED | No |
| park2026 | SUPPORTED | No |
| phi4card | SUPPORTED | No |
| pillutla2021 | SUPPORTED | No |
| pu2023zeroshot | SUPPORTED | No |
| qwen35card | PARTLY / CANNOT VERIFY (card gives no date; BibTeX says Feb 2026; public release 2 Mar 2026 per secondary sources) | Minor: source the month or cite the Qwen3.5 blog |
| rallapalli2026 | SUPPORTED | No |
| reinhart2025 | SUPPORTED | No (optional: add e2422455122) |
| sadasivan2025 | SUPPORTED | No |
| shaib2024 | SUPPORTED | No |
| shumailov2024 | SUPPORTED (both sentences) | No |
| sourati2025 | SUPPORTED | No |
| sun2025 | SUPPORTED | No |
| sun2025idiosyncrasies | SUPPORTED | No |
| touvron2023llama2 | SUPPORTED | No |
| wu2025monoculture | SUPPORTED | No |
| yakura2024 | SUPPORTED (both sentences) | No |
| yang2025qwen3 | PARTLY (report gives no release month) | Optional: add HF card as date source |
| yang2026coverage | SUPPORTED | No |
| zheng2023judging | PARTLY (paper covers LLaMA-based Vicuna, not v1.5/Llama 2) | **Yes**: reword footnote d; bib should be NeurIPS 2023 D&B, not arXiv |
