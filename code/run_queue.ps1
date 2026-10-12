# GPU queue: wait for essay generation, then Hansard, then arXiv (after the arXiv sampler finishes).
$py = "F:\downloads\Outreach and other plans\research-paper\.venv\Scripts\python.exe"
$code = "F:\downloads\Outreach and other plans\research-paper\code"
$d = "F:\research-data"
function Wait-For($pattern) {
    while (Get-CimInstance Win32_Process -Filter "Name='python.exe'" | Where-Object CommandLine -like $pattern) { Start-Sleep 60 }
}
Wait-For "*generate.py*seed_essay*"
& $py "$code\generate.py" "$d\seed_essay.parquet" "$d\llm_essay.jsonl" 150   # finish any skipped essay cells
& $py "$code\generate.py" "$d\seed_hansard.parquet" "$d\llm_hansard.jsonl" 150
Wait-For "*fetch_arxiv.py*"
& $py "$code\build_sources.py" arxiv $d
& $py "$code\generate.py" "$d\seed_arxiv.parquet" "$d\llm_arxiv.jsonl" 150
"queue done"
