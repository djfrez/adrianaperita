# -*- coding: utf-8 -*-
"""Aplica a SEO-051 em `/honorarios-pericia-judicial/`.

Idempotente: a seção e a FAQ nova vivem entre marcadores `seo051:*` e são
removidas antes de reaplicadas; a correção da resposta de reembolso é troca de
texto exato (antigo → novo), no visível, no JSON-LD e no `llms.txt`, e vira
no-op quando o texto novo já está lá.

Maquinaria de JSON-LD reutilizada da SEO-050 (`nulidade_build`): array por
balanceamento de colchetes, objetos por balanceamento de chaves consciente de
string/escape, indentação **lida do arquivo**, entrada nova em posição
**penúltima** (a última é contratualmente a de intake da SEO-046).
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from honorarios_final import (ANSWER, ART_465_4, ART_465_5, ART_84, ART_91_2, CALENDARIO,
                              CLT_790B_3, LLMS_NEW, LLMS_OLD, QUESTION, REEMBOLSO_NEW,
                              REEMBOLSO_OLD, SO_NO_FIM, TABELA_NEW, TABELA_OLD)
from nulidade_build import _plain, object_spans, span_of_array, strip_marks

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "honorarios-pericia-judicial"

SEC_A, SEC_B = "<!-- seo051:sec:start -->", "<!-- seo051:sec:end -->"
FAQ_A, FAQ_B = "<!-- seo051:faq:start -->", "<!-- seo051:faq:end -->"
INTAKE_A = "<!-- faqintake:start -->"

# Depois da gratuidade (que já fala da execução após o trânsito em julgado) e
# antes do custo do assistente: é a costura natural entre "de onde sai o
# dinheiro" e "quanto custa o seu lado".
ANCHOR = "    <h2>O que faz o custo de um assistente técnico variar</h2>"

N_MOMENTOS = {5: "cinco", 6: "seis", 7: "sete", 8: "oito"}[len(CALENDARIO)]


def _rows(rows):
    return "\n".join(
        f"          <tr>\n"
        f"            <td><strong>{a}</strong></td>\n"
        f"            <td>{b}</td>\n"
        f"            <td>{c}</td>\n"
        f"          </tr>" for a, b, c in rows)


def _table(cols, rows):
    th = "\n".join(f'            <th scope="col">{c}</th>' for c in cols)
    return f"""    <div class="table-scroll">
      <table>
        <thead>
          <tr>
{th}
          </tr>
        </thead>
        <tbody>
{_rows(rows)}
        </tbody>
      </table>
    </div>"""


SECTION = f"""{SEC_A}
    <h2 id="final-do-processo">“Ao final do processo”: quando o perito recebe e quem devolve o quê</h2>

    <p>
      “Pagamento de honorários periciais ao final do processo” é uma das dúvidas mais comuns sobre o
      tema — e a resposta curta é que, no processo civil, esse não é o regime normal. O Código manda
      <strong>adiantar</strong>. O que existe “ao final” são momentos diferentes, com regras
      diferentes, que a expressão mistura. São {N_MOMENTOS} os momentos em que o dinheiro da perícia
      se move:
    </p>

{_table(("Momento", "O que acontece com o dinheiro", "Onde"), CALENDARIO)}

    <p>
      O ponto que mais confunde está no <strong>art. 465, §4º</strong>: “{ART_465_4}” O
      “final” ali é o da <em>perícia</em> — laudo entregue e esclarecimentos prestados —, não o
      trânsito em julgado. E a retenção do saldo tem função: é ela que dá efeito ao §5º, “{ART_465_5}”
      Um parecer de assistente técnico que demonstre, com fundamento, que o laudo não respondeu aos
      quesitos é também o que sustenta esse pedido de redução. Sobre como montar essa crítica, ver
      <a href="/impugnacao-laudo-pericial/">como impugnar o laudo pericial</a>.
    </p>

    <h3>Onde o perito recebe, de fato, só no fim</h3>

{_table(("Situação", "Regra", "Onde"), SO_NO_FIM)}

    <p>
      No caso dos entes públicos, a lei fala expressamente em fim do processo. O art. 91, §2º:
      “{ART_91_2}” Na Justiça do Trabalho, o efeito é o mesmo por outro caminho: o art. 790-B,
      §3º, da CLT é taxativo: “{CLT_790B_3}” Sem adiantamento, o perito, na prática, recebe
      depois do julgamento.
    </p>

    <div class="box">
      <div class="box-lbl">Na Justiça do Trabalho, quem paga não é necessariamente quem perdeu a ação</div>
      <p>
        A CLT atribui o custo à parte sucumbente <strong>na pretensão objeto da perícia</strong>, não
        ao vencido no processo como um todo. Quem ganha a ação em outros pedidos e perde exatamente o
        pedido que dependia da perícia arca com os honorários do perito. Para o beneficiário da
        gratuidade, essa cobrança foi afastada pelo STF na ADI 5766, que declarou inconstitucionais a
        expressão “ainda que beneficiária da justiça gratuita”, do caput, e o §4º — o texto compilado
        do Planalto traz a anotação nos dois pontos. O teto de valor fica a cargo do Conselho Superior da Justiça do Trabalho (§1º), e o juiz
        pode parcelar (§2º).
      </p>
    </div>

    <p>
      Do lado de quem contratou <a href="/assistente-tecnica/">assistente técnico</a>, a regra do
      fim do processo é a do reembolso: o art. 84 diz que “{ART_84}” Somado ao art. 82, §2º, isso
      põe a remuneração do assistente no acerto da sentença — desde que o pagamento esteja
      comprovado e o pedido tenha sido feito. As datas que abrem e fecham cada uma dessas janelas
      estão em <a href="/cpc-prova-pericial/">prazos da prova pericial no CPC</a>.
    </p>
    {SEC_B}
"""


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
    return doc[:i] + block[:open_at + 1] + arr + block[close_at:] + doc[end_script:]


def swap(doc, old, new, n, what):
    """Troca exata e idempotente: `n` ocorrências do antigo, ou já todas novas."""
    if doc.count(old) == n:
        return doc.replace(old, new)
    if doc.count(old) == 0 and doc.count(new) == n:
        return doc
    raise SystemExit(f"{SLUG}: {what}: {doc.count(old)} antigas / {doc.count(new)} novas, esperava {n}")


def apply():
    path = os.path.join(ROOT, SLUG, "index.html")
    doc = original = open(path, encoding="utf-8").read()
    doc = apply_json_faq(apply_visible_faq(apply_section(doc)))
    # a resposta de reembolso aparece 2x (visível + JSON-LD); texto sem tag/entidade nas duas
    doc = swap(doc, REEMBOLSO_OLD, REEMBOLSO_NEW, 2, "resposta de reembolso")
    doc = swap(doc, TABELA_OLD, TABELA_NEW, 1, "célula de reembolso")

    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S):
        try:
            json.loads(b)
        except Exception as e:
            raise SystemExit(f"{SLUG}: JSON-LD inválido após a inserção — {e}")

    changed = doc != original
    if changed:
        open(path, "w", encoding="utf-8").write(doc)

    lp = os.path.join(ROOT, "llms.txt")
    llms = open(lp, encoding="utf-8").read()
    new_llms = swap(llms, LLMS_OLD, LLMS_NEW, 1, "llms.txt")
    if new_llms != llms:
        open(lp, "w", encoding="utf-8").write(new_llms)
        changed = True
    return changed


if __name__ == "__main__":
    print(("escrito     " if apply() else "sem mudança ") + SLUG)
