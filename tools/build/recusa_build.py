# -*- coding: utf-8 -*-
"""Aplica a SEO-063 em `/impugnacao-laudo-pericial/`.

Idempotente: tudo o que este script escreve vive entre marcadores `seo063:*` e
é removido antes de ser reaplicado.

Maquinaria de JSON-LD herdada sem alteração da SEO-048/049/050/062, com as duas
invariantes que já custaram caro:

  1. As entradas novas do `FAQPage` entram **antes** da última — a última é
     contratualmente a de intake da SEO-046 —, e a ordem visível tem de bater
     com a do JSON-LD, par a par, pergunta E resposta (controle negativo 2 da
     SEO-062).
  2. Nada é inserido por casamento de indentação: o array `mainEntity` é achado
     por balanceamento de colchetes, os objetos por balanceamento de chaves
     consciente de string/escape, e a indentação é **lida do arquivo**.
"""
import html as _html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recusa import (CIT_145_2, CIT_148_1, CIT_148_2, CIT_148_CAPUT, CIT_149,
                    CIT_466_1, CIT_467, CIT_467_PU, FAQS, INSTRUMENTOS, MOTIVOS)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "impugnacao-laudo-pericial"

SEC_A, SEC_B = "<!-- seo063:sec:start -->", "<!-- seo063:sec:end -->"
FAQ_A, FAQ_B = "<!-- seo063:faq:start -->", "<!-- seo063:faq:end -->"
INTAKE_A = "<!-- faqintake:start -->"

# A seção entra depois do bloco da SEO-050 (nulidade, recurso, nova perícia) e
# antes das perguntas frequentes: a SEO-050 esgota o que se faz com o
# *documento* e com o *ato*; falta o que se faz com a *pessoa*.
ANCHOR = "    <h2>Perguntas frequentes</h2>"


def _rows(rows, strong_first=True):
    out = []
    for r in rows:
        cells = "".join(
            f"            <td>{'<strong>%s</strong>' % c if (i == 0 and strong_first) else c}</td>\n"
            for i, c in enumerate(r))
        out.append(f"          <tr>\n{cells}          </tr>")
    return "\n".join(out)


