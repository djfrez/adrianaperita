# -*- coding: utf-8 -*-
"""Aplica a SEO-049 em `/assistente-tecnica/`.

Idempotente: tudo o que este script escreve vive entre marcadores `seo049:*` e é
removido antes de ser reaplicado.

As duas invariantes da SEO-048 continuam valendo, e por isso a maquinaria de
JSON-LD abaixo é a dela, sem alteração de comportamento:

  1. A entrada nova do `FAQPage` entra em posição **penúltima** — a última é
     contratualmente a de intake da SEO-046.
  2. Nada é inserido no JSON-LD por casamento de indentação: o array
     `mainEntity` é achado por balanceamento de colchetes, os objetos por
     balanceamento de chaves consciente de string/escape, e a indentação é
     **lida do arquivo** (nesta página ela é de 6 espaços, não 4 — presumir o
     valor da SEO-048 estragaria o recuo).
"""
import html as _html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vocabulario import ANSWER, CIVIL_PENAL, CPC_AT_ARTIGOS, CPC_AT_OCORRENCIAS, QUESTION, VOCABULARIO

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "assistente-tecnica"

SEC_A, SEC_B = "<!-- seo049:sec:start -->", "<!-- seo049:sec:end -->"
FAQ_A, FAQ_B = "<!-- seo049:faq:start -->", "<!-- seo049:faq:end -->"
INTAKE_A = "<!-- faqintake:start -->"

# A seção entra depois da tabela perito × assistente e antes do calendário: o
# leitor acabou de aprender que os papéis diferem; agora aprende como se chamam.
ANCHOR = "    <h2>O calendário da prova pericial e onde o assistente entra</h2>"

ARTS = ", ".join(str(a) for a in CPC_AT_ARTIGOS[:-1]) + f" e {CPC_AT_ARTIGOS[-1]}"


def _rows4(rows):
    out = []
    for termo, na_lei, correto, onde in rows:
        out.append(f"          <tr>\n"
                   f"            <td><strong>{termo}</strong></td>\n"
                   f"            <td>{na_lei}</td>\n"
                   f"            <td>{correto}</td>\n"
                   f"            <td>{onde}</td>\n"
                   f"          </tr>")
    return "\n".join(out)


def _rows3(rows):
    out = []
    for dim, civil, penal in rows:
        out.append(f"          <tr>\n"
                   f"            <td><strong>{dim}</strong></td>\n"
                   f"            <td>{civil}</td>\n"
                   f"            <td>{penal}</td>\n"
                   f"          </tr>")
    return "\n".join(out)


SECTION = f"""{SEC_A}
    <h2 id="vocabulario">Perito assistente, perito judicial, perito oficial: o que o Código chama de quê</h2>

    <p>
      <strong>“Perito assistente” não é termo de lei processual: a expressão não aparece nenhuma vez
      no CPC/2015 nem no Código de Processo Penal.</strong> É hibridismo do uso corrente, que
      cola o <em>perito</em> do juízo ao <em>assistente</em> da parte e descreve, na prática, o
      profissional que o Código chama de <strong>assistente técnico</strong>. Vale a pena saber
      disso antes de redigir a petição: o termo legal é o que os sistemas dos tribunais indexam.
    </p>

    <p>
      A surpresa maior é do outro lado. <strong>“Perito judicial”, que é como quase todo mundo se
      refere ao perito do juízo, aparece uma única vez em todo o CPC</strong> — no art. 468, §2º, e
      apenas para dizer que o perito substituído que não devolve os valores recebidos fica impedido
      de atuar como perito judicial por cinco anos. Fora dessa punição, o Código diz apenas
      <em>perito</em>, ou <em>perito do juízo</em>. Já <em>assistente técnico</em> aparece
      {CPC_AT_OCORRENCIAS} vezes, distribuídas por {len(CPC_AT_ARTIGOS)} artigos: {ARTS}.
    </p>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th scope="col">Como se digita</th>
            <th scope="col">Está na lei?</th>
            <th scope="col">Termo do Código</th>
            <th scope="col">Onde</th>
          </tr>
        </thead>
        <tbody>
{_rows4(VOCABULARIO)}
        </tbody>
      </table>
    </div>

    <h3>A diferença que realmente muda a estratégia: cível não é criminal</h3>

    <p>
      O mesmo nome — assistente técnico — designa dois regimes bem diferentes. No processo civil ele
      entra por indicação da parte e <strong>acompanha</strong> a perícia. No processo penal ele
      depende de admissão pelo juiz e só atua <strong>depois</strong> de o laudo oficial estar
      pronto.
    </p>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th scope="col"></th>
            <th scope="col">Processo civil (CPC/2015)</th>
            <th scope="col">Processo penal (CPP)</th>
          </tr>
        </thead>
        <tbody>
{_rows3(CIVIL_PENAL)}
        </tbody>
      </table>
    </div>

    <div class="box">
      <div class="box-lbl">Por que essa distinção custa caro quando se erra</div>
      <p>
        No cível, o valor do assistente técnico está em grande parte na fase que o art. 466, §2º
        garante: estar presente na coleta da amostra, na medição, na vistoria — porque é ali que os
        vícios de método nascem, e depois eles já estão dentro do laudo. No penal essa fase é
        fechada: o art. 159, §4º, só admite o assistente <em>após</em> a elaboração do laudo pelos
        peritos oficiais, e a crítica passa a ser documental. Quem transpõe uma regra para a outra
        perde a fase mais valiosa da prova — no cível, por achar que precisa esperar um deferimento
        que o CPC não exige; no penal, por contar com um acompanhamento que o CPP não permite.
        Sobre a janela civil e as datas, ver
        <a href="/cpc-prova-pericial/">os prazos da prova pericial no CPC</a>; sobre a redação das
        perguntas, <a href="/quesitos-periciais/">como formular quesitos</a>.
      </p>
    </div>
    {SEC_B}
"""


# --------------------------------------------------------------------------
# aplicação — maquinaria herdada da SEO-048
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
    block = (f"{FAQ_A}\n"
             f"{ind}  <div>\n"
             f"{ind}    <h3>{QUESTION}</h3>\n"
             f"{ind}    <p>{ANSWER}</p>\n"
             f"{ind}  </div>\n"
             f"{ind}{FAQ_B}\n{ind}")
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

    name = json.dumps(_plain(QUESTION), ensure_ascii=False)
    text = json.dumps(_plain(ANSWER), ensure_ascii=False)

    open_at, close_at = span_of_array(block, block.index('"mainEntity"'))
    arr = block[open_at + 1:close_at]

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
