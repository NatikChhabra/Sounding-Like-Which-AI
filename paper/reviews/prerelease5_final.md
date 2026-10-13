# Pre-release check 5: final zero-defect pass

Commit c63ada2. I edited no project file except this report and pushed nothing. Clone, logs and scripts are in the session scratchpad.

**Counts: Blocking 0 · Important 1 · Minor 5**

---

## Blocking

None.

---

## Important

### I1. Appendix A(3) misstates when the 2026-model texts were merged (raised in round 3, still open)
`main.tex` l. 493 says: "The 2026 model's texts were merged two minutes after a preliminary arXiv run without them was committed". Git shows otherwise:

| Commit | Time | Content |
|---|---|---|
| f586d6c | 15:35:31 | preliminary arXiv run (5 local models + RAID) |
| c11d3ce | 15:37:49 | 2026-model **prompt batches** (`claude_prompts.py`, `run_queue2.ps1`) |
| 01ef90f | 15:44:42 | "Claude frontier **abstracts merged**" |

The prompt batches were committed two minutes after the preliminary run. The texts were merged nine minutes after it. `preregistration.md` deviation 7 already gives the correct account ("prompt batches were committed at 15:37 (c11d3ce), two minutes after"), so the paper contradicts both the plan and git. `round3_AC.md` N3 and item i flagged the same error.

Copy-ready replacement (main.tex l. 493):
```
The 2026 model's prompt batches were committed two minutes, and its texts merged nine minutes, after a preliminary arXiv run without them was committed;
```

---

## Minor

### M1. "No more than a quarter" is slightly too strong (6.5/25.4 = 25.6%)
- Intro, contribution (3), l. 70: "Placebo dates and instruments trained on earlier years give gaps no more than a quarter as large".
- §6.3, l. 313: "gaps of up to \R{robustness_v4.drift_to_2016.excess}\pp, a quarter of the observed gap".

Fixes:
```
l. 70:  ... give gaps at most about a quarter as large (\S\ref{sec:shift}).
l. 313: ... gaps of up to \R{robustness_v4.drift_to_2016.excess}\pp, about a quarter of the observed gap;
```

### M2. Abstract is at 199 of 200 words, and "all but the newest" cannot be checked
- Word count after substituting the `\R` values: 199, counting `$n=18$` as one token. A counter that reads the rendered PDF sees "n = 18" as three tokens and gets 201.
- "overlap with all but the newest rose and then fell" (abstract; README says "all but the newest rises and then turns down") assumes the 2026 model is the newest generator. Its release month is not public (§6.4, Fig. 4 caption), and Granite 4.2 was released in August 2026.

One edit fixes both and saves 3 words (abstract becomes 196):
```
Against single generators, overlap with most rose and then fell, peaking later for later generators (exploratory rank
correlation \R{arxiv_vintage_peak.rho}, $n=\R{arxiv_vintage_peak.n}$).
```
README, third bullet: "overlap with all but the newest rises and then turns down" → "overlap with every generator but the 2026 model rises and then turns down".

### M3. Fig. 4b: the "Qwen3.5 9B" label sits directly above the unlabelled green cluster
The label ends at the orange 2026Q1 point, but it also sits above the three green 2025Q4 points (Gemma 3, Granite 3.3, Qwen3), which readers could take as Qwen3.5. This is optional. In `code/figures.py`, move the Qwen3.5 annotation to the right of its point, or above-right of it, as is already done for Granite 4.2.

### M4. Do not upload the anonymous version's LaTeX source
`main.tex` l. 22–25 contains the name, affiliation, ORCID and repository URL inside the `\ifdefined\PREPRINT` branch. The anonymous PDF does not show them (see Verified, item 5), but the `.tex` file would. If a source or supplementary upload is ever made for review, strip that branch first.

### M5. PLAN.md status line
"- [ ] Five pre-release audit rounds" is still unchecked. Tick it once I1 is closed.

---

## Verified

