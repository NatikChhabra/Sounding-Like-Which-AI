# v4: full re-run after the cleaning fix ('Title:' lines dropped). Waits for GPU generation; CPU jobs sequential.
$py = "F:\downloads\Outreach and other plans\research-paper\.venv\Scripts\python.exe"
$d = "F:\research-data"
$inv = Join-Path $PSScriptRoot "invalidate_title.py"  # one-off cache cleanup, kept here for the record
Set-Location "F:\downloads\Outreach and other plans\research-paper\code"
New-Item -ItemType Directory -Force "$d\logs" | Out-Null
"=== generate (resumes)"
& $py generate.py "$d\seed_arxiv.parquet" "$d\llm_arxiv_old.jsonl" 150 "llama2:7b,vicuna:7b,granite4.2:8b,qwen3.5:9b,gemma4:12b" *> "$d\logs\generate_vintage.log"
"=== invalidate"
& $py -I $inv $d
function Run($name, [scriptblock]$cmd) {
    "=== $name"
    & $cmd *> "$d\logs\$name.log"
    Select-String -Path "$d\logs\$name.log" -CaseSensitive -Pattern "Traceback|[A-Za-z]Error: " | Select-Object -First 3 | ForEach-Object { "ERR $name : $($_.Line)" }
}
Run "ppl_qwen" { & $py perplexity.py $d }
$env:PPL_MODEL = "gpt2"; Run "ppl_gpt2" { & $py perplexity.py $d }; Remove-Item Env:\PPL_MODEL
foreach ($job in "essay", "essay_perplexity") { Run $job { & $py analysis.py $d $job } }
$env:PPL_MODEL = "gpt2"; Run "essay_perplexity_gpt2" { & $py analysis.py $d essay_perplexity }; Remove-Item Env:\PPL_MODEL
foreach ($job in "hansard", "arxiv", "gensets", "drift", "nodash", "control", "vintage", "robust3", "robust4") {
    Run $job { & $py analysis.py $d $job }
}
& $py make_numbers.py
& $py figures.py
"v4 done"
