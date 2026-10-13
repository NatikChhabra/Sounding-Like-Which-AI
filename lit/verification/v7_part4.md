# v7 citation verification, part 4 (18 keys)

Done independently on 2026-10-13 against primary sources. Metadata comes from the Crossref API (DOIs), ACL Anthology, the ICLR proceedings pages and their BibTeX, the NeurIPS proceedings, arXiv abstract pages and PDFs (read with pdftotext), the Hugging Face API (model cards and commit history), the GitHub FastChat README, and the PERSUADE 2.0 GitHub README. Abstracts that were paywalled (science.org, pnas.org, nature.com and ScienceDirect all returned 403) were read through OpenAlex or Semantic Scholar. I read the earlier reports in this folder only after reaching my own verdicts; disagreements are listed at the end.

Verdict scale: SUPPORTED / PARTLY / NOT SUPPORTED. "Bib OK" means title, authors (order and spelling), venue, year, volume, pages and DOI all match the source.

---

## bao2024fastdetectgpt
**Bib status:** OK. The ICLR 2024 proceedings page and its BibTeX match on every field: title, five authors in order, editors, pp. 24814--24836 and URL. The official BibTeX also has `volume = {2024}`, which the entry leaves out (harmless).

**Citing sentences**
1. l.102 "Zero-shot detectors use token-likelihood statistics \citep{hans2024binoculars, bao2024fastdetectgpt}". **SUPPORTED.** The criterion is built from token log-probabilities under a scoring model ("conditional probability curvature").
2. l.306 "Fast-DetectGPT ... with GPT-2 small, a zero-shot detector". **SUPPORTED.** The paper describes it as "an optimized zero-shot detector".
3. l.549 "analytic Fast-DetectGPT criterion ... with GPT-2 small as both sampling and scoring model"; l.555 "The larger scoring models of the original method might do better". **SUPPORTED.** The paper notes the sampling and scoring steps "have an analytical solution" (Appendix B) when the same model does both. The original experiments used GPT-J/Neo-2.7B, which are larger than GPT-2 small.

## casal2023
**Bib status:** OK. Crossref gives Casal, J. Elliott; Kessler, Matt; *Research Methods in Applied Linguistics* 2(3), 100068, Dec 2023; DOI 10.1016/j.rmal.2023.100068.

**Citing sentence:** l.101 "Readers misjudge machine text \citep{clark2021, jakesch2023, casal2023, gao2023}". **SUPPORTED.** The 72 linguist reviewers judging abstracts had an overall positive identification rate of 38.9%. The source page itself was paywalled, so this figure comes from the University of Memphis release and secondary reports of the paper.

## crossley2024persuade
**Bib status:** OK. Crossref gives Crossley, Tian, Baffour, Franklin, Benner, Boser; *Assessing Writing* 61, 100865, Jul 2024; DOI 10.1016/j.asw.2024.100865.

**Citing sentence:** l.159 "PERSUADE 2.0 ..., pre-ChatGPT essays by US students in grades 6--12 on N prompts, with English-language-learner (ELL) status and a holistic score". **SUPPORTED.**
- The abstract says the essays were "produced by 6th-12th grade students in the United States" (15 prompts).
- The GitHub README says version 2.0 adds "holistic essay scores".
- ELL status: the abstract only says "detailed individual and demographic information". The `ell_status` field is confirmed by the released CSV schema that `code/build_sources.py` reads, not by the article text I could access.
- Licence (stated at l.453 without a citation): the README says "CC BY-NC-SA 4.0 ... Attribution-NonCommercial-ShareAlike 4.0 International". This matches.

## gao2023
**Bib status:** OK. Crossref gives 7 authors in the bib's order; *npj Digital Medicine* 6(1), article 75, online 26 Apr 2023; DOI 10.1038/s41746-023-00819-6.

