# Round 1: Area Chair meta-review and editorial pass

**Submission:** "Sounding Like AI Before AI: Machine-Style Overlap in Human Writing"
**Track:** ACL 2027 theme track, "Homogenization and knowledge collapse in LLMs" (long paper)
**Inputs:** `paper/main.tex`, `paper/main.pdf` (8 pp. incl. references), `paper/figures/*.pdf`. I also checked `results/*`, `preregistration.md`, `lit/CITATIONS.md`, `paper/AI_DISCLOSURE.md` and parts of `code/`, because reviewers who follow the repository link will check them too.

Line numbers below are `main.tex` source lines.

Caveat on this review: an agent from the same model family as the system that drafted the paper wrote it. Shared blind spots are possible, so a human should do a final read.

---

## 1. Meta-review

### Summary
The paper defines Machine-Style Overlap (MSO): the share of a genre's documents that a balanced, calibrated classifier places on the LLM side (p >= 0.5). The classifier uses content-word-free features (function words, POS trigrams, dependency labels, punctuation, length and lexical diversity) and is trained to separate pre-ChatGPT human text from LLM text. Main results:

- 9.4% of pre-ChatGPT arXiv abstracts are already "in the region", with a range of 4.7% (astro-ph) to 16.2% (econ).
- arXiv MSO rose to about 40% by 2026, an excess of 22.5 points over the pre-ChatGPT trend in June 2025. Parliamentary speech moved 1.4 points.
- Marker-word share rose and then fell back, while MSO did not fall.
- Chat tuning raises the share of model output that lands in the region.
- In PERSUADE essays, English-language learners (ELL) are less often in the region than other writers.

### Strengths
1. **A useful reframing.** Treating the pre-ChatGPT "LLM share" as an overlap quantity rather than a nuisance is a clean idea. It connects naturally to the theme track, because it measures convergence from the human side.
2. **Careful design for a corpus study.** The design has a monthly interrupted time series, placebo breaks, a control genre, a field gradient, leave-one-generator-out regions, two classifier families, grouped CV, and identical cleaning for human and LLM text. Every number is inserted automatically from the result files, which is strong reproducibility practice.
3. **The marker-versus-style divergence (Fig. 1c vs 1a) is the most interesting finding.** It is practically relevant for anyone who tracks LLM influence with word lists.
4. **Honest scoping in places.** The paper does not separate LLM use from human adoption (L130-131), the feedback-loop paragraph is labelled as a hypothesis, and the fragility of the ELL contrast is reported rather than hidden.
5. **Short and readable.** The main text is about 5.3 pages, the prose is mostly plain, and there is little padding.

### Weaknesses (ordered by how much they will cost in review)
1. **Unfinished artefacts are visible.** Appendix A is a red `[TODO: table from results/...]` (L374). The main text cites that appendix as evidence for the generalisation claim (L213-214). Many reviewers stop trusting a submission at this point.
2. **The text and the results disagree on facts.**
   - **Generators.** §4 says seven open-weight models were run (incl. Phi-4 and Granite 3.3), but no Phi-4 or Granite outputs appear in any result file (`*_lomo.csv`, `*_separability.csv`). Only five local models were used.
   - **Evaluation month.** June 2025 is called "the last month covered by both treatment and control" (L191-192). `hansard_monthly.csv` has no April-June 2025 data (no sittings around the May 2025 election), and it does have July 2025.
   - **Generalisation.** "The region generalises to generators it never saw" (L213) conflicts with the authors' own LOMO recall: 20.9% (frontier model), 63.3% (Cohere-chat) and 65.3% (gpt-oss), against 85-95% for the others.
   - **2026 trend.** "The rise continued into 2026" (L251) is not what the monthly series shows. It peaked at 43.5% in May 2026 and was 37.7-39.5% in July-September. The 6-month mean in Fig. 1a visibly turns down.
3. **The generator set changed after the results were seen.** L257-258 says that "in a preliminary run without the frontier model, arXiv MSO appeared to fall in 2026; with it, the rise continues". That is an analysis choice made after seeing an unwelcome result. The pre-registration's deviation log says "no analysis choice was changed afterwards" (deviation 5) and dates the frontier-model addition to "before the final run" (deviation 7). Reviewers who read both will see a garden-of-forking-paths problem and an inconsistent record. Report both regions side by side, say exactly when and why the change was made, and stop calling the June 2025 quantity "pre-registered" unless the frozen plan says so. The plan in the repository is marked `Status: DRAFT`, is not on a registry, and does not name June 2025.
4. **The region may partly be a typographic marker.** In both arXiv and essays, the second-strongest LLM-typical feature is the em dash, and the en dash is third for arXiv (`*_features_llm_typical.csv`). `features.py` deliberately keeps them. Human arXiv abstracts from the API often carry LaTeX `--`/`---` rather than Unicode dashes, while chat output uses Unicode. This weakens three claims:
   - "excluding content words entirely" (L82) and "no content words" (L178), insofar as these imply the method avoids marker-like signals;
   - "marker words recede; style does not" (§6.4), which may partly mean "em dashes did not recede";
   - the mechanism in L289-291 ("richer vocabulary, longer words and more uniform sentences"), which leaves dashes out.
   A dash ablation (or mapping `--`/`---` to Unicode for all text) is needed. A top-features table belongs in the main paper; there is room for it.
