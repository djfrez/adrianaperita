# -*- coding: utf-8 -*-
"""Aplica a SEO-070 em `/assistente-tecnica/`.

Idempotente: tudo o que este script escreve vive entre marcadores `seo070:*` e é
removido antes de ser reaplicado. FAQ pelas funções da SEO-066, importadas.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cpaq_build import strip_marks
from lote_build import apply_json_faq, apply_visible_faq
from assistencia_servico import DEFINICAO, FAQS, QUADRO

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "assistente-tecnica"

SEC_A, SEC_B = "<!-- seo070:sec:start -->", "<!-- seo070:sec:end -->"
FAQ_A, FAQ_B = "<!-- seo070:faq:start -->", "<!-- seo070:faq:end -->"

# O serviço é definido logo depois do profissional: depois do box "Definição" e
# antes da tabela perito × assistente.
ANCHOR = "    <h2>Perito judicial e assistente técnico: as diferenças que importam</h2>"

ROWS = "\n".join(
    f"          <tr>\n            <td>{a}</td>\n            <td>{b}</td>\n"
    f"            <td>{c}</td>\n          </tr>" for a, b, c in QUADRO)

SECTION = f"""{SEC_A}
    <h2 id="assistencia-tecnica-pericial">Assistência técnica pericial: o serviço, momento a momento</h2>
    <p>
      {DEFINICAO}
    </p>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th scope="col">Momento da prova</th>
            <th scope="col">O que a assistência técnica faz</th>
            <th scope="col">Base no CPC</th>
          </tr>
        </thead>
        <tbody>
{ROWS}
        </tbody>
      </table>
    </div>

    <p>
      O momento em que o serviço começa decide quanto dele ainda é possível. Contratada antes da
      perícia, a assistência técnica pode evitá-la — é o uso descrito em
      <a href="#parecer-antes-da-pericia">parecer antes da perícia</a>. Contratada depois do laudo,
      sobra o último momento: o parecer crítico e as vias de
      <a href="#impugnacao-laudos">impugnação do laudo</a>. A remuneração do assistente é
      adiantada pela parte que o indicou (art. 95 do CPC), e não pela que requereu a perícia.
    </p>
    {SEC_B}
"""


def apply_section(doc):
    doc = strip_marks(doc, SEC_A, SEC_B)
    if doc.count(ANCHOR) != 1:
        raise SystemExit(f"{SLUG}: {doc.count(ANCHOR)} âncoras de inserção — esperava 1")
    return doc.replace(ANCHOR, SECTION + ANCHOR, 1)


def apply():
    path = os.path.join(ROOT, SLUG, "index.html")
    doc = original = open(path, encoding="utf-8").read()
    doc = apply_section(doc)
    doc = apply_visible_faq(doc, FAQS, FAQ_A, FAQ_B, SLUG)
    doc = apply_json_faq(doc, FAQS, SLUG)
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S):
        try:
            json.loads(b)
        except Exception as e:
            raise SystemExit(f"{SLUG}: JSON-LD inválido após a inserção — {e}")
    if doc == original:
        return False
    open(path, "w", encoding="utf-8").write(doc)
    return True


if __name__ == "__main__":
    print(("escrito     " if apply() else "sem mudança ") + SLUG)
