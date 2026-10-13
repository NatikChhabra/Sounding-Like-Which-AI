# Round 4: Final verification pass (senior ACL reviewer)

Scope: `paper/main.tex` and the compiled `main.pdf` (15 pages; the body ends on p. 8), `results/*`,
`code/{analysis,features,make_numbers,figures,mso}.py`, `preregistration.md`, `paper/AI_DISCLOSURE.md`,
`README.md`, and the three round-3 reviews. I read every number in the text from `results/`, re-ran no analysis
that writes to `results/`, and ran one read-only check of the cleaning rules on the raw data (`F:\research-data`).

**Verdict.** The revision closes most of what round 3 asked for. All 210 `\R{}` keys resolve, and every value I
checked (45, listed in section 2) matches the results files and is formatted correctly. Three new problems remain:

1. A code bug: the "No dash features" robustness row does not remove em or en dashes.
2. One requested statistic was computed, came out null, and is not reported.
3. Some abstract and Discussion sentences claim more about the 2026 open models than the quarterly data show.

None of these changes the headline finding, and each takes under an hour to fix.

---

## 1. Round-3 "top changes": status

### AC (round3_AC.md §8)

| # | Request | Status | Evidence |
|---|---|---|---|
| 1a | Bootstrap CIs for each 2025→2026 change, plus seed ranges | **Done** | `arxiv_vintage_uncertainty.csv` gives document-bootstrap CIs and a 5-seed min/max for all 19 single-generator regions and 7 pooled regions. The text (§6.4) states the result correctly: all changes except Gemma 4 exclude 0 and keep their sign in 5/5 seeds. |
| 1b | Error bars in Fig. 2b | **Not done** | Fig. 2b now plots the peak quarter, with no uncertainty. |
| 1c | Spearman ρ of release date vs **change**, with a permutation p | **Partly; see issue M2** | ρ(release, change) is computed in `arxiv_vintage_release_corr.json`: annual 0.66 (p=0.003); from 2025Q4, **0.22 (p=0.37)**. Neither is reported. The paper reports a different statistic, ρ(release, **peak quarter**) = 0.83, with an asymptotic p rather than a permutation p. |
| 1d | Matched 12-month windows | **Partly** | The change is measured from 2025Q4 to the 2026Q1–Q3 mean (1 quarter against 3), not over matched 12-month windows. |
| 1e | Log the post-hoc 2026 open models; say 2 of 3 conformed | **Mostly done** | App. G(5) and plan deviation 9 say "added after the pattern had been seen". "2 of 3 conformed" is not stated. Label "exploratory": done for ρ. |
| 1f | Fix the Fig. 2 caption and release order | **Done** | Release months now match Table 1 and `RELEASE`. |
| 2a | `make_numbers` PCT rule, plus asserts for `ci_lo` and `logit_gap` | **Done** | Asserts are present (lines 102–103). All rendered keys checked in §3. |
| 2b | Compute yearly min/max and the "only X rose" lists in code | **Partly** | `vintage_summary` writes `rose`, but the text types the names. The yearly range uses hand-picked keys `2016`/`2020`. They are correct now, but are not computed. The quarter-of-peak lists in §6.4 are typed. |
| 2c | "non-physics", GPT-2 claim, Phi-4/Granite timing, base-model sentence, reference artefacts | **Mostly done** | "non-physics" is gone, the Phi-4/Granite timing is in App. G(3), and the base-model sentence is gone. The GPT-2 claim is softened but still too strong (m5). Some reference artefacts remain (m9). |
| 2d | Fig. 1a legend; Fig. 4 labels | **Partly** | Fig. 4 is fine. **Fig. 1a's legend now hides the 2024–25 rise** (issue M5). |
| 3a | Pre-ChatGPT-data: compare with the P1-only region; lead with 3.5 pp; disclose RAID prompt and 2023 tuning; "cannot"→"unlikely" | **Partly** | Comparison with `local_p1` (20.3): done. The RAID-prompt caveat is in the text. The abstract still leads with 7.5, not 3.5. §6.4 still says the generators "**cannot** have learned their style from post-ChatGPT scientific writing (… but not arXiv abstracts)" (issue M4). |
| 3b | Length-control the markers; replace the *delve* claim | **Not done** | There is no length-controlled marker series. §6.5 still says "the decline of *delve* mostly reflects which models the markers come from", which the paper's own numbers contradict (issue M3). |
| 3c | Scope the dispersion conclusion | **Done** | App. C: "excludes an extra decline larger than about three years of trend" (−0.36/−0.11 ≈ 3.3). |
| 4 | Report existing sensitivities | **Mostly done** | Table 2 has no-Claude 22.2 and no-revision 17.9. §4 has the 24.2% revision exclusion, and App. B has the Hansard marker gap of 1.6. The pre-trend from 2017 (26.5) is not reported (2019 and to-2020 are). "2026 model"→"Claude" was **not** done, and Fig. 2a now says "Claude" while the text says "the 2026 model". |
| 5 | **[HUMAN]** read-through, `HUMAN-EDIT:` commits, completed spot-check | **Not done** | Zero `HUMAN-EDIT:` commits, and every box in `lit/SPOT_CHECK.md` is unticked. The paper and the disclosure say so honestly. |

