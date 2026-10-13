# Citation verification v7, part 1 (18 keys)

I checked these from scratch against primary sources: Crossref for every DOI, the arXiv API and PDFs, ACL Anthology, PMLR, ICLR proceedings (BibTeX), Europe PMC, Zenodo (DataCite CSL), the Hugging Face model API and cards, and ai.google.dev. OpenReview was blocked by a bot challenge, so I took the TMLR metadata from mlanthology.org. I read the earlier verification reports only after reaching my own verdicts; disagreements are listed at the end.

Line numbers refer to paper/main.tex as it stands on 2026-10-13.

## Summary

| Key | Bib | Claims | Action |
|---|---|---|---|
| anderson2024homog | OK | SUPPORTED | none |
| bentley2026 | OK | SUPPORTED | none |
| chakraborty2024 | OK | SUPPORTED | none |
| doshi2024 | OK | SUPPORTED (x2) | none |
| gemma3card | OK | SUPPORTED | none |
| geng2025 | OK | PARTLY (hedging, x2) | optional rewording |
| hans2024binoculars | OK | SUPPORTED | none |
| jiang2023mistral | OK | SUPPORTED | none |
| katz2025hansard | OK | SUPPORTED (x2) | none |
| krishna2023 | OK | SUPPORTED | none |
| liang2023detectors | OK | SUPPORTED (x5) | none |
| lin2025 | **author name wrong** | SUPPORTED (x3) | **fix bib** |
| munozortiz2024 | OK | SUPPORTED | none |
| park2026 | OK | SUPPORTED | none |
| qwen35card | OK | **PARTLY: release month** | **fix Table 1** |
| sadasivan2025 | minor (title case) | SUPPORTED | optional |
| sun2025 | OK | SUPPORTED | none |
| wu2025monoculture | OK | SUPPORTED | none |

---

