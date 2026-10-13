# v4b: after run_v4.ps1, redo the jobs that depend on Hansard (its first run crashed in the dispersion step) and the
# vintage job (first run stopped: original generators were seeded from the first arXiv sample, now in the pool).
$py = "F:\downloads\Outreach and other plans\research-paper\.venv\Scripts\python.exe"
$d = "F:\research-data"
Set-Location "F:\downloads\Outreach and other plans\research-paper\code"
while (Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" | Where-Object { $_.CommandLine -like "*run_v4.ps1*" }) { Start-Sleep 60 }
foreach ($job in "hansard", "control", "robust4", "vintage") {
    "=== $job"
    & $py analysis.py $d $job *> "$d\logs\$job.v4b.log"
    Select-String -Path "$d\logs\$job.v4b.log" -CaseSensitive -Pattern "Traceback|[A-Za-z]Error: " | Select-Object -First 3 | ForEach-Object { "ERR $job : $($_.Line)" }
}
& $py make_numbers.py *> "$d\logs\make_numbers.log"
& $py figures.py *> "$d\logs\figures.log"
"v4b done"
