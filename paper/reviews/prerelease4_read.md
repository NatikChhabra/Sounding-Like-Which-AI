# Pre-release read 4: area-chair first read of `paper/preprint.pdf`

Reader: senior ACL area chair, first contact with the paper, no knowledge of its history (earlier review files were not read).
Commit 80e1355. I read all 16 pages of `paper/preprint.pdf` and looked at rendered pages 1, 4, 5, 6, 8, 15 and 16 at 130 dpi. Where a
number looked off I checked it against `results/*.csv|json`. I edited no project file except this report.

Counts: **Must fix 9 · Should fix 14 · Polish 22**

---

## Verdict

**What the paper does.** It defines Machine-Style Overlap (MSO), the share of documents that a calibrated style
classifier puts on the LLM side of a likelihood-ratio-one boundary, and measures it in 131k arXiv abstracts from 2015 to 2026.
The headline is a 25.4 pp rise above the pre-ChatGPT trend by June 2025, with careful placebo, drift and specification
checks. The more original part is the vintage analysis. Against generators whose pretraining data predate ChatGPT the shift
is smaller but present. With a single generator as the reference, overlap peaks later for later generators, so a fixed
reference set (including a fixed marker-word list) can show the shift receding even while writing keeps moving.

**Strengths.** The estimand is clean and well motivated (§3). The robustness work in Table 2 is unusually thorough for a
corpus study. Hypotheses that failed are reported honestly (H5), and so are the analysis-plan deviations and the AI
authorship. The idea that "LLM style" depends on the reference model's vintage is timely and useful to the
prevalence-estimation literature.

**Weaknesses a reviewer will raise.**
1. The core of the title question (§6.4) is post hoc. It was added after simulated review, three of its generators were
   added after the pattern had been seen, and the first test that was tried (release date vs 2025→2026 change) gives
   ρ = 0.67 on annual means but 0.18 from 2025Q4 (Appendix A). The main text and abstract give only ρ = 0.79.
2. The "pre-ChatGPT-data" result rests mostly on RAID. Three quarters of that region's training texts come from RAID,
   which used a different prompt. The two models the author ran on the paper's own prompts give 3.5 pp, but the abstract
   calls the gap "clear" at 7.5 pp. One of the four models (Vicuna) is fine-tuned on ChatGPT conversations.
3. The paper is very dense. §6.4 has more than 40 numbers in about one column, and the secondary results (Hansard,
   dispersion, essays, perplexity bias) take abstract and main-text space away from the main contribution.
4. Some statements contradict each other or the paper's own tables (Must fix 1–5 below).

**Recommendation.**
- *ACL main:* weak reject in current form. It is a single-genre measurement study whose most novel claim is exploratory
  and based on 18 points with correlated errors.
- *Findings:* borderline to weak accept once the Must-fix items are done. The measurement and robustness work is solid
  and the vintage point is a real contribution if it is framed as exploratory.
- *Student research workshop:* accept. Note that the author describes himself as an independent researcher, so check
  SRW eligibility.

