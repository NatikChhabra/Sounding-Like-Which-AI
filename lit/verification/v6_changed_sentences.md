# Citation verification, v6: citing sentences changed since v5

Sources were read on 2026-10-13. This was an AI check; no human checked these citations.

**Baseline.** The v5 verification ended at commit `c1a5193`, the follow-up pass that added `v5_followup.md`. The later commit [pre-rewrite commit] only added `lit/verification/README.md`. Scope is `git diff c1a5193 HEAD -- paper/main.tex paper/references.bib`, and the working tree is clean for `paper/`.

**Method.**
- Every sentence in HEAD `main.tex` that contains `\cite*` and does not appear verbatim in `c1a5193` was extracted. There are 25.
- Wording changes that alter what a sentence claims were re-checked against the source.
- Where only citation order or a few words changed and the claim stayed the same, the v5 evidence still applies. Existence and bibliographic details were re-confirmed for keys whose bib entry changed.
- `\R{}` numbers were checked only where a sentence compares them with a cited figure.

## Changed citing sentences

| # | Key(s) | Sentence excerpt (HEAD) | What changed | Exists | Supports | Evidence | Fix |
|---|---|---|---|---|---|---|---|
| 1 | kobak2025, liang2024monitoring, liang2024mapping, liang2025widespread, brooks2024; yakura2024, anderson2025spoken | "Corpus studies find traces of LLM-assisted writing in abstracts, peer reviews, press releases and encyclopedias ..." | Order of citations only | Y | Y | Unchanged claim; v5 batch1/2/3 SUPPORTED for each. The bib changes (month, ISSN) do not touch identity. | none |
| 2 | clark2021, jakesch2023, casal2023; sadasivan2025, krishna2023, dugan2024raid; liang2023detectors | "Judging individual documents is harder: readers are poor at telling ... detectors can be evaded ..." | "Individual documents are harder" became "Judging individual documents is harder" | Y | Y | Unchanged claim; v5 SUPPORTED. Liang 2023: average FPR on TOEFL essays 61.22%. | none. See the bib note on krishna2023 below. |
| 3 | liang2024mapping, lin2025, brooks2024 | "Prevalence estimators report a small 'LLM share' for it, which studies read as consistent with false positives ..." | "treat as" became "read as"; "it" refers to pre-ChatGPT text | Y | Y | Liang 2024 Sec. 5.1 (re-read): Nov 2022 values "consistent with the false positive rate reported in the earlier section". Lin: subtracts the pre-period rate. Brooks: 1% FPR thresholds. | none |
| 4 | forman2008 | "(1) We define Machine-Style Overlap ..., a classify-and-count quantity (forman2008) ..." | Contribution (3) split; section ref fixed | Y | Y | Forman (DMKD 17(2):164-206, 2008) names "classify and count"; v5 SUPPORTED (term only). | none |
| 5 | kobak2025, holzwarth2026, lee2026; liang2024monitoring, liang2024mapping, liang2025widespread, geng2024; lin2025, brooks2024, sun2025, khan2026 | "Excess-vocabulary methods compare word frequencies with a counterfactual ...; distributional methods ...; classifier- and detector-based studies label documents ..." | Order only | Y | Y | Unchanged; v5 SUPPORTED for each. Lee 2026 (arXiv 2609.07447, re-read) adapts excess vocabulary above the pre-2023 trend. | none, but see #6 |
| 6 | (kobak ... khan2026 by reference) + kusumegi2025 | "**All target the share of text produced with LLM help**; LLM adoption also changes how many papers scientists produce (kusumegi2025)." | New clause characterising every work cited in #5 | Y | **partly** | Kusumegi (Science 390(6779):1240-1243): adopters show "a large increase in paper production" (the abstract's own causal-leaning wording); OK. **Khan 2026** (J. Informetrics 20(4):101869) says its score "captures stylistic similarity to large-language-model outputs rather than confirmed AI usage", so it does *not* target the LLM-help share. Lee 2026's main quantity is excess vocabulary; its prevalence figures are "scenario-dependent" lower bounds (still acceptable). | Narrow it, e.g. "Most target the share of text produced with LLM help (\citet{khan2026} instead treat detector scores as AI-likeness); ...". Or drop khan2026 from "label documents" and cite it near the overlap framing, since it is the closest to an overlap estimand. |
| 7 | chang2026 | "\citet{chang2026} shows that PubMed, Wikipedia and Stack Exchange text became more predictable ..." | "show" became "shows" (single author) | Y | Y | Sole author Eunsuk Chang (Scientometrics 131(3):1635-1654); v5 SUPPORTED. | none |
| 8 | geng2025 | "We also exclude content words from the features, since authors react to publicised markers (geng2025) ..." | Sentence split; claim unchanged | Y | Y | Findings of ACL 2025: "delve" etc. drop after being pointed out; v5 SUPPORTED. | none |
| 9 | padmakumar2024, doshi2024, anderson2024homog; sourati2025 | "Writing or ideating with instruction-tuned models reduces content diversity across users ..., and LLM rewriting compresses stylistic variance ..." | Split from a longer sentence; "Homogenization" became "Homogenisation" | Y | Y | v5 SUPPORTED. Sourati: rewriting homogenises style, variance falls 21-50%. | none |
| 10 | kirk2024, wu2025monoculture; juzek2025 | "Preference tuning reduces output diversity ... and plausibly produces LLM-overused words ..." | Became its own sentence | Y | Y | Kirk: RLHF "significantly reduces output diversity compared to SFT". Juzek: RLHF role consistent but inconclusive, which matches "plausibly". | none |
| 11 | clark2021, jakesch2023, casal2023, gao2023 | "Readers misjudge machine text ...; we collect no human judgements." | Clause added about own study | Y | Y | Unchanged claim; v5 SUPPORTED. | none |
| 12 | katz2023scidata, katz2025hansard | "Australian House of Representatives Hansard ..., up to 150 spoken speeches per month from 2015 to July 2025" | "January 2015" became "2015" | Y | Y | Zenodo 17351233 (v8, 14 Oct 2025, CC BY 4.0) covers House sitting days from 2 March 1998 to 31 July 2025. Sci Data 10:567 covers 1998-2022. | none |
| 13 | dugan2024raid; openai2023gpt4; touvron2023llama2; vicuna15card; zheng2023judging | Table 1 rows and caption: "...release month (year or quarter where only that is documented; ...)" | "Llama-2-70B-chat" renamed "Llama-2-Chat 70B"; Claude moved to its own group; caption parenthetical added | Y | Y / **partly (Qwen3.5)** | GPT-4 cutoff Sep 2021 and Llama 2 cutoff Sep 2022: v5 SUPPORTED. The new caption says a quarter is given only where no month is documented, but the Qwen3.5-9B card's BibTeX gives "month = {February}", year 2026, and v5 had "2026-02/03". | Minor: give Qwen3.5 as 2026-02, or reword the caption, e.g. "quarter where sources disagree on the month". |
| 14 | jiang2023mistral, mistralv03card, llama31card, phi4card, gemma3card, qwen3card, granitecards, openai2025gptoss, qwen35card, gemmareleases, gemma4card | "Other dates: ..." (caption tail) | Cite list unchanged; bib notes reworded | Y | Y | Re-read: gemmareleases lists Gemma 4 12B Unified on 3 June 2026 and Gemma 3 on 10 Mar 2025. gemma4card gives a cutoff of "January 2025". gpt-oss card says "Our model has a knowledge cutoff of June 2024", 8 Aug 2025. Granite 4.2 card: 25 Aug 2026. | none |
| 15 | mccarthy2010 | "MTLD lexical diversity (measure of textual lexical diversity; \citealp{mccarthy2010})" | Expansion of MTLD added; citation form changed | Y | Y | McCarthy & Jarvis 2010 (BRM 42(2):381-392) validate MTLD, "measure of textual lexical diversity". | none |
| 16 | bao2024fastdetectgpt | "The analytic Fast-DetectGPT criterion ..., computed with GPT-2 small, ... larger scoring models, as in the original method, might detect the shift." | New hedge about scoring-model size; "does not rise" became "falls" | Y | Y | Fast-DetectGPT (ICLR 2024, arXiv 2310.05130). Black-box setting uses GPT-J-6B to sample and GPT-Neo-2.7B to score; the largest GPT-2 used is gpt2-xl (1.5B), never GPT-2 small. App. B: analytic solution "almost identical" to sampling. The "falls" numbers are the paper's own (11.3% to 5.3%). | none |
| 17 | liang2024mapping | "... would imply that X% of computer-science and Y% of mathematics abstracts were LLM output in 2024, the ordering that \citet{liang2024mapping} report at lower levels" | Now compares ordering and level and points to the appendix | Y | Y | Implied 42.1% (CS) and 7.8% (math), against Liang's 17.5% and 4.9%, so the ordering is the same and Liang's levels are lower. Liang's unit is sentences; ours is documents. | Optional: add "(of sentences)" so the main text does not read as like-for-like. |
| 18 | liang2023detectors | "A GPT-2 perplexity instrument flags 63.7% of TOEFL essays but 8.0% of US 8th-grade essays, reproducing the bias reported by ..." | Second clause reworded | Y | Y | Liang 2023: TOEFL FPR averaged 61.22% across detectors; 8th-grade essays near-perfectly classified (v5). | none |
| 19 | shumailov2024, gerstgrasser2024 | "Either way, recent LLMs and recent scientific writing can no longer serve as independent references ..., a precondition for the recursive dynamics studied in model-collapse work ... but not evidence of them." | Sentences merged; claim the same | Y | Y | v5 SUPPORTED: Nature 631:755-759 (collapse when data replaced); Gerstgrasser COLM 2024 (accumulation avoids it). | none |
| 20 | katz2025hansard, liang2023detectors | Ethics: "Australian Hansard (Parliament of Australia, CC BY-NC-ND 4.0), through the database of \citet{katz2025hansard} (CC BY 4.0); ... RAID and the Hugging Face release of \citet{liang2023detectors} (MIT)." | Hansard licence changed from CC BY 4.0 to NC-ND plus Katz's CC BY | Y | Y | aph.gov.au copyright page: material provided under "Attribution-NonCommercial-NoDerivs 4.0 International licence". Zenodo record: CC BY 4.0. HF dataset WxWx/ChatGPT-Detector-Bias: MIT. "Hansard text may not be adapted" matches ND. | none. Katz's CC BY sits on top of NC-ND source text, and the paper correctly applies the stricter terms. |
| 21 | liang2023detectors | Appendix A: "the essays of \citet{liang2023detectors} (TOEFL, US 8th-grade and US college) ... used only for out-of-genre checks" | "style check" added | Y | Y | The HF release has TOEFL_real_91 and CollegeEssay_real_70; the 8th-grade (Hewlett ASAP) essays are on the GitHub repo (v5). | none |
| 22 | liang2024mapping | Appendix C: "\citet{liang2024mapping} estimate 17.5% and 4.9% of abstract sentences by February 2024, the same ordering at lower levels." | Moved here from the main text | Y | Y | Sec. 5.1 (re-read): CS "17.5% for abstracts"; mathematics "4.9% for abstracts" "by the end of the studied period" (Feb 2024); "sentences as the unit". | none |
| 23 | padmakumar2024, doshi2024 | Appendix E: "Diversity of content or ideas may behave differently ..." | Split from the preceding sentence | Y | Y | Both report reduced content or idea diversity (v5). | none |
| 24 | liang2023detectors | Appendix F: "The same GPT-2 instrument reproduces the bias reported by ... TOEFL essays by non-native test-takers ..." | Only `GPT-2` became `\gptii{}` | Y | Y | As #18. | none |
| 25 | jiang2024 | "The TOEFL essays are predictable and the PERSUADE learners' essays are not, ... consistent with detectors that showed no bias in a large writing assessment ..." | First clause split off | Y | Y | Jiang et al. (C&E 217:105070): "no evidence of bias disadvantaging non-native English speakers" (v5). | none |

