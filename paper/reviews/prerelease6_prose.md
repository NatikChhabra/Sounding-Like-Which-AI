# Pre-release round 6: prose copy-edit and changed-citation check

Commit `0ec57b6`. I read `paper/preprint.pdf` (16 pages, text extracted with pymupdf) alongside `paper/main.tex`. This is an AI check; no human has reviewed it.

**Page budget.** The main text ends at the foot of page 8, so every rewrite below is the same length as the original or shorter, unless it says otherwise. The few that add words are offset by cuts elsewhere (see the tally at the end of Part A). Limitations, Ethics, Acknowledgements and the appendices fall outside the 8 pages. Rewrites there are shorter anyway.

Rewrites are in LaTeX and use the `\R{}` keys already in `main.tex`, so they can be pasted directly.

---

## Part A: Prose

### Must fix

**A1. Abstract, whole paragraph (several problems; word count unchanged in net).**
- "Rather than how much text was produced…, we ask" leaves "rather than" with nothing to compare against.
- "on our own prompts" is ambiguous, because the 7.5 pp region also contains texts we generated.
- "peaking later for later, and longer-writing, generators" is hard to parse.
- "the 15 chosen in advance" is inaccurate. Llama-2-Chat 7B and Vicuna were also added after the second review (App. A(5)). What is true is that these 15 were chosen before the pattern was seen.
- "like a fixed list of marker words such as" stacks two comparisons.
- In the last sentence, "learners" is undefined, "than peers'" is missing "their", and "largely tracking essay scores" is a dangling modifier.

Replacement:
> We ask not how much text was produced with LLM help but how much writing, by any author, falls on the LLM side of a stylistic boundary, and which LLMs define that side. We define \textbf{Machine-Style Overlap} (\mso{}): the share of documents that a calibrated classifier on style features that ignore content-word identity judges at least as likely to be LLM output as pre-ChatGPT human writing. In \R{corpus_stats.arxiv_n_docs} arXiv abstracts (2015--2026), \mso{} was \R{arxiv_baseline_pre2022.all.mso}\% before ChatGPT and by June 2025 stood \R{arxiv_its.all.excess} percentage points (pp) above its pre-ChatGPT trend, far above placebo and instrument-drift gaps. Because recent LLMs learn from recent writing, we compare generators by vintage. Against generators whose pretraining data predate ChatGPT, the gap is smaller (\R{arxiv_vintage.pre2022data_matched.gap}\,pp; \R{arxiv_vintage.old_open_p1.gap}\,pp for the two we ran ourselves). Single-generator overlap mostly rose then fell, peaking later for newer (and longer-writing) generators (exploratory rank correlation \R{arxiv_vintage_peak.rho}, $n=\R{arxiv_vintage_peak.n}$; \R{arxiv_vintage_peak.rho_no_new} without the three added post hoc). A fixed reference set, like a fixed marker-word list (\emph{delve}), can thus show the shift receding while overlap with newer models still rises. In US school essays, English learners' essays fall in the region less often than their peers'; essay scores explain most of this.

**A2. §6.3, feature-family ablation (ambiguous: it reads as if all families were removed at once).**
Old: "and removing all closed-class words, part-of-speech trigrams, dependency labels, punctuation or sentence statistics gives between X and Y pp."
New:
> and removing any one family (closed-class words, part-of-speech trigrams, dependency labels, punctuation or sentence statistics) gives \R{arxiv_ablation.function_words.excess} to \R{arxiv_ablation.pos_trigrams.excess}\pp.

**A3. §6.3, "its 2026 rise" (contradicts the clause before it).** The sentence calls the monthly series flat since late 2025, then refers to "its 2026 rise". Only the annual mean rose.
Old: "The monthly series has been roughly flat since late 2025 (Figure 1a), and its 2026 rise depends on the 2026 model (§6.4)."
New:
> The monthly series has been roughly flat since late 2025 (Figure~\ref{fig:ts}a); the higher 2026 annual mean depends on the 2026 model (\S\ref{sec:vintage}).

