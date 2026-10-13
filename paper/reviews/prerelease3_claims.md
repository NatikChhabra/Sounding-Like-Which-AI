# Pre-release audit 3: typed claims vs results, macros, figures, prose

Auditor: fresh hostile pass on commit 0795e4b (paper/main.tex, results/*, main.pdf, preprint.pdf, README.md).
Method: every \R key used in main.tex was resolved against results/numbers.tex (412 keys, none missing); every
typed count, list, ordering and direction was checked against results/*.csv|json; all 16 pages were rendered at
150 dpi and the figure PDFs at 200 dpi; a scratch copy was compiled with tectonic `--keep-logs` to get a log
(the repo has no main.log). The project files were not edited.

Counts: **Blocking 2 · Important 11 · Minor 24 · Verified: about 70 typed claims (listed at the end)**

---

## Blocking

### B1. Limitations: the length sentence names the wrong "shortest" generators
> "medians range from 102 to 110 words for Vicuna, Llama-2-Chat 7B and GPT-4, whose outputs are the shortest, and from 138 to 186 for the 2025--2026 open models."

Evidence (`results/arxiv_generator_lengths.csv`, median_words): MPT-30B-chat **90** is the shortest of all 19.
Vicuna 102, Llama-2-Chat 7B 105, GPT-4 110. **Llama-2-Chat 70B, the fourth member of the pre-ChatGPT-data region, is
250**, which is the truncation length and the longest of all. Other RAID models: ChatGPT 121, Cohere 129, Mistral-chat 134.
The sentence therefore suggests the pre-ChatGPT-data region is uniformly short, when it holds both the shortest
local outputs and the longest outputs overall.
Also, 138 comes from 138.5 (Granite 3.3), rounded half to even.

Fix (copy-ready):
> "medians range from \R{...vicuna:7b.median_words} words (Vicuna) to 250, the truncation length (Llama-2-Chat 70B), within the pre-ChatGPT-data region, from 90 (MPT-30B-chat) to 134 for the other RAID models, and from \R{...granite3.3:8b.median_words} to \R{...granite4.2:8b.median_words} for the 2025--2026 open models."

(Use `\R{arxiv_generator_lengths.single:raid-llama-chat.median_words}` and `...raid-mpt-chat...` / `...raid-mistral-chat...` instead of typing the numbers.)

### B2. Limitations says the prompt is fixed, which contradicts §6.4 for RAID
> Limitations: "The vintage comparison holds the prompt fixed but not decoding (for RAID) or output length"

§6.4 says the opposite: "the two small local models, run on exactly our prompts" and "the pooled estimate leans on
RAID's prompt". §5 says only that RAID outputs are "title-based". RAID used its own prompt wording, so only the
*task* (an abstract from a title) is fixed. The 2026 model also had no decoding control.

Fix:
> "The vintage comparison holds the task (an abstract from a title) fixed, but not the prompt wording or decoding for RAID, decoding for the 2026 model, or output length:"

---

## Important

### I1. "cannot explain the timing" is too strong for Qwen3.5 (§6.4, Discussion, README)
> §6.4: "All three 2026 open models peaked before or in the quarter of their release (Gemma~4 12B, released in June 2026, in 2025Q4), so authors' use of them cannot explain the timing."
> Discussion: "The 2026 open models peaked before or as they were released, so authors' use of them cannot explain their peaks"
> README: "The three 2026 open models peaked before or as they were released, so authors using them cannot explain it."

Evidence: `arxiv_vintage_quarterly.csv`. Qwen3.5's peak is 2026Q1, its release quarter (code `RELEASE` 2026.17, about
early March), so the peak quarter includes weeks after the release. Its 80% bootstrap range is **2026Q1–2026Q2**,
which extends past the release. Granite 4.2 (range 2026Q1–Q2, released Aug) and Gemma 4 (2025Q4–2026Q1, released Jun)
do support the claim. The Discussion sentence also repeats the §6.4 sentence almost word for word.

Fix (§6.4):
> "Gemma~4 and Granite~4.2 peaked before their release (Gemma~4 12B, released in June 2026, in 2025Q4) and Qwen3.5 in its release quarter, so authors' use of these models can explain little of the timing."

Discussion: delete "The 2026 open models peaked before or as they were released, so authors' use of them cannot explain their peaks;" and start the sentence with "These models may have learned from recent writing, or ...".
README: "Two of the three 2026 open models peaked before they were released and the third in its release quarter, so authors using them can explain little of it."

### I2. The aggregate's 2026 rise is attributed to two generators without evidence, and the evidence that exists says something different
> "The aggregate 14-generator series (Figure~\ref{fig:ts}a) still rose in 2026, carried by gpt-oss and the 2026 model, although 12 of its 14 single-generator regions fell."

The count is correct: of the 14, only gpt-oss and the 2026 model rose (`arxiv_vintage.csv`). The attribution is untested, though.
`results/arxiv_gensets.csv`:
- without the 2026 model (13 generators) the aggregate **fell** in 2026: 37.9% to 36.8%. The 2026 model alone turns the headline 2026 rise (40.6% to 44.7%) into a fall, and that model also drafted the paper.
- the seven local models pooled over P1–P3 (`local`) **rose** from 43.3% to 48.4%, although six of their seven title-only single regions fell. A pooled multi-prompt region does not follow its single-generator P1 regions. Contrast: `local_p1` +0.8 pp, with only 2/5 seed draws of the same sign (`arxiv_vintage_uncertainty.csv`).

Fix:
> "The aggregate 14-generator series (Figure~\ref{fig:ts}a) still rose in 2026, although 12 of its 14 single-generator regions fell. Without the 2026 model it did not rise (\R{arxiv_gensets.no_frontier.y2025}\% to \R{arxiv_gensets.no_frontier.y2026}\%), and pooled regions need not follow their members' title-only regions (the seven local models pooled over all three prompts rose from \R{arxiv_gensets.local.y2025}\% to \R{arxiv_gensets.local.y2026}\%)."

(Add these keys to make_numbers if they are not already exported.) Also tone down §6.3: "The monthly series has been roughly flat since late 2025". Consider adding there that the 2026 level depends on the 2026 model.

### I3. Abstract and §6.4: "rises and then falls" rests on a single shared last quarter for the latest generators
> Abstract: "overlap with all but the newest rises and then falls"

For gpt-oss and Granite 4.2 the whole decline is 2026Q2 to 2026Q3, the last observed quarter. In that quarter **all 18 dated
generators fell together** (`arxiv_vintage_peak.json` n_fell_last_quarter = 18). A common end-of-series shock cannot be
told apart from a turn. The paper states the single-quarter fact in §6.4 but the abstract states the pattern without
qualification.

Fix (abstract):
> "overlap with all but the newest rises and then, at least for one quarter, falls, peaking later for later generators"

Alternatively add to §6.4 after "that single quarter is the whole downturn": "Because all 18 fell in that quarter, these two peaks may mark a shared fluctuation rather than a turn."

### I4. Appendix D table cannot support the "five draws" claim, and its Gemma 4 row reads as a contradiction
> §6.4: "Each change has a document-bootstrap interval that excludes zero and keeps its sign across five draws of the human training sample and ten refits on 80\% of the generator's texts (Appendix~\ref{app:peaks}), except under Gemma~4"

Table 5 shows only the subsample refits ("Same sign"). These are 10/10 for every row, **including Gemma 4**. The seed-draw count
(Gemma 4: 4/5, `arxiv_vintage_uncertainty.csv` n_seeds_same_sign) and the bootstrap CI (Gemma 4: −1.8 to 0.1) are not
in the appendix the sentence points to. A reader who checks Table 5 sees Gemma 4 as stable.

Fix: add two columns to Table 5. "CI" is `change_lo`–`change_hi` in pp and "Seeds" is `n_seeds_same_sign`/`n_seeds`. Rename "Same sign" to "Subsamples". Caption addition:
> "CI: 95\% document-bootstrap interval of the change; Seeds and Subsamples: draws of the human training sample (of 5) and 80\% refits on the generator's texts (of 10) whose change has the same sign as the estimate."

### I5. Figure 2b: labels overlap at print size
Rendered p.8: "2026 model (still rising)" is printed over "gpt-oss 20B" and runs into "Granite 4.2 8B". "Qwen3.5 9B" is partly
covered by its own marker. The three green 2025Q4 points (Gemma 3, Granite 3.3, Qwen3) carry a single label, "Qwen3 8B".
Label text is about 5 pt in print.
Fix in `code/figures.py::fig_vintage`: move the open-circle label below or left of the marker
(e.g. `ha="right", va="top"`), offset the gpt-oss label down, label the 2025Q4 cluster
"Gemma 3, Granite 3.3, Qwen3", and raise annotation fontsize to at least 7.

### I6. Figure 3 caption overstates: "The baseline does not predict the gap."
From `arxiv_baseline_pre2022.csv` and `arxiv_its.json`, the 8-field Spearman correlation of baseline with gap is about
**0.60** (computed by hand from the ranks: astro-ph lowest on both, cs/econ high baseline with cs the highest gap).
That is moderate and positive, though not significant with n = 8.
Fix:
> "The baseline is only loosely related to the gap (rank correlation about 0.6 across the eight fields)."

Export the value as a macro, or drop the sentence.

### I7. The figure that carries "still rising" is also the least separable single region
Under the 2026 model, single-region MSO was already **17.9% in 2015** (`arxiv_vintage.csv` single:claude-opus-5.5
y2015). The other dated generators range from 0.8% to 8.3%. Its CV AUC is 0.942, against at least 0.96 for every other
single region except Cohere (0.909) (`arxiv_v_single_*_instrument.json`). The one generator "still rising in 2026Q3" is
therefore also the one whose region overlaps human abstracts most, and the one with no decoding control that drafted the
paper. Limitations mentions only the session-grouping issue.
Add to Limitations:
> "The 2026 model's single region is the least distinct from human abstracts (\R{arxiv_vintage.single:claude-opus-5.5.y2015}\% of 2015 abstracts fall in it, against at most \R{arxiv_vintage.single:raid-cohere-chat.y2015}\% for any other generator)."

### I8. Reference list misspells an author: "Emke-Ágnes Horvát" (Kobak et al. 2025)
The tectonic log reports `Missing character: There is no ő ("151) in font ptmr8t!`, so "Emőke" prints as "Emke" (p.11).
Fix `paper/references.bib` line 1: `Horv{\'a}t, Em{\H{o}}ke-{\'A}gnes`. Add `Missing character` to the
`Select-String` filter in `paper/build.ps1` so this cannot recur silently.

### I9. Abstract and intro state the learner result without its main qualifier
> Abstract: "In student essays, English learners' writing is less machine-like than their peers'."

The style result rests on **15** in-region learner essays (`essay_ell_counts.json`). After adjusting for proficiency the OR is
0.87 (CI 0.50–1.52), and Appendix H says "Most of the difference is proficiency". Only the GPT-2 instrument stays
significant after adjustment (0.66, CI 0.52–0.85).
Fix (abstract):
> "In student essays, English learners' writing is less machine-like than their peers', mostly because of proficiency."

### I10. Table 1 omits release months that the analysis uses
The Table 1 caption promises "release month", but the six RAID rows give only "2023" and Qwen3.5 gives "2026-Q1". The rank correlation
uses specific months from `code/analysis.py` `RELEASE`: GPT-4, ChatGPT and MPT 2023.45; Llama-2-Chat 2023.55;
Mistral-Instr. v0.1 2023.7; Cohere 2023.85; Qwen3.5 2026.17. These months are unsourced in the paper. The result is robust:
ρ = 0.83 if all RAID models are tied at mid-2023, and 0.82 without Cohere (computed in this audit).
Fix: add the months to Table 1 with sources, or add to §6.4:
> "(RAID release months are approximate; tying all six at mid-2023 gives 0.83)".

### I11. Acknowledgements make a time-bound statement that is false once released
> "Citations were not checked by a human; the human \theauthor{} will read the final paper before release."

This matches README "Status: pre-release draft: not yet read or approved by the author". At release both must be
updated to state what the author actually read and approved, or the released preprint carries a stale claim. This item
gates the release.

---

## Minor

M1. §6.4 enumeration omits Gemma 4, but reads as complete:
"It peaked between 2024Q3 and 2025Q3 under the 2023 models other than Cohere's, in 2025Q2–Q3 under the 2024 models, in 2025Q4 under Gemma~3, Granite~3.3 and Qwen3, and in 2026Q1–Q2 under gpt-oss, Qwen3.5 and Granite~4.2."
Fix: "... in 2025Q4 under Gemma~3, Granite~3.3, Qwen3 and Gemma~4, and in 2026Q1–Q2 under gpt-oss, Qwen3.5 and Granite~4.2." Then shorten the later parenthesis to "(Gemma~4 12B, released in June 2026)".

M2. "From 2026Q2 to 2026Q3, overlap fell under all 18 generators but the 2026 model" is ambiguous. Fix: "under all \R{arxiv_vintage_peak.n_fell_last_quarter} generators other than the 2026 model".

M3. Marker/style peak counts sum to 18, not 19 (the 2026 model is silently excluded; its marker and style peaks coincide in 2026Q3). Fix: "...for 7 of the 18 dated generators, later for 6 and in the same quarter for 5".

M4. "In all three same-family pairs, the newer model's change was higher." This is true on annual means and from 2025Q4. The Gemma pair differs by 1.2 pp (−2.0 vs −0.9), within Gemma 4's CI, which includes zero. Fix: "...was higher (by 1.2 pp only for Gemma)".

M5. The RAID subset sentence is unclear about filtering: "the RAID models alone give 8.6pp with summary-style outputs kept and 7.4pp with ChatGPT added". The 7.4 also keeps summaries. With summaries dropped, RAID alone gives 7.3 (`pre2022data_abstract_register`). Fix: "...give \R{arxiv_vintage.pre2022data_abstract_register.gap}\pp{} (\R{arxiv_vintage.pre2022data.gap} with summary-style outputs kept, \R{arxiv_vintage.pre2022data_plus_chatgpt.gap} with ChatGPT added and summaries kept)".

M6. Figure 2a legend: "Open models 2024–25" (`local_p1`) includes gpt-oss, which is also drawn separately as "gpt-oss (Aug 2025)". Relabel "Open models 2024–25 (incl. gpt-oss)" or drop gpt-oss from that set. The "RAID 2023 chat models" line (`raid_all`) keeps summary-style outputs (17% of texts) and so is inconsistent with §5. Say so in the caption.

M7. Figure 4: "$n=\R{essay_mso_by_group.non-ELL.n}$" renders as "n = 6, 758" (math-mode comma). Fix: drop the math mode for the number, `$n={}$\R{...}`, or have make_numbers emit `6{,}758`.

M8. BibTeX: 6 warnings `string name "july"/"june" is undefined` (references.bib lines 1, 3, 7, 31, 237, 257: `month=July`/`June` unbraced), so those months are silently dropped. Fix: `month=jul` / `month=jun`.

M9. "the original method's larger scoring models may not miss the shift" is a double negative and a hedge. Fix: "larger scoring models, as in the original method, might detect it." Also "does not rise (8.3\% in 2015, 5.3\% in 2026)" understates the result: it *falls* from 11.3% in 2022 (`arxiv_fastdetect.csv`). Fix: "falls (\R{arxiv_fastdetect.2022.share_flagged}\% in 2022, \R{...2026...}\% in 2026)".

M10. "scoring only never-revised papers barely changes yearly MSO (2026: 44.7% vs 44.7%)" picks the year with the fewest revisions (75.6% never revised). 2024 is the informative year: 27.0 vs 27.8 (`robustness_v5.json`). Fix: "(2024: \R{robustness_v5.never_revised.mso_never_y2024}\% vs \R{robustness_v5.never_revised.mso_all_y2024}\%; 2026: ...)".

M11. "abstracts without math give a similar ordering": math moves from the third-lowest field to the sixth (9.1% to 10.9%; `arxiv_baseline_pre2022.csv` nomath rows); only the extremes hold. Fix: "abstracts without math keep astrophysics lowest and economics highest".

M12. §6.6 Hansard contrast: "the arXiv gap exceeds it by 30.7 pp ... with both regions built from the same generators". Readers will subtract 25.4 − 1.3 and get 24.1. Fix: insert "(arXiv gap \R{control_difference.arxiv_excess}\pp{} with those eight generators)".

M13. "Local models answered three prompt styles, 150 prompts each" is not exact for Hansard: gemma3 P1/P2 157/141, llama3.1 158/156/155, qwen3 152/155/156 (`F:\research-data\llm_hansard.jsonl`). Fix: "about 150 prompts each (141–158 for speech)".

M14. Ethics: "models of 7 to 20 billion parameters". gpt-oss-20b has about 21B total parameters (3.6B active) per its model card. Fix: "7 to 21 billion". Also the licence list names "Gemma Terms of Use for Gemma~3" but not Gemma 4, which falls under "Apache 2.0 or MIT for the others". Verify Gemma 4's licence and name it.

M15. Discussion: "the commercial models in use, which we did not run" is inaccurate. RAID's GPT-4 and ChatGPT outputs and the 2026 model are commercial. Fix: "the commercial models authors used in 2024–2026, which we did not run apart from the 2026 model".

M16. Discussion overreach: "LLM style and human scientific style can no longer serve as independent references for each other". The paper itself keeps the pre-ChatGPT-data region as such a reference. Fix: "recent LLMs and recent scientific writing can no longer serve as independent references for each other".

M17. "the 2026 model is excluded because its release month is not used" is circular. Fix: "because its release month is not public" (or "not stated").

M18. "Individual peak quarters are less certain, typically by one or two quarters". Fix: "Individual peak quarters are uncertain by one or two quarters (80\% bootstrap ranges in Appendix~\ref{app:peaks}; up to five for Cohere's model)".

M19. "Our data cannot fully say why abstracts in 2026 resemble the newest models." This is a hedge stack. Fix: "Our data cannot say why ...".

M20. Repetition across sections (anti-slop). Each item is stated two or three times in near-identical words:
  - marker share fell under gpt-oss/Qwen3.5 while style rose: §6.5 twice, in consecutive sentences ("In 2026 the share fell ... including gpt-oss and Qwen3.5, under which style overlap rose." and "Under gpt-oss and Qwen3.5 the mined-marker share fell in 2026 while style overlap rose, so ..."), and again in the Discussion. Delete the first part of the §6.5 repeat; keep "so a falling marker share does not by itself show that writing stopped moving" by appending it to the earlier sentence.
  - "as did style overlap under every generator except Cohere's chat model" (§6.5) repeats §6.4 verbatim. Delete it.
  - "Hansard is a weak comparison" (§6.6 and App. F); "the 2022 change of government altered the speaker population six months before ChatGPT" (App. F and Limitations, verbatim). Keep each once.
  - "does not represent the arXiv population" (§4) vs "is not the arXiv population" (Limitations).
  - "no score here should be used to judge an individual writer" (Limitations) vs "caution against using any overlap or detector score to judge an individual writer" (Ethics).

M21. Units: the abstract uses "percentage points" and then "points" ("7.5 points; 11.9 measured nonparametrically"), while the body uses "pp". Use "percentage points" both times in the abstract. §6.6 "2025 gap 0.05, CI −0.36 to 0.51" has no unit. Add "(feature-space distance)".

M22. Undefined abbreviations: ITS (Table 2 "Primary (linear trend, ITS)"), POS (§6.3 "POS trigrams"; §5 says only "part-of-speech"), MTLD (never expanded), TPR/FPR (§3). Fix: "interrupted time-series (ITS)" in §5, "part-of-speech (POS)", "MTLD (measure of textual lexical diversity)", "true- and false-positive rates (TPR, FPR)".

M23. Inconsistent generator names: "Cohere command" (Table 1, Table 5), "Cohere's chat model" (§6.4/6.5), "Cohere chat" (Fig. 2b), "RAID Cohere-chat" (Table 4). Likewise "Mistral-7B-Instr. v0.1" vs "RAID Mistral-chat", "Llama-2-Chat 70B" vs "RAID Llama-chat", "MPT-30B-chat" vs "RAID MPT-chat", "2026 model" vs "Claude Opus 5.5" (Table 4) vs "Claude (2026 model)" (Fig. 2a). Use the Table 1 names in Table 4 and the figures.

M24. Layout and log. Page 8: the right column is stretched, with large gaps around "8 Conclusion" (`Underfull \vbox (badness 10000)` at main.tex:395). Use `\raggedbottom` or rebalance the text. Table 5 (`table*`) floats into the middle of Appendices F–G, so put `[p]` or `\clearpage` before Appendix E. Table 5's "80% range" prints "2026Q2–2026Q2" and "2026Q3–2026Q3"; print a single quarter when lo = hi. In inline p-values, `$p\R{...}$` gives an unspaced "p<0.001", while elsewhere the paper writes "p < 0.05".

---

## LaTeX log (scratch compile of main.tex with tectonic --keep-logs)
- 0 Overfull boxes, 0 undefined references or citations, 0 multiply-defined labels.
- 1 missing glyph (ő, see I8). 6 BibTeX month warnings (M8).
- About 40 Underfull \hbox warnings (badness up to 10000 at main.tex:362–375, the "Generators whose pretraining data predate ChatGPT" run-in heading line) and 3 Underfull \vbox warnings (page 8 stretch). These are cosmetic.
- Harmless: `inputenc package ignored with utf8 based engines` and the lineno.sty UTF-8 note.

## Page limit
main.pdf has 16 pages. §8 Conclusion ends on **page 8** (bottom of the right column), and Limitations starts on p.9. Within the ACL 8-page limit.
Anonymity: main.pdf contains no author name, ORCID, repo URL or commit hash, and its metadata is empty.

---

## Verified (typed claims and macro choices that match results)
- Abstract: 131,448 docs; 9.2%; 25.4 pp; 7.5 / 11.9; ρ 0.79, n = 18. All match the macros.
- Contributions: 19 generators; four pre-ChatGPT-data (GPT-4, Llama-2-Chat 70B, Llama-2-Chat 7B, Vicuna); four from 2026. "at most about a quarter as large": max drift 6.5 / 25.4 = 0.26, max 30-month placebo 5.8.
- §4: main instrument has 14 generators (6 RAID + 7 local + 2026 model), capped at 450; five added models; "each pairs with a 2025 model of the same family" (Qwen3/3.5, Gemma 3/4, Granite 3.3/4.2); Hansard and essays use 8 generators.
- §5: summary share 5.4% (GPT-4 + Llama-chat RAID part), Cohere 32.9%. "Three quarters of the region's training texts come from RAID": 900 of 1,200 per class (`arxiv_v_pre2022data_matched_separability.csv`).
- §6.2: yearly range 7.3% (2016) to 10.2% (2020) is the true min and max for 2015–2021. Econ has the largest Holm-adjusted p (1.9e-10), so "all adjusted p<0.001" is correct.
- §6.3: threshold/sample/trend variants span 23.5–29.1 (region variants 22.2 and 17.9 are correctly excluded). Ablations span 22.9–26.6, with MTLD 25.4. Event residuals stay within ±0.6 pp through 2022 and reach 28.5 in 2025. cs − math 38.1 − 10.5 = 27.6. Drift horizons 41–65 months; 34 placebo breaks.
- §6.4: pre-ChatGPT-data region 6.5 / 15.5 / 17.9 / 11.9%, peaking in 2025. "rose 2022→2025 under every generator except Cohere's" holds for all 19 (Cohere 10.6→9.2). Peak groupings: 2023 models other than Cohere 2024Q3–2025Q3; 2024 models 2025Q2–Q3; Gemma 3/Granite 3.3/Qwen3 2025Q4; gpt-oss 2026Q2, Qwen3.5 2026Q1, Granite 4.2 2026Q2; 2026 model rising in 2026Q3 (0.392→0.407). Fell 15 of 19; rose: gpt-oss, Qwen3.5, Granite 4.2, 2026 model. Every annual change except Gemma 4 has a CI excluding zero, 5/5 seeds and 10/10 subsamples. From 2025Q4 only gpt-oss (+3.9), Granite 4.2 (+2.9), 2026 model (+7.2) and Qwen3.5 (+0.4) rose. Same-family pairs hold on both measures. 18 generators fell in the last quarter. n_cutoff 9 matches Table 1 (ChatGPT excluded). n_no2023 = 10. open2026 pooled region 28.9→34.9. "12 of its 14" correct.
- §6.5: published markers 1.1 / 5.3 / 1.5%, peaking in 2024 (2025: 4.2%). Mined markers rose 2022→2025 for all 19 and from 2024 to 2025 for all 19 ("rose until 2025"). They fell in 2026 for 17; only Granite 4.2 (33.6→35.6) and the 2026 model (49.4→57.4) rose. 2026-model mined words are indeed ordinary academic vocabulary ("substantial, comparable, difficult, discuss ..."). Earlier/later/same counts 7/6/5 recomputed.
- §6.6 and appendices: Hansard numbers; 23.5% placebo share; dispersion CI and the "about three years of trend" claim (0.36 vs 3 × 0.11); learner counts 15/666; ORs and CIs; embedding 5.3 vs 10.0; GPT-2 15.5 vs 30.6; TOEFL 63.7 vs 8th-grade 8.0; Qwen 41.8 vs 3.4.
- Ethics: "11,730 texts" is exact (3,150 arXiv + 2,250 vintage + 3,180 Hansard + 3,150 essays, `F:\research-data\llm_*.jsonl`). "over two days": first commit 2026-10-12 06:57, last 2026-10-13 16:24.
- Appendix A: "other 16 generators" = 19 − 3. Cited commits ef4fa21 and 50e2a17 exist.
- Table 4 values and caption (22.8%). Table 5 rows match `arxiv_vintage_quarterly.csv` and `arxiv_vintage_uncertainty.csv`; the caption says release order, and the rows are in release order.
- Macro sign handling: negative values sit in `$...$` (true minus signs). CIs are attached to the right estimates. No "--" placeholders, and no fractions printed where percentages are meant.
- README "Main findings": every number matches the paper and results. Its only problem is the inherited I1 wording.
- main.pdf and preprint.pdf differ only in the author block, "author(s)" vs "author", the commit id and line breaks.
