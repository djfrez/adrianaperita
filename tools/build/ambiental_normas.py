# -*- coding: utf-8 -*-
"""SEO-047 — Lei nº 9.605/1998 e Decreto nº 6.514/2008 no quadro de vigência.

Fonte única das quatro inserções em `/normas-tecnicas-pericia/`: as duas linhas
do quadro, a entrada de "as que mudaram" e o par pergunta/resposta da FAQ, este
último escrito uma vez e emitido nas duas pontas (visível e JSON-LD). É a 11ª
aplicação do método da SEO-037 — o objetivo não é economizar digitação, é
tornar a divergência entre schema e texto visível impossível por construção.

Tudo conferido em fonte primária (Planalto, texto compilado) em 06/09/2026.
Uso: python3 tools/build/ambiental_normas.py [--check]
"""
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGE = os.path.join(ROOT, "normas-tecnicas-pericia", "index.html")

# ── Fonte ───────────────────────────────────────────────────────────────────

ROWS = [
    ("Ambiental",
     "Lei nº 9.605/1998, arts. 70 a 76",
     "Definição de infração administrativa ambiental, sanções aplicáveis e limites da multa",
     "Vigente. O art. 70 define a infração administrativa ambiental; o art. 71 fixa os prazos "
     "máximos do processo administrativo; o art. 72 lista as onze sanções; e o art. 75 fixa o "
     "piso de R$ 50,00 e o teto de R$ 50.000.000,00. O art. 73, sobre a destinação do "
     "arrecadado, está na redação da Lei nº 14.691/2023."),
    ("Ambiental",
     "Decreto nº 6.514/2008",
     "Tipificação das infrações administrativas ambientais, dosimetria da multa e processo "
     "administrativo federal",
     "Vigente, em texto compilado e muito alterado. Os critérios de dosimetria estão no art. 4º "
     "(redação do Decreto nº 6.686/2008) e no art. 11 (redação do Decreto nº 11.080/2022, que "
     "mudou o marco de contagem da reincidência). A alteração mais recente é o Decreto nº "
     "12.877/2026, restrita ao art. 29 — maus-tratos a animais. <strong>Regula apenas a esfera "
     "federal</strong>: autuação estadual ou municipal segue a norma do ente que a lavrou."),
]

ENTRY_ID = "dec-6514-art11"
ENTRY_TITLE = "Decreto nº 6.514/2008, art. 11 — a reincidência passou a contar da decisão definitiva"
ENTRY_PARAS = [
    "Na redação original, a multa era aplicada em dobro ou em triplo quando o mesmo infrator "
    "cometia nova infração dentro de cinco anos contados <strong>da lavratura do auto "
    "anterior</strong>, confirmado no julgamento. O Decreto nº 11.080/2022 trocou o marco "
    "inicial: os cinco anos passaram a correr <strong>da data em que a decisão administrativa "
    "condenatória anterior se tornou definitiva</strong>. O agravamento continua sendo multa em "
    "triplo no caso da mesma infração e em dobro no caso de infração distinta.",
    "<strong>Na prática pericial:</strong> o agravamento por reincidência costuma responder por "
    "parte expressiva do valor autuado, e depende de uma data que não é a do auto anterior. "
    "Conferi-la é trabalho documental, não opinião: se a decisão anterior ainda não era "
    "definitiva, ou se ficou definitiva há mais de cinco anos, falta pressuposto ao agravamento "
    "e o memorial de cálculo precisa ser refeito. O mesmo Decreto nº 11.080/2022 acrescentou ao "
    "art. 9º dois parágrafos que também entram na conta: vencido o prazo do art. 113, a multa "
    "fica sujeita a atualização monetária, e o valor da multa ambiental consolidada não pode "
    "exceder o teto de R$ 50.000.000,00. Como se lê a dosimetria e o enquadramento de um auto "
    "ambiental está em <a href=\"/auto-infracao-ambiental/\">defesa técnica contra auto de "
    "infração ambiental</a>.",
]

FAQ_Q = "Quando a multa de um auto de infração ambiental é aplicada em dobro ou em triplo?"
FAQ_A = (
    "Por reincidência, nos termos do art. 11 do Decreto nº 6.514/2008: em triplo quando o "
    "infrator comete a mesma infração, em dobro quando comete infração distinta. O que mais se "
    "erra é o marco de contagem. Na redação dada pelo Decreto nº 11.080/2022, os cinco anos "
    "contam da data em que a decisão administrativa que condenou o infrator por infração "
    "anterior se tornou definitiva — e não, como previa a redação original, da lavratura do auto "
    "anterior. A diferença entre as duas datas costuma ser de anos e se resolve por documento: "
    "se a decisão anterior não era definitiva, ou ficou definitiva há mais de cinco anos, falta "
    "pressuposto ao agravamento e o memorial de cálculo da multa precisa ser refeito."
)

NOTA = ("As duas linhas ambientais da Lei nº 9.605/1998 e do Decreto nº 6.514/2008 foram "
        "acrescentadas em 06/09/2026 e conferidas na fonte nessa data; as demais mantêm a "
        "conferência de 18/08/2026.")

