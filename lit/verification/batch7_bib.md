# Batch 7: bibliography verification (references.bib)

Checked 2026-10-13. Sources: the OpenReview API (`api2.openreview.net/notes/search`), the COLM 2024 accepted-papers page, the arXiv API and abstract pages, the Crossref REST API, the Zenodo REST API and its BibTeX export, the ACL Anthology `.bib` files, and OpenAlex.
Semantic Scholar rate-limited almost every request (HTTP 429), and dblp.org could not be reached. Item 10 therefore uses Crossref, OpenAlex, OpenReview (which mirrors dblp records) and arXiv `journal_ref`/comments instead. I did not edit references.bib.

---

## 1. liang2024mapping: confirmed at COLM 2024

- OpenReview forum: **YX7QnhxESU** (venue `colmweb.org/COLM/2024/Conference`, published 2024-07-10).
- The COLM 2024 accepted-papers page lists it with the same 14 authors: https://colmweb.org/2024/AcceptedPapers.html
- The BibTeX below is the official OpenReview `_bibtex`, copied verbatim:

```bibtex
@inproceedings{liang2024mapping,
  title     = {Mapping the Increasing Use of {LLM}s in Scientific Papers},
  author    = {Weixin Liang and Yaohui Zhang and Zhengxuan Wu and Haley Lepp and Wenlong Ji and Xuandong Zhao and Hancheng Cao and Sheng Liu and Siyu He and Zhi Huang and Diyi Yang and Christopher Potts and Christopher D Manning and James Y. Zou},
  booktitle = {First Conference on Language Modeling},
  year      = {2024},
  url       = {https://openreview.net/forum?id=YX7QnhxESU}
}
```
Verified at https://openreview.net/forum?id=YX7QnhxESU (through the API) and the COLM listing.

## 2. gerstgrasser2024: confirmed at COLM 2024

- OpenReview forum: **5B2K4LRgmz** (COLM 2024 Conference, published 2024-07-10). The paper is also on the COLM 2024 accepted-papers page.
- **The author list differs from the current bib.** The COLM record has a different order (Korbak before Sleight, Hughes after Agrawal) and different name forms ("Dhruv Bhandarkar Pai", "Dan Roberts"). The entry below follows the official record.
- The BibTeX below is the official OpenReview `_bibtex`. Only the key was changed, back to the paper's key:

```bibtex
@inproceedings{gerstgrasser2024,
  title     = {Is Model Collapse Inevitable? {B}reaking the Curse of Recursion by Accumulating Real and Synthetic Data},
  author    = {Matthias Gerstgrasser and Rylan Schaeffer and Apratim Dey and Rafael Rafailov and Tomasz Korbak and Henry Sleight and Rajashree Agrawal and John Hughes and Dhruv Bhandarkar Pai and Andrey Gromov and Dan Roberts and Diyi Yang and David L. Donoho and Sanmi Koyejo},
  booktitle = {First Conference on Language Modeling},
  year      = {2024},
  url       = {https://openreview.net/forum?id=5B2K4LRgmz}
}
```
I added `{B}` to protect the capital (see item 9).

## 3. sadasivan2023: published in TMLR in 2025

- OpenReview forum: **OOgsAZdFOt**, "Accepted by TMLR", published 2025-01-23. The arXiv v4 comment also says "Published in Transactions on Machine Learning Research (TMLR)".
- The TMLR title adds a subtitle: "... Stress Testing AI Text Detectors Under Various Attacks".
- Earlier submissions to TMLR (1YYpg9tdVb) and ICLR 2024 (NvSwR4IvLO) were rejected. Cite only OOgsAZdFOt.
- The BibTeX below is the official OpenReview `_bibtex`. I changed the key, dropped the empty `note`, and protected the subtitle capital:

```bibtex
@article{sadasivan2023,
  title   = {Can {AI}-Generated Text be Reliably Detected? {S}tress Testing {AI} Text Detectors Under Various Attacks},
  author  = {Vinu Sankar Sadasivan and Aounon Kumar and Sriram Balasubramanian and Wenxiao Wang and Soheil Feizi},
  journal = {Transactions on Machine Learning Research},
  issn    = {2835-8856},
  year    = {2025},
  url     = {https://openreview.net/forum?id=OOgsAZdFOt}
}
```
The citation now renders as 2025, so you may want to rename the key to `sadasivan2025` and update the `\cite` calls.

## 4. doshi2024: verified against Crossref

