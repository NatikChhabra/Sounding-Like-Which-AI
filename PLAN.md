# Project status

**Paper:** "Sounding Like Which AI? Machine-Style Overlap of arXiv Abstracts with Language Models of Different
Vintages" (`paper/main.tex`). **Author:** Natik Chhabra. **Written and analysed by:** Claude Opus 5.5 (AI), fully
disclosed in `paper/AI_DISCLOSURE.md`. **Field:** computational linguistics. **Budget:** $0, one desktop PC.

## Rules kept throughout
- No human participants; public data only.
- Every number in the paper is computed by the code in `code/` and inserted from `results/`.
- Citations are resolved automatically from DOI/arXiv/venue records and checked against their sources by
  separate AI sessions (`lit/verification/`).
- AI writes all prose and code; any human edit is a separate git commit labelled `HUMAN-EDIT:`.
- Every change to the analysis plan is logged in `preregistration.md`.

## Done
- [x] Literature survey, term originality search, data and venue notes (`lit/01`-`04`)
- [x] Analysis plan committed before any result (`preregistration.md`)
- [x] Data: stratified arXiv sample (131k abstracts), Hansard, PERSUADE 2.0, RAID
- [x] Generations: 12 local open models, the 2026 model, RAID's 2023 models
- [x] Analyses (`code/analysis.py`) and figures; four rounds of simulated peer review (`paper/reviews/`)
- [x] Paper v5 (8 pages + appendices)
- [x] Full citation verification of every reference, two passes (`lit/verification/`)
- [x] Public repository with generated data, exact samples and pinned requirements
- [ ] Five pre-release audit rounds (`paper/reviews/prerelease_*.md`)

## Remaining (author only; see `paper/reviews/prerelease2_ethics.md`)
- [ ] Final read-through and critical revision by the author (edits as `HUMAN-EDIT:` commits); ACL authorship
      requires it
- [ ] Before any ACL/ARR submission or arXiv post: the author opens every reference and confirms it exists and
      supports its sentence (`lit/HUMAN_CITATION_CHECK.md`, `HUMAN-EDIT:` commit). ACL requires authors to confirm
      every source by hand and desk-rejected 2026 papers citing non-existent work; arXiv can ban authors for
      hallucinated references
- [ ] Then put the AI-use statements in the past tense (`main.tex`, `AI_DISCLOSURE.md`, README status), rebuild
- [ ] Release v1.0 on GitHub (Zenodo mints the DOI from `.zenodo.json`); set `date-released` in `CITATION.cff`
- [ ] Ask the EACL 2027 SRW chairs whether a secondary-school student may be first author (before 2026-11-06)
- [ ] EACL 2027 Student Research Workshop: pre-submission mentorship (deadline 2026-11-06)
- [ ] Submit: EACL 2027 SRW (2026-12-15) and/or ACL Rolling Review for ACL 2027 (2027-01-04; needs a complete
      OpenReview profile and a qualified "service contributor", or the paper enters a desk-rejection lottery)