5. **The baseline is claimed to be a "population property".** This holds only for a fixed feature map, a fixed researcher-chosen generator mixture and a fixed classifier. L224-225 says "Estimator noise would be uniform across fields". That is a false dichotomy: classifier error can easily differ by field, for example because the train pool and LLM seeds follow field proportions. The Bayes paragraph also contains two technical errors (see L122-125 below). Reviewers with ML training will catch them.
6. **Confounds for the post-2022 rise are not discussed.** The candidates are a topic and genre shift inside CS (LLM papers have their own abstract conventions), the growth and changing author mix of arXiv, and template or venue changes. Topic-robust features reduce this risk but do not remove it. "Dose" by field is confounded with how much each field's subject matter changed. At minimum, add a Limitations sentence. Better, add a within-subfield check, for example cs excluding cs.CL/cs.LG/cs.AI.
7. **Several claims go beyond the evidence:**
   - "What humans hear as 'sounding like AI'" (L273-274) and "the perception reflects a real change" (L317). The paper collects no human judgements (L104-105).
   - "Chat tuning makes the style" (§6.5, L318). Base models are already 24-56% in region (MPT base 56.2%, GPT-3 44.5%, Cohere base 39.8%), against a human baseline of 9.4%. Chat tuning amplifies the style; it does not create it.
   - "Learners are the *least* machine-like writers". The comparison has two groups, only 8 of 666 ELL essays are in region, and the thresholded effect is significant in 3 of 10 draws.
   - The self-test conclusion (L332-333) is logically invalid; see the line edits.
8. **The ELL result reverses the pre-registered H5 without saying so.** H5 predicted that learners would have *higher* MSO. The labels "H1-H5" appear in section headings but are never defined in the paper. Saying "contrary to our pre-registered H5" turns a liability into a credibility gain.
9. **Theme fit is asserted, not shown.** The homogenization and knowledge-collapse link lives in one Discussion paragraph. MSO measures movement into a region, not loss of diversity. A simple dispersion statistic over time (feature-space variance of abstracts per year) would make the track fit concrete.
10. **Citations have not been verified.** Every box in `lit/CITATIONS.md` is unticked, yet the paper says the author "verified the citations". Six references are 2026 arXiv preprints with high IDs. Because the paper discloses AI drafting, reviewers will spot-check citations first. One misattributed claim would be fatal; for example, check that Lin and Zhu 2025 and Brooks et al. 2024 really "treat [the pre-period share] as estimator error" (L55-56).

### Formatting and compliance
- **Length.** The main text ends on p. 6 (about 5.3 pages), well within 8. The unused space should go to the feature table, the LOMO table, a results table, the dash ablation and a confound check. There is currently **no table** in the paper.
- **Limitations.** Present, unnumbered, placed after the Discussion: compliant. Its content is incomplete (see L347-353 edits).
- **Ethics statement and AI-use section.** Both present.
- **Conclusion.** There is no Conclusion section. It is not required, but the paper ends on "Implications for detection". Add 3-4 lines.
- **Anonymity.** The PDF header and metadata are clean. Risks:
  - L366 points to "the public repository". The repository contains the author's name (`AI_DISCLOSURE.md`, likely `CITATION.cff` and git author fields). Use an anonymised mirror (for example anonymous.4open.science) or omit the link at review time.
  - "the author" (singular) discloses team size. Prefer "the author(s)" or "the human authors".
- **References.**
  - Unprotected capitals render as "ai", "llm", "chatgpt", "gpt", "raid", "rlhf", "mauve", "mtld", "persuade", "australian".
  - Page ranges lost their en dash ("413425", "16351654", "381392", "755759"); use `--`.
  - Katz and Alexander 2025 has no venue or URL.
  - Peer-reviewed versions should replace arXiv versions: Clark et al. 2021 (ACL), Dugan et al. 2024 (ACL), Pillutla et al. 2021 (NeurIPS), Krishna et al. 2023 (NeurIPS), Kirk et al. (ICLR 2024), Padmakumar and He (ICLR 2024), Liang et al. 2024a (ICML), Liang et al. 2024b (COLM), Wu et al. 2024 (NeurIPS), Juzek and Ward (COLING 2025). Verify each. An ACL audience notices ACL papers cited as arXiv.
- **Responsible NLP checklist.** The AI-assistance question must match the AI-use section and the repository disclosure word for word in substance.

### Figures
- **Fig. 1 (time series).** Clear and the strongest visual. Issues:
  - The arXiv 6-month mean turns down in 2026, which contradicts L251-252.
  - The y-axes differ across panels without a note, so (b) looks more volatile than (a) at a glance. Add "note different y-scales" or share a scale for (a)/(b).
  - The "ChatGPT" label sits on the x-axis line.
  - Rotated year ticks are unnecessary.
  - Say whether the 6-month mean is centred or trailing; the endpoints behave differently.
  - The Hansard monthly points at 0% and 11% come from n = 150 per month. Show a band, or drop the raw points to reduce noise.
- **Fig. 2 (fields).** Good. Issues:
  - The axis uses "pp" and "2025-06" while the text uses "points" and "June 2025". Unify.
  - Add n per field (econ n = 1,256 explains its wide interval).
  - The caption should state the takeaway: baseline and excess orderings differ (econ has the highest baseline but a middling excess), so the baseline does not predict the shift.
- **Fig. 3 (learners).** It is a dot-and-whisker plot, but the caption says "Bars". The legend sits inside the data area. Add n and the in-region count (8/666 ELL). Note that the two instruments have different absolute levels.
- **Missing figure or table:** what defines the region (top LLM-typical and human-typical features), and LOMO recall per generator.

