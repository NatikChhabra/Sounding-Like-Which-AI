# ARR Review, Round 3: Reviewer 2 (machine-generated text detection, stylometry, LLM evaluation)

**Submission (v3):** "Sounding Like Which AI? Machine-Style Overlap of arXiv Abstracts with Language Models of Different Vintages"
**Previous title (v2):** "After the Delve Fades: Scientific Abstracts Keep Moving Toward LLM Style"

**What I read.** `paper/main.tex` with every `\R{}` value looked up in `results/*.json|csv`; `paper/main.pdf` (all 13 pages rendered with pymupdf; Figure 2 inspected at full size); `code/features.py`, `generate.py`, `claude_prompts.py`, `fetch_raid.py`, `mso.py`, `perplexity.py` and the vintage, marker and perplexity parts of `analysis.py`; `preregistration.md`; `references.bib`; my round-2 review and the round-2 AC report.

**What I re-ran.** All of it was read-only, with scripts in my own scratch folder and the project venv. I used the cached spaCy features from `F:\research-data`.

1. A residual-artefact scan of all 19 chat generators after `features.clean`.
2. 6-gram overlap between each generation and its source abstract.
3. A re-implementation of `mso.training_set`/`mso.fit` for the single-generator P1 regions. With seed 0 it reproduces the paper's `arxiv_vintage.csv` values exactly: Granite 4.2 at 25.4% to 33.0%, Gemma 4 at 19.2% to 18.4%, Qwen3.5 at 21.2% to 23.5%, Qwen3 at 22.4% to 18.7%. I then varied the human training draw (10 seeds), stripped the Granite word-count notes, length-matched the 2026 abstracts to 2025, and split 2025 and 2026 by quarter.

I also checked release dates against public sources.

---

## Summary of the revision

v3 rebuilds the paper around generator *vintage*. It adds two open models whose pretraining data predate ChatGPT (Llama-2-Chat 7B and Vicuna 7B v1.5, run locally) and three open models released in 2026 (Qwen3.5 9B, Gemma 4 12B, Granite 4.2 8B), all with logged decoding. It defines a title-only (P1) region per generator, plus a "pre-ChatGPT-data" region (RAID GPT-4 and Llama-2-70B-chat, minus summary-register outputs, plus the two local Llama-2-family models).

Headline claims:

- **(a)** Against pre-ChatGPT-data generators, abstracts still moved into the region: a gap of 7.7 pp (CI 4.7–10.6).
- **(b)** From 2025 to 2026, MSO fell under all 14 generators released before August 2025 and rose under four of the five released since, including within the Granite and Qwen families.
- **(c)** Marker words mined from each generator track its style region until 2025, so the fall of *delve* "mostly reflects the age of the reference".

The title, abstract and Discussion no longer say abstracts "keep moving". Tool turnover is named as an equally consistent reading. The marker comparison is now matched by generator.

This is a real improvement and directly answers the core of my round-2 W1 and W2. The paper is now more honest about what a reference set can and cannot show. Most remaining problems are in the newest layer: how the 2025-to-2026 "rose/fell" result is computed and described, how the generators are dated, and several text/result mismatches introduced in the rewrite.

---

## 1. Round-2 weaknesses: status

