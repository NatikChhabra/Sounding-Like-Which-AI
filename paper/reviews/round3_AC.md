# Round 3: Area Chair meta-review and copy edit

**Submission:** "Sounding Like Which AI? Machine-Style Overlap of arXiv Abstracts with Language Models of Different Vintages"
**Track:** ACL Rolling Review, theme track "Homogenization and knowledge collapse in LLMs" (long paper)

**What I read**
- `paper/main.tex` (all 687 lines). Every `\R{}` value I checked was traced to `results/numbers.tex` and then to the underlying JSON or CSV.
- `paper/main.pdf` (13 pp.). All 13 pages were rendered with pymupdf and inspected, and the four figure PDFs were also rendered at 200 dpi.
- The rest of the record:
  - `paper/AI_DISCLOSURE.md`, `preregistration.md`, `README.md`, `CITATION.cff`
  - `lit/SPOT_CHECK.md`, `lit/verification/batch6_v3.md`, `lit/verification/batch7_bib.md`
  - `code/make_numbers.py`, `code/figures.py`, and the relevant parts of `code/analysis.py`
  - the full git log, including the intermediate versions of `vintage.pdf` and `numbers.tex`
  - my round-2 review (`paper/reviews/round2_AC.md`)

**Conventions.** "L" means a `main.tex` source line; "p." means a PDF page. **[HUMAN]** marks a check that only the human author can do.

**Caveat.** I am the same model family (Claude Opus 5.5) that conducted the study, drafted the paper, generated the Claude texts and wrote rounds 1-2. Shared blind spots are likely. In this round I found two errors that I also made in round 2 ("non-physics" archives, and accepting the GPT-2 "predates both collections" premise). A human pass is required before submission.

---

## 0. Verdict in brief

v3 is a different and better paper.
- **New framing.** The awkward "2026 model" story is replaced by a generator-vintage design:
  - a region built from generators whose pretraining data predate ChatGPT;
  - 19 single-generator regions on a matched title-only task;
  - three 2026 open models run with logged decoding, so the 2026 result no longer rests on the uncontrolled Claude data.
- **R1's time-series requests are done:**
  - a 34-break placebo grid and drift placebos at three origins;
  - quadratic, window and nonparametric pre-trends;
  - a 12-month block bootstrap and yearly event residuals;
  - Holm correction and the cs-minus-math contrast.
- **The record is now honest about the spot-check, human editing and the Claude timing.**
- **The theme fit is real.** The question "is human text still an independent anchor for LLM style?" is exactly what this track is about.

What stops me recommending main conference as the paper stands:

1. **The headline vintage result has no uncertainty and an undisclosed post-hoc step.**
   - None of the 19 changes from 2025 to 2026 has a CI. Two of the decisive ones are small: Gemma 4 −0.9 pp and Qwen3.5 +2.3 pp.
   - The local single-generator instruments are each trained on only 150 texts.
   - The "released before August 2025" split was drawn after seeing the data. It is the line that puts gpt-oss (2025-08) on the "new" side.
   - The three 2026 open models were generated after the 14-generator pattern had been plotted. `vintage.pdf` in commit 3a59ba8 (02:48) already shows "fell under all except gpt-oss and Claude", and the models were added in 868661e (03:00).
   - That makes them a genuine out-of-sample test, which is a strength, but the test is not logged and its outcome is not stated: 2 of 3 rose, and Gemma 4 fell. It is missing from App. D(5), from the plan's deviation 9 and from the README.
   - The Fig. 2 caption still describes the 14-generator version ("fell against every generator except the two newest"), which contradicts the text ("four of the five").
2. **Too many visible factual and rendering errors for a paper whose selling point is an auditable record.**
   - "Eight non-physics archives" is false: astro-ph and cond-mat are physics archives.
   - The dispersion CI prints as "−35.9 to 50.8"; the true CI is −0.36 to 0.51.
   - The logit gaps print as "27.7 against 149.0"; the true values are 0.28 and 1.49.
   - The yearly pre-ChatGPT range omits the 2020 maximum.
   - "Kept rising only for the 2026 model" is false: Granite 4.2's mined markers also rose.
   - "GPT-2 was trained before either collection was public" is false for the ASAP-derived 8th-grade essays (2012).
   - Fig. 1a's legend hides the 2025-26 plateau the text describes.
   - Fig. 4's y-labels are clipped.
   - Fig. 2b is not in the release order its caption claims.
   - Each of these alone is minor. Together, a reviewer will read them as "no human checked this", which the AI Use section confirms ("no human has edited the text").
3. **Two interpretive claims are contradicted by the authors' own numbers.**
   - The claim that the decline of *delve* "mostly reflects the age of the reference" is contradicted by mined markers falling for gpt-oss and Qwen3.5, whose style regions rose.
   - The claim that the pre-ChatGPT-data region "cannot be an artefact" of newer models is weakened in three ways:
     - RAID's prompts come from titles of 2023+ papers;
     - Llama 2 and Vicuna were tuned on 2023 data, Vicuna on ChatGPT conversations;
     - the two local-only old models give 3.5 pp, not 7.7.

**Likely decision: Findings**, with an overall score of about 3.0-3.5. The paper becomes a plausible main-conference paper (overall about 3.5) if the five changes in §6 are made. All of them are reanalysis or editing except one optional extra generator.

---

## 1. Round-2 items: status

Key: **Fixed** = resolved. **Mostly** = substance fixed, minor parts missing. **Partly** = important parts missing. **Not** = not addressed. **Moot** = the analysis was removed.

### 1a. Round-2 tables on the round-1 weaknesses (R1 methods)

| # | Item | Status | Evidence in v3 | Still missing |
|---|---|---|---|---|
| W1 | Sampler, estimand | **Mostly** | Estimand stated (L172-173, Limitations L576-577) | No submission-volume-weighted series. Acceptable now that it is stated. |
| W2 | Drift; one origin | **Mostly** | Three origins (L274-276; Table 2): 6.8 (p=.035), −2.5 (p=.017), −1.2 pp. 34-break placebo grid (L342-344). | Two of three drift placebos are significant, with opposite signs. L347-348 turns that into "at most a quarter", which three draws cannot bound. No author or subfield check. |
| W3 | Bayes wording; instrument uncertainty; H1 length | **Mostly** | Contribution (1) reworded (L68-70). Length-standardised field baselines (L325-327). | Instrument variation is still outside every CI. This is stated in L162-163 and Limitations, which is acceptable. |
| W4 | 2026 result rests on one uncontrolled model added post hoc | **Mostly** | Three 2026 open models with logged decoding (L199-201, L425-427). Claude timing now consistent in App. D(3) and plan dev. 7. | The 2026 open models were themselves added after the pattern was seen; this is not logged (§0.1, §2.3). 2026 is not labelled exploratory. |
| W5 | Hansard as control | **Mostly** | Relative and logit scales (L469-471), 2022 government change (L478), placebo grid 17.6% (L477), threshold 0.6 (L474-475) | The logit values misprint (×100). The Hansard **marker** gap is significant, +1.6 pp (CI 0.4-2.8, `hansard_its.json` `marker`), and still unreported. No speaker fixed effects. |
| W6 | Encoding | **Mostly** | The dash text now renders (p.4 l.298) | MTLD is still the top feature (1.29, Table 4) and is not ablated. |
| W7 | ITS specification | **Mostly** | Quadratic and window trends, nonparametric gap, block bootstrap, event residuals, placebo grid (L271-276, L338-350, Table 2) | No field-month cluster bootstrap. Placebo level and slope parameters are not shown. The 2017-start variant is computed (26.8 pp) but missing from Table 2, although L271 lists it. astro-ph still has a significant negative level shift (−3.8 pp, p=.002). |
| W8a | Phi-4/Granite | **Not → new inconsistency** | App. D(3) (L676-678) says Phi-4 and Granite were "added ... before the first review". | Git shows they were not used in v1 (`02bde27:results/arxiv_lomo.csv` has 12 generators). The plan's dev. 7 says "first used in v2", and L198 says "the 14 generators available before review". Fix App. D(3) and L198. |
| W8c | "Every number" | **Mostly** | Now "every reported result" (L606-607) | Some results are still typed: "±1 pp" (L349), "all 14" and "four of the five" (abstract L35-36, L413, L418), "by less than a point" (L414), "1,200 per year" (L487), and the counts "11/1/20" (L605). Put the counts in macros, or say "every reported statistic". |
| W8d | Table label | **Fixed** | `tab:lomo` | |
| W8e / N9 | Revision exclusion | **Partly** | Shares for 2016 and 2021 given (L175-176) | **2022 (24.2%) is omitted** (`robustness_v4.json`), and it is the pre-period year most affected. The "trend to 2020" row (25.7 pp) is the right sensitivity check, but the text does not connect it to the exclusion. |
| W8g | "arXiv" overstates | **Partly, now worse** | "Eight non-physics archives" (L169, L576) | astro-ph and cond-mat are physics archives, so "non-physics" is false. The title and abstract say "arXiv abstracts" without qualification. |
| W8i | Plan record | **Mostly** | Status honest; deviations 1-12 in order; "pre-registered" gone from the paper | Dev. 9 omits Qwen3.5, Gemma 4 and Granite 4.2. Dev. 9 names the pre-ChatGPT-data region as "RAID GPT-4 and ChatGPT", but code and paper use GPT-4 and Llama-2-70B-chat (`analysis.py` L404). The file is still titled "Pre-registration". |
| W9.2 | Rare events | **Mostly** | All 10 seeds p<0.05 (L500-501) | No Firth. 15/666 in region. |
| W11a | RAID identities | **Fixed / Moot** | Table 1 gives the model IDs. The base-vs-chat analysis was removed. | **Dangling:** L197-198 "and, for one analysis, five base models" now refers to nothing. Delete it. |
| W11b | Marker narrative | **Partly** | Marker gap with CI (L448-449). Mined markers (L450-457). | The new interpretation (L459-460, L545-546) is contradicted by the data (§2.5). |
| W11c | Multiplicity; H4 | **Fixed** | Holm, cs−math 27.6 pp (22.3-33.0) (L353-355) | |

