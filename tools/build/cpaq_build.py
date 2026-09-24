# -*- coding: utf-8 -*-
"""Aplica a SEO-065 em `/produtos-quimicos-controlados/`.

Idempotente: tudo o que este script escreve vive entre marcadores `seo065:*` e é
removido antes de ser reaplicado.

Maquinaria de JSON-LD herdada sem alteração da SEO-048/049/050/062, com as duas
invariantes que já custaram caro:

  1. As entradas novas do `FAQPage` entram **antes** da última — a última é
     contratualmente a de intake da SEO-046. São três entradas novas, e a ordem
     visível tem de bater com a do JSON-LD (paridade exigida pelo controle
     negativo 2 da SEO-061).
  2. Nada é inserido por casamento de indentação: o array `mainEntity` é achado
     por balanceamento de colchetes, os objetos por balanceamento de chaves
     consciente de string/escape, e a indentação é **lida do arquivo**.

Além da seção e das FAQs, este script corrige o H2 de abertura: a página dizia
"Dois regimes federais" e passa a dizer "Dois regimes federais de licenciamento",
porque a partir desta execução ela apresenta um terceiro controle — declaratório,
não licenciador. Deixar o título como estava criaria contradição interna na
própria página, que é o defeito que um leitor atento e um LLM pegam primeiro.
"""
import html as _html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cpaq import (AUTORIDADE, DECLARACOES, DISTINCAO, FAQS, MEMBROS,
                  PRAZOS_LITERAL, SECRETARIA, VIGENCIA_BR)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "produtos-quimicos-controlados"

SEC_A, SEC_B = "<!-- seo065:sec:start -->", "<!-- seo065:sec:end -->"
FAQ_A, FAQ_B = "<!-- seo065:faq:start -->", "<!-- seo065:faq:end -->"
INTAKE_A = "<!-- faqintake:start -->"

# A seção entra depois de "Enquadramento: quando a concentração decide" e antes
# das perguntas frequentes: o enquadramento acabou de estabelecer que identidade
# e concentração decidem o regime, e é exatamente esse o teste que a CPAQ aplica
# — agora sobre o que a instalação sintetiza, e não sobre uma lista nacional.
ANCHOR = "    <h2 id=\"faq\">Perguntas frequentes</h2>"

# Correção do H2 de abertura (ver docstring). Par (de, para), aplicado uma vez.
H2_FIX = ("<h2 id=\"dois-regimes\">Dois regimes federais, independentes entre si</h2>",
          "<h2 id=\"dois-regimes\">Dois regimes federais de licenciamento, "
          "independentes entre si</h2>")


def _rows3(rows):
    return "\n".join(
        f"          <tr>\n"
        f"            <td><strong>{a}</strong></td>\n"
        f"            <td>{b}</td>\n"
        f"            <td>{c}</td>\n"
        f"          </tr>" for a, b, c in rows)


