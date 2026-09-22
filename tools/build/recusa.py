# -*- coding: utf-8 -*-
"""SEO-063 — quando o problema é o perito, e não o laudo.

Por que esta página (GSC, 28 dias findos em 22/09/2026):

    /impugnacao-laudo-pericial/ ... 60 impressões · pos 11,6 · 0 cliques

É a **maior página livre de janela de medição** e a de maior intenção
comercial do domínio. Todas as maiores estão sob janela: /assistente-tecnica/
(734 impr, SEO-056 até ~29/09) · /quesitos-periciais/ (573, SEO-048 ~28/09) ·
/honorarios-pericia-judicial/ (163, SEO-058 ~02/10) · /laudo-pericial/ (113,
SEO-062 ~05/10) · /cpc-prova-pericial/ (112, SEO-057 ~30/09) ·
/normas-tecnicas-pericia/ (107, SEO-061 ~04/10) · /prazo-validade-alimentos/
(77, SEO-055 ~28/09) · /pericia-contaminacao-alimentos/ (53, SEO-060 ~03/10).

**Não é execução de snippet, e isso é deliberado** — mesma razão da SEO-062:
SEO-057 (title+description) e SEO-058 (só description) estão em medição para
dizer qual é a alavanca. Uma terceira variante antes de 30/09–02/10 produziria
um ponto não controlado.

O cruzamento page × query de hoje confirma que **não há vocabulário de usuário
para decodificar nesta página**: /impugnacao-laudo-pericial/ tem **uma única
consulta atribuída** em 28 dias (`como fazer impunação ao laudo pericial`,
1 impressão, pos 55). As 60 impressões são cauda anonimizada. Logo, o método
das SEO-044/048/049/050/051 não se aplica aqui — o caminho é cobertura
semântica verificável.

--------------------------------------------------------------------------
A MEDIÇÃO QUE DESCARTOU DUAS HIPÓTESES ANTES DE UMA LINHA SER ESCRITA
--------------------------------------------------------------------------
Contagem sobre as 21 páginas, antes de escrever:

    "art. 473" .......... 76 ocorrências, em 11 páginas   JÁ COBERTO (descartado)
    "art. 466, §2º" ..... já nesta própria página          JÁ COBERTO (descartado)
    "art. 467" .......... 1 página (/cpc-prova-pericial/)  parcial
    "art. 468" .......... 5 páginas                        parcial
    "art. 158" .......... 1 página (/cpc-prova-pericial/)  coberto
    "art. 148" .......... 0                                ← o buraco
    "art. 144" .......... 0                                ← o buraco
    "art. 145" .......... 0                                ← o buraco
    "em apartado" ....... 0                                ← o buraco
    "auxiliares da justiça" 0                              ← o buraco

Duas hipóteses de partida caíram na medição: o art. 473 (esta página não o
cita, mas /laudo-pericial/ tem uma tabela inteira sobre ele) e o art. 466, §2º
(já está nesta página, no quadro da SEO-050). Medir evitou duas duplicatas.

O que sobrou é um buraco real e específico: **/cpc-prova-pericial/ ensina que
impedimento e suspeição do perito se arguem em 15 dias contados da intimação
da nomeação (art. 465, §1º, I) — e o site nunca diz o que acontece quando o
motivo só aparece no laudo**, que é exatamente a situação de quem chega nesta
página. Lido isoladamente, o site sugere que o prazo venceu e não há o que
fazer. O art. 148, §1º diz outra coisa, e nenhuma página do site o cita.

--------------------------------------------------------------------------
FONTE
--------------------------------------------------------------------------
Todas as citações saem do texto oficial da Lei nº 13.105/2015 no Planalto,
baixado e conferido nesta execução. Cada artigo citado tem **uma única
ocorrência** no arquivo (conferido: arts. 144, 145, 148, 149, 466, 467, 468,
477) — não há redação alterada a desempatar, que é a armadilha registrada na
regra "Planalto: todas as ocorrências, ficar com a última".

O que NÃO se afirma, por não ter sido verificado nesta execução: qualquer tese
jurisprudencial sobre aplicação analógica do prazo de 15 dias do art. 146 ao
perito. O texto se limita ao que o Código diz — "na primeira oportunidade" —
e extrai daí a consequência prática, sem inventar prazo.
"""

LEI = "Lei nº 13.105/2015"
LEI_URL = "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm"

