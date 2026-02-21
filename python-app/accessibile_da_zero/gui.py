from __future__ import annotations

import pathlib
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from accessibile_da_zero import APP_AUTORE, APP_HOME, APP_NOME, APP_VERSIONE
from accessibile_da_zero.checklist import build_checklist_markdown
from accessibile_da_zero.docx_gen import write_accessible_docx
from accessibile_da_zero.html_gen import build_accessible_html


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title(f"{APP_NOME} v{APP_VERSIONE} - {APP_AUTORE}")
        self.geometry("860x520")
        self.minsize(780, 460)

        self.titolo = tk.StringVar(value="Documento accessibile")
        self.base = tk.StringVar(value="pacchetto")
        self.lingua_docx = tk.StringVar(value="it-IT")
        self.lingua_html = tk.StringVar(value="it")
        self.out_dir = tk.StringVar(value=str(pathlib.Path("_output").resolve()))

        self._build()

    def _build(self) -> None:
        root = ttk.Frame(self, padding=12)
        root.pack(fill="both", expand=True)

        menubar = tk.Menu(self)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Informazioni", command=self._about)
        menubar.add_cascade(label="Aiuto", menu=helpmenu)
        self.config(menu=menubar)

        form = ttk.LabelFrame(root, text="Parametri")
        form.pack(fill="x")

        ttk.Label(form, text="Titolo").grid(row=0, column=0, padx=8, pady=8, sticky="w")
        ttk.Entry(form, textvariable=self.titolo).grid(row=0, column=1, padx=8, pady=8, sticky="ew")

        ttk.Label(form, text="Nome base").grid(row=1, column=0, padx=8, pady=8, sticky="w")
        ttk.Entry(form, textvariable=self.base).grid(row=1, column=1, padx=8, pady=8, sticky="ew")

        ttk.Label(form, text="Lingua DOCX").grid(row=2, column=0, padx=8, pady=8, sticky="w")
        ttk.Entry(form, textvariable=self.lingua_docx, width=10).grid(row=2, column=1, padx=8, pady=8, sticky="w")

        ttk.Label(form, text="Lingua HTML").grid(row=3, column=0, padx=8, pady=8, sticky="w")
        ttk.Entry(form, textvariable=self.lingua_html, width=10).grid(row=3, column=1, padx=8, pady=8, sticky="w")

        ttk.Label(form, text="Cartella output").grid(row=4, column=0, padx=8, pady=8, sticky="w")
        ttk.Entry(form, textvariable=self.out_dir).grid(row=4, column=1, padx=8, pady=8, sticky="ew")
        ttk.Button(form, text="Scegli...", command=self._choose_dir).grid(row=4, column=2, padx=8, pady=8)

        form.columnconfigure(1, weight=1)

        actions = ttk.LabelFrame(root, text="Azioni")
        actions.pack(fill="x", pady=(12, 0))
        ttk.Button(actions, text="Crea DOCX", command=self._new_docx).pack(side="left", padx=8, pady=10)
        ttk.Button(actions, text="Crea HTML", command=self._new_html).pack(side="left", padx=8, pady=10)
        ttk.Button(actions, text="Crea Pacchetto", command=self._new_pack).pack(side="left", padx=8, pady=10)
        ttk.Button(actions, text="Apri output", command=self._open_output).pack(side="left", padx=8, pady=10)

        log_box = ttk.LabelFrame(root, text="Esito")
        log_box.pack(fill="both", expand=True, pady=(12, 0))
        self.log = tk.Text(log_box, height=12, wrap="word")
        self.log.pack(fill="both", expand=True, padx=8, pady=8)
        self._write("Pronto.")

    def _about(self) -> None:
        msg = "\n".join(
            [
                f"{APP_NOME} v{APP_VERSIONE}",
                f"Autore: {APP_AUTORE}",
                f"Home: {APP_HOME}",
            ]
        )
        messagebox.showinfo("Informazioni", msg)

    def _write(self, text: str) -> None:
        self.log.insert("end", text + "\n")
        self.log.see("end")

    def _choose_dir(self) -> None:
        p = filedialog.askdirectory(title="Cartella output")
        if p:
            self.out_dir.set(p)

    def _ensure_outdir(self) -> pathlib.Path:
        out = pathlib.Path(self.out_dir.get().strip() or "_output").resolve()
        out.mkdir(parents=True, exist_ok=True)
        return out

    def _basename(self) -> str:
        base = self.base.get().strip()
        if not base:
            raise ValueError("Inserisci un nome base.")
        return base

    def _new_docx(self) -> None:
        try:
            out = self._ensure_outdir()
            base = self._basename()
            docx = out / f"{base}.docx"
            write_accessible_docx(docx, self.titolo.get().strip() or "Documento", lingua=self.lingua_docx.get().strip() or "it-IT")
            self._write(f"OK DOCX: {docx}")
        except Exception as exc:  # noqa: BLE001
            messagebox.showerror("Errore", str(exc))

    def _new_html(self) -> None:
        try:
            out = self._ensure_outdir()
            base = self._basename()
            html = out / f"{base}.html"
            html.write_text(
                build_accessible_html(self.titolo.get().strip() or "Documento", lingua=self.lingua_html.get().strip() or "it"),
                encoding="utf-8",
            )
            self._write(f"OK HTML: {html}")
        except Exception as exc:  # noqa: BLE001
            messagebox.showerror("Errore", str(exc))

    def _new_pack(self) -> None:
        try:
            out = self._ensure_outdir()
            base = self._basename()
            docx = out / f"{base}.docx"
            html = out / f"{base}.html"
            checklist = out / f"{base}-CHECKLIST.md"
            write_accessible_docx(docx, self.titolo.get().strip() or "Documento", lingua=self.lingua_docx.get().strip() or "it-IT")
            html.write_text(
                build_accessible_html(self.titolo.get().strip() or "Documento", lingua=self.lingua_html.get().strip() or "it"),
                encoding="utf-8",
            )
            checklist.write_text(build_checklist_markdown(), encoding="utf-8")
            self._write(f"OK Pacchetto: {docx.name}, {html.name}, {checklist.name}")
        except Exception as exc:  # noqa: BLE001
            messagebox.showerror("Errore", str(exc))

    def _open_output(self) -> None:
        out = self._ensure_outdir()
        try:
            import os

            os.startfile(str(out))  # type: ignore[attr-defined]
        except Exception:
            self._write(f"Output: {out}")


def main() -> int:
    app = App()
    app.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