SECTION = f"""{SEC_A}
    <h2 id="cpaq">O terceiro controle: a CPAQ, a declaração à OPAQ e a inspeção internacional</h2>

    <p>
      Os dois regimes anteriores são de licenciamento: ambos perguntam se o produto está em uma
      lista e se a empresa tem o papel correspondente. Existe um terceiro controle, de lógica
      diferente, que não licencia nada e que <strong>é disparado pelo que a instalação sintetiza,
      e não pelo que ela vende</strong>. É o da <strong>Convenção sobre a Proibição das Armas
      Químicas (CPAQ)</strong> — e é o que mais pega empresa de surpresa, porque uma planta pode
      dever declaração sem produzir um único item das listas da Polícia Federal ou do Exército.
    </p>

    <p>
      A Convenção foi assinada em Paris em 13 de janeiro de 1993, aprovada pelo
      <strong>Decreto Legislativo nº 9, de 1996</strong>, e promulgada pelo
      <strong>Decreto nº 2.977, de 1º de março de 1999</strong>; vigora para o Brasil desde
      <strong>{VIGENCIA_BR}</strong>. As obrigações internas e a autoridade competente estão no
      <strong>Decreto nº 2.074, de 14 de novembro de 1996</strong>, que criou a Comissão
      Interministerial (CIAD/CPAQ), e as sanções estão na
      <strong>Lei nº 11.254, de 27 de dezembro de 2005</strong>. Na Comissão, {AUTORIDADE}; a
      Secretaria-Executiva Permanente é exercida pela {SECRETARIA}, e os ministérios representados
      são {MEMBROS}.
    </p>

    <h3>O que declarar, quem declara e quando</h3>

    <p>
      O art. 4º do Decreto nº 2.074/1996 impõe o dever a quem exerce atividade de produção,
      comercialização ou pesquisa envolvendo os elementos abrangidos pela Convenção. São quatro
      obrigações distintas, e duas delas têm data fixa no calendário: {PRAZOS_LITERAL}.
    </p>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th scope="col">Obrigação</th>
            <th scope="col">Quem deve</th>
            <th scope="col">Prazo</th>
          </tr>
        </thead>
        <tbody>
{_rows3(DECLARACOES)}
        </tbody>
      </table>
    </div>

    <div class="box">
      <div class="box-lbl">A armadilha do DOC: a obrigação não depende de lista</div>
      <p>
        Além das substâncias das Listas 1, 2 e 3, a Convenção alcança as instalações que fabricam
        <strong>substâncias orgânicas definidas</strong> (DOC, na sigla em inglês) e, em condição
        própria, as que contêm <strong>fósforo, enxofre ou flúor</strong> (DOC/PSF) — porque a
        planta capaz de sintetizá-las é tecnicamente capaz de outra coisa. A consequência prática
        é que <strong>o teste de declarabilidade não se responde consultando uma relação de
        produtos</strong>: responde-se lendo a rota de síntese e a fórmula molecular do que sai do
        reator, e comparando a quantidade com o limiar aplicável. Os limiares estão no Anexo sobre
        Implementação e Verificação da Convenção e nos formulários vigentes da CGBS, e devem ser
        conferidos <strong>no formulário do ano-base</strong> — não de memória, nem por analogia
        com o ano anterior. É trabalho de engenharia química, e é anterior ao jurídico: o
        departamento legal não tem como saber se a molécula é uma DOC.
      </p>
    </div>

    <h3>O que distingue este controle dos dois anteriores</h3>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th scope="col">Dimensão</th>
            <th scope="col">Polícia Federal e Exército</th>
            <th scope="col">CPAQ</th>
          </tr>
        </thead>
        <tbody>
{_rows3(DISTINCAO)}
        </tbody>
      </table>
    </div>

    <h3>Inspeção: quem entra, o que mede e o que leva embora</h3>

    <p>
      O art. 5º do Decreto nº 2.074/1996 obriga a empresa, a pedido da Comissão, a permitir o
      acesso de <strong>inspetores da OPAQ</strong> às instalações sob sua responsabilidade, a
      facultar-lhes o uso da aparelhagem pertinente e <strong>a coleta e a retirada de amostras
      para análise no local ou fora dele</strong>, além de garantir a comunicação dos inspetores
      sem monitoramento. O mesmo artigo prevê <strong>visitas de verificação de dados</strong> por
      inspetores indicados pela própria Comissão, e sujeita a recusa de colaboração às sanções da
      lei. Não é fiscalização documental: é medição.
    </p>

    <p>
      Daí decorre a exposição técnica. O que a inspeção compara é a <strong>identidade e a
      concentração do que está no tanque</strong> com o que foi declarado no formulário do
      ano-base. É o mesmo problema de reconciliação da
      <a href="#autuacao-escritural">autuação escritural</a>, deslocado para outra base: em lugar
      do mapa de controle e da nota fiscal, a declaração internacional; em lugar da diferença de
      saldo, a diferença entre a substância declarada e a substância presente. E vale aqui o que a
      seção de <a href="#enquadramento">enquadramento</a> já estabeleceu: identidade e concentração
      são resultado de análise, e resultado de análise depende de amostragem, de método e de
      cadeia de custódia — não de rótulo de tambor.
    </p>

    <div class="box">
      <div class="box-lbl">Regra de decisão: a infração declaratória é a mesma nos três regimes</div>
      <p>
        O art. 12, III, da Lei nº 10.357/2001 pune a informação prestada com dados incompletos ou
        inexatos. O art. 3º, III, do Decreto nº 2.074/1996 e o art. 1º, III, da Lei nº 11.254/2005
        punem omitir informação ou prestar informação incorreta à Comissão Interministerial. Nos
        três casos, <strong>o que se pune é a divergência entre o declarado e o real — não a
        operação</strong>. Por isso a defesa é a mesma engenharia: balanço de massa do período,
        identidade e concentração da substância, e demonstração de que a diferença tem assinatura
        física de perda, de conversão de unidade ou de enquadramento, e não de desvio. A
        Lei nº 11.254/2005, no art. 3º, § 4º, assegura <strong>amplo direito de defesa em processo
        administrativo</strong> antes de qualquer penalidade: é nele que o parecer técnico entra.
        Sobre a forma de levar isso a juízo ou ao processo administrativo, ver
        <a href="/laudo-pericial/">o que um laudo técnico precisa conter</a> e, quando o laudo já
        existe e está errado, <a href="/impugnacao-laudo-pericial/">as vias de impugnação</a>.
      </p>
    </div>
    {SEC_B}
"""


# --------------------------------------------------------------------------
# aplicação — maquinaria herdada da SEO-048/049/050/062
# --------------------------------------------------------------------------

def strip_marks(doc, a, b, eat_indent=False):
    tail = r"\n[ \t]*" if eat_indent else r"\n"
    return re.sub(re.escape(a) + r".*?" + re.escape(b) + tail, "", doc, flags=re.S)


def apply_h2_fix(doc):
    """Idempotente pela ordem: se o destino já está no arquivo, não faz nada."""
    old, new = H2_FIX
    if new in doc:
        return doc
    if doc.count(old) != 1:
        raise SystemExit(f"{SLUG}: {doc.count(old)} ocorrências do H2 de abertura — esperava 1")
    return doc.replace(old, new, 1)


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
    doc = apply_json_faq(apply_visible_faq(apply_section(apply_h2_fix(doc))))

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