| # | Round-2 weakness | Status | Evidence in v3 | What remains |
|---|---|---|---|---|
| W1 | Vintage confounded with prompt task; "2023-era → later style" unwarranted; title implied a change in human style | **Mostly** | §5 "Vintage": single-generator regions trained on P1 only; pre-ChatGPT-data region on title-only outputs; summary-register RAID outputs dropped from that region (L278–283). Title and abstract no longer say "keep moving". Tool turnover acknowledged (L431–433, L548–549). | Task is matched only nominally across vintages. RAID prompts carry no length instruction, while P1 does ("About {n} words"). The RAID single-generator regions still mix greedy, sampling and repetition-penalty decoding, and still include the summary register (ChatGPT 30%, Cohere 33%, Mistral 22%, MPT 16% match the paper's own `SUMMARY` regex; the filter is applied only to the pooled sets). Output lengths differ systematically by vintage (§2.1). |
| W2 | Marker comparison not like-for-like; credit Geng & Trotta; report lift not r | **Mostly** | Per-generator mined markers, source-matched (L285–291, §6.5). The abstract claim is now "a fixed reference set, or a fixed list of marker words … shows the shift fading as its models age", which is the qualified form I asked for. 5.8% vs 1.4% enrichment reported. | **The text contradicts the data:** "it kept rising only for the 2026 model" (L455–456), but Granite 4.2's mined-marker share also rose (34.4% → 35.6%; `arxiv_vintage.csv`; 17 of 19 fell, so two rose). **Granite 4.2's top mined word is *count*,** an artefact of uncleaned "(Word count: N)" notes (§2.4). Other lists contain topic words (*robotics, ablation, universe, latency, geometric, engineering*). Geng & Trotta's decline-with-persistence finding is still not credited in §6.5; geng2025 is cited only for "authors react to publicised markers". |
| W3 | MSO vs prevalence: implied α; off-the-shelf detector baseline | **Partly** | Mixture identity in §3. Implied α for cs and math in 2024 under CV and LOMO recall, compared with Liang et al. (2024b) (L356–363), with a sensible caveat on sentence vs document units. | Only two field-years. No field × year table, no TPR range. **No Binoculars or Fast-DetectGPT flag-rate series**, so it is still impossible to say what the content-word-free instrument adds over a standard zero-shot detector. |
| W4 | 2026 model uncontrolled and is the drafting system | **Partly (mitigated for the vintage claim)** | Three 2026 open models with logged decoding reproduce the pooled 2026 rise (`open2026_p1` 29.3% → 35.5%). Limitations restate the dual role. | No API regeneration, no disclosure of the sub-agent instructions, no near-copy filter. 62% of Claude P2 revisions still share >30% of their source's 6-grams (Qwen3 48%, Vicuna 45%, other models 1–23%). The 0.90-overlap memorised P1 output is still in the data. Claude is still one of the 14 generators of the main instrument, and of essays and Hansard. |
| W5 | Perplexity: proficiency, spelling, contamination, Jiang 2024, overgeneralisation | **Mostly** | Proficiency-adjusted OR for the perplexity instrument (GPT-2: 0.47 → 0.66, CI 0.52–0.85). GPT-2 scorer added. Jiang et al. (2024) cited twice. The claim is narrowed to "in these data … depends on the population". | No spelling normalisation (ELL log-perplexity 3.74 vs 3.43 may be partly orthographic). No standard zero-shot detector. **New factual error:** "GPT-2 was trained before either collection was public" (L519–520). Liang et al.'s US 8th-grade essays come from the Hewlett ASAP data, released on Kaggle in 2012, as the paper's own Ethics Statement says; the TOEFL essays were scraped from a public forum. Say instead that the collections were assembled later and that GPT-2's WebText is unlikely to contain them. |
| W6 | MTLD dominance and feature-family ablation; length-confounded dispersion | **Partly** | Dispersion recomputed on 150-word windows (§6.7): **Fixed**. | **The feature-family ablation is still missing** after two rounds. MTLD is still the top LLM-typical feature. The essay section concludes the region is "largely one of fluent, lexically diverse writing"; whether the arXiv rise and the vintage ordering survive without MTLD/scalars is unknown. |
| W7 | Generator set unrepresentative of what authors use; report quantisation and tags | **Partly** | Three 2026 open models added. | No GPT-5/Gemini-class API model. Ollama tags, digests and quantisation still unreported (default Ollama builds are 4-bit). Which Vicuna build `vicuna:7b` resolves to is not stated. |
| W8 | Presentation: TODO, "8.00 archives", bib encoding, COLM version, observed window means, base-vs-chat title, q-bio caveat | **Mostly** | TODO gone (the spot-check is now stated in the future tense). "Eight non-physics archives". Bib apostrophe and en dash fixed. Liang 2024b cites COLM. Nonparametric window gaps in Table 2. | The q-bio caveat is still missing (q-bio has the largest gap and is not in Liang 2024b). The base-vs-chat section was dropped, but §4 still says RAID base models are used "for one analysis" (L197–198), which now points nowhere. New macro bugs (§5). |
| Refs | Askitas, Kusumegi, Jiang | **Fixed** (all three cited) | | Kusumegi et al. gets one tacked-on sentence (L102–103); see §4. |

---

## 2. The vintage design (main new content)

### 2.1 Is the task matched across vintages?

Only partly. The P1 template is shared by the local and 2026 models. The RAID part, which is half the generators in Figure 2b and about three quarters of the training texts of the pre-ChatGPT-data region (900 of ~1,200 after the 450 cap), differs in:

- **Prompt.** RAID's template has no length target and no "Output only the abstract".
- **Decoding.** RAID mixes greedy and sampling; Llama-2-70B-chat, Mistral and MPT also have repetition-penalty variants. The local models use temperature 0.8 with Ollama defaults.
- **Length.** Median cleaned length (words) of title-only outputs by vintage:

| Vintage | Generators (median words) |
|---|---|
| RAID 2023 | GPT-4 107–114, ChatGPT 115–119, MPT 86–97, Cohere 131, Mistral 126–140, **Llama-2-70B 250** |
| Local pre-ChatGPT-data | Llama-2-Chat 7B 105, Vicuna 102 |
| 2024–25 | 139–169 |
| 2026 | Gemma 4 147, Qwen3.5 177, Granite 4.2 188, Claude 156 |

Human arXiv abstracts have a median of 169 words (2025) and 176 words (2026).

**Truncated Llama-2-70B outputs.** 50–71% of RAID Llama-2-70B-chat outputs hit the 250-word cap and end mid-sentence. This generator is one of the four that define the "identified" pre-ChatGPT-data region.

**Length checks.** I checked whether *human* length drives the 2026 changes. It does not: reweighting 2026 abstracts to the 2025 length deciles changes every single-generator Δ by ≤0.5 pp. Generator-side length is a different matter. Older generators systematically produce shorter texts than the abstracts they are compared with, newer ones do not, and sentence-length mean and SD are features. Please report per-generator output length and refit the single-generator regions on length-matched subsets (or truncate every training text to the human median).

**Register.** The summary filter is applied only to the pooled pre-ChatGPT-data sets, not to the RAID single-generator regions in Figure 2b, although §6.4 describes them as "the title-only task". Apply the filter there too, or say otherwise.

### 2.2 Is "pre-ChatGPT-data" defensible?

It is defensible for the specific confound the paper cares about: none of these models can have learned the style of *post-ChatGPT arXiv abstracts*. It is not defensible as worded.

- "cannot reflect models that learned from post-ChatGPT writing" (L399) and "cannot be an artefact of newer models learning from newer abstracts" (L408) are too strong. All four models were *post-trained* in 2023:
  - Llama 2's tuning data run to July 2023 (Touvron et al.).
  - GPT-4-0613's RLHF post-dates ChatGPT.
  - Vicuna v1.5 is supervised fine-tuning on ShareGPT, i.e. **distilled 2023 ChatGPT output**. Footnote d says this.
- The paper's own round-2 base-vs-chat result found chat tuning moves text into the region. Most of the "LLM style" in question is therefore created exactly in the post-training stage that is not pre-ChatGPT.

The defensible phrasing is "pretraining data predate ChatGPT, and post-training (2023) predates most LLM-assisted arXiv writing". Limitations already says "their instruction tuning used data from 2023". Bring that into §6.4 and the abstract.

**What carries the 7.7 pp gap.** Single-generator gaps are GPT-4 11.5, Llama-2-70B-chat 5.5, Llama-2-Chat 7B 3.7 (CI 1.3–6.2) and Vicuna 1.4 (CI 0.3–2.6) pp. The two small local models together give 3.5. "Smaller but clear" is fair for GPT-4. For the open models it is "small but non-zero". The abstract's "clear (7.7 points)" should say that GPT-4 carries most of it.

### 2.3 The 2025-to-2026 "rose/fell" result: robust in sign to the training draw, fragile in timing

**(i) Instrument variation.** Each local single-generator region is trained on only 150 LLM texts against 150 human texts, and its level depends heavily on the human draw. I refit each with 10 different human training draws:

| Generator | 2025 MSO, range over draws | Δ 2025→2026, mean (min, max) | Draws with Δ > 0 |
|---|---|---|---|
| Claude Opus 5.5 | 24.2–29.3 | +10.7 (+9.3, +12.9) | 10/10 |
| gpt-oss 20B | 27.3–33.6 | +10.5 (+9.0, +11.8) | 10/10 |
| Granite 4.2 8B | 16.1–26.4 | +7.2 (+4.8, +10.0) | 10/10 |
| Qwen3.5 9B | 14.4–21.6 | +2.3 (+0.6, +3.4) | 10/10 |
| **Gemma 4 12B** | 14.5–19.2 | **−0.3 (−1.3, +0.5)** | **4/10** |
| Gemma 3 12B | 24.0–31.6 | −2.0 (−3.1, −0.5) | 0/10 |
| Granite 3.3 8B | 15.7–28.8 | −2.4 (−3.6, −1.5) | 0/10 |
| Qwen3 8B | 17.8–28.0 | −3.1 (−4.3, −2.0) | 0/10 |
| Llama 3.1 / Mistral / Phi-4 | — | −4.1 to −4.7 | 0/10 each |
| Llama-2-Chat 7B / Vicuna | — | −4.3 / −3.0 | 0/10 each |

The *sign* is stable for every generator except Gemma 4, which is indistinguishable from zero. Credit to the authors: their dichotomy survives this check. Two caveats remain. Gemma 4 should be reported as "no change", not "fell by less than a point". The *levels* vary by up to 13 pp across draws (Granite 3.3: 15.7–28.8%), so Figure 2a's level comparisons between single generators are not interpretable without intervals.

**(ii) Timing.** The comparison is the 2025 *annual* mean against January–September 2026. The aggregate series rose throughout 2025, so the 2025 annual mean sits below late-2025 values, and a region that merely plateaued in late 2025 will show a 2025→2026 "rise". Same seed-0 instruments, by period:

| Generator | Jan–Sep 2025 | Oct–Dec 2025 | 2026 Q1 / Q2 / Q3 | 2026 vs Q4 2025 |
|---|---|---|---|---|
| Claude | 28.4 | 32.0 | 37.6 / 39.2 / 40.7 | **+7.2** |
| gpt-oss | 27.7 | 34.6 | 38.0 / 39.9 / 37.5 | +3.9 |
| Granite 4.2 | 23.9 | 29.9 | 32.8 / 34.2 / 32.0 | +3.1 |
| **Qwen3.5** | 20.5 | 23.1 | 25.2 / 24.3 / **21.2** | **+0.4** |
| Gemma 4 | 18.6 | 21.2 | 20.7 / 18.2 / 16.4 | −2.8 |
| Qwen3 | 22.2 | 22.9 | 21.7 / 18.8 / 16.0 | −4.2 |
| Granite 3.3 | 21.9 | 23.6 | 22.0 / 20.2 / 17.2 | −3.9 |
| Llama-2-Chat 7B | 16.0 | 13.7 | 12.5 / 10.1 / 8.3 | −3.5 |

Against Q4 2025, Qwen3.5 is flat, and within 2026 it *declines* quarter by quarter, as the older models do. The Qwen within-family contrast therefore rests on the annual-mean artefact. Granite (3.3 −3.9 vs 4.2 +3.1) is the one within-family contrast that survives. gpt-oss and Granite 4.2 also turn down in Q3 2026; only Claude rises throughout.

A more defensible and more interesting summary is a **peak-timing ordering**. Older-vintage regions peaked earlier: Vicuna and Cohere in 2024, Llama-2-Chat in H1 2025. 2024–25 models peaked in late 2025. gpt-oss, Granite 4.2 and Qwen3.5 peak in 2026 Q1–Q2. Only Claude has not yet peaked.

**Requested:** replace the binary annual Δ with (a) quarterly series per single generator, (b) the timing of each region's peak with a bootstrap interval, (c) intervals that include instrument variation (re-draw the human and LLM training sets). Then restate "rose under four of the five" and "the pattern holds within model families" accordingly.

**(iii) "Vintage" is release date, not training-data recency, and the August 2025 split is post hoc.**

- gpt-oss's knowledge cutoff is June 2024 (OpenAI model card; widely listed as 30 June 2024). That is *earlier* than Gemma 3 (Aug 2024), which fell, and Gemma 4 (the paper's own "Jan 2025"), which did not rise. Yet gpt-oss shows one of the two largest rises.
- So the 2026 ordering is not explained by how recent the pretraining data are. The paper's alternative reading, "the newest models learned from 2025 writing" (L431–432, L548–549), is unavailable for gpt-oss at least as far as pretraining goes. This actually *helps* the paper's argument against the circularity reading, and the authors should use it.
- It also shows that the relevant variable is something about the post-training generation of these models: reasoning-era RL, house style of the developer, or similarity to the assistants authors actually use, such as GPT-5-class tools for gpt-oss.
- Table 1 leaves the gpt-oss cutoff blank. Fill it in.
- Say explicitly that the "since August 2025" boundary was chosen after seeing the result. It sits five days before gpt-oss's release.

