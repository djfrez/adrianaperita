# -*- coding: utf-8 -*-
"""Fonte única da SEO-056 — `/assistente-tecnica/#quem-pode`.

A consulta que escolheu esta execução é `quem pode ser assistente técnico em
perícia`, **posição 61** — a pior posição nomeada de todo o domínio, na página
que deveria ser dona dela. O `grep` confirmou o buraco: "quem pode ser" não
aparecia nenhuma vez em `/assistente-tecnica/`.

O achado que sustenta a seção, e que é o oposto do que quase todo texto
concorrente dá a entender: **o CPC não impõe nenhum requisito de qualificação
ao assistente técnico.** Todos os requisitos de habilitação do Código são
endereçados ao *perito* — cadastro do tribunal (art. 156, §1º) e currículo com
comprovação de especialização (art. 465, §2º, II). Ao assistente o Código só
diz que é "de confiança da parte" e que não se sujeita a impedimento ou
suspeição (art. 466, §1º).

Isso **não** significa que qualquer pessoa assine um parecer útil: o limite
existe, só não está no CPC. Está na legislação da profissão — para a Química,
no Decreto nº 85.877/1981, que põe a perícia e o parecer técnico entre as
atividades do químico (art. 1º, VI) e, nos termos do art. 2º, IV, "g", entre os
privativos; e reserva o estudo, o planejamento e o projeto de equipamentos e
instalações industriais a quem tem currículo de Engenharia Química (art. 3º).

Todo número e toda transcrição abaixo são reconferidos no Planalto por
`tools/verify-elegibilidade.py`. Número afirmado no texto é afirmação
verificável.
"""

# Ocorrências de "assistente(s) técnico(s)" no CPC/2015 — recontadas na fonte.
# Herdado da SEO-049 e reconfirmado em 15/09/2026 com o mesmo fold que preserva
# comprimento (o fold NFKD+ascii encurta a string e faz o offset derivar).
CPC_AT_OCORRENCIAS = 15
CPC_AT_ARTIGOS = [84, 95, 361, 465, 466, 471, 473, 475, 477]

# Exigência · perito do juízo · assistente técnico · onde
EXIGENCIAS = [
    ("Como entra no processo",
     "Nomeado pelo juiz, especializado no objeto da perícia.",
     "Indicado pela parte, dentro de 15 dias contados da intimação do despacho de nomeação.",
     "arts. 465, <em>caput</em>, e 465, §1º, II"),
    ("Inscrição em cadastro do tribunal",
     "Sim — os peritos são nomeados entre os profissionais legalmente habilitados e os órgãos técnicos ou científicos inscritos em cadastro mantido pelo tribunal.",
     "<strong>O Código não exige.</strong>",
     "art. 156, §1º"),
    ("Currículo com comprovação de especialização",
     "Sim — apresentado em 5 dias da ciência da nomeação, junto com a proposta de honorários.",
     "<strong>O Código não exige.</strong>",
     "art. 465, §2º, II"),
    ("Impedimento e suspeição",
     "Sujeito: pode escusar-se ou ser recusado por impedimento ou suspeição.",
     "<strong>Não está sujeito</strong> — é de confiança da parte.",
     "arts. 467 e 466, §1º"),
    ("Termo de compromisso",
     "Cumpre o encargo escrupulosamente, independentemente de termo de compromisso.",
     "Não há termo de compromisso a prestar.",
     "art. 466, <em>caput</em>"),
    ("Quem adianta a remuneração",
     "A parte que requereu a perícia, ou rateada quando determinada de ofício ou requerida por ambas.",
     "Cada parte adianta a do assistente que indicou.",
     "art. 95, <em>caput</em>"),
    ("Mais de um profissional",
     "Em perícia complexa que abranja mais de uma área de conhecimento especializado, o juiz pode nomear mais de um perito.",
     "Na mesma hipótese, a parte pode indicar mais de um assistente técnico.",
     "art. 475"),
]

# Trechos que o verificador cobra, literais, no texto do Planalto.
FONTE_CPC = {
    "art. 156, §1º": "Os peritos serão nomeados entre os profissionais legalmente habilitados e os órgãos técnicos ou científicos devidamente inscritos em cadastro mantido pelo tribunal",
    "art. 465, §1º, II": "Incumbe às partes, dentro de 15 (quinze) dias contados da intimação do despacho de nomeação do perito",
    "art. 465, §2º, II": "currículo, com comprovação de especialização",
    "art. 466, §1º": "Os assistentes técnicos são de confiança da parte e não estão sujeitos a impedimento ou suspeição",
    "art. 466, caput": "O perito cumprirá escrupulosamente o encargo que lhe foi cometido, independentemente de termo de compromisso",
    "art. 467": "O perito pode escusar-se ou ser recusado por impedimento ou suspeição",
    "art. 471, §1º": "As partes, ao escolher o perito, já devem indicar os respectivos assistentes técnicos para acompanhar a realização da perícia",
    "art. 475": "Tratando-se de perícia complexa que abranja mais de uma área de conhecimento especializado, o juiz poderá nomear mais de um perito, e a parte, indicar mais de um assistente técnico",
    "art. 95": "Cada parte adiantará a remuneração do assistente técnico que houver indicado",
    "art. 84": "As despesas abrangem as custas dos atos do processo, a indenização de viagem, a remuneração do assistente técnico e a diária de testemunha",
    "art. 465, §6º": "poder-se-á proceder à nomeação de perito e à indicação de assistentes técnicos no juízo ao qual se requisitar a perícia",
}

FONTE_DECRETO = {
    "art. 1º, VI": "vistoria, perícia, avaliação, arbitramento e serviços técnicos, elaboração de pareceres, laudos e atestados, no âmbito das respectivas atribuições",
    "art. 2º, IV, g": "pesquisa, estudo, planejamento, perícia, consultoria e apresentação de pareceres técnicos na área de Química",
    "art. 3º": "são privativas dos profissionais com currículo da Engenharia Química",
}

QUESTION = "Quem pode ser assistente técnico em perícia?"
ANSWER = (
    "O CPC não impõe nenhum requisito de qualificação ao assistente técnico. Os requisitos de "
    "habilitação do Código são todos endereçados ao perito do juízo: inscrição em cadastro mantido "
    "pelo tribunal (art. 156, §1º) e currículo com comprovação de especialização (art. 465, §2º, II). "
    "Sobre o assistente, o art. 466, §1º, diz apenas que é de confiança da parte e que não está "
    "sujeito a impedimento ou suspeição — pode, portanto, ter vínculo com quem o indicou. O limite "
    "real não está no processo, está na profissão: o parecer só tem peso se quem o assina tem "
    "atribuição legal para o ato técnico que pratica. Na área de Química, o Decreto nº 85.877/1981 "
    "põe a perícia e o parecer técnico entre as atividades do químico (art. 1º, VI) e, nos termos do "
    "art. 2º, IV, \"g\", entre os privativos, reservando ainda o estudo e o projeto de instalações "
    "industriais a quem tem currículo de Engenharia Química (art. 3º). Em perícia complexa que "
    "abranja mais de uma área, a parte pode indicar mais de um assistente técnico (art. 475)."
)
