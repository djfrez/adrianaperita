# -*- coding: utf-8 -*-
"""Bloco 'O que enviar na primeira mensagem' (SEO-045).

Fonte única do conteúdo do bloco de intake que vai no `cta-sec` das páginas de
conteúdo. Ler daqui, gerar o HTML por `intake_build.py` — mesmo método da
SEO-037/SEO-044: o texto é definido uma vez e nunca copiado à mão.

Motivo do item: 78 sessões em 56 dias com leitura profunda (156 s a 621 s de
duração média nas páginas de conteúdo) produziram 1 `form_start` e 1
`manual_event_CONTACT`. A leitura acontece; o contato não. O bloco remove as
três dúvidas que travam a primeira mensagem — o que enviar, o que volta, e de
que data corre o prazo.
"""

# Frase de abertura e fechamento — idênticas em todas as páginas de propósito:
# o leitor que circula por três páginas do cluster deve reconhecer o mesmo
# procedimento, não três ofertas diferentes.
LEDE = ("Uma leitura preliminar só é possível com o documento em disputa à vista. "
        "Para um caso deste tipo, o mínimo é:")

# Não promete prazo de resposta nem gratuidade — nenhuma das duas coisas foi
# autorizada pela cliente, e uma promessa de SLA no site é compromisso que ela
# passa a ter de cumprir. Descreve o que a análise preliminar estabelece, que é
# o que a home já oferece ("análise preliminar de casos").
CLOSE = ("O primeiro retorno estabelece se há tese técnica sustentável, qual via "
         "processual ela comporta e o que precisaria ser produzido para sustentá-la. "
         "Não substitui o parecer — é o que permite decidir se vale contratá-lo.")

PRAZO = ("Se há prazo correndo, informe qual é e <strong>a data da intimação</strong> — "
         "não a do despacho nem a da juntada.")

PAGES = {
 "analise-microbiologica-alimentos": [
  "Laudo laboratorial completo, com método, incerteza de medição e limite de quantificação",
  "Plano de amostragem adotado e identificação do lote amostrado",
  "Laudo de contraprova, se houve",
  "Registros de temperatura e de processo do lote analisado"],
 "assistente-tecnica": [
  "Decisão que deferiu a perícia e nomeou o perito",
  "Quesitos já apresentados pelas partes e pelo juízo",
  "Laudo, se já juntado aos autos",
  "Contrato, nota fiscal ou ficha técnica que descreve o produto ou processo em disputa"],
 "auto-infracao-ambiental": [
  "Auto de infração e o relatório de fiscalização que o instrui",
  "Licença ambiental vigente e as condicionantes do período autuado",
  "Laudos e relatórios de automonitoramento do mesmo período",
  "Data da ciência do auto"],
 "classificacao-fiscal-ncm": [
  "Auto de infração e o laudo ou parecer do fisco que fundamenta a reclassificação",
  "Ficha técnica e composição quantitativa do produto",
  "Laudo de análise do produto, se houver",
  "Declarações de importação ou notas fiscais do período autuado"],
 "cpc-prova-pericial": [
  "Qual ato foi publicado — o nome do movimento, como aparece na tela do processo",
  "Data da intimação e o meio (portal eletrônico ou DJe)",
  "Decisão que deferiu a perícia e definiu o objeto",
  "Laudo, se já juntado"],
 "dano-motor-combustivel": [
  "Laudo do combustível, com o método e o parâmetro reprovado",
  "Ordem de serviço e laudo da oficina que abriu o motor",
  "Nota fiscal do abastecimento e identificação do posto",
  "Fotos das peças danificadas — e, se possível, a peça preservada"],
 "honorarios-pericia-judicial": [
  "Decisão que arbitrou os honorários e a proposta apresentada pelo perito",
  "Quesitos e decisão que deferiu a perícia, que definem a complexidade do trabalho",
  "Se há gratuidade de justiça deferida a alguma das partes"],
 "impugnacao-laudo-pericial": [
  "Laudo integral, com anexos, planilhas e memoriais de cálculo",
  "Quesitos apresentados e as respostas correspondentes",
  "Data da intimação do laudo",
  "Documentos técnicos que estavam nos autos e o laudo não examinou"],
 "laudo-pericial": [
  "Laudo integral, com anexos, memoriais de cálculo e registro fotográfico",
  "Quesitos das partes e do juízo",
  "Data da intimação do laudo",
  "Documentos técnicos do caso que já constavam dos autos"],
 "normas-tecnicas-pericia": [
  "Trecho do laudo em que a norma é citada",
  "A data do fato e a data em que a perícia foi realizada",
  "A norma invocada, com número e ano da edição efetivamente usada"],
 "pericia-ambiental": [
  "Laudos de investigação — preliminar, confirmatória ou detalhada — e os resultados analíticos",
  "Licença ambiental e condicionantes",
  "Histórico de uso e ocupação da área",
  "Auto de infração, termo de compromisso ou TAC, se houver"],
 "pericia-combustiveis": [
  "Laudo de análise do combustível, com método e parâmetros reprovados",
  "Nota fiscal e documentação de origem do produto",
  "Registros de recebimento, descarga e controle de tanque",
  "Auto de infração da ANP, se houver"],
 "pericia-contaminacao-alimentos": [
  "Laudo laboratorial com método declarado e a cadeia de custódia da amostra",
  "Identificação e rastreabilidade do lote",
  "Registros de APPCC e de processo do lote envolvido",
  "Notificação sanitária ou reclamação que originou o caso"],
 "pericia-industria-quimica": [
  "Batch record ou registro do historiador de processo do lote ou turno em questão",
  "Relatório do evento e a investigação interna, se houve",
  "P&amp;ID, estudo HAZOP e ordens de manutenção do equipamento envolvido",
  "FDS do produto e certificados de análise das matérias-primas"],
 "prazo-validade-alimentos": [
  "Estudo de vida útil que embasa o prazo declarado no rótulo",
  "Laudo que contesta o produto e a data da coleta",
  "Identificação do lote e data de fabricação",
  "Registros de armazenamento e transporte até a coleta"],
 "producao-antecipada-prova": [
  "O que está perecendo, por quê e em que prazo estimado",
  "Fotos e documentos do estado atual do bem, produto ou instalação",
  "Laudos ou medições já realizados",
  "Se há ação em curso ou apenas risco iminente"],
 "produtos-quimicos-controlados": [
  "Auto de infração e o relatório de fiscalização",
  "Licença de funcionamento (Polícia Federal) ou certificado de registro (Exército) vigentes",
  "Mapas e livros de controle do período autuado",
  "Notas fiscais de entrada e saída dos produtos controlados"],
 "quesitos-periciais": [
  "Decisão que deferiu a perícia e definiu o objeto",
  "Data da intimação e o prazo que ela abriu",
  "Documentos técnicos do caso — contratos, laudos, fichas técnicas, registros de processo",
  "Quesitos da parte contrária, se já apresentados"],
 "rotulagem-alimentos": [
  "Auto de infração e o termo que descreve a irregularidade apontada",
  "Arte do rótulo autuado e a ficha técnica do produto",
  "Laudos de composição ou nutricional que embasam as declarações do rótulo",
  "Data da ciência do auto"],
 "sobre": [
  "O caso em duas ou três linhas — matéria técnica e fase processual",
  "O documento técnico central: laudo, auto de infração, contrato ou ficha técnica",
  "O prazo em curso, se houver, e a data da intimação"],
}
