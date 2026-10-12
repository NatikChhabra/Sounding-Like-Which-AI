# AI use and authorship

This file and the paper's "AI Use and Authorship" section say the same thing; if they ever differ, the paper's
section is authoritative and this file is out of date.

## What the human author did
- Chose the topic (why so much writing "sounds like AI") and the goal of a fully disclosed, AI-conducted study.
- Set the constraints: public data only, no human participants, no budget, local hardware.
- Approved the analysis plan, every deviation from it, every download and every public action.
- Checked a random sample of five citations against their sources (see `lit/SPOT_CHECK.md`) and is accountable
  for the final content.

## What the AI system did
The AI system is Claude Opus 5.5 (Anthropic), used as an agent through Claude Code on the author's computer. It:
- proposed the specific research question, the term "Machine-Style Overlap" and the five hypotheses, and wrote
  the analysis plan (`preregistration.md`);
- searched the literature, wrote all code, collected the public data and generated the local-model texts;
- produced the "2026 frontier model" texts through separate sub-agent sessions, so its own outputs are part of
  the LLM reference set (the paper reports results with and without them);
- ran all analyses and made all figures;
- drafted every sentence of the paper;
- ran simulated peer review (separate AI sessions; `paper/reviews/`) and citation verification (separate AI
  sessions; `lit/verification/`), and revised the paper in response.

## How to audit it
- The git history is the complete record. AI-written commits carry "(AI-written)" and a
  `Co-Authored-By: Claude` trailer; any human edit to AI-written text is a separate commit starting `HUMAN-EDIT:`.
- Every number in the paper is inserted from `results/` by `code/make_numbers.py`; the PDF does not compile if a
  number is missing.
- No AI system is listed as an author, in line with ACL and arXiv policy.
