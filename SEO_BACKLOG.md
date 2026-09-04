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
- **`llms.txt`:** a linha "Em elaboração" — que prometia exatamente essa página inexistente — foi removida, já que não há mais nenhum item pendente.

### SEO-009 — Perfil no Google Business e citações locais
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

### SEO-012 — Sinais estruturais para sitelinks (pedido do cliente)
- **Descrição:** Cliente pediu que quatro destinos existam como sitelinks no resultado de busca do Google: Assistente Técnica, Parecer Técnico, Classificação Fiscal, Contato.
- **Categoria:** Técnico / Structured Data
- **Status:** done (dentro do que é tecnicamente possível — ver ressalva)
- **Descoberto:** 2026-08-03 · **Concluído:** 2026-08-03
- **Ressalva importante, comunicada ao cliente antes de executar:** sitelinks do Google são gerados algoritmicamente. Não existe tag, schema ou configuração que force ou garanta sua exibição — a documentação do próprio Google afirma que não há como especificar ou influenciar diretamente quais aparecem. Eles também dependem de volume de busca pela marca e histórico de cliques, que este domínio ainda não tem (GSC seguia com zero linhas de impressão na última verificação). O que foi implementado é o preparo técnico de melhor prática, não uma garantia.
- **Implementado:**
  - `WebSite` + quatro nós `SiteNavigationElement` no `<head>` da home, cada um com `name`, `description` e `url` exatamente como pedido pelo cliente (Assistente Técnica, Parecer Técnico, Classificação Fiscal, "Solicite uma Consulta" → Contato).
  - **"Parecer Técnico" não é uma página própria** — o conteúdo já existe dentro de `/assistente-tecnica/`, na seção "O que um assistente técnico efetivamente entrega". Perguntado ao cliente como tratar isso dado que a própria instrução condicionava a existência da página; decisão do cliente foi ancorar (`id="parecer-tecnico"`) em vez de criar conteúdo duplicado — mesmo padrão já usado no SEO-008.
  - Nenhuma mudança na navegação visível do site (o menu do cabeçalho continua com sua estrutura atual); a mudança é inteiramente em dados estruturados, não em UI.
- **Follow-up realista:** sitelinks tendem a aparecer só depois que o site acumula autoridade de domínio e volume de busca pelo nome da marca — normalmente meses, não dias. O item de maior alavancagem para isso continua sendo o SEO-009 (Google Business Profile, hoje bloqueado por verificação de identidade) e a indexação básica das páginas novas, que ainda não aconteceu.

### SEO-013 — Páginas-pilar: Perícia Ambiental e Combustíveis
- **Descrição:** Dois serviços com card próprio na home (`Perícias Ambientais` e `Combustíveis`) não tinham página de destino. Isso bloqueava dois ad groups do Google Ads (AG07 e AG08) e deixava dois dos cinco pilares de expertise sem conteúdo indexável.
- **URLs:** `/pericia-ambiental/` · `/pericia-combustiveis/`
- **Categoria:** Conteúdo / Autoridade tópica / Suporte a mídia paga
- **Impacto:** 8 · **Esforço:** 5 · **Confiança:** 8 · **Valor de negócio:** 9
- **Priority Score:** 115,2
- **Status:** done
- **Descoberto:** 2026-08-04 · **Concluído:** 2026-08-04
- **Origem:** identificado durante a auditoria de Google Ads — o playbook de PPC bloqueou AG07/AG08 por ausência de landing page. Criar as páginas destrava mídia paga **e** cobre o cluster orgânico, com o mesmo esforço.
- **Implementado:** `Article` + `FAQPage` (7 itens cada, paridade com texto visível verificada por script) + `BreadcrumbList`, com o `@id` canônico do `Person`. Links de entrada: cards de expertise da home, "Continue lendo" das quatro páginas existentes, sitemap e llms.txt. GA4 e o disparo de conversão `manual_event_CONTACT` presentes nas duas.
- **Verificação factual — quatro pontos checados em fonte antes de publicar:**
  1. **ABNT NBR 10004 foi revisada em 2024** — dividida em NBR 10004-1:2024 e 10004-2:2024, com Sistema Geral de Classificação de Resíduos. As classes **I / II-A / II-B foram substituídas por Classe 1 (Perigoso) e Classe 2 (Não Perigoso)**. Período de transição até **31/12/2026**; depois disso só a nova vale. Muito conteúdo concorrente ainda cita a versão de 2004 — vantagem competitiva real, com prazo.
  2. **CONAMA 420/2009 segue vigente** (há proposta de revisão do IBAMA, ainda não aprovada). Em SP existe camada estadual da CETESB, revisada por decisão de diretoria para alinhar valores de intervenção em água subterrânea aos padrões de potabilidade.
  3. **CONAMA 430/2011 vigente**, complementa/altera a 357/2005. **Consulta pública de revisão em andamento** — tratada como "em andamento", não como norma nova.
  4. **ANP:** gasolina pela Resolução 807/2020; **diesel pela Resolução 968/2024, em vigor desde 31/07/2024** (alterou limites de S10/S500); marcação de solventes pela Resolução 902/2022. Súmula 618 do STJ (inversão do ônus da prova em degradação ambiental) e responsabilidade objetiva do art. 14, §1º da Lei 6.938/1981 confirmados.
- **Manutenção — duas datas a acompanhar:** (a) **31/12/2026**, fim da transição da NBR 10004 — a tabela comparativa da página ambiental precisa ser revista; (b) conclusão da consulta pública da CONAMA 430/2011.

### SEO-014 — Página-pilar: Perícia em Indústria Química
- **Descrição:** O quinto e último card de expertise da home (`Processos Químicos Industriais` / produtos controlados) não tinha página de destino. Era o pilar de maior proximidade com a formação da perita — engenharia química — e o único sem conteúdo indexável.
- **URL:** `/pericia-industria-quimica/`
- **Categoria:** Conteúdo / Autoridade tópica / Entity SEO
- **Impacto:** 8 · **Esforço:** 5 · **Confiança:** 8 · **Valor de negócio:** 9
- **Priority Score:** 115,2
- **Status:** done
- **Descoberto:** 2026-08-04 · **Concluído:** 2026-08-05
- **Nota de execução:** a página foi escrita na execução de 2026-08-04, que **terminou sem commit e sem registro no backlog**. A execução de 2026-08-05 validou, completou os links e fechou o item. Ficou o aprendizado: *escrever o arquivo não é entregar* — o item só existe depois de validado, documentado e commitado.
- **Implementado:**
  - ~4.300 palavras. As quatro famílias de litígio industrial (acidente de processo, falha de processo/desvio de lote, dano causado por produto químico, autuação regulatória) e a prova que sustenta cada uma.
  - Análise de causa raiz e a distinção jurídica entre falha aleatória de componente e falha de gestão — que é onde a responsabilidade normalmente se decide.
  - Os documentos que decidem o caso: batch record, historiador de processo, certificado de análise, FDS, P&ID, HAZOP, ordens de manutenção e registros de calibração.
  - Tabela dos dois regimes de produtos controlados (Polícia Federal × Exército), com base normativa e objeto de controle de cada um.
  - NR-13, NR-20 e NR-26 tratadas como parâmetro de exigibilidade **na data do fato**, não na data da perícia.
  - `Article` + `FAQPage` (7 itens, paridade com o texto visível verificada por script) + `BreadcrumbList`, com o `@id` canônico do `Person`. GA4 e disparo de `manual_event_CONTACT` presentes.
  - Links de entrada: card de expertise da home, "Continue lendo" das seis páginas existentes, `sitemap.xml` e `llms.txt`. A própria página linka os cinco pilares — cluster fechado, sem link quebrado (verificado por script).
- **Verificação factual — dois pontos posteriores ao meu conhecimento interno, checados em fonte antes do commit:**
  1. **IN DG/PF nº 338, de 29/07/2026 — confirmada.** Reeditou os procedimentos de controle e fiscalização de produtos químicos e **revogou as INs nº 166/2020 e nº 211/2021**. Detalha o regime sancionador (dosimetria da multa, suspensão e cancelamento de licença). **Correção registrada em 27/08/2026:** esta nota dizia "multas até R$ 350 mil", número vindo de cobertura secundária. A faixa é legal e está no art. 14, V da Lei nº 10.357/2001 — **R$ 2.128,20 a R$ 1.064.100,00** —, confirmada no Planalto e na página oficial da PF; a IN dosa a multa dentro dela e não pode ampliá-la (ver SEO-037). **Não alterou a relação de produtos controlados**, que segue na Portaria MJSP nº 204/2022 — como a página afirma. Fonte: gov.br/pf e cobertura especializada.
  2. **ABNT NBR 14725:2023 — confirmada.** Publicada em 03/07/2023, consolidou as quatro partes anteriores e substituiu FISPQ por FDS. O período de adequação de 24 meses **encerrou em 03/07/2025**; desde 04/07/2025 só o formato FDS é admitido. A página trata o prazo como encerrado, o que está correto.
- **Vantagem competitiva com prazo:** a IN 338/2026 tem uma semana. Praticamente todo o conteúdo concorrente ainda cita as INs 166/2020 e 211/2021 como vigentes. Janela curta — vale acompanhar se a concorrência atualiza.
- **Manutenção:** revisar se a Portaria MJSP 204/2022 for substituída (é ela que lista os produtos, e é o ponto que muda com mais frequência).

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
| 2026-08-03 | Ícone WhatsApp nos links de contato | `Add WhatsApp icon affordance to contact number links` |
| 2026-08-03 | SEO-012 — sinais estruturais para sitelinks | `SEO: Add sitelinks structured data for four key destinations` |
| 2026-08-04 | SEO-013 — páginas-pilar ambiental e combustíveis | `SEO: Add environmental and fuel pillar pages (SEO-013)` |
| 2026-08-05 | SEO-014 — página-pilar `/pericia-industria-quimica/` | `SEO: Add chemical industry pillar page (SEO-014)` |
| 2026-08-05 | Auditoria + seleção da próxima tarefa | `SEO: Record 2026-08-05 audit, select next task (SEO-015)` |
| 2026-08-05 | Medição destravada (service account) | `SEO: Record first real Search Console data (measurement unblocked)` |
| 2026-08-05 | SEO-015 — spoke `/impugnacao-laudo-pericial/` | `SEO: Add impugnação de laudo pericial spoke page (SEO-015)` |
| 2026-08-05 | SEO-017 — spoke `/honorarios-pericia-judicial/` | `SEO: Add honorários periciais spoke page (SEO-017)` |
| 2026-08-06 | SEO-018 — spoke `/quesitos-periciais/` | `SEO: Add quesitos periciais spoke page (SEO-018)` |
| 2026-08-16 | SEO-030 — referência `/cpc-prova-pericial/` | `SEO: Add CPC prova pericial reference page (SEO-030)` |
| 2026-08-27 | SEO-037 — spoke `/produtos-quimicos-controlados/` | `SEO: Add produtos químicos controlados spoke page (SEO-037)` |

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

---

## Estado da medição — 2026-08-05

**Não foi possível medir nesta execução.** As credenciais locais do Google (Application Default Credentials, `gcloud`) estão expiradas: `searchAnalytics.query` responde **401 UNAUTHENTICATED / Invalid Credentials**. Renovar exige `gcloud auth application-default login`, que é um fluxo **interativo** — impossível numa execução agendada sem operador presente.

- **Bloqueio para o cliente:** rodar uma vez, num terminal interativo, para destravar GSC/GA4 nas próximas execuções. **Os escopos são obrigatórios** — o `login` sem `--scopes` autentica, mas o token sai só com `cloud-platform` e o Search Console responde `403 ACCESS_TOKEN_SCOPE_INSUFFICIENT` (foi o que aconteceu na primeira tentativa de 2026-08-05):

  ```
  gcloud auth application-default login --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/webmasters.readonly,https://www.googleapis.com/auth/analytics.readonly"
  ```

- **Consequência enquanto durar:** a priorização continua sendo por intenção comercial, sem dados de impressão. A verificação de indexação prevista para ~2026-08-08 (ver seção anterior) **fica pendente até a reautenticação**.

---

## Auditoria — 2026-08-05 (pós-publicação da SEO-014)

Rodada sobre as 8 páginas em produção. **Sem GSC** (credencial expirada — ver "Estado da medição — 2026-08-05"), então a auditoria é de artefato e de cobertura semântica, não de desempenho.

### O que está saudável — não mexer

- **Técnico:** HTTP/2, TLS, `www` → apex 301, `http` → `https` 301, `robots.txt` liberando os crawlers de IA nominalmente, sitemap com as 8 URLs, canonical e hreflang corretos em todas.
- **Estrutura:** 1 `<h1>` por página, 6–9 `<h2>`, **zero páginas órfãs**, zero links internos quebrados, zero imagens sem `alt`.
- **Schema:** `Article` + `FAQPage` + `BreadcrumbList` nas seis páginas-pilar, `ProfilePage` em `/sobre/`, `Person`/`ProfessionalService`/`WebSite`/`SiteNavigationElement` na home. Nó `Person` único em todo o site.
- **Peso:** 32–50 kB por página, CSS inline, sem JS de terceiros além do GA4. Não há problema de Core Web Vitals a resolver — otimizar isso agora seria trabalho sem ganho.

### Fraquezas encontradas

1. **Nenhum conteúdo de segundo nível.** As 7 páginas de conteúdo são todas **pilares**. Nenhum cluster tem spoke. A instrução "expandir clusters antes de criar novos" está sendo violada por omissão: o próximo pilar seria o sexto pilar raso, não profundidade.
2. **Perguntas de decisão de compra mal cobertas.** "Quanto custa" e "honorários" aparecem só em `/assistente-tecnica/`, dentro do FAQ. **"Gratuidade de justiça" não aparece em nenhuma página** — e é exatamente o que trava a nomeação de perito e a contratação de assistente na prática forense.
3. **Metadados acima do limite de exibição em 100% das páginas.** Títulos de 66–84 caracteres (corte em ~60) e meta descriptions de 259–445 (corte em ~155). O texto está bem front-loaded, então o dano é moderado — mas é dano gratuito.
4. **Link interno faltante** — `/pericia-ambiental/` era a única página que não linkava `/pericia-combustiveis/`, seu vizinho tópico mais próximo. **Corrigido nesta execução** (uma linha).

### SEO-015 — Spoke: impugnação de laudo pericial *(selecionada para 2026-08-06)*
- **Descrição:** Página dedicada ao momento de maior urgência do cliente — o advogado com um laudo desfavorável na mão. Cobre o que torna um laudo tecnicamente atacável (vício de método, amostragem inválida, ausência de fundamentação, conclusão que extrapola os quesitos), a diferença entre **pedido de esclarecimentos** (art. 477, §§1º e 2º, do CPC), **impugnação** e **nova perícia** (art. 480), os prazos de cada via, e como o parecer divergente do assistente técnico é instrumentado para sustentar cada uma.
- **URL:** `/impugnacao-laudo-pericial/` (a criar)
- **Categoria:** Conteúdo / Spoke de cluster / Intenção transacional
- **Impacto:** 8 · **Esforço:** 4 · **Confiança:** 8 · **Valor de negócio:** 10
- **Priority Score:** 160
- **Status:** done
- **Descoberto:** 2026-08-05 · **Concluído:** 2026-08-05
- **Por que esta e não um sexto pilar:** é o primeiro conteúdo de segundo nível do site e aprofunda o cluster de maior valor comercial (Assistência Técnica), em vez de abrir mais uma frente rasa. Quem busca "como impugnar laudo pericial" tem prazo correndo — é a consulta de maior urgência e menor concorrência qualificada de todo o mapa.
- **Risco a administrar — canibalização:** `/assistente-tecnica/` já tem a seção "Como um parecer técnico derruba um laudo" e o FAQ "É possível ter assistente técnico depois de entregue o laudo?". A divisão precisa ser explícita: o **pilar** responde *quem, quando e por quê*; o **spoke** responde *como*, com o detalhamento processual e metodológico que não cabe no pilar. Ao publicar, a seção do pilar deve ser encurtada e passar a apontar para o spoke — não duplicada.
- **Implementado:** ~2.500 palavras. Tabela das três vias (base legal × defeito que resolve × prazo); árvore de decisão em três perguntas para escolher a via; as seis famílias de falha que tornam um laudo atacável, cada uma com *o que se demonstra* — o ângulo que o pilar não tinha; anatomia da manifestação em cinco partes; cinco erros que a enfraquecem; e o que resta quando o prazo já passou. `Article` (com `isPartOf` apontando para o pilar) + `FAQPage` (8 itens, paridade verificada por script) + `BreadcrumbList` de três níveis. Title 54 caracteres, description 153 — dentro do limite de exibição, ao contrário das oito páginas anteriores (ver SEO-016).
- **Canibalização resolvida na origem:** a seção "Como um parecer técnico derruba um laudo" do pilar foi **encurtada** — a lista de seis falhas virou um parágrafo-resumo que aponta para o spoke. O pilar responde *quem, quando e por quê*; o spoke responde *como*. Nenhum texto duplicado entre as duas páginas.
- **Card da home realocado:** o quarto card de Insights apontava para a âncora `/assistente-tecnica/#impugnacao-laudos` (solução do SEO-008, quando não havia página própria). Agora aponta para a página, com título e resumo próprios. A âncora continua existindo e não quebrou nada.
- **Links de entrada:** 8 — card da home, "Continue lendo" das sete páginas, mais o link contextual dentro do próprio pilar. `sitemap.xml` e `llms.txt` atualizados.
- **Verificação factual — cinco dispositivos conferidos em fonte antes de publicar:**
  1. **Art. 477, §1º** — prazo **comum de 15 dias** para manifestação das partes; o parecer do assistente técnico é apresentado **no mesmo prazo**. Redação inalterada desde 2015.
  2. **Art. 477, §2º** — dever do perito de esclarecer, em 15 dias, pontos divergentes apontados no parecer do assistente. É o que transforma o parecer em alavanca processual, não em peça decorativa.
  3. **Art. 477, §3º e §4º** — esclarecimentos em audiência, com perguntas formuladas **desde logo sob forma de quesitos**, e intimação do perito com no mínimo **10 dias de antecedência**. Confirmados — é a via de recuperação para quem perdeu o prazo do §1º.
  4. **Art. 480, §1º e §3º** — a segunda perícia tem o mesmo objeto da primeira e **não a substitui**, cabendo ao juiz apreciar o valor de uma e de outra. É a base da tese central da página: a via mais pedida é a mais fraca.
  5. **Art. 479** — o juiz indica na sentença os motivos, **levando em conta o método utilizado pelo perito**. É o que sustenta a orientação de atacar o método, não a conclusão.
- **Nenhuma surpresa nesta verificação** — ao contrário dos SEO-002 (dois pontos desatualizados) e SEO-014 (norma de uma semana). Direito processual civil é bem mais estável que regulação técnica; o custo da checagem foi baixo e continua valendo a pena como rotina.
- **Manutenção:** baixa. Só muda se houver reforma do CPC na parte da prova pericial.

### SEO-016 — Metadados dentro do limite de exibição
- **Descrição:** Reescrever os 8 títulos para ≤ 60 caracteres e as 8 meta descriptions para 150–160, preservando o termo-cabeça no início e acrescentando um diferencial verificável (UNICAMP, CRQ, +8 anos) onde couber.
- **URL:** todas as 8
- **Categoria:** CTR / On-page
- **Impacto:** 5 · **Esforço:** 2 · **Confiança:** 6 · **Valor de negócio:** 6
- **Priority Score:** 90
- **Status:** done · **Descoberto:** 2026-08-05 · **Concluído:** 2026-08-07
- **Por que esperou dois dias:** otimizar CTR **antes de haver impressões** é otimizar no vazio. O item ficou parado por decisão registrada, esperando o gatilho explícito — "página com impressão de dois dígitos e CTR baixo". O gatilho disparou em 07/08 (ver medição abaixo). Ver `### SEO-016 — execução` para o que foi feito.

### SEO-017 — Spoke: honorários, custos e gratuidade de justiça na prova pericial
- **Descrição:** Como se formam os honorários do perito e do assistente técnico, quem adianta, o arbitramento judicial, e o que acontece quando a parte é beneficiária da gratuidade de justiça (hoje **ausente do site inteiro**). Consulta de fundo de funil pura.
- **URL:** `/honorarios-pericia-judicial/` (a criar)
- **Categoria:** Conteúdo / Spoke de cluster / Intenção transacional
- **Impacto:** 7 · **Esforço:** 4 · **Confiança:** 7 · **Valor de negócio:** 9
- **Priority Score:** 110,25
- **Status:** done
- **Descoberto:** 2026-08-05 · **Concluído:** 2026-08-05
- **Decisão do cliente:** **sem preços publicados.** Confirmada antes de escrever. A página explica *como o custo se forma e quem paga* e encaminha para contato. Verificado por script que não há nenhum valor em reais no texto.
- **Implementado:** ~2.280 palavras. A tese organizadora é a distinção que nenhuma página concorrente faz com clareza: **"quanto custa a perícia" são duas contas independentes** — a do perito e a do assistente técnico —, com regimes, prazos e destinos distintos ao final do processo. Tabela comparativa das duas (quem define, quem adianta, quando, gratuidade, recuperação do vencido); o procedimento do art. 465 em quatro passos, com destaque para a **janela de 5 dias do §3º** como o momento mais barato de discutir valor; seção de gratuidade de justiça; o que faz o custo do assistente variar; **quando não vale a pena contratar** (quatro sinais); e checklist do que enviar para receber estimativa — que é o mecanismo de conversão, no lugar de uma promessa de análise gratuita, que não foi criada por ser compromisso de agenda da Adriana, não decisão de SEO.
- **Lacuna fechada:** "gratuidade de justiça" **não aparecia em nenhuma página do site** antes desta. Era o item 2 das fraquezas da auditoria de 2026-08-05.
- **Verificação factual — cinco dispositivos e uma resolução conferidos em fonte:**
  1. **Art. 95, caput** — cada parte **adianta** a remuneração do assistente que indicou; a do perito é adiantada por quem requereu, ou rateada se de ofício/ambas. O verbo é *adiantar*, não pagar — a página explora isso.
  2. **Art. 95, §3º, I e II** — servidor ou órgão público conveniado com recursos do ente público; ou particular pago com recursos da União/Estado/DF, **pela tabela do respectivo tribunal e, na omissão, a do CNJ**. **§5º** veda usar recursos do fundo da Defensoria. Após o trânsito em julgado, o valor é executado contra o condenado às despesas.
  3. **Art. 465, §2º** (5 dias: proposta, currículo, contatos), **§3º** (partes se manifestam em 5 dias comuns, depois o juiz arbitra), **§4º** (até 50% no início, saldo ao final).
  4. **Art. 98, §1º, V e VI** — a gratuidade cobre despesas com exames essenciais e honorários do perito.
  5. **Resolução CNJ nº 232/2016 — vigente, e com uma pegadinha.** Os valores do anexo são **reajustados anualmente em janeiro pela variação do IPCA-E**, e há **grupo de trabalho do CNJ revisando a tabela, com prazo prorrogado em 2026**. Citar o valor nominal de 2016 como vigente é o erro mais comum do conteúdo concorrente — e foi mais uma razão para não publicar números: qualquer valor aqui estaria velho antes do próximo janeiro. A decisão comercial de não publicar preços e a decisão editorial de não citar a tabela nominal convergiram.
