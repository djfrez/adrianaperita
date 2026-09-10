# -*- coding: utf-8 -*-
"""SEO-050 — o vocabulário de *desfazer* o laudo, que o site nunca escreveu.

Por que este arquivo existe (GSC, 28 dias findos em 09/09/2026):

    /impugnacao-laudo-pericial/ ....... 93 impressões · pos 12,1 · 0 cliques

É a página livre de janela de medição com mais impressões e a de maior
intenção comercial do domínio — quem tem um laudo desfavorável e prazo
correndo é exatamente o cliente da assistência técnica. Suas consultas
nominais estão entre 26 e 47 (`impugnação ao laudo pericial` 26,8 ·
`impugnação de laudo pericial` 44,0 · `impugnar laudo pericial` 47,0).

O achado que escolheu o conteúdo é o mesmo método das SEO-044/048/049 —
responder no vocabulário que o usuário digita — medido por script sobre as
21 páginas do site:

    "nulidade do laudo" ... 0 ocorrências     "anular" ......... 0
    "laudo nulo" ......... 0                  "recorrer" ....... 0
    "invalidar" .......... 0                  "revisão do laudo" 0

Ou seja: todo o vocabulário de *desfazer* o laudo — que é como a parte
descreve o que quer — estava ausente do site inteiro.

Fontes primárias abertas nesta execução (texto compilado do Planalto,
todas as ocorrências extraídas e a última escolhida — regra 8 do handoff):

  - CPC/2015, Título III (Das Nulidades), arts. 276, 277, 278, 282 e 283.
  - CPC/2015, arts. 466, §2º; 474; 477, §§1º e 2º; 479; 480, §3º.
  - CPC/2015, arts. 1.015 (caput e 13 incisos) e 1.009, §1º.
  - STJ, Tema 988 — REsp 1.704.520/MT, Corte Especial, Rel. Min. Nancy
    Andrighi, DJe 19/12/2018 (tese transcrita literalmente).

Regra 11 do backlog: visível e JSON-LD saem DAQUI, uma vez só.
"""

# Contagens conferidas no texto do Planalto nesta execução. O verificador as
# reconta na fonte: número afirmado no texto é afirmação verificável.
CPC_AUSENTES = ("nulidade do laudo", "laudo nulo")   # 0 ocorrências cada
ROL_1015_INCISOS = 13          # I a XIII, com o XII vetado
ROL_1015_VETADO = "XII"

# --------------------------------------------------------------------------
# Tabela 1 — o decodificador: como se digita → o que o Código oferece
# (como se digita, o que existe no CPC, o que se obtém, onde)
# --------------------------------------------------------------------------

VOCABULARIO = [
    ("“anular o laudo”, “laudo nulo”",
     "Nulidade do <strong>ato processual</strong>, não do documento. O Título III do CPC trata de atos: ao pronunciar a nulidade, o juiz declara que atos são atingidos e ordena que sejam repetidos ou retificados.",
     "A repetição do ato viciado — e só quando a parte tiver sido prejudicada.",
     "Arts. 276 a 283"),
    ("“impugnar o laudo”, “contestar o laudo”",
     "<strong>Manifestação sobre o laudo</strong>, em prazo comum de 15 dias, na qual o assistente técnico da parte apresenta o seu parecer.",
     "A crítica técnica nos autos, antes da sentença. É a via principal.",
     "Art. 477, §1º"),
    ("“recorrer do laudo”",
     "Não existe. Laudo é <strong>prova</strong>, não é decisão — não há recurso contra prova. Recorre-se da <em>decisão</em> que indefere os esclarecimentos ou a nova perícia.",
     "Em regra, preliminar de apelação: essa decisão não está no rol do agravo de instrumento.",
     "Art. 1.009, §1º"),
    ("“refazer a perícia”, “segunda perícia”",
     "<strong>Nova perícia</strong>, quando a matéria não ficar suficientemente esclarecida.",
     "Um segundo laudo <em>ao lado</em> do primeiro — que ele não substitui.",
     "Art. 480, §3º"),
    ("“perícia complementar”",
     "<strong>Esclarecimentos do perito</strong> sobre ponto obscuro ou divergente apontado pela parte, pelo juiz, pelo Ministério Público ou pelo parecer do assistente.",
     "A complementação do laudo já produzido, em 15 dias.",
     "Art. 477, §2º"),
    ("“desconsiderar o laudo”",
     "<strong>Apreciação motivada</strong> da prova pericial pelo juiz, levando em conta o método utilizado pelo perito.",
     "Sentença que diz por que deixou de considerar as conclusões do laudo. Não é nulidade — e é o desfecho mais comum de uma crítica técnica bem-sucedida.",
     "Art. 479"),
]

