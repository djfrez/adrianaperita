#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificador estrito da SEO-049 — `/assistente-tecnica/#vocabulario`.

Cobra, na ordem:

  1. seção e âncora `#vocabulario` presentes, e `<h3>` da comparação cível×penal;
  2. cada célula das duas tabelas com o texto exato da fonte
     (`tools/build/vocabulario.py`) — nenhuma edição manual silenciosa na página;
  3. pergunta e resposta visíveis idênticas, caractere a caractere, ao que a
     fonte gera; a mesma resposta no JSON-LD, sem tag e sem entidade HTML;
  4. **posição penúltima** da entrada nova no `FAQPage`, com a de intake da
     SEO-046 em último — a invariante que a SEO-047 descobriu do jeito difícil;
  5. paridade contagem visível × schema;
  6. os links internos declarados na seção;
  7. **os números afirmados, recontados no texto compilado do Planalto.** Esta é
     a regra nova do handoff de 07/09: número afirmado no texto é afirmação
     verificável — o verificador cobra, ou ele apodrece. Sem rede, esta checagem
     reporta SKIP e o script sai com 1; ela nunca "passa" por omissão.
"""
import html as _html
import json
import os
import re
import sys
import unicodedata
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools", "build"))
from vocabulario import (ANSWER, CIVIL_PENAL, CPC_AT_ARTIGOS, CPC_AT_OCORRENCIAS,
                         QUESTION, VOCABULARIO)

PAGE = os.path.join(ROOT, "assistente-tecnica", "index.html")
INTAKE_Q = "O que enviar ao assistente técnico no primeiro contato?"
PLANALTO = {
    "CPC": "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm",
    "CPP": "https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689.htm",
}

fails = []


def check(cond, msg):
    if cond:
        print(f"  ok    {msg}")
    else:
        print(f"  FALHA {msg}")
        fails.append(msg)


def plain(s):
    return _html.unescape(re.sub(r"<[^>]+>", "", s))


def fold(s):
    """Fold sem diacrítico preservando o comprimento (1 char por char).

    Folding com NFKD+ascii encurta a string e faz o offset derivar — foi o bug
    que apareceu na apuração desta execução, e ele silenciaria a checagem 7.
    """
    out = []
    for ch in s:
        d = unicodedata.normalize("NFD", ch)
        b = "".join(c for c in d if not unicodedata.combining(c))
        out.append((b[:1] or ch).lower())
    return "".join(out)


def main():
    doc = open(PAGE, encoding="utf-8").read()

    # 1 — seção e âncoras
    check('<h2 id="vocabulario">' in doc, 'âncora id="vocabulario" presente')
    check("<!-- seo049:sec:start -->" in doc and "<!-- seo049:sec:end -->" in doc,
          "marcadores da seção presentes")
    check("A diferença que realmente muda a estratégia: cível não é criminal" in doc,
          "<h3> da comparação cível × penal presente")

    # 2 — cada célula das duas tabelas, texto exato da fonte
    miss = [c for row in VOCABULARIO for c in row if f"<td>{c}</td>" not in doc
            and f"<td><strong>{c}</strong></td>" not in doc]
    check(not miss, f"tabela de vocabulário: {len(VOCABULARIO)} linhas × 4 células conferidas"
                    + (f" — faltando {miss[:2]}" if miss else ""))
    miss = [c for row in CIVIL_PENAL for c in row if f"<td>{c}</td>" not in doc
            and f"<td><strong>{c}</strong></td>" not in doc]
    check(not miss, f"tabela cível × penal: {len(CIVIL_PENAL)} linhas × 3 células conferidas"
                    + (f" — faltando {miss[:2]}" if miss else ""))

    # 3 — visível e JSON-LD da mesma fonte
    check(f"<h3>{QUESTION}</h3>" in doc, "pergunta visível idêntica à fonte")
    check(f"<p>{ANSWER}</p>" in doc, "resposta visível idêntica à fonte")

    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S)
    faq = None
    for b in blocks:
        d = json.loads(b)
        if d.get("@type") == "FAQPage":
            faq = d
    check(faq is not None, "FAQPage parseia")

    names = [q["name"] for q in faq["mainEntity"]]
    texts = {q["name"]: q["acceptedAnswer"]["text"] for q in faq["mainEntity"]}
    check(plain(QUESTION) in names, "pergunta presente no JSON-LD, sem tag")
    check(texts.get(plain(QUESTION)) == plain(ANSWER),
          "resposta do JSON-LD idêntica à visível (sem tag, sem entidade HTML)")
    check("&" not in texts.get(plain(QUESTION), "") or "&amp;" not in texts.get(plain(QUESTION), ""),
          "resposta do JSON-LD sem entidade HTML crua")

    # 4 — posição penúltima; intake em último
    check(len(names) >= 2 and names[-2] == plain(QUESTION),
          "entrada nova em posição PENÚLTIMA no FAQPage")
    check(names[-1] == INTAKE_Q, "entrada de intake da SEO-046 segue em ÚLTIMO")

    # 5 — paridade visível × schema
    vis = re.search(r'<div class="faq">(.*?)\n    </div>\s*\n', doc, re.S)
    n_vis = len(re.findall(r"<h3>", vis.group(1))) if vis else -1
    check(n_vis == len(names), f"paridade contagem: {n_vis} visíveis × {len(names)} no schema")

    # 6 — links internos declarados na seção
    sec = doc.split("<!-- seo049:sec:start -->")[1].split("<!-- seo049:sec:end -->")[0]
    for href in ('href="/cpc-prova-pericial/"', 'href="/quesitos-periciais/"'):
        check(href in sec, f"link interno na seção: {href}")

    # 7 — números recontados na fonte primária
    print("  --- recontagem no Planalto (fonte primária) ---")
    try:
        texts_law = {}
        for k, u in PLANALTO.items():
            req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
            raw = urllib.request.urlopen(req, timeout=90).read()
            for enc in ("utf-8", "latin-1"):
                try:
                    t = raw.decode(enc)
                    break
                except UnicodeDecodeError:
                    continue
            t = _html.unescape(re.sub(r"<[^>]+>", " ", t))
            texts_law[k] = re.sub(r"\s+", " ", t)
    except Exception as e:
        print(f"  SKIP  recontagem indisponível (rede): {e}")
        fails.append("recontagem no Planalto não executada")
    else:
        cpc, cpp = texts_law["CPC"], texts_law["CPP"]
        fc, fp = fold(cpc), fold(cpp)
        check(fc.count("perito assistente") == 0,
              '"perito assistente": 0 ocorrências no CPC (a afirmação central da seção)')
        check(fp.count("perito assistente") == 0,
              '"perito assistente": 0 ocorrências no CPP')
        n_at = len(re.findall(r"assistentes? tecnicos?", fc))
        check(n_at == CPC_AT_OCORRENCIAS,
              f'"assistente técnico" no CPC: {n_at} ocorrências (página afirma {CPC_AT_OCORRENCIAS})')
        n_pj = fc.count("perito judicial")
        check(n_pj == 1, f'"perito judicial" no CPC: {n_pj} ocorrência (página afirma uma única)')
        check(fp.count("perito judicial") == 0, '"perito judicial": 0 ocorrências no CPP')
        check(fc.count("perito oficial") == 0,
              '"perito oficial": 0 ocorrências no CPC (é vocabulário do CPP)')
        check(fp.count("perito oficial") > 0, '"perito oficial": presente no CPP')
        # a única ocorrência de "perito judicial" está no art. 468, §2º
        m = re.search("perito judicial", fc)
        head = max(cpc.rfind("Art. 468.", 0, m.start()), 0)
        check(head and (m.start() - head) < 1200 and "restituirá" in cpc[head:m.start()],
              '"perito judicial" localizado no art. 468, §2º (contexto de punição)')
        # os 9 artigos afirmados
        arts = set()
        heads = [(mm.start(), int(mm.group(1))) for mm in re.finditer(r"Art\.\s*(\d+)\.\s", cpc)]
        for mm in re.finditer(r"assistentes? tecnicos?", fc):
            cur = None
            for s, num in heads:
                if s <= mm.start():
                    cur = num
                else:
                    break
            arts.add(cur)
        check(sorted(arts) == sorted(CPC_AT_ARTIGOS),
              f"artigos com 'assistente técnico': {sorted(arts)} == afirmado {sorted(CPC_AT_ARTIGOS)}")
        # a regra do CPP que sustenta o box
        check("a partir de sua admissao pelo juiz e apos a conclusao dos exames" in fp,
              "CPP art. 159, §4º: admissão pelo juiz + após conclusão dos exames (texto conferido)")

    print()
    if fails:
        print(f"{len(fails)} falha(s):")
        for f in fails:
            print("  ·", f)
        return 1
    print("OK — SEO-049 verificada")
    return 0


if __name__ == "__main__":
    sys.exit(main())
