# -*- coding: utf-8 -*-
"""Aplica a SEO-066 em `/pericia-industria-quimica/`.

Idempotente: tudo o que este script escreve vive entre marcadores `seo066:*` e é
removido antes de ser reaplicado. A maquinaria de JSON-LD (balanceamento de
colchetes/chaves, entradas novas antes da de intake) é importada da SEO-065,
não copiada.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cpaq_build import _plain, object_spans, span_of_array, strip_marks
from lote import CONTRATO, FAQS, LEITURAS

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "pericia-industria-quimica"

SEC_A, SEC_B = "<!-- seo066:sec:start -->", "<!-- seo066:sec:end -->"
FAQ_A, FAQ_B = "<!-- seo066:faq:start -->", "<!-- seo066:faq:end -->"
INTAKE_A = "<!-- faqintake:start -->"

# Depois de "Os documentos que decidem o caso" (que acaba de apresentar o
# certificado de análise) e antes da FDS: a seção nova é a leitura do conflito
# entre dois desses documentos.
ANCHOR = "    <h2>FDS: o que mudou com a ABNT NBR 14725:2023</h2>"

ROWS_LEITURA = "\n".join(
    f"          <tr>\n            <td>{a}</td>\n            <td>{b}</td>\n"
    f"            <td>{c}</td>\n          </tr>" for a, b, c in LEITURAS)
ITENS_CONTRATO = "\n".join(
    f"      <li><strong>{a}</strong> — {b}.</li>" for a, b in CONTRATO)

SECTION = f"""{SEC_A}
    <h2 id="lote-recusado">Lote recusado: quando o certificado do fornecedor e o laboratório do cliente discordam</h2>
    <p>
      É a disputa mais comum entre empresas da cadeia química, e a que mais cedo toma o rumo
      errado. O fornecedor emite certificado de análise dizendo que o lote está conforme; o
      comprador analisa no recebimento, ou depois de o lote dar problema no processo, e encontra
      um parâmetro fora da especificação. Segue-se recusa, devolução, pedido de abatimento ou
      pedido de indenização pelo que se perdeu na linha — e as duas partes passam a discutir
      <strong>qual laboratório errou</strong>. Essa quase nunca é a primeira pergunta certa.
    </p>

    <h3>Repetibilidade e reprodutibilidade: a pergunta que vem antes de “quem errou”</h3>
    <p>
      Dois laboratórios competentes, medindo o mesmo lote pelo mesmo método, não chegam ao mesmo
      número. A série <strong>ISO 5725</strong> dá nome e tamanho a essa diferença. O
      <strong>limite de repetibilidade (r)</strong> é o quanto podem diferir dois resultados obtidos
      no mesmo laboratório, pelo mesmo operador, com o mesmo equipamento, em intervalo curto. O
      <strong>limite de reprodutibilidade (R)</strong> é o quanto podem diferir dois resultados
      obtidos em laboratórios diferentes. Ambos valem cerca de <strong>2,8 vezes o desvio-padrão
      correspondente</strong>: dois laboratórios trabalhando corretamente ultrapassam R em apenas
      cerca de 5% das comparações.
    </p>
    <p>
      A <strong>ISO 5725-6</strong>, que trata do uso prático desses valores, dá o teste para o
      caso típico da disputa comercial, em que cada laboratório tem um único resultado: compara-se
      a diferença absoluta entre os dois com R. <strong>Se ela não excede R, os resultados
      concordam</strong>, e a média pode ser tomada como resultado final. Os valores de r e R não
      são do laboratório: estão na <strong>seção de precisão do próprio método de ensaio</strong>
      (ABNT, ISO ou ASTM), e é lá que se leem.
    </p>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th scope="col">Situação</th>
            <th scope="col">O que significa</th>
            <th scope="col">Consequência para a disputa</th>
          </tr>
        </thead>
        <tbody>
{ROWS_LEITURA}
        </tbody>
      </table>
    </div>

    <p>
      A segunda linha é a que mais gera litígio e a que menos precisa de perícia sobre o lote:
      nenhum dos laboratórios errou, e o que falta é saber quem assume o risco do resultado perto
      do limite. É o problema da <strong>regra de decisão</strong>, tratado em
      <a href="/laudo-pericial/#laboratorio">o que o símbolo de acreditação do laboratório
      cobre</a>. A terceira é a que exige perícia de verdade — e a resposta costuma estar na
      amostra, não no ensaio.
    </p>

    <h3>Os quatro pontos do contrato que decidem antes do laboratório</h3>
    <ul>
{ITENS_CONTRATO}
    </ul>
    <p>
      Quando o contrato é omisso, a perícia tem de reconstruir cada um desses pontos a partir
      dos documentos — pedido, certificado, nota fiscal, registro de recebimento, laudo interno —,
      e o trabalho fica mais caro e mais incerto. Se a amostra retida ainda existe mas está perto
      do fim do prazo de guarda ou pode se degradar, a análise não precisa esperar a ação: cabe
      <a href="/producao-antecipada-prova/">produção antecipada da prova pericial</a>.
    </p>

    <h3>O relógio do Código Civil: trinta dias</h3>
    <p>
      Entre empresas, quando o produto químico entra como insumo no processo produtivo do
      comprador, a disputa costuma correr pelo <strong>Código Civil</strong>, e não pelo Código de
      Defesa do Consumidor. O lote com vício oculto que o torne impróprio ao uso ou lhe diminua o
      valor pode ser rejeitado (<strong>art. 441</strong>) ou mantido com
      <strong>abatimento no preço</strong> (<strong>art. 442</strong>); se o fornecedor conhecia o
      vício, responde também por perdas e danos (<strong>art. 443</strong>).
    </p>
    <p>
      O prazo é curto. Pelo <strong>art. 445</strong>, o comprador decai do direito em
      <strong>trinta dias da entrega efetiva</strong>, para bem móvel. Quando o vício, por sua
      natureza, só puder ser conhecido mais tarde, o prazo conta da ciência, até o máximo de
      <strong>cento e oitenta dias</strong> (<strong>§ 1º</strong>). Havendo cláusula de garantia,
      os prazos não correm durante ela, mas o defeito tem de ser denunciado ao fornecedor
      <strong>nos trinta dias seguintes ao seu descobrimento</strong>, sob pena de decadência
      (<strong>art. 446</strong>).
    </p>

    <div class="box">
      <div class="box-lbl">Onde a perícia entra no prazo</div>
      <p>
        A qualificação jurídica é do advogado; o que a perícia fornece são os dois fatos de que ela
        depende. O primeiro é <strong>a data</strong>: o laudo de recebimento, quando existe, fixa
        quando o comprador soube do desvio. O segundo é <strong>a detectabilidade</strong>: se o
        parâmetro fora de especificação é daqueles que o ensaio de recebimento usual mediria, é
        difícil sustentar que o vício só podia ser conhecido mais tarde; se só se manifesta no
        processo — uma impureza que o certificado não controla, uma degradação que aparece na
        reação —, a demonstração técnica disso é o que dá substância ao § 1º. Nos dois casos, os
        <a href="/quesitos-periciais/">quesitos</a> precisam perguntar pelas duas coisas.
      </p>
    </div>
    {SEC_B}