**A4. §6.4, opening two sentences (says three times that pretraining data predate ChatGPT; the parenthesis repeats "shared ChatGPT conversations"; "and … and" chain).** The change saves about 12 words.
Old: "The pre-ChatGPT-data region (…) reflects models unlikely to have learned their style from post-ChatGPT scientific writing. Their pretraining data predate ChatGPT, and their 2023 instruction tuning used annotator data or shared ChatGPT conversations and, as far as is documented, no recent abstracts (Vicuna was tuned on user-shared ChatGPT chats)."
New:
> The pre-ChatGPT-data region (GPT-4, Llama-2-Chat 70B, Llama-2-Chat~7B and Vicuna~7B on the title-only task) holds models unlikely to have learned their style from post-ChatGPT scientific writing: their 2023 instruction tuning used annotator data or (Vicuna) user-shared ChatGPT conversations and, as far as is documented, no recent abstracts.

**A5. §6.4, "GPT-4 carries most of it (alone 11.4 pp; Vicuna 1.4 pp)."** "It" seems to point to the 3.5 pp gap of the two local models, which does not include GPT-4. Even if it means the 7.5 pp region gap, GPT-4 alone is larger than that, so "most of it" does not fit.
New:
> Within the region, GPT-4 drives the gap (\R{arxiv_vintage.single:raid-gpt4.gap}\pp{} alone; Vicuna \R{arxiv_vintage.single:vicuna:7b.gap}\pp).

**A6. §6.4, "on our title-only prompts that part is small (12.5 pp over all three prompts)".** The number in the parenthesis is large and contradicts "small".
New (+2 words):
> Part of the shift therefore points towards generators unlikely to have learned it from recent abstracts. On our own prompts that part is small from titles alone but \R{arxiv_vintage.old_open_all.gap}\pp{} over all three prompt styles.

**A7. §6.4, "The analysis is exploratory: … 0.37 given length)."** This is one sentence with two independent claims, eight numbers and a three-part parenthesis. Split it (same length):
> The analysis is exploratory. A first test, release date against the 2025-to-2026 change, gave \R{arxiv_vintage_release_corr.rho_annual} on annual means but \R{arxiv_vintage_release_corr.rho_q4} from 2025Q4 (Appendix~\ref{app:deviations}). Without the three 2026 open models, added after the pattern was seen, the correlation is \R{arxiv_vintage_peak.rho_no_new} ($n=\R{arxiv_vintage_peak.n_no_new}$, $p=\R{arxiv_vintage_peak.rho_no_new_p}$; \R{robustness_v7.seeds.rho_no_new_min}--\R{robustness_v7.seeds.rho_no_new_max} across training draws), or \R{arxiv_vintage_peak.partial_release_given_length_no_new} given length.

**A8. §6.6, "yet flags the PERSUADE learners less often than their peers, because their writing is less predictable".** The second "their" could refer to the peers.
New:
> yet flags PERSUADE learners less often than their peers because the learners' writing is less predictable (Appendix~\ref{app:learners}).

**A9. Discussion, sentence 2 (four clauses chained with "and … while … so").**
New (split, same length):
> Overlap tended to peak later for more recent generators, and under three of the four 2026 generators it peaked in 2026 or was still rising. Words mined from most generators fell meanwhile, so the decline of \emph{delve} need not mean that writing stopped moving.

**A10. Discussion, "refreshed ones may mistake what models learned from writing for it."** The antecedent of "it" is unclear.
New (+2 words):
> …may therefore understate recent change; refreshed ones may mistake models' learning from writing for a shift in writing.

**A11. Table 1 caption.** "or quarter" is stale: no row gives a quarter any more, since Qwen3.5 is now 2026-02. The caption also nests three clauses inside one parenthesis.
New (shorter):
> Reference generators, with release month (year where only that is documented, approximated for the peak analysis; not public for the 2026 model) and pretraining-data cutoff where the developer states one.

### Should fix

**A12. Contribution (4), and "longer-writing" in general.** "Longer-writing" is a coinage. Use "newer generators, which also write longer" or, as in A1, "newer (and longer-writing)". Contribution (4) new text:
> single-generator overlap tends to peak later for newer generators, which also write longer, so the trajectory depends on the reference (\S\ref{sec:vintage}).