### 2.4 Are the 2026 open models correctly described?

| Model | Paper says | What I could verify |
|---|---|---|
| Qwen3.5 9B | "2026-02" | The Qwen3.5 *family* launched mid-February 2026, but the small dense models (0.8B–9B) were released around **2 March 2026**. |
| Gemma 4 12B | "2026-05" | Gemma 4 launched on 2 April 2026 with E2B, E4B, 26B A4B and 31B. **The 12B appears in Google's release log on 3 June 2026**, not May. |
| Gemma 4 cutoff | "Jan 2025" | I could not find a published cutoff. Cite the exact source, or leave it blank as for other models. |
| Granite 4.2 8B | "2026-08" | Consistent with public listings (about 25 August 2026). |

**Figure 2b's "release order" is wrong.** Granite 4.2 (Aug 2026) is plotted before Qwen3.5 (Mar 2026) and Gemma 4 (Jun 2026).

**Figure 2's caption is stale.** It says "Overlap fell against every generator except the two newest". The bars and §6.4 show four rises: gpt-oss, Granite 4.2, Qwen3.5 and Claude. The two newest by date are Granite 4.2 and Gemma 4, and Gemma 4 fell.

**Within-family validity.**

- Qwen3 → Qwen3.5 and Granite 3.3 → Granite 4.2 differ in architecture, post-training recipe (both newer members are reasoning-RL models) and multimodality, not only in data vintage.
- "Developer and size are roughly fixed" is fair. "Vintage" here should be read as "generation of the family's post-training", not "training-data date".
- Thinking was disabled via Ollama `think: false` for Qwen3, Qwen3.5, Gemma 4 and Granite 4.2, and set to `"low"` for gpt-oss. That is a reasonable choice but should be stated, because reasoning-trained models in non-thinking mode are not how many users run them.
- Gemma 3 vs Gemma 4 gives no contrast (both ≈ 0 or negative), so it is one of three families showing the effect at best.

