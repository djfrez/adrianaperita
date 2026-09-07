# -*- coding: utf-8 -*-
"""Aplica a SEO-048 em `/quesitos-periciais/` e `/laudo-pericial/`.

Idempotente: tudo o que este script escreve vive entre marcadores `seo048:*` e
é removido antes de ser reaplicado.

Duas invariantes que valem em cada gravação:

  1. A entrada nova do `FAQPage` entra em posição **penúltima**. A última é
     contratualmente a de intake da SEO-046 — a SEO-047 descobriu isso do jeito
     difícil, quando duas guardas se pegaram mutuamente.
  2. A inserção no JSON-LD **não** usa casamento de texto de indentação
     (regra 6 do handoff de 05/09). O array `mainEntity` é localizado por
     balanceamento de colchetes e os objetos de primeiro nível por
     balanceamento de chaves; a indentação real do arquivo é lida, não
     presumida. Antes de gravar, **todos** os blocos `ld+json` da página são
     reparseados, e o script aborta se algum ficar inválido.
"""
import html as _html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from andamento_tela import APOS_ESCLARECIMENTOS, CNJ_TOTAL, JANELAS, answer, question

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SEC_A, SEC_B = "<!-- seo048:sec:start -->", "<!-- seo048:sec:end -->"
FAQ_A, FAQ_B = "<!-- seo048:faq:start -->", "<!-- seo048:faq:end -->"
INTAKE_A = "<!-- faqintake:start -->"


# --------------------------------------------------------------------------
# blocos visíveis
# --------------------------------------------------------------------------

def _rows(rows, first_col_strong):
    out = []
    for a, b, c in rows:
        head = f"<strong>{a}</strong>" if first_col_strong else a
        out.append(f"          <tr>\n"
                   f"            <td>{head}</td>\n"
                   f"            <td>{b}</td>\n"
                   f"            <td>{c}</td>\n"
                   f"          </tr>")
    return "\n".join(out)


SEC_QUESITOS = f"""{SEC_A}
    <h2 id="sem-quesitos">“Emitir despacho — sem quesitos”: o que esse andamento está dizendo</h2>

    <p>
      É uma das expressões que mais trazem gente a esta página, digitada exatamente como aparece na
      tela do processo. Vale começar pelo que ela <em>não</em> é: <strong>não é movimento das
      Tabelas Processuais Unificadas do CNJ</strong>. A tabela nacional de movimentos tem
      {CNJ_TOTAL} itens e nenhum deles se chama “Emitir despacho” — nem “quesito”, nem
      “esclarecimento”. O que se lê ali é rótulo de <em>tarefa</em> da fila interna do tribunal,
      seguido de complemento livre digitado pela secretaria. Os movimentos nacionais que
      correspondem ao episódio são <em>Despacho › Mero expediente</em> (11009 › 11010) e
      <em>Decurso de Prazo</em> (1051).
    </p>

    <p>
      O que o complemento registra é simples e ruim: o prazo de 15 dias do art. 465, §1º, venceu sem
      que quesitos fossem apresentados. A pergunta que importa não é essa — é a seguinte.
    </p>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th>Janela</th>
            <th>O que ela permite</th>
            <th>Base</th>
          </tr>
        </thead>
        <tbody>
{_rows(JANELAS, True)}
        </tbody>
      </table>
    </div>

    <p>
      Ou seja: <strong>o decurso de uma janela não fecha as outras.</strong> A crítica técnica ao
      laudo — que é onde a perícia costuma efetivamente virar — acontece na janela do art. 477, §1º,
      e ela existe para quem não apresentou quesitos no início. Uma ressalva honesta: o art. 477,
      §1º, pressupõe assistente técnico já indicado, e o CPC não diz se a indicação pode ser feita
      depois de vencido o prazo do art. 465, §1º. Este texto não afirma que pode.
    </p>

    <div class="box">
      <div class="box-lbl">O rótulo orienta; o inteiro teor decide</div>
      <p>
        Nenhuma tabela substitui abrir o documento intimado. Cada tribunal cria a sua tabela
        complementar, e o texto de tela quase sempre traz complemento livre. Para converter o
        movimento em data de vencimento com dia certo, veja
        <a href="/cpc-prova-pericial/#andamento">o quadro completo de andamento e prazos</a>.
      </p>
    </div>
    {SEC_B}
"""

SEC_LAUDO = f"""{SEC_A}
    <h2 id="esclarecimentos">“Apresentação de esclarecimentos ao laudo pericial”: o que corre depois</h2>

    <p>
      Quando o andamento registra <em>“anexo juntado: apresentação de esclarecimentos ao laudo
      pericial”</em>, o que houve foi o cumprimento de um dever do perito, e não a abertura de um
      prazo para a parte. Como no caso anterior, a expressão de tela não é movimento nacional:
      nenhum dos {CNJ_TOTAL} movimentos da tabela do CNJ se chama “esclarecimento”. O movimento
      padronizado é <em>Juntada</em> (67), nas suas duas espécies — <em>Petição</em> (85) e
      <em>Documento</em> (581); o resto é o título do próprio arquivo.
    </p>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th>Pergunta</th>
            <th>Resposta</th>
            <th>Base</th>
          </tr>
        </thead>
        <tbody>
{_rows(APOS_ESCLARECIMENTOS, False)}
        </tbody>
      </table>
    </div>

    <p>
      A consequência prática é contraintuitiva e cara: <strong>quem fica esperando um “prazo para se
      manifestar sobre os esclarecimentos” aparecer no andamento espera por algo que o CPC não
      prevê.</strong> O movimento seguinte é da parte, é um requerimento, e ele já precisa chegar com
      as perguntas escritas — o §3º exige que sejam formuladas <em>desde logo</em>, sob forma de
      quesitos. Sobre a redação dessas perguntas, ver
      <a href="/quesitos-periciais/">como formular quesitos que o perito não pode deixar de
      responder</a>; sobre a conversão do movimento em data,
      <a href="/cpc-prova-pericial/#andamento">o quadro de andamento e prazos</a>.
    </p>
    {SEC_B}
"""