### R1 (round3_R1_methods.md §9)

| # | Request | Status | Evidence |
|---|---|---|---|
| 1 | Narrow the vintage claims | **Partly** | "fixed set shows fading" is now a forecast ("will eventually show the shift receding"), which the 13-generator set without Claude does support (37.9→36.8, `arxiv_gensets.csv`). The paper acknowledges that the 14-generator set rose. Drift placebos for the pre-ChatGPT-data region (+0.5/−1.3/−2.0) and 3.5 pp are reported. The component's 2026 decay is given as MSO 11.9%, not as a gap above trend. |
| 2 | False statements | **Done** | fmt bug, Granite 4.2 marker sentence, Fig. 2 caption, "up to about a quarter", archive weighting, "pretraining". |
| 3 | Uncertainty on the vintage design | **Mostly done** | Δ CIs and seed ranges, region drift placebos, and the 30-month grid (24 breaks, 8.3%, max 5.8) are in. There is no tie band and no table of the six region definitions (only four variants are in the text). |
| 4 | Cutoff axis | **Partly** | Table 1 cutoffs are filled where stated, and the "gpt-oss vs Gemma 4" argument is in. No plot against cutoff. |
| 5 | Round-2 leftovers | **Partly** | Done: never-revised check, field TPR, family ablation. Not done: astro-ph/econ level shifts, trend-based FPR. The implied α still uses pooled TPR. |

### R2 (round3_R2_nlp.md §7)

| # | Request | Status | Evidence |
|---|---|---|---|
| 1 | Quarterly series, peak timing **with intervals**, Δ vs Q4, Gemma 4 as no change, Granite-only within-family claim | **Mostly done** | Peak quarters have no instrument-variation intervals. For flat-topped curves the argmax is fragile (Gemma 3: 32.0/32.6/33.0/32.6 across 2025Q2–2026Q1). |
| 2 | Define vintage; drop the Aug-2025 split; cutoffs; soften "cannot" | **Mostly done** | A vestige remains: Fig. 2a still draws a separate "gpt-oss (Aug 2025)" line. "cannot" remains (M4). |
| 3 | Match the task (summary filter on RAID singles, decoding, length) | **Not done**, except cleaning | RAID single regions still include summary-register outputs (chatgpt 30.6%, cohere 32.9%, mistral 21.5%). There is no length-matched refit; a Limitation acknowledges length. Residual-artefact cleaning is done. |
| 4 | Feature ablation + zero-shot baseline | **Mostly done** | The ablation covers the main gap only, not the pre-ChatGPT-data gap or the single-generator Δ signs. Fast-DetectGPT uses GPT-2 small, so it is a weak baseline. The text says so. |
| 5 | Factual and presentation fixes | **Partly** | Done: Pu et al. and Sun et al. added, perplexity AUC reported (0.830), Contribution 5 fixed, dispersion fixed. Not done: spell-normalised rerun, Ollama tags/quantisation disclosure, filtering Claude's near-copy P2 outputs. |

---

## 2. Numbers verified against results (45 checks; all match unless noted)

