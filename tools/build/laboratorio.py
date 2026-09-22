# -*- coding: utf-8 -*-
"""SEO-062 — a regra de decisão: o que a acreditação do laboratório NÃO cobre.

Por que esta página (GSC, 28 dias findos em 21/09/2026):

    /laudo-pericial/ ......... 106 impressões · pos 8,7 · 0 cliques

É a **maior página livre de janela de medição**. Todas as maiores estão sob
janela: /assistente-tecnica/ (689 impr, SEO-056 até ~29/09) ·
/quesitos-periciais/ (584, SEO-048 ~28/09) · /honorarios-pericia-judicial/
(162, SEO-058 ~02/10) · /cpc-prova-pericial/ (115, SEO-057 ~30/09) ·
/normas-tecnicas-pericia/ (114, SEO-061 ~04/10) ·
/pericia-contaminacao-alimentos/ (53, SEO-060 ~03/10).

**Não é execução de snippet, e isso é deliberado.** SEO-057 (title+description)
e SEO-058 (só description) estão em medição exatamente para dizer qual é a
alavanca. Abrir uma terceira variante antes de 30/09–02/10 não replicaria nada:
produziria um terceiro ponto não controlado. E a tese do handoff (item 5) manda
o contrário para páginas médias — conteúdo de precisão, não snippet.

O buraco, medido sobre as 21 páginas antes de escrever uma linha — e a
medição corrigiu a hipótese de partida, que era muito mais larga do que o
buraco real:

    "17025" .................... 11 ocorrências, em 7 páginas   JÁ COBERTO
    "incerteza de medição" ..... 15, em 6 páginas                JÁ COBERTO
    "limite de quantificação" .. 32, em 12 páginas               JÁ COBERTO
    "Cgcre" .................... 4, em 3 páginas                 JÁ COBERTO
    "regra de decisão" ......... 0                               ← o buraco
    "RBLE" ..................... 0                               ← o buraco

O site já diz que o laboratório tem de ser acreditado, que a acreditação é por
ensaio e que método/incerteza/LQ precisam constar. O que ele **nunca** disse é
o que a acreditação deixa de fora, e como se confere:

  1. **Interpretação não é acreditada.** O símbolo cobre o resultado de
     medição; a frase que diz o que o resultado significa, não.
  2. **“Conforme” é declaração regulada, não opinião** — e exige regra de
     decisão documentada. Sem ela, não se sabe se a incerteza foi considerada.
  3. **A ressalva do item 7.4.3** é o laboratório registrando, por escrito, que
     a amostra chegou fora de especificação.
  4. **O escopo é consultável de graça**, ensaio por ensaio, na RBLE — o site
     mandava conferir sem dizer onde.

Fontes primárias abertas nesta execução (regra 8 do handoff — PDF baixado e
trecho extraído, não citado de memória):

  - **DOQ-Cgcre-087, Revisão 00 – MAR/2018** — "Orientações gerais sobre os
    requisitos da ABNT NBR ISO/IEC 17025:2017", Coordenação Geral de
    Acreditação do Inmetro. **Gratuito**, e é isso que importa: a norma ABNT é
    paga, e uma página que manda conferir precisa apontar para fonte que o
    leitor consiga abrir. Itens usados: 3.7, 7.1.3, 7.4.3, 7.8.3.1, 7.8.6.1,
    7.8.6.2 e 7.8.7.
  - **RBLE — Rede Brasileira de Laboratórios de Ensaio**, catálogo público dos
    escopos de acreditação: http://www.inmetro.gov.br/laboratorios/rble/
  - CPC/2015, art. 473, III e §1º — já na página; aqui apenas amarrados.

Regra 11 do backlog: visível e JSON-LD saem DAQUI, uma vez só.
"""

# --------------------------------------------------------------------------
# Citações literais do DOQ-Cgcre-087. O verificador rebaixa o PDF a cada
# execução e reconfere: trecho entre aspas na página é afirmação verificável.
# --------------------------------------------------------------------------

DOQ = "DOQ-Cgcre-087"
DOQ_REV = "Revisão 00 – MAR/2018"
DOQ_URL = ("https://www.gov.br/cdtn/pt-br/centrais-de-conteudo/"
           "documentos-cgcre-abnt-nbr-iso-iec-17025/doq-cgcre-087")
RBLE_URL = "http://www.inmetro.gov.br/laboratorios/rble/"

# 3.7 — definição de regra de decisão
REGRA_DECISAO = ("regra que descreve como a incerteza de medição é considerada "
                 "ao declarar a conformidade com um requisito especificado")

# 7.8.6.1 — o que o laboratório deve documentar
REQ_7861 = ("o laboratório deve documentar a regra de decisão empregada, "
            "considerando o nível de risco (como falsa aceitação e falsa rejeição "
            "e pressupostos estatísticos) associado à regra de decisão empregada, "
            "e aplicar a regra de decisão")

# 7.1.3 — quando se pede declaração de conformidade
REQ_713 = ("a especificação ou norma e a regra de decisão devem ser claramente "
           "definidas")

