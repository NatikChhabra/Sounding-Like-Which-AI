# Citation verification, v5 follow-up pass

Scope: full citing sentences from `_v5_followup_input.md`, plus every date in Table `tab:gens` (main.tex lines 208-246) checked against the sources the caption cites. `\R{}` values were not checked. Sources were read on 2026-10-13.

Bibliography check: `vicuna15card`, `qwen3card` and `gemmareleases` showed "?" in the input file, but all three exist in `paper/references.bib` (lines 529-551). They will resolve.

---

## bao2024fastdetectgpt
Source: arXiv 2310.05130 (ICLR 2024), full PDF read.

1. "Zero-shot detectors use token-likelihood statistics (hans2024binoculars, bao2024fastdetectgpt) ..." **SUPPORTED.** The abstract calls Fast-DetectGPT an optimized zero-shot detector. Its conditional probability curvature is computed from the scoring model's token log-probabilities (Sec. 2, Eq. 3-4).
2. "the analytic Fast-DetectGPT criterion (bao2024fastdetectgpt) computed with GPT-2 small ..." **SUPPORTED.** Sec. 2 says the sampling and scoring steps "have an analytical solution". Appendix B derives it and reports accuracy almost identical to the 10k-sample version. Using GPT-2 small and the AUC and flag-rate numbers are the authors' own choices and results, so they were not checked.

Fix: none.

## gemma3card
Source: ai.google.dev/gemma/docs/core/model_card_3.
- Table row "Gemma 3 12B | 2025-03 | Aug 2024". The cutoff is **SUPPORTED**: the card says the knowledge cutoff for the training data was August 2024. The card gives no release date. The month 2025-03 comes from `gemmareleases`, which dates Gemma 3 (1B/4B/12B/27B) to March 10, 2025. The row is supported by the cited set.

Fix: none.

## gemma4card
Source: huggingface.co/google/gemma-4-12B-it. The card says it is for "the Gemma 4 12B Unified model".
- Table row "Gemma 4 12B | 2026-06 | Jan 2025". The cutoff is **SUPPORTED**: the card gives a training-data cutoff of January 2025. The card has no release date. 2026-06 comes from `gemmareleases`, which lists "Gemma 4 12B Unified" on June 3, 2026, the same model. Supported by the cited set.

Fix: none.

## gemmareleases
Source: ai.google.dev/gemma/docs/releases (bib entry present).
- It supports Gemma 3 (12B) on March 10, 2025 and Gemma 4 12B Unified on June 3, 2026. **SUPPORTED.**

Fix: none.

## granitecards
Bib URL: huggingface.co/ibm-granite/granite-4.2-8b (`howpublished` is the ibm-granite org page).
- "Granite 4.2 8B | 2026-08": **SUPPORTED.** The 4.2 card lists a release date of August 25, 2026. It states no cutoff, and the table leaves that cell blank.
- "Granite 3.3 8B | 2025-04": **SUPPORTED by the source, PARTLY by the bib entry.** The Granite 3.3 8B Instruct card (huggingface.co/ibm-granite/granite-3.3-8b-instruct) gives "April 16th, 2025". The 4.2 card at the bib `url` does not mention 3.3. The bib title names both cards, but only the 4.2 URL is given.
- Fix (bib only, optional): add the 3.3 URL, e.g. `howpublished = {\url{https://huggingface.co/ibm-granite/granite-3.3-8b-instruct} and \url{https://huggingface.co/ibm-granite/granite-4.2-8b}}`.

## jiang2023mistral
Source: arXiv 2310.06825 (v1 only, 10 Oct 2023). It describes Mistral 7B v0.1 and states no data cutoff.
- RAID row "Mistral-7B-Instr. v0.1 | 2023": **SUPPORTED.**
- "Mistral 7B Instruct v0.3 | 2024-05": **NOT SUPPORTED by any cited source.** The paper predates v0.3 and never mentions it. The v0.3 HF card (huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) also states no date, though the HF API shows the repo was created 2024-05-22. The month looks correct but has no citation.
- Fix: add a bib entry for the v0.3 card and add it to "Other dates". Suggested entry: `@misc{mistral03card, title={Mistral-7B-Instruct-v0.3 Model Card}, author={{Mistral AI}}, year={2024}, howpublished={\url{https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3}}, note={Hugging Face repository created 22 May 2024}}`. Because the card itself has no date, the `note` should carry the date.