| # | Claim (location) | Value in paper | Source and check |
|---|---|---|---|
| 1 | Corpus size (abstract) | 131,448 | `corpus_stats.arxiv_n_docs` ✓ |
| 2 | Pre-ChatGPT MSO (abstract) | 9.2 (8.9–9.5) | `arxiv_baseline_pre2022` ✓ |
| 3 | Trend gap (abstract) | 25.4 (23.2–27.7) | `arxiv_its.all` 0.2544 ✓ |
| 4 | Block bootstrap | 23.3–27.3 | `robustness_v4` ✓ |
| 5 | Ratio to trend | 2.09 | 0.2544 / trend 0.122 ✓ |
| 6 | Yearly range 2015–21 | 7.3 (2016), 10.2 (2020) | Min is 2016 and max is 2020 ✓ (2019 9.9, 2021 9.7) |
| 7 | 2022–2026 yearly values | 11.1, 17.7, 27.8, 40.6, 44.7 | ✓ |
| 8 | Robustness range, "between 23.5 and 29.1" | | Over the threshold/sample/trend rows of Table 2 the minimum is thr 0.6 and the maximum is no-math ✓ |
| 9 | Ablation | MTLD 25.4; range 22.9 (function words) to 26.6 (POS) | Deps 25.0, punct 25.7, sentence 25.4 are inside the range ✓ |
| 10 | Fast-DetectGPT | AUC 0.737; 8.3 / 11.3 / 5.3 | ✓. "Does not rise" holds: the maximum is 11.7 in 2018. |
| 11 | Placebo grid | 34 breaks, 8.8%, max 3.2 | ✓ |
| 12 | 30-month grid | 8.3%, max 5.8 | 24 breaks ✓ |
| 13 | Drift placebos | 6.5 / −2.3 / −1.0 | ✓. 6.5/25.4 = 0.26, so "about a quarter" ✓. Note: −2.3 has p=0.020; not discussed. |
| 14 | Event residuals | within ±1 through 2022; 6.4 / 16.1 / 28.5 / 32.2 | Maximum pre-period \|resid\| is 0.60 ✓ |
| 15 | Field ranking | cs 38.1, q-bio 36.2 (largest); math 10.5, astro 13.7 (smallest) | ✓ |
| 16 | Holm | "all adjusted p<0.001" | Largest is econ, 1.9e-10 ✓ |
| 17 | cs − math | 27.6 (22.2–32.9) | ✓ |
| 18 | Implied α (2024) | 42.1 / 7.8; LOMO 44.4 / 8.2 | ✓ |
| 19 | TPR by field | 85.8 / 75.8 | n = 551 / 566 ✓ |
| 20 | Revision exclusion | 0.5 / 7.8 / 24.2% | ✓ |
| 21 | Never-revised | 40.7 vs 40.6; 44.7 vs 44.7 | ✓. The "all" values equal `arxiv_yearly` (same instrument). |
| 22 | Pre-ChatGPT-data region | 6.5 / 15.5 / 17.9 / 11.9; gap 7.5 (4.6–10.4) | ✓ |
| 23 | Region variants | `local_p1` 20.3; summary kept 8.6; +ChatGPT 7.4; old open 3.5 (1.5–5.5) | ✓ |
| 24 | "Three quarters … from RAID" | | Capped training mix is 900 RAID / 1,200 ✓ |
| 25 | Region drift placebos | 0.5 / −1.3 / −2.0 | ✓ (the last has p=0.001) |
| 26 | "rose 2022→2025 under every generator except Cohere" | | Cohere 10.3→9.3; all 18 others rose ✓ |
| 27 | Peak quarters by vintage group | | 2023 models 2024Q3–2025Q2; 2024 models 2025Q2–Q3; Gemma 3, Granite 3.3, Qwen3 2025Q4; gpt-oss 2026Q2, Qwen3.5 2026Q1, Granite 4.2 2026Q2; Claude 2026Q3 (last) ✓ |
| 28 | ρ(release, peak) | 0.83, n=18, p<0.001 | ✓. Claude is excluded (no release month). |
| 29 | Annual 2025→2026 counts | fell under 15/19; rose: gpt-oss 29.4→38.5, Qwen3.5, Granite 4.2, Claude 29.3→39.2 | ✓ |
| 30 | Gemma 4 | −0.9 (−1.8 to 0.1); 4/5 seeds | ✓ |
| 31 | Change from 2025Q4 | Qwen3.5 +0.4; Granite 3.3 −3.9; Granite 4.2 +2.9 | ✓ |
| 32 | "Newer model fared better in all three pairs" | | ✓ on both annual and Q4 measures |
| 33 | 2026 open models pooled | 28.9→34.9 (annual) | ✓ |
| 34 | "12 of its 14 single-generator regions fell" | | 14 = 19 minus 5 vintage-only; rose: gpt-oss and Claude ✓ |
| 35 | "carried by gpt-oss and the 2026 model" | | Without Claude, the 13-generator set fell 37.9→36.8 (`arxiv_gensets.csv`) ✓ |
| 36 | Published markers | 1.1 / 5.3 / 1.5; peak in 2024; gap 1.9 (0.8–3.0) | ✓ |
| 37 | Mined markers | rose 2022→25 for all 19; fell in 2026 for 17/19; Granite 4.2 33.6→35.6; Claude 49.1→57.5 | ✓ |
| 38 | Point-biserial and in-region shares | r = 0.12; 5.9 vs 1.4 | ✓ |
| 39 | Hansard | 1.3 (−0.7–3.4); difference 30.7 (28.3–33.2); 8-generator arXiv gap 32.1; placebo grid 23.5% | ✓ |
| 40 | Hansard pre-trend range | −3.2 to 3.1 | Minimum is to-2020, maximum is quadratic ✓ |
| 41 | Dispersion | 0.05 (−0.36–0.51), trend −0.11/yr; 34.20→30.86 | ✓ |
| 42 | Learners | 2.3 vs 4.2; OR 0.55 (0.32–0.95), 0.87 (0.50–1.52); 15 of 666; significant in 10/10 seeds | ✓ |
| 43 | Perplexity instruments | GPT-2 AUC 0.830; 29.2%; 15.5 vs 30.6; logppl 3.74 / 3.43; TOEFL 63.7 vs 8.0; Qwen 41.8 vs 3.4 | ✓ |
| 44 | Classifier agreement | 22.8 / 22.6; κ 0.64 / 0.26 / 0.29 | ✓ |
| 45 | Held-out-generator recall range | 59.6 (Cohere) – 95.6 (GPT-4); Claude 20.7, essays 36.4; P2 AUC 0.675 | ✓ (minimum and maximum exclude Claude, as the text says) |

