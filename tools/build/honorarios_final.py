# -*- coding: utf-8 -*-
"""SEO-051 — "ao final do processo": quando o dinheiro da perícia se move.

Por que este arquivo existe (GSC, 28 dias findos em 10/09/2026):

    /honorarios-pericia-judicial/ ...... 99 impressões · pos 11,1 · 2 cliques

É a página com mais impressões **sem nenhuma janela de medição aberta** (as
quatro acima dela estão embargadas até 14–20/09). A consulta nominal mais
específica que ela recebe é `pagamento de honorários periciais ao final do
processo` (pos 53) — e a página não respondia: "ao final do processo" aparecia
uma vez, de passagem. Medido por script sobre a página:

    "art. 82" ... 0     "art. 84" ... 0     "art. 91" ... 0
    "790-B" ..... 0     "trabalhista" 0     "465, §5º" .. 0

Fontes primárias abertas nesta execução (texto compilado do Planalto, todas
as ocorrências extraídas e a última escolhida — regra 8 do handoff):

  - CPC/2015, arts. 82 (caput e §2º), 84, 91 (caput, §§1º e 2º), 95 (§§1º a 4º),
    98 (§§2º e 3º) e 465 (§§3º a 5º).
  - CLT, art. 790-B, caput e §§1º a 4º, com as duas anotações do Planalto
    "(Declarado inconstitucional pela ADI 5766)".

O que NÃO entra, por não ter sido conferido na fonte: valores do teto do CSJT,
número de resolução do CSJT, e qualquer precedente do STJ sobre o reembolso do
assistente técnico citado por número.

Regra 11 do backlog: visível e JSON-LD saem DAQUI, uma vez só.
"""

# --------------------------------------------------------------------------
# Transcrições literais (conferidas no Planalto; o verificador reconfere)
# --------------------------------------------------------------------------
ART_82_2 = "A sentença condenará o vencido a pagar ao vencedor as despesas que antecipou."
ART_84 = ("As despesas abrangem as custas dos atos do processo, a indenização de viagem, "
          "a remuneração do assistente técnico e a diária de testemunha.")
ART_465_4 = ("O juiz poderá autorizar o pagamento de até cinquenta por cento dos honorários "
             "arbitrados a favor do perito no início dos trabalhos, devendo o remanescente ser "
             "pago apenas ao final, depois de entregue o laudo e prestados todos os "
             "esclarecimentos necessários.")
ART_465_5 = ("Quando a perícia for inconclusiva ou deficiente, o juiz poderá reduzir a "
             "remuneração inicialmente arbitrada para o trabalho.")
ART_91_2 = ("Não havendo previsão orçamentária no exercício financeiro para adiantamento dos "
            "honorários periciais, eles serão pagos no exercício seguinte ou ao final, pelo "
            "vencido, caso o processo se encerre antes do adiantamento a ser feito pelo ente "
            "público.")
CLT_790B_3 = "O juízo não poderá exigir adiantamento de valores para realização de perícias."
CLT_790B_CAPUT = ("A responsabilidade pelo pagamento dos honorários periciais é da parte "
                  "sucumbente na pretensão objeto da perícia")
CPC = [ART_82_2, ART_84, ART_465_4, ART_465_5, ART_91_2]
CLT = [CLT_790B_3, CLT_790B_CAPUT]

# --------------------------------------------------------------------------
# Tabela 1 — o calendário do dinheiro da perícia no cível
# (momento, o que acontece, onde)
# --------------------------------------------------------------------------
CALENDARIO = [
    ("Arbitramento",
     "O juiz fixa o valor depois da proposta do perito e dos 5 dias de manifestação das partes, e as intima para adiantar.",
     "Art. 465, §3º"),
    ("Depósito",
     "O juiz pode mandar a parte responsável depositar o valor em juízo; o dinheiro fica em conta judicial, corrigido monetariamente.",
     "Art. 95, §§1º e 2º"),
    ("Início dos trabalhos",
     "O perito pode levantar <strong>até metade</strong> do valor arbitrado, se o juiz autorizar.",
     "Art. 465, §4º"),
    ("Laudo entregue e esclarecimentos prestados",
     "O perito levanta o restante. Este é o “final” do art. 465, §4º: o fim <strong>da perícia</strong>, não o do processo.",
     "Art. 465, §4º"),
    ("Laudo inconclusivo ou deficiente",
     "O juiz pode <strong>reduzir</strong> a remuneração arbitrada — e o saldo retido é o que torna a redução possível na prática.",
     "Art. 465, §5º"),
    ("Sentença",
     "O vencido é condenado a devolver ao vencedor o que ele antecipou — honorários do perito e remuneração do assistente técnico incluídos.",
     "Arts. 82, §2º, e 84"),
    ("Depois do trânsito em julgado, com gratuidade",
     "Se a perícia foi paga com dinheiro público, a Fazenda executa quem foi condenado nas despesas; se esse condenado também é beneficiário, a cobrança fica suspensa por 5 anos e depois se extingue.",
     "Arts. 95, §4º, e 98, §§2º e 3º"),
]

