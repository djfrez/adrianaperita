# -*- coding: utf-8 -*-
"""SEO-061 — reconferência do quadro de vigência de /normas-tecnicas-pericia/.

O quadro estava datado de 18/08/2026 numa página cuja promessa é justamente
dizer qual norma vale na data do fato. Esta é a reconferência de 20/09/2026,
com três correções materiais achadas na fonte primária:

  1. gasolina: E30 -> E32 desde 01/08/2026 (Resolução CNPE nº 9, de 14/07/2026);
  2. RIISPOA: o rito do processo administrativo foi revogado pelo Decreto
     nº 12.502/2025, que passou a reger a matéria com prazos diferentes;
  3. Lei nº 9.847/1999 na redação da Lei nº 14.993/2024.

Fonte única das perguntas: FAQ_NEW/FAQ_REWRITE abaixo geram o HTML visível e o
JSON-LD da mesma estrutura — 14ª aplicação do método da SEO-037. A inserção no
FAQPage é feita sobre o JSON parseado, nunca por casamento de indentação
(regra 6 do handoff de 05/09), e todos os blocos ld+json são reparseados antes
de gravar.

Uso: python3 tools/build/revigencia.py [--check]
"""
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGE = os.path.join(ROOT, "normas-tecnicas-pericia", "index.html")

DATA = "2026-09-20"
DATA_BR = "20 de setembro de 2026"
DATA_CURTA = "20/09/2026"

# ── Substituições de texto: (o que sai, o que entra, rótulo) ────────────────
# Cada par é aplicado uma vez. Se o texto novo já estiver na página, o par é
# considerado cumprido — é o que torna a reaplicação idempotente.

