#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEO-065 — verificador da seção `#cpaq` em `/produtos-quimicos-controlados/`.

Regra 8 do handoff: **fonte primária baixada a cada execução**. Nada aqui é
conferido contra a memória do modelo. Os três atos são rebaixados do Planalto e
as afirmações da página são procuradas neles, literalmente, com espaços
normalizados.

Regra de 20/09 (controle negativo): sair com 1 não basta — tem de sair com 1
**pela linha de FAIL certa**. Por isso todo crash vira FAIL nomeado, e não
exceção solta: `ROOT` é derivado do arquivo, e um verificador copiado para fora
de `tools/` sairia 1 por FileNotFoundError parecendo reprovar.

Regra da SEO-064: o invariante do `mainEntity` é **relacional** — a entrada de
intake é a última —, nunca posicional. Aqui não se checa índice de entrada
nenhuma; checa-se que as três novas estão presentes e que a de intake fechou o
array.

Sem rede, sai com 1 e diz que foi a rede — que é diferente de reprovar.
"""
import html as _html
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools", "build"))

PAGE = os.path.join(ROOT, "produtos-quimicos-controlados", "index.html")

FONTES = {
    "l11254": "https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2005/lei/l11254.htm",
    "d2074": "https://www.planalto.gov.br/ccivil_03/decreto/1996/d2074.htm",
    "d2977": "https://www.planalto.gov.br/ccivil_03/decreto/d2977.htm",
}

fails = []
checks = 0


def check(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)


def norm(s):
    """Espaços colapsados e pontuação tipográfica rebaixada — o Planalto quebra
    linha no meio da frase (inclusive entre 'Art.' e o número) e usa aspas e
    travessões diferentes dos da página."""
    s = _html.unescape(re.sub(r"<[^>]+>", " ", s))
    s = (s.replace("“", '"').replace("”", '"')
          .replace("‘", "'").replace("’", "'")
          .replace("–", "-").replace("—", "-")
          .replace("­", "").replace(" ", " "))
    return re.sub(r"\s+", " ", s).strip()


def jsonld_part(doc):
    return " ".join(re.findall(r'<script type="application/ld\+json">(.*?)</script>',
                               doc, re.S))


def visible_part(doc):
    return re.sub(r'<script type="application/ld\+json">.*?</script>', " ", doc, flags=re.S)


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    raw = urllib.request.urlopen(req, timeout=60).read()
    return norm(raw.decode("latin-1"))


def main():
    if not os.path.exists(PAGE):
        print(f"FAIL  página não encontrada: {PAGE}")
        return 1
    doc = open(PAGE, encoding="utf-8").read()
    vis, js = norm(visible_part(doc)), jsonld_part(doc)

    try:
        src = {k: fetch(u) for k, u in FONTES.items()}
    except Exception as e:
        print(f"FAIL  rede — fonte primária não baixada: {e}")
        print("      (isto é falha de rede, NÃO reprovação de conteúdo)")
        return 1

    for k, t in src.items():
        check(len(t) > 3000, f"fonte {k} veio curta demais ({len(t)} chars) — download suspeito")

    # ---------------------------------------------------------------- Lei 11.254
    # Penalidades do art. 3º, citadas na página e na FAQ.
    for frag in ("advertência",
                 "perda do bem envolvido na infração",
                 "suspensão do direito de comercializar",
                 "cassação da habilitação para atuação no comércio"):
        check(frag in src["l11254"], f"Lei 11.254: '{frag}' não encontrado na fonte")
    check("R$ 5.000,00" in src["l11254"] and "R$ 50.000,00" in src["l11254"],
          "Lei 11.254: faixa de multa R$ 5.000,00–50.000,00 não confirmada na fonte")
    check("reclusão, de 1 (um) a 10 (dez) anos" in src["l11254"],
          "Lei 11.254: pena de reclusão de 1 a 10 anos não confirmada na fonte")
    check("amplo direito de defesa" in src["l11254"],
          "Lei 11.254: amplo direito de defesa (art. 3º, § 4º) não confirmado na fonte")
    # A página afirma que multa/perda/suspensão/cassação são cumuláveis.
    check("podem ser aplicadas cumulativamente" in src["l11254"],
          "Lei 11.254: cumulatividade das penalidades não confirmada na fonte")

    # ---------------------------------------------------------------- Decreto 2.074
    check("omitirá informação ou prestará informação incorreta" in src["d2074"],
          "Decreto 2.074: infração declaratória (art. 3º, III) não confirmada na fonte")
    check("declaração inicial" in src["d2074"],
          "Decreto 2.074: declaração inicial (art. 4º, I) não confirmada na fonte")
    check("realizadas no exercício anterior" in src["d2074"],
          "Decreto 2.074: declarações de atualização do exercício anterior não confirmadas")
    check("coleta e a retirada de amostras para análise in situ ou em outro local" in src["d2074"],
          "Decreto 2.074: coleta/retirada de amostras (art. 5º, II) não confirmada na fonte")
    check("visita de verificação" in src["d2074"],
          "Decreto 2.074: visita de verificação (art. 5º, IV) não confirmada na fonte")
    check("produção, comercialização ou pesquisa" in src["d2074"],
          "Decreto 2.074: alcance do art. 4º (produção/comercialização/pesquisa) não confirmado")

    # ---------------------------------------------------------------- Decreto 2.977
    check("13 de janeiro de 1993" in src["d2977"],
          "Decreto 2.977: data de assinatura em Paris não confirmada na fonte")
    check("29 de abril de 1997" in src["d2977"],
          "Decreto 2.977: vigência para o Brasil (29/04/1997) não confirmada na fonte")
    check("Promulga a Convenção" in src["d2977"],
          "Decreto 2.977: caráter promulgatório não confirmado na fonte")

    # A divergência de fonte registrada na SEO-065: os dois decretos discordam do
    # DIA do Decreto Legislativo nº 9/1996. A guarda é que a página NÃO cite dia.
    check("6 de março de 1996" in src["d2074"] and "29 de fevereiro de 1996" in src["d2977"],
          "divergência entre 2.074 e 2.977 sobre o Decreto Legislativo nº 9 desapareceu — "
          "reler as fontes antes de acrescentar o dia na página")
    # "de 1996" é o que a página deve dizer; "de 6 de março de 1996" é o que ela
    # não pode dizer. O dia é um número de 1–2 algarismos seguido de " de ", e é
    # só isso que esta guarda proíbe — a primeira versão proibia "de \d" e
    # reprovava o próprio ano.
    check(not re.search(r"Decreto Legislativo n[ºo°]\s*9,\s*de\s*\d{1,2}\s+de\s", vis),
          "a página passou a citar o DIA do Decreto Legislativo nº 9 — as fontes discordam dele")

    # ---------------------------------------------------------------- página
    check("<h2 id=\"cpaq\">" in doc, "seção #cpaq ausente da página")
    check("<!-- seo065:sec:start -->" in doc and "<!-- seo065:sec:end -->" in doc,
          "marcadores de seção da SEO-065 ausentes")

    # Limiares: decisão registrada é NÃO publicar número. Guarda contra regressão.
    check(not re.search(r"limiar[^.]{0,120}\b\d+(?:[.,]\d+)?\s*(?:t|kg|tonelada)", vis, re.I),
          "a página passou a afirmar limiar quantitativo — não foi conferido em fonte primária")
    # Contagem, não presença — regra de 21/09. "formulário do ano-base" aparece
    # DUAS vezes no visível: a instrução da caixa do DOC e a menção na seção de
    # inspeção. A primeira versão desta guarda checava só presença, e o controle
    # negativo 5 removeu a instrução sem reprovar, porque a outra ocorrência
    # sustentava o teste. O que importa é a instrução, então ela é checada em
    # separado, com a adjacência que a torna instrução.
    check(vis.count("formulário do ano-base") == 2,
          f"'formulário do ano-base' aparece {vis.count('formulário do ano-base')}x no "
          f"visível — esperava 2 (instrução da caixa do DOC e menção na inspeção)")
    check("devem ser conferidos no formulário do ano-base" in vis,
          "a INSTRUÇÃO de conferir o limiar no formulário do ano-base desapareceu")

    # O H2 de abertura tem de estar corrigido, senão a página se contradiz.
    check("Dois regimes federais de licenciamento" in vis,
          "H2 de abertura não corrigido — a página apresenta três controles e diz 'dois regimes'")

    # dateModified × visível, mesma data.
    m = re.search(r'"dateModified": "(\d{4}-\d{2}-\d{2})"', doc)
    check(bool(m), "dateModified ausente")
    if m:
        check(m.group(1) == "2026-09-24", f"dateModified {m.group(1)} — esperava 2026-09-24")
        check("24 de setembro de 2026" in vis,
              "data de atualização visível não confere com o dateModified")

    # ------------------------------------------------- paridade visível × JSON-LD
    try:
        from cpaq import FAQS
    except Exception as e:
        print(f"FAIL  módulo de conteúdo não importável: {e}")
        return 1

    faq_block = None
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S):
        try:
            d = json.loads(b)
        except Exception as e:
            print(f"FAIL  JSON-LD não parseia: {e}")
            return 1
        if isinstance(d, dict) and d.get("@type") == "FAQPage":
            faq_block = d
    check(faq_block is not None, "FAQPage não encontrado na página")

    if faq_block:
        ents = faq_block.get("mainEntity", [])
        names = [e.get("name", "") for e in ents]
        for q, a in FAQS:
            plain_q = norm(q)
            plain_a = norm(a)
            check(plain_q in names, f"FAQ ausente do JSON-LD: {plain_q[:60]}")
            check(plain_q in vis, f"FAQ ausente do texto visível: {plain_q[:60]}")
            found = next((e for e in ents if e.get("name") == plain_q), None)
            if found:
                txt = norm(found["acceptedAnswer"]["text"])
                check(txt == plain_a,
                      f"resposta do JSON-LD diverge da fonte: {plain_q[:50]}")
                check(plain_a in vis,
                      f"resposta não aparece no texto visível: {plain_q[:50]}")
        # Invariante RELACIONAL (SEO-064): a de intake é a ÚLTIMA — e qual é ela
        # se **lê do arquivo**, pelos marcadores da SEO-046, nunca se adivinha por
        # palavra-chave. A primeira versão desta guarda procurava "primeiro
        # contato" no texto e reprovou uma página em que a pergunta de intake tem
        # outra redação: é a regra de 21/09 (invariante lido da fonte) sendo
        # quebrada dentro do próprio verificador que a invoca.
        mk = re.search(r"<!-- faqintake:start -->(.*?)<!-- faqintake:end -->", doc, re.S)
        check(bool(mk), "marcadores de intake da SEO-046 não encontrados na página")
        if mk:
            intake_qs = [norm(h) for h in re.findall(r"<h3>(.*?)</h3>", mk.group(1), re.S)]
            check(len(intake_qs) == 1,
                  f"bloco de intake tem {len(intake_qs)} perguntas — esperava 1")
            if intake_qs:
                check(bool(names) and names[-1] == intake_qs[0],
                      f"a última entrada do mainEntity não é a de intake lida do arquivo "
                      f"({intake_qs[0][:50]}): {names[-1][:50] if names else '—'}")

    # números citados na FAQ têm de bater com a fonte, não só com o corpo
    check("R$ 5.000,00 a R$ 50.000,00" in vis,
          "faixa de multa não aparece no texto visível na forma conferida")

    print(f"{checks} checagens · {len(fails)} falha(s)")
    for f in fails:
        print(f"FAIL  {f}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
