#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificador estrito da SEO-047.

`ALL PASS` do seo-report não prova paridade entre o texto visível e o JSON-LD —
é a sétima vez que isso se registra. Este script confere, contra a fonte única
(`tools/build/ambiental_normas.py`), que as quatro inserções existem, que a
pergunta de FAQ é idêntica caractere a caractere nas duas pontas, que a entrada
de intake da SEO-046 continua sendo a última do FAQPage e que o link recíproco
de `/auto-infracao-ambiental/` aponta para a âncora que existe.
"""
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools", "build"))
from ambiental_normas import ROWS, ENTRY_ID, ENTRY_TITLE, ENTRY_PARAS, FAQ_Q, FAQ_A, NOTA

PAGE = os.path.join(ROOT, "normas-tecnicas-pericia", "index.html")
AMB = os.path.join(ROOT, "auto-infracao-ambiental", "index.html")
fails = []


def bad(m):
    fails.append(m)


doc = open(PAGE, encoding="utf-8").read()
amb = open(AMB, encoding="utf-8").read()

# --- linhas do quadro -------------------------------------------------------
for materia, norma, rege, sit in ROWS:
    for campo in (norma, rege, sit):
        if f"<td>{campo}</td>" not in doc:
            bad(f"linha do quadro ausente ou divergente: {campo[:60]!r}")
if doc.count(f"<td>{ROWS[0][1]}</td>") != 1:
    bad("linha da Lei 9.605 duplicada")

# --- nota de data -----------------------------------------------------------
if f"<p>{NOTA}</p>" not in doc:
    bad("nota de data da conferência ausente ou divergente")

# --- entrada de 'as que mudaram' -------------------------------------------
if f'<h3 id="{ENTRY_ID}">{ENTRY_TITLE}</h3>' not in doc:
    bad("h3 da entrada nova ausente ou divergente")
for p in ENTRY_PARAS:
    if f"<p>{p}</p>" not in doc:
        bad(f"parágrafo da entrada nova divergente: {p[:60]!r}")
if "As nove que mudaram" not in doc:
    bad("contagem do h2 não foi atualizada para nove")
n_entries = len(re.findall(r'<div class="art-entry">', doc))
if n_entries != 9:
    bad(f"a seção tem {n_entries} entradas, mas o h2 diz nove")

# --- FAQ visível ------------------------------------------------------------
start = doc.find('<div class="faq">')
end = doc.find("</section>", start)
faq_html_block = doc[start:end]
if f"<h3>{FAQ_Q}</h3>" not in faq_html_block:
    bad("pergunta visível ausente ou divergente")
if f"<p>{FAQ_A}</p>" not in faq_html_block:
    bad("resposta visível ausente ou divergente")

# --- FAQ em JSON-LD ---------------------------------------------------------
faq = None
for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S):
    try:
        o = json.loads(b)
    except Exception as e:
        bad(f"JSON-LD inválido — {e}")
        continue
    if o.get("@type") == "FAQPage":
        faq = o
if faq is None:
    bad("FAQPage ausente")
else:
    entries = faq["mainEntity"]
    names = [e.get("name") for e in entries]
    if len(names) != len(set(names)):
        bad("pergunta duplicada no FAQPage")
    if FAQ_Q not in names:
        bad("pergunta nova ausente do FAQPage")
    else:
        if names.index(FAQ_Q) != len(names) - 2:
            bad("a pergunta nova não é a penúltima — a de intake tem de ser a última")
        got = entries[names.index(FAQ_Q)]["acceptedAnswer"]["text"]
        if got != html.unescape(re.sub(r"<[^>]+>", "", FAQ_A)):
            bad("texto da resposta no JSON-LD != fonte")
    # paridade de contagem
    visiveis = len(re.findall(r"<h3>", faq_html_block))
    if visiveis != len(entries):
        bad(f"{visiveis} perguntas visíveis contra {len(entries)} no schema")

# --- link recíproco ---------------------------------------------------------
if f'/normas-tecnicas-pericia/#{ENTRY_ID}' not in amb:
    bad("/auto-infracao-ambiental/ não linka a âncora nova")
if f'id="{ENTRY_ID}"' not in doc:
    bad("âncora de destino não existe na página de normas")

if fails:
    print("FALHOU:")
    for f in fails:
        print("  ·", f)
    sys.exit(1)
print("OK — quadro, entrada, FAQ (duas pontas), contagem e link recíproco conferem com a fonte")
