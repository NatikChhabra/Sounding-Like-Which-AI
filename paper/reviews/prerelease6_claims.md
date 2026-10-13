# Pre-release audit 6: claims vs results (hostile re-check)

Commit checked: `0ec57b6` (working tree clean). Sources: `paper/main.tex`, `results/*`, `results/numbers.tex`,
rendered `paper/main.pdf` / `paper/preprint.pdf` (pymupdf text plus page renders at 140 dpi, zooms at 300 dpi),
`code/analysis.py` / `code/mso.py` (to confirm what each column means), raw generations in `F:\research-data`
(read only). No project file was edited apart from this report.

Scope: abstract, §1, §6.3–§6.6, Discussion, Conclusion, Limitations, Ethics, Acknowledgements, Appendices A, D, E, F;
README "Main findings"; `.zenodo.json`; figure and table pages; page limit; abstract length.

Summary: **0 Blocking, 3 Important, 9 Minor.** Every `\R` value I checked has the right quantity, unit and interval.
The new §6.4 claims are all supported by the result files, apart from the wording problems listed below.
I recomputed the main rank correlations from the CSVs (scipy): release vs peak 0.785 (n = 18), release vs median
length 0.705, length vs peak 0.729. They match `arxiv_vintage_peak.json`.

---

## Blocking

None.

---

## Important

### I1. "GPT-4 carries most of it" is not shown by any result (§6.4; same claim in §1 contribution (4))
- Quote (§6.4): "GPT-4 carries most of it (alone \R{arxiv_vintage.single:raid-gpt4.gap}\pp; Vicuna \R{arxiv_vintage.single:vicuna:7b.gap}\pp)."
  Quote (§1, (4)): "The shift is present, though smaller and carried mainly by GPT-4, against generators unlikely to have learned it…"
- Evidence (`arxiv_vintage.csv`, gap in pp): pooled pre-ChatGPT-data region 7.5; single regions GPT-4 11.4,
  Llama-2-Chat 70B 5.5, Llama-2-Chat 7B 3.7, Vicuna 1.4. RAID-only subset (GPT-4 + Llama-2-Chat 70B) 7.3; two local
  models 3.5. No region leaves GPT-4 out of the pool. GPT-4's single gap is *larger* than the pooled gap, so "carries
  most of it" is not a share that was measured. The results only show that GPT-4 alone gives the largest gap, and that the
  two members that are not from RAID give much less. The text also omits Llama-2-Chat 70B (5.5 pp), the second-largest gap.
- Fix (§6.4):
  ```
  GPT-4 alone gives the largest gap (\R{arxiv_vintage.single:raid-gpt4.gap}\pp; Llama-2-Chat 70B
  \R{arxiv_vintage.single:raid-llama-chat.gap}, Llama-2-Chat~7B \R{arxiv_vintage.single:llama2:7b.gap}, Vicuna
  \R{arxiv_vintage.single:vicuna:7b.gap}\pp).
  ```
  Fix (§1, (4)): "The shift is present, though smaller and largest under GPT-4, against generators unlikely to have learned it from post-ChatGPT writing; …"

### I2. "on our title-only prompts that part is small (12.5 pp over all three prompts)": the number contradicts the clause it supports (§6.4)
- Quote: "Part of the shift therefore points towards generators unlikely to have learned it from recent abstracts; on our
  title-only prompts that part is small (\R{arxiv_vintage.old_open_all.gap}\pp{} over all three prompts)."
- Evidence: `old_open_all.gap` = 12.5 pp (CI 8.7–16.2), from Llama-2-Chat 7B and Vicuna over P1–P3. The title-only value
  is `old_open_p1.gap` = 3.5 pp. The sentence calls the title-only part "small" but cites the all-prompt figure, which is
  neither title-only nor small (half the 25.4 pp primary gap). A reader cannot tell which number backs which clause.
- Fix:
  ```
  Part of the shift therefore points towards generators unlikely to have learned it from recent abstracts; on our own
  title-only prompts that part is small (\R{arxiv_vintage.old_open_p1.gap}\pp), though larger over all three prompt
  styles (\R{arxiv_vintage.old_open_all.gap}\pp), which include revisions of human drafts.
  ```

