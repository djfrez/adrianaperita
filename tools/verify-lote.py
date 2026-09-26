#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEO-066 — verificador da seção `#lote-recusado` em `/pericia-industria-quimica/`.

- Código Civil rebaixado do Planalto a cada execução; cada frase que a página
  afirma é procurada literalmente. Guarda de redação: cada artigo citado tem de
  aparecer UMA vez — se aparecer duas, houve alteração e é preciso reconferir.
- Paridade visível × JSON-LD por parse, das duas FAQs novas.
- Invariante relacional (SEO-064): as novas estão antes da de intake, e a de
  intake — lida dos marcadores `faqintake`, não adivinhada — fecha o array.
- Guarda contra número não conferido: nenhum valor de r ou R na página.
Sem rede, sai com 1 e diz que foi a rede.
"""
import html as _html
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools", "build"))
PAGE = os.path.join(ROOT, "pericia-industria-quimica", "index.html")
CC = "https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm"

fails, checks = [], 0


def check(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)


def norm(s):
    s = _html.unescape(re.sub(r"<[^>]+>", " ", s))
    s = s.replace("“", '"').replace("”", '"').replace("\xa0", " ").replace("\xad", "")
    s = re.sub(r"§\s*1\s*o\b", "§ 1º", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    try:
        from lote import CONTRATO, FAQS, LEITURAS
    except Exception as e:
        print(f"FAIL  conteúdo-fonte tools/build/lote.py não importa: {e}")
        return 1
    if not os.path.exists(PAGE):
        print(f"FAIL  página não encontrada: {PAGE}")
        return 1
    doc = open(PAGE, encoding="utf-8").read()
    vis = norm(re.sub(r'<script type="application/ld\+json">.*?</script>', " ", doc, flags=re.S))

    try:
        req = urllib.request.Request(CC, headers={"User-Agent": "Mozilla/5.0"})
        cc = norm(urllib.request.urlopen(req, timeout=90).read().decode("latin-1"))
    except Exception as e:
        print(f"FAIL  rede — Código Civil não baixado: {e}")
        print("      (isto é falha de rede, NÃO reprovação de conteúdo)")
        return 1
    check(len(cc) > 500000, f"Código Civil veio curto demais ({len(cc)} chars)")

    # ---- fonte primária: o que a página afirma está no texto da lei
    for art in ("441", "442", "443", "445", "446"):
        n = len(re.findall(rf"Art\. {art}\. ", cc))
        check(n == 1, f"CC art. {art}: {n} ocorrências — redação alterada? reconferir à mão")
    for frag, onde in (
        ("vícios ou defeitos ocultos, que a tornem imprópria ao uso a que é destinada, ou lhe diminuam o valor", "art. 441"),
        ("pode o adquirente reclamar abatimento no preço", "art. 442"),
        ("restituirá o que recebeu com perdas e danos", "art. 443"),
        ("no prazo de trinta dias se a coisa for móvel", "art. 445"),
        ("contado da entrega efetiva", "art. 445"),
        ("só puder ser conhecido mais tarde, o prazo contar-se-á do momento em que dele tiver ciência, até o prazo máximo de cento e oitenta dias", "art. 445, § 1º"),
        ("Não correrão os prazos do artigo antecedente na constância de cláusula de garantia", "art. 446"),
        ("nos trinta dias seguintes ao seu descobrimento, sob pena de decadência", "art. 446"),
    ):
        check(frag in cc, f"CC {onde}: '{frag[:50]}…' não está na fonte")

    # ---- a página diz o que a fonte sustenta
    for frag in ("trinta dias da entrega efetiva", "cento e oitenta dias",
                 "nos trinta dias seguintes ao seu descobrimento",
                 "abatimento no preço", "perdas e danos"):
        check(frag in vis, f"página: '{frag}' ausente da seção")
    check(not re.search(r"(noventa|sessenta|quinze) dias da entrega", vis),
          "página: prazo de entrega diferente de trinta dias")
    check("2,8 vezes o desvio-padrão" in vis, "página: fator 2,8 de r/R ausente")
    check("ISO 5725-6" in vis and "Se ela não excede R, os resultados concordam" in vis,
          "página: teste da ISO 5725-6 ausente ou reescrito")
    # número não conferido: nenhum valor de r ou R
    check(not re.search(r"\b[rR]\s*=\s*\d", vis), "página: valor numérico de r/R publicado sem fonte")

    # ---- estrutura
    check(doc.count('id="lote-recusado"') == 1, "âncora id=lote-recusado ausente ou duplicada")
    sec = re.search(r"<!-- seo066:sec:start -->(.*?)<!-- seo066:sec:end -->", doc, re.S)
    if not sec:
        fails.append("seção seo066 ausente")
    else:
        s = norm(sec.group(1))
        for a, b, c in LEITURAS:
            check(all(norm(x) in s for x in (a, b, c)), f"tabela: linha '{a[:40]}…' ausente")
        for a, _ in CONTRATO:
            check(norm(a) in s, f"contrato: ponto '{a}' ausente")
        for href in ("/laudo-pericial/#laboratorio", "/producao-antecipada-prova/", "/quesitos-periciais/"):
            check(f'href="{href}"' in sec.group(1), f"link contextual {href} ausente")
            path = os.path.join(ROOT, href.split("#")[0].strip("/"), "index.html")
            check(os.path.exists(path), f"link {href} não resolve")
        check('id="laboratorio"' in open(os.path.join(ROOT, "laudo-pericial", "index.html"),
                                         encoding="utf-8").read(), "âncora #laboratorio sumiu do destino")

    # ---- FAQ: paridade e invariante relacional
    ents = None
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S):
        try:
            d = json.loads(b)
        except Exception as e:
            fails.append(f"JSON-LD inválido: {e}")
            continue
        if d.get("@type") == "FAQPage":
            ents = d["mainEntity"]
    if not ents:
        fails.append("FAQPage ausente")
    else:
        names = [e["name"] for e in ents]
        intake = re.search(r"<!-- faqintake:start -->.*?<h3>(.*?)</h3>", doc, re.S)
        iq = norm(intake.group(1)) if intake else None
        check(iq is not None and names[-1] == iq, "a FAQ de intake não é a última do mainEntity")
        for q, a in FAQS:
            q, a = norm(q), norm(a)
            hit = [e for e in ents if e["name"] == q]
            check(len(hit) == 1, f"JSON-LD: FAQ '{q[:40]}…' presente {len(hit)} vezes")
            if hit:
                check(hit[0]["acceptedAnswer"]["text"] == a, f"JSON-LD: resposta divergente em '{q[:40]}…'")
                check(names.index(q) < len(names) - 1, f"FAQ '{q[:40]}…' depois da de intake")
            check(vis.count(q) == 1, f"visível: pergunta '{q[:40]}…' aparece {vis.count(q)} vezes")
            check(a in vis, f"visível: resposta de '{q[:40]}…' diverge da fonte")
        vis_q = [norm(h) for h in re.findall(r"<h3>(.*?)</h3>", doc.split('<div class="faq">')[1].split("</main>")[0])]
        check(vis_q == names, "ordem visível das FAQs ≠ ordem do JSON-LD")

    # ---- datas e distribuição
    check('"dateModified": "2026-09-25"' in doc or re.search(r'"dateModified": "2026-(09-(2[5-9]|30)|1[0-2]-\d\d)"', doc),
          "dateModified anterior à SEO-066")
    sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    m = re.search(r"pericia-industria-quimica/</loc>\s*<lastmod>([^<]+)", sm)
    dm = re.search(r'"dateModified": "([^"]+)"', doc)
    check(m and dm and m.group(1) == dm.group(1), "sitemap lastmod ≠ dateModified")
    check("ISO 5725" in open(os.path.join(ROOT, "llms.txt"), encoding="utf-8").read(),
          "llms.txt não menciona a seção de lote recusado")

    for f in fails:
        print(f"FAIL  {f}")
    print(f"{checks - len(fails)}/{checks} checagens ok")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
