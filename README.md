# Sounding Like Which AI?

**Machine-Style Overlap of arXiv Abstracts with Language Models of Different Vintages**
Natik Chhabra · ORCID [0009-0004-8786-7703](https://orcid.org/0009-0004-8786-7703)

How much human writing sounds like AI, how much already did before ChatGPT, and *which* AI does it sound like?

This repository holds the paper (`paper/preprint.pdf`), its source, every analysis, all generated data and the full
audit trail for a study of **Machine-Style Overlap (MSO)**: the share of documents that a calibrated classifier on
content-word-free style features judges at least as likely to be LLM output as pre-ChatGPT human writing.

**Status:** release v1.0 (preprint, not yet peer reviewed).

## Main findings
- In 131,448 arXiv abstracts from eight fields (2015–2026), MSO was **9.2%** before ChatGPT and stood
  **25.4 percentage points** (95% CI 23.2–27.7) above its pre-ChatGPT trend by June 2025. The gap holds across
  trend specifications, thresholds, feature-family ablations and never-revised papers, and is far larger than any
  placebo or instrument-drift gap. It is smaller, though still large, when the generators that write closest to
  human abstracts are left out (22.2 pp without the 2026 model, 17.9 pp without revisions of human drafts).
- Against generators whose pretraining data predate ChatGPT the gap is smaller but clear (**7.5 pp**), so part of
  the shift is unlikely to come from newer models learning from newer abstracts.
- Measured against one generator at a time, overlap rises and then turns down, and the turn **tends to come later
  for later-released models** (exploratory rank correlation 0.83, n = 18). A reference set that is not refreshed,
  like a fixed list of words such as *delve*, will eventually show the shift "fading".
- A zero-shot detector statistic computed with a small, older scoring model (Fast-DetectGPT criterion with GPT-2)
  does not see the shift.
- In student essays, English learners' writing is *less* machine-like than their peers' (2.3% vs 4.2%), even under
  a GPT-2 perplexity instrument that reproduces a published bias against TOEFL essays (63.7% vs 8.0% flagged).

## How this was made
The study was carried out by an AI system (Claude Opus 5.5, via Claude Code) under the author's direction: it
wrote the code, ran the analyses and drafted the text; the author chose the topic and constraints and is
responsible for the content. "The 2026 model" in the paper is that same system, used as one of the reference
generators. Details, including what has and has not been checked by a human, are in
[`paper/AI_DISCLOSURE.md`](paper/AI_DISCLOSURE.md). The git history is the complete record: AI-written commits say
so, and any human edit is a separate commit labelled `HUMAN-EDIT:`. Simulated peer-review rounds and the citation
verification reports are included (`paper/reviews/`, `lit/verification/`).

## Layout
| Path | What |
|---|---|
| `paper/` | `preprint.pdf`, LaTeX source (`main.tex`; `build.ps1` rebuilds both PDFs from the results), figures, AI disclosure, review rounds |
| `data/` | Every LLM generation used, and the exact samples and train/score splits (see `data/README.md`) |
| `code/` | All code; `run_all.ps1` runs the pipeline in order; `queues/` holds the exact batches used |
| `results/` | Every table the analyses write; `numbers.tex` feeds each result into the paper |
| `preregistration.md` | Analysis plan, committed before any result, with the full deviation log |
| `lit/` | Literature notes, citation list (`citations.txt`), verification reports |
| `PLAN.md` | Project status |

## Reproduce
The pipeline was run on Windows 11 (PowerShell scripts; Python 3.12.10).
```
py -3.12 -m venv .venv
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\python -m spacy download en_core_web_sm
powershell -File code\run_all.ps1 -Data D:\research-data         # or -Stage data|generate|perplexity|analysis|paper
```
Put these downloads in the data folder first:
- `hansard_au\corpus_1998_to_2025.parquet` from Zenodo record 17351233 (Australian Hansard)
- `learner\persuade_2.0_train.csv` from github.com/scrosseye/persuade_corpus_2.0
- `learner\liang_toefl_all_data.json` (`all_data.json` from HF `WxWx/ChatGPT-Detector-Bias`) and
  `learner\liang_us8th.json` (`HewlettStudentEssay_real_88/data.json` from the authors' GitHub repository)

The arXiv sample and RAID are fetched by the scripts. To reproduce the analyses exactly rather than regenerate the
texts, unpack `data/generated/*.gz` into the data folder: the 2026-model texts cannot be regenerated bit for bit
(no decoding control), and local-model outputs depend on hardware and Ollama version (0.40.3 was used; models
llama3.1:8b, qwen3:8b, gemma3:12b, mistral:7b, gpt-oss:20b, phi4:14b, granite3.3:8b, and for the vintage analysis
only llama2:7b, vicuna:7b, qwen3.5:9b, gemma4:12b and granite4.2:8b; temperature 0.8, fixed seeds). Re-fetching
arXiv abstracts by id (`data/samples/`) returns their current version. The paper compiles with
[Tectonic](https://tectonic-typesetting.github.io): `powershell -File paper\build.ps1`.

## Licences
- Code: MIT (`LICENSE`).
- Paper text, figures and results: CC BY 4.0.
- Generated data: see `data/README.md` (CC BY 4.0, except the essay generations: CC BY-NC-SA 4.0, as they derive
  from PERSUADE 2.0).
- Source datasets keep their own licences: arXiv metadata (CC0), Australian Hansard (CC BY 4.0), PERSUADE 2.0
  (CC BY-NC-SA 4.0), RAID and the Hugging Face release of Liang et al. 2023 (MIT). The Liang et al. US 8th-grade
  essays come from the authors' GitHub repository (no licence file; its README shows an MIT badge) and are not
  redistributed here.

Cite via `CITATION.cff` (GitHub's "Cite this repository" button).