**Top three changes within the 8-page limit.** The main text currently ends at the foot of page 8, so every addition
needs a matching cut.
1. **Rewrite the abstract (it is 253 words; ACL's limit is 200) and the first paragraph of the introduction** so the
   finding comes first and the over-claims are gone (Must fix 1–3, 9). Cut the perplexity/TOEFL sentence and the
   "one quarter long" clause from the abstract. In the introduction, swap the detection sentence in paragraph 1 for a
   sentence stating the finding (copy-ready text under Must fix 9).
2. **Make §6.4 honest and readable at the same length.** Say in its first sentence which parts are exploratory. Report ρ
   on the generators that were fixed before the pattern was seen (my approximate recomputation gives about 0.77, n = 15,
   which strengthens the paper). Fix the Gemma sentence. Pay for this by moving the RAID-subset parenthetical and the
   nonparametric duplicates to Appendix D.
3. **Move the secondary results to the appendix.** Cut §6.6 to three sentences (Hansard, dispersion, learners), cut the
   Homogenisation paragraph of §2 by half, and move the Fast-DetectGPT sentence to an appendix. Use about 12 of the lines
   saved to define the Table 2 variants, state the equal-weighting caveat in §3, and give the instrument-agreement number
   for the pre-ChatGPT-data region.

---

## Must fix

### M1. The abstract is over the ACL word limit and contains two claims the body does not support
The abstract is 253 words; the ACL limit is 200.

(a) *"for the latest generators the fall is one quarter long."*
This is true only for gpt-oss and Granite 4.2 (§6.4: "for gpt-oss and Granite 4.2 that one quarter is the whole
decline"). gpt-oss (2025-08) is not among the latest models. Of the 2026 models, Gemma 4 peaked in 2025Q4 and has been
falling for three quarters, Qwen3.5 peaked in 2026Q1, and the 2026 model has not fallen at all (Table 5). The body also
says these one-quarter falls "may mark a shared fluctuation rather than a turn", which the abstract leaves out.

(b) *"If this pattern persists, a fixed reference set, including a list of marker words such as delve, will eventually
show the shift receding."*
Two fixed reference sets in the paper did **not** recede in 2026. The 14-generator main region went from 40.6% to 44.7%,
and the seven local models pooled over P1–P3 went from 43.3% to 48.4% (§6.4). "Will eventually" is a forecast; the
evidence supports "can".

(c) *"the gap is smaller but clear (7.5 percentage points; 11.9 measured nonparametrically)."*
Three quarters of this region's training texts come from RAID, which used RAID's own prompt (§6.4). On the paper's own
prompts the gap is 3.5 pp (CI 1.5–5.5). "Clear" should not rest on the part with the uncontrolled prompt. The number
11.9 is also the region's 2026 MSO (11.9%), quoted two sentences earlier in §6.4, so readers will mix the two up.

Copy-ready abstract (200 words):
> Studies of LLM-assisted writing estimate how much text was produced with LLM help. We ask how much writing, by any
> author, falls on the LLM side of a stylistic boundary, and which LLMs define that side. We define **Machine-Style
> Overlap** (MSO): the share of documents that a calibrated classifier on closed-class, syntactic and length features
> judges at least as likely to be LLM output as pre-ChatGPT human writing. In 131,448 arXiv abstracts (2015–2026), MSO
> was 9.2% before ChatGPT and by June 2025 stood 25.4 percentage points (pp) above its pre-ChatGPT trend, nearly four
> times the largest placebo or drift gap. Because recent LLMs learn from recent writing, we compare reference generators
> by vintage. Against generators whose pretraining data predate ChatGPT the gap is smaller (7.5 pp; 3.5 pp for the two
> we ran on our own prompts). With one generator at a time as reference, overlap rose and then fell, peaking later for
> later generators (exploratory rank correlation 0.79, n = 18), so a fixed reference set, like a fixed list of marker
> words such as *delve*, can show the shift receding while writing keeps moving. In student essays, English learners'
> writing is less machine-like than their peers', mostly because of proficiency.

("Nearly four times": 25.4/6.5 = 3.9 for the largest drift placebo, 25.4/5.8 = 4.4 for the largest 30-month placebo.)

### M2. §6.4: the Gemma comparison is false as written
> "In all three same-family pairs the newer model's change was higher, for Gemma within Gemma 4's interval."

From `results/arxiv_vintage_uncertainty.csv`: Gemma 3's change is −2.04 pp (CI −3.11 to −0.93) and Gemma 4's is −0.88 pp
(CI −1.82 to +0.06). Gemma 3's estimate lies outside Gemma 4's interval, and Gemma 4's estimate lies just outside Gemma
3's interval. The two intervals overlap; neither estimate lies inside the other's interval.
Fix:
> "In all three same-family pairs the newer model's change was higher; for Gemma the difference is 1.2 pp and the two
> intervals overlap."

### M3. §3 defines P_LLM as an equal-weight mixture, but the vintage regions are not equal-weighted
§3: *"P_LLM the distribution for LLM output in the same genre, an equal-weight mixture over a reference set of generators
and prompting styles chosen by us."*
§6.4: *"Three quarters of the region's training texts come from RAID, so its generators are not equally weighted."*
In `arxiv_v_pre2022data_matched_separability.csv` the region has 900 RAID texts against 150 + 150 local. Readers will
see this as a contradiction of the definition.
Fix in §3:
> "…an equal-weight mixture over a reference set of generators and prompting styles chosen by us (the main instrument
> caps each generator at 450 texts; §6.4 notes where a region departs from equal weights)."

### M4. "Simulated review" is used before it is defined, and it is what the title analysis rests on
§1: *"The vintage analysis was added after simulated review."* §4: *"Five further open models were added after review."*
A first-time reader cannot tell that this means AI-simulated peer review (defined only in the Acknowledgements on page 10).
Because the vintage analysis is the title's question, this matters.
Fix in §1:
> "The vintage analysis, which gives the paper its title, was added after simulated peer review by separate AI sessions
> (Acknowledgements) and is exploratory."

Fix in §4: "added after review" → "added after the second simulated review".

### M5. "No LLM-topic abstracts" (Table 2) is never defined, and "abstracts without math" is ambiguous
Table 2 lists "No LLM-topic abstracts 23.9" but no section says how LLM-topic abstracts were identified. "Abstracts
without math" (§6.2, §6.3, Table 2) can be read as "not from the mathematics field", especially since §6.3 then
compares computer science with mathematics.
Fix: in §5 *Time series*, add the clause
> "…hold the field mix fixed, drop abstracts that mention language models (keyword list in the repository) or contain
> LaTeX math…"

In Table 2 and §6.3, rename the row to "Abstracts without LaTeX math".

### M6. The Acknowledgements use the future tense for something that must already have happened in a released preprint
> "Citations were not checked by a human; the human author will read the final paper before release."

If the PDF is released, that sentence is either already false or describes a step that was skipped.
Fix after the read:
> "Citations were not checked by a human; the human author read the final paper before release."

### M7. "Content-word-free" over-states what the features do
Abstract: *"a calibrated classifier on content-word-free style features"*. §5: *"Features exclude content words."*
The strongest feature is MTLD lexical diversity (Table 3, coefficient 1.30), and it is computed over all tokens, content
words included. Mean word length also depends on content words. The features ignore the *identity* of content words; they
do not exclude them.
Fix in §5:
> "Features use no content-word identities, to limit topic sensitivity: …"

In the abstract, use the wording from M1.

### M8. Drift placebos: "before any LLM writing assistance" is too strong, and a significant drift placebo is not discussed
§5: *"…test for a gap in June 2022, 41 to 65 months later and before any LLM writing assistance, so any gap they show
reflects instrument ageing."* The Table 2 header repeats "no LLM writing assistance".
GPT-3-based writing tools existed from 2020. A gap could also come from a misspecified pre-trend, not only from ageing.
The "instrument to 2017" placebo is −2.3 pp with p = 0.020, the only significant row in the placebo block, and the text
never mentions it.
Fixes:
> §5: "…41 to 65 months later and before ChatGPT, so any gap they show reflects instrument ageing or trend
> misspecification."

> Table 2 header: "*Placebos (before ChatGPT; gap in June 2022)*"

> §6.3, after "−2.3 and −1.0 pp (Table 2)": "; only the −2.3 pp gap has p < 0.05"

### M9. The first paragraph of the introduction does not state the finding
The introduction's first paragraph is all literature (traces of LLM use, then human and detector failure). The first
result appears in contribution (3) on page 2, and there without a number ("moved far into the LLM region").
Fix: replace the sentence "Judging individual documents is harder: … (Liang et al., 2023)." (about 5 lines; the
non-native point is made again in §2 and §6.6) with:
> "We find that by mid-2025 the share of arXiv abstracts on the LLM side of a calibrated style boundary stood 25 points
> above its pre-ChatGPT trend, and that whether it was still rising in 2026 depends on which LLMs define the boundary."

In contribution (3), change "moved far into the LLM region after 2022" to "moved into the LLM region after 2022 (25.4 pp
above trend by June 2025)".