**Citing sentence:** l.101 "Readers misjudge machine text". **SUPPORTED, with a nuance.** Blinded reviewers "correctly identified 68% of generated abstracts" and wrongly flagged 14% of the originals, and called the task "surprisingly difficult". So they made frequent errors in both directions but did better than chance. "Misjudge" fits this; "cannot detect" would not. No change needed.

## geng2024
**Bib status:** OK. arXiv:2404.08627 is "Is ChatGPT Transforming Academics' Writing Style?" by Mingmeng Geng and Roberto Trotta; v1 is from Apr 2024 and v2 from Nov 2024. arXiv lists no journal-ref, and I found no journal version; a same-title listing exists on icml.cc for 2024.

**Citing sentence:** l.80 "distributional methods fit a mixture of human and LLM word distributions \citep{liang2024monitoring, liang2024mapping, liang2025widespread, geng2024}". **SUPPORTED.** Their Eq. 3 writes the observed word frequency as (1-η)·f + η·f(r+1), where η is the share of LLM-processed abstracts. The model is "calibrated and validated on a mixture of real abstracts and ChatGPT-modified abstracts".

## gray2024
**Bib status:** OK. arXiv:2403.16887 is a single-author paper by Andrew Gray, v1 only (25 Mar 2024), with no journal-ref. The bib title is a title-cased form of 'ChatGPT "contamination": estimating the prevalence of LLMs in the scholarly literature'; this is acceptable.

**Citing sentence:** l.250--252, the marker-word list (delve, underscore, showcase, meticulous, intricate, intricacies, commendable, boast), cited jointly as \citealp{kobak2025, gray2024, yakura2024}. **SUPPORTED as a joint citation.**
- Gray's test list (12 adjectives, 12 adverbs) contains **commendable, meticulous, intricate** (plus meticulously).
- It does *not* contain delve, underscore, showcase, intricacies or boast. Those come from the other two sources (see kobak2025).

## jakesch2023
**Bib status:** OK. Crossref gives Jakesch, Hancock, Naaman; PNAS 120(11), e2208839120, 2023 (online 7 Mar, print 14 Mar); DOI 10.1073/pnas.2208839120.

**Citing sentence:** l.101 "Readers misjudge machine text". **SUPPORTED.** Participants (N = 4,600) "were unable to detect self-presentations generated by" AI.

## katz2023scidata
**Bib status:** OK. Crossref gives Katz, Lindsay; Alexander, Rohan; "Digitization of the Australian Parliamentary Debates, 1998–2022"; *Scientific Data* 10(1), article 567, 2023; DOI 10.1038/s41597-023-02464-w.

**Citing sentence:** l.157 "Australian House of Representatives Hansard \citep{katz2023scidata, katz2025hansard}, ... from 2015 to July 2025". **SUPPORTED as a joint citation.** The 2023 paper is the source of the database ("proceedings of the Australian parliamentary debates from 1998 to 2022"). Coverage of 2023 to July 2025 depends on katz2025hansard, which is cited alongside, so this is fine.

## kobak2025
**Bib status:** OK. Crossref gives Kobak, González-Márquez, Horvát, Lause; *Science Advances* 11(27), eadt3813, 4 Jul 2025; DOI 10.1126/sciadv.adt3813. The arXiv version is 2406.07016.

**Citing sentences**
1. l.48 "Corpus studies find traces of LLM-assisted writing in abstracts, peer reviews, press releases and encyclopedias". **SUPPORTED.** The paper studies more than 15M PubMed abstracts from 2010 to 2024.
2. l.79 "Excess-vocabulary methods compare word frequencies with a counterfactual extrapolated from pre-LLM years". **SUPPORTED.** The figures show "counterfactual extrapolations", and the counterfactual frequency is projected from the two preceding years.
3. l.252, the marker words. **SUPPORTED jointly.** Kobak's excess-word material contains delves/delve, underscores/underscore, showcasing, intricate, intricacies, meticulously/meticulous and commendable. The last three appear in the appendix list of excess words.
   - **boast** is not in Kobak or Gray. It is in yakura2024, which is cited in the same parenthesis and lists "delve, showcase, boast, intricacies and meticulous" in its abstract.
   - So every one of the eight words is covered by at least one of the three cited sources.

