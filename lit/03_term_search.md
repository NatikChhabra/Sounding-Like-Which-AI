# 03 - Term collision search

Search date: 2026-10-12.
Phenomenon: the share of human-written documents in a genre that a style model (trained on pre-2022 human text vs LLM output) cannot separate from LLM output, tracked over time against a pre-2022 baseline.

## Method and tool notes

- **arXiv API** (`export.arxiv.org/api/query?search_query=all:"TERM"`). This worked. Caveat: arXiv tokenizes hyphens, so "AI-likeness" and "machine-likeness" also match "AI like" and "Machin-like". Those counts are inflated with noise, and I read the titles by hand.
- **Semantic Scholar bulk search** (`/paper/search/bulk?query="TERM"`) does exact-phrase matching over titles and abstracts in the S2 index. It worked, but the API sometimes returned HTTP 429 (rate limit). Every query in the tables below did complete.
- **WebSearch** (general web, exact-phrase queries). This worked, but the results come back as model-written summaries, so I checked the key claims against primary pages where I could.
- **Crossref DOI resolution** gave metadata for the 2026 journal papers. Springer's landing page redirected to a login and could not be fetched (Chang 2026). The semanticscholar.org web UI returned 403.
- Google Scholar and the ACL Anthology were not queried directly. Their content was partly covered through S2 (which indexes the ACL Anthology) and WebSearch.

## Per-term results