# --------------------------------------------------------------------------
# Tabela 2 — onde o perito recebe, de fato, só no fim
# (situação, regra, onde)
# --------------------------------------------------------------------------
SO_NO_FIM = [
    ("Perícia requerida pela Fazenda Pública, pelo Ministério Público ou pela Defensoria",
     "As despesas são pagas ao final pelo vencido. A perícia pode ser feita por entidade pública ou adiantada por quem a requereu, se houver previsão orçamentária; sem ela, paga-se no exercício seguinte — ou ao final, pelo vencido, se o processo terminar antes.",
     "CPC, art. 91, caput e §§1º e 2º"),
    ("Justiça do Trabalho",
     "O juiz <strong>não pode exigir adiantamento</strong>. Paga a parte sucumbente na pretensão objeto da perícia, dentro do teto fixado pelo Conselho Superior da Justiça do Trabalho, com parcelamento possível.",
     "CLT, art. 790-B, caput e §§1º a 3º"),
    ("Justiça do Trabalho, sucumbente com gratuidade",
     "O STF declarou inconstitucional a cobrança do beneficiário: a expressão “ainda que beneficiária da justiça gratuita” do caput e o §4º inteiro.",
     "ADI 5766"),
]

# --------------------------------------------------------------------------
# FAQ nova (penúltima; a de intake da SEO-046 segue última)
# --------------------------------------------------------------------------
QUESTION = "Os honorários periciais são pagos só ao final do processo?"
ANSWER = (
    "Em regra, não. No processo civil, quem requereu a perícia adianta o valor, e o juiz pode "
    "autorizar o perito a levantar até metade no início dos trabalhos, ficando o restante para "
    "depois de entregue o laudo e prestados os esclarecimentos (arts. 95 e 465, §4º, do CPC) — "
    "esse “final” é o da perícia, não o do processo. O fim do processo entra em três situações: "
    "na sentença, que condena o vencido a devolver ao vencedor o que ele antecipou, inclusive a "
    "remuneração do assistente técnico (arts. 82, §2º, e 84); quando a perícia é requerida pela "
    "Fazenda Pública, pelo Ministério Público ou pela Defensoria sem previsão orçamentária "
    "(art. 91, §2º); e na Justiça do Trabalho, onde o juiz não pode exigir adiantamento e paga a "
    "parte sucumbente na pretensão objeto da perícia (CLT, art. 790-B).")

# --------------------------------------------------------------------------
# Correção de uma resposta existente (SEO-017) que omitia o art. 84
# --------------------------------------------------------------------------
REEMBOLSO_Q = "A parte vencida reembolsa os honorários do assistente técnico?"
REEMBOLSO_OLD = (
    "Não automaticamente, e o tema é controvertido. Há decisões que tratam o valor como "
    "consectário da sucumbência e decisões que o classificam como despesa extraprocessual de "
    "interesse privado — sob o argumento de que o assistente atua na defesa de quem o contratou, "
    "sem o dever de imparcialidade do perito. O que é razoavelmente pacífico: se o ressarcimento "
    "não foi pedido e decidido no processo, não se cobra depois em ação própria. Quem pretende "
    "recuperar o valor precisa pedir expressamente, no momento adequado.")
REEMBOLSO_NEW = (
    "O Código prevê o reembolso, mas ele não é automático. O art. 84 do CPC inclui "
    "expressamente a remuneração do assistente técnico entre as despesas processuais, e o "
    "art. 82, §2º manda a sentença condenar o vencido a pagar ao vencedor as despesas que "
    "antecipou. Na prática, pesam duas condições: o pagamento ao assistente precisa estar "
    "comprovado nos autos — contrato e recibo ou nota fiscal —, e o ressarcimento precisa ser "
    "pedido e decidido no processo; o que não foi pedido ali dificilmente se cobra depois. Ainda "
    "há decisões que resistem a transferir ao vencido o valor integral livremente contratado, sob o "
    "argumento de que o assistente atua na defesa de quem o contratou — razão para documentar "
    "escopo e horas desde o início.")
TABELA_OLD = "Não automática, e controvertida — precisa ser pedida no processo"
TABELA_NEW = "Prevista no art. 84, mas precisa ser pedida e comprovada no processo"

LLMS_OLD = ("e a controvérsia sobre reembolso dos honorários do assistente técnico pela parte "
            "vencida — não é automático, e se não for pedido e decidido no processo não se cobra depois")
LLMS_NEW = ("o reembolso dos honorários do assistente técnico pela parte vencida — previsto no "
            "art. 84 do CPC, que inclui a remuneração do assistente entre as despesas, combinado com o "
            "art. 82, §2º, mas não automático: exige prova do pagamento e pedido decidido no processo; "
            "e o que \"pagamento ao final do processo\" significa em cada regime (seção #final-do-processo): "
            "no cível o \"final\" do art. 465, §4º é o fim da perícia (até 50% no início, saldo depois do "
            "laudo e dos esclarecimentos; redução por laudo inconclusivo ou deficiente no §5º), a sentença "
            "condena o vencido a reembolsar o que o vencedor antecipou (arts. 82, §2º, e 84), perícia "
            "requerida pela Fazenda Pública, MP ou Defensoria sem previsão orçamentária é paga no "
            "exercício seguinte ou ao final pelo vencido (art. 91, §2º), e na Justiça do Trabalho o juiz "
            "não pode exigir adiantamento e paga a parte sucumbente NA PRETENSÃO OBJETO DA PERÍCIA, não "
            "necessariamente o vencido na ação (CLT, art. 790-B, caput e §3º), com a cobrança do "
            "beneficiário da gratuidade afastada pelo STF na ADI 5766")
