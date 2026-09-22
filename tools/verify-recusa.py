#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificador da SEO-063 em /impugnacao-laudo-pericial/ — 16º da suíte.

O que ele prova, e por que cada checagem existe:

  · As nove citações literais do CPC são procuradas **no texto oficial do
    Planalto baixado nesta execução**. Sem rede, o script sai com 1 dizendo
    que foi a rede — que é diferente de reprovar.
  · Cada artigo citado tem de ter **uma única ocorrência** no arquivo do
    Planalto. É a regra "todas as ocorrências, ficar com a última" invertida em
    guarda: se aparecer mais de uma, há redação alterada e a citação precisa
    ser reconferida à mão antes de o verificador voltar a passar.
  · **Invariante de citação (lição do controle negativo 1 da SEO-062):** não
    basta "o trecho está na página" — toda vez que a abertura da citação
    aparece, o que vem depois tem de ser a citação inteira. Cada citação
    aparece na prosa e de novo na FAQ, e `trecho in doc` só prova que *alguma*
    cópia confere.
  · **Paridade FAQ par a par, pergunta E resposta** (lição do controle negativo
    2 da SEO-062): é o JSON-LD que o buscador lê.
  · A entrada de intake da SEO-046 continua sendo a **última** do `mainEntity`.
    Relação, não posição fixa — proxy posicional envelhece (SEO-062).
  · Guarda de estrutura: nenhuma busca de âncora sem checar o resultado, para
    que a remoção de uma seção reprove com FAIL e não com ValueError (lição do
    controle negativo 10 da SEO-062).
