$ErrorActionPreference = "Stop"

$here = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $here

python -m pip install -r .\requirements-build.txt

# EXE console (CLI)
pyinstaller `
  --noconfirm `
  --clean `
  --onefile `
  --name "AccessibileDaZero" `
  .\accessibile_da_zero\cli.py

# EXE grafico (GUI)
pyinstaller `
  --noconfirm `
  --clean `
  --onefile `
  --windowed `
  --name "AccessibileDaZeroGUI" `
  .\accessibile_da_zero\gui.py

Write-Host "OK: EXE creati in $here\\dist\\"