### 1b. Round-2 tables (R2 detection/stylometry)

| # | Item | Status | Evidence / missing |
|---|---|---|---|
| W1 | Trajectory is an artefact of the generator set | **Fixed in framing; Partly in inference** | Now the paper's central question (§6.4). Missing: per-generator uncertainty, a pre-specifiable statistic and a like-for-like baseline (§2.1-2.2). |
| W2 | Implied α | **Fixed** | L356-363: cs 42.0% and math 7.9% (CV), against Liang's 17.5% and 4.9%, with the right caveats. |
| W3 | Topic and length robustness | **Mostly** | Length-standardised baselines. MTLD is not ablated. Mined-marker shares are not length-controlled (§2.5). |
| W4 | Hansard generator set and common scale | **Mostly** | Scales added (display bug, N-new-3). Still no commercial model other than Claude in Hansard or essays. |
| W5 | Base vs chat | **Moot** | Removed; dangling mention at L197-198. |
| W7 | Frontier data uncontrolled | **Mostly** | Three logged 2026 models, but see §2.3. |
| W8 | n per archive | **Fixed** | Fig. 4 labels carry n, but they are clipped (§5). |
| W11 | Askitas, Chang, "overlap" vs flag rate | **Fixed** | L95-101. Askitas is described correctly as IZA working papers (verification batch 6 §6). |

### 1c. AC round-1 items carried in round 2

| Item | Status | Evidence / remaining |
|---|---|---|
| Visible TODO | **Fixed** | No `\TODO{}` call is left, but the macro is still defined at L14. Delete it so a stray TODO cannot compile silently. |
| Text vs results | **Partly** | New mismatches: yearly range (L334), Fig. 2 caption (L440), marker "only" (L455), dispersion CI (L489), logit (L470-471). See §2. |
| Generator timing record | **Mostly** | Claude is now consistent. Phi-4/Granite (W8a) and the 2026 open models (§2.3) are not. |
| Confounds | **Mostly** | Topic, length, math, dash, revision, drift. Subfield and author composition are still not checked. |
| Theme fit | **Mostly** | The vintage framing makes the link concrete (L113-114, L549-551). Dispersion is redone, but the CI misprints and the conclusion overclaims (§2.6). |
| Citations verified | **Mostly** | Batches 6-7 applied. Human spot-check not done (disclosed). `SPOT_CHECK.md` is **stale**: it quotes sentences that are no longer in the paper (e.g. the park2026 "shift with professional editing" sentence and the krishna2023/dugan2024raid sentences). |
| Missing feature table | **Fixed** | App. C, Table 4 |
| Accountability sentence | **Fixed** | L607-608 |
| Simulated reviewers not independent | **Fixed** | L602-603 |
| Fig. 1 legend / Hansard band | **Not → worse** | The legend in (a) now **covers the 2025-26 monthly points and the end of the 6-month mean**, so the plateau stated at L336-337 cannot be seen. Hansard raw points still have no band. |
| Fig. 2 (fields) n | **Fixed**, but the labels are clipped | |
| Fig. 3 (learners) n | **Fixed** | Caption gives ELL n=666 and non-ELL n=6,758 |

### 1d. Round-2 new problems N1-N20

| N | Problem | Status | Note |
|---|---|---|---|
| N1 | Genset paragraph contradicted its figure | **Fixed (replaced)** | The genset table and paragraph are gone. |
| N2 | "Keep moving" | **Fixed in text** | New title. L336-337 says "roughly flat since late 2025". Fig. 1a hides it (§5). |
| N3 | Three accounts of Claude timing | **Mostly** | Paper App. D(3) and plan dev. 7 agree with git. Small error: App. D says the **texts** were "merged two minutes after". The prompt batches were committed 2 min after (c11d3ce 15:37); the texts were merged at 15:44 (01ef90f), 9 min after. |
| N4 | Spot-check claimed, not done | **Fixed (claim retracted)** | Paper: "will check" (L606). Disclosure: "has not yet". Consistent. The check itself is still open and the sheet is stale. **[HUMAN]** |
| N5 | "Checked against its source" | **Fixed** | L603-606. The counts (11/1/20) date from batches 1-5. Batches 6-7 moved at least Kusumegi, Khan, Sadasivan, Gerstgrasser and Liang (mapping) to published versions. Recount or say "at least". |
| N6 | Hansard selectivity | **Mostly** | Threshold 0.6, placebo grid and pre-trend range now reported. Hansard marker rise (+1.6 pp, CI 0.4-2.8) still omitted. |
| N7 | arXiv−Hansard region | **Fixed** | L471-473 states the region (arXiv 32.0 pp); relative and logit added. |
| N8 | Dispersion | **Mostly, with a display bug** | Length-fixed (150 words), trend test, bootstrap. CI prints ×100. No figure. The conclusion is too strong for the interval (§2.6). |
| N9 | Revision exclusion | **Partly** | See W8e. |
| N10 | Detector-bias overclaim in abstract | **Fixed** | Abstract L37-39 is scoped. |
| N11 | Instruments not in §5 | **Fixed** | L261-265 |
| N12 | Rendering bugs | **Fixed (old ones)** | New ones in §2.4. |
| N13 | Estimand | **Fixed** | But "non-physics" is false. |
| N14 | 14 vs 8 generators | **Fixed** | L201-202 |
| N15 | "Older generators" | **Fixed** | L308 |
| N16 | Table 1 placebo columns | **Fixed** | Header "95% CI or p"; "gap in June 2022" |
| N17 | Licences | **Fixed** | L588-592 |
| N18 | Claude near-human revisions | **Fixed** | L312-314 (AUC 0.674). The consequence is unstated: near-human generators widen the region and raise MSO for everyone. The P2-free region gives an **18.0 pp** gap (15.8-20.2, `arxiv_vintage.csv` `all_no_revision`), against 25.7, and this is **unreported**. Add it to Table 2. |
| N19 | κ for all genres | **Fixed** | L554-557 (0.65 / 0.28 / 0.29) |
| N20 | Promised changes | **Mostly** | Turnover, "pre-registered" and Askitas done. No instrument-summary table, which is acceptable given the page budget. |

### 1e. Round-2 "five changes"