REPLACES = [

    # 1. cabeçalho do quadro e da coluna de situação
    ('<h2 id="quadro">Quadro de vigência — situação em 18 de agosto de 2026</h2>',
     f'<h2 id="quadro">Quadro de vigência — situação em {DATA_BR}</h2>',
     "h2 do quadro"),

    ('<th scope="col">Situação em 18/08/2026</th>',
     f'<th scope="col">Situação em {DATA_CURTA}</th>',
     "cabeçalho da coluna"),

    # 2. gasolina — a correção material do dia
    ('<td>Vigente, <strong>alterada pela Resolução ANP nº 988/2025</strong>: a gasolina C comum '
     'passou a 30% de etanol anidro (E30) e a premium a 25%, por determinação da Resolução CNPE '
     'nº 9, de 25/06/2025, com obrigatoriedade desde 01/08/2025, e o RON mínimo subiu de 93 para 94.</td>',

     '<td>Vigente, <strong>alterada pela Resolução ANP nº 988/2025</strong> (RON mínimo de 93 para '
     '94 e novos valores de massa específica). <strong>O percentual de etanol não está nela</strong>: '
     'desde <strong>01/08/2026</strong> a gasolina C comum e a comum aditivada têm <strong>32% de '
     'etanol anidro (E32)</strong>, por determinação da <strong>Resolução CNPE nº 9, de 14/07/2026</strong> '
     '— medida temporária, por 180 dias, prorrogável uma única vez. Entre 01/08/2025 e 31/07/2026 o '
     'teor era de 30% (E30). A premium segue em 25% e o RON mínimo, em 94,0.</td>',
     "linha da gasolina"),

    # 3. diesel — o teor de biodiesel mora em outra norma
    ('<td>Vigente desde 31/07/2024. Alterou limites do diesel S10 e S500, entre eles estabilidade '
     'à oxidação e ponto de entupimento.</td>',

     '<td>Vigente desde 31/07/2024. Alterou limites do diesel S10 e S500, entre eles estabilidade '
     'à oxidação e ponto de entupimento. <strong>O teor de biodiesel não está nela</strong>: é de '
     '<strong>15% (B15) desde 01/08/2025</strong>, pela Resolução CNPE nº 9/2025, e o biodiesel puro '
     'tem especificação própria na Resolução ANP nº 920/2023.</td>',
     "linha do diesel"),

    # 4. RIISPOA — o rito do processo administrativo saiu do decreto
    ('<td>Decreto nº 9.013/2017 (RIISPOA), art. 443, VII</td>\n'
     '            <td>Produtos de origem animal sob inspeção do MAPA/SIF</td>\n'
     '            <td>Vigente, na redação do Decreto nº 10.468/2020.</td>',

     '<td>Decreto nº 9.013/2017 (RIISPOA), arts. 443, VII, e 474-A a 474-B</td>\n'
     '            <td>Produtos de origem animal sob inspeção do MAPA/SIF: rotulagem e análise '
     'pericial de contraprova</td>\n'
     '            <td>Vigentes; o art. 443, VII, na redação do Decreto nº 10.468/2020. '
     '<strong>O rito do processo administrativo saiu do RIISPOA</strong>: o Decreto nº 12.502/2025 '
     '(art. 40, XII) revogou os arts. 520, 522 e 525 a 529 e o § 1º do art. 474-B, e o processo '
     'passou a correr pelo próprio Decreto nº 12.502/2025 — defesa e recursos em 20 dias, contados '
     'em dias corridos, com terceira instância na Comissão Especial de Recursos de Defesa '
     'Agropecuária.</td>',
     "linha do RIISPOA"),

    # 5. Lei nº 6.437/1977 — redação vigente do inciso
    ('<td>Infração sanitária por expor à venda produto vencido ou apor-lhe nova data</td>\n'
     '            <td>Vigente.</td>',

     '<td>Infração sanitária por importar, exportar, expor à venda ou entregar ao consumo produto '
     'com prazo de validade expirado, ou apor-lhe nova data</td>\n'
     '            <td>Vigente, na redação da Medida Provisória nº 2.190-34/2001.</td>',
     "linha da Lei 6.437"),

    # 6. Lei nº 9.847/1999 — reescrita pela lei do Combustível do Futuro
    ('<td>Sanções administrativas no abastecimento nacional de combustíveis</td>\n'
     '            <td>Vigente.</td>',

     '<td>Sanções administrativas no abastecimento nacional de combustíveis</td>\n'
     '            <td>Vigente, <strong>na redação da Lei nº 14.993/2024</strong> (Combustível do '
     'Futuro), que reescreveu os arts. 1º e 3º e estendeu a fiscalização da ANP aos combustíveis '
     'sintéticos, aos biocombustíveis e à estocagem geológica de dióxido de carbono.</td>',
     "linha da Lei 9.847"),

    # 7. a entrada de "as que mudaram" sobre a gasolina
    ('<h3 id="anp-807">Resolução ANP nº 807/2020 — a gasolina mudou em agosto de 2025</h3>',
     '<h3 id="anp-807">Resolução ANP nº 807/2020 — a gasolina mudou de novo em agosto de 2026</h3>',
     "h3 da gasolina"),

    ('<p>Desde <strong>1º de agosto de 2025</strong>, a gasolina C comum tem <strong>30% de etanol '
     'anidro (E30)</strong> e a premium, 25%, por determinação da Resolução CNPE nº 9, de 25/06/2025. '
     'A Resolução ANP nº 988/2025 ajustou a especificação da 807/2020 a esse teor e elevou o RON '
     'mínimo de 93 para 94.</p>',

     '<p>Desde <strong>1º de agosto de 2026</strong>, a gasolina C comum e a comum aditivada têm '
     '<strong>32% de etanol anidro (E32)</strong>, por determinação da <strong>Resolução CNPE nº 9, '
     'de 14 de julho de 2026</strong>, publicada no DOU de 30/07/2026, em edição extra. A medida é '
     '<strong>temporária</strong>: vale por 180 dias, prorrogáveis uma única vez por ato do '
     'Presidente do CNPE. Entre 01/08/2025 e 31/07/2026 o teor era de 30% (E30), pela Resolução CNPE '
     'nº 9, de 25/06/2025; antes disso, 27%. A gasolina premium continua em 25%.</p>\n'
     '      <p><strong>A especificação não mudou junto.</strong> A ANP registrou que a adoção do E32 '
     'não altera, por ora, as demais especificações da Resolução ANP nº 807/2020, e que o RON mínimo '
     'permanece em 94,0 — valor fixado pela Resolução ANP nº 988/2025 na passagem para o E30. '
     'O percentual obrigatório vive na resolução do CNPE; a especificação, na da ANP. Quem confere '
     'só a 807/2020 lê 30% e erra o teor vigente.</p>',
     "parágrafo da gasolina"),

    ('<p><strong>Na prática pericial:</strong> o teor de etanol é o ensaio central em quase toda '
     'perícia de adulteração de gasolina. Aplicar o limite antigo a uma amostra coletada depois de '
     '01/08/2025 produz um “fora de especificação” que não existe; aplicar o limite novo a uma coleta '
     'anterior produz uma conformidade que também não existe. <strong>A pergunta que resolve é uma só: '
     'qual era a especificação vigente na data da coleta?</strong></p>',

     '<p><strong>Na prática pericial:</strong> o teor de etanol é o ensaio central em quase toda '
     'perícia de adulteração de gasolina, e foram <strong>três teores obrigatórios em pouco mais de '
     'um ano</strong> — 27%, 30% desde 01/08/2025 e 32% desde 01/08/2026. Aplicar o limite de uma '
     'época à amostra de outra produz um “fora de especificação” que não existe, ou uma conformidade '
     'que também não existe. <strong>A pergunta que resolve é uma só: qual era o teor obrigatório na '
     'data da coleta?</strong> Há ainda a janela de trânsito: o art. 15-B da Resolução ANP nº 807/2020 '
     'é a regra criada exatamente para a mudança de percentual, e a ANP fixou prazos antes da '
     'autuação — 15 dias para distribuidoras (30 na região Norte) e 30 dias para postos revendedores '
     '(60 no Norte). Amostra colhida dentro dessa janela pode carregar a mistura anterior sem que a '
     'divergência em relação ao teor novo renda autuação.</p>',
     "prática pericial da gasolina"),

    # 8. a quarta armadilha
    ('<h2 id="armadilhas">As três armadilhas de vigência</h2>',
     '<h2 id="armadilhas">As quatro armadilhas de vigência</h2>',
     "h2 das armadilhas"),

    ('<li><strong>Tratar período de transição como se já tivesse terminado.</strong> Enquanto a '
     'transição da NBR 10004 corre, as duas versões são admissíveis. O que não se admite é aplicar '
     'uma e comparar com a outra.</li>',

     '<li><strong>Tratar período de transição como se já tivesse terminado.</strong> Enquanto a '
     'transição da NBR 10004 corre, as duas versões são admissíveis. O que não se admite é aplicar '
     'uma e comparar com a outra.</li>\n'
     '      <li><strong>Tomar o número da norma por identificação suficiente.</strong> A Resolução '
     'CNPE nº 9 <em>de 2025</em> fixou o E30 e o B15; a Resolução CNPE nº 9 <em>de 2026</em> fixou o '
     'E32. Mesmo número, mesmo conselho, mesma matéria, e ambas com efeito a partir de 1º de agosto. '
     'Citação sem o ano não identifica a norma aplicada — e aqui a diferença entre as duas é o teor '
     'obrigatório contra o qual a amostra foi confrontada.</li>',
     "quarta armadilha"),
]