---

## Should fix

### S1. The exploratory status and robustness of ρ need one more sentence in the main text
The main text gives ρ = 0.79 and says it "was chosen after a first test (Appendix A)". It does not say that the first
test (release date vs 2025→2026 change) gave 0.67 on annual means and 0.18 (p = 0.464) from 2025Q4. Nor does it say
whether the peak correlation survives without the three 2026 open models, which were added after the pattern was seen.
My approximate recomputation, using Table 1 months, RAID tied at mid-2023 and Table 5 peaks, gives ρ ≈ 0.77 (n = 15)
without them. Partialling out each region's 2015–2021 baseline MSO leaves ρ ≈ 0.78, so region distinctness does not
explain the pattern either. Both results help the paper.
Copy-ready replacement for "The analysis is exploratory and was chosen after a first test (Appendix A)." (similar length):
> "The analysis is exploratory: a first test, release date against the 2025-to-2026 change, gave 0.67 on annual means
> but 0.18 from 2025Q4 (Appendix A). Without the three 2026 open models, added after the pattern was seen, ρ = [value]."

(Generate [value] from the analysis code; do not type my approximation.)

### S2. The "pre-ChatGPT-data" label hides that Vicuna imitates ChatGPT
The label, and the claim that the region "reflects models unlikely to have learned their style from post-ChatGPT
scientific writing", are true for scientific writing. But Vicuna is fine-tuned on shared ChatGPT conversations (Table 1,
note d), so it learned ChatGPT's style directly. That is disclosed only in a table footnote. Add to §6.4 after "…no
recent abstracts":
> "Vicuna imitates ChatGPT's conversational style, but not its abstracts."

