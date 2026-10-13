# prerelease2_style.md: applied changes

Target: `paper/main.tex`. README items #R1-#R5 are out of scope here and are handled separately.

## Applied verbatim (63)
#1-#14, #16-#42, #44-#59, #61-#68.
- #6 and #68 were marked optional. Both were applied because the page budget allowed it.
- #13 removes the duplicate `\ref{sec:dispersion}` and `\ref{sec:hansard}` from contribution (5). The `\label`s are unchanged.
- #29 was applied as two matches: the opening sentence, and the Granite 4.2 / 2026-model semicolon.
- #31: checked against `results/numbers.tex`. In all three same-family pairs the newer model's 2025-to-2026 change is higher: Qwen3 -3.7 vs Qwen3.5 +2.3, Gemma 3 -2.1 vs Gemma 4 -0.8, Granite 3.3 -2.7 vs Granite 4.2 +7.5. The same holds from 2025Q4. "change was higher" is therefore accurate.
- #40 includes the companion change at L121: "an anchor independent" became "a reference independent".
- #44 and #46 are two-part moves: Kusumegi moved to the first paragraph, and "we collect no human judgements" moved into the Readers sentence.

## Adapted (1)
- **#15 (Conclusion).** The proposed text adds a second `\R{arxiv_its.all.excess}`, which breaks the rule that the macro multiset must stay identical. I kept the restructuring, replaced "far beyond trend" with "well above its pre-ChatGPT trend" and added no macro. Everything else follows the report.

## Skipped (2)
- **#43.** The report says to leave it as is.
- **#60.** The tense change for "will read the final paper before release" waits until the human author has read the paper.

## Checks
- Multiset of `\R`, `\cite*` keys, `\ref` and `\label`: identical before and after, except the two duplicate refs that #13 removes (`ref:sec:dispersion`, `ref:sec:hansard`).
- Build: no error, Overfull or undefined lines.
- Page fit: in both main.pdf and preprint.pdf the Conclusion ends on page 8. Limitations now also starts on page 8, so page 9 opens partway through Limitations.
