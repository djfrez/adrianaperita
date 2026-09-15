#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificador estrito da SEO-056 — `/assistente-tecnica/#quem-pode`.

Cobra, na ordem:

  1. seção e âncora `#quem-pode` presentes, e o `<h3>` das vias de indicação;
  2. **cada célula da tabela** com o texto exato da fonte (`tools/build/
     elegibilidade.py`) — nenhuma edição manual silenciosa na página;
  3. pergunta e resposta visíveis idênticas, caractere a caractere, ao que a
     fonte gera; a mesma resposta no JSON-LD, sem tag e sem entidade HTML;
  4. a entrada nova vem **antes** da de intake da SEO-046 e a de intake é a
     **última** — a invariante descoberta na SEO-047, na formulação durável que
     esta execução teve de corrigir também na SEO-049;
  5. paridade contagem visível × schema;
  6. os links internos declarados na seção;
  7. **cada transcrição legal reconferida na fonte primária** — CPC/2015 e
     Decreto nº 85.877/1981 no Planalto. Sem rede, esta checagem reporta SKIP e
     o script **sai com 1**: ela nunca passa por omissão.
  8. `dateModified` e o `<time>` visível na data da execução.
"""
import html as _html
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools", "build"))
from elegibilidade import (ANSWER, EXIGENCIAS, FONTE_CPC, FONTE_DECRETO, QUESTION)

PAGE = os.path.join(ROOT, "assistente-tecnica", "index.html")
INTAKE_Q = "O que enviar ao assistente técnico no primeiro contato?"
DATA = "2026-09-15"
PLANALTO = {
    "CPC/2015": "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm",
    "Decreto 85.877/1981": "https://www.planalto.gov.br/ccivil_03/decreto/1980-1989/D85877.htm",
}
LINKS = ["/normas-tecnicas-pericia/", "/quesitos-periciais/", "/cpc-prova-pericial/"]

fails = []


def check(cond, msg):
    print(("  ok    " if cond else "  FALHA ") + msg)
    if not cond:
        fails.append(msg)


def plain(s):
    return _html.unescape(re.sub(r"<[^>]+>", "", s))


def norm(s):
    """Normaliza só espaço em branco — nada de dobrar acento ou caixa."""
    return re.sub(r"\s+", " ", s).strip()


doc = open(PAGE, encoding="utf-8").read()
sec = re.search(r"<!-- seo056:sec:start -->(.*?)<!-- seo056:sec:end -->", doc, re.S)

# 1 ------------------------------------------------------------------------
check(sec is not None, "seção seo056 presente entre marcadores")
if not sec:
    sys.exit(1)
sec = sec.group(1)
check('<h2 id="quem-pode">' in sec, "âncora #quem-pode presente")
check("<h3>Quando e por qual via a indicação é feita</h3>" in sec,
      "h3 das vias de indicação presente")

# 2 ------------------------------------------------------------------------
cells = [norm(plain(c)) for c in re.findall(r"<td>(.*?)</td>", sec, re.S)]
esperado = [norm(plain(v)) for row in EXIGENCIAS for v in row]
check(len(cells) == len(esperado),
      f"tabela com {len(EXIGENCIAS)} linhas × 4 colunas ({len(cells)} células)")
for i, (got, want) in enumerate(zip(cells, esperado)):
    check(got == want, f"célula {i // 4 + 1}.{i % 4 + 1} idêntica à fonte")

# 3/4/5 --------------------------------------------------------------------
vis_q = re.findall(r"<h3>(.*?)</h3>", doc, re.S)
faq = re.search(r'"@type": "FAQPage".*?"mainEntity"\s*:\s*(\[.*?\])\s*\}\s*</script>', doc, re.S)
check(faq is not None, "FAQPage com mainEntity encontrado")
entries = json.loads(faq.group(1)) if faq else []
names = [e["name"] for e in entries]

vis_block = re.search(r"<!-- seo056:faq:start -->(.*?)<!-- seo056:faq:end -->", doc, re.S)
check(vis_block is not None, "bloco visível da FAQ nova presente")
if vis_block:
    b = vis_block.group(1)
    q = re.search(r"<h3>(.*?)</h3>", b, re.S).group(1)
    a = re.search(r"<p>(.*?)</p>", b, re.S).group(1)
    check(norm(q) == norm(QUESTION), "pergunta visível idêntica à fonte")
    check(norm(a) == norm(ANSWER), "resposta visível idêntica à fonte")

# A lição que esta execução aprendeu ao quebrar o verificador da SEO-049:
# "posição penúltima" NÃO é invariante durável — vale só para a entrada mais
# recente, e a próxima execução que acrescentar uma FAQ nesta página empurra
# esta para a antepenúltima, reprovando uma página correta. O contrato real da
# SEO-046 é: **a de intake é a última**, e toda entrada nova entra antes dela.
check(names.count(plain(QUESTION)) == 1,
      "entrada nova presente exatamente uma vez no FAQPage")
check(plain(QUESTION) in names and names.index(plain(QUESTION)) < len(names) - 1,
      "entrada nova vem ANTES da de intake")
check(bool(names) and names[-1] == INTAKE_Q,
      "entrada de intake da SEO-046 segue em ÚLTIMO")
alvo = [e for e in entries if e["name"] == plain(QUESTION)]
check(len(alvo) == 1, "exatamente uma entrada nova no schema")
if alvo:
    check(alvo[0]["acceptedAnswer"]["text"] == plain(ANSWER),
          "resposta do JSON-LD idêntica ao visível, sem tag e sem entidade")

vis_count = len(re.findall(r"<h3>", doc.split('<h2 id="faq"')[-1])) if '<h2 id="faq"' in doc else None
faq_sec = re.search(r'id="faq".*?(?=<section|<footer|\Z)', doc, re.S)
if faq_sec:
    n_vis = len(re.findall(r"<h3>", faq_sec.group(0)))
    check(n_vis == len(entries), f"paridade visível × schema ({n_vis} × {len(entries)})")

# 6 ------------------------------------------------------------------------
for href in LINKS:
    check(f'href="{href}"' in sec, f"link interno para {href}")

# 8 ------------------------------------------------------------------------
check(f'"dateModified": "{DATA}"' in doc, f"dateModified em {DATA}")
check(f'Atualizado em <time datetime="{DATA}"' in doc, f"<time> visível em {DATA}")

# 7 ------------------------------------------------------------------------
print("\n  -- transcrições reconferidas na fonte primária --")
skipped = False
for nome, url in PLANALTO.items():
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        raw = urllib.request.urlopen(req, timeout=120).read()
    except Exception as e:
        print(f"  SKIP  {nome} inacessível — {e}")
        skipped = True
        continue
    for enc in ("utf-8", "latin-1"):
        try:
            txt = raw.decode(enc)
            break
        except Exception:
            pass
    txt = norm(_html.unescape(re.sub(r"<[^>]+>", " ", txt)))
    fonte = FONTE_CPC if nome.startswith("CPC") else FONTE_DECRETO
    for rotulo, trecho in fonte.items():
        check(norm(trecho) in txt, f"{nome} · {rotulo} — transcrição confere")

if skipped:
    print("\n  a checagem 7 não pôde rodar — saindo com 1 para não passar por omissão.")
    sys.exit(1)

print()
if fails:
    print(f"{len(fails)} FALHA(S)")
    sys.exit(1)
print("OK")