| # | Change | Status |
|---|---|---|
| 1 | 2026/generator story matches data; second 2026 source | **Mostly.** Three logged 2026 open models; vintage framing. Missing: uncertainty, a pre-specified statistic, logging that the models were added post hoc, and a correct Fig. 2 caption. |
| 2 | Consistent record and human checks | **Mostly / Partly.** Spot-check and human-edit claims are now truthful. Still not done: the human check itself and any human reading. New inconsistencies: Phi-4/Granite timing, the 2026 open models missing from three documents, and the plan's dev. 9 region definition. |
| 3 | R1's time-series robustness | **Fixed / Mostly.** Nearly all done. Only the cluster bootstrap is missing. |
| 4 | Scales and construct | **Mostly.** Logit/relative, implied α, feature table, Askitas and Chang all done. Logit display bug. |
| 5 | Theme link | **Mostly.** Dispersion is length-controlled with CIs. The learner claim is scoped and the instruments described. The dispersion conclusion is still too strong and its CI misprints. |

---

## 2. New and remaining problems (most serious first)

### 2.1 The vintage result needs uncertainty and a statistic fixed in advance

The abstract, Contribution (4), §6.4, the Discussion and the Conclusion all rest on 19 point changes from 2025 to 2026 (`arxiv_vintage.csv` y2025/y2026), with no intervals.

- **Small changes carry the conclusion.** Gemma 4 is −0.9 pp, Qwen3.5 +2.3, Gemma 3 −2.0, Granite 3.3 −2.6. Sampling error alone is about 0.5 pp (n≈14,751 in 2025 and 11,727 in 2026). Instrument error is larger: each local single-generator region is trained on **150** P1 texts (`n_llm`), against 3,532-7,064 for RAID. That is the regime where retraining noise dominates.
- **The 2026 window is January-September, but 2025 is a full year.** For regions still rising through 2025, a full-year mean understates the late-2025 level. Use matched windows: Oct 2024-Sep 2025 against Oct 2025-Sep 2026, or the fitted monthly slope over the last 12 months.
- **The cut-point is post hoc.** "Released before August 2025" separates 14/14 from 4/5 only because it was placed after the data were seen.
- **Fixes, all cheap:**
  - (a) A bootstrap over documents and over generator training texts (or 10 training seeds) for each 2025→2026 change, shown as error bars in Fig. 2b.
  - (b) One pre-specifiable statistic: Spearman ρ between release date and the change, with a permutation p, over all 19 generators. Report it in the abstract instead of the "before August 2025" split.
  - (c) Matched 12-month windows.
  - (d) Report each generator's change relative to its own pre-ChatGPT trend. Claude's region has a 2015-2022 baseline of about 17% and a negative pre-trend (17.9% to 16.3%); the open models sit at 1-8%.

### 2.2 The pre-ChatGPT-data comparison is not like-for-like and is overstated

- **L404: "about a third of the gap under all 14 generators."** The 14-generator gap (25.7) uses prompts P1-P3; the vintage region uses P1 only. On the same title-only task:
  - the seven 2024-25 open models give **20.2 pp** (`local_p1`);
  - the RAID 2023 chat models give **5.8 pp** (`raid_all`).
  - The fair statement is "7.7 pp against 20.2 pp for the 2024-25 open models on the same task".
- **Topic of the RAID prompts.** RAID's arXiv generations were written from titles of papers from 2023 onward (verification batch 6 §4). The LLM class of the pre-ChatGPT-data region is therefore on 2023 topics, while the human class is 2015-2022. Function-word and POS features are not topic-free, so 2023+ human abstracts can look more "LLM-like" partly through topic. The region built only from the two locally run models, whose prompts are pre-ChatGPT titles, gives **3.5 pp** (CI 1.5-5.5), less than half of 7.7. State this, and make the local-only number the conservative headline for "the shift is present against old models".
- **"Cannot" overclaims (L75-76, L398-399, L407-408, L432-433, L538).** Llama 2's "tuning data is more recent, up to July 2023" (Touvron et al., Table 52). Vicuna is tuned on ShareGPT ChatGPT conversations from Dec 2022 to mid-2023. GPT-4's post-training includes "a small amount of more recent data". Limitations L573-574 concedes part of this, so the body should match it.

### 2.3 The 2026 open models are an unlogged post-hoc test

- **Timeline:**
  - 3a59ba8 (02:48): `paper/figures/vintage.pdf` shows the single-generator pattern for 14 generators. All fell except gpt-oss and Claude.
  - 868661e (03:00): `run_v3c.ps1` generates `llama2:7b, vicuna:7b, granite4.2:8b, qwen3.5:9b, gemma4:12b`.
- **Not logged.** The three 2026 open models therefore tested a prediction made from data. Two of three rose and Gemma 4 fell slightly. None of this is logged:
  - App. D(5) (L680-681) names only Llama-2-Chat and Vicuna.
  - Plan dev. 9 names only "Llama 2 chat and Vicuna".
  - The README's model list omits all three.
- **Fix.** Add to App. D(5) and dev. 9: "Qwen3.5 9B, Gemma 4 12B and Granite 4.2 8B were generated after the 2025-2026 changes for the first 14 single-generator regions had been plotted (commit 3a59ba8), as a test of the pattern; two of the three showed a rise." Reported this way it is a strength.
- **Fig. 2 caption (L440)** still says "Overlap fell against every generator except the two newest", which is the 3a59ba8 version. Replace it (§5).

### 2.4 Factual and rendering errors (each verified)

| # | Location | Error | Correct |
|---|---|---|---|
| a | L169, L576; README L8; plan dev. 1 | "eight non-physics archives (... astro-ph, cond-mat)" | astro-ph and cond-mat are arXiv physics archives. Write "eight archives: six outside physics plus astro-ph and cond-mat (no hep, gr-qc, quant-ph or physics.*)". I missed this in round 2. |
| b | L489-490 | "(bootstrap CI −35.9 to 50.8)" | −0.36 to 0.51 (`arxiv_len150_dispersion_trend.json`). **Root cause:** `make_numbers.py` L33 `leaf.endswith(PCT)` with "lo"/"hi" in PCT multiplies `ci_lo`/`ci_hi` by 100. `arxiv_dispersion.*.lo/hi` are also ×100 (3380.5), unused. |
| c | L470-471 | "on the logit scale 27.7 against 149.0" | 0.28 and 1.49 logits. **Root cause:** `leaf.startswith(PCT)` with "lo" matches `logit_gap`. **Fix:** match whole leaf tokens, e.g. `leaf in PCT or leaf.split("_")[-1] in PCT or leaf.split("_")[0] in PCT`. Add asserts for `logit_gap` and `ci_lo`. |
| d | L488 | "(-0.11 per year)" prints a hyphen | `$\R{...trend_per_year}$` |
| e | L334 | "ranged from 7.5% to 9.9% in 2015–2021" | 2020 is 10.1% (`arxiv_yearly.csv`). The hand-picked macros went stale after the re-run. Use `\R{arxiv_yearly.2020.mso}`, or compute min/max in code. |
| f | L455 | "it kept rising only for the 2026 model" | Granite 4.2's mined-marker share also rose, 34.4% to 35.6% (`m2025`/`m2026`). `n_marker_fell_2026`=17 implies 2 rose. |
| g | L520 (and L263-264) | "GPT-2 was trained before either collection was public" | Liang's US 8th-grade essays derive from Hewlett ASAP, public on Kaggle since 2012 (your own Ethics statement, L591). GPT-2's WebText was collected through 2017. The TOEFL essays' date is unverified. Write "GPT-2's training data are unlikely to include these essays". |
| h | L197-198 | "and, for one analysis, five base models" | No base-model analysis remains. Delete. |
| i | L676-678 (App. D(3)) | Phi-4 and Granite "added ... before the first review" | First used after the first review (v1 LOMO has 12 generators; plan dev. 7). Also "texts were merged two minutes after" → "prompt batches were committed two minutes after". |
| j | L198 | "the 14 generators available before review" | Twelve were used before the first review. Write "the 14 generators of the main design". |
| k | Table 1, L228 | Vicuna 7B v1.5 "2023-07" | Released 1 Aug 2023 (FastChat table; verification batch 6 §2) |
| l | L351-352 | "largest in quantitative biology (36.8 pp) and computer science (38.4)" | cs is the larger. Swap the order. |
| m | L323-324 | "$\chi^2$ $p<0.001$" | "$\chi^2(7)=348.5$, $p<0.001$" (macros exist: `arxiv_its.baseline_field_heterogeneity.chi2/dof`) |
| n | L425-427 | "give the same 2026 rise as the 2026 model (29.3% to 35.5%)" | Claude rose 29.3→39.2 (+9.9), the open set 29.3→35.5 (+6.2). Write "also rise (29.3% to 35.5%, against 29.3% to 39.2% for Claude)". |
| o | L419-420 | "The pattern holds within model families" | Two of three families: Gemma 4 fell as well, only by less. |
| p | references | `Computers \&amp; Education` prints "&amp;" (Jiang 2024) | `Computers \& Education` |
| q | references | gpt-oss: "OpenAI, :, Sandhini Agarwal, ..." | `author = {{OpenAI}}` |
| r | references | Juzek & Ward: "so much? exploring" | `{E}xploring` |