- **Um ponto tratado como controverso, e não como pacífico:** o **reembolso dos honorários do assistente técnico pela parte vencida**. A jurisprudência diverge — há decisões que o tratam como consectário da sucumbência e decisões que o classificam como despesa extraprocessual de interesse privado. A página apresenta a divergência e registra o ponto praticamente pacífico (se não foi pedido e decidido no processo, não se cobra depois). **O FAQ do pilar já afirmava "não reembolsados automaticamente"** — continua correto graças ao advérbio, e agora aponta para o tratamento completo.
- **Links de entrada:** 9 — quinto card de Insights na home, "Continue lendo" das oito páginas, mais o link contextual dentro do FAQ de custo do pilar. `sitemap.xml` e `llms.txt` atualizados.
- **Manutenção — uma data a acompanhar:** a **conclusão do grupo de trabalho do CNJ** sobre a tabela de honorários. Se resultar em nova resolução, a seção da tabela precisa ser revista.

---

## Estado da medição — 2026-08-05 (segunda leitura, já com service account)

**Medição destravada.** A autenticação agora é por **service account** (`seo-reader@adriana-seo.iam.gserviceaccount.com`, `siteFullUser`), não mais por ADC de usuário — não expira e funciona em execução agendada. Chave em `~/.config/adrianarezende/seo-sa.json` (fora do repositório, chmod 600). Script de coleta em `~/.config/adrianarezende/seo-report.py`:

```
python3 ~/.config/adrianarezende/seo-report.py 30
```

**Duas armadilhas que custaram tempo — registradas para não se repetirem:**

1. **`gcloud auth application-default login` não resolve.** O ADC usa o client OAuth embutido do próprio gcloud (`764086051850-…`), então escopos adicionados ao consent screen de um client próprio **não têm efeito nenhum** sobre ele. Sem `--scopes`, o token sai só com `cloud-platform` e o Search Console responde `403 ACCESS_TOKEN_SCOPE_INSUFFICIENT`. O caminho que funciona é service account.
2. **A propriedade é de domínio, não de prefixo de URL.** O identificador correto é **`sc-domain:adrianarezende.com.br`**; chamar a API com `https://adrianarezende.com.br/` devolve `403 User does not have sufficient permission`, que parece falta de permissão e **não é**. O script agora consulta `GET /webmasters/v3/sites` e detecta o identificador em vez de supor.

### Indexação — 2026-08-05

| URL | Veredito | Estado | Antes (03/08) |
|---|---|---|---|
| `/` | PASS | Submitted and indexed | PASS |
| `/sobre/` | PASS | Submitted and indexed | — |
| `/assistente-tecnica/` | PASS | Submitted and indexed | Discovered — not indexed |
| `/classificacao-fiscal-ncm/` | PASS | Submitted and indexed | URL unknown to Google |
| `/pericia-contaminacao-alimentos/` | PASS | Submitted and indexed | — |
| `/pericia-ambiental/` | NEUTRAL | Discovered — not indexed | (publicada em 04/08) |
| `/pericia-combustiveis/` | NEUTRAL | Discovered — not indexed | (publicada em 04/08) |
| `/pericia-industria-quimica/` | NEUTRAL | URL unknown to Google | (publicada hoje) |

**Leitura:** **cinco de oito páginas indexadas.** A hipótese registrada em 03/08 — de que a ausência de indexação após ~7 dias indicaria autoridade de domínio insuficiente para justificar o rastreamento — **fica descartada**. Era latência, e a latência observada é de **2 a 4 dias** entre publicação e indexação. Nenhuma ação técnica é necessária; as três páginas restantes devem entrar sozinhas até ~09/08. **Não pedir indexação manualmente** — não acelera e consome quota.

### Desempenho — 2026-08-05

- **3 impressões no período de 30 dias**, todas em 2026-08-03, todas na home, posição média 6,0, **zero cliques**.
- Dimensão `query` **sem linhas** — abaixo do limiar de anonimização do GSC, então não dá para saber se foram buscas pelo nome dela ou ruído residual do histórico do domínio (SEO-010).

**Consequência para a priorização: nenhuma.** Três impressões não sustentam decisão alguma. O **SEO-016 (metadados)** continua parado esperando volume — a regra segue valendo: só vira Prioridade 1 quando houver página com impressão real e clique baixo. **SEO-015 permanece a tarefa selecionada.**

**Pendência:** GA4 ainda não instrumentado no script — falta o ID numérico da propriedade em `~/.config/adrianarezende/ga4-property`. Search Console funciona sem isso.

---

## Estado da medição — 2026-08-06

Coleta por service account (`python3 ~/.config/adrianarezende/seo-report.py 30`), período 2026-07-07 → 2026-08-06.

- **6 impressões no acumulado de 30 dias**, zero cliques: home (3, posição 6,0), `/assistente-tecnica/` (2, posição 5,0), `/classificacao-fiscal-ncm` (1, posição 11,0). Dimensão `query` continua **sem linhas** — abaixo do limiar de anonimização.
- **Indexação: 7 de 10.** Entraram desde 05/08 `/pericia-ambiental/` e `/pericia-combustiveis/` (eram *Discovered — not indexed*). Continuam fora `/pericia-industria-quimica/`, `/impugnacao-laudo-pericial/` e `/honorarios-pericia-judicial/` — todas publicadas há 1–2 dias, dentro da latência de 2 a 4 dias já medida. **Nenhuma ação.**
- **GA4** ainda não instrumentado no script (falta o ID numérico da propriedade em `~/.config/adrianarezende/ga4-property`).

**Consequência para a priorização: nenhuma.** Seis impressões não sustentam decisão. **SEO-016 (metadados) segue parado** — a regra continua sendo que ele só vira Prioridade 1 quando existir página com impressão real e clique baixo. Vale registrar que as três páginas mais novas já nascem com metadados dentro do limite, então o escopo do SEO-016 encolheu de 8 para 7 páginas e vai encolhendo sozinho.

---

## Auditoria — 2026-08-06

Sobre as 10 páginas em produção. Sem dados de desempenho utilizáveis, então é auditoria de artefato e de cobertura semântica.

### O que está saudável — não mexer

- **Zero links internos quebrados, zero páginas órfãs, zero imagens sem `alt`, 1 `<h1>` por página, canonical correto em todas as 10, sitemap idêntico ao sistema de arquivos.** Verificado por script nesta execução.
- **Schema** íntegro nas 10: `Article` + `FAQPage` + `BreadcrumbList` nas páginas de conteúdo, paridade texto-visível ↔ JSON-LD conferida por script.
- **Peso e CWV:** sem JS de terceiros além do GA4, CSS inline. Nada a otimizar com ganho real.

### Fraquezas encontradas

1. **A promessa mais repetida do site não tinha página.** `/assistente-tecnica/` afirma em três lugares distintos que a redação dos quesitos é o momento de maior impacto e que "quesitos mal formulados limitam o alcance de toda a prova pericial" — e nenhuma página explicava **como se formula um quesito**. O site criava a demanda e não a atendia. Resolvido pela SEO-018.
2. **Grafo interno completo (todos ligam a todos).** Com 10 páginas o bloco "Continue lendo" liga cada página a todas as outras, o que não distingue vizinhança tópica de vizinhança qualquer. Ainda não é problema em escala de 10 páginas, mas vira um por volta de 15. Registrado como SEO-019.
3. **SEO-016 (metadados) segue aplicável a 7 páginas**, sem dado que o justifique. Continua parado por decisão, não por esquecimento.

### SEO-018 — Spoke: quesitos periciais *(executada em 2026-08-06)*
- **Descrição:** Como se formula um quesito que produz resposta utilizável — a única peça técnica que a parte escreve *antes* de a perícia existir, e a que define o alcance de tudo o que vem depois.
- **URL:** `/quesitos-periciais/`
- **Categoria:** Conteúdo / Spoke de cluster / Intenção transacional
- **Impacto:** 8 · **Esforço:** 4 · **Confiança:** 8 · **Valor de negócio:** 10
- **Priority Score:** 160
- **Status:** done · **Descoberto:** 2026-08-06 · **Concluído:** 2026-08-06
- **Por que esta:** "Quesitos Periciais" está na lista de serviços-alvo e é a consulta em que o cliente ideal (advogado com prazo de 15 dias correndo) tem urgência máxima. O pilar já vinha afirmando três vezes que é o momento decisivo sem nunca ensinar a fazê-lo — a lacuna mais gritante do site, e a única em que a própria página existente cria a demanda que não atende. Aprofunda o cluster de maior valor comercial em vez de abrir um sexto pilar raso.
- **Implementado:** ~2.850 palavras. A tese organizadora é uma assimetria que o conteúdo concorrente (quase todo banco de modelos para copiar) não formula: **o art. 473, IV obriga o perito a dar resposta conclusiva a todos os quesitos, e o art. 473, §2º o proíbe de ultrapassar a designação e de opinar.** Daí decorre que a pergunta mais comum em processos técnicos — "houve negligência?" — não é apenas fraca: é uma pergunta que o perito está **legalmente impedido de responder**. Estrutura: tabela das três janelas para perguntar (inicial art. 465 §1º III / suplementar art. 469 / esclarecimento art. 477 §§1º-3º) com a assimetria explícita — só a primeira *define* o objeto, as outras duas *reagem* a ele; os dois limites legais que anulam uma pergunta (arts. 470, I e 473, §2º); as quatro partes de um quesito eficaz; **tabela de quatro quesitos reformulados, antes e depois**, um por matéria (alimentos, NCM, ambiental, combustíveis); a sequência de cinco perguntas que expõe o método; seis defeitos; e quando o problema não se resolve com quesitos (prova técnica simplificada do art. 464 §§2º-4º e dispensa da perícia pelo art. 472).
- **Por que a tabela antes/depois é o ativo da página:** é a única seção que nenhum concorrente tem e que **serve os cinco clusters ao mesmo tempo** — cada linha demonstra domínio de uma matéria diferente com norma nomeada. Faz da página um hub que reforça todo o site, não só o cluster processual.
- **Canibalização — sem sobreposição a resolver.** Ao contrário da SEO-015, o pilar não ensinava a formular quesitos; apenas afirmava que importava. Nada foi encurtado, porque não havia conteúdo duplicado — só uma promessa pendente, que agora aponta para a página que a cumpre. Os dois trechos do pilar que falavam de quesitos viraram links contextuais.
- **Links de entrada:** 12 no total, vindos de 10 páginas — sexto card de Insights na home, "Continue lendo" das nove demais, mais dois links contextuais dentro do pilar (caixa "Ponto de atenção" e item "Quesitos suplementares" do calendário) e um dentro de `/impugnacao-laudo-pericial/`. `sitemap.xml` e `llms.txt` atualizados.
- **Ligação de cluster deliberada:** a sequência de cinco perguntas que expõe o método corresponde quase uma a uma às seis famílias de falha da `/impugnacao-laudo-pericial/`, e o texto diz isso explicitamente — fazer a pergunta antes é o que viabiliza a crítica depois. As duas spokes passam a se sustentar mutuamente em vez de apenas coexistirem.
- **Verificação factual — seis dispositivos conferidos no texto literal da lei antes de publicar** (o Planalto recusou a requisição; usado PDF oficial da Seção X do CPC, texto extraído e lido na íntegra):
  1. **Art. 465, §1º, I a III** — os três atos (impedimento/suspeição, indicação de assistente, quesitos) vencem no **mesmo prazo de 15 dias**. É o detalhe de calendário que a página explora: a parte gasta o prazo escolhendo o assistente e redige os quesitos por último, sem que ele tenha lido os autos.
  2. **Art. 469** — quesitos suplementares **durante a diligência**, respondidos previamente ou na AIJ; o escrivão dá ciência da juntada à parte contrária.
  3. **Art. 470, I e II** — dever do juiz de indeferir quesitos impertinentes e faculdade de formular os que entender necessários.
  4. **Art. 473, IV** — resposta **conclusiva a todos** os quesitos. É a base da tese central.
  5. **Art. 473, §2º** — vedação de ultrapassar a designação e de emitir opiniões pessoais que excedam o exame técnico. Idem.
  6. **Art. 473, III** — o laudo deve indicar o método **e demonstrar que é predominantemente aceito** pelos especialistas da área. É o que dá lastro à sequência de cinco perguntas.
  - Conferidos ainda **art. 464, §§2º a 4º** (prova técnica simplificada, com a exigência de formação acadêmica específica do especialista) e **art. 472** (dispensa da perícia por pareceres técnicos juntados na inicial e na contestação).
- **Normas técnicas citadas na tabela — conferidas em fonte e cruzadas com as páginas existentes:**
  - **Alimentos:** a página cita **IN ANVISA nº 161/2022** (que carrega as tabelas de padrões microbiológicos) observada a **RDC nº 724/2022** (que dispõe sobre sua aplicação), ambas publicadas em 01/07/2022 e **em vigor desde 01/09/2022**. A distinção entre as duas é justamente o tipo de precisão que um quesito exige. Não conflita com `/pericia-contaminacao-alimentos/`, que trata de outras RDCs (275/2002, 216/2004, 655/2022) e não cobria o padrão microbiológico.
  - **Ambiental:** **CONAMA nº 420/2009**, consistente com `/pericia-ambiental/`. O quesito acrescenta a ressalva dos **valores orientadores estaduais quando existentes e mais restritivos** — a camada CETESB que a página ambiental já documenta.
  - **Combustíveis e NCM:** referências genéricas e estáveis ("especificação da ANP vigente na data da coleta", RGI e Notas de Seção/Capítulo), deliberadamente sem número de resolução, para não criar um ponto de manutenção redundante com as páginas que já os detalham.
- **Nenhuma surpresa na verificação processual** — o CPC na parte da prova pericial segue sem alteração, confirmando o padrão registrado na SEO-015. As surpresas continuam concentradas em regulação técnica (SEO-002, SEO-014), não em direito processual.
- **Validação executada:** title 59 caracteres, description 156 (dentro do limite de exibição); os três blocos JSON-LD parseiam; **paridade FAQ conferida por script** — as 8 perguntas e as 8 respostas do `FAQPage` são idênticas, caractere a caractere, ao texto visível; HTML balanceado (parser sem tags pendentes); zero links internos quebrados no site inteiro; sitemap idêntico ao sistema de arquivos; canonical correto nas 10 páginas; nenhuma página órfã; as duas tabelas cabem sem overflow horizontal em desktop e têm contêiner com rolagem em telas estreitas. Renderização conferida no navegador.
- **Manutenção:** baixa no processual. O ponto a acompanhar é a **IN ANVISA nº 161/2022**, que é a única norma com número e ano citada na tabela e a mais sujeita a revisão.

### SEO-019 — Diferenciar o bloco "Continue lendo" por proximidade tópica
- **Descrição:** Hoje cada página lista **todas** as outras no "Continue lendo". Com 10 páginas ainda funciona como navegação, mas não transmite hierarquia: um link do pilar de alimentos para o de combustíveis pesa o mesmo que para sua própria spoke. Substituir por 3–4 links de vizinhança real (mesma matéria + spokes do cluster) e mover o restante para um índice compacto no rodapé.
- **URL:** todas
- **Categoria:** Links internos / Arquitetura de cluster
- **Impacto:** 4 · **Esforço:** 3 · **Confiança:** 5 · **Valor de negócio:** 5
- **Priority Score:** 33,3
- **Status:** done · **Descoberto:** 2026-08-06 · **Concluído:** 2026-08-12 (segunda execução do dia) · **Reavaliado:** Impacto 7 · Esforço 4 · Confiança 6 · Valor 8 → **Priority Score 84**
- **Por que não era a tarefa de 06/08 (avaliação original, mantida para registro):** score baixo e o problema ainda é teórico em 10 páginas — o grafo completo até ajuda a distribuir rastreamento num domínio novo. Vira relevante por volta de 15 páginas, ou antes disso se o GSC mostrar páginas recebendo tráfego irrelevante entre clusters.
- **Ver a execução de 2026-08-12 (segunda)** mais abaixo para o que foi implementado e por que o score subiu de 33,3 para 84.

---

## Estado da medição — 2026-08-27

**Primeira coleta com sinal utilizável.** Período 28 dias, service account.

- **484 impressões · 5 cliques · 15 de 15 páginas indexadas (PASS em todas).** Não há mais pendência de indexação: o item que vinha sendo acompanhado desde 03/08 está encerrado.
- **Crescimento real na quinzena** (14 dias anteriores → 14 dias recentes): `/quesitos-periciais/` 49 → 128 impressões (pos 10,3 → 9,5); `/impugnacao-laudo-pericial/` 15 → 69 (pos 17,5 → 12,7); `/honorarios-pericia-judicial/` 9 → 32; `/normas-tecnicas-pericia/` 0 → 31 já em **pos 4,3**; `/cpc-prova-pericial/` 0 → 9. O volume quase triplicou.
- **GA4:** 67 sessões, das quais **6 de Organic Search**. Ainda não há base para otimizar conversão — Prioridade 1 do mandato continua sem dado que a sustente.

### O achado estrutural: a cauda ranqueia, a cabeça não

Cruzando `query × page` (90 dias), o padrão se repete em dois clusters independentes, **na mesma página**:

| Consulta | Página | Posição |
|---|---|---|
| impugnação ao laudo pericial **cpc** | `/impugnacao-laudo-pericial/` | **9,0** |
| impugnação ao laudo pericial | idem | 26,8 |
| impugnação de laudo pericial | idem | 44,0 |
| **prazo** apresentacao quesitos | `/quesitos-periciais/` | **12,0** |
| emitir **despacho** - sem quesitos | idem | **9,4** |
| quesitos | idem | 40,3 |
| apresentação de quesitos | idem | 46,5 |

**Leitura:** o Google confia nestas páginas para a consulta *qualificada* (com artigo, prazo, ato processual) e não para o termo-cabeça comercial, onde a SERP é ocupada por portais jurídicos de alta autoridade. A média da página (13,5 e 9,7) vem da cauda anonimizada, não da cabeça.

**Consequência para a estratégia:** o retorno mais rápido está em **ser mais específico**, não mais abrangente — e de preferência em terreno onde a autoridade da concorrência não é jurídica. As duas páginas de melhor posição do site (`/normas-tecnicas-pericia/` 4,3 e `/pericia-industria-quimica/` 4,0) e a de melhor CTR (`/pericia-combustiveis/`, 8,7% em pos 6,3) são exatamente as mais técnicas e mais estreitas. As mais amplas e mais jurídicas são as que ficam em 27–47.

### Mobile: o sinal pré-registrado não se confirmou nem se desmentiu

O item 8 da lista anterior previa ler o primeiro clique móvel por volta de 01/09 como veredito sobre SEO-035/SEO-036.

- **MOBILE:** 127 impressões · **0 cliques** · pos **8,7**
- **DESKTOP:** 354 impressões · 5 cliques · CTR 1,41% · pos 10,3

As impressões móveis subiram de quase nada para 127, com posição *melhor* que a do desktop. Mas **0 de 127 não é anomalia estatística**: a uma CTR móvel plausível de ~0,8% na posição 8,7 (a CTR móvel é sistematicamente menor que a desktop na mesma posição nominal, por causa da coluna única e dos blocos de AI Overview e PAA acima), o esperado seria ~1 clique. Observar zero tem probabilidade ~0,36. **A amostra não distingue as hipóteses.** Não se pode dizer que o layout resolveu, nem que não era a causa. Fica pendente até haver ~400 impressões móveis.

**O desdobramento previsto para SEO-016 (título/descrição na SERP móvel) foi verificado e descartado:** os 15 títulos (49–64 caracteres) e as 15 descriptions (156–168) foram inspecionados um a um. Estão front-loaded, dentro ou muito perto do limite de exibição e são melhores que os da concorrência. **SEO-016 está materialmente concluído** — não há reescrita de metadado com ganho esperável, e insistir nele seria trabalho cosmético. Encerrado.

---

## Auditoria — 2026-08-27

Sobre as 15 páginas em produção. `deploy` e `valid` passaram integralmente antes de qualquer alteração: 0 commits pendentes, sitemap em dia, 15 URLs em 200, e as 15 páginas sem falha de título, description, canonical, `h1`, JSON-LD, link interno, órfã ou paridade de FAQ.

### O que está saudável — não mexer

- **Técnico e estrutural:** nada a corrigir. Não há ganho disponível em metadado, schema, link interno, sitemap, robots, `llms.txt` (que cobre as 15 páginas) ou indexação. **Não restava "melhoria fácil de ranking"** — a regra do mandato de não criar conteúdo enquanto houver ganho fácil disponível foi verificada e liberada, não presumida.
- **AI crawlers** nominalmente liberados no `robots.txt` (GPTBot, ClaudeBot, Google-Extended, PerplexityBot, anthropic-ai, Amazonbot, Applebot).

### Três hipóteses de página nova testadas contra o conteúdo existente — e descartadas

Registrado para que execuções futuras não as reproponham:

1. **Página de "parecer técnico".** Motivação aparente forte: a expressão aparece **24 vezes** em `/assistente-tecnica/`, é serviço nomeado no mandato e não tem página. **Descartada:** o pilar já *ensina* o parecer — definição, tabela laudo × parecer (quem assina, base legal, objeto, prazo, efeito), a seção "as sete partes de um parecer que o juízo consegue usar", os poderes do art. 473, §3º e o uso antecipado do art. 472, além de 4 entradas de FAQ. Diferente do caso da SEO-018 (quesitos), em que o pilar apenas *afirmava* a importância sem ensinar. Aqui a canibalização seria severa.
2. **Página de "prazos da perícia".** **Descartada:** `/cpc-prova-pericial/` já traz a tabela única com os 11 prazos da fase pericial, incluindo os arts. 95 e 98 fora do bloco 464–480.
3. **Página de "recall / recolhimento de produto".** **Descartada:** o tema aparece 14 vezes em `/pericia-contaminacao-alimentos/`, com a RDC 655/2022 tratada na seção de normas.

### A lacuna real

**"Produtos Químicos Controlados" é serviço nomeado no mandato, não tem página, e o que existe está no contêiner errado.** A cobertura vivia inteiramente dentro de `/pericia-industria-quimica/` — uma `<h2>`, uma `<h3>` e duas entradas de FAQ — enquadrada como *uma das quatro famílias de litígio industrial*. Quem procura o regime de licenciamento, a obrigação de escrituração ou o que fazer com uma autuação recém-recebida não está procurando uma página sobre acidente de processo. Público distinto (empresa, não advogado), intenção distinta (conformidade e defesa administrativa, não perícia judicial) e concorrência distinta (consultorias de compliance, não portais jurídicos).

