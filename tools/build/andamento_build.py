# -*- coding: utf-8 -*-
"""Aplica a seção SEO-044 em /cpc-prova-pericial/index.html. Idempotente."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from andamento import MOVIMENTOS, CONTAGEM, FAQ

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
PAGE = os.path.normpath(os.path.join(ROOT, "cpc-prova-pericial", "index.html"))
TODAY, TODAY_BR = "2026-09-03", "3 de setembro de 2026"

def rows_mov():
    return "\n".join(
        f"          <tr>\n"
        f"            <td>{m}</td>\n            <td>{o}</td>\n"
        f"            <td>{c}</td>\n            <td>{b}</td>\n          </tr>"
        for m, o, c, b in MOVIMENTOS)

def rows_cont():
    return "\n".join(
        f"          <tr>\n            <td>{n}</td>\n            <td>{r}</td>\n"
        f"            <td>{b}</td>\n          </tr>" for n, r, b in CONTAGEM)

SECTION = f"""    <h2 id="andamento">Do andamento ao prazo: como ler o que o sistema escreveu</h2>

    <p>
      A tabela acima diz que o prazo dos quesitos corre &ldquo;da intimação do despacho de nomeação do
      perito&rdquo;. O andamento do processo não escreve isso. Ele escreve <em>Conclusão</em>, depois
      <em>Despacho</em>, depois <em>Perícia — Determinada/Designada</em>, depois <em>Intimação —
      Eletrônica</em>. Entre a linha da lei e a linha da tela há uma tradução que ninguém publica, e é
      nela que o prazo se perde.
    </p>

    <div class="box">
      <div class="box-lbl">Por que os nomes são iguais em qualquer tribunal</div>
      <p>
        Os nomes dos movimentos processuais são <strong>nacionais e padronizados</strong>: vêm das
        Tabelas Processuais Unificadas do Conselho Nacional de Justiça, mantidas no Sistema de Gestão
        de Tabelas (SGT). Por isso as mesmas expressões aparecem no PJe, no e-SAJ, no eproc e no
        Projudi. Os códigos entre parênteses na tabela abaixo são os da tabela de movimentos do CNJ, e
        as descrições de <em>Conclusão</em>, <em>Decurso de Prazo</em> e <em>Expedição de documento</em>
        reproduzem o glossário oficial de cada movimento.
      </p>
      <p>
        Duas ressalvas honestas: cada tribunal pode criar tabela complementar de documentos, e o texto
        que aparece na tela costuma vir acompanhado de um complemento livre digitado pela secretaria.
        <strong>O rótulo orienta; o inteiro teor decide.</strong> Nenhuma tabela substitui abrir o
        documento intimado.
      </p>
    </div>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th scope="col">Movimento (nome e código do CNJ)</th>
            <th scope="col">O que acabou de acontecer</th>
            <th scope="col">O que passa a correr</th>
            <th scope="col">Base</th>
          </tr>
        </thead>
        <tbody>
{rows_mov()}
        </tbody>
      </table>
    </div>

    <h3>Da intimação eletrônica a uma data com dia certo</h3>

    <p>
      Saber que o prazo é de 15 dias não diz quando ele vence. A conversão tem sete passos, e cada um
      tem base legal própria — inclusive o passo que a maioria pula, que é o da intimação ficta.
    </p>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th scope="col">Passo</th>
            <th scope="col">Regra</th>
            <th scope="col">Base legal</th>
          </tr>
        </thead>
        <tbody>
{rows_cont()}
        </tbody>
      </table>
    </div>

    <p>
      Quando a intimação se dá pelo Diário da Justiça eletrônico em vez do portal, dois dispositivos
      substituem os passos 2 a 4: considera-se data de publicação o primeiro dia útil seguinte ao da
      disponibilização, e a contagem começa no primeiro dia útil seguinte ao da publicação
      (art. 224, §2º e §3º).
    </p>

    <h3>Os três enganos que esta conversão produz</h3>

    <ol>
      <li>
        <strong>Misturar dias corridos com dias úteis.</strong> A janela de consulta do art. 5º, §3º,
        da Lei nº 11.419/2006 é de <strong>10 dias corridos</strong>. O prazo processual que ela
        dispara é contado <strong>em dias úteis</strong>, pelo art. 219 do CPC. São duas contagens
        diferentes encadeadas, e tratá-las como uma só é o erro de cálculo mais comum da fase pericial.
      </li>
      <li>
        <strong>Contar prazo em dobro em autos eletrônicos.</strong> O art. 229 do CPC dá prazo em
        dobro aos litisconsortes com procuradores de escritórios distintos — mas o §2º do mesmo artigo
        afasta essa contagem nos processos em autos eletrônicos. Quem soma a dobra sobre os 15 dias do
        art. 465, §1º, num processo eletrônico está trabalhando com um prazo que não existe.
      </li>
      <li>
        <strong>Ler <em>Decurso de Prazo</em> como fim da participação técnica.</strong> O decurso de
        uma janela não fecha as outras. Perdidos os quesitos iniciais do art. 465, §1º, permanecem os
        quesitos suplementares do art. 469, apresentados durante a diligência, e — sobretudo — os
        <strong>15 dias comuns do art. 477, §1º</strong>, contados da intimação sobre o laudo, em que a
        parte se manifesta e o assistente técnico apresenta seu parecer. É nessa janela que a crítica
        técnica ao laudo é feita, e ela existe independentemente do que aconteceu no início.
      </li>
    </ol>

    <p>
      Cada uma dessas janelas pede um produto técnico diferente:
      <a href="/quesitos-periciais/">quesitos</a> na primeira,
      <a href="/assistente-tecnica/">acompanhamento de diligência</a> na do meio,
      <a href="/laudo-pericial/">leitura crítica do laudo</a> e
      <a href="/impugnacao-laudo-pericial/">parecer divergente</a> na última. Quem só descobre o
      assistente técnico ao ler <em>Juntada — laudo pericial</em> ainda tem 15 dias úteis — e é o
      prazo mais decisivo dos três.
    </p>

