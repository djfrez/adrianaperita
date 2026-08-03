# SEO Backlog — adrianarezende.com.br

Priority Score = (Impact × Confidence × Business Value) ÷ Effort

Status: `open` · `in progress` · `done` · `blocked`

---

## Contexto do site (auditoria de 2026-08-01)

- Site estático de **uma única URL** (`/`), hospedado no **GitHub Pages** (confirmado via header `server: GitHub.com`).
- Metadados, Open Graph, canonical, hreflang, robots.txt, sitemap.xml e llms.txt já existem e estão corretos.
- Schema já presente na home: `Person`, `ProfessionalService`, `FAQPage`, `BreadcrumbList`.
- Imagens já em WebP com `width`/`height` e preload do LCP.
- Sem acesso a Google Search Console **no momento da auditoria** — priorização feita por intenção comercial e cobertura semântica, não por dados de impressão. GSC e GA4 foram conectados ainda em 2026-08-01 (ver SEO-007); os dados começam a ficar disponíveis a partir de ~2026-08-04.

### Maiores fraquezas encontradas

1. **Ausência total de conteúdo indexável além da home.** Nenhuma página de serviço, nenhum artigo. A seção "Insights" listava 4 títulos sem destino — promessa de conteúdo que não existia.
2. **Zero clusters temáticos.** Nenhuma cobertura de perguntas de pré-contratação (prazos, custos, diferença perito × assistente, impugnação de laudo).
3. **`_headers` inerte.** O arquivo segue o formato Cloudflare Pages/Netlify, mas o site é servido pelo GitHub Pages, que o ignora.
4. **CSS duplicado entre páginas.** Cada página traz seu próprio bloco `<style>` inline. Aos ~5 páginas, extrair para `/style.css` compartilhado; abaixo disso, o inline evita requisição extra e o risco de deriva é só cosmético.
5. **Inconsistência de E-E-A-T no llms.txt** — dizia "8 anos de experiência" enquanto o site diz "+20 anos técnicos / +8 anos em perícia". (corrigido em 2026-08-01)

---

## Itens

### SEO-001 — Página-pilar: Assistente Técnico
- **Descrição:** Criar a primeira página do cluster "Assistência Técnica" — guia completo de pré-contratação, com base no CPC/2015, tabela comparativa perito × assistente, linha do tempo da perícia, checklist e FAQ.
- **URL:** `/assistente-tecnica/`
- **Categoria:** Conteúdo / Autoridade tópica / AI citation
- **Impacto:** 9 · **Esforço:** 4 · **Confiança:** 9 · **Valor de negócio:** 10
- **Priority Score:** 202,5
- **Status:** done
- **Descoberto:** 2026-08-01 · **Concluído:** 2026-08-01
- **Notas:** Article + FAQPage + BreadcrumbList schema. Linkada a partir da seção Insights da home, do sitemap e do llms.txt.

### SEO-002 — Página-pilar: Classificação Fiscal / NCM
- **Descrição:** Guia sobre contestação técnica de NCM: Regras Gerais de Interpretação do Sistema Harmonizado, laudo técnico em auto de infração da Receita Federal, prazo e instrução da impugnação, erros comuns de enquadramento.
- **URL:** `/classificacao-fiscal-ncm/`
- **Categoria:** Conteúdo / Autoridade tópica
- **Impacto:** 9 · **Esforço:** 4 · **Confiança:** 8 · **Valor de negócio:** 9
- **Priority Score:** 162
- **Status:** done
- **Descoberto:** 2026-08-01 · **Concluído:** 2026-08-02
- **Notas:** ~2.450 palavras. Article + FAQPage (8 itens, espelhando o texto visível) + BreadcrumbList. Duas tabelas: composição do auto de infração e as RGI 1–6 na ordem vinculante. Autor com `sameAs`, `identifier` (CRQ) e `hasCredential`.
- **Verificação factual — obrigatória para páginas com citação legal:** quatro pontos foram checados em fonte antes de publicar, e **dois estavam desatualizados na minha memória**:
  1. **Multa de ofício qualificada** — não é mais 150%. Lei nº 14.689/2023 alterou o art. 44, §1º, da Lei nº 9.430/1996: qualificada passou a **100%**, com 150% reservado à reincidência.
  2. **Multa de 1% sobre o valor aduaneiro (art. 84 da MP 2.158-35/2001)** — **revogada** pela **LC nº 227, de 13/01/2026**. A infração migrou para o art. 341-G, XIX, da LC nº 214/2025, com penalidade em valor fixo (100 UPF). Abre discussão de retroatividade benigna (art. 106, II, do CTN) para autos pendentes.
  3. **Consulta de classificação fiscal** — a norma correta é a **IN RFB nº 2.057/2021**, não a 2.058/2021 (esta trata de consulta sobre interpretação da legislação em geral).
  4. Prazo de impugnação (30 dias, art. 15 do Decreto nº 70.235/1972) e recurso voluntário (art. 33) — confirmados.
