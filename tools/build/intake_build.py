# -*- coding: utf-8 -*-
"""Insere (ou reescreve) o bloco de intake no `cta-sec` de cada página.

Idempotente: se o bloco já existe, é substituído pela versão gerada agora.
Assim o conteúdo vive só em `intake.py` e nunca deriva entre as 20 páginas.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from intake import PAGES, LEDE, CLOSE, PRAZO

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MARK_A, MARK_B = "<!-- intake:start -->", "<!-- intake:end -->"
ANDAMENTO = "/cpc-prova-pericial/#andamento"


def block(slug):
    href = "#andamento" if slug == "cpc-prova-pericial" else ANDAMENTO
    items = "\n".join(f"        <li>{i}</li>" for i in PAGES[slug])
    return (
f"""{MARK_A}
      <div class="box narrow">
        <div class="box-lbl">O que enviar na primeira mensagem</div>
        <p>{LEDE}</p>
        <ul>
{items}
        </ul>
        <p>{PRAZO} <a href="{href}">Como a intimação eletrônica vira data de vencimento</a>.</p>
        <p>{CLOSE}</p>
      </div>
      {MARK_B}""")


def apply(slug):
    path = os.path.join(ROOT, slug, "index.html")
    html = open(path, encoding="utf-8").read()
    new = block(slug)
    if MARK_A in html:
        out = re.sub(re.escape(MARK_A) + r".*?" + re.escape(MARK_B), new, html, flags=re.S)
    else:
        # Ancorar no <div class="ctas"> do cta-sec: o bloco entra imediatamente
        # antes dos botões, depois do parágrafo de serviços.
        m = re.search(r'(<section class="cta-sec">.*?)(\n\s*<div class="ctas">)', html, re.S)
        if not m:
            raise SystemExit(f"{slug}: âncora <div class=\"ctas\"> não encontrada no cta-sec")
        indent = "\n      "
        out = html[:m.end(1)] + indent + new + html[m.end(1):]
    if out == html:
        return False
    open(path, "w", encoding="utf-8").write(out)
    return True


if __name__ == "__main__":
    for slug in sorted(PAGES):
        print(("escrito " if apply(slug) else "sem mudança ") + slug)