"""
import html as _html
import json
import os
import re
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools", "build"))
from recusa import (CITACOES, FAQS, INSTRUMENTOS, LEI_URL, MOTIVOS)

PAGE = os.path.join(ROOT, "impugnacao-laudo-pericial", "index.html")
ARTIGOS = ["Art. 144.", "Art. 145.", "Art. 148.", "Art. 149.", "Art. 465.",
           "Art. 466.", "Art. 467.", "Art. 468.", "Art. 477."]

fails = []
n = 0


def check(cond, msg):
    global n
    n += 1
    if not cond:
        fails.append(msg)


def norm(s):
    """Texto comparável: sem tags, sem entidade, aspas e espaços normalizados."""
    s = _html.unescape(re.sub(r"<[^>]+>", "", s))
    s = s.replace("“", '"').replace("”", '"').replace("’", "'")
    s = s.replace(" ", " ").replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", s).strip()


# --------------------------------------------------------------------------
# 1. fonte primária
# --------------------------------------------------------------------------
def planalto():
    req = urllib.request.Request(LEI_URL, headers={"User-Agent": "Mozilla/5.0"})
    raw = urllib.request.urlopen(req, timeout=60).read()
    for enc in ("utf-8", "latin-1"):
        try:
            return norm(raw.decode(enc))
        except UnicodeDecodeError:
            continue
    return norm(raw.decode("latin-1", errors="replace"))


try:
    lei = planalto()
except (urllib.error.URLError, OSError, TimeoutError) as e:
    print(f"REDE: não foi possível baixar o texto do CPC ({e}).")
    print("Sem fonte primária não há verificação de citação. Isto NÃO é reprovação de conteúdo.")
    sys.exit(1)

check(len(lei) > 500_000, "texto do Planalto veio curto demais para ser a lei inteira")

for art in ARTIGOS:
    c = lei.count(art)
    check(c == 1, f"{art} aparece {c}x no Planalto — redação alterada? reconferir à mão")

for cit in CITACOES:
    check(norm(cit) in lei, f"citação não encontrada na fonte primária: {norm(cit)[:70]}…")

# --------------------------------------------------------------------------
# 2. página: seção, âncora, tabelas
# --------------------------------------------------------------------------
doc = open(PAGE, encoding="utf-8").read()
flat = norm(doc)

check('id="recusa"' in doc, 'âncora id="recusa" ausente da página')
check("<!-- seo063:sec:start -->" in doc and "<!-- seo063:sec:end -->" in doc,
      "marcadores da seção SEO-063 ausentes")

i = doc.find("<!-- seo063:sec:start -->")
j = doc.find("<!-- seo063:sec:end -->")
check(i != -1 and j != -1 and j > i, "seção SEO-063 ausente ou marcadores fora de ordem")
sec = doc[i:j] if (i != -1 and j != -1 and j > i) else ""

for a, *_ in MOTIVOS:
    check(norm(a) in norm(sec), f"linha da tabela de motivos ausente: {norm(a)[:60]}…")
for a, *_ in INSTRUMENTOS:
    check(norm(a) in norm(sec), f"linha da tabela de instrumentos ausente: {norm(a)[:60]}…")

check(norm(sec).count("Art. 144") >= 1 and norm(sec).count("Art. 145") >= 1,
      "a seção precisa citar os arts. 144 e 145, que são a origem dos motivos")

# --------------------------------------------------------------------------
# 3. invariante de citação: toda abertura tem de ser seguida da citação inteira
# --------------------------------------------------------------------------
for cit in CITACOES:
    c = norm(cit)
    head = c[:36]
    copies = [m.start() for m in re.finditer(re.escape(head), flat)]
    check(len(copies) >= 1, f"citação ausente da página: {c[:60]}…")
    bad = [k for k, p in enumerate(copies, 1) if not flat.startswith(c, p)]
    check(not bad, f"citação adulterada em {len(bad)} de {len(copies)} cópias: {c[:60]}…")

# --------------------------------------------------------------------------
# 4. FAQ: paridade par a par entre visível e JSON-LD, e intake por último
# --------------------------------------------------------------------------
blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S)
check(bool(blocks), "nenhum bloco JSON-LD na página")
faqpage = None
for b in blocks:
    try:
        data = json.loads(b)
    except Exception as e:
        check(False, f"JSON-LD inválido: {e}")
        continue
    for node in (data if isinstance(data, list) else [data]):
        for g in (node.get("@graph", []) if isinstance(node, dict) else []) or \
                 ([node] if isinstance(node, dict) else []):
            if isinstance(g, dict) and g.get("@type") == "FAQPage":
                faqpage = g

check(faqpage is not None, "FAQPage não encontrado no JSON-LD")
jsonld = [(norm(q.get("name", "")), norm(q.get("acceptedAnswer", {}).get("text", "")))
          for q in (faqpage or {}).get("mainEntity", [])]

m = re.search(r'<div class="faq">(.*?)</div>\s*</section>', doc, re.S)
faq_html = m.group(1) if m else doc[doc.find('<div class="faq">'):doc.find("<h2>Laudo desfavorável")]
check(bool(faq_html.strip()), "bloco visível de FAQ não localizado")
visible = [(norm(q), norm(a)) for q, a in
           re.findall(r"<h3>(.*?)</h3>\s*<p>(.*?)</p>", faq_html, re.S)]

check(len(visible) == len(jsonld),
      f"FAQ visível ({len(visible)}) e JSON-LD ({len(jsonld)}) têm contagens diferentes")
for k, (v, j_) in enumerate(zip(visible, jsonld), 1):
    check(v[0] == j_[0], f"FAQ {k}: pergunta divergente entre visível e JSON-LD")
    check(v[1] == j_[1], f"FAQ {k}: resposta divergente entre visível e JSON-LD")

for q, a in FAQS:
    nq, na = norm(q), norm(a)
    check(any(nq == x for x, _ in jsonld), f"FAQ nova ausente do JSON-LD: {nq[:60]}…")
    check(any(nq == x and na == y for x, y in jsonld),
          f"FAQ nova com resposta divergente no JSON-LD: {nq[:60]}…")
    idx = [k for k, (x, _) in enumerate(jsonld) if x == nq]
    check(bool(idx) and idx[0] < len(jsonld) - 1,
          f"FAQ nova não pode ser a última — a de intake é contratualmente a última: {nq[:50]}…")

# A de intake não se reconhece por palavra-chave adivinhada — reconhece-se pelo
# marcador que a SEO-046 deixou no arquivo. Invariante relacional: ela é a
# última do mainEntity, seja qual for a sua redação.
mi = re.search(r"<!-- faqintake:start -->(.*?)<!-- faqintake:end -->", doc, re.S)
check(mi is not None, "marcador de intake da SEO-046 não encontrado na página")
mq = re.search(r"<h3>(.*?)</h3>", mi.group(1), re.S) if mi else None
check(mq is not None, "pergunta de intake não encontrada dentro do marcador")
if mq:
    nq = norm(mq.group(1))
    check(bool(jsonld) and jsonld[-1][0] == nq,
          "a entrada de intake da SEO-046 deixou de ser a última do mainEntity")

# --------------------------------------------------------------------------
# 5. datas, sitemap, llms.txt
# --------------------------------------------------------------------------
DATA = "2026-09-22"
check(f'"dateModified": "{DATA}"' in doc, f"dateModified não está em {DATA}")
check(f'Atualizado em <time datetime="{DATA}">' in doc, f"<time> visível não está em {DATA}")
check("2026-09-09" not in doc, "sobrou a data anterior (2026-09-09) na página")

sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
k = sm.find("https://adrianarezende.com.br/impugnacao-laudo-pericial/")
check(k != -1, "página ausente do sitemap")
check(k != -1 and f"<lastmod>{DATA}</lastmod>" in sm[k:k + 300],
      f"lastmod do sitemap fora de sincronia com {DATA}")

llms = norm(open(os.path.join(ROOT, "llms.txt"), encoding="utf-8").read())
for marca in ("art. 148, §1º", "art. 148, §2º", "art. 149", "art. 466, §1º", "art. 467"):
    check(norm(marca) in llms, f"llms.txt não registra {marca}")

# --------------------------------------------------------------------------
print(f"verify-recusa: {n} checagens")
if fails:
    for f in fails:
        print(f"  FAIL  {f}")
    sys.exit(1)
print("  OK")