# --------------------------------------------------------------------------
# Citações literais. São a cadeia de evidência: o verificador procura cada uma
# destas no texto do Planalto baixado na hora.
# --------------------------------------------------------------------------
CIT_148_CAPUT = ("Aplicam-se os motivos de impedimento e de suspeição: I - ao membro do "
                 "Ministério Público; II - aos auxiliares da justiça; III - aos demais "
                 "sujeitos imparciais do processo.")
CIT_148_1 = ("A parte interessada deverá arguir o impedimento ou a suspeição, em petição "
             "fundamentada e devidamente instruída, na primeira oportunidade em que lhe "
             "couber falar nos autos.")
CIT_148_2 = ("O juiz mandará processar o incidente em separado e sem suspensão do processo, "
             "ouvindo o arguido no prazo de 15 (quinze) dias e facultando a produção de prova, "
             "quando necessária.")
CIT_149 = ("São auxiliares da Justiça, além de outros cujas atribuições sejam determinadas "
           "pelas normas de organização judiciária, o escrivão, o chefe de secretaria, o "
           "oficial de justiça, o perito")
CIT_145_2 = ("Será ilegítima a alegação de suspeição quando: I - houver sido provocada por "
             "quem a alega; II - a parte que a alega houver praticado ato que signifique "
             "manifesta aceitação do arguido.")
CIT_466_1 = ("Os assistentes técnicos são de confiança da parte e não estão sujeitos a "
             "impedimento ou suspeição.")
CIT_467 = "O perito pode escusar-se ou ser recusado por impedimento ou suspeição."
CIT_467_PU = ("O juiz, ao aceitar a escusa ou ao julgar procedente a impugnação, nomeará "
              "novo perito.")
CIT_468_2 = ("O perito substituído restituirá, no prazo de 15 (quinze) dias, os valores "
             "recebidos pelo trabalho não realizado, sob pena de ficar impedido de atuar "
             "como perito judicial pelo prazo de 5 (cinco) anos.")

CITACOES = [CIT_148_CAPUT, CIT_148_1, CIT_148_2, CIT_149, CIT_145_2,
            CIT_466_1, CIT_467, CIT_467_PU, CIT_468_2]

# --------------------------------------------------------------------------
# Tabela 1 — o motivo do juiz, lido para o perito.
# Cada linha traz a hipótese como ela aparece na perícia técnica, o dispositivo
# e a natureza. Nada aqui generaliza o texto legal: quando o inciso é restrito
# (o VII fala só de instituição de ensino), a linha diz que é restrito.
# --------------------------------------------------------------------------
MOTIVOS = [
    ("O perito é sócio, dirigente ou administrador da empresa que é parte",
     "Art. 144, V", "Impedimento",
     "Hipótese objetiva: verifica-se pelo contrato social, não por juízo sobre a conduta."),

    ("O perito é empregador de uma das partes — ou herdeiro presuntivo ou donatário dela",
     "Art. 144, VI", "Impedimento",
     "O inciso alcança o <em>empregador</em>. A relação inversa — o perito empregado da parte — "
     "não está no rol do art. 144 e se discute como suspeição pelo art. 145, IV."),

    ("Parentesco até o terceiro grau com a parte, ou com o advogado que postula no processo",
     "Art. 144, III e IV", "Impedimento",
     "Alcança parente consanguíneo ou afim, em linha reta ou colateral, até o terceiro grau. "
     "É a hipótese de verificação mais simples e a mais rara."),

    ("A parte é instituição de ensino com a qual o perito tem emprego ou contrato de prestação de serviços",
     "Art. 144, VII", "Impedimento",
     "Hipótese estreita e literal: vale para instituição de ensino. Contrato de prestação de "
     "serviços com parte de outra natureza não cabe aqui — cabe no art. 145."),

    ("O perito já prestou consultoria ou assinou parecer técnico para uma das partes sobre o mesmo objeto",
     "Art. 145, II", "Suspeição",
     "É a hipótese mais frequente em matéria técnica: o inciso alcança quem “aconselhar alguma "
     "das partes acerca do objeto da causa”. Costuma ser descoberta no currículo anexo ao laudo."),

    ("O perito é credor ou devedor de uma das partes, de seu cônjuge ou de parentes até o terceiro grau",
     "Art. 145, III", "Suspeição",
     "Inclui a relação comercial corrente — fornecimento, prestação de serviço, contrato em curso."),

    ("Amigo íntimo ou inimigo de qualquer das partes ou de seus advogados",
     "Art. 145, I", "Suspeição",
     "Exige demonstração, não adjetivo: mensagem, vínculo societário, histórico documentado."),

    ("Interessado no julgamento em favor de uma das partes",
     "Art. 145, IV", "Suspeição",
     "É a cláusula aberta, e a que exige mais prova. É onde entra o interesse econômico indireto "
     "— o perito que atende regularmente o setor de uma das partes, por exemplo."),
]