## li2024mage
**Bib status:** OK. ACL Anthology and Crossref give 9 authors in order, editors Ku/Martins/Srikumar, ACL 2024 (Volume 1: Long Papers), pp. 36--53; DOI 10.18653/v1/2024.acl-long.3.

**Citing sentence:** l.105--106 "Detectors transfer unevenly to unseen generators \citep{pu2023zeroshot, li2024mage}". **SUPPORTED.** Detectors struggle "particularly in out-of-distribution scenarios", meaning unseen models and domains. The best detector still reaches 84.12% on out-of-domain text from a new LLM, which fits "unevenly".

## liang2025widespread
**Bib status:** OK. Crossref gives Liang, Zhang, Codreanu, Wang, Cao, Zou; *Patterns* 6(12), 101366, Dec 2025; DOI 10.1016/j.patter.2025.101366.

**Citing sentences**
1. l.48 "traces ... in ... press releases". **SUPPORTED.** The paper covers corporate and UN press releases, consumer complaints and job postings.
2. l.80 "distributional methods fit a mixture of human and LLM word distributions". **SUPPORTED.** It uses the population-level framework of liang2024monitoring and fits word frequencies of pre-ChatGPT and LLM-modified corpora.

## mistralv03card
**Bib status:** OK for a model-card entry. The URL resolves. The Hugging Face API gives repo `createdAt` 2024-05-22, which supports the bib note "May 2024".

**Citing sentence:** Table 1 caption l.212 "Other dates: \citet{..., mistralv03card, ...}". The row reads "Mistral 7B Instruct v0.3 | 2024-05 | (no cutoff)". **SUPPORTED.**
- Release month: the first commit is dated 22 May 2024.
- No cutoff: the card states no training-data cutoff, so leaving the cell blank is correct.
- Licence: the card says Apache-2.0, matching l.453 ("Apache 2.0 for the others").
- Training details on the card: it is an instruct fine-tune of Mistral-7B-v0.3 with vocabulary extended to 32768, the v3 tokenizer and function calling. The paper claims nothing beyond this.

## padmakumar2024
**Bib status:** OK. The ICLR 2024 proceedings BibTeX gives Padmakumar, Vishakh and He, He, pp. 642--669, the same editors and the same URL. Only `volume = {2024}` is missing (harmless).

**Citing sentences**
1. l.88 "Writing or ideating with instruction-tuned models reduces content diversity across users". **SUPPORTED.** Writing with InstructGPT "(but not the GPT3)" reduced diversity and "increases the similarity between the writings of different authors". "Instruction-tuned" is the right qualifier.
2. l.633 "Diversity of content or ideas may behave differently". **SUPPORTED.** The paper measures content and lexical diversity, not syntactic style.

## pu2023zeroshot
**Bib status:** OK. ACL Anthology and Crossref give Pu, Zhang, Han, Tsvetkov, He; Findings of EMNLP 2023, pp. 4799--4808; editors Bouamor/Pino/Bali; DOI 10.18653/v1/2023.findings-emnlp.318.

**Citing sentence:** l.105--106 "Detectors transfer unevenly to unseen generators". **SUPPORTED.** The abstract says "none of the detectors can generalize to all generators", although some transfer from medium to larger models works.

## reinhart2025
**Bib status:** OK. Crossref gives 7 authors in order (Reinhart, Markey, Laudenbach, Pantusen, Yurko, Weinberg, Brown); PNAS 122(8), e2422455122, 2025 (online 18 Feb); DOI 10.1073/pnas.2422455122.

**Citing sentence:** l.94 "LLM text differs systematically from human text in lexico-grammatical features". **SUPPORTED.** Using Biber's lexical, grammatical and rhetorical features, the authors "identify systematic differences between LLMs and humans".

