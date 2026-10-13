# Citation verification v7, part 2 (18 keys)

Independent check made on 2026-10-13 against `paper/main.tex` and `paper/references.bib`. Earlier reports were read only after the verdicts below were formed; disagreements are listed at the end.

Sources used: Crossref API (all DOIs), the ACL Anthology `.bib` file, arXiv abstract and HTML pages, PMLR metadata, the COLM 2024 accepted-papers list (OpenReview was behind a bot challenge, so it was not used), Hugging Face cards with the HF API, Google's Gemma release log and launch blog, the Qwen3 blog, the Llama 3.1 MODEL_CARD.md, ScienceDirect abstract pages (read in a browser because WebFetch got a 403), Springer meta tags, OpenAlex abstracts, the GPT-4 report PDF (v6), and OpenAI's model pages.

Verdicts: SUPPORTED / PARTLY / NOT SUPPORTED. "Bib OK" means title, authors (order and spelling), venue, year, volume, pages and DOI all match the source.

---

## anderson2025spoken
**Bib:** OK. Crossref for 10.1609/aies.v8i1.36540 gives the same title, the authors Anderson, Galpin and Juzek in that order, AIES vol. 8 no. 1, pp. 179-191, online 15 Oct 2025.
- l.49 "LLM-associated words have become more frequent in unscripted speech": **SUPPORTED.** The source built a corpus of "unscripted spoken language drawn from conversational science and technology podcasts" (22.1M words) and found a "moderate yet significant increase" after 2022.
- l.89 "LLM-associated vocabulary has grown in human speech": **SUPPORTED.** Same evidence.

## berbersardinha2024
**Bib:** OK. Crossref gives Applied Corpus Linguistics 4(1), article 100083, April 2024, sole author Tony Berber Sardinha.
- l.95 "LLM text differs systematically from human text in lexico-grammatical features": **SUPPORTED.** The study compares texts on Biber's (1988) five dimensions, which are lexico-grammatical, and reports "significant disparities between AI-generated and human-authored texts".

## chang2026
**Bib:** OK. Crossref gives Scientometrics 131(3):1635-1654, sole author Eunsuk Chang, online 9 Mar 2026, print March 2026. Crossref sets the title in sentence case; the bib's title case is fine.
- l.83 "PubMed, Wikipedia and Stack Exchange text became more predictable to small language models over 2014-2024, a trend that began before generative AI": **SUPPORTED.** The abstract (Springer meta tag) covers 2014-2024 on those three corpora, uses OPT-125M, GPT-2 and Llama-3.2, finds text "more machine-predictable over time", and says "This trend predates the widespread adoption of generative AI".

## dugan2024raid
**Bib:** OK. The ACL Anthology bib and Crossref both give the author order Dugan, Hwang, Trhlík, Zhu, Ludan, Xu, Ippolito, Callison-Burch, plus ACL 2024 Vol. 1, pp. 12463-12492 and DOI 10.18653/v1/2024.acl-long.674. The arXiv version swaps Zhu and Ludan; the bib correctly follows the ACL version.
- l.101 "detectors can be evaded": **SUPPORTED.** The abstract says "current detectors are easily fooled by adversarial attacks".
- l.170-171 "RAID generations without adversarial attack, written from titles of arXiv papers by six 2023 chat models": **SUPPORTED.**
  - RAID's chat prompt for this domain is "Write the abstract for the academic paper titled "{title}"", and the source is an arXiv-abstracts dataset.
  - RAID has exactly six chat generators (App. E.2, Table 10): gpt-4-0613, gpt-3.5-turbo-0613, Llama-2-70b-chat-hf, Mistral-7B-Instruct-v0.1, mpt-30b-chat, and Cohere `command` called through co.chat().
  - Generation ran 1-15 Nov 2023 (App. E.6).
  - RAID also has a no-attack subset.
- Table 1 RAID rows (l.182-187): **SUPPORTED, with two nits.**
  - The model IDs match Table 10 of the source.
  - "Cohere command" is RAID's `command` through the chat endpoint. Optional fix: "Cohere command (chat)".
  - "Released 2023" for Cohere's model means the snapshot queried in Nov 2023. Command itself first appeared in late 2022 as a beta, so "2023" is a snapshot year, not a launch year. This is acceptable.
  - RAID mixes four decoding settings (greedy or sampling, each with or without a repetition penalty). l.437 already says RAID decoding is not held fixed.

## gemma4card
**Bib:** OK (an HF card; the URL resolves). Optional: the card calls the model "Gemma 4 12B Unified", so the title could be "Gemma 4 12B (Unified) Model Card".
- Table 1, l.204, "Gemma 4 12B | 2026-06 | Jan 2025" (cited with gemmareleases at l.212-213): **SUPPORTED.**
  - The card states a pretraining dataset "with a cutoff date of January 2025".
  - Parameters: 11.95B total.
  - Licence: Apache 2.0, which matches l.453.
  - The card gives no release date. Google's release log gives "June 3, 2026: Release of Gemma 4 12B Unified", and the launch blog's published_time is 2026-06-03. The HF repo was created 2026-05-23, before the public release. So 2026-06 is right, sourced through `gemmareleases`.