# ── Emissão ─────────────────────────────────────────────────────────────────

M = {"rows": "amb047:rows", "entry": "amb047:entry", "faq": "amb047:faq", "nota": "amb047:nota"}


def marked(key, body, indent):
    return f"{indent}<!-- {M[key]}:start -->\n{body}\n{indent}<!-- {M[key]}:end -->"


def rows_html():
    out = []
    for materia, norma, rege, sit in ROWS:
        out.append("          <tr>\n"
                   f"            <td>{materia}</td>\n"
                   f"            <td>{norma}</td>\n"
                   f"            <td>{rege}</td>\n"
                   f"            <td>{sit}</td>\n"
                   "          </tr>")
    return "\n".join(out)


def entry_html():
    ps = "\n".join(f"      <p>{p}</p>" for p in ENTRY_PARAS)
    return ('    <div class="art-entry">\n'
            f'      <h3 id="{ENTRY_ID}">{ENTRY_TITLE}</h3>\n'
            f"{ps}\n"
            "    </div>")


def faq_html():
    return ("      <div>\n"
            f"        <h3>{FAQ_Q}</h3>\n"
            f"        <p>{FAQ_A}</p>\n"
            "      </div>")


def nota_html():
    return f'    <p>{NOTA}</p>'


def strip(doc, key):
    """Remove um bloco marcado, para que reaplicar seja idempotente."""
    return re.sub(rf"[ \t]*<!-- {M[key]}:start -->.*?<!-- {M[key]}:end -->\n",
                  "", doc, flags=re.S)


def insert_before(doc, needle, block, what):
    i = doc.find(needle)
    if i == -1:
        raise SystemExit(f"âncora não encontrada ({what}): {needle[:60]!r}")
    return doc[:i] + block + "\n" + doc[i:]


def json_ld_faq(doc):
    """Insere a entrada no FAQPage ANTES da entrada de intake (SEO-046 exige que
    a de intake continue sendo a última). Localiza o objeto por balanceamento de
    chaves, nunca por texto de indentação — regra 6 do handoff de 05/09."""
    blocks = list(re.finditer(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S))
    target = None
    for m in blocks:
        try:
            o = json.loads(m.group(1))
        except Exception:
            continue
        if o.get("@type") == "FAQPage":
            target = (m, o)
    if target is None:
        raise SystemExit("FAQPage não encontrado")
    m, obj = target
    entries = obj["mainEntity"]
    entries = [e for e in entries if e.get("name") != FAQ_Q]
    novo = {"@type": "Question", "name": FAQ_Q,
            "acceptedAnswer": {"@type": "Answer", "text": html.unescape(strip_tags(FAQ_A))}}
    entries.insert(len(entries) - 1, novo)   # penúltima: a de intake fica por último
    obj["mainEntity"] = entries
    novo_bloco = json.dumps(obj, ensure_ascii=False, indent=2)
    return doc[:m.start(1)] + "\n" + novo_bloco + "\n  " + doc[m.end(1):]


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def build():
    doc = open(PAGE, encoding="utf-8").read()
    for k in M:
        doc = strip(doc, k)

    # 1. linhas do quadro — depois da Lei nº 6.938/1981, fim do bloco Ambiental
    anchor = "            <td>ABNT NBR 14725:2023</td>"
    tr_open = doc.rfind("          <tr>", 0, doc.find(anchor))
    doc = doc[:tr_open] + marked("rows", rows_html(), "          ") + "\n" + doc[tr_open:]

    # 2. nota de data logo abaixo do parágrafo de abertura do quadro
    doc = insert_before(doc, '    <div class="table-scroll">',
                        marked("nota", nota_html(), "    "), "nota")

    # 3. entrada nova, depois do bloco da CONAMA 430
    fim_conama = doc.find("</div>", doc.find('id="conama-430"')) + len("</div>\n")
    doc = doc[:fim_conama] + "\n" + marked("entry", entry_html(), "    ") + "\n" + doc[fim_conama:]

    # 4. FAQ visível — antes do bloco de intake, que continua sendo o último
    doc = insert_before(doc, "    <!-- faqintake:start -->",
                        marked("faq", faq_html(), "      "), "faq visível")

    # 5. FAQ em JSON-LD, da mesma fonte
    doc = json_ld_faq(doc)

    # 6. contagem no título da seção
    doc = doc.replace("As oito que mudaram e ainda circulam na versão antiga",
                      "As nove que mudaram e ainda circulam na versão antiga")

    doc = re.sub(r"\n{3,}", "\n\n", doc)

    # Nenhum bloco ld+json pode ficar inválido — regra 6 do handoff de 05/09.
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S):
        json.loads(b)
    return doc


if __name__ == "__main__":
    novo = build()
    atual = open(PAGE, encoding="utf-8").read()
    if "--check" in sys.argv:
        print("sem mudança" if novo == atual else "DIFERE")
        sys.exit(0 if novo == atual else 1)
    open(PAGE, "w", encoding="utf-8").write(novo)
    print("sem mudança" if novo == atual else "gravado")
