#!/usr/bin/env python3
"""SEO-061 — verificador da reconferência do quadro de vigência.

Confere a página contra as FONTES PRIMÁRIAS, baixadas a cada execução:
  · Planalto — Decreto nº 9.013/2017 (RIISPOA), Decreto nº 12.502/2025,
    Lei nº 9.605/1998, Lei nº 9.847/1999, Lei nº 6.437/1977, Lei nº 6.938/1981,
    Decreto nº 6.514/2008;
  · ANP — comunicado oficial do E32.

Sem rede, sai com 1: aprovar sem conferir é pior que não conferir.
Uso: /usr/bin/python3 tools/verify-revigencia.py
"""
import html
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, "normas-tecnicas-pericia", "index.html")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122.0 Safari/537.36")

FAILS = []
OKS = 0


def check(cond, msg):
    global OKS
    if cond:
        OKS += 1
    else:
        FAILS.append(msg)


def fetch(url):
    r = subprocess.run(["curl", "-sS", "-L", "--max-time", "150", "-A", UA, url],
                       capture_output=True)
    raw = r.stdout
    if len(raw) < 3000:
        print(f"FATAL: sem rede ou fonte indisponível: {url} ({len(raw)} bytes)")
        sys.exit(1)
    try:
        txt = raw.decode("utf-8")
    except UnicodeDecodeError:
        txt = raw.decode("latin-1")
    txt = re.sub(r"<[^>]+>", " ", txt)
    txt = html.unescape(txt)
    return re.sub(r"[ \t\xa0\n\r]+", " ", txt)


def flat(doc):
    t = re.sub(r"<script.*?</script>", " ", doc, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"[ \t\xa0\n\r]+", " ", html.unescape(t))


def ld(doc):
    out = []
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S):
        out.append(json.loads(m.group(1)))
    return out


