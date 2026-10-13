# Release data

Written by `code/export_data.py` from the working data folder. Human documents are given as ids (plus arXiv
titles and Hansard opening sentences), never as full third-party texts, so they must be re-fetched from their
sources; everything the study generated is included in full.

## `generated/`: every LLM text used in the paper (gzipped JSON lines)
| File | Contents | Licence |
|---|---|---|
| `llm_arxiv.jsonl.gz` | Abstracts from the 7 local models and the 2026 model (P1 title-only, P2 revision, P3 "avoid AI phrasing") | CC BY 4.0 (prompts built from arXiv metadata, CC0) |
| `llm_arxiv_old.jsonl.gz` | Vintage-only models: Llama-2-Chat 7B, Vicuna 7B v1.5, Qwen3.5 9B, Gemma 4 12B, Granite 4.2 8B | CC BY 4.0 |
| `llm_hansard.jsonl.gz` | Parliamentary speeches (prompts and revisions built from Australian Hansard) | CC BY 4.0, derived from Hansard (CC BY 4.0; Katz and Alexander, Zenodo 17351233) |
| `llm_essay.jsonl.gz` | Student-style essays; P2 rows revise PERSUADE 2.0 essays | **CC BY-NC-SA 4.0** (share-alike, derived from PERSUADE 2.0) |

Fields: `src_id` (the human document a prompt was built from), `genre`, `model`, `prompt` (P1/P2/P3), `text`.
RAID generations are not repeated here; `code/fetch_raid.py` downloads them (MIT).

## `samples/`: exact samples and train/score splits
| File | Contents |
|---|---|
| `arxiv_v2_sample_ids.csv.gz` | The stratified arXiv sample used for all measurements: id, field, primary category, first-submission and latest-version dates |
| `arxiv_sample_ids.csv.gz` | The first sample, which seeded the prompts of the original generators |
| `arxiv_split.csv.gz` | Every analysed abstract: id, date, field, title, train/score pool |
| `hansard_split.csv.gz` | Every analysed speech: id (date:order), date, speaker id, opening sentence, pool |
| `essay_split.csv.gz` | Every analysed PERSUADE essay: id, ELL status, pool (texts and scores stay with PERSUADE) |
| `arxiv_v1_seed_sources.jsonl.gz` | The 434 source abstracts (CC0) of generations seeded from the first sample that are not in the analysed corpus; the vintage analysis needs them |

Notes:
- arXiv ids: the `*_sample_ids` files hold the API's versioned id (e.g. `1501.02046v1`), and
  `code/fetch_arxiv.py ids` re-fetches exactly that version. Split files and generations use `arxiv:` plus the
  unversioned id.
- Hansard: generations made before a bug fix carry the speaker id as `src_id` (2,167 rows) and 113 rows have
  none (analysis plan, deviation 5); they are still grouped by speaker. Some speeches have an empty party field.