`make_numbers.fmt` renders correctly for every key used. The checked families are: `y####`/`m####` ×100;
`summary_register_share` ×100 (0.054→5.4); `pre_slope_per_year` ×100 (0.005→0.5 pp); `relative_gap`/`logit_gap`
raw; `*dispersion*` raw, including `ci_lo`/`trend_per_year`; `alpha`/`tpr` ×100; `rho` raw; `rho_p`/`excess_p`/`field_holm`
as p-values; `mean_logppl_*`, `coef_*`, `or_*`, `odds_*` raw; `n_*` as integers. **No value is off by ×100, and no
decimals are wrong.** `make_numbers.missing()` returns `[]`.

---

## 3. Code checks of the new analyses

- **`nodash` (BUG, issue M1).** `analysis.py:901` reads `mso.EXCLUDE = ("pun:â€”", "pun:â€“", "pun:-")`.
  These are UTF-8→cp1252 mojibake strings (bytes `c3 a2 e2 82 ac e2 80 9d`). They were introduced in commit
  d5dac01 (round-2 fixes). The previous commit 6e16675 had the correct bytes `e2 80 94`. `_mask` uses
  `startswith`, so **only the hyphen is excluded**: em-dash and en-dash features stay in the "No dash features"
  instrument. The output confirms it: `pun:-` disappears from `arxiv_nodash_features_llm_typical.csv`, and the
  result (25.41 vs 25.44) is almost identical to the primary.
  Mitigating: the new `ablation` "punctuation" row removes every `pun:` feature and gives 25.7, so the
  conclusion survives. The row as labelled is still false.