### 2.5 The marker-word interpretation contradicts its own evidence

L458-460: "once markers and style region come from the same model, the decline of *delve* mostly reflects the age of the reference". Discussion L545-546 repeats it, and the abstract L36-37 implies it. The evidence says otherwise:
- **Mined markers fell for 17/19 generators,** including gpt-oss and Qwen3.5, whose style regions rose. Marker decline therefore occurs **even against current references**. That is the pattern you would expect if authors avoid conspicuous words (Geng & Trotta), not if references age.
- **Claude's "markers"** (*substantial, comparable, whose*) occur in 40.0% of 2015 abstracts (`m2015`). Their rise from 49.1% to 57.5% is mostly a vocabulary-and-length effect.
- **No length control.** Median abstract length rose from 149 to 176 words, which mechanically raises the share of abstracts containing any one of 20 words. Neither marker series controls for it.
- **Topic words in the mined lists.** The lists still contain topic words (pre-ChatGPT-data list: *robotics, ablation*; gpt-oss: *engineering, lightweight*), so "topic words of the prompt set cancel" (L291) is too strong.
- **Fix:**
  - Truncate to 150 words, as for dispersion, or use per-1,000-word rates.
  - Rewrite L458-460 as in §4.
  - Drop "the rise and fall of *delve* is mostly what any fixed word list ... would show" (L545-546).

### 2.6 The dispersion conclusion is stronger than the interval

With the true CI (−0.36 to 0.51) and a pre-trend of −0.11 per year, the data cannot exclude an extra decline of about three years' worth of trend. "Without a faster loss of stylistic spread" (L491-492) should become "we detect no acceleration, but cannot exclude a modest one". Also, the full-length series has a 2025 gap of **+0.50 (CI 0.01-1.04)**, meaning more spread than the trend predicts. One clause on this would pre-empt a reviewer who finds it in `arxiv_dispersion_trend.json`.

### 2.7 Unreported sensitivity results that a reviewer will want

All of these are already computed; each is one row of Table 2 or a clause:
- Gap without Claude: **22.5 pp** (19.0-26.0), `arxiv_gensets_its.no_frontier`. `AI_DISCLOSURE.md` says "the paper reports results with and without them". For the trend gap it no longer does.
- Gap without the P2 (revision) texts: **18.0 pp** (15.8-20.2). That is 30% smaller; the reader should know.
- Pre-trend from 2017: 26.8 pp. L271 promises it.
- Revision-exclusion share for 2022: 24.2%.
- Hansard marker gap: +1.6 pp (0.4-2.8).
- Revision-overlap check (`revision_overlap.csv`). It is listed in plan dev. 9 but appears nowhere in the paper. Claude and Qwen3 P2 outputs keep more than 30% of the human draft in about 37% of cases. Either report it in one clause (it explains the near-human P2 AUC) or drop it from dev. 9.

### 2.8 "The 2026 model" is now ambiguous

Four generators are from 2026, but the text still calls Claude "the 2026 model" in about 15 places (L194, L225, L310, L313 area, L417, L426, L455-456, L572, L600-601, App. D). A reader of "the 2026 model rose" (L417) cannot tell which one is meant. Use **"Claude Opus 5.5" (or "Claude")** throughout; the name is already disclosed in Table 1 and AI Use. Fig. 2 already does this.

### 2.9 Smaller items

- L86 and L198-199 say "added after review". To an ARR reviewer this reads as a previous ARR round. Write "after two rounds of simulated review (AI Use)".
- Section 6.4 has no H-label; it is post hoc. Say so in its first sentence ("This analysis was not in the plan").
- L273: placebo breaks are "each evaluated 12 months later". The code caps evaluation at November 2022 (`placebo_grid`, `min(f+12, T0-1)`). Add "or in November 2022 if earlier".
- L347-348: "instrument ageing can thus produce gaps of a few points, about a quarter of the observed gap at most". Three draws cannot give "at most", and two of them are significant. See §4.
- Placebo 2020-11 has a significant level shift (−1.4 pp, p=.008) although its gap is not significant. This is fine to leave out.

---

## 3. Consistency audit: paper vs AI_DISCLOSURE vs plan vs README vs git

| Topic | Paper | AI_DISCLOSURE.md | preregistration.md | README.md | Git | Verdict |
|---|---|---|---|---|---|---|
| Plan committed before results | ef4fa21, "before any result" (L668) | n/a | ef4fa21, 07:53 | "committed before any result" | ef4fa21 07:53; first result commit 50e2a17 10:31 | **Consistent** |
| Claude added | App. D(3): after pilot, before 1st review; "texts merged two minutes after" | n/a | Dev. 7: batches 15:37, 2 min after f586d6c | n/a | c11d3ce 15:37 batches; 01ef90f 15:44 texts | **Minor error** in the paper (texts vs batches) |
| Phi-4/Granite added | App. D(3): before 1st review. L198: "14 available before review" | n/a | Dev. 7: "first used in v2"; dev. 8: added in round 1 | Listed among the local models | v1 LOMO has 12 generators | **Paper wrong**; plan right |
| Llama-2-Chat 7B, Vicuna | After 2nd review (App. D(5), L199) | n/a | Dev. 9 | Listed | 37971d5 / 868661e | **Consistent** |
| Qwen3.5, Gemma 4, Granite 4.2 | L199-201: "after review", "three released in 2026"; **absent from App. D(5)** | Absent | **Absent** from dev. 9 | **Absent** from the model list | Added in 868661e (03:00), after the vintage figure in 3a59ba8 (02:48) | **Inconsistent; post-hoc status unlogged** |
| Pre-ChatGPT-data region | GPT-4 + Llama-2-70B-chat (+2 local); ChatGPT only as a sensitivity check | n/a | Dev. 9: "RAID GPT-4 and ChatGPT" | n/a | `PRE2022_DATA=("raid-gpt4","raid-llama-chat")` | **Plan wrong** |
| Cleaning fix | App. D(5): Title-line fix, "every analysis was re-run". No magnitude. | n/a | Dev. 9: 13% of local arXiv and 18% of essay LLM texts; "found while adding generators" | n/a | cde9132 03:33, after the v3 draft 868661e 03:00. Headline 25.7→25.7, Hansard 1.7→1.8, ELL OR 0.53→0.56 (`numbers.tex` 7bdc17c vs 1012d6b) | **Consistent, incomplete.** Add the affected share and "the primary gap was unchanged (25.7 pp)" to App. D. |
| Human role | Chose topic and constraints; approved plan and deviations "in the working conversation" | Same, plus "every download and public action"; "not separate commits" | "approved by the author" | "under the human author's direction" | No commit is attributable to the human. 6675865 "Strip BOM" has neither "(AI-written)" nor a Co-Authored-By trailer. | **Consistent.** The unlabelled commit breaks the stated audit rule ("AI-written commits carry '(AI-written)'"): either label it, or say it is the human's. |
| Human edits | "no human has edited the text" | "zero HUMAN-EDIT: commits" | n/a | "no human has edited the text so far" | 0 HUMAN-EDIT commits | **Consistent** (and the main reviewer risk; §6) |
| Spot-check | "will check ... before publication" | "has not yet" | n/a | n/a | SPOT_CHECK.md 0/5 ticked | **Consistent.** The sheet quotes v1/v2 sentences that no longer exist; regenerate it from current `main.tex`. **[HUMAN]** |
| Citation-verification counts | 11 / 1 / 20 | 11 / 1 / 20 | n/a | n/a | 17601b9 (batches 1-5); batches 6-7 changed more entries later | **Stale in both** |
| "Results with and without Claude" | Trend gap without Claude no longer reported (only LOMO overall MSO, Table 3) | "the paper reports results with and without them" | n/a | n/a | `arxiv_gensets_its.no_frontier` = 22.5 pp exists | **Disclosure overstates.** Add the row (§2.7). |
| Archives | "non-physics" | n/a | "8 non-physics archives" | "eight non-physics archives" | n/a | **All wrong** (§2.4a) |
| Title | New | n/a | Old construct title | Unnamed | n/a | `CITATION.cff` still has the round-1 title and the author identity (anonymity, §4.3) |

