#!/usr/bin/env python3
"""Verificador estrito da SEO-051 em `/honorarios-pericia-judicial/`.

Roda:  /usr/bin/python3 tools/verify-honorarios-final.py

  1. Seção, âncora `#final-do-processo` e o `<h3>` presentes.
  2. Cada célula das duas tabelas com o texto exato de `tools/build/honorarios_final.py`,
     e a contagem de `<tr>` igual à da fonte.
  3. O número de momentos na prosa derivado de `len(CALENDARIO)` — conferido na
     renderização, não só no dado (regra da SEO-050).
  4. As transcrições literais do CPC e da CLT na seção.
  5. FAQ nova: visível idêntica à fonte; a mesma resposta no JSON-LD sem tag nem
     entidade; posição penúltima; a última é a de intake da SEO-046
     (conferida chamando `faq_intake.question`, não por heurística); paridade.
  6. A correção da resposta de reembolso: texto novo no visível e no JSON-LD,
     texto antigo em lugar nenhum (página e `llms.txt`), célula da tabela corrigida.
  7. Os três links internos da seção.
  8. Transcrições reconferidas no Planalto (CPC e CLT), e a anotação da ADI 5766
     presente no art. 790-B. Sem rede: SKIP e **exit 1** — nunca passa por omissão.
"""
import html as _html
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools", "build"))
from honorarios_final import (ANSWER, CALENDARIO, CLT, CPC, LLMS_OLD, QUESTION, REEMBOLSO_NEW,
                              REEMBOLSO_OLD, REEMBOLSO_Q, SO_NO_FIM, TABELA_NEW, TABELA_OLD)
from faq_intake import question as intake_question

SLUG = "honorarios-pericia-judicial"
PAGE = os.path.join(ROOT, SLUG, "index.html")
URLS = {"CPC": "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm",
        "CLT": "https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452.htm"}

fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)


def plain(s):
    return _html.unescape(re.sub(r"<[^>]+>", "", s))


def ws(s):
    return re.sub(r"\s+", " ", s)


doc = open(PAGE, encoding="utf-8").read()
sec = doc[doc.index("<!-- seo051:sec:start -->"):doc.index("<!-- seo051:sec:end -->")]

# 1
check('<h2 id="final-do-processo">' in sec, "âncora #final-do-processo ausente")
check("<h3>Onde o perito recebe, de fato, só no fim</h3>" in sec, "<h3> ausente")

# 2
for tabela, rows in (("calendário", CALENDARIO), ("só no fim", SO_NO_FIM)):
    for row in rows:
        for cell in row:
            check(cell in sec, f"célula ausente ({tabela}): {plain(cell)[:60]!r}")
check(sec.count("<tr>") == len(CALENDARIO) + len(SO_NO_FIM) + 2,
      "número de linhas das tabelas difere da fonte")

# 3
n = {5: "cinco", 6: "seis", 7: "sete", 8: "oito"}[len(CALENDARIO)]
check(f"São {n} os momentos" in ws(sec),
      f"a prosa não renderiza os {len(CALENDARIO)} momentos que a fonte declara")

# 4
# ART_82_2 é só parafraseado na página; entra na reconferência (8), não aqui.
for lit in [x for x in CPC if x != CPC[0]] + [CLT[0]]:
    check(lit in ws(sec), f"transcrição ausente ou alterada na seção: {lit[:50]!r}")

# 5 e 6 — FAQ
vis = doc[doc.index("<!-- seo051:faq:start -->"):doc.index("<!-- seo051:faq:end -->")]
check(f"<h3>{QUESTION}</h3>" in vis, "pergunta visível difere da fonte")
check(f"<p>{ANSWER}</p>" in vis, "resposta visível difere da fonte")
check(f"<h3>{REEMBOLSO_Q}</h3>\n        <p>{REEMBOLSO_NEW}</p>" in doc,
      "resposta visível de reembolso não é a corrigida")
check(REEMBOLSO_OLD not in doc, "texto antigo de reembolso ainda na página")
check(TABELA_NEW in doc and TABELA_OLD not in doc, "célula de reembolso não corrigida")
check(LLMS_OLD not in open(os.path.join(ROOT, "llms.txt"), encoding="utf-8").read(),
      "llms.txt ainda traz a descrição antiga do reembolso")

faq = None
for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S):
    d = json.loads(blk)
    if d.get("@type") == "FAQPage":
        faq = d
check(faq is not None, "FAQPage não encontrado ou não parseia")
if faq:
    ents = faq["mainEntity"]
    by = {e["name"]: e["acceptedAnswer"]["text"] for e in ents}
    names = [e["name"] for e in ents]
    check(plain(QUESTION) in names, "pergunta ausente do JSON-LD")
    if plain(QUESTION) in names:
        i = names.index(plain(QUESTION))
        check(i == len(ents) - 2, f"entrada nova em posição {i + 1}/{len(ents)} — esperava penúltima")
        check(by[plain(QUESTION)] == plain(ANSWER), "resposta do JSON-LD difere da visível")
    check(by.get(REEMBOLSO_Q) == REEMBOLSO_NEW, "reembolso no JSON-LD difere do visível")
    check(names[-1] == plain(intake_question(SLUG)),
          f"última entrada não é a de intake da SEO-046: {names[-1]!r}")
    start = doc.index('<div class="faq">')
    block = doc[start:doc.index("</section>", start)] if "</section>" in doc[start:] else doc[start:]
    block = block[:block.index("</main>")] if "</main>" in block else block
    n_vis = len(re.findall(r"<h3[^>]*>", block))
    check(n_vis == len(ents), f"paridade quebrada: {n_vis} perguntas visíveis × {len(ents)} no schema")

# 7
for href in ("/impugnacao-laudo-pericial/", "/assistente-tecnica/", "/cpc-prova-pericial/"):
    check(f'href="{href}"' in sec, f"link interno ausente na seção: {href}")

# 8 — fonte primária
try:
    txt = {}
    for k, url in URLS.items():
        raw = urllib.request.urlopen(
            urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=90).read()
        try:
            src = raw.decode("utf-8")
        except UnicodeDecodeError:
            src = raw.decode("latin-1")
        txt[k] = ws(_html.unescape(re.sub(r"<[^>]+>", " ", src)).replace("\xa0", " "))
    for lit in CPC:
        check(ws(lit) in txt["CPC"], f"transcrição não confere com o CPC no Planalto: {lit[:50]!r}")
    for lit in CLT:
        check(ws(lit) in txt["CLT"], f"transcrição não confere com a CLT no Planalto: {lit[:50]!r}")
    a = txt["CLT"].rindex("Art. 790-B.")
    b = txt["CLT"].index("Art. 791", a)
    check(txt["CLT"][a:b].count("Declarado inconstitucional pela ADI 5766") == 2,
          "art. 790-B: a página afirma duas anotações da ADI 5766 no Planalto")
    print("  reconferência no Planalto: feita")
except Exception as e:
    print(f"  SKIP — Planalto indisponível ({type(e).__name__}: {e})")
    print("  Uma checagem que não roda não é uma checagem: saindo com 1.")
    for f in fails:
        print("  FAIL " + f)
    sys.exit(1)

if fails:
    for f in fails:
        print("  FAIL " + f)
    sys.exit(1)
print("  verify-honorarios-final: OK")