## liang2023detectors
Source: Patterns 2023 / arXiv 2304.02819, full text read. Also the HF dataset WxWx/ChatGPT-Detector-Bias and the GitHub repo Weixin-Liang/ChatGPT-Detector-Bias.

1. "some detectors have flagged non-native writers' human text as AI-generated at high rates": **SUPPORTED.** Across seven detectors, the average false-positive rate on 91 TOEFL essays was 61.22% (main text, first results paragraph).
2. "...and have flagged non-native writing (liang2023detectors)": **SUPPORTED** (same passage).
3. "...flags X% of TOEFL essays but Y% of US 8th-grade essays, reproducing the bias reported by liang2023detectors": **SUPPORTED.** The paper reports near-perfect accuracy on 88 US 8th-grade essays and more than half of TOEFL essays misclassified (Fig. 1a).
4. "RAID and the Hugging Face release of liang2023detectors, MIT; their US 8th-grade essays come from the authors' GitHub repository, which states no licence, and derive from the Hewlett Foundation ASAP data ...": **PARTLY.**
   - The HF dataset licence field is "mit", so "MIT" is correct. The HF folder list (TOEFL, CollegeEssay, CS224N) has no Hewlett essays, so taking them from GitHub is consistent.
   - The essays deriving from Hewlett Foundation ASAP is correct: the paper says the 88 essays were sourced from the ASAP dataset (ref. 24, Kaggle asap-aes). The GitHub folder is `HewlettStudentEssay_real_88/`.
   - **"which states no licence" is inaccurate.** The repo has no LICENSE file (the GitHub licence API returns 404), but README line 3 shows an "MIT license" badge.
   - Fix: replace "which states no licence," with "which has no licence file (its README shows an MIT badge)," and keep the rest. The decision to release only scores still holds because of the ASAP origin.

## liang2024mapping
Source: COLM 2024 / arXiv 2404.01268, HTML full text read.

1. Intro: "Corpus studies find traces of LLM-assisted writing in abstracts ...": **SUPPORTED** (arXiv, bioRxiv and Nature abstracts and introductions, 2020 to Feb 2024).
2. "Prevalence estimators report a small 'LLM share' for text written before ChatGPT, which studies treat as consistent with false positives (liang2024mapping)": **SUPPORTED.** Sec. 5.1 gives Nov 2022 alpha values of about 2.3-3.1% and calls them consistent with the false-positive rate from Sec. 4.2. Sec. 6 refers to consistently low false-positive estimates in 2022.
3. Related work: "distributional methods fit a mixture of human and LLM word distributions": **SUPPORTED** (Sec. 3, distributional quantification framework).
4. "This is the high-CS, low-mathematics ordering that prevalence studies report": **SUPPORTED.** The abstract and Fig. 1 show CS with the largest, fastest growth and mathematics (with Nature portfolio) the least.
5. "...against prevalence estimates of 17.5% and 4.9% of sentences by February 2024 (liang2024mapping)": **SUPPORTED.** Fig. 1 and Sec. 5.1 give alpha for abstracts in Feb 2024: CS 17.5%, Mathematics 4.9%. Sec. 3 says sentences are the unit for the main estimates. Note that the abstract's "up to 6.3%" is the Nature portfolio figure, not mathematics, so 4.9% is the correct mathematics value. For introductions, CS is 15.3-15.5% and math 3.5-3.9%, so the cited figures are the abstract ones, which matches the context.
   - Optional clarity: "17.5\% and 4.9\% of abstract sentences by February 2024".

## llama31card
Source: meta-llama/llama-models MODEL_CARD.md (Llama 3.1).
- "Llama 3.1 8B | 2024-07 | Dec 2023": **SUPPORTED.** The card gives a release date of July 23, 2024 and says the pretraining data has a cutoff of December 2023.

Fix: none.

## mccarthy2010
Source: Behavior Research Methods 42(2):381-392 (DOI 10.3758/BRM.42.2.381).
- "MTLD lexical diversity (mccarthy2010)": **SUPPORTED.** The paper validates MTLD (with vocd-D and HD-D) as a lexical-diversity measure, as stated in the title and abstract. The bib title is complete. The input showed `{MTLD` only because of an extraction artefact.

