# v5b: after run_v5.ps1, the quarterly vintage job (first run failed on a numpy string call).
$py = "F:\downloads\Outreach and other plans\research-paper\.venv\Scripts\python.exe"
$d = "F:\research-data"
Set-Location "F:\downloads\Outreach and other plans\research-paper\code"
while (Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" | Where-Object { $_.CommandLine -like "*run_v5.ps1*" }) { Start-Sleep 60 }
"=== vquarter"
& $py analysis.py $d vquarter *> "$d\logs\vquarter.v5b.log"
Select-String -Path "$d\logs\vquarter.v5b.log" -CaseSensitive -Pattern "Traceback|[A-Za-z]Error: " | Select-Object -First 3 | ForEach-Object { "ERR vquarter : $($_.Line)" }
& $py make_numbers.py *> "$d\logs\make_numbers.v5b.log"
& $py figures.py *> "$d\logs\figures.v5b.log"
"v5b done"
