#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEO-069 — verificador da seção `#o-que-e-quesito` em `/quesitos-periciais/`.

- CPC/2015 e CPP (Planalto) rebaixados a cada execução, trechos tachados
  removidos; cada dispositivo citado é procurado na fonte, uma ocorrência.
- A página afirma que "quesitação" não ocorre no CPC nem no CPP: guarda que
  reprova se a palavra passar a ocorrer. Guardas negativas: nenhuma etimologia
  (não conferida) e o quesito do Júri nunca dito "ao perito".
- Paridade visível × JSON-LD por parse; intake lida dos marcadores, última.
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
SLUG = "quesitos-periciais"
PAGE = os.path.join(ROOT, SLUG, "index.html")
CPC = "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm"
CPP = "https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689.htm"

fails, checks = [], 0


def check(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)


def norm(s):
    s = _html.unescape(re.sub(r"<[^>]+>", " ", s))
    s = s.replace("“", '"').replace("”", '"').replace("\xa0", " ").replace("\xad", "")
    return re.sub(r"\s+", " ", s).strip()


def fetch(url, enc):
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/126 Safari/537.36",
        "Accept": "text/html", "Accept-Language": "pt-BR"})
    raw = urllib.request.urlopen(req, timeout=60).read().decode(enc, "replace")
    return norm(re.sub(r"<strike>.*?</strike>", " ", raw, flags=re.S | re.I))


