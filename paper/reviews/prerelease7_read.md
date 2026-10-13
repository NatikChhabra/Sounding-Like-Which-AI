# Pre-release read 7 (fresh AC-level read)

Read from main.pdf (17 pp.). Figure pages (6, 8, 15, 17) were rendered and checked. Numbers were spot-checked against results/*.json|csv: the ablation csv, arxiv_vintage_peak.json, arxiv_vintage_peak_checks.csv, arxiv_vintage_release_corr.json and robustness_v6 in numbers.tex. The marker-vs-style peak counts (7/6/5), the 15-of-19 and 12-of-14 counts, "three of the four 2026 generators", the Table 5 signs, the nine-cutoff subset and the Fig. 2b point placement all check out. Items are ranked by how much a reviewer would care.

## (1) Claims stronger than the evidence

**1. Abstract: the vintage gap quoted is the one the paper calls an understatement.**
Abstract: "Against generators whose pretraining data predate ChatGPT, the gap is smaller (7.5 pp; 3.5 pp for the two we ran from titles)."
§6.4 says this region peaked in 2025 and fell to 11.9% in 2026, so "a straight post-ChatGPT line fitted through 2026 understates their June 2025 gap". Fitted only to June 2025, the gap is 13.1 pp (7.6 for the two local models), against 27.5 for the main region. The direction ("smaller") holds under either fit. The size of the contrast does not: 0.30 of the main gap versus 0.48.
Rewrite: "the gap is smaller (7.5–13.1 pp across post-trend fits; 3.5–7.6 pp for the two we ran from titles)."

**2. Discussion and Conclusion attribute late peaks to vintage alone; §6.4 says vintage and length cannot be separated.**
Discussion: "Overlap tended to peak later for more recent generators". Conclusion: "Single-generator overlap tended to peak later for more recent generators, so studies ... should report their reference models' vintage".
§6.4 and Limitations report that output length predicts the peak about as well (0.73). The partial correlation given length is 0.56 (n=18) and 0.37 (n=15, without the three post-hoc models), and the text concludes "vintage and length cannot be separated". The abstract and contribution (4) already say "(and longer-writing)". The two closing sections drop it.
Rewrite (Conclusion): "Single-generator overlap tended to peak later for newer, longer-writing generators, so studies of LLM influence on writing should report their reference models' vintage and output length." Make the same insertion in the Discussion's first sentence ("for more recent (and longer-writing) generators").

**3. §6.4 last sentence contradicts the Limitations.**
"Only the pre-ChatGPT-data region avoids the question of who learned from whom."
Limitations: "their instruction tuning used data from 2023". §6.4 notes that Vicuna was tuned on user-shared ChatGPT conversations. GPT-4-0613's post-training data are undocumented. So the region reduces the question but does not avoid it.
Rewrite: "Only the pre-ChatGPT-data region largely sidesteps the question of who learned from whom."

**4. Appendix H compares quantities in different units.**
"so any faster loss of stylistic spread is small next to the shift towards the LLM region."
Dispersion is a Euclidean distance in standardised feature space, and the shift is in percentage points of MSO. The comparison has no common scale.
Rewrite: "so any faster loss of stylistic spread is at most about three years' worth of the pre-ChatGPT decline." Relatedly, contribution (5) says dispersion "did not change beyond its trend once length is fixed". That is a null result, better put as "showed no change beyond its trend".

## (2) Internal contradictions

**5. When the three 2026 open models were added (§4 and §6.4 vs Appendix A).**
§4 and Appendix A (5) place them "after the second simulated review", "after the single-generator pattern of the other 16 generators had been seen". §6.4 says "added after the pattern was seen", which a reader takes to mean the peak-quarter pattern. But Appendix A (6) places the quarterly single-generator series, and hence the peak analysis, after the third review. The pattern seen can only have been the annual 2025-to-2026 changes. This does not change any number, but it affects how readers weigh "post hoc" in the abstract.
Fix: in §6.4 write "added after the annual single-generator changes had been seen". In Appendix A (5) write "the single-generator 2025-to-2026 changes".

No other contradictions were found. Text, Tables 1–5, Figures 1–4 and captions agree on every value checked.

## (3) Hard-to-follow points (minor)

6. §2: "our pre-ChatGPT slope, partly a field-mix effect" gives no number in the paper. The results have it: 0.5 pp/yr overall versus 0.3 pp/yr with equal field weights (robustness_v6.equal_fields.pre_slope_per_year). Add it in §6.2 after "rose by 0.5 pp per year".
7. Table 1 caption: release months for the RAID models are "approximated for the peak analysis", but the months used are never stated. The code dates them 2023.45 to 2023.85, with Cohere at about Nov 2023. Give the months, or the rule used, in the caption or Appendix E.
8. §5 Time series: "weighted least squares" does not say what the weights are (presumably documents per month).
9. §6.4: "a document bootstrap within quarters gives 0.64–0.86" does not state the interval level.
10. Layout, p. 15: the left column has a large blank block before the Appendix F heading, which sits at the bottom of the column, apart from its text. This is a float-placement artefact.

## (4) AI-slop phrasing

None material. A grep found no stock LLM phrasing and no em-dashes. The prose is plain and specific.

## ARR scores

- **Soundness: 3.5.** The main arXiv gap is well supported by placebos, drift instruments, ablations and generator-set variants. The vintage result is honestly labelled exploratory but stays confounded with output length.
- **Excitement: 3.** The point that "LLM style" depends on the reference models' vintage is useful and new for this literature. The findings are descriptive and partly post hoc.
- **Overall: 3.5.** A careful, transparent measurement paper that fits Findings, or the main track if the vintage-length confound is stated as plainly in the Discussion and Conclusion as in §6.4.
