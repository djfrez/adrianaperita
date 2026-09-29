#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEO-070 — verificador da seção `#assistencia-tecnica-pericial` em `/assistente-tecnica/`.

- CPC/2015 (Planalto) rebaixado a cada execução, trechos tachados removidos;
  cada dispositivo citado é procurado na fonte, uma ocorrência.
- A página afirma que "assistência técnica" não ocorre no CPC: guarda que
  reprova se a expressão passar a ocorrer.
- Guardas negativas: o prazo do parecer é 15 dias (nunca outro número na
  seção); a remuneração do assistente nunca dita adiantada por quem requereu a
  perícia; o conjunto de artigos citados na tabela é exatamente o conferido.
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
SLUG = "assistente-tecnica"
PAGE = os.path.join(ROOT, SLUG, "index.html")
CPC = "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm"

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
        from assistencia_servico import DEFINICAO, FAQS, QUADRO
    except Exception as e:
        print(f"FAIL  conteúdo-fonte tools/build/assistencia_servico.py não importa: {e}")
        return 1
    doc = open(PAGE, encoding="utf-8").read()
    vis = norm(re.sub(r'<script type="application/ld\+json">.*?</script>', " ", doc, flags=re.S))
    try:
        cpc = fetch(CPC, "latin-1")  # Planalto serve ISO-8859-1
    except Exception as e:
        print(f"FAIL  rede — fonte não baixada: {e}")
        print("      (isto é falha de rede, NÃO reprovação de conteúdo)")
        return 1

    # ---- fonte primária: cada dispositivo citado, uma ocorrência
    for frag in (
        "§ 1º Incumbe às partes, dentro de 15 (quinze) dias contados da intimação do despacho de "
        "nomeação do perito: I - arguir o impedimento ou a suspeição do perito, se for o caso; "
        "II - indicar assistente técnico; III - apresentar quesitos.",
        "O perito deve assegurar aos assistentes das partes o acesso e o acompanhamento das "
        "diligências e dos exames que realizar, com prévia comunicação, comprovada nos autos, com "
        "antecedência mínima de 5 (cinco) dias",
        "Art. 469. As partes poderão apresentar quesitos suplementares durante a diligência",
        "§ 1º As partes, ao escolher o perito, já devem indicar os respectivos assistentes técnicos",
        "Art. 472. O juiz poderá dispensar prova pericial quando as partes, na inicial e na "
        "contestação, apresentarem, sobre as questões de fato, pareceres técnicos",
        "manifestar-se sobre o laudo do perito do juízo no prazo comum de 15 (quinze) dias, podendo "
        "o assistente técnico de cada uma das partes, em igual prazo, apresentar seu respectivo parecer",
        "§ 2º O perito do juízo tem o dever de, no prazo de 15 (quinze) dias, esclarecer ponto:",
        "II - divergente apresentado no parecer do assistente técnico da parte",
        "formulando, desde logo, as perguntas, sob forma de quesitos",
        "Art. 480. O juiz determinará, de ofício ou a requerimento da parte, a realização de nova "
        "perícia quando a matéria não estiver suficientemente esclarecida",
        "Art. 95. Cada parte adiantará a remuneração do assistente técnico que houver indicado",
    ):
        check(cpc.count(frag) == 1, f"CPC: trecho mudou ou duplicou — '{frag[:50]}…'")
    check(not re.search(r"assist[êe]ncia t[ée]cnica", cpc, re.I),
          "CPC: 'assistência técnica' passou a ocorrer — a página afirma que não ocorre")

    # ---- a seção
    check(doc.count('id="assistencia-tecnica-pericial"') == 1, "âncora ausente ou duplicada")
    raw = re.search(r"<!-- seo070:sec:start -->(.*?)<!-- seo070:sec:end -->", doc, re.S)
    s = norm(raw.group(1)) if raw else ""
    if not raw:
        fails.append("seção seo070 ausente")
    check(norm(DEFINICAO) in s, "seção: definição diverge da fonte")
    # a guarda do CPC só vale se a página afirmar exatamente o que ela guarda
    check('em nenhum momento em "assistência técnica"' in s,
          "seção: a afirmação sobre o CPC foi reescrita — a guarda da fonte deixou de cobri-la")
    check('A expressão "assistência técnica" não aparece no CPC' in norm(FAQS[0][1]),
          "FAQ: a afirmação sobre o CPC foi reescrita")
    check(set(re.findall(r"(\d+) dias", s)) == {"15", "5"}, "seção: prazo em dias diferente de 15/5")
    check(not re.search(r"adiantada pela parte que (requereu|requerer)", s), "seção: remuneração atribuída a quem requereu a perícia")
    check("adiantada pela parte que o indicou (art. 95 do CPC)" in s, "seção: art. 95 ausente ou reescrito")
    # a citação inteira (artigo, parágrafo, inciso), não só o número do artigo:
    # fonte e página adulteradas juntas passariam numa guarda por número
    cites = [c for _, _, c in QUADRO]
    check(cites == ["Arts. 472 e 471, § 1º", "Art. 465, § 1º, II e III", "Arts. 466, § 2º, e 469",
                    "Arts. 477, §§ 1º a 3º, e 480"], f"tabela: citações {cites}")
    for a, b, c in QUADRO:
        check(all(norm(x) in s for x in (a, b, c)), f"tabela: linha '{a}' ausente")
    check(raw and raw.group(1).count("<tr>") == len(QUADRO) + 1, "tabela: número de linhas ≠ quadro + cabeçalho")
    check("quatro entregas" in s and len(QUADRO) == 4, "definição promete quatro entregas e o quadro não tem quatro")
    for a in ("parecer-antes-da-pericia", "impugnacao-laudos"):
        check(f'href="#{a}"' in (raw.group(1) if raw else "") and doc.count(f'id="{a}"') == 1,
              f"link interno #{a} quebrado")
    box = doc.find('<div class="box-lbl">Definição</div>')
    tab = doc.find("<h2>Perito judicial e assistente técnico: as diferenças que importam</h2>")
    sec = doc.find('id="assistencia-tecnica-pericial"')
    check(-1 < box < sec < tab, "seção fora de lugar (entre o box Definição e a tabela perito × assistente)")
    t = re.search(r"<title>(.*?)</title>", doc)
    check(t and t.group(1) == "Assistente técnico na perícia: o que faz e quando contratar",
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
    check(dm and dm.group(1) >= "2026-09-29", "dateModified anterior à SEO-070")
    sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    m = re.search(SLUG + r"/</loc>\s*<lastmod>([^<]+)", sm)
    check(m and dm and m.group(1) == dm.group(1), "sitemap lastmod ≠ dateModified")
    check("assistente-tecnica/#assistencia-tecnica-pericial" in open(os.path.join(ROOT, "llms.txt"), encoding="utf-8").read(),
          "llms.txt não menciona a seção")

    for f in fails:
        print(f"FAIL  {f}")
    print(f"{checks - len(fails)}/{checks} checagens ok")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