Also align the Figure 2a legend ("Pre-ChatGPT pretraining data") with the text label ("pre-ChatGPT-data region").

### S3. 7.5 pp vs 11.9 pp: two estimates of one gap that disagree beyond the CI
The ITS gap is 7.5 (CI 4.6–10.4) and the nonparametric gap is 11.9 (no CI). The text explains why the ITS line
understates the gap, but then the abstract quotes both. `results/arxiv_vintage.csv` already has
`gap_to_eval` = 13.1 (CI 12.1–14.2), the ITS fitted only to June 2025, which matches the "Post-trend fitted to June 2025"
row of Table 2. Use that one estimator for every vintage region in §6.4 and drop the nonparametric triplet. This saves
two lines and removes the 11.9/11.9 clash.

### S4. Fast-DetectGPT result: contrary evidence answered with speculation
> "…its flag rate on 600 abstracts per year falls (11.3% in 2022, 5.3% in 2026); larger scoring models, as in the
> original method, might detect the shift."

A standard detector moving the other way is relevant, and "might detect the shift" is untested. The threshold used for
the "flag rate" is also not stated.
Fix: move the sentence to an appendix with its threshold, and in §6.3 keep:
> "A zero-shot detector with GPT-2 small separates our human and LLM abstracts poorly (AUC 0.737) and does not track
> the shift (Appendix C)."

### S5. The 2026Q3 quarter drives the "latest peaks"
> "From 2026Q2 to 2026Q3 overlap fell under every generator other than the 2026 model."

A fall in the same final quarter for 18 of 19 regions points to something about 2026Q3 abstracts (sampling, season,
revision lag), not about the generators. Peaks in 2026Q2 (gpt-oss, Granite 4.2) are therefore placed by this single
quarter. Say so plainly in the Fig. 2b caption:
> "Peaks in 2026Q2 rest on a fall in 2026Q3 that is shared by every generator except the 2026 model."