Fix: none.

## openai2023gpt4
Source: arXiv 2303.08774, PDF text extracted.
- "GPT-4 (gpt-4-0613) | 2023 | Sep 2021^a": **SUPPORTED.** The Limitations section (Sec. 5) says GPT-4 lacks knowledge of events after its pre-training data "cuts off in September 2021". The report is dated 2023. The specific 0613 snapshot is not described there, but the year is consistent.

Fix: none.

## openai2025gptoss
Source: arXiv 2508.10925 (model card dated August 5, 2025; arXiv v1 dated 8 Aug 2025).
- "gpt-oss 20B | 2025-08 | Jun 2024": **SUPPORTED.** Sec. 2.4 says "Our model has a knowledge cutoff of June 2024", and the card is dated August 2025.

Fix: none.

## phi4card
Source: huggingface.co/microsoft/phi-4.
- "Phi-4 14B | 2024-12 | Jun 2024": **SUPPORTED.** The card gives a release date of December 12, 2024 and an offline dataset with cutoff dates of June 2024 and earlier for publicly available data. The card says 14B parameters.

Fix: none.

## qwen35card
Source: huggingface.co/Qwen/Qwen3.5-9B.
- "Qwen3.5 9B | 2026-02/03": **SUPPORTED (weakly).** The card's BibTeX says February 2026. Its commit history runs from Feb 27 to Mar 2, and the HF API shows the repo was created 2026-02-27. That fits "2026-02/03". There is no cutoff, and the cell is blank.

Fix: none needed. "2026-02" alone would also be defensible.

## qwen3card
Source: huggingface.co/Qwen/Qwen3-8B (bib entry present).
- "Qwen3 8B | 2025-04": **PARTLY.** The model card states no release date, and the only date on it is the tech report (May 14, 2025). The month is correct by other evidence: the HF repo was created 2025-04-27 with weights uploaded Apr 28, and the Qwen3 blog linked from the card is dated April 29, 2025 and lists Qwen3-8B. The cited source does not itself state the date.
- Fix (bib, optional): add `note = {Released 29 April 2025; see \url{https://qwenlm.github.io/blog/qwen3/}}`, or cite the blog.

## touvron2023llama2
Source: arXiv 2307.09288 (v1 18 Jul 2023), PDF text extracted.
- "Llama-2-70B-chat | 2023 | Sep 2022^b" and "Llama-2-Chat 7B | 2023-07 | Sep 2022^b": **SUPPORTED.** The model card in Appendix A.7 says the pretraining data has a cutoff of September 2022, with some tuning data up to July 2023. The paper and release are from July 2023.
- "Vicuna 7B v1.5 | ... | Sep 2022^b": **SUPPORTED** as a *pretraining*-data cutoff, which is what the column claims, because Vicuna v1.5 inherits Llama 2 pretraining. Footnote d already says its fine-tuning data are ChatGPT conversations, which postdate ChatGPT. No change needed.

## vicuna15card
Source: huggingface.co/lmsys/vicuna-7b-v1.5 (bib entry present).
- Footnote d, "fine-tuned from Llama 2 (vicuna15card)": **SUPPORTED.** The card says Vicuna is trained by fine-tuning Llama 2 on about 125K user-shared ShareGPT conversations.
- "Vicuna 7B v1.5 | 2023-08": **NOT SUPPORTED by any cited source.** The card has no release date. `zheng2023judging` (versions Jun-Dec 2023) never mentions v1.5 or Llama 2. The month is correct by external evidence: the FastChat README news reads "[2023/08] We released Vicuna v1.5 based on Llama 2", and the HF repo was created 2023-07-29.
- Fix: add `note = {Released August 2023 per \url{https://github.com/lm-sys/FastChat}}` to `vicuna15card`, or cite the FastChat repo.