def main():
    doc = open(PAGE, encoding="utf-8").read()
    body = flat(doc)
    blocks = ld(doc)
    faq = next(b for b in blocks if b.get("@type") == "FAQPage")
    qs = faq["mainEntity"]

    # ── 1. estrutura e invariantes ─────────────────────────────────────────
    check(qs[-1]["name"].startswith("Como verificar se a norma técnica"),
          "a FAQ de intake deixou de ser a última do JSON-LD")
    # A ordem e o conjunto precisam ser conferidos DENTRO do contêiner da FAQ.
    # Conferir só o JSON-LD aprovaria uma pergunta visível intrusa depois da de
    # intake — foi o que o controle negativo 6 flagrou nesta execução.
    fm = re.search(r'<div class="faq">(.*?)\n  </div>', doc, re.S)
    check(fm is not None, "contêiner <div class=\"faq\"> não localizado")
    faq_html = fm.group(1) if fm else ""
    vis = [re.sub(r"\s+", " ", html.unescape(v)).strip()
           for v in re.findall(r"<h3>(.*?)</h3>", faq_html, re.S)]
    names = [q["name"] for q in qs]
    check(vis == names,
          f"ordem/conjunto da FAQ visível diverge do JSON-LD: "
          f"{[v for v in vis if v not in names] or 'mesma lista, ordem diferente'}")
    check(vis and vis[-1].startswith("Como verificar se a norma técnica"),
          f"a FAQ de intake deixou de ser a última visível (última: {vis[-1][:50] if vis else '?'})")

    # paridade integral pergunta a pergunta
    for q in qs:
        name = q["name"]
        ans = q["acceptedAnswer"]["text"]
        check(f"<h3>{html.escape(name, quote=False)}</h3>" in doc,
              f"pergunta ausente do HTML visível: {name[:60]}")
        check(re.sub(r"\s+", " ", ans) in re.sub(r"\s+", " ", body),
              f"resposta do JSON-LD não bate com o texto visível: {name[:60]}")

    # a pergunta antiga da gasolina não pode ter sobrado em lugar nenhum
    check("O que mudou na especificação da gasolina em 2025?" not in doc,
          "a pergunta antiga da gasolina ainda está na página")
    check("30% de etanol anidro (E30)</strong> e a premium" not in doc,
          "o parágrafo antigo do E30 ainda está na página")

    # datas
    check('"dateModified": "2026-09-20"' in doc, "dateModified não é 2026-09-20")
    check('Atualizado em <time datetime="2026-09-20">' in doc, "<time> visível não é 2026-09-20")
    check("Quadro de vigência — situação em 20 de setembro de 2026" in doc,
          "o h2 do quadro não traz a data da reconferência")
    check("Situação em 20/09/2026" in doc, "o cabeçalho da coluna não traz a data nova")
    check("As quatro armadilhas de vigência" in doc, "as armadilhas continuam sendo três")

    # ── 2. gasolina: comunicado oficial da ANP ─────────────────────────────
    anp = fetch("https://www.gov.br/anp/pt-br/canais_atendimento/imprensa/"
                "noticias-comunicados/e32-gasolina-com-32-de-etanol-passa-a-valer-"
                "temporariamente-a-partir-de-amanha-1-8")
    check("32%" in anp and "etanol anidro" in anp,
          "a fonte da ANP não confirma o teor de 32%")
    check("gasolina C comum" in anp, "a fonte da ANP não menciona a gasolina C comum")
    check(re.search(r"premium\s+permanece\s+em\s+25", anp) is not None,
          "a fonte da ANP não confirma que a premium permanece em 25%")
    check("180 dias" in anp, "a fonte da ANP não confirma os 180 dias")
    check("94,0" in anp, "a fonte da ANP não confirma o RON em 94,0")
    check("15-B" in anp, "a fonte da ANP não menciona o art. 15-B")

    # a página não pode afirmar E30 como teor vigente
    check(not re.search(r"(?:hoje|atualmente|vigente)[^.]{0,80}30% de etanol", body),
          "a página ainda apresenta o E30 como teor vigente")
    for needle in ("32% de etanol anidro (E32)", "01/08/2026",
                   "Resolução CNPE nº 9, de 14/07/2026"):
        check(needle in body, f"afirmação ausente do corpo: {needle}")

    # TODAS as afirmações de teor da gasolina C comum devem ser 32/E32, e o
    # par número-sigla tem de ser coerente. Checar só a presença de "32%"
    # aprovaria a página com uma das três cópias trocada para E30 — foi o que
    # o controle negativo 1 flagrou nesta execução.
    pares = re.findall(r"(\d\d)% de etanol anidro \(E(\d\d)\)", body)
    check(len(pares) >= 3, f"esperava ao menos 3 afirmações de teor, achei {len(pares)}")
    check(all(a == b for a, b in pares),
          f"percentual e sigla divergem entre si: {pares}")
    check({a for a, _ in pares} == {"32"},
          f"teor divergente da gasolina C comum: {sorted({a for a, _ in pares})}")
    # o E30 só pode aparecer como período encerrado, nunca como teor atual
    check("Entre 01/08/2025 e 31/07/2026 o teor era de 30% (E30)" in body
          or "Entre 1º de agosto de 2025 e 31 de julho de 2026 o teor era de 30% (E30)" in body,
          "o E30 não está delimitado como período encerrado")

    # ── 3. RIISPOA e Decreto 12.502/2025 no Planalto ───────────────────────
    d12502 = fetch("https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/d12502.htm")
    check("DECRETO Nº 12.502, DE 11 DE JUNHO DE 2025" in d12502.upper(),
          "não confirmei a identificação do Decreto nº 12.502/2025")
    check("14.515" in d12502, "o Decreto 12.502/2025 não remete à Lei nº 14.515/2022")
    m = re.search(r"XII - do Decreto nº 9\.013, de 29 de março de 2017\s*:(.{0,220})", d12502)
    check(m is not None, "art. 40, XII do Decreto 12.502/2025 não localizado")
    if m:
        seg = m.group(1)
        for needle in ("474-B", "520", "522", "525"):
            check(needle in seg, f"art. 40, XII não lista o art. {needle} como revogado")
    check(re.search(r"prazo de vinte dias, contado da data de seu recebimento, para a "
                    r"apresentação de defesa", d12502) is not None,
          "o prazo de 20 dias para defesa não confere na fonte")
    check("dias corridos" in d12502, "a contagem em dias corridos não confere na fonte")
    check("Comissão Especial de Recursos de Defesa Agropecuária" in d12502,
          "a terceira instância não confere na fonte")

    riispoa = fetch("https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/decreto/d9013.htm")
    check(re.search(r"Art\. 474-A\..{0,320}formação e competência técnica", riispoa, re.S) is not None,
          "art. 474-A do RIISPOA não confere na fonte")
    check("será considerado protelatório" in riispoa,
          "o efeito protelatório do art. 474-A, § 1º, não confere na fonte")
    check(re.search(r"Art\. 474-B\..{0,200}prazo de dez dias", riispoa, re.S) is not None,
          "os dez dias do art. 474-B, caput, não conferem na fonte")
    check(re.search(r"§ 1º Aplica-se à contagem.{0,400}Revogado pelo Decreto nº 12\.502",
                    riispoa, re.S) is not None,
          "a revogação do § 1º do art. 474-B não confere na fonte")
    check(re.search(r"VII - prazo de validade e identificação do lote;\s*\(Redação dada pelo "
                    r"Decreto nº 10\.468", riispoa) is not None,
          "art. 443, VII, na redação do Decreto 10.468/2020 não confere na fonte")
    # a página precisa dizer as duas coisas
    for needle in ("Decreto nº 12.502/2025", "474-A", "protelatório"):
        check(needle in body, f"afirmação ausente do corpo: {needle}")

    # TODAS as afirmações sobre o prazo de defesa/recurso do novo rito devem
    # dizer 20. Checar presença isolada aprovaria a página com uma das cópias
    # trocada — foi assim que três controles negativos passaram em 19/09.
    prazos = set(re.findall(r"(?:defesa e recursos|defesa|recurso)[^.]{0,60}?em (\w+) dias", body))
    prazos |= set(re.findall(r"passou a ser de (\w+) dias", body))
    prazos |= set(re.findall(r"também passou a (\w+) dias", body))
    check(prazos <= {"20"} and prazos,
          f"prazo divergente do novo rito do MAPA: {prazos or 'nenhum'}")
    # e os prazos REVOGADOS só podem aparecer como history, nunca como vigentes
    check("era de 30 dias pelo art. 525" in body,
          "a página não contrasta o prazo revogado de 30 dias com o novo")

    # ── 4. Lei nº 9.847/1999 na redação da Lei nº 14.993/2024 ──────────────
    l9847 = fetch("https://www.planalto.gov.br/ccivil_03/leis/l9847.htm")
    check(re.search(r"Art\. 1º Será realizada pela Agência Nacional do Petróleo.{0,160}"
                    r"Redação dada pela Lei nº 14\.993", l9847, re.S) is not None,
          "a redação do art. 1º da Lei 9.847 pela Lei 14.993/2024 não confere na fonte")
    for needle in ("combustíveis sintéticos", "estocagem geológica"):
        check(needle in l9847, f"a Lei 9.847 não traz '{needle}' na fonte")
    check("na redação da Lei nº 14.993/2024" in body,
          "a página não registra a redação da Lei 14.993/2024 na linha da Lei 9.847")

    # ── 5. Lei nº 6.437/1977, art. 10, XVIII — redação vigente ─────────────
    l6437 = fetch("https://www.planalto.gov.br/ccivil_03/leis/l6437.htm")
    check(re.search(r"XVIII - importar ou exportar, expor à venda ou entregar ao consumo.{0,160}"
                    r"Medida Provisória nº 2\.190-34", l6437, re.S) is not None,
          "a redação vigente do art. 10, XVIII, da Lei 6.437 não confere na fonte")
    check("Medida Provisória nº 2.190-34/2001" in body,
          "a página não registra a redação vigente do art. 10, XVIII")

    # ── 6. linhas ambientais — reconferência ───────────────────────────────
    l9605 = fetch("https://www.planalto.gov.br/ccivil_03/leis/l9605.htm")
    check("mínimo de R$ 50,00" in l9605 and "R$ 50.000.000,00" in l9605,
          "o piso e o teto do art. 75 da Lei 9.605 não conferem na fonte")
    m = re.search(r"Lei nº 15\.355", l9605)
    check(m is not None, "a Lei nº 15.355/2026 não aparece na Lei 9.605")
    if m:
        seg = l9605[max(0, m.start() - 1400):m.start()]
        arts = re.findall(r"Art\. (\d+)", seg)
        check(arts and arts[-1] == "32",
              f"a Lei 15.355/2026 não está restrita ao art. 32 (achei art. {arts[-1] if arts else '?'})")
    check("restrita ao art. 32" in body,
          "a página não registra que a Lei 15.355/2026 se restringe ao art. 32")

    l6938 = fetch("https://www.planalto.gov.br/ccivil_03/leis/l6938.htm")
    check("independentemente da existência de culpa" in l6938,
          "a responsabilidade objetiva do art. 14, § 1º, da Lei 6.938 não confere na fonte")

    d6514 = fetch("https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/decreto/d6514.htm")
    ds = sorted({int(x.replace(".", "")) for x in re.findall(r"Decreto nº (1[0-9]\.\d{3}), de 20\d\d", d6514)})
    check(ds and ds[-1] == 12877,
          f"a alteração mais recente do Decreto 6.514 não é a 12.877 (achei {ds[-1] if ds else '?'})")

    # ── 7. JSON-LD íntegro ─────────────────────────────────────────────────
    check(len(blocks) == 3, f"esperava 3 blocos ld+json, achei {len(blocks)}")

    print(f"\n{OKS} checagens ok, {len(FAILS)} falha(s)")
    for f in FAILS:
        print("  FAIL", f)
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