# 7.4.3 — a ressalva da amostra recebida fora de especificação
REQ_743 = ("o laboratório deve incluir uma ressalva no relatório, indicando "
           "quais resultados podem estar afetados pelo desvio")

# 7.8.7 — o limite da acreditação
REQ_787 = ("A Cgcre não faz acreditação para opiniões e interpretações, exceto "
           "para programas de acreditação específicos")

# 7.8.3.1 c) — como a incerteza deve ser apresentada
REQ_7831 = ("na mesma unidade do mensurando ou na forma de um termo relativo ao "
            "mensurando (por exemplo, percentual)")

# 7.8.6.2 — o que a declaração de conformidade deve identificar
DECL_IDENTIFICA = ("para quais resultados se aplica; o atendimento ou não às "
                   "especificações, normas ou suas partes; e a regra de decisão")

# Exemplo do DOQ para desvio de condição no recebimento (item 7.4.3)
EXEMPLO_743 = "temperatura elevada"

# --------------------------------------------------------------------------
# Tabela 1 — o que o símbolo de acreditação cobre, e o que não cobre
# (o que está no relatório, situação perante a acreditação, o que decorre)
# --------------------------------------------------------------------------

COBERTURA = [
    ("O resultado do ensaio que está no escopo",
     "<strong>Coberto.</strong> É o objeto da acreditação: aquele ensaio, naquela matriz, por aquele método.",
     "Sustenta o art. 473, III — método identificado e demonstradamente aceito na área."),

    ("O resultado de um ensaio fora do escopo",
     "<strong>Não coberto</strong>, ainda que o laboratório seja acreditado para outros ensaios. "
     "A acreditação é concedida ensaio a ensaio.",
     "O número pode estar certo, mas perdeu a demonstração externa de competência. Confere-se abrindo o "
     "escopo do laboratório na RBLE e procurando a linha do ensaio — não o nome do laboratório."),

    ("A amostragem, quando feita pelo próprio laboratório",
     "<strong>Coberta</strong> nessa hipótese: a norma trata a amostragem associada ao ensaio como atividade "
     "de laboratório, com requisitos próprios de registro.",
     "Quando quem colhe é o perito, a parte ou um terceiro, a acreditação começa no recebimento — e tudo o que "
     "aconteceu antes se prova pela cadeia de custódia, não pelo símbolo."),

    ("A ressalva sobre a condição em que a amostra chegou",
     "<strong>Prevista e obrigatória.</strong> Havendo desvio das condições especificadas — o exemplo do próprio "
     f"documento da Cgcre é {EXEMPLO_743} —, “{REQ_743}”.",
     "É o defeito de cadeia de custódia escrito pelo próprio laboratório. Costuma estar no rodapé, em corpo "
     "menor, e é o achado mais barato de toda a conferência."),

    ("A frase que diz o que o resultado significa para o caso",
     f"<strong>Não coberta.</strong> “{REQ_787}”.",
     "Quem assume a interpretação é o perito, pelo art. 473, III e §1º. Laudo que transfere a conclusão para o "
     "laboratório — “conforme atesta o laudo laboratorial” — não fundamentou: delegou."),

    ("A declaração de que a amostra está “conforme”",
     "<strong>Coberta, mas condicionada.</strong> Declarar conformidade não é opinião nem interpretação: é "
     "declaração regulada, e só é completa com a regra de decisão documentada.",
     "É o item mais rendoso da conferência, e o único que quase nunca é feito. Ver o quadro abaixo."),
]

# --------------------------------------------------------------------------
# FAQ — duas entradas. Visível e JSON-LD saem daqui.
# A de intake (SEO-046) é contratualmente a última.
# --------------------------------------------------------------------------

FAQS = [
    ("O laudo do laboratório tem o símbolo de acreditação. Isso valida a conclusão do laudo pericial?",
     "Não. A acreditação cobre o ensaio que está dentro do escopo acreditado daquele laboratório — o resultado "
     "de medição, com o método e a incerteza declarados — e, quando o próprio laboratório colhe a amostra, "
     "também a amostragem. Ela não cobre a interpretação: o "
     f"{DOQ} ({DOQ_REV}), da Coordenação Geral de Acreditação do Inmetro, registra que “{REQ_787}”. "
     "O número é acreditado; a frase que diz o que o número significa para o caso, não. Quem assume essa "
     "interpretação é o perito, pelo art. 473, III e §1º, do CPC — e o laudo que a transfere ao laboratório "
     "deixou de fundamentar."),

    ("O relatório diz que a amostra está “conforme”. Dá para conferir isso?",
     "Dá, e é a conferência mais produtiva e a menos feita. Declarar conformidade não é opinião: é declaração "
     "regulada. Pela ABNT NBR ISO/IEC 17025:2017, item 7.8.6.1, “"
     f"{REQ_7861}”, e o item 7.8.6.2 exige que a declaração identifique {DECL_IDENTIFICA}. Regra de decisão é, "
     f"na definição do item 3.7, “{REGRA_DECISAO}”. Na prática: um “conforme” sem regra de decisão declarada "
     "não diz se a incerteza foi considerada — e, quando o resultado está perto do limite, é a regra de decisão "
     "que decide o caso, não o ensaio."),
]
