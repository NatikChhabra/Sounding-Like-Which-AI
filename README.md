# Sounding Like Which AI?

**Machine-Style Overlap of arXiv Abstracts with Language Models of Different Vintages**
Natik Chhabra · ORCID [0009-0004-8786-7703](https://orcid.org/0009-0004-8786-7703)

How much human writing sounds like AI, how much already did before ChatGPT, and *which* AI does it sound like?

This repository holds the paper (`paper/preprint.pdf`), its source, every analysis, all generated data and the full
audit trail for a study of **Machine-Style Overlap (MSO)**: the share of documents that a calibrated classifier on
content-word-free style features judges at least as likely to be LLM output as pre-ChatGPT human writing.

**Status:** pre-release draft: not yet read or approved by the author, not peer reviewed. v1.0 will be tagged
after the author's read-through.

## Main findings
- In 131,448 arXiv abstracts from eight fields (2015–2026), MSO was **9.2%** before ChatGPT and stood
  **25.4 percentage points** (95% CI 23.2–27.7) above its pre-ChatGPT trend by June 2025. The gap holds across
  trend specifications, thresholds and feature-family ablations, yearly values barely change when only
  never-revised papers are counted, and it is far larger than any placebo or instrument-drift gap. It is smaller, though still large, when the generators that write closest to
  human abstracts are left out (22.2 pp without the 2026 model, 17.9 pp without revisions of human drafts).
- Against generators whose pretraining data predate ChatGPT the gap is smaller (**7.5 pp**; GPT-4 alone gives the largest gap; 3.5 pp for the two
  models run from titles on the paper's own prompts but 12.5 pp over all three prompt styles; 13.1 pp with the trend line fitted only to June 2025, against 22.7 pp for
  the 2024–2025 open models), so part of the shift points towards models unlikely to have learned it from
  recent abstracts.
- Measured against one generator at a time, overlap with most generators rises and then turns down, and the turn
  **tends to come later for later-released models** (exploratory rank correlation 0.79, n = 18; 0.66 for the 15
  generators chosen before the annual single-generator pattern was seen). The correlation holds across training draws (0.79–0.85; 0.73–0.84 with equal training sizes),
  with abstract length or field mix held fixed (0.84, 0.81) and without the 2023 models (0.82). But newer models
  also write longer outputs, and output length predicts the peak about as well (0.73), so vintage and output length
  cannot be separated. Two of the three 2026 open models peaked before they were released and the third in its
  release quarter, so authors using them can explain little of the timing. A fixed reference set, like a fixed
  list of words such as *delve*, can therefore show the shift "fading" while overlap with newer models still rises.
- A zero-shot detector statistic computed with a small, older scoring model (Fast-DetectGPT criterion with GPT-2)
  does not see the shift (its flag rate falls after 2022); the larger scoring models of the original method might.
- In US school essays (PERSUADE 2.0), English learners' writing falls in the region *less* often than their peers'
  (2.3% vs 4.2%), largely tracking essay scores, even under a GPT-2 perplexity instrument that reproduces a
  published bias against TOEFL essays (63.7% vs 8.0% flagged).

## How this was made
The study was carried out by an AI system (Claude Opus 5.5, via Claude Code) under the author's direction: it
wrote the code, ran the analyses and drafted the text; the author chose the topic and constraints and is
responsible for the content. "The 2026 model" in the paper is that same system, used as one of the reference
generators. Details, including what has and has not been checked by a human, are in
[`paper/AI_DISCLOSURE.md`](paper/AI_DISCLOSURE.md). The git history is the complete record of changes to the
files: AI-written commits say
so, and any human edit is a separate commit labelled `HUMAN-EDIT:`. On 2026-10-13 the public history was rewritten
once, with the author's approval, to remove the LLM revisions of Hansard speeches (they had been released in two
earlier commits; Hansard text may not be adapted) and a local Windows username in file paths (the speech-generation file was removed from those two commits whole);
the commit ids cited in the paper and the analysis plan are unchanged. Simulated peer-review rounds and the citation
verification reports are included (`paper/reviews/`, `lit/verification/`).

## Layout
| Path | What |
|---|---|
| `paper/` | `preprint.pdf`, LaTeX source (`main.tex`; `build.ps1` rebuilds both PDFs from the results), figures, AI disclosure, review rounds |
| `data/` | The LLM generations used (all but the speech revisions), and the exact samples and train/score splits (see `data/README.md`) |
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
powershell -File code\run_all.ps1 -Data D:\research-data         # or -Stage data|generate|perplexity|analysis|paper
```
Put these downloads in the data folder first:
- `hansard_au\corpus_1998_to_2025.parquet` from Zenodo record 17351233 (Australian Hansard)
- `learner\persuade_2.0_train.csv` from github.com/scrosseye/persuade_corpus_2.0
- `learner\liang_toefl_all_data.json` (`all_data.json` from HF `WxWx/ChatGPT-Detector-Bias`) and
  `learner\liang_us8th.json` (`HewlettStudentEssay_real_88/data.json` from the authors' GitHub repository)

The scripts fetch RAID and rebuild the paper's exact arXiv sample from the released ids (`fetch_arxiv.py ids`; the
ids carry their version, so the abstracts are the ones analysed). To reproduce the analyses exactly rather than regenerate the
texts, unpack `data/generated/*.gz` into the data folder: the 2026-model texts cannot be regenerated bit for bit
(no decoding control), and local-model outputs depend on hardware and Ollama version (0.40.3 was used; models
llama3.1:8b, qwen3:8b, gemma3:12b, mistral:7b, gpt-oss:20b, phi4:14b, granite3.3:8b, and for the vintage analysis
only llama2:7b, vicuna:7b, qwen3.5:9b, gemma4:12b and granite4.2:8b; temperature 0.8, fixed seeds). The Hansard results are the exception: the LLM revisions of real speeches are not
released (Hansard text may not be adapted), so those results need the speech revisions regenerated: after unpacking, run the stages `data`, `perplexity`,
`analysis` and `paper`, and run `generate` only to regenerate the withheld local-model speech revisions (it skips
existing texts; the 2026 model's revisions cannot be regenerated). The paper compiles with
[Tectonic](https://tectonic-typesetting.github.io): `powershell -File paper\build.ps1`.

## Licences
- Code: MIT (`LICENSE`), except the ACL style files in `paper/` (`acl.sty`, `acl_natbib.bst`), which keep the
  ACL template's licence.
- Paper text, figures, results, review reports, literature notes and the analysis plan: CC BY 4.0.
- Data: per file in `data/README.md`. Generated abstracts: CC BY 4.0; speech generations: CC BY-NC 4.0 (the
  revisions of real speeches are not released); essay generations: CC BY-NC-SA 4.0, as they derive from
  PERSUADE 2.0.
- Source datasets keep their own licences: arXiv metadata, including titles and abstracts (CC0); Australian
  Hansard (Parliament of Australia, CC BY-NC-ND 4.0), via the database of Katz and Alexander (CC BY 4.0); PERSUADE 2.0
  (CC BY-NC-SA 4.0), RAID and the Hugging Face release of Liang et al. 2023 (MIT). The Liang et al. US 8th-grade
  essays come from the authors' GitHub repository (no licence file; its README shows an MIT badge) and are not
  redistributed here.

Cite via `CITATION.cff` (GitHub's "Cite this repository" button).
