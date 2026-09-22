# -*- coding: utf-8 -*-
"""Aplica a SEO-062 em `/laudo-pericial/`.

Idempotente: tudo o que este script escreve vive entre marcadores `seo062:*` e é
removido antes de ser reaplicado.

Maquinaria de JSON-LD herdada sem alteração da SEO-048/049/050, com as duas
invariantes que já custaram caro:

  1. A entrada nova do `FAQPage` entra **antes** da última — a última é
     contratualmente a de intake da SEO-046. Aqui são duas entradas novas, e a
     ordem visível tem de bater com a do JSON-LD (foi o controle negativo 2 da
     SEO-061 que exigiu essa paridade).
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
from laboratorio import (COBERTURA, DECL_IDENTIFICA, DOQ, DOQ_REV, DOQ_URL,
                         FAQS, RBLE_URL, REGRA_DECISAO, REQ_713, REQ_7831,
                         REQ_7861)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "laudo-pericial"

SEC_A, SEC_B = "<!-- seo062:sec:start -->", "<!-- seo062:sec:end -->"
FAQ_A, FAQ_B = "<!-- seo062:faq:start -->", "<!-- seo062:faq:end -->"
INTAKE_A = "<!-- faqintake:start -->"

# A seção entra depois de "Três leituras que parecem defeito e não são" e antes
# das perguntas frequentes: o roteiro de conferência já mandou o leitor abrir o
# laudo do laboratório (itens 14 a 17), e é aqui que ele descobre o que fazer
# com o documento que tem na mão.
ANCHOR = "    <h2 id=\"faq\">Perguntas frequentes</h2>"


def _rows3(rows):
    return "\n".join(
        f"          <tr>\n"
        f"            <td><strong>{a}</strong></td>\n"
        f"            <td>{b}</td>\n"
        f"            <td>{c}</td>\n"
        f"          </tr>" for a, b, c in rows)


SECTION = f"""{SEC_A}
    <h2 id="laboratorio">O símbolo de acreditação no laudo do laboratório: o que ele cobre</h2>

    <p>
      Os itens 14 a 17 do roteiro mandam abrir o laudo do laboratório que instrui a perícia. O que
      quase sempre acontece a seguir é a leitura parar no símbolo de acreditação: ele está lá, o
      laboratório é acreditado, o resultado vale. <strong>O símbolo cobre menos do que parece</strong> —
      e o que ele deixa de fora é, com frequência, exatamente a frase em que o laudo pericial se apoiou.
    </p>

    <p>
      A norma de competência é a <strong>ABNT NBR ISO/IEC 17025:2017</strong>, e a acreditação no Brasil
      é concedida pela <strong>Coordenação Geral de Acreditação (Cgcre) do Inmetro</strong>. O texto da
      ABNT é pago, mas os requisitos estão explicados em documento oficial e gratuito — o
      <a href="{DOQ_URL}" rel="noopener">{DOQ} ({DOQ_REV})</a> —, e é dele que saem as citações abaixo.
      O <a href="{RBLE_URL}" rel="noopener">catálogo da RBLE</a>, também público e gratuito, lista o
      escopo de cada laboratório <strong>ensaio por ensaio</strong>, com matriz e método ao lado.
    </p>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th scope="col">O que está no relatório de ensaio</th>
            <th scope="col">Situação perante a acreditação</th>
            <th scope="col">O que decorre disso na perícia</th>
          </tr>
        </thead>
        <tbody>
{_rows3(COBERTURA)}
        </tbody>
      </table>
    </div>

    <h3>A regra de decisão: o que decide um resultado que ficou perto do limite</h3>

    <p>
      Quando o relatório diz “conforme”, “aprovado”, “dentro da especificação” — ou os contrários —,
      ele não está opinando: está emitindo uma <strong>declaração de conformidade</strong>, que a norma
      regula. O item <strong>7.8.6.1</strong> exige que “{REQ_7861}”, e o item <strong>7.8.6.2</strong>
      exige que a declaração identifique {DECL_IDENTIFICA}. Quando a declaração é pedida ao laboratório,
      o item <strong>7.1.3</strong> antecipa a exigência: já na contratação, “{REQ_713}”.
    </p>

    <div class="box">
      <div class="box-lbl">Por que isso muda o resultado, e não só a forma</div>
      <p>
        Regra de decisão é, na definição do item <strong>3.7</strong>, “{REGRA_DECISAO}”. Ela pode
        estabelecer que a incerteza <em>não</em> será considerada — e aí “conforme” significa apenas que
        o valor medido ficou do lado de dentro. Pode estabelecer que será, e aí o laboratório só declara
        conformidade quando o resultado <strong>e a sua faixa de incerteza</strong> ficam do lado de
        dentro. São critérios diferentes que produzem declarações opostas a partir do mesmo número.
        Um limite de 0,10 mg/kg, um resultado de 0,09 mg/kg e uma incerteza de 20% dão “conforme” pela
        primeira regra e “não conclusivo” pela segunda. <strong>Se a regra não está declarada, não se
        sabe qual das duas produziu a palavra que está no relatório</strong> — e é essa palavra que o
        laudo pericial costuma reproduzir como se fosse o resultado.
      </p>
    </div>

    <p>
      A incerteza, quando informada, vem “{REQ_7831}” (item 7.8.3.1). Isso importa na leitura: 20% e
      0,02 mg/kg podem ser a mesma coisa, e a comparação com o limite legal tem de ser feita na mesma
      unidade em que o limite está escrito. Sobre o que pedir quando o objeto é um resultado de
      laboratório, ver <a href="/analise-microbiologica-alimentos/">a leitura de um laudo de análise
      microbiológica</a> e, quando a discussão é o agente e não o número,
      <a href="/pericia-contaminacao-alimentos/">a investigação de contaminação</a>.
    </p>

    <div class="box">
      <div class="box-lbl">Três perguntas que cabem em um quesito complementar</div>
      <p>
        Nenhuma delas discute o ensaio — todas pedem o que a norma já obriga o laboratório a ter:
        <strong>(1)</strong> qual foi a regra de decisão empregada na declaração de conformidade, e se
        a incerteza de medição foi nela considerada; <strong>(2)</strong> se o ensaio relatado consta do
        escopo acreditado do laboratório na data do ensaio, com indicação da linha do escopo;
        <strong>(3)</strong> se houve ressalva quanto à condição da amostra no recebimento e quais
        resultados ela pode ter afetado. São perguntas de resposta objetiva, e a ausência de resposta
        é ela própria um achado. Sobre a forma de redigi-las,
        <a href="/quesitos-periciais/">como se formula um quesito</a>; sobre o que fazer com o defeito
        depois de encontrado, <a href="/impugnacao-laudo-pericial/">as três vias de impugnação</a>.
      </p>
    </div>
    {SEC_B}
"""


# --------------------------------------------------------------------------
# aplicação — maquinaria herdada da SEO-048/049/050
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

    # remove reaplicações anteriores, uma a uma
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
