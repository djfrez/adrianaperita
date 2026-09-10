#!/usr/bin/env python3
"""Verificador estrito da SEO-050 em `/impugnacao-laudo-pericial/`.

Roda:  /usr/bin/python3 tools/verify-nulidade.py

O que ele garante, e por que cada checagem existe:

  1. Seção, âncora `#nulidade` e os dois `<h3>` presentes.
  2. **Cada célula das duas tabelas** com o texto exato de `tools/build/nulidade.py`
     — que é a fonte única do visível e do JSON-LD (regra 11).
  3. As transcrições literais do CPC usadas fora das tabelas, e a tese do Tema 988.
  4. Pergunta e resposta visíveis idênticas, caractere a caractere, à fonte.
  5. A **mesma** resposta no JSON-LD, sem tag e sem entidade HTML.
  6. Posição **penúltima** da entrada nova no `FAQPage` — a última é
     contratualmente a de intake da SEO-046 — e paridade de contagem
     visível × schema.
  7. Os três links internos da seção.
  8. **Os números afirmados no texto, recontados na fonte** (Planalto): as duas
     expressões que a página diz não existirem no CPC, o número de incisos do
     art. 1.015 e a ausência de “perícia/laudo/pericial” nesse rol. Sem rede, a
     recontagem reporta SKIP e **o script sai com 1**: ela nunca passa por omissão.

`ALL PASS` do seo-report NÃO prova nada disso — é a nona confirmação registrada
no backlog. Por isso este verificador existe separado.
"""
import html as _html
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools", "build"))
from nulidade import (ANSWER, ART_282, ART_466_2, ART_474, ART_1009_1, CPC_AUSENTES,
                      EXIGENCIAS, QUESTION, ROL_1015_INCISOS, TEMA_988, VOCABULARIO)
from faq_intake import question as intake_question

PAGE = os.path.join(ROOT, "impugnacao-laudo-pericial", "index.html")
PLANALTO = "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm"

fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)


def plain(s):
    return _html.unescape(re.sub(r"<[^>]+>", "", s))


def fold(s):
    """Dobra acento preservando o comprimento — se encurtar, o offset deriva e a
    checagem passa a medir outra coisa (erro cometido e corrigido na SEO-049)."""
    tbl = str.maketrans("áàâãäéèêëíìîïóòôõöúùûüçÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÇ",
                        "aaaaaeeeeiiiiooooouuuucAAAAAEEEEIIIIOOOOOUUUUC")
    out = s.translate(tbl).lower()
    assert len(out) == len(s)
    return out


doc = open(PAGE, encoding="utf-8").read()
sec = doc[doc.index("<!-- seo050:sec:start -->"):doc.index("<!-- seo050:sec:end -->")]

# 1 — estrutura
check('<h2 id="nulidade">' in sec, "âncora #nulidade ausente")
check(sec.count("<h3>") == 2, f"esperava 2 <h3> na seção, achei {sec.count('<h3>')}")
check("Nulidade é do ato, não do documento" in sec, "<h3> da nulidade ausente")
check("Recorrer do quê: o laudo não é decisão" in sec, "<h3> do recurso ausente")

# 2 — cada célula das duas tabelas
for row in VOCABULARIO:
    for cell in row:
        check(cell in sec, f"célula ausente na tabela de vocabulário: {plain(cell)[:60]!r}")
for row in EXIGENCIAS:
    for cell in row:
        check(cell in sec, f"célula ausente na tabela de exigências: {cell[:60]!r}")

# 2b — os números como a página os renderiza, contra a fonte única.
# Sem isto, um número editado à mão na página passa: foi o que o controle
# negativo 3a mostrou nesta execução, e é o buraco que ele fechou.
NUM_EXIG = {1: "uma", 2: "duas", 3: "três", 4: "quatro", 5: "cinco", 6: "seis"}[len(EXIGENCIAS)]
check(f"<strong>{ROL_1015_INCISOS} incisos</strong>" in sec,
      f"o texto não renderiza os {ROL_1015_INCISOS} incisos do art. 1.015 declarados na fonte")
check(f"a lei exige {NUM_EXIG} condições" in re.sub(r"\s+", " ", sec),
      f"o texto não renderiza as {len(EXIGENCIAS)} exigências que a fonte declara")
check(sec.count("<tr>") == len(VOCABULARIO) + len(EXIGENCIAS) + 2,
      "número de linhas das tabelas difere da fonte")