- Note for authors (not a citation error): a 2026 release with a January 2025 pretraining cutoff cannot have learned 2025-2026 writing in pretraining. Only post-training data could be newer. This bears on the l.428 suggestion that the 2026 models "may have learned from recent writing". Consider adding: "(Gemma 4's stated pretraining cutoff is January 2025)".

## gerstgrasser2024
**Bib:** OK. The COLM 2024 accepted-papers list gives the same 14 authors in the bib's order (Korbak, Sleight, Agrawal, Hughes, "Dhruv Bhandarkar Pai", "Dan Roberts"). arXiv v2 orders some middle authors differently; the bib correctly follows the COLM version.
- l.428 "a precondition for the recursive dynamics studied in model-collapse work ... but not evidence of them": **SUPPORTED.** The paper studies recursive training on generated data: replacing real data "tend[s] towards model collapse", while accumulating data avoids it. The paper's hedged wording claims nothing more.

## herbold2023
**Bib:** OK. Crossref gives Sci. Rep. 13, article 18617, 30 Oct 2023, authors Herbold, Hautli-Janisz, Heuer, Kikteva, Trautsch in that order.
- l.95 (same sentence as berbersardinha2024): **SUPPORTED.** The abstract says ChatGPT's style "exhibits linguistic characteristics that are different from those of the human-written essays". The features measured are lexical diversity, syntactic complexity, nominalisations, modals, epistemic and discourse markers.

## jiang2024
**Bib:** OK. Crossref gives Computers & Education 217, article 105070, Aug 2024, authors Jiang, Hao, Fauss, Li in that order.
- l.104 "detectors trained on a large writing assessment showed no such bias": **SUPPORTED.** The detectors were built on GRE data from e-rater and perplexity features. The abstract reports "no evidence of bias disadvantaging non-native English speakers".
- l.655 "consistent with detectors that showed no bias in a large writing assessment": **SUPPORTED.** Same evidence.

## khan2026
**Bib:** OK. Crossref gives J. Informetrics 20(4), article 101869, Dec 2026, authors Farhan Kamrul Khan, Ibrahim, AlDahoul, Rahwan, Zaki. OpenAlex lists the first author as "Fahad Khan", which looks like an OpenAlex disambiguation error; Crossref agrees with the bib.
- l.81 "classifier- and detector-based studies label documents": **SUPPORTED.** The study scores about 230k Scopus CS articles with Binoculars, plus a binary classification.
- The next sentence, "Most target the share of text produced with LLM help", is hedged with "Most" and so is acceptable. Khan itself is an exception: its score "captures stylistic similarity to large-language-model outputs rather than confirmed AI usage". That makes Khan arguably the cited work closest to the paper's overlap estimand. Optional: add "(\citet{khan2026} instead read detector scores as AI-likeness)".

## kusumegi2025
**Bib:** OK. Crossref gives Science 390(6779):1240-1243, 18 Dec 2025, authors Kusumegi, Yang, Ginsparg, de Vaan, Stuart, Yin in that order.
- l.81 "LLM adoption also changes how many papers scientists produce": **SUPPORTED.** The abstract (arXiv 2601.13187) says adopters show "a large increase in paper production", 23.7-89.3% depending on field and background. Optional: "increases" is more specific than "changes".

## liang2024mapping
**Bib:** OK. COLM 2024: the accepted-papers list gives the same 14 authors in the same order. The arXiv 2404.01268 author list also matches.
- l.48 "traces of LLM-assisted writing in abstracts ...": **SUPPORTED.**
- l.55 "Prevalence estimators report a small LLM share for [pre-ChatGPT text], which studies read as consistent with false positives": **SUPPORTED.** The November 2022 estimates (CS 2.3%, math 2.4%) are described as "consistent with the false positive rate"; the paper also reports "consistently low false positives estimates of α in 2022".
- l.80 "distributional methods fit a mixture of human and LLM word distributions": **SUPPORTED.**
- l.315 "the ordering that \citet{liang2024mapping} report at lower levels": **SUPPORTED.** This paper's implied shares (`numbers.tex`) are CS 42.1% and math 7.8%. Liang reports CS 17.5% and math 4.9%. Same ordering, lower levels.
- l.602 "17.5% and 4.9% of abstract sentences by February 2024": **SUPPORTED.** Both are abstract-sentence fractions; the data run Jan 2020 to Feb 2024. For introductions the figures are 15.3-15.5% (CS) and 3.5-3.9% (math), which the paper does not use.

## llama31card
**Bib:** OK (the GitHub MODEL_CARD.md resolves).
- Table 1, "Llama 3.1 8B | 2024-07 | Dec 2023": **SUPPORTED.** The card gives "Model Release Date: July 23, 2024", "The pretraining data has a cutoff of December 2023", the 8B size, and the Llama 3.1 Community License (matches l.453).

