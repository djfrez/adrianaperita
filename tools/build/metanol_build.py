# -*- coding: utf-8 -*-
"""Aplica a SEO-067 em `/pericia-combustiveis/`.

Idempotente: tudo o que este script escreve vive entre marcadores `seo067:*` e é
removido antes de ser reaplicado. As funções de FAQ (visível e JSON-LD) são as
da SEO-066, importadas com parâmetros — não copiadas.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cpaq_build import strip_marks
from lote_build import apply_json_faq, apply_visible_faq
from metanol import FAQS, METODOS

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "pericia-combustiveis"

SEC_A, SEC_B = "<!-- seo067:sec:start -->", "<!-- seo067:sec:end -->"
FAQ_A, FAQ_B = "<!-- seo067:faq:start -->", "<!-- seo067:faq:end -->"

# Depois do marcador de solvente (a prova que o metanol NÃO deixa) e antes da
# tabela de ensaios de rotina (os que não o encontram).
ANCHOR = "    <h2>Ensaios e o que cada resultado sugere</h2>"

ROWS = "\n".join(
    f"          <tr>\n            <td>{a}</td>\n            <td>{b}</td>\n"
    f"            <td>{c}</td>\n          </tr>" for a, b, c in METODOS)

SECTION = f"""{SEC_A}
    <h2 id="metanol">Metanol: o adulterante que o teste da proveta não enxerga</h2>
    <p>
      O marcador denuncia o solvente. O metanol não traz marcador, e tem uma vantagem a mais
      para quem adultera: comporta-se, nos ensaios de rotina, como o etanol que a gasolina já
      contém. A ANP regula o próprio metanol (<strong>Resolução ANP nº 697/2017</strong>) e diz
      por quê: pela toxicidade do produto e pelo seu potencial como adulterador do etanol
      combustível e da gasolina.
    </p>

    <h3>O limite de 0,5% não é autorização</h3>
    <p>
      As duas especificações trazem o mesmo número: teor de metanol de no máximo
      <strong>0,5% em volume</strong> na gasolina (<strong>Resolução ANP nº 807/2020</strong>) e
      no etanol combustível, anidro e hidratado (<strong>Resolução ANP nº 907/2022</strong>). Nas
      duas, a nota que acompanha o parâmetro diz o mesmo: <strong>proibida a adição</strong>. O
      limite existe para acomodar contaminação involuntária, não para permitir mistura. Um teor
      confirmado acima de 0,5% é fato que alguém na cadeia terá de explicar; um teor abaixo
      dele não prova que não houve adição, só que ela não ultrapassou a tolerância.
    </p>

    <h3>Por que os ensaios de rotina não o encontram</h3>
    <p>
      O <strong>teste da proveta</strong> (ABNT NBR 13992), que mede o teor de etanol anidro na
      gasolina, extrai o álcool com água e lê o volume da fase aquosa. O metanol é extraído pela
      água do mesmo modo que o etanol: o ensaio soma os dois e informa o total como etanol.
      Estudo apresentado no 1º Congresso Brasileiro de P&amp;D em Petróleo e Gás (UNIFACS, 2001)
      mostrou que gasolina em que parte do etanol foi trocada por metanol, mantido o teor
      alcoólico total, passa despercebida pelo teste da proveta feito nos postos. A massa
      específica do metanol é muito próxima à do etanol, de modo que a densidade também não
      denuncia a troca. Na gasolina, a própria resolução trata o metanol como parâmetro a medir
      <strong>quando houver dúvida quanto à ocorrência de contaminação</strong> — não é ensaio de
      rotina.
    </p>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th scope="col">Método</th>
            <th scope="col">O que faz</th>
            <th scope="col">O que o resultado sustenta</th>
          </tr>
        </thead>
        <tbody>
{ROWS}
        </tbody>
      </table>
    </div>

    <h3>O que o certificado de origem realmente atesta</h3>
    <p>
      Na disputa sobre em que elo o metanol entrou, os documentos de origem pesam — e dizem
      menos do que parecem. Na gasolina, o boletim de conformidade do distribuidor precisa trazer,
      quanto ao metanol, a <strong>indicação de que o teor de metanol no etanol anidro está abaixo
      ou igual a 0,5%</strong> (art. 9º, § 1º, I, da Resolução nº 807/2020): uma indicação sobre o
      etanol recebido, não uma medição da gasolina entregue. No etanol, o fornecedor pode não
      fazer a análise: deixa em branco o campo de resultado do certificado e declara que o teor
      está abaixo do limite, <strong>assumindo toda e qualquer responsabilidade pelo não
      atendimento à especificação</strong> (nota 20 da Resolução nº 907/2022). Um certificado assim
      não é prova de conformidade; é a assinatura de quem responde se ela faltar.
    </p>

    <div class="box">
      <div class="box-lbl">Três perguntas para qualquer laudo que afirme metanol</div>
      <p>
        <strong>1. Qual método produziu o número?</strong> Triagem colorimétrica sem confirmação
        pela ABNT NBR 16041 é indício, não resultado.
        <strong>2. O resultado está dentro do escopo do método?</strong> A ABNT NBR 16943 só vale
        até 1,50% em volume de metanol; acima disso, o número precisa vir da cromatografia.
        <strong>3. O certificado de origem trazia medição ou declaração?</strong> Campo de resultado
        em branco desloca a pergunta de responsabilidade para quem declarou. Se o laboratório
        tinha o ensaio no <a href="/laudo-pericial/#laboratorio">escopo da acreditação</a> é a
        quarta pergunta, e as quatro cabem em <a href="/quesitos-periciais/">quesitos</a>.
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