## anderson2024homog
**Bib:** Matches Crossref (10.1145/3635636.3656204): "Homogenization Effects of Large Language Models on Human Creative Ideation"; Anderson, Barrett R.; Shah, Jash Hemant; Kreminski, Max; Creativity and Cognition (C&C '24), ACM, pp. 413-425, 23 June 2024. OK.

- **l.88** "Writing or ideating with instruction-tuned models reduces content diversity across users": **SUPPORTED.** Participants ideated with ChatGPT or with Oblique Strategies, and at group level the ChatGPT users' ideas were less diverse. Evidence: "different users tended to produce less semantically distinct ideas with ChatGPT" (arXiv 2402.01536 abstract).

## bentley2026
**Bib:** Matches arXiv 2606.27052v1 (25 Jun 2026): the title (with "Human--LLM") and the six authors (Bentley, Vidiella, Ruck, Dutta, Li, Valverde) in order. OK.

- **l.81** "track a composite LLM-associated style index alongside vocabulary-complexity measures in arXiv abstracts": **SUPPORTED.** Evidence: "a sharp increase in a composite LLM-associated style index after early 2023". The complexity metrics are vocabulary size and the Heaps and Zipf exponents, measured on millions of arXiv abstracts from 2010 to 2025.

## chakraborty2024
**Bib:** Matches PMLR v235 (chakraborty24a): the title with the "Position:" prefix, the six authors in order, pp. 6093-6115, ICML 2024. OK.

- **l.103** "detection needs more text as machine and human distributions converge": **SUPPORTED.** Evidence: detection "becomes harder as it nears human quality" but "remains possible with adequate text data". The paper derives sample-complexity bounds by sample size or sequence length.

## doshi2024
**Bib:** Matches Crossref and Europe PMC: Science Advances 10(28), eadn5290, 12 July 2024, Doshi & Hauser, DOI 10.1126/sciadv.adn5290. OK.

- **l.88** (with padmakumar2024 and anderson2024homog), on reduced content diversity across users: **SUPPORTED.** Evidence: "generative AI-enabled stories are more similar to each other". Writers received story ideas from an LLM.
- **l.633** "Diversity of content or ideas may behave differently": **SUPPORTED.** The finding concerns story content and novelty, not style.

## gemma3card
**Bib:** The card page is "Gemma 3 model card" by Google DeepMind at ai.google.dev/gemma/docs/core/model_card_3 (last updated 2025-08-14). Its suggested citation is "Gemma 3", Gemma Team, 2025, but the misc entry is acceptable. OK.

- **Table 1 (l.193 and the caption at l.212)**, "Gemma 3 12B, 2025-03, cutoff Aug 2024": **SUPPORTED.**
  - Cutoff: the card says "The knowledge cutoff date for the training data was August 2024."
  - Size: a 12B size exists; the HF safetensors count is 12.19B.
  - Release month: the card itself gives no date. The HF repo google/gemma-3-12b-it was created 1 Mar 2025, and Gemma 3 launched in March 2025 (the caption also cites gemmareleases). 2025-03 is correct.
- **l.453** "Gemma Terms of Use for Gemma 3": **SUPPORTED.** The card links to the Gemma Terms of Use, and the HF licence tag is `gemma`.

## geng2025
**Bib:** Matches Crossref and ACL Anthology: "Human-LLM Coevolution: Evidence from Academic Writing", Geng & Trotta, Findings of ACL 2025, pp. 12689-12696, DOI 10.18653/v1/2025.findings-acl.657. OK.

- **l.85** "since authors react to publicised markers": **PARTLY (hedging).** The drop in "delve" etc. began "soon after they were pointed out in early 2024". The authors present the adaptation only as a suggestion: "These phenomena suggest that some authors ... have adapted". The paper states it as fact and of authors in general.
- **l.90** "academic authors adapt their LLM use once overused words are publicised": **PARTLY**, for the same reason. The content matches; only the certainty and scope are stronger than the source's.
- **Copy-ready fixes:**
  - l.85: "...since some authors appear to react to publicised markers \citep{geng2025}..."
  - l.90: "...some academic authors appear to adapt their LLM use once overused words are publicised \citep{geng2025}..."

  This is low priority. Many readers would accept the current wording as a fair summary.

## hans2024binoculars
**Bib:** Matches PMLR v235 (hans24a): the title, the eight authors in order, pp. 17519-17537. OK.

- **l.102** "Zero-shot detectors use token-likelihood statistics": **SUPPORTED.** Binoculars is zero-shot, and its score is a ratio of log-perplexity to cross-perplexity. Evidence: "we look at the ratio of perplexity to cross-perplexity" (arXiv 2401.12070 HTML).

## jiang2023mistral
**Bib:** Matches arXiv 2310.06825v1 (10 Oct 2023): title "Mistral 7B", the 18 authors in the same order with the same spelling (including Lélio Renard Lavaud and Timothée Lacroix). OK.

- **Table 1 caption (l.212)**, "Other dates" source for "Mistral-7B-Instr. v0.1, 2023": **SUPPORTED.** The paper introduces "Mistral 7B v0.1" and "Mistral 7B -- Instruct" in 2023. The HF repo mistralai/Mistral-7B-Instruct-v0.1 was created 27 Sep 2023 under Apache 2.0, with 7.24B parameters.

## katz2025hansard
**Bib:** Matches the DataCite record for 10.5281/zenodo.17351233: "A new, comprehensive database of all proceedings of the Australian Parliamentary Debates (1998-2025)", Katz, Lindsay; Alexander, Rohan; Zenodo dataset, 14 Oct 2025. OK.

- **l.157** "Australian House of Representatives Hansard ..., 2015 to July 2025": **SUPPORTED.** The record covers House of Representatives sitting days "from 02 March 1998 to 31 July 2025".
- **l.453** "through the database of \citet{katz2025hansard} (CC BY 4.0)": **SUPPORTED.** The record's licence is "Creative Commons Attribution 4.0 International".

## krishna2023
**Bib:** Matches Crossref (10.52202/075280-1195): the title, the five authors in order (Krishna, Song, Karpinska, Wieting, Iyyer), NeurIPS 36, pp. 27469-27500, 2023. OK.

- **l.101** "detectors can be evaded": **SUPPORTED.** Evidence (title): "Paraphrasing evades detectors of AI-generated text". The DIPPER paraphraser drives detection rates of several detectors close to zero.

## liang2023detectors
**Bib:** Matches Crossref (10.1016/j.patter.2023.100779): Patterns 4(7), 100779, July 2023; Liang, Yuksekgonul, Mao, Wu, Zou. OK.

- **l.103** "Off-the-shelf detectors have flagged non-native writing": **SUPPORTED.** Seven detectors "misclassified over half of the TOEFL essays as 'AI-generated'" (average false-positive rate 61.22%).
- **l.422 and l.649**, the GPT-2 perplexity instrument "reproduces the bias against TOEFL essays reported by": **SUPPORTED.** Liang reports high FPR on TOEFL essays, near-perfect accuracy on US 8th-grade essays, and attributes the bias to low perplexity. The TOEFL essays came "from a Chinese educational forum", so "non-native test-takers" is fine.
- **l.453** "the Hugging Face release ... (MIT)": **SUPPORTED.** HF dataset WxWx/ChatGPT-Detector-Bias is licensed MIT.
- **l.453** "US 8th-grade essays come from the authors' GitHub repository, which has no licence file but whose README shows an MIT badge, and derive from the Hewlett Foundation ASAP data": **SUPPORTED.** The repo root lists no LICENSE file and the README carries an "MIT license" badge. The data sit in the folder HewlettStudentEssay_real_88. The paper says the 88 essays are "sourced from the Hewlett Foundation's Automated Student Assessment Prize (ASAP) dataset".
- **l.478** "the essays of \citet{liang2023detectors} (TOEFL, US 8th-grade and US college)": **SUPPORTED.** The repo holds TOEFL_real_91, HewlettStudentEssay_real_88 and CollegeEssay_real_70.

## lin2025: bib author name wrong
**Bib discrepancy (must fix).** The arXiv listing for 2504.13629 gives the first author as "Cong William Lin", and the bib copies it. The PDF title page names the author "Lin William Cong" (Cornell SC Johnson and NBER, will.cong@cornell.edu). His surname is **Cong**, so the bib makes natbib print "Lin and Zhu (2025)" when it should print "Cong and Zhu (2025)". Title, year and eprint are correct. No peer-reviewed version was found; the arXiv preprint and RePEc copies exist.

Copy-ready entry (renaming the key to cong2025 is optional; if renamed, update the 3 \citep uses at l.56, 81 and 91):
```
@misc{lin2025,
  title = {Divergent {LLM} Adoption and Heterogeneous Convergence Paths in Research Writing},
  author = {Cong, Lin William and Zhu, Wu},
  year = {2025},
  eprint = {2504.13629},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2504.13629}
}
```

- **l.56** pre-ChatGPT LLM share is "subtract[ed] as baseline misclassification": **SUPPORTED.** Section 4: "we adjusted the raw values by subtracting the average adoption rate observed before November 2022". The pre-ChatGPT rate is attributed to "misclassification by the model".
- **l.81** "classifier- and detector-based studies label documents": **SUPPORTED.** The authors fine-tune "discipline-specific large language models to detect the style of ChatGPT-revised texts" on more than 627k arXiv papers.
- **l.91** "adoption of LLM revision varies across disciplines and author groups": **SUPPORTED.** Evidence: "disparities in LLM adoption across academic disciplines, gender, native language status, and career stage".

## munozortiz2024
**Bib:** Matches Crossref (10.1007/s10462-024-10903-2): Artificial Intelligence Review 57(10), article 265, 23 Aug 2024; Muñoz-Ortiz, Gómez-Rodríguez, Vilares. OK.

- **l.95** "LLM text differs systematically from human text in lexico-grammatical features": **SUPPORTED.** The study covers news text from six LLMs across morphological, syntactic, psychometric and sociolinguistic dimensions. Evidence: "The results reveal various measurable differences between human and AI-generated texts". Specific differences include sentence-length spread, dependency and constituent types, and auxiliaries.

## park2026
**Bib:** Matches arXiv 2608.26710v1 (27 Aug 2026): the title and the three authors in order (Park, Jeong, Kim). OK.

- **l.104** "false-positive rates on non-native manuscripts vary widely": **SUPPORTED.** Evidence: "FPRs for human-written texts varied widely, from 0.0% to 100.0%" across 13 detectors. Per the HTML full text, this range applies to the original non-native manuscripts (pre-ChatGPT 2018-2022 subset): 0.0% for Binoculars and 100.0% for Log-rank.

## qwen35card: Table 1 release month
**Bib:** The card is huggingface.co/Qwen/Qwen3.5-9B, by the Qwen Team, Apache-2.0. The card's suggested citation is the family blog "Qwen3.5: Towards Native Multimodal Agents" (February 2026). The misc entry is acceptable. OK.

- **Table 1 (l.203 and caption l.212)** "Qwen3.5 9B, 2026-02", with no cutoff: **PARTLY.**
  - **Release month is 2026-03, not 2026-02.** The February 2026 date belongs to the Qwen3.5 family launch (the 397B-A17B repo was created 16 Feb 2026). The small dense models (0.8B/2B/4B/9B) were announced and released on **2 March 2026**: Qwen's tweets of that date, as reported by GIGAZINE on 3 Mar 2026, and the NYU Shanghai RITS write-up. The HF repo Qwen/Qwen3.5-9B was created 27 Feb 2026, privately before release, and last modified 2 Mar 2026. The card's "February" refers to the family blog, not this checkpoint.
  - Parameter count: the card says "Number of Parameters: 9B" and safetensors gives 9.65B. Consistent with "9B" and with "7 to 21 billion parameters" at l.453.
  - Licence: Apache-2.0, consistent with "Apache 2.0 for the others" at l.453.
  - Cutoff: none stated on the card, so the blank cell is correct.
  - This is the post-trained (thinking/non-thinking) model, not -Base.
- **Copy-ready fix (l.203):** `Qwen3.5 9B & 2026-03 & \\`
- **Knock-on effects: none.**
  - l.370 "Qwen3.5 [peaked] in its release quarter" stays true, since the peak and the release are both in 2026Q1.
  - code/analysis.py:1000 uses `"qwen3.5:9b": 2026.12`. Changing it to about 2026.17 leaves every rank unchanged: the nearest neighbours are gpt-oss at 2025.6 and Gemma 4 at 2026-06, and the 2026 Claude model is excluded. The release-peak rank correlations therefore do not change.
  - If the authors prefer to keep the card as sole source, write "2026-02/03" and note that the card dates only the family.

## sadasivan2025
**Bib:** Matches TMLR 2025 (mlanthology; OpenReview forum OOgsAZdFOt, which was blocked by a bot check, so I used the mirror). The five authors are in order: Sadasivan, Kumar, Balasubramanian, Wang, Feizi. The official title capitalises "Be": "Can AI-Generated Text Be Reliably Detected? ...". The bib has "be". This is cosmetic; optional fix: `title = {Can {AI}-Generated Text Be Reliably Detected? {S}tress Testing {AI} Text Detectors Under Various Attacks}`.

- **l.101** "detectors can be evaded": **SUPPORTED.** The paper introduces a recursive paraphrasing attack that substantially lowers detection rates of watermark, neural, zero-shot and retrieval detectors, and it also shows spoofing attacks.

## sun2025
**Bib:** Matches Crossref (10.18653/v1/2025.acl-long.1120): the title, the eight authors in order (Sun, Zhang, Shen, Zhang, Liu, Backes, Zhang, He), ACL 2025 Long, pp. 22975-23005. OK.

- **l.81** "classifier- and detector-based studies label documents ... Most target the share of text produced with LLM help": **SUPPORTED.** Evidence: "We then apply OSM-Det to SM-D to track AIGTs across social media platforms". The study reports an AI Attribution Rate on Medium, Quora and Reddit from Jan 2022 to Oct 2024.

## wu2025monoculture
**Bib:** Matches the ICLR 2025 proceedings BibTeX exactly: Wu, Black, Chandrasekaran; editors Yue, Garg, Peng, Sha, Yu; pp. 33068-33107. OK.

- **l.88** "Preference tuning reduces output diversity": **SUPPORTED.** Section heading: "RLHF Hurts Diversity the Most". The appendix finds "the pre-trained model is much more diverse than the aligned model". The abstract hedges ("likely embedded within the LLM's alignment processes"), and the evidence comes from one family (Llama-2 vs Llama-2-chat, with Vicuna as the SFT point). kirk2024 is co-cited, so the sentence is adequately supported.

---

## Disagreements with earlier reports (read after forming verdicts)
- **qwen35card release month.** An earlier report accepted "2026-03" while noting that the card itself does not date the 9B. v6_changed_sentences.md (row 13) then suggested "2026-02" based on the card's BibTeX month, and the table now says 2026-02. I disagree with the v6 suggestion: that BibTeX dates the Qwen3.5 family blog, and the 9B checkpoint was released on 2 Mar 2026. The table should say 2026-03, or cite a release source for it.
- **lin2025 author.** All earlier reports (batch4.md, v5_batch2.md, batch7_bib.md) accepted "Cong William Lin" from the arXiv listing. The PDF shows the author is Lin William Cong (surname Cong), so the bib's author field is wrong.
- **geng2025.** batch2.md proposed the current l.90 wording and marked it supported. I would add a hedge ("some ... appear to"), since the source says "suggest that some authors". This is minor.
