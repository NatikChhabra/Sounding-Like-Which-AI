# Sounding Like Which AI?

**Machine-Style Overlap of arXiv Abstracts with Language Models of Different Vintages**
Natik Chhabra · ORCID [0009-0004-8786-7703](https://orcid.org/0009-0004-8786-7703)

How much human writing sounds like AI, how much already did before ChatGPT, and *which* AI does it sound like?

This repository holds the data pipeline, every analysis, and the paper (`paper/main.tex`) for a study of
**Machine-Style Overlap (MSO)**: the share of documents that a calibrated classifier on content-word-free style
features judges at least as likely to be LLM output as pre-ChatGPT human writing.

## Main findings
- In 131,448 arXiv abstracts from eight fields (2015–2026), MSO was **9.2%** before ChatGPT and stood
  **25.4 percentage points** (95% CI 23.2–27.7) above its pre-ChatGPT trend by June 2025, robust to trend
  specification, placebo dates, instrument drift, feature-family ablations and never-revised papers.
- Against generators whose pretraining data predate ChatGPT the gap is smaller but clear (**7.5 pp**), so part of
  the shift is unlikely to come from newer models learning from newer abstracts.
- Measured against one generator at a time, overlap rises and then turns down, and the **later a model was
  released, the later the turn** (Spearman ρ = 0.83, n = 18). A reference set that is not refreshed, like a fixed
  list of words such as *delve*, eventually shows the shift "fading".
- An off-the-shelf zero-shot detector statistic (Fast-DetectGPT criterion with GPT-2) does not see the shift.
- In student essays, English learners' writing is *less* machine-like than their peers' (2.3% vs 4.2%), even under
  a GPT-2 perplexity instrument that reproduces a published bias against TOEFL essays (63.7% vs 8.0% flagged).

**Status:** preprint version v5; not yet peer reviewed.

## How this was made
The study was carried out by an AI system (Claude Opus 5.5, via Claude Code) under the author's direction: it wrote
the code, ran the analyses and drafted the text; the author chose the topic and constraints and is responsible for
the content. Details, including what has and has not been checked by a human, are in
[`paper/AI_DISCLOSURE.md`](paper/AI_DISCLOSURE.md). The git history is the complete record: AI-written commits say
so, and any human edit is a separate commit labelled `HUMAN-EDIT:`. Simulated peer-review rounds and the citation
verification reports are included (`paper/reviews/`, `lit/verification/`).

## Layout
| Path | What |
|---|---|
| `paper/` | Manuscript (`main.tex`), figures, bibliography, AI disclosure, review rounds |
| `code/` | All code; `run_all.ps1` runs the pipeline in order; `queues/` holds the exact batches used |
| `results/` | Every table the analyses write; `numbers.tex` feeds each result into the paper |
| `preregistration.md` | Analysis plan, committed before any result, with the full deviation log |
| `lit/` | Literature notes, citation list (`citations.txt`), verification reports |
| `PLAN.md` | Project status |

Raw and intermediate data (about 2 GB) are not in the repository; the scripts rebuild them from public sources.

## Reproduce
```
py -3.12 -m venv .venv
.venv\Scripts\pip install pandas pyarrow scikit-learn statsmodels spacy matplotlib transformers torch sentence-transformers pymupdf
.venv\Scripts\python -m spacy download en_core_web_sm
powershell -File code\run_all.ps1 -Data D:\research-data            # or -Stage data|generate|perplexity|analysis|paper
```
- Download first: Australian Hansard (Zenodo record 17351233), PERSUADE 2.0 (github.com/scrosseye/persuade_corpus_2.0),
  and the essays of Liang et al. (2023) (HF `WxWx/ChatGPT-Detector-Bias`; 8th-grade essays from the authors' GitHub).
- Local models run through [Ollama](https://ollama.com): llama3.1:8b, qwen3:8b, gemma3:12b, mistral:7b, gpt-oss:20b,
  phi4:14b, granite3.3:8b, and for the vintage analysis only llama2:7b, vicuna:7b, qwen3.5:9b, gemma4:12b and
  granite4.2:8b (temperature 0.8, fixed seeds). The 2026-model texts were produced from the prompt batches written by
  `code/claude_prompts.py` (not reproducible bit-for-bit: no decoding control).
- The paper compiles with [Tectonic](https://tectonic-typesetting.github.io) from `paper/main.tex`.

## Data sources and licences
- arXiv metadata via the arXiv API (metadata CC0)
- Australian Hansard 1998–2025, Zenodo record 17351233 (CC BY 4.0)
- PERSUADE 2.0, Crossley et al. 2024 (CC BY-NC-SA 4.0; share-alike applies to derived data)
- Liang et al. 2023 TOEFL and US college essays, HF `WxWx/ChatGPT-Detector-Bias` (MIT); their US 8th-grade essays
  come from the authors' GitHub repository (no licence stated; texts are not redistributed here)
- RAID, Dugan et al. 2024, HF `liamdugan/raid` (MIT)

Code is MIT-licensed (`LICENSE`). Cite via `CITATION.cff` (GitHub's "Cite this repository" button).