# --------------------------------------------------------------------------
# Tabela 2 — as cinco exigências da nulidade (o que provar, o que a lei diz, onde)
# Os textos da coluna do meio são transcrição literal do CPC: o verificador
# confere cada célula contra a fonte.
# --------------------------------------------------------------------------

EXIGENCIAS = [
    ("Forma prescrita em lei, e finalidade não alcançada",
     "Quando a lei prescrever determinada forma, o juiz considerará válido o ato se, realizado de outro modo, lhe alcançar a finalidade.",
     "Art. 277"),
    ("Prejuízo concreto para quem alega",
     "O ato não será repetido nem sua falta será suprida quando não prejudicar a parte.",
     "Art. 282, §1º"),
    ("Alegação na primeira oportunidade",
     "A nulidade dos atos deve ser alegada na primeira oportunidade em que couber à parte falar nos autos, sob pena de preclusão.",
     "Art. 278"),
    ("Não ter sido a própria parte a causar o vício",
     "Quando a lei prescrever determinada forma sob pena de nulidade, a decretação desta não pode ser requerida pela parte que lhe deu causa.",
     "Art. 276"),
    ("Que o ato não seja aproveitável",
     "Dar-se-á o aproveitamento dos atos praticados desde que não resulte prejuízo à defesa de qualquer parte.",
     "Art. 283, parágrafo único"),
]

# Transcrições literais usadas fora das tabelas — todas reconferidas na fonte.
ART_466_2 = ("O perito deve assegurar aos assistentes das partes o acesso e o acompanhamento das "
             "diligências e dos exames que realizar, com prévia comunicação, comprovada nos autos, "
             "com antecedência mínima de 5 (cinco) dias.")
ART_474 = ("As partes terão ciência da data e do local designados pelo juiz ou indicados pelo perito "
           "para ter início a produção da prova.")
ART_282 = ("Ao pronunciar a nulidade, o juiz declarará que atos são atingidos e ordenará as "
           "providências necessárias a fim de que sejam repetidos ou retificados.")
ART_1009_1 = ("As questões resolvidas na fase de conhecimento, se a decisão a seu respeito não "
              "comportar agravo de instrumento, não são cobertas pela preclusão e devem ser "
              "suscitadas em preliminar de apelação, eventualmente interposta contra a decisão "
              "final, ou nas contrarrazões.")

# STJ, Tema 988 — tese transcrita literalmente.
TEMA_988 = ("O rol do art. 1.015 do CPC é de taxatividade mitigada, por isso admite a interposição "
            "de agravo de instrumento quando verificada a urgência decorrente da inutilidade do "
            "julgamento da questão no recurso de apelação.")
TEMA_988_FONTE = "STJ, REsp 1.704.520/MT, Corte Especial, Rel. Min. Nancy Andrighi, DJe 19/12/2018"

# --------------------------------------------------------------------------
# FAQ — uma entrada. Fonte única das duas pontas (visível e JSON-LD).
# --------------------------------------------------------------------------

QUESTION = "Dá para anular um laudo pericial?"
ANSWER = (
    "Não com esse nome. A expressão “nulidade do laudo” não aparece nenhuma vez no CPC/2015: o "
    "Título III trata da nulidade de <em>atos processuais</em> (arts. 276 a 283), e o juiz, ao "
    "pronunciá-la, declara que atos são atingidos e ordena que sejam repetidos ou retificados "
    "(art. 282). Aplicado à perícia, isso exige, cumulativamente: um vício de forma "
    "prescrita em lei — o caso típico é a diligência realizada sem a comunicação prévia de cinco "
    "dias ao assistente técnico da parte, exigida pelo art. 466, §2º —, prejuízo demonstrado "
    "(art. 282, §1º) e alegação na primeira oportunidade em que couber falar nos autos, sob pena "
    "de preclusão (art. 278). Erro de método não é nulidade: é matéria de crítica técnica na "
    "manifestação do art. 477, §1º e de apreciação motivada do juiz na sentença (art. 479)."
)
