$ErrorActionPreference = "Stop"

$here = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $here

python -m pip install -r .\requirements-build.txt

# EXE console (comodo per CLI). Esegui `AccessibileDaZero.exe --help`.
pyinstaller `
  --noconfirm `
  --clean `
  --onefile `
  --name "AccessibileDaZero" `
  .\accessibile_da_zero\cli.py

Write-Host "OK: EXE creato in $here\\dist\\AccessibileDaZero.exe"

