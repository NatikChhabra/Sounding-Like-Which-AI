# v5: re-run after the second cleaning fix (inline labels, keyword lines, word counts) + round-3 analyses.
# CPU only, sequential.
$py = "F:\downloads\Outreach and other plans\research-paper\.venv\Scripts\python.exe"
$d = "F:\research-data"
Set-Location "F:\downloads\Outreach and other plans\research-paper\code"
function Run($name, [scriptblock]$cmd) {
    "=== $name"
    & $cmd *> "$d\logs\$name.v5.log"
    Select-String -Path "$d\logs\$name.v5.log" -CaseSensitive -Pattern "Traceback|[A-Za-z]Error: " | Select-Object -First 3 | ForEach-Object { "ERR $name : $($_.Line)" }
}
Run "ppl_qwen" { & $py perplexity.py $d }
$env:PPL_MODEL = "gpt2"; Run "ppl_gpt2" { & $py perplexity.py $d }; Remove-Item Env:\PPL_MODEL
foreach ($job in "essay", "essay_perplexity") { Run $job { & $py analysis.py $d $job } }
$env:PPL_MODEL = "gpt2"; Run "essay_perplexity_gpt2" { & $py analysis.py $d essay_perplexity }; Remove-Item Env:\PPL_MODEL
foreach ($job in "hansard", "arxiv", "gensets", "drift", "nodash", "control", "vintage", "vsummary", "robust3", "robust4",
                 "vquarter", "ablate", "robust5", "fastdetect") {
    Run $job { & $py analysis.py $d $job }
}
& $py make_numbers.py *> "$d\logs\make_numbers.v5.log"
& $py figures.py *> "$d\logs\figures.v5.log"
"v5 done"