# 3 — transcrições literais e a tese
for lit, nome in ((ART_282, "art. 282"), (ART_466_2, "art. 466, §2º"), (ART_474, "art. 474"),
                  (ART_1009_1, "art. 1.009, §1º"), (TEMA_988, "tese do Tema 988")):
    check(lit in sec, f"transcrição literal ausente ou alterada: {nome}")

# 4 — FAQ visível idêntico à fonte
vis = doc[doc.index("<!-- seo050:faq:start -->"):doc.index("<!-- seo050:faq:end -->")]
check(f"<h3>{QUESTION}</h3>" in vis, "pergunta visível difere da fonte")
check(f"<p>{ANSWER}</p>" in vis, "resposta visível difere da fonte")

# 5 e 6 — JSON-LD: mesmo texto, posição penúltima, paridade de contagem
faq = None
for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S):
    d = json.loads(blk)
    if d.get("@type") == "FAQPage":
        faq = d
check(faq is not None, "FAQPage não encontrado ou não parseia")
if faq:
    ents = faq["mainEntity"]
    names = [e["name"] for e in ents]
    check(plain(QUESTION) in names, "pergunta ausente do JSON-LD")
    if plain(QUESTION) in names:
        i = names.index(plain(QUESTION))
        check(i == len(ents) - 2,
              f"entrada nova em posição {i + 1}/{len(ents)} — esperava penúltima")
        check(ents[i]["acceptedAnswer"]["text"] == plain(ANSWER),
              "resposta do JSON-LD difere da visível")
    check(names[-1] == plain(intake_question("impugnacao-laudo-pericial")),
          f"última entrada não é a de intake da SEO-046: {names[-1]!r}")
    start = doc.index('<div class="faq">')
    block = doc[start:doc.index("</section>", start)]
    n_vis = len(re.findall(r"<h3[^>]*>", block))
    check(n_vis == len(ents),
          f"paridade quebrada: {n_vis} perguntas visíveis × {len(ents)} no schema")

# 7 — links internos da seção
for href in ("/assistente-tecnica/", "/cpc-prova-pericial/", "/quesitos-periciais/"):
    check(f'href="{href}"' in sec, f"link interno ausente na seção: {href}")

# 8 — os números afirmados, recontados na fonte
try:
    req = urllib.request.Request(PLANALTO, headers={"User-Agent": "Mozilla/5.0"})
    raw = urllib.request.urlopen(req, timeout=90).read()
    try:
        src = raw.decode("utf-8")
    except UnicodeDecodeError:
        src = raw.decode("latin-1")
    txt = _html.unescape(re.sub(r"<[^>]+>", " ", src))
    low = fold(txt)
    for expr in CPC_AUSENTES:
        n = low.count(fold(expr))
        check(n == 0, f"a página afirma que “{expr}” não está no CPC, mas há {n} ocorrência(s)")
    a = txt.rindex("Art. 1.015.")
    b = txt.index("Art. 1.016.", a)
    rol = re.sub(r"\s+", " ", txt[a:b])
    n_inc = len(re.findall(r"\b(?:I|II|III|IV|V|VI|VII|VIII|IX|X|XI|XII|XIII)\s*-\s", rol))
    check(n_inc == ROL_1015_INCISOS,
          f"art. 1.015: a página afirma {ROL_1015_INCISOS} incisos, a fonte tem {n_inc}")
    check("(VETADO)" in rol, "art. 1.015: inciso vetado não encontrado na fonte")
    for w in ("pericia", "pericial", "laudo"):
        check(fold(rol).count(w) == 0,
              f"art. 1.015: a página afirma que o rol não menciona “{w}”, mas menciona")
    for lit in (ART_282, ART_466_2, ART_474, ART_1009_1):
        check(re.sub(r"\s+", " ", lit) in re.sub(r"\s+", " ", txt),
              f"transcrição não confere com o Planalto: {lit[:50]!r}")
    print("  recontagem no Planalto: feita")
except Exception as e:
    print(f"  SKIP — recontagem no Planalto indisponível ({type(e).__name__}: {e})")
    print("  Uma checagem que não roda não é uma checagem: saindo com 1.")
    for f in fails:
        print("  FAIL " + f)
    sys.exit(1)

if fails:
    for f in fails:
        print("  FAIL " + f)
    sys.exit(1)
print("  verify-nulidade: OK")
