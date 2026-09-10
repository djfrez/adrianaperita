# -*- coding: utf-8 -*-
"""Aplica a SEO-050 em `/impugnacao-laudo-pericial/`.

Idempotente: tudo o que este script escreve vive entre marcadores `seo050:*` e é
removido antes de ser reaplicado.

Maquinaria de JSON-LD herdada sem alteração da SEO-048/049, com as duas
invariantes que já custaram caro:

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
from nulidade import (ANSWER, ART_282, ART_466_2, ART_474, ART_1009_1, EXIGENCIAS,
                      QUESTION, ROL_1015_INCISOS, ROL_1015_VETADO, TEMA_988,
                      TEMA_988_FONTE, VOCABULARIO)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "impugnacao-laudo-pericial"

SEC_A, SEC_B = "<!-- seo050:sec:start -->", "<!-- seo050:sec:end -->"
FAQ_A, FAQ_B = "<!-- seo050:faq:start -->", "<!-- seo050:faq:end -->"
INTAKE_A = "<!-- faqintake:start -->"

# A seção entra depois de "Se o prazo já passou" e antes das perguntas
# frequentes: é exatamente ali que o leitor que perdeu a via principal começa a
# procurar as palavras deste bloco — anular, recorrer, refazer.
ANCHOR = "    <h2>Perguntas frequentes</h2>"


def _rows4(rows):
    return "\n".join(
        f"          <tr>\n"
        f"            <td><strong>{a}</strong></td>\n"
        f"            <td>{b}</td>\n"
        f"            <td>{c}</td>\n"
        f"            <td>{d}</td>\n"
        f"          </tr>" for a, b, c, d in rows)


def _rows3(rows):
    return "\n".join(
        f"          <tr>\n"
        f"            <td><strong>{a}</strong></td>\n"
        f"            <td>{b}</td>\n"
        f"            <td>{c}</td>\n"
        f"          </tr>" for a, b, c in rows)


AUSENTE = "“nulidade do laudo”"
NUM_EXIG = {1: "uma", 2: "duas", 3: "três", 4: "quatro", 5: "cinco", 6: "seis"}[len(EXIGENCIAS)]

SECTION = f"""{SEC_A}
    <h2 id="nulidade">Anular, recorrer, refazer: o que cada palavra significa no Código</h2>

    <p>
      Quem recebe um laudo desfavorável quase nunca procura por “manifestação sobre o laudo”.
      Procura por <em>anular</em>, <em>recorrer</em>, <em>refazer</em> — os verbos do que quer que
      aconteça. O problema é que <strong>o CPC/2015 não usa nenhum deles a respeito do laudo</strong>:
      a expressão {AUSENTE} não aparece uma única vez no Código, e “laudo nulo”, tampouco.
      O que existe tem outro nome, outro prazo e outro efeito — e escolher o nome errado costuma
      custar a via certa.
    </p>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th scope="col">Como se digita</th>
            <th scope="col">O que o Código oferece</th>
            <th scope="col">O que se obtém na prática</th>
            <th scope="col">Onde</th>
          </tr>
        </thead>
        <tbody>
{_rows4(VOCABULARIO)}
        </tbody>
      </table>
    </div>

    <h3>Nulidade é do ato, não do documento</h3>

    <p>
      O Título III do CPC — <em>Das Nulidades</em>, arts. 276 a 283 — trata de <strong>atos
      processuais</strong>, não do conteúdo técnico de um documento. O art. 282 diz o que o juiz
      faz ao pronunciá-la: “{ART_282}” Repetir ou retificar o <em>ato</em>. Um laudo com método
      errado não é um ato nulo: é uma prova que o juiz pode deixar de considerar, motivadamente,
      pelo art. 479. São coisas diferentes, e pedir a errada é o modo mais rápido de perder as duas.
    </p>

    <p>
      Quando a nulidade é mesmo o caminho, ela não vem sozinha: a lei exige {NUM_EXIG} condições
      simultâneas.
    </p>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th scope="col">O que precisa ficar demonstrado</th>
            <th scope="col">O que a lei diz</th>
            <th scope="col">Onde</th>
          </tr>
        </thead>
        <tbody>
{_rows3(EXIGENCIAS)}
        </tbody>
      </table>
    </div>

    <div class="box">
      <div class="box-lbl">O vício de forma que a perícia oferece com mais frequência</div>
      <p>
        É o do <strong>art. 466, §2º</strong>: “{ART_466_2}” Some-se o <strong>art. 474</strong>:
        “{ART_474}” Diligência realizada sem essa comunicação comprovada nos autos é forma prescrita
        em lei descumprida — e é a hipótese em que a nulidade tem chance real. Ainda assim continuam
        valendo o prejuízo do art. 282, §1º e a alegação na primeira oportunidade do art. 278: quem
        recebe o laudo, deixa passar os 15 dias e só depois alega que o assistente não foi
        comunicado, alegou tarde. É mais uma razão para
        <a href="/assistente-tecnica/">indicar o assistente técnico no prazo do art. 465, §1º</a> —
        sem assistente indicado, não há a quem comunicar, e o vício sequer chega a existir.
      </p>
    </div>

    <h3>Recorrer do quê: o laudo não é decisão</h3>

    <p>
      Não há recurso contra prova. O que se recorre é da <strong>decisão</strong> que indefere os
      esclarecimentos ou a nova perícia — e essa decisão é interlocutória. O rol do
      <strong>art. 1.015</strong>, que lista as interlocutórias atacáveis por agravo de instrumento,
      tem <strong>{ROL_1015_INCISOS} incisos</strong> (o {ROL_1015_VETADO} vetado) e
      <strong>nenhum deles menciona perícia, laudo ou prova pericial</strong>; a única vez em que a
      palavra “prova” aparece ali é no inciso XI, sobre redistribuição do <em>ônus</em> da prova.
    </p>

    <p>
      A consequência está no <strong>art. 1.009, §1º</strong>: “{ART_1009_1}” Traduzindo: o
      indeferimento não precisa ser atacado na hora e <strong>não preclui</strong> — mas precisa ser
      retomado na apelação, sob pena de o tribunal considerar a questão não devolvida. A exceção é
      a urgência, pela tese de <strong>taxatividade mitigada</strong> fixada em recurso repetitivo:
      “{TEMA_988}” ({TEMA_988_FONTE}, Tema 988).
    </p>

    <div class="box">
      <div class="box-lbl">A ordem prática, em uma linha</div>
      <p>
        Crítica técnica <strong>dentro</strong> dos 15 dias do art. 477, §1º, com parecer do
        assistente; esclarecimentos para o que ficou obscuro; nova perícia como pedido subsidiário;
        nulidade apenas se houver vício de <em>forma</em> com prejuízo demonstrável; e a questão
        renovada em preliminar de apelação se o pedido for indeferido. Nessa ordem — porque cada
        etapa depende do que ficou registrado na anterior. Sobre as datas que abrem e fecham essas
        janelas, ver <a href="/cpc-prova-pericial/">os prazos da prova pericial no CPC</a>; sobre a
        redação das perguntas ao perito, <a href="/quesitos-periciais/">como formular quesitos</a>.
      </p>
    </div>
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
