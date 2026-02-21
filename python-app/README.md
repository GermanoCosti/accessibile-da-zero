# Accessibile Da Zero (Python)

## Installazione (sviluppo)
```powershell
cd python-app
python -m pip install -e .
```

## Download EXE (Windows)
Se vuoi usare l'app senza installare Python:
- https://github.com/GermanoCosti/accessibile-da-zero/releases/latest
- `AccessibileDaZeroGUI.exe` (consigliato, interfaccia grafica)
- `AccessibileDaZero.exe` (CLI)

## Esecuzione senza installare (fallback)
```powershell
cd python-app
python -m accessibile_da_zero --help
```

## Comandi
```powershell
accessibile-da-zero --help
accessibile-da-zero new-docx --out .\\documento.docx --titolo "Titolo" --lingua it-IT
accessibile-da-zero new-html --out .\\pagina.html --titolo "Titolo" --lingua it
accessibile-da-zero new-pack --dir .\\output --nome demo
accessibile-da-zero-gui
```
