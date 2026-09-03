# -*- coding: utf-8 -*-
"""SEO-044 — seção "Do andamento ao prazo" em /cpc-prova-pericial/.

Regra 11 do backlog: FAQ visível e JSON-LD saem DA MESMA fonte de dados.
Nada aqui é escrito duas vezes.

Fontes primárias conferidas nesta execução (ver SEO_BACKLOG.md):
  - CPC/2015 (Lei 13.105/2015), texto compilado do Planalto.
  - Lei 11.419/2006, art. 5º.
  - Tabelas Processuais Unificadas do CNJ, tabela de movimentos (SGT/CNJ,
    webservice público sgt_ws.php) — nomes e glossários oficiais.
"""

# --- Tabela 1: movimento padronizado -> o que corre -----------------------
# Coluna 1 usa o NOME OFICIAL da tabela de movimentos do CNJ (código entre
# parênteses), não uma redação inventada. Onde o movimento é pai/filho, a
# forma é "Pai › Filho", como o SGT a expõe.
MOVIMENTOS = [
    ("Conclusão <span class=\"cod\">(51)</span>",
     "Os autos foram apresentados ao juiz para que produza despacho, decisão, sentença ou voto.",
     "Nada, para as partes. É movimento interno do juízo.",
     "Glossário do movimento 51"),
    ("Despacho › Mero expediente <span class=\"cod\">(11009 › 11010)</span>",
     "Pronunciamento do juiz sem conteúdo decisório — a categoria residual do art. 203, §3º. O prazo que ele abre depende do que está escrito nele, não do rótulo.",
     "Depende do teor. Ler o inteiro teor é obrigatório: é aqui que costuma estar a nomeação do perito.",
     "Art. 203, §3º"),
    ("Perícia › Determinada/Designada <span class=\"cod\">(14901)</span>",
     "O juiz deferiu a prova pericial e nomeou o perito, fixando desde logo o prazo de entrega do laudo.",
     "<strong>15 dias</strong> para arguir impedimento ou suspeição, indicar assistente técnico e apresentar quesitos.",
     "Art. 465, caput e §1º, I a III"),
    ("Intimação › Eletrônica <span class=\"cod\">(12263)</span>",
     "A intimação foi disponibilizada no portal do sistema. É este o marco que dispara a contagem — não a data do despacho, nem a da juntada.",
     "O prazo do ato a que a intimação se refere. Ver a tabela de contagem abaixo.",
     "Lei 11.419/2006, art. 5º · CPC, art. 231, V"),
    ("Juntada › Petição <span class=\"cod\">(67)</span> — proposta de honorários",
     "O perito apresentou proposta de honorários, currículo com comprovação de especialização e contatos profissionais.",
     "<strong>5 dias</strong>, em prazo comum, para as partes se manifestarem antes do arbitramento.",
     "Art. 465, §2º e §3º"),
    ("Perícia › Agendada / Reagendada <span class=\"cod\">(14901)</span>",
     "Data e local do início da produção da prova foram designados pelo juiz ou indicados pelo perito.",
     "Nenhum prazo da parte, mas nasce um dever do perito: comunicar os assistentes com <strong>antecedência mínima de 5 dias</strong>, comprovada nos autos.",
     "Arts. 474 e 466, §2º"),
    ("Perícia › Realizada <span class=\"cod\">(14901)</span>",
     "A diligência foi cumprida.",
     "A janela dos <strong>quesitos suplementares</strong> é durante a diligência — depois dela, não há mais.",
     "Art. 469"),
    ("Juntada › Documento <span class=\"cod\">(67)</span> — laudo pericial",
     "O perito protocolou o laudo. A lei exige que isso ocorra ao menos 20 dias antes da audiência de instrução e julgamento.",
     "<strong>15 dias</strong>, em prazo comum, para manifestação das partes e para o parecer de cada assistente técnico.",
     "Art. 477, caput e §1º"),
    ("Juntada › Petição <span class=\"cod\">(67)</span> — esclarecimentos do perito",
     "O perito respondeu a ponto divergente ou duvidoso apontado pela parte, pelo juiz, pelo Ministério Público ou no parecer do assistente técnico.",
     "Persistindo a necessidade, cabe requerer a intimação do perito ou do assistente para a audiência, <em>formulando desde logo as perguntas sob forma de quesitos</em>.",
     "Art. 477, §2º e §3º"),
    ("Decurso de Prazo <span class=\"cod\">(1051)</span>",
     "O prazo terminou sem a manifestação esperada. O movimento cobre todas as hipóteses de decurso, salvo as que geram trânsito em julgado.",
     "Nada mais naquela janela. Mas o decurso de <em>uma</em> janela não fecha as outras — ver os três enganos abaixo.",
     "Glossário do movimento 1051"),
    ("Expedição de documento <span class=\"cod\">(60)</span>",
     "Um documento ou certidão ficou pronto e foi encaminhado para produzir sua finalidade.",
     "Em regra nada, por si só. O prazo vem da intimação que o acompanha, não da expedição.",
     "Glossário do movimento 60"),
]

