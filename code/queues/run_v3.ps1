# v3 analyses (CPU only, sequential).
$py = "F:\downloads\Outreach and other plans\research-paper\.venv\Scripts\python.exe"
$d = "F:\research-data"
Set-Location "F:\downloads\Outreach and other plans\research-paper\code"
foreach ($job in "vintage", "robust3", "overlap") { "=== $job"; & $py analysis.py $d $job 2>&1 | Select-String -Pattern "Error|Traceback" }
$env:PPL_MODEL = "gpt2"
"=== perplexity gpt2"; & $py perplexity.py $d 2>&1 | Select-Object -Last 1
"=== essay_perplexity gpt2"; & $py analysis.py $d essay_perplexity 2>&1 | Select-String -Pattern "Error|Traceback"
Remove-Item Env:\PPL_MODEL
& $py make_numbers.py
"v3 done"