**A13. Terminology for learners.** The paper uses "learners", "US learners", "English learners", "ELL" (defined in §4 and used only in Fig. 4), "learner essays", "proficiency", "essay score" and "holistic score". Use "English learners" at first mention in each of the abstract, contribution (5) and §6.6. Pick one of "essay score" or "proficiency". The analysis adjusts for the holistic score, so "essay score (proficiency)" once, then "essay score". Contribution (5) new text:
> …and, contrary to our plan, English learners' essays fall in the region \emph{less} often than their peers'.

**A14. Introduction, "models whose pretraining data predate ChatGPT, models released in 2023–2025, and models released in 2026".** The first two groups overlap, because the pre-ChatGPT-data models were released in 2023. Use "…, other models released in 2023–2025, and…" (+1 word).

**A15. Related Work, Kusumegi.** The semicolon joins two unrelated clauses: "Most target the share …; LLM adoption also changes how many papers scientists produce." Replace the semicolon with a full stop.

**A16. Related Work, Chang.** In "our pre-ChatGPT slope (partly field mix) agrees", the parenthesis is cryptic. "Agrees" also overstates the link, because Chang measures LM predictability and diversity, not a classifier flag rate.
New (same length):
> …a trend that began before generative AI; our pre-ChatGPT slope, partly a field-mix effect, points the same way.

**A17. Related Work, detection sentence (three clauses, seven citations).** Split after `\citep{chakraborty2024}`:
> …converge \citep{chakraborty2024}. Off-the-shelf detectors have flagged non-native writing \citep{liang2023detectors}, although…

**A18. §4, field mix (the last clause repeats Limitations almost word for word: "The overall arXiv series averages a stratified sample").**
New (about 8 words shorter):
> Smaller fields contribute fewer documents, especially in early years, so the field mix changes (eess: \R{robustness_v6.field_share.eess_2015}\% of scored abstracts in 2015, \R{robustness_v6.field_share.eess_2022}\% in 2022); the overall series is a stratified sample, not the arXiv population.

**A19. §4, "The API returns the latest version of each abstract, so papers … are excluded".** The exclusion is a choice, not a consequence of the API. Use "…, so we exclude papers first submitted before ChatGPT but revised after it (…)."

**A20. §5, "MTLD lexical diversity (MTLD; McCarthy and Jarvis, 2010)".** The acronym appears twice. Use "and lexical diversity (MTLD; \citealp{mccarthy2010})".

**A21. §5, essay perplexity instrument.** It is unclear what "whose" refers to. Read literally, it says Qwen2.5-0.5B's training data predate PERSUADE, which is false.
New (same length):
> …and a one-feature isotonic classifier on mean token negative log-likelihood (the statistic behind perplexity-based detectors) under Qwen2.5-0.5B or \gptii{} small; \gptii{}'s training data predate the TOEFL and PERSUADE releases.

**A22. §5, ITS sentence.** "a slope change at December 2022 and Newey–West (6 lags) standard errors" leads the reader down the wrong parse. Use "a level shift and slope change at December 2022, with Newey--West (6-lag) standard errors."

**A23. §6.3, "a gap 2.1 times as large as the extrapolated trend value itself".** The phrasing is padded. Use "\R{…relative_gap} times the extrapolated trend value."

**A24. §6.3, variant range.** "Across the variants in Table 2 that change the threshold, the sample or the trend, the gap stays between 23.5 and 29.1 pp." Table 2 now also has the gradient-boosted-trees row at 29.5, which falls outside that range. The qualifier technically excludes it, but readers will compare against the table. Add "(gradient-boosted trees: \R{robustness_v7.gbm_main.excess}\pp)" or move the GBM row next to the generator-set rows (+4 words if added).

**A25. §6.3, nested commas inside the parenthesis "(Fast-DetectGPT, Bao et al., 2024, with GPT-2 small)".** Use "Fast-DetectGPT \citep{bao2024fastdetectgpt} with \gptii{} small, a zero-shot detector, separates…".

**A26. §6.4, "fitted only up to June 2025 it is 13.1 pp against 22.7 pp for the 2024–2025 open models, and 7.6 pp for the two small local models."** The trailing "and 7.6 pp" attaches to the wrong comparison.
New:
> fitted only to June 2025, the gap is \R{…gap_to_eval}\pp{} (two small local models: \R{arxiv_vintage.old_open_p1.gap_to_eval}\pp), against \R{arxiv_vintage.local_p1.gap_to_eval}\pp{} for the 2024--2025 open models.

