# Pre-release proofread: preprint.pdf (15 pp.)

Method: I rendered all 15 pages to PNG at 110 dpi, and Figures 1, 2 and 4 again at 200–250 dpi, and looked at each one. I extracted the text with PyMuPDF and checked it against main.tex, results/numbers.tex and references.bib. "l." is a main.tex line and "bib l." is a references.bib line.

What I checked and found clean: there are no "??" references or undefined citations, and no bib key is duplicated. Every number repeated between the abstract, body, figures, Table 3 and the conclusion matches numbers.tex: 9.2%, 25.4 pp, 7.5 pp, 0.83/18, 40.6%, 15 of 19, 17 of 19, 12 of 14, the 34 placebo breaks, and the 41–65 month and 30-month horizons. The generator counts add up (14 + 5 = 19; four pre-ChatGPT-data generators; four from 2026; 16 seen before the 2026 open models). Fig. 2b has 8 + 3 + 4 + 3 + 1 points, which matches Table 1. Every figure caption matches its plotted values.

---

## A. Errors (fix before release)

1. **p. 4, Table 1 (l. 228, 235).** The group heading "*Local; main instrument, all genres*" includes "Claude Opus 5.5 (2026 model)". That model was not run locally: §4 says it ran through sub-agent sessions, and §4 also says "the seven local models and the 2026 model".
   Fix: rename the heading to "*Main instrument, all genres (seven local models and the 2026 model)*", or give the Claude row its own sub-heading.

2. **p. 9, AI Use (l. 604).** The sentence "the human author(s) will read the final paper before release." is stale in the released version.
   Fix: "the human author read the final paper before release."

3. **p. 9, AI Use (l. 595, 604, 606).** "The human author(s)" appears three times, but the preprint names one author.
   Fix: change all three to "The human author".

4. **p. 14, App. G (l. 743–744).** "(the commit will be identified after review)" is an anonymous-review leftover in a non-anonymous preprint that gives a GitHub URL. The same claim is made on p. 2 (l. 91–92).
   Fix: give the commit hash or link, for example "(commit `abc1234` in the repository above)". Wrap it in `\ifdefined\PREPRINT` if the review version must stay anonymous.

5. **p. 7 (l. 465).** "Gemma 4 (-0.9 pp, CI −1.8 to 0.1)" uses a hyphen instead of a minus.
   Fix: `($\R{arxiv_vintage_uncertainty.single:gemma4:12b.change_seed0}$\pp, CI ...` so it renders "(−0.9 pp, CI −1.8 to 0.1)".

6. **p. 13, App. B (l. 651).** "(CI -0.1–2.9)" has a hyphen-minus and an en-dash range after a negative number.
   Fix: `(CI $\R{hansard_its.threshold_06.excess_lo}$ to \R{hansard_its.threshold_06.excess_hi})`, which renders "(CI −0.1 to 2.9)" and matches every other negative CI.

7. **p. 13, App. C (l. 666).** "(-0.11 per year)" uses a hyphen.
   Fix: `($\R{arxiv_len150_dispersion_trend.gap_2025.trend_per_year}$ per year)`, which renders "(−0.11 per year)".

8. **p. 2 (l. 103).** "Chang (2026) show that…" has a single author with a plural verb.
   Fix: "Chang (2026) shows that…".

9. **p. 14, App. E (l. 716–724).** Section "E Field results" has no body text. Its heading runs straight into "F Top features", and Figure 4 floats into the other column, so the appendix looks broken.
   Fix: add a sentence such as "Figure~\ref{fig:fields} shows pre-ChatGPT \mso{} and the June 2025 trend gap by field." Optionally use `[H]` (float package) or `\FloatBarrier`.

10. **p. 6, Figure 1a (figures/timeseries.pdf).** The legend (top left, running to "…extrapolated") overlaps the rising 2024–2026 curve and monthly points at about 35–48%.
    Fix: move the legend to the lower right (`loc="lower right"`, an empty area before 2022), or raise ylim to about 55.

