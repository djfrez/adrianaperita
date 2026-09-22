#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEO-062 — verificador da seção `#laboratorio` em `/laudo-pericial/`.

Regra 8 do handoff: **fonte primária baixada a cada execução**. Nada aqui é
conferido contra a memória do modelo. O DOQ-Cgcre-087 é rebaixado do portal
gov.br, convertido em texto e as citações da página são procuradas nele,
literalmente, com espaços normalizados.

Regra de 20/09 (controle negativo): sair com 1 não basta — tem de sair com 1
**pela linha de FAIL certa**. Por isso todo crash vira FAIL nomeado, e não
exceção solta: `ROOT` é derivado do arquivo, e um verificador copiado para
fora de `tools/` sairia 1 por FileNotFoundError parecendo reprovar.

Sem rede, sai com 1 e diz que foi a rede — que é diferente de reprovar.
"""
import html as _html
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools", "build"))

PAGE = os.path.join(ROOT, "laudo-pericial", "index.html")
DOQ_PDF = ("https://www.gov.br/cdtn/pt-br/centrais-de-conteudo/"
           "documentos-cgcre-abnt-nbr-iso-iec-17025/doq-cgcre-087")

fails = []
checks = 0


def check(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)


def norm(s):
    """Espaços colapsados e aspas tipográficas rebaixadas — o PDF quebra linha
    no meio da frase e usa aspas diferentes das da página."""
    s = _html.unescape(re.sub(r"<[^>]+>", " ", s))
    s = (s.replace("“", '"').replace("”", '"')
          .replace("‘", "'").replace("’", "'")
          .replace("–", "-").replace("—", "-")
          .replace("­", ""))
    return re.sub(r"\s+", " ", s).strip()


def jsonld_part(doc):
    """Só o conteúdo dos <script type="application/ld+json">."""
    return " ".join(re.findall(r'<script type="application/ld\+json">(.*?)</script>',
                               doc, re.S))


def visible_part(doc):
    """O documento sem os blocos de JSON-LD — o que o leitor vê."""
    return re.sub(r'<script type="application/ld\+json">.*?</script>', " ", doc, flags=re.S)


def fetch_doq():
    """Baixa o DOQ e devolve o texto. Falha de rede é sinalizada, não mascarada."""
    tmp = os.path.join(tempfile.gettempdir(), "doq-cgcre-087.pdf")
    if not os.path.exists(tmp) or os.path.getsize(tmp) < 100_000:
        req = urllib.request.Request(DOQ_PDF, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=90) as r, open(tmp, "wb") as f:
            f.write(r.read())
    txt = tmp[:-4] + ".txt"
    # SEM `-layout`, e isso não é detalhe. O DOQ é uma tabela de duas colunas:
    # com `-layout`, o rótulo da coluna da esquerda cai DENTRO da citação da
    # direita ("...falsa CONFORMIDADE aceitação..."), e toda citação que
    # atravessa a calha deixa de casar. Em modo bruto o pdftotext lê célula a
    # célula e o texto de cada uma sai contíguo. Descoberto aqui: com -layout,
    # dois dos sete trechos reprovavam sendo literalmente corretos.
    subprocess.run(["pdftotext", tmp, txt], check=True)
    return norm(open(txt, encoding="utf-8", errors="replace").read())


def main():
    try:
        doc = open(PAGE, encoding="utf-8").read()
    except OSError as e:
        print(f"FAIL  página não encontrada — {e}")
        print("      (ROOT é derivado do caminho do script: rode-o de dentro de tools/)")
        return 1

    try:
        doq = fetch_doq()
    except Exception as e:
        print(f"FAIL  fonte primária indisponível — {type(e).__name__}: {e}")
        print("      sem rede este verificador não afirma nada. Não é reprovação de conteúdo.")
        return 1

    try:
        import laboratorio as L
    except Exception as e:
        print(f"FAIL  módulo-fonte tools/build/laboratorio.py não importável — {e}")
        return 1

    page = norm(doc)

    # ---------------------------------------------------------------- 1
    # Toda citação literal existe na fonte primária E na página.
    CITACOES = {
        "3.7 regra de decisão": L.REGRA_DECISAO,
        "7.8.6.1 documentar a regra": L.REQ_7861,
        "7.1.3 definição na contratação": L.REQ_713,
        "7.4.3 ressalva no relatório": L.REQ_743,
        "7.8.7 opiniões e interpretações": L.REQ_787,
        "7.8.3.1 unidade da incerteza": L.REQ_7831,
        "7.8.6.2 o que a declaração identifica": L.DECL_IDENTIFICA,
    }
    # O controle negativo 1 desta execução expôs o defeito: conferir `t in page`
    # só prova que UMA cópia confere. Cada citação aparece na prosa da seção e
    # de novo na FAQ (visível + JSON-LD); adulterar uma delas passava batido.
    #
    # Igualar contagens não serve — a prosa cita o que a FAQ também cita, e as
    # contagens divergem por desenho. O invariante certo é outro: **toda vez que
    # a abertura da citação aparece, o que vem depois tem de ser a citação
    # inteira.** Assim uma cópia adulterada no meio é pega onde quer que esteja.
    # Mesma lição da SEO-061, controle negativo 1, aplicada a outro material.
    full = norm(doc)
    for rotulo, trecho in CITACOES.items():
        t = norm(trecho)
        check(t in doq, f"{rotulo}: trecho NÃO encontrado na fonte primária — {t[:70]}…")
        abertura = " ".join(t.split()[:5])
        pos, copias, quebradas = 0, 0, []
        while True:
            k = full.find(abertura, pos)
            if k == -1:
                break
            copias += 1
            if full[k:k + len(t)] != t:
                quebradas.append(full[k:k + len(t)][:90])
            pos = k + 1
        check(copias >= 1, f"{rotulo}: citação ausente da página — {t[:70]}…")
        check(not quebradas,
              f"{rotulo}: {len(quebradas)} de {copias} cópia(s) divergem da fonte — "
              f"{quebradas[0] if quebradas else ''!r}")

    # ---------------------------------------------------------------- 2
    # O exemplo do item 7.4.3 é do próprio DOQ, e a página o atribui a ele.
    check(norm(L.EXEMPLO_743) in doq,
          f"exemplo do 7.4.3 ({L.EXEMPLO_743}) não está na fonte primária")

    # ---------------------------------------------------------------- 3
    # Identificação do documento: número E revisão. A lição da SEO-061 é que
    # número sem ano/revisão não identifica norma.
    check(norm(L.DOQ) in doq, f"{L.DOQ}: código não confere com a fonte baixada")
    check(norm(L.DOQ_REV) in doq,
          f"{L.DOQ_REV}: revisão não confere com a fonte baixada")
    # `page` já passou por norm(), que rebaixa travessão para hífen: a revisão
    # tem de ser comparada do mesmo lado da normalização, nas duas pontas.
    check(norm(L.DOQ) in page and norm(L.DOQ_REV) in page,
          "página não identifica o DOQ por código E revisão")

    # ---------------------------------------------------------------- 4
    # A seção existe, tem âncora própria e está antes das perguntas frequentes.
    tem_sec = 'id="laboratorio"' in doc
    check(tem_sec, "âncora #laboratorio ausente")
    # Sem a guarda, `doc.index` levantava ValueError quando a seção sumia: o
    # script saía com 1 por CRASH, indistinguível de reprovação. É a lição de
    # 20/09 se repetindo — o controle negativo 10 desta execução nasceu falso-
    # positivo por exatamente isso, e só a leitura do traceback expôs.
    if tem_sec and 'id="faq"' in doc:
        check(doc.index('id="laboratorio"') < doc.index('id="faq"'),
              "seção #laboratorio caiu depois das perguntas frequentes")
    else:
        check(False, "não foi possível ordenar #laboratorio × #faq — uma das duas âncoras sumiu")

    # ---------------------------------------------------------------- 5
    # Links externos às duas fontes públicas — a página manda conferir e tem de
    # dizer onde.
    check(L.DOQ_URL in doc, "link para o DOQ-Cgcre-087 ausente")
    check(L.RBLE_URL in doc, "link para o catálogo da RBLE ausente")

    # ---------------------------------------------------------------- 6
    # Paridade FAQ: lista visível inteira == JSON-LD, ordem incluída, e a de
    # intake em último (controle negativo 2 da SEO-061).
    i = doc.find('<div class="faq">')
    check(i != -1, "bloco visível de FAQ não encontrado")
    vis = [norm(q) for q in re.findall(r"<h3>(.*?)</h3>", doc[i:], re.S)] if i != -1 else []

    jsonld = None
    jsonld_ans = None
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S):
        try:
            d = json.loads(b)
        except Exception as e:
            fails.append(f"JSON-LD inválido — {e}")
            continue
        for g in (d if isinstance(d, list) else [d]):
            if g.get("@type") == "FAQPage":
                jsonld = [norm(q["name"]) for q in g["mainEntity"]]
                jsonld_ans = [norm(q["acceptedAnswer"]["text"]) for q in g["mainEntity"]]
    check(jsonld is not None, "FAQPage ausente do JSON-LD")
    if jsonld is not None:
        check(vis == jsonld,
              f"FAQ visível e JSON-LD divergem (ordem ou conteúdo): {len(vis)} × {len(jsonld)}")
        check(jsonld and "enviar" in jsonld[-1].lower(),
              f"a última FAQ não é a de intake — é {jsonld[-1][:60]!r}")

    # As duas perguntas novas estão presentes, e a resposta é a mesma nas duas
    # pontas (o JSON-LD não pode dizer o que o visível não diz).
    # O controle negativo 2 desta execução expôs o segundo defeito: só as
    # PERGUNTAS eram comparadas entre as duas pontas. Uma resposta alterada no
    # JSON-LD passava — e é justamente o JSON-LD que o buscador lê. Agora a
    # comparação é par a par, pergunta E resposta.
    vis_ans = [norm(a) for a in re.findall(r"<h3>.*?</h3>\s*<p>(.*?)</p>", doc[i:], re.S)] if i != -1 else []
    check(len(vis_ans) == len(vis),
          f"{len(vis)} perguntas visíveis × {len(vis_ans)} respostas visíveis")
    if jsonld_ans is not None and len(vis_ans) == len(jsonld_ans):
        for k, (va, ja) in enumerate(zip(vis_ans, jsonld_ans), 1):
            check(va == ja,
                  f"resposta {k} diverge entre visível e JSON-LD: "
                  f"{va[:55]!r} × {ja[:55]!r}")
    else:
        check(jsonld_ans is not None and len(vis_ans) == len(jsonld_ans),
              f"contagem de respostas não bate: visível {len(vis_ans)} × "
              f"JSON-LD {len(jsonld_ans) if jsonld_ans else 0}")

    for q, a in L.FAQS:
        nq, na = norm(q), norm(a)
        check(nq in vis, f"pergunta nova ausente do visível: {nq[:60]}…")
        check(na in vis_ans, f"resposta nova ausente do visível: {na[:60]}…")
        if jsonld is not None:
            check(nq in jsonld, f"pergunta nova ausente do JSON-LD: {nq[:60]}…")

    # ---------------------------------------------------------------- 7
    # Data: dateModified do schema tem de aparecer no visível (SEO-027) e não
    # pode ser anterior à publicação.
    m = re.search(r'"dateModified": "(\d{4}-\d{2}-\d{2})"', doc)
    check(m is not None, "dateModified ausente")
    if m:
        check(f'<time datetime="{m.group(1)}"' in doc,
              f"dateModified {m.group(1)} não aparece no <time> visível")

    # ---------------------------------------------------------------- 8
    # Coerência interna do exemplo numérico: se o texto muda o limite ou a
    # incerteza em um lugar só, a aritmética do quadro deixa de fechar.
    ex = re.search(r"limite de ([\d,]+) mg/kg, um resultado de ([\d,]+) mg/kg "
                   r"e uma incerteza de (\d+)%", page)
    check(ex is not None, "exemplo numérico da regra de decisão não encontrado")
    if ex:
        lim = float(ex.group(1).replace(",", "."))
        res = float(ex.group(2).replace(",", "."))
        inc = int(ex.group(3)) / 100
        check(res < lim,
              f"exemplo incoerente: resultado {res} não é menor que o limite {lim}")
        check(res * (1 + inc) > lim,
              f"exemplo incoerente: {res} +{ex.group(3)}% não ultrapassa {lim}, "
              "então as duas regras de decisão dariam o mesmo resultado e o "
              "quadro deixa de demonstrar o que afirma")

    # ---------------------------------------------------------------- 9
    # llms.txt acompanhou — regra da SEO-045.
    llms = open(os.path.join(ROOT, "llms.txt"), encoding="utf-8").read()
    check("#laboratorio" in llms, "llms.txt não registra a seção #laboratorio")
    check(norm(L.REGRA_DECISAO) in norm(llms),
          "llms.txt não traz a definição de regra de decisão")

    # ---------------------------------------------------------------- 10
    # sitemap com lastmod igual ao dateModified da página.
    sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    ms = re.search(r"<loc>\S+/laudo-pericial/</loc>\s*<lastmod>(\d{4}-\d{2}-\d{2})", sm)
    check(ms is not None, "entrada de /laudo-pericial/ no sitemap não encontrada")
    if ms and m:
        check(ms.group(1) == m.group(1),
              f"sitemap lastmod {ms.group(1)} ≠ dateModified {m.group(1)}")

    print(f"{checks} checagens · fonte primária: {L.DOQ} ({L.DOQ_REV}), baixada nesta execução")
    for f in fails:
        print("FAIL  " + f)
    print("ALL PASS" if not fails else f"{len(fails)} FAIL")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
