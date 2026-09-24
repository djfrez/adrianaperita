# -*- coding: utf-8 -*-
"""SEO-065 — conteúdo da seção `#cpaq` em `/produtos-quimicos-controlados/`.

Fatos conferidos em fonte primária nesta execução (24/09/2026). Nada aqui saiu
da memória do modelo — duas execuções anteriores (SEO-002, SEO-061) já foram
corrigidas por isso, e este tema é novo no site inteiro.

  · Decreto nº 2.977, de 1º de março de 1999 — promulga a CPAQ, assinada em
    Paris em 13/01/1993; vigente para o Brasil desde 29/04/1997. Texto integral
    baixado do Planalto.
  · Decreto nº 2.074, de 14 de novembro de 1996 — cria a Comissão
    Interministerial e ELENCA as obrigações: art. 3º (vedações e infração
    declaratória), art. 4º (declaração inicial, declarações de atualização do
    exercício anterior, informação a pedido), art. 5º (acesso de inspetores da
    OPAQ, coleta e retirada de amostras, visitas de verificação de dados).
    Texto integral baixado do Planalto.
  · Lei nº 11.254, de 27 de dezembro de 2005 — art. 3º: advertência; multa de
    R$ 5.000,00 a R$ 50.000,00; perda do bem; suspensão do direito de
    comercializar de 6 meses a 5 anos; cassação da habilitação em reincidência.
    § 3º cumulatividade; § 4º penalidades aplicadas pela Comissão após processo
    administrativo com amplo direito de defesa. Art. 4º: crime, reclusão de 1 a
    10 anos. Texto integral baixado do Planalto.
  · Prazos das declarações — MCTI/CGBS, com a redação literal "até 31 de
    janeiro, para as atividades realizadas no ano anterior; e até 31 de julho,
    para a previsão das atividades para o ano seguinte". Conferido em DUAS
    páginas oficiais (portal atual gov.br/mcti e portal antigo mctic), porque
    prazo é o tipo de fato que um advogado usa sem reconferir.
  · Presidência e Autoridade Nacional — o Ministro de Estado da Ciência,
    Tecnologia e Inovação preside a CIAD/CPAQ e nessa qualidade corresponde à
    Autoridade Nacional; Secretaria-Executiva Permanente é a Coordenação-Geral
    de Bens Sensíveis (CGBS/MCTI). Membros: MCTI, Defesa, MDIC, Fazenda, MJSP e
    MRE.

DIVERGÊNCIA DE FONTE, resolvida e registrada: o Decreto nº 2.074/1996 diz que a
Convenção foi aprovada pelo "Decreto Legislativo n° 9, de 6 de março de 1996";
o Decreto nº 2.977/1999 diz "Decreto Legislativo nº 9, de 29 de fevereiro de
1996". Dois decretos federais discordam do DIA do mesmo ato. A página cita o
Decreto Legislativo nº 9 **sem o dia** — não se afirma o que a fonte contesta.

O QUE NÃO SE PUBLICA, e é decisão, não esquecimento: os **limiares
quantitativos** que disparam cada declaração (Listas 1, 2 e 3, DOC e DOC/PSF)
estão no Anexo sobre Implementação e Verificação da Convenção e nos formulários
vigentes da CGBS. Não foram obtidos em fonte primária nesta execução, e por isso
a página manda conferi-los no formulário do ano-base em vez de repeti-los. Um
limiar errado aqui seria pior do que a ausência dele.
"""

# Presidência, Autoridade Nacional e Secretaria-Executiva.
AUTORIDADE = (
    "o Ministro de Estado da Ciência, Tecnologia e Inovação preside a CIAD/CPAQ e, "
    "nessa qualidade, corresponde à Autoridade Nacional exigida pela Convenção"
)
SECRETARIA = (
    "Coordenação-Geral de Bens Sensíveis (CGBS) do Ministério da Ciência, "
    "Tecnologia e Inovação"
)
MEMBROS = ("Ciência, Tecnologia e Inovação; Defesa; Desenvolvimento, Indústria, "
           "Comércio e Serviços; Fazenda; Justiça e Segurança Pública; e "
           "Relações Exteriores")

# Redação literal do MCTI sobre os prazos — conferida em duas páginas oficiais.
PRAZOS_LITERAL = ("até 31 de janeiro, para as atividades realizadas no ano anterior; "
                  "e até 31 de julho, para a previsão das atividades para o ano seguinte")

# Vigência da Convenção para o Brasil (Decreto nº 2.977/1999, considerandos).
VIGENCIA_BR = "29 de abril de 1997"