11. **p. 8, Figure 2b (figures/vintage.pdf).** Two labels are misplaced, and the x-axis is confusing.
    - "Qwen3.5 9B" sits under the green gpt-oss point at about 2025.6, well left of its own red point at 2026Q1. Readers will attach it to gpt-oss. Fix: put it beside the red point at about (2026.15, 2026Q1).
    - "2026 model (still rising)" sits under the Granite 4.2 point, not next to the open circle at n/a / 2026Q3. Fix: anchor it to the open circle.
    - The x-axis has unlabelled tick marks at mid-years, while the year labels sit on the gridlines between them. Fix: put the tick marks at the labelled positions or remove the minor ticks.

12. **p. 14, Figure 4 left panel (figures/fields.pdf).** The astro-ph point (4.4%) sits on the y-axis spine, so its left whisker is clipped. Fix: set `xlim(0, …)` or start at about 3.

13. **p. 4–5, Method vs Table 2 (l. 283 vs l. 407–410).** The Method says the pre-trend start is varied "in 2017 or 2019". Table 2 reports only "trend from 2019", and no 2017 variant appears anywhere.
    Fix: add a "trend from 2017" row, or change l. 283 to "start in 2019".

14. **p. 6, Table 2 placebo rows (l. 413–414) vs §5 Time series (l. 285–286).** The rows "Break Nov 2019" and "Break Nov 2020" (gap in June 2022) are not described in the Method. The Method's grid uses even months from June 2016, so November is not on it, and each grid break is evaluated 12 months later, not in June 2022.
    Fix: add a sentence to §5, for example "Two further placebo breaks (November 2019 and November 2020) are evaluated in June 2022 (Table 2)."

15. **p. 6, Table 2 "No dash features" (l. 404).** This row is identical to the primary row in gap and CI (25.4, 23.2–27.7). numbers.tex has identical SE (1.1) and p as well (`arxiv_nodash_its.all.*` = `arxiv_its.all.*`). Please verify that this variant actually ran on the reduced feature set. If the result really is identical, say so in the text or caption ("identical to the primary estimate") so it does not look like a copy error.

16. **p. 1 and p. 2 (l. 51, l. 99).** The citations render as "Liang et al., 2024b,a". The reversed suffix order looks like an error.
    Fix: in both `\citep`s put `liang2024monitoring` before `liang2024mapping`, giving "2024a,b".

17. **p. 11, Jiang et al. (2023) reference (bib l. 368).** "Mistral 7b" should be "Mistral 7B". Fix: `title = {Mistral {7B}}`.

18. **p. 13, Zheng et al. (2023) reference (bib l. 361).** "MT-bench and chatbot arena" should be "MT-Bench and Chatbot Arena". Fix: `{MT-Bench} and {Chatbot Arena}`.

19. **p. 12, Mistral AI (2024) reference (bib l. 557).** "Mistral-7B-instruct-v0.3 model card" should be "Mistral-7B-Instruct-v0.3 model card". Fix: brace the whole name, `{Mistral-7B-Instruct-v0.3}`.

20. **p. 9, Anderson et al. (2024) reference (bib l. 31).** It renders "C&C 24" because the curly apostrophe is dropped. Fix: `series={C\&C~'24}` so it reads "C&C '24", or delete the series field.

21. **p. 13, Yakura et al. reference (bib l. 112, 114).** "arXiv:2409.01754v4" has a stray version suffix. Fix: `eprint = {2409.01754}` and use the unversioned URL.

22. **p. 11, Lee (2026) reference (bib l. 91).** "2018-2026" has a hyphen in a year range. Fix: `2018--2026`.

23. **p. 11, Katz and Alexander (2025) reference (bib l. 239–242).** The entry ends "Zenodo dataset." with no DOI or URL, so the dataset cannot be found. Fix: add the Zenodo DOI.

## B. Consistency and style

24. **Spelling (l. 111, l. 661).** "Homogenization" (paragraph heading, p. 2) and "homogenization" (App. C, p. 13) use -ize. The rest of the paper uses -ise (standardised, normalisation, regularised, summarise, publicised, penalises).
    Fix: "Homogenisation" and "homogenisation". Leave the cited title "Homogenization effects…" unchanged.

25. **"toward" ×6 (l. 68, 440, 480, 538, 561, 670).** British usage elsewhere suggests "towards". This is optional, but it is currently consistent, so change all six or none.

26. **p-value spacing (l. 335, 379, 453; App. D l. 679).** Macro values `{<}0.001` render tight ("χ2 p<0.001", "all adjusted p<0.001", "n = 18, p<0.001"). Hand-written values render spaced ("p < 0.05", "p = 0.375").
    Fix: drop the braces around `<` in the numbers.tex generator, or write the spaced form everywhere.

