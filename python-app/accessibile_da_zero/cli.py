from __future__ import annotations

import argparse
from pathlib import Path

from accessibile_da_zero import APP_AUTORE, APP_NOME, APP_VERSIONE
from accessibile_da_zero.checklist import build_checklist_markdown
from accessibile_da_zero.docx_gen import write_accessible_docx
from accessibile_da_zero.html_gen import build_accessible_html


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="accessibile-da-zero",
        description=f"{APP_NOME} - {APP_AUTORE}",
    )
    parser.add_argument("--version", action="store_true", help="Mostra versione e esce")
    sub = parser.add_subparsers(dest="cmd")

    p_docx = sub.add_parser("new-docx", help="Crea un DOCX accessibile di base")
    p_docx.add_argument("--out", required=True, help="Percorso file .docx")
    p_docx.add_argument("--titolo", required=True, help="Titolo documento")
    p_docx.add_argument("--lingua", default="it-IT", help="Lingua (es. it-IT)")

    p_html = sub.add_parser("new-html", help="Crea un HTML accessibile di base")
    p_html.add_argument("--out", required=True, help="Percorso file .html")
    p_html.add_argument("--titolo", required=True, help="Titolo pagina")
    p_html.add_argument("--lingua", default="it", help="Lingua (es. it)")

    p_pack = sub.add_parser("new-pack", help="Crea DOCX+HTML+Checklist in una cartella")
    p_pack.add_argument("--dir", required=True, help="Cartella output")
    p_pack.add_argument("--nome", required=True, help="Nome base file (senza estensione)")
    p_pack.add_argument("--titolo", default="Documento", help="Titolo (opzionale)")
    p_pack.add_argument("--lingua-docx", default="it-IT")
    p_pack.add_argument("--lingua-html", default="it")

    args = parser.parse_args()
    if args.version:
        print(f"{APP_NOME} v{APP_VERSIONE} - {APP_AUTORE}")
        return 0
    if not args.cmd:
        parser.print_help()
        return 2

    if args.cmd == "new-docx":
        out = write_accessible_docx(args.out, args.titolo, lingua=args.lingua)
        print(f"OK DOCX: {out}")
        return 0

    if args.cmd == "new-html":
        out = Path(args.out).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(build_accessible_html(args.titolo, lingua=args.lingua), encoding="utf-8")
        print(f"OK HTML: {out}")
        return 0

    if args.cmd == "new-pack":
        outdir = Path(args.dir).resolve()
        outdir.mkdir(parents=True, exist_ok=True)
        base = args.nome.strip()
        if not base:
            raise SystemExit("Nome non valido.")

        docx = outdir / f"{base}.docx"
        html = outdir / f"{base}.html"
        checklist = outdir / f"{base}-CHECKLIST.md"

        write_accessible_docx(docx, args.titolo, lingua=args.lingua_docx)
        html.write_text(build_accessible_html(args.titolo, lingua=args.lingua_html), encoding="utf-8")
        checklist.write_text(build_checklist_markdown(), encoding="utf-8")

        print(f"OK: {docx.name}, {html.name}, {checklist.name}")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