## openai2023gpt4
**Bib:** OK (arXiv 2303.08774, OpenAI, 2023).
- Table 1 footnote a, "GPT-4 (gpt-4-0613) | 2023 | Sep 2021": **PARTLY.**
  - Report §5 says GPT-4 lacks knowledge of events after "the vast majority of its pre-training data cuts off in September 2021". Footnote 10 adds that pre- and post-training data "contain a small amount of more recent data".
  - The report describes the March 2023 model, not the 0613 snapshot.
  - **New conflict:** OpenAI's current official model page for GPT-4 (developers.openai.com/api/docs/models/gpt-4), which lists the snapshots gpt-4-0613 and gpt-4-0314, now gives "Dec 01, 2023 knowledge cutoff". That date is implausible for a June 2023 snapshot and probably describes the `gpt-4` alias generically, but a reviewer could find it.
  - Because GPT-4 is one of the four generators in the pre-ChatGPT-data region, the hedge matters.
  - Copy-ready fix for the caption: "$^a$\citet{openai2023gpt4}, for the vast majority of pretraining data (a small amount is more recent; OpenAI's current model page gives a later date for the \texttt{gpt-4} family)".
  - At minimum, write "Sep 2021 (most data)".

## phi4card
**Bib:** OK. Optional: also cite the Phi-4 technical report, arXiv 2412.08905.
- Table 1, "Phi-4 14B | 2024-12 | Jun 2024": **SUPPORTED.** The card gives "14B parameters", "Release date: December 12, 2024", "cutoff dates of June 2024 and earlier for publicly available data", and licence MIT (matches l.453). The HF repo was created 2024-12-11.

## qwen3card
**Bib:** OK. Its note sources the month from the Qwen3 blog.
- Table 1, "Qwen3 8B | 2025-04 | (no cutoff)": **SUPPORTED (by the bib note).**
  - The HF card states no date, so the month comes from the Qwen3 blog, dated 29 Apr 2025. The HF repo was created 2025-04-27.
  - Parameters: 8.2B. Licence: Apache 2.0 (matches l.453).
  - The card states no cutoff, so the blank cell is correct.

## shaib2024
**Bib:** OK. The ACL Anthology and Crossref give EMNLP 2024 pp. 6416-6431, authors Shaib, Elazar, Li, "Wallace, Byron C".
- l.95 "recurring part-of-speech templates": **SUPPORTED.** The paper defines templates as POS strings and finds that models "produce templated text ... at a higher rate than ... human-reference texts".

## sun2025idiosyncrasies
**Bib:** OK. PMLR v267 sun25z gives pp. 57854-57885 and authors Sun, Yin, Xu, Kolter, Liu.
- l.106-107 "individual models have distinctive, identifiable output patterns": **SUPPORTED.** The paper reports 97.1% accuracy on five-way source-LLM classification.

## yakura2024
**Bib:** OK for the version cited. Title and the 10 authors in order match arXiv 2409.01754. v4 is dated 16 Jul 2026, so year=2026 is consistent with eprint `2409.01754v4`. No journal version was found.
- l.49 "LLM-associated words have become more frequent in unscripted speech": **SUPPORTED.** v4 analyses 737k hours from 824k podcast episodes "screened for unscripted speech" and reports abrupt rises in words such as delve, showcase and meticulous.
  - Earlier versions (v1-v3) also used YouTube academic talks. The citation pins v4, so this is fine.
- l.89 "LLM-associated vocabulary has grown in human speech": **SUPPORTED.**
- l.252 marker-word list (delve, underscore, showcase, meticulous, intricate, intricacies, commendable, boast), cited jointly with kobak2025 and gray2024: **SUPPORTED as a joint citation.**
  - Yakura v4 contains delve, underscore, showcase, meticulous, intricacies and boast. It does not use "intricate" or "commendable"; those must come from kobak2025 or gray2024, which were not checked here.
  - Yakura v4 also reports that "delve" later fell back and that "underscore" declined. This does not affect a list citation.

---

## Related observation outside my keys (Table 1, RAID block)
Footnote c says ChatGPT's cutoff is "reported only in secondary sources". OpenAI's own model page for gpt-3.5-turbo (developers.openai.com/api/docs/models/gpt-3.5-turbo) states "Sep 01, 2021 knowledge cutoff". The 0613 snapshot is not listed there; the page lists 0125, 1106 and instruct.
- Copy-ready fix: "$^c$stated by OpenAI for the current \texttt{gpt-3.5-turbo} snapshots, not for 0613, so ChatGPT enters the pre-ChatGPT-data region only as a sensitivity check".

## Disagreements with earlier reports
- **openai2023gpt4:** v5_batch3 and v5_followup marked this SUPPORTED with no fix needed. I mark it PARTLY because of the "vast majority" and footnote-10 hedge and the conflicting "Dec 01, 2023" on OpenAI's current GPT-4 model page, which no earlier report noted.
- **Footnote c:** v5_followup accepted "secondary sources". OpenAI's gpt-3.5-turbo page is a primary statement of Sep 2021, though not for 0613.
- **khan2026:** v6 flagged "All target the share ..." as PARTLY. The text now reads "Most", which resolves it. I agree with that resolution.
- **gemma4card, qwen3card:** I agree with v5 (the card has no date; the month is confirmed by the release log or blog). For Qwen3 the bib note now covers this.