- **`vintage_quarterly`.** Correct. The region is trained exactly as in `vintage()`: Claude's `mso_2026` = 39.2 =
  `y2026`. `peak = idxmax` takes the first maximum, has no uncertainty, and is censored at 2026Q3. Censoring is
  harmless for the reported ρ because Claude is excluded. `change_q4` compares 2026Q1–Q3 with one quarter. The
  docstring promises "rank correlation of release date with the 2026 change". It was computed and is null from
  Q4 (ρ = 0.22, p = 0.37), and it goes unreported (M2).
- **`vintage_peak`.** Correct for what it computes (18 generators; Claude dropped via `RELEASE`). The job
  `vpeak` is **not in any run script** (`run_v5.ps1`, `run_v5b.ps1`) or in the README job list, so the figure and
  the abstract statistic cannot be reproduced from the documented pipeline (m7).
- **`ablation`.** Correct. `EXCLUDE` is restored in `finally`, and the "none" row reproduces the primary
  (0.25444). "sentence_and_length" (`s:`) also removes MTLD, which is fine. It covers the main gap only.
- **`fastdetect`.** The analytic criterion is implemented correctly (sampling model = scoring model = GPT-2;
  (Σll − Σμ)/√Σσ²). The AUC is in-sample ("heldin"), which the key name admits. NaN scores are set to 0 before
  calibration; this is harmless. The yearly samples are not field-stratified, which is minor.
- **`robustness_v5`.** Correct. `mso.SEED` is read at call time in `training_set` and the GBM, and is reset in
  `finally`. Seed-0 changes equal `vintage` exactly (max |diff| 1e-16). The bootstrap resamples documents and
  ignores field-month clustering, so the intervals are slightly narrow. The never-revised id join works (60–76%
  never-revised by year). The TPR join leaves RAID and v1-only seeds as "other", so it rests on 551/566 texts.
- **`features._MD` cleaning.** I ran the rules on the raw data. The inline-label rule
  `\b(abstract|speech|essay)\s*:` also fires on 13 human abstracts, 25 human speeches and 1 essay (for example
  "in his speech: …" loses its colon). The effect is negligible but asymmetric in principle, so anchor it or
  apply it to LLM text only. The `Title:` rule hits no human text. No local or Claude output becomes empty.
  **RAID chat outputs** (not cleaning-related): 42 chat-model texts clean to fewer than 30 words, 11 of them
  empty (URLs, HTML, "Read More"). They enter the LLM class, while human abstracts under 50 words are removed
  (m8).

---

## 4. Claims checked in the abstract, introduction, §6.4, Discussion and Conclusion

**Unsupported or overstated:**

1. **Abstract:** "under the newest, including open models run with logged decoding, it was still rising in
   2026". Quarterly, **no** 2026 open model was still rising at the end: Granite 4.2 peaked in 2026Q2, Qwen3.5 in
   2026Q1 (flat from Q4 by the paper's own account) and Gemma 4 in 2025Q4. Only Claude was rising in 2026Q3. The
   support offered in §6.4 ("rose with the 2026 model, 28.9%→34.9% on annual means") is the annual-mean measure
   that round 3 showed manufactures rises. What the data do support is "peaked in 2026 rather than earlier". (M3a)
2. **§6.5:** "Once markers and style region come from the same model, the decline of *delve* mostly reflects which
   models the markers come from." This is contradicted by the same paragraph: mined markers fell in 2026 for
   17 of 19 references, including gpt-oss and Qwen3.5, whose style overlap rose, and Gemma 4, released in 2026.
   The decline is general across references, not specific to the reference. (M3b)
3. **§6.4:** "models that **cannot** have learned their style from post-ChatGPT scientific writing (their
   instruction tuning used 2023 data, **but not arXiv abstracts**)". The tuning data of GPT-4-0613 and
   Llama-2-chat are undisclosed. Vicuna is tuned on ShareGPT, which consists of user-shared ChatGPT conversations
   (Table 1, note d), so the "not arXiv abstracts" part cannot be verified and is unlikely for Vicuna. (M4)
4. **Discussion:** "words mined from most generators, including two whose style overlap **kept rising**". One of
   the two is Qwen3.5, which §6.4 calls flat from 2025Q4 (+0.4) and which peaked in 2026Q1. (m1)
