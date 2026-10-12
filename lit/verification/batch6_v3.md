# Verification batch 6 (v3)

Checked 2026-10-13. Every quote below comes from the primary source: the arXiv PDF text extracted with pdftotext, the publisher page, the model card, or the repository.

---

## 1. Llama 2 data cutoff (Touvron et al. 2023, arXiv:2307.09288)
- **Quote** (Appendix A.7, Table 52 "Model card for Llama 2", row "Data Freshness"): "The pretraining data has a cutoff of September 2022, but some tuning data is more recent, up to July 2023."
- Same table, "Model Dates": "Llama 2 was trained between January 2023 and July 2023."
- URL: https://arxiv.org/pdf/2307.09288 (v2)
- **Verdict: SUPPORTED.** Cite it as the Llama 2 model card (Table 52, Appendix A.7). The abstract does not mention the cutoff.

## 2. Vicuna: training data, base models, Ollama tag
- **ShareGPT data.** Zheng et al. 2023 (arXiv:2306.05685), App. E: "Vicuna is created by fine-tuning a LLaMA base model using user-shared conversations gathered from ShareGPT.com". It adds: "ShareGPT is a website where users can share their ChatGPT conversations." The data comes to "125K conversations after data cleaning". Footnote 4: "we use more data (125K) than the version in our earlier blog post (70K)." **SUPPORTED.**
- **LMSYS blog** (https://lmsys.org/blog/2023-03-30-vicuna/): "we collected around 70K conversations from ShareGPT.com". This applies to v0 (30 Mar 2023).
- **v1.5.** HF card (https://huggingface.co/lmsys/vicuna-7b-v1.5): "Finetuned from model: Llama 2". The training data is "around 125K conversations collected from ShareGPT.com", and the license is the Llama 2 Community License. **SUPPORTED.**
- **v1.3.** HF card (https://huggingface.co/lmsys/vicuna-7b-v1.3): "Finetuned from model: LLaMA" (links arXiv:2302.13971). The data is the same ~125K ShareGPT conversations, under a non-commercial license. **SUPPORTED.**
- **FastChat weights table** (https://github.com/lm-sys/FastChat/blob/main/docs/vicuna_weights_version.md):
  - v1.5 has base "Llama 2", released Aug. 1, 2023, trained on "370M tokens".
  - v1.3 has base "Llama 1", released Jun. 22, 2023, trained on "370M tokens".
  - v1.3 note: "Train with twice the amount of ShareGPT data compared to previous versions."
- **Ollama `vicuna:7b`.** On https://ollama.com/library/vicuna/tags, `vicuna:7b` = `vicuna:latest` = digest **370739dc897b** (3.8GB, 4K context). That is the same digest as **`7b-v1.5-q4_0`**, so `vicuna:7b` is **Vicuna v1.5 7B (Llama 2 base), 4-bit q4_0**. The library page says "v1.5 is trained by fine-tuning Llama 2", "v1.3 is trained by fine-tuning Llama", and "All three variants are trained using conversations collected from ShareGPT." The page states no license. **SUPPORTED** (inferred from the shared digest).
- **When the ShareGPT data was collected.** No primary Vicuna source gives collection dates. **UNCLEAR.** Indirect bounds:
  - ShareGPT launched in early Dec 2022. Voicebot.ai, 12 Dec 2022: https://voicebot.ai/2022/12/12/new-sharegpt-tool-turns-chatgpt-conversations-into-sharable-links/
  - The 70K set existed by 30 Mar 2023 and the 125K set by the v1.3 release (22 Jun 2023).
  - So the safe wording is "ChatGPT conversations shared via ShareGPT, roughly Dec 2022 to mid-2023". Mark it as an inference.
- **Conversation counts.** About 125K for v1.3 and v1.5 (both HF cards, and the paper's App. E). About 70K for the original v0 (blog).

## 3. GPT-4 knowledge cutoff (OpenAI 2023, arXiv:2303.08774)
- **Quote** (Sec. 5 "Limitations", p. 10): "GPT-4 generally lacks knowledge of events that have occurred after the vast majority of its pre-training data cuts off in September 2021".
- Footnote 10: "The pre-training and post-training data contain a small amount of more recent data".
- URL: https://arxiv.org/pdf/2303.08774
- **Verdict: SUPPORTED.** Keep the hedge "vast majority" if you paraphrase.

## 4. RAID generators and abstract prompt (Dugan et al. 2024, arXiv:2405.07940)
Source: Table 10 "The generative models used in our project" and Appendix E.2 (https://arxiv.org/pdf/2405.07940, v2).

| RAID label | Exact identifier (paper) |
|---|---|
| gpt2 | `gpt2-xl` (GPT-2 XL 1.5B) |
| gpt3 | `text-davinci-002` ("In this study, we use the text-davinci-002 model.") |
| chatgpt | `gpt-3.5-turbo-0613` |
| gpt4 | `gpt-4-0613` |
| cohere / cohere-chat | Cohere `command` via `co.generate()` / `co.chat()`. Unversioned, queried 1–2 Nov 2023 |
| llama-chat | `Llama-2-70b-chat-hf` (70B; no base Llama in RAID) |
| mistral / mistral-chat | `Mistral-7B-v0.1` / `Mistral-7B-Instruct-v0.1` |
| mpt / mpt-chat | `mpt-30b` / `mpt-30b-chat` |

- **Discrepancy:** the GitHub README (https://github.com/liamdugan/raid) lists "GPT-3 (text-davinci-003)". The paper's Table 10 and App. E.2 both say **text-davinci-002**. Cite the paper. If you need to note the conflict, say the README differs.
- **Abstract prompt templates** (Table 2 / Table 12):
  - Chat models: `Write the abstract for the academic paper titled "{title}".`
  - Non-chat (continuation) models: `The following is the full text of the abstract for a research paper titled "{title}" from arxiv.org:`
- **Abstracts source:** the abstracts are scraped from arXiv, from the Kaggle dataset of Paul & Rakshit (2021). "we filter the data such that only papers from 2023 or later are present". Only the title is passed to the generator.
- **Verdict: SUPPORTED** (paper). The README contradicts the paper on the GPT-3 identifier.

## 5. Liang et al. 2024, "Mapping the Increasing Use of LLMs in Scientific Papers" (arXiv:2404.01268)
- **Quote** (Sec. 5.1): "By February 2024, the estimated α for Computer Science had increased to 17.5% for abstracts". Also: "the estimated α for Mathematics had increased to 4.9% for abstracts".
- The latest time point is **February 2024**. The Nov 2022 pre-ChatGPT baselines are CS 2.3% and Math 2.4%.
- **Caution:** the abstract says "Mathematics papers and the Nature portfolio showed the least LLM modification (up to 6.3%)". The 6.3% is the **Nature portfolio** figure. **Math abstracts = 4.9%.**
- The PDF is internally inconsistent on CS introductions: Sec. 1 says 15.3%, Sec. 5.1 says 15.5%.
- arXiv has only v1 (1 Apr 2024). The abs page does not mention COLM, so check the COLM camera-ready if you cite numbers from it.
- URL: https://arxiv.org/pdf/2404.01268
- **Verdict: SUPPORTED** for CS 17.5% (Feb 2024). The Math value is **4.9%, not 6.3%**.

## 6. Askitas (2025), IZA DP No. 18062
- **Corpus:** this is **not arXiv**. The corpus is economics working-paper abstracts from the **IZA Discussion Paper series**, taken from RePEc metadata, 2010 onward. "We examine the uptake and measurable effects of GPT-assisted writing in economics working paper abstracts."
- **Method:** stylometry (mean word length, type-token ratio, readability), event-study regressions with fixed effects and a placebo cutoff (2018), and a GPT-3.5 "optimise this abstract" similarity experiment. It also uses a classifier trained on original vs. GPT-optimised abstracts (97% accuracy).
- **Main finding:** "we detect a significant stylistic shift following the public release of ChatGPT-3.5 in March 2023". The paper estimates "adoption rates, ranging from 16% to 19%", while only 5.3% of papers mention generative AI. The classifier's GPT-like share rises "from a stable baseline of 13% to over 32%". Readability declines.
- **Note:** the paper dates the shock to March 2023 ("ChatGPT-3.5"), not to ChatGPT's 30 Nov 2022 launch. Don't restate that date as fact. The author also discloses "Extensive use of the OpenAI API" in drafting.
- URL: https://docs.iza.org/dp18062.pdf (Aug 2025)
- **Verdict: SUPPORTED** (summary as above).

## 7a. Kusumegi et al. (citations.txt: `kusumegi2026 arxiv:2601.13187`)
- Title: "Scientific production in the era of Large Language Models" (Kusumegi, Yang, Ginsparg, de Vaan, Stuart, Yin).
- **Year note:** the PDF states "The definitive version was published in Science on 18 Dec 2025, DOI: 10.1126/science.adw3000." The key "2026" reflects the arXiv posting. Consider citing it as Science 2025.
- **Data:** 2.1M preprints from arXiv, bioRxiv and SSRN (Jan 2018–Jun 2024). LLM use is detected on abstracts using a distributional method with GPT-3.5-turbo-0125 rewrites.
- **Key quote:** "scientists adopting LLMs to draft manuscripts demonstrate a large increase in paper production, ranging from 23.7-89.3%". The effects are 36.2% for arXiv, 52.9% for bioRxiv and 59.8% for SSRN, and largest for authors with Asian names.
- **Second finding:** LLM use "reversed the relationship between writing complexity and paper quality". For LLM-assisted papers, higher Flesch-based complexity predicts *lower* publication odds.
- URL: https://arxiv.org/abs/2601.13187
- **Verdict: SUPPORTED** for LLM-assisted writing and productivity.

## 7b. Jiang et al. 2024 (citations.txt: `jiang2024 doi:10.1016/j.compedu.2024.105070`)
- Jiang, Hao, Fauss & Li, "Detecting ChatGPT-generated essays in a large-scale writing assessment: Is there a bias against non-native English speakers?" *Computers & Education* 217, 105070 (Aug 2024). The abstract was read on ScienceDirect.
- **Key quote:** "our carefully constructed detectors not only achieved near-perfect detection accuracy, but also showed no evidence of bias disadvantaging non-native English speakers."
- **Method:** GRE essays; detectors built on e-rater linguistic features **and text perplexity features**.
- **Important:** the paper finds **no** ESL bias in its own detectors. It is a counterpoint to Liang et al. 2023 ("GPT detectors are biased against non-native English writers"), not support for it. The abstract and highlights say **nothing about data contamination**.
- URL: https://www.sciencedirect.com/science/article/abs/pii/S0360131524000848
- **Verdict:**
  - NOT SUPPORTED if the paper cites Jiang 2024 as showing perplexity detectors are biased against non-native writers.
  - NOT SUPPORTED for any contamination claim.
  - SUPPORTED only as "carefully trained detectors (incl. perplexity features) showed no ESL bias on GRE data".

## 8. Chang 2026 (citations.txt: `chang2026 doi:10.1007/s11192-026-05589-y`)
- Eunsuk Chang, "Human writing and machine patterns: analyzing a decade of convergence", *Scientometrics* 131(3):1635–1654 (online 9 Mar 2026).
- **Quote:** "This study analyzes a decade of human writing (2014–2024) across PubMed, Wikipedia, and Stack Exchange". It finds "human writing has become less linguistically diverse and more machine-predictable over time."
- **Models:** perplexity and Binoculars from OPT-125M, GPT-2 and Llama-3.2, plus sentence length and TTR. "Small LMs" fits OPT-125M and GPT-2. Llama-3.2 size is not stated in the abstract.
- **Predates GenAI:** "This trend predates the widespread adoption of generative AI, suggesting it is not solely due to direct LLM use". The abstract also notes "the recent acceleration of convergence".
- URL: https://link.springer.com/article/10.1007/s11192-026-05589-y (abstract and meta description)
- **Verdict: SUPPORTED** on both points.
