# Round 1 → v2: what we change and why

Reviews: `round1_R1_methods.md` (S2/E3/O2), `round1_R2_nlp.md` (S2/E3/O2), `round1_AC_writing.md`.

## Data and measurement (re-run everything)
- [ ] **Sampler bug** (R1): v1 kept first 400 results per window → recent cs windows truncated to early-UTC submissions. v2 fetches all, samples 200/cell at random, records `updated`. Pre-period = v1 *and* last revision before 2022-11-30.
- [ ] **Encoding artefacts** (R1, R2): Unicode dashes 0% in human abstracts (LaTeX `--`). `features.delatex` maps `---`/`--` → em/en dash, `$…$` → X, strips commands. All caches rebuilt.
- [ ] **Math confound** (R2): report no-math subset (baseline by field + ITS).
- [ ] **Length confound** (R1, R2): length-reweighted series (pre-2022 length bins).
- [ ] **LLM-topic confound** (R1 found in our favour): series on abstracts not mentioning LLMs.
- [ ] **Generator dependence** (R1, R2, AC): table of yearly MSO + excess for generator sets: all / no-frontier / local only / local+frontier / RAID only. Claims limited to what holds across sets.
- [ ] **Parity across genres** (R2): Claude + Phi-4 + Granite for all three genres; Hansard compared with arXiv region built from the *same* generator set (local+frontier).
- [ ] **Drift placebo** (R1): region trained on 2015–2018 humans only, excess at 2021/22 vs 2015–2018 trend (out-of-sample placebo).
- [ ] **Grouped calibration** (R1) and Hansard LLM src→speaker group mapping (R1).
- [ ] **Learner SE** (R1): HC1 not HC3; add holistic score covariate (proficiency); drop/merge grade 12 (quasi-separated); perplexity-detector instrument on the same essays (Qwen2.5-0.5B log-ppl) to test the Liang-direction claim directly.
- [ ] arXiv threshold sensitivity (prereg deviation 3 said dropped).
- [ ] Equal field weights for "all" series (design-weighted).

## Claims and framing
- [ ] MSO = classify-and-count flag rate (cite Forman 2008); Bayes error = estimand only; drop "conservative", "uniform noise" straw man, "rising towards ½" / "zero only if separable" errors.
- [ ] H5 stated as **not supported (opposite direction)**; define H1–H5 in text or drop labels.
- [ ] Hansard = comparison genre, not a clean control; election-turnover caveat; 1998→2015 cut logged.
- [ ] Base vs chat: report all generators, held-out recall for chat, prompt/length confounds; "increases" not "makes"; no "humans hear".
- [ ] Markers: report 2025 excess and in-region ratio honestly.
- [ ] Self-test removed from paper (circular; out of genre) → AI-authorship companion piece.
- [ ] Frontier-model timing stated with commit evidence; results with and without.
- [ ] "pre-registered" → "analysis plan committed before results"; freeze plan; full deviation list.
- [ ] Disclosure paragraph rewritten (AC draft): who did what, Claude as drafter *and* data source; citation check stated only once done.
- [ ] Anonymity: no repository link in review version.
- [ ] Missing refs (verify each): Forman 2008, Khan et al. 2025, Askitas 2025, Shaib et al. 2024, Binoculars, Fast-DetectGPT, Herbold et al. 2023, Berber Sardinha 2024, Mizumoto 2026.
- [ ] Tables: instrument summary, generator-set sensitivity, LOMO appendix. Conclusion section. AC line edits.
- [ ] Hard-coded numbers → macros (159,102; prompt count 14 vs 15).
