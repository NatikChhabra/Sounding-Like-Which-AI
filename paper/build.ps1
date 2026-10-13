# Rebuild the paper from the results: numbers and figures are regenerated first, so the PDF can never show stale
# values. Usage: powershell -File paper\build.ps1   (needs tectonic on PATH or at F:\tools\tectonic)
$ErrorActionPreference = "Stop"
$root = Split-Path $PSScriptRoot -Parent
$py = Join-Path $root ".venv\Scripts\python.exe"
$tec = if (Get-Command tectonic -ErrorAction SilentlyContinue) { "tectonic" } else { "F:\tools\tectonic\tectonic.exe" }
Push-Location (Join-Path $root "code")
& $py make_numbers.py; if ($LASTEXITCODE) { throw "make_numbers failed" }
& $py -c "import make_numbers as M, sys; m = M.missing(); print('missing keys:', m); sys.exit(1 if m else 0)"
if ($LASTEXITCODE) { throw "paper uses result keys that do not exist" }
& $py figures.py; if ($LASTEXITCODE) { throw "figures failed" }
Pop-Location
Push-Location $PSScriptRoot
$ErrorActionPreference = "Continue"  # tectonic writes harmless fontconfig notes to stderr
foreach ($doc in "main", "preprint") {
    $start = Get-Date
    $log = & $tec "$doc.tex" 2>&1 | ForEach-Object { "$_" }
    $log | Select-String -Pattern "error:|Overfull|undefined" | Where-Object { $_ -notmatch "Fontconfig" }
    if (-not (Test-Path "$doc.pdf") -or (Get-Item "$doc.pdf").LastWriteTime -lt $start) { throw "$doc.pdf was not rebuilt" }
}
Pop-Location
"built main.pdf (anonymous review version) and preprint.pdf (named)"