# ── FAQ: fonte única do visível e do JSON-LD ────────────────────────────────

FAQ_REWRITE = [(
    "O que mudou na especificação da gasolina em 2025?",
    "Qual é o teor de etanol na gasolina hoje, e qual valia na data da coleta?",
    "Desde 1º de agosto de 2026 a gasolina C comum e a comum aditivada têm 32% de etanol anidro "
    "(E32), por determinação da Resolução CNPE nº 9, de 14 de julho de 2026 — medida temporária, "
    "com 180 dias de vigência, prorrogáveis uma única vez. Entre 1º de agosto de 2025 e 31 de julho "
    "de 2026 o teor era de 30% (E30), pela Resolução CNPE nº 9, de 25 de junho de 2025; antes disso, "
    "27%. A gasolina premium permanece em 25%. O percentual obrigatório não está na Resolução ANP "
    "nº 807/2020, que traz a especificação e cujo RON mínimo segue em 94,0 — conferir apenas a "
    "resolução da ANP leva ao teor errado. Em perícia de adulteração, o limite aplicável é o da data "
    "da coleta da amostra, não o da data do laudo."
)]

FAQ_NEW = [
    ("Mudou o prazo de defesa em auto de infração do MAPA/SIF?",
     "Mudou, e o rito inteiro saiu de onde estava. O Decreto nº 12.502/2025, que regulamenta a Lei "
     "nº 14.515/2022, revogou os arts. 520, 522 e 525 a 529 do RIISPOA (Decreto nº 9.013/2017) e "
     "passou a reger o processo administrativo de fiscalização agropecuária. A defesa, que era de "
     "30 dias pelo art. 525 do RIISPOA, passou a ser de 20 dias contados do recebimento do auto de "
     "infração (art. 3º, § 1º, II); o recurso, que era de 10 dias, também passou a 20 dias (arts. 6º "
     "e 7º), agora com três instâncias, a última na Comissão Especial de Recursos de Defesa "
     "Agropecuária. Os prazos correm em dias corridos, excluído o dia do início e incluído o do "
     "término, prorrogando-se para o primeiro dia útil (art. 8º). Como o decreto entrou em vigor em "
     "12 de junho de 2025, o prazo aplicável é o da data do auto: autuação anterior segue o rito "
     "revogado."),

    ("Quem pode ser assistente técnico na análise pericial de contraprova do MAPA?",
     "Só quem comprovar formação e competência técnica para acompanhar aquela análise, segundo os "
     "critérios definidos pelo Ministério da Agricultura (art. 474-A do Decreto nº 9.013/2017, "
     "incluído pelo Decreto nº 10.468/2020). A consequência de errar a indicação é severa e pouco "
     "conhecida: se o indicado não atender aos requisitos, o pedido de análise pericial de "
     "contraprova é considerado protelatório, é indeferido, e prevalece o resultado da análise "
     "fiscal (§§ 1º e 2º) — a empresa perde a contraprova sem que o mérito seja examinado. A "
     "manifestação adicional sobre o resultado continua sendo de dez dias contados da assinatura da "
     "ata (art. 474-B, caput), mas o § 1º, que dizia como contá-los, foi revogado pelo Decreto nº "
     "12.502/2025; a contagem passou a seguir o art. 8º desse decreto."),
]