### S6. "Overlap with each generator but the 2026 model rose and then fell" vs "MSO rose from 2022 to 2025 under every generator except Cohere's"
Both are true (Cohere peaked in 2023Q2), but read one after the other they look contradictory.
Fix:
> "…under every generator except Cohere's chat model, whose overlap peaked in 2023Q2."

### S7. Pooled vs single regions: the explanation is unclear
> "…and pooled regions need not follow their members' title-only regions: the seven local models pooled over all three
> prompts rose from 43.3% to 48.4%."

This mixes two changes: pooling, and adding P2/P3 prompts. Readers will not know which one drives the rise.
`arxiv_vintage.csv` has `local_p1` (title-only, pooled), so split them:
> "…pooled title-only regions need not follow their members (the seven local models pooled on P1: [y2025]% to
> [y2026]%), and adding revision and style-avoiding prompts raises the 2026 value further (all three prompts: 43.3% to
> 48.4%)."

### S8. "2.1 times the extrapolated trend value" is ambiguous
> "The trend gap in June 2025 is 25.4 pp …, about 2.1 times the extrapolated trend value."

Most readers will take this to mean that observed MSO is 2.1× the trend. In fact the *gap* is 2.1× the trend, so observed
MSO is about 3.1× the trend.
Fix:
> "…, so the fitted value is about three times the extrapolated trend."

Mirror this in Appendix F ("about 0.2 times its extrapolated trend value").

### S9. H1 "non-zero" is guaranteed by construction
H1, "pre-ChatGPT MSO is non-zero", must hold for any classifier whose two classes are not perfectly separable. Only the
"differs by field" part is a test. Say so, which costs no space:
> §1: "pre-ChatGPT MSO differs by field (H1; that it is non-zero follows from imperfect separability)"

### S10. Instrument agreement on the region that carries the vintage argument is not reported
The Limitations give κ = 0.64 between classifier families for the main abstract instrument. In
`arxiv_v_pre2022data_matched_instrument.json` the same κ is 0.48, and in `arxiv_v_old_open_p1_instrument.json` (the 3.5 pp
own-prompt result) it is 0.42. The population-level MSO agrees (10.3% vs 10.4%). Add to the Limitations sentence:
> "(Cohen's κ = 0.64; 0.48 for the pre-ChatGPT-data region; speech 0.26, essays 0.29)"

### S11. The learner odds ratio is mislabelled in the main text
§6.6: *"(2.3% vs 4.2%; odds ratio 0.55, 0.87 after adjusting for proficiency)"* reads as if 0.55 were unadjusted.
Appendix H says 0.55 is already adjusted for prompt and grade.
Fix:
> "odds ratio 0.55 adjusted for prompt and grade, 0.87 when proficiency is added"

### S12. Marker words rose in Hansard almost as much as in arXiv
Appendix F: *"Published marker words also rose in speeches (1.6 pp above trend)"*, against 1.9 pp for arXiv (§6.5).
This sits uneasily with "parliamentary speech changed little" (contribution 5). Give the CI. If it overlaps the arXiv
value, say in Appendix F:
> "…, close to the arXiv marker gap, so the genres differ in style overlap more than in marker words."

### S13. The same caveat is repeated three times
- "so a falling marker share does not by itself show that writing stopped moving" (§6.5)
- "even if writing keeps moving" (§6.4)
- "so the decline of delve need not mean that writing stopped moving" (§7)

Keep the §7 version and delete the other two clauses (about 2 lines saved). Similarly, "Hansard is a weak comparison"
appears in §6.6, Appendix F and the Limitations; keep the §6.6 version and the Limitations sentence and cut "The
comparison is weak, however." from Appendix F.

