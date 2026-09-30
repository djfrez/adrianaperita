#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEO-071 — verificador da seção `#producao-antecipada` em
`/analise-microbiologica-alimentos/`.

- CPC art. 381 e art. 382 rebaixados a cada execução no Planalto.
- Guarda negativa: a seção nova NÃO cita Lei 6.437 / art. 27 (isso fica em
  `#uma-so-chance`); só "três" hipóteses; nenhum R$.
- Paridade visível × JSON-LD; intake última; posição antes de `#erros`.
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
SLUG = "analise-microbiologica-alimentos"
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
    return norm(urllib.request.urlopen(req, timeout=60).read().decode(enc, "replace"))


def main():
    try:
        from micro_antecipada import FAQS, QUADRO
    except Exception as e:
        print(f"FAIL  conteúdo-fonte tools/build/micro_antecipada.py não importa: {e}")
        return 1
    doc = open(PAGE, encoding="utf-8").read()
    vis = norm(re.sub(r'<script type="application/ld\+json">.*?</script>', " ", doc, flags=re.S))
    try:
        cpc = fetch(CPC, "latin-1")
    except Exception as e:
        print(f"FAIL  rede — fonte não baixada: {e}")
        print("      (isto é falha de rede, NÃO reprovação de conteúdo)")
        return 1

    # ---- CPC: cada trecho citado, uma ocorrência
    for frag in (
        "Art. 381. A produção antecipada da prova será admitida nos casos em que:",
        "I - haja fundado receio de que venha a tornar-se impossível ou muito difícil a "
        "verificação de certos fatos na pendência da ação",
        "II - a prova a ser produzida seja suscetível de viabilizar a autocomposição ou "
        "outro meio adequado de solução de conflito",
        "III - o prévio conhecimento dos fatos possa justificar ou evitar o ajuizamento "
        "de ação",
        "Art. 382. Na petição, o requerente apresentará as razões que justificam a "
        "necessidade de antecipação da prova e mencionará com precisão os fatos sobre os "
        "quais a prova há de recair",
        "§ 4º Neste procedimento, não se admitirá defesa ou recurso, salvo contra decisão "
        "que indeferir totalmente a produção da prova pleiteada pelo requerente originário",
    ):
        check(cpc.count(frag) == 1, f"CPC: trecho mudou ou duplicou — '{frag[:50]}…'")
    # Guarda de ausência no Código (a página afirma o número de hipóteses; se o
    # Código ganhar um inciso IV, a tabela de três linhas fica falsa).
    check("IV -" not in cpc[cpc.find("Art. 381."):cpc.find("Art. 382.")],
          "CPC art. 381 ganhou inciso IV — tabela de três hipóteses obsoleta")

    # ---- a seção
    check(doc.count('id="producao-antecipada"') == 1, "âncora id=producao-antecipada ausente ou duplicada")
    raw = re.search(r"<!-- seo071:sec:start -->(.*?)<!-- seo071:sec:end -->", doc, re.S)
    s = norm(raw.group(1)) if raw else ""
    if not raw:
        fails.append("seção seo071 ausente")
    # Guarda negativa: a seção NÃO reabre a Lei 6.437 / art. 27 como citação
    # normativa própria — só a contrapõe, mencionando-a uma vez cada no box e
    # no parágrafo de abertura. Contagem exacta = 2 (abertura + box).
    check(s.count("Lei nº 6.437/1977") == 2, f"seção: Lei 6.437 citada {s.count('Lei nº 6.437/1977')} vezes (esperado 2)")
    check(s.count("art. 27") == 2, f"seção: art. 27 citado {s.count('art. 27')} vezes (esperado 2)")
    check(not re.search(r"R\$\s*\d", s), "seção: valor em reais publicado")
    check(set(re.findall(r"três hipóteses", s)) and s.count("três hipóteses") >= 1,
          "seção: 'três hipóteses' ausente")
    # Citação completa por linha do quadro
    for a, b, c in QUADRO:
        check(all(norm(x) in s for x in (a, b, c)), f"tabela: linha '{a}' ausente ou truncada")
    check(raw and raw.group(1).count("<tr>") == len(QUADRO) + 1,
          "tabela: número de linhas ≠ quadro + cabeçalho")
    # Guarda contra adulteração autoconsistente fonte+página (III→IV nas duas):
    # o CPC só tem I–III; a tabela não pode ganhar inciso inventado.
    incisos = set(re.findall(r">([IVX]+) — ", raw.group(1))) if raw else set()
    check(incisos == {"I", "II", "III"},
          f"incisos da tabela = {sorted(incisos)}, esperado I II III (CPC art. 381)")
    for frag in ("art. 381", "art. 382", "IN nº 161/2022", "RDC nº 724/2022",
                 "indeferimento parcial", "§ 4º"):
        check(frag in s, f"seção: '{frag}' ausente")
    for href in ("/producao-antecipada-prova/",):
        check(raw and raw.group(1).count(f'href="{href}"') >= 2,
              f"link contextual {href} ausente ou único (esperado ≥2)")
        check(os.path.exists(os.path.join(ROOT, href.strip("/"), "index.html")),
              f"link {href} não resolve")
    # Posição: depois de uma-so-chance, antes de erros
    check(doc.index('id="uma-so-chance"') < doc.index('id="producao-antecipada"') < doc.index('id="erros"'),
          "seção fora de lugar (deve ficar entre #uma-so-chance e #erros)")

    # ---- related
    rel = re.search(r"<!-- seo071:rel:start -->(.*?)<!-- seo071:rel:end -->", doc, re.S)
    check(rel and '/producao-antecipada-prova/' in rel.group(1), "related: link ausente")

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
        names = [norm(e["name"]) for e in ents]
        intake = re.search(r"<!-- faqintake:start -->.*?<h3>(.*?)</h3>", doc, re.S)
        check(intake and names[-1] == norm(intake.group(1)), "a FAQ de intake não é a última do mainEntity")
        check(doc.find("<!-- seo071:faq:start -->") < doc.find("<!-- faqintake:start -->"),
              "FAQ seo071 depois da intake no HTML")
        for q, a in FAQS:
            q, a = norm(q), norm(a)
            hit = [e for e in ents if norm(e["name"]) == q]
            check(len(hit) == 1, f"JSON-LD: FAQ '{q[:40]}…' presente {len(hit)} vezes")
            if hit:
                check(norm(hit[0]["acceptedAnswer"]["text"]) == a,
                      f"JSON-LD: resposta divergente em '{q[:40]}…'")
            check(vis.count(q) == 1, f"visível: pergunta '{q[:40]}…' aparece {vis.count(q)} vezes")
            check(a in vis, f"visível: resposta de '{q[:40]}…' diverge da fonte")
        vis_q = [norm(h) for h in re.findall(
            r"<h3>(.*?)</h3>", doc.split('<div class="faq">')[1].split("</main>")[0])]
        check(vis_q == names, "ordem visível das FAQs ≠ ordem do JSON-LD")

    # ---- datas e distribuição
    dm = re.search(r'"dateModified": "([^"]+)"', doc)
    check(dm and dm.group(1) >= "2026-09-30", "dateModified anterior à SEO-071")
    tv = re.search(r'Atualizado em <time datetime="([^"]+)"', doc)
    check(tv and dm and tv.group(1) == dm.group(1), "<time> visível ≠ dateModified")
    sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    m = re.search(SLUG + r"/</loc>\s*<lastmod>([^<]+)", sm)
    check(m and dm and m.group(1) == dm.group(1), "sitemap lastmod ≠ dateModified")
    llms = open(os.path.join(ROOT, "llms.txt"), encoding="utf-8").read()
    check("`#producao-antecipada`" in llms, "llms.txt não menciona a seção")
    check(not re.search(r"R\$\s*\d", open(PAGE, encoding="utf-8").read()),
          "página: R$ publicado em algum lugar")

    for f in fails:
        print(f"FAIL  {f}")
    print(f"{checks - len(fails)}/{checks} checagens ok")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
