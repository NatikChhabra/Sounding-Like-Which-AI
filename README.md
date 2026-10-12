# Machine-Style Overlap

How much human writing sounds like AI, and how much of that was already true before ChatGPT?

This repository holds the data pipeline, analysis and paper for a study of **Machine-Style Overlap (MSO)**:
the share of human-written documents whose style is at least as typical of LLM output as of pre-2022 human
writing. The paper was written by an AI system (Claude) and verified by the human author; see
`paper/AI_DISCLOSURE.md` and the git history (human edits are commits labelled `HUMAN-EDIT:`).

## Layout
| Path | What |
|---|---|
| `PLAN.md` | Project tracker and checklist |
| `preregistration.md` | Hypotheses and analysis plan, frozen before the full run |
| `lit/` | Verified literature notes (01–04) and the citation checklist |
| `code/` | All code; every number in the paper comes from here |
| `results/` | Tables and figures written by `code/analysis.py` |
| `paper/` | Manuscript, disclosure statement, cover letters |
| `F:\research-data\` (not in git) | Raw and intermediate data, rebuilt by the steps below |

## Reproduce
```
py -3.12 -m venv .venv
.venv\Scripts\pip install pandas pyarrow scikit-learn statsmodels spacy matplotlib duckdb
.venv\Scripts\python -m spacy download en_core_web_sm
python code/fetch_arxiv.py DATA/arxiv                         # stratified arXiv sample, ~1.5 h
python code/build_sources.py {essay|arxiv|hansard} DATA       # human corpora + train/score split
python code/generate.py DATA/seed_<genre>.parquet DATA/llm_<genre>.jsonl 150   # needs Ollama
python code/analysis.py DATA                                  # all tables and figures
```
Models (Ollama): llama3.1:8b, qwen3:8b, gemma3:12b, mistral:7b, gpt-oss:20b; temperature 0.8, fixed seeds.

## Data sources and licences
- arXiv metadata via the arXiv API (metadata CC0)
- Australian Hansard 1998–2025, Zenodo record 17351233 (CC BY 4.0)
- PERSUADE 2.0, Crossley et al. 2024 (CC BY-NC-SA 4.0)
- Liang et al. 2023 TOEFL / US essays, HF `WxWx/ChatGPT-Detector-Bias` (MIT)
- RAID, Dugan et al. 2024, HF `liamdugan/raid` (MIT)