Crossref (https://api.crossref.org/works/10.1126/sciadv.adn5290) gives:
- Science Advances, volume **10**, issue **28**, article number **eadn5290**, published 2024-07-12.

The current entry already has volume and number. Add `pages = {eadn5290}`; acl_natbib has no article-number field, so this is the usual workaround.

```bibtex
@article{doshi2024,
  title     = {Generative {AI} enhances individual creativity but reduces the collective diversity of novel content},
  author    = {Doshi, Anil R. and Hauser, Oliver P.},
  journal   = {Science Advances},
  volume    = {10},
  number    = {28},
  pages     = {eadn5290},
  year      = {2024},
  month     = jul,
  doi       = {10.1126/sciadv.adn5290},
  url       = {https://doi.org/10.1126/sciadv.adn5290}
}
```

## 5. katz2025hansard: Zenodo dataset

Zenodo record https://zenodo.org/records/17351233 (checked through the API and the `/export/bibtex` endpoint) gives:
- Creators: Katz, Lindsay (University of Toronto); Alexander, Rohan (University of Toronto)
- Title: "A new, comprehensive database of all proceedings of the Australian Parliamentary Debates (1998-2025)"
- Publication date 2025-10-14; resource type: Dataset; licence: CC-BY-4.0
- Version DOI 10.5281/zenodo.17351233; concept DOI (all versions) 10.5281/zenodo.7336075
- **The record has no `version` field.** I have not added one; nothing on the record supports it.

Zenodo's own export uses `@dataset`. acl_natbib.bst has no `@dataset` type, so BibTeX would warn and fall back to misc formatting. Use `@misc`:

```bibtex
@misc{katz2025hansard,
  author       = {Katz, Lindsay and Alexander, Rohan},
  title        = {A New, Comprehensive Database of All Proceedings of the {A}ustralian {P}arliamentary {D}ebates (1998--2025)},
  howpublished = {Dataset},
  publisher    = {Zenodo},
  year         = {2025},
  month        = oct,
  doi          = {10.5281/zenodo.17351233},
  url          = {https://doi.org/10.5281/zenodo.17351233}
}
```
- The source title is in sentence case with an ASCII hyphen. The title case and `--` above are typographic choices.
- To keep the exact source wording, use `{A new, comprehensive database of all proceedings of the {A}ustralian {P}arliamentary {D}ebates (1998-2025)}`.
- acl_natbib ignores `publisher` for `@misc`. If "Zenodo" must appear in the reference, use `howpublished = {Zenodo dataset}` instead.

## 6. katz2023scidata: exact title

Crossref (https://api.crossref.org/works/10.1038/s41597-023-02464-w) gives the title "Digitization of the Australian Parliamentary Debates, 1998–2022". The dash is U+2013 (en dash).
- Scientific Data, volume 10, issue 1, article number **567**, published 2023-08-26.

```bibtex
@article{katz2023scidata,
  title     = {Digitization of the {A}ustralian {P}arliamentary {D}ebates, 1998--2022},
  author    = {Katz, Lindsay and Alexander, Rohan},
  journal   = {Scientific Data},
  volume    = {10},
  number    = {1},
  pages     = {567},
  year      = {2023},
  month     = aug,
  doi       = {10.1038/s41597-023-02464-w},
  url       = {https://doi.org/10.1038/s41597-023-02464-w}
}
```
The current entry has `{Debates,} 1998–2022` (a raw Unicode en dash with an odd brace) and no article number.

## 7. kusumegi2026: confirmed in Science

- Crossref (https://api.crossref.org/works/10.1126/science.adw3000) gives:
  - Title: "Scientific production in the era of large language models"
  - Authors: Keigo Kusumegi, Xinyu Yang, Paul Ginsparg, Mathijs de Vaan, Toby Stuart, Yian Yin
  - Science, volume **390**, issue **6779**, pages **1240–1243**, published 2025-12-18
- arXiv 2601.13187 agrees: its `journal_ref` is "Science, 390(6779), pp.1240-1243 (2025)", its DOI field is 10.1126/science.adw3000, and its comment says the definitive version was published in Science on 18 Dec 2025.

```bibtex
@article{kusumegi2025,
  title   = {Scientific Production in the Era of Large Language Models},
  author  = {Kusumegi, Keigo and Yang, Xinyu and Ginsparg, Paul and de Vaan, Mathijs and Stuart, Toby and Yin, Yian},
  journal = {Science},
  volume  = {390},
  number  = {6779},
  pages   = {1240--1243},
  year    = {2025},
  month   = dec,
  doi     = {10.1126/science.adw3000},
  url     = {https://doi.org/10.1126/science.adw3000}
}
```
- The year is now 2025, so either rename the key and update the cites, or keep `kusumegi2026` as the key.
- The title follows Crossref's wording; capitalisation does not matter much because acl_natbib lowercases titles anyway.

## 8. yakura2024: still a preprint, as far as I can verify

- The bib has `year = {2026}` and `eprint = {2409.01754v4}`.
- arXiv submission history: v1 on 2024-09-03, v2 on 2025-06-30, v3 on 2025-07-08, v4 on 2026-07-16. **No version has a journal_ref, DOI or comment.**
- Crossref title search found no published version.
- OpenAlex lists only the arXiv preprint and the Zenodo data/model deposits.
- OpenReview/dblp lists only "CoRR 2024".
- **I found no published journal or conference record.** Semantic Scholar was rate-limited, and I could not run Google Scholar.

Suggested fix: keep `@misc`. Either keep v4 and `year = {2026}`, which is consistent if you cite v4 deliberately, or use the unversioned id:

```bibtex
@misc{yakura2024,
  title         = {Empirical Evidence of Large Language Model's Influence on Human Spoken Communication},
  author        = {Hiromu Yakura and Ezequiel Lopez-Lopez and Levin Brinkmann and Ignacio de la Serna and Lara Kirfel and Prateek Gupta and Ivan Soraperra and Thomas F. Eisenmann and Dirk U. Wulff and Iyad Rahwan},
  year          = {2024},
  eprint        = {2409.01754},
  archivePrefix = {arXiv},
  url           = {https://arxiv.org/abs/2409.01754}
}
```
- With `year = {2024}` and no version, the reference points to the latest version.
- With `year = {2026}`, keep the `v4` suffix in the eprint so the year matches.
- I did not re-check the author list for v4 against the arXiv page. Do that if you keep v4.

## 9. Title capitalisation fixes

Mechanism: acl_natbib.bst runs `"t" change.case$`, which lowercases everything outside braces. It spares only the first character and a character that follows ": " at brace level 0.
- After a **question mark**, an unbraced capital is lowercased.
- After a **colon inside braces** (for example `{RAID:}`), the closing brace resets the colon check, so the next word is lowercased too. This follows my reading of the bibtex.web source; I did not test it by compiling.

| key | problem (as rendered) | corrected title |
|---|---|---|
| gerstgrasser2024 | "? breaking" | `Is Model Collapse Inevitable? {B}reaking the Curse of Recursion by Accumulating Real and Synthetic Data` |
| juzek2025 | "? exploring" | `Why Does {C}hat{GPT} ``Delve'' So Much? {E}xploring the Sources of Lexical Overrepresentation in Large Language Models` |
| khan2025 | "{AI?} adoption" | `Who Gets Seen in the Age of {AI}? {A}doption Patterns of Large Language Models in Scholarly Writing and Citation Outcomes` |
| reinhart2025 | "? variation" | `Do {LLMs} Write Like Humans? {V}ariation in Grammatical and Rhetorical Styles` |
| sun2025 | "? quantifying" | `Are We in the {AI}-Generated Text World Already? {Q}uantifying and Monitoring {AIGT} on Social Media` |
| sadasivan2023 (if you switch to TMLR) | "? stress" | `Can {AI}-Generated Text be Reliably Detected? {S}tress Testing {AI} Text Detectors Under Various Attacks` |
| gray2024 | lowercase "estimating" in the source; straight `"` quotes | `{ChatGPT} ``Contamination'': {E}stimating the Prevalence of {LLMs} in the Scholarly Literature` |
| chang2026 | lowercase "analyzing" in the source | `Human Writing and Machine Patterns: {A}nalyzing a Decade of Convergence` |
| mccarthy2010 | "vocd-d"; "{HD-D:} a validation" | `{MTLD}, vocd-{D}, and {HD-D}: {A} Validation Study of Sophisticated Approaches to Lexical Diversity Assessment` |
| dugan2024raid | "{RAID:} a shared" | `{RAID}: {A} Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors` |
| geng2025 | "{Coevolution:} evidence" | `{Human-LLM} Coevolution: {E}vidence from Academic Writing` |
| bao2024fastdetectgpt | "{Fast-DetectGPT:} efficient" | `{Fast-DetectGPT}: {E}fficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature` |
| pillutla2021 | "{MAUVE:} measuring" | `{MAUVE}: {M}easuring the Gap Between Neural Text and Human Text using Divergence Frontiers` |
| clark2021 | Unicode ’ ‘ quotes (the apostrophe goes missing) | ``All That{'}s {`}{H}uman{'} Is Not Gold: {E}valuating Human Evaluation of Generated Text`` |

Notes:
- clark2021: the ACL Anthology `.bib` (https://aclanthology.org/2021.acl-long.565.bib) has ``All That{'}s `Human' Is Not Gold: Evaluating Human Evaluation of Generated Text``. Use ASCII `'` and `` ` `` (or `{'}`) instead of the Unicode ’ ‘ in the current entry. `{E}valuating` is not strictly needed after a top-level ": ", but it does no harm.
- Entries with a subtitle after a top-level ": " followed by a capital are already safe: casal2023 (`?: A`), jiang2024 (`: Is`), liang2024monitoring (`: A`), anderson2025spoken (`: Traces`), crossley2024persuade, chakraborty2024 (`: On`), park2026 (`: False`), yang2026coverage (`: A`) and lee2026 (`: A`).
- In reinhart2025, "Write Like Humans" and the other words after the first are lowercased by the style anyway. Only the braced letters are guaranteed to stay capitalised.

## 10. Other arXiv `@misc` entries that are now published

| key | venue | year | record |
|---|---|---|---|
| **agents4science2025** | Nature Biotechnology 44(1):11–14 | 2025 online (17 Dec); 2026 print (Jan) | doi:10.1038/s41587-025-02963-8 (Crossref; same title and five authors) |
| **khan2025** | Journal of Informetrics 20(4), article 101869 | 2026 (Dec issue) | doi:10.1016/j.joi.2026.101869 (Crossref; same five authors; Crossref spells the third surname "AlDahoul") |
| **kusumegi2026** | Science 390(6779):1240–1243 | 2025 | doi:10.1126/science.adw3000 (item 7) |
| **liang2024mapping** | COLM 2024 | 2024 | openreview YX7QnhxESU (item 1) |
| **gerstgrasser2024** | COLM 2024 | 2024 | openreview 5B2K4LRgmz (item 2) |
| **sadasivan2023** | TMLR | 2025 | openreview OOgsAZdFOt (item 3) |

The DOIs above work in `fetch_bib.py` and are the cleanest fix. For example, in citations.txt change the line to `agents4science2025 doi:10.1038/s41587-025-02963-8`.

Partial or uncertain results:
- **park2026**: the arXiv comment says "Presented in EMNLP 2026". The ACL Anthology EMNLP 2026 event page returns 404 (not out yet), so there is no DOI or `.bib` to cite. Keep `@misc` and re-check when the Anthology publishes. You could add `note = {To appear at EMNLP 2026}`, but the only source for that is the authors' arXiv comment.
- **yang2026coverage**: a workshop version with a different title ("Where Models Concentrate and Humans Spread: ...") is on OpenReview as JeqWtPeoaP, at the ICML 2026 Pluralistic-Alignment workshop. That workshop is usually non-archival, so keep the arXiv citation.
- **geng2024**: an ICML 2024 NextGenAISafety workshop poster (OpenReview 0CfKpG94co) exists, and the paper was rejected by TMLR. I found no archival venue, so keep the arXiv citation.
- **lin2025**: only arXiv and SSRN versions exist (doi:10.2139/ssrn.5170513 and 10.2139/ssrn.5216300). Keep the arXiv citation.
- **No published record found** (Crossref, OpenAlex, OpenReview/dblp, arXiv `journal_ref`) for:
  - gray2024
  - bentley2026
  - lee2026 (it has a Zenodo deposit, doi:10.5281/zenodo.22303588, which is not peer reviewed)
  - holzwarth2026
  - rallapalli2026
  - yakura2024
  - openai2023gpt4 (a technical report; it was never peer reviewed)
- Semantic Scholar could not be queried. A manual Google Scholar check of gray2024 and holzwarth2026 is advisable.

Ready-to-paste entries for the two newly found journal versions (from Crossref):

```bibtex
@article{agents4science2025,
  title   = {Exploring the Use of {AI} Authors and Reviewers at {Agents4Science}},
  author  = {Bianchi, Federico and Queen, Owen and Thakkar, Nitya and Sun, Eric and Zou, James},
  journal = {Nature Biotechnology},
  volume  = {44},
  number  = {1},
  pages   = {11--14},
  year    = {2025},
  doi     = {10.1038/s41587-025-02963-8},
  url     = {https://doi.org/10.1038/s41587-025-02963-8}
}

@article{khan2025,
  title   = {Who Gets Seen in the Age of {AI}? {A}doption Patterns of Large Language Models in Scholarly Writing and Citation Outcomes},
  author  = {Khan, Farhan Kamrul and Ibrahim, Hazem and AlDahoul, Nouar and Rahwan, Talal and Zaki, Yasir},
  journal = {Journal of Informetrics},
  volume  = {20},
  number  = {4},
  pages   = {101869},
  year    = {2026},
  doi     = {10.1016/j.joi.2026.101869},
  url     = {https://doi.org/10.1016/j.joi.2026.101869}
}
```
- agents4science2025: the year is 2025 because it was published online on 17 Dec 2025. Use 2026 if you cite the print issue (Crossref `published-print` is 2026-01).
- khan2025: the year is now 2026, so consider renaming the key to `khan2026`.