### S14. Fig. 2a and its caption disagree with the headline RAID number
The caption says *"The RAID line in (a) keeps summary-style outputs."* The text's headline RAID number (7.3 pp) drops
them. Either plot the version that drops summaries, or explain why the figure keeps them. As written, a reader comparing
figure and text will think they disagree.

---

## Polish

**Prose, hedging, padding**
1. §1 contribution (1): *"that, for an optimal classifier, equals the Bayes classifier's false-positive rate on
   pre-ChatGPT writing"* says "optimal classifier" and "Bayes classifier" for the same thing. Replace with "that, on
   pre-ChatGPT writing, equals the false-positive rate of the Bayes classifier".
2. §1 contribution (3): *"give gaps at most about a quarter as large"* stacks two approximators. Replace with "give
   gaps no more than a quarter as large".
3. §6.3: *"Instrument ageing can thus produce gaps of a few points, up to about a quarter of the observed gap."*
   Replace with "Instrument ageing can thus produce gaps of up to 6.5 pp, a quarter of the observed gap."
4. §6.3: *"Of the 34 placebo breaks, 8.8% give a gap with p < 0.05"*. A count reads better here: "3 of the 34
   placebo breaks give p < 0.05 (1.7 expected)".
5. §6.2: *"Overall MSO was also rising slowly before ChatGPT (0.5 pp per year)."* The "also" has nothing to refer to.
   Replace with "Before ChatGPT, overall MSO rose by 0.5 pp per year."
6. §6.4: *"Part of the shift is therefore towards the style of the pre-ChatGPT-data generators and is unlikely to be an
   artefact of newer models learning from newer abstracts, though the estimate from our own prompts is small."*
   This is one sentence carrying three hedges. Replace with "Part of the shift therefore points towards generators that
   could not have learned it from recent abstracts; on our own prompts that part is 3.5 pp."
7. §6.4: *"Of our comparisons, only the pre-ChatGPT-data region is free of the question of who learned from whom."*
   Replace with "Only the pre-ChatGPT-data region avoids the question of who learned from whom."
8. §6.4: *"Gemma 4 (12B released in June 2026)"*. Replace with "Gemma 4 12B (released June 2026)".
9. §6.4: *"and 0.83 with all RAID models, whose release months are approximate, dated mid-2023."* This can be read as
   "0.79 excluded some RAID models". Replace with "and 0.83 when all six RAID models are dated mid-2023".
10. §5: *"MTLD lexical diversity (measure of textual lexical diversity; McCarthy and Jarvis, 2010)"* says the same
    thing twice. Replace with "lexical diversity (MTLD; McCarthy and Jarvis, 2010)".
11. Figure 3 caption: *"The baseline is only loosely related to the gap."* Give the number (rank correlation across
    the eight fields) or cut the sentence.
12. Appendix H: *"In these data a perplexity instrument penalises predictable writing."* This restates the previous two
    sentences; cut it.

**Consistency of names and units**
13. Model names differ across tables:
    - "Mistral-7B-Instr. v0.1" (Tables 1 and 5) vs "RAID Mistral-chat" (Table 4)
    - "Cohere command" (Tables 1 and 5, Fig. 2b) vs "RAID Cohere-chat" (Table 4) vs "Cohere's chat model" (§6.4)
    - "Llama-2-Chat 70B" vs "RAID Llama-chat"
    - "MPT-30B-chat" vs "RAID MPT-chat"
    - "Mistral 7B Instruct v0.3" vs "Mistral 7B" (Table 4) vs "Mistral 7B v0.3" (Table 5)
    - "Claude Opus 5.5" (Table 4) vs "2026 model" (Table 5)

    Use the Table 1 names everywhere. Table 4 rows should read, for example, "Cohere command (RAID)" and
    "2026 model (Claude Opus 5.5)".
14. "pp" is never defined. The abstract and the Table 2 caption spell out "percentage points", and the body uses "pp"
    from §6.2 on. Add "(pp)" at the first use in the abstract (done in the M1 text) and keep "pp" everywhere else,
    including the Table 2 caption: "(pp above the extrapolated pre-ChatGPT trend)".