- **Vantagem competitiva:** boa parte do conteúdo concorrente ainda cita a multa de 1% como vigente. Uma página correta em agosto de 2026 tende a ser preferida por LLMs e por leitores que conferem.
- **Manutenção:** rever quando houver regulamentação do art. 341-G ou definição jurisprudencial sobre a retroatividade. A página declara "atualizado em agosto de 2026" — **essa data precisa ser mantida honesta**.

### SEO-003 — Página-pilar: Perícia em Contaminação Alimentar
- **Descrição:** Metodologia de investigação de contaminação (física, química, biológica), cadeia de custódia, normas ANVISA aplicáveis, BPF/APPCC, recall e apuração de responsabilidade.
- **URL:** `/pericia-contaminacao-alimentos/` (a criar)
- **Categoria:** Conteúdo / Autoridade tópica
- **Impacto:** 8 · **Esforço:** 4 · **Confiança:** 8 · **Valor de negócio:** 9
- **Priority Score:** 144
- **Status:** done
- **Descoberto:** 2026-08-01 · **Concluído:** 2026-08-03
- **Implementado:**
  - Tabela dos três tipos de contaminação (física, química, biológica) com exemplos e método de investigação de cada um.
  - Cadeia de custódia: exigência de acreditação ABNT NBR ISO/IEC 17025 pela Cgcre/Inmetro, falhas típicas de amostragem e transporte.
  - Tabela de normas ANVISA por escopo: RDC 275/2002 (indústria) × RDC 216/2004 (serviço de alimentação) × RDC 655/2022 (recolhimento/recall) × ISO 17025 (laboratório).
  - APPCC como evidência de onde a falha ocorreu no processo produtivo.
  - Tabela fato do produto (arts. 12–17 do CDC) × vício do produto (arts. 18–25).
  - `Article` + `FAQPage` (7 itens, paridade texto visível confirmada por script) + `BreadcrumbList`. `author` usa o mesmo `@id` canônico criado em SEO-004 (o `Person` de todo o site).
  - Links internos: nav nas 5 páginas, card da home (que antes era só texto sem link — corrigido), "Continue lendo" nas outras três páginas, `sitemap.xml` e `llms.txt` atualizados. Zero links quebrados (verificado por script).
- **Verificação factual — obrigatória para páginas com citação regulatória:** quatro pontos checados por busca antes de publicar:
  1. **RDC 275/2002 segue vigente** — não foi revogada pela RDC 216/2004 (hipótese que precisou ser descartada). São normas complementares de escopo distinto: 275 para indústria/produção, 216 para serviço de alimentação.
  2. **Recolhimento (recall) é regido pela RDC nº 655/2022**, não por norma mais antiga.
  3. **CDC arts. 12–17 (fato do produto) × 18–25 (vício do produto)** — regimes de responsabilidade distintos, confirmados na fonte primária.
  4. **Consulta pública CP 1.362/2025** propõe substituir a RDC 275/2002 por marco único (BPF + POP + APPCC obrigatório em toda a cadeia). **Ainda não está em vigor** — tratada na página como "em andamento", não como norma vigente, seguindo o mesmo cuidado do SEO-002 com o art. 341-G.
- **Manutenção:** revisar quando a CP 1.362/2025 for concluída — se resultar em nova RDC, a seção "Normas técnicas aplicáveis" precisa ser atualizada antes que fique desatualizada como a multa de 1% estava no SEO-002.

