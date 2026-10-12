# v4: full re-run after the cleaning fix ('Title:' lines dropped). Waits for GPU generation; CPU jobs sequential.
$py = "F:\downloads\Outreach and other plans\research-paper\.venv\Scripts\python.exe"
$d = "F:\research-data"
$inv = "C:\Users\<user>\AppData\Local\Temp\claude\F--downloads-Outreach-and-other-plans\edfd1841-3fd5-443d-a6f6-04508c35831b\scratchpad\invalidate_title.py"
Set-Location "F:\downloads\Outreach and other plans\research-paper\code"
New-Item -ItemType Directory -Force "$d\logs" | Out-Null
while (Get-CimInstance Win32_Process -Filter "Name='python.exe'" | Where-Object { $_.CommandLine -like "*generate.py*" }) { Start-Sleep 60 }
"=== generation finished"
& $py $inv $d
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