**1. Reproducibility**
- I cloned c63ada2 into the scratchpad, linked the repo's `.venv` into the clone as a junction, and ran `powershell -ExecutionPolicy Bypass -File paper\build.ps1`. It reported `missing keys: []` and wrote all 5 figures and both PDFs.
- `tectonic` is not on PATH in this PowerShell session, so `build.ps1` used its fallback `F:\tools\tectonic\tectonic.exe` (Tectonic 0.17.0).
- `git status` in the clone was clean afterwards.
- SHA-256 against the committed blobs:
  - Byte-identical: `paper/preprint.pdf` and all five `paper/figures/*.pdf`.
  - `results/numbers.tex` matches once CR is stripped. It differs only by CRLF line endings from the `core.autocrlf=true` checkout (`i/lf w/crlf`), not in content.
  - The rebuilt `paper/main.pdf` (gitignored) is byte-identical to the working copy's `main.pdf` (sha256 prefix ed6924bf…).
- In `code/` of the clone, `python analysis.py F:/research-data vpeak` and `python analysis.py F:/research-data robust6` reproduced `results/arxiv_vintage_peak.json` and `results/robustness_v6.json` byte-for-byte after normalising line endings.

**2. Numbers written in words** (checked against `results/` or the raw data in `F:\research-data`)
- 131,448 abstracts; eight fields; dates run Jan 2015 – Sep 2026; minimum length 50 words.
- 19 generators: 14 in the main instrument plus 5 added for the vintage analysis. Four have pre-ChatGPT pretraining data and four were released in 2026. 16 + 3 = 19; seven local models plus the 2026 model for Hansard and essays.
- About 150 prompts per prompt style (Hansard has 141–158). Nine Claude batches of 50 cover the 450 arXiv prompts.
- 11,730 local texts = 3,150 (arXiv) + 3,150 (essays) + 3,180 (Hansard) + 2,250 (vintage models, all three prompts).
- Hansard: at most 150 speeches per month, Feb 2015 – Jul 2025. PERSUADE: 14 prompts once essays without ELL status are dropped.
- Pre-ChatGPT-data region: 900 of its 1,200 training texts come from RAID, so "three quarters" is correct. Three of its four generators are built on Llama 2.
- Placebo grid: 34 breaks, with 3/34 = 8.8% at p < 0.05. Drift horizons are 41–65 months. Yearly residuals stay within ±0.6 pp through 2022.
- Holm correction: the largest adjusted p is 1.9e-10 (econ). CS and q-bio have the largest field gaps; math and astrophysics the smallest.
- Without LaTeX math, astrophysics (5.8%) is still lowest and economics (15.9%) highest. The same holds after length reweighting.
- The feature-family ablation range (22.9–26.6) is correct. The yearly 2015–2021 range is 7.3 (2016) to 10.2 (2020).
- Peak quarters for all 19 generators match every grouped statement in §6.4. The bootstrap peak uncertainty is at most 2 quarters, or 5 for Cohere.
- "Rose 2022→2025 under every generator except Cohere" holds.
- 2025→2026: 15 of 19 fell; gpt-oss, Qwen3.5, Granite 4.2 and the 2026 model rose. In the 14-generator main set, 12 fell. Measured from 2025Q4, exactly those four rose. 18 generators fell from 2026Q2 to 2026Q3.
- All change intervals exclude zero and are stable over 5/5 seeds and 10/10 subsamples, except Gemma 4 (4/5, CI −1.8 to 0.1). In all three same-family pairs the newer model changed more, and the Gemma intervals overlap.
- Mined markers fell for 17 of 19 (Granite 4.2 and the 2026 model rose). Marker peaks came earlier than style peaks for 7 generators, later for 6 and in the same quarter for 5; I recounted these from the quarterly CSV.
- 2015 MSO: 17.9% for the 2026 model; the next highest is 8.3% (Cohere).
- Median-length ranges in Limitations (102–250, 90–134, 138–186) match `arxiv_generator_lengths.csv`.
- Fast-DetectGPT was scored on 600 abstracts per year. The dispersion check uses 1,200 abstracts per year at 150 words, and the full-length dispersion falls in every year. The −0.36 lower bound against −0.11 per year is about three years of trend.
- Essay seed stability: all 10 draws have the ELL odds ratio below 1 with p < 0.05.
- Design constants (C = 0.1, 1% feature threshold, 6 Newey–West lags, 12-month blocks, 80% subsamples, 450 cap, 250-word cut, June 2025 EVAL month) match the code.
- The "16 generators" count, the ten-row feature table and the "seven local models" are correct.
- Python 3.12.10 (`pyvenv.cfg`) and Ollama 0.40.3 (`ollama_serve.log`) are correct. Zenodo 17351233 is the Hansard record.
- README, .zenodo.json, CITATION.cff and PLAN.md ("131k abstracts", "12 local open models", "four rounds of simulated peer review", "8 pages + appendices") are all consistent with the results.

