# CPU queue: waits until no generation (GPU) job is running, then runs every analysis job one at a time.
# Never overlaps GPU and heavy CPU work (two system crashes on this machine under combined load).
$py = "F:\downloads\Outreach and other plans\research-paper\.venv\Scripts\python.exe"
$code = "F:\downloads\Outreach and other plans\research-paper\code"
$d = "F:\research-data"
while (Get-CimInstance Win32_Process -Filter "Name='python.exe'" | Where-Object CommandLine -like "*generate.py*") { Start-Sleep 60 }
Get-Process ollama* -ErrorAction SilentlyContinue | Stop-Process -Force -Confirm:$false   # free the GPU
Set-Location $code
foreach ($job in "corpus", "essay") { "=== $job"; & $py analysis.py $d $job 2>&1 | Select-String -NotMatch "Warning" | Select-Object -Last 3 }
"=== perplexity"; & $py perplexity.py $d 2>&1 | Select-Object -Last 2
foreach ($job in "essay_perplexity", "hansard", "arxiv", "gensets", "drift", "nodash", "control") {
    "=== $job"; & $py analysis.py $d $job 2>&1 | Select-String -NotMatch "Warning" | Select-Object -Last 3
}
& $py make_numbers.py; & $py figures.py
"cpu queue done"
