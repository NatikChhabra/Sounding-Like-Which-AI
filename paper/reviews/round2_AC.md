# Round 2: Area Chair meta-review and editorial pass (revised submission)

**Submission:** "After the Delve Fades: Scientific Abstracts Keep Moving Toward LLM Style"
**Track:** ACL 2027 theme track, "Homogenization and knowledge collapse in LLMs" (long paper)
**Inputs read:** `paper/main.tex` (all 529 lines), `paper/main.pdf` (10 pp.; text extracted and pages 5-7 rendered), `paper/figures/*`, every file in `results/` that the paper cites, `code/analysis.py` (time series, placebo, dispersion, perplexity and embedding instruments), `preregistration.md`, `paper/AI_DISCLOSURE.md` (current version, commit 6e16675), `lit/SPOT_CHECK.md`, `lit/CITATIONS.md`, `lit/verification/batch1-5.md`, `README.md`, `CITATION.cff`, the git log, the three round-1 reviews and `RESPONSE_PLAN.md`.

Line numbers are `main.tex` source lines; "p." means PDF page.

**Caveat.** This review was written by an agent of the same model family (Claude Opus 5.5) that drafted the paper, generated the "2026 model" texts and wrote the round-1 reviews. Shared blind spots are likely. A human reader should do the final pass, and the human author should do the checks marked **[HUMAN]** below.

---

## 0. Verdict in brief

The revision is a large and mostly honest response. The verified round-1 defects are fixed: the sampler truncation, the dash/LaTeX encoding artefact, the HC3 standard error, the missing appendix, the seven-versus-five generator mismatch, the self-test, the reversed H5 and the Bayes-error errors. A drift placebo, generator-set sensitivity, length, math, topic and dash checks, a perplexity instrument on the same essays and a proficiency adjustment have been added. The headline survives every check. Soundness has moved from about 2 to about 3.

Three kinds of problem remain:

1. **The 2026 narrative does not match the authors' own numbers.** The text says the series levels off without the 2026 model. In fact the local-only region, which also lacks that model, keeps rising. What flattens 2026 is including RAID's 2023 models. The primary series itself plateaus at about 45% from late 2025, so the title's "Keep Moving" overstates.
2. **The record is not yet consistent.**
   - A human citation spot-check is claimed in the past tense, but `SPOT_CHECK.md` is unticked and a red TODO remains.
   - Three documents give three accounts of when the 2026 model was added.
   - The plan file is still "DRAFT" and still contains the "conservative estimate" claim that the paper now retracts.
3. **The time-series design is still largely untested.** None of R1's specification requests were done: no event study, no pre-trend sensitivity, no clustered or instrument-level uncertainty, only one drift origin and no multiplicity control. The Hansard comparison is reported selectively: its own placebos fail, and its gap is significant at threshold 0.6.

**Likely decision now: Findings** (overall about 3.0 with a 2.5-3.5 spread). Main conference is possible if the five changes in §6 are made.

---

## 1. Round-1 weaknesses: status

Status key:
- **Fixed**: the revision resolves the point.
- **Mostly**: the substance is fixed but minor parts are missing.
- **Partly**: some of the requested work was done, and important parts are missing.
- **Not**: the point was not addressed.

### 1a. Reviewer 1 (methods)

| # | Round-1 weakness | Status | Evidence in v2 | What is still missing |
|---|---|---|---|---|
| W1 | arXiv sampler truncated windows at 400 results (early-UTC bias in 2026) | **Mostly** | L161-163: all papers in each random window fetched, then 200 sampled at random; App. B(1) logs the replacement. N falls from 159,102 to 131,448. | No population-weighted series: "all" averages documents with roughly equal archive weights (`analysis.py` `monthly`, weight 1). State this estimand. No submission-hour check, but it is moot after the fix. |
| W2 | Frozen classifier under covariate drift; in-sample placebos uninformative | **Partly** | Drift placebo: 2015-18 instrument, break Jan 2019, evaluated June 2022, -0.5 pp (CI -1.9 to 0.9; Table 1). No-LLM-topic series 24.1 pp. Length-reweighted series 24.4 pp. | Only **one** origin, so there is no distribution of drift-only gaps to compare against. No author panel, no subfield-level topic check, no reweighting beyond length. The 41-month placebo horizon is good and should be stated. |
| W3 | "Human half of a Bayes error" and "population property" do not hold for the estimator | **Mostly** | §3 now says MSO is classify-and-count (Forman), that a finite classifier's flag rate "is neither an upper nor a lower bound", and that CIs exclude instrument variation (L150-154). The straw man and "remove exactly" are gone. | Contribution (1) (L65-66) still says the pre-ChatGPT value "estimates" the Bayes component. Instrument uncertainty is not propagated into any CI. The H1 field baseline is not length-standardised. |
| W4 | 2026 result depends on one generator added post hoc, run without controls | **Partly** | Generator-set table and Fig. 3; §6.5 L344-345 discloses that the model was added after a preliminary run; Limitations L450-451. | No API regeneration with logged decoding (still batches of 50 per session, `claude_prompts.py`). No frozen addendum. 2026 is not labelled exploratory. **The record is inconsistent:** App. B(4) says the 2026 model was "added after review", but git shows it was added at 15:37 on 12 Oct, two minutes after the preliminary arXiv results (f586d6c) and before v1 and round 1. `preregistration.md` deviation 5 still says "no analysis choice was changed afterwards". |
| W5 | Hansard is not a credible control | **Partly** | Now built from the same eight generators. Reframed as "comparison genre", "less exposed, not unexposed". 1998 to 2015 restriction logged (App. B(7)). | No common scale (logit, relative, or injection-calibrated). No speaker fixed effects. The **2022 election turnover** caveat promised in RESPONSE_PLAN is absent. HAC still uses row order over 92 non-contiguous months. **New:** Hansard's own placebos fail (§2, N6). |
| W6 | Encoding artefacts (Unicode vs LaTeX dashes, math) | **Fixed** | L194-201: delatex, math placeholder. No-dash instrument gives 26.2 pp. Dashes no longer among the arXiv top features (`arxiv_features_llm_typical.csv`: MTLD, DET_NOUN_VERB, comma, *that*...). | The PDF misrenders the explanation (N12). MTLD, now by far the strongest feature (coef 1.25), is not ablated. |
| W7 | ITS misspecified; CIs ignore clusters and instrument; placebo parameters unreported | **Not** | Unchanged specification (`segmented`: WLS, one linear post-slope, HAC 6). | No event study or flexible post-period. No quadratic or spline pre-trend. No window sensitivity. No cluster bootstrap. Table 1 gives only placebo excess and p, not level or slope. astro-ph still has a significant **negative** level shift (-3.5 pp, p<0.001; `arxiv_its.json`), a symptom R1 flagged. |
| W8a | Phi-4/Granite described but unused | **Fixed** | Both appear in all LOMO files and in Table 2. | App. B(4) should say they were described in v1 but used only from v2. |
| W8b | Grouped CV/calibration false for Hansard and in calibration | **Fixed (as stated)** | L213-215 | Not re-audited in code here. |
| W8c | Hard-coded numbers | **Mostly** | Results now come from macros. | "Every number in the paper is inserted automatically" (L477) is still literally false (1,500; 200; 150; 450; 250; 50 words; 6 lags; C=0.1). Say "every result". |
| W8d | Appendix A was a TODO | **Fixed** | Table 2 | Table 2 has no `\label` and is not referenced as a table; it floats above the Appendix A heading (p.10). |
| W8e | Latest-version abstracts dated by v1 | **Fixed, with a new issue** | L163-164: pre-ChatGPT papers revised after ChatGPT are excluded. | Introduces time-varying selection (N9). |
| W8f | Prompt count 15 vs 14 | **Fixed** | Macro gives 14. | |
| W8g | "arXiv" overstates: no physics archives | **Partly** | Archives listed at L160-161. | The title, abstract and Conclusion still say "scientific abstracts" / "arXiv abstracts" with no "non-physics" qualifier. |
| W8h | "Noun-heavy registers" claim contradicted | **Fixed** | Removed. | |
| W8i | Plan never frozen; deviations unlogged or out of order | **Partly** | App. B lists 7 deviations; "analysis plan ... committed to version control" (L80). | `preregistration.md` still says "DRAFT", still says "conservative estimate", still numbers deviations 1,2,3,4,6,7,5, and deviation 5 contradicts §6.5. "Pre-registered" is still used twice (L75, L378). Not logged: no arXiv embedding classifier, no H4 contrast test, equal-archive weighting, revision exclusion. |
| W9.1 | H5 reversal not stated | **Fixed** | §6.8 heading "(H5, not supported)"; Contribution (5). | |
| W9.2 | Rare events, quasi-separation | **Mostly** | 15/666 in region now. Grade bands merged in the perplexity model. "Lower in all 10 draws", p<0.05 in all 10 (`essay_seed_stability.json`). | No Firth or exact logit. Prompt-stratified contrast not shown. |
| W9.3 | HC3 SE numerically wrong | **Fixed** | Continuous CI is now -0.45 to -0.28 (`essay_ell_continuous.json`), which is plausible. | |
| W9.4 | Proficiency confound | **Fixed** | OR 0.82 (0.47-1.43) and margin -0.12 after adjusting for holistic score (L382-386). | |
| W9.5 | No perplexity detector on the same essays | **Fixed** | Qwen2.5-0.5B log-perplexity instrument on PERSUADE, plus replication on Liang's TOEFL and 8th-grade essays. | The instrument is not described in §5 (N11), and the abstract now overclaims (N10). |
| W9.6 | "Near chance" for TOEFL/college | **Fixed** | App. B(2) gives 35.2% / 8.0% / 51.4% and states that the region is genre-specific. | |
| W10 | Self-test circular | **Fixed** | Removed (App. B(3)). | |
| W11a | Base-vs-chat cherry-picked and in-sample | **Mostly** | All five base models reported (22.3-51.9%); held-out recall for chat models; prompt and length confound stated; "indicative". | RAID model identities (is "gpt3" text-davinci-00x? is "cohere" command?) still not verified or cited. |
| W11b | Marker narrative | **Mostly** | 5.9% vs 1.4% enrichment reported; both explanations given in Discussion (L422-426). | The 2025 marker gap is called "only 1.9 pp" without its CI (0.8-3.0) or the fact that it is about three times trend, just like MSO (§4 line edits). §6.4 still offers only author avoidance. |
| W11c | Multiplicity; H4 untested as a contrast | **Not** | | No Holm or BH. No primary/secondary hierarchy. No cs-minus-math contrast. From the reported SEs it would be about 27.1 pp (CI about 21.7-32.5), easy to add. |

