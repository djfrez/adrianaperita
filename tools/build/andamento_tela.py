# -*- coding: utf-8 -*-
"""SEO-048 — a decodificação do andamento nas páginas que já rankeiam por ela.

Por que este arquivo existe (dado de GSC de 07/09/2026, 28 dias):

    emitir despacho - sem quesitos ............ /quesitos-periciais/  pos 8,9  11 impr
    anexo juntado: apresentação de
    esclarecimentos ao laudo pericial ......... /laudo-pericial/      pos 8,2   4 impr

As duas são consultas de andamento — exatamente a classe que a SEO-044 previu
e para a qual construiu o decodificador. Só que o decodificador está em
`/cpc-prova-pericial/`, e essa página tem **zero consultas nominais atribuídas**.
O Google escolheu para responder as páginas que apenas *linkam* para a resposta.
A correção não é mover o decodificador: é pôr a resposta autossuficiente na
página que o Google já escolheu, e de lá remeter ao quadro completo.

Fontes primárias abertas nesta execução:
  - CPC/2015, texto compilado do Planalto — arts. 465, §1º; 469; 470;
    477, caput e §§ 1º a 4º. Todas as ocorrências extraídas, última escolhida
    (regra 8 do handoff de 02/09).
  - Tabelas Processuais Unificadas do CNJ, tabela de movimentos (M), via
    webservice SOAP público `sgt_ws.php`, operação `pesquisarItemPublicoWS`:
    **964 movimentos**. Nenhum deles se chama "Emitir despacho", "quesito" ou
    "esclarecimento" — achado que sustenta a tese central dos dois blocos e que
    não sairia da memória. Hierarquia conferida item a item.

Regra 11 do backlog: visível e JSON-LD saem DAQUI, uma vez só.
"""

# Códigos conferidos no SGT nesta execução (pai › filho, como o SGT expõe):
#   Despacho 11009 › Mero expediente 11010
#   Decurso de Prazo 1051 (pai 48)      Juntada 67 › Petição 85 · Documento 581
CNJ_TOTAL = "964"

# --------------------------------------------------------------------------
# /quesitos-periciais/ — «Emitir despacho - sem quesitos»
# --------------------------------------------------------------------------

JANELAS = [
    ("Fechada",
     "Quesitos iniciais, indicação de assistente técnico e arguição de impedimento ou suspeição — os três atos vencem no mesmo prazo de 15 dias.",
     "Art. 465, §1º, I a III"),
    ("Aberta",
     "<strong>Quesitos suplementares</strong>, apresentados <em>durante a diligência</em>. Podem ser respondidos previamente ou na audiência de instrução e julgamento.",
     "Art. 469"),
    ("Aberta",
     "<strong>15 dias comuns</strong>, contados da intimação sobre o laudo, para a parte se manifestar — prazo em que o assistente técnico apresenta o seu parecer.",
     "Art. 477, §1º"),
    ("Aberta",
     "Requerer que o perito ou o assistente compareça à audiência, <em>formulando desde logo as perguntas sob forma de quesitos</em>.",
     "Art. 477, §3º e §4º"),
]

# --------------------------------------------------------------------------
# /laudo-pericial/ — «Apresentação de esclarecimentos ao laudo pericial»
# --------------------------------------------------------------------------

APOS_ESCLARECIMENTOS = [
    ("O que o perito acabou de cumprir",
     "O dever de esclarecer, em 15 dias, ponto sobre o qual exista divergência ou dúvida de qualquer das partes, do juiz ou do Ministério Público, ou ponto divergente apresentado no parecer do assistente técnico da parte.",
     "Art. 477, §2º, I e II"),
    ("Que prazo passa a correr para a parte",
     "<strong>Nenhum, automaticamente.</strong> O CPC não abre nova janela de manifestação depois da juntada dos esclarecimentos.",
     "Art. 477, §3º, a contrario"),
    ("Qual é, então, o movimento da parte",
     "<strong>Requerer</strong> ao juiz que mande intimar o perito ou o assistente técnico a comparecer à audiência — e o requerimento já tem de trazer as perguntas escritas, sob forma de quesitos.",
     "Art. 477, §3º"),
    ("Com que antecedência isso precisa acontecer",
     "O perito ou o assistente é intimado por meio eletrônico com pelo menos <strong>10 dias de antecedência</strong> da audiência, o que fixa na prática o limite para o requerimento.",
     "Art. 477, §4º"),
]

# --------------------------------------------------------------------------
# FAQ — uma entrada por página. Fonte única das duas pontas.
# --------------------------------------------------------------------------

FAQ = {
    "quesitos-periciais": (
        "O andamento diz “Emitir despacho — sem quesitos”. Ainda dá para atuar tecnicamente?",
        "Dá, em três janelas que não dependem da primeira. “Emitir despacho — sem quesitos” não é "
        "movimento das Tabelas Processuais Unificadas do CNJ: nenhum dos 964 movimentos da tabela "
        "se chama assim. É rótulo de tarefa interna do tribunal, com complemento livre digitado "
        "pela secretaria, e o que ele registra é que o prazo de 15 dias do art. 465, §1º, do CPC "
        "venceu sem quesitos. Permanecem abertos os quesitos suplementares durante a diligência "
        "(art. 469), os 15 dias comuns do art. 477, §1º, para manifestação sobre o laudo, e o "
        "requerimento do art. 477, §3º, para que o perito seja intimado a comparecer à audiência, "
        "com as perguntas já formuladas. O rótulo orienta; o inteiro teor do despacho decide."),
    "laudo-pericial": (
        "O perito juntou os esclarecimentos ao laudo. Abre novo prazo para a parte se manifestar?",
        "Não automaticamente. O art. 477, §2º, do CPC impõe ao perito o dever de esclarecer, em 15 "
        "dias, ponto divergente ou duvidoso apontado pelas partes, pelo juiz, pelo Ministério "
        "Público ou no parecer do assistente técnico — mas o CPC não abre, depois dessa juntada, "
        "nova janela de manifestação para a parte. O que o §3º prevê é um requerimento: persistindo "
        "a necessidade de esclarecimento, a parte pede ao juiz que mande intimar o perito ou o "
        "assistente técnico a comparecer à audiência, formulando desde logo as perguntas sob forma "
        "de quesitos. Como o §4º exige intimação eletrônica com pelo menos 10 dias de antecedência "
        "da audiência, quem espera aparecer no andamento um “prazo para se manifestar sobre os "
        "esclarecimentos” tende a chegar à audiência sem pergunta nenhuma protocolada."),
}


def question(slug):
    return FAQ[slug][0]


def answer(slug):
    return FAQ[slug][1]
