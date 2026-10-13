# GPU queue 2: after the Phi-4 / Granite downloads finish, generate all three genres with them.
$py = "F:\downloads\Outreach and other plans\research-paper\.venv\Scripts\python.exe"
$code = "F:\downloads\Outreach and other plans\research-paper\code"
$d = "F:\research-data"
while (Get-Process ollama -ErrorAction SilentlyContinue | Where-Object { $_.CommandLine -like "*pull*" -or (Get-CimInstance Win32_Process -Filter "ProcessId=$($_.Id)").CommandLine -like "*pull*" }) { Start-Sleep 60 }
foreach ($g in "essay", "hansard", "arxiv") {
    & $py "$code\generate.py" "$d\seed_$g.parquet" "$d\llm_$g.jsonl" 150 "phi4:14b,granite3.3:8b"
}
"queue2 done"