### 2.5 Residual cleaning artefacts

From my scan of all 19 chat generators after `features.clean`:

- **Granite 4.2 P1: 31% (46/150) end with a word-count note**, such as "(Word count: 149)" or "(Approx. 110 words)". `_NOTE` only matches notes in a separate trailing paragraph. These notes contaminate the Granite 4.2 mined-marker list (its top word is *count*). Removing them and recomputing features leaves the style result intact (Granite 4.2 Δ 7.4 pp vs 7.6 pp, seed 0), so this is a marker-side problem only. Granite 4.2 P3 shows it occasionally (1.3%).
- **Llama-2-Chat 7B P2:** 22% contain an inline "Abstract:" label and 21% "revised/improved abstract"; 11% have a trailing "Keywords: …" line. Mistral P1/P3 has "Keywords:" in 4%. `_MD` strips "abstract:" only at line start after a newline. P2 enters `old_open_all` but not the P1 regions.
- **RAID Llama-2-70B-chat truncation:** 50–71% end mid-sentence at the 250-word cap (§2.1).
- **No thinking-tag leakage** in any model. Wrappers and markdown are essentially gone (<2%). The cleaning is now good apart from the items above.

### 2.6 Mined markers

The source-matched log-ratio is a sensible design. It is much better than my round-2 version, which used the pooled training set. Three problems remain:

1. **Topic leakage.** Mined lists contain *robotics, ablation* (pre-ChatGPT-data region), *universe* (Vicuna), *latency, geometric* (Gemma 4) and *engineering, soft, near* (gpt-oss). These track arXiv's topic mix, which shifted toward ML over 2022–2025, so part of every marker "rise until 2025" may be compositional. Matching on the source abstract cancels topic only for words the source contains; a title-only model elaborates the title's topic with its own topical words. Filter words with high document frequency in post-2022 *human* LLM-topic abstracts, or show the series on the no-LLM-topic subset.
2. **Register words.** The pre-ChatGPT-data list still contains *discusses, contributes, explores, summarized, highlights*, i.e. the third-person summary register that the style-side filter was meant to remove.
3. **Text vs data.** See W2 above: Granite 4.2's marker share rose too, so "kept rising only for the 2026 model" is false. The interpretation "the decline of *delve* mostly reflects the age of the reference" is reasonable for the older generators. It is weaker for gpt-oss and Qwen3.5, whose markers fell while style rose (n_style_rose_marker_fell = 2). The paper reports this honestly, but the generalisation should be restated with that exception.

---

## 3. Learner and perplexity section

This section is now careful and mostly correctly scoped. Remaining overclaims:

1. **"GPT-2 was trained before either collection was public, so the contrast does not come from memorised essays."** Factually wrong for the 8th-grade essays (ASAP, Kaggle 2012) and doubtful for forum-scraped TOEFL essays. The conclusion is probably still right, since WebText is Reddit-linked pages, but the stated reason is not.
2. **The "detector" is a toy.** It is a one-feature isotonic threshold on mean token NLL. Under GPT-2 it flags **29% of all human PERSUADE essays** (31% of non-ELL). Its AUC is not reported. "Reproduces a published bias" is fair as a qualitative replication (63.7% TOEFL vs 8.0% 8th grade, close to Liang et al.'s ~61% average). "Which learners such a detector flags depends on the population" should become "which learners *a perplexity threshold calibrated on PERSUADE* flags…". Report its AUC on held-out PERSUADE human vs LLM essays.
3. **Spelling.** ELL essays have higher log-perplexity (3.74 vs 3.43). Subword NLL is inflated by misspellings, so the direction of the PERSUADE contrast may be partly orthographic. A spell-normalised rerun is cheap and was requested in round 2.
4. **Jiang et al. (2024).** "Consistent with detectors that showed no bias in a large writing assessment" is acceptable. Note, though, that Jiang et al.'s detectors were trained in-domain on GRE essays with many features. Their result supports "bias depends on detector training and calibration domain" at least as much as "depends on the population". Both readings fit; state both.
5. The abstract sentence ("even under a GPT-2 perplexity instrument that reproduces a published bias against TOEFL essays") is fine.

---

## 4. Related-work positioning

- **Askitas (2025).** Now cited and described accurately (stylometric shift in econ working-paper abstracts, event study, classifier). Fine. One line on how MSO differs, beyond "estimand", would help: Askitas uses a GPT-like classifier share too.
- **Bentley et al. (2026).** "track an LLM-associated style index for arXiv abstracts built from a few markers". The arXiv abstract of 2606.27052 describes a composite LLM-associated style index and complexity metrics (vocabulary size, Zipf/Heaps exponents, top-word turnover) over millions of arXiv abstracts from 2010 to 2025. It does not say the index is "built from a few markers". Check the paper and describe it accurately. It is the closest arXiv-population competitor and deserves more than half a sentence.
- **Chang (2026).** Description is plausible and consistent with my round-2 notes. Fine.
- **Kobak (2025), Liang (2024b), Geng & Trotta (2025).** Accurate. Geng & Trotta should be credited in §6.5 for the decline-with-persistence pattern (W2).
- **Kusumegi et al. (2025, *Science*).** The one-sentence mention ("LLM adoption also changes how much scientists write") undersells its relevance. It identifies LLM adopters among ~2M arXiv/bioRxiv/SSRN preprints and studies writing complexity. That bears directly on the "fluent but not better" reading of MSO and on the composition caveat in Limitations.

**Missing and relevant to the new vintage framing:**

- **Pu et al. (2023)**, "On the Zero-Shot Generalization of Machine-generated Text Detectors" (Findings of EMNLP 2023). Detectors trained on older or smaller generators transfer asymmetrically to newer ones. This is directly the LOMO and vintage point.
- **Sun et al. (2025)**, "Idiosyncrasies in Large Language Models" (ICML 2025). Model families are separable from each other by output style. This is relevant to treating each generator as its own region and to the within-family comparison.
- **Cross-generator detection benchmarks**, e.g. MAGE (Li et al., ACL 2024) and M4GT-Bench (Wang et al., ACL 2024). These are the standard evidence that "LLM style" is generator-specific. One sentence suffices.

---

## 5. New problems and presentation

1. **Macro scaling bugs in the PDF.**
   - §6.7 prints "in 2025 lies 0.05 above that trend (bootstrap CI −35.9 to 50.8)". The CI macros are multiplied by 100 and the estimate is not: the JSON has est 0.046, CI −0.359 to 0.508.
   - §6.6 prints "on the logit scale 27.7 against 149.0". The JSON has 0.277 and 1.490.
2. **Dispersion is underpowered, so "without a faster loss of stylistic spread" overreads it.** The 2025 CI (−0.36 to +0.51) spans roughly ±4 years of the pre-trend (−0.11/yr). The right wording is "no detectable change; the measure cannot exclude an acceleration of several years' worth of pre-trend decline". This is the paper's only direct homogenization measure for the theme track.
3. **Figure 2 caption and ordering** (§2.4).
4. **Dangling reference:** "for one analysis, five base models" (L197–198), but no base-model analysis remains in v3.
5. **Contribution (5) wording.** "Marker words mined from each generator rise with its style region until 2025" is not true for Cohere and Vicuna, whose markers peak in 2025 while style peaks in 2024. "Overlap rose until 2025" in the abstract has the same problem (Vicuna's region peaks in 2024 at 7.3%, then 6.1%).
6. **Claude's single region has a pre-ChatGPT level of ~17%**, versus 1–8% for every other generator. Its P1 outputs are much closer to human abstracts. That is worth one sentence, because it makes the Claude region's "rise" a different kind of object from the others.
7. **H4 q-bio caveat** still missing (round 2).
8. **Reproducibility.** Ollama tags, digests and quantisation are not reported. The Claude sub-agent instructions are not disclosed. The analysis plan has not been updated for the vintage analysis, which is correctly logged as post-review deviation (5).

**Writing that reads as AI-generated.** The prose is much cleaner than in round 1: no "notably/crucially/moreover", and no em-dash cascades. What remains:

- Aphoristic closers and a recurring "X, not Y" cadence, e.g. "so 'sounding like AI' there partly means writing well"; "which is the precondition, though not evidence, for the recursive dynamics"; "whoever wrote it" (twice in the first page).
- Very number-dense sentences with nested parentheticals. §6.3 L333–363 and §6.8 L496–524 each pack 10–20 macros into a paragraph, which is hard to read and typical of generated drafts.

Move the secondary numbers into a small table: per-generator 2025 level, Δ, interval and peak quarter would do this naturally for §6.4.

---

## 6. Scores

- **Soundness: 3.5 / 5.**
  - The core arXiv shift is well established. It now also holds against pre-ChatGPT-data generators, mostly via GPT-4. I could reproduce every vintage number I checked, and the sign of the single-generator Δ is robust to the instrument's training draw.
  - Against that:
    - The "rose/fell" headline uses an annual-mean comparison that manufactures one of the four rises (Qwen3.5) and one within-family contrast.
    - "Vintage" is operationalised as release date with a post hoc split that training-data cutoffs contradict (gpt-oss).
    - Task, length, decoding and register are only partly matched across vintages.
    - Several text/figure/result mismatches remain: the Figure 2 caption, "only the 2026 model", the release dates and the GPT-2 claim.
- **Excitement: 3.5 / 5.** "Which AI does writing sound like, and does the answer depend on the reference's vintage?" is a better and more original question than v2's. Showing that any fixed reference set makes the shift look like it fades is a useful methodological warning for prevalence and detection work. A peak-timing analysis by vintage would make it a strong one.
- **Overall assessment: 3.5 / 5.** Findings-ready now. Main conference if items 1–3 below are done.
- **Reviewer confidence: 4 / 5.** I re-implemented the single-generator regions, reproduced the authors' numbers exactly, and ran the instrument-variation, timing, length and artefact checks. My knowledge of the 2026 model release details comes from public listings and is less certain than the rest.

## 7. The five most important changes (in order of impact)

1. **Make the 2025→2026 vintage result a properly timed, uncertainty-bearing analysis.**
   - Report quarterly single-generator series, each region's peak timing with intervals that include instrument variation (re-drawn human and LLM training sets), and Δ against Q4 2025 rather than the 2025 annual mean.
   - Report Gemma 4 as no change.
   - Rest the within-family claim on Granite only, unless Qwen survives the timed comparison. In my check it does not (+0.4 pp vs Q4 2025, declining through 2026).
   - Rewrite the abstract sentence "rose under four of the five released since" accordingly.
2. **Define "vintage" correctly and drop the post hoc August-2025 split.**
   - Fill in the training cutoffs (gpt-oss: June 2024), correct the release months (Qwen3.5 9B: March 2026; Gemma 4 12B: June 2026), source or drop the Gemma 4 cutoff, and fix Figure 2b's order and caption.
   - Acknowledge that cutoff recency does not order the 2026 changes. Use the gpt-oss case against the "models learned from 2025 writing" reading, and say that the dividing variable looks like post-training generation, house style or proximity to tools in use.
   - Soften "cannot reflect models that learned from post-ChatGPT writing" to the pretraining-only claim, noting 2023 post-training and Vicuna's ChatGPT distillation.
3. **Match the vintage comparison on everything except the model, or show it does not matter.**
   - Apply the summary filter to RAID single-generator regions. Restrict RAID to one decoding without repetition penalty. Drop or re-truncate the mid-sentence Llama-2-70B outputs. Report per-generator output length and refit on length-matched training texts.
   - Clean the residual artefacts (inline "Abstract:" / "Keywords:" / "(Word count: N)").
   - Purge topic and register words from the mined-marker lists, and fix "kept rising only for the 2026 model" (Granite 4.2 rose too).
4. **Deliver the two round-2 checks still missing:** (a) a feature-family ablation, at minimum without MTLD and scalars, for the main gap, the pre-ChatGPT-data gap and the single-generator Δ signs; (b) one off-the-shelf zero-shot detector series (Binoculars or Fast-DetectGPT at a pre-period-calibrated threshold) on the same arXiv sample, to show what MSO adds over a standard detector.
5. **Correct the factual and presentation errors.**
   - The GPT-2/"before either collection was public" claim; the macro scaling bugs in §6.6–6.7; the dispersion interpretation (underpowered).
   - The dangling base-model sentence; Contribution (5) and the abstract's "rose until 2025".
   - The Bentley et al. description. Add Pu et al. (2023) and Sun et al. (2025).
   - Report the perplexity instrument's AUC and a spell-normalised rerun. Disclose the Ollama tags/quantisation and the Claude sub-agent instructions, and filter Claude's near-copy P2 revisions and memorised P1 output.