**A27. §6.4, "From 2026Q2 to 2026Q3 overlap fell under every other generator, also with equal field weights, so…".** "Also with equal field weights" dangles. Use "…under every other generator, with or without equal field weights, so…".

**A28. "Later for later generators".** The jingle appears in the abstract, twice in §6.4 ("the turn tended to come later for later generators", "keeps turning down later for later generators") and in Fig. 2. Use "later for newer generators".

**A29. §6.4, length sentence (two clauses and four numbers).** Split:
> Newer generators, however, also write longer (rank correlation \R{…rho_release_length} between release date and median output length), and length predicts the peak about as well (\R{…rho_length}). Given length, the partial correlation of release date and peak is \R{…partial_release_given_length}; vintage and length cannot be separated.

**A30. §6.4, "If overlap keeps turning down later for later generators, a fixed reference set will show the shift receding while overlap with newer models still rises."** This restates the abstract almost word for word. Use a shorter version (−6 words):
> If newer generators keep peaking later, any fixed reference set will eventually show the shift receding.

**A31. §6.5, "and the 2026 model (49.4% to 57.4%), whose mined words are ordinary academic vocabulary."** It is unclear whether "whose" covers both models or only the 2026 model. Use "…; the latter's mined words are ordinary academic vocabulary."

**A32. §6.6, "with both regions built from the same eight generators (arXiv gap 32.1 pp with those)".** The ending "with those" is vague. Use "when both regions use the same eight generators (arXiv gap then \R{control_difference.arxiv_excess}\pp)."

**A33. Discussion, "Authors' use of the 2026 open models explains little of their peaks; … they and the authors may share the style of the commercial models authors used…".** Problems: "their" is ambiguous; §6.4 says "can explain little", but here it is stated as fact; "authors" is repeated.
New:
> Authors' use of the 2026 open models can explain little of those models' peaks: the models may have learned from recent writing, or they and the authors may share the style of commercial models used in 2024--2026, which, apart from the 2026 model, we did not run.

**A34. Conclusion, "Machine-Style Overlap rose … well above its pre-ChatGPT trend, partly towards generators whose pretraining data predate ChatGPT."** Overlap cannot rise "towards" generators; that mixes two images.
New:
> …rose from \R{…}\% before ChatGPT to \R{…}\% in 2025, well above its pre-ChatGPT trend; overlap with generators whose pretraining data predate ChatGPT rose less.

In the next sentence, "compare several" leaves the noun to be guessed. Use "compare several vintages".

**A35. Typography of p-values.** The macros `arxiv_its.baseline_field_heterogeneity.p` and `robustness_v3.field_holm.econ` expand to `{<}0.001`. The braces suppress relation spacing, so the PDF shows "p<0.001" in §6.2 and §6.3 but "p < 0.05" everywhere else. Make the macros emit `<0.001`, or write `$p<0.001$`.

**A36. Model names differ across tables.**
- Table 1 has "Mistral-7B-Instr. v0.1" and "Mistral 7B Instruct v0.3". Table 5 has "Mistral 7B v0.3". Table 4 has "Mistral 7B" and "RAID Mistral-chat".
- "Cohere command" (Tables 1 and 5, Fig. 2) vs "RAID Cohere-chat" (Table 4) vs "Cohere's chat model" (text).
- "Llama-2-Chat 70B" vs "RAID Llama-chat" (Table 4).

Use the Table 1 names in Tables 4 and 5, with a "RAID" group label instead of a prefix.

**A37. Year ranges.** The Fig. 2a legend has "Open models 2024–25", while the text has "2024–2025 open models". Make the legend say 2024–2025.

**A38. Table 5, "Draws" column.** The column means bootstrap draws, but the text uses "training draws" for the Seeds column. Rename the column to "Recurs (%)" and adjust the caption.

### Outside the 8 pages (Limitations, appendices)