SECTION = f"""{SEC_A}
    <h2 id="recusa">Quando o problema é o perito, e não o laudo</h2>

    <p>
      A lista de erros acima abre com <em>atacar o perito, não o laudo</em> — e a advertência vale
      inteira <strong>dentro da manifestação do art. 477, §1º</strong>. Mas existe o caso em que o
      perito <em>é</em> o problema: o currículo anexo ao laudo revela que ele já assinou parecer
      para a outra parte sobre o mesmo objeto, ou que presta serviço à empresa que está no polo
      contrário. Aí a manifestação é o lugar errado. O instrumento é outro, a peça é outra, o
      procedimento é outro — e misturar os dois costuma perder os dois.
    </p>

    <h3>O prazo que venceu, e o que o reabre</h3>

    <p>
      O <strong>art. 465, §1º, I</strong> dá às partes 15 dias, contados da intimação do despacho
      de nomeação, para arguir o impedimento ou a suspeição do perito. Na data em que esse prazo
      corre, a parte em geral não sabe nada sobre o perito além do nome — o currículo com
      comprovação de especialização só chega depois, pelo §2º, II, e o vínculo problemático
      raramente está nele de forma ostensiva. Quando o fato aparece, meses depois, o prazo do
      art. 465 já venceu.
    </p>

    <p>
      O que governa a arguição a partir daí é o <strong>art. 148</strong>, que o site inteiro
      precisava dizer e não dizia. O caput: “{CIT_148_CAPUT}” O perito é auxiliar da justiça por
      força do <strong>art. 149</strong>, que o nomeia expressamente: “{CIT_149}…”. E o
      <strong>§1º</strong> fixa o marco, que não é uma data de calendário:
      “{CIT_148_1}”
    </p>

    <div class="box">
      <div class="box-lbl">Primeira oportunidade não é o mesmo que prazo em dias</div>
      <p>
        O art. 148, §1º não concede um número de dias: prende a arguição à <strong>primeira fala
        nos autos depois de conhecido o fato</strong>. Para o motivo que só aparece no laudo, essa
        primeira oportunidade é a fase de manifestação. A consequência prática é o oposto de um
        prazo generoso: como não há período fixo a consumir, qualquer espera precisa ser
        justificada, e a arguição tem de carregar <strong>quando e como o fato foi conhecido</strong>,
        não apenas o fato.
      </p>
    </div>

    <h3>Mas não dentro da manifestação</h3>

    <p>
      A arguição é <strong>petição própria</strong> — “fundamentada e devidamente instruída”, diz o
      §1º — e segue caminho separado. O <strong>§2º</strong>: “{CIT_148_2}” O
      <strong>art. 467</strong> fecha o circuito do lado do perito: “{CIT_467}”, e o parágrafo
      único: “{CIT_467_PU}”
    </p>

    <p>
      Por isso a advertência do início não se contradiz. Levar imparcialidade para dentro da
      manifestação sobre o laudo produz exatamente o efeito descrito no erro nº 1: desloca a
      crítica técnica para um terreno em que o juízo tende a defender quem nomeou, e ainda deixa a
      arguição sem a instrução que o §1º exige. <strong>Duas peças, no mesmo dia, em autos
      diferentes.</strong>
    </p>

    <h3>O motivo do juiz, lido para o perito</h3>

    <p>
      O art. 148, II não cria hipóteses próprias: manda aplicar ao perito os motivos escritos para
      o juiz nos arts. 144 (impedimento, objetivo) e 145 (suspeição, ligado à parcialidade). A
      tabela traz as hipóteses que de fato aparecem em perícia técnica — e diz onde o inciso é
      literal demais para ser esticado.
    </p>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th scope="col">A situação, como aparece na perícia</th>
            <th scope="col">Dispositivo</th>
            <th scope="col">Natureza</th>
            <th scope="col">O que isso exige de quem argui</th>
          </tr>
        </thead>
        <tbody>
{_rows(MOTIVOS)}
        </tbody>
      </table>
    </div>

    <div class="box">
      <div class="box-lbl">As duas coisas que tornam a alegação ilegítima</div>
      <p>
        O <strong>art. 145, §2º</strong>: “{CIT_145_2}” A segunda hipótese é a que mais derruba
        arguição em perícia: a parte que conhecia o vínculo, apresentou quesitos, acompanhou a
        diligência e só arguiu depois do laudo desfavorável praticou atos de aceitação. É a outra
        razão para a arguição dizer <strong>quando</strong> o fato foi conhecido — a data separa
        “descobri agora” de “esperei para ver o resultado”.
      </p>
    </div>

    <h3>Três instrumentos que não se substituem</h3>

    <p>
      Imparcialidade, falta de aptidão técnica e descumprimento de prazo são problemas diferentes,
      com bases, momentos e efeitos diferentes. O pedido errado não é apenas indeferido: consome a
      credibilidade do conjunto, como qualquer pedido fora de lugar.
    </p>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th scope="col">O que se constata</th>
            <th scope="col">Instrumento</th>
            <th scope="col">Base legal</th>
            <th scope="col">Quando</th>
            <th scope="col">O que se obtém</th>
          </tr>
        </thead>
        <tbody>
{_rows(INSTRUMENTOS)}
        </tbody>
      </table>
    </div>

    <div class="box">
      <div class="box-lbl">O que a arguição não faz</div>
      <p>
        Não conserta o defeito técnico do laudo e <strong>não suspende o prazo de 15 dias</strong> da
        manifestação: o incidente corre “em separado e sem suspensão do processo”. Mesmo acolhida,
        ela produz a nomeação de novo perito — não a demonstração de que o primeiro laudo errou.
        Quem aposta tudo na arguição e deixa vencer o prazo do art. 477, §1º perde a via principal e
        fica com um incidente. Sobre as datas que abrem e fecham cada janela, ver
        <a href="/cpc-prova-pericial/">os prazos da prova pericial no CPC</a>; sobre a conferência do
        documento antes de decidir qualquer coisa,
        <a href="/laudo-pericial/">o que o laudo deve conter e como conferir</a>.
      </p>
    </div>

    <h3>A assimetria que protege o assistente técnico</h3>

    <p>
      O instrumento não é recíproco, e isso está escrito. <strong>Art. 466, §1º</strong>:
      “{CIT_466_1}” A parte contrária não tem, contra o assistente técnico, o que a parte tem contra
      o perito do juízo: o que lhe resta é atacar o parecer pelo conteúdo — método, dado, norma.
      É a contrapartida de o parecer nascer declaradamente parcial, e é uma das razões pelas quais
      <a href="/assistente-tecnica/">indicar assistente técnico no prazo do art. 465, §1º</a> tem
      custo processual baixo: o profissional de confiança da parte não abre uma frente de recusa.
    </p>
    {SEC_B}
"""


