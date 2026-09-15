# -*- coding: utf-8 -*-
"""Aplica a SEO-056 em `/assistente-tecnica/`.

Idempotente: tudo o que este script escreve vive entre marcadores `seo056:*` e é
removido antes de ser reaplicado.

A maquinaria de JSON-LD é a da SEO-048/049, sem alteração de comportamento:

  1. A entrada nova do `FAQPage` entra em posição **penúltima** — a última é
     contratualmente a de intake da SEO-046.
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
from elegibilidade import ANSWER, EXIGENCIAS, QUESTION

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "assistente-tecnica"

SEC_A, SEC_B = "<!-- seo056:sec:start -->", "<!-- seo056:sec:end -->"
FAQ_A, FAQ_B = "<!-- seo056:faq:start -->", "<!-- seo056:faq:end -->"
INTAKE_A = "<!-- faqintake:start -->"

# A seção entra depois do vocabulário dos papéis (SEO-049) e antes do calendário:
# o leitor acabou de aprender como cada papel se chama; a pergunta seguinte é
# quem pode ocupar o dele.
ANCHOR = "    <h2>O calendário da prova pericial e onde o assistente entra</h2>"


def _rows4(rows):
    out = []
    for exig, perito, assistente, onde in rows:
        out.append(f"          <tr>\n"
                   f"            <td><strong>{exig}</strong></td>\n"
                   f"            <td>{perito}</td>\n"
                   f"            <td>{assistente}</td>\n"
                   f"            <td>{onde}</td>\n"
                   f"          </tr>")
    return "\n".join(out)


SECTION = f"""{SEC_A}
    <h2 id="quem-pode">Quem pode ser assistente técnico: o que o Código exige — e o que não exige</h2>

    <p>
      <strong>O CPC não impõe nenhum requisito de qualificação ao assistente técnico.</strong>
      Isso costuma surpreender, porque o Código é minucioso do outro lado: exige que o
      <em>perito do juízo</em> seja nomeado entre profissionais legalmente habilitados e órgãos
      inscritos em cadastro mantido pelo tribunal (art. 156, §1º) e que apresente, em 5 dias da
      ciência da nomeação, currículo com comprovação de especialização (art. 465, §2º, II).
      Sobre o assistente, a única regra de qualificação é uma regra de <em>desqualificação que não
      se aplica</em>: o art. 466, §1º, diz que ele é de confiança da parte e
      <strong>não está sujeito a impedimento ou suspeição</strong>.
    </p>

    <p>
      A consequência prática é direta e raramente dita: o assistente técnico
      <strong>pode ter vínculo com quem o indicou</strong> — pode ser o consultor de sempre da
      empresa, pode já ter trabalhado no caso antes do processo. Não é um defeito a esconder; é o
      regime que a lei escolheu, porque o assistente não decide nada. Ele instrui a parte, e o
      contraditório se faz com o parecer dele exposto ao perito e ao juízo.
    </p>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th scope="col">Exigência</th>
            <th scope="col">Perito do juízo</th>
            <th scope="col">Assistente técnico</th>
            <th scope="col">Onde</th>
          </tr>
        </thead>
        <tbody>
{_rows4(EXIGENCIAS)}
        </tbody>
      </table>
    </div>

    <div class="box">
      <div class="box-lbl">Onde a exigência realmente está</div>
      <p>
        O silêncio do CPC não é licença. O limite existe — só não está no processo, está na
        profissão: o parecer só tem peso se quem o assina tem <strong>atribuição legal para o ato
        técnico que pratica</strong>. Na área de Química, o
        <strong>Decreto nº 85.877/1981</strong> põe “vistoria, perícia, avaliação, arbitramento e
        serviços técnicos, elaboração de pareceres, laudos e atestados” entre as atividades da
        profissão (art. 1º, VI) e, nos termos do art. 2º, IV, “g”, arrola entre os
        <em>privativos</em> a “pesquisa, estudo, planejamento, perícia, consultoria e apresentação
        de pareceres técnicos na área de Química”; o art. 3º reserva o estudo, o planejamento e o
        projeto de equipamentos e instalações industriais a quem tem currículo de Engenharia
        Química. Um parecer assinado fora da atribuição é contestável na raiz — antes mesmo de se
        discutir o método. Sobre qual norma técnica governa cada exame, ver
        <a href="/normas-tecnicas-pericia/">o índice de normas aplicáveis à prova técnica</a>.
      </p>
    </div>

    <h3>Quando e por qual via a indicação é feita</h3>

    <p>
      Há três momentos, e eles não se equivalem. O ordinário é o
      <strong>prazo de 15 dias</strong> contados da intimação do despacho de nomeação do perito, no
      qual a parte argui impedimento ou suspeição do perito, indica assistente técnico e apresenta
      <a href="/quesitos-periciais/">quesitos</a> (art. 465, §1º). Na
      <strong>perícia consensual</strong>, em que as partes escolhem o perito de comum acordo, a
      indicação dos assistentes tem de ser feita <em>já no momento da escolha</em> (art. 471, §1º) —
      quem deixa para depois perde a via. E quando a perícia se realiza
      <strong>por carta</strong>, a nomeação do perito e a indicação dos assistentes podem ser
      feitas no juízo ao qual se requisita a perícia (art. 465, §6º). O calendário completo está
      <a href="/cpc-prova-pericial/">nos prazos da prova pericial no CPC</a>.
    </p>
    {SEC_B}
"""


# --------------------------------------------------------------------------
# aplicação — maquinaria herdada da SEO-048/049
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
