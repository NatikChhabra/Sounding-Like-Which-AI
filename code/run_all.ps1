# Full pipeline, in order. Usage: powershell -File code\run_all.ps1 -Data F:\research-data [-Stage analysis]
# Stages: data, generate, perplexity, analysis, paper. Each stage is resumable (caches are keyed by document id).
# Run GPU stages (generate) and heavy CPU stages separately on a desktop machine; the scripts in code\queues are the
# exact batches used for the paper, kept for the record.
param([Parameter(Mandatory = $true)][string]$Data, [string]$Stage = "all")
$ErrorActionPreference = "Stop"
$root = Split-Path $PSScriptRoot -Parent
$py = Join-Path $root ".venv\Scripts\python.exe"
Set-Location $PSScriptRoot

function Step($name, [scriptblock]$cmd) { "=== $name"; & $cmd; if ($LASTEXITCODE) { throw "$name failed" } }

if ($Stage -in "all", "data") {
    Step "arXiv sample" { & $py fetch_arxiv.py "$Data\arxiv_v2" }
    Step "RAID generations" { & $py fetch_raid.py "$Data\raid_arxiv.jsonl" }
    Step "RAID human abstracts" { & $py fetch_raid.py "$Data\raid_arxiv_human.jsonl" human }
    # Hansard (Zenodo 17351233) and PERSUADE 2.0 / Liang et al. essays must be downloaded first; see README
    foreach ($g in "essay", "arxiv", "hansard") { Step "sources $g" { & $py build_sources.py $g $Data } }
}
if ($Stage -in "all", "generate") {  # needs Ollama; the 2026-model texts come from code\claude_prompts.py
    $main = "llama3.1:8b,qwen3:8b,gemma3:12b,mistral:7b,gpt-oss:20b,phi4:14b,granite3.3:8b"
    foreach ($g in "essay", "hansard", "arxiv") { Step "generate $g" { & $py generate.py "$Data\seed_$g.parquet" "$Data\llm_$g.jsonl" 150 $main } }
    Step "generate vintage-only models" {
        & $py generate.py "$Data\seed_arxiv.parquet" "$Data\llm_arxiv_old.jsonl" 150 "llama2:7b,vicuna:7b,granite4.2:8b,qwen3.5:9b,gemma4:12b" }
}
if ($Stage -in "all", "perplexity") {
    Step "perplexity Qwen2.5-0.5B" { & $py perplexity.py $Data }
    $env:PPL_MODEL = "gpt2"; Step "perplexity GPT-2" { & $py perplexity.py $Data }; Remove-Item Env:\PPL_MODEL
}
if ($Stage -in "all", "analysis") {
    foreach ($job in "corpus", "essay", "essay_perplexity") { Step $job { & $py analysis.py $Data $job } }
    $env:PPL_MODEL = "gpt2"; Step "essay_perplexity gpt2" { & $py analysis.py $Data essay_perplexity }; Remove-Item Env:\PPL_MODEL
    foreach ($job in "hansard", "arxiv", "gensets", "drift", "nodash", "control", "vintage", "vsummary", "robust3",
                     "robust4", "vquarter", "vpeak", "ablate", "robust5", "fastdetect", "overlap") {
        Step $job { & $py analysis.py $Data $job }
    }
}
if ($Stage -in "all", "paper") {
    Step "numbers" { & $py make_numbers.py }
    Step "figures" { & $py figures.py }
    Step "bibliography" { & $py fetch_bib.py (Join-Path $root "lit\citations.txt") }
    Set-Location (Join-Path $root "paper")
    Step "compile" { tectonic main.tex }
}
"done"