## zheng2023judging
Source: arXiv 2306.05685 (v4, 24 Dec 2023), HTML read.
- Footnote d, "with the Vicuna recipe of training on user-shared ChatGPT conversations (zheng2023judging)": **SUPPORTED.** Appendix E describes training Vicuna by fine-tuning a LLaMA base model on cleaned ShareGPT conversations, which are user-shared ChatGPT conversations. The paper describes the original LLaMA-based Vicuna, not v1.5, but the sentence attributes only the recipe to it, so this is fine.

Fix: none.

---

## Table tab:gens date coverage (rows vs cited sources)

| Row | Released | Cutoff | Source that supports it | OK? |
|---|---|---|---|---|
| GPT-4 (0613) | 2023 | Sep 2021 | openai2023gpt4 (Sec. 5) | yes |
| Llama-2-70B-chat | 2023 | Sep 2022 | touvron2023llama2 (App. A.7) | yes |
| ChatGPT 3.5-turbo-0613 | 2023 | (2021) | footnote c, secondary sources (no citation) | release year uncited (minor) |
| Mistral-7B-Instr. v0.1 | 2023 | none | jiang2023mistral | yes |
| MPT-30B-chat; Cohere command | 2023 | none | none cited | release year uncited (minor) |
| Mistral 7B Instruct v0.3 | 2024-05 | none | **none cited** (jiang2023mistral is v0.1, Oct 2023) | **no** |
| Llama 3.1 8B | 2024-07 | Dec 2023 | llama31card | yes |
| Phi-4 14B | 2024-12 | Jun 2024 | phi4card | yes |
| Gemma 3 12B | 2025-03 | Aug 2024 | gemmareleases + gemma3card | yes |
| Granite 3.3 8B | 2025-04 | none | Granite 3.3 card (named in granitecards title; URL not in bib) | yes, bib URL incomplete |
| Qwen3 8B | 2025-04 | none | qwen3card has no date; blog/HF history confirm | partly |
| gpt-oss 20B | 2025-08 | Jun 2024 | openai2025gptoss | yes |
| Claude Opus 5.5 | 2026 | none | authors' own use | n/a |
| Llama-2-Chat 7B | 2023-07 | Sep 2022 | touvron2023llama2 | yes |
| Vicuna 7B v1.5 | 2023-08 | Sep 2022 | cutoff via touvron2023llama2; **release month uncited** (FastChat confirms) | partly |
| Qwen3.5 9B | 2026-02/03 | none | qwen35card (Feb 2026 BibTeX; commits Feb 27-Mar 2) | yes |
| Gemma 4 12B | 2026-06 | Jan 2025 | gemmareleases + gemma4card | yes |
| Granite 4.2 8B | 2026-08 | none | granitecards (4.2 card, Aug 25 2026) | yes |

Optional, for the uncited 2023 years of the RAID rows: cite `dugan2024raid` in the RAID group header, or drop the "Released" year for those rows.

---

## Summary

| Key | Verdict | Needs fix? |
|---|---|---|
| bao2024fastdetectgpt | SUPPORTED (both sentences) | no |
| gemma3card | SUPPORTED (cutoff; month via gemmareleases) | no |
| gemma4card | SUPPORTED (cutoff; month via gemmareleases) | no |
| gemmareleases | SUPPORTED | no |
| granitecards | SUPPORTED; bib URL covers only 4.2 | optional (add 3.3 URL) |
| jiang2023mistral | SUPPORTED for v0.1/2023; NOT SUPPORTED for v0.3 2024-05 | **yes** (cite v0.3 card) |
| liang2023detectors | SUPPORTED x3; PARTLY for the licence sentence | **yes** ("states no licence" is wrong) |
| liang2024mapping | SUPPORTED (all 5, incl. 17.5% / 4.9%) | optional ("abstract sentences") |
| llama31card | SUPPORTED | no |
| mccarthy2010 | SUPPORTED | no |
| openai2023gpt4 | SUPPORTED | no |
| openai2025gptoss | SUPPORTED | no |
| phi4card | SUPPORTED | no |
| qwen35card | SUPPORTED | no |
| qwen3card | PARTLY (card has no date; month correct per blog) | optional (bib note) |
| touvron2023llama2 | SUPPORTED | no |
| vicuna15card | SUPPORTED (Llama 2 base); release month 2023-08 not in any cited source | **yes** (bib note / FastChat) |
| zheng2023judging | SUPPORTED | no |