### I3. README makes a stronger claim than the paper: "could not have learned"
- Quote (README, bullet 2): "so part of the shift points towards models that could not have learned it from recent abstracts."
- Evidence: The paper says "unlikely to have learned" (§1 (4), §6.4). §6.4 and the Limitations say that the region's instruction
  tuning used 2023 data, and that Vicuna was tuned on user-shared ChatGPT conversations. "Could not" is stronger than
  the paper's claim.
- Fix: "…so part of the shift points towards models that were unlikely to have learned it from recent abstracts."

---

## Minor

### M1. Pooled title-only local region: a +0.8 pp change that is not stable is used as evidence (§6.4, last paragraph)
- Quote: "Pooled regions also need not follow their members: the seven local models pooled on title-only prompts went from \R{arxiv_vintage.local_p1.y2025}\% to \R{arxiv_vintage.local_p1.y2026}\%"
- Evidence (`arxiv_vintage_uncertainty.csv`, `local_p1`): change +0.78 pp, 95% CI −0.33 to 1.90, same sign in only 2/5
  training draws. Six of its seven members fell (gpt-oss rose). The all-prompt local region (43.3 → 48.4) carries the
  point by itself. The paper reports stability for every single-generator change, but not for this one.
- Fix: "…went from 28.2\% to 29.0\% (a change not stable across training draws), and over all three prompts from …", or drop the title-only clause.

### M2. "In all three same-family pairs" undercounts the pairs in the generator set (§6.4)
- Quote: "In all three same-family pairs the newer model's change was higher; for Gemma the two intervals overlap."
- Evidence: the three pairs meant are the 2025/2026 pairs from §4 (Qwen3/3.5: −3.7 vs +2.4; Gemma 3/4: −2.0
  [−3.1, −0.9] vs −0.9 [−1.8, 0.1]; Granite 3.3/4.2: −2.6 vs +7.4). All of these are correct. The generator set also contains
  Mistral v0.1/v0.3 (−5.4 vs −4.6), Llama-2-Chat/Llama 3.1 (−5.5, −5.2 vs −5.0) and GPT-4, ChatGPT/gpt-oss (−3.6, −5.1 vs +9.0).
  In each of those the newer model's change is also higher, so the claim holds, but "all three" reads as if there were only three.
- Fix: "In each of the three 2025--2026 same-family pairs (\S\ref{sec:data}) the newer model's change was higher; for Gemma the two intervals overlap."

### M3. Appendix E peak groupings leave out the 2026 model
- Quote: "…in 2025Q4 under Gemma~3, Granite~3.3, Qwen3 and Gemma~4, and in 2026Q1--Q2 under gpt-oss, Qwen3.5 and Granite~4.2."
- Evidence: all groupings match `arxiv_vintage_quarterly.csv`. The 2023 models other than Cohere's are 2024Q3–2025Q3, and the 2024 models
  2025Q2–Q3. But the sentence does not cover the 19th generator (2026 model: 2026Q3, the last quarter, still rising).
- Fix: append ", while under the 2026 model it was still rising in the last quarter, 2026Q3." Table 5 caption: add "The 2026 model's peak is the last observed quarter."

### M4. §6.3 robustness range: GBT is not in the stated range
- Quote: "Across the variants in Table~\ref{tab:robust} that change the threshold, the sample or the trend, the gap stays between 23.5\pp{} … and 29.1\pp{}"
- Evidence: Table 2 also lists gradient-boosted trees at 29.5 pp (27.8–31.3), above 29.1. The qualifier technically
  excludes it (classifier change), but a reader scanning Table 2 sees a value outside the stated range.
- Fix: add after the range: "(\R{robustness_v7.gbm_main.excess}\pp{} with gradient-boosted trees)".

### M5. Table 1 header vs §6.4: P2/P3 of the old open models are used
- Quote (Table 1): "Local; vintage analysis only (abstracts; P1 used)". §6.4 uses `old_open_all` ("over all three prompts") for Llama-2-Chat 7B and Vicuna.
- Evidence: `F:\research-data\llm_arxiv_old.jsonl` has 450 texts (P1–P3) per vintage-only model. `vintage_sets` uses all three prompts for `old_open_all`.
- Fix: "Local; vintage analysis only (abstracts; P1, and P1--P3 for one check)".