5. **Conclusion and abstract:** "Overlap with **each** generator peaked later the more recent the generator".
   This is a tendency (ρ = 0.83), with Gemma 4 a stated exception. Say "in general" or give ρ. (m2)
6. **§6.4:** "only Granite shows opposite signs". From 2025Q4, Qwen3 (−4.2) and Qwen3.5 (+0.4) also have
   opposite signs; the text calls +0.4 "flat". Say "only Granite shows a clear rise against a fall". (m3)
7. **§6.5:** "whose mined words (*substantial, comparable, implications, whose*) are ordinary academic vocabulary".
   The relative clause refers to Granite 4.2 and Claude, but all four words come from Claude's list. Granite
   4.2's list (*grounded, interpretable, superior, principled, …*) is not "ordinary". (m4)
8. **Contribution (1):** MSO "equals the human-side component of the Bayes error". It equals the Bayes FPR, which
   is twice the human-side term in ½(FPR+FNR). Say "equals the Bayes classifier's false-positive rate". (m6)
9. **AI Use:** "Every result of our analyses reported in the paper is inserted automatically". This is false.
   Peak quarters, "12 of its 14", "except Cohere's chat model", "all three pairs", "±1 pp", "three quarters",
   the mined words and the typed names of the generators that rose are all typed. The disclosure's phrase
   "design constants are typed" does not cover them. (M6)

**Supported:** the abstract's 9.2 / 25.4 / 7.5 / ρ 0.83 over 18 generators, and the learner and TOEFL sentence.
In the introduction, the contribution counts (19 generators; 4 pre-ChatGPT-data, 4 from 2026), the "quarter as
large or smaller" placebo and drift claim, and Contribution 5. In §6.4, every count and quarter list (§2 #26–35).
The Discussion's κ values and the "every instrument" learner claim (style 2.3/4.2, embeddings 5.3/10.0, GPT-2
15.5/30.6, Qwen 7.1/15.6). **What ρ excludes:** Claude, because its release month is not used. The abstract's
"18 generators" against "19" elsewhere is never explained in the text, only in the Fig. 2 caption.

---

## 5. Figures, tables, references

- **Fig. 1a (M5).** The legend (white box, `framealpha=0.9`, placed at `bbox_to_anchor=(0, 0.62)`) covers the
  arXiv series between about 28% and 38% in 2024–25: the central rise of the paper's headline figure is hidden.
- **Fig. 2b (M5).**
  - No colour legend.
  - Colours **contradict panel (a)**. In (a), orange = gpt-oss and green = "open models 2024-25". In (b), orange
    = 2024 releases and green = 2025 releases, including gpt-oss.
  - Vicuna and Llama-2-7B are pink, which (a) defines as "RAID 2023 chat models".
  - Overplotting hides 2 of the 8 pink points: ChatGPT and MPT both sit at 2023.45/2025Q1, and Llama-2-70B and
    Llama-2-7B both sit at 2023.55/2025Q1.
  - Claude's open circle is placed at x = 2026.85, which implies a release after the data end.
  - The ρ label omits n=18 and "Claude excluded".
- **Fig. 2a.** The "gpt-oss (Aug 2025)" line is a leftover of the dropped August-2025 split. Naming is
  inconsistent: the legend says "Claude (2026 model)", the text says "the 2026 model".
- **Table 2.** The "No dash features" row is wrong (M1). It reports the instrument drift placebos but not the
  pre-ChatGPT-data region's drift placebos (those are in the text).
- **Appendix F** "Top features" is an empty heading followed directly by G, with Table 4 floated above it. The
  table row label "punctuation ," is hard to read; use `\texttt{,}`.
- **Feature text (§6.1)** lists *we* among the top human-typical features. *we* is 11th and does not appear in
  Table 4 (top 10), while *are*, aux and *is* (ranks 5–7) are skipped.