## sourati2025
**Bib status:** OK for an online-first article, with one cosmetic issue.
- Crossref gives "The shrinking landscape of linguistic diversity in the age of large language models", *Nature Human Behaviour*, published online 24 Aug 2026, with 10 authors matching the bib (including "Tak, Ala N."). It has no volume or pages yet; DOI 10.1038/s41562-026-02550-0.
- The bib has year 2026, which is correct, so the rendered citation reads "Sourati et al., 2026". The key name `sourati2025` reflects the arXiv v1 date (2502.11266, Feb 2025). This has no visible effect.
- Optional: add volume and pages once the article is assigned to an issue.

**Citing sentence:** l.88 "LLM rewriting compresses stylistic variance". **SUPPORTED.** LLMs "homogenize writing styles, reducing writing-complexity variance by" 21 to 50% (arXiv v2 abstract, which matches the published version).

## vicuna15card
**Bib status:** OK. The URL resolves. The card lists the "Llama 2 Community License Agreement" and says the model is fine-tuned from Llama 2 on "around 125K conversations collected from ShareGPT.com". The bib note's release month (Aug 2023, from FastChat) matches the FastChat README news item "[2023/08] We released Vicuna v1.5 based on Llama 2".
- Minor: the Hugging Face weights were first uploaded on 29 Jul 2023 (commit history), but the public announcement is August 2023. "2023-08" is defensible as a release month; no change needed.

**Citing sentence:** Table 1 footnote d, l.210 "fine-tuned from Llama 2 \citep{vicuna15card}". **SUPPORTED.**
- The table row "2023-08" is supported via the bib note and FastChat.
- The cutoff "Sep 2022" is attributed to touvron2023llama2, not this card.
- Licence at l.453 ("Llama 2 ... licence ... also covering Vicuna") matches the card.

## zheng2023judging
**Bib status:** OK. Crossref (DOI 10.52202/075280-2020) gives *Advances in Neural Information Processing Systems 36*, pp. 46595--46623, with the 13 authors in the bib's order. The URL is the NeurIPS Datasets and Benchmarks track PDF, which resolves.

**Citing sentence:** Table 1 footnote d, l.211 "with the Vicuna recipe of training on user-shared ChatGPT conversations". **SUPPORTED.** Appendix E (present in the NeurIPS PDF and in arXiv v4) says "Vicuna is created by fine-tuning a LLaMA base model using user-shared conversations gathered from ShareGPT.com". The footnote correctly attributes the Llama 2 base to the card and the recipe to this paper.

---

## Summary
- Keys checked: 18.
- Fully OK (bib correct and every citing sentence SUPPORTED): 18.
- No NOT SUPPORTED or PARTLY verdicts.

Notes; none needs a change:
- sourati2025: the key says 2025 but the bib year is 2026, which is correct. The article is online-first with no volume or pages yet; add them when assigned.
- gray2024: on its own it supports only commendable, meticulous and intricate. The other five marker words rest on kobak2025 and yakura2024 (boast on yakura2024 only). The joint citation covers all eight.
- crossley2024persuade: the article abstract does not name ELL status explicitly ("detailed individual and demographic information"). The field exists in the released data (`ell_status`).
- vicuna15card: the weights were uploaded 29 Jul 2023 and announced in Aug 2023; "2023-08" is fine.
- bao2024fastdetectgpt and padmakumar2024: the official BibTeX has `volume = {2024}`, which the bib omits (cosmetic).

## Disagreements with earlier reports
- v5_batch3 marked zheng2023judging PARTLY and wanted the NeurIPS version. Both issues are fixed in the current text: footnote d now splits the Llama 2 base (card) from the recipe (Zheng), and the bib is NeurIPS 2023. No disagreement remains.
- v5_followup flagged the Vicuna release month as uncited. The current bib note now cites FastChat, which resolves this.
- v6 flagged ISSNs written as `--`. In the current bib, the entries for my keys use single hyphens (e.g. kobak2025 `2375-2548`), so this is fixed for these keys.