ANCHOR_FAQ = "      <!-- amb047:faq:start -->"


def faq_visible(q, a):
    return ("      <div>\n"
            f"        <h3>{html.escape(q, quote=False)}</h3>\n"
            f"        <p>{html.escape(a, quote=False)}</p>\n"
            "      </div>")


# ── JSON-LD ────────────────────────────────────────────────────────────────

def ld_blocks(doc):
    return list(re.finditer(r'(<script type="application/ld\+json">)(.*?)(</script>)', doc, re.S))


def patch_faqpage(doc):
    """Reescreve e insere perguntas no FAQPage manipulando o JSON parseado."""
    changed = False
    for m in ld_blocks(doc):
        try:
            obj = json.loads(m.group(2))
        except json.JSONDecodeError as e:
            raise SystemExit(f"JSON-LD inválido antes de editar: {e}")
        if not (isinstance(obj, dict) and obj.get("@type") == "FAQPage"):
            continue
        entries = obj["mainEntity"]

        for old_q, new_q, new_a in FAQ_REWRITE:
            for e in entries:
                if e["name"] == old_q:
                    e["name"] = new_q
                    e["acceptedAnswer"]["text"] = new_a
                    changed = True

        have = {e["name"] for e in entries}
        # âncora: as novas entram antes da pergunta da SEO-047, que por sua vez
        # precede a de intake — a de intake continua sendo a última.
        idx = next((i for i, e in enumerate(entries)
                    if e["name"].startswith("Quando a multa de um auto")), len(entries) - 1)
        add = [{"@type": "Question", "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a}}
               for q, a in FAQ_NEW if q not in have]
        if add:
            obj["mainEntity"] = entries[:idx] + add + entries[idx:]
            changed = True

        if changed:
            body = json.dumps(obj, ensure_ascii=False, indent=2)
            body = "\n".join("  " + ln for ln in body.splitlines())
            doc = doc[:m.start()] + m.group(1) + "\n" + body + "\n  " + m.group(3) + doc[m.end():]
        return doc, changed
    raise SystemExit("FAQPage não encontrado")


def verify_ld(doc):
    for m in ld_blocks(doc):
        json.loads(m.group(2))   # levanta se algum bloco ficou inválido


# ── Aplicação ──────────────────────────────────────────────────────────────

def apply(doc):
    changed = False

    for old, new, label in REPLACES:
        if new in doc:
            continue                      # já aplicado
        if doc.count(old) != 1:
            raise SystemExit(f"âncora ausente ou ambígua ({label}): {doc.count(old)} ocorrências")
        doc = doc.replace(old, new)
        changed = True

    # FAQ visível
    have_vis = []
    for q, a in FAQ_NEW:
        if f"<h3>{html.escape(q, quote=False)}</h3>" not in doc:
            have_vis.append(faq_visible(q, a))
    if have_vis:
        if ANCHOR_FAQ not in doc:
            raise SystemExit("âncora da FAQ visível não encontrada")
        doc = doc.replace(ANCHOR_FAQ, "\n".join(have_vis) + "\n" + ANCHOR_FAQ, 1)
        changed = True

    for old_q, new_q, new_a in FAQ_REWRITE:
        old_h = f"<h3>{html.escape(old_q, quote=False)}</h3>"
        if old_h in doc:
            i = doc.find(old_h)
            j = doc.find("</p>", i)
            doc = (doc[:i] + f"<h3>{html.escape(new_q, quote=False)}</h3>\n"
                   f"        <p>{html.escape(new_a, quote=False)}" + doc[j:])
            changed = True

    doc, ld_changed = patch_faqpage(doc)
    changed = changed or ld_changed

    # datas — só quando houve mudança real de conteúdo
    if changed:
        doc = re.sub(r'"dateModified": "\d{4}-\d{2}-\d{2}"', f'"dateModified": "{DATA}"', doc)
        doc = re.sub(r'Atualizado em <time datetime="\d{4}-\d{2}-\d{2}">[^<]+</time>',
                     f'Atualizado em <time datetime="{DATA}">{DATA_BR}</time>', doc)
        doc = doc.replace("com a situação de cada uma em agosto de 2026",
                          "reconferida em 20/09/2026")

    verify_ld(doc)
    return doc, changed


def main():
    check = "--check" in sys.argv
    src = open(PAGE, encoding="utf-8").read()
    out, changed = apply(src)
    if not changed:
        print("sem mudança")
        return
    if check:
        print("mudaria")
        return
    open(PAGE, "w", encoding="utf-8").write(out)
    print("aplicado")


if __name__ == "__main__":
    main()
