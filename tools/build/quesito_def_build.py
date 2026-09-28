# -*- coding: utf-8 -*-
"""Aplica a SEO-069 em `/quesitos-periciais/`.

Idempotente: tudo o que este script escreve vive entre marcadores `seo069:*` e é
removido antes de ser reaplicado. FAQ pelas funções da SEO-066, importadas.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cpaq_build import strip_marks
from lote_build import apply_json_faq, apply_visible_faq
from quesito_def import DEFINICAO, FAQS, QUADRO

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "quesitos-periciais"

SEC_A, SEC_B = "<!-- seo069:sec:start -->", "<!-- seo069:sec:end -->"
FAQ_A, FAQ_B = "<!-- seo069:faq:start -->", "<!-- seo069:faq:end -->"

# A definição vem antes de tudo o que a pressupõe: logo depois do box do
# art. 473, IV, e antes das três janelas.
ANCHOR = "    <h2>As três janelas para perguntar</h2>"

ROWS = "\n".join(
    f"          <tr>\n            <td>{a}</td>\n            <td>{b}</td>\n"
    f"            <td>{c}</td>\n          </tr>" for a, b, c in QUADRO)

SECTION = f"""{SEC_A}
    <h2 id="o-que-e-quesito">O que é quesito — e o que significa quesitação</h2>
    <p>
      {DEFINICAO}
    </p>
    <p>
      A mesma palavra aparece em quatro lugares do processo, com funções diferentes. Quem chega a
      ela por um andamento, por uma intimação ou por um julgamento no Júri costuma estar diante de
      uma só delas — e a confusão mais comum é tratar o quesito do Júri como se fosse pergunta ao
      perito.
    </p>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th scope="col">Figura</th>
            <th scope="col">Quem formula, e quando</th>
            <th scope="col">O que a lei exige da resposta</th>
          </tr>
        </thead>
        <tbody>
{ROWS}
        </tbody>
      </table>
    </div>

    <p>
      O que une as três primeiras figuras é a consequência: o perito tem de responder. É isso que
      torna a redação decisiva — uma pergunta que admite resposta conclusiva vira prova; uma que
      pede opinião jurídica é indeferida ou devolve uma frase vaga. O restante desta página trata
      de como escrever a primeira e evitar a segunda, começando pelos três momentos em que se pode
      perguntar.
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
