from __future__ import annotations

import datetime as _dt


def build_accessible_html(titolo: str, lingua: str = "it") -> str:
    now = _dt.datetime.now().isoformat(timespec="seconds")
    titolo_safe = titolo.replace("<", "").replace(">", "").strip() or "Documento"

    return f"""<!doctype html>
<html lang="{lingua}">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{titolo_safe}</title>
    <style>
      :root {{
        color-scheme: light;
      }}
      body {{
        font-family: system-ui, Segoe UI, Arial, sans-serif;
        max-width: 980px;
        margin: 24px auto;
        padding: 0 16px;
        line-height: 1.55;
      }}
      a:focus, button:focus, input:focus {{
        outline: 3px solid #0b57d0;
        outline-offset: 2px;
      }}
      .box {{
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 14px;
        background: #fafafa;
      }}
      table {{
        border-collapse: collapse;
        width: 100%;
      }}
      th, td {{
        border: 1px solid #ddd;
        padding: 8px;
        text-align: left;
      }}
      th {{
        background: #f2f2f2;
      }}
      .sr-only {{
        position: absolute;
        width: 1px;
        height: 1px;
        padding: 0;
        margin: -1px;
        overflow: hidden;
        clip: rect(0, 0, 0, 0);
        white-space: nowrap;
        border: 0;
      }}
    </style>
  </head>
  <body>
    <a class="sr-only" href="#contenuto">Salta al contenuto principale</a>

    <header>
      <h1>{titolo_safe}</h1>
      <p class="box">
        Template accessibile generato il <strong>{now}</strong>.
        Suggerimento: usa titoli (H2/H3), link descrittivi e descrivi le immagini.
      </p>
    </header>

    <main id="contenuto">
      <h2>Sezione esempio</h2>
      <p>
        Questo e' un paragrafo di esempio. Link descrittivo:
        <a href="https://www.agid.gov.it/">Sito istituzionale AgID</a>.
      </p>

      <h2>Immagine (con testo alternativo)</h2>
      <p>
        Sostituisci l'immagine e aggiorna sempre <code>alt</code>.
      </p>
      <img src="immagine-esempio.jpg" alt="Descrizione dell'immagine: cosa mostra e perche' e' rilevante." />

      <h2>Modulo (label associata)</h2>
      <form class="box" action="#" method="post">
        <label for="email">Email</label><br />
        <input id="email" name="email" type="email" autocomplete="email" />
        <button type="submit">Invia</button>
      </form>

      <h2>Tabella (con intestazioni)</h2>
      <table>
        <thead>
          <tr>
            <th scope="col">Campo</th>
            <th scope="col">Valore</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Versione</td>
            <td>0.1.0</td>
          </tr>
          <tr>
            <td>Lingua</td>
            <td>{lingua}</td>
          </tr>
        </tbody>
      </table>
    </main>

    <footer class="box" style="margin-top: 20px;">
      <p>Creato con Accessibile Da Zero (Germano Costi).</p>
    </footer>
  </body>
</html>
"""