15. Table 1 date formats are mixed: "2024-05", "2026-Q1" and "2023". The quarter notation elsewhere is "2026Q1"; use
    "2026Q1" in the table too.
16. Table 1 group header: *"Local; vintage analysis only (abstracts, P1–P3)"*. The vintage analysis uses P1 only
    (§5 *Vintage*). Change to "(abstracts; P1 used)".
17. §6.2: *"χ2(7) = 354.55"*. Two decimals is spurious precision; use "χ²(7) = 355".
18. Run-in headings: "*Fields (H4).*" starts mid-paragraph in §6.3, while §6.4 starts its run-ins on new lines. A
    paragraph break before "Fields (H4)" costs no extra line at the current break.

**Figures**
19. Fig. 2a: the legend sits over the ChatGPT line and the 2015–2021 series, and "Open models 2026" (dashed orange) is
    hard to tell apart from "2026 model" (solid orange). Move the legend below the panel or to the upper left, and give
    the 2026 model a distinct colour or marker.
20. Fig. 2b: the 2023 generators sit left of the first tick (2024) and there is no 2023 tick. The "Granite 4.2 8B"
    label overlaps its marker and the "2026 model (still rising)" label. Add a 2023 tick and nudge the labels.

**Front matter and references**
21. The author-block URL ends in a hyphen ("…/Sounding-Like-Which-AI-"). If that is the real repository name, it is
    fine; otherwise fix it, because readers will assume a line-break artefact.
22. References: Yakura et al. carries a version suffix ("arXiv:2409.01754v4") that no other preprint has. The IBM
    Granite entry folds two model cards and two URLs into one note. Split it, or keep only the organisation URL.

---

## Space accounting for the suggested changes (main text, 2-column lines, approximate)

| Change | Lines |
|---|---|
| M9: replace the "Judging individual documents…" sentence with a finding sentence | −1 |
| S3: drop the nonparametric triplet in §6.4 | −2 |
| S4: move Fast-DetectGPT to the appendix (keep one sentence) | −2 |
| S13: cut the duplicated "writing keeps moving" clauses | −2 |
| §6.4: move the RAID-subset parenthetical "(8.6 with summary-style… kept)" to Appendix D | −2 |
| §6.6: move the TOEFL/GPT-2 sentence to Appendix H (the abstract no longer mentions it) | −4 |
| §2: cut the model-collapse sentence (already cited in §7) | −3 |
| **Saved** | **−16** |
| M3, M4, M5, M8 additions | +5 |
| S1, S2, S6, S11 additions | +5 |
| **Net** | **about −6** |

The main text would still end on page 8, with room to spare.

---

## Summary

9 Must fix, 14 Should fix, 22 Polish.

The most important items:
- **M1:** the abstract is 253 words (limit 200). It claims "for the latest generators the fall is one quarter long",
  which holds only for gpt-oss and Granite 4.2. It says a fixed reference set "will eventually show the shift receding",
  but two fixed sets in the paper rose in 2026. It calls the pre-ChatGPT-data gap "clear" when it rests on RAID's prompt
  (3.5 pp on the paper's own prompts). A copy-ready 200-word abstract is given.
- **M2:** "for Gemma within Gemma 4's interval" is false per `arxiv_vintage_uncertainty.csv`.
- **M3:** §3's "equal-weight mixture" contradicts §6.4's 75%-RAID region.
- **M4, M5:** "simulated review" and the Table 2 row "No LLM-topic abstracts" are undefined.
- **M6:** the Acknowledgements' "will read the final paper before release" is in the future tense.
- **M7, M8:** "content-word-free" (MTLD uses content words) and "before any LLM writing assistance" over-state.
- **M9:** the finding is missing from the first paragraph of the introduction.
- **Verdict:** Findings borderline to weak accept after the fixes; main track weak reject; SRW accept.
