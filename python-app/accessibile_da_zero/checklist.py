from __future__ import annotations


def build_checklist_markdown() -> str:
    # Checklist pratica: serve a ricordare cosa controllare prima di pubblicare.
    lines: list[str] = []
    lines.append("# Checklist accessibilita' (prima di pubblicare)")
    lines.append("")
    lines.append("## Struttura")
    lines.append("- [ ] Il documento ha un **Titolo** chiaro (non solo nome file).")
    lines.append("- [ ] I titoli usano stili/heading (H1/H2...) e non testo ingrandito a mano.")
    lines.append("- [ ] La lingua del documento e' corretta (italiano).")
    lines.append("")
    lines.append("## Testo e link")
    lines.append("- [ ] I link sono descrittivi (evitare \"clicca qui\").")
    lines.append("- [ ] Il testo e' leggibile (frasi brevi, niente tutto MAIUSCOLO).")
    lines.append("")
    lines.append("## Immagini")
    lines.append("- [ ] Ogni immagine ha una descrizione (testo alternativo).")
    lines.append("- [ ] Se l'immagine e' decorativa, e' marcata come decorativa.")
    lines.append("")
    lines.append("## Tabelle")
    lines.append("- [ ] Le tabelle hanno intestazioni di colonna/riga (header).")
    lines.append("- [ ] Evita celle unite e layout complicati se non necessario.")
    lines.append("")
    lines.append("## Colori e contrasto")
    lines.append("- [ ] Non usi solo il colore per trasmettere informazioni (es. rosso/verde).")
    lines.append("- [ ] Il contrasto e' sufficiente (testo su sfondo).")
    lines.append("")
    lines.append("## Export PDF (se serve)")
    lines.append("- [ ] PDF generato da DOCX mantenendo tag/struttura (se disponibile).")
    lines.append("- [ ] Controllo rapido con lettore schermo o verificatore (se disponibile).")
    lines.append("")
    return "\n".join(lines)

