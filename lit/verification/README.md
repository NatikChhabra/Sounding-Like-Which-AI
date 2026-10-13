# Citation verification reports

Separate AI sessions checked each citing sentence of the paper against the cited work (no human checked citations;
see `paper/AI_DISCLOSURE.md`).

- `batch1.md`–`batch5.md`: first full pass (paper v2).
- `batch6_v3.md`, `batch7_bib.md`: facts added for v3 (model cutoffs, RAID models, published versions) and the
  bibliography records.
- `v5_batch1.md`–`v5_batch3.md`, `v5_followup.md`: second full pass on the final text.
- `_v5_batch*_input.md`, `_v5_followup_input.md`: the exact inputs those sessions received (each cited key with
  every sentence that cites it), kept so the check can be audited.
