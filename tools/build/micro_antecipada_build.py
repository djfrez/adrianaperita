# -*- coding: utf-8 -*-
"""Aplica a SEO-071 em `/analise-microbiologica-alimentos/`.

Idempotente: tudo o que este script escreve vive entre marcadores `seo071:*` e é
removido antes de ser reaplicado. FAQ pelas funções da SEO-066.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cpaq_build import strip_marks
from lote_build import apply_json_faq, apply_visible_faq
from micro_antecipada import FAQS, QUADRO

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "analise-microbiologica-alimentos"

SEC_A, SEC_B = "<!-- seo071:sec:start -->", "<!-- seo071:sec:end -->"
FAQ_A, FAQ_B = "<!-- seo071:faq:start -->", "<!-- seo071:faq:end -->"
REL_A, REL_B = "<!-- seo071:rel:start -->", "<!-- seo071:rel:end -->"

# Depois de `#uma-so-chance` (rito administrativo da Lei 6.437) e antes dos
# seis erros — a seção nova é o caminho judicial quando ainda não há apreensão.
ANCHOR = '    <h2 id="erros">'

ROWS = "\n".join(
    f"          <tr>\n            <td>{a}</td>\n            <td>{b}</td>\n"
    f"            <td>{c}</td>\n          </tr>" for a, b, c in QUADRO)

SECTION = f"""{SEC_A}
    <h2 id="producao-antecipada">Quando o alimento ainda existe: produção antecipada da prova microbiológica</h2>
    <p>
      A seção anterior trata do caso em que a autoridade sanitária <em>já apreendeu</em> o produto e a
      análise fiscal vai ocorrer sob o art. 27 da Lei nº 6.437/1977 — aí o direito de acompanhar o
      ensaio com perito próprio é exercido uma única vez. Há o caso simétrico e anterior: o alimento
      ainda está no estoque, na câmara ou na amostra retida da empresa, <strong>ninguém apreendeu
      nada</strong>, e a ação principal ainda não foi ajuizada. Se o exame esperar o processo, o que
      restará para examinar será outra coisa — lote misturado, validade vencida, amostra cuja
      população microbiana já não é a do fato. É para esse caso que existe a
      <a href="/producao-antecipada-prova/">produção antecipada de prova pericial</a>.
    </p>

    <p>
      O <strong>art. 381 do CPC</strong> admite a medida em <strong>três hipóteses independentes</strong>,
      e só a primeira é de urgência. Em microbiologia de alimentos as três têm encaixe próprio:
    </p>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th scope="col">Inciso do art. 381</th>
            <th scope="col">O que a lei exige</th>
            <th scope="col">Situação microbiológica típica</th>
          </tr>
        </thead>
        <tbody>
{ROWS}
        </tbody>
      </table>
    </div>

    <p>
      Fundamentar o pedido só na urgência, quando o caso é de decidir se vale litigar (inciso III) ou
      de viabilizar acordo (inciso II), enfraquece um pedido que teria fundamento próprio. E o contrário
      também vale: se o lote está a dias do vencimento ou da próxima produção que o misturará, o
      inciso I é o encaixe correto — e a janela se mede em eventos, não em dias de calendário.
    </p>

    <h3>O que a petição precisa fixar — art. 382</h3>
    <p>
      O <strong>art. 382</strong> exige que a petição apresente as razões da antecipação e
      <strong>mencione com precisão os fatos sobre os quais a prova há de recair</strong>. Em
      microbiologia essa precisão é técnica, não retórica: a matriz e o lote; a categoria e a
      categoria específica do Anexo I da <strong>IN nº 161/2022</strong> (ou o padrão de
      <em>Listeria</em> do Anexo II); os micro-organismos e os limites m e M; o <strong>n</strong> do
      plano e se as unidades serão analisadas individualmente; o método entre os do art. 9º da
      <strong>RDC nº 724/2022</strong>. Recorte genérico (“análise microbiológica do produto”) é o
      caminho mais curto para indeferimento parcial do objeto — e o § 4º do art. 382 não abre recurso
      contra indeferimento parcial, só contra o total.
    </p>

    <div class="box">
      <div class="box-lbl">Duas vias que não se substituem</div>
      <p>
        Acompanhar a análise fiscal da autoridade (art. 27 da Lei nº 6.437/1977) e requerer produção
        antecipada no juízo (art. 381 do CPC) resolvem problemas diferentes. A primeira reage a uma
        apreensão já feita; a segunda preserva prova <em>antes</em> da ação, inclusive para decidir se
        a ação existe. Nos dois caminhos o trabalho técnico é ler o plano de amostragem — n, c, m e M —
        e o método. O que muda é quem pauta o calendário: a autoridade sanitária, ou o juiz da medida.
        O rito, a competência e a diferença entre ata notarial e perícia antecipada estão na página de
        <a href="/producao-antecipada-prova/">produção antecipada de prova pericial</a>.
      </p>
    </div>
    {SEC_B}
"""

# Acrescenta o link na lista "Como essa prova entra no processo", sem tocar nas
# páginas embargadas que a SEO-059 originalmente apontava.
REL_ITEM = (
    f'{REL_A}\n'
    f'      <li><span><a href="/producao-antecipada-prova/">Produção antecipada de prova: '
    f'quando o objeto do exame não espera</a></span></li>\n'
    f'{REL_B}\n'
)
REL_ANCHOR = '      <li><span><a href="/assistente-tecnica/">'


def apply_section(doc):
    doc = strip_marks(doc, SEC_A, SEC_B)
    if doc.count(ANCHOR) != 1:
        raise SystemExit(f"{SLUG}: {doc.count(ANCHOR)} âncoras de inserção — esperava 1")
    return doc.replace(ANCHOR, SECTION + ANCHOR, 1)


def apply_related(doc):
    # Sem eat_indent: o marcador de fim come a indentação da linha seguinte
    # (assistente-técnica) e a 2ª execução deixa de achar o âncora.
    doc = strip_marks(doc, REL_A, REL_B)
    if doc.count(REL_ANCHOR) != 1:
        raise SystemExit(f"{SLUG}: {doc.count(REL_ANCHOR)} âncoras de related — esperava 1")
    return doc.replace(REL_ANCHOR, REL_ITEM + REL_ANCHOR, 1)


def apply():
    path = os.path.join(ROOT, SLUG, "index.html")
    doc = original = open(path, encoding="utf-8").read()
    doc = apply_section(doc)
    doc = apply_related(doc)
    doc = apply_visible_faq(doc, FAQS, FAQ_A, FAQ_B, SLUG)
    doc = apply_json_faq(doc, FAQS, SLUG)
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
