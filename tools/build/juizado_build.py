# -*- coding: utf-8 -*-
"""Aplica a SEO-068 em `/dano-motor-combustivel/`.

Idempotente: tudo o que este script escreve vive entre marcadores `seo068:*` e é
removido antes de ser reaplicado. FAQ pelas funções da SEO-066, importadas.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cpaq_build import strip_marks
from lote_build import apply_json_faq, apply_visible_faq
from juizado import FAQS, QUADRO

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "dano-motor-combustivel"

SEC_A, SEC_B = "<!-- seo068:sec:start -->", "<!-- seo068:sec:end -->"
FAQ_A, FAQ_B = "<!-- seo068:faq:start -->", "<!-- seo068:faq:end -->"

# Depois de "quem responde" (o regime) e antes dos quesitos (que são da perícia
# formal — a seção explica quando não haverá perícia formal).
ANCHOR = '    <h2 id="quesitos">'

ROWS = "\n".join(
    f"          <tr>\n            <td>{a}</td>\n            <td>{b}</td>\n"
    f"            <td>{c}</td>\n          </tr>" for a, b, c in QUADRO)

SECTION = f"""{SEC_A}
    <h2 id="juizado">Juizado Especial ou vara cível: a prova técnica escolhe a porta</h2>
    <p>
      Pelo valor, boa parte das ações de consumidor contra posto por quebra de motor cabe no
      Juizado Especial Cível: a <strong>Lei nº 9.099/1995</strong> admite causas de até quarenta
      salários mínimos (art. 3º, I), sem custas em primeiro grau (art. 54) e, até vinte salários
      mínimos, sem advogado obrigatório (art. 9º). O valor, porém, não é o único requisito. O
      Juizado julga causas cíveis <em>de menor complexidade</em>, e o <strong>Enunciado 54 do
      FONAJE</strong> diz como se mede: pelo objeto da prova, e não pelo direito material. Uma
      ação de consumo simples no direito pode ser complexa na prova — e dano ao motor por
      combustível costuma ser exatamente isso, pelas <a href="#tres-perguntas">três perguntas</a> do início desta página.
    </p>

    <h3>No Juizado não há perícia formal — há técnico e parecer</h3>
    <p>
      O rito da Lei nº 9.099/1995 não prevê a perícia do CPC, com perito nomeado, quesitos e prazo
      para laudo. Prevê outra coisa, no <strong>art. 35</strong>: quando a prova do fato exigir, o
      juiz pode inquirir técnicos de sua confiança, <strong>permitida às partes a apresentação de
      parecer técnico</strong>; e pode, no curso da audiência, fazer ou mandar fazer inspeção em
      pessoas ou coisas, com relato informal do que se verificou. O <strong>Enunciado 12 do
      FONAJE</strong> confirma que a perícia informal é admissível nessa hipótese. E todas as
      provas são produzidas na audiência de instrução e julgamento (art. 33). Na prática: no
      Juizado, a análise da amostra e o exame das peças têm de chegar prontos, em
      <strong>parecer técnico</strong>, porque não haverá etapa posterior para produzi-los.
    </p>

    <h3>O risco da extinção</h3>
    <p>
      Quando o juiz conclui que a causa exige perícia que o rito não comporta, o processo é extinto
      sem julgamento de mérito pelo <strong>art. 51, II</strong> — inadmissível o procedimento da
      lei. É argumento previsível da defesa do posto ou da distribuidora. A extinção não impede nova
      ação na justiça comum, mas consome tempo, e tempo é o que a amostra-testemunha não tem. Quem
      opta pelo Juizado também renuncia ao crédito que exceder quarenta salários mínimos, salvo
      conciliação (art. 3º, § 3º) — conta que precisa ser feita antes, quando o reparo atinge bomba
      e bicos injetores.
    </p>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th scope="col">Dimensão</th>
            <th scope="col">Juizado Especial Cível</th>
            <th scope="col">Vara cível (CPC)</th>
          </tr>
        </thead>
        <tbody>
{ROWS}
        </tbody>
      </table>
    </div>

    <div class="box">
      <div class="box-lbl">Como decidir, na prática</div>
      <p>
        Se a amostra já foi analisada, as peças já foram examinadas e a conclusão cabe num parecer
        que o técnico do juiz consegue conferir, o Juizado é viável. Se a autoria ainda depende de
        comparar a amostra do veículo, a amostra-testemunha e o certificado da distribuidora sob
        contraditório, a causa tende a ser complexa pela prova — e a vara cível, precedida de
        <a href="/producao-antecipada-prova/">produção antecipada de prova</a>, protege melhor o
        caso. Nos dois caminhos o trabalho técnico é o mesmo; muda o papel de quem o assina: autora
        de parecer no Juizado, <a href="/assistente-tecnica/">assistente técnica</a> na perícia
        formal.
      </p>
    </div>
    {SEC_B}
"""


def apply_section(doc):
    doc = strip_marks(doc, SEC_A, SEC_B)
    if doc.count(ANCHOR) != 1:
        raise SystemExit(f"{SLUG}: {doc.count(ANCHOR)} âncoras de inserção — esperava 1")
    return doc.replace(ANCHOR, SECTION + ANCHOR, 1)


def apply():
    path = os.path.join(ROOT, SLUG, "index.html")
    doc = original = open(path, encoding="utf-8").read()
    doc = apply_section(doc)
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