- **References (m9).**
  - "Daniel Mcfarland" should be McFarland.
  - "Granite 3.3 8B instruct and granite 4.2 8B model cards": lowercase "granite".
  - Title-case artefacts: "Traces of AI-Associated language", "Machine-Generated text detectors",
    "AI-Generated content".
  - "arXiv:2409.01754v4" has a version suffix that no other entry has.
  - Bao et al. (ICLR): "volume 2024, pages 24814–24836".
  - Askitas: "Listing: https://ideas.repec…".
  - No unresolved citations or `??`.

---

## 6. Consistency: paper vs AI_DISCLOSURE, preregistration and README

- **Plan deviation 9** says the pre-ChatGPT-data region is "RAID **GPT-4 and ChatGPT**". The paper says GPT-4 and
  **Llama-2-70B-chat**, with ChatGPT only as a sensitivity check. The plan also says "training data", where the
  paper says "pretraining".
- **Plan deviation 9** says "GPT-2 perplexity **to rule out** training-data contamination". The paper is
  softer, and the claim itself is doubtful (m5).
- **The plan's deviation log stops at round 2.** The paper's App. G(5b) lists the round-3 additions (quarterly
  series, seeds, ablation, Fast-DetectGPT, never-revised, 30-month grid, region drift placebos). The plan has
  none of them, although the README calls it the "full deviation log". The post-hoc peak-ρ statistic should be
  logged as exploratory there.
- **README** omits the `vpeak` (and `vmarkers`) jobs, and no run script runs `vpeak`.
- **AI_DISCLOSURE.md** matches the paper on roles, zero human edits and the pending spot-check. It does not
  match on "every reported result is inserted from results/" (M6).
- **Anonymity.** App. G says "the commit will be identified after review" ✓. The plan names commit hashes; that
  is fine if the repository is not linked during review.

---

## 7. Scores (ARR)

- **Soundness: 3.5.** The headline shift is robust and fully traceable. Every rendered number matches. The
  vintage analysis now has uncertainty. Points off for:
  - the dash-ablation bug;
  - the unreported null ρ(release, Δ);
  - overclaims about 2026 open models and *delve*;
  - no intervals on peak timing.
- **Excitement: 3.5.** "Which AI does writing sound like?" with peak timing ordered by vintage is fresh and
  theme-central. The strongest new evidence (ρ = 0.83) is exploratory and post hoc.
- **Overall: 3.5.** Strong Findings; borderline main conference. Fix M1–M6 before submission.
- **Confidence: 4.**

---

## 8. Remaining issues, ranked, each with an exact fix

**M1. The dash ablation does not remove dashes (code bug; Table 2 row mislabelled).**
Fix: in `code/analysis.py:901` change the line to
`mso.EXCLUDE = ("pun:\u2014", "pun:\u2013", "pun:-")`. Use escapes so the file encoding cannot break it again.
Add `assert any(n.startswith(mso.EXCLUDE) for n in ("pun:\u2014",))` and re-run `nodash` and `make_numbers`.
If there is no time, relabel the row "No hyphen features" and add a row "No punctuation features" =
`arxiv_ablation.punctuation.excess` (25.7). Also grep the repository for `â€`.

**M2. Unreported null for the requested statistic (forking paths).**
Fix: after the ρ = 0.83 sentence in §6.4, add:
"The rank correlation of release date with the 2025→2026 change, which we computed first, is
\R{arxiv_vintage_release_corr.rho_annual} on annual means and \R{arxiv_vintage_release_corr.rho_q4}
($p=\R{arxiv_vintage_release_corr.rho_q4_p}$) when measured from 2025Q4; peak timing was chosen after these."
Log the same in plan deviation 13. Replace the asymptotic p with a permutation p (10,000 shuffles).

**M3a. Abstract and Discussion overstate the 2026 open models.**
Fix, abstract: "…under the newest it peaked in 2026 (open models with logged decoding) or, for the 2026 model,
was still rising in 2026Q3."
Fix, Discussion: "under the newest it peaked in 2026 or was still rising".
Fix, §6.4 last sentence: "The three 2026 open models, run with logged decoding, peaked in 2025Q4–2026Q2, later
than all but gpt-oss among older generators, so the late peak does not rest on the uncontrolled generator; only
the 2026 model was still rising in 2026Q3."

