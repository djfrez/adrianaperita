#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEO-067 — verificador da seção `#metanol` em `/pericia-combustiveis/`.

- Resoluções ANP nº 807/2020 e nº 907/2022 rebaixadas do DOU a cada execução;
  cada fato que a página afirma é procurado literalmente na fonte.
- Guarda negativa para o número afirmado (SEO-066): nenhum limite de metanol
  diferente de 0,5% e nenhum escopo da NBR 16943 diferente de 1,50%.
- Guarda contra número não conferido: nenhuma massa específica publicada.
- E32 × E30: a página não pode voltar a dizer que o teor atual é 30%.
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
PAGE = os.path.join(ROOT, "pericia-combustiveis", "index.html")
R807 = "https://www.in.gov.br/en/web/dou/-/resolucao-n-807-de-23-de-janeiro-de-2020-239635261"
R907 = "https://www.in.gov.br/en/web/dou/-/resolucao-anp-n-907-de-18-de-novembro-de-2022-445396653"

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


def fetch(url):
    # O DOU devolve 403 a "Mozilla/5.0" seco; aceita UA de navegador completo.
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/126 Safari/537.36",
        "Accept": "text/html", "Accept-Language": "pt-BR"})
    return norm(urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace"))


def main():
    try:
        from metanol import FAQS, METODOS
    except Exception as e:
        print(f"FAIL  conteúdo-fonte tools/build/metanol.py não importa: {e}")
        return 1
    doc = open(PAGE, encoding="utf-8").read()
    vis = norm(re.sub(r'<script type="application/ld\+json">.*?</script>', " ", doc, flags=re.S))

    try:
        r807, r907 = fetch(R807), fetch(R907)
    except Exception as e:
        print(f"FAIL  rede — resolução ANP não baixada: {e}")
        print("      (isto é falha de rede, NÃO reprovação de conteúdo)")
        return 1

    # ---- fonte primária
    check(re.search(r"Teor de Metanol, máx \(18\)\(19\) % volume 0,5 16041", r807),
          "807: linha do metanol (0,5 % vol, NBR 16041) mudou — reconferir")
    check("(18) Proibida a adição. Devem ser medidos quando houver dúvida quanto à ocorrência de contaminação" in r807,
          "807: nota (18) mudou")
    check("exige a confirmação pelo método cromatográfico ABNT NBR 16041" in r807, "807: nota (19) mudou")
    check("indicação de que o teor de metanol no etanol anidro está abaixo ou igual a 0,5%" in r807,
          "807: art. 9º, § 1º, I mudou")
    check("(17) Proibida a adição" in r907, "907: nota (17) mudou")
    check("assume toda e qualquer responsabilidade pelo não atendimento à especificação" in r907,
          "907: nota (20) mudou")
    check("teor de metanol de, no máximo, 1,50% em volume" in r907, "907: nota (21) mudou")
    check("confirmação do resultado pelo método cromatográfico ABNT NBR 16041" in r907, "907: nota (19) mudou")
    check(len(re.findall(r"Teor de metanol, máx", r907)) == 2, "907: esperava a linha do metanol nas Tabelas 1 e 2")

    # ---- a página diz o que a fonte sustenta
    check('id="metanol"' in doc and doc.count('id="metanol"') == 1, "âncora id=metanol ausente ou duplicada")
    sec = re.search(r"<!-- seo067:sec:start -->(.*?)<!-- seo067:sec:end -->", doc, re.S)
    if not sec:
        fails.append("seção seo067 ausente")
        s = ""
    else:
        s = norm(sec.group(1))
    check(s.count("0,5% em volume") == 1, "seção: '0,5% em volume' deveria aparecer 1 vez")
    check(set(m[0] for m in re.findall(r"(?<![\d,])(\d+(,\d+)?)% em volume\b(?! de metanol)", s)) == {"0,5"},
          "seção: limite de metanol diferente de 0,5% publicado")
    check(set(re.findall(r"até (\d,\d\d)% em volume", s)) == {"1,50"}, "seção: escopo da NBR 16943 ≠ 1,50%")
    check(not re.search(r"\d+[,.]\d+\s*(kg/m|g/cm|g/mL)", s), "seção: massa específica publicada sem fonte")
    for frag in ("proibida a adição", "ABNT NBR 13992", "Resolução ANP nº 697/2017",
                 "art. 9º, § 1º, I, da Resolução nº 807/2020", "nota 20 da Resolução nº 907/2022",
                 "quando houver dúvida quanto à ocorrência de contaminação"):
        check(frag in s, f"seção: '{frag}' ausente")
    for a, b, c in METODOS:
        check(all(norm(x) in s for x in (a, b, c)), f"tabela: linha '{a}' ausente")
    for href in ("/laudo-pericial/#laboratorio", "/quesitos-periciais/"):
        check(sec and f'href="{href}"' in sec.group(1), f"link contextual {href} ausente")
        check(os.path.exists(os.path.join(ROOT, href.split("#")[0].strip("/"), "index.html")),
              f"link {href} não resolve")

    # ---- E32: o teor vigente não pode regredir para 30%
    check(vis.count("desde 1º de agosto de 2026 a gasolina C comum tem 32%") == 1, "FAQ visível: E32 ausente")
    check("32% na gasolina C comum desde 01/08/2026" in vis, "tabela de ensaios: E32 ausente")
    check(not re.search(r"desde (1º de agosto de 2025|01/08/2025) a gasolina C comum tem 30%|30% na gasolina C comum desde", doc),
          "página: 30% ainda apresentado como teor vigente")

    dano = open(os.path.join(ROOT, "dano-motor-combustivel", "index.html"), encoding="utf-8").read()
    check("gasolina C comum tem 32% de etanol anidro (E32)" in norm(dano)
          and not re.search(r"agosto de 2025 a gasolina C comum tem 30%", norm(dano)),
          "/dano-motor-combustivel/: teor vigente não é E32")

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
        e32 = [e for e in ents if e["name"].startswith("Quais resoluções da ANP")]
        check(e32 and "32% de etanol anidro (E32)" in e32[0]["acceptedAnswer"]["text"], "JSON-LD: E32 ausente")
        vis_q = [norm(h) for h in re.findall(r"<h3>(.*?)</h3>", doc.split('<div class="faq">')[1].split("</main>")[0])]
        check(vis_q == names, "ordem visível das FAQs ≠ ordem do JSON-LD")

    # ---- datas e distribuição
    dm = re.search(r'"dateModified": "([^"]+)"', doc)
    check(dm and dm.group(1) >= "2026-09-26", "dateModified anterior à SEO-067")
    sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    m = re.search(r"pericia-combustiveis/</loc>\s*<lastmod>([^<]+)", sm)
    check(m and dm and m.group(1) == dm.group(1), "sitemap lastmod ≠ dateModified")
    check("`#metanol`" in open(os.path.join(ROOT, "llms.txt"), encoding="utf-8").read(),
          "llms.txt não menciona a seção de metanol")

    for f in fails:
        print(f"FAIL  {f}")
    print(f"{checks - len(fails)}/{checks} checagens ok")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