---

## 4. Page limit, anonymity, policy sections, references

### 4.1 Page limit

- The main text ends at the **bottom of p.8** (Conclusion, PDF line 647). Limitations starts p.9. This is compliant, with **zero slack**.
- Every addition in §2 must be paid for. Cuts that free about 12-15 lines without losing content:
  - L506 duplicates L539-540 ("region of fluent, lexically diverse writing"). Keep one: −2 lines.
  - L429-433: compress to two sentences (§5 below): −3 lines.
  - L105-114 (Homogenization paragraph): drop the Kirk/Wu clause, which is not used later: −2 lines.
  - L521-524: drop "consistent with detectors that showed no bias ..." (already in Related Work L127): −2 lines.
  - L537-540 and L563-565 restate the abstract. Shorten the Discussion's first paragraph to one sentence: −3 lines.
  - Table 2: merge "Threshold 0.4/0.6" and the four nonparametric rows into two rows. That frees space for the no-Claude, no-P2 and trend-2017 rows.
- **"AI Use and Authorship" placement.** ARR exempts Limitations, Ethics, Acknowledgments and References from the limit. An extra unnumbered section after the Ethics statement is very likely fine. Because the main text has no slack, a strict reading would push the paper over. The safe option is to make it a paragraph of the Ethics Statement (`\paragraph{AI use and authorship.}`). **[HUMAN]** Confirm against the ACL 2027 CFP.

### 4.2 Appendix layout

- On p.12 the headings A, B and C stack with empty bodies, and all their floats land on p.13. The App. D text then starts under the C heading.
- **Fix.** Load `float` and use `[H]` for Tables 3-4 and Fig. 4, or add `\clearpage` before `\appendix`.

### 4.3 Anonymity

- PDF metadata: author and title empty; "Anonymous ACL submission". **OK.**
- **Commit hash `ef4fa21` in App. D (L668).** `CITATION.cff` names a public GitHub repository (`NatikChhabra/machine-style-overlap`). If that repository is public, a reviewer can search the hash, or the coined term "Machine-Style Overlap", and find the author.
  - ARR permits preprints but forbids identifying links in the submission.
  - Either keep the repository private during review and supply an anonymised copy (e.g. anonymous.4open.science) with the hash, or replace the hash with "(commit hash in the anonymised supplement)".
  - **[HUMAN]** Check the repository's visibility.
- Supplement hygiene, as in round 2: strip `CITATION.cff` (name, ORCID), the git author fields, the noreply e-mail and the `Co-Authored-By` trailers. `AI_DISCLOSURE.md` says "the human author" (singular); use "author(s)".
- "Used as an agent through Claude Code" and "the system that drafted this paper" do not identify the authors. **OK.**

### 4.4 Limitations, Ethics and AI Use against ACL policy

**Limitations (L570-585).** Present and in the right place, and now covers most round-2 items. Add:
1. The 2025→2026 single-generator changes have no uncertainty, the local regions are trained on 150 texts each, and the 2026 window is nine months.
2. The release-date split and the three 2026 open models were chosen after the 14-generator pattern was seen.
3. RAID's prompts come from 2023+ papers, so the pre-ChatGPT-data region is not topic-matched to the human class.
4. The marker series are not length-controlled.
5. Correct "eight non-physics archives".

**Ethics (L587-593).** Licences are now complete. It could add one clause that the generated texts are released under each generator's terms; the Llama 2 and Gemma licences attach conditions to outputs. That is optional.

**AI Use (L595-608).** This is the best part of the record and is compliant with the ACL policy on AI writing assistance: disclosure, no AI author, human responsibility. Remaining issues:
1. The **verification counts** are stale (§3).
2. **"Every reported result is inserted automatically"** is not literally true (W8c list). Say "every reported statistic from the analysis".
3. **Zero human reading is the single largest acceptance risk.** ACL policy holds the human authors responsible for correctness. A paper with "no human has edited the text" and a pending five-citation spot-check, *and* the visible errors in §2.4, will draw an ethics or responsibility flag. **[HUMAN]** Do a full read-through, fix what you find in `HUMAN-EDIT:` commits, complete the spot-check from a regenerated sheet, and then change the sentence to "The human author(s) read the full paper, corrected N passages (commits labelled HUMAN-EDIT) and checked five randomly chosen citations."
4. The Responsible NLP checklist answer on AI assistants must match this section. **[HUMAN]**

### 4.5 References (rendered list, pp. 9-12)

**Errors to fix**
- Jiang et al. 2024 prints "Computers &amp; Education".
- OpenAI et al. 2025 (gpt-oss) prints "OpenAI, :, Sandhini Agarwal, …".
- Juzek & Ward 2025: "so much? exploring" (lowercase after "?").
- Anderson et al. 2024: "C&C 24" has lost its apostrophe; prefer "Proceedings of the 16th Conference on Creativity & Cognition".
- Askitas 2025: "IZA Network @ LISER. Listing: https://ideas.repec.org/…". Use "IZA Discussion Paper No. 18062, IZA Institute of Labor Economics" with the docs.iza.org URL.

**Inconsistent capitalisation** (protect with braces, or lowercase consistently):
- Bao 2024: "Zero-Shot detection of Machine-Generated text"
- Hans 2024: "Zero-Shot detection of Machine-Generated text"
- Brooks 2024: "AI-Generated content"
- Dugan 2024: "Machine-Generated text"
- Muñoz-Ortiz 2024: "LLM-Generated news text"
- Anderson 2025: "AI-Associated language"
- Lee 2026: "LLM-Associated register shift … Morphology-Aware Excess-Vocabulary study"
- Park 2026: "Non-Native academic writing"
- Touvron 2023: "Fine-Tuned chat models"
- IBM Granite Team 2026: "granite 4.2 8B model cards"
- Geng & Trotta 2025: "Human-LLM Coevolution: Evidence"

**Missing article numbers or volumes** (ACL style puts them in `pages`):
- Gao 2023 npj Digit. Med. 6(1): 75
- Herbold 2023 Sci. Rep. 13(1): 18617
- Kobak 2025 Sci. Adv. 11(27): eadt3813
- Jakesch 2023 PNAS 120(11): e2208839120
- Reinhart 2025 PNAS 122(8): e2422455122
- Muñoz-Ortiz 2024 AI Review 57(10): 269 (verify)
- Sourati 2026 Nat. Hum. Behav.: no volume/pages; mark "online first" or add them.

**Other formatting**
- Crossley 2024 uses initials only, and "S.A." has no space. Give full names as in the other entries.
- Casal & Kessler: "writing?: A study" is the source title, so keep it.
- Bao 2024, Kirk 2024, Padmakumar 2024 and Wu 2025 (ICLR) print "volume 2024, pages …", a scraper artefact. ICLR proceedings have no volume or pages; use "In The Twelfth International Conference on Learning Representations".

**arXiv entries with published versions**
- **Zheng et al. 2023**, "Judging LLM-as-a-Judge", was published at NeurIPS 2023 (Datasets and Benchmarks). For Vicuna's training data you may prefer the LMSYS blog or the FastChat card.
- Park 2026 is "to appear at EMNLP 2026" (batch 7); add a note.
- All other `@misc` entries were checked in batch 7 (Gray, Bentley, Lee, Holzwarth, Rallapalli, Yakura, Lin, Geng 2024: no archival version). **OK.**
- Batch 7 reports that Semantic Scholar was rate-limited and dblp unreachable. **[HUMAN]** Do a quick Google Scholar check of Gray 2024, Holzwarth 2026 and Bentley 2026.