27. **χ² report (p. 5, l. 334–335).** "χ2 p<0.001" has no statistic. Fix: `$\chi^2(7)=354.6$, $p<0.001$` (values from `arxiv_its.baseline_field_heterogeneity`).

28. **"Llama-2-70B-chat" vs "Llama-2-Chat 7B" (Table 1 l. 223/238; l. 293, 427, 428).** The same family is capitalised two ways. Use one style, for example "Llama-2-70B-Chat" and "Llama-2-7B-Chat", or note that the first is RAID's label.

29. **Table 1 "Released" column (l. 222–242).** The formats are mixed ("2023", "2024-05", "2026-Q1", "2026") and centred, so the column looks ragged. With `\tabcolsep` 2pt the Released and Cutoff columns touch ("2024-07 Dec 2023", "2023-07 Sep 2022"). Fix: left-align and raise `\tabcolsep` to 4pt.

30. **Table 4 (l. 731).** Same cramping: "NOUN_VERB_SCONJ 0.32", "PUNCT_PRON_NOUN 0.32", "sentence length (mean) −0.42". Increase `\tabcolsep`. Optionally render "punctuation ," as "punctuation (comma)".

31. **p. 2 (l. 77).** "(§4–5)" should be "(§§4–5)".

32. **p. 4 (l. 206).** "(see AI Use)" should be "(see AI Use and Authorship)", the actual section title.

33. **p. 5 (l. 322).** Appendix A is never named in the text; it is reached only via "Table 3". Fix: "Table~\ref{tab:lomo} in Appendix~\ref{app:lomo}".

34. **Appendix order.** Appendices are first referenced in the order G (p. 2), F (p. 4), A (p. 5), E (p. 5), B, C, D (p. 8). Optionally reorder to follow first mention.

35. **App. G numbering (l. 761).** The list runs "(5b)" then "(6)" and "(7)". Renumber to (6), (7), (8).

36. **Table 2 label (l. 401) vs text (l. 338, 353).** The table says "No math notation"; the text says "abstracts without math". Use one term, for example "Abstracts without math".

37. **"about 2.09 times" (p. 5, l. 351; p. 13, l. 645).** "About" with two decimals is over-precise. Fix: "about 2.1 times" (and "0.2 … against 2.1" in App. B), or drop "about".

38. **p. 7 (l. 470–471).** "Granite 3.3 −3.9 pp, Granite 4.2 2.9 pp" puts two numbers side by side. Fix: "Granite 3.3: −3.9 pp; Granite 4.2: +2.9 pp".

39. **p. 7 (l. 509).** "even for most recent generators" is ambiguous: it can read as "the newest generators". Fix: "even for most of the recent generators".

40. **p. 4 (l. 275–276).** "(Qwen2.5-0.5B, and GPT-2 small, whose training data predate…)" lets "whose" seem to cover both models. Fix: "(Qwen2.5-0.5B; or GPT-2 small, whose training data predate…)".

41. **p. 3 (l. 197).** "In every genre half of the pre-ChatGPT documents" needs a comma. Fix: "In every genre, half of the pre-ChatGPT documents".

42. **p. 15 (l. 759).** "the cs–mathematics contrast" mixes an archive code with a field name. Fix: "the computer science–mathematics contrast".

43. **"vs" and "versus" are mixed** (for example l. 527 "2.3% vs 4.2%" and l. 676 "2.3% versus 4.2%"). Pick one.

44. **"n=666" vs "n = 18".** Fig. 3 caption (l. 710) uses unspaced plain text; §6.4 uses math. Use `$n=\R{…}$` in the caption.

45. **Hyphenation at line breaks.** p. 6 breaks "Chat-GPT" (§6.4 run-in heading). p. 4 and p. 5 break "GPT-/2 small".
    Fix: add `\hyphenation{ChatGPT}` to the preamble, and write `GPT\nobreakdash-2` or `\mbox{GPT-2}` at l. 275 and l. 360.

