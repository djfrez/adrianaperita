#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificador da SEO-058 — meta description de `/honorarios-pericia-judicial/`.

Teste de description isolada: o title fica intocado para que uma mudança de CTR
seja atribuível só à description. Cobra:
  1. description nova (150–160) e og/twitter:description novos; os antigos em
     lugar nenhum; title antigo preservado nos 4 lugares;
  2. cada afirmação do snippet sustentada pela tabela "As duas contas" da página
     (linha "Quem adianta") e pela seção de gratuidade (art. 95, §3º);
  3. dateModified e <time> NÃO mudaram — metadado não é conteúdo, e a data
     visível tem de continuar honesta;
  4. **art. 95, caput e §3º, reconferidos no Planalto.** Sem rede: SKIP e sai
     com 1 — nunca passa por omissão.
"""
import html as _html
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, "honorarios-pericia-judicial", "index.html")
TITLE = "Honorários periciais: quem paga, quem adianta e gratuidade"
DATA_CONTEUDO = "2026-09-10"
DESC = ("Perito: adianta quem pediu a perícia, com rateio se ambas pediram ou o juiz a "
        "determinou (art. 95 do CPC). Assistente técnico: adianta a parte que o indicou.")
SOCIAL = ("Perito: adianta quem pediu a perícia (art. 95 do CPC). Assistente técnico: a parte "
          "que o indicou. Na gratuidade, o custeio é público (art. 95, §3º).")
ANTIGAS = [
    "Quem adianta os honorários do perito e do assistente técnico, como o juiz arbitra o valor",
    "As duas contas que se confundem numa perícia",
    "Como se formam e quem suporta os custos da prova pericial",
]
CPC = "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm"
FONTE = {
    "art. 95, caput": "Cada parte adiantará a remuneração do assistente técnico que houver indicado, "
                      "sendo a do perito adiantada pela parte que houver requerido a perícia ou rateada "
                      "quando a perícia for determinada de ofício ou requerida por ambas as partes",
    "art. 95, §3º, I": "custeada com recursos alocados no orçamento do ente público",
    "art. 95, §3º, II": "paga com recursos alocados no orçamento da União, do Estado ou do Distrito Federal",
}

fails = []


def check(cond, msg):
    print(("  ok    " if cond else "  FALHA ") + msg)
    if not cond:
        fails.append(msg)


def norm(s):
    return re.sub(r"\s+", " ", _html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


doc = open(PAGE, encoding="utf-8").read()

# 1
check(f'<meta name="description" content="{DESC}">' in doc, "meta description nova")
check(150 <= len(DESC) <= 160, f"description com {len(DESC)} caracteres (150–160)")
check(f'<meta property="og:description" content="{SOCIAL}">' in doc, "og:description nova")
check(f'<meta name="twitter:description" content="{SOCIAL}">' in doc, "twitter:description nova")
for a in ANTIGAS:
    check(a not in doc, f"texto antigo removido: '{a[:40]}…'")
check(f"<title>{TITLE}</title>" in doc and f'"headline": "{TITLE}"' in doc
      and doc.count(f'content="{TITLE}"') == 2, "title intocado nos 4 lugares")

# 2
rows = [norm(r) for r in re.findall(r"<tr>(.*?)</tr>", doc, re.S)]
hit = [r for r in rows if r.startswith("Quem adianta")]
check(len(hit) == 1, "linha 'Quem adianta' existe uma vez na tabela")
if hit:
    r = hit[0]
    check("Quem requereu a prova" in r and "rateado se de ofício ou requerida por ambas" in r,
          "tabela sustenta 'adianta quem pediu, com rateio se ambas ou o juiz'")
    check("A parte que indicou o assistente (art. 95)" in r,
          "tabela sustenta 'assistente: adianta a parte que o indicou'")
body = norm(doc.split("<body", 1)[1])
check("O art. 95, §3º , dá dois caminhos" in body or "O art. 95, §3º, dá dois caminhos" in body,
      "seção de gratuidade sustenta 'custeio público (art. 95, §3º)'")

# 3
check(f'"dateModified": "{DATA_CONTEUDO}"' in doc, f"dateModified preservado em {DATA_CONTEUDO}")
check(f'Atualizado em <time datetime="{DATA_CONTEUDO}"' in doc, f"<time> visível preservado em {DATA_CONTEUDO}")

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