### SEO-037 — Spoke: produtos químicos controlados *(executada em 2026-08-27)*
- **Descrição:** Os dois regimes federais de controle de produto químico, as obrigações de cada um, o que mudou com a IN DG/PF nº 338/2026 e a defesa técnica da autuação escritural.
- **URL:** `/produtos-quimicos-controlados/`
- **Categoria:** Conteúdo / Spoke de cluster / Conformidade e defesa administrativa
- **Impacto:** 8 · **Esforço:** 4 · **Confiança:** 8 · **Valor de negócio:** 9
- **Priority Score:** 144
- **Status:** done · **Descoberto:** 2026-08-27 · **Concluído:** 2026-08-27
- **Por que esta:** aprofunda o cluster de Indústria Química, que tinha **uma única página**, em vez de abrir frente nova; é serviço nomeado no mandato sem página; e vai para o tipo de terreno que os dados de hoje mostram ser o mais produtivo para este domínio — técnico, estreito e sem concorrência de portal jurídico. As alternativas de Prioridade 1 e 2 foram avaliadas e não tinham lastro: conversão não tem dado (6 sessões orgânicas) e a melhoria fácil de ranking não existe (auditoria integralmente limpa).
- **Implementado:** ~3.540 palavras. Tabela comparativa dos dois regimes em seis dimensões; tabela das nove obrigações da Lei nº 10.357/2001 artigo a artigo; as treze infrações do art. 12 em lista numerada; as cinco medidas do art. 14; a seção dos trinta dias do art. 15; o regime do Exército com a revogação das dispensas; **a tabela das quatro hipóteses de divergência escritural, com mecanismo físico e forma de demonstração de cada uma**; e a seção de enquadramento por concentração. `Article` (com `isPartOf` apontando para o pilar) + `FAQPage` (8 itens) + `BreadcrumbList` de três níveis, com o `@id` canônico do `Person`.
- **A tese que a página tem e a concorrência não:** *uma divergência sistemática tem assinatura física; um desvio, não.* Perda por evaporação é proporcional ao volume operado e reprodutível período a período; erro de conversão é constante em percentual; desvio é episódico e não guarda relação com variável de processo. Demonstrar a **regularidade do padrão** é, em si, prova de que a diferença é escritural. É o argumento que só um engenheiro químico formula, e é o ativo da página.
- **Paridade de FAQ garantida por construção, não por conferência:** as 8 perguntas e respostas foram definidas uma única vez em estrutura de dados, e o HTML visível e o JSON-LD foram **gerados da mesma fonte**. Conferido depois por script: idênticos caractere a caractere. Método melhor que o das páginas anteriores (escrever duas vezes e comparar) — vale repetir.
- **Canibalização resolvida na origem, no padrão da SEO-015:** a `<h3>` "As autuações mais comuns são escriturais" do pilar foi **encurtada** de lista de quatro itens para um parágrafo-resumo que aponta para a spoke, e o parágrafo operacional sobre a IN 338/2026 (SIPROQUIM, CRC/CLF, prazo dos mapas, retificação) foi condensado ao essencial. O pilar mantém a tabela dos dois órgãos, porque ela é contexto das quatro famílias de litígio. **Nenhum texto duplicado entre as duas páginas.**
- **Regra de negócio da cliente preservada:** o pilar declara em caixa própria que a atuação **não é consultoria regulatória de rotina** (licença, cadastro, escrituração periódica são compliance, não prova técnica). Como a página nova fala de obrigações de conformidade, ela **repete a delimitação de escopo** e o CTA vende defesa técnica e laudo, não licenciamento. Sem isso, a página atrairia demanda que a cliente não atende.
- **Links de entrada:** 5 páginas — card de Insights na home, dois links contextuais dentro do pilar, e "Continue lendo" de `/classificacao-fiscal-ncm/` (autuação e enquadramento administrativos) e `/normas-tecnicas-pericia/` (índice de normas). Vizinhança tópica real, no critério da SEO-019 — não foi adicionada a todas as páginas. `sitemap.xml` e `llms.txt` atualizados, com a lista de Serviços do `llms.txt` passando a nomear "Produtos Químicos Controlados" como serviço próprio.

- **Verificação factual — texto literal da lei e fonte oficial antes de publicar. Duas correções e uma confirmação que a memória interna errava:**
  1. **Multa: R$ 2.128,20 a R$ 1.064.100,00** (art. 14, V da Lei nº 10.357/2001, lido no Planalto). **O "até R$ 350 mil" que circula na cobertura secundária da IN 338/2026 — e que estava na nota do SEO-014 neste backlog — não corresponde à lei.** A página oficial da PF confirma a mesma faixa. Instrução normativa **dosa** a multa; não pode ampliar teto legal. Corrigido aqui e não propagado.
  2. **Decreto nº 10.030/2019 segue vigente no que importa.** Havia risco real de erro: buscas indicam que o Decreto nº 11.615/2023 "revogou o Decreto nº 10.030/2019". Lido o texto no Planalto, **o art. 83 do D. 11.615/2023 revoga dispositivos do Decreto nº 9.847/2019** (armas), e as revogações internas ao D. 10.030 atingem seus **arts. 2º a 4º, que alteravam outros decretos sobre armas de fogo**. O **art. 1º, que aprova o R-105, não foi revogado** — e o próprio D. 11.615 remete ao "Regulamento de Produtos Controlados" como norma existente. A citação do site estava certa; a fonte secundária é que induzia ao erro.
  3. **As dispensas de registro do art. 7º, §1º do R-105 foram revogadas pelo Decreto nº 11.366/2023** — inclusive a de quem usava PCE apenas eventualmente. Achado próprio da leitura do texto integral, ausente do material de orientação disponível, que ainda as descreve como vigentes. É o ponto mais acionável da seção do Exército.
  4. **IN DG/PF nº 338/2026: assinada em 29/07/2026, publicada no DOU em 03/08/2026**, vigente da publicação. Revogou as INs nº 166/2020 e nº 211/2021 e **não alterou a lista de produtos**, que segue na Portaria MJSP nº 204, de 21/10/2022. Novidades: PAI instaurado **só quando constatada a infração**, critérios de pena-base com atenuantes e agravantes, consolidação no SIPROQUIM2. Fonte: página oficial da PF em gov.br.
  5. **Prazo dos mapas confirmado, depois de quase ter sido removido.** A afirmação do pilar — mapas mensais até o **décimo quinto dia do mês subsequente** — não constava da lei (o art. 9º remete a portaria) e por isso foi tratada como não verificada e deixada de fora da primeira versão da página. Confirmada nas páginas de SIPROQUIM2 do gov.br/pf, junto com os instrumentos **CRC** e **CLF**, e então **acrescentada** à página. *Não verificado ainda não é falso — vale um segundo esforço de busca antes de descartar um dado útil.*
  - Conferidos ainda, no texto do Planalto: arts. 4º a 10 (licença, autorização especial, renovação anual, licenciamento de todas as partes, comércio exterior, escrituração, suspensão), art. 12, I a XIII (as treze infrações) e art. 15 (trinta dias para sanar, destinação do produto não regularizado, destinação imediata em risco iminente).
- **O único ponto deixado deliberadamente sem número:** a lista de PCE do Exército é descrita como "elaborada e atualizada pelo Comando do Exército", sem citar portaria específica, porque não foi possível confirmar em fonte primária qual está vigente. Melhor uma referência genérica correta do que um número que envelhece errado — a lição do SEO-002.
- **Vantagem competitiva com prazo:** a IN 338/2026 tem menos de um mês. O material de orientação disponível ainda descreve o regime das INs 166/2020 e 211/2021, e a revogação das dispensas do R-105 (2023) segue mal documentada na web. Janela real, mas curta.
- **Manutenção:** rever se a **Portaria MJSP nº 204/2022** for substituída — é ela que lista os produtos e é o ponto que muda com mais frequência. A faixa de multa só muda por lei.

### Verificação de renderização — e um falso "OK" que quase passou

Medição em Chrome real (Playwright, `channel="chrome"`) contra `http://localhost:8899`, a 375 px e 1280 px, em vez do harness de iframes.

- **Sem overflow horizontal em nenhuma página, nas duas larguras:** `scrollWidth == clientWidth` (375 e 1280), com `innerWidth == clientWidth` confirmando a validade da leitura (regra do SEO-033). As tabelas ultrapassam 375 px **dentro do `.table-scroll`**, que é o comportamento desejado — e o mesmo padrão medido, na mesma sessão, em `/pericia-industria-quimica/` e `/laudo-pericial/`, que são páginas boas conhecidas (controle do SEO-034).
- **9 de 9 âncoras assentam em y = 112 px**, abaixo do cabeçalho fixo de 98 px. `scroll-margin-top: 7rem` clonado corretamente.
- **A primeira medição de âncora deu "9/9 OK" e estava errada.** Reportava o texto em y = 365, 1399, 4080… — valores que só podem significar que o salto não aconteceu. A segunda tentativa, com recarga completa por âncora, ainda errava: o déficit **crescia com a distância** (135, 345, 798 … 4057 px), assinatura de `scroll-behavior: smooth` ainda em animação quando a medição ocorreu. Só a terceira, esperando `scrollY` estabilizar, deu o número real e constante.
- **Regra nova, que generaliza o item 5 anterior:** *um resultado uniforme demais ("tudo OK") merece a mesma desconfiança que um resultado idêntico ao anterior.* E, especificamente: **com `scroll-behavior: smooth`, nenhuma medição de posição vale antes de `scrollY` parar de mudar.** O harness de iframes não tinha essa espera — o Playwright com espera de estabilização substitui os dois arquivos de `scratchpad/` com vantagem, porque elimina o problema de cache por construção.

### Próxima execução — o que checar primeiro

1. **Rodar `tools/seo-report.py` em `deploy`, `valid` e `gsc` separados, antes de decidir qualquer coisa.** Hoje as três passaram limpas e foi isso que **liberou** a criação de conteúdo: a regra do mandato é não criar página enquanto houver ganho fácil de ranking, e "não há ganho fácil" precisa ser verificado, não presumido.
2. **A verificação de renderização agora é Playwright com Chrome real, não o harness de iframes.** `pw.chromium.launch(channel="chrome")` — o browser do Playwright não está instalado, o Chrome do sistema está. Mede overflow (`scrollWidth` vs `clientWidth`, com `innerWidth == clientWidth` como validade) e âncoras. **Esperar `scrollY` estabilizar antes de medir posição**, senão o `scroll-behavior: smooth` devolve número errado que cresce com a distância. Os dois arquivos de `scratchpad/` estão obsoletos.
3. **Desconfiar de resultado uniforme, não só de resultado repetido.** "9/9 OK" foi falso duas vezes hoje antes de ser verdadeiro. Um número que não varia quando deveria variar é tão suspeito quanto um número idêntico ao da medição anterior.
4. **SEO-016 está encerrado** — os 15 títulos e descriptions foram inspecionados e estão bons. Não reabrir por hábito.
5. **Indexação está 15/15.** Parar de tratá-la como pendência aberta; verificar só quando entrar página nova.
6. **O sinal móvel ainda não decide nada.** 127 impressões, 0 cliques, pos 8,7 — estatisticamente compatível com CTR normal. **Só voltar ao assunto com ~400 impressões móveis**, por volta de meados de setembro. Não tirar conclusão sobre SEO-035/SEO-036 antes disso, em nenhuma direção.
7. **`/produtos-quimicos-controlados/`: primeira leitura a partir de ~05/09.** Consultas a vigiar: `produtos químicos controlados`, `licença polícia federal produtos químicos`, `mapa de controle siproquim`, `autuação produto controlado`, `IN 338/2026`. **Conferir canibalização com `/pericia-industria-quimica/` por `query × page`** antes de concluir qualquer coisa — foi de lá que o conteúdo saiu.
8. **A hipótese estratégica a testar é a da especificidade.** Os dados de hoje dizem que este domínio ranqueia 4–13 em consulta técnica qualificada e 27–47 em termo-cabeça jurídico. Se a página nova confirmar (entrar direto abaixo de 10 em consulta de conformidade), **a fila seguinte é técnica, não processual** — e os candidatos naturais são os temas ainda presos dentro de pilares: **HACCP/APPCC como sistema de prova**, **análise laboratorial e acreditação ISO/IEC 17025**, e **rotulagem**. Se não confirmar, a limitação é de autoridade de domínio, e aí o trabalho vira aquisição de citação e menção, não mais conteúdo.
9. **Quando os cliques saírem de um dígito, a prioridade inverte** — de exposição para conversão. `/quesitos-periciais/` (177 impressões, CTR 0,6%, pos 9,7) segue primeira da fila, e `/impugnacao-laudo-pericial/` (84, pos 12,7) segunda.
10. **Gerar FAQ visível e JSON-LD da mesma fonte de dados**, como na SEO-037, em vez de escrever duas vezes e conferir depois. Elimina a classe de erro em vez de detectá-la.
11. **Ao citar norma, separar o que a lei fixa do que a regulamentação dosa.** O erro dos "R$ 350 mil" entrou aqui por cobertura secundária de uma IN; a faixa estava na lei o tempo todo. E **não verificado não é falso**: o prazo dos mapas quase foi descartado por não estar na lei, e estava na fonte oficial da PF.
12. **Escalar o Google Ads sem entrega.** Décima execução como nota de rodapé. **Não é item de SEO e não se resolve no backlog** — cabe uma mensagem direta à cliente.

---

## Auditoria — 2026-08-28

`deploy` e `valid` passaram integralmente antes de qualquer alteração: 0 commits pendentes, sitemap em dia, **16 URLs em 200 e 16 de 16 páginas indexadas** — `/produtos-quimicos-controlados/`, publicada ontem, já entrou como "Enviada e indexada". Nenhuma falha de título, description, canonical, `h1`, JSON-LD, link interno, órfã ou paridade de FAQ.

### Medição: crescimento continua, conversão continua sem base

- **543 impressões · 5 cliques em 28 dias** (era 484 · 5 em 27/08). `/quesitos-periciais/` 200 impressões (pos 9,9), `/impugnacao-laudo-pericial/` 87 (13,4), `/assistente-tecnica/` 72 (9,8), `/honorarios-pericia-judicial/` 45 (10,3), `/normas-tecnicas-pericia/` 37 já em **pos 4,2**.
- **GA4: 70 sessões, 8 de Organic Search.** A Prioridade 1 do mandato (conversão em página de alta impressão) segue **sem dado que a sustente** — 8 sessões orgânicas não distinguem hipótese nenhuma. Verificado, não presumido.
- **Nenhum ganho fácil de ranking disponível.** O cruzamento `query × page` a 90 dias devolve 24 linhas somando 44 impressões das 543 (o resto é anonimizado), e **todas** são do cluster jurídico-processual já coberto. Não há consulta em posição 5–20 apontando para tema que uma página existente cubra pela metade — que é a única forma de a Prioridade 2 ter alavanca. Liberada a criação de conteúdo.

### A hipótese da especificidade tem confirmação independente da página de ontem

O item 8 da execução anterior condicionava a fila seguinte à primeira leitura de `/produtos-quimicos-controlados/`, prevista para ~05/09. **Essa leitura continua pendente e não foi antecipada.** Mas a escolha do *terreno* não dependia dela: as duas melhores posições do site (`/normas-tecnicas-pericia/` 4,2 e `/pericia-industria-quimica/` 4,3) e a melhor CTR (`/pericia-combustiveis/`, 8,7% em pos 6,4, com 2 dos 5 cliques do site) são as três páginas mais técnicas e mais estreitas; as mais amplas e mais jurídicas seguem em 27–47. O sinal já existia antes da página de ontem e não depende dela.

### Duas das três candidatas pré-registradas foram descartadas na leitura do conteúdo existente

Registrado para que execuções futuras não as reproponham:

1. **HACCP/APPCC como sistema de prova.** **Descartada.** `/pericia-contaminacao-alimentos/` tem `<h2>` própria ("APPCC: o mapa da fábrica onde a falha pode ter ocorrido") que *ensina* o sistema — o que ele identifica, o valor probatório duplo do registro bem mantido, e o uso na apuração de etapa —, mais entrada de FAQ e presença na tabela dos três tipos de contaminação e na lista de "como a perícia atua". Mesmo perfil do "parecer técnico" descartado em 27/08: já ensinado, não apenas afirmado. Canibalização severa.
2. **Análise laboratorial e acreditação ISO/IEC 17025.** **Descartada como página própria, e incorporada.** O tema aparece em 5 páginas e tem seção dedicada ("Cadeia de custódia da amostra") no pilar de alimentos. Não é assunto de página: é *método*, e vale mais aplicado a um caso concreto. Foi para dentro da página de hoje como exame de método, escopo de acreditação e incerteza dentro do processo de contraprova.
3. **Rotulagem. Selecionada** — ver abaixo.

### A lacuna real

**A rotulagem estava coberta só na dimensão da data.** `/prazo-validade-alimentos/` tem a seção "O que a rotulagem obriga — e o que ela não obriga", mas ela trata exclusivamente da declaração de validade: precisão exigida, isenções, condicionamento às instruções de conservação. Fora isso, o site tinha **zero cobertura** de rotulagem nutricional (RDC 429/2020 e IN 75/2020 não eram citadas em nenhuma das 16 páginas), de advertência de alérgenos e lactose, e — o mais relevante — **do regime sancionatório e processual da Lei nº 6.437/1977**, que é o que rege qualquer autuação sanitária de alimento e não estava em lugar nenhum.

### SEO-038 — Spoke: rotulagem de alimentos, autuação e perícia de contraprova *(executada em 2026-08-28)*
- **Descrição:** As duas naturezas de uma autuação de rótulo e as provas opostas que cada uma exige; as normas vigentes de rotulagem geral e nutricional; o regime sancionatório e os prazos da Lei nº 6.437/1977; e a perícia de contraprova do art. 27.
- **URL:** `/rotulagem-alimentos/`
- **Categoria:** Conteúdo / Spoke de cluster / Defesa administrativa sanitária
- **Impacto:** 8 · **Esforço:** 4 · **Confiança:** 8 · **Valor de negócio:** 9
- **Priority Score:** 144
- **Status:** done · **Descoberto:** 2026-08-28 · **Concluído:** 2026-08-28
- **Por que esta:** aprofunda o cluster de Alimentos (que tinha duas páginas) em vez de abrir frente nova; é terreno técnico e estreito, com concorrência de consultoria de rotulagem e não de portal jurídico — o tipo de SERP em que este domínio ranqueia 4–13 em vez de 27–47; e cobre um público que o site não alcançava, a **empresa autuada**, distinto do advogado em perícia judicial. Prioridades 1 e 2 foram verificadas e não tinham alavanca (ver acima).
- **Implementado:** ~4.510 palavras. Tabela das duas naturezas de autuação em cinco dimensões; tabela de competência Anvisa × MAPA × via consumerista; tabela dos três limites da declaração frontal; tabela da faixa de multa cruzada com o critério de classificação do art. 4º; tabela dos sete prazos do processo administrativo sanitário; a perícia de contraprova em oito passos numerados; sete quesitos. `Article` (com `isPartOf` no pilar de alimentos) + `FAQPage` (8) + `BreadcrumbList` de três níveis, com o `@id` canônico do `Person`.

- **A tese que a página tem e a concorrência não:** *toda autuação de rotulagem é documental ou analítica, e as duas se defendem com provas opostas.* Na documental não existe amostra a reexaminar — requerer contraprova ali só consome os quinze dias de defesa. Na analítica existe um direito que caduca em silêncio: não requerer a contraprova torna o laudo condenatório definitivo. O material disponível na web trata "autuação de rotulagem" como bloco único, e é por isso que a classificação vale mais que qualquer checklist de conformidade.
- **A segunda tese, que só um engenheiro formula:** *um resultado analítico diferente do declarado não é, por si, divergência.* O valor de rótulo carrega variabilidade de matéria-prima e processo, a incerteza expandida do método e o arredondamento da própria IN 75/2020; só há infração quando a diferença **excede a incerteza combinada**, e isso é demonstração estatística, não retórica. É a mesma família de argumento da SEO-037 (assinatura física de uma divergência sistemática), aplicada a outro regime.
- **Paridade de FAQ garantida por construção**, no método da SEO-037: as 8 perguntas foram definidas uma vez em estrutura de dados e o HTML visível e o JSON-LD foram gerados da mesma fonte. Conferido depois por script: idênticos.
- **Delimitação de escopo repetida, como manda a regra de negócio da cliente:** a página fala de obrigações de conformidade, então declara em caixa própria que elaborar layout de rótulo, calcular tabela nutricional para lançamento e manter conformidade periódica **são consultoria regulatória, não o objeto do trabalho**. O CTA vende exame de laudo, parecer de incerteza, atuação como perita indicada na contraprova e quesitos.
- **Canibalização resolvida na origem:** `/prazo-validade-alimentos/` **não perdeu conteúdo** — a divisão é limpa por natureza (aquela página trata da *data*, esta das *demais* exigências e do processo sancionatório), então bastou um parágrafo de fronteira explícita apontando para a nova página. Diferente da SEO-037, em que houve texto a encurtar no pilar.
- **Links de entrada:** 4 páginas — card de Insights na home, link contextual + "no mesmo tema" em `/pericia-contaminacao-alimentos/`, parágrafo de fronteira + "no mesmo tema" em `/prazo-validade-alimentos/`, e entrada em "Onde cada norma é aplicada" de `/normas-tecnicas-pericia/`. Vizinhança tópica real (critério da SEO-019); não foi adicionada a todas as páginas. `sitemap.xml` e `llms.txt` atualizados, com "Rotulagem de Alimentos" passando a serviço próprio na lista do `llms.txt`.