**Duplicates.** None. Liang 2024a/b and Google DeepMind 2025/2026 are distinct works. `yakura2024` renders as 2026 (v4), which is acceptable.

---

## 5. Figures and tables

| Item | Readable | Labelled | Takeaway in caption | n | Consistent with text | Fix |
|---|---|---|---|---|---|---|
| **Table 1** (generators) | Yes | Yes | n/a (inventory) | Texts per generator not given | Vicuna date (2023-08); the "Cutoff" column is blank for 11 of 19, so say "where stated" in the header | Add "150 texts per prompt style per local generator; 450 per generator in the main instrument; 3,532-7,064 per RAID model in the single-generator regions" to the caption. |
| **Fig. 1** (time series) | (a) **No**: the legend box covers the 2025-26 monthly points and the end of the 6-month mean, hiding the plateau stated at L336-337. (b) Raw Hansard points (n≤150/month) without a band. | Yes | Yes | No | (a) contradicts L336-337 visually | Move the legend to `loc="lower right"` or below the axes, or raise ylim to 55 and put it at the upper left of the pre-period. Add "about 300-1,400 scored abstracts and at most 150 speeches per month" to the caption. |
| **Table 2** (robustness) | Yes | Yes | No: the caption describes but gives no takeaway | n/a | Missing rows: trend from 2017 (promised at L271), without Claude (22.5), without P2 (18.0) | Caption: add "Every variant stays within 23.6-29.3 pp; placebo and drift gaps are at most 6.8 pp." |
| **Fig. 2** (vintage) | (a) Mostly; orange gpt-oss and orange-red Claude are close, as are blue and purple. (b) Labels at 5.6 pt, small but legible. | Yes | **Wrong**: "fell against every generator except the two newest" (stale; the text says 4 of 5) | No | (b) is **not in release order**: Granite 4.2 (2026-08) is plotted before Qwen3.5 (2026-02) and Gemma 4 (2026-05) (`figures.py` VINTAGE list). (a)'s "Open models 2024-25" includes gpt-oss, which is also plotted separately. | Reorder VINTAGE to Qwen3.5, Gemma 4, Granite 4.2, Claude. Add bootstrap error bars to (b). New caption in §6. Use a distinct hue for gpt-oss. |
| **Fig. 3** (learners) | Yes; large empty band under the legend | Yes | Yes ("differ in level but agree in direction") | Yes | Yes | Trim the bottom whitespace (`bbox_inches="tight"`). |
| **Table 3** (LOMO) | Yes | Yes | Partial | No | Yes | Add "n held-out texts" to the caption. |
| **Fig. 4** (fields) | **No**: y-labels clipped ("q-bio" → "ɡ-bio", "math" → "nath", "cond-mat" → "-mat", "astro-ph" → "o-ph") | Partly | Yes ("baseline does not predict the gap") | Yes | Yes | `fig.subplots_adjust(left=0.22)` or `bbox_inches="tight"`. |
| **Table 4** (features) | Yes, at `\scriptsize` | Yes | No | n/a | Yes; MTLD 1.29 matches the text | Caption: "Lexical diversity and determiner-noun-verb sequences mark LLM text; coordination, adjectival modifiers and *we* mark human abstracts." |

---

## 6. Line-level writing edits

Format: **L#**: "original" → "replacement" [reason].

### 6.1 Title and abstract

- **L18** (title): fine. "Sounding Like Which AI?" states the contribution. Optionally make the subtitle "… of Abstracts in Eight arXiv Archives with Language Models of Different Vintages". It is long; keeping "arXiv Abstracts" is acceptable if the abstract qualifies it.
- **L30**: "In \R{...} arXiv abstracts (2015--2026)" → "In \R{...} abstracts from eight arXiv archives (2015--2026)".
- **L33-34**: "Against generators whose training data predate ChatGPT, the gap is smaller but clear (7.7 points)." → "Against generators whose pretraining data predate ChatGPT, the gap is smaller but clear (7.7 points; 3.5 with only the two locally run models)." [§2.2]
- **L34-36**: "Against one generator at a time, overlap rose until 2025; in 2026 it fell under all 14 generators released before August 2025 and rose under four of the five released since, including three open models with logged decoding." → "Measured against one generator at a time, overlap rose until 2025 under 18 of 19 generators. From 2025 to 2026 the change correlated with the generator's release date (ρ = …): overlap fell under all 14 generators released before August 2025 and rose under four of the five released later, two of them open models we added to test this pattern." [§2.1, §2.3]
- **L36-37**: "A fixed reference set, or a fixed list of marker words such as \emph{delve}, shows the shift fading as its models age." → "A reference set that is not refreshed can therefore show the shift fading while writing keeps moving; published marker words such as \emph{delve} also fell in 2026." [§2.5; removes the aphorism and the unsupported marker claim]

### 6.2 Introduction

- **L54-57**: "The two questions read one number differently: the small ``LLM share'' that prevalence estimators report for text written before ChatGPT, which studies treat as …" → "The two questions treat one number differently. Prevalence studies treat the small ``LLM share'' they report for pre-ChatGPT text as …". ["Read one number differently" is opaque.]
- **L57-59**: "For a fixed feature map and a fixed set of reference generators, that share describes the two text distributions, and its change over time is our object of study." → "For a fixed feature map and reference set, we treat that share as a property of the two text distributions and study how it changes."
- **L75-77** (Contribution 4): "against generators that cannot have learned it from post-ChatGPT writing; in 2026 overlap fell under every generator released before August 2025 and rose under most newer ones, also within model families, so the trajectory depends on the vintage of the reference" → "against generators whose pretraining data predate ChatGPT; from 2025 to 2026 overlap fell under every generator released before August 2025 and rose under four of the five released later, including within two of three model families, so the trajectory depends on the reference's vintage". [§2.2, §2.4o]
- **L79-80**: "stylistic dispersion of abstracts did not change beyond its pre-ChatGPT trend once length is held fixed" → "we detect no change in stylistic dispersion beyond its pre-ChatGPT trend once length is held fixed". [§2.6]
- **L86**: "The vintage analysis was added after review." → "The vintage analysis was added after two rounds of simulated review (AI Use; Appendix~\ref{app:deviations})." [§2.9]

### 6.3 Related work

- **L99**: "a trend that began before generative AI; our pre-ChatGPT slope points the same way" → keep it, but add "(\R{arxiv_its.all.pre_slope_per_year}\pp{} per year)".
- **L113-114**: "whether ``human'' text remains an independent anchor is the question our vintage comparison bears on." → "our vintage comparison asks whether human text still provides a reference independent of LLM style." [aphoristic inversion]

### 6.4 Data and Method

- **L169**: "For each of eight non-physics archives (cs, math, stat, eess, q-bio, econ, astro-ph, cond-mat; …" → "For each of eight arXiv archives (cs, math, stat, eess, q-bio, econ, and the physics archives astro-ph and cond-mat; …". [§2.4a]
- **L175-176**: "(0.5\% of sampled 2016 papers, 7.8\% of 2021 papers)" → "(0.5\% of sampled 2016 papers, 7.8\% of 2021 and \R{robustness_v4.revision_exclusion_share.y2022}\% of 2022 papers; ending the pre-trend in 2020 leaves the gap unchanged, Table~\ref{tab:robust})".
- **L196-198**: "written from titles of arXiv papers by six 2023 chat models and, for one analysis, five base models. The main instrument uses the 14 generators available before review" → "written by six 2023 chat models from titles of arXiv papers from 2023 onward. The main instrument uses 14 generators". [§2.4h, §2.4j, §2.2]
- **L199-201**: after "…pair with 2025 models of the same families." add "The three 2026 models were generated after the single-generator results for the first 14 generators had been seen, as a test of that pattern (Appendix~\ref{app:deviations})." [§2.3]
- **L263-264**: "(Qwen2.5-0.5B, and GPT-2 small, whose training data predate both essay collections)" → "(Qwen2.5-0.5B, and GPT-2 small, whose 2017 training data are unlikely to contain these essays)". [§2.4g]
- **L273-274**: "each evaluated 12 months later" → "each evaluated 12 months later or in November 2022, whichever is earlier".
- **L275-276**: "41 to 65 months after the fake break and before any LLM writing assistance: an instrument that merely ages would produce one." → "41 to 65 months after the fake break and before any LLM writing assistance, so any gap there reflects instrument ageing." [aphoristic closer]
- **L280**: "and, as the identified comparison, an instrument on generators whose pretraining data predate ChatGPT" → "and an instrument on generators whose pretraining data predate ChatGPT". ["Identified" implies a causal identification the design does not have.]
- **L289-291**: "…so that topic words of the prompt set cancel." → "…which removes most topic words of the prompt set (a few remain, e.g., \emph{robotics})." [§2.5]

