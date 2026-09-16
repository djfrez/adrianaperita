#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificador da SEO-057 — snippet (title + description) de `/cpc-prova-pericial/`.

Cobra:
  1. o title novo em <title>, og:title, twitter:title e headline do Article,
     e o antigo em lugar nenhum;
  2. comprimentos dentro do limite de exibição (title ≤ 60; description 150–160);
  3. cada prazo afirmado no snippet existe na linha correspondente da tabela
     de prazos da própria página — o snippet não promete o que a página não tem;
  4. **as duas transcrições que sustentam os números, reconferidas no Planalto.**
     Sem rede: SKIP e sai com 1 — nunca passa por omissão;
  5. dateModified e <time> visível na data da execução.
"""
import html as _html
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, "cpc-prova-pericial", "index.html")
DATA = "2026-09-16"
TITLE = "Prova pericial no CPC: prazos de quesitos, laudo e parecer"
OLD_TITLE = "Prova pericial no CPC: os artigos e prazos, em ordem"
DESC = ("Quesitos: 15 dias (art. 465). Manifestação sobre o laudo e parecer do "
        "assistente: 15 dias comuns (art. 477). Todos os prazos da perícia no CPC em uma tabela.")
# (rótulo, trecho que deve estar na linha da tabela, base legal da linha)
LINHAS = [
    ("quesitos em 15 dias", "15 dias", "Art. 465, §1º, I a III"),
    ("manifestação e parecer em 15 dias comuns", "15 dias, comum", "Art. 477, §1º"),
]
CPC = "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm"
FONTE = {
    "art. 465, §1º": "Incumbe às partes, dentro de 15 (quinze) dias contados da intimação do despacho de nomeação do perito",
    "art. 477, §1º": "manifestar-se sobre o laudo do perito do juízo no prazo comum de 15 (quinze) dias, podendo o assistente técnico de cada uma das partes, em igual prazo, apresentar seu respectivo parecer",
}

fails = []


def check(cond, msg):
    print(("  ok    " if cond else "  FALHA ") + msg)
    if not cond:
        fails.append(msg)


def norm(s):
    return re.sub(r"\s+", " ", _html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


doc = open(PAGE, encoding="utf-8").read()

# 1 · 2
check(f"<title>{TITLE}</title>" in doc, "<title> novo")
check(f'<meta property="og:title" content="{TITLE}">' in doc, "og:title igual ao title")
check(f'<meta name="twitter:title" content="{TITLE}">' in doc, "twitter:title igual ao title")
check(f'"headline": "{TITLE}"' in doc, "headline do Article igual ao title")
check(OLD_TITLE not in doc, "title antigo removido de todos os lugares")
check(f'<meta name="description" content="{DESC}">' in doc, "meta description nova")
check(len(TITLE) <= 60, f"title com {len(TITLE)} caracteres (≤ 60)")
check(150 <= len(DESC) <= 160, f"description com {len(DESC)} caracteres (150–160)")

# 3
rows = [norm(r) for r in re.findall(r"<tr>(.*?)</tr>", doc, re.S)]
for rotulo, prazo, base in LINHAS:
    hit = [r for r in rows if r.endswith(base) and prazo in r]
    check(len(hit) == 1, f"tabela da página sustenta '{rotulo}' ({base})")

# 5
check(f'"dateModified": "{DATA}"' in doc, f"dateModified em {DATA}")
check(f'Atualizado em <time datetime="{DATA}"' in doc, f"<time> visível em {DATA}")

# 4
print("\n  -- transcrições reconferidas no Planalto --")
try:
    raw = urllib.request.urlopen(urllib.request.Request(
        CPC, headers={"User-Agent": "Mozilla/5.0"}), timeout=120).read()
except Exception as e:
    print(f"  SKIP  CPC inacessível — {e}\n  saindo com 1 para não passar por omissão.")
    sys.exit(1)
try:
    txt = raw.decode("utf-8")
except UnicodeDecodeError:
    txt = raw.decode("latin-1")
txt = norm(txt)
for rotulo, trecho in FONTE.items():
    check(trecho in txt, f"CPC {rotulo} — transcrição confere")

print()
if fails:
    print(f"{len(fails)} FALHA(S)")
    sys.exit(1)
print("OK")
