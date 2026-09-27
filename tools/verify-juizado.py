#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEO-068 — verificador da seção `#juizado` em `/dano-motor-combustivel/`.

- Lei nº 9.099/1995 (Planalto) e enunciados cíveis do FONAJE (página do CNJ)
  rebaixados a cada execução; cada dispositivo citado é procurado na fonte.
- Guarda negativa para o número afirmado: só "quarenta" e "vinte" salários
  mínimos, e nenhum valor em reais na seção (salário mínimo não conferido).
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
SLUG = "dano-motor-combustivel"
PAGE = os.path.join(ROOT, SLUG, "index.html")
L9099 = "https://www.planalto.gov.br/ccivil_03/leis/l9099.htm"
# O site do FONAJE (AMB) bloqueia acesso automatizado; o CNJ publica a mesma lista.
FONAJE = "https://www.cnj.jus.br/programas-e-acoes/juizados-especiais/enunciados-fonaje/enunciados-civeis/"

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
        from juizado import FAQS, QUADRO
    except Exception as e:
        print(f"FAIL  conteúdo-fonte tools/build/juizado.py não importa: {e}")
        return 1
    doc = open(PAGE, encoding="utf-8").read()
    vis = norm(re.sub(r'<script type="application/ld\+json">.*?</script>', " ", doc, flags=re.S))
    try:
        lei = fetch(L9099, "latin-1")  # Planalto serve ISO-8859-1
        fon = fetch(FONAJE, "utf-8")
    except Exception as e:
        print(f"FAIL  rede — fonte não baixada: {e}")
        print("      (isto é falha de rede, NÃO reprovação de conteúdo)")
        return 1

    # ---- fonte primária: cada dispositivo citado, uma ocorrência
    for frag in (
        "I - as causas cujo valor não exceda a quarenta vezes o salário mínimo",
        "§ 3º A opção pelo procedimento previsto nesta Lei importará em renúncia ao crédito excedente "
        "ao limite estabelecido neste artigo, excetuada a hipótese de conciliação",
        "Art. 9º Nas causas de valor até vinte salários mínimos, as partes comparecerão pessoalmente, "
        "podendo ser assistidas por advogado",
        "Art. 33. Todas as provas serão produzidas na audiência de instrução e julgamento",
        "Art. 35. Quando a prova do fato exigir, o Juiz poderá inquirir técnicos de sua confiança, "
        "permitida às partes a apresentação de parecer técnico",
        "realizar inspeção em pessoas ou coisas, ou determinar que o faça pessoa de sua confiança, "
        "que lhe relatará informalmente o verificado",
        "II - quando inadmissível o procedimento instituído por esta Lei ou seu prosseguimento",
        "Art. 54. O acesso ao Juizado Especial independerá, em primeiro grau de jurisdição, do "
        "pagamento de custas",
    ):
        check(lei.count(frag) == 1, f"Lei 9.099: trecho mudou ou duplicou — '{frag[:50]}…'")
    check("ENUNCIADO 12 – A perícia informal é admissível na hipótese do art. 35 da Lei 9.099/1995" in fon,
          "FONAJE: Enunciado 12 mudou")
    check("ENUNCIADO 54 – A menor complexidade da causa para a fixação da competência é aferida pelo "
          "objeto da prova e não em face do direito material" in fon, "FONAJE: Enunciado 54 mudou")

    # ---- a seção
    check(doc.count('id="juizado"') == 1, "âncora id=juizado ausente ou duplicada")
    raw = re.search(r"<!-- seo068:sec:start -->(.*?)<!-- seo068:sec:end -->", doc, re.S)
    s = norm(raw.group(1)) if raw else ""
    if not raw:
        fails.append("seção seo068 ausente")
    check(set(re.findall(r"(\w+) salários mínimos", s)) == {"quarenta", "vinte"},
          "seção: número de salários mínimos diferente de quarenta/vinte")
    check(not re.search(r"R\$\s*\d", s), "seção: valor em reais publicado sem conferência")
    for frag in ("Lei nº 9.099/1995", "art. 3º, I", "art. 3º, § 3º", "art. 9º", "art. 33",
                 "art. 35", "art. 51, II", "art. 54", "Enunciado 12 do FONAJE",
                 "Enunciado 54 do FONAJE", "permitida às partes a apresentação de parecer técnico"):
        check(frag in s, f"seção: '{frag}' ausente")
    for a, b, c in QUADRO:
        check(all(norm(x) in s for x in (a, b, c)), f"tabela: linha '{a}' ausente")
    check(raw and raw.group(1).count("<tr>") == len(QUADRO) + 1,
          "tabela: número de linhas ≠ quadro + cabeçalho")
    for href in ("/producao-antecipada-prova/", "/assistente-tecnica/", "#tres-perguntas"):
        check(raw and f'href="{href}"' in raw.group(1), f"link contextual {href} ausente")
        if href.startswith("/"):
            check(os.path.exists(os.path.join(ROOT, href.strip("/"), "index.html")), f"link {href} não resolve")
        else:
            check(f'id="{href[1:]}"' in doc, f"âncora {href} não existe na página")
    check(doc.index('id="juizado"') < doc.index('id="quesitos"'), "seção fora de lugar (deve vir antes dos quesitos)")

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
        check(vis_q == names, "ordem visível das FAQs ≠ ordem do JSON-LD")

    # ---- datas e distribuição
    dm = re.search(r'"dateModified": "([^"]+)"', doc)
    check(dm and dm.group(1) >= "2026-09-27", "dateModified anterior à SEO-068")
    sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    m = re.search(SLUG + r"/</loc>\s*<lastmod>([^<]+)", sm)
    check(m and dm and m.group(1) == dm.group(1), "sitemap lastmod ≠ dateModified")
    check("`#juizado`" in open(os.path.join(ROOT, "llms.txt"), encoding="utf-8").read(),
          "llms.txt não menciona a seção do Juizado")

    for f in fails:
        print(f"FAIL  {f}")
    print(f"{checks - len(fails)}/{checks} checagens ok")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
