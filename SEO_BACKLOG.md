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
  1. **IN DG/PF nº 338, de 29/07/2026 — confirmada.** Reeditou os procedimentos de controle e fiscalização de produtos químicos e **revogou as INs nº 166/2020 e nº 211/2021**. Detalha o regime sancionador (multas até R$ 350 mil, suspensão e cancelamento de licença). **Não alterou a relação de produtos controlados**, que segue na Portaria MJSP nº 204/2022 — como a página afirma. Fonte: gov.br/pf e cobertura especializada.
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
- **Status:** open · **Descoberto:** 2026-08-05
- **Por que não é a tarefa de hoje:** otimizar CTR **antes de haver impressões** é otimizar no vazio. Este item ganha prioridade assim que o GSC voltar e mostrar páginas com impressão e clique baixo — que é literalmente a Prioridade 1 do playbook. Fica na fila esperando o dado que o justifica.

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
- **Status:** open · **Descoberto:** 2026-08-06
- **Por que não é a tarefa de hoje:** score baixo e o problema ainda é teórico em 10 páginas — o grafo completo até ajuda a distribuir rastreamento num domínio novo. Vira relevante por volta de 15 páginas, ou antes disso se o GSC mostrar páginas recebendo tráfego irrelevante entre clusters.

### Próxima execução — o que checar primeiro
1. **Indexação das três pendentes** (`/pericia-industria-quimica/`, `/impugnacao-laudo-pericial/`, `/honorarios-pericia-judicial/`). Se `/pericia-industria-quimica/` continuar fora depois de ~09/08, aí sim investigar — passaria da latência medida de 2–4 dias.
2. **Se aparecer qualquer página com impressão de dois dígitos e CTR baixo, o SEO-016 assume a Prioridade 1** e deixa de esperar.
3. Se o quadro de dados continuar vazio, a próxima tarefa por intenção é **aprofundar um segundo cluster** — o de alimentos é o candidato natural (recall e recolhimento pela RDC 655/2022, ou prazo de validade e vida de prateleira), já que hoje só o cluster processual tem spokes.