### SEO-004 — Página "Sobre" dedicada (E-E-A-T)
- **Descrição:** Página própria de biografia profissional com trajetória detalhada, setores atendidos, formação, normas de domínio e tipos de processo — hoje esse conteúdo está comprimido em duas seções da home. Fortalece a entidade "Adriana Rezende" para o Knowledge Graph e para citação por LLMs.
- **URL:** `/sobre/` (a criar)
- **Categoria:** E-E-A-T / Entity SEO
- **Impacto:** 7 · **Esforço:** 3 · **Confiança:** 8 · **Valor de negócio:** 8
- **Priority Score:** 149,3
- **Status:** done
- **Descoberto:** 2026-08-01 · **Concluído:** 2026-08-03
- **Implementado:**
  - `ProfilePage` com `mainEntity` `Person` carregando `@id` canônico `https://adrianarezende.com.br/#adriana-rezende`, `hasCredential` duplo (registro CRQ + graduação UNICAMP), `hasOccupation` para os dois papéis, `knowsAbout` com 18 entidades e `workLocation` Brasil.
  - O mesmo `@id` foi aplicado ao `Person` da home e ao `author` das duas páginas-pilar, e o `url` do autor passou a apontar para `/sobre/`. **Os quatro nós `Person` do site agora são um único nó no grafo**, em vez de quatro entidades soltas com o mesmo nome — que é exatamente o problema que o histórico do domínio (SEO-010) cria.
  - `FAQPage` com 7 perguntas, todas espelhando o texto visível.
  - Tabela de matéria técnica → o que se examina → órgãos/normas (7 linhas), e tabela perita × assistente (4 dimensões).
  - Links internos: "Sobre" na navegação das quatro páginas (desktop e mobile na home), link contextual na seção de Qualificações da home, e entrada em "Continue lendo" das duas páginas-pilar. `/sobre/` recebe inbound das três páginas existentes.
  - `sitemap.xml` e `llms.txt` atualizados.
- **Decisão de conteúdo:** a página foi escrita apenas com fatos já verificáveis no site (UNICAMP, CRQ 04341673, 14 anos em multinacionais de alimentos/higiene/limpeza, área ambiental de águas e efluentes, Departamento de Processos Químicos da UNICAMP, tipos de processo). **Nenhuma data, empregador, número de casos ou publicação foi inventado para dar volume ao texto.** O valor da página vem da organização decisória — quais matérias, quais órgãos, qual papel, como começa — não de biografia inflada.
- **Desambiguação — o que foi e o que não foi feito:** optou-se por âncoras positivas (número de registro, conselho correto, universidade, LinkedIn, `@id` único) em vez de uma nota na página dizendo "não confundir com outra profissional homônima". Uma negativa visível chamaria atenção para a ambiguidade sem resolvê-la. A ressalva explícita ficou apenas no `llms.txt`, que é lido por máquina e não por cliente.

### SEO-005 — `_headers` inerte no GitHub Pages
- **Descrição:** O arquivo `_headers` não é interpretado pelo GitHub Pages (formato Cloudflare Pages/Netlify). O cache de imagens de 30 dias pretendido não está em vigor; o GH Pages serve `cache-control: max-age=600`. Decidir entre (a) colocar o domínio atrás do Cloudflare, (b) migrar a hospedagem, ou (c) remover o arquivo para não induzir a erro.
- **URL:** `/_headers`
- **Categoria:** Técnico / Performance
- **Impacto:** 4 · **Esforço:** 5 · **Confiança:** 9 · **Valor de negócio:** 3
- **Priority Score:** 21,6
- **Status:** open
- **Descoberto:** 2026-08-01
- **Notas:** Impacto real baixo — o site é leve e o LCP já tem preload. Não bloqueia nada.

