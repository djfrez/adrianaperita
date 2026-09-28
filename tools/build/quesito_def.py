# -*- coding: utf-8 -*-
"""SEO-069 — conteúdo da seção `#o-que-e-quesito` em `/quesitos-periciais/`.

Proveniência (conferida na execução de 2026-09-28, nada de memória):

- CPC/2015, texto compilado do Planalto (l13105.htm), baixado, trechos
  tachados removidos; cada dispositivo ocorre uma única vez:
  art. 465, § 1º, III (partes apresentam quesitos em 15 dias da intimação da
  nomeação); art. 469 (quesitos suplementares durante a diligência); art. 470,
  I e II (juiz indefere impertinentes e formula os que entender necessários);
  art. 473, IV (resposta conclusiva a todos os quesitos do juiz, das partes e do
  Ministério Público); art. 477, § 3º (perguntas ao perito na audiência
  formuladas "sob forma de quesitos"); art. 361, I (perito e assistentes
  respondem na audiência aos quesitos de esclarecimentos, se não respondidos
  por escrito).
- CPP, texto compilado do Planalto (del3689.htm), baixado:
  art. 160 (o laudo descreve o exame e responde aos quesitos formulados);
  art. 159, § 3º (MP, assistente de acusação, ofendido, querelante e acusado
  podem formular quesitos e indicar assistente técnico); art. 176 (quesitos
  "até o ato da diligência"); art. 482, caput e parágrafo único (Conselho de
  Sentença questionado sobre matéria de fato e absolvição; quesitos em
  proposições afirmativas, simples e distintas); art. 483, I a III (ordem:
  materialidade, autoria ou participação, se o acusado deve ser absolvido).

O que NÃO se afirma, por decisão:
- nenhuma etimologia de "quesito" — não se conferiu dicionário nesta execução;
- "quesitação" é tratada como uso forense (o ato de formular quesitos e o
  conjunto deles), não como termo legal: a palavra não ocorre nem no CPC nem no
  CPP (contagem 0 nos dois textos baixados);
- nada sobre quesitos na Justiça do Trabalho (CLT não conferida) nem sobre o
  procedimento do art. 483, §§ 1º a 5º, do CPP além da ordem dos incisos I–III;
- nenhum número de quesitos "ideal" além do que a página já dizia.
"""

# (figura, quem formula e quando, o que a lei exige da resposta)
QUADRO = [
    ("Quesito da perícia cível",
     "As partes, em 15 dias da intimação da nomeação do perito (art. 465, § 1º, III); "
     "o juiz, quando entender necessário (art. 470, II); durante a diligência, como "
     "quesito suplementar (art. 469)",
     "Resposta conclusiva no laudo (art. 473, IV); o juiz indefere o impertinente "
     "(art. 470, I)"),
    ("Quesito de esclarecimento",
     "A parte, depois do laudo, ao requerer que o perito ou o assistente técnico "
     "compareça à audiência, formulando desde logo as perguntas “sob forma de "
     "quesitos” (art. 477, § 3º)",
     "Resposta na audiência de instrução e julgamento, se não dada antes por "
     "escrito (art. 361, I)"),
    ("Quesito da perícia criminal",
     "Ministério Público, assistente de acusação, ofendido, querelante e acusado "
     "(CPP, art. 159, § 3º), até o ato da diligência (CPP, art. 176)",
     "O laudo descreve o que foi examinado e responde aos quesitos formulados "
     "(CPP, art. 160)"),
    ("Quesito do Tribunal do Júri",
     "O juiz presidente, dirigido aos jurados — não ao perito (CPP, art. 482)",
     "Proposições afirmativas, simples e distintas, na ordem legal: materialidade, "
     "autoria ou participação, e se o acusado deve ser absolvido (CPP, art. 483)"),
]

DEFINICAO = (
    "<strong>Quesito é a pergunta escrita dirigida ao perito que delimita o que a perícia "
    "deve examinar — e que ele é obrigado a responder de forma conclusiva no laudo</strong> "
    "(art. 473, IV, do CPC). Formulam quesitos as partes (art. 465, § 1º, III), o juiz "
    "(art. 470, II) e o Ministério Público. Na linguagem forense, <em>quesitação</em> é o "
    "ato de formular os quesitos e, por extensão, o conjunto deles; a palavra não aparece "
    "no CPC nem no CPP, que falam apenas em quesitos."
)

FAQS = [
    ("O que é quesito em uma perícia judicial?",
     "É a pergunta escrita dirigida ao perito que delimita o que a perícia deve examinar. "
     "O art. 473, IV, do CPC obriga o laudo a conter resposta conclusiva a todos os "
     "quesitos apresentados pelo juiz, pelas partes e pelo Ministério Público — por isso "
     "o quesito funciona como uma obrigação de resposta registrada nos autos. As partes "
     "apresentam quesitos em 15 dias da intimação da nomeação do perito (art. 465, § 1º, "
     "III), o juiz pode formular os que entender necessários e deve indeferir os "
     "impertinentes (art. 470). Quesitação é o nome que a prática forense dá ao ato de "
     "formulá-los e ao conjunto deles."),
    ("Quesito do Tribunal do Júri é a mesma coisa que quesito de perícia?",
     "Não. No Júri, o quesito é dirigido aos jurados, não ao perito: o Conselho de "
     "Sentença é questionado sobre matéria de fato e sobre se o acusado deve ser "
     "absolvido (art. 482 do CPP), em proposições afirmativas, simples e distintas, na "
     "ordem do art. 483 — materialidade, autoria ou participação e absolvição. O quesito "
     "de perícia é pergunta técnica ao perito, no processo civil (arts. 465, 469 e 470 do "
     "CPC) ou no processo penal (arts. 159, § 3º, e 176 do CPP). A palavra é a mesma; a "
     "função é outra."),
]
