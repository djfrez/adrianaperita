# -*- coding: utf-8 -*-
"""SEO-068 — conteúdo da seção `#juizado` em `/dano-motor-combustivel/`.

Proveniência (conferida na execução de 2026-09-27, nada de memória):

- Lei nº 9.099/1995, texto compilado do Planalto (l9099.htm), baixado; cada
  dispositivo aparece uma única vez no texto:
  art. 3º, I (até quarenta vezes o salário mínimo) e § 3º (renúncia ao
  excedente, salvo conciliação); art. 9º (até vinte salários mínimos, parte
  pode comparecer sem advogado); art. 33 (todas as provas na audiência de
  instrução e julgamento); art. 35 e parágrafo único (técnicos de confiança do
  juiz, "permitida às partes a apresentação de parecer técnico", inspeção
  relatada informalmente); art. 51, II (extinção quando inadmissível o
  procedimento); art. 54 (sem custas em primeiro grau).
- Enunciados cíveis do FONAJE, página do CNJ (o site do FONAJE/AMB bloqueia
  acesso automatizado por Cloudflare): Enunciado 12 ("A perícia informal é
  admissível na hipótese do art. 35 da Lei 9.099/1995") e Enunciado 54 ("A
  menor complexidade da causa para a fixação da competência é aferida pelo
  objeto da prova e não em face do direito material").
- CPC: arts. 82, 95, 465 e 477, § 1º — já conferidos no Planalto nas SEO-048
  e SEO-051 e citados no site desde então.

O que NÃO se afirma, por decisão:
- nenhum valor em reais do salário mínimo nem do teto do Juizado — não se
  conferiu o salário mínimo vigente nesta execução, e o número envelhece todo
  janeiro;
- nenhuma jurisprudência (STJ, turmas recursais) sobre complexidade de causa
  de combustível — não se leu acórdão;
- nada sobre advogado obrigatório na justiça comum (art. 103 do CPC não foi
  conferido nesta execução);
- que a produção antecipada de prova caiba no Juizado — a Lei nº 9.099/1995
  não a prevê e isso não foi verificado; a página só a associa à vara cível.
"""

# (dimensão, Juizado Especial Cível, vara cível)
QUADRO = [
    ("Limite de valor",
     "Até quarenta salários mínimos; quem opta pelo Juizado renuncia ao que "
     "exceder, salvo conciliação (art. 3º, I e § 3º)",
     "Sem limite de valor"),
    ("Custas",
     "Não há custas em primeiro grau (art. 54)",
     "Custas e honorários do perito adiantados na forma do CPC (arts. 82 e 95)"),
    ("Prova técnica",
     "Técnico de confiança do juiz, inspeção relatada informalmente e parecer "
     "técnico das partes (art. 35)",
     "Perícia com perito nomeado, quesitos e assistentes técnicos (art. 465)"),
    ("Quando a prova é produzida",
     "Na audiência de instrução e julgamento (art. 33)",
     "Em fase própria, com laudo e prazo comum de 15 dias para as partes se "
     "manifestarem (art. 477, § 1º)"),
    ("Risco próprio do rito",
     "Extinção sem julgamento de mérito se a prova exigir perícia que o rito "
     "não comporta (art. 51, II; Enunciado 54 do FONAJE)",
     "Tempo e custo da perícia formal"),
]

# (pergunta, resposta) — entram antes da FAQ de intake, visível e JSON-LD
FAQS = [
    ("Ação contra posto por dano ao motor pode ir para o Juizado Especial Cível?",
     "Pode, se o valor couber no limite de quarenta salários mínimos (art. 3º, I, "
     "da Lei nº 9.099/1995) e se a prova não for complexa. O Enunciado 54 do "
     "FONAJE mede a complexidade pelo objeto da prova, não pelo direito material: "
     "se a causa exige perícia que o rito do Juizado não comporta, o processo é "
     "extinto sem julgamento de mérito (art. 51, II). No Juizado, a prova técnica "
     "entra por parecer técnico das partes e por técnico de confiança do juiz "
     "(art. 35) e é produzida na audiência de instrução e julgamento (art. 33): "
     "a análise da amostra e o exame das peças precisam chegar prontos."),
    ("Parecer técnico particular vale como prova no Juizado Especial?",
     "Vale. O art. 35 da Lei nº 9.099/1995 permite expressamente às partes a "
     "apresentação de parecer técnico, ao lado da inquirição de técnicos de "
     "confiança do juiz, e o Enunciado 12 do FONAJE admite a perícia informal "
     "nessa hipótese. O parecer pesa mais quando mostra como a amostra foi "
     "coletada e guardada, qual método produziu cada resultado e por que o "
     "mecanismo de dano é compatível com a avaria encontrada nas peças — porque "
     "é isso que o técnico do juiz vai conferir."),
]