### 1b. Reviewer 2 (detection / stylometry)

| # | Round-1 weakness | Status | Evidence | What is still missing |
|---|---|---|---|---|
| W1 | Trajectory and the marker-vs-MSO contrast are an artefact of the generator set | **Partly** | Five generator sets in Fig. 3 and Table 1. The abstract (L36-38) concedes that a RAID-only region "shows the shift receding". | The heading "Marker words recede; style overlap does not", the Conclusion and the title still present the divergence as a fact about writing, but under a 2023 region MSO retraces the marker curve, which was R2's point. §6.5 misdescribes which sets rise (N1). No updated marker list (frontier-mined, or Kobak's full method). |
| W2 | MSO is unadjusted classify-and-count; novelty vs FPR; implied α | **Partly** | Forman cited; "population property" qualified; straw man removed. | No mixture identity, so no implied α = (MSO − FPR)/(TPR − FPR) compared with Liang et al. 2024 for cs and math. This is the cheapest way to show what MSO adds beyond prevalence. No external validation of the baseline (Fig. 2 even shows it does not predict the shift). |
| W3 | Not topic-robust: length, LaTeX, encoding, MTLD | **Mostly** | Dash and LaTeX fixed; no-math series and baselines; length-reweighted series. | No feature-family ablation (only dashes). MTLD is the top feature in all genres and is not ablated. The field baselines (H1) are not length-adjusted, although R1 and R2 both showed a strong length gradient. |
| W4 | Hansard uses a different, weaker generator set and is not on a common scale | **Partly** | Same eight generators for Hansard, essays and the arXiv comparison region. | Still no commercial model other than Claude in Hansard or essays. No common scale. No arXiv-internal control. |
| W5 | Base vs chat in-sample and confounded | **Mostly** | See R1 W11a. Perception claim removed. | No matched decoding or length; no same-family checkpoint pairs. Acceptable now that it is labelled "indicative". |
| W6 | Learner result predetermined; H5 reversal; not compared with the claimed instrument | **Fixed** | See R1 W9. | New abstract overclaim (N10). |
| W7 | Frontier-model data uncontrolled; plan not frozen; record inconsistent | **Partly** | With/without reported; disclosure of dual role (L183, L473-474). | Same as R1 W4 and W8i. Still uses "pre-registered". |
| W8 | Factual inconsistencies; Appendix A TODO; Fig. 2 n | **Mostly** | Generator list, appendix and generalisation claim fixed. | Fig. 2 still shows no n per archive (econ n=976 pre-ChatGPT, which explains its wide interval). |
| W9 | Self-test overclaims | **Fixed** | Removed. | |
| W10 | Title and framing promise perception | **Fixed** | Retitled; L121-122 says no human judgements were collected. | The Discussion heading "What 'sounding like AI' measures" is fine. |
| W11 | Name and prior constructs (Khan, Askitas, Mizumoto, Chang) | **Partly** | Khan cited; Mizumoto removed after verification found the citation unsupported, which is acceptable. | **Askitas (2025) is still not cited**, although it is the closest econ-abstract study. Chang (2026) is still described only by its title (L91-92). The verification report offers a concrete description. "Overlap" vs a one-sided flag rate is not justified. |
| Refs | Missing references | **Mostly** | Forman, Khan, Shaib, Binoculars, Fast-DetectGPT, Chakraborty, Herbold, Berber Sardinha added. | Askitas is missing. |

### 1c. Area Chair (round 1)

