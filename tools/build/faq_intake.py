# -*- coding: utf-8 -*-
"""Entrada de FAQ "o que enviar no primeiro contato" (SEO-046).

Fonte única da pergunta e da resposta que passam a existir no `FAQPage` de cada
página de conteúdo. A lista de documentos NÃO é redigida aqui: vem de
`intake.py` (SEO-045), de modo que o bloco visível do `cta-sec` e a entrada de
FAQ nunca podem divergir — se um documento mudar lá, muda nos dois lugares.

Motivo do item (item 7 do handoff de 2026-09-04): a resposta a "o que eu mando"
já existia escrita e específica por matéria, mas em prosa dentro do CTA — fora
de `FAQPage`. É o formato que LLMs e AI Overviews citam, e era a oportunidade de
menor esforço e maior citabilidade disponível.
"""
import html as _html
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from intake import PAGES

# Fecho comum às 20 páginas — espelha o `CLOSE` do bloco de intake, porque a
# promessa tem de ser a mesma nos dois lugares. Não promete prazo de resposta
# nem gratuidade: nenhuma das duas foi autorizada pela cliente (SEO-045).
CLOSE = ("O primeiro retorno estabelece se há tese técnica sustentável, qual via "
         "processual ela comporta e o que precisaria ser produzido para sustentá-la; "
         "não substitui o parecer.")

# Duas variantes do aviso de prazo, porque o marco é diferente conforme a via:
# no processo judicial conta da intimação; no processo administrativo, da
# ciência do auto.
PRAZO_JUD = ("Havendo prazo em curso, informe qual é e a data da intimação — "
             "não a do despacho nem a da juntada.")
PRAZO_ADM = ("Havendo prazo de defesa em curso, informe a data da ciência do auto, "
             "que é o marco de contagem.")