"""

def faq_visible():
    return "\n".join(
        f"      <div>\n        <h3>{q}</h3>\n        <p>{a}</p>\n      </div>"
        for q, a in FAQ)

def main():
    h = open(PAGE, encoding="utf-8").read()
    if 'id="andamento"' in h:
        print("já aplicado — nada a fazer"); return 0

    anchor = '    <h2 id="antes-da-acao">'
    assert h.count(anchor) == 1, "âncora de inserção não é única"
    h = h.replace(anchor, SECTION + anchor)

    # FAQ visível: antes do fechamento do div.faq
    end = h.index('</div>\n    </div>\n\n  </div>\n</main>')
    h = h[:end] + '</div>\n' + faq_visible().lstrip() + '\n    ' + h[end+len('</div>\n'):]

    # FAQ JSON-LD, da mesma fonte
    def patch(m):
        d = json.loads(m.group(1))
        if d.get("@type") == "FAQPage":
            d["mainEntity"] += [{"@type": "Question", "name": q,
                                 "acceptedAnswer": {"@type": "Answer", "text": a}}
                                for q, a in FAQ]
        elif d.get("@type") == "Article":
            d["dateModified"] = TODAY
        return '<script type="application/ld+json">' + json.dumps(
            d, ensure_ascii=False, indent=2) + '</script>'
    h = re.sub(r'<script type="application/ld\+json">(.*?)</script>', patch, h, flags=re.S)

    # data visível de atualização
    h = re.sub(r'Atualizado em <time datetime="[^"]+">[^<]+</time>',
               f'Atualizado em <time datetime="{TODAY}">{TODAY_BR}</time>', h)

    # estilo do código do movimento
    if '.cod{' not in h:
        h = h.replace('</style>', '.cod{color:#6b7280;font-weight:400;white-space:nowrap}\n</style>', 1)

    open(PAGE, "w", encoding="utf-8").write(h)
    print(f"ok — seção + {len(FAQ)} FAQ aplicadas")
    return 0

if __name__ == "__main__":
    sys.exit(main())