| # | Round-1 issue | Status | Evidence / remaining |
|---|---|---|---|
| 1 | Visible TODO appendix | **Fixed**, but a **new red TODO** sits in the AI Use section (L477; p.8 top). |
| 2 | Text vs results facts (generators, June 2025 month, generalisation, 2026 trend) | **Mostly.** The June 2025 rationale is now honest (L221-223). "Kept rising" in 2026 is again too strong: the monthly series has been flat at about 42-49% since October 2025 (`arxiv_monthly.csv`; Oct-Dec 2025 mean 43.8%, Jan-Sep 2026 mean 45.0%). |
| 3 | Generator set changed after seeing results; inconsistent record | **Partly.** Disclosed in §6.5 but contradicted by App. B(4) and plan deviations 5 and 7 (see R1 W4). |
| 4 | Dash typography as hidden marker | **Fixed.** |
| 5 | "Population property"; Bayes-paragraph errors | **Fixed** in §3 (errors corrected). Contribution (1) wording is still slightly strong. |
| 6 | Confounds for the post-2022 rise | **Partly.** Topic, length and math checks added; composition is in Limitations. No within-cs subfield check, no author-composition check. |
| 7 | Overclaims (perception, "makes", "least", self-test) | **Fixed**, but new overclaims were added (N2, N6, N10, §4 edits). |
| 8 | H5 reversal and undefined H1-H5 | **Fixed** (L78-81). |
| 9 | Theme fit asserted, not shown | **Partly.** A dispersion analysis was added (§6.7), but it has no uncertainty, no test and no figure, and is plausibly a length artefact (N8). It finds no acceleration, which is honest but leaves the homogenization link thin. |
| 10 | Citations unverified | **Partly.** Five AI verification batches were run and applied: 11 rewordings, 1 removal, 20 published versions (commit 17601b9). The human spot-check has **not** happened (`SPOT_CHECK.md`: 0 of 5 ticked; `CITATIONS.md`: 0 of 52 ticked), yet it is claimed (§5). |
| Fmt: length | Fine. Main text ends on p.7 (Conclusion, line 521), about 6.6 pages. |
| Fmt: Conclusion | Added. |
| Fmt: anonymity | Repository link removed. "The human author" (singular) still discloses team size; use "author(s)". |
| Fmt: references | **Mostly.** Most venues updated. Remaining problems are listed in §4.6. |
| Fig. 1 | **Mostly.** Different y-scales noted; the ChatGPT label and tick rotation are fixed; "centred 6-month mean" in the legend. The legend in (a) overlaps the dashed trend line. Hansard raw monthly points (n=150) are still shown without a band. |
| Fig. 2 | **Mostly.** Units unified; caption gives the takeaway. n per archive still missing. |
| Fig. 3/4 (old learner fig.) | **Mostly.** "Lines" caption is fixed; legend is outside the plot. n and in-region counts (15/666 ELL) are still missing. |
| Missing feature table | **Not.** There is still no table of top LLM-typical and human-typical features, although there is about 1.3 pages of space. |
| Policy: RQ attribution, dual role, model version | **Fixed** (L469-474). |
| Policy: "verified citations" claim | **Partly**: see item 10. |
| Policy: concrete human decisions | **Fixed** ("approved the analysis plan and its deviations"), but it cannot be verified (no human commits). |
| Policy: "take full responsibility" | **Not.** The accountability sentence proposed in round 1 is missing from the paper; `AI_DISCLOSURE.md` has it. |

---

## 2. New problems introduced by the revision (most serious first)

**N1. The generator-set paragraph contradicts its own figure.**
L341-342: "Without the 2026 model the series levels off (38.1% to 37.2%)." That set is all-but-2026 (13 generators: 7 local plus 6 RAID). The **local-only** set (7 open models, also without the 2026 model) rises from 42.4% in 2025 to **48.3%** in 2026 (`arxiv_gensets.csv`; green line in Fig. 3), and has the *largest* trend gap after local+2026 (29.1 pp).

What the data show is this: any region that includes RAID's 2023 models flattens or reverses in 2026, and any region built from 2024-2026 models rises, with or without Claude. That is a stronger result, because it does not hinge on the uncontrolled Claude data. But the abstract ("regions that include current models"), §6.5, the Limitations ("adding one model changed the 2026 trajectory") and Fig. 3's caption all need rewriting to say it.

**N2. "Keep Moving" and "kept rising" overstate 2026.**
- Yearly 2025 to 2026 is 40.6% to 45.0%, but that rise mostly reflects growth within 2025. The monthly series has been flat since October 2025 (43.8% vs 45.0%), and Fig. 1a's 6-month mean visibly flattens.
- Under the RAID region it falls.
- Write "stayed near 45% in 2026" and reconsider the title verb (for example "Moved", or "Kept Moving ... Through 2025").

**N3. Three inconsistent accounts of when the 2026 model was added.**
- §6.5 L344: "after a preliminary run without it".
- App. B(4) L523-524: "Added after review: ... Phi-4, Granite and the 2026 model". This is false for the 2026 model, which is in v1 (commits c11d3ce and 01ef90f, before the round-1 reviews).
- `preregistration.md` deviation 7: "before the final run", and deviation 5: "no analysis choice was changed afterwards".

Git supports §6.5. Fix App. B and the plan file. Given the AI-authorship disclosure, a reviewer who finds this will discount the rest of the record.

**N4. The human citation spot-check is claimed but has not been done.**
- The paper (L476-477) says "the human author then checked a random sample of five citations" and then shows `[TODO: confirm after the author's spot-check]` in red on p.8.
- `AI_DISCLOSURE.md` says "Checked a random sample of five citations".
- `lit/SPOT_CHECK.md` has all five boxes unticked and is addressed to the author ("Tell Claude if anything looks wrong").

This is the same problem as round-1 policy item 2. **[HUMAN]** Do the check, record it in a `HUMAN-EDIT:` commit, then remove the TODO. Otherwise change both documents to "has not yet".

**N5. "Every citation was checked against its source" (L475) overstates the AI verification.** The batch reports say that ScienceDirect, ACM DL and Springer pages returned 403 errors. Several sources were checked only through Crossref metadata, institutional mirrors, search-index copies (Chang 2026) or secondary sources (Forman 2008, which is paywalled). Say "against its abstract or full text where accessible (N sources only via metadata or mirrors)" and give the counts: 11 rewordings, 1 removal, 20 published versions.

**N6. The Hansard null is reported selectively.**
- Hansard's own placebo breaks give **significant negative** gaps: -2.5 pp (p=0.010) at 2019-11 and -2.8 pp (p<0.001) at 2020-11 (`hansard_its.json`). That points to a poorly fitting linear model, yet only the arXiv placebos are shown.
- At threshold 0.6 the Hansard gap is **significant**: 1.8 pp (CI 0.3-3.2).
- Hansard marker words also rose significantly: 1.6 pp (CI 0.4-2.8).
- Relative to its 5.4% baseline, the primary 1.7 pp gap is about +30%, and Fig. 1b visibly shifts upward after 2022.