### 6.5 Results

- **L305** (heading) "Separable, but not completely": fine.
- **L323-324**: "$\chi^2$ $p\R{…}$" → "$\chi^2(\R{arxiv_its.baseline_field_heterogeneity.dof})=\R{arxiv_its.baseline_field_heterogeneity.chi2}$, $p\R{…}$".
- **L334**: "ranged from \R{arxiv_yearly.2016.mso}\% to \R{arxiv_yearly.2019.mso}\%" → "ranged from \R{arxiv_yearly.2016.mso}\% to \R{arxiv_yearly.2020.mso}\%". [§2.4e]
- **L339-340**: "about 2.14 times the extrapolated trend value" → "2.1 times the extrapolated trend value". [false precision]
- **L346-348**: "The positive one comes from the instrument trained on 2015--2016 only, extrapolated over 65 months from a two-year trend; instrument ageing can thus produce gaps of a few points, about a quarter of the observed gap at most." → "The largest (6.8\pp, from an instrument trained on 2015--2016 and extrapolated 65 months from a two-year trend) is about a quarter of the observed gap; two of the three drift gaps are significant, with opposite signs, so instrument ageing alone moves the gap by several points." [§2.9]
- **L351-353**: "largest in quantitative biology (\R{…q-bio…}\pp) and computer science (\R{…cs…})" → "largest in computer science (\R{arxiv_its.cs.excess}\pp) and quantitative biology (\R{arxiv_its.q-bio.excess})".
- **L398-400**: "A region built only from GPT-4, Llama-2-70B-chat, Llama-2-Chat~7B and Vicuna~7B on the title-only task cannot reflect models that learned from post-ChatGPT writing." → "A region built only from GPT-4, Llama-2-70B-chat, Llama-2-Chat~7B and Vicuna~7B on the title-only task uses models whose pretraining data predate ChatGPT (their instruction tuning used data up to mid-2023)."
- **L403-404**: "about a third of the gap under all 14 generators" → "against \R{arxiv_vintage.local_p1.gap}\pp{} for the seven 2024--25 open models on the same task". [§2.2]
- **L407-408**: "Part of the shift is therefore toward the style of pre-2023 LLMs and cannot be an artefact of newer models learning from newer abstracts." → "Part of the shift is therefore toward the style of 2023-era LLMs and is unlikely to come from newer models learning from newer abstracts. RAID's outputs, however, were written from titles of 2023 papers; the two local models, prompted with pre-ChatGPT titles, give the smaller gap." [§2.2]
- **L411-415**: add uncertainty: "…fell under 15 of the 19 generators (Figure~\ref{fig:vintage}b, with 95\% bootstrap intervals; Spearman $\rho$ between release date and change \R{…})". [§2.1]
- **L419-420**: "The pattern holds within model families, where developer and size are roughly fixed:" → "The pattern holds within two of three model families, where developer and size are roughly fixed:".
- **L425-427**: "The three 2026 open models, run with logged decoding, give the same 2026 rise as the 2026 model (…% to …%), so it does not rest on the uncontrolled generator." → "Pooled, the three 2026 open models, run with logged decoding, also rise in 2026 (\R{arxiv_vintage.open2026_p1.y2025}\% to \R{arxiv_vintage.open2026_p1.y2026}\%, against \R{…claude…y2025}\% to \R{…claude…y2026}\% for Claude), so the rise does not rest on the uncontrolled generator alone."
- **L429-433**: "The aggregate series in Figure~\ref{fig:ts}a mixes these: it flattened in 2026 because most of its 14 generators are older than the abstracts it now measures. Any reference set that is not refreshed will show the shift fading as its models age, whether or not writing moves on. We cannot tell … The pre-ChatGPT-data region is the only comparison free of that ambiguity." → "The aggregate series in Figure~\ref{fig:ts}a mixes these, and its 2026 flattening is consistent with most of its 14 generators predating the abstracts it now measures. We cannot tell whether 2026 abstracts moved toward the newest models or those models learned from 2025 writing; the pre-ChatGPT-data region is least affected by that ambiguity." [two aphorisms out; −3 lines]
- **L449-450**: "so the fair comparison is with marker words of the same generators that define each style region" → "so we also compare with words mined from the generators that define each style region".
- **L454-460**: "…including gpt-oss and Qwen3.5, under which style overlap rose; it kept rising only for the 2026 model (…), whose mined words (…) are ordinary academic vocabulary rather than conspicuous markers. Lexical and stylistic measures therefore diverge in 2026 for some recent generators, not for older ones: once markers and style region come from the same model, the decline of \emph{delve} mostly reflects the age of the reference." → "…including gpt-oss and Qwen3.5, under which style overlap rose; it rose only for Granite~4.2 and Claude, whose mined words (\emph{substantial}, \emph{comparable}, \emph{whose}) already appeared in \R{arxiv_vintage.single:claude-opus-5.5.m2015}\% of 2015 abstracts. Lexical markers therefore fell in 2026 even where style overlap with recent models rose, consistent with authors avoiding publicised words \citep{geng2025}." [§2.4f, §2.5]
- **L470-471**: after the macro fix, "(on the logit scale 0.28 against 1.49)" → "(0.28 against 1.49 on the logit scale)".
- **L474**: after "Hansard is a weak comparison, however:" add "its marker-word gap is \R{hansard_its.marker.excess}\pp{} (CI …), and". [N6]
- **L489-492**: "(bootstrap CI −35.9 to 50.8). Within the precision of this measure, the post-ChatGPT change is a shift toward the LLM region without a faster loss of stylistic spread; diversity of content or ideas may behave differently" → "(bootstrap CI $-0.36$ to $0.51$, i.e. within about three years of the pre-ChatGPT trend). We detect no acceleration in the loss of stylistic spread but cannot exclude a modest one; diversity of content or ideas may behave differently". [§2.4b, §2.6]
- **L506**: delete "In essays the LLM region is largely a region of fluent, lexically diverse writing." It is repeated in L539-540. Keep the Discussion version. [−2 lines]
- **L520**: "GPT-2 was trained before either collection was public, so the contrast does not come from memorised essays." → "GPT-2's training data (web pages linked from Reddit up to 2017) are unlikely to contain these essays, which makes memorisation an unlikely explanation." [§2.4g]
- **L521-524**: delete "consistent with detectors that showed no bias in a large writing assessment \citep{jiang2024}" (it duplicates L127). [−1 line]

### 6.6 Discussion and Conclusion

- **L537-541**: "…so ``sounding like AI'' there partly means writing well." → "…so in essays, flagged writing tends to be writing that receives higher holistic scores." [aphoristic closer; ties the claim to the measured variable]
- **L542** (heading) "The reference decides the trajectory." → "Trajectories depend on the reference."
- **L544-546**: "The same holds for lexical markers: the rise and fall of \emph{delve} is mostly what any fixed word list or reference set would show as its models age." → delete. [§2.5]
- **L546-548**: "…marker lists built on a fixed set of models will understate recent change unless the reference is refreshed" → "…built on a fixed set of models may understate recent change unless the reference is refreshed".
- **L549-551**: "Both readings imply that LLM style and human scientific style are no longer independent anchors for each other, which is the precondition, though not evidence, for the recursive dynamics studied in model-collapse work" → "Under either reading, LLM style and human scientific style are no longer independent references for each other. This is a precondition for the recursive dynamics studied in model-collapse work, not evidence of them".
- **L558**: "Every instrument we tried flags fluent student writing more than learner writing" → "Every instrument we tried flags non-learner essays more often than learner essays".
- **L565-567**: "Which models define ``LLM style'' decides whether the shift looks finished: against older generators it receded in 2026, while against the newest it continued." → "Measured against generators released before August 2025 the shift receded in 2026; measured against the newest it continued."