### SEO-006 — Formulário de contato depende de `mailto:`
- **Descrição:** O envio do formulário abre o cliente de e-mail do usuário. Em navegador sem cliente configurado (comum em desktop corporativo), o lead se perde silenciosamente. Avaliar endpoint de formulário estático (Formspree, Web3Forms) ou CTA direto para WhatsApp como ação primária.
- **URL:** `/#contact`
- **Categoria:** Conversão
- **Impacto:** 8 · **Esforço:** 4 · **Confiança:** 6 · **Valor de negócio:** 9
- **Priority Score:** 108
- **Status:** done
- **Descoberto:** 2026-08-01 · **Concluído:** 2026-08-03
- **Decisão do cliente:** WhatsApp como canal primário, sem serviço de terceiros — com mensagem padrão para identificar que o contato veio do site.
- **Implementado:**
  - O formulário de contato da home não abre mais o cliente de e-mail do visitante. O `submit` agora monta o texto estruturado (nome, organização, e-mail, telefone, assunto, mensagem) e abre `wa.me` com o texto pré-preenchido via `?text=`, em nova aba. Zero dependência de terceiro, zero cadastro.
  - Botão do formulário renomeado para "Enviar via WhatsApp"; e-mail (`mailto:`) permanece como alternativa secundária logo abaixo, para quem preferir.
  - Na seção de contato da home, WhatsApp passou a ser o primeiro item (antes era e-mail), com o mesmo texto padrão pré-preenchido nos links "avulsos" (o telefone clicável fora do formulário) e no rodapé.
  - Os botões de CTA "WhatsApp" nas quatro páginas de conteúdo (`/sobre/`, `/assistente-tecnica/`, `/classificacao-fiscal-ncm/`, `/pericia-contaminacao-alimentos/`) ganharam texto pré-preenchido identificando a página de origem (ex.: "vim pelo site (guia de Classificação Fiscal NCM)"), para que a cliente saiba de qual página veio o contato sem precisar de analytics.
  - Handler testado em sandbox Node com três cenários (preenchimento completo, campos opcionais vazios, campos obrigatórios ausentes) — todos geram a URL `wa.me` esperada ou o alerta de validação, conforme o caso.
- **Por que não um serviço de formulário de terceiros:** a alternativa (Formspree/Web3Forms) exigiria criar conta em serviço externo e decidir o que acontece com os dados enviados nos servidores dele — exatamente o tipo de decisão que travava este item. A escolha do cliente elimina essa dependência por completo.

### SEO-007 — Conectar Google Search Console e GA4
- **Descrição:** Sem GSC não há dados de impressão, CTR nem posição média; toda a Prioridade 1 e 2 do mandato (melhorar páginas com impressão alta e palavras em 5–20) fica cega. Verificar propriedade e submeter o sitemap.
- **Categoria:** Medição
- **Impacto:** 9 · **Esforço:** 2 · **Confiança:** 10 · **Valor de negócio:** 8
- **Priority Score:** 360
- **Status:** done
- **Descoberto:** 2026-08-01 · **Concluído:** 2026-08-01
- **Notas:** Tag GA4 `G-NL5HWSTKPF` instalada nas duas páginas. Projeto Google Cloud `adriana-seo`, conta de serviço `adriana-seo@adriana-seo.iam.gserviceaccount.com`, credenciais em `~/.config/claude-seo/google-api.json` (tier 2 — API key + service account + GA4).
  - Search Console: propriedade `sc-domain:adrianarezende.com.br`, permissão `siteFullUser` — verificado por chamada real à API.
  - GA4: propriedade `properties/548153325` (BRL, America/Sao_Paulo) — Data API e Realtime API respondendo.
  - **Ainda sem linhas de dados em ambos**: a propriedade GSC acabou de ser verificada (latência típica de 2–3 dias) e a tag GA4 entrou no ar em 2026-08-01. A partir da próxima execução com dados, a priorização deixa de ser por intenção comercial e passa a usar impressões, CTR e posição reais.
  - `sitemap.xml` submetido ao Search Console em 2026-08-02 (autorizado pelo cliente); estado `isPending`, 0 avisos e 0 erros.