**A39. Limitations, median lengths.** The sentence is hard to parse. The label "2025–2026 open models" also leaves out the 2024 models (Mistral v0.3 at 139, Llama 3.1 at 139, Phi-4 at 150), although they fall inside the stated 138–186 range.
New:
> Median lengths are \R{…vicuna…} (Vicuna) to \R{…raid-llama-chat…} words (Llama-2-Chat 70B, at the truncation limit) within the pre-ChatGPT-data region, \R{…mpt…} to \R{…mistral-chat…} for the other RAID models and \R{…granite3.3…} to \R{…granite4.2…} for the local 2024--2026 models.

**A40. Limitations, "Output length rises … so the vintage pattern is not separated from length, and the single-generator regions of the local models share one human training sample."** This joins two unrelated points, and the first repeats §6.4. Split it into two sentences.

**A41. Limitations, "The three 2026 open models were added after the pattern … had been seen, and single-generator regions rest on 150 texts each…, so instrument precision differs by vintage."** The "so" applies only to the second clause. Split it into two sentences.

**A42. Limitations, classifier-agreement sentence.** It joins two topics. Split it at ", and both the style and the perplexity instruments flag TOEFL essays…" into a new sentence: "Both the style and…".

**A43. App. A(3), "The 2026 model's prompt batches were committed two minutes, and its texts merged nine minutes, after a preliminary arXiv run without them was committed".** The gapped construction is hard to follow. Also, "The pilot may have informed this decision" is separated by one sentence from the decision it refers to.
New:
> A preliminary arXiv run without the 2026 model was committed two minutes before its prompt batches and nine minutes before its texts were merged; the pilot may have informed this choice. Phi-4 and Granite were first used after the first review.

**A44. App. A(6), "the correlation without the 2026 open models, across training draws, with length or field weights and given output length".** This reads as a single correlation with all of those properties. Use "the peak correlation without the 2026 open models, across training draws, under length or field weights, and given output length".

**A45. App. F, implied prevalence.**
- The first sentence repeats the §6.3 sentence word for word. Replace it with: "Using held-out-generator recall, the implied 2024 shares (§\ref{sec:shift}) become \R{…}\% and \R{…}\%."
- "Implied shares are larger if partly revised documents enter the region or…" leaves unclear what they are larger than. Use: "Implied shares overstate LLM output if partly revised documents enter the region or authors adopt LLM style without an LLM, which the identity cannot tell apart."

**A46. App. G, number pile-up.** The sentence "about 0.2 times as large as its extrapolated trend value, against 2.1 times for abstracts (0.21 against 1.47 on the logit scale)" puts 0.2 next to 0.21 and invites a misreading. Split it, and move the logit values to their own clause. Also, "Its gap is 1.4 pp at threshold 0.6" follows a sentence about the genre difference, so "Its" is ambiguous. Use "The Hansard gap is…".

**A47. App. I, "(odds ratio 0.47; 0.66, CI 0.52–0.85, after adjusting for proficiency)".** The commas inside the parenthesis nest. Use "(odds ratio 0.47, or 0.66 [CI 0.52–0.85] adjusted for essay score)".

**A48. App. D, "The larger scoring models of the original method might."** The verb is missing. Use "…might do better."

**A49. Acknowledgements, "in two full passes".** Changed sentences have since had further passes (v6, and this round). Consider "in two full passes, with later re-checks of changed sentences".

### Main-text length tally (approximate words)
Abstract: 0 (A1). Body: A4 −12, A6 +2, A10 +2, A11 −4, A14 +1, A18 −8, A20 −2, A23 −4, A30 −6, A24 +4 (optional). All others: 0 or −1. The net change is about −25 words, so the main text should not grow if all of these are applied. Rebuild the PDF and confirm that the Conclusion still ends on page 8.

---

## Part B: Citations changed or moved (`git diff c63ada2 0ec57b6 -- paper/main.tex`)

`references.bib` did not change between the two commits (`git diff --stat` lists no bib change), so no keys were added. The keys whose citing context moved (`shumailov2024`, `gerstgrasser2024`) and `chang2026` were re-checked against publisher and Crossref metadata.

