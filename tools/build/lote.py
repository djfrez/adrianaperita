# -*- coding: utf-8 -*-
"""SEO-066 — conteúdo da seção `#lote-recusado` em `/pericia-industria-quimica/`.

Proveniência (conferida na execução de 2026-09-25, nada de memória):

- Código Civil (Lei nº 10.406/2002), texto compilado do Planalto, baixado:
  arts. 441, 442, 443, 445 (caput e § 1º) e 446 — uma única ocorrência de
  cada no arquivo. `verify-lote.py` rebaixa e procura as frases literais.
- ISO 5725: r = 2,8·σr e R = 2,8·σR (fator 1,96·√2 para a diferença de dois
  resultados, ~95 %); ISO 5725-6 — quando cada laboratório tem um único
  resultado, a diferença absoluta é comparada com R e, se não o excede, os
  resultados concordam e a média pode ser o resultado final. Conferido no
  resumo publicado da norma (a norma é paga; o texto integral não foi lido).

O que NÃO se afirma, por decisão:
- nenhum procedimento da ISO 5725-6 além da comparação com R (o que fazer
  quando a diferença excede R não foi lido na fonte — a página manda o
  contrato prever laboratório árbitro, que é recomendação, não citação);
- nenhum valor numérico de r ou R: eles são do método de ensaio, e a página
  manda lê-los na seção de precisão do próprio método;
- nenhuma tese de jurisprudência sobre CDC × Código Civil entre empresas —
  "costuma" é deliberado, e a qualificação jurídica fica com o advogado.
"""

# (situação, o que significa, consequência) — tabela de leitura da divergência
LEITURAS = [
    ("A diferença entre os dois resultados não excede R, e os dois estão dentro "
     "da especificação",
     "Não há divergência técnica: é a variação normal do método entre laboratórios",
     "Não há o que discutir sobre o lote"),
    ("A diferença não excede R, mas um resultado cai de cada lado do limite da "
     "especificação",
     "Os dois laboratórios trabalharam corretamente; o lote está perto do limite, "
     "e o método não consegue dizer de que lado",
     "A questão deixa de ser “quem errou” e passa a ser quem suporta o risco do "
     "resultado perto do limite — a regra de decisão, que é matéria de contrato"),
    ("A diferença excede R",
     "Há uma causa a encontrar: amostras diferentes (ponto de coleta, "
     "homogeneidade, degradação no transporte ou na armazenagem), padrão ou "
     "calibração, execução do método",
     "É aqui que a perícia trabalha: a pergunta é qual das duas amostras "
     "representa o lote entregue"),
    ("Os laboratórios usaram métodos diferentes",
     "O R de um método não se aplica à comparação com outro; os números não são "
     "diretamente comparáveis",
     "Antes de qualquer conclusão, saber se o contrato fixou o método — e, se "
     "fixou, qual dos dois resultados foi obtido fora dele"),
]

# Os quatro pontos do contrato (ponto, por que decide)
CONTRATO = [
    ("Método de ensaio nomeado, com a versão",
     "sem ele, cada laboratório escolhe o seu, e a comparação da tabela acima "
     "fica impossível"),
    ("Onde e como se amostra",
     "amostra coletada na expedição e amostra coletada no recebimento não "
     "representam o mesmo momento; o que acontece no caminho fica de fora de uma "
     "delas"),
    ("Amostra retida, lacrada, com quantidade e prazo de guarda",
     "é a única que permite repetir a análise depois que o lote foi consumido ou "
     "devolvido"),
    ("Laboratório árbitro, e quem paga",
     "escolhido antes da disputa, encerra a divergência sem processo; escolhido "
     "depois, vira mais uma divergência"),
]

FAQS = [
    ("O certificado de análise do fornecedor diz que o lote está conforme e o meu "
     "laboratório diz que não. Quem está certo?",
     "Possivelmente os dois. Dois laboratórios competentes, medindo o mesmo lote "
     "pelo mesmo método, não chegam ao mesmo número, e a própria norma do método "
     "diz quanto eles podem diferir: é o limite de reprodutibilidade, R, definido "
     "na série ISO 5725. Se a diferença entre os dois resultados não excede R, "
     "eles são compatíveis, e a média pode ser tomada como resultado. Se o lote "
     "está perto do limite da especificação, um resultado pode cair de cada lado "
     "sem que nenhum laboratório tenha errado — e a disputa passa a ser sobre "
     "quem suporta esse risco, o que se resolve pelo contrato. Só quando a "
     "diferença excede R há uma causa técnica a investigar, quase sempre na "
     "amostra e não no ensaio."),
    ("Qual o prazo para reclamar de um lote de produto químico fora de "
     "especificação comprado de outra empresa?",
     "Quando a disputa corre pelo Código Civil — o caso comum de insumo comprado "
     "para o processo produtivo —, o art. 445 fixa trinta dias da entrega efetiva "
     "para bem móvel, para rejeitar o lote ou pedir abatimento no preço. Se o "
     "vício, por sua natureza, só puder ser conhecido mais tarde, o prazo conta da "
     "ciência, até o máximo de cento e oitenta dias (art. 445, § 1º). Havendo "
     "cláusula de garantia, esses prazos não correm durante ela, mas o defeito "
     "tem de ser denunciado ao fornecedor nos trinta dias seguintes ao "
     "descobrimento, sob pena de decadência (art. 446). Em perícia, isso faz do "
     "laudo de recebimento um documento de data: ele diz quando o comprador "
     "soube, ou poderia ter sabido."),
]