"""


def apply_section(doc):
    doc = strip_marks(doc, SEC_A, SEC_B)
    if doc.count(ANCHOR) != 1:
        raise SystemExit(f"{SLUG}: {doc.count(ANCHOR)} âncoras de inserção — esperava 1")
    return doc.replace(ANCHOR, SECTION + ANCHOR, 1)


def apply_visible_faq(doc):
    doc = strip_marks(doc, FAQ_A, FAQ_B, eat_indent=True)
    i = doc.find(INTAKE_A)
    if i == -1:
        raise SystemExit(f"{SLUG}: bloco de intake da SEO-046 não encontrado")
    bol = doc.rfind("\n", 0, i) + 1
    ind = doc[bol:i]
    inner = "".join(
        f"{ind}  <div>\n{ind}    <h3>{q}</h3>\n{ind}    <p>{a}</p>\n{ind}  </div>\n"
        for q, a in FAQS)
    return doc[:i] + f"{FAQ_A}\n{inner}{ind}{FAQ_B}\n{ind}" + doc[i:]


def apply_json_faq(doc):
    i = doc.find('"@type": "FAQPage"')
    if i == -1:
        raise SystemExit(f"{SLUG}: FAQPage não encontrado")
    end_script = doc.find("</script>", i)
    block = doc[i:end_script]
    open_at, close_at = span_of_array(block, block.index('"mainEntity"'))
    arr = block[open_at + 1:close_at]

    for q, _ in FAQS:  # remove reaplicações anteriores
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
    last = spans[-1][0]
    indent = arr[arr.rfind("\n", 0, last) + 1:last]
    entries = ""
    for q, a in FAQS:
        entries += (f"{indent}{{\n"
                    f"{indent}  \"@type\": \"Question\",\n"
                    f"{indent}  \"name\": {json.dumps(_plain(q), ensure_ascii=False)},\n"
                    f"{indent}  \"acceptedAnswer\": {{\n"
                    f"{indent}    \"@type\": \"Answer\",\n"
                    f"{indent}    \"text\": {json.dumps(_plain(a), ensure_ascii=False)}\n"
                    f"{indent}  }}\n"
                    f"{indent}}},\n")
    arr = arr[:last - len(indent)] + entries + arr[last - len(indent):]
    return doc[:i] + block[:open_at + 1] + arr + block[close_at:] + doc[end_script:]


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