- **Verificação factual — texto literal da lei e da norma antes de publicar. Três correções à memória interna, duas delas de classe grave:**
  1. **A RDC nº 26/2015 não é mais a norma de alérgenos.** O art. 40 da RDC nº 727/2022 a revogou expressamente, junto com a RDC nº 259/2002, a 123/2004, a 340/2002, a 35/2009, a 136/2017, a 459/2020 e a IN nº 67/2020. Citar a RDC 26/2015 como vigente — o que material de orientação ainda faz — é o tipo de erro que derruba a credibilidade de uma peça antes do mérito. A página cita a revogação explicitamente, e isso é vantagem competitiva.
  2. **A faixa de multa vigente é a do art. 2º, § 1º, na redação da MP nº 2.190-34/2001: R$ 2.000–75.000 (leve), R$ 75.000–200.000 (grave), R$ 200.000–1.500.000 (gravíssima).** O texto compilado do Planalto exibe **duas** redações sobrepostas: o § 1º-A da Lei nº 9.695/1998 (com teto de R$ 50.000 para a grave) e o § 1º da MP 2.190-34/2001. Prevalece a posterior. Fontes secundárias citam a antiga com frequência. **Mesma classe de erro dos "R$ 350 mil" corrigidos ontem no SEO-037 — e desta vez o risco não veio de cobertura secundária, veio do próprio texto compilado, que empilha redações sem marcar qual vale.** Regra nova: em lei compilada, ler até o fim do artigo; a primeira redação encontrada raramente é a vigente.
  3. **O art. 5º da Lei nº 6.437/1977 é armadilha:** tem cadeia de redações em Cr$, NCz$, MP 116/1989 e Lei 7.967/1989. Os valores operativos **não estão nele**, e sim no art. 2º, § 1º. Citar o art. 5º seria citar moeda extinta.
  4. **Os prazos 12/36/48/60 meses que a busca devolve associados à RDC 727/2022 não são dela.** O art. 41 da RDC 727 diz apenas que a resolução entra em vigor em **1º de setembro de 2022**, com um prazo específico até 23/12/2022 para o art. 34. Os prazos escalonados são da **RDC 429/2020** (art. 50): 12 meses geral, 24 para pequenos negócios, 36 para bebidas não alcoólicas em embalagem retornável, contados da vigência em **09/10/2022**. Conflação de fonte secundária, desfeita na leitura dos dois textos.
  5. **Todos os prazos de adequação da rotulagem nutricional já venceram** — o último em **09/10/2025**. A página afirma isso e registra que "ainda estou no prazo de adequação" deixou de ser defesa. Fato com data, que envelhece bem.
  6. **Limites do Anexo XV da IN nº 75/2020, lidos na fonte:** açúcares adicionados ≥ 15 g/100 g e ≥ 7,5 g/100 ml; gorduras saturadas ≥ 6 g/100 g e ≥ 3 g/100 ml; sódio ≥ 600 mg/100 g e ≥ 300 mg/100 ml. A busca inicial devolveu gordura e sódio, **e omitiu açúcares** — número só confirmado indo ao texto do ato.
  7. **A Lei nº 6.437/1977 não tem inciso de rotulagem.** Achado próprio da leitura integral do art. 10, e o ponto mais acionável da página: as autuações de rótulo entram pelo art. 10, IV ou pela cláusula residual do art. 10, XXIX, de modo que auto que não aponta o dispositivo concreto da RDC 727/2022 ou da IN 75/2020 violado é atacável por impedir a defesa.
  8. **Art. 4º: leve/grave/gravíssima é função da contagem de atenuantes e agravantes**, não da gravidade intrínseca do defeito. Consequência prática — atacar as agravantes é caminho mais curto que discutir a seriedade do rótulo.
  9. **Art. 27, §§ 1º a 8º, conferidos palavra a palavra**: divisão da amostra em três, presença do perito indicado pela empresa quando não é possível dividir (§ 1º), requerimento da contraprova com perito próprio (§ 4º), ata com todos os quesitos (§ 5º), **amostra violada impede a contraprova** (§ 6º), **mesmo método** salvo acordo (§ 7º), recurso em 10 dias e terceiro exame na segunda amostra (§ 8º). Também art. 21 (20% em 20 dias com desistência tácita), art. 22 (15 dias), art. 29, art. 30 e § único (20 dias), art. 38 (prescrição em 5 anos), art. 28-A (termo de compromisso, incluído pela Lei nº 14.671/2023).
  10. **CDC conferido no Planalto:** art. 31, art. 37 §§ 1º e 3º, art. 18 (a disparidade com a rotulagem é **vício**, distinto do fato dos arts. 12–17) e arts. 66 e **69** — este último, que tipifica deixar de organizar os dados que dão base à publicidade, é o dispositivo que transforma o dossiê de sustentação de alegação nutricional em exigência legal, e não aparece na cobertura concorrente.
- **O que foi deixado deliberadamente de fora:** (a) **números de artigo do RIISPOA** — a divisão de competência MAPA × Anvisa foi confirmada só em fonte secundária, então a página descreve a competência corretamente ("o MAPA diz o que o produto é, a Anvisa diz como a informação é apresentada") **sem citar artigo**, na regra do SEO-037 de preferir referência genérica correta a número que envelhece errado; (b) **a RDC nº 819/2023 e a suspensão judicial do prazo de esgotamento de embalagens** — a janela expirou em outubro de 2024 e o assunto é histórico, então citá-lo adicionaria risco de erro sem valor decisório.
- **Vantagem competitiva com prazo:** a **Consulta Pública nº 1.400/2026** (declaração quantitativa de ingredientes, transmissão por tecnologia, alimentos irradiados com Radura facultativo) está **aberta até 19/10/2026**. A página a trata como o SEO-003 tratou a CP 1.362/2025 e o SEO-037 tratou o art. 341-G: em andamento, **sem força obrigatória**, com a observação de que autuação que invoque exigência em consulta é autuação sem norma.
- **Manutenção:** rever quando a CP 1.400/2026 for concluída — é o ponto que muda primeiro. A faixa de multa só muda por lei. Os limites do Anexo XV mudam por IN.

### SEO-039 — `</head>` duplicado e a checagem que faltava *(executada em 2026-08-28)*
- **Descrição:** `/produtos-quimicos-controlados/` foi publicada em 27/08 com **dois `</head>`** consecutivos. O navegador se recupera e nenhuma das checagens existentes olhava a moldura do documento, então o erro passou por `valid`, por `deploy`, pela verificação de renderização em Chrome real e pela indexação.
- **URL:** `/produtos-quimicos-controlados/` e `tools/seo-report.py`
- **Categoria:** Técnico / Ferramental
- **Impacto:** 3 · **Esforço:** 1 · **Confiança:** 10 · **Valor de negócio:** 3
- **Priority Score:** 90
- **Status:** done · **Descoberto:** 2026-08-28 · **Concluído:** 2026-08-28
- **Implementado:** tag duplicada removida; `section_valid()` passou a exigir **exatamente uma** ocorrência de `<head>`, `</head>`, `<body>` e `</body>` em cada página. A checagem foi **testada contra o defeito real** — reintroduzido de propósito numa cópia, detectado, e revertido — em vez de aceita porque "passou".
- **A lição, que é maior que o bug:** a primeira tentativa da checagem usava `doc.count("<head")`, que casa também com `</head>` e acusou 17 páginas de uma vez. **Um resultado que reprova tudo é tão suspeito quanto um que aprova tudo** — é o simétrico da regra 3 de ontem, e as duas se resumem a: resultado uniforme merece desconfiança, em qualquer direção.
- **Por que o esforço se justifica num item de impacto 3:** fecha a classe de erro em vez do caso. A malformação era invisível a todo o ferramental existente, e a próxima página gerada por template poderia repeti-la.

### Próxima execução — o que checar primeiro

1. **Rodar `tools/seo-report.py` em `deploy`, `valid` e `gsc` separados antes de decidir qualquer coisa.** A regra do mandato — não criar conteúdo enquanto houver ganho fácil de ranking — exige que "não há ganho fácil" seja **verificado**. Hoje o teste concreto foi o `query × page` a 90 dias: se nenhuma consulta em posição 5–20 aponta para tema meio coberto por página existente, não há alavanca de Prioridade 2.
2. **`/produtos-quimicos-controlados/`: a leitura de ~05/09 continua pendente e agora vale dobrado**, porque decide sobre duas páginas. Consultas a vigiar: `produtos químicos controlados`, `licença polícia federal produtos químicos`, `mapa de controle siproquim`, `autuação produto controlado`, `IN 338/2026`. **Conferir canibalização com `/pericia-industria-quimica/` por `query × page`.**
3. **`/rotulagem-alimentos/`: primeira leitura a partir de ~06/09.** Consultas a vigiar: `rotulagem nutricional frontal`, `autuação rotulagem alimento`, `perícia de contraprova`, `lei 6437 multa`, `alérgenos rótulo RDC 727`, `limites lupa açúcar sódio`. **Conferir canibalização com `/prazo-validade-alimentos/`**, que é a página vizinha mais próxima.
4. **Se as duas páginas novas entrarem abaixo de 10 em consulta técnica, a hipótese da especificidade está confirmada e a fila segue técnica.** Candidatos remanescentes, já filtrados contra o conteúdo existente: **microbiologia de alimentos como prova** (a única do exemplo de cluster do mandato ainda sem tratamento próprio) e **recall/recolhimento** — este último foi descartado em 27/08 por estar coberto em `/pericia-contaminacao-alimentos/`, e a decisão continua válida. Se **não** entrarem, a limitação é de autoridade de domínio, e o trabalho vira aquisição de citação e menção — não mais conteúdo.
5. **Prioridade 1 continua bloqueada por falta de dado**, não por falta de oportunidade. 8 sessões orgânicas em 28 dias. Reavaliar quando os cliques passarem de um dígito; `/quesitos-periciais/` (200 impressões, CTR 0,5%, pos 9,9) é a primeira da fila, `/assistente-tecnica/` (72, pos 9,8, 0 cliques) subiu para segunda.
6. **O sinal móvel segue sem decidir nada.** Só voltar ao assunto com ~400 impressões móveis, por volta de meados de setembro.
7. **Indexação está 16/16.** Verificar só quando entrar página nova.
8. **Em lei compilada, ler o artigo até o fim.** O Planalto empilha redações sucessivas sem marcar qual vale, e a primeira que aparece costuma ser a revogada. Foi assim com a faixa de multa da Lei nº 6.437/1977 hoje, e a consequência de errar é a mesma dos "R$ 350 mil" de ontem: número errado com aparência de fonte primária.
9. **Gerar FAQ visível e JSON-LD da mesma fonte de dados.** Terceira execução com o método; continua eliminando a classe de erro em vez de detectá-la. O gerador vive em `scratchpad/` e é descartável — o que precisa sobreviver é a regra.
10. **Testar toda checagem nova contra o defeito real antes de confiar nela.** A da SEO-039 só valeu depois de reprovar uma cópia deliberadamente quebrada.
11. **Escalar o Google Ads sem entrega.** Décima primeira execução como nota de rodapé. Não é item de SEO e não se resolve no backlog — cabe uma mensagem direta à cliente.


---

## Auditoria — 2026-08-29

`deploy` e `valid` passaram integralmente antes de qualquer alteração: 0 commits pendentes, sitemap em dia, **17 URLs em 200 e 17 páginas locais sem falha** de título, description, canonical, `h1`, JSON-LD, link interno, órfã, paridade de FAQ ou moldura de documento (checagem da SEO-039).

**Uma pendência de indexação, e ela não é defeito:** `/rotulagem-alimentos/`, publicada ontem, está "Rastreada, mas não indexada no momento" — 16 de 17 indexadas. É latência normal de página com menos de 24 horas, e a comparação com `/produtos-quimicos-controlados/` (que entrou como indexada em ~24 h) não autoriza conclusão: uma observação não faz série. **Reverificar em 31/08; só tratar como problema se persistir após ~72 h.**

### Medição: crescimento segue, conversão segue sem base

- **628 impressões · 7 cliques em 28 dias** (era 543 · 5 em 28/08; 484 · 5 em 27/08). Terceiro dia consecutivo de alta de impressões. `/quesitos-periciais/` 219 (pos 10,1), `/impugnacao-laudo-pericial/` 91 (13,2), `/assistente-tecnica/` 76 (9,9), `/honorarios-pericia-judicial/` 54 (9,9), `/laudo-pericial/` 48 (8,7), `/normas-tecnicas-pericia/` 41 (**pos 4,2**), `/pericia-combustiveis/` 25 com **CTR 8,0%** em pos 6,0.
- **Nenhum ganho fácil de ranking disponível — verificado, não presumido.** O cruzamento `query × page` a 90 dias devolve **27 linhas somando 50 impressões** das 628 (o resto é anonimizado), e **todas** pertencem ao cluster jurídico-processual já coberto. Nenhuma consulta em posição 5–20 aponta para tema que uma página existente cubra pela metade — a única forma de a Prioridade 2 ter alavanca. Liberada a criação de conteúdo.
- **Prioridade 1 continua bloqueada por falta de dado, não por falta de oportunidade.** 7 cliques em 28 dias não distinguem hipótese de CTR nenhuma, e a SEO-016 já inspecionou os títulos e descriptions. Não reabrir por hábito.

### A hipótese da especificidade ganhou mais um voto, sem depender das páginas novas

As leituras de `/produtos-quimicos-controlados/` (~05/09) e `/rotulagem-alimentos/` (~06/09) **seguem pendentes e não foram antecipadas.** Mas o sinal independente ficou mais forte hoje: as duas melhores posições do site continuam sendo as páginas mais técnicas e mais estreitas (`/normas-tecnicas-pericia/` 4,2 e `/pericia-industria-quimica/` 5,0), e a melhor CTR segue sendo `/pericia-combustiveis/` (8,0% em pos 6,0, com 2 dos 7 cliques do site), enquanto os termos-cabeça jurídicos permanecem em 26–47. A escolha do terreno técnico não dependia das páginas de ontem e de anteontem.

### A lacuna: o site ensinava a investigar contaminação, mas não a ler o laudo

Levantamento por termo nas 17 páginas: **`RDC 331`, `IN 60`, `coliforme`, `swab`, `ICMSF` e `desafio microbiológico` não apareciam em nenhuma delas.** `/pericia-contaminacao-alimentos/` tem seção própria de cadeia de custódia, APPCC, recall e responsabilidade sob o CDC — ensina a **investigar** —, mas em nenhum lugar do site se dizia **quais são os limites, como se compõe um plano de amostragem e como um resultado é classificado**. Era o último tema do exemplo de cluster do mandato ("Microbiologia") ainda sem tratamento próprio, e o único dos três candidatos pré-registrados em 28/08 que sobreviveu à conferência contra o conteúdo existente.

### SEO-040 — Spoke: análise microbiológica, plano de amostragem e leitura do laudo *(executada em 2026-08-29)*
- **Descrição:** O que compõe um padrão microbiológico (n, c, m, M), como a RDC nº 724/2022 classifica um resultado, por que "qualidade intermediária" não é infração, o caso da *Listeria*, a diferença entre amostra indicativa e representativa, e por que na microbiologia quase nunca há contraprova.
- **URL:** `/analise-microbiologica-alimentos/`
- **Categoria:** Conteúdo / Spoke de cluster / Prova técnica em alimentos
- **Impacto:** 8 · **Esforço:** 4 · **Confiança:** 8 · **Valor de negócio:** 9
- **Priority Score:** 144
- **Status:** done · **Descoberto:** 2026-08-29 · **Concluído:** 2026-08-29
- **Por que esta:** terceira página do cluster de Alimentos, aprofundando em vez de abrir frente nova; terreno técnico e estreito, com concorrência de laboratório e de consultoria de qualidade — não de portal jurídico —, que é o tipo de SERP em que este domínio ranqueia 4–13 e não 27–47. Prioridades 1 e 2 foram verificadas e não tinham alavanca.
- **Implementado:** ~4.650 palavras. Tabela da situação de cada norma com o dispositivo que a revogou; tabela dos oito elementos do padrão com o inciso de cada um; tabela das três classificações cruzando plano de duas e de três classes; tabela do padrão de *Listeria* nas duas categorias; seis falhas numeradas; nove quesitos. `Article` (com `isPartOf` no pilar de alimentos) + `FAQPage` (8) + `BreadcrumbList` de três níveis, com o `@id` canônico do `Person`.

- **A tese que a página tem e a concorrência não:** *um resultado microbiológico não é um número, é um plano.* O padrão se compõe de n, c, m e M, e a regra do art. 11 da RDC nº 724/2022 classifica o lote comparando **quantas** unidades ficaram entre m e M com o valor de c. Laudo que informa uma contagem sem informar o plano executado não demonstra o descumprimento que afirma. Daí saem as duas consequências acionáveis: **a amostra indicativa não executa o plano** (tem n inferior, art. 3º, II) e por isso indica sem medir a conformidade do lote; e **"satisfatório com qualidade intermediária" não é infração** — permanece satisfatório e dispara apenas o dever de investigar do art. 6º, IV.
- **A segunda tese, contraintuitiva e verificável:** para **alimento pronto para o consumo em geral**, o padrão de *Listeria monocytogenes* do Anexo II da IN nº 161/2022 é **n=5, c=0, m=10² UFC/g** — limite **quantitativo**, não exigência de ausência. A ausência em 25 g (n=10) vale só para lactentes e fins especiais. Logo, laudo que registra apenas "presença de *Listeria*", sem contagem, não demonstra descumprimento do padrão do alimento pronto comum. Pesquisa qualitativa e ensaio quantitativo respondem a perguntas diferentes.
- **Paridade de FAQ garantida por construção** (quarta execução do método da SEO-037): as 8 perguntas foram definidas uma vez em estrutura de dados e o HTML visível e o JSON-LD gerados da mesma fonte. Conferido depois por script: 8/8 idênticos, campo a campo.
- **Delimitação de escopo declarada**, como nas três páginas anteriores: implantar plano de autocontrole, montar programa de coleta de rotina e conduzir monitoramento ambiental de fábrica **são consultoria em qualidade, não o objeto do trabalho**. O CTA vende exame de laudo e de plano de amostragem executado, parecer de método e representatividade, atuação como perita indicada na análise fiscal do art. 27, § 1º, e quesitos.
- **Canibalização resolvida na origem, e a fronteira é limpa:** `/pericia-contaminacao-alimentos/` ensina a **investigar** a contaminação (custódia, APPCC, recall, CDC); esta página ensina a **ler o laudo** (limites, plano, classificação). `/rotulagem-alimentos/` já ensinava o **rito** do art. 27 em detalhe, então a página nova **não o reensina** — trata só do que é específico da microbiologia (por que a contraprova em regra não se sustenta) e remete o rito completo àquela página. Nenhum texto precisou ser encurtado em página existente; bastou um parágrafo de fronteira no pilar de contaminação.
- **Links de entrada:** 5 páginas — card de Insights na home, parágrafo de fronteira + "no mesmo tema" em `/pericia-contaminacao-alimentos/`, "no mesmo tema" em `/prazo-validade-alimentos/`, entrada em "Onde cada norma é aplicada" de `/normas-tecnicas-pericia/` (nomeando a revogação) e a lista de leitura de `/rotulagem-alimentos/`. Vizinhança tópica real, critério da SEO-019. `sitemap.xml` e `llms.txt` atualizados, com "Análise Microbiológica de Alimentos" passando a serviço próprio na lista do `llms.txt`.

- **Verificação factual — texto literal antes de publicar. Um achado de classe grave, e é o ativo competitivo da página:**
  1. **A RDC nº 331/2019 e a IN nº 60/2019 estão revogadas, e continuam sendo ensinadas como vigentes.** O **art. 14 da RDC nº 724/2022** revogou a RDC nº 331/2019; o **art. 6º da IN nº 161/2022** revogou as INs nº 60/2019, nº 79/2020 e nº 110/2021. Ambas as normas novas vigem desde **1º de setembro de 2022**. Buscar "padrões microbiológicos" ainda devolve, em primeira página, material de consultoria e de órgão público explicando a RDC 331 e a IN 60 como se valessem. **Mesma classe de erro da RDC 26/2015 de ontem** — e a terceira execução seguida em que a norma "conhecida" do tema estava revogada. *Regra que já se pode generalizar: em regulação sanitária de alimentos, presumir revogação e provar vigência, não o contrário.*
  2. **A IN nº 161/2022 foi alterada pela IN nº 313, de 4 de setembro de 2024**, e as alterações são de fundo, não de forma: incluíram o parágrafo único do art. 1º (alimento pronto **deteriorado** é de qualidade inaceitável e **não** se sujeita aos padrões); trocaram o inciso VI do parágrafo único do art. 3º; incluíram o inciso VII; e **revogaram o parágrafo único do art. 7º e o Anexo IV** (*Salmonella* em carne suína crua). Trabalhar com o texto original da IN 161, sem a consolidação, levaria a citar o Anexo IV — que não existe mais. Usado o **texto consolidado** por isso.
  3. **As exclusões da IN 313/2024 para alimentos fermentados são o achado mais acionável do ato:** **não se aplicam** os padrões de "aeróbios mesófilos" nem de "bolores e leveduras" aos alimentos cujo processo envolva a adição desses micro-organismos, quando viáveis e capazes de impactar a contagem — nem aos que os contenham como ingrediente. Autuar produto fermentado por contagem alta de mesófilos passou a ser expressamente contrário à norma.
  4. **Art. 11 da RDC nº 724/2022 transcrito e conferido inciso a inciso**, porque é dele que sai a tese central. Plano de duas classes: insatisfatório com presença ou resultado **maior que m** em **qualquer** unidade. Plano de três classes: satisfatório com qualidade intermediária quando as unidades entre m e M são **em número igual ou menor que c** e nenhuma supera M; insatisfatório quando **mais de c** ficam entre m e M **ou** alguma supera M.
  5. **Exemplo numérico extraído do Anexo I, não inventado:** frutas *in natura* inteiras têm *E. coli* com **n=5, c=2, m=10², M=10³** — até duas unidades entre 100 e 1.000 UFC/g mantêm o lote satisfatório — e *Salmonella* com **n=5, c=0, ausência em 25 g**. Conferido também que **o n varia por categoria**: frutas preparadas, branqueadas, secas ou em polpa exigem **n=10** para *Salmonella*. Dois micro-organismos, o mesmo produto, lógicas opostas de julgamento.
  6. **Art. 27, § 1º, da Lei nº 6.437/1977 lido no Planalto, e a redação importa:** *"se a sua quantidade ou natureza **não permitir a colheita de amostras**"* — não "a divisão em três", como a paráfrase corrente sugere. É esse o dispositivo que sustenta a tese procedimental da página, e o § 2º completa: ausentes o detentor e o perito indicado, **convocam-se duas testemunhas**.
  7. **Conferência colateral que valeu a pena:** relidas as faixas de multa do art. 2º da Lei nº 6.437/1977 para checar a página de ontem. O texto compilado empilha o **§ 1º-A** (Lei nº 9.695/1998: 2.000–20.000 / 20.000–50.000 / 50.000–200.000) e o **§ 1º** (MP nº 2.190-34/2001: 2.000–75.000 / 75.000–200.000 / 200.000–1.500.000). **A `/rotulagem-alimentos/` está correta** — usa a redação posterior. Nenhuma correção necessária no site.
- **O que foi deixado deliberadamente de fora:** (a) **prazo máximo entre coleta e ensaio** — é parâmetro de método, varia por micro-organismo e referência, e não há número único citável, então a página o trata como **quesito** ("qual o intervalo entre coleta e início do ensaio?") em vez de afirmar um limite; (b) **planos de amostragem do ICMSF por categoria de risco** — a lógica é a mesma, mas a IN nº 161/2022 traz os valores próprios e citar a fonte estrangeira acrescentaria autoridade aparente sem valor decisório; (c) **os padrões do Anexo III** (alimentos comercialmente estéreis) foram descritos em uma linha, sem tabela, porque o critério é qualitativo e não rende leitura de plano.
- **Manutenção:** rever quando a **IN nº 161/2022** for novamente alterada — é o ato que muda com mais frequência (já alterado uma vez em dois anos) e é ele que carrega os números. A RDC nº 724/2022 muda menos, porque é a regra de aplicação.

### Verificação de renderização — com controle negativo, desta vez

Chrome real via Playwright (`channel="chrome"`, `/usr/bin/python3` — é o Python 3.9 do sistema que tem `playwright` e `googleapiclient`, não o do Homebrew) contra `http://localhost:8899`, a 375 px e 1280 px.