46. **Loose, underfull lines** with visible gaps between words:
    - p. 3, "arXiv abstracts. For each of eight arXiv"
    - p. 6, "The pre-ChatGPT-data region (GPT-4, Llama-2-70B-chat,"
    - p. 8, run-in headings "Trajectories depend on the reference." and "Implications for detection."
    - References: IBM Granite Team, LMSYS, Google DeepMind 2025 and Mistral AI (long URLs)

    Light rewording, `\sloppy` locally, or `\usepackage{xurl}` for the reference URLs would help.

47. **Figure 2a (vintage.pdf).** The legend says "Open models 2024-25"; use an en dash: "2024–25". The panel title "(a) Region defined by" reads as truncated; use "(a) Region defined by generator set" or make "Region defined by" the legend title. The x ticks "2015 2018 2021 2024 2026" are unevenly spaced and "2024 2026" crowd each other; use 2015, 2018, 2021, 2024, or label every second year.

48. **Figure 2b colours.** 2024 (amber) and 2026 (orange-red) are hard to tell apart in print and for colour-vision deficiency. Optional: use a more distinct hue for one of them.

49. **Reference initials.** Initials are missing their full stop:
    - "Barrett R Anderson" (bib l. 31)
    - "Christopher D Manning" (bib l. 37)
    - "Byron C Wallace" (bib l. 261)
    - "J Zico Kolter" (bib l. 516)

    Fix: "R.", "D.", "C.", "J.".

50. **Crossley et al. (2024) reference (bib l. 237).** It uses initials only, with no space in "S.A.", while every other entry has full names. Fix: "Scott A. Crossley, Yu Tian, Perpetual Baffour, Alex Franklin, Meg Benner, Ulrich Boser" (verify against the DOI).

51. **Title capitalisation in references.**
    - Geng and Trotta (2025) renders "Human-LLM Coevolution: Evidence" (bib l. 70). Use sentence case with an en dash: `{Human--LLM} coevolution: {E}vidence from academic writing`, matching Bentley's "Human–LLM".
    - Hans et al. (2024) renders "Binoculars: zero-shot" (bib l. 264), lowercase after the colon, while other entries capitalise there ("Fast-DetectGPT: Efficient"). Use `{Z}ero-shot`.
    - IBM Granite Team renders "8B instruct". Use `{Instruct}`.

52. **NeurIPS formatting is inconsistent.**
    - Krishna et al. (bib l. 202): "Advances in Neural Information Processing Systems 36, NeurIPS 2023, … Neural Information Processing Systems Foundation, Inc. (NeurIPS)"
    - Pillutla and Zheng: "…Systems, volume 34/36, … Curran Associates, Inc."

    Make Krishna match the other two.

53. **Model-card notes are ad hoc and inconsistent:**
    - "V1.5 released August 2023 (…)" (bib l. 536). The capital "V" comes from sentence-casing; use `{v1.5}`.
    - "Hugging Face repository created 22 May 2024" (bib l. 562)
    - "Released 29 April 2025 (…)" (bib l. 545)
    - "Granite 3.3: <url>" (bib l. 467). This entry's printed URL is the org page, while the title link points to Granite 4.2.

    Standardise them, for example drop the notes and give one URL each (plus an access date if wanted).

54. **Corporate authors.** "Google" (Gemma releases) and "Google DeepMind" (Gemma 3/4 cards) are both used. Pick one if both are the same source.

55. **Sourati et al. (2026) reference (bib l. 133).** "Nature Human Behaviour." has no volume, pages or DOI in print. Add the DOI (10.1038/s41562-026-02550-0) or "Advance online publication".

56. **Abstract length (l. 30–46).** It is about 225 words. ACL guidance is 200 words or fewer. This is optional for an archive preprint; the shortest cut is the sentence "Because recent LLMs are trained on recent writing, we compare reference generators by vintage."

57. **Author block (l. 22).** The GitHub URL ends in a hyphen ("…/Sounding-Like-Which-AI-"), which looks like a truncation. Please confirm it is the exact repository name; if it is, it may still be worth renaming the repository before DOI archiving.

58. **Runt lines.** "them." (p. 8, end of the Discussion's first paragraph) and "author." (p. 9, end of AI Use) are single-word last lines. This is cosmetic and optional.

59. **p. 4.** Large empty space between the Table 1 caption and "and 'avoid typical AI phrasing'". This is cosmetic: `[t]` placement plus a short caption block. Optionally move Table 1 to `[t!]` on p. 3 or shorten the footnote list.