# --------------------------------------------------------------------------
# Tabela: o que declarar, quem declara, quando
# --------------------------------------------------------------------------
DECLARACOES = [
    ("Declaração inicial",
     "Instalação que passa a produzir, consumir, processar, importar ou exportar "
     "substância abrangida pela Convenção, ou a fabricar substâncias orgânicas "
     "definidas (DOC e DOC/PSF) acima do limiar",
     "Em formulário fornecido pela Secretaria-Executiva, ao iniciar a atividade "
     "(art. 4º, I, do Decreto nº 2.074/1996)"),
    ("Declaração de atividades realizadas",
     "Todos os declarantes, quanto às operações e atividades do exercício anterior",
     "Até 31 de janeiro"),
    ("Declaração de previsão de atividades",
     "Somente quem produz substâncias das Listas 2 e 3",
     "Até 31 de julho, para o ano seguinte"),
    ("Informação a pedido",
     "Qualquer declarante, quando a Secretaria-Executiva julgar necessário ao "
     "cumprimento da Convenção",
     "A qualquer momento (art. 4º, III, do Decreto nº 2.074/1996)"),
]

# --------------------------------------------------------------------------
# Tabela: o que distingue este controle dos dois anteriores
# --------------------------------------------------------------------------
DISTINCAO = [
    ("O que dispara a obrigação",
     "Constar o produto da relação da Portaria MJSP nº 204/2022 ou da lista de PCE "
     "do Exército",
     "O que a instalação sintetiza, ainda que nada do que ela produza esteja em "
     "qualquer lista nacional"),
    ("Natureza do dever",
     "Licenciamento e registro prévios — há um instrumento habilitante a obter",
     "Declaração periódica — não há licença a pedir, e a ausência de licença não "
     "isenta de declarar"),
    ("Quem fiscaliza",
     "Polícia Federal e Comando do Exército, em território nacional",
     "Comissão Interministerial, em visita de verificação, e inspetores da OPAQ, "
     "em inspeção internacional"),
    ("Sanção da irregularidade declaratória",
     "Art. 12, III, da Lei nº 10.357/2001 — informação com dados incompletos ou "
     "inexatos",
     "Art. 3º, III, do Decreto nº 2.074/1996 e art. 1º, III, da Lei nº 11.254/2005 "
     "— omitir informação ou prestar informação incorreta"),
]

# --------------------------------------------------------------------------
# FAQ — três entradas. Entram ANTES da última, que é contratualmente a de
# intake da SEO-046 (invariante relacional, não posicional — SEO-064).
# --------------------------------------------------------------------------
FAQS = [
    ("Minha empresa precisa declarar à OPAQ mesmo sem produzir produto controlado?",
     "Pode precisar. O dever de declarar da Convenção sobre a Proibição das Armas "
     "Químicas não se limita a quem opera substâncias das Listas 1, 2 e 3: alcança "
     "também as instalações que fabricam substâncias orgânicas definidas (DOC) e as "
     "que contêm fósforo, enxofre ou flúor (DOC/PSF), acima dos limiares fixados no "
     "Anexo sobre Implementação e Verificação da Convenção. O teste é sobre o que a "
     "instalação sintetiza, não sobre a presença do produto em lista nacional — por "
     "isso uma empresa impecável perante a Polícia Federal e o Exército pode estar "
     "em falta aqui. Os limiares vigentes devem ser conferidos no formulário da "
     "Coordenação-Geral de Bens Sensíveis relativo ao ano-base, e a verificação "
     "exige ler a rota de síntese e a fórmula molecular dos produtos, não apenas o "
     "cadastro comercial."),
    ("Quando vencem as declarações da CPAQ?",
     "São duas por ano: até 31 de janeiro, para as atividades realizadas no ano "
     "anterior, e até 31 de julho, para a previsão das atividades do ano seguinte — "
     "esta última exigida somente de quem produz substâncias das Listas 2 e 3. Além "
     "delas, há a declaração inicial, devida quando a instalação passa a exercer "
     "atividade abrangida, e a informação a pedido da Secretaria-Executiva, que pode "
     "ser solicitada a qualquer momento, nos termos do art. 4º do Decreto nº "
     "2.074/1996."),
    ("Qual a penalidade por erro na declaração da Convenção sobre Armas Químicas?",
     "A Lei nº 11.254/2005, no art. 3º, sujeita quem omite informação, presta "
     "informação imprecisa ou deixa de colaborar com a Comissão Interministerial a "
     "advertência, multa de R$ 5.000,00 a R$ 50.000,00, perda do bem envolvido na "
     "infração, suspensão do direito de comercializar por 6 meses a 5 anos e, em "
     "caso de reincidência, cassação da habilitação para atuação no comércio. As "
     "penalidades de multa, perda do bem, suspensão e cassação podem ser aplicadas "
     "cumulativamente, conforme a gravidade e os antecedentes. Quem aplica é a "
     "própria Comissão Interministerial, depois de apurada a infração em processo "
     "administrativo no qual se assegura amplo direito de defesa — é nesse processo "
     "que cabe a demonstração técnica. Situação distinta é a do art. 4º, que trata "
     "de uso ou contribuição para o uso de armas químicas e é crime, com pena de "
     "reclusão de 1 a 10 anos."),
]
