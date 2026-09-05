#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificador estrito da SEO-046.

Confere, para as 20 páginas, que a entrada de FAQ de intake existe nas duas
pontas e que as duas são idênticas caractere a caractere à fonte
(`tools/build/faq_intake.py`). `ALL PASS` do seo-report não prova isso — é a
quinta vez que isso é registrado, e a razão de este script existir.
"""
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools", "build"))
from faq_intake import ENTRIES, answer, question

fails = []


def bad(slug, msg):
    fails.append(f"{slug}: {msg}")


for slug in sorted(ENTRIES):
    path = os.path.join(ROOT, slug, "index.html")
    doc = open(path, encoding="utf-8").read()
    q, a = question(slug), answer(slug)

    # --- JSON-LD ---------------------------------------------------------
    faq = None
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S):
        try:
            o = json.loads(b)
        except Exception as e:
            bad(slug, f"JSON-LD inválido — {e}")
            continue
        if o.get("@type") == "FAQPage":
            faq = o
    if faq is None:
        bad(slug, "FAQPage ausente")
        continue
    entries = faq.get("mainEntity") or []
    names = [e.get("name") for e in entries]
    if names[-1] != html.unescape(q):
        bad(slug, f"última pergunta do FAQPage != fonte: {names[-1]!r}")
    if len(names) != len(set(names)):
        bad(slug, "pergunta duplicada no FAQPage")
    got = {e["name"]: e["acceptedAnswer"]["text"] for e in entries if e.get("name")}
    if got.get(html.unescape(q)) != html.unescape(a):
        bad(slug, "texto da resposta no JSON-LD != fonte")

    # --- HTML visível ----------------------------------------------------
    start = doc.find('<div class="faq">')
    if start == -1:
        bad(slug, 'contêiner <div class="faq"> ausente')
        continue
    end = doc.find("</section>", start)
    block = doc[start:end if end != -1 else len(doc)]
    vis = [" ".join(html.unescape(re.sub("<[^>]*>", " ", h)).split())
           for h in re.findall(r"<h3[^>]*>(.*?)</h3>", block, re.S)]
    if len(vis) != len(names):
        bad(slug, f"{len(vis)} perguntas visíveis × {len(names)} no FAQPage")
    if vis and vis[-1] != html.unescape(q):
        bad(slug, f"último <h3> != pergunta: {vis[-1]!r}")
    if f"<h3>{q}</h3>" not in block:
        bad(slug, "pergunta visível não é idêntica à fonte")
    if f"<p>{a}</p>" not in block:
        bad(slug, "resposta visível não é idêntica à fonte")
    # O bloco tem de estar DENTRO do contêiner .faq, não solto na página.
    if "<!-- faqintake:start -->" not in block:
        bad(slug, "marcador fora do contêiner .faq")

print("\n".join("  FAIL  " + f for f in fails) if fails
      else f"  OK    {len(ENTRIES)}/{len(ENTRIES)} páginas — pergunta e resposta idênticas à fonte nas duas pontas")
sys.exit(1 if fails else 0)
