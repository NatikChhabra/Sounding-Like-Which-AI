# v3c: vintage-only open models (pre-ChatGPT data + 2026) on GPU, then CPU analyses. Never GPU and heavy CPU at once.
$py = "F:\downloads\Outreach and other plans\research-paper\.venv\Scripts\python.exe"
$d = "F:\research-data"
Set-Location "F:\downloads\Outreach and other plans\research-paper\code"
while (Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" | Where-Object { $_.CommandLine -like "*run_v3.ps1*" }) { Start-Sleep 60 }
while (Get-CimInstance Win32_Process -Filter "Name='ollama.exe'" | Where-Object { $_.CommandLine -like "*pull*" }) { Start-Sleep 60 }
"=== generate vintage models"
& $py generate.py "$d\seed_arxiv.parquet" "$d\llm_arxiv_old.jsonl" 150 "llama2:7b,vicuna:7b,granite4.2:8b,qwen3.5:9b,gemma4:12b" 2>&1 | Select-Object -Last 6
foreach ($job in "robust3", "robust4", "vintage") { "=== $job"; & $py analysis.py $d $job 2>&1 | Select-String -Pattern "Error|Traceback|assert" -Context 0,3 }
& $py make_numbers.py
& $py figures.py
"v3c done"
