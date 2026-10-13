# AI use and authorship

This file and the paper's "Acknowledgements: AI Use and Authorship" section say the same thing; if they ever differ, the paper's
section is authoritative and this file is out of date.

## What the human author did
- Chose the topic (why so much writing "sounds like AI") and the goal of a fully disclosed, AI-conducted study.
- Set the constraints: public data only, no human participants, no budget, local hardware.
- Approved the analysis plan; gave standing permission for downloads and setup; was told of the deviations,
  several of which the AI system made while working unattended under an instruction to continue; approved
  making the repository public. All of this happened in the working conversation, not in commits.
- Takes full responsibility for the content, including the citations and the analysis choices.
- Citations: delegated to the AI system (see below); the author has not checked citations. The author will read
  the final paper before release; this line will be updated, in a `HUMAN-EDIT:` commit, when that is done.

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
  Citation verification: every citing sentence was compared with the cited work's abstract or full text, in two
  full passes by separate sessions (`lit/verification/`, latest `v5_*.md`); some publisher pages were blocked and
  those sources were checked through metadata, institutional mirrors or secondary copies. This led to rewordings,
  one removed citation and published versions replacing preprints.

## How to audit it
- One early commit, `6675865` ("Strip BOM"), was made by the AI system but lacks the "(AI-written)" label and
  trailer; it only removed byte-order marks and regenerated `results/numbers.tex`.
- The git history is the complete record of changes to the files (not of the author's instructions, which stayed
  in the conversation). AI-written commits carry "(AI-written)" and a
  `Co-Authored-By: Claude` trailer; any human edit to AI-written text is a separate commit starting `HUMAN-EDIT:`.
- The public history was rewritten once (2026-10-13, approved by the author) to remove the LLM revisions of
  Hansard speeches, which had been released in two earlier commits, and a local Windows username in file paths.
  The rewrite used `git filter-repo` and changed nothing else; the commit ids cited in the paper are unchanged.
- Every numerical result in the paper is inserted from `results/` by `code/make_numbers.py`; the PDF does not
  compile if one is missing. Design constants (sample sizes, caps, lags) and a few counts and orderings stated
  in words (read from the same result files) are typed.
- No AI system is listed as an author, in line with ACL and arXiv policy.