def main():
    try:
        from quesito_def import DEFINICAO, FAQS, QUADRO
    except Exception as e:
        print(f"FAIL  conteúdo-fonte tools/build/quesito_def.py não importa: {e}")
        return 1
    doc = open(PAGE, encoding="utf-8").read()
    vis = norm(re.sub(r'<script type="application/ld\+json">.*?</script>', " ", doc, flags=re.S))
    try:
        cpc = fetch(CPC, "latin-1")  # Planalto serve ISO-8859-1
        cpp = fetch(CPP, "cp1252")  # o CPP traz travessão 0x96 (Windows-1252)
    except Exception as e:
        print(f"FAIL  rede — fonte não baixada: {e}")
        print("      (isto é falha de rede, NÃO reprovação de conteúdo)")
        return 1

    # ---- fonte primária: cada dispositivo citado, uma ocorrência
    for lei, nome, frags in (
        (cpc, "CPC", (
            "III - apresentar quesitos",
            "Art. 469. As partes poderão apresentar quesitos suplementares durante a diligência",
            "Art. 470. Incumbe ao juiz: I - indeferir quesitos impertinentes; II - formular os quesitos "
            "que entender necessários ao esclarecimento da causa",
            "IV - resposta conclusiva a todos os quesitos apresentados pelo juiz, pelas partes e pelo "
            "órgão do Ministério Público",
            "formulando, desde logo, as perguntas, sob forma de quesitos",
            "I - o perito e os assistentes técnicos, que responderão aos quesitos de esclarecimentos",
        )),
        (cpp, "CPP", (
            "a formulação de quesitos e indicação de assistente técnico",
            "Art. 160. Os peritos elaborarão o laudo pericial, onde descreverão minuciosamente o que "
            "examinarem, e responderão aos quesitos formulados",
            "Art. 176. A autoridade e as partes poderão formular quesitos até o ato da diligência",
            "Art. 482. O Conselho de Sentença será questionado sobre matéria de fato e se o acusado deve "
            "ser absolvido",
            "Os quesitos serão redigidos em proposições afirmativas, simples e distintas",
            "I – a materialidade do fato",
            "II – a autoria ou participação",
            "III – se o acusado deve ser absolvido",
        )),
    ):
        for frag in frags:
            check(lei.count(frag) == 1, f"{nome}: trecho mudou ou duplicou — '{frag[:50]}…'")
    for nome, lei in (("CPC", cpc), ("CPP", cpp)):
        check(not re.search(r"quesita[çc][ãa]o", lei, re.I),
              f"{nome}: 'quesitação' passou a ocorrer — a página afirma que não ocorre")

    # ---- a seção
    check(doc.count('id="o-que-e-quesito"') == 1, "âncora id=o-que-e-quesito ausente ou duplicada")
    raw = re.search(r"<!-- seo069:sec:start -->(.*?)<!-- seo069:sec:end -->", doc, re.S)
    s = norm(raw.group(1)) if raw else ""
    if not raw:
        fails.append("seção seo069 ausente")
    check(norm(DEFINICAO) in s, "seção: definição diverge da fonte")
    check(set(re.findall(r"art\. 473, ([IVX]+)", s)) == {"IV"},
          "seção: art. 473 citado com inciso diferente do IV")
    check(not re.search(r"latim|etimolog|quaer", s, re.I), "seção: etimologia publicada sem conferência")
    juri = re.search(r"<tr>\s*<td>Quesito do Tribunal do Júri</td>(.*?)</tr>", raw.group(1) if raw else "", re.S)
    check(juri and "perito" not in norm(juri.group(1)).replace("não ao perito", ""),
          "tabela: quesito do Júri dito dirigido ao perito")
    for frag in ("art. 473, IV", "art. 465, § 1º, III", "art. 470, II", "art. 477, § 3º", "art. 361, I",
                 "CPP, art. 159, § 3º", "CPP, art. 160", "CPP, art. 176", "CPP, art. 482", "CPP, art. 483",
                 "dirigido aos jurados — não ao perito"):
        check(frag in s, f"seção: '{frag}' ausente")
    for a, b, c in QUADRO:
        check(all(norm(x) in s for x in (a, b, c)), f"tabela: linha '{a}' ausente")
    check(raw and raw.group(1).count("<tr>") == len(QUADRO) + 1,
          "tabela: número de linhas ≠ quadro + cabeçalho")
    check("<h2>As três janelas para perguntar</h2>" in doc and
          doc.index('id="o-que-e-quesito"') < doc.index("<h2>As três janelas para perguntar</h2>"),
          "seção fora de lugar (deve vir antes das três janelas)")
    h1 = re.search(r"<title>(.*?)</title>", doc)
    check(h1 and h1.group(1) == "Quesitos periciais: como formular e por que a maioria falha",
          "title alterado — fica intocado enquanto SEO-057/058 estiverem em leitura")

    # ---- FAQ
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
        check(intake and names[-1] == norm(intake.group(1)), "a FAQ de intake não é a última do mainEntity")
        for q, a in FAQS:
            q, a = norm(q), norm(a)
            hit = [e for e in ents if e["name"] == q]
            check(len(hit) == 1, f"JSON-LD: FAQ '{q[:40]}…' presente {len(hit)} vezes")
            if hit:
                check(norm(hit[0]["acceptedAnswer"]["text"]) == a, f"JSON-LD: resposta divergente em '{q[:40]}…'")
            check(vis.count(q) == 1, f"visível: pergunta '{q[:40]}…' aparece {vis.count(q)} vezes")
            check(a in vis, f"visível: resposta de '{q[:40]}…' diverge da fonte")
        vis_q = [norm(h) for h in re.findall(r"<h3>(.*?)</h3>", doc.split('<div class="faq">')[1].split("</main>")[0])]
        check(vis_q == [norm(n) for n in names], "ordem visível das FAQs ≠ ordem do JSON-LD")

    # ---- datas e distribuição
    dm = re.search(r'"dateModified": "([^"]+)"', doc)
    check(dm and dm.group(1) >= "2026-09-28", "dateModified anterior à SEO-069")
    sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    m = re.search(SLUG + r"/</loc>\s*<lastmod>([^<]+)", sm)
    check(m and dm and m.group(1) == dm.group(1), "sitemap lastmod ≠ dateModified")
    check("`#o-que-e-quesito`" in open(os.path.join(ROOT, "llms.txt"), encoding="utf-8").read(),
          "llms.txt não menciona a seção de definição")

    for f in fails:
        print(f"FAIL  {f}")
    print(f"{checks - len(fails)}/{checks} checagens ok")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