### Changed context around claims with no citation
- Vintage section (main.tex l.363): "cannot have learned" became "unlikely to have learned ... as far as is documented, no recent abstracts". This is more cautious and consistent with touvron2023llama2, vicuna15card and zheng2023judging. OK.
- Vintage section (l.381): "Gemma 4 (12B released in June 2026) ... peaked before their release". This is correct. The Gemma 4 family (E2B, E4B, 26B A4B, 31B) came out on 31 March 2026 and the 12B on 3 June 2026. The 2025Q4 peak predates both, so the claim holds either way.

## Specific facts

| Fact in paper | Primary source | Verdict |
|---|---|---|
| Katz & Alexander database (Zenodo 17351233): CC BY 4.0, coverage 1998-2025, used to July 2025 | zenodo.org/records/17351233: v8, published 14 Oct 2025, licence CC BY 4.0, House of Representatives sitting days from 2 March 1998 to 31 July 2025 | **Correct.** The bib title "(1998--2025)", authors, year and DOI match. |
| Parliament of Australia Hansard licence: CC BY-NC-ND 4.0 | aph.gov.au/Help/Disclaimer_Privacy_Copyright: all material provided under "Attribution-NonCommercial-NoDerivs 4.0 International licence", except the Coat of Arms | **Correct.** Older secondary pages cite 3.0, but the current APH page says 4.0. |
| gpt-oss-20b total parameters; "models of 7 to 21 billion parameters" | arXiv 2508.10925 Sec. 2: "20.9B total and 3.6B active parameters" (Table 1: 20.91B); the HF card says 21B | **Correct.** 21B is the rounded total. |
| Gemma 4 under Apache 2.0 | HF google/gemma-4-12B-it: License apache-2.0. The Gemma releases page's "Gemma 4 license" link goes to ai.google.dev/gemma/apache_2, which reproduces the Apache License 2.0 text | **Correct.** |
| Gemma 4 12B released June 2026 | ai.google.dev/gemma/docs/releases: "Gemma 4 12B Unified", 3 June 2026 | **Correct.** The rest of the Gemma 4 family was released 31 March 2026. |
| Liang et al. 2024: ~17.5% CS and 4.9% math abstract sentences by Feb 2024 | arXiv 2404.01268 Sec. 5.1 | **Correct.** |