- **Sem overflow horizontal em nenhuma das três páginas medidas, nas duas larguras** (`scrollWidth == clientWidth`, com `innerWidth == clientWidth` confirmando a validade da leitura). As duas páginas de controle — `/pericia-contaminacao-alimentos/` e `/rotulagem-alimentos/` — mediram igual, como esperado.
- **12 de 12 âncoras assentam em y = 112 px**, abaixo do cabeçalho fixo de 98 px.
- **E, desta vez, o "tudo OK" foi testado contra o defeito antes de ser aceito** — aplicando a regra 10 de ontem à própria ferramenta de medição, não só às checagens de conteúdo. Três controles:
  1. **Sem a espera de estabilização**, a mesma âncora `#faq` mede **1716 px** em vez de 112 — o `scroll-behavior: smooth` ainda em animação. Confirma que a espera está fazendo trabalho real e reproduz, de propósito, o erro que enganou a medição de 27/08.
  2. **Com `scroll-margin-top` desligado por `add_style_tag`**, `#listeria` cai em **y = 0** — sob o cabeçalho. O harness **detecta** a falha, logo o 12/12 não é vacuoso.
  3. **As quatro tabelas realmente excedem a viewport de 375 px dentro do `.table-scroll`** (544 px de conteúdo em 311 px de contêiner) — o resultado "sem overflow" não vem de tabelas estreitas demais para transbordar.
- **Regra nova, que fecha o ciclo das três anteriores:** *um resultado uniforme só vale depois que se demonstrou que a medição sabe reprovar.* "Desconfie do resultado uniforme" (27/08) diagnosticava; "teste a checagem contra o defeito real" (28/08) resolvia para checagens de conteúdo; falta**va** aplicar o mesmo ao instrumento de medição. Custou três chamadas de Playwright e substitui a desconfiança por prova.

### Próxima execução — o que checar primeiro

1. **Rodar `tools/seo-report.py` em `deploy`, `valid` e `gsc` antes de decidir qualquer coisa** — e note que `gsc` exige `/usr/bin/python3`, não `python3` (o do Homebrew não tem `googleapiclient`). O teste concreto de Prioridade 2 continua sendo o `query × page` a 90 dias: se nenhuma consulta em posição 5–20 aponta para tema meio coberto por página existente, não há alavanca e a criação de conteúdo está liberada.
2. **Conferir a indexação de `/rotulagem-alimentos/`** (crawleada, não indexada em 29/08) e de `/analise-microbiologica-alimentos/`. Só tratar como problema se a de ontem persistir após ~72 h, isto é, a partir de 31/08.
3. **`/produtos-quimicos-controlados/`: leitura de ~05/09.** Consultas: `produtos químicos controlados`, `licença polícia federal produtos químicos`, `mapa de controle siproquim`, `autuação produto controlado`, `IN 338/2026`. Conferir canibalização com `/pericia-industria-quimica/` por `query × page`.
4. **`/rotulagem-alimentos/`: leitura de ~06/09.** Consultas: `rotulagem nutricional frontal`, `autuação rotulagem alimento`, `perícia de contraprova`, `lei 6437 multa`, `alérgenos rótulo RDC 727`. Conferir canibalização com `/prazo-validade-alimentos/`.
5. **`/analise-microbiologica-alimentos/`: primeira leitura a partir de ~07/09.** Consultas a vigiar: `padrões microbiológicos alimentos`, `RDC 724/2022`, `IN 161/2022`, `plano de amostragem microbiológico`, `n c m M microbiologia`, `listeria alimentos limite`, `amostra indicativa representativa`. **Conferir canibalização com `/pericia-contaminacao-alimentos/`**, que é o pilar de onde a fronteira foi traçada.
6. **Se as três páginas novas entrarem abaixo de 10 em consulta técnica, a hipótese da especificidade está confirmada e a fila segue técnica.** O cluster de Alimentos terá então quatro páginas e passa a ser o mais profundo do site — **momento de parar de expandi-lo e verificar se ele converte**, em vez de acrescentar a quinta. Se **não** entrarem, a limitação é de autoridade de domínio, e o trabalho vira aquisição de citação e menção, não mais conteúdo.
7. **Candidatos remanescentes, já filtrados contra o conteúdo existente:** nenhum do exemplo de cluster do mandato sobrou — microbiologia era o último. HACCP/APPCC (28/08), recall (27/08), parecer técnico (27/08) e análise laboratorial/ISO 17025 (28/08) foram descartados por cobertura existente e **não devem ser repropostos**. Uma frente nova exigirá levantamento próprio, não a lista antiga.
8. **Presumir revogação e provar vigência**, em regulação sanitária de alimentos. Três execuções seguidas em que a norma "conhecida" do tema estava revogada: RDC 26/2015 (alérgenos), RDC 331/2019 e IN 60/2019 (padrões microbiológicos). O custo de conferir é uma busca; o custo de errar é a credibilidade da peça inteira.
9. **Usar texto consolidado quando a norma tiver ato alterador.** A IN 161/2022 sem a IN 313/2024 levaria a citar um Anexo IV revogado.
10. **Um resultado uniforme só vale depois que se demonstrou que a medição sabe reprovar.** Vale para o harness de renderização tanto quanto para as checagens de `seo-report.py`.
11. **Gerar FAQ visível e JSON-LD da mesma fonte de dados.** Quarta execução; segue eliminando a classe de erro em vez de detectá-la. O gerador vive em `scratchpad/` e é descartável — o que precisa sobreviver é a regra.
12. **Escalar o Google Ads sem entrega.** Décima segunda execução como nota de rodapé. Não é item de SEO e não se resolve no backlog — cabe uma mensagem direta à cliente.

---

## Estado da medição — 2026-08-31

Coleta de 28 dias, service account. **713 impressões · 8 cliques · 18 de 18 páginas indexadas (PASS em todas).**

- **A pendência de indexação aberta em 29/08 está encerrada.** `/rotulagem-alimentos/` e `/analise-microbiologica-alimentos/` aparecem como "Enviada e indexada". O item 2 da lista da execução anterior não precisa de acompanhamento a partir de 31/08.
- **Volume cresceu de 484 para 713 impressões** desde 27/08, com os cliques passando de 5 para 8.
- **GA4:** 71 sessões, das quais 9 de Organic Search, 8 de Paid Search e 2 de AI Assistant. Ainda sem base para otimizar conversão — Prioridade 1 do mandato segue sem dado que a sustente, como em 27/08 e 29/08.

### A hipótese da especificidade ganhou mais uma confirmação

| Página | Impressões | Posição | CTR |
|---|---|---|---|
| `/normas-tecnicas-pericia/` | 52 | **5,8** | 0% |
| `/pericia-industria-quimica/` | 11 | **5,1** | 0% |
| `/pericia-combustiveis/` | 27 | **5,9** | **7,4%** |
| `/pericia-contaminacao-alimentos/` | 12 | **6,2** | **16,7%** |
| `/prazo-validade-alimentos/` | 8 | **6,0** | 0% |
| `/produtos-quimicos-controlados/` | 2 | **6,0** | 0% |
| `/quesitos-periciais/` | 248 | 10,6 | 0,4% |
| `/impugnacao-laudo-pericial/` | 94 | 13,1 | 0% |
| `/classificacao-fiscal-ncm/` | 15 | 13,7 | 0% |

As páginas técnicas e estreitas ocupam a faixa 5–6; as amplas e jurídicas ficam em 10–14 na média e em 27–48 nos termos-cabeça. O padrão registrado em 27/08 e 29/08 se repete pela terceira leitura. **`/produtos-quimicos-controlados/` entrou em posição 6,0 na sua primeira leitura** — a leitura formal de ~05/09 continua marcada, mas o sinal inicial confirma a escolha do terreno.

### Prioridades 1 e 2 verificadas e liberadas — não presumidas

- **Prioridade 1 (conversão em página de alta impressão):** o candidato óbvio é `/quesitos-periciais/`, com 248 impressões — 35% de todo o site — e CTR de 0,4%. **Não é problema de metadado.** Uma média de 10,6 significa, na prática, topo da página 2, onde a CTR desaba independentemente do título; e a SEO-016 foi encerrada em 27/08 depois da inspeção um a um dos 15 títulos e descriptions. A alavanca aqui é posição, isto é, autoridade — não reescrita.
- **Prioridade 2 (consultas em 5–20 apontando para tema meio coberto):** teste do `query × page` a 90 dias executado. Das 31 linhas expostas (61 de ~713 impressões; o resto é anonimizado), as que estão em 5–20 são `emitir despacho - sem quesitos` (9,0), `anexo juntado: apresentação de esclarecimentos ao laudo` (8,2), `art. 95, § 3º, ii, do cpc` (9,0), `impugnação ao laudo pericial cpc` (9,0), `prazo apresentacao quesitos` (12,0), `prazo para se manifestar sobre laudo pericial` (11,0) e `assistente tecnico pericia` (16,0). **A única que sugeria tema meio coberto era a de esclarecimentos ao laudo — e a conferência descartou:** "esclarecimento" aparece 17 vezes em `/impugnacao-laudo-pericial/` e 11 em `/laudo-pericial/`, e o art. 477 está tratado nas duas. Sem alavanca de ranking fácil, a criação de conteúdo fica liberada pela regra do mandato.

### A lacuna: o site prova que o combustível estava fora do limite, não que ele quebrou o motor

`/pericia-combustiveis/` é a página de melhor CTR do site (7,4%, 2 dos 8 cliques), está em posição 5,9, é a **mais curta** das 17 (3.772 palavras) e o seu cluster tinha **uma única página**. Levantamento por termo nela: **`nexo` aparece 0 vez, `bomba injetora` 0 vez, `motor` 1 vez.** A página ensina a provar adulteração e não conformidade — e nunca chega à pergunta que o advogado do consumidor efetivamente tem, que é se aquele combustível causou aquela avaria. `art. 381` do CPC (produção antecipada de prova) **não aparecia em nenhuma das 17 páginas do site.**

### SEO-041 — Spoke: dano ao motor por combustível e a prova do nexo causal *(executada em 2026-08-31)*
- **Descrição:** Por que um laudo de amostra não demonstra o nexo causal; o mecanismo físico de cada parâmetro fora de especificação e a assinatura que ele deixa no componente; a janela de preservação da prova; e a diferença entre vício e fato do produto, que decide o prazo.
- **URL:** `/dano-motor-combustivel/`
- **Categoria:** Conteúdo / Spoke de cluster / Prova técnica em litígio de consumo
- **Impacto:** 8 · **Esforço:** 4 · **Confiança:** 8 · **Valor de negócio:** 9
- **Priority Score:** 144
- **Status:** done · **Descoberto:** 2026-08-31 · **Concluído:** 2026-08-31
- **Por que esta:** aprofunda o cluster de melhor CTR e menor profundidade do site, em vez de abrir frente nova; terreno técnico e estreito, com concorrência de blog automotivo e de escritório de advocacia — não de portal jurídico de alta autoridade —, que é a SERP em que este domínio ranqueia 5–6 e não 27–48; e a intenção comercial é a mais direta do site, porque quem busca já tem um veículo parado e precisa de assistente técnica agora. O cluster de Alimentos ficou de fora deliberadamente: o item 6 da lista de 29/08 mandava parar de expandi-lo em quatro páginas e verificar se converte.
- **Implementado:** ~4.500 palavras de texto corrido. Quatro tabelas: parâmetro → mecanismo → assinatura no componente (8 linhas); limites da Tabela 1 do Anexo da RANP 968/2024 relevantes para dano (8 linhas); vício × fato do produto em 6 dimensões; e o quadro do ponto de entupimento de filtro a frio por região e mês. Nove quesitos. `Article` (com `isPartOf` apontando para `/pericia-combustiveis/`) + `FAQPage` (8) + `BreadcrumbList` de três níveis, com o `@id` canônico do `Person`.

- **A tese que a página tem e a concorrência não:** *estar fora de especificação e ter causado o dano são duas afirmações diferentes, e a segunda não decorre da primeira.* Cada parâmetro atua por um mecanismo físico próprio e deixa uma marca própria: água **corrói** e alimenta borra microbiológica; particulado **risca** (desgaste abrasivo); lubricidade insuficiente **escoria e transfere material** (desgaste adesivo), sem produto de corrosão; enxofre envenena o **pós-tratamento** e não toca no sistema de injeção. Daí o discriminador que decide a maioria dos casos: **se o laudo aponta um desvio e a peça exibe a marca de outro, a conclusão não se sustenta.** É argumento que só um engenheiro formula, e é o ativo da página.
- **A segunda tese, procedimental e mais acionável ainda:** *a peça avariada é a prova que ninguém preserva.* Três provas precisam coexistir e desaparecem em ritmos diferentes — o combustível do tanque do veículo (consumido na primeira intervenção da oficina), a amostra-testemunha do posto (RANP 898/2022, três últimos recebimentos: **o prazo real se mede em caminhões, não em dias**) e as peças (descartadas ou limpas no reparo, e a limpeza apaga a assinatura). Por isso a medida mais útil raramente é a inicial: é a **produção antecipada de prova do art. 381, I, do CPC**, cujo texto — "fundado receio de que venha a tornar-se impossível ou muito difícil a verificação de certos fatos na pendência da ação" — descreve este caso literalmente. O inciso III cobre o exame que pode **evitar** o ajuizamento.
- **A terceira tese, de prazo:** combustível fora de especificação, em si, é **vício** (art. 18, decadência de 30 ou 90 dias pelo art. 26); **motor danificado é fato do produto** (art. 12), porque o dano extrapolou o produto, e prescreve em **cinco anos** pelo art. 27, contados *do conhecimento do dano e de sua autoria*. Em litígio de combustível a autoria só se conhece quando o exame identifica o elo — o que é, em si, trabalho técnico. Tratar quebra de motor como vício troca cinco anos por três meses sem necessidade.
- **Paridade de FAQ garantida por construção** (quinta execução do método da SEO-037): as 8 perguntas e respostas foram definidas uma única vez em `faq.py` e o HTML visível e o JSON-LD gerados da mesma fonte. Conferido depois por script estrito: 8/8 idênticos caractere a caractere.
- **Delimitação de escopo declarada**, como nas quatro páginas anteriores: avaliação de valor de veículo, orçamento de reparo e vistoria de sinistro para seguradora **são outros serviços**, não o objeto do trabalho. Sem isso a página atrairia demanda de vistoria de seguradora, que a cliente não atende.
- **Canibalização resolvida na origem:** `/pericia-combustiveis/` já dizia, numa única oração da seção de sanções, que "o mesmo fato pode gerar repercussão cível, por dano a consumidores e a veículos" — e nunca desenvolvia. Essa oração virou a porta: acrescentou-se ali um parágrafo de fronteira que declara o que o pilar **não** trata e remete à spoke. Nenhum texto precisou ser encurtado, porque não havia texto duplicado a encurtar — a lacuna era real, não uma sobreposição.
- **Links de entrada:** 4 páginas — card de Insights na home, parágrafo de fronteira + "Áreas técnicas relacionadas" em `/pericia-combustiveis/`, entrada em "Onde cada norma é aplicada" de `/normas-tecnicas-pericia/` (nomeando a RANP 968/2024) e "Referência técnica" de `/laudo-pericial/`, com âncora que descreve o defeito ("quando o laudo conclui pelo nexo sem ter examinado a peça"). Vizinhança tópica real, critério da SEO-019. `sitemap.xml` e `llms.txt` atualizados, com "Dano ao Motor por Combustível" passando a serviço próprio na lista do `llms.txt`.

- **Verificação factual — texto literal antes de publicar. Um erro próprio pego na conferência final, e uma confusão de norma descartada:**
  1. **Resolução ANP nº 968/2024 lida no texto integral** (PDF do DOU de 02/05/2024, extraído localmente). Limites da Tabela 1 do Anexo conferidos linha a linha: **teor de água máx. 200 mg/kg no diesel A e C e 250 mg/kg no B; contaminação total máx. 24 mg/kg; lubricidade máx. 460 µm (HFRR, ISO 12156-1); estabilidade à oxidação máx. 2,5 mg/100 mL; enxofre 10 e 500 mg/kg; viscosidade a 40 °C de 2,0 a 4,5 mm²/s; corrosividade ao cobre máx. 1.** Art. 39: vigor em 31/07/2024.
  2. **Erro meu, corrigido antes do commit.** A primeira redação dizia que o ponto de entupimento de filtro a frio em SP, MG e MS é de "3 °C entre abril e julho". A Tabela 2 do Anexo diz **abril = 7 °C** e **3 °C de maio a agosto**. Corrigido na página e no `llms.txt`. *A tabela estava aberta na tela e mesmo assim a paráfrase saiu errada — parafrasear tabela de memória imediata é tão arriscado quanto parafrasear norma de memória longa.*
  3. **Art. 18 da RANP 968/2024 explica-se pela química, e essa é a ligação que dá autoridade à seção do biodiesel:** a análise de lubricidade só é **obrigatória** quando a Lei nº 13.033/2014 conduzir à dispensa da adição de biodiesel ou a teor **≤ 2%**; acima disso é **facultada**. A razão está no manual técnico de óleo diesel da Petrobras (versão março/2023): o hidrotratamento profundo necessário para chegar a 10 mg/kg de enxofre remove os compostos polares que dão lubricidade natural, e **cerca de 2% de biodiesel já bastam para trazer a cicatriz HFRR para bem abaixo de 460 µm**. Consequência prática registrada na página: num caso em que se suspeita de lubricidade, **o certificado da qualidade pode simplesmente não trazer o dado**, e o ensaio precisa ser requerido.
  4. **O mesmo manual sustenta o outro lado do biodiesel:** as moléculas têm oxigênio e são muito mais polares que os hidrocarbonetos, o que torna o produto **mais higroscópico**; as duplas ligações reduzem a estabilidade; e diglicerídeos e triglicerídeos favorecem entupimento de filtro e **lacas** em bomba e bico. Água no fundo do tanque cria atividade microbiana, gera borra, satura filtro e corrói componentes da bomba. É a base física da primeira tabela da página.
  5. **B15 desde 1º/08/2025, por Resolução CNPE nº 9/2025** — confirmado na página oficial de biodiesel da ANP no gov.br, que também identifica a **RANP 920/2023** como a especificação do biodiesel. Havia ruído na busca (uma notícia de "11% a partir de setembro", antiga) que não foi propagado.
  6. **Resolução ANP nº 988, de 8 de setembro de 2025:** altera a RANP 807/2020, **RON mínimo de 93 para 94** enquanto o teor de etanol anidro for de 30%, com o novo **art. 15-A** prevendo o retorno a 93,0 se o teor obrigatório cair abaixo de 30%, e o **art. 15-B** fixando carência para autuação pelo novo teor (15 dias na distribuição e 30 na revenda; 30 e 60 no Norte). Esse detalhe de carência é o que permite dizer que um produto coletado dentro do prazo, com teor referido ao percentual anterior, **não estava em infração por essa característica**.
  7. **Confusão de norma descartada na origem:** a **RANP 902/2022 é o Programa de Marcação Compulsória**, não a especificação do etanol — esta é a **RANP 907/2022**. Conferido porque `/pericia-combustiveis/` cita a 902/2022 e havia risco de a página nova replicar um erro. **O pilar está correto**: cita a 902/2022 exatamente no contexto do marcador de solvente. Nenhuma correção necessária.
  8. **Amostra-testemunha: Resolução ANP nº 898/2022**, com guarda dos **três últimos recebimentos** de cada combustível — confirmado no FAQ oficial da ANP no gov.br, que é também onde consta que as amostras podem servir de prova em defesa administrativa ou judicial desde que coletadas pelo procedimento da resolução.
  9. **Proconve P-8 obrigatório para veículos novos desde 1º/01/2023**, com dependência de catalisador e SCR com ARLA 32, e o enxofre em excesso envenenando esses catalisadores. Base da seção que separa dano de pós-tratamento de dano de sistema de injeção.
  10. **CDC lido no texto compilado do Planalto**, artigo a artigo: art. 12 (caput e § 3º, III — culpa exclusiva de terceiro), art. 13 (caput, três incisos e parágrafo único do regresso), art. 18, art. 25 § 1º (solidariedade), art. 26 (30/90 dias e o § 3º do vício oculto) e art. 27 (cinco anos "a partir do conhecimento do dano e de sua autoria"). **Art. 381 do CPC lido no texto do Planalto**, incisos I a III.
- **O que foi deixado deliberadamente de fora:** (a) **valores da especificação da gasolina** — goma lavada, massa específica e destilação —, porque o Anexo da RANP 807/2020 não foi lido em fonte primária nesta execução e citar número não conferido é exatamente o erro do SEO-002; a página trata a gasolina por regime (E30, RON, carência) e não por tabela de limites; (b) **jurisprudência sobre responsabilidade do posto revendedor** — o art. 13 é apresentado no seu texto, como a estrutura do argumento que a prova técnica precisa alimentar, sem afirmar entendimento consolidado que não foi verificado; (c) **prazo entre abastecimento e falha** — não há número citável, e a página trata o ponto como quesito de causas concorrentes.
- **Manutenção:** rever quando a **Resolução ANP nº 968/2024** for alterada, porque é ela que carrega todos os números da página, e quando o teor obrigatório de etanol ou de biodiesel mudar — as duas mudanças de 1º/08/2025 mostram que esse é o parâmetro mais volátil do setor.

### Verificação de renderização — e uma correção de método

Chrome real via Playwright (`channel="chrome"`, `/usr/bin/python3`) contra `http://localhost:8899`, a 375 px e 1280 px, com `/pericia-combustiveis/` e `/analise-microbiologica-alimentos/` como controle.

- **Sem overflow horizontal nas três páginas, nas duas larguras** (`scrollWidth == clientWidth`, com `innerWidth == clientWidth` confirmando a leitura). As três tabelas medem 544 px de conteúdo em contêiner de 311 px a 375 px — o "sem overflow" não vem de tabela estreita demais para transbordar.
- **12 de 12 âncoras assentam em y = 112 px**, abaixo do cabeçalho fixo de 98 px. **Controle negativo:** com `scroll-margin-top` desligado por `add_style_tag`, as 12 caem para **y = 0** — a medição sabe reprovar.
- **Correção de método sobre a execução de 29/08.** A primeira rodada mediu `#janela` em 204 px e, num segundo teste, em 946 px — números que pareciam defeito de layout e não eram: eram a **animação do `scroll-behavior: smooth` ainda em curso**, e a espera fixa de 700 ms não a cobria em saltos longos de página. A solução não é esperar mais: é **injetar `html { scroll-behavior: auto !important }` antes de medir**, tornando a medida determinística. Com isso, 12/12 em 112 com a regra e 12/12 em 0 sem ela, sem nenhuma espera. *Substituir a espera pela remoção da animação é melhor do que calibrar o tempo de espera — a regra 10 vale também contra falsos positivos, não só contra falsos negativos.*

### Sobre a checagem de paridade de FAQ do `seo-report.py` — o que ela não faz

