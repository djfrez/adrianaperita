# -*- coding: utf-8 -*-
"""SEO-071 — conteúdo da seção `#producao-antecipada` em
`/analise-microbiologica-alimentos/`.

Proveniência (conferida na execução de 2026-09-30, nada de memória):

- CPC/2015, texto compilado do Planalto (l13105.htm), baixado nesta execução
  (latin-1). Cada dispositivo aparece uma única vez no texto:
  art. 381 caput e incisos I, II e III; art. 381, §§ 1º a 5º; art. 382 caput
  e §§ 1º a 4º.
- A página já trata o rito administrativo da Lei nº 6.437/1977, art. 27, na
  seção `#uma-so-chance` (SEO-040). Esta seção NÃO reabre esse artigo: só o
  contrapõe ao caminho judicial do art. 381, e a guarda de ausência de
  "6.437" / "art. 27" no corpo da seção nova garante que não se misturam.

O que NÃO se afirma, por decisão:
- nenhum prazo de holding time / preservação de amostra (Guia Nacional de
  Coleta e Preservação de Amostras não foi aberto nesta execução);
- nenhuma frequência estatística de uso da medida em microbiologia;
- nenhum valor, honorário ou prazo de resposta;
- que a produção antecipada caiba no Juizado Especial — não verificado aqui
  (ver juizado.py / SEO-068);
- nada sobre ISO 6579, ISO 11290 ou métodos específicos além do que a página
  já sustenta via art. 9º da RDC nº 724/2022.
"""

# (inciso, o que o art. 381 exige, situação microbiológica típica)
QUADRO = [
    ("I — urgência",
     "Fundado receio de que a verificação dos fatos se torne impossível ou "
     "muito difícil na pendência da ação",
     "Lote que será consumido, vencido, descartado ou misturado; amostra cuja "
     "população microbiana muda com tempo e temperatura"),
    ("II — autocomposição",
     "A prova ser suscetível de viabilizar a autocomposição ou outro meio "
     "adequado de solução de conflito",
     "Exame prévio que dá base comum para recall, indenização ou acordo "
     "antes do processo"),
    ("III — decidir se litiga",
     "O prévio conhecimento dos fatos poder justificar ou evitar o "
     "ajuizamento da ação",
     "Saber se o lote descumpre o padrão da IN nº 161/2022 — e em qual "
     "classificação do art. 11 da RDC nº 724/2022 — antes de ajuizar"),
]

# (pergunta, resposta) — entram antes da FAQ de intake, visível e JSON-LD
FAQS = [
    ("Quando cabe produção antecipada de prova em disputa microbiológica de alimento?",
     "Cabe quando o exame precisa ocorrer enquanto o lote ou a amostra ainda "
     "existem nas condições do fato. O art. 381 do CPC admite a medida em três "
     "hipóteses independentes: receio de impossibilidade ou dificuldade na "
     "pendência da ação (I); viabilizar autocomposição (II); ou justificar ou "
     "evitar o ajuizamento (III). Em microbiologia o inciso I é o mais "
     "frequente — a população microbiana muda com tempo e temperatura, e o "
     "reexame tardio não reproduz a condição original —, mas os incisos II e "
     "III também cabem e não exigem urgência. O art. 382 exige que a petição "
     "mencione com precisão os fatos sobre os quais a prova há de recair: "
     "matriz, lote, parâmetros da IN nº 161/2022 e o n do plano. O rito "
     "completo está em produção antecipada de prova pericial."),
]