### SEO-008 — Restantes "Insights" sem destino
- **Descrição:** Três cartões da seção Insights ainda são títulos sem página. Serão resolvidos por SEO-002 e SEO-003; o quarto ("O papel do assistente técnico na impugnação de laudos periciais") foi absorvido pelo conteúdo de SEO-001 e deve ser substituído por outro tema do cluster ou removido.
- **URL:** `/#insights`
- **Categoria:** UX / Confiança
- **Impacto:** 5 · **Esforço:** 2 · **Confiança:** 9 · **Valor de negócio:** 6
- **Priority Score:** 135
- **Status:** done
- **Descoberto:** 2026-08-01 · **Concluído:** 2026-08-03
- **Implementado:** os três primeiros cartões já tinham destino (SEO-001, SEO-002, SEO-003). O quarto — "O papel do assistente técnico na impugnação de laudos periciais" — não virou página nova, porque o próprio conteúdo já existe dentro de `/assistente-tecnica/`, na seção "Como um parecer técnico derruba um laudo" (art. 479 do CPC, seis falhas metodológicas). Em vez de inventar uma página ou remover o cartão, adicionei `id="impugnacao-laudos"` a essa seção e apontei o cartão para `/assistente-tecnica/#impugnacao-laudos`, com título e resumo reescritos para refletir o conteúdo real de destino.
- **Por que não virou página própria:** o mandato veda publicar conteúdo só para preencher um cartão. Como a matéria já estava integralmente coberta em outra página do site, criar uma segunda página só duplicaria conteúdo — a correção certa era linkar para o que já existe, não gerar mais uma URL.
- **`llms.txt`:** a linha "Em elaboração" — que prometia exatamente essa página inexistente — foi removida, já que não há mais nenhum item pendente. — Perfil no Google Business e citações locais
- **Descrição:** Nenhum sinal de perfil GBP para "perita judicial Campinas". Criar/reivindicar perfil, padronizar NAP e buscar citações (CRQ, associações de peritos, diretórios jurídicos).
- **Categoria:** Local SEO / Autoridade
- **Impacto:** 7 · **Esforço:** 5 · **Confiança:** 7 · **Valor de negócio:** 8
- **Priority Score:** 78,4
- **Status:** blocked
- **Descoberto:** 2026-08-01
- **Bloqueio:** exige verificação de identidade do proprietário.

### SEO-010 — Histórico do domínio: contexto de interpretação (não é oportunidade)
- **Descrição:** O Search Console expôs um sitemap registrado em 2010-03-03 e baixado pela última vez em 2018-01-27, indicando site anterior no domínio. Investigado via Wayback Machine: entre ~2021 e 2023 o domínio hospedou um site de **consultoria de imagem e estilo** (coloração pessoal, análise de óculos, corte e cor, consultoria express — URLs como `/colocaraopessoal`, `/analiseoculos`, `/consultoria-express`, `/blog/hashtags/...`, padrão Wix). **Confirmado pelo cliente: não era a Adriana Rezende perita judicial** — é outra profissional de mesmo nome.
- **Categoria:** Contexto / Medição
- **Status:** done (investigado; sem ação de recuperação)
- **Descoberto:** 2026-08-02 · **Concluído:** 2026-08-02
- **Conclusão:** A hipótese original — recuperar backlinks legados via 301 — **fica descartada**. Links apontando para conteúdo de consultoria de imagem são topicamente irrelevantes para perícia em engenharia química; redirecioná-los não gera autoridade e apenas cria ruído. Os redirecionamentos de host já estão corretos (`www` → apex, `http` → `https`, ambos 301), então nada quebra.
- **Por que continua registrado — dois efeitos práticos:**
  1. **Ao ler os primeiros dados do GSC, esperar ruído residual.** Podem aparecer impressões para termos como "coloração pessoal", "consultoria de imagem", "análise de óculos". **Isso é herança do domínio, não sinal de demanda.** Sem este registro, uma execução futura poderia interpretar essas consultas como oportunidade e perseguir a vertical errada.
  2. **Existe ambiguidade de entidade no nome "Adriana Rezende".** Há outra profissional com o mesmo nome, em outra área, que ocupou este domínio por anos. Isso aumenta o risco de o Google confundir as duas entidades e reforça a prioridade de sinais de desambiguação — ver SEO-004.