**`\R` macros**
- All 545 `\R{}` uses resolve: my resolver found 0 missing out of 11,591 keys, and `make_numbers.missing()` returned `[]`.
- I read every macro in context in a resolved copy of `main.tex`. About 130 I traced to the source JSON or CSV to confirm the key is the quantity the sentence claims. That covers all of the abstract, introduction, §6.3–6.5, Table 2 (robustness), Table 4 (held-out recall), Table 5 (peaks: peak, range, seeds and subsamples for all 19 rows), and the field, Hansard, dispersion and learner appendices.
- No mismatches. Two examples: `relative_gap` = 0.254/0.122 = 2.09, which is what "2.1 times the trend value" means; `field_holm.econ` is the largest Holm-adjusted p, so "all adjusted p < 0.001" holds.

**3. Cross-document consistency**
- Abstract, introduction, §6, Conclusion, README "Main findings" and the .zenodo.json description give the same numbers: 9.2%, 25.4 pp (23.2–27.7), 7.5 / 3.5 / 13.1 / 22.7 pp, ρ = 0.79 (n = 18; bootstrap 0.64–0.86; 0.66 without the 2026 open models), 22.2 and 17.9 pp, 2.3% vs 4.2%, and 63.7% vs 8.0%.
- Claim strength matches across documents, apart from M1 and M2. The pre-ChatGPT-data gap is called "smaller" everywhere. The peak ordering is called exploratory in the abstract, introduction, §6.4 and README. H5 is reported as not supported. No document contradicts another. The .zenodo.json description makes no quantitative claims.

**4. LaTeX hygiene** (`tectonic --keep-logs` into the scratchpad, for main and preprint)
- No undefined references or citations, no multiply-defined labels and no rerun requests.
- No overfull boxes, no missing characters, and no BibTeX warnings (both `.blg` files are clean).
- There are 63 underfull boxes, all cosmetic. They are mostly in bibliography URL lines; the worst in body text is badness 7832 in the "arXiv abstracts." paragraph.
- No Type 3 fonts, and all fonts are embedded.
- Page layout in `main.pdf`: the Conclusion heading and its full text are on page 8, and Limitations starts page 9.
- Abstract length: 199 words (see M2).

**5. Anonymity of `paper/main.pdf`**
- The author line reads "Anonymous ACL submission", and the Acknowledgements say "author(s)". The commit is given as "will be identified after review".
- The PDF Info dictionary has empty title and author fields, and there is no XMP metadata.
- Searching the text and every decompressed stream found none of: Chhabra, Natik, ORCID, 0009-0004, NatikChhabra, Bilaspur, ef4fa21, c63ada2, local paths, or the user or account names.
- All link annotations point to cited works; none points to the project repository. "GitHub" appears only in the Ethics licence note about Liang et al. and in reference URLs for FastChat and Llama 3.1.
- `main.pdf` is gitignored, so the anonymous version is never committed; it is built by `build.ps1`.
