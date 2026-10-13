# Pre-release style audit 2: AI-tell and clarity pass

Scope: `paper/main.tex` (abstract through appendices) and `README.md`. I read the rendered `paper/preprint.pdf`
(pymupdf) alongside the source. Line numbers refer to `main.tex` as of this audit. In "Current" quotes, source
line breaks are shown as spaces. Every replacement keeps all `\R{...}` macros, citations, labels and refs unless a
note says otherwise. Δ is the approximate change in words (negative = shorter).

**Page budget.** Page 8 is full: the Conclusion's last line sits at y≈775 pt, the bottom of the text block. There is
no slack. Items #1-#54 (pages 1-8) sum to about **-65 words** if all are applied. That is a rough count: sentence
splits can still cost a line, so rebuild and check that the Conclusion ends on page 8. Items marked "+" must not be
applied without the savings items, chiefly #36 (-19), #33 (-9), #37, #38, #24 and #32. Limitations, Ethics, AI Use,
the appendices and the README sit outside the page budget.

---

## Overall verdict

**Would a reader suspect AI authorship from the prose? Partly. A careful reader would likely suspect it, though not
from vocabulary.** The usual lexical tells are absent: no "delve", "crucially", "notably", "comprehensive", "robust"
(except in macro names), "landscape", "furthermore" or "moreover"; I grepped for them. Claims are mostly hedged and
numbers come with intervals. The suspicion comes from structure, repeated at a density human authors rarely reach:

1. **Colon-explanation sentences.** About 48 colons in eight pages of running text. The pattern is a short claim, a
   colon, then the evidence ("Its parts agree:", "Individual documents are harder:", "No single feature family carries
   it:", "depends on which LLM:").
2. **Semicolon chaining.** About 105 semicolons in the source. Many sentences join three or four independent results
   with semicolons; contribution (5) is one 70-word sentence with three semicolons and three identical "(§6.6)" refs.
3. **Aphoristic closers that generalise one step beyond the evidence.** "will eventually show the shift receding",
   "lexical measures recede earlier than stylistic ones", "no longer independent anchors for each other", "which
   learners such a detector penalises depends on how predictable their writing is", "The two questions treat one
   number differently." These quotable lines are the most recognisably model-written feature of the paper.
4. **Phrase recycling.** The same constructions recur verbatim or near-verbatim: "peak later the more recent the
   generator" (L85, L482, L541, L565, plus L44/L452/L493 variants), "is not on its own evidence that writing stopped
   moving" (L513, L544), "will eventually show the shift receding" (L46, L482, README), "whoever wrote it" (L36, L63),
   "fails its own placebo tests/grid" (L89, L523, L584), "Against ... Against ..." (L42-43).
5. **Uniform, number-dense sentence length.** Most Results sentences run 35-60 words and carry 3-6 macros in
   parentheses. The rhythm hardly varies; short sentences appear almost only as aphoristic closers.
6. **Over-compression.** In a few places the prose drops to shorthand that only its writer can parse: "Individual
   documents are harder", "with gaps ... about a quarter as large or smaller", "the controlled estimate", "a clear
   rise against a fall", "and the following", "Decided after ...: Phi-4, Granite and the 2026 model",
   "exclude ... the field-month cluster design".

**Top 5 changes with the biggest effect**

1. **Remove the aphoristic generalisations** (#5, #8, #33, #36, #37, #40). They are the lines a reader would quote as
   "sounds like ChatGPT", and two of them (#36, #40) overstate the evidence.
2. **Break the semicolon chains in the Introduction and Results** (#13, #14, #18, #20, #21, #23, #29, #48, #50). Split
   each into two or three sentences with one main result apiece.
3. **De-duplicate recycled phrases**, above all the "the more recent the generator" comparative-correlative and the
   "not on its own evidence" clause (#8, #12, #15, #33, #38, #39).
4. **Repair the cryptic compressions** (#7, #11, #28, #30, #31, #53, #57, #61, #62). These read as LLM compression
   artefacts and also hurt clarity.
5. **Fix the places where wording overstates the result**: "Its parts agree" for subset gaps of 3.5 vs 7.4-8.6 pp
   (#27), and "overlap with each generator rises and then turns down" when the 2026 model is still rising (#29). In
   the README, also fix "the gap holds across ... never-revised papers" (#R3).

---

## Priority 1: Abstract, Introduction, Conclusion

### Abstract

**#1. L35-36. Repeated flourish and "they X; we Y" pivot.**
Current: `Studies of LLM-assisted writing estimate how much text was produced with LLM help. We ask how much writing, whoever wrote it, falls on the LLM side of a stylistic boundary, and which LLMs define that side.`
Replace: `Studies of LLM-assisted writing estimate how much text was produced with LLM help. We ask how much writing, by any author, falls on the LLM side of a stylistic boundary, and which LLMs define that side.`
Note: "whoever wrote it" appears again at L63. Keep the abstract form and change L63 (#8), or apply both. Δ 0.

**#2. L40-41. Inflated "far beyond".**
Current: `pre-ChatGPT trend, far beyond placebo and instrument-drift gaps.`
Replace: `pre-ChatGPT trend, well above any placebo or instrument-drift gap.`
Note: the largest drift gap (6.5 pp) is about a quarter of the main gap, so "far beyond" overstates the contrast. Δ +1.

**#3. L41-42. The causal link is left implicit; the reader has to infer why training data matter.**
Current: `Because recent LLMs are trained on recent writing, we compare reference generators by vintage.`
Replace: `Recent LLMs learn from recent writing, so overlap with them is ambiguous; we compare reference generators by vintage.`
Δ +3 (+). Offset with #4 and #5.

**#4. L43-45. Repeated "Against ..." opening, "turns down ... the turn", and a missing caveat. The body (L457) and the README both call this analysis exploratory; the abstract does not.**
Current: `Against one generator at a time, overlap rises and then turns down, and the turn tends to come later for later generators (rank correlation \R{arxiv_vintage_peak.rho}, $n=\R{arxiv_vintage_peak.n}$).`
Replace: `With one generator at a time as reference, overlap rises and then falls, peaking later for later generators (exploratory rank correlation \R{arxiv_vintage_peak.rho}, $n=\R{arxiv_vintage_peak.n}$).`
Δ -3.

**#5. L45-46. A quotable aphorism with a "like ... such as" double simile.**
Current: `A reference set that is not refreshed, like a fixed list of marker words such as \emph{delve}, will eventually show the shift receding.`
Replace: `A fixed reference set, including a list of marker words such as \emph{delve}, will eventually show the shift receding.`
Δ -4.

**#6. L46-48. The "even under" twist makes the reader stop and work out the logic.**
Current: `In student essays, English learners' writing is less machine-like than their peers', even under a \gptii{} perplexity instrument that reproduces a published bias against TOEFL essays.`
Replace: `In student essays, English learners' writing is less machine-like than their peers'. A \gptii{} perplexity instrument agrees, although it reproduces a published bias against non-native TOEFL essays.`
Note: "non-native" comes from L757. Δ +3 (+). Optional; apply only with savings elsewhere.

### Introduction

**#7. L56. Cryptic compression: harder to do what?**
Current: `Individual documents are harder:`
Replace: `Judging individual documents is harder:`
Δ +1.

**#8. L61-64. Mirrored "X answer a ... question: ...? We answer a ... question: ...?", the repeated "whoever wrote it", a teaser sentence, and "treat" used three times in four lines (L63, L65, L67).**
Current: `Existing measurements answer a \emph{prevalence} question: what fraction of a corpus was produced or modified with an LLM? We answer an \emph{overlap} question: what fraction of a genre's writing is stylistically closer to LLM output than to pre-ChatGPT human writing, whoever wrote it? The two questions treat one number differently. Prevalence estimators report a small ``LLM share'' for text written before ChatGPT, which studies treat as consistent with false positives`
Replace: `Existing measurements answer a \emph{prevalence} question: what fraction of a corpus was produced or modified with an LLM? We ask an \emph{overlap} question: what fraction of a genre's writing, by any author, is stylistically closer to LLM output than to pre-ChatGPT human writing? The two differ in how they handle text written before ChatGPT. Prevalence estimators report a small ``LLM share'' for it, which studies read as consistent with false positives`
Δ -1.

**#9. L66-67. Third "treat".**
Current: `we treat that share as a property of the two text distributions`
Replace: `we regard that share as a property of the two text distributions`
Δ 0.

**#10. L69-71. Chatty, unsupported jab ("share but rarely face directly") and a clumsy relative clause.**
Current: `The overlap question has a complication that prevalence studies share but rarely face directly: ``LLM style'' is defined by whichever models are used as the reference. Recent models are trained on recent text, so an overlap with them that rises over time may mean`
Replace: `Both questions share a complication that prevalence studies seldom discuss: ``LLM style'' is defined by whichever models serve as the reference. Recent models are trained on recent text, so a rising overlap with them may mean`
Δ -4.

**#11. L81-83. Contribution (3) ends in a garden path. "about a quarter as large or smaller" attaches to a noun six words back.**
Current: `(3)~Abstracts moved far into the LLM region after 2022, more in computer science than in mathematics, with gaps at placebo dates and under instruments trained on earlier years about a quarter as large or smaller (\S\ref{sec:shift}).`
Replace: `(3)~Abstracts moved far into the LLM region after 2022, more in computer science than in mathematics. Placebo dates and instruments trained on earlier years give gaps at most about a quarter as large (\S\ref{sec:shift}).`
Δ -2.

**#12. L84-86. First use of a construction the paper repeats about seven times.**
Current: `overlap with a generator tends to peak later the more recent the generator, so the trajectory depends on the vintage of the reference (\S\ref{sec:vintage}).`
Replace: `overlap with a single generator tends to peak later for more recent generators, so the trajectory depends on the reference's vintage (\S\ref{sec:vintage}).`
Δ -2.

**#13. L87-90. Contribution (5): one 70-word sentence, three semicolons, and three refs that all render as "§6.6".**
Current: `(5)~Secondary results: marker words mined from each generator rose until 2025, and most fell in 2026 (\S\ref{sec:markers}); we detect no change in the stylistic dispersion of abstracts beyond its pre-ChatGPT trend once length is held fixed (\S\ref{sec:dispersion}); parliamentary speech changed little but fails its own placebo tests (\S\ref{sec:hansard}); and, contrary to our analysis plan, essays by English-language learners are \emph{less} machine-like than their peers' (\S\ref{sec:learners}).`
Replace: `(5)~Secondary results: marker words mined from each generator rose until 2025, and most fell in 2026 (\S\ref{sec:markers}). Once length is held fixed, we detect no change in the stylistic dispersion of abstracts beyond its pre-ChatGPT trend. Parliamentary speech changed little but fails its own placebo tests. Contrary to our analysis plan, essays by English-language learners are \emph{less} machine-like than their peers' (\S\ref{sec:learners}).`
Note: the labels `sec:dispersion` and `sec:hansard` stay defined at L519; only two duplicate refs are dropped. Δ -2.

**#14. L91-94. Five hypotheses packed into one parenthesis inside one sentence (about 60 words).**
Current: `Our analysis plan, with five hypotheses (H1: pre-ChatGPT \mso{} is non-zero and differs by field; H2: arXiv \mso{} rises above its pre-ChatGPT trend; H3: more than in a less-exposed genre; H4: more in computer science than in mathematics; H5: learner essays have higher \mso{}), was committed to version control before any result was computed (Appendix~\ref{app:deviations}).`
Replace: `Our analysis plan was committed to version control before any result was computed (Appendix~\ref{app:deviations}). It stated five hypotheses: pre-ChatGPT \mso{} is non-zero and differs by field (H1); arXiv \mso{} rises above its pre-ChatGPT trend (H2), more than in a less-exposed genre (H3) and more in computer science than in mathematics (H4); and learner essays have higher \mso{} (H5).`
Δ +1.

### Conclusion

**#15. L562-566. The opening sentence repeats the abstract's definition. "far beyond trend" is vague. "partly towards the style of" is compressed. The closer is generic.**
Current: `Machine-Style Overlap measures how much of a genre's writing sits on the LLM side of a stylistic boundary. In arXiv abstracts it rose from \R{arxiv_baseline_pre2022.all.mso}\% before ChatGPT to \R{arxiv_yearly.2025.mso}\% in 2025, far beyond trend, partly towards the style of the pre-ChatGPT-data generators. Overlap with a generator tended to peak later the more recent the generator, so studies of LLM influence on writing should report and refresh the vintage of their reference models.`
Replace: `In arXiv abstracts, Machine-Style Overlap rose from \R{arxiv_baseline_pre2022.all.mso}\% before ChatGPT to \R{arxiv_yearly.2025.mso}\% in 2025, \R{arxiv_its.all.excess} points above its pre-ChatGPT trend by June 2025. Part of this shift is towards generators whose pretraining data predate ChatGPT. Overlap with a single generator tended to peak later for more recent generators, so studies of LLM influence on writing should report the vintage of their reference models and update it.`
Note: this reuses the abstract's existing `arxiv_its.all.excess` macro, so no new claim is added. Δ -4.

---

## Priority 2: Results (§6) and Discussion

**#16. L321. A "X, but not Y" heading.**
Current: `\subsection{Separable, but not completely}`
Replace: `\subsection{Separability of human and LLM text}`
Δ 0.

**#17. L333. "structured" is vague.**
Current: `\subsection{Pre-ChatGPT overlap is structured (H1)}`
Replace: `\subsection{Pre-ChatGPT overlap varies by field (H1)}`
Δ 0.

**#18. L349-352. A three-part chain of yearly numbers spread over two sentences and a semicolon.**
Current: `Yearly arXiv \mso{} ranged from \R{arxiv_yearly.2016.mso}\% to \R{arxiv_yearly.2020.mso}\% in 2015--2021 and was \R{arxiv_yearly.2022.mso}\% in 2022. It was \R{arxiv_yearly.2023.mso}\%, \R{arxiv_yearly.2024.mso}\% and \R{arxiv_yearly.2025.mso}\% in 2023--2025 and \R{arxiv_yearly.2026.mso}\% in January--September 2026; the monthly series has been roughly flat since late 2025 (Figure~\ref{fig:ts}a).`
Replace: `Yearly arXiv \mso{} ranged from \R{arxiv_yearly.2016.mso}\% to \R{arxiv_yearly.2020.mso}\% in 2015--2021, was \R{arxiv_yearly.2022.mso}\% in 2022, then \R{arxiv_yearly.2023.mso}\%, \R{arxiv_yearly.2024.mso}\% and \R{arxiv_yearly.2025.mso}\% in 2023--2025 and \R{arxiv_yearly.2026.mso}\% in January--September 2026. The monthly series has been roughly flat since late 2025 (Figure~\ref{fig:ts}a).`
Δ -2.

**#19. L360. A colon-led aphorism.**
Current: `No single feature family carries it: removing MTLD,`
Replace: `The gap does not rest on one feature family. Removing MTLD,`
Δ +2.

**#20. L363-367. About 60 words, with a colon-led, hedged tail.**
Current: `The analytic Fast-DetectGPT criterion \citep{bao2024fastdetectgpt}, computed with \gptii{} small, separates our human and LLM abstracts only moderately (AUC \R{arxiv_fastdetect_auc.heldin_auc}), and its flag rate on 600 abstracts per year does not rise (\R{arxiv_fastdetect.2015.share_flagged}\% in 2015, \R{arxiv_fastdetect.2026.share_flagged}\% in 2026): a small, older scoring model misses the shift, though the original method's larger models may not.`
Replace: `The analytic Fast-DetectGPT criterion \citep{bao2024fastdetectgpt}, computed with \gptii{} small, separates our human and LLM abstracts only moderately (AUC \R{arxiv_fastdetect_auc.heldin_auc}). Its flag rate on 600 abstracts per year does not rise (\R{arxiv_fastdetect.2015.share_flagged}\% in 2015, \R{arxiv_fastdetect.2026.share_flagged}\% in 2026), so this small, older scoring model misses the shift; the original method's larger models may not.`
Δ -1.

**#21. L367-371. More than two clauses of numbers. The parenthetical "(with the real gap's 30-month horizon, X% and at most Y)" does not say what X% and Y are. The method was already given in §5.**
Current: `Of \R{robustness_v3.arxiv_placebo_grid.n_breaks} placebo breaks placed every second month from 2016 to 2021, \R{robustness_v3.arxiv_placebo_grid.share_p_below_05}\% give a gap with $p<0.05$, close to the nominal 5\%, and the largest is \R{robustness_v3.arxiv_placebo_grid.max_abs_gap}\pp{} (with the real gap's 30-month horizon, \R{robustness_v5.arxiv_placebo_grid_30m.share_p_below_05}\% and at most \R{robustness_v5.arxiv_placebo_grid_30m.max_abs_gap}\pp).`
Replace: `Of the \R{robustness_v3.arxiv_placebo_grid.n_breaks} placebo breaks, \R{robustness_v3.arxiv_placebo_grid.share_p_below_05}\% give a gap with $p<0.05$, close to the nominal 5\%, and the largest gap is \R{robustness_v3.arxiv_placebo_grid.max_abs_gap}\pp. At the real gap's 30-month horizon, \R{robustness_v5.arxiv_placebo_grid_30m.share_p_below_05}\% give $p<0.05$ and the largest is \R{robustness_v5.arxiv_placebo_grid_30m.max_abs_gap}\pp.`
Δ -3.

**#22. L373-375. Semicolon split.**
Current: `extrapolated over 65 months from a two-year trend; instrument ageing can thus produce gaps of a few points, up to about a quarter of the observed gap.`
Replace: `extrapolated over 65 months from a two-year trend. Instrument ageing can thus produce gaps of a few points, up to about a quarter of the observed gap.`
Δ 0.

**#23. L378-382. Fields: a semicolon joins two number-heavy clauses.**
Current: `and astrophysics (\R{arxiv_its.astro-ph.excess}); computer science exceeds mathematics by`
Replace: `and astrophysics (\R{arxiv_its.astro-ph.excess}). Computer science exceeds mathematics by`
Δ 0.

**#24. L383. Vague "This", and "CS" is used only here.**
Current: `This is the high-CS, low-mathematics ordering that prevalence studies report \citep{liang2024mapping}.`
Replace: `Prevalence studies report the same ordering \citep{liang2024mapping}.`
Δ -5.

**#25. L383-390. An implied-prevalence sentence of about 70 words, followed by a vague "That".**
Current: `Through the mixture identity (\S\ref{sec:mso}), the 2024 values imply that \R{robustness_v4.implied.cs_2024_alpha_cv}\% of computer-science and \R{robustness_v4.implied.math_2024_alpha_cv}\% of mathematics abstracts were LLM output if nothing else had changed (\R{robustness_v4.implied.cs_2024_alpha_lomo}\% and \R{robustness_v4.implied.math_2024_alpha_lomo}\% using held-out-generator recall), against prevalence estimates of 17.5\% and 4.9\% of abstract sentences by February 2024 \citep{liang2024mapping}. The implied shares are larger, with the same ordering. That is expected if a document moves into the region when only some of its sentences are LLM-revised,`
Replace: `If nothing else had changed, the mixture identity (\S\ref{sec:mso}) would imply that \R{robustness_v4.implied.cs_2024_alpha_cv}\% of computer-science and \R{robustness_v4.implied.math_2024_alpha_cv}\% of mathematics abstracts were LLM output in 2024 (\R{robustness_v4.implied.cs_2024_alpha_lomo}\% and \R{robustness_v4.implied.math_2024_alpha_lomo}\% using held-out-generator recall). \citet{liang2024mapping} estimate 17.5\% and 4.9\% of abstract sentences by February 2024, the same ordering at lower levels. Larger implied shares are expected if a document moves into the region when only some of its sentences are LLM-revised,`
Δ -3.

**#26. L430-433. About 55 words, with a colon and an interrupted "not, as far as is documented,".**
Current: `reflects models that are unlikely to have learned their style from post-ChatGPT scientific writing: their pretraining data predate ChatGPT, and their 2023 instruction tuning used annotator data or shared ChatGPT conversations, not, as far as is documented, recent abstracts.`
Replace: `reflects models unlikely to have learned their style from post-ChatGPT scientific writing. Their pretraining data predate ChatGPT, and their 2023 instruction tuning used annotator data or shared ChatGPT conversations and, as far as is documented, no recent abstracts.`
Δ -2.

**#27. L439-443. Overclaim and an unclear referent. "Its parts agree" describes 3.5 pp against 7.4-8.6 pp; the next sentence concedes the gap. "the larger estimate" is ambiguous.**
Current: `Its parts agree: the RAID models alone, with summary-style outputs kept (\R{arxiv_vintage.pre2022data.gap}\pp) or with ChatGPT added (\R{arxiv_vintage.pre2022data_plus_chatgpt.gap}\pp), and the two small local models alone, run on exactly our prompts (\R{arxiv_vintage.old_open_p1.gap}\pp, CI \R{arxiv_vintage.old_open_p1.gap_lo}--\R{arxiv_vintage.old_open_p1.gap_hi}). Three quarters of the region's training texts come from RAID, so the larger estimate leans on RAID's prompt.`
Replace: `Its subsets point the same way but differ in size: the RAID models alone give \R{arxiv_vintage.pre2022data.gap}\pp{} with summary-style outputs kept and \R{arxiv_vintage.pre2022data_plus_chatgpt.gap}\pp{} with ChatGPT added, and the two small local models, run on exactly our prompts, give \R{arxiv_vintage.old_open_p1.gap}\pp{} (CI \R{arxiv_vintage.old_open_p1.gap_lo}--\R{arxiv_vintage.old_open_p1.gap_hi}). Three quarters of the region's training texts come from RAID, so the pooled estimate leans on RAID's prompt.`
Δ +3 (+).

**#28. L444-445. "the controlled estimate" is opaque; it means the two local models run on our prompts.**
Current: `though the controlled estimate is small.`
Replace: `though the estimate from our own prompts is small.`
Δ +2.

**#29. L450-455. "each generator" is inaccurate, because the 2026 model has not turned down. The sentence runs to about 75 words with a colon and a semicolon.**
Current: `Followed quarter by quarter, overlap with each generator rises and then turns down, and the turning point tends to come later for later generators (Figure~\ref{fig:vintage}b): it peaked between 2024Q3 and 2025Q2 under the 2023 models, in 2025Q2--Q3 under the 2024 models, in 2025Q4 under Gemma~3, Granite~3.3 and Qwen3, and in 2026Q1--Q2 under gpt-oss, Qwen3.5 and Granite~4.2; under the 2026 model it was still rising in 2026Q3.`
Replace: `Quarter by quarter, overlap with each generator but the 2026 model rises and then turns down, and the turning point tends to come later for later generators (Figure~\ref{fig:vintage}b). It peaked between 2024Q3 and 2025Q2 under the 2023 models, in 2025Q2--Q3 under the 2024 models, in 2025Q4 under Gemma~3, Granite~3.3 and Qwen3, and in 2026Q1--Q2 under gpt-oss, Qwen3.5 and Granite~4.2. Under the 2026 model it was still rising in 2026Q3.`
Δ +3 (+).

**#30. L457-460. "was chosen after a first one:" is cryptic.**
Current: `This analysis is exploratory and was chosen after a first one: the rank correlation between release date and the 2025-to-2026 change is`
Replace: `This analysis is exploratory. We chose it after a first test, the rank correlation between release date and the 2025-to-2026 change, which is`
Δ +1.

**#31. L471-474. "fared better" is vague, and "a clear rise against a fall" is cryptic.**
Current: `Within families, the newer model fared better in all three pairs; measured from 2025Q4, only Granite shows a clear rise against a fall (Granite~3.3`
Replace: `In all three same-family pairs, the newer model's change was higher. Measured from 2025Q4, only in the Granite pair does the newer model rise while the older falls (Granite~3.3`
Δ +3 (+). Check that "change was higher" is what "fared better" meant.

**#32. L475-476. "rather than" pivot, and "points to" asserts more than a rank ordering of 18 points supports.**
Current: `Release date sorts them better, which points to the style of recent post-training rather than to the recency of pretraining data.`
Replace: `Release date sorts them better, consistent with an effect of recent post-training more than of pretraining-data recency.`
Δ -5.

**#33. L480-483. Vague "mixes these", and the abstract's aphorism repeated nearly verbatim.**
Current: `The aggregate 14-generator series in Figure~\ref{fig:ts}a mixes these: it still rose in 2026, carried by gpt-oss and the 2026 model, while 12 of its 14 single-generator regions fell. Because overlap tends to turn down later the more recent the generator, a reference set that is not refreshed will eventually show the shift receding, even if writing keeps moving.`
Replace: `The aggregate 14-generator series (Figure~\ref{fig:ts}a) still rose in 2026, carried by gpt-oss and the 2026 model, although 12 of its 14 single-generator regions fell. Since overlap turns down later for later generators, a fixed reference set will eventually show the shift receding, even if writing keeps moving.`
Δ -9.

**#34. L503-506. The parenthetical is misattached. "(for the pre-ChatGPT-data generators from X% to Y%)" gives marker shares (`m2022`, `m2025`), but it follows the style-overlap clause, so it reads as style overlap.**
Current: `rose from 2022 to 2025, as did style overlap under every generator except Cohere's chat model (for the pre-ChatGPT-data generators from \R{arxiv_vintage.pre2022data_matched.m2022}\% to \R{arxiv_vintage.pre2022data_matched.m2025}\%).`
Replace: `rose from 2022 to 2025 (for the pre-ChatGPT-data generators, from \R{arxiv_vintage.pre2022data_matched.m2022}\% to \R{arxiv_vintage.pre2022data_matched.m2025}\%), as did style overlap under every generator except Cohere's chat model.`
Δ 0.

**#35. L508. Semicolon split.**
Current: `including gpt-oss and Qwen3.5, under which style overlap rose; it kept rising only for Granite~4.2`
Replace: `including gpt-oss and Qwen3.5, under which style overlap rose. It kept rising only for Granite~4.2`
Δ 0.

**#36. L511-513. Redundant restatement of the previous sentence plus an over-general aphorism. "lexical measures recede earlier than stylistic ones" generalises from two generators.**
Current: `Marker shares thus turned down in 2026 for most generators, including recent ones, while style overlap with gpt-oss and Qwen3.5 kept rising: lexical measures recede earlier than stylistic ones, so a falling marker share is not on its own evidence that writing stopped moving.`
Replace: `For these generators, lexical measures turned down before stylistic ones, so a falling marker share does not by itself show that writing stopped moving.`
Note: the hedge "For these generators" narrows the claim; it does not add one. Δ -19. This is the largest single saving.

**#37. L528-535. Learner essays: a colon-led aphorism closes the paragraph, and "these school learners" is unclear next to the TOEFL takers.**
Current: `Our plan predicted higher \mso{} for English learners; it is lower (`
Replace: `Our plan predicted higher \mso{} for English learners, but it is lower (`
and
Current: `while flagging these school learners less than their peers: which learners such a detector penalises depends on how predictable their writing is (Appendix~\ref{app:learners}).`
Replace: `yet it flags the PERSUADE learners less often than their peers, because their writing is less predictable (Appendix~\ref{app:learners}).`
Note: "less predictable" is stated in App. G (L754-755), so it is not a new claim. Δ -7.

**#38. L540-542. A colon-led quotable opener, and the comparative-correlative again.**
Current: `Whether abstracts were still moving towards LLM style in 2026 depends on which LLM: overlap with each generator tended to peak later the more recent the generator, and under three`
Replace: `Whether abstracts were still moving towards LLM style in 2026 depends on the reference LLM. Overlap tended to peak later for more recent generators, and under three`
Δ -7.

**#39. L542-544. Verbatim repeat of "not on its own evidence that writing stopped moving" from L513.**
Current: `Lexical markers recede earlier: words mined from most generators, including two whose style overlap kept rising, fell in 2026, so the fall of \emph{delve} is not on its own evidence that writing stopped moving.`
Replace: `Lexical markers turned earlier: words mined from most generators, including two whose style overlap kept rising, fell in 2026, so the decline of \emph{delve} need not mean that writing stopped moving.`
Δ -1.

**#40. L548-550. A metaphor ("independent anchors"), a vague "This", and a hedged tail.**
Current: `Under either reading, LLM style and human scientific style are no longer independent anchors for each other. This is a precondition for the recursive dynamics studied in model-collapse work \citep{shumailov2024, gerstgrasser2024}, though not evidence of them.`
Replace: `Either way, LLM style and human scientific style can no longer serve as independent references for each other, a precondition for the recursive dynamics studied in model-collapse work \citep{shumailov2024, gerstgrasser2024} but not evidence of them.`
Note: L121 also uses "anchor". If this item is applied, change L121's "an anchor independent of LLM style" to "a reference independent of LLM style" for consistency. Δ -4.

**#41. L558-559. A moralising closer that repeats the Ethics statement.**
Current: `These findings argue against using any single score to judge an individual writer.`
Replace: `Neither result supports judging an individual writer by a single score.`
Δ -2.

**#42. L317 (Fig. 1 caption). A takeaway tricolon with semicolons and "far".**
Current: `(a) rises far above trend; (b) shows a small gap; (c) peaks in 2024.`
Replace: `Series (a) rises well above trend, (b) shows a small gap and (c) peaks in 2024.`
Δ +1.

**#43. L493 (Fig. 2 caption). Fine as it stands, but it is the seventh wording of the same idea. Leave it, and treat it as the canonical phrasing that items #12, #15, #33 and #38 converge on ("peak later for later/more recent generators").**

---

## Priority 3: Related Work, MSO, Data, Method

**#44. L102-111. A dangling last sentence (Kusumegi) after the "We differ" closer, and a "we differ in ...; in ...; and in ..." tricolon.**
Current (L102): `All target the share of text produced with LLM help.`
Replace: `All target the share of text produced with LLM help; LLM adoption also changes how many papers scientists produce \citep{kusumegi2025}.`
Current (L107-111): `We differ in the estimand, a thresholded overlap (the flag rate of a calibrated classifier) whose pre-ChatGPT level is itself of interest; in excluding content words from the features, since authors react to publicised markers \citep{geng2025}; and in comparing reference generators by training-data vintage. LLM adoption also changes how many papers scientists produce \citep{kusumegi2025}.`
Replace: `Our estimand differs: a thresholded overlap (the flag rate of a calibrated classifier) whose pre-ChatGPT level is itself of interest. We also exclude content words from the features, since authors react to publicised markers \citep{geng2025}, and compare reference generators by training-data vintage.`
Δ -3 overall.

**#45. L114-117. Stacked semicolons.**
Current: `\citep{padmakumar2024, doshi2024, anderson2024homog}; LLM rewriting compresses stylistic variance \citep{sourati2025}; preference tuning reduces output diversity`
Replace: `\citep{padmakumar2024, doshi2024, anderson2024homog}, and LLM rewriting compresses stylistic variance \citep{sourati2025}. Preference tuning reduces output diversity`
Δ +1.

**#46. L138. An orphaned sentence at the end of the paragraph, cut off from the perception literature it qualifies.**
Current: `so a style region depends on the models that define it. We collect no human judgements.`
Replace: `so a style region depends on the models that define it.` Then append to L132's first sentence: `Readers misjudge machine text \citep{clark2021, jakesch2023, casal2023, gao2023}; we collect no human judgements.`
Δ 0.

**#47. L163. "agnostic" is jargon with a ChatGPT flavour.**
Current: `It is agnostic to authorship:`
Replace: `It says nothing about authorship:`
Δ +1.

**#48. L179-184. The archive list carries two nested semicolons inside a parenthesis, then a long semicolon sentence ends in "X rather than Y".**
Current: `For each of eight arXiv archives (cs, math, stat, eess, q-bio, econ, astro-ph, cond-mat; by primary category; we use ``field'' for archive below) and each month from January 2015 to September 2026, we fetched all papers submitted in one randomly placed window of consecutive days through the arXiv API and drew up to 200 at random. Field-months with at least 200 papers therefore carry equal weight; smaller fields (economics in particular) contribute fewer documents, more so in early years, so the overall series is an average over a stratified sample rather than over the arXiv population.`
Replace: `We sampled eight arXiv archives by primary category (cs, math, stat, eess, q-bio, econ, astro-ph, cond-mat; ``fields'' below). For each field and each month from January 2015 to September 2026, we fetched through the arXiv API all papers submitted in one randomly placed window of consecutive days and drew up to 200 at random. Field-months with at least 200 papers therefore carry equal weight. Smaller fields, economics in particular, contribute fewer documents, especially in early years, so the overall series averages a stratified sample and does not represent the arXiv population.`
Δ +1.

**#49. L210-214. "which give ... and pair with" is ambiguous; it is unclear what pairs with what.**
Current: `Five further open models were added after review for the vintage analysis only: two whose pretraining data predate ChatGPT and three released in 2026, which give the 2026 comparison a second source with logged decoding and pair with 2025 models of the same families.`
Replace: `Five further open models were added after review, for the vintage analysis only: two whose pretraining data predate ChatGPT and three released in 2026. The latter give the 2026 comparison a second source with logged decoding, and each pairs with a 2025 model of the same family.`
Δ +3 (+).

**#50. L262-266. A 70-word cleaning sentence. Its "which would otherwise" clause has an ambiguous antecedent (Unicode? the difference?).**
Current: `All texts pass through the same normalisation: chat wrappers (``Here's the abstract:''), lines echoing the prompt's title, markdown and trailing notes are removed; typographic variants and mis-decoded characters are mapped to plain equivalents; LaTeX math becomes a placeholder and LaTeX dashes (\texttt{-{}-}, \texttt{-{}-{}-}) become Unicode dashes, since human arXiv abstracts write them in LaTeX while chat models emit Unicode, which would otherwise separate the sources by encoding alone.`
Replace: `All texts are normalised alike. We remove chat wrappers (``Here's the abstract:''), lines echoing the prompt's title, markdown and trailing notes, and map typographic variants and mis-decoded characters to plain equivalents. LaTeX math becomes a placeholder and LaTeX dashes (\texttt{-{}-}, \texttt{-{}-{}-}) become Unicode dashes: human arXiv abstracts write dashes in LaTeX and chat models in Unicode, a difference that would otherwise separate the sources by encoding alone.`
Δ +2 (+).

**#51. L272-273. Semicolon split.**
Current: `(\texttt{en\_core\_web\_sm}); features present in fewer than 1\% of training documents are dropped`
Replace: `(\texttt{en\_core\_web\_sm}). Features present in fewer than 1\% of training documents are dropped`
Δ 0.

**#52. L278-280. A dangling appositive. "the statistic behind perplexity-based detectors" follows a parenthesis about GPT-2 and seems to describe it.**
Current: `a one-feature isotonic classifier on the mean token negative log-likelihood of the essay under a small causal language model (Qwen2.5-0.5B, or \gptii{} small, whose training data predate the TOEFL and PERSUADE releases), the statistic behind perplexity-based detectors.`
Replace: `a one-feature isotonic classifier on mean token negative log-likelihood, the statistic behind perplexity-based detectors, under a small causal language model (Qwen2.5-0.5B, or \gptii{} small, whose training data predate the TOEFL and PERSUADE releases).`
Δ -3.

**#53. L290-292. "over that trend" has no antecedent, "fake break" is informal, and the break date is never stated. In the code (`code/analysis.py` L679) the break falls in the January after training ends.**
Current: `Drift placebos train the instrument on human abstracts up to 2016, 2017 or 2018 only and test for a gap in June 2022 over that trend, 41 to 65 months after the fake break and before any LLM writing assistance, so any gap they show reflects instrument ageing.`
Replace: `Drift placebos train the instrument only on human abstracts up to 2016, 2017 or 2018, place a break in the following January and test for a gap in June 2022, 41 to 65 months later and before any LLM writing assistance, so any gap they show reflects instrument ageing.`
Δ +1.

**#54. L295-299. The second instrument ("and one on generators whose ...") is buried in a long sentence.**
Current: `To separate generators by vintage at a fixed task we train one instrument per generator on its title-only (P1) outputs (RAID outputs are title-based) and one on generators whose pretraining data predate ChatGPT (the \emph{pre-ChatGPT-data region}): GPT-4 and Llama-2-Chat 70B from RAID plus Llama-2-Chat~7B and Vicuna~7B run locally on P1.`
Replace: `To compare vintages on a fixed task, we train one instrument per generator on its title-only (P1) outputs (RAID outputs are title-based). A further instrument pools the generators whose pretraining data predate ChatGPT (the \emph{pre-ChatGPT-data region}): GPT-4 and Llama-2-Chat 70B from RAID, plus Llama-2-Chat~7B and Vicuna~7B run locally on P1.`
Δ 0.

---

## Back matter (outside the page budget)

**#55. L573-577 (Limitations). One sentence of about 70 words mixes two unrelated limitations, joined by a semicolon. "or, for RAID, decoding" dangles after a long parenthesis.**
Current: `The vintage comparison holds the prompt fixed but not output length (median \R{arxiv_generator_lengths.single:vicuna:7b.median_words} to \R{arxiv_generator_lengths.single:raid-gpt4.median_words} words for Vicuna, Llama-2-Chat 7B and GPT-4, whose outputs are the shortest, against \R{arxiv_generator_lengths.single:granite3.3:8b.median_words} to \R{arxiv_generator_lengths.single:granite4.2:8b.median_words} for the 2025--2026 open models) or, for RAID, decoding; the three 2026 open models were added after the pattern of the other generators had been seen, and`
Replace: `The vintage comparison holds the prompt fixed but not decoding (for RAID) or output length: medians range from \R{arxiv_generator_lengths.single:vicuna:7b.median_words} to \R{arxiv_generator_lengths.single:raid-gpt4.median_words} words for Vicuna, Llama-2-Chat 7B and GPT-4, whose outputs are the shortest, and from \R{arxiv_generator_lengths.single:granite3.3:8b.median_words} to \R{arxiv_generator_lengths.single:granite4.2:8b.median_words} for the 2025--2026 open models. The three 2026 open models were added after the pattern of the other generators had been seen, and`

**#56. L579-580. Semicolon split.**
Current: `and is not the arXiv population; changes in authorship,`
Replace: `and is not the arXiv population. Changes in authorship,`

**#57. L582-583. "exclude ... the field-month cluster design" is cryptic.**
Current: `Confidence intervals exclude instrument variation and the field-month cluster design.`
Replace: `Confidence intervals ignore instrument variation and clustering by field-month.`

**#58. L591-595 (Ethics). Five licences in one parenthesis, with semicolons and a nested parenthesis.**
Current: `The study uses only public datasets under their licences (arXiv metadata CC0; Australian Hansard CC~BY~4.0; PERSUADE~2.0 CC~BY-NC-SA~4.0, whose share-alike terms apply to derived data we release; RAID and the Hugging Face release of \citet{liang2023detectors}, MIT; their US 8th-grade essays come from the authors' GitHub repository, which has no licence file (its README shows an MIT badge), and derive from the Hewlett Foundation ASAP data, so we release only scores, not texts).`
Replace: `The study uses only public datasets under their licences: arXiv metadata (CC0), Australian Hansard (CC~BY~4.0), PERSUADE~2.0 (CC~BY-NC-SA~4.0, whose share-alike terms apply to derived data we release), and RAID and the Hugging Face release of \citet{liang2023detectors} (MIT). Their US 8th-grade essays come from the authors' GitHub repository, which has no licence file but whose README shows an MIT badge, and derive from the Hewlett Foundation ASAP data, so we release only scores for them, not texts.`

**#59. L606-609 (AI Use). Passive voice, and a semicolon chain with a parenthetical.**
Current: `Every citing sentence was checked against the cited work's abstract or full text by separate AI sessions, in two full passes (some sources only through metadata or mirrors); this led to rewordings, one removed citation and published versions replacing preprints.`
Replace: `Separate AI sessions checked every citing sentence against the cited work's abstract or full text in two full passes, some sources only through metadata or mirrors. The checks led to rewordings, one removed citation and the replacement of preprints by published versions.`

**#60. L609. The tense will be wrong at release.** `the human \theauthor{} will read the final paper before release` becomes false or odd once released. After the read, change it to `the human \theauthor{} read the final paper before release` (past tense). Note that "no human has edited the text" (L604) must stay true at that point.

**#61. L623-624 (App. A). "and the following" is cryptic.**
Current: `are used only for out-of-genre checks: the perplexity replication and the following. The style instrument places`
Replace: `are used only for out-of-genre checks: the perplexity replication and the style check below. The style instrument places`

**#62. L627-628 (App. A). An inverted, verbless construction.**
Current: `(3)~Decided after an arXiv pilot on partial data and before the first review: Phi-4, Granite and the 2026 model.`
Replace: `(3)~Phi-4, Granite and the 2026 model were chosen after an arXiv pilot on partial data and before the first review.`

**#63. L630-631 (App. A). The bug is not explained: why would identifying the speaker be wrong?**
Current: `(the corpus field we first used identifies the speaker)`
Replace: `(the corpus field we first used as a speech identifier identifies the speaker)`

**#64. L712-717 (App. E). Four clauses of numbers in one sentence after a colon.**
Current: `Hansard is a weak comparison, however: its gap is \R{hansard_its.threshold_06.excess}\pp{} at threshold 0.6 (CI $\R{hansard_its.threshold_06.excess_lo}$ to \R{hansard_its.threshold_06.excess_hi}), its nonparametric gap ranges from $\R{robustness_v4.hansard_pretrend.linear_to_2020}$ to \R{robustness_v4.hansard_pretrend.quadratic_2015}\pp{} across pre-trend specifications, \R{robustness_v3.hansard_placebo_grid.share_p_below_05}\% of its placebo breaks give $p<0.05$, and the 2022 change of government altered the speaker population six months before ChatGPT.`
Replace: `Hansard is a weak comparison, however. Its gap is \R{hansard_its.threshold_06.excess}\pp{} at threshold 0.6 (CI $\R{hansard_its.threshold_06.excess_lo}$ to \R{hansard_its.threshold_06.excess_hi}), and its nonparametric gap ranges from $\R{robustness_v4.hansard_pretrend.linear_to_2020}$ to \R{robustness_v4.hansard_pretrend.quadratic_2015}\pp{} across pre-trend specifications. Of its placebo breaks, \R{robustness_v3.hansard_placebo_grid.share_p_below_05}\% give $p<0.05$, and the 2022 change of government altered the speaker population six months before ChatGPT.`

**#65. L731-732 (App. F). Semicolon split.**
Current: `small next to the shift towards the LLM region; diversity of content or ideas may behave differently`
Replace: `small next to the shift towards the LLM region. Diversity of content or ideas may behave differently`

**#66. L747-755 (App. G). The longest sentence in the paper (about 110 words, three levels of parentheses, a semicolon inside a parenthesis).**
Current: `The other instruments agree in direction (Figure~\ref{fig:learners}): sentence embeddings (\R{essay_embedding_instrument.ELL.mso}\% vs \R{essay_embedding_instrument.non-ELL.mso}\%) and perplexity under \gptii{} (separating human from LLM essays with AUC \R{essay_perplexity_adjusted_gpt2.heldin_auc}, against \R{essay_instrument.cv_auc_all} for style features, so it flags \R{essay_perplexity_instrument_gpt2.all.mso}\% of all human essays; \R{essay_perplexity_instrument_gpt2.ELL.mso}\% vs \R{essay_perplexity_instrument_gpt2.non-ELL.mso}\%; odds ratio \R{essay_perplexity_adjusted_gpt2.odds_ratio}, and \R{essay_perplexity_adjusted_gpt2.odds_ratio_prof}, CI \R{essay_perplexity_adjusted_gpt2.or_lo_prof}--\R{essay_perplexity_adjusted_gpt2.or_hi_prof}, after adjusting for proficiency), because these learners' essays are \emph{less} predictable (mean token log-perplexity \R{essay_perplexity_adjusted_gpt2.mean_logppl_ell} vs \R{essay_perplexity_adjusted_gpt2.mean_logppl_nonell}).`
Replace: `The other instruments agree in direction (Figure~\ref{fig:learners}). Sentence embeddings flag \R{essay_embedding_instrument.ELL.mso}\% of learner and \R{essay_embedding_instrument.non-ELL.mso}\% of other essays. Perplexity under \gptii{} separates human from LLM essays less well than style features (AUC \R{essay_perplexity_adjusted_gpt2.heldin_auc} against \R{essay_instrument.cv_auc_all}), so it flags \R{essay_perplexity_instrument_gpt2.all.mso}\% of all human essays. It flags \R{essay_perplexity_instrument_gpt2.ELL.mso}\% of learner vs \R{essay_perplexity_instrument_gpt2.non-ELL.mso}\% of other essays (odds ratio \R{essay_perplexity_adjusted_gpt2.odds_ratio}; \R{essay_perplexity_adjusted_gpt2.odds_ratio_prof}, CI \R{essay_perplexity_adjusted_gpt2.or_lo_prof}--\R{essay_perplexity_adjusted_gpt2.or_hi_prof}, after adjusting for proficiency), because these learners' essays are \emph{less} predictable (mean token log-perplexity \R{essay_perplexity_adjusted_gpt2.mean_logppl_ell} vs \R{essay_perplexity_adjusted_gpt2.mean_logppl_nonell}).`

**#67. L761-766 (App. G). The semicolon hides the logic: the 2012 date is a caveat to the memorisation argument. A colon-led aphorism follows.**
Current: `so that contrast is unlikely to come from memorised test essays; the 8th-grade essays derive from data public since 2012. In these data a perplexity instrument penalises predictable writing: the TOEFL essays are predictable and these school learners' essays are not, so which learners such a detector flags depends on the population,`
Replace: `so that contrast is unlikely to come from memorised test essays, although the 8th-grade essays derive from data public since 2012. In these data a perplexity instrument penalises predictable writing. The TOEFL essays are predictable and the PERSUADE learners' essays are not, so which learners such a detector flags depends on the population,`

**#68. L772 (Fig. 4 caption). A tidy aphorism.** `The instruments differ in level but agree in direction.` Optional: `Levels differ across instruments; all flag learner essays less often.`

---

## README.md

**#R1. L6. A rhetorical tricolon used as a hook, with a grammatical shift in its third part.**
Current: `How much human writing sounds like AI, how much already did before ChatGPT, and *which* AI does it sound like?`
Replace: `This study asks how much human writing sounds like LLM output, how much did so before ChatGPT, and *which* LLMs it sounds like.`

**#R2. L8. Intensifier stack ("every ... all ... full").**
Current: `This repository holds the paper (`paper/preprint.pdf`), its source, every analysis, all generated data and the full audit trail for a study of`
Replace: `This repository holds the paper (`paper/preprint.pdf`), its source, the analyses, the generated data and the audit trail for a study of`

**#R3. L17-18. An overstatement. The paper reports that the never-revised restriction barely changes *yearly MSO* (§4); it does not report a trend gap for never-revised papers.**
Current: `The gap holds across trend specifications, thresholds, feature-family ablations and never-revised papers, and is far larger than any placebo or instrument-drift gap.`
Replace: `The gap holds across trend specifications, thresholds and feature-family ablations, yearly MSO barely changes when only never-revised papers are scored, and the gap is well above any placebo or instrument-drift gap.`

**#R4. L22-24. The "turn ... later for later" construction, scare quotes, and the aphorism.**
Current: `overlap rises and then turns down, and the turn **tends to come later for later-released models** (exploratory rank correlation 0.83, n = 18). A reference set that is not refreshed, like a fixed list of words such as *delve*, will eventually show the shift "fading".`
Replace: `overlap rises and then falls, and it **tends to peak later for later-released models** (exploratory rank correlation 0.83, n = 18). A fixed reference set, including a list of marker words such as *delve*, will eventually show the shift receding.`

**#R5. L25-26. The caveat from the paper is lost, and "see" anthropomorphises the detector.**
Current: `does not see the shift.`
Replace: `does not detect the shift; the original method's larger scoring models might.`

---

## Items considered and left alone

- Hedged "though" tails at L84 and L550 (#40 handles L550). Five in the main text is acceptable.
- "We therefore" at L72 and L170. Both follow a real premise; two uses in eight pages is not over-signposting.
- The comparative "about \R{...} times the extrapolated trend value" (L354-355) is clear in the PDF.
- The deviation log (App. A, items 4-6) is list-like by design. Splitting it would add length without improving clarity.
- Vocabulary-level tells ("crucially", "notably", "comprehensive", "robust", "highlight", "underscore" outside the
  marker list, "furthermore", "moreover", "landscape"). A grep of `main.tex` and `README.md` found none in prose.