"Did not move measurably" (L35, L284-285) and "held still" (L446) overstate. Report the placebo and threshold results and use "changed little / not significant at the primary threshold".

**N7. The arXiv-minus-Hansard difference uses an unstated region.** "Exceeds the Hansard gap by 30.6 pp" uses the arXiv gap under the local+2026 region (32.3 pp), not the headline 25.7 pp. A reader who subtracts 25.7 − 1.7 gets 24.0 and suspects an error. Say so, and add the local+2026 row to Table 1. The comparison is still across instruments with different baselines (11-12% vs 5.4%). Add a relative or logit version, as both reviewers asked.

**N8. The dispersion result (the paper's only explicit homogenization measure) is not yet interpretable.** Problems:
- *No uncertainty and no test.* "Did not visibly accelerate" is an eyeball judgement.
- *Length confound.* Median abstract length rose from 149 to 176 words. Per-token rate features become less noisy as documents get longer, so dispersion would fall mechanically even with no change in style.
- *Distance metric.* Euclidean distance over hundreds of standardised, mostly sparse POS-trigram features is dominated by noise features.
- *Missing robustness checks.* There is no figure, and no check within archives or for fixed length.

Fixes:
- Compute dispersion on texts truncated to a fixed length (for example 120 words), or within length bins and within archives.
- Bootstrap CIs.
- Fit the same ITS model to the dispersion series.
- Add a small figure, or a column in Table 1.

Until then, "Movement toward LLM style, not loss of variety, is what changed sharply" (L374) is too strong for the theme-track's key claim.

**N9. The revision exclusion creates time-varying selection.** Excluding pre-ChatGPT papers whose latest version postdates ChatGPT removes more 2021-22 papers than 2015-16 papers, because revisions cluster soon after submission. The late pre-period is therefore a more selected sample (papers never revised), which can bias the pre-trend slope that the trend gap extrapolates. Post-ChatGPT papers, by contrast, are kept whatever their latest revision date and are dated by v1, so a 2023 paper revised in 2025 counts as 2023. Report the exclusion rate by year and show that the gap is stable if the exclusion is dropped (using v1 date with the latest text, as in v1).

**N10. New abstract overclaim on detector bias.** L40-41: "detector bias depends on the population, not on non-native authorship". The evidence is:
- one 0.5B scoring model with a threshold calibrated on PERSUADE;
- 91 TOEFL vs 88 8th-grade essays that differ in genre, prompt, age and length;
- an unmeasured mechanism ("whose essays contain more errors", L401: no error measure is reported).

The PERSUADE perplexity odds ratio (0.46) is adjusted for prompt and grade but **not** for proficiency, unlike the style result. Scope the claim to "in these data, a perplexity instrument penalises predictable writing, which test-takers produce and these school learners do not". Do not put it in the abstract as a general law.

**N11. Two instruments appear only in Results.**
- The sentence-embedding classifier (all-MiniLM-L6-v2 with calibrated logistic regression) is not described in §5.
- The perplexity instrument (Qwen2.5-0.5B mean token NLL with a one-feature isotonic classifier trained on the same human-vs-LLM essays) is not described in §5.

Add 2-3 sentences to §5: model, training data, calibration, threshold, and the held-out AUC (`essay_embedding_auc.json`).

**N12. PDF rendering bugs.**
- (a) L160: `\R{corpus_stats.arxiv_n_fields}` prints "**8.00** archives" (p.3).
- (b) L198-199: `\texttt{--}` and `\texttt{---}` are typeset as an en dash and an em dash, so the sentence reads "LaTeX dashes (–, —) become typographic en and em dashes" and "human arXiv abstracts write dashes as –" (p.3-4). The key methodological fix is unreadable. Use `\texttt{-{}-}` and `\texttt{-{}-{}-}`, or `\verb|--|`.

**N13. The headline estimand is an equal-archive average, which the paper does not state.** The "all" series averages documents, and each archive-month contributes up to 200, so the eight archives get roughly equal weight. "arXiv MSO was 45.0% in 2026" is therefore not the arXiv-population share; cs is a much larger share of submissions, and its gap is 37.4 pp. State the estimand in §4. Ideally add a submission-volume-weighted series, which R1 requested.

**N14.** Contribution (2) (L67) says "14 reference generators" for "three genres". Hansard and essays use 8 (`corpus_stats.json`).

**N15.** L245: "older generators are still recognised (59.5-94.9%)". The held-out set includes 2025 models: gpt-oss 65.3% and Qwen3 76.0%. Use "the other generators".

**N16. Table 1.** The "95% CI" column holds p-values for the placebos. "Mid-2022" should be "June 2022". The drift placebo's break date (January 2019) and 41-month horizon are not stated. Add the local+2026 row (N7).

**N17. Licence statement.**
- The Liang 8th-grade essays come from the authors' GitHub repository, which has no LICENSE file (verification batch4). They derive from the Hewlett ASAP Kaggle data, which has its own terms, but the Ethics statement lists everything under "MIT".
- The PERSUADE ShareAlike terms (CC BY-NC-SA 4.0) also apply to any derived data you release.

**N18. The 2026 model's revision outputs are almost indistinguishable from human text.** Its P2 AUC is 0.67 (`arxiv_separability.csv`; Qwen3 P2 is 0.70). Each generator has equal weight, so near-human texts pull the boundary toward human abstracts and raise MSO for everyone, which helps explain why local+2026 gives the highest 2026 value (57.6%). One sentence in §6.5 should say this.

**N19. Classifier-family agreement is reported only where it is good.** κ is 0.65 for arXiv but **0.27 for Hansard and 0.30 for essays** (`*_instrument.json`). Hansard MSO is 5.9% under logistic regression vs 4.4% under GBM. L436-440 should report all three: that strengthens, not weakens, the "do not judge individuals" point.

**N20. Promised changes that were not made.** RESPONSE_PLAN items not reflected in the paper:
- the election-turnover caveat;
- replacing "pre-registered";
- "freeze plan";
- the instrument-summary table;
- the Askitas citation.

---

## 3. Writing: line-level edits

Format: **L# (section)**, then the original in quotes, then → the fix, with the reason in brackets where it is not obvious.

### 3.1 Title and abstract

- **Title (L18)**
  - Original: "Scientific Abstracts Keep Moving Toward LLM Style"
  - Fix: "Scientific Abstracts Moved Toward LLM Style", or "...Kept Moving Toward LLM Style Through 2025".
  - Why: N2. "Scientific" also overstates eight non-physics arXiv archives. Consider "arXiv Abstracts".
- **L28-30**
  - Original: "places at least as close to LLM output as to pre-ChatGPT human writing"
  - Fix: "judges at least as likely to come from LLM output as from pre-ChatGPT human writing".
  - Why: "close" suggests a distance, but the rule is a likelihood ratio of at least one.
- **L30**
  - Original: "In 131,448 arXiv abstracts (2015–2026)"
  - Fix: "In 131,448 abstracts from eight non-physics arXiv archives (2015–2026)".
- **L33**
  - Original: "reached 45.0% in 2026"
  - Fix: "reached 45.0% in January–September 2026".
- **L35-36**
  - Original: "Australian parliamentary speech did not move measurably"
  - Fix: "the gap in Australian parliamentary speech was small (1.7 pp) and not significant".
  - Why: N6.
- **L37-38**
  - Original: "a region built only from 2023 models shows the shift receding in 2026, whereas regions that include current models show it continuing"
  - Fix: "regions that include 2023 models show it flattening or receding in 2026, whereas regions built from 2024–2026 models, with or without the 2026 model, show it continuing".
  - Why: N1.
- **L39**
  - Original: "Marker-word counts therefore understate how far"
  - Fix: "Marker-word counts may therefore understate how far".
- **L40-41**
  - Original: "a perplexity-based detector reproduces a published bias against TOEFL essays yet flags US school learners less than their peers: detector bias depends on the population, not on non-native authorship."
  - Fix: "a perplexity-based instrument reproduces a published bias against TOEFL essays yet flags US school learners less often than their peers, so which writers such a detector penalises depends on the population."
  - Why: N10.

### 3.2 Introduction

- **L52-53**
  - Original: "No existing measure says how much writing falls on the machine side of that boundary, in which genres, or since when."
  - Fix: "Prevalence estimates do not say how much writing, whoever wrote it, falls on the machine side of that boundary, in which genres, or since when; detector 'AI-likeness' scores \citep{khan2025} and style indices \citep{bentley2026} come closest."
  - Why: overclaim, given Khan, Bentley, Chang and Askitas.
- **L65-66**
  - Original: "a classify-and-count quantity \citep{forman2008} whose pre-ChatGPT value estimates the human-side component of a Bayes error"
  - Fix: "a classify-and-count quantity \citep{forman2008} which, for an optimal classifier, equals the human-side component of the Bayes error before ChatGPT; we estimate it with calibrated classifiers and report how the estimate varies across them".
  - Why: consistency with L150-152.
- **L67**
  - Original: "with content-word-free features and 14 reference generators"
  - Fix: "with content-word-free features and eight reference generators per genre (14 for abstracts)".
  - Why: N14.
- **L70-71**
  - Original: "and no measurable change in parliamentary speech"
  - Fix: "and a small, non-significant gap in parliamentary speech".
- **L75 and L378**
  - Originals: "contrary to our pre-registered hypothesis" and "We pre-registered that"
  - Fixes: "contrary to the hypothesis in our analysis plan" and "Our analysis plan predicted that".
  - Why: the plan was never frozen externally; the RESPONSE_PLAN promised this change.
- **L80**
  - Original: "was committed to version control before any result was computed"
  - Fix: add "(Appendix B gives the commit date)".
  - Why: verifiability. A hash is anonymity-safe.

### 3.3 Related work

- **L91-92**
  - Original: "\citet{chang2026} analyse a decade of convergence between human writing and machine patterns"
  - Fix: "\citet{chang2026} show that PubMed, Wikipedia and Stack Exchange text became more predictable to small language models over 2014–2024". Then add one sentence contrasting this with MSO and with your own pre-ChatGPT slope (0.4 pp/yr) and dispersion decline.
  - Why: this restates the title (round-1 R2 and AC, and verification batch1). Confirm the "predates generative AI" point in the full text before using it.
- **After L92**
  - Fix: add Askitas (2025, IZA DP 18062), the closest prior arXiv/econ stylometric event study.
- **L93**
  - Original: "a distributional overlap whose pre-ChatGPT level is itself of interest"
  - Fix: "a thresholded overlap (the flag rate of a calibrated classifier) whose pre-ChatGPT level is itself of interest".
  - Why: R2 W11.
- **L108**
  - Original: "genre shapes stylistic features more strongly than source does"
  - Fix: "texts cluster by genre more than by source".
  - Why: verification batch5 found that the source shows clustering, not variance shares.

### 3.4 Sections 3-5

- **L152 ("instrument-dependent") and L154 ("this instrument variation")**
  - Problem: "instrument" is used here but defined only at L215.
  - Fix: move the definition sentence to §3 or write "classifier-dependent" here.
- **L160**
  - Original: "For each of \R{corpus_stats.arxiv_n_fields} archives"
  - Fix: "For each of eight non-physics archives", or fix the macro format.
  - Why: prints "8.00" (N12a).
- **L163**
  - Original: "so every archive-month has the same design weight"
  - Fix: "so archive-months with at least 200 papers carry equal weight; the overall series therefore weights the eight archives about equally, not by submission volume".
  - Why: N13.
- **L163-164**: add the share of pre-ChatGPT papers excluded, by year (N9).
- **L181-182**
  - Original: "through sub-agent sessions without control over decoding"
  - Fix: add "(50 prompts per session)".
  - Why: R1 W4 and R2 W7 asked for this; it matters for within-batch dependence.
- **L198-199**: replace `\texttt{--}` and `\texttt{---}` with `\texttt{-{}-}` and `\texttt{-{}-{}-}` in both places (N12b).
- **After L215**: add the embedding and perplexity instrument descriptions (N11).
- **L221-223**
  - Original: "(Hansard has no sittings from April to June 2025, which the model interpolates)"
  - Fix: "(Hansard has no sittings from April to June 2025; its gap is read off the fitted line, which uses the February, March and July 2025 sittings)".
- **L223**
  - Original: "Placebo breaks are placed at November 2019 and November 2020."
  - Fix: add "with gaps evaluated in June 2022".
- **L224**
  - Original: "tests for a gap in mid-2022 over the 2015–2018 trend"
  - Fix: "tests for a gap in June 2022 over a 2015–2018 trend with a break at January 2019 (a 41-month horizon, longer than the 30 months of the main analysis)".

### 3.5 Results

- **L245**
  - Original: "older generators are still recognised"
  - Fix: "the other generators are mostly recognised (from 59.5% for Cohere-chat to 94.9% for GPT-4)".
  - Why: N15.
- **L249**
  - Original: "At least one current model writes outside the region defined by its predecessors."
  - Fix: "The 2026 model writes largely outside the region defined by the other 13 generators."
  - Why: plainer, and it does not imply a general law.
- **L253-254**
  - Original: "as did 5.4% of speeches and 4.1% of student essays"
  - Fix: add CIs: "(4.9–6.0)" and "(3.7–4.6)".
  - Why: requested in round 1.
- **L255**
  - Original: "$\chi^2$ $p<0.001$"
  - Fix: "$\chi^2(7)=369$, $p<0.001$".
- **L259-260**
  - Original: "so it is not an artefact of notation"
  - Fix: add "Length, which also differs by archive, is not adjusted here".
  - Why: R1 W3 and R2 W3 both showed a length gradient.
- **L276**
  - Original: "45.0% in 2023–2026"
  - Fix: "45.0% (January–September) in 2023–2026".
- **L278**
  - Original: "Table~\ref{tab:robust} shows it under every check we ran"
  - Fix: "Across the robustness variants in Table~\ref{tab:robust} the gap stays between 23.7 and 29.5 pp".
  - Why: "every check we ran" invites the reply that some checks were not run.
- **L284-285**
  - Original: "Parliamentary speech did not move measurably (1.7 pp, CI −0.6 to 4.0)."
  - Fix: "The Hansard gap is small and not significant at the primary threshold (1.7 pp, CI −0.6 to 4.0), but it is significant at threshold 0.6 (1.8 pp, CI 0.3–3.2), and Hansard's own placebo breaks give significant negative gaps (−2.5 and −2.8 pp), so its linear trend fits less well."
  - Why: N6.
- **L285-287**
  - Original: "With both regions built from the same eight generators, the arXiv gap exceeds the Hansard gap by 30.6 pp"
  - Fix: "With the arXiv region rebuilt from the eight generators used for Hansard (arXiv gap 32.3 pp), the arXiv gap exceeds the Hansard gap by 30.6 pp (CI 27.9–33.3); relative to each genre's pre-ChatGPT level the gaps are about 2.7 and 0.3 times baseline."
  - Why: N7. The relative figures come from the macros; compute them in code.
- **L288-291**: add the H4 contrast: "cs exceeds mathematics by 27.1 pp (CI 21.7–32.5)". Compute this in code from the fits, not from these rounded SEs.
- **L326-328**
  - Original: "its June 2025 trend gap only 1.9 pp, consistent with authors avoiding publicised markers"
  - Fix: "its June 2025 trend gap was 1.9 pp (CI 0.8–3.0). In relative terms that is about three times the extrapolated trend, as for MSO, so the two series diverge only in 2026, when the marker share fell to 1.5% while MSO stayed near 45%. Authors avoiding publicised markers \citep{geng2025} and newer models no longer producing them both fit this."
  - Why: "only" is misleading on a 1% base. Both 2025 yearly values are roughly three times their extrapolated trends.
- **L323 (heading)**
  - Original: "Marker words recede; style overlap does not"
  - Fix: "Marker words recede; style overlap measured against recent models does not".
- **L337-345: rewrite the core of §6.5.** Suggested text:
  > All five regions show the rise from 2022 to 2025 and a positive trend gap (Table 1). They diverge in 2026. Regions that include RAID's 2023 models flatten or fall (RAID only: 17.2% to 10.9%; all except the 2026 model: 38.1% to 37.2%). Regions built from 2024–2026 models keep rising, with or without the 2026 model (local open models: 42.4% to 48.3%; local plus the 2026 model: 46.5% to 57.6%). The 2026 model's revisions of human drafts are hard to separate from human text (AUC 0.67), which raises MSO under every region that includes it. This pattern is consistent with abstracts moving away from 2023-era LLM style toward the style of later models. A measure built only on 2023 models would have shown the shift receding in 2026. We added the 2026 model after a preliminary run without it; both versions are reported.
- **L356-357**
  - Original: "(GPT-2, GPT-3, and base Cohere, Mistral and MPT)"
  - Fix: give the RAID model IDs and cite RAID's model table; say whether "GPT-3" and "Cohere" are instruction-tuned API models.
  - Why: R1 W11a.
- **L370-374**: add "Euclidean, in the feature space standardised on pre-ChatGPT abstracts", CIs, a test, and a length control. Replace "Movement toward LLM style, not loss of variety, is what changed sharply." with "Within the precision of this measure, the post-ChatGPT change is a shift toward the LLM region rather than a faster loss of spread." (N8)
- **L382**
  - Original: "lower in all 10 training draws"
  - Fix: "lower, and significant at p<0.05, in all 10 training draws".
  - Why: this is now true and worth saying, because round 1 had 3/10.
- **L391-392**
  - Original: "odds ratio 0.46"
  - Fix: "odds ratio 0.46, adjusted for prompt and grade but not proficiency".
- **L399-402**
  - Original: "what it penalises is predictable, formulaic text, which test-takers produce and school learners, whose essays contain more errors, do not. Detector bias depends on the population, not on non-native authorship as such."
  - Fix: "what it penalises is predictable text: the TOEFL essays are highly predictable and these school learners' essays are not. In these data, which learners a perplexity detector flags depends on the population rather than on non-native status alone."
  - Why: no error measure is reported. N10.

### 3.6 Discussion, Conclusion

- **L417-418**
  - Original: "so at least part of the change is in the writing itself"
  - Fix: "and the drift placebo shows no comparable gap from instrument ageing, so at least part of the change is in the documents".
  - Why: Hansard alone cannot show this. The drift placebo is the better evidence.
- **L422**
  - Original: "Marker words are what readers notice and what authors can edit out."
  - Fix: "Marker words are easy to spot and easy to edit out."
  - Why: no perception data.
- **L425-426**
  - Original: "the region of 2023-era LLM style is emptying while the region of current models is filling"
  - Fix: "MSO measured against 2023 models fell in 2026, while MSO measured against 2024–2026 models rose".
  - Why: the original is a metaphor and reads as AI-written.
- **L436-440**: add Hansard and essay agreement: "κ = 0.65 for abstracts, 0.27 for speech and 0.30 for essays". (N19)
- **L445-446**
  - Original: "while marker words came and went and parliamentary speech held still"
  - Fix: "while marker words came and went and parliamentary speech changed little".
- **L446-447**
  - Original: "Measuring that shift requires reference generators as current as the writing being measured."
  - Fix: "Our generator-set results suggest that such measurements need reference generators about as recent as the writing they measure."

### 3.7 Limitations (L449-460): additions

1. Only one 2026-era generator (with uncontrolled decoding, batched 50 per session), and the 2026 values depend on whether 2023 models are in the region.
2. The overall arXiv series is an equal-archive average of eight non-physics archives, not the arXiv population (N13).
3. Confidence intervals exclude instrument variation and the field-month cluster design.
4. Hansard's linear trend fails its own placebo tests.
5. The 2022 change of government changed the speaker population six months before ChatGPT.
6. The dispersion measure is sensitive to document length.
7. Learner analysis: the perplexity instrument uses one small language model and a threshold calibrated on PERSUADE.
8. Excluding papers revised after ChatGPT changes the pre-period sample over time (N9).

Also update "rests on 15 in-region learner essays" if the counts change.

### 3.8 Appendix B (deviations)

- **(4)**: split it.
  - "Added after the preliminary arXiv run, before the first review: the 2026 model."
  - "Described in v1 but first used after review: Phi-4 and Granite."
  - "Added after review: ..." (the rest).
- **Add new items**:
  - equal-archive weighting of the overall series;
  - exclusion of pre-ChatGPT papers revised after ChatGPT;
  - the plan's arXiv embedding classifier was not run;
  - H4 is not tested as a formal contrast (or add the test);
  - the plan's claim that a weaker classifier gives a conservative estimate is withdrawn (§3);
  - the plan was never frozen on Zenodo.
- **Table 2**: add `\label{tab:lomo}` and cite it as Table~\ref{tab:lomo} at L246.

### 3.9 Terminology consistency

| Term | Defined | Status | Fix |
|---|---|---|---|
| pre-ChatGPT | L128-129 (before 30 Nov 2022) | Consistent in text, figures (Fig. 1 legend, Fig. 2 axis) and Table 1. "pre-period" (L142) and "pre-LLM years" (L87, describing Kobak) are acceptable. | None |
| trend gap | L220-221 | Consistent (Table 1, Fig. 2 axis, §6.4). No stray "excess" in the text. | Its evaluation month for placebos (June 2022) should be stated where it is used. |
| instrument | L215 | Used before definition (L152, L154). Applied loosely to the embedding and perplexity classifiers (acceptable if §5 describes them). | Move the definition to §3. |
| MSO | L28, §3 | Small caps in text, "MSO" in figures; harmless. "Region"/"LLM region" is never formally defined. | One clause in §3: "the LLM region, {x: η̂(x) ≥ ½}". |
| archive / field | L160 says "archives"; §6.2 onward says "fields" and "field gradient" | Mixed | "archive (field)" once, then one term. |
| 2026 model / frontier model / Claude Opus 5.5 / current models | | "Current models" (abstract L38, L249) is ambiguous: does it mean Claude only, or 2024-2026 models? | Use "the 2026 model" for Claude and "2024–2026 models" for the set. |
| pre-registered / analysis plan | | Both used (L75, L378 vs L78-80, App. B) | "Analysis plan" throughout. |

### 3.10 Captions, figures, tables, references

**Captions and figures**
- **Fig. 1:**
  - The legend in (a) overlaps the dashed trend line; move it to the upper left of the pre-period.
  - Add a binomial band or drop the raw Hansard monthly points.
  - The caption could state the takeaway: "(a) rises far above trend; (b) shows a small, non-significant gap; (c) peaks in 2024".
- **Fig. 2:**
  - Add n per archive. Econ has 976 pre-ChatGPT documents and 139 months.
- **Fig. 3:**
  - The caption has no takeaway. Suggested: "Regions including 2023 models flatten in 2026; regions built from 2024–2026 models keep rising."
  - The legend calls the local models "2024-25 open models", but Mistral 7B is a 2023 release. Say "seven open models (2023–25)" or give the versions.
  - The 2024 and 2026 ticks crowd each other.
- **Fig. 4:** add n and in-region counts (ELL 15/666) to the caption.
- **Table 1:** CI column header (N16); add the local+2026 row; consider a "relative to trend" column.

**Feature table.** A top-features table is still missing. Use 10 LLM-typical and 10 human-typical features for arXiv, for example MTLD, DET_NOUN_VERB and comma against conj, amod, *by*, sentence length and *we*. Reviewers of a stylometric construct expect it, and there is room.

**References**
- "All thats human is not gold" has lost its apostrophe; use `That{'}s`.
- Katz & Alexander 2023 "19982022" has lost its en dash.
- Katz & Alexander 2025 has no venue or URL.
- Lowercase after "?" or ":" in Gerstgrasser ("breaking"), Juzek ("exploring"), Khan ("adoption"), Reinhart ("variation") and Sun ("quantifying"); "vocd-d" should be "vocd-D". Protect capitals with braces.
- Inconsistent capitalisation from BibTeX: "AI-Generated", "Machine-Generated text", "Zero-Shot", "LLM-Generated news text".
- Still listed as arXiv preprints: Liang et al. 2024b (COLM 2024) and Gerstgrasser et al. 2024 (COLM 2024 per verification batch2; confirm on OpenReview). Sadasivan et al. may now be in TMLR (batch5); check.
- Doshi & Hauser lacks an article number.
- Key `yakura2024` now has year 2026. That is harmless but confusing in `.bib` review.

### 3.11 Page limit, Limitations, anonymity, TODOs

- **Page limit:** main text ends on p.7 at L521, about 6.6 of 8 pages. Limitations, Ethics, AI Use, References and Appendix follow, which is compliant. There is about 1.3 pages of room for the feature table, H4 contrast, implied α, a dispersion panel and the Hansard placebo row. The "AI Use and Authorship" section is placed with Limitations and Ethics. If a strict PC counted it as main text, it would still fit. Merging it into the Ethics Statement is the safest option.
- **Limitations:** present and placed correctly; incomplete (§3.7).
- **Anonymity:**
  - PDF metadata is clean (author field empty; "Anonymous ACL submission").
  - There is no repository link. "Released with the code and data" is acceptable.
  - Risks: "the human author" (singular) on L470 and L476 → "the human author(s)".
  - Any supplementary code or data must strip `CITATION.cff` (name, ORCID, GitHub URL), `LICENSE`, `README.md`, git author fields ("NatikChhabra") and `Co-Authored-By` trailers. Use an anonymised archive, not the git history.
- **Remaining red TODOs:**
  1. L477 `\TODO{confirm after the author's spot-check}` (prints at the top of p.8). This is the only `\TODO` in `main.tex` and `references.bib`.
  - Delete the `\TODO` macro (L14) before submission so a stray TODO cannot compile silently.
  - Non-red items that block submission: `SPOT_CHECK.md` (0/5 ticked); `preregistration.md` "Status: DRAFT"; Katz 2025 bib entry incomplete.

### 3.12 Patterns that read as AI-generated

**"X, not Y" constructions.** There are at least nine; cut about half.
- "depends on the population, not on non-native authorship" (abstract and L401-402)
- "Movement toward LLM style, not loss of variety" (L374)
- "Dispersion: steady, not sudden" (heading)
- "less exposed ..., not unexposed" (L169-170, L457)
- "school learners, not the TOEFL population" (L173-174)
- "stratified, not the full archive" (L456)
- "our own repository, not a third-party registry" (L459-460)

**Aphoristic closers.**
- L374
- L402
- L425-426 ("emptying ... filling")
- L446-447 ("as current as the writing being measured")
- L249 ("writes outside the region defined by its predecessors")

**Parallel aphorism.** L422 ("what readers notice and what authors can edit out").

There are no `HUMAN-EDIT:` commits in the history. A short human editing pass, logged as such, is still the cheapest credibility gain available, as it was in round 1.

---

## 4. Policy: AI Use section, AI_DISCLOSURE.md and ACL policy

### 4.1 Applicable policy

- **ACL policy on AI writing assistance.** As set out in 2023 and, to my knowledge, still in force for ARR, this is a "new ideas plus new text" use: the AI proposed the research question and hypotheses, wrote all code and drafted all text.
  - Such use is discouraged but not prohibited.
  - Disclosure is required.
  - AI systems cannot be authors.
  - The human authors are responsible for correctness, originality and citations.
- **Responsible NLP checklist.** The question on AI assistants must give the same content as the paper.
- I cannot verify ACL 2027-specific changes. **[HUMAN]** Check the ACL 2027 CFP and ARR policy page before submission.

### 4.2 Is the AI Use section honest and complete?

It is much better than in round 1. The research-question attribution is corrected, the dual role (drafter and data source) is disclosed in §4 and in AI Use, the model and interface are named, and simulated peer review is disclosed. Remaining problems, in order of importance:

1. **A human verification is claimed but has not happened** (N4). The past tense ("then checked") plus a TODO is the worst combination, because it shows a claim written ahead of the fact. Either do it, or write: "The human author(s) will check a random sample of five citations before publication."
2. **There is no accountability sentence.** Add: "The human author(s) take full responsibility for the content, including the citations and the analysis choices." `AI_DISCLOSURE.md` already says "accountable"; the paper must too.
3. **"Checked against its source" overstates the AI verification** (N5). Give counts and access limits.
4. **The extent of human editing is unstated.** Git has no `HUMAN-EDIT:` commits. Either do and log an editing pass, or say "the text has not been edited by a human". Readers will check, and the current wording ("drafted all text" with human edits "labelled separately") implies that edits exist.
5. **The analysis plan's authorship is omitted.** `AI_DISCLOSURE.md` says the AI "wrote the analysis plan" and coined the term "Machine-Style Overlap". Add both to the paper: one clause.
6. **"Approved the analysis plan and its deviations" cannot be verified.** There are no human commits, and `preregistration.md` says "Written by Claude (AI); verified by the author". A dated human commit approving the final plan and deviation log would make this checkable.
7. **The simulated reviewers are not independent.** They are sessions of the same model family. Say so ("separate sessions of the same AI system"). It is a real limitation of that process.
8. **"Every number ... is inserted automatically"** should read "every reported result" (design constants are typed).

### 4.3 Consistency with AI_DISCLOSURE.md

`AI_DISCLOSURE.md` was rewritten in commit 6e16675 at 00:48 today, during this review. The version I first opened was the older one, which named the author and claimed the author "checks every citation". The current file is close to the paper. What must still change:

| Item | Paper | AI_DISCLOSURE.md | Required change |
|---|---|---|---|
| Citation spot-check | "then checked a random sample of five" + TODO | "Checked a random sample of five citations (see `lit/SPOT_CHECK.md`)" | Both are untrue until done. Fix both, after doing the check. |
| Accountability | absent | "is accountable for the final content" | Add to the paper. |
| Analysis plan and term | not stated | AI "wrote the analysis plan", proposed the term | Add to the paper. |
| AI verification | "checked against its source" | "citation verification (separate AI sessions)" | Both should give counts and access limits. |
| Human edits | implies labelled human edits exist | "any human edit ... starting HUMAN-EDIT:" | State the number (currently zero) in both. |
| Simulated review | "separate AI sessions" | "separate AI sessions; `paper/reviews/`" | Add "of the same model family" to both. |
| "If they differ, the paper is authoritative" | n/a | present | Fine. Keep the two in sync instead of relying on it. |

Other repository files that contradict the paper and will be read by any reviewer who opens the supplement:
- **`README.md`.** Old title. Says "five local models". Says the plan was "frozen before the full run". Says the paper was "verified by the human author".
- **`preregistration.md`.**
  - "Status: DRAFT".
  - The retracted "conservative estimate" sentence.
  - Deviation 5, "no analysis choice was changed afterwards", contradicts §6.5.
  - Deviation 7 dates the 2026 model to "before the final run" but omits that it came after the preliminary arXiv results.
  - Deviations are numbered out of order.
  - Its Liang deviation says the release lacks 8th-grade essays; verification batch4 found this inaccurate.
- **`CITATION.cff`.** Old title, plus the author's identity (anonymity).

### 4.4 Likely reviewer reaction

- The disclosure is now compliant and, apart from the items above, unusually complete.
- The swing factor remains the same as in round 1: any visible gap between a claim and the record (N3, N4) will be read as "the AI wrote a claim and no human checked it". Fix those two and the disclosure becomes a strength.
- An ethics flag is still moderately likely because of the discouraged-use tier. The Ethics/AI Use text should not argue that AI authorship is desirable, and it does not.

---

## 5. Scores as I would expect them

| | Round 1 (R1/R2) | Round 2 (expected) |
|---|---|---|
| Soundness | 2 / 2 | 3 (range 2.5-3.5): core fixes are done, but the ITS specification, Hansard handling and 2026 narrative are still open |
| Excitement | 3 / 3 | 3-3.5: the generator-vintage result, if correctly stated, is a genuine, quotable finding |
| Overall | 2 / 2 | about 3.0 |

## 6. Likely decision and the five changes with the biggest effect

**Likely decision now: Findings of ACL.**
- *Main conference:* not yet. Reviewers will still find the unchanged ITS specification, the selectively reported Hansard results and the 2026 inconsistency.
- *Theme-track workshop:* near-certain accept.
- *Main conference after revision:* plausible (borderline) if the five changes below are made. They are mostly reanalysis of data already collected; only (1b) needs new generation.

**The five changes, in order of effect on acceptance:**

1. **Make the 2026 and generator-set story match the data, and stop resting it on one uncontrolled model.**
   - Rewrite the abstract, title verb, §6.5, Fig. 3 caption, Limitations and Conclusion around what Table 1 and Fig. 3 show: regions with 2023 models flatten, while regions built from 2024-2026 models rise with or without Claude (N1, N2). Say "plateaued near 45%".
   - (1b) Add at least one more 2025-26 generator with logged decoding, one prompt per call (an API model, or a second recent open model). Re-run per-generator LOMO time series. Label 2026 exploratory.
   - Without this, the paper's most distinctive claim is attackable in one sentence.
2. **Make the record internally consistent and finish the human checks.**
   - Do and log the spot-check, or retract the claim, and remove the TODO.
   - Add the accountability sentence.
   - Reconcile App. B(4), §6.5 and the plan's deviations 5 and 7 with git.
   - Freeze or archive the plan with an honest status, and drop "pre-registered".
   - Log every deviation (§3.8).
   - Update `README.md` and `AI_DISCLOSURE.md` (§4.3).
   - Fix the "8.00" and dash rendering bugs.
   - Cheap, and decisive for how reviewers read an AI-conducted paper.
3. **Do R1's time-series robustness work.**
   - Event study with yearly or quarterly post indicators.
   - Quadratic/spline and window sensitivity of the pre-trend.
   - Field-month block bootstrap.
   - Drift placebos at several origins (for example ≤2016, ≤2017, ≤2018), compared as a distribution with the 25.7 pp gap.
   - All placebo parameters, including Hansard's failed placebos.
   - The H4 contrast with Holm correction across the eight archives.
   - These are all reanalyses of existing caches.
4. **Put the comparison and the construct on defensible scales.**
   - Report the arXiv-Hansard contrast on a relative or logit scale (or with injection-calibrated sensitivity), with the Hansard caveats (2022 turnover, threshold 0.6 significance, marker rise; N6, N7).
   - Add the mixture identity with implied α next to Liang et al. 2024 for cs and math.
   - Add the top-features table.
   - Cite and differentiate Askitas 2025 and Chang 2026.
   - This answers R2's novelty objection ("this is just a detector flag rate") directly.
5. **Make the theme-track link credible.**
   - Redo the dispersion analysis with length control (fixed truncation or within length and archive bins), bootstrap CIs, the same ITS test, and a small figure (N8).
   - Scope the learner/detector conclusion in the abstract (N10).
   - Describe the two extra instruments in §5 (N11).
   - A clean "location moved, spread did not accelerate" result, properly controlled, is a useful homogenization finding for this track. The current version is not yet one.