| # | Location | Key(s) | What changed | Source checked | Supports as worded? | Bib entry |
|---|---|---|---|---|---|---|
| B1 | §2, Prevalence para. | chang2026 | The ending changed from "our pre-ChatGPT slope points the same way" to "our pre-ChatGPT slope (partly field mix) agrees". | Springer article page `dc.description` (DOI 10.1007/s11192-026-05589-y). It covers PubMed, Wikipedia and Stack Exchange over 2014–2024, using perplexity and Binoculars under OPT-125M, GPT-2 and Llama-3.2. Quote: "This trend predates the widespread adoption of generative AI". | **Yes**, for the cited clause. "Agrees" is the paper's own comparison, between Chang's predictability trend and the paper's MSO slope. These are different quantities, so "points the same way" is safer (A16). | Correct: Eunsuk Chang, *Scientometrics* 131(3):1635–1654, March 2026 (Crossref, OpenAlex). |
| B2 | §7 Discussion | shumailov2024, gerstgrasser2024 | Changed from "can no longer serve as independent references" to "may no longer be independent references". These keys are now cited only here, because the Related Work sentence was deleted (B4). | Nature page and Crossref for Shumailov et al.: collapse from "indiscriminate use of model-generated content in training". arXiv 2404.01413 and the COLM 2024 listing for Gerstgrasser et al.: accumulating real and synthetic data "avoids model collapse". | **Yes.** Both papers study recursive training on model outputs, and the sentence claims only a precondition, "not evidence". The new hedge "may" is more cautious than before. Optional: with B4 gone, the paper no longer mentions that collapse is avoidable when real data accumulate. A clause such as "(avoidable when real data accumulate; Gerstgrasser et al.)" would restore that, but it costs space. | Correct. Shumailov: *Nature* 631(8022):755–759, 2024; the author order matches. Gerstgrasser: COLM 2024 (OpenReview 5B2K4LRgmz, listed under COLM.2024); the 14 authors are in the COLM order. |
| B3 | §2, Homogenisation para. | yakura2024, anderson2025spoken, geng2025, lin2025 | The wording is unchanged. The line shows up in the diff only because the next sentence was deleted, and the text now runs on to "Our vintage comparison asks…". | Not re-opened; the claim is unchanged. v6 and v5 record it as SUPPORTED. | Yes (unchanged). | Unchanged. |
| B4 | §2, Homogenisation para. (deleted) | shumailov2024, gerstgrasser2024 | Sentence removed: "Models trained on their own outputs degrade when synthetic data replace real data … but not when the two accumulate". | n/a | n/a. Both keys are still cited in the Discussion (B2), so neither bib entry is orphaned. | n/a |
| B5 | Table 1 caption | openai2023gpt4, touvron2023llama2, vicuna15card, zheng2023judging, and the "Other dates" list | Only the first, uncited sentence changed (it now says the 2026 model's month is not public). The cited footnotes are unchanged. | Vicuna 7B v1.5 Hugging Face card, re-checked: fine-tuned from Llama 2 on "around 125K conversations collected from ShareGPT.com". | Yes (unchanged). For the stale "or quarter" in the caption, see A11. | Unchanged. |
| B6 | §6.4, uncited parenthesis | (Table 1 note d) | The parenthesis changed from "(Vicuna imitates ChatGPT's conversational style, not its abstracts)" to "(Vicuna was tuned on user-shared ChatGPT chats)". | Same Vicuna card as B5. | The fact is correct. The new parenthesis repeats the clause before it, and it drops the old reason why this does not contradict "no recent abstracts". A4 fixes both. | n/a |
| B7 | §6.3; App. A(2) | bao2024fastdetectgpt; liang2023detectors | Context lines in the diff only; the wording is unchanged. | Not re-opened. | Yes (unchanged). | Unchanged. |

**Part B summary.** I found two citing sentences whose wording changed (B1, B2) and one deletion (B4). Both changed sentences are supported by their sources as now worded. All bibliography entries involved are correct. The only recommendation is a wording change in B1 ("agrees" → "points the same way"); there is no citation error.

---

## Counts
- Part A: 11 must-fix (A1–A11), 27 should-fix in the main text (A12–A38), and 11 outside the 8-page limit (A39–A49). Net effect on the main text is about −25 words.
- Part B: 7 diff locations checked. 2 changed citing sentences, both supported; 1 deleted sentence with no orphaned keys; 0 bibliography errors; 1 wording suggestion (B1).
