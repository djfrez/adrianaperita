# -*- coding: utf-8 -*-
"""SEO-067 — conteúdo da seção `#metanol` em `/pericia-combustiveis/`.

Proveniência (conferida na execução de 2026-09-26, nada de memória):

- Resolução ANP nº 807/2020 (gasolina), texto do DOU (in.gov.br), baixado:
  Tabela 1 — "Teor de Metanol, máx (18)(19) | % volume | 0,5 | 16041";
  nota (18) "Proibida a adição. Devem ser medidos quando houver dúvida quanto
  à ocorrência de contaminação."; nota (19) — ISO 1388-8; mudança de
  coloração "ou ainda a obtenção de resultados inconclusivos, exige a
  confirmação pelo método cromatográfico ABNT NBR 16041"; art. 9º, § 1º, I —
  boletim do distribuidor traz "indicação de que o teor de metanol no etanol
  anidro está abaixo ou igual a 0,5%". A Resolução ANP nº 988/2025 (E30)
  alterou a 807 sem tocar o metanol (nota da ANP de 08/09/2025, conferida).
- Resolução ANP nº 907/2022 (etanol), cópia do DOU em PDF, baixada: teor de
  metanol máx. 0,5 % volume para EAC e EHC, métodos 16041 e 16943; notas
  (17) "Proibida a adição", (18)/(19) ISO 1388-8 com confirmação por NBR
  16041, (20) campo "Resultado" em branco + declaração com responsabilidade,
  (21) NBR 16943 só até 1,50 % em volume de metanol.
- Página "Metanol" da ANP (gov.br): 0,5 % nos dois combustíveis; 807/2020,
  907/2022 e Resolução ANP nº 697/2017 como regulação do próprio metanol;
  motivo: "toxicidade do produto, seu potencial como adulterador do etanol
  combustível e da gasolina".
- Teste da proveta × metanol: Teixeira, Almeida e Vitor Sobrinho (UNIFACS),
  "Adição ilegal de metanol na gasolina automotiva: impactos nas análises de
  qualidade", 1º Congresso Brasileiro de P&D em Petróleo e Gás, Natal, 2001
  (PDF baixado) — a proveta (NBR 13992) extrai o álcool em água, o metanol é
  extraído junto, e a troca parcial de etanol por metanol com teor alcoólico
  mantido não é detectada.

O que NÃO se afirma, por decisão:
- nenhum valor de massa específica — "muito próxima" é qualitativo de
  propósito; não se leu tabela de propriedade nesta execução;
- nenhuma técnica analítica da NBR 16943 (norma paga, não lida): só o que a
  nota (21) da 907 diz dela;
- nada sobre operações policiais, toxicologia clínica ou dano a motor por
  metanol — fora do que a fonte baixada sustenta.
"""

# (método, o que faz, o que o resultado sustenta)
METODOS = [
    ("Teste da proveta (ABNT NBR 13992)",
     "Extrai o álcool da gasolina com água e lê o volume da fase aquosa",
     "Nada sobre metanol: metanol e etanol são extraídos juntos e lidos como "
     "um só teor"),
    ("Triagem colorimétrica (base ISO 1388-8)",
     "Indica a presença de metanol por mudança de coloração no tubo de ensaio",
     "Indício, não número: as duas resoluções exigem confirmação pelo método "
     "cromatográfico ABNT NBR 16041 quando a cor muda — e, na gasolina, também "
     "quando o resultado é inconclusivo"),
    ("Cromatografia gasosa (ABNT NBR 16041)",
     "Separa e quantifica metanol e etanol na amostra",
     "É o método de confirmação indicado nas duas resoluções; é sobre ele que "
     "um teor de metanol se sustenta"),
    ("ABNT NBR 16943",
     "Método alternativo que a Resolução ANP nº 907/2022 admite para o etanol "
     "combustível",
     "Vale só para amostras com até 1,50% em volume de metanol: um resultado "
     "acima disso está fora do escopo do próprio método"),
]

# (pergunta, resposta) — entram antes da FAQ de intake, visível e JSON-LD
FAQS = [
    ("O teste da proveta detecta metanol na gasolina?",
     "Não. O teste da proveta (ABNT NBR 13992) extrai o álcool da gasolina com "
     "água e mede o volume da fase aquosa; o metanol é extraído pela água do "
     "mesmo modo que o etanol, e o ensaio lê os dois como um só teor. Uma "
     "gasolina em que parte do etanol foi trocada por metanol, mantido o teor "
     "alcoólico total, passa pelo teste com resultado normal. Para metanol, as "
     "resoluções da ANP indicam triagem colorimétrica com base na ISO 1388-8 e "
     "confirmação por cromatografia gasosa, pelo método ABNT NBR 16041."),
    ("Qual é o limite de metanol na gasolina e no etanol combustível?",
     "0,5% em volume nos dois: na gasolina, pela Resolução ANP nº 807/2020; no "
     "etanol anidro e no hidratado, pela Resolução ANP nº 907/2022. Nas duas "
     "resoluções a nota do parâmetro diz “proibida a adição”: o limite "
     "acomoda contaminação involuntária, não autoriza mistura. Um teor acima de "
     "0,5% só se sustenta se confirmado pelo método cromatográfico ABNT NBR "
     "16041; triagem colorimétrica, sozinha, é indício."),
]
