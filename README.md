# Machine-Style Overlap

How much human writing sounds like AI, how much already did before ChatGPT, and which AI does it sound like?

This repository holds the data pipeline, analysis and paper for a study of **Machine-Style Overlap (MSO)**: the
share of documents that a calibrated classifier on content-word-free style features judges at least as likely
to come from LLM output as from pre-ChatGPT human writing. The main corpus is a stratified sample of arXiv
abstracts from eight non-physics archives (2015-2026); Australian parliamentary speech and US student essays
are secondary. Reference generators range from models whose training data predate ChatGPT to a 2026 model.

The study was carried out by an AI system (Claude Opus 5.5, via Claude Code) under the human author's
direction; no human has edited the text so far. See `paper/AI_DISCLOSURE.md` and the git history (AI-written
commits say so; human edits are commits labelled `HUMAN-EDIT:`).

## Layout
| Path | What |
|---|---|
| `PLAN.md` | Project tracker and checklist |
| `preregistration.md` | Hypotheses and analysis plan, committed before any result (never frozen with a third party), with the full deviation log |
| `lit/` | Literature notes, citation list, citation-verification reports, spot-check sheet |
| `code/` | All code; every reported result in the paper comes from here |
| `results/` | Tables written by `code/analysis.py`; `numbers.tex` feeds every result into the paper |
| `paper/` | Manuscript, figures, disclosure statement, simulated review rounds |
| `F:\research-data\` (not in git) | Raw and intermediate data, rebuilt by the steps below |

## Reproduce
```
py -3.12 -m venv .venv
.venv\Scripts\pip install pandas pyarrow scikit-learn statsmodels spacy matplotlib transformers torch sentence-transformers
.venv\Scripts\python -m spacy download en_core_web_sm
python code/fetch_arxiv.py DATA/arxiv_v2                      # stratified arXiv sample (API, ~1.5 h)
python code/fetch_raid.py DATA/raid_arxiv.jsonl                # RAID generations (no attack)
python code/fetch_raid.py DATA/raid_arxiv_human.jsonl human    # RAID human abstracts (marker baseline only)
python code/build_sources.py {essay|arxiv|hansard} DATA        # human corpora + train/score split
python code/generate.py DATA/seed_<genre>.parquet DATA/llm_<genre>.jsonl 150 "<models>"   # needs Ollama
python code/generate.py DATA/seed_arxiv.parquet DATA/llm_arxiv_old.jsonl 150 "llama2:7b,vicuna:7b"
python code/claude_prompts.py DATA <genre>                     # 2026-model prompt batches (answered by sub-agents)
python code/perplexity.py DATA                                 # Qwen2.5-0.5B; set PPL_MODEL=gpt2 for GPT-2
python code/analysis.py DATA <job>                             # corpus, essay, essay_perplexity, arxiv, hansard,
                                                               # gensets, drift, nodash, control, vintage,
                                                               # robust3, robust4, overlap
python code/make_numbers.py && python code/figures.py
```
Local models (Ollama): llama3.1:8b, qwen3:8b, gemma3:12b, mistral:7b, gpt-oss:20b, phi4:14b, granite3.3:8b,
and for the vintage analysis llama2:7b and vicuna:7b; temperature 0.8, fixed seeds. The paper compiles with
Tectonic from `paper/main.tex`.

## Data sources and licences
- arXiv metadata via the arXiv API (metadata CC0)
- Australian Hansard 1998-2025, Zenodo record 17351233 (CC BY 4.0)
- PERSUADE 2.0, Crossley et al. 2024 (CC BY-NC-SA 4.0; share-alike applies to derived data)
- Liang et al. 2023 TOEFL / US college essays, HF `WxWx/ChatGPT-Detector-Bias` (MIT); their US 8th-grade essays
  come from the authors' GitHub repository (no licence stated; texts not redistributed)
- RAID, Dugan et al. 2024, HF `liamdugan/raid` (MIT)