### M6. Limitations length range: rounding of 138.5
- Quote: "from \R{arxiv_generator_lengths.single:granite3.3:8b.median_words} to … for the 2025--2026 open models" renders "from 138 to 186".
- Evidence: Granite 3.3 median = 138.5 (half-to-even rounding gives 138; the 2026 model's 155.5 rounds to 156 elsewhere if shown). The 2024 open models
  (139, 139, 150.5) fall inside the range but are not named, so the reader cannot place them.
- Fix (optional): "from about 139 to 186 for the 2024--2026 open models".

### M7. Fig. 2a: ChatGPT line runs through the legend
- Evidence (p. 8, 300 dpi zoom): the vertical ChatGPT line at end-2022 crosses the legend text "Open models 2024–25 (incl. gpt-oss)" and "(Claude Opus 5.5)". The legend has no opaque background.
- Fix (`code/figures.py`): `ax.legend(..., framealpha=1)` or move the legend to `loc="upper left", bbox_to_anchor=(0, 0.98)` with a white frame.

### M8. Fig. 2b: labels touch the open circle and run past the axes
- Evidence (p. 8): the open circle of the 2026 model touches the top of "Granite 4.2 8B". That label and the ρ annotation
  ("… (n = 15)") extend beyond the right spine. Nothing is clipped. The plotted points all match
  `arxiv_vintage_quarterly.csv` peaks and the `RELEASE` dates in `analysis.py`.
- Fix: place the Granite 4.2 label to the left (`ha="right"`) or below its point. Break the ρ annotation over two lines.

### M9. README zero-shot bullet: "its flag rate falls" needs a time frame
- Quote: "does not see the shift (its flag rate falls)".
- Evidence (`arxiv_fastdetect.csv`): 8.3% (2015) → 11.3% (2022) → 7.3% (2025) → 5.3% (2026). The rate falls only after 2022.
  The paper says "does not track the shift".
- Fix: "does not see the shift (its flag rate falls after 2022)".

---

## Verified (no change needed)

**Abstract** (198 tokens rendered, from "Rather" to "scores.", in both PDFs; 196 counting "n = 18" as one word. It is under 200
words, but only 2 words remain, so any fix above must not lengthen it.)
- 131,448 docs; 9.2% pre-ChatGPT; 25.4 pp gap. "Far above placebo and instrument-drift gaps": the largest is 3.2 pp at 12 months, 5.8 pp at 30 months, 6.5 pp for drift.
- 7.5 pp pre-ChatGPT-data region; 3.5 pp own prompts (`old_open_p1`).
- "mostly rose then fell": 18 of 19 rose then fell; the 2026 model is still rising.
- ρ 0.79, n = 18; 0.66 for the 15 dated generators chosen before the 2026 open models (n_no_new = 15). "Longer-writing": ρ(release, length) 0.70.
- Learners less often (2.3 vs 4.2%). "Largely tracking essay scores": OR 0.55 → 0.87 once proficiency is added.

**§1**: 19 generators (6 RAID + 7 local + 2026 model + 5 vintage-only). Four predate ChatGPT (GPT-4, Llama-2-Chat 70B/7B,
Vicuna) and four are from 2026. "At most 6.5 pp": the maximum over placebo grid, fixed placebos and drift (0.5, −1.3, −2.0 for
the pre-ChatGPT-data region). Mined words rose 2022→2025 for all 19 and fell in 2026 for 17. Dispersion gap 0.05 (−0.36 to 0.51).
Hansard gap 1.3 (−0.7 to 3.4). Five hypotheses match Appendix A.

**§6.3**: yearly 2015–2021 minimum 2016 (7.3) and maximum 2020 (10.2); 2022 11.1; 2023–2026 17.7/27.8/40.6/44.7. The monthly
series is flat from 2025-08 to 2026-09 (42.0–48.0). relative_gap = 25.4/12.15 = 2.09. Block bootstrap 23.3–27.3. Ablation
range 22.9 (function words) to 26.6 (POS trigrams); MTLD 25.4. Placebos: 3/34 = 8.8%, maximum 3.2; 30-month 2/24 = 8.3%,
maximum 5.8. Drift 6.5/−2.3/−1.0, only −2.3 with p < 0.05; 65 and 41 months correct; 6.5/25.4 ≈ a quarter. Yearly residuals
|·| ≤ 0.6 pp through 2022, 28.5 in 2025. Field ordering cs 38.1 > q-bio 36.2 > eess > stat > econ > cond-mat > astro 13.7 > math 10.5.
Holm maximum adjusted p (econ) 1.9e−10. cs−math 27.6 (22.2–32.9). Implied 42.1%/7.8% (cv) and 44.4%/8.2% (lomo).

**§6.4** (all against `arxiv_vintage*.{csv,json}`, `robustness_v5/v7.json`, `arxiv_vintage_peak_checks.csv`, `arxiv_generator_lengths.csv`)
- Pre-ChatGPT-data region 6.5/15.5/17.9% (2022/24/25), 11.9% in 2026, gap 7.5 (4.6–10.4). Title-only 2024–25 open models 20.3.
  To-June-2025 fits: 13.1 / 22.7 / 7.6.
- "Three quarters … from RAID": the training cap `PER_MODEL = 450` gives GPT-4 450 + Llama-2-Chat 70B 450 out of 1,200 = 75%.
- "Rose 2022→2025 under every generator except Cohere's" (Vicuna 3.9→6.1; Cohere 10.6→9.2). Cohere peaked in 2023Q2.
- "From 2026Q2 to 2026Q3 overlap fell under every other generator, also with equal field weights": all 18 Q3 − Q2 < 0
  (−0.5 Vicuna to −4.6 Gemma 3); `fell_last_quarter_field_weighted` is True for all 18 and `field_weighted.n_fell_last_quarter` = 18.
  gpt-oss and Granite 4.2 both peak in 2026Q2. The 2026 model rose (39.2 → 40.7).
- ρ 0.79; bootstrap 0.64–0.86 (2.5–97.5 percentiles of 1,000); seeds 0.79–0.85; length-weighted 0.84; field-weighted 0.81;
  without 2023 models 0.82 (n = 10); RAID tied 0.83.
- "Newer generators also write longer": ρ(release, length) = 0.70. Length vs peak 0.73. Partial 0.56. Without the 2026 open models
  0.66 (n = 15, p = 0.007), seeds 0.66–0.77, partial 0.37. First test 0.67 annual / 0.18 from 2025Q4.
- "Uncertain by one or two quarters, up to five for Cohere": Cohere's 80% range is 2023Q2–2024Q3. The others are at most 2 from the observed peak.
- Gemma 4 (2026.42) peaked 2025Q4 and Granite 4.2 (2026.65) peaked 2026Q2, both before release. Qwen3.5 (2026.12) peaked 2026Q1, its release quarter.
- 15 of 19 fell; rose: gpt-oss 29.4→38.5, Qwen3.5, Granite 4.2, 2026 model 29.3→39.2.
- "Every change but Gemma 4's is stable": all other 18 have CIs excluding 0, 5/5 seeds and 10/10 subsamples. Gemma 4 CI −1.8 to 0.1, 4/5 seeds.
- Cutoff vs release on 9 generators: 0.59 vs 0.62. The 9 match the Table 1 cutoffs, with ChatGPT's "(2021)" excluded.
- Pooled 2026 open models 28.9→34.9 (stable: CI 4.9–7.2, 5/5, 10/10).
- Aggregate: 12 of 14 main-instrument single regions fell (gpt-oss and the 2026 model rose). Without the 2026 model 37.9→36.8. Local all-prompt 43.3→48.4.

**Appendix D**: 1,500 per class, AUC 0.737, 600 per year, 8.3/11.3/5.3%.
**Appendix E**: all peak groupings match. "Each annual change … except under Gemma 4" holds. Subsets 7.3 / 8.6 / 7.4
(`pre2022data` is RAID-only with summaries kept, 5.4% summaries; `plus_chatgpt` 11.7% summaries). From 2025Q4 only the
2026 model (+7.2), gpt-oss (+3.9), Granite 4.2 (+2.9) and Qwen3.5 (+0.43) rose.
**Appendix A**: "other 16 generators" = 19 − 3. Release-change correlations 0.67 and 0.18 (p = 0.464).
**Appendix F**: TPR math 75.8 vs cs 85.8. A lower TPR raises the implied α, so the direction is right. Liang et al. 17.5%/4.9% are
the abstract values per `lit/verification/v5_followup.md`.

**§6.5**: marker 1.1 (2022) → 5.3 (2024, peak) → 1.5 (2026); gap 1.9 (0.8–3.0). Mined words: all 19 rose 2022→2025; 17 fell
in 2026; gpt-oss and Qwen3.5 are the style-rose / marker-fell pair; Granite 4.2 33.6→35.6 and 2026 model 49.4→57.4.
Pre-ChatGPT-data region 17.4→34.9. Marker vs style peaks: 7 earlier / 6 later / 5 same, recounted by hand from `arxiv_vintage_quarterly.csv`.
**§6.6**: Hansard values, 30.7 difference with "the same eight generators" (7 local + 2026 model), 23.5% placebo grid. ELL values and the other instruments' direction.
**Discussion**: "three of the four 2026 generators … peaked in 2026 or still rising" (2026 model, Qwen3.5, Granite 4.2; not Gemma 4); "most generators" for mined words (17/19).
**Conclusion**: 9.2% → 40.6%; partly towards pre-ChatGPT-data generators.
**Limitations**: four 2026 generators. Three of four in the pre-ChatGPT-data region are Llama-2-based. Medians 102 (Vicuna) to 250 (Llama-2-Chat 70B), 90–134 for the other RAID
models. 2026 model 17.9% of 2015 abstracts against a maximum of 8.3% (Cohere) for the others. 150 / 450 texts per single region (cap
confirmed in `mso.py`). κ 0.64 / 0.48 / 0.26 / 0.29. MSO 22.8 vs 22.6. TOEFL 34.1 vs 5.7. 15 in-region learner essays.
**Ethics**: "11,730 texts" is exact: local-model rows in `F:\research-data` are 3,150 (arXiv) + 2,250 (vintage-only) + 3,150 (essays) + 3,180 (Hansard).
The 7–21 B range is consistent (gpt-oss 20B is 21 B total).
**Acknowledgements**: the counts typed in words (19, 14, four, 12 of 14, three of four, 16, 11,730) are all confirmed above.
**README "Main findings"**: every number matches (25.4, 23.2–27.7, 22.2, 17.9, 7.5, 3.5, 13.1, 22.7, 0.79, 0.66/15, 0.79–0.85, 0.84,
0.81, 0.82, 0.73, 2.3 vs 4.2, 63.7 vs 8.0). The claims match the paper's strength except I3 and M9.
**.zenodo.json**: contains no numbers. The description (arXiv 2015–2026; speech and essays as secondary genres; AI-made disclosure) matches the paper.

**Figures/tables (rendered)**: Fig. 1 (p. 6) matches the caption (a rises above trend, b small gap, c peaks in 2024); no clipping.
Table 2 values match the text. Fig. 2a lines match `arxiv_vintage.csv` (`pre2022data_matched`, `raid_all`, `local_p1`, gpt-oss,
`open2026_p1`, 2026 model). Fig. 2b's 19 points match the peak quarters and the release dates. Table 1, Tables 3–5 and Figs. 3–4 have no overlaps or clipping.
Table 5 matches `arxiv_vintage_quarterly.csv` / `arxiv_vintage_uncertainty.csv` row by row, and its order is by release date. Fig. 3 ordering (econ highest baseline,
astro lowest; cs/q-bio largest gap, math smallest) matches the text. Fig. 4 directions match.

**Page limit**: in `main.pdf` the Conclusion ends on page 8 (Limitations starts at the bottom of page 8). Same in `preprint.pdf`.