Aplicando a regra 10, injetou-se um defeito para ver a checagem reprovar. **Ela passou.** A investigação mostrou que isso é **projeto, não bug**: `check_faq_parity` reprova apenas quando *nem a pergunta nem a resposta* aparecem na página, porque o que carrega penalidade do Google é o dado estruturado oculto, e exigir correspondência integral geraria ruído em página cuja `<h3>` é redigida mais curta que a pergunta do schema. Três controles delimitaram a fronteira: corromper **só** a resposta → o `seo-report` passa e o script estrito reprova; **remover** uma pergunta visível → o script estrito reprova por contagem; corromper **pergunta e resposta** → o `seo-report` reprova com `FAQPage oculto`. **Consequência operacional: `ALL PASS` do `seo-report` não é prova de paridade caractere a caractere — o script estrito continua necessário, e não é redundante.**

### Próxima execução — o que checar primeiro

1. **Rodar `tools/seo-report.py` em `deploy`, `valid` e `gsc` antes de decidir qualquer coisa** — `gsc` exige `/usr/bin/python3`. O teste de Prioridade 2 continua sendo o `query × page` a 90 dias contra o conteúdo existente, com conferência por levantamento de termo, não por impressão.
2. **`/dano-motor-combustivel/`: primeira leitura a partir de ~07/09.** Consultas a vigiar: `combustível adulterado danificou motor`, `perícia combustível dano motor`, `bomba injetora combustível ruim`, `diesel com água dano motor`, `lubricidade diesel bomba`, `S500 em veículo S10`, `produção antecipada de prova combustível`, `filtro entupido parafina diesel frio`. **Conferir canibalização com `/pericia-combustiveis/`**, de onde a fronteira foi traçada.
3. **`/produtos-quimicos-controlados/` (~05/09) e `/rotulagem-alimentos/` (~06/09): leituras seguem marcadas.** A primeira já apareceu em posição 6,0 com 2 impressões.
4. **O cluster de Combustíveis passou a ter duas páginas; o de Alimentos tem quatro e está em observação.** Antes de acrescentar uma terceira em Combustíveis, verificar se a segunda entra abaixo de 10 — mesma disciplina aplicada a Alimentos no item 6 de 29/08.
5. **Se as páginas novas continuarem entrando em 5–6 e os cliques não subirem proporcionalmente, o gargalo deixou de ser posição e passou a ser CTR e volume de consulta.** Nesse caso a fila deixa de ser conteúdo e vira aquisição de citação e menção — Prioridade 8 do mandato, ainda nunca executada.
6. **`art. 381` do CPC entrou no site por esta página, e `/cpc-prova-pericial/` — que é a referência processual do site — continua sem tratá-lo.** É a única lacuna interna aberta hoje: candidata a uma seção nova naquela página, não a uma página nova.
7. **Parafrasear tabela é tão arriscado quanto parafrasear norma.** O erro do ponto de entupimento saiu com a tabela aberta na tela. Copiar os valores para o texto e reconferir contra a fonte, célula a célula, antes do commit.
8. **`ALL PASS` do `seo-report` não prova paridade de FAQ.** Rodar sempre o script estrito de comparação caractere a caractere.
9. **Para medir âncora, desligar a animação em vez de esperar por ela.** `html { scroll-behavior: auto !important }` via `add_style_tag`.
10. **Presumir revogação e provar vigência** — segue valendo, e nesta execução evitou tratar a RANP 902/2022 como especificação de etanol quando ela é o programa de marcação.
11. **Gerar FAQ visível e JSON-LD da mesma fonte de dados.** Quinta execução; segue eliminando a classe de erro.
12. **Escalar o Google Ads sem entrega.** Décima terceira execução como nota de rodapé. Não é item de SEO — cabe uma mensagem direta à cliente.

---

## Estado da medição — 2026-09-02

Período 28 dias. **728 impressões · 9 cliques · CTR 1,24%.** GA4: 62 sessões, **9 de Organic Search**.

| Página | Impressões | Posição | Cliques |
|---|---|---|---|
| `/quesitos-periciais/` | 257 | 11,0 | 1 |
| `/impugnacao-laudo-pericial/` | 94 | 13,1 | 0 |
| `/assistente-tecnica/` | **80** | **9,9** | 0 |
| `/honorarios-pericia-judicial/` | 65 | 11,5 | 1 |
| `/laudo-pericial/` | 62 | 8,9 | 0 |
| `/normas-tecnicas-pericia/` | 53 | **5,7** | 0 |
| `/pericia-combustiveis/` | 27 | **5,9** | 2 |
| `/cpc-prova-pericial/` | 27 | 8,1 | 0 |
| `/pericia-industria-quimica/` | 13 | **6,2** | 1 |
| `/pericia-contaminacao-alimentos/` | 12 | **6,2** | 2 |
| `/prazo-validade-alimentos/` | 8 | **6,0** | 0 |
| `/produtos-quimicos-controlados/` | 2 | **6,0** | 0 |

### O gatilho pré-registrado do item 5 de 31/08 foi testado — e **não** disparou

O item 5 previa: *se as páginas novas continuarem entrando em 5–6 e os cliques não subirem proporcionalmente, o gargalo deixou de ser posição e passou a ser CTR e volume — e a fila deixa de ser conteúdo e vira aquisição de citação (Prioridade 8).*

- **27/08:** 484 impressões · 5 cliques · CTR 1,03%
- **02/09:** 728 impressões · 9 cliques · CTR 1,24%

Impressões **+50%**, cliques **+80%**. Os cliques subiram *mais rápido* que as impressões e a CTR agregada subiu. **A condição do gatilho não se verificou**, e a Prioridade 8 não foi acionada. Registrado como teste falseável que saiu negativo — a estratégia de conteúdo segue sendo a alavanca. Reavaliar no mesmo formato na próxima leitura.

### Prioridades 1 e 2 verificadas — sem alavanca disponível

- **Prioridade 1:** `/quesitos-periciais/` mantém 257 impressões (35% do site) a 0,4% de CTR na posição 11,0. Diagnóstico de 27/08 e 31/08 inalterado: posição 11 é topo de página 2, onde a CTR desaba independentemente do metadado, e a SEO-016 foi encerrada após inspeção um a um dos títulos e descriptions. A alavanca é autoridade, não reescrita.
- **Prioridade 2:** o `query × page` expôs 32 linhas (62 de 728 impressões; o resto anonimizado). Na faixa 5–20: `emitir despacho - sem quesitos` (9,0), `anexo juntado: apresentação de esclarecimentos ao laudo` (8,2), `art. 95, § 3º, ii, do cpc` (9,0), `impugnação ao laudo pericial cpc` (9,0), `assistente tecnico pericia` (16,0), `assistente técnico` (18,0). Todas apontam para tema **já coberto** — as duas últimas para `/assistente-tecnica/`, que é justamente a página que mais cresceu (80 impressões, pos 9,9). Sem tema meio coberto, a criação de conteúdo fica liberada pela regra do mandato.
- **Indexação:** 19 de 20 páginas indexadas. `/dano-motor-combustivel/` em *"Detectada, mas não indexada no momento"* — publicada em 31/08, um dia antes da leitura. Aguardar, não agir.
- **Falha transitória descartada:** `[deploy]` reprovou `/honorarios-pericia-judicial/` por *read timeout*. Três novas requisições retornaram **200** em 0,38 s, 0,10 s e 0,08 s. Rede, não site.

### A lacuna: o site inteiro ignora a prova que se produz antes da ação

Levantamento por termo nas 19 páginas (~93.000 palavras):

| Termo | Ocorrências no site |
|---|---|
| "produção antecipada" | **5 — todas em `/dano-motor-combustivel/`**, publicada em 31/08 |
| "381" | 3 — idem |
| "cautelar" | 1 — em página de outro assunto |
| "ata notarial" | **0** |
| "perpetuação" / "prevenção do juízo" | **0** |

`/cpc-prova-pericial/`, que é a referência processual do site e percorre os arts. 464 a 480 mais os arts. 95, 98 e 156 a 158, **não mencionava o art. 381 uma única vez**. Era a lacuna interna registrada no item 6 de 31/08.

**Por que virou página e não seção**, contrariando a hipótese do item 6: (a) é procedimento próprio, com competência, contraditório, recurso e destino dos autos próprios — arts. 381 a 383; (b) a intenção de busca é distinta da de "prova pericial no CPC"; (c) o momento comercial é o mais valioso do site, porque o cliente contrata a assistente técnica **antes** de existir ação; (d) `/cpc-prova-pericial/` é organizado explicitamente "na ordem em que o processo os aciona" e começa no art. 464 — o art. 381 acontece antes de haver processo e quebraria essa espinha. A seção foi feita **também**, como porta de entrada, resolvendo a canibalização na origem.

### SEO-042 — Página: produção antecipada de prova pericial *(executada em 2026-09-02)*
- **Descrição:** As três hipóteses do art. 381, o que perece em cada matéria técnica e em que ritmo, a fronteira entre ata notarial e perícia antecipada, o recorte do objeto no art. 382 e o papel do assistente técnico numa prova que não se repete.
- **URL:** `/producao-antecipada-prova/`
- **Categoria:** Conteúdo / Referência processual / Prova técnica pré-processual
- **Impacto:** 8 · **Esforço:** 4 · **Confiança:** 8 · **Valor de negócio:** 9
- **Priority Score:** 144
- **Status:** done · **Descoberto:** 2026-09-02 · **Concluído:** 2026-09-02
- **Por que esta:** maior lacuna tópica do site medida por levantamento de termo (cobertura zero de um instrumento processual central); conecta **seis** clusters em vez de abrir frente nova, porque prova perece em combustível, alimento, microbiologia, ambiental, indústria química e rotulagem; captura o cliente no ponto mais precoce e mais valioso da jornada; e a própria página de 31/08 já gerava demanda interna de link sem destino.
- **Implementado:** ~4.200 palavras. Três tabelas: as três hipóteses do art. 381 (inciso → texto → o que demonstrar → situação técnica); o que perece por matéria (6 linhas: combustíveis, alimentos-conformidade, alimentos-microbiológico, ambiental-efluente, ambiental-solo, indústria química); e ata notarial × produção antecipada em 7 dimensões. Nove quesitos de estrutura. Cinco erros que inutilizam a medida. `Article` (com `isPartOf` apontando para `/cpc-prova-pericial/`) + `FAQPage` (8) + `BreadcrumbList` de três níveis, com o `@id` canônico do `Person`.

- **A tese central:** *a prova técnica tem prazo próprio, e esse prazo não é o do processo.* Quando o objeto do exame é consumido, reparado, descartado ou muda com o tempo, a perícia da ação principal chega para examinar **outra coisa** — e nada disso é má-fé, é o funcionamento normal de uma oficina, de uma fábrica e de um corpo d'água.
- **A segunda tese, a que corrige um erro difundido de fundamentação:** *o art. 381 tem três hipóteses independentes e só a primeira é de urgência.* O inciso II (viabilizar autocomposição) e o inciso III (justificar ou **evitar** o ajuizamento) não contêm elemento de perigo na demora. Fundamentar só em perecimento, quando o caso é de inciso III, cria uma controvérsia sobre urgência que o pedido não precisaria travar.
- **A terceira tese, que separa dois instrumentos que a prática confunde:** *ata notarial preserva aparência; perícia antecipada preserva análise.* O tabelião atesta a existência e o modo de existir de um fato perceptível (art. 384) — não mede teor, contagem microbiana, concentração nem composição. Daí o uso combinado e a ordem correta: a ata lavrada no dia seguinte registra o estado, o lacre e a guarda, **documentando a cadeia de custódia** enquanto o pedido de produção antecipada é preparado.
- **A quarta tese, operacional e a mais específica do site:** *a janela de perecimento se mede em eventos, não em dias de calendário* — o próximo recebimento de combustível, a próxima parada de manutenção, o próximo ciclo de limpeza. E **a limpeza destrói tanta prova quanto o descarte**: peça lavada perde borra, particulado e produto de corrosão, que são a assinatura do mecanismo.
- **O achado de redação que muda a petição:** o art. 382, § 4º, só admite recurso contra o indeferimento **totalmente** denegatório. O indeferimento **parcial** — o que autoriza o exame mas recorta o objeto — não abre recurso. Como o recorte é onde se decide se o laudo responderá à pergunta do caso, o momento de acertar é a inicial.
- **Paridade de FAQ garantida por construção** (sexta execução do método da SEO-037): as 8 perguntas e respostas definidas uma única vez em `faq.py`, com HTML visível e JSON-LD gerados da mesma fonte. Conferido por script estrito: **8/8 idênticos caractere a caractere**.
- **Links de entrada:** 5 páginas — card de Insights na home; **seção nova em `/cpc-prova-pericial/`** ("Antes da ação: a perícia que não pode esperar o processo", que fecha o item 6 de 31/08 e serve de porta); link contextual **no parágrafo do art. 381 em `/dano-motor-combustivel/`**, que citava o artigo sem destino, mais entrada no "Continue lendo"; e entradas em `/assistente-tecnica/`, `/pericia-contaminacao-alimentos/` e `/laudo-pericial/`, com âncoras diferenciadas por vizinhança (critério da SEO-019). `sitemap.xml` e `llms.txt` atualizados, com "Produção Antecipada de Prova" passando a serviço próprio na lista do `llms.txt`.

- **Verificação factual — texto literal do CPC antes de publicar:**
  1. **Arts. 381, 382, 383 e 384 lidos no texto compilado da Lei nº 13.105/2015 no Planalto**, baixado localmente e extraído artigo a artigo. Conferidos: art. 381 caput e incisos I a III; §1º (arrolamento só para documentação, sem atos de apreensão); §2º (competência do foro onde a prova deva ser produzida **ou** do foro de domicílio do réu); §3º (**não previne** a competência); §4º (juízo estadual contra União, autarquia ou empresa pública federal onde não houver vara federal); §5º (justificação, "para simples documento e sem caráter contencioso"). Art. 382 caput e §§ 1º a 4º. Art. 383 e parágrafo único. Art. 384 e parágrafo único.
  2. **Art. 383 diz "durante 1 (um) mês"**, não "trinta dias" — a página usa "um mês", e a expressão saiu certa porque o texto literal estava aberto quando foi redigida, não porque tenha sido corrigida depois. Registrado como o tipo de detalhe que a paráfrase de memória erra: "um mês" e "trinta dias" divergem em quatro meses do ano.
  3. **Art. 382, § 4º — a palavra é "totalmente".** A ressalva recursal alcança apenas o indeferimento **total**; o indeferimento parcial, que recorta o objeto do exame, não abre recurso. Nenhum erro foi cometido e depois corrigido aqui — o advérbio foi lido na fonte e o ponto virou seção própria (caixa "O detalhe do § 4º que muda a redação do pedido") justamente porque é ele que carrega a consequência prática. **Nesta execução não houve erro factual próprio a registrar**, ao contrário das SEO-002 e SEO-041.
  4. **Arts. 464, 465 e 466 lidos no mesmo texto**, para a articulação com a perícia: art. 464 caput ("exame, vistoria ou avaliação"); art. 465, § 1º, I a III (quinze dias para impedimento/suspeição, indicação de assistente técnico e quesitos); art. 466, § 2º (acesso e acompanhamento dos assistentes, comunicação prévia comprovada, **antecedência mínima de cinco dias**).
  5. **Nenhuma jurisprudência e nenhuma doutrina foram afirmadas.** A tese sobre a autonomia dos incisos II e III é sustentada **pelo próprio texto legal**, que não contém elemento de urgência neles — não por entendimento consolidado que não foi verificado. Mesma disciplina do item (b) deixado de fora em 31/08.
  6. **Reuso apenas de fato já verificado no site:** Resolução ANP nº 898/2022 e os três últimos recebimentos (verificados em 31/08); Lei nº 6.437/1977 e a amostra de contraprova (verificada em 28/08); acreditação ABNT NBR ISO/IEC 17025 (verificada em 03/08).
- **O que foi deixado deliberadamente de fora:** (a) **números de resolução em matéria ambiental** — a tabela do que perece trata efluente e pluma pelo comportamento físico (fluxo × estoque, migração e atenuação), sem citar limite ou norma que não tenha sido lida em fonte primária nesta execução; (b) **prazos e custos do procedimento** — não há número citável e a variação por comarca é grande; (c) **discussão sobre eficácia do laudo antecipado perante quem não foi citado** — depende de entendimento jurisprudencial não verificado, e a página se limita a registrar o que o art. 382, § 1º, determina.
- **Manutenção:** baixa. A base é texto de código processual, que muda pouco. Rever se houver alteração nos arts. 381 a 384.

### Verificação de renderização

Chrome real via Playwright (`channel="chrome"`, `/usr/bin/python3`) contra `http://localhost:8899`, a 375 px e 1280 px, com `/cpc-prova-pericial/` — a página modificada — como controle.

- **Sem overflow horizontal nas duas páginas, nas duas larguras** (`scrollWidth == clientWidth`, com `innerWidth` confirmando a leitura).
- **9 de 9 âncoras assentam em y = 112 px**, abaixo do cabeçalho fixo. **Controle negativo:** com `scroll-margin-top` desligado, as 9 caem para **y = 0**. A medição sabe reprovar.
- Animação desligada por `html { scroll-behavior: auto !important }` antes de medir, conforme o item 9 de 31/08. Zero espera, medida determinística.

### Controle negativo da paridade de FAQ

Aplicando a regra 10 também ao script estrito: injetou-se um defeito em **uma única resposta visível** (troca de acentuação em 4 caracteres), deixando o JSON-LD intacto. O script **reprovou, apontando o item 2**. Página restaurada e paridade reconferida depois do restauro. O `seo-report` seguiu em `ALL PASS` durante o defeito, confirmando de novo o que o item 8 de 31/08 registrou: **`ALL PASS` não é prova de paridade**.

### Próxima execução — o que checar primeiro

1. **Rodar `tools/seo-report.py` em `deploy`, `valid` e `gsc` antes de decidir qualquer coisa** — `gsc` exige `/usr/bin/python3`. Um `ERR timeout` isolado no `[deploy]` deve ser reconferido com `curl` antes de virar item: em 02/09 foi rede, não site.
2. **Repetir o teste do gatilho do item 5 no formato de 02/09** — impressões e cliques lado a lado contra a leitura anterior. Se desta vez os cliques crescerem **menos** que as impressões, a Prioridade 8 (citação e menção) passa à frente do conteúdo. Hoje: +50% impressões, +80% cliques, gatilho não disparado.
3. **`/dano-motor-combustivel/`: conferir se saiu de "Detectada, mas não indexada".** Se ainda não estiver indexada por volta de 10/09, aí sim é item, não espera.
4. **`/producao-antecipada-prova/`: primeira leitura a partir de ~09/09.** Consultas a vigiar: `produção antecipada de prova pericial`, `art 381 cpc`, `produção antecipada de prova requisitos`, `ata notarial ou perícia`, `perícia antes de entrar com ação`, `assistente técnico produção antecipada`, `preservar prova antes do processo`. **Conferir canibalização com `/cpc-prova-pericial/`**, de onde a fronteira foi traçada, e observar se a seção nova daquela página muda a sua posição média (hoje 8,1).
5. **`/assistente-tecnica/` foi a página que mais cresceu (80 impressões, pos 9,9) e é a de maior valor comercial do site.** As consultas `assistente técnico` (18,0) e `assistente tecnico pericia` (16,0) estão na faixa 5–20 e apontam para ela. É a primeira candidata de Prioridade 2 da próxima leitura — verificar se a nova página de entrada precoce a empurra.
6. **O cluster processual tem agora 7 páginas** (cpc, assistente, quesitos, laudo, impugnação, honorários, produção antecipada) e é o que ranqueia 9–13, não 5–6. Antes de acrescentar a oitava, verificar se a sétima entra abaixo de 10 — mesma disciplina aplicada a Alimentos e a Combustíveis.
7. **Advérbio em texto legal costuma ser o que carrega a consequência.** "Indeferir **totalmente**" (art. 382, § 4º) e "durante **1 (um) mês**" (art. 383) são os dois casos desta execução. Ambos saíram corretos porque o texto do Planalto estava aberto durante a redação — o método que funcionou foi *redigir com a fonte à vista*, não *redigir e conferir depois*. Manter esse método: baixar o texto literal antes de escrever a seção, não antes do commit.
8. **`ALL PASS` do `seo-report` não prova paridade de FAQ.** Rodar sempre o script estrito, e passar o controle negativo nele.
9. **Para medir âncora, desligar a animação em vez de esperar por ela.**
10. **Presumir revogação e provar vigência** — segue valendo.
11. **Gerar FAQ visível e JSON-LD da mesma fonte de dados.** Sexta execução; segue eliminando a classe de erro.
12. **Escalar o Google Ads sem entrega.** Décima quarta execução como nota de rodapé. Não é item de SEO — cabe uma mensagem direta à cliente.

---

## Estado da medição — 2026-09-02 (segunda execução do dia)

Período 28 dias. **782 impressões · 9 cliques · CTR 1,15%.** A leitura da manhã registrou 728 · 9. As duas leituras estão separadas por horas, não por dias: **a variação não é tendência e o teste do gatilho do item 5 não foi repetido aqui** — repeti-lo com esse intervalo seria medir ruído. Fica para a próxima execução em dia distinto, no formato de 02/09 (manhã).

| Página | Impressões | Posição | Cliques |
|---|---|---|---|
| `/quesitos-periciais/` | 280 | 10,8 | 1 |
| `/impugnacao-laudo-pericial/` | 97 | 12,9 | 0 |
| `/assistente-tecnica/` | 80 | 10,0 | 0 |
| `/honorarios-pericia-judicial/` | 75 | 10,7 | 1 |
| `/laudo-pericial/` | 62 | 8,9 | 0 |
| `/normas-tecnicas-pericia/` | 57 | **5,8** | 0 |
| `/cpc-prova-pericial/` | 35 | 8,3 | 0 |
| `/pericia-combustiveis/` | 28 | **5,7** | 2 |
| `/classificacao-fiscal-ncm/` | 16 | 12,7 | 0 |
| `/pericia-industria-quimica/` | 13 | **6,2** | 1 |
| `/pericia-contaminacao-alimentos/` | 12 | **6,2** | 2 |
| `/prazo-validade-alimentos/` | 8 | **6,0** | 0 |
| `/` | 7 | **6,0** | 1 |
| `/sobre/` | 5 | 11,8 | 1 |
| `/produtos-quimicos-controlados/` | 3 | **4,3** | 0 |
| `/analise-microbiologica-alimentos/` | 2 | 39,5 | 0 |
| `/pericia-ambiental/` | **2** | **7,5** | 0 |

- **Indexação:** `/dano-motor-combustivel/` segue em *"Detectada, mas não indexada"* (publicada em 31/08 — dentro da janela de espera do item 3). `/producao-antecipada-prova/` em *"O Google não reconhece o URL"*, publicada hoje — esperado. `/pericia-combustiveis/` teve **falha de inspeção por timeout**, não reprovação de indexação: mesma classe de ruído de rede registrada em 02/09 (manhã) no `[deploy]`.
- **Novo canal na leitura do GA4:** `/quesitos-periciais/` recebeu 2 sessões de **`AI Assistant`**. É a primeira vez que o canal de busca por LLM aparece nominalmente nos dados desta propriedade. Não é base para decisão ainda — é marco para acompanhar.