# slug -> (pergunta, abertura da lista, fecho específico da matéria, aviso de prazo)
ENTRIES = {
 "analise-microbiologica-alimentos": (
  "Que documentos são necessários para revisar um laudo de análise microbiológica?",
  "A revisão de um resultado microbiológico depende do laudo e dos registros que o cercam",
  "Sem método declarado, incerteza de medição e plano de amostragem, o resultado não é "
  "verificável — e é essa verificação que decide se o laudo sustenta a autuação ou a "
  "rejeição do lote.",
  PRAZO_ADM),
 "assistente-tecnica": (
  "O que enviar ao assistente técnico no primeiro contato?",
  "O que permite dizer se há tese técnica e qual janela processual ainda está aberta",
  "Perdido o prazo dos quesitos iniciais, permanecem os quesitos suplementares do art. 469 "
  "e os 15 dias comuns do art. 477, §1º para a manifestação e o parecer do assistente "
  "técnico.",
  PRAZO_JUD),
 "auto-infracao-ambiental": (
  "Quais documentos são necessários para avaliar a defesa de um auto de infração ambiental?",
  "A defesa técnica se constrói sobre o que o órgão afirmou e sobre o que a empresa "
  "demonstra do mesmo período",
  "O confronto entre o relatório de fiscalização e o automonitoramento do período autuado é "
  "o que define se a impugnação discute o fato, o enquadramento ou a dosimetria da multa.",
  PRAZO_ADM),
 "classificacao-fiscal-ncm": (
  "O que é preciso enviar para contestar tecnicamente uma reclassificação fiscal (NCM)?",
  "A contestação compara o que o fisco afirmou sobre o produto com o que o produto "
  "tecnicamente é",
  "É a composição quantitativa, confrontada com as Regras Gerais de Interpretação do Sistema "
  "Harmonizado, que determina se o enquadramento do auto se sustenta.",
  PRAZO_ADM),
 "cpc-prova-pericial": (
  "O que informar para saber qual prazo pericial está correndo?",
  "Para converter um andamento processual em data de vencimento, o essencial é",
  "O nome do movimento indica qual prazo abriu; a data da intimação, e não a do despacho ou "
  "a da juntada, é o marco a partir do qual ele corre.",
  ""),
 "dano-motor-combustivel": (
  "Que documentos comprovam o nexo entre combustível fora de especificação e dano ao motor?",
  "O nexo se demonstra encadeando o produto, a falha e a peça",
  "Sem a peça preservada ou seu registro fotográfico, a prova do modo de falha passa a "
  "depender inteiramente do laudo da oficina.",
  PRAZO_JUD),
 "honorarios-pericia-judicial": (
  "O que enviar para avaliar se os honorários periciais arbitrados estão adequados?",
  "A avaliação compara o valor arbitrado com o trabalho que a perícia efetivamente exige",
  "A complexidade não se afere pelo valor da causa, e sim pelo objeto fixado para a perícia e "
  "pelos quesitos a responder.",
  PRAZO_JUD),
 "impugnacao-laudo-pericial": (
  "Quais documentos são necessários para impugnar um laudo pericial?",
  "A crítica ao laudo é feita sobre o documento inteiro, não sobre a conclusão",
  "Anexos, planilhas e memoriais de cálculo são onde os vícios de método aparecem; a "
  "conclusão raramente os revela.",
  PRAZO_JUD),
 "laudo-pericial": (
  "O que enviar para uma análise preliminar de laudo pericial?",
  "A leitura preliminar verifica o laudo contra os quatro requisitos do art. 473 do CPC/2015 "
  "e contra os quesitos respondidos",
  "Os 15 dias comuns do art. 477, §1º correm da intimação sobre o laudo, e é dentro deles que "
  "a manifestação da parte e o parecer do assistente técnico são apresentados.",
  ""),
 "normas-tecnicas-pericia": (
  "Como verificar se a norma técnica citada em um laudo era a vigente?",
  "A verificação de vigência depende de três informações",
  "A norma aplicável é a vigente na data do fato, não a da realização do exame — e o defeito "
  "mais comum não é usar uma versão ou outra, e sim não declarar qual delas foi aplicada.",
  PRAZO_JUD),
 "pericia-ambiental": (
  "Que documentos são necessários para uma perícia ambiental?",
  "O exame parte do que já foi investigado na área e do que a licença autorizava",
  "É o confronto entre os resultados analíticos, o histórico de uso e as condicionantes que "
  "separa passivo preexistente de dano imputável ao período em disputa.",
  PRAZO_JUD),
 "pericia-combustiveis": (
  "O que enviar para avaliar um caso de combustível fora de especificação?",
  "A análise parte do resultado laboratorial e da rastreabilidade do produto até o tanque",
  "O parâmetro reprovado e o método empregado definem a discussão: nem toda não conformidade "
  "indica adulteração, e a distinção entre as duas decide a responsabilidade.",
  PRAZO_ADM),
 "pericia-contaminacao-alimentos": (
  "Que documentos são necessários para investigar uma contaminação alimentar?",
  "A investigação exige o resultado, a amostra que o originou e o processo que produziu o lote",
  "Sem cadeia de custódia íntegra, o laudo é atacável antes mesmo de se discutir o resultado; "
  "com os registros de APPCC, é possível localizar em que etapa a falha ocorreu.",
  PRAZO_ADM),
 "pericia-industria-quimica": (
  "Que registros são necessários para periciar um acidente ou desvio de processo químico?",
  "A reconstrução do evento depende dos registros do próprio processo",
  "O batch record mostra o que a planta fez; o HAZOP e as ordens de manutenção mostram o que "
  "se sabia que poderia acontecer e o que foi feito a respeito.",
  PRAZO_JUD),
 "prazo-validade-alimentos": (
  "O que enviar para discutir tecnicamente o prazo de validade de um alimento?",
  "A discussão se resolve entre o estudo que fixou o prazo e as condições em que o produto "
  "chegou à coleta",
  "O prazo de validade é declaração técnica do fabricante sustentada em estudo de vida útil; "
  "sem esse estudo, não há como defender o prazo declarado nem atacá-lo.",
  PRAZO_ADM),
 "producao-antecipada-prova": (
  "O que é preciso reunir para pedir a produção antecipada de prova pericial?",
  "O pedido depende de demonstrar o que se perde com o tempo e em que prazo",
  "A urgência se prova com o estado atual do bem, registrado agora: medição feita depois do "
  "perecimento não recupera a prova.",
  PRAZO_JUD),
 "produtos-quimicos-controlados": (
  "Que documentos são necessários para responder a uma autuação por produto químico controlado?",
  "A defesa da autuação escritural se faz com os próprios registros do período",
  "A autuação escritural discute divergência de saldo entre mapa, livro e nota fiscal — "
  "reconciliar esses três registros é o núcleo da defesa.",
  PRAZO_ADM),
 "quesitos-periciais": (
  "O que enviar para a elaboração de quesitos periciais?",
  "Os quesitos se escrevem a partir do objeto fixado pelo juízo e dos documentos técnicos do caso",
  "Quesito útil pergunta o que o documento técnico permite responder; quesito que pede juízo "
  "de culpa ou de responsabilidade é vedado ao perito pelo art. 473, §2º.",
  PRAZO_JUD),
 "rotulagem-alimentos": (
  "Que documentos são necessários para defender uma autuação de rotulagem de alimentos?",
  "A defesa compara o que o rótulo declara com o que o produto comprovadamente é",
  "A irregularidade de rotulagem pode ser formal ou de conteúdo, e a distinção muda a defesa: "
  "a primeira se corrige, a segunda se prova com laudo.",
  PRAZO_ADM),
 "sobre": (
  "Como iniciar uma consulta técnica com Adriana Rezende?",
  "Por WhatsApp ou e-mail, com o mínimo necessário para uma leitura preliminar",
  "A análise documental, a elaboração de quesitos e a redação de pareceres são feitas "
  "remotamente, com atendimento em todo o território nacional.",
  ""),
}


def _lower_first(item):
    """Minúscula na primeira letra, para o item caber no meio da frase.

    Preserva siglas: se as duas primeiras letras forem maiúsculas (P&ID, FDS),
    o item entra como está. O teste é feito sobre o texto desescapado, senão o
    `&amp;` de "P&ID" injeta um "amp" minúsculo e a sigla seria rebaixada.
    """
    letters = [c for c in _html.unescape(item) if c.isalpha()]
    if len(letters) >= 2 and letters[0].isupper() and letters[1].isupper():
        return item
    return item[0].lower() + item[1:]


def answer(slug):
    """Resposta única — a mesma string alimenta o HTML visível e o JSON-LD."""
    question, lead, tail, prazo = ENTRIES[slug]
    items = "; ".join(_lower_first(i) for i in PAGES[slug])
    parts = [f"{lead}: {items}.", tail]
    if prazo:
        parts.append(prazo)
    parts.append(CLOSE)
    return " ".join(parts)


def question(slug):
    return ENTRIES[slug][0]