# --------------------------------------------------------------------------
# aplicação — maquinaria herdada da SEO-048/049/050/062
# --------------------------------------------------------------------------

def strip_marks(doc, a, b, eat_indent=False):
    tail = r"\n[ \t]*" if eat_indent else r"\n"
    return re.sub(re.escape(a) + r".*?" + re.escape(b) + tail, "", doc, flags=re.S)


def apply_section(doc):
    doc = strip_marks(doc, SEC_A, SEC_B)
    if ANCHOR not in doc:
        raise SystemExit(f"{SLUG}: âncora de inserção não encontrada")
    return doc.replace(ANCHOR, SECTION + ANCHOR, 1)


def apply_visible_faq(doc):
    doc = strip_marks(doc, FAQ_A, FAQ_B, eat_indent=True)
    i = doc.find(INTAKE_A)
    if i == -1:
        raise SystemExit(f"{SLUG}: bloco de intake da SEO-046 não encontrado")
    bol = doc.rfind("\n", 0, i) + 1
    ind = doc[bol:i]
    inner = "".join(
        f"{ind}  <div>\n"
        f"{ind}    <h3>{q}</h3>\n"
        f"{ind}    <p>{a}</p>\n"
        f"{ind}  </div>\n" for q, a in FAQS)
    block = f"{FAQ_A}\n{inner}{ind}{FAQ_B}\n{ind}"
    return doc[:i] + block + doc[i:]


def span_of_array(text, start):
    open_at = text.index("[", start)
    depth = 0
    for i in range(open_at, len(text)):
        if text[i] == "[":
            depth += 1
        elif text[i] == "]":
            depth -= 1
            if depth == 0:
                return open_at, i
    raise SystemExit("array sem fechamento")


def object_spans(arr):
    spans, depth, start, in_str, esc = [], 0, None, False, False
    for i, ch in enumerate(arr):
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                spans.append((start, i + 1))
    return spans


def _plain(s):
    """Texto do JSON-LD: sem tags e sem entidade HTML — mesma fonte do visível."""
    return _html.unescape(re.sub(r"<[^>]+>", "", s))


def apply_json_faq(doc):
    i = doc.find('"@type": "FAQPage"')
    if i == -1:
        raise SystemExit(f"{SLUG}: FAQPage não encontrado")
    end_script = doc.find("</script>", i)
    block = doc[i:end_script]

    open_at, close_at = span_of_array(block, block.index('"mainEntity"'))
    arr = block[open_at + 1:close_at]

    for q, _ in FAQS:
        name = json.dumps(_plain(q), ensure_ascii=False)
        for a, b in object_spans(arr):
            if f'"name": {name}' in arr[a:b]:
                head, tail = arr[:a], arr[b:]
                if tail.lstrip().startswith(","):
                    tail = tail.lstrip()[1:]
                else:
                    head = head.rstrip().rstrip(",")
                arr = head.rstrip() + "\n" + tail.lstrip("\n")
                break

    spans = object_spans(arr)
    if not spans:
        raise SystemExit(f"{SLUG}: mainEntity vazio")
    last = spans[-1][0]
    indent = arr[arr.rfind("\n", 0, last) + 1:last]

    entries = ""
    for q, a in FAQS:
        name = json.dumps(_plain(q), ensure_ascii=False)
        text = json.dumps(_plain(a), ensure_ascii=False)
        entries += (f"{indent}{{\n"
                    f"{indent}  \"@type\": \"Question\",\n"
                    f"{indent}  \"name\": {name},\n"
                    f"{indent}  \"acceptedAnswer\": {{\n"
                    f"{indent}    \"@type\": \"Answer\",\n"
                    f"{indent}    \"text\": {text}\n"
                    f"{indent}  }}\n"
                    f"{indent}}},\n")
    arr = arr[:last - len(indent)] + entries + arr[last - len(indent):]

    new_block = block[:open_at + 1] + arr + block[close_at:]
    return doc[:i] + new_block + doc[end_script:]


def apply():
    path = os.path.join(ROOT, SLUG, "index.html")
    doc = original = open(path, encoding="utf-8").read()
    doc = apply_json_faq(apply_visible_faq(apply_section(doc)))

    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S):
        try:
            json.loads(b)
        except Exception as e:
            raise SystemExit(f"{SLUG}: JSON-LD inválido após a inserção — {e}")

    if doc == original:
        return False
    open(path, "w", encoding="utf-8").write(doc)
    return True


if __name__ == "__main__":
    print(("escrito     " if apply() else "sem mudança ") + SLUG)
