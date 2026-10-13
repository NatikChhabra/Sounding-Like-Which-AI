# Release data

Written by `code/export_data.py` from the working data folder. Human documents are given as ids (plus arXiv
titles and Hansard opening sentences), never as full third-party texts, so they must be re-fetched from their
sources; everything the study generated is included in full, except the revisions of real speeches (below).

## `generated/`: the LLM texts used in the paper (gzipped JSON lines)
| File | Contents | Licence |
|---|---|---|
| `llm_arxiv.jsonl.gz` | Abstracts from the 7 local models and the 2026 model (P1 title-only, P2 revision, P3 "avoid AI phrasing") | CC BY 4.0 (prompts built from arXiv metadata, CC0) |
| `llm_arxiv_old.jsonl.gz` | Vintage-only models: Llama-2-Chat 7B, Vicuna 7B v1.5, Qwen3.5 9B, Gemma 4 12B, Granite 4.2 8B | CC BY 4.0 |
| `llm_hansard.jsonl.gz` | Parliamentary speeches written from a topic (P1, P3). The P2 revisions of real speeches are left out, as Hansard text may not be adapted; `hansard_p2_rows.csv.gz` lists them | CC BY-NC 4.0 (prompts built from Australian Hansard, see below) |
| `hansard_p2_rows.csv.gz` | `src_id`, `model`, `prompt` of the 1,202 withheld P2 rows; the local models' rows can be regenerated with `code/generate.py` (fixed seeds), the 150 rows of the 2026 model cannot | CC0 |
| `llm_essay.jsonl.gz` | Student-style essays; P2 rows revise PERSUADE 2.0 essays | **CC BY-NC-SA 4.0** (share-alike, derived from PERSUADE 2.0) |

Fields: `src_id` (the human document a prompt was built from), `genre`, `model`, `prompt` (P1/P2/P3), `text`.
RAID generations are not repeated here; `code/fetch_raid.py` downloads them (MIT).
Because the P2 speech revisions are withheld, the Hansard results (a secondary comparison in the paper) cannot be
recomputed exactly from this release; the arXiv and essay results can.

Rows are outputs of models under their own licences (Llama 2 and Vicuna: Llama 2 Community License; Llama 3.1:
Llama 3.1 Community License; Gemma 3: Gemma Terms of Use; the others: Apache 2.0 or MIT; Claude: Anthropic's
terms). Some of these restrict using outputs to train other models; check them before doing so.

## `samples/`: exact samples and train/score splits
| File | Contents | Licence |
|---|---|---|
| `arxiv_v2_sample_ids.csv.gz` | The stratified arXiv sample used for all measurements: id, field, primary category, first-submission and latest-version dates | CC0 |
| `arxiv_sample_ids.csv.gz` | The first sample, which seeded the prompts of the original generators | CC0 |
| `arxiv_split.csv.gz` | Every analysed abstract: `id`, `date`, `group` (field), `grp`, `pool` (train/score), `title` | CC0 |
| `hansard_split.csv.gz` | Every analysed speech: `id` (date:order), `date`, `group` (party; empty for 402 rows), `grp` (speaker id), `pool`, `title` (opening sentence) | Opening sentences © Parliament of Australia, CC BY-NC-ND 4.0, unmodified but truncated, taken from the database of Katz and Alexander (Zenodo 17351233, CC BY 4.0) after sampling |
| `essay_split.csv.gz` | Every analysed PERSUADE essay: id, ELL status, pool (texts and scores stay with PERSUADE) | CC BY-NC-SA 4.0 (from PERSUADE 2.0) |
| `arxiv_v1_seed_sources.jsonl.gz` | The 434 source abstracts (CC0) of generations seeded from the first sample that are not in the analysed corpus; the vintage analysis needs them | CC0 |

Notes:
- arXiv ids: the `*_sample_ids` files hold the API's versioned id (e.g. `1501.02046v1`), and
  `code/fetch_arxiv.py ids` re-fetches exactly that version. Split files and generations use `arxiv:` plus the
  unversioned id.
- Hansard: generations made before a bug fix carry the speaker id as `src_id` (2,167 rows, 1,448 of them released) and
  113 rows (80 released) have none (analysis plan, deviation 5); they are still grouped by speaker. Some speeches have an empty party field.
