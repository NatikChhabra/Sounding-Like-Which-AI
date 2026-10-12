# AI authorship and disclosure

**What the AI did.** This study was designed, coded, run and written by an AI system (Claude, by Anthropic,
model "Claude Opus 5.5"), operating as an agent in Claude Code on the author's computer, at the author's
request. This includes: the literature search (with web tools), the research question and hypotheses, the
pre-registration, all Python code, data collection from public sources, LLM text generation with local
open-weight models, the statistical analysis, the figures, and every sentence of the manuscript.

**What the human author did.** Natik Chhabra proposed the topic and the goal of an openly AI-written paper,
set the constraints (no human participants, $0 budget, local hardware), approved downloads and every
public action, and is accountable for the final content. Before submission the author checks every
citation against its source (`lit/CITATIONS.md`) and every reported number against `results/`.

**How to audit it.** The git history is the complete record. AI-written commits are labelled
"(AI-written)" and carry a `Co-Authored-By: Claude` trailer. Every human edit to AI-written text is a
separate commit whose message starts with `HUMAN-EDIT:`. Every number in the paper is inserted from
`results/` by `code/make_numbers.py`; the PDF does not compile if a number is missing.

**Why.** The paper studies how hard it has become to tell human from machine writing. Writing it with an AI,
and disclosing that fully, lets readers audit exactly what an AI-produced study looks like and where human
verification was needed. No AI system is listed as an author, in line with ACL and arXiv policy.