### Prioridades 1 e 2 verificadas — e por que a Prioridade 2 pré-registrada não virou tarefa

- **Prioridade 1:** `/quesitos-periciais/` mantém o padrão (280 impressões, 36% do site, CTR 0,4%, posição 10,8). Diagnóstico de 27/08, 31/08 e 02/09 inalterado — posição 11 é topo de página 2. A SEO-016 já encerrou a via de metadado. Sem alavanca nova.
- **Prioridade 2 — o item 5 pré-registrado foi testado e recusado por falta de massa.** O item 5 de 02/09 (manhã) apontava `/assistente-tecnica/` como primeira candidata, pelas consultas `assistente técnico` (pos 18,0) e `assistente tecnico pericia` (pos 16,0). Ao abrir o `query × page` desta leitura, **as duas consultas têm 1 impressão cada**. Agir sobre elas seria otimizar ruído, não uma faixa 5–20 com massa. Ordenadas por impressão, as consultas em 5–20 são `emitir despacho - sem quesitos` (9 impressões, pos 9,0) e `anexo juntado: apresentação de esclarecimentos ao laudo` (4, pos 8,2) — ambas apontam para tema **já coberto**. Registrado como candidata pré-registrada que **não se confirmou ao ser medida**, e não como item pendente.
- **Um padrão que a lista de consultas expõe e que não estava registrado:** as páginas ranqueiam bem em cauda longa processual e **mal no termo-cabeça do próprio assunto**. `/impugnacao-laudo-pericial/` está em 9,0 para `impugnação ao laudo pericial cpc`, mas em **26,8 / 30,3 / 44,0 / 47,0** para `impugnação ao laudo pericial`, `impugnação laudo pericial`, `impugnação de laudo pericial` e `impugnar laudo pericial`. O mesmo em quesitos (`quesitos` 36,8; `quesitos periciais` 42,5). Isso é sinal de **autoridade tópica**, não de metadado — e é coerente com a decisão de seguir expandindo cluster.

### A lacuna: o cluster Ambiental tem pilar e não tem nada mais

Levantamento por termo nas 20 páginas:

| Termo | Ocorrências no site | Onde |
|---|---|---|
| "IBAMA" | **0** | — |
| "9.605" (Lei de Crimes Ambientais) | **0** | — |
| "6.514" (regulamento das infrações) | **0** | — |
| "automonitoramento" | **0** | — |
| "condicionante" | **0** | — |
| "outorga" | **0** | — |
| "DBO" / "DQO" | **0** | — |
| "licenciamento" | 1 | numa página de outro assunto |
| "auto de infração" | 30 | **1 única** em `/pericia-ambiental/`; 11 em NCM, 6 em rotulagem |

O contraste com o próprio site é o argumento: **o padrão que converte aqui é "você foi autuado, esta é a defesa técnica"** — é o que sustenta `/classificacao-fiscal-ncm/`, `/rotulagem-alimentos/` e `/produtos-quimicos-controlados/`. Esse padrão **não existia no cluster Ambiental**, que tinha só o pilar genérico.

O dado empírico fecha o diagnóstico: `/pericia-ambiental/` e `/pericia-combustiveis/` foram publicadas no **mesmo dia** (04/08), com esforço equivalente. Um mês depois, Combustíveis tem 28 impressões, 2 cliques e a melhor CTR do site (7,1%); Ambiental tem **2 impressões**, posição 7,5, zero clique. Ambiental ranqueia bem e **não é procurada**, porque o pilar responde a uma categoria e não a uma pergunta. A disciplina do mandato foi respeitada: antes de acrescentar a segunda página do cluster, verificou-se que a primeira entra **abaixo de 10** (7,5).

### SEO-043 — Página: auto de infração ambiental e defesa técnica *(executada em 2026-09-02, segunda execução)*
- **Descrição:** O que o auto precisa descrever, o teste do vício insanável, o ônus da prova no processo administrativo sancionador, o calendário federal, a distinção entre descumprir padrão de lançamento e praticar a infração de poluição, e as condições de validade do dado analítico em efluentes.
- **URL:** `/auto-infracao-ambiental/`
- **Categoria:** Conteúdo / Autoridade tópica / Defesa administrativa / Cluster Ambiental
- **Impacto:** 8 · **Esforço:** 4 · **Confiança:** 8 · **Valor de negócio:** 9
- **Priority Score:** 144
- **Status:** done · **Descoberto:** 2026-09-02 · **Concluído:** 2026-09-02
- **Por que esta:** o cluster mais fraco do site medido por dado (2 impressões em 28 dias contra 28 do gêmeo publicado no mesmo dia); a maior lacuna de entidade medida por levantamento de termo (IBAMA, Lei 9.605/1998, Decreto 6.514/2008, automonitoramento — todos em zero); e a aplicação, ao único cluster que ainda não a tinha, do padrão editorial que já sustenta as três páginas de autuação do site. Prioridade 1 sem alavanca e Prioridade 2 recusada por falta de massa, ambas verificadas antes.
- **Implementado:** ~7.275 palavras. Três tabelas: vício sanável × insanável (4 dimensões, com o teste do art. 100, § 1º); fases e prazos do processo federal (8 linhas, com a coluna "o que a técnica produz aqui"); e as condições de lançamento do art. 16, I, da CONAMA 430/2011 (8 linhas, valor a valor). Cinco falhas que enfraquecem a defesa. Checklist de análise preliminar. `Article` (com `isPartOf` apontando para `/pericia-ambiental/`) + `FAQPage` (8) + `BreadcrumbList` de três níveis, com o `@id` canônico do `Person`. Entidades novas para o grafo: **IBAMA**, **Licenciamento Ambiental**, **Efluentes Industriais**, **Auto de Infração Ambiental**.

- **A tese central:** *no processo administrativo sancionador, o ônus da prova dos fatos alegados pela defesa é do autuado* — art. 118 do Decreto nº 6.514/2008. Isso inverte a intuição formada na esfera cível, onde a responsabilidade é objetiva e o ônus é invertido em favor de quem alega o dano. São esferas diferentes com regras de prova opostas, e confundi-las é o erro estratégico mais caro: alegação técnica sem laudo, sem série histórica e sem memorial de cálculo é argumento, e argumento não desloca dado.
- **A segunda tese, que separa duas perguntas que chegam no mesmo papel:** *ultrapassar um padrão de lançamento não é, por si só, a infração de poluição.* O caput do art. 61 do Decreto nº 6.514/2008 exige níveis que resultem ou possam resultar em dano à saúde humana, mortandade de animais ou destruição significativa da biodiversidade — há elemento de nível e de efeito que não decorre aritmeticamente da superação de um limite. E o parágrafo único condiciona a penalidade a **laudo técnico do órgão identificando a dimensão do dano e a gradação do impacto**, o que dá à dosimetria um pressuposto documental verificável.
- **A terceira tese, que dá critério objetivo a uma discussão normalmente retórica:** *o vício é insanável quando corrigi-lo implica modificar o fato descrito no auto* (art. 100, § 1º). Traduzido para a prática técnica: se o auto imputa lançamento num ponto e o laudo mede outro, ou autua um parâmetro e ensaia outro, a correção não é convalidação — é autuação nova. Isso transforma "o auto está mal fundamentado" numa checagem documental linha a linha.
- **A quarta tese, operacional e específica do site:** *na maior parte das autuações por lançamento, a prova contra a empresa foi produzida e entregue pela própria empresa* — automonitoramento do art. 24 e Declaração de Carga Poluidora do art. 28 da CONAMA 430/2011, esta até 31 de março de cada ano. A mesma resolução que obriga a produzir o dado fixa as condições que ele precisa cumprir (amostragem representativa no art. 24; coleta e análise por profissional legalmente habilitado no art. 25; laboratório acreditado pelo INMETRO com controle de qualidade analítica implementado no art. 26). Dado que não cumpre as condições da própria norma é frágil **nos dois sentidos**.
- **O achado de leitura que evita erro de cálculo:** o padrão de DBO do art. 16 é **remoção mínima de 60%** — uma eficiência, não uma concentração. Demonstrá-la exige medição pareada de afluente e efluente. Autuação que compara a DBO de saída com um número absoluto está aplicando outro critério, que pode ser legítimo se vier da licença ou de norma estadual mais restritiva, mas então é essa a norma que precisa constar do auto.
- **Paridade de FAQ garantida por construção** (sétima execução do método da SEO-037): as 8 perguntas e respostas definidas uma única vez em `faq.py`, com HTML visível e JSON-LD gerados da mesma fonte. Conferido por script estrito: **8/8 idênticos caractere a caractere**.
- **Links de entrada:** 6 páginas — card de Insights na home; **parágrafo contextual novo em `/pericia-ambiental/`**, colocado exatamente na dobra entre a seção de efluentes e a de responsabilidade civil, porque é ali que a troca de esfera (e a inversão do ônus) precisa ser avisada; e entradas em `/normas-tecnicas-pericia/`, `/pericia-industria-quimica/`, `/classificacao-fiscal-ncm/` (o paralelo direto da autuação) e `/assistente-tecnica/`, com âncoras diferenciadas por vizinhança (critério da SEO-019). `sitemap.xml` e `llms.txt` atualizados, com "Defesa Técnica em Auto de Infração Ambiental" passando a serviço próprio na lista do `llms.txt`.

- **Verificação factual — 41 pontos conferidos por script contra a fonte primária baixada:**
  1. **Método:** os textos do **Decreto nº 6.514/2008** e da **Lei nº 9.605/1998** foram baixados do Planalto e a **Resolução CONAMA nº 430/2011** do sítio do CONAMA (PDF oficial, 9 páginas), extraídos para texto e mantidos abertos durante a redação — o método registrado no item 7 de 02/09 (manhã): *redigir com a fonte à vista*, não redigir e conferir depois. Ao final, um script conferiu **41 agulhas literais** (valores, prazos e trechos citados) contra os três textos: **41/41 ok**.
  2. **A armadilha do texto compilado do Planalto, que quase custou um erro:** o HTML compilado exibe **as redações revogadas junto com a vigente**, na mesma sequência. Os arts. 98, 99, 100, 113, 119, 120 e 127 aparecem em duas ou três versões seguidas. Foi preciso extrair **todas** as ocorrências de cada artigo e escolher a última deliberadamente. Ler o primeiro resultado teria produzido citação de norma revogada em pelo menos quatro artigos.
  3. **O art. 119, § 1º, do Decreto nº 6.514/2008 — prazo de dez dias para o parecer técnico — foi REVOGADO pelo Decreto nº 11.373/2023.** A redação vigente do art. 119, dada pelo mesmo decreto, não tem prazo. Este é o achado que mais se aproximou de virar erro: o prazo de dez dias é o que aparece primeiro no texto compilado e é o que circula em material de terceiros. A página **registra a revogação em caixa própria**, o que a torna mais correta que a maior parte do conteúdo concorrente — mesma vantagem competitiva da multa de 1% na SEO-002.
  4. **Redações vigentes confirmadas artigo a artigo:** art. 99 e art. 100 na redação do **Decreto nº 11.080/2022**; art. 113 na redação do **Decreto nº 11.080/2022**; art. 97-A e o sobrestamento do prazo incluídos pelo **Decreto nº 9.760/2019**; art. 120 na redação do **Decreto nº 11.080/2022**; art. 119 na redação do **Decreto nº 11.373/2023**.
  5. **Valores da CONAMA 430/2011 copiados célula a célula e reconferidos** (item 7 de 31/08): pH 5 a 9; temperatura inferior a 40 °C com variação do corpo receptor até 3 °C no limite da zona de mistura; materiais sedimentáveis até 1 mL/L em teste de uma hora; vazão máxima de até 1,5 vez a vazão média do período de atividade diária; óleos minerais até 20 mg/L; óleos vegetais e gorduras animais até 50 mg/L; ausência de materiais flutuantes; DBO 5 dias a 20 °C com remoção mínima de 60%.
  6. **Uma divergência de grafia tratada explicitamente:** o PDF oficial da CONAMA 430/2011 imprime "cone **Inmhoff**"; o equipamento é o cone **Imhoff**. A página usa a grafia correta **em descrição, não entre aspas**, para não atribuir à norma um texto que ela não tem nem propagar o erro de digitação da fonte.
  7. **Nenhuma jurisprudência foi afirmada.** A tese sobre o elemento de nível e efeito do art. 61 é sustentada **pelo próprio texto do caput e do parágrafo único**, não por entendimento consolidado que não foi verificado. Mesma disciplina das duas execuções anteriores.
- **O que foi deixado deliberadamente de fora:** (a) **prazos e procedimento de órgãos estaduais e municipais** — a página abre com caixa de ressalva dizendo que o Decreto nº 6.514/2008 é federal e que o prazo do caso precisa ser lido na norma do órgão que lavrou o auto; citar prazos da CETESB sem ler a norma paulista seria exatamente o erro que a caixa alerta; (b) **a Tabela I do art. 16 (padrões por parâmetro)** — foi lida e conferida, mas reproduzi-la inteira acrescentaria volume sem decisão, e a página remete à resolução; (c) **critérios de dosimetria e valores de multa por infração além do art. 61** — dependem de leitura completa do Anexo e de atos do órgão que não foram verificados nesta execução; (d) **efeitos do pagamento com desconto sobre o direito de recorrer** — o art. 126 apresenta as duas condutas como alternativas, e ir além disso exigiria entendimento não verificado; a página diz o que o artigo diz e registra que a escolha é jurídica, informada pela pergunta técnica de se a base fática do auto sobrevive ao exame.
- **Manutenção:** média. O Decreto nº 6.514/2008 foi alterado três vezes em quatro anos (Decretos 9.760/2019, 11.080/2022 e 11.373/2023) — é norma **em movimento**, ao contrário do CPC da SEO-042. Reconferir as redações dos arts. 97-A, 99, 100, 113, 119 e 120 a cada revisão. A CONAMA 430/2011 tem consulta pública de revisão dos padrões de lançamento em andamento, já registrada em `/pericia-ambiental/` — se resultar em norma nova, **as duas páginas** precisam ser atualizadas juntas.

### Verificação de renderização

Chrome real via Playwright (`channel="chrome"`, `/usr/bin/python3`) contra `http://localhost:8899`, a 375 px e 1280 px, com `/pericia-ambiental/` — a página modificada — e a home como controles.

- **Sem overflow horizontal nas três páginas, nas duas larguras** (`scrollWidth == clientWidth`, com `innerWidth` confirmando a leitura).
- **Controle negativo:** injetado um bloco de 3000 px de largura, a medição passou a acusar `scrollWidth=3000` contra `clientWidth=375`. A medição sabe reprovar.
- A página não tem âncoras internas, então o teste de `scroll-margin-top` das execuções anteriores não se aplica aqui.

### Controle negativo da paridade de FAQ

Sétima aplicação da regra 10 ao script estrito: injetou-se um defeito em **uma única pergunta visível** (remoção do acento em "ônus"), deixando o JSON-LD intacto. O script **reprovou, apontando o item 5**; o `seo-report` seguiu em **`ALL PASS`** durante o defeito. Página restaurada e paridade reconferida depois do restauro. Terceira confirmação de que `ALL PASS` não é prova de paridade.

### Próxima execução — o que checar primeiro

1. **Rodar `tools/seo-report.py` em `deploy`, `valid` e `gsc` antes de decidir qualquer coisa** — `gsc` exige `/usr/bin/python3`. **Rodar com `python3 -u`**: com a saída redirecionada para arquivo, o Python bufferiza e a seção `[gsc]` parece travada por mais de dez minutos quando na verdade está progredindo. Custou duas execuções abortadas hoje. Falha isolada de `timeout` no `[deploy]` ou na inspeção de URL é rede — reconferir com `curl` antes de virar item.
2. **Repetir o teste do gatilho do item 5 de 31/08 em dia distinto**, no formato de 02/09 (manhã): impressões e cliques lado a lado contra a leitura anterior. Se os cliques crescerem **menos** que as impressões, a Prioridade 8 (citação e menção) passa à frente do conteúdo. **Não repetir com poucas horas de intervalo** — foi por isso que não se repetiu nesta execução.
3. **`/dano-motor-combustivel/`: se ainda não estiver indexada por volta de 10/09, aí sim é item, não espera.** `/producao-antecipada-prova/` e `/auto-infracao-ambiental/`: primeira checagem de indexação a partir de ~09/09.
4. **`/auto-infracao-ambiental/`: primeira leitura a partir de ~09/09.** Consultas a vigiar: `auto de infração ambiental`, `defesa auto de infração ambiental`, `prazo defesa auto de infração ambiental`, `multa ambiental CETESB defesa`, `lançamento de efluente fora do padrão`, `CONAMA 430 padrões de lançamento`, `automonitoramento de efluentes`, `art 61 decreto 6514`. **Conferir canibalização com `/pericia-ambiental/`**, de onde a fronteira foi traçada (conformidade e prova judicial no pilar; autuação e defesa administrativa na nova), e observar se o parágrafo novo do pilar muda a sua posição média (hoje 7,5) ou o seu volume (hoje 2 impressões — o número a bater).
5. **O cluster Ambiental agora tem duas páginas.** Antes de acrescentar a terceira, verificar se a segunda entra abaixo de 10 — mesma disciplina aplicada a Alimentos, Combustíveis e Processual.
6. **A lacuna interna aberta hoje:** `/normas-tecnicas-pericia/`, que é o quadro de vigência do site, **não cita a Lei nº 9.605/1998 nem o Decreto nº 6.514/2008**, que passaram a existir no site por esta página. É candidata a linha nova naquela tabela, não a página nova — mesma forma do item 6 de 31/08, que virou seção em `/cpc-prova-pericial/`.
7. **Candidata de Prioridade 3 registrada, ainda não medida:** o padrão "termo-cabeça mal posicionado, cauda longa bem posicionada" descrito acima é o sintoma que o cluster processual apresenta há três leituras. Se persistir na próxima, a resposta não é mais conteúdo no mesmo cluster — é Prioridade 8. Vigiar `impugnação de laudo pericial` (hoje 26,8–47,0) como o indicador dessa virada.
8. **Ao ler o Planalto, extrair TODAS as ocorrências do artigo e escolher a última deliberadamente.** O texto compilado exibe redações revogadas em sequência com a vigente. Hoje isso valeu para sete artigos e um parágrafo revogado que circula como vigente. Regra nova, e a mais importante desta execução.
9. **`ALL PASS` do `seo-report` não prova paridade de FAQ.** Rodar sempre o script estrito, e passar o controle negativo nele.
10. **Presumir revogação e provar vigência** — segue valendo, e hoje pegou o art. 119, § 1º.
11. **Gerar FAQ visível e JSON-LD da mesma fonte de dados.** Sétima execução; segue eliminando a classe de erro.
12. **`AI Assistant` apareceu como canal no GA4 pela primeira vez** (2 sessões em `/quesitos-periciais/`). Marcar e acompanhar: se crescer, é a primeira medida direta do retorno do trabalho de citação por LLM, que hoje só é otimizado às cegas.
13. **Escalar o Google Ads sem entrega.** Décima quinta execução como nota de rodapé. Não é item de SEO — cabe uma mensagem direta à cliente.

---

## Estado da medição — 2026-09-03

Período 28 dias, service account. Leitura comparada com a de 27/08.

- **821 impressões · 9 cliques · CTR 1,10%** (em 27/08: 484 · 5). **18 de 21 páginas indexadas.**
- **Quinzena contra quinzena** (04–17/08 → 18–31/08): **186 → 599 impressões** e **1 → 8 cliques**. As impressões triplicaram; os cliques octuplicaram.
- **GA4:** 52 sessões, 11 de Organic Search, **2 de AI Assistant** (canal que apareceu pela primeira vez em 02/09, em `/quesitos-periciais/`, e se manteve).

### Dois gatilhos pré-registrados foram testados. Um fechou, o outro não disparou.

1. **O gatilho móvel do item 8 de 27/08 fechou — e a hipótese SEO-035/SEO-036 não se confirma.** Em 27/08 o mobile tinha 127 impressões e **0 cliques**, e ficou registrado que a amostra não distinguia as hipóteses (probabilidade ~0,36 de observar zero). Agora: **MOBILE 199 impressões · 2 cliques · CTR 1,01% · pos 8,9**, contra **DESKTOP 561 · 7 · CTR 1,25% · pos 10,5**. As CTRs são estatisticamente indistinguíveis. **Não há defeito de layout móvel a corrigir.** O item está encerrado por dado, não por opinião.
2. **O gatilho do item 5 de 31/08 (repetido conforme o item 2 do handoff) NÃO disparou.** A regra era: se os cliques crescerem menos que as impressões, a Prioridade 8 (citação e menção) passa à frente do conteúdo. Impressões ×3,2; cliques ×8. **A estratégia de conteúdo continua justificada.**

### O que a CTR agregada diz — e corrige uma suspeita anterior

CTR de 1,10% na posição média 10,5 está **dentro do esperado** para essa posição, não abaixo. Ou seja: **o problema do site não é CTR, é posição.** Isso remove a Prioridade 1 (conversão em páginas de impressão alta) da mesa por ausência de alavanca — pela segunda leitura consecutiva, mas agora por um motivo diferente e mais forte do que em 27/08. Confirma também o encerramento do SEO-016: não há metadado a reescrever com ganho esperável.

### O achado que decidiu a execução: as consultas nomeadas são texto de andamento processual

Só **66 das 821 impressões (8%)** vêm de consultas nomeadas — o resto é cauda anonimizada. Como o GSC oculta as consultas *raras*, as nomeadas são as **mais frequentes**. E elas têm uma forma comum:

| Consulta nomeada | Posição |
|---|---|
| **emitir despacho - sem quesitos** (a consulta nº 1 do site, 9 impressões) | **9,0** |
| **anexo juntado: apresentação de esclarecimentos ao laudo pericial** | **8,2** |
| prazo para se manifestar sobre laudo pericial | 11,0 |
| prazo apresentacao quesitos | 12,0 |
| quesitos podem ser apresentados até a perícia | 29,0 |
| art. 95, § 3º, ii, do cpc | 9,0 |
| impugnação ao laudo pericial **cpc** | 9,0 |
| — contra os termos-cabeça — | |
| quesitos · apresentação de quesitos · quesitos periciais | 36,8 · 48,3 · 42,5 |
| laudo pericial · impugnação de laudo pericial | 34,3 · 44,0 |

**As consultas em que o site fica entre 8 e 12 são, em sua maioria, strings copiadas da tela do processo** — nomes de movimento e de expediente, não conceitos. As conceituais ficam entre 22 e 53, e **não se moveram desde a leitura de 27/08**, o que é o indicador do item 7 do handoff: mais conteúdo no mesmo cluster jurídico não resolve o termo-cabeça.

Terceira confirmação do achado estrutural de 27/08 — *o retorno está em ser mais específico, em terreno onde a autoridade da concorrência não é jurídica*. E uma direção nova: o terreno mais específico disponível não é uma matéria técnica, é **o vocabulário da própria tramitação**.