# --------------------------------------------------------------------------
# Tabela 2 — três instrumentos distintos, frequentemente confundidos.
# --------------------------------------------------------------------------
INSTRUMENTOS = [
    ("O perito não é imparcial",
     "Arguição de impedimento ou suspeição, em <strong>petição própria</strong>, fundamentada e instruída",
     "Art. 467 c/c art. 148, II e §§ 1º e 2º",
     "Na primeira oportunidade de falar nos autos <strong>depois de conhecido o fato</strong>",
     "Acolhida a recusa, o juiz nomeia novo perito (art. 467, parágrafo único)."),

    ("O perito não tem conhecimento técnico na área do objeto",
     "Pedido de substituição",
     "Art. 468, I",
     "Assim que se constatar — não depende de o laudo existir",
     "Substituição do perito. Não é crítica ao resultado: é falta de aptidão para produzi-lo."),

    ("O perito não entregou o laudo no prazo, sem motivo legítimo",
     "Pedido de substituição",
     "Art. 468, II e §§ 1º a 3º",
     "Vencido o prazo fixado pelo juiz e a prorrogação do art. 476",
     "Substituição e comunicação à corporação profissional, com possível multa (§ 1º). E o § 2º, "
     "literalmente: “O perito substituído restituirá, no prazo de 15 (quinze) dias, os valores "
     "recebidos pelo trabalho não realizado, sob pena de ficar impedido de atuar como perito "
     "judicial pelo prazo de 5 (cinco) anos.” Não havendo restituição voluntária, a parte que "
     "adiantou os honorários pode executá-lo (§ 3º)."),
]

# --------------------------------------------------------------------------
# FAQ — duas entradas. Visível e JSON-LD saem daqui.
# A de intake (SEO-046) é contratualmente a última.
# --------------------------------------------------------------------------
FAQS = [
    ("Descobri no laudo que o perito já trabalhou para a outra parte. O prazo para arguir suspeição não venceu?",
     "Não necessariamente. O prazo de 15 dias do art. 465, §1º, I, corre da intimação do despacho de "
     "nomeação — quando a parte, em regra, ainda não sabe nada sobre o perito além do nome. Quem "
     "governa a arguição depois disso é o art. 148: o inciso II manda aplicar os motivos de "
     "impedimento e de suspeição aos auxiliares da justiça, e o perito é auxiliar da justiça pelo "
     "art. 149, que o nomeia expressamente. O §1º fixa o marco: a parte deve arguir “em petição "
     "fundamentada e devidamente instruída, na primeira oportunidade em que lhe couber falar nos "
     "autos”. Fato que só aparece no laudo tem a sua primeira oportunidade na fase de manifestação "
     "— mas em petição própria, porque o §2º determina que o incidente seja processado em separado "
     "e sem suspensão do processo. Duas cautelas: a arguição precisa dizer quando e como o fato foi "
     "conhecido, e o art. 145, §2º, II torna ilegítima a alegação da parte que já praticou ato de "
     "manifesta aceitação do perito."),

    ("Arguir suspeição do perito suspende o prazo de 15 dias para me manifestar sobre o laudo?",
     "Não suspende. O art. 148, §2º, é expresso: o juiz manda processar o incidente “em separado e "
     "sem suspensão do processo”, ouvindo o arguido em 15 dias. Os 15 dias comuns do art. 477, §1º, "
     "seguem correndo, e a manifestação com o parecer do assistente técnico continua sendo a via "
     "principal. Na prática, as duas coisas andam juntas e em peças separadas: a crítica técnica ao "
     "laudo nos autos principais, a arguição em petição autuada em apartado. Quem aposta tudo na "
     "arguição e deixa vencer a manifestação perde a via principal e fica com um incidente que, "
     "mesmo vencido, só produz a nomeação de novo perito (art. 467, parágrafo único) — não corrige "
     "o defeito técnico do laudo que já está nos autos."),
]
