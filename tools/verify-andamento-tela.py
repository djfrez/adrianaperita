#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificador estrito da SEO-048.

Confere, nas duas páginas que o Google já escolheu para as consultas de
andamento, que:

  1. a seção nova existe, com o `h2` e a âncora certos;
  2. cada linha das tabelas aparece com o texto exato da fonte;
  3. a pergunta e a resposta visíveis são idênticas, caractere a caractere,
     às da fonte (`tools/build/andamento_tela.py`);
  4. a MESMA resposta está no `FAQPage`, sem entidade HTML;
  5. a entrada nova é a **penúltima** do `mainEntity` — a última é
     contratualmente a de intake da SEO-046 (invariante da SEO-047);
  6. a contagem de perguntas visíveis bate com a do schema;
  7. os links recíprocos apontam para âncoras que existem de fato;
  8. os códigos de movimento do CNJ na página `/cpc-prova-pericial/` são
     idênticos aos da fonte `andamento.py` — a correção pai→filho desta
     execução não pode regredir silenciosamente.

`ALL PASS` do seo-report não prova nada disso. É a oitava vez que isso é
registrado no backlog, e a razão de este script existir.
"""
import html as _html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools", "build"))
from andamento import MOVIMENTOS
from andamento_tela import APOS_ESCLARECIMENTOS, CNJ_TOTAL, JANELAS, answer, question

PAGES = {"quesitos-periciais": ("sem-quesitos", JANELAS),
         "laudo-pericial": ("esclarecimentos", APOS_ESCLARECIMENTOS)}

fails = []


def bad(slug, msg):
    fails.append(f"{slug}: {msg}")


def faq_block(doc):
    i = doc.find('"@type": "FAQPage"')
    j = doc.find("</script>", i)
    k = doc.rfind('<script type="application/ld+json">', 0, i)
    return json.loads(doc[k + len('<script type="application/ld+json">'):j])


for slug, (anchor, rows) in sorted(PAGES.items()):
    doc = open(os.path.join(ROOT, slug, "index.html"), encoding="utf-8").read()

    # 1 — seção e âncora
    if f'<h2 id="{anchor}">' not in doc:
        bad(slug, f'h2 com id="{anchor}" ausente')
    if "<!-- seo048:sec:start -->" not in doc:
        bad(slug, "marcador de seção ausente")

    # 2 — linhas da tabela, texto exato da fonte
    for a, b, c in rows:
        for cell in (b, c):
            if cell not in doc:
                bad(slug, f"célula ausente ou alterada: {cell[:60]}…")

    # 3 — pergunta e resposta visíveis idênticas à fonte
    q, a = question(slug), answer(slug)
    if f"<h3>{q}</h3>" not in doc:
        bad(slug, "pergunta visível diferente da fonte")
    if f"<p>{a}</p>" not in doc:
        bad(slug, "resposta visível diferente da fonte")

    # 4/5/6 — schema
    data = faq_block(doc)
    entries = data["mainEntity"]
    names = [e["name"] for e in entries]
    qq, aa = _html.unescape(q), _html.unescape(a)
    if qq not in names:
        bad(slug, "pergunta ausente do FAQPage")
    else:
        idx = names.index(qq)
        if entries[idx]["acceptedAnswer"]["text"] != aa:
            bad(slug, "resposta do JSON-LD difere da visível")
        if idx != len(entries) - 2:
            bad(slug, f"entrada nova não é a penúltima (índice {idx} de {len(entries)})")
    if "primeira mensagem" not in names[-1] and "enviar" not in names[-1].lower():
        bad(slug, f"a última entrada não parece ser a de intake: {names[-1][:50]}…")
    visible = len(re.findall(r"<h3>", doc[doc.find('<div class="faq">'):]))
    if visible != len(entries):
        bad(slug, f"{visible} perguntas visíveis × {len(entries)} no schema")

    # 7 — links recíprocos com âncora existente
    if "/cpc-prova-pericial/#andamento" not in doc:
        bad(slug, "link para o decodificador ausente")

    # o número de movimentos do CNJ é afirmação verificável, não decoração
    if CNJ_TOTAL not in doc:
        bad(slug, f"a página não declara os {CNJ_TOTAL} movimentos da tabela do CNJ")

cpc = open(os.path.join(ROOT, "cpc-prova-pericial", "index.html"), encoding="utf-8").read()
if 'id="andamento"' not in cpc:
    bad("cpc-prova-pericial", "âncora #andamento ausente — links das duas páginas quebrariam")
for label, *_ in MOVIMENTOS:
    if label not in cpc:
        bad("cpc-prova-pericial", f"rótulo/código divergente da fonte: {label[:70]}…")
for parent_only in ('<span class="cod">(14901)</span>', '<span class="cod">(12263)</span>',
                    '<span class="cod">(67)</span>'):
    if parent_only in cpc:
        bad("cpc-prova-pericial", f"código de PAI onde cabe o do filho: {parent_only}")

if fails:
    print("REPROVADO")
    for f in fails:
        print("  ·", f)
    sys.exit(1)
print(f"OK — {len(PAGES)} páginas, paridade visível×schema, penúltima posição e "
      f"{len(MOVIMENTOS)} códigos do CNJ conferidos contra a fonte")
