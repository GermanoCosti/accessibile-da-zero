# Accessibile Da Zero

Generatore (Python) di file **DOCX** e **HTML** gia impostati con una struttura accessibile (titoli, liste, tabelle, link descrittivi) + checklist finale.

Obiettivo: partire con documenti "giusti" fin dall'inizio, invece di correggere dopo.

## Download e uso rapido (Windows)
Se non vuoi installare Python, in futuro questo repo potra' avere un EXE in Releases. Per ora:

## Uso (sviluppo)
```powershell
cd python-app
python -m pip install -e .
accessibile-da-zero --help
```

## Uso senza installare (fallback)
Se `pip install -e .` ti da problemi, puoi eseguire direttamente:
```powershell
cd python-app
python -m accessibile_da_zero --help
python -m accessibile_da_zero new-pack --dir ..\\examples --nome demo --titolo "Documento accessibile"
```

## Crea un DOCX
```powershell
accessibile-da-zero new-docx --out .\\examples\\documento-accessibile.docx --titolo "Relazione tecnica" --lingua it-IT
```

## Crea un HTML
```powershell
accessibile-da-zero new-html --out .\\examples\\pagina-accessibile.html --titolo "Pagina informativa" --lingua it
```

## Crea un pacchetto (DOCX + HTML + Checklist)
```powershell
accessibile-da-zero new-pack --dir .\\examples --nome "pacchetto-demo"
```

## Note importanti (onesta')
- Questo tool imposta **struttura e contenuti modello**: non puo' garantire accessibilita' al 100% se poi il testo viene scritto male (es. link "clicca qui", tabelle senza intestazioni, immagini senza descrizione).
- Per il **PDF**: la qualita' dipende dall'export (Word/LibreOffice) e dalle impostazioni.

## Autore
Creato e mantenuto da **Germano Costi**.