| # | Term (variants searched) | arXiv exact | S2 exact | Web | Closest existing use | Meaning match? | Collision |
|---|---|---|---|---|---|---|---|
| 1 | "machine-style overlap" / "machine style overlap" | 0 | 0 | 0 exact hits | none | n/a | **LOW** |
| 2 | "stylistic convergence" (+ "human-LLM stylistic convergence") | 2 | 63 (mostly film, archaeology, sociolinguistics) | many | Malik & Awan 2026, *The Assistant Erased You* (arXiv:2608.00926): "rewriting produces stylistic convergence". Chang 2026, *Human writing and machine patterns: analyzing a decade of convergence*, Scientometrics, doi:10.1007/s11192-026-05589-y. Fast Company coverage of LLMs "making us sound the same". "Human-LLM stylistic convergence": 0 exact hits. | **Yes, close.** Chang 2026 measures human text (2014-2024, PubMed/Wikipedia/StackExchange) becoming more machine-predictable (perplexity/Binoculars). That is nearly the same phenomenon. | **HIGH** (the concept is already claimed. The exact compound "human-LLM stylistic convergence" is free but generic.) |
| 3 | "synthetic register" | 0 | 2 (ECG; biochemistry) | 0 relevant | none in LLM sense. Nearby: Nieth et al. 2026, *How Human-Like Are LLMs? A Register-Aware Linguistic Evaluation Framework* (arXiv:2605.23651) | n/a | **LOW-MED** (free as a phrase, but "register" already carries a different meaning for LLM text, described in row 4) |
| 4 | "machine register" / "LLM register" / "AI register" | 2 (unrelated) / 0 | 125 (compiler register allocation) / 2 (unrelated) | "AI register" used in Tricontinental essay *Controlling AI Writing Style* (2026, https://thetricontinental.org/wp-content/uploads/2026/05/ART_Currents_ControllingAIWritingStyle-1.pdf) for the default style of LLM output | Kim & Yi 2025, *Machine-Facing English: Defining a Hybrid Register Shaped by Human-AI Discourse* (arXiv:2505.23035). Milička, Marklová & Cvrček, AI-Brown corpus and "register variability in machine-generated texts" (Biber MDA) | Partial. These terms name the style of LLM output, or how humans talk *to* AI. They do not name the share of human text that falls in it. "Machine register" also collides with compilers/CPU registers. | **MED** (HIGH for "machine register" in mixed-field search) |
| 5 | "AI-likeness" / "machine-likeness" | 33 (noisy) / 86 (noise: Machin-like formulas) | 6 / 15 (robot perception, HRI) | many detector blogs | **"When Human Writing Looks Artificial: Perceived AI-Likeness as a Property of Text"**, *Research Result. Theoretical and Applied Linguistics*, 2026-09-30, doi:10.18413/2313-8912-2026-12-3-0-1 (28 Russian texts, perceived AI-likeness of human texts). Mizumoto 2026, *Corpus-informed AI-likeness screening for L2 writing*, Applied Corpus Linguistics, doi:10.1016/j.acorp.2026.100223. Khan et al. 2025, *Who Gets Seen in the Age of AI?* (arXiv:2509.08306): "zero-shot detection of AI-likeness" tracked across 230k CS papers 2021-2025. "Machine-likeness" is an established HRI term for perceptions of robots. | **Yes, very close.** These papers already use "AI-likeness" for human text that reads as AI, and Khan et al. track it over time with a detector. | **HIGH** |
| 6 | "stylistic indistinguishability" / "style indistinguishability" | 0 / 0 | 3 (art history) / 1 (cryptography) | No definitional use. Many papers argue whether LLM text is "indistinguishable" from human text (e.g. UCC stylometry study, HSSC 2025). | Indistinguishability is a cryptography term of art. | Not as a term. Reviewers will read it as a Turing-test or detection claim. | **MED** (the phrase is free, but it evokes the detection literature and crypto "indistinguishability") |
| 7 | "convergent register" | 0 | 1 (a Finnish IBD patient registry) | 0 exact hits | none | n/a | **LOW** (but vague: it does not say convergent with what) |
| 8 | "ambient AI style" / "AI-style saturation" | 0 / 0 | 0 / 0 | 0 exact hits ("ambient AI" is used in clinical scribe products and art) | none | n/a | **LOW** (but informal and hard to operationalize. "Ambient AI" collides with clinical ambient-scribe products.) |
| 9 | "register collapse" | 0 | 9 (landslides, databases, Urdu translation) | No established linguistics term. The nearest is "functional collapse" in a "Structure x Register Factorial", arXiv:2606.00935. | Readers will hear "model collapse" (Shumailov et al.; 348 arXiv hits for "model collapse"). | No. It implies loss of register *variation*, which is a different claim. | **MED** (semantic confusion with model collapse) |
| 10 | "LLM-ese" / "ChatGPT-ese" / "GPTese" / "LLMese" / "AI-ese" | 1 (incidental) / 0 / 0 | 0 / 0 / 1 (unrelated) | Informal use: "LLMese" (passo.uno blog, compressed writing *for* LLMs), "AI-ese" (Italian press, fanpage.it), "LLM'isms" / "Claude speak" (WSJ via tovima.com) | Not an academic term. In casual use it names the style of LLM output. Formal analogue: "translationese" / "machine translationese" (arXiv:2506.22050). | Partial. It names the style, not the share of human text in it. | **MED** (informal, jokey, and its meaning is unstable) |

## Existing terms that name (parts of) this phenomenon

| Term | Who uses it / where | Meaning | Fit to our phenomenon |
|---|---|---|---|
| **homogenization / "homogenizing effect"** | Sourati, Ziabari & Dehghani, *The Homogenizing Effect of LLMs on Human Expression and Thought*, Trends in Cognitive Sciences 2026 (arXiv:2508.01491). Also "linguistic homogenization" in Yakura et al. 2024, *Empirical evidence of LLM's influence on human spoken communication* (arXiv:2409.01754; S2 phrase hit) | Reduced diversity of human expression due to LLMs | The dominant umbrella term, but it means *less variance*, not *overlap with the LLM region*. It is the most likely reviewer comparison. |
| **convergence** | Chang 2026 (Scientometrics, above). Geng et al. 2025, *Human-LLM Coevolution: Evidence from Academic Writing* (ACL 2025, arXiv:2502.09606). Paper on 627k arXiv papers (arXiv:2504.13629): "LLMs drive convergence in academic writing" | Human writing drifts toward LLM-predictable or LLM-preferred patterns | **Closest prior work.** Chang 2026 is the nearest to our operationalization (machine-predictability over time). Cite it and differentiate: we use a separability share under a fixed pre-2022 anchor, not mean perplexity. |
| **"AI-ness" / "AI-likeness"** | Khan et al. 2025 (arXiv:2509.08306) report an "uptick in AI-ness". 2026 AI-likeness papers above | Detector-scored machine-likeness of documents | Very close to our metric. Avoid the term and cite these papers. |
| **"Human-LLM coevolution"** | Geng et al. 2025, ACL | Humans adapt their wording (e.g. avoid "delve") while LLM use rises | Related, broader framing |
| **"linguistic flattening"** | *AI and the great linguistic flattening* (PhilPapers, PASAAT-7). Teacher-role paper on "AI-induced linguistic homogenization" (Bodhi IJR 2025). "Losing our Tail, Again" (ACL 2025, arXiv:2507.03933) | Loss of diversity and the long tail | Same as homogenization, not overlap |
| **"Idiolect Erasure Rate"** | Malik & Awan 2026 (arXiv:2608.00926) | Drop in authorship-attribution accuracy after AI rewriting | A neighbouring metric, built on authorship rather than human-vs-LLM separability |
| **"slop" / "slopification"** | *Measuring AI "Slop" in Text* (arXiv:2509.19163). Substack essays. Merriam-Webster 2025 Word of the Year "slop" (per search summary, not independently checked) | Low-quality, generic text, explicitly *not* limited to AI authorship | Pejorative and quality-based. Unsuitable. |
| **"AI accent"** | Bernoff blog (bernoff.com, tag ai-accent). In academia, "AI accent" means synthetic *speech* accents (tourism and applied-linguistics papers, 2024-2025) | Telltale stylistic signs of LLM text | Informal. Collides with speech research. |
| **"AI-ification", "ChatGPTization", "machine-ification of language"** | 0 hits on arXiv and S2. No established web usage found | n/a | Unused, but too informal |
| **"Machine-Facing English"** | Kim & Yi 2025 (arXiv:2505.23035) | The register humans use when addressing AI | A different phenomenon (interaction register) |

## Three new candidate terms (verified LOW collision)

Each returned 0 exact-phrase hits on the arXiv API, 0 on Semantic Scholar bulk search, and 0 exact matches on the web as of 2026-10-12.

1. **machine-indistinguishable share (MIS)**: the fraction of human-written documents in a genre that a fixed, pre-2022-anchored human-vs-LLM style classifier cannot separate from LLM output.
2. **human-machine style overlap (HMSO)**: the proportion of a genre's human-written documents that fall inside the LLM output region of a style space calibrated on pre-2022 human text and LLM text. The phrase "style overlap" exists generically (e.g. arXiv:2409.07072), but the full compound does not.
3. **machine-region occupancy**: the share of human-written documents occupying the LLM-associated region of a fixed style model, reported per genre and per year relative to a pre-2022 baseline.

Also clean, but checked less thoroughly: "style-overlap rate" (0 arXiv, 0 S2, 0 web) and "machine-style overlap" (from the original list, 0/0/0).

Recommendation: **machine-indistinguishable share** is the most descriptive and self-explaining name, and it maps directly onto the operational definition. Position it against Chang 2026 ("convergence", machine-predictability), Khan et al. 2025 ("AI-likeness" via zero-shot detection) and Sourati et al. 2026 ("homogenization").

## Sources consulted

- arXiv API exact-phrase queries (see method). Raw output is kept in the session scratchpad.
- Semantic Scholar bulk search API.
- https://arxiv.org/abs/2608.00926 · https://arxiv.org/abs/2603.18161 · https://arxiv.org/abs/2509.08306 · https://arxiv.org/abs/2505.23035 · https://arxiv.org/abs/2508.01491 · https://arxiv.org/abs/2409.01754 · https://arxiv.org/abs/2502.09606 · https://arxiv.org/abs/2504.13629 · https://arxiv.org/abs/2509.19163 · https://arxiv.org/abs/2605.23651
- doi:10.18413/2313-8912-2026-12-3-0-1 · doi:10.1016/j.acorp.2026.100223 · doi:10.1007/s11192-026-05589-y (Crossref metadata only. The abstract summary comes from WebSearch, and the full text was not accessed.)
- https://thetricontinental.org/wp-content/uploads/2026/05/ART_Currents_ControllingAIWritingStyle-1.pdf · https://bernoff.com/blog/tag/ai-accent · https://passo.uno/write-docs-llms-language/ · https://www.tovima.com/wsj/now-were-all-starting-to-talk-like-ai-chatbots-too/ · https://fastcompany.com/91598016/ai-is-making-us-sound-the-same-and-killing-our-personal-expression