SECOES = {
    "quesitos-periciais": (SEC_QUESITOS, '    <h2>Os dois limites legais que anulam uma pergunta</h2>'),
    "laudo-pericial": (SEC_LAUDO, '    <h2 id="roteiro">Roteiro de conferência: 22 pontos, na ordem em que se lê o laudo</h2>'),
}


# --------------------------------------------------------------------------
# aplicação
# --------------------------------------------------------------------------

def strip_marks(doc, a, b, eat_indent=False):
    """Remove o bloco E a indentação que o segue.

    Deixar a indentação para trás faz o marcador andar alguns espaços para a
    direita a cada execução — foi o que a checagem de idempotência acusou aqui,
    e é o mesmo bug de acúmulo que a SEO-047 registrou.
    """
    tail = r"\n[ \t]*" if eat_indent else r"\n"
    return re.sub(re.escape(a) + r".*?" + re.escape(b) + tail, "", doc, flags=re.S)


def apply_section(doc, slug):
    block, anchor = SECOES[slug]
    doc = strip_marks(doc, SEC_A, SEC_B)
    if anchor not in doc:
        raise SystemExit(f"{slug}: âncora de inserção não encontrada")
    return doc.replace(anchor, block + anchor, 1)


def apply_visible_faq(doc, slug):
    """Entrada visível imediatamente ANTES do bloco de intake — que fica por último."""
    doc = strip_marks(doc, FAQ_A, FAQ_B, eat_indent=True)
    i = doc.find(INTAKE_A)
    if i == -1:
        raise SystemExit(f"{slug}: bloco de intake da SEO-046 não encontrado")
    # Indentação real da linha do marcador de intake — não se presume 6 espaços:
    # nas duas páginas desta execução ela é de 4.
    bol = doc.rfind("\n", 0, i) + 1
    ind = doc[bol:i]
    block = (f"{FAQ_A}\n"
             f"{ind}  <div>\n"
             f"{ind}    <h3>{question(slug)}</h3>\n"
             f"{ind}    <p>{answer(slug)}</p>\n"
             f"{ind}  </div>\n"
             f"{ind}{FAQ_B}\n{ind}")
    return doc[:i] + block + doc[i:]


def span_of_array(text, start):
    """(abre, fecha) do array que começa no primeiro `[` após `start`."""
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
    """(início, fim_exclusivo) de cada objeto de primeiro nível do array.

    Consciente de string e de escape: uma chave dentro de `"..."` não conta.
    Devolver o fim, e não só o início, é o que torna a remoção exata — a
    primeira versão deste script removia o objeto e deixava a vírgula, e a
    checagem de idempotência pegou o JSON quebrado na segunda execução.
    """
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


def apply_json_faq(doc, slug):
    i = doc.find('"@type": "FAQPage"')
    if i == -1:
        raise SystemExit(f"{slug}: FAQPage não encontrado")
    end_script = doc.find("</script>", i)
    block = doc[i:end_script]

    name = json.dumps(_html.unescape(question(slug)), ensure_ascii=False)
    text = json.dumps(_html.unescape(answer(slug)), ensure_ascii=False)

    open_at, close_at = span_of_array(block, block.index('"mainEntity"'))
    arr = block[open_at + 1:close_at]

    # Remover a entrada desta execução, se já existir (idempotência). Remove-se
    # o objeto E a vírgula que o liga ao vizinho — nunca só o objeto.
    for a, b in object_spans(arr):
        if f'"name": {name}' in arr[a:b]:
            head, tail = arr[:a], arr[b:]
            if tail.lstrip().startswith(","):
                tail = tail.lstrip()[1:]          # vírgula à direita: era um do meio
            else:
                head = head.rstrip().rstrip(",")  # sem vírgula à direita: era o último
            arr = head.rstrip() + "\n" + tail.lstrip("\n")
            break

    spans = object_spans(arr)
    if not spans:
        raise SystemExit(f"{slug}: mainEntity vazio")
    last = spans[-1][0]                    # a entrada de intake (contratualmente a última)
    indent = arr[arr.rfind("\n", 0, last) + 1:last]   # indentação real, lida do arquivo
    entry = (f"{indent}{{\n"
             f"{indent}  \"@type\": \"Question\",\n"
             f"{indent}  \"name\": {name},\n"
             f"{indent}  \"acceptedAnswer\": {{\n"
             f"{indent}    \"@type\": \"Answer\",\n"
             f"{indent}    \"text\": {text}\n"
             f"{indent}  }}\n"
             f"{indent}}},\n")
    arr = arr[:last - len(indent)] + entry + arr[last - len(indent):]

    new_block = block[:open_at + 1] + arr + block[close_at:]
    return doc[:i] + new_block + doc[end_script:]


def apply(slug):
    path = os.path.join(ROOT, slug, "index.html")
    doc = original = open(path, encoding="utf-8").read()
    doc = apply_json_faq(apply_visible_faq(apply_section(doc, slug), slug), slug)

    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S):
        try:
            json.loads(b)
        except Exception as e:
            raise SystemExit(f"{slug}: JSON-LD inválido após a inserção — {e}")

    if doc == original:
        return False
    open(path, "w", encoding="utf-8").write(doc)
    return True


if __name__ == "__main__":
    check = "--check" in sys.argv
    for slug in sorted(SECOES):
        changed = apply(slug)
        print(("escrito     " if changed else "sem mudança ") + slug)