**M3b. The *delve* sentence contradicts the data.**
Fix: replace "Once markers and style region come from the same model, the decline of *delve* mostly reflects
which models the markers come from." with "Mined markers fell in 2026 even for references released in 2025–26,
so the fall of lexical markers is general and does not track style overlap."

**M4. "cannot have learned … but not arXiv abstracts".**
Fix: "…reflects models whose pretraining data predate ChatGPT; their instruction tuning used 2023 data
(undisclosed for GPT-4 and Llama 2, ChatGPT conversations for Vicuna), so they are unlikely to have learned their
style from post-ChatGPT scientific writing."

**M5. Figures hide or contradict data.**
Fix, Fig. 1a: in `figures.py its_panel`, use `loc="upper left"` with no `bbox_to_anchor`. The region from 2015 to
2022 above 20% is empty.
Fix, Fig. 2b:
- add a legend for the release-year colours;
- use one palette across both panels (by release year) and drop the separate gpt-oss line in (a);
- offset overlapping points by ±0.03 in x;
- place Claude in a separate column labelled "release month n/a" at x = 2026.95 behind a vertical divider;
- change the label to "Spearman ρ = 0.83 (n = 18; 2026 model excluded)".

**M6. "Every result … inserted automatically" is false.**
Fix (preferred): emit the quarter lists, "12 of 14", "fell under all but", within-family flags and the
`rose` list from `vintage_summary`/`vintage_quarterly` as `\R` strings.
Fix (fallback): change the AI Use sentence and AI_DISCLOSURE.md to "Every number from our analyses is inserted
automatically; a few counts and lists of generator names are typed and were checked against `results/`."

**m1.** Discussion: change "including two whose style overlap kept rising" to "including gpt-oss, whose style
overlap kept rising".

**m2.** Conclusion: change "Overlap with each generator peaked later the more recent the generator" to
"Overlap with a generator tended to peak later the more recent the generator (ρ = 0.83)". In the abstract, add
"(the 2026 model, without a release month, excluded)" after "18 generators".

**m3.** §6.4: change "only Granite shows opposite signs" to "only Granite shows a clear rise against a fall".

**m4.** §6.5: change "whose mined words (…) are ordinary academic vocabulary" to "the 2026 model's mined words
(…) are ordinary academic vocabulary".

**m5.** Learners (App. D): Liang et al.'s TOEFL essays were collected from a public forum, so their originals may
predate 2019. Change "so that contrast does not come from memorised test essays" to "so the released collection
postdates GPT-2; memorisation of individual forum posts is unlikely but not excluded". Change plan deviation 9's
"to rule out" to "to reduce".

**m6.** Contribution (1): change "equals the human-side component of the Bayes error" to "equals the Bayes
classifier's false-positive rate".

**m7.** Add `vpeak` to `run_v5b.ps1` (after `vquarter`) and to the README job list.

**m8.** Drop LLM training texts that clean to fewer than 50 words, the same rule as for human abstracts; this
removes 42 RAID chat outputs. Anchor the inline-label rule to LLM text, or to `(^|\n)`.

**m9.** Fix the reference artefacts listed in §5. Use braces in the `.bib` titles to protect capitalisation.

**m10.** Limitations: change "single-generator regions rest on 150 texts each" to "150 texts each (450 for RAID
generators)". Mention that RAID single regions keep summary-register outputs (21–33% for ChatGPT, Cohere and
Mistral chat).

**m11.** Appendix F: move Table 4 into the section with `[h!]`, or add one sentence under the heading. In §6.1,
replace *we* with *is*/*are*, or say "(11th)".

**m12.** Plan: add deviation 13 for the round-3 additions, and correct deviation 9 (GPT-4 + Llama-2-70B-chat;
"pretraining").

**m13.** Report bootstrap intervals for the peak quarter by resampling documents within quarters with the
seed-0 instrument. At minimum, state that the argmax is unstable for flat-topped curves (Gemma 3, Granite 3.3).

**m14.** Rename "the 2026 model" to "Claude Opus 5.5 (Claude)" throughout, as asked in round 3. There are now
four 2026 models.

**[HUMAN]** These still need the human author: complete `lit/SPOT_CHECK.md`, do a full read-through, and make
`HUMAN-EDIT:` commits, as asked in round 3.