Licences of the other "Apache 2.0" models in the Ethics statement were also spot-checked. Qwen3.5-9B, Granite 4.2 8B and gpt-oss are apache-2.0 on their HF cards. Qwen3.5's card BibTeX gives February 2026, which bears on #13.

## Bibliography changes since v5 (`references.bib`)

1. **krishna2023 `url` is broken.** It became `http://dx.doi.org/10.52202/075280--1195` (double hyphen); the `DOI` field is correct. The PDF links the DOI, so the reader does not see the error, but the bib field is wrong. Fix: set it back to `075280-1195`.
2. **ISSN fields changed to `--`** in 20 entries (for example kobak2025 `2375--2548`, liang2023detectors `2666--3899`). ISSNs use a plain hyphen. acl_natbib does not print ISSN, so there is no visible effect, but the data is wrong (forman2008 still has `1573-756X`). Fix: change `--` back to `-` in ISSN fields.
3. The other changes are correct or harmless:
   - Month macros (`jul`, `feb`, ...).
   - `{\H{o}}` in Emőke.
   - "Christopher D. Manning", "Barrett R.", "J. Zico".
   - Title bracing (MT-Bench, Mistral 7B, Gemma).
   - The katz2025hansard `howpublished` URL, which renders once.
   - The Vicuna, Qwen3 and Mistral v0.3 date notes.
   - `gemmareleases` author "Google DeepMind". The page is ai.google.dev; "Google" would be equally fine.

## Summary

25 changed citing sentences were checked, plus 6 specific facts. 4 problems were found: 1 claim, 1 minor table/caption issue and 2 bibliography-data errors. There is 1 optional clarity note. All 6 specific facts are correct.

- #6 (main.tex l.83): "All target the share of text produced with LLM help" overstates khan2026, which says its Binoculars score is AI-likeness, not confirmed AI use. lee2026 gives only scenario-dependent lower bounds. Narrow it to "Most" or single out khan2026.
- #13 (Table 1 caption, Qwen3.5 "2026-Q1"): the caption says a quarter is given only where no month is documented, but the Qwen3.5-9B card gives February 2026. Use 2026-02 or reword the caption.
- Bib krishna2023: the `url` field reads `075280--1195` (broken). Set it back to `075280-1195`. It is not rendered, because the DOI is used.
- Bib ISSN fields (20 entries): `--` was introduced; use a single hyphen. It is not rendered.
- Optional, #17 (main.tex l.321): comparing implied document shares with Liang's sentence shares; add "(of sentences)".
