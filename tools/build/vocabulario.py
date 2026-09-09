# -*- coding: utf-8 -*-
"""Fonte única da SEO-049 — o vocabulário de papéis na prova pericial.

Por que esta página precisa disto: o Search Console mostra 15 consultas nominais
para `/assistente-tecnica/` entre as posições 25 e 50, e três delas usam um termo
que **não existe em lei nenhuma**: `perito assistente` (3 impressões, pos 33,3),
`perito assistente técnico` (pos 25,0) e `o papel do perito judicial e do perito
assistente técnico` (pos 27,0). O site nunca escreveu essa expressão — zero
ocorrências nas 21 páginas. É o mesmo achado que rendeu a melhor consulta do
domínio na SEO-044/048: **o usuário digita um vocabulário que a norma não usa.**

Todos os números afirmados aqui são verificáveis contra o texto compilado do
Planalto, e o verificador (`tools/verify-vocabulario.py`) os reconta na fonte em
vez de confiar neste arquivo. Contagem feita em 08/09/2026:

    CPC/2015   "assistente técnico(s)"  15 ocorrências, em 9 artigos
               "perito judicial"         1 ocorrência  (art. 468, §2º)
               "perito do juízo"         2
               "perito assistente"       0
               "perito oficial"          0
               "consultor técnico"       0
    CPP        "assistente técnico(s)"   6
               "perito assistente"       0
               "perito oficial"          6 (+5 no plural)
               "perito judicial"         0
"""

# Contagens verificadas em fonte primária. O verificador reconta.
CPC_AT_OCORRENCIAS = 15
CPC_AT_ARTIGOS = [84, 95, 361, 465, 466, 471, 473, 475, 477]

# Termo digitado → (está na lei?, termo correto, onde)
VOCABULARIO = [
    ("perito assistente",
     "Não — nenhuma ocorrência, nem no CPC nem no CPP",
     "assistente técnico",
     "art. 466, §1º"),
    ("perito da parte",
     "Não",
     "assistente técnico",
     "art. 465, §1º, II"),
    ("assistente técnico",
     f"Sim — {CPC_AT_OCORRENCIAS} ocorrências, em {len(CPC_AT_ARTIGOS)} artigos",
     "assistente técnico",
     "arts. " + ", ".join(str(a) for a in CPC_AT_ARTIGOS[:-1]) + f" e {CPC_AT_ARTIGOS[-1]}"),
    ("perito judicial",
     "Uma única vez em todo o CPC — e para punir",
     "perito, ou perito do juízo",
     "art. 468, §2º (a única); art. 477, §1º"),
    ("perito oficial",
     "Não no CPC — é vocabulário do processo penal",
     "perito nomeado pelo juízo",
     "CPP, art. 159"),
    ("consultor técnico",
     "Não — nenhuma ocorrência",
     "assistente técnico, quando a atuação é no processo",
     "—"),
]

# Dimensão → (processo civil, processo penal)
CIVIL_PENAL = [
    ("Como entra no processo",
     "Indicação da parte, em 15 dias contados da intimação do despacho de nomeação do perito "
     "(art. 465, §1º, II). Não depende de deferimento.",
     "Indicação é facultada às partes (art. 159, §3º), mas o assistente só atua "
     "<strong>a partir de sua admissão pelo juiz</strong> (art. 159, §4º)."),
    ("Quando pode atuar",
     "Acompanha a perícia: o perito deve assegurar acesso às diligências e aos exames, com "
     "comunicação prévia de 5 dias (art. 466, §2º).",
     "Somente <strong>após a conclusão dos exames e a elaboração do laudo</strong> pelos peritos "
     "oficiais (art. 159, §4º)."),
    ("Imparcialidade",
     "É de confiança da parte e não está sujeito a impedimento ou suspeição (art. 466, §1º).",
     "O CPP não repete a regra; a admissão pelo juiz é que filtra a atuação."),
    ("Entregável",
     "Parecer, no prazo comum de 15 dias contados da intimação sobre o laudo (art. 477, §1º).",
     "Parecer em prazo fixado pelo juiz, ou inquirição em audiência (art. 159, §5º, II)."),
    ("Perícia complexa",
     "A parte pode indicar mais de um assistente técnico (art. 475).",
     "A parte pode indicar mais de um assistente técnico (art. 159, §7º)."),
]

QUESTION = "Perito assistente e assistente técnico são a mesma coisa?"

ANSWER = (
    "São o mesmo profissional, mas só um dos dois nomes está na lei. A expressão "
    "<strong>“perito assistente” não aparece nenhuma vez no CPC/2015 nem no Código de Processo "
    "Penal</strong>: é hibridismo do uso corrente, que cola o “perito” do juízo ao “assistente” da "
    f"parte. O termo do Código é <strong>assistente técnico</strong>, com {CPC_AT_OCORRENCIAS} "
    f"ocorrências distribuídas por {len(CPC_AT_ARTIGOS)} artigos — "
    + ", ".join(str(a) for a in CPC_AT_ARTIGOS[:-1]) + f" e {CPC_AT_ARTIGOS[-1]}. "
    "Curiosamente, “perito judicial” também é termo do uso e não do Código: aparece uma única vez "
    "no CPC, no art. 468, §2º, e apenas para dizer que o perito substituído que não devolve os "
    "valores recebidos fica impedido de atuar como perito judicial por cinco anos. Na petição e nos "
    "quesitos, vale escrever “assistente técnico” — é o termo que a lei usa e que os sistemas dos "
    "tribunais indexam."
)