### SEO-011 — Desambiguação de entidade: `sameAs` e identificadores profissionais
- **Descrição:** O schema `Person` não tinha `sameAs` nem identificador profissional. Dado o histórico do domínio (SEO-010) e a existência de outra profissional homônima, faltavam âncoras dizendo ao Google e aos LLMs *qual* Adriana Rezende é esta.
- **URL:** `/` e `/assistente-tecnica/`
- **Categoria:** Entity SEO / E-E-A-T
- **Impacto:** 7 · **Esforço:** 2 · **Confiança:** 8 · **Valor de negócio:** 8
- **Priority Score:** 224
- **Status:** done
- **Descoberto:** 2026-08-02 · **Concluído:** 2026-08-02
- **Implementado:**
  - `sameAs` com o LinkedIn (`adriana-rezende-5992554a`) no `Person` da home, no `provider` do `ProfessionalService` e no `author` do Article.
  - `identifier` (`PropertyValue`, propertyID `CRQ`, valor `04341673`) e `hasCredential` (`EducationalOccupationalCredential` reconhecida pelo CRQ-IV) nos dois `Person`.
  - Menções visíveis: bloco "Registro Profissional" na seção de Qualificações com link para a consulta pública do CRQ, rodapé das duas páginas, e assinatura do autor na página de assistente técnico.
  - `llms.txt` atualizado com registro e LinkedIn.
- **Nota sobre o órgão:** o domínio canônico do CRQ-IV é `crqsp.org.br`; `crq4.org.br` redireciona para lá. Usado o canônico.
- **Ainda úteis, se existirem:** currículo Lattes, ORCID, publicações, associações de peritos.

---

## Histórico de execuções

| Data | Item executado | Commit |
|---|---|---|
| 2026-08-01 | SEO-001 — página-pilar `/assistente-tecnica/` | `SEO: Add Assistente Técnico pillar page` |
| 2026-08-02 | SEO-002 — página-pilar `/classificacao-fiscal-ncm/` | `SEO: Add NCM classification pillar page (SEO-002)` |
| 2026-08-03 | SEO-004 — página `/sobre/` e unificação do nó `Person` | `SEO: Add /sobre/ profile page and unify Person entity` |
| 2026-08-03 | SEO-003 — página-pilar `/pericia-contaminacao-alimentos/` | `SEO: Add food contamination pillar page (SEO-003)` |
| 2026-08-03 | SEO-008 — último cartão Insights sem destino | `SEO: Link last dead Insights card to existing content` |
| 2026-08-03 | SEO-006 — formulário de contato via WhatsApp | `SEO: Route contact form through WhatsApp instead of mailto` |

---

## Estado da medição — 2026-08-03

Verificado por chamada direta às APIs nesta execução:

- **Search Console — ainda zero linhas.** `searchAnalytics.query` para 2026-07-01 → 2026-08-02 retorna resposta vazia nas dimensões `query`, `page` e `date`. A propriedade foi verificada em 2026-08-01; a latência é esperada. **A priorização continua sendo por intenção comercial, não por dados.**
- **Indexação (URL Inspection API):**

  | URL | Veredito | Estado |
  |---|---|---|
  | `/` | PASS | Submitted and indexed (último rastreamento 2026-08-02) |
  | `/assistente-tecnica/` | NEUTRAL | Discovered — currently not indexed |
  | `/classificacao-fiscal-ncm/` | NEUTRAL | URL is unknown to Google |

- **GA4** — 5 sessões no período 2026-07-25 → 2026-08-02, todas em `/`, canais `Unassigned` e `Direct`. Volume compatível com acessos próprios; sem valor analítico ainda.

**Leitura:** as páginas novas ainda não entraram no índice, o que é normal para conteúdo de 1–2 dias em domínio de baixa autoridade. O sitemap já foi submetido e o caminho de rastreamento a partir da home (que *está* indexada) foi reforçado hoje com links de navegação. **Nada a fazer além de aguardar** — pedir indexação repetidamente não acelera o processo.

**Para a próxima execução:** reconferir indexação e GSC *antes* de escolher a tarefa. Se as páginas continuarem fora do índice depois de ~7 dias (a partir de 2026-08-08), aí vira item de backlog técnico — e a hipótese a investigar é autoridade de domínio insuficiente para justificar o rastreamento, não erro de configuração, que já foi descartado (robots ALLOWED, canonical correto, sitemap aceito sem erros).