### Likely decision
- **ACL main conference, as submitted: unlikely (reject or borderline).** The TODO appendix, the text-versus-results inconsistencies, the post-hoc generator change and the unverified citations are each enough for a reviewer to give a 2 to 2.5 overall. The AI-authorship disclosure will make reviewers less forgiving of exactly these slips.
- **Findings: plausible after revision.** Required: fill the appendix, fix the facts, report both generator sets, add the dash ablation and feature table, soften the overclaims, and reconcile the disclosure. The idea and the time-series evidence are solid enough for Findings. A main-track accept would also need the confound analysis and an explicit homogenization measurement tied to the theme.
- **Theme-track workshop or non-archival venue: likely accept even now.** The reflexive AI-written framing will be valued there.

**Why:** the core contribution (overlap estimand plus marker-versus-style divergence) is novel enough and well powered. The current version, however, reads as unfinished and occasionally unreliable. In this paper, reliability of reporting is the main thing reviewers will judge, given the disclosure.

---

## 2. Policy and disclosure assessment

### What ACL policy says
The ACL 2023 policy on AI writing assistance (https://2023.aclweb.org/blog/ACL-2023-policy/) distinguishes several kinds of use:

| Kind of use | ACL position |
|---|---|
| Polishing the authors' own text, short-form input assistance | No disclosure needed |
| Literature search | Allowed; authors must read and verify what they cite |
| Low-novelty text | Must be identified and checked |
| New ideas | Acknowledge the model's use and look for the human sources of the ideas |
| **New ideas plus new text** | Models cannot be co-authors. ACL "would discourage such use in ACL submissions", though authors may argue to reviewers that it should be allowed, provided the content is correct, coherent, original and properly cited |
| Code | Acknowledge use and scope, for example in the repository |

Disclosure goes in the Responsible NLP checklist, and checklist answers are not grounds for automatic desk rejection. Reviewers see them and may flag a paper for ethics review.

**Where this paper falls.** By the repository's own account (`AI_DISCLOSURE.md`), the AI produced "the research question and hypotheses, the pre-registration, all Python code ... and every sentence of the manuscript". That is the **discouraged "new ideas plus new text" tier**. It is not prohibited, and disclosure is compliant, but the authors carry the burden of arguing that the work is correct, original and well cited.

### Is the current wording honest and consistent?
**No, not yet.** There are four problems.

1. **The paper understates the AI's role compared with the repository.**

   | Item | Paper (L363) | `AI_DISCLOSURE.md` |
   |---|---|---|
   | Research question | "The author conceived the research question" | The AI did "the research question and hypotheses"; the author "proposed the topic" |

   A topic is not a research question. Any reviewer who opens the repository will see a discrepancy that runs in the self-serving direction. This is the single most damaging issue in the disclosure, and it is easy to fix: make the paper match the more complete account.
2. **"Verified the citations and results" is stated in the past tense, but the record says it has not happened.** All boxes in `lit/CITATIONS.md` are unticked, and the pre-registration is still "DRAFT ... verified by the author". Either do the verification before submission and keep the sentence, or do not claim it. If it was done, say what it involved and what it found (for example, "N of 37 citations were corrected").
3. **"Approved every decision with external effect" is vague and reads as a minimisation.** It sounds as though the human approved downloads, not scientific choices. State concretely which scientific decisions the human made or approved: which hypotheses, the post-hoc frontier-model addition, the analysis plan.
4. **The dual role of the AI is not disclosed.** The same system (Claude Opus 5.5) that drafted the paper also generated one of the LLM text sources (the "2026 frontier model"). Its inclusion changed a headline trend, and the self-test scores that system's own prose. This is a methodological dependency and must be stated in §4 and in the AI-use section. Also give the model version and interface ("Claude Opus 5.5 via Claude Code"), because the policy asks for scope and nature.

### Anonymity
"the public repository" (L366) is a deanonymisation path. Use an anonymised link. Also scrub the `Co-Authored-By` trailers and author names from the anonymised copy, or refer only to "supplementary material".

### Likely reviewer reactions
- **Negative or skeptical (expect at least one of three reviewers).**
  - "ACL discourages exactly this."
  - "Who is accountable for the analysis choices?"
  - "Did a human check these 2026 citations?"
  - "An AI-written paper about AI-sounding text is a stunt."
  Some reviewers will lower scores on principle. The AC should instruct reviewers to judge the work on its merits and treat the disclosure as compliant. Ethics flagging is moderately likely.
- **Positive (a minority, more on this theme track).** These reviewers will value the audit trail (labelled commits, auto-inserted numbers) and see the paper as a meta-scientific data point.
- **The swing factor is the quality of execution.** With a TODO appendix, inconsistent generator counts and unticked citations, the disclosure turns into "the AI made mistakes and the human did not catch them". With those fixed, the disclosure becomes a strength.

### Recommendations
- Keep the disclosure and make it more precise, not shorter.
- Remove "a self-test" from the main text, or move it to an appendix (see the L328-333 edits). It foregrounds AI authorship while making an invalid inference, which is the worst combination.
- Do not argue in the paper that AI authorship is desirable. One factual sentence on why it was done is enough; the repository can hold the longer rationale.
- Answer the checklist AI question with the same content.

**Proposed replacement for L361-367:**

> **AI Use and Authorship.** An AI system (Claude Opus 5.5, Anthropic, used as an agent through Claude Code) carried out most of this study. The human author(s) chose the topic, the goal of a fully disclosed AI-conducted study, and the constraints (public data only, no human participants, local compute), and approved the pre-registration and every deviation from it. The AI system proposed the specific research question and hypotheses, searched the literature, wrote all code, generated the local-model texts, ran the analyses, made the figures, and drafted all text. The same AI system also generated the "2026 frontier model" abstracts used in §4, so its own outputs are part of the LLM reference set. The human author(s) checked every citation against its source [state outcome, e.g. "correcting N of 37 entries"] and every reported number against the analysis outputs, and take full responsibility for the content. Every number in the paper is inserted automatically from the analysis outputs. AI-written and human-edited changes are labelled separately in the version history, available in anonymised form at [anonymised link]. No AI system is listed as an author, in line with ACL policy.

---

## 3. Line-level edits

Format: **L# (section)**, then the original text, the problem, and the fix.

### Title and abstract
- **L17**
  - Original: "Sounding Like AI Before AI: Machine-Style Overlap in Human Writing"
  - Problem: Catchy, but it puts the weakest and most construct-dependent result (the baseline) in the headline and leaves out the strongest one (the post-2022 shift and the marker-versus-style divergence).
  - Fix: see §4.
- **L25**
  - Original: "Corpus studies of large language models (LLMs) ask how much text was written with LLM help."
  - Problem: These are studies of LLM *use*, not of LLMs.
  - Fix: "Corpus studies of LLM-assisted writing estimate how much text was produced with large language model (LLM) help."
- **L29-30**
  - Original: "For pre-LLM text, MSO is the human half of a Bayes error, so the 'false positives' that prevalence studies subtract are a population property."
  - Problem: Jargon-dense, and it overclaims. The result holds only for a fixed feature map and generator set, and prevalence studies use other feature maps.
  - Fix: "For pre-ChatGPT text, MSO is the false-positive rate of an optimal classifier: a property of the two text distributions under a fixed feature set, not estimator noise."
- **L32-33**
  - Original: "After November 2022, MSO rose 22.5 points above its pre-2022 trend"
  - Problem: No date, the unit is ambiguous, and the "pre-2022" trend actually includes January-November 2022.
  - Fix: "By June 2025, arXiv MSO was 22.5 percentage points above its pre-ChatGPT trend (95% CI 20.7-24.4) and reached about 40% in 2026."
- **L34**
  - Original: "versus 1.4 points in parliamentary speech"
  - Fix: "versus 1.4 points (CI -0.2 to 3.1) in Australian parliamentary speech"
- **L35-36**
  - Original: "Marker words such as *delve* rose and then fell back towards baseline, while MSO stayed high."
  - Fix: "The share of abstracts with marker words such as *delve* peaked in 2024 and fell back almost to its trend, while MSO did not fall."
- **L36-37**
  - Original: "Among pre-LLM student essays, English-language learners are *less* machine-like than their peers, the opposite of the bias reported for perplexity-based detectors."
  - Problem: Overstated given the 3/10 significance, and it hides that this contradicts the authors' own pre-registered hypothesis.
  - Fix: "Contrary to our pre-registered hypothesis, essays by English-language learners lie further from the LLM region than their peers' essays (on a continuous score; the thresholded difference is not robust), unlike the bias reported for perplexity-based detectors."
- **L37-38**
  - Original: "Whether text 'sounds like AI' depends on the instrument asking, and for scientific prose the answer has changed more than word counts suggest."
  - Problem: An aphoristic closer with personification ("the instrument asking"). "Word counts" is ambiguous; it means marker-word counts. This reads as AI-generated.
  - Fix: "Marker-word counts therefore understate how far the style of scientific abstracts has moved toward LLM output."

### Introduction
- **L43**
  - Original: "Two findings about writing since November 2022 sit uneasily together."
  - Problem: The paragraph then lists three findings, and they are not in tension: corpus-level detectability and document-level undetectability are compatible.
  - Fix: "LLM influence on writing is easy to detect in aggregate but hard to detect in individual documents."
- **L50**
  - Original: "The boundary between human and machine writing appears thin, but existing work does not say how thin, for which kinds of writing, or since when."
  - Problem: An acceptable sentence, but the rhetorical triad reads as filler.
  - Fix: "No existing measure says how much human writing falls on the machine side of that boundary, in which genres, or since when."
- **L54**
  - Original: "The two diverge in an informative place."
  - Problem: Vague.
  - Fix: "The two questions read one number differently: the small 'LLM share' that prevalence estimators report for text written before ChatGPT."
- **L55-56**
  - Original: "treat it as estimator error \citep{liang2024mapping, lin2025, brooks2024}"
  - Problem: Verify that each of the three papers says this. Misattribution here is high-risk.
- **L57**
  - Original: "Under a fixed feature map it is a property of the two text populations"
  - Fix: "For a fixed feature map and a fixed set of reference generators, it is a property of the two text populations"
- **L58**
  - Original: "before AI could write"
  - Problem: Inaccurate, since GPT-2 and GPT-3 are in the data.
  - Fix: "before ChatGPT"
- **L62-63**
  - Original: "a broad set of open-weight and commercial generators"
  - Problem: Overclaims, and it conflicts with Limitations ("mostly mid-sized").
  - Fix: "five local open-weight models, six RAID generators including GPT-4 and ChatGPT, and one 2026 frontier model"
- **L64**
  - Original: "varying more than threefold across scientific fields"
  - Problem: Fine, but this is the econ (n = 1,256) to astro-ph comparison.
  - Fix: add "(4.7% to 16.2%)".
- **L65-66**
  - Original: "with a field-level dose pattern, placebo breaks and a parliamentary-speech control"
  - Problem: "Dose pattern" is epidemiology jargon.
  - Fix: "larger in fields with higher reported LLM adoption, absent at placebo dates, and much smaller in parliamentary speech"
- **L66-69**
  - Problem: Contribution (4) has no section reference, uses the superlative "the *least* machine-like" for a comparison between two groups, and omits the frontier-model and chat-tuning findings.
  - Fix: "...English-language learners, scores *less* machine-like than other students (§6.6)." Add (5): "We show that region definitions built only from older generators miss most text from a current model (§6.3)."
- **General.** "H1-H5" are used as section tags (L218, L236, L277) but never defined.
  - Fix: add one sentence at the end of the Introduction: "We pre-registered five hypotheses (H1 baseline > 0 and field-dependent; H2 post-ChatGPT excess; H3 excess larger than in a control genre; H4 larger in CS than math; H5 higher MSO for learners) [anonymised link]." Or drop the tags.

### Related work
- **L79-80**
  - Original: "\citet{chang2026}, who analyse a decade of convergence between human writing and machine patterns"
  - Problem: Restates the cited title and says nothing about how this paper differs.
  - Fix: "\citet{chang2026}, who measure convergence through language-model predictability" (verify this description), then say how MSO differs.
- **L82**
  - Original: "and in excluding content words entirely"
  - Problem: True, but the feature set includes dash typography, which acts like a marker.
  - Fix: add "(though punctuation, including dashes, is retained; §5)".
- **L90-91**
  - Original: "If LLM style partly reflects preferences that human raters already held, some pre-LLM human writing should already sit inside the LLM region, which is what MSO measures."
  - Problem: Faulty logic. Any two overlapping distributions give a non-zero MSO, whatever the raters' preferences, so a non-zero baseline does not test this mechanism.
  - Fix: "MSO quantifies how much pre-LLM human writing already shares that style. A non-zero value is necessary for, but not evidence of, the preference-amplification account."

### §3 Machine-Style Overlap
- **L110-112, notation.** $H_0$ for a distribution collides with null-hypothesis notation and with the H1-H5 labels.
  - Fix: use $P_{\text{pre}}$ (or $\mathcal{H}$) and $P_{\text{LLM}}$.
- **L112 and throughout, terminology drift.** The paper uses "pre-LLM", "pre-ChatGPT", "pre-2022", "pre-cutoff", "before 30 November 2022" and "a break at December 2022" interchangeably. "Pre-2022 trend" is literally wrong, because the trend includes 2022.
  - Fix: define "pre-ChatGPT (before 30 Nov 2022)" once and use it everywhere, including the figure legends ("pre-2022 trend, extrapolated" becomes "pre-ChatGPT trend").
- **L113**
  - Original: "a mixture over generators and prompting styles with equal weights"
  - Fix: add "chosen by us; MSO is defined relative to this reference set".
- **L123-125**
  - Original: "zero only if human and LLM styles are perfectly separable, and rising towards ½ as the distributions coincide"
  - Problem: Mathematically wrong in two ways.
    1. MSO(H0) can be 0 without perfect separability. Example: H0 = U[0,1] and L = U[0,2], so that p_L < p_H0 on all of H0's support.
    2. With the ≥ rule, identical distributions give η = ½ everywhere, so MSO(H0) = 1, not ½.

    Only the Bayes error is bounded by ½.
  - Fix: "The Bayes error is zero only if the two styles are perfectly separable and reaches ½ when they coincide; the baseline is its human-side component."
- **L125-126**
  - Original: "Prevalence studies that subtract a pre-period share as 'misclassification' remove exactly this quantity."
  - Fix: "...remove the analogue of this quantity under their own feature map."
- **L135-136**
  - Original: "treat their spread as part of the uncertainty"
  - Problem: The reported CIs (e.g., 9.1-9.6) appear to be document-level bootstrap intervals only, so they do not include this spread.
  - Fix: say what the CIs include, and report the cross-instrument and LOMO range separately (LOMO MSO is 18.6-22.7%).

### §4 Data
- **L142**
  - Original: "a stratified random sample drawn through the arXiv API: for each of 8 fields"
  - Problem: Two colons in one sentence.
  - Fix: "a stratified random sample from the arXiv API. For each of 8 fields..."
- **L145-146**
  - Original: "(5,400 pre-ChatGPT abstracts per class enter training; 159,102 abstracts in total)"
  - Problem: "Per class" is unclear. Where the 5,400 LLM texts come from is also unclear, as is the relation to "half of the pre-cutoff documents".
  - Fix: "The classifier is trained on 5,400 human abstracts (drawn from the train pool) and 5,400 LLM abstracts; all other abstracts (N = ...) are scored."
- **L149**
  - Original: "Spoken parliamentary speech is our less-exposed control genre."
  - Problem: Hansard is an *edited* transcript produced by parliamentary reporters. That needs a sentence, because reporters may or may not use LLM tools.
  - Fix: add "Hansard is lightly edited by parliamentary reporters; we treat it as less exposed, not unexposed."
- **L150-151**
  - Problem: ELL students in US grades 6-12 are not the TOEFL population of Liang et al. (2023).
  - Fix: make this explicit here, not only in §6.7.
- **L152**
  - Original: "In every genre half of the pre-cutoff documents"
  - Fix: "In every genre, half of the pre-ChatGPT documents"
- **L156-157**
  - Original: "Seven open-weight models ... (..., Phi-4 14B, Granite 3.3 8B ...)"
  - Problem: **Factually inconsistent with every result file**, which contain five local models.
  - Fix: "Five open-weight models (Llama 3.1 8B, Qwen3 8B, Gemma 3 12B, Mistral 7B, gpt-oss 20B)", or rerun with all seven.
- **L159-160**
  - Original: "the instruction a writer evading detection would give"
  - Fix: "a plausible evasion instruction"
- **L161**
  - Original: "the unattacked generations in RAID"
  - Problem: Jargon.
  - Fix: "RAID generations without adversarial attacks"
- **L162**
  - Original: "abstracts from a 2026 frontier model (Claude) answering the same prompt instances"
  - Fix: "...(Claude Opus 5.5, the same system that drafted this paper; no control over decoding) answering the same prompt instances."

### §5 Method
- **L171-172**
  - Original: "curly quotes, non-breaking hyphens and non-breaking spaces are mapped to ASCII"
  - Problem: Say that em and en dashes are deliberately kept, and justify that choice, because they are among the strongest features.
- **L172-173**
  - Original: "Without this step formatting artefacts alone separate LLM output from human text."
  - Problem: An unsupported assertion.
  - Fix: give the AUC without cleaning.
- **L175**
  - Original: "Features are deliberately topic-robust"
  - Problem: Function words, PROPN trigrams and "we" are not topic-free.
  - Fix: "Features exclude content words to reduce topic sensitivity"
- **L182 and throughout ("instrument")**
  - Problem: "Instrument", "primary instrument", "abstract instrument" and "the style instrument" are never defined. In econometrics the word means an instrumental variable.
  - Fix: define it once ("we call a trained, calibrated classifier with its 0.5 threshold an *instrument*") or say "classifier" throughout.
- **L188-190**
  - Original: "segmented regression with a level shift and a slope change ... Newey-West errors (6 lags)"
  - Fix: add "(an interrupted time-series design)" and "(standard errors robust to autocorrelation)" for a general NLP reader.
- **L190-192**
  - Original: "The pre-registered quantity is the *excess*: ... at June 2025, the last month covered by both treatment and control."
  - Problem: Three issues.
    1. The pre-registration does not name June 2025.
    2. Hansard has no data for April-June 2025 but does have July 2025.
    3. "Excess" collides with "excess-vocabulary" (L74, Kobak et al.), and "treatment" is jargon.
  - Fix: "Our primary quantity is the *trend gap*: the difference between the fitted post-ChatGPT series and the extrapolated pre-ChatGPT trend, evaluated at June 2025 (chosen because ...; Hansard has no sittings April-June 2025)." Rename "excess" everywhere, including the Fig. 2 axis.
- **L193-196, marker list.** Eight marker words is a very small list compared with Kobak et al.'s hundreds, and the peak marker share of about 5.4% is low.
  - Fix: justify the list, or add a robustness check with a larger list.

### §6 Results
- **L211-213**
  - Original: "cross-validated AUC 0.934 for abstracts, 0.977 for speech, 0.987 for essays"
  - Fine. Add "(1 = perfect separation)" once for general readers.
- **L213-214**
  - Original: "the region generalises to generators it never saw (recall on held-out generators in Appendix~\ref{app:lomo})"
  - Problem: Contradicted by the LOMO results, and the appendix is a TODO.
  - Fix: "Recall on a held-out generator ranges from 63-95% for older generators but is only 21% for the 2026 model (Table X)."
- **L214-215**
  - Original: "The hardest case everywhere is LLM revision of a human draft (P2)"
  - Fix: give numbers, e.g. "(AUC 0.69-0.94 for P2 vs 0.84-0.99 for P1)".
- **L221**
  - Original: "as did 3.7% of parliamentary speeches and 3.2% of student essays"
  - Fix: add CIs (3.2-4.2; 2.8-3.6), as was done for arXiv.
- **L224-225**
  - Original: "Estimator noise would be uniform across fields; this structure is what a property of the writing predicts."
  - Problem: A false dichotomy and an overclaim.
  - Fix: "Field differences are far larger than sampling error. They are what a property of the writing predicts, though they could also reflect classifier fit that varies by field."
- **L226**
  - Original: "It was also rising slowly before ChatGPT"
  - Problem: Ambiguous antecedent.
  - Fix: "Overall arXiv MSO was also rising slowly before ChatGPT"
- **L237**
  - Original: "Yearly arXiv MSO was 8.4% in 2018 and 10.7% in 2022"
  - Problem: Why 2018? It looks cherry-picked. The 2022 figure also includes post-ChatGPT December.
  - Fix: "Yearly arXiv MSO was 8.2-10.2% in 2015-2021 and 10.7% in 2022, then..."
- **L245, CI formatting.**
  - Original: "CI -0.2–3.1"
  - Problem: A negative bound followed by an en dash is unreadable, and the format is inconsistent with "-0.32 to -0.29" at L286-287.
  - Fix: use "−0.2 to 3.1" (math minus) everywhere. The `\R{}` macro outputs ASCII hyphens; wrap negatives as `$\R{...}$`.
- **L244**
  - Original: "Parliamentary speech moved far less"
  - Fix: "Parliamentary speech did not move measurably"
- **L248**
  - Original: "*Dose.*"
  - Fix: "*Field gradient.*"
- **L251-252**
  - Original: "The rise continued into 2026 (40.7% through September)."
  - Problem: Monthly values peaked in May 2026 (43.5%) and were 37.7-39.5% in July-September.
  - Fix: "MSO stayed near 40% in 2026 (January-September mean 40.7%)."
- **L254**
  - Original: "**The region must include current models.**"
  - Problem: Prescriptive heading for what is a post-hoc sensitivity result.
  - Fix: "**Sensitivity to the generator set.**"
- **L257-258**
  - Original: "In a preliminary run without the frontier model, arXiv MSO appeared to fall in 2026; with it, the rise continues."
  - Problem: This admits a result-contingent analysis change and conflicts with the deviation log.
  - Fix: "We added the 2026 model after a run without it [state when, and that this deviates from the plan]. Without it, 2026 MSO is X%; with it, Y%. We report both (Table Z)."
- **L258-259**
  - Original: "Newer models no longer sound like 'classic' LLM text, so an overlap measure defined only by older models will understate recent movement."
  - Problem: Generalises from one model.
  - Fix: "At least one current model writes outside the region defined by older generators, so a region built only from older models may understate recent movement."
- **L265**
  - Original: "MSO remained far above trend."
  - Fix: "MSO remained 22.5 points above trend."
- **L267**
  - Original: "only 5.7% of in-region abstracts contain a marker word"
  - Problem: Meaningless without a base rate.
  - Fix: add "(vs X% of out-of-region abstracts)".
- **L268**
  - Original: "lexical counts capture the visible tip of a broader stylistic shift"
  - Problem: The iceberg metaphor implies nesting, but r = 0.11 means the two measures are nearly independent.
  - Fix: "marker words and MSO capture largely different documents."
- **L270, heading.**
  - Original: "Chat tuning makes the style"
  - Fix: "Chat tuning amplifies the style"
- **L271-273**
  - Problem: Cherry-picks GPT-2 and base Mistral.
  - Fix: report all three base/chat pairs: Mistral 23.8→86.9%, MPT 56.2→96.0%, Cohere 39.8→73.0%. Note that base models already exceed the 9.4% human baseline.
- **L273-275**
  - Original: "What humans hear as 'sounding like AI' is largely a product of instruction and preference tuning"
  - Problem: No human judgements were collected (L104-105).
  - Fix: "The style our classifier associates with LLMs is strongly amplified by instruction and preference tuning"
- **L277, heading.**
  - Original: "Learners are the least machine-like writers (H5)"
  - Fix: "Learner essays are less machine-like (contrary to H5)"
- **L280-281**
  - Original: "Because few learner essays cross the threshold"
  - Fix: "Because only 8 of 666 learner essays cross the threshold"
- **L281-284**
  - Original: "(100.0% of draws)" and "in only 30.0% of draws"
  - Fix: "in all 10 draws" and "in only 3 of 10 draws"
- **L285**
  - Original: "gives a clear answer"
  - Problem: Rhetorical.
  - Fix: "shows a consistent difference". Also state that the margin comes from an *uncalibrated* logistic model trained separately, and that SD means the raw SD of the margin. The CI (-0.32 to -0.29, n_ELL = 666) is narrow enough that readers will suspect an error unless you say that prompt fixed effects absorb most of the variance.
- **L287-288**
  - Original: "A different instrument built on sentence embeddings agrees (4.7% vs 7.9%)."
  - Problem: The embedding model and classifier are never described in §5.
  - Fix: define them in §5 and add CIs here.
- **L289-291**
  - Original: "the style region is defined by richer vocabulary, longer words and more uniform sentences, which learners use less"
  - Problem: "More uniform sentences" is not among the top features, and the em dash, the second-strongest feature, is left out.
  - Fix: cite the feature table: "higher lexical diversity (MTLD), em dashes and longer words".
- **L291**
  - Original: "The same text can be 'AI-like' to one instrument and 'human-like' to another."
  - Problem: No perplexity detector was run on these essays, so this is inferred across datasets.
  - Fix: run a perplexity baseline on PERSUADE, or write "Our style-based result and published perplexity-based results point in opposite directions for learner writing."
- **L302-303**
  - Original: "(21.5% vs 21.0% for abstracts)"
  - Problem: Which population is this? It is not the 9.4% baseline (apparently all scored abstracts, 2015-2026).
  - Fix: "(21.5% vs 21.0% over all scored abstracts, 2015-2026)"
- **L307**
  - Original: "near chance"
  - Problem: 34.1% is not near chance, and "chance" is undefined.
  - Fix: "...places 34.1% of TOEFL and 51.4% of US college essays in the region, several times the in-genre baseline of 3.2%, so the region does not transfer across genres. (The TOEFL < college ordering matches the learner result.)"
- **L307-308**
  - Original: "Population-level overlap is stable"
  - Fix: "Population-level MSO varies little across classifier families (21.0-21.5%) and held-out-generator regions (18.6-22.7%)". Those LOMO numbers support the claim, so use them.

### §7 Discussion
- **L313**
  - Original: "Three results jointly reframe the perception that everything now sounds like AI."
  - Problem: Strawman ("everything"), and it is the kind of sentence an AI writes.
  - Fix: "Three results bear on the common impression that writing increasingly sounds like AI."
- **L315**
  - Original: "formal, noun-heavy registers were closest to what instruction-tuned models produce"
  - Problem: Not shown anywhere in the paper.
  - Fix: support it with the feature table, or cut it.
- **L316-317**
  - Original: "while parliamentary speech did not, so the perception reflects a real change in some writing, not only heightened suspicion"
  - Problem: Perception was not measured.
  - Fix: "while parliamentary speech did not measurably move, so at least part of the change is in the writing itself."
- **L318**
  - Original: "the style region is created by chat tuning rather than by language modelling as such"
  - Fix: "chat tuning strongly amplifies the style region, though base models already lie partly inside it"
- **L322-326**
  - Problem: Two explanations for the marker decline (authors editing markers out, and newer models not producing them) are given in separate sentences without being compared.
  - Fix: present them together, and say the data cannot distinguish them.
- **L324**
  - Original: "may therefore understate continued LLM influence"
  - Problem: Conflicts with L130-131 (MSO is authorship-agnostic).
  - Fix: "may understate how far writing style has continued to move toward LLM output"
- **L328-333 (self-test)**
  - Problems, five in all:
    1. n = 29 paragraphs, so the 95% CI is roughly ±15 points.
    2. 20.7% is essentially the held-out recall for the same model (20.9%). This is the frontier-model result again, not new evidence.
    3. `latex_paragraphs()` scores LaTeX source in which dashes stay ASCII `--`, while the em dash is a top LLM feature. The paper's prose also contains no em dashes. The test is mechanically biased toward "human".
    4. The conclusion "most 2026 computer-science abstracts read as more machine-like than an AI-drafted paper about them" does not follow. A 59.1% in-region share is not a pairwise comparison, and the paper is not "about" CS abstracts.
    5. The pre-registration specifies cs.CL, but the paper uses all of cs.
  - Fix: move it to an appendix as "illustrative, n = 29", or cut it. If kept: "Scored by the abstract classifier, 6 of 29 prose paragraphs of this AI-drafted paper (21%) fall in the LLM region, matching the 21% recall for held-out text from the same model (§6.3)."
- **L339**
  - Original: "Our results show the human side of such a loop moving in one genre"
  - Problem: The paper cannot separate human adoption from LLM use (L130-131).
  - Fix: "Our results are consistent with the human-written side of such a loop moving in one genre"
- **L341-344.** Good. Soften "stable across instruments" to "similar across two classifier families".
- **Missing Conclusion.** Add 3-4 lines restating the estimand, the 9.4% to about 40% shift, the marker divergence, and the caution about individual judgements.
- **Missing theme link.** Add one paragraph or one analysis on homogenization proper, such as the yearly dispersion of abstracts in feature space.

### Limitations, Ethics, AI use
- **L347-353, additions to Limitations.**
  1. Punctuation, including dash typography, is among the strongest features.
  2. MSO is defined relative to a researcher-chosen generator mix; adding one model changed the 2026 trend.
  3. Compositional and topic change in arXiv (especially CS) may contribute to the shift.
  4. English only, abstracts truncated to 250 words.
  5. One generator is the system that drafted this paper.
  6. The pre-registration was self-hosted, not on a third-party registry.
- **L352**
  - Original: "rests on few in-region learner essays"
  - Fix: "rests on 8 in-region learner essays"
- **L357**
  - Original: "RAID and the \citealp{liang2023detectors} data, MIT"
  - Problem: Renders as "the Liang et al., 2023 data", which is awkward.
  - Fix: "RAID and the data of \citet{liang2023detectors}, MIT". Also note that the CC BY-NC-SA ShareAlike terms apply to any derived PERSUADE data you release.
- **L362-367.** Replace as proposed in §2.
- **L374.** Fill in Appendix A (LOMO table for all three genres) or remove the reference. Never submit with `\TODO` defined to print red.

### Patterns that read as AI-generated
- Aphoristic closers: L37-38 ("depends on the instrument asking"), L268 ("visible tip"), L308 ("bears directly on"), L326 ("itself a moving target").
- Framing devices: "Two findings ... sit uneasily together" (L43), "The two diverge in an informative place" (L54), "Three results jointly reframe" (L313).
- Bold, prescriptive paragraph heads ("The region must include current models").
- Superlatives on two-group comparisons ("least machine-like").

These are individually minor. Together, and given the disclosure, reviewers will read them as evidence that no human edited the prose. A human editing pass (logged as `HUMAN-EDIT:` commits) is the cheapest credibility gain available.

---

## 4. Title and takeaway suggestions

**Titles (best first):**
1. *After the Delve Fades: Scientific Abstracts Keep Converging on LLM Style* (headlines the strongest and most theme-relevant finding)
2. *Machine-Style Overlap: How Much Human Writing Falls in the LLM Style Region, 2015-2026* (neutral, descriptive, safe for main track)
3. *Did Human Writing Sound Like AI Before AI? Machine-Style Overlap in arXiv, Parliament and Student Essays* (keeps the current hook, and the question form hedges the construct-dependent baseline claim)
4. *Homogenization from the Human Side: Measuring Convergence of Human Writing toward LLM Style* (maximises theme-track fit; only use if a dispersion analysis is added)

**One-sentence takeaway (current abstract has none that is crisp):**
> Measured with function-word and syntax features instead of marker words, the share of arXiv abstracts that a classifier places on the LLM side rose from about 10% before ChatGPT to about 40% in 2026, while marker words like *delve* returned almost to trend and parliamentary speech barely moved.

**Shorter version (for the end of the Introduction or a talk slide):**
> Marker words came and went; the LLM-like style of scientific abstracts did not.