### 6.7 Limitations, AI Use, Appendix D

- **L572**: "Four generators are from 2026; one of them was run …" → "Four generators are from 2026, three of them added after the 2025--2026 pattern for the others had been seen; one (Claude) was run …".
- **L576**: "eight non-physics archives" → "eight arXiv archives".
- **Limitations, add after L580**: "The 2025--2026 changes under single-generator regions rest on instruments trained on 150 texts per local generator and compare a nine-month window with a full year. RAID outputs were prompted with titles of 2023 papers."
- **L604-606**: "…leading to 11 rewordings, one removed citation and 20 preprints replaced by published versions" → update the counts after batches 6-7, or write "leading to rewordings, one removed citation and replacement of preprints by published versions (counts in the supplement)".
- **L606-607**: "Every reported result is inserted automatically from the analysis outputs." → "Every reported statistic from the analyses is inserted automatically from their outputs."
- **L676-678**, App. D(3): "Added after an arXiv pilot on partial data and before the first review: Phi-4, Granite and the 2026 model, whose texts were merged two minutes after a preliminary arXiv run without them was committed" → "Decided after an arXiv pilot on partial data: Phi-4, Granite~3.3 and Claude. Claude's prompt batches were committed two minutes after a preliminary arXiv run without them and its texts were used from the first version; Phi-4 and Granite were first used after the first review".
- **L680-683**, App. D(5): "…the vintage analysis with Llama-2-Chat~7B and Vicuna~7B…" → "…the vintage analysis with Llama-2-Chat~7B and Vicuna~7B, and Qwen3.5, Gemma~4 and Granite~4.2, which were generated after the single-generator results for the first 14 generators had been seen (two of the three rose in 2026)…". Also add to the cleaning-fix clause: "(13\% of local arXiv and 18\% of essay LLM texts; the primary gap was 25.7\pp{} before and after)".

### 6.8 Terminology

| Term | Problem | Fix |
|---|---|---|
| "the 2026 model" | Ambiguous now that four generators are from 2026 (§2.8) | "Claude" or "Claude Opus 5.5" throughout, text and Table 3 |
| Pre-ChatGPT-data generators | Five names: "generators whose training data predate ChatGPT" (L33), "pre-2023 LLMs" (L408), "pre-ChatGPT-data generators" (L453), "models trained before ChatGPT" (L565), "Pre-ChatGPT training data" (Fig. 2) | Define "pre-ChatGPT-data generators" once (L64) and use it. "Pre-2023 LLMs" is also wrong: they were released in 2023. |
| vintage | Used for release date (Fig. 2b, "released before August 2025") and for data cutoff (pre-ChatGPT-data region) | One sentence at L64: "By vintage we mean release date, except for the pre-ChatGPT-data region, defined by pretraining cutoff." |
| "2023 models" / "2023-era" / "RAID 2023 chat models" | Mixed | "2023 chat models" |
| field / archive | Defined at L170 and used consistently | OK |
| instrument, LLM region, trend gap | Defined (L159, L141, L269) | OK |
| "current models" | Gone | OK |

### 6.9 Patterns that read as AI-generated

These are much reduced since round 2. What remains:

**Aphoristic closers**
- L276 "an instrument that merely ages would produce one"
- L431 "whether or not writing moves on"
- L433 "the only comparison free of that ambiguity"
- L540 "partly means writing well"
- L542 "The reference decides the trajectory"
- L566 "decides whether the shift looks finished"

All six have replacements above.

**"X, not Y" / contrastive pivots**
- L458-459 "for some recent generators, not for older ones"
- L511 "ordinary academic vocabulary rather than conspicuous markers"
- L592 "compares groups, never individuals"

The first two are rewritten above. The third is fine in an Ethics statement.

**Inversions with a delayed subject**
- L113-114 "whether 'human' text remains an independent anchor is the question our vintage comparison bears on"
- L549-551 "which is the precondition, though not evidence, for…"

Both are rewritten above.

**Parallel triads**
- L47-50 "readers are poor…, detectors can be evaded…, and some detectors have flagged…"
- L546 "Detectors, prevalence estimators and marker lists"

Both are acceptable. Do not add more.

**"Therefore" chains.** L64, L172, L407, L458 and L567 each draw a "therefore" conclusion; two of them (L407, L458) overreach. The rewrites above remove both.

---

## 7. Expected scores and decision

| | Round 2 (expected) | Round 3 as submitted | Round 3 after the §8 changes |
|---|---|---|---|
| Soundness | 3 (2.5-3.5) | **3** (2.5-3.5). Robustness is now strong; the vintage inference lacks uncertainty, and the visible errors cost half a point with careful reviewers. | 3.5 |
| Excitement | 3-3.5 | **3.5**. "Sounding like which AI?" is a fresh, theme-central question with a clean, quotable answer, plus the anchor/model-collapse link. | 3.5-4 |
| Overall | ~3.0 | **3.0-3.5** (spread 2.5-4) | ~3.5 |
| Reviewer confidence | | 3-4 | |

**Likely decision: Findings of ACL.**
- *Main conference:* borderline after the changes below, because the theme-track fit is strong.
- *Reject:* unlikely unless an ethics reviewer escalates the "AI-conducted, no human reading" combination. A human read-through and a completed spot-check remove most of that risk.

---

## 8. The five changes with the biggest effect

1. **Put uncertainty and a pre-specified statistic on the vintage result, and log how it was reached.**
   - Bootstrap CIs for every 2025→2026 change (documents × training texts or seeds), shown as error bars in Fig. 2b.
   - Spearman ρ (release date vs change) with a permutation p, replacing the post-hoc "August 2025" split in the abstract.
   - Matched 12-month windows.
   - State in §4, App. D(5), plan dev. 9 and the README that Qwen3.5, Gemma 4 and Granite 4.2 were added after the pattern was seen, as a test, and that 2 of 3 conformed.
   - Fix the Fig. 2 caption and the release order. Label 2026 as exploratory.
   - About a day of CPU, no new generation.
2. **Fix every factual and rendering error in §2.4**, at the root:
   - Repair `make_numbers.py`'s PCT prefix/suffix rule and add asserts for `ci_lo` and `logit_gap`.
   - Compute the yearly min/max and the "only X rose" lists in code instead of typing them.
   - Correct "non-physics", the GPT-2 claim, Phi-4/Granite timing, the dangling base models and the three reference-list artefacts.
   - Fix Fig. 1a's legend and Fig. 4's labels.
   - This is cheap. It is the difference between "careful" and "unchecked" for every reviewer.
3. **Make the pre-ChatGPT-data and marker claims match the evidence.**
   - Compare 7.7 pp with the P1-only 2024-25 region (20.2), lead with the local-only 3.5 pp as the conservative number, and disclose RAID's 2023-title prompts and the 2023 tuning data. Replace "cannot" with "unlikely".
   - Length-control the marker series, and replace the "decline of *delve* reflects the age of the reference" claim with what the data show: markers fell even against new references.
   - Scope the dispersion conclusion to its interval.
4. **Report the sensitivity results you already have** (§2.7) in Table 2 or one sentence each:
   - without Claude (22.5);
   - without the revision prompts (18.0);
   - pre-trend from 2017 (26.8);
   - 2022 revision exclusion (24.2%);
   - Hansard marker gap (+1.6).
   Also rename "the 2026 model" to "Claude". Pay for the space with the cuts in §4.1.
5. **Make the human role real and visible.** **[HUMAN]**
   - Read the whole paper and log corrections as `HUMAN-EDIT:` commits.
   - Regenerate `SPOT_CHECK.md` from the current text and complete it.
   - Label or explain commit 6675865.
   - Recount the verification numbers.
   - Move AI Use into the Ethics Statement.
   - Check repository visibility before citing a commit hash.
   - Then the AI Use section can truthfully say that a human read the paper, corrected errors and checked citations. Under ACL's responsibility policy that removes the most likely reason for an ethics flag, and for a reviewer's general distrust of an AI-conducted paper.
