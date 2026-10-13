# v3b: pre-ChatGPT-data open models (GPU), then CPU analyses. Never GPU and heavy CPU at once.
$py = "F:\downloads\Outreach and other plans\research-paper\.venv\Scripts\python.exe"
$d = "F:\research-data"
Set-Location "F:\downloads\Outreach and other plans\research-paper\code"
# wait for run_v3.ps1 (perplexity on CPU) to finish
while (Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" | Where-Object { $_.CommandLine -like "*run_v3.ps1*" }) { Start-Sleep 60 }
"=== generate old models"; & $py generate.py "$d\seed_arxiv.parquet" "$d\llm_arxiv_old.jsonl" 150 "llama2:7b,vicuna:7b" 2>&1 | Select-Object -Last 3
foreach ($job in "robust3", "robust4", "vintage") { "=== $job"; & $py analysis.py $d $job 2>&1 | Select-String -Pattern "Error|Traceback|assert" -Context 0,3 }
& $py make_numbers.py
"v3b done"
