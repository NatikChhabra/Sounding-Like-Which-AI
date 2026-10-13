# AI use and authorship

This file and the paper's "AI Use and Authorship" section say the same thing; if they ever differ, the paper's
section is authoritative and this file is out of date.

## What the human author did
- Chose the topic (why so much writing "sounds like AI") and the goal of a fully disclosed, AI-conducted study.
- Set the constraints: public data only, no human participants, no budget, local hardware.
- Approved the analysis plan, its deviations, every download and every public action, in the working
  conversation with the AI system (these approvals are not separate commits).
- Takes full responsibility for the content, including the citations and the analysis choices.
- Citation spot-check: the author **has not yet** checked the random sample of five citations in
  `lit/SPOT_CHECK.md`. This line will be changed, in a `HUMAN-EDIT:` commit, only after the check is done.

## What the AI system did
The AI system is Claude Opus 5.5 (Anthropic), used as an agent through Claude Code on the author's computer. It:
- proposed the specific research question, the term "Machine-Style Overlap" and the five hypotheses, and wrote
  the analysis plan (`preregistration.md`);
- searched the literature, wrote all code, collected the public data and generated the local-model texts;
- produced the "2026 model" texts through separate sub-agent sessions (50 prompts per session, no decoding
  control), so its own outputs are part of the LLM reference set (the paper reports results with and without
  them);
- ran all analyses and made all figures;
- drafted every sentence of the paper; no human has edited the text so far (zero `HUMAN-EDIT:` commits);
- ran simulated peer review and citation verification in separate sessions **of the same model family**
  (`paper/reviews/`, `lit/verification/`), which share its blind spots, and revised the paper in response.
  Citation verification compared each claim with the cited work's abstract or full text where accessible;
  some publisher pages were blocked, and those sources were checked through metadata, institutional mirrors or
  secondary copies (details in `lit/verification/`). It led to 11 rewordings, 1 removed citation and 20
  preprints replaced by published versions.

## How to audit it
- The git history is the complete record. AI-written commits carry "(AI-written)" and a
  `Co-Authored-By: Claude` trailer; any human edit to AI-written text is a separate commit starting `HUMAN-EDIT:`.
- Every numerical result in the paper is inserted from `results/` by `code/make_numbers.py`; the PDF does not
  compile if one is missing. Design constants (sample sizes, caps, lags) and a few counts and orderings stated
  in words (read from the same result files) are typed.
- No AI system is listed as an author, in line with ACL and arXiv policy.