# --- Tabela 2: da intimação eletrônica à data com dia certo ---------------
CONTAGEM = [
    ("1", "A intimação é disponibilizada no portal próprio do sistema, dispensada a publicação em órgão oficial.",
     "Lei 11.419/2006, art. 5º, caput"),
    ("2", "Se o advogado consulta o teor, a intimação considera-se realizada <strong>no dia da consulta</strong>. Consulta em dia não útil conta como o primeiro dia útil seguinte.",
     "Lei 11.419/2006, art. 5º, §1º e §2º"),
    ("3", "Se ninguém consulta, a intimação considera-se automaticamente realizada no término de <strong>10 dias corridos</strong> contados do envio.",
     "Lei 11.419/2006, art. 5º, §3º"),
    ("4", "O prazo começa a correr no <strong>dia útil seguinte</strong> à consulta — ou ao término do prazo para que ela se desse.",
     "CPC, art. 231, V"),
    ("5", "Conta-se excluindo o dia do começo e incluindo o do vencimento, e <strong>somente em dias úteis</strong>.",
     "CPC, arts. 224, caput, e 219"),
    ("6", "Começo ou vencimento em dia de expediente encerrado antes ou iniciado depois da hora normal, ou com indisponibilidade da comunicação eletrônica, são protraídos para o primeiro dia útil seguinte.",
     "CPC, art. 224, §1º"),
    ("7", "Entre 20 de dezembro e 20 de janeiro, inclusive, o curso do prazo fica suspenso.",
     "CPC, art. 220"),
]

# --- FAQ: fonte única (visível + JSON-LD saem daqui) ----------------------
FAQ = [
    ("Quando começa a contar o prazo da perícia no processo eletrônico?",
     "No dia útil seguinte à intimação, e não na data do despacho nem na da juntada. A intimação eletrônica considera-se realizada no dia em que o advogado consulta o teor no portal (art. 5º, §1º, da Lei nº 11.419/2006) ou, se não houver consulta, no término de 10 dias corridos contados do envio (art. 5º, §3º). A partir daí, o art. 231, V, do CPC manda iniciar a contagem no dia útil seguinte, o art. 224 manda excluir o dia do começo e incluir o do vencimento, e o art. 219 manda contar apenas dias úteis."),
    ("O que significa “Conclusão” no andamento do processo?",
     "É o registro de que os autos foram apresentados ao juiz para que produza despacho, decisão, sentença ou voto — a definição do glossário do movimento 51 das Tabelas Processuais Unificadas do CNJ. Por si só não abre prazo para as partes: é movimento interno do juízo. O prazo aparece depois, quando o pronunciamento é proferido e a intimação correspondente é disponibilizada."),
    ("O prazo em dobro do art. 229 vale na perícia em processo eletrônico?",
     "Não. O art. 229 do CPC concede prazo em dobro aos litisconsortes com procuradores de escritórios distintos, mas o §2º do mesmo artigo afasta expressamente essa contagem nos processos em autos eletrônicos. Como a quase totalidade dos processos cíveis hoje tramita eletronicamente, o prazo de 15 dias dos arts. 465, §1º, e 477, §1º é simples, ainda que haja litisconsórcio com advogados diferentes."),
    ("Perdi o prazo dos quesitos. Ainda dá para atuar tecnicamente no processo?",
     "O decurso de uma janela não fecha as outras. O prazo de 15 dias do art. 465, §1º, é o de arguir impedimento, indicar assistente técnico e apresentar quesitos iniciais. Independentemente dele, o art. 469 admite quesitos suplementares durante a diligência, e o art. 477, §1º, abre 15 dias comuns, contados da intimação sobre o laudo, para a manifestação da parte e para o parecer do assistente técnico. É nessa última janela que a crítica técnica ao laudo é apresentada, e ela existe mesmo para quem não apresentou quesitos no início."),
]