### O levantamento que confirmou a lacuna

Contagem por termo nas 21 páginas (~100.000 palavras):

| Termo | Ocorrências no site |
|---|---|
| intimação / 15 dias / esclarecimentos | 50 / 68 / 37 — a **lei** está bem coberta |
| **PJe · e-SAJ · certidão · conclusos · vista dos autos** | **0 · 0 · 0 · 0 · 0** |
| movimento | 1 |

O site **ensina o regime e é invisível ao vocabulário pelo qual ele é procurado**. Mesma forma do caso da SEO-018 (quesitos), em que o pilar afirmava a importância sem ensinar a coisa — aqui o pilar ensina a lei sem nomear a tela.

### Por que seção, e não página nova — contrariando o instinto

O mandato manda não criar conteúdo enquanto houver ganho de ranking fácil disponível. Três fatos empurraram para dentro de uma página existente:

1. **Três das 21 páginas não estão indexadas** (`/dano-motor-combustivel/` e `/producao-antecipada-prova/` como *detectadas, não indexadas*; `/auto-infracao-ambiental/` o Google ainda não reconhece). A cadência de publicação está à frente da demanda de rastreamento do domínio. **O valor marginal da página 22 é menor que o de fazer as 21 ranquearem.**
2. `/cpc-prova-pericial/` já está indexada, já está em **pos 8,2**, e é organizada explicitamente *na ordem em que o processo aciona cada ato* — que é exatamente a espinha de um decodificador de andamento. Ao contrário do art. 381 na SEO-042, isto **não quebra a espinha: percorre-a**.
3. Página nova produziria canibalização direta com `/cpc-prova-pericial/` e `/quesitos-periciais/`, as duas páginas de maior volume do site.

### SEO-044 — Decodificador de andamento processual em `/cpc-prova-pericial/` *(executada em 2026-09-03)*
- **Descrição:** Traduzir os nomes oficiais dos movimentos processuais para o prazo do CPC que cada um dispara, e converter a intimação eletrônica em data de vencimento com dia certo.
- **URL:** `/cpc-prova-pericial/#andamento`
- **Categoria:** Prioridade 2 (posições 5–20) / Cobertura semântica / Conversão
- **Impacto:** 8 · **Esforço:** 4 · **Confiança:** 8 · **Valor de negócio:** 9
- **Priority Score:** 144
- **Status:** done · **Descoberto:** 2026-09-03 · **Concluído:** 2026-09-03
- **Implementado:** ~1.900 palavras dentro da página existente. Tabela de **11 movimentos** (nome e código oficiais do CNJ → o que aconteceu → o que passa a correr → base legal); tabela de **7 passos** da intimação eletrônica até a data de vencimento; três enganos que a conversão produz; e um parágrafo de encaminhamento que liga cada janela ao produto técnico correspondente. **4 novas entradas de FAQ** (de 8 para 12), visíveis e em JSON-LD.
- **A fonte que dá vantagem competitiva:** os nomes de movimento não foram escritos de memória. Foram extraídos do **webservice público do Sistema de Gestão de Tabelas do CNJ** (`sgt_ws.php`, operação `pesquisarItemPublicoWS`, tabela `M`), que devolveu **964 movimentos** com código, hierarquia pai/filho e glossário oficial. Daí saíram: Conclusão (51), Despacho (11009) › Mero expediente (11010), Perícia (14901) › Determinada/Designada · Agendada · Reagendada · Realizada, Intimação (12263) › Eletrônica, Juntada (67) › Petição · Documento, Decurso de Prazo (1051) e Expedição de documento (60). As descrições de *Conclusão*, *Decurso de Prazo* e *Expedição de documento* reproduzem o glossário oficial. **Não há, até onde se verificou, conteúdo em português que ligue a tabela de movimentos do CNJ aos prazos periciais do CPC.**
- **A tese central, que é onde o prazo se perde:** *o marco não é a data do despacho nem a da juntada — é a da intimação, e no processo eletrônico ela pode ser ficta.* A cadeia completa, em sete passos com base legal em cada um: disponibilização no portal (Lei nº 11.419/2006, art. 5º); intimação realizada no dia da consulta, ou no primeiro dia útil seguinte se a consulta se der em dia não útil (§§ 1º e 2º); **intimação automaticamente realizada no término de 10 dias corridos do envio, se não houver consulta (§ 3º)**; início da contagem no dia útil seguinte (CPC, art. 231, V); contagem excluindo o dia do começo e incluindo o do vencimento (art. 224) e **somente em dias úteis** (art. 219); protração do art. 224, § 1º; e suspensão de 20/12 a 20/01 (art. 220). Pelo DJe, valem o art. 224, §§ 2º e 3º.
- **O engano mais caro, que é aritmético:** a janela de consulta é de **10 dias corridos**; o prazo que ela dispara corre **em dias úteis**. São duas contagens encadeadas com unidades diferentes.
- **O engano contraintuitivo:** **o prazo em dobro do art. 229 não se aplica em autos eletrônicos** — o § 2º do próprio artigo o afasta. Quem soma a dobra sobre os 15 dias do art. 465, § 1º, num processo eletrônico trabalha com prazo inexistente.
- **O engano com maior valor comercial:** ler *Decurso de Prazo* como fim da participação técnica. Perdidos os quesitos iniciais, permanecem os quesitos suplementares do art. 469 e, sobretudo, **os 15 dias comuns do art. 477, § 1º** para a manifestação e o parecer do assistente técnico. É a janela em que a crítica ao laudo é feita, e ela existe para quem perdeu a primeira — que é exatamente o visitante que chega por uma consulta de andamento.
- **Verificação factual — fonte primária aberta durante a redação**, método das três execuções anteriores. CPC/2015 e Lei nº 11.419/2006 baixados do Planalto; tabela de movimentos obtida do SGT/CNJ. Todos os artigos citados (203, 219, 220, 224, 229, 231, 465, 466, 469, 470, 474, 476, 477, 480) foram extraídos com **todas as ocorrências listadas e a última escolhida deliberadamente** (regra 8 do handoff de 02/09). Conferidos um a um: 15 dias do art. 465, § 1º; 5 dias do art. 465, §§ 2º e 3º; 5 dias de antecedência do art. 466, § 2º; 20 dias do art. 477, caput; 15 dias comuns do art. 477, § 1º; 10 dias do art. 477, § 4º; e os 10 dias **corridos** do art. 5º, § 3º, da Lei nº 11.419/2006.
- **Um achado colateral que reforça a tabela:** o art. 203, § 4º dispõe que *os atos meramente ordinatórios, como a juntada e a vista obrigatória, independem de despacho* — o que explica por que *Juntada* aparece no andamento sem despacho que a preceda, e por que o rótulo sozinho não permite inferir se há prazo correndo.
- **Nenhuma jurisprudência foi afirmada.** As três teses saem do texto legal. Em particular, a terceira (decurso de uma janela não fecha as outras) é sustentada pela existência autônoma dos arts. 469 e 477, § 1º, e **não** por entendimento sobre a admissibilidade de indicação tardia de assistente técnico, que não foi verificado e por isso não é mencionado.
- **Honestidade metodológica registrada na própria página:** uma caixa avisa que cada tribunal pode criar tabela complementar de documentos e que o texto de tela costuma trazer complemento livre digitado pela secretaria — *o rótulo orienta; o inteiro teor decide*. Isso impede que a tabela seja lida como promessa de correspondência exata.
- **Links internos:** três **contextuais novos** apontando para `#andamento`, colocados exatamente nas páginas que carregam as consultas de andamento e no ponto do texto em que a dúvida nasce — `/impugnacao-laudo-pericial/` (na lista de erros, como um quarto erro: contar da data errada), `/laudo-pericial/` (logo após a frase dos 15 dias do art. 477, § 1º) e `/quesitos-periciais/` (no bloco de "o que enviar", citando o movimento *Perícia — Determinada/Designada* pelo nome). Âncoras diferenciadas por vizinhança, critério da SEO-019. A seção nova, por sua vez, liga às quatro páginas de produto técnico. `sitemap.xml` (4 `lastmod`) e `llms.txt` atualizados.
- **Manutenção:** baixa para o CPC, que é estável. **Média para a tabela do CNJ**, que é versionada e ganha movimentos novos — reconferir pelo SGT antes de citar código novo. A Lei nº 11.419/2006 é estável, mas o art. 5º é candidato perene a alteração por marco de processo eletrônico.

### Verificação

- **Paridade de FAQ garantida por construção** (oitava execução do método da SEO-037): as 12 perguntas definidas uma única vez em `tools/build/andamento.py`; HTML visível e JSON-LD gerados da mesma estrutura por `andamento_build.py`. Script estrito: **12/12 idênticos caractere a caractere**.
- **Controle negativo da paridade** (regra 9): removido o acento de uma única pergunta *visível*, com o JSON-LD intacto. O script estrito **reprovou, apontando o item 10**; o `seo-report` seguiu em **`ALL PASS`** durante o defeito. **Quarta confirmação de que `ALL PASS` não prova paridade.** Página restaurada e paridade reconferida.
- **Renderização** em Chrome real via Playwright, a 375 px e 1280 px, em `/cpc-prova-pericial/`, `/laudo-pericial/` e a home: **sem overflow horizontal** (`scrollWidth == clientWidth`). Controle negativo com bloco de 3000 px: a medição **acusou** `scrollWidth=3000`.
- **Armadilha de medição descoberta hoje, e que custou uma investigação:** medida logo após a navegação, a âncora `#andamento` parecia parar 95 px **abaixo** do `scroll-margin-top` de 112 px, enquanto `#prazos` e `#faq` acertavam. **Não era defeito.** O CSS do site usa `scroll-behavior: smooth`, e a rolagem suave **ainda estava em curso** — quanto mais fundo o alvo, mais tempo ela leva, e `#andamento` está a 3.016 px. Desligado o `scroll-behavior`, as três âncoras repousam **exatamente em 112 px, nas duas larguras**. Regra nova: **medir posição de âncora sempre com `scroll-behavior: auto` forçado**, ou a medição reprova página boa.

### Próxima execução — o que checar primeiro

1. **Rodar `tools/seo-report.py` em `deploy`, `valid` e `gsc` antes de decidir**, com `/usr/bin/python3 -u`. Falha isolada de `timeout` é rede — reconferir com `curl`.
2. **A leitura que decide o próximo passo é a de `#andamento`.** A partir de ~10/09, vigiar em `query × page` para `/cpc-prova-pericial/`: `emitir despacho sem quesitos`, `anexo juntado apresentação de esclarecimentos ao laudo pericial`, `prazo para se manifestar sobre laudo pericial`, `o que significa conclusão no processo`, `intimação eletrônica quando começa o prazo`, `prazo em dobro processo eletrônico`, `decurso de prazo o que significa`. **A página está hoje em pos 8,2 com 41 impressões — são esses os números a bater.** Se as consultas de andamento subirem para o top 5, a tese está validada e o próximo passo é replicar a forma (decodificar o vocabulário de tela) nos clusters administrativos — autuação fiscal, ambiental e sanitária têm o mesmo problema: o cidadão lê o rótulo do órgão, não o nome da norma.
3. **Se as consultas de andamento NÃO subirem até ~24/09**, a hipótese cai, e aí sim a Prioridade 8 assume: o site terá esgotado o que dá para fazer on-page com o conteúdo que tem.
4. **Indexação:** `/dano-motor-combustivel/` (publicada em 31/08) segue *detectada, não indexada* — o prazo do item 3 de 02/09 é **10/09**; se persistir, vira item. `/producao-antecipada-prova/` e `/auto-infracao-ambiental/` são de 02/09: primeira checagem legítima a partir de **09/09**. **Três páginas não indexadas ao mesmo tempo é o sinal para reduzir a cadência de publicação**, não para publicar mais.
5. **A cadência de publicação está à frente da demanda de rastreamento.** 21 páginas em ~33 dias contra 9 cliques em 28 dias. Enquanto houver página não indexada, preferir melhorar página existente a criar página nova — foi o que esta execução fez, e a regra deve valer para a próxima.
6. **Lacuna interna ainda aberta** (item 6 de 02/09, não resolvida hoje): `/normas-tecnicas-pericia/`, que é o quadro de vigência do site, **não cita a Lei nº 9.605/1998 nem o Decreto nº 6.514/2008**. É linha nova naquela tabela, não página nova.
7. **`AI Assistant` no GA4 manteve-se em 2 sessões**, ambas em `/quesitos-periciais/`. Ainda é a única medida direta do retorno do trabalho de citação por LLM. Continuar acompanhando.
8. **Medir posição de âncora com `scroll-behavior: auto` forçado.** Regra nova desta execução.
9. **`ALL PASS` do `seo-report` não prova paridade de FAQ.** Rodar sempre o script estrito com o controle negativo. Quarta confirmação.
10. **Ao ler o Planalto, extrair TODAS as ocorrências do artigo e escolher a última.** Segue valendo.
11. **Gerar FAQ visível e JSON-LD da mesma fonte.** Oitava execução; segue eliminando a classe de erro.
12. **Escalar o Google Ads sem entrega.** Décima sexta execução como nota de rodapé — cabe mensagem direta à cliente, não é item de SEO.

---

## Execução de 2026-09-04 — a leitura acontece, o contato não

### O que os dados disseram, e por que mudaram a prioridade

Primeira execução em que **o GA4, não o Search Console, decidiu a tarefa**.

O quadro do Search Console (28 dias) é o mesmo das últimas execuções — 937 impressões, 11 cliques, páginas em posição 6–13. Mas o GA4 em 56 dias mostrou algo que nenhuma leitura anterior tinha isolado:

| Sinal | Valor em 56 dias |
|---|---|
| Sessões | 78 · 239 page views |
| `scroll` | 22 |
| `click` | 2 |
| `form_start` | **1** |
| `manual_event_CONTACT` | **1** |

E a duração média por página de destino: `/quesitos-periciais/` 156 s · `/pericia-contaminacao-alimentos/` 232 s · `/assistente-tecnica/` 329 s · `/laudo-pericial/` 453 s · `/pericia-industria-quimica/` 524 s · `/quesitos-periciais/?v=1` 621 s.

**As pessoas leem — de dois a dez minutos, com bounce zero nas páginas de conteúdo — e não escrevem.** Isso não é problema de tráfego nem de posição: é a Prioridade 1 do mandato, *conversão em página que já recebe visita*, e é o único degrau com falha medida em vez de hipótese.

### Por que não foi título/meta, nem conteúdo novo

- **Título e meta já estão bons.** As 20 páginas têm título de intenção e descrição dentro do limite de SERP (regra da SEO-016). Reescrevê-los sem dado de CTR por consulta seria mexer no que funciona — o mandato veda mudança sem justificativa.
- **Não cabia página nova.** Duas páginas seguem *detectadas, não indexadas* (`/dano-motor-combustivel/`, `/auto-infracao-ambiental/`). A regra do item 5 do handoff de 03/09 continua valendo: enquanto houver página não indexada, melhorar existente.
- **Não cabia atacar o termo-cabeça.** As consultas conceituais de `/quesitos-periciais/` seguem em posição 28–56 (`quesitos` 36,5 · `apresentação de quesitos` 48 · `elaboração de quesitos` 56). Quarta confirmação de que o termo genérico não se move com mais conteúdo do mesmo cluster.
- **Não cabia julgar a SEO-044.** O `#andamento` foi publicado em 03/09; a leitura legítima é a partir de ~10/09. `emitir despacho - sem quesitos` segue a maior consulta nominal do site (10 impressões, pos 9,1).

### SEO-045 — Bloco "O que enviar na primeira mensagem" nas 20 páginas de conteúdo *(executada em 2026-09-04)*
- **Descrição:** Remover as três dúvidas que travam a primeira mensagem de um advogado que acabou de ler 4.000 palavras com prazo correndo — *o que eu mando, de que data conta o prazo, e o que volta*.
- **URL:** as 20 páginas de conteúdo, dentro do `cta-sec` existente
- **Categoria:** Prioridade 1 (conversão em página com visita) / UX / AI citation
- **Impacto:** 9 · **Esforço:** 3 · **Confiança:** 7 · **Valor de negócio:** 10
- **Priority Score:** 210
- **Status:** done · **Descoberto:** 2026-09-04 · **Concluído:** 2026-09-04
- **Implementado:** uma caixa `.box` no `cta-sec`, **antes** dos botões, com quatro partes:
  1. **A lista do que enviar, específica de cada página** — não genérica. `/laudo-pericial/` pede laudo integral com memoriais e o registro fotográfico; `/pericia-industria-quimica/` pede batch record, P&ID, HAZOP e ordens de manutenção; `/classificacao-fiscal-ncm/` pede o parecer do fisco que fundamenta a reclassificação e a ficha técnica quantitativa; `/produtos-quimicos-controlados/` pede os mapas e livros de controle do período autuado. São 20 listas distintas, cada uma com o documento que efetivamente permite a leitura preliminar daquela matéria.
  2. **A data que conta**, com a correção que é o erro mais caro do processo eletrônico: *a data da intimação, não a do despacho nem a da juntada*.
  3. **Um link contextual novo para `/cpc-prova-pericial/#andamento`** em cada página — 19 links de entrada para a seção publicada ontem, colocados no momento exato em que o leitor precisa converter a intimação em data. Na própria `/cpc-prova-pericial/` o link é âncora local.
  4. **O que o primeiro retorno estabelece** — se há tese técnica sustentável, qual via ela comporta, o que precisaria ser produzido — e, explicitamente, **que isso não substitui o parecer**.
- **O que deliberadamente NÃO foi prometido:** nenhum prazo de resposta ("retorno em 24 h") e nenhuma gratuidade ("análise sem custo"). As duas coisas aumentariam a conversão e **nenhuma foi autorizada pela cliente** — um SLA publicado no site vira compromisso que ela passa a ter de cumprir. O texto se limita a descrever o que a análise preliminar estabelece, que é o que a home já oferece ("análise preliminar de casos"). **Se a cliente quiser autorizar prazo de retorno ou triagem sem custo, esse é o próximo salto de conversão disponível, e é dela a decisão.**
- **Fonte única, nono uso do método da SEO-037:** as 20 listas e os três textos fixos vivem em `tools/build/intake.py`; `intake_build.py` gera e reescreve o bloco entre marcadores `<!-- intake:start/end -->`. É idempotente — rodar de novo restaura qualquer página que tenha derivado. Nenhuma lista foi copiada à mão para 20 arquivos.
- **CSS:** uma linha (`.cta-sec .box { background: var(--bg) }`), porque o `cta-sec` já é branco e a caixa também era — sem isso a caixa desapareceria no fundo. Nenhuma classe nova.

### Verificação

- **Verificador estrito** (`/tmp/verify_intake.py`): para as 20 páginas, confirma que o bloco existe, está **dentro** do `cta-sec`, vem **antes** dos botões, que os itens `<li>` são idênticos caractere a caractere aos de `intake.py`, que os textos fixos estão presentes, que o `href` do andamento é o certo para cada caso e que o destino `id="andamento"` existe. **20/20 OK.**
- **Controle negativo** (regra 9): tirado o acento de "juízo" num único `<li>` de `/laudo-pericial/`. O verificador **reprovou apontando a página e o item**; o `seo-report valid` seguiu em **`ALL PASS`** durante o defeito. **Quinta confirmação de que `ALL PASS` não prova paridade de conteúdo.** Página restaurada e reconferida.
- **Renderização** em Chromium real, 5 páginas × 375 px e 1280 px, com `scroll-behavior: auto` forçado (regra nova de 03/09): sem overflow horizontal, caixa dentro da viewport nas duas larguras, itens renderizados. **Controle negativo** com bloco de 3000 px dentro da própria caixa: a medição **acusou** `scrollWidth=3062` contra `clientWidth=375`.
- `sitemap.xml`: 20 `lastmod` para 2026-09-04, XML bem formado. A home não mudou e não foi tocada.
- `llms.txt` não mudou — nenhuma URL nova; o bloco é seção interna de páginas já listadas.

### Próxima execução — o que checar primeiro

1. **A leitura que decide tudo agora é `form_start` e `manual_event_CONTACT` no GA4.** A linha de base é **1 e 1 em 56 dias**, com 78 sessões. Se subirem sem que o tráfego suba, a tese da SEO-045 está validada e o próximo passo é levar o mesmo bloco para a home. Se **não** subirem até ~25/09 com volume de sessão comparável, o gargalo não é a fricção do primeiro contato — é a qualificação do visitante, e aí a Prioridade 8 (autoridade) assume de vez.
2. **`#andamento` (SEO-044) fica legível a partir de ~10/09.** Consultas a vigiar em `query × page` para `/cpc-prova-pericial/`: `emitir despacho sem quesitos` (hoje pos 9,1), `anexo juntado apresentação de esclarecimentos ao laudo pericial` (8,2), `prazo para se manifestar sobre laudo pericial` (11,0), `decurso de prazo o que significa`. A página está em **pos 8,4 com 47 impressões** — são esses os números a bater. A SEO-045 acabou de dar a ela 19 links internos novos, o que é uma variável a mais na leitura: **uma subida agora pode ser do conteúdo ou do link, e as duas coisas entraram com um dia de diferença.**
3. **Indexação:** `/dano-motor-combustivel/` (31/08) e `/auto-infracao-ambiental/` (02/09) seguem *detectadas, não indexadas*. `/producao-antecipada-prova/` passou a indexada. Se as duas restantes persistirem depois de ~15/09, vira item próprio.
4. **Decisão pendente com a cliente, de alto valor:** autorizar (ou não) prazo de retorno declarado e/ou triagem preliminar sem custo no bloco de intake. É o maior ganho de conversão restante e não é decisão de SEO.
5. **Lacuna interna ainda aberta** (arrastada de 02/09 e 03/09): `/normas-tecnicas-pericia/` não cita a **Lei nº 9.605/1998** nem o **Decreto nº 6.514/2008**. Linha nova na tabela de vigência, não página nova. Terceira execução em que fica para depois — se não sair na próxima, virar item formal com prioridade própria.
6. **`AI Assistant` no GA4 subiu de 2 para 3 sessões**, todas em `/quesitos-periciais/`. Segue a única medida direta do retorno do trabalho de citação por LLM.
7. **Oportunidade de citação por LLM não executada hoje:** "o que enviar ao assistente técnico no primeiro contato" é pergunta de FAQ com resposta agora escrita e específica por matéria. Não virou entrada de `FAQPage` porque a paridade de FAQ é construída por página, em scripts separados, e mexer nos 20 JSON-LD de uma vez era risco desproporcional numa execução só. **É o item de menor esforço e maior citabilidade disponível para a próxima.**
8. **Regras que seguem valendo:** `ALL PASS` não prova paridade (5ª confirmação) · medir âncora com `scroll-behavior: auto` · extrair todas as ocorrências do artigo no Planalto e escolher a última · gerar visível e JSON-LD da mesma fonte.
9. **Google Ads segue sem entrega.** Décima sétima execução como nota de rodapé — é mensagem direta à cliente, não item de SEO.
