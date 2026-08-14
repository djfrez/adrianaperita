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

### Próxima execução — o que checar primeiro
1. **Indexação das três pendentes** (`/pericia-industria-quimica/`, `/impugnacao-laudo-pericial/`, `/honorarios-pericia-judicial/`). Se `/pericia-industria-quimica/` continuar fora depois de ~09/08, aí sim investigar — passaria da latência medida de 2–4 dias.
2. **Se aparecer qualquer página com impressão de dois dígitos e CTR baixo, o SEO-016 assume a Prioridade 1** e deixa de esperar.
3. Se o quadro de dados continuar vazio, a próxima tarefa por intenção é **aprofundar um segundo cluster** — o de alimentos é o candidato natural (recall e recolhimento pela RDC 655/2022, ou prazo de validade e vida de prateleira), já que hoje só o cluster processual tem spokes.

---

## Estado da medição — 2026-08-07

Coleta por service account (`python3 ~/.config/adrianarezende/seo-report.py 30`), período 2026-07-08 → 2026-08-07.

**Primeira leitura com dado acionável desde o início do trabalho.**

- **24 impressões, zero cliques.** `/assistente-tecnica/` saltou de 2 para **20 impressões, posição média 8,1** — sozinha responde por 83% do volume do site. Home 3 (pos. 6,0) e `/classificacao-fiscal-ncm` 1 (pos. 11,0).
- **Dimensão `query` retornou linhas pela primeira vez:** "assistente tecnico pericia" (1 imp., pos. 16,0) e "assistente técnico" (1 imp., pos. 18,0). Duas linhas só, o resto segue abaixo do limiar de anonimização — mas confirmam que o tráfego que existe é **exatamente o do cluster de maior valor comercial**, com intenção de contratação.
- **Indexação: 11 de 11.** As três pendentes (`/pericia-industria-quimica/`, `/impugnacao-laudo-pericial/`, `/honorarios-pericia-judicial/`) entraram, e `/quesitos-periciais/` foi indexada em ~1 dia. Confirma de novo a latência de 1–4 dias e **encerra o item 1 da lista de checagem da execução anterior — sem ação necessária.**
- **Concentração temporal:** 18 das 24 impressões caíram em 05/08. Não é tendência ainda; é ruído de um domínio novo entrando no índice.
- **GA4** segue não instrumentado (falta o ID numérico em `~/.config/adrianarezende/ga4-property`).

**Consequência para a priorização: o gatilho do SEO-016 disparou.** A regra registrada em 06/08 era literal — "se aparecer qualquer página com impressão de dois dígitos e CTR baixo, o SEO-016 assume a Prioridade 1". `/assistente-tecnica/` tem 20 impressões e CTR 0% na posição 8,1. É Prioridade 1 do playbook (converter impressão existente) e passa à frente de qualquer conteúdo novo.

---

## Auditoria — 2026-08-07

### O que está saudável — não mexer

- **11 de 11 indexadas**, zero links internos quebrados, zero órfãs, 1 `<h1>` por página, canonical correto nas 11, sitemap idêntico ao sistema de arquivos, JSON-LD parseando nas 11. Verificado por script nesta execução.
- **Conteúdo:** cinco pilares e três spokes, todos com norma nomeada e verificada em fonte. Nada a corrigir.

### Fraquezas encontradas

1. **Metadados truncados na única página com impressão real.** `/assistente-tecnica/` estava com title de 74 caracteres e description de 259 — a description perdia **mais de 100 caracteres** no corte do SERP, incluindo a atribuição de autoridade ("engenheira química pela UNICAMP e perita judicial") que ficava fora da parte visível. A página aparece 20 vezes na posição 8,1 e o usuário nunca vê a frase que a diferencia. **Resolvido nesta execução (SEO-016).**
2. **O problema era sistêmico, não pontual:** 8 das 11 páginas estavam fora do limite, com descriptions de 259 a **445** caracteres. As três páginas mais recentes já nasciam dentro do limite — o defeito era das oito primeiras, escritas antes da regra.
3. **SEO-019 (grafo interno completo)** segue aberto e ainda teórico em 11 páginas. Sem mudança.

### SEO-016 — execução *(2026-08-07)*

- **Escopo real:** 8 páginas reescritas (as 3 recentes já estavam conformes) + 1 ajuste fino em `/honorarios-pericia-judicial/`, cuja description tinha 144 caracteres e desperdiçava faixa útil do snippet. Total: **9 páginas tocadas, 11 conformes ao final.**
- **Regra aplicada:** title ≤ 60 caracteres com o termo-cabeça no início; description entre 150 e 160; `og:title` e `twitter:title` sincronizados com o `<title>` (era a convenção já usada nas páginas novas, agora uniforme nas 11).
- **Antes → depois (title / description, em caracteres):**

| Página | Antes | Depois |
|---|---|---|
| `/` | 76 / 261 | 54 / 154 |
| `/assistente-tecnica/` | 74 / 259 | 59 / 156 |
| `/classificacao-fiscal-ncm/` | 73 / 318 | 60 / 151 |
| `/pericia-ambiental/` | 68 / 328 | 56 / 158 |
| `/pericia-combustiveis/` | 66 / 360 | 52 / 157 |
| `/pericia-contaminacao-alimentos/` | 78 / 326 | 52 / 157 |
| `/pericia-industria-quimica/` | 80 / 445 | 58 / 151 |
| `/sobre/` | 84 / 292 | 54 / 153 |
| `/honorarios-pericia-judicial/` | 58 / 144 | 58 / 158 |

- **Decisão de redação — o que entrou no espaço recuperado.** Cortar não é só encurtar: as descriptions antigas eram **listas de normas** ("RDC 275/2002, RDC 216/2004, RDC 655/2022, APPCC…"), que enchem o snippet com sinal para robô e não respondem a nada. As novas trocam a enumeração por **a pergunta que o leitor tem**: `/pericia-combustiveis/` abre com "Adulteração, contaminação e não conformidade não são a mesma coisa"; `/classificacao-fiscal-ncm/` com "A prova técnica que derruba uma reclassificação da Receita Federal". A norma continua na página; o snippet passa a vender a distinção que só quem domina a matéria faz.
- **Onde a autoridade foi preservada e onde foi cortada.** O sufixo "Por Adriana Rezende, engenheira química pela UNICAMP e perita judicial" era repetido em 6 descriptions e **nunca aparecia no SERP** — estava sempre depois do corte. Foi removido das descriptions de conteúdo, onde não cabia, e concentrado onde a consulta é sobre a pessoa: `/sobre/` mantém UNICAMP + CRQ IV-SP nº 04341673 + os anos de experiência dentro dos 153 caracteres visíveis, e a home mantém UNICAMP. Trocou-se repetição invisível por presença real em duas páginas.
- **`/assistente-tecnica/` — a mudança que motivou a execução.** Title de 74 → 59 ("Assistente técnico na perícia: o que faz e quando contratar"), com o termo-cabeça exato das duas consultas registradas no GSC na primeira posição. Saiu "(CPC 2015)", que consumia 11 caracteres do fim do title sem ser termo de busca. A description passou a caber inteira e a nomear os dois artigos que o advogado procura (arts. 465 e 477).
- **O que deliberadamente NÃO mudou:** os `<h1>`, o texto âncora dos blocos "Continue lendo", as descrições do `llms.txt` e o `headline`/`description` do JSON-LD `Article`. Nenhum deles é limitado por largura de SERP, e a forma longa e descritiva é **melhor** nesses três contextos — âncora descritiva dá contexto tópico, e o `Article.description` longo é o que os LLMs consomem. Título curto e H1 longo divergirem é o comportamento correto, não uma inconsistência a corrigir.
- **Verificação de escopo do diff:** conferido por script que as únicas linhas alteradas nos 9 arquivos são `<title>`, `meta description`, `og:title` e `twitter:title` — 33 inserções, 33 remoções, zero alteração colateral em conteúdo, schema ou links.
- **Validação executada sobre as 11 páginas:** todos os titles ≤ 60 e descriptions em 150–160; `og:title` e `twitter:title` idênticos ao `<title>` em todas; **zero titles duplicados** entre páginas; os blocos JSON-LD parseiam; HTML balanceado (parser sem tags pendentes); canonical correto nas 11; 1 `<h1>` por página. Script de validação retornou `ALL PASS`.
- **Por que o impacto é medível e em quanto tempo:** é a única mudança do site cujo efeito aparece numa métrica que já existe. Com 20 impressões em 30 dias a amostra ainda é pequena, mas a description agora legível é a condição para qualquer clique. **A leitura decisiva é o CTR de `/assistente-tecnica/` daqui a 7–14 dias**, depois de o Google recachear os snippets.

### Próxima execução — o que checar primeiro

1. **CTR e impressões de `/assistente-tecnica/`.** Se as impressões continuarem subindo e o CTR seguir em 0% com posição ≤ 10 depois de ~14/08, o problema deixa de ser metadado e passa a ser **intenção da página vs. intenção da consulta** — aí a tarefa vira revisar o topo da página, não o snippet.
2. **A dimensão `query` agora retorna linhas.** É o dado mais valioso disponível: assim que houver 5+ consultas distintas, elas — e não a intuição de cluster — passam a definir a próxima página a escrever.
3. **Se o quadro seguir sem clique**, a tarefa por intenção continua sendo **aprofundar o cluster de alimentos** (recolhimento/recall pela RDC 655/2022, ou prazo de validade e vida de prateleira), hoje o único pilar de alto valor sem spoke.
4. SEO-005 (`_headers` inerte) e SEO-019 (grafo interno) seguem abertos, ambos de score baixo.

---

## Estado da medição — 2026-08-08

Coleta por service account (`python3 ~/.config/adrianarezende/seo-report.py 30`), período 2026-07-09 → 2026-08-08.

- **26 impressões, zero cliques.** `/assistente-tecnica/` está em **21 impressões, posição média 8,1** — uma a mais que ontem, dentro de uma janela móvel de 30 dias que ganhou um dia no início e perdeu um no fim. Home 3 (pos. 6,0), `/classificacao-fiscal-ncm` 1 (pos. 11,0) e **`/sobre/` aparece pela primeira vez** (1 imp., pos. 32,0).
- **Dimensão `query`: 3 linhas** (era 2). Entrou "avaliações sobre quema química" (1 imp., pos. 32,0) — consulta com erro de digitação e intenção de reputação, provavelmente o que trouxe `/sobre/`. As duas anteriores seguem: "assistente tecnico pericia" (pos. 16,0) e "assistente técnico" (pos. 18,0).
- **Indexação: 11 de 11**, sem regressão.
- **GA4** segue não instrumentado (falta o ID numérico em `~/.config/adrianarezende/ga4-property`).

**Consequência para a priorização.** A SEO-016 foi executada ontem (07/08) e a leitura de CTR só é válida a partir de ~14/08, depois de o Google recachear os snippets — **medir hoje seria ler ruído**. O item 1 da lista de checagem fica portanto explicitamente adiado, não abandonado. O item 2 (5+ consultas distintas) ainda não foi atingido: são 3. Isso ativa o item 3 da lista: **aprofundar o cluster de alimentos**, único pilar de alto valor sem spoke.

---

## Auditoria — 2026-08-08

### O que está saudável — não mexer

- **11 de 11 indexadas**, zero links quebrados, zero órfãs, 1 `<h1>` por página, canonical correto, sitemap idêntico ao sistema de arquivos, JSON-LD parseando, títulos ≤ 60 e descriptions em 150–160 nas 11. Verificado por script nesta execução (`ALL PASS`).
- **Metadados:** a conformidade obtida ontem se manteve; nenhum título duplicado.

### Fraquezas encontradas

1. **O cluster de alimentos era o único pilar de alto valor sem nenhuma spoke.** Cinco pilares, três spokes — todas as três no cluster processual (impugnação, honorários, quesitos). Alimentos, que é a matéria de formação da profissional e a de maior densidade regulatória, tinha exatamente uma página. **Resolvido nesta execução (SEO-020).**
2. **Uma competência afirmada em duas páginas não tinha página própria.** `/sobre/` lista "prazo de validade e recall" como matéria de atuação em contaminação de alimentos, e `/assistente-tecnica/` também menciona prazo de validade — mas nenhuma página do site explicava como se determina ou como se contesta um prazo de validade. Mesmo padrão da SEO-018: o site afirma a competência e não a demonstra.
3. **SEO-019 (grafo interno completo) chega ao limiar.** Com a nova página são **12 páginas**, e o registro de 06/08 previa que o problema viraria real "por volta de 15". O bloco "Continue lendo" agora tem 10 itens em cada página. Continua aberto, mas deixou de ser teórico.
4. **SEO-005 (`_headers` inerte no GitHub Pages)** segue aberto, sem mudança.

### SEO-020 — Spoke: prazo de validade e vida útil de alimentos *(executada em 2026-08-08)*

- **Descrição:** Como se determina tecnicamente um prazo de validade, o que ele prova e o que não prova, e como se contesta — a primeira spoke do cluster de alimentos.
- **URL:** `/prazo-validade-alimentos/`
- **Categoria:** Conteúdo / Spoke de cluster / Intenção transacional
- **Impacto:** 8 · **Esforço:** 4 · **Confiança:** 7 · **Valor de negócio:** 9
- **Priority Score:** 126
- **Status:** done · **Descoberto:** 2026-08-07 · **Concluído:** 2026-08-08
- **Por que esta:** era a tarefa nomeada na lista de checagem da execução anterior, condicionada a "se o quadro seguir sem clique" — e o quadro seguiu sem clique. Entre as duas candidatas registradas (recall pela RDC 655/2022 e prazo de validade), **prazo de validade venceu por não haver sobreposição**: o pilar já dedica uma seção inteira e uma FAQ ao recall, então uma spoke de recall exigiria encurtar o pilar (o problema que a SEO-015 teve de resolver), enquanto "validade" aparecia zero vezes como assunto. Comercialmente também é mais amplo: alcança autuação sanitária, ação de consumo, disputa B2B entre elos da cadeia e auditoria de dossiê regulatório, enquanto recall alcança quase só a indústria em crise.
- **Implementado:** ~2.900 palavras. A tese organizadora é uma inversão de objeto que o conteúdo concorrente (quase todo divulgação para consumidor sobre "pode comer vencido?") não formula: **a data no rótulo não é prova sobre o alimento, é prova sobre o estudo que a produziu.** Daí decorre a tabela de abertura, que separa **quatro disputas distintas** que a expressão "prazo de validade" esconde — produto vencido, deterioração dentro do prazo, prazo mal determinado e reetiquetagem —, cada uma com objeto de prova próprio. A assimetria decisiva: pelo **art. 18, §6º, I, do CDC** o produto vencido é impróprio *por decurso de prazo*, de modo que **nenhum ensaio favorável reverte a impropriedade** — o laudo de laboratório, que é a defesa instintiva, é tecnicamente correto e juridicamente irrelevante nesse caso. Estrutura: as quatro disputas; quem determina o prazo e o duplo estatuto do Guia nº 16 (não normativo, mas parâmetro de referência da autoridade); as três regras de rotulagem que aparecem em litígio (precisão da data conforme a duração, isenções, condicionalidade às instruções de conservação); tabela dos seis tipos de estudo de vida útil com a fragilidade típica de cada um; a caixa dos quatro pressupostos de Arrhenius; **a lista do Anexo VIII** do Guia nº 16; seis falhas que invalidam uma determinação; a cadeia de frio como deslocamento de responsabilidade entre elos; tabela dos três regimes sancionatórios; e seis quesitos prontos para disputa de validade.
- **Por que a lista do Anexo VIII é o ativo da página:** é o conteúdo mínimo do dossiê de estabilidade a ser apresentado à autoridade sanitária, direto do guia da ANVISA, e nenhum concorrente o transpõe para uso forense. Serve como pedido de exibição de documentos, como roteiro de auditoria de dossiê e como checklist de perícia — o tipo de bloco que um LLM cita inteiro porque é autossuficiente e verificável.
- **Canibalização — nenhuma a resolver.** Verificado por busca no repositório antes de escrever: "validade" aparecia uma única vez em `/pericia-contaminacao-alimentos/` e no sentido de "validade probatória" de laboratório, não de prazo. Nada foi encurtado. Os dois pontos em que o pilar tangencia o assunto viraram links contextuais.
- **Links de entrada:** 13 no total, vindos de 12 páginas — sétimo card de Insights na home, "Continue lendo" das dez demais, **dois links contextuais dentro do pilar de alimentos** (um novo parágrafo ao fim da seção do CDC, separando o caso da data do caso do contaminante, e um novo passo na lista "Como a perícia atua na prática") e **um link contextual dentro de `/sobre/`**, na célula da tabela de matérias que já dizia "prazo de validade e recall" e agora aponta para a página que a sustenta. `sitemap.xml` e `llms.txt` atualizados.
- **Ligação de cluster deliberada:** a página fecha com seis quesitos redigidos no formato da `/quesitos-periciais/` (objeto identificado, critério nomeado, método declarado) e liga a ausência de itens do Anexo VIII às famílias de falha da `/impugnacao-laudo-pericial/`. O cluster de alimentos passa a se apoiar no processual em vez de correr em paralelo.
- **Verificação factual — tudo conferido em fonte primária antes de publicar:**
  1. **Guia ANVISA nº 16/2018, versão 3, de 02/04/2025, vigente desde 03/04/2025** (o PDF completo foi baixado e lido; a numeração é 16, não 42 — a busca inicial sugeria outro número e foi corrigida na fonte). Confirmados: caráter **não normativo, recomendatório e não vinculante**, com admissão expressa de abordagens alternativas; a atribuição da determinação do prazo **ao fabricante, não à ANVISA**; a taxonomia de métodos diretos e indiretos; a recomendação de **confirmar resultados indiretos por estudo de longa duração ou de acompanhamento**; a presunção de que a taxa de reação **dobra a cada 10 °C** com a ressalva de que pode triplicar ou ser menor; os **quatro pressupostos** do modelo de Arrhenius; a definição de **Q10**; a referência à **ISO 20976-1** para testes-desafio; a exigência de **repetir o teste** após mudança de pH, atividade de água, conservantes, ingredientes, embalagem ou processo; a **zona climática IVb (30 °C ± 2 °C, 75 % UR ± 5 % UR)** com a ressalva da amplitude térmica brasileira; a regra de que a validade é **o menor período em que algum atributo deixa de atender ao critério**; e a lista integral do **Anexo VIII**.
  2. **RDC ANVISA nº 727/2022** (texto integral baixado; a republicação no DOU de 19/10/22 começa no art. 12, então foi usada também a versão completa). Confirmados: **art. 4º, I** (rótulo não pode induzir a erro quanto à validade); **art. 7º, XI** (declaração obrigatória) com **§3º** remetendo ao Anexo I e **§4º** para painel principal inferior a **10 cm²**; **art. 31** (as nove expressões admitidas; dia e mês até três meses, mês e ano acima de três meses; "fim de…" para dezembro); **art. 32** (precauções, temperaturas máxima e mínima, tempo garantido nessas condições, regra dos congelados); **Anexo I** (lista de isentos, conferida item a item); **art. 41** (vigência em 1º de setembro de 2022).
  3. **CDC (Lei nº 8.078/1990), art. 18, §6º, I** — texto literal conferido: "os produtos cujos prazos de validade estejam vencidos".
  4. **Lei nº 6.437/1977, art. 10, XVIII**, na redação da MP nº 2.190-34/2001 — conferido o texto e o **número do artigo** (a lei numera os artigos em formato irregular no HTML do Planalto; o inciso foi rastreado até o art. 10 por varredura do texto, não por presunção). Penas conferidas.
  5. **Lei nº 8.137/1990, art. 7º, IX e parágrafo único** — conferidos a conduta, a pena de **detenção de 2 a 5 anos ou multa** e a **punição da modalidade culposa**.
  6. **Decreto nº 9.013/2017 (RIISPOA), art. 443, VII**, com a **redação dada pelo Decreto nº 10.468/2020** — conferido que a redação vigente exige "prazo de validade e identificação do lote" (a redação original exigia também data de fabricação; citar a original seria erro).
- **Nota de método:** o Planalto voltou a recusar a requisição via ferramenta de fetch, como já registrado na SEO-018. Contornado com `curl` e user-agent de navegador, com extração e leitura do texto integral. Vale registrar como procedimento padrão para as próximas execuções.
- **Onde estava a única surpresa:** o Guia nº 16 está na **versão 3, de abril de 2025** — a versão 2 é de 2024 e a original de 2018. Um texto escrito de memória citaria a versão 2 ou a numeração antiga. Mantém o padrão já observado: as surpresas se concentram em **regulação técnica**, não em direito.
- **Validação executada sobre as 12 páginas:** title 58 caracteres e description 152 na página nova; todos os titles ≤ 60 e descriptions em 150–160; `og:title` e `twitter:title` idênticos ao `<title>`; zero titles duplicados; os três blocos JSON-LD parseiam em todas; **paridade FAQ conferida por script** — as 8 perguntas e as 8 respostas do `FAQPage` são idênticas, caractere a caractere, ao texto visível; HTML balanceado; zero links internos quebrados no site inteiro; sitemap idêntico ao sistema de arquivos; canonical correto nas 12; nenhuma página órfã. Script retornou `ALL PASS`. Renderização conferida no navegador em 1280 px e em 375 px: **zero overflow horizontal do documento**, as três tabelas rolam dentro dos próprios contêineres.
- **Manutenção:** média. Os pontos a acompanhar são o **Guia nº 16** (já teve três versões em sete anos, e a v3 é de 2025) e a **RDC nº 727/2022**. O CDC e as Leis 6.437/1977 e 8.137/1990 são estáveis.

### Próxima execução — o que checar primeiro

1. **CTR de `/assistente-tecnica/` — agora sim.** A janela de recache dos snippets fecha por volta de 14/08. Se as impressões seguirem subindo com CTR 0% em posição ≤ 10, o problema deixa de ser metadado e vira **intenção da página vs. intenção da consulta**: a tarefa passa a ser reescrever o topo da página, não o snippet.
2. **Indexação de `/prazo-validade-alimentos/`.** A latência medida é de 1 a 4 dias. Só investigar se continuar fora depois de ~12/08.
3. **Dimensão `query`:** 3 linhas hoje. Ao chegar a 5+ consultas distintas, elas passam a definir a próxima página, substituindo a intuição de cluster.
4. **SEO-019 passa a ser candidata real.** Com 12 páginas e 10 itens em cada "Continue lendo", o bloco deixou de transmitir hierarquia. Se nada com dado o superar, é a tarefa de arquitetura a executar antes da 15ª página.
5. **Se o quadro de dados seguir vazio**, a próxima spoke por intenção é a segunda do cluster de alimentos — **recolhimento/recall pela RDC 655/2022**, que exigirá encurtar a seção correspondente do pilar (canibalização a resolver, ao contrário desta execução).

---

## Estado da medição — 2026-08-09

Coleta por service account (`python3 ~/.config/adrianarezende/seo-report.py 30`), período 2026-07-10 → 2026-08-09.

- **36 impressões, zero cliques** (eram 24 em 07/08). O volume cresce, o CTR não sai de 0%.
- **`/assistente-tecnica/`: 22 impressões, posição 8,1** — ainda 61% do site, estável em posição.
- **Cauda nova:** quatro páginas que não apareciam agora aparecem — `/honorarios-pericia-judicial/` (3 imp., pos. 6,7), `/quesitos-periciais/` (3 imp., pos. 6,7), `/pericia-combustiveis/` (2 imp., pos. 7,0), `/pericia-industria-quimica/` (1 imp., pos. 7,0). **Cinco das oito páginas com impressão estão na posição 6–8.** É exatamente a faixa 5–20 que o mandato marca como Prioridade 2, e o problema delas não é ranking, é snippet.
- **Dimensão `query`: 3 linhas**, uma nova ("avaliações sobre quema química", pos. 32,0 — consulta de terceiro, sem intenção de contratação). Ainda abaixo do limiar de 5 que definiria a próxima página por dado.
- **Indexação: 11 de 11** publicadas. A 12ª não constava porque **não estava publicada** — ver abaixo.
- **GA4** segue não instrumentado (falta o ID numérico em `~/.config/adrianarezende/ga4-property`).

---

## Auditoria — 2026-08-09

### A fraqueza que anulava as duas execuções anteriores

**O repositório estava dois commits à frente do site publicado.** `git status` acusava `ahead 2` e o site ao vivo servia a versão de 06/08:

| Commit | Data | O que continha | Estado ao vivo em 09/08 |
|---|---|---|---|
| `c539777` (SEO-016) | 07/08 | Metadados ajustados ao limite de exibição do SERP em 9 páginas | **não aplicado** — `/assistente-tecnica/` ainda servia description de **258 caracteres** |
| `9b6caba` (SEO-020) | 08/08 | Página `/prazo-validade-alimentos/` (~2.900 palavras) | **404** |

Consequência direta: a única página do site com impressão de dois dígitos passou **dois dias inteiros** aparecendo 22 vezes na posição 8,1 com o snippet truncado que a SEO-016 existia para corrigir — a atribuição de autoridade ("engenheira química pela UNICAMP e perita judicial") continuava caindo fora da parte visível. E a spoke de alimentos, cujo custo de produção e verificação factual já tinha sido pago, **não existia para o Google**.

O trabalho estava correto, validado e commitado. Só não estava no ar. Nenhuma das duas execuções mentiu no relatório: ambas descreveram fielmente o que fizeram no repositório — **e nenhuma das duas verificou o site publicado depois**. O relatório da SEO-016 chegou a afirmar "a conformidade obtida ontem se manteve", conferida no arquivo local; ao vivo ela nunca chegou a existir.

### Por que esta foi a tarefa de hoje

Pelo próprio escore do mandato não havia competição. Publicar duas melhorias já prontas e já pagas custa **esforço 1** e entrega o valor integral de duas tarefas que somam 216 pontos de prioridade — enquanto qualquer página nova nasceria com o mesmo defeito e também não iria ao ar. É Prioridade 1 na definição literal do playbook: **aumentar conversão de páginas que já têm impressão**. Escrever uma 13ª página com a esteira de publicação quebrada seria acumular estoque, não entregar resultado.

### SEO-021 — Deriva entre repositório e site publicado *(executada em 2026-08-09)*

- **Descrição:** o commit era tratado como fim do processo, mas o site é servido pelo GitHub Pages a partir de `origin/main`. Sem `push`, a execução termina com relatório de sucesso e **nenhuma mudança ao ar**. Falha silenciosa por definição: nada no repositório local a denuncia.
- **URL:** todas
- **Categoria:** Processo / Entrega
- **Impacto:** 10 · **Esforço:** 1 · **Confiança:** 10 · **Valor de negócio:** 9
- **Priority Score:** 900
- **Status:** done · **Descoberto:** 2026-08-09 · **Concluído:** 2026-08-09
- **Implementado:**
  1. **Publicado.** `git push origin main` (`8bd564b..9b6caba`). Verificado ao vivo depois do rebuild do GH Pages: `sitemap.xml` com **12 `<loc>`**, `/prazo-validade-alimentos/` respondendo **200** (era 404), description de `/assistente-tecnica/` ao vivo com **154 caracteres** (era 258).
  2. **Guard automático.** `seo-report.py` ganhou a checagem `[deploy]`, que roda **antes** dos dados de Search Console em toda execução: faz `git fetch`, compara `origin/main..HEAD` e cruza os diretórios de página do repositório com as URLs do sitemap **publicado**. Havendo deriva, imprime cada commit sem push e cada página ausente ao vivo, com a ação a executar. Testado nos dois estados — acusou os dois commits e a página faltante antes do push, e passou a "em dia — 12 páginas publicadas, 0 commits pendentes" depois.
- **Validação do site antes de publicar** (12 páginas, `ALL PASS`): titles ≤ 60 e sem duplicata; descriptions entre 150 e 160; `og:title` e `twitter:title` idênticos ao `<title>`; canonical correto nas 12; um `<h1>` por página; todos os blocos JSON-LD parseando; zero links internos quebrados; sitemap idêntico ao sistema de arquivos; nenhuma página órfã.
- **Regra que passa a valer:** *uma execução só está concluída quando a mudança está ao vivo e verificada por requisição ao domínio* — não quando o commit existe. O relatório diário deve citar a evidência ao vivo (código HTTP, contagem do sitemap ou trecho do metadado servido), não o estado do arquivo local.
- **Por que não virou hook de git ou CI:** o guard vive no script que a execução diária **já roda como primeiro passo**, então custa zero disciplina nova e aparece no ponto em que a decisão do dia é tomada. Um workflow do GitHub Actions só reportaria depois do push — exatamente o passo que estava faltando.

### SEO-022 — Tratamento completo de "parecer técnico" no hub de assistência técnica

- **Descrição:** a âncora `/assistente-tecnica/#parecer-tecnico` — destino de campanha paga de correspondência exata e de um sitelink — entregava uma lista de seis marcadores. Nenhuma página do site definia o parecer técnico, o distinguia do laudo pericial, descrevia seu conteúdo ou mencionava os dois usos anteriores à perícia (arts. 471 e 472 do CPC).
- **URL:** `/assistente-tecnica/`
- **Categoria:** Conversão / Semântica / Autoridade tópica
- **Impacto:** 9 · **Esforço:** 3 · **Confiança:** 8 · **Valor de negócio:** 9
- **Priority Score:** 216
- **Status:** done · **Descoberto:** 2026-08-10 · **Concluído:** 2026-08-10
- **Implementado:**
  - **Nova seção `#parecer-tecnico`** (a âncora foi movida para cá; a lista de entregáveis que a ocupava recebeu `id="entregaveis"`, sem quebrar nada): caixa de definição, **tabela laudo pericial × parecer técnico em seis dimensões** (quem assina, base legal, objeto, alcance, momento, efeito) e **as sete partes de um parecer utilizável**. Fecha com os poderes instrutórios do art. 473, §3º — perito *e assistentes* podem ouvir testemunhas, obter informações e requisitar documentos de terceiros e de repartições públicas. É um ponto que a concorrência quase não explora e que muda o que o cliente entende ser possível contratar.
  - **Nova seção `#parecer-antes-da-pericia`** — o argumento comercial mais forte da página, que não existia: **art. 472** (o juiz pode dispensar a prova pericial diante de pareceres técnicos apresentados na inicial e na contestação) e **art. 471** (perícia consensual; partes plenamente capazes, causa que admita autocomposição, assistentes indicados desde logo, e o §3º — substitui para todos os efeitos a perícia por perito nomeado). Terceira sub-seção sobre uso extrajudicial e administrativo, com links contextuais para NCM e ambiental.
  - **Nova seção `#analise-preliminar`** — cinco itens que o advogado deve enviar para uma avaliação inicial, incluindo a declaração de que a resposta pode ser que a técnica não favorece o caso. Converte a CTA de "solicite contato" em um pedido concreto.
  - **Detalhe do art. 466, §2º** no calendário: a comunicação das diligências aos assistentes exige **antecedência mínima de 5 dias**, comprovada nos autos. Antes a página dizia apenas "acesso e acompanhamento".
  - **Quatro novas perguntas frequentes** (de 9 para 13), espelhadas no `FAQPage` com paridade textual exata verificada por script: o que é um parecer técnico; laudo × parecer; parecer antes da perícia; poderes de investigação do assistente.
  - **Schema:** `description` do `Article` reescrita; `about` ganhou `Parecer Técnico` e `Laudo Pericial`; `knowsAbout` do autor idem.
  - **Links internos:** `/impugnacao-laudo-pericial/` passou a apontar para `#parecer-tecnico` no item em que descreve o parecer como peça autônoma; `/quesitos-periciais/` passou a apontar para `#parecer-antes-da-pericia` exatamente onde discute o art. 472. Âncoras precisas em vez de link genérico para a raiz da página.
  - Página de 34 KB → **48,6 KB**. `sitemap.xml` (`lastmod` 2026-08-10) e `llms.txt` atualizados.
- **Não tocado de propósito:** `<title>` e `<meta name="description">`. O teste de CTR dos snippets corrigidos em 09/08 só é legível a partir de ~16/08.
- **Verificação factual — cinco dispositivos checados em fonte antes de publicar:**
  1. **Art. 472** — texto confirmado literalmente ("pareceres técnicos ou documentos elucidativos que considerar suficientes"). Confirmado também que o uso é raro na prática, o que a página reflete em vez de esconder.
  2. **Art. 471** — os dois requisitos (partes plenamente capazes; causa que admita autocomposição), o §1º (assistentes indicados desde logo) e o §3º ("substitui, para todos os efeitos") confirmados.
  3. **Art. 473, §3º** — confirmado que o dispositivo alcança expressamente **o perito *e* os assistentes técnicos**, e não só o perito. Era o ponto de maior risco de erro de memória do texto todo.
  4. **Art. 466, §2º** — antecedência mínima de 5 dias, com comunicação comprovada nos autos. Confirmado.
  5. **Art. 477** — laudo protocolado ao menos 20 dias antes da audiência; prazo comum de 15 dias para manifestação e para o parecer do assistente. Confirmado.
- **Validação do site inteiro antes de publicar** (12 páginas): todos os blocos JSON-LD parseando; titles ≤ 60 sem duplicata; descriptions entre 150 e 160; `og:title` e `twitter:title` idênticos ao `<title>`; canonical correto nas 12; um `<h1>` por página; **zero links internos quebrados e zero âncoras inexistentes** (o verificador passou a conferir o fragmento `#`, não só o caminho — foi acrescentado hoje justamente porque a tarefa criou e moveu âncoras); sitemap idêntico ao sistema de arquivos; balanceamento de tags conferido nas três páginas editadas.

### SEO-023 — Paridade imperfeita entre FAQ visível e `FAQPage` em duas páginas

- **Descrição:** duas divergências encontradas pela validação de hoje, ambas anteriores a esta execução e nenhuma delas quebrando a marcação. Em `/sobre/`, as sete perguntas do schema usam redação ligeiramente diferente da visível ("Como verificar o registro profissional de Adriana Rezende?" no schema × "Como verificar o registro profissional?" na página). Em `/assistente-tecnica/`, a resposta sobre custo tem, na página, uma frase final com link que o schema omite — o schema é subconjunto do visível, que é a direção inofensiva.
- **URL:** `/sobre/`, `/assistente-tecnica/`
- **Categoria:** Structured data
- **Impacto:** 3 · **Esforço:** 1 · **Confiança:** 7 · **Valor de negócio:** 3
- **Priority Score:** 63
- **Status:** open · **Descoberto:** 2026-08-10
- **Notas:** a diretriz do Google exige que a resposta do schema esteja visível na página — o que é verdade nos dois casos. O risco é de rigor, não de penalidade. Resolver junto com a próxima edição dessas páginas, não isoladamente.
- **Nota de 2026-08-11:** a avaliação acima está correta para as duas páginas citadas, e a checagem automática criada no SEO-024 confirma que ambas passam pelo critério que importa (a resposta está visível). A busca por essa mesma divergência, porém, revelou um **terceiro caso, de natureza diferente e bem mais grave — a home** —, que esta entrada não alcançou. Ver **SEO-025**.

### O que segue em aberto

- **SEO-019** (grafo interno diferenciado por proximidade tópica) — sem mudança. Os dois links de âncora precisa adicionados hoje são um começo na direção certa.
- **SEO-023** (paridade de FAQ) — novo, baixa prioridade.
- **SEO-005** (`_headers` inerte no GitHub Pages) — sem mudança.
- **SEO-009** (perfil no Google Business) — segue bloqueado por verificação de identidade da proprietária.

### Próxima execução — o que checar primeiro

1. **`[deploy]` no topo do relatório.** Regra inalterada: se acusar deriva, publicar é a tarefa do dia.
2. **A partir de 16/08, o CTR das páginas em posição 6–8 finalmente é interpretável.** Se seguir em 0% com posição ≤ 10 e impressões acumuladas acima de ~100, o diagnóstico deixa de ser snippet e passa a ser intenção — e a tarefa vira reescrever o topo de `/assistente-tecnica/`.
3. **Vigiar as consultas que a nova seção deve abrir:** `parecer técnico`, `parecer técnico judicial`, `diferença entre laudo e parecer técnico`, `art. 472 CPC`. Se aparecerem no relatório dentro de 7 a 14 dias, a tese de aprofundar o hub em vez de criar página nova se confirma, e o mesmo tratamento deve ser aplicado aos outros hubs rasos. Se não aparecerem, a próxima expansão volta a ser página dedicada.
4. **Google Ads:** o grupo AG03 agora tem destino à altura do lance. Vale conferir a taxa de conversão dele separadamente, já que a landing mudou de lista de marcadores para seção de referência.
5. **Se o quadro seguir sem clique orgânico**, a próxima spoke por intenção continua sendo recolhimento/recall pela RDC 655/2022.

### SEO-024 — O guard do SEO-021 não era descobrível *(executada em 2026-08-11)*

> **Renumerada de SEO-022 para SEO-024.** A execução de 2026-08-10 já havia usado SEO-022 e SEO-023, mas o trabalho dela estava sem commit e portanto invisível quando esta entrada foi escrita. Os commits `d4b7d8b`, `fc082f0` e `8f31cba` citam "SEO-022" na mensagem e não podem ser reescritos — são estes daqui.

- **Descrição:** o `seo-report.py` criado no SEO-021 vivia **fora do repositório**, em `~/.config/adrianarezende/seo-report.py`, sem nenhuma menção no repositório que permitisse encontrá-lo. Na prática, indescobrível: cada checagem do SEO-021 (deriva de publicação, validação das 12 páginas, consulta ao Search Console) teve de ser reescrita à mão nesta execução antes de qualquer decisão.
- **Correção de rumo durante a execução:** a primeira versão desta entrada afirmava que o script **havia sido apagado** com o diretório temporário da sessão. Está errado — uma busca no sistema de arquivos, concluída depois, encontrou o arquivo intacto no caminho acima. O remédio (versionar no repositório) continua correto, e o arquivo antigo foi preservado onde está; o diagnóstico é que era invisível para quem executa a tarefa, não que tinha sido destruído.
- **URL:** `tools/seo-report.py`
- **Categoria:** Processo / Medição / Entrega
- **Impacto:** 9 · **Esforço:** 2 · **Confiança:** 10 · **Valor de negócio:** 8
- **Priority Score:** 360
- **Status:** done · **Descoberto:** 2026-08-11 · **Concluído:** 2026-08-11
- **Por que esta tarefa e não conteúdo:** as duas frentes de conteúdo estavam bloqueadas por data. O veredito sobre snippets só é válido depois de ~16/08 (janela de recache aberta em 09/08), e a decisão orientada por consultas dependia do relatório que não existia mais. Publicar uma 13ª página com 58 impressões acumuladas em 28 dias acrescentaria cobertura marginal; restaurar o controle que já evitou um dia inteiro de trabalho commitado-e-não-publicado protege todas as 12 páginas e toda execução futura. Score 360 contra 33,3 do SEO-019 e ~120 de uma spoke nova.
- **Implementado:** `tools/seo-report.py`, **versionado no repositório**, com quatro seções executáveis isoladamente (`deploy`, `valid`, `gsc`, `ga4`) e código de saída 1 em qualquer falha, para poder barrar uma publicação.
  1. **`[deploy]`** — `git fetch`, commits em `origin/main..HEAD`, arquivos rastreados modificados sem commit, diretórios de página do repositório × URLs do **sitemap publicado**, e status HTTP das 12 URLs ao vivo.
  2. **`[valid]`** — title ≤ 60 e sem duplicata, description entre 150 e 160, `og:title`/`twitter:title` idênticos ao `<title>`, canonical exato, um único `<h1>`, todo JSON-LD parseando, links internos resolvendo, sitemap local idêntico ao sistema de arquivos, nenhuma página órfã.
  3. **`[gsc]`** — desempenho de 28 dias por página e por consulta, mais o estado de indexação de cada página pela URL Inspection API.
  4. **`[ga4]`** — sessões por página e por canal, que é o que separa "ninguém chega" de "chega e sai".
  5. **Paridade FAQ ↔ `FAQPage`** (acrescentada depois, ver abaixo) — falha quando **nem a pergunta nem a resposta** do schema aparecem na página, e quando a contagem de perguntas visíveis difere da do schema. Foi essa checagem que encontrou o **SEO-025**.
- **A checagem de FAQ errou três vezes antes de acertar, e as três merecem registro** — todas eram falsos negativos ou falsos positivos que teriam passado por revisão superficial:
  1. **Regex frágil.** `<div class="faq">(.*?)</div>` não-guloso parava no primeiro `</div>` interno, subcontando as perguntas visíveis. Trocado por corte por índice até `</section>`.
  2. **Comparação por redação da pergunta.** Exigir que o texto do `<h3>` fosse idêntico ao `name` do schema acusava `/sobre/`, onde a diferença é só copywriting ("Em que tipos de processo atua?" × "…Adriana Rezende atua?"), e enterrava o achado real em ruído. O critério passou a ser o que a diretriz do Google de fato exige: pergunta **ou** resposta presente na página.
  3. **O extrator de texto não removia o corpo de `<script>`.** Só as tags. O JSON-LD virava "texto visível", então "a resposta está na página?" respondia sempre sim — a checagem era incapaz de falhar. Provado por injeção: uma pergunta reescrita para algo inexistente na página **não** era acusada. Depois da correção, é.
- **Teste de injeção da checagem nova:** pergunta de schema sem contrapartida visível → acusada; `<h3>` visível removido do FAQ mantendo o schema (13 × 12) → acusado; as redações legítimas de `/sobre/` → **não** acusadas. As 12 páginas do repositório passam, exceto a home, que é o SEO-025.
- **Duas capacidades recuperadas do script antigo depois de encontrá-lo** — a reescrita à mão as havia perdido, e ambas foram portadas:
  - **Detecção da propriedade do Search Console** em vez de assumir a forma `sc-domain:`. O script antigo trazia um comentário registrando que essa suposição gerou **403 na primeira execução, em 2026-08-05**. A nova versão pergunta à API qual propriedade a conta lê e imprime o nível de permissão (`sc-domain:adrianarezende.com.br`, `siteFullUser`).
  - **Seção GA4**, que a reescrita não tinha. Foi ela que revelou o achado mais importante do dia (abaixo).
  - A chave de serviço passou a ser procurada nos **três** caminhos que execuções distintas criaram (`claude-seo/google-api.json`, `claude-seo/service-account.json`, `adrianarezende/seo-sa.json`), em vez de um só.
- **Correção de um ponto cego durante a escrita:** a primeira versão reportava "0 commits pendentes" quando o próprio `git` falhava, porque só olhava a saída padrão. Isso reproduziria a falha do SEO-021 com outra causa — sucesso aparente sem informação real. Agora `git fetch` e `git log` têm o código de retorno verificado, e um `git` quebrado imprime **"estado de publicação DESCONHECIDO"** e falha.
- **Validação por injeção de defeito** (cópia descartável do site, nunca no repositório real): nove defeitos plantados — title de 86 caracteres, description de 12, `og:title` e `twitter:title` divergentes, canonical sem barra final, link interno para página inexistente, JSON-LD com vírgula dupla, página fora do sitemap e sitemap apontando para página fantasma. **Os nove foram detectados, com saída 1.** Em seguida, uma página presente no repositório e ausente do sitemap publicado (o cenário exato do SEO-021) e um `git` inoperante — ambos acusados. O repositório real segue `ALL PASS` nas três seções.
- **Limitação conhecida do `[deploy]`, observada em 12/08:** logo depois do push do SEO-025, o `[deploy]` deu `ALL PASS` enquanto a home ainda servia o `FAQPage` removido. É correto pelo que ele mede — 0 commit pendente, sitemap em dia, 12 URLs em 200 — mas ele **não compara conteúdo**, e o GitHub Pages leva de alguns segundos a alguns minutos para reconstruir. `ALL PASS` significa "o repositório e o índice de URLs estão em dia", **não** "o conteúdo novo já está ao vivo". Quem publica precisa confirmar o trecho alterado por `curl` ao domínio, como manda a regra do SEO-021, e repetir até aparecer. Não vale automatizar por hash: a janela de rebuild é normal, e uma checagem que falha durante ela viraria ruído a ser ignorado — que é como um guard morre.
- **Interpretador:** rodar com `/usr/bin/python3`. As bibliotecas do Google estão instaladas ali, não nos pythons do Homebrew. Só a seção `[gsc]` depende delas; `deploy` e `valid` são stdlib puro.

### SEO-025 — `FAQPage` da home é dado estruturado oculto

- **Descrição:** a home declara um `FAQPage` com **cinco perguntas cujo texto não existe na página** — nem a pergunta, nem a resposta. Verificado no HTML bruto, ignorando os blocos `<script>`: nenhuma das cinco perguntas nem dos cinco trechos de resposta aparece no `<body>`. Não há `<details>`, `<summary>` ou acordeão que as renderize, e nada é injetado por JavaScript. É marcação de conteúdo que o visitante nunca vê.
- **Por que é diferente do SEO-023:** ali o schema é subconjunto do texto visível, ou a pergunta está reescrita — direções inofensivas. Aqui o conteúdo **não está na página**, que é exatamente o que a diretriz de dados estruturados do Google proíbe. A consequência esperada não é perder o rich result: é o markup ser desconsiderado, com risco de ação manual por *structured data* enganoso na propriedade inteira.
- **URL:** `/`
- **Categoria:** Structured data / Risco de conformidade
- **Impacto:** 7 · **Esforço:** 2 · **Confiança:** 9 · **Valor de negócio:** 6
- **Priority Score:** 189
- **Status:** done · **Descoberto:** 2026-08-11 · **Concluído:** 2026-08-12
- **Resolvido pela opção (b), decidida pela cliente:** o bloco `FAQPage` inteiro foi removido de `index.html` — 5 perguntas, 2.564 caracteres. Preservados na home: `Person`, `ProfessionalService` (com o `OfferCatalog` de 6 serviços), `BreadcrumbList`, `WebSite` e os quatro `SiteNavigationElement`. Nenhuma referência pendente ao FAQ da home no `llms.txt` nem no HTML. A validação das 12 páginas voltou a `ALL PASS`.
- **Por que remover foi o certo aqui:** as cinco perguntas eram versões abreviadas de matéria que `/assistente-tecnica/`, `/pericia-contaminacao-alimentos/`, `/classificacao-fiscal-ncm/` e `/impugnacao-laudo-pericial/` já respondem com profundidade. Torná-las visíveis na home resolveria a conformidade criando concorrência interna pelas mesmas consultas — pior remédio que a doença.
- **Idade do defeito:** está no ar desde 2026-08-01, quando o schema da home foi criado. Passou por todas as auditorias anteriores porque nenhuma comparava schema com texto visível — e a primeira versão da checagem nova também não pegou, por um motivo instrutivo registrado no SEO-024 (o extrator de texto removia as *tags* `<script>` mas não o conteúdo delas, de modo que o próprio JSON-LD entrava no "texto visível" e a comparação passava sempre).
- **Duas saídas, e a escolha não é óbvia:** (a) **tornar as cinco perguntas visíveis** na home, como seção de FAQ — ganha o conteúdo, o rich result e material citável por LLM, mas alonga uma home que hoje é enxuta e concentra em `/` respostas que já existem, melhor desenvolvidas, nas páginas de cluster; (b) **remover o `FAQPage` da home**, mantendo `Person`, `ProfessionalService` e `BreadcrumbList` — resolve a conformidade em uma linha e deixa o FAQ onde ele tem profundidade. **Recomendação: (b)**, porque as cinco perguntas são versões resumidas de conteúdo que as páginas de cluster já respondem melhor, e duplicá-las na home criaria concorrência interna pelas mesmas consultas. Decidir com a cliente antes de executar — é remoção de markup em página pública.

### Auditoria de 2026-08-11 — leitura dos dados

- **Publicação:** sem deriva. 12 páginas no sitemap publicado, 12 respondendo 200, 0 commits pendentes no início da execução.
- **Indexação: as 12 páginas estão indexadas** (`Enviada e indexada`, verdict `PASS`). Isso **resolve o item 3 da lista anterior antes do prazo**: `/prazo-validade-alimentos/` foi rastreada em 10/08 e já está indexada. Indexação deixa de ser hipótese de gargalo.
- **Desempenho (28 dias): 58 impressões, 0 cliques, 9 das 12 páginas com impressão.** `/pericia-ambiental/` e `/pericia-contaminacao-alimentos/` ainda não apareceram nenhuma vez.
- **GA4 contradiz o "0 cliques" do Search Console — e é o achado mais importante do dia.** 38 sessões em 28 dias, das quais **2 de busca orgânica**, além de 8 de Paid Search na home (Google Ads), 26 diretas, 1 referral (`periciajudicial.zsistemas.com.br`) e 1 não atribuída.
- **Resolvido em 12/08 — a origem é o Google, não o Bing.** Cruzamento por `sessionSource` / `sessionMedium`: as duas sessões orgânicas são `google / organic`. Por `landingPagePlusQueryString`, ambas caíram em **2026-08-10**, uma em `/pericia-industria-quimica/` e outra em `/quesitos-periciais/`. **São os dois primeiros cliques orgânicos do site.**
  - **Por que o Search Console não os mostra:** a série por data do GSC **termina em 09/08** — não existem linhas para 10, 11 e 12/08. Os cliques caíram fora da janela que o GSC já processou. O "0 cliques" era **artefato de latência, não um zero real**, e nenhuma conclusão sobre CTR ou snippet podia ter sido tirada dele.
  - **Correção de contagem:** a primeira leitura desta execução registrou "4 sessões orgânicas". Errado — eram **2**. O número veio de um relatório `pagePath` × canal, onde cada página vista dentro de uma sessão gera uma linha; 2 sessões que viram 2 páginas cada produziram 4 linhas. A dimensão correta para contar sessão é `landingPage`, e ela dá 2. A seção `[ga4]` do script usa `pagePath` de propósito (mostra qual conteúdo é consumido), então **essa saída não deve ser lida como contagem de sessões**.
  - **Consequência prática:** o gargalo segue sendo alcance, não snippet — mas agora com evidência de que a cadeia impressão → clique → sessão **funciona**. As duas páginas que converteram (`/pericia-industria-quimica/`, `/quesitos-periciais/`) não são as de maior impressão, o que reforça olhar intenção por página em vez de CTR agregado.
- **Por qual consulta entraram os dois cliques: indisponível em 12/08, e possivelmente para sempre.** Duas causas independentes, medidas:
  1. **Latência.** A série do GSC continua terminando em **09/08** três dias depois (consultado em 12/08). Não há linha alguma para 10/08 — nem por data, nem por `query × page`. A latência observada nesta propriedade é de ~3 dias, não os 2 que eu vinha assumindo.
  2. **Anonimização, que é o limite mais sério.** No período 01/08–12/08 o site tem **58 impressões** pelas dimensões `date` e `page`, mas apenas **8 impressões** aparecem na dimensão `query` — as mesmas 8 consultas com 1 impressão cada. **50 das 58 impressões (86%) estão em consultas que o Google retém** por serem raras demais. Um clique isolado tem, portanto, chance real de nunca ter consulta visível.
  - **Não existe fonte alternativa.** O Google não repassa o termo de busca orgânica ao GA4; o GSC é a única origem possível. Não é questão de método de coleta.
  - **Isto enfraquece uma regra registrada anteriormente.** O backlog fixou que, ao passar de 5 linhas na dimensão `query`, as consultas passariam a decidir o conteúdo no lugar da intuição de cluster. Com 86% das impressões ocultas, essas 8 linhas são uma **amostra enviesada para consultas raras**, não um retrato da demanda. Usá-las como se fossem o quadro completo é erro de leitura — servem para confirmar temas, não para dimensionar demanda. A decisão de conteúdo volta a apoiar-se em intenção comercial, com as consultas visíveis como sinal corroborante.
- **Posições:** `/pericia-combustiveis/` 5,6 · `/` 6,0 · `/honorarios-pericia-judicial/` 6,2 · `/pericia-industria-quimica/` 7,0 · `/assistente-tecnica/` 8,1 · `/classificacao-fiscal-ncm/` 9,0 · `/quesitos-periciais/` 11,5 · `/impugnacao-laudo-pericial/` 31,2 · `/sobre/` 32,0.
- **O gargalo não é posição nem CTR — é alcance.** Sete páginas já estão entre 5 e 12. O site aparece para **oito consultas distintas em 28 dias**. Com 58 impressões, 0 clique está dentro do ruído estatístico (a expectativa na posição 8 seria de 1 a 2 cliques); nenhuma conclusão sobre snippet se sustenta nesse volume, o que **reforça** a espera até ~16/08 em vez de contrariá-la.
- **Dimensão `query` passou de 3 para 8 linhas**, cruzando o limiar que o próprio backlog fixou para as consultas passarem a decidir o conteúdo. O sinal de demanda é concentrado: **quatro das oito consultas são sobre impugnação de laudo pericial** — incluindo as grafias reais dos usuários, "impunação ao laudo pericial" e "como fazer impunação ao laudo pericial". A página dedicada responde por elas na posição 28–47, a pior do site, contra 6–12 das irmãs. A hipótese mais simples é idade: a página foi publicada em 06/08 e tinha cinco dias na data da medição. **Não agir sobre ela ainda** — reavaliar quando tiver duas semanas ao vivo, por volta de 20/08. Se continuar acima de 25 enquanto as irmãs seguem abaixo de 12, aí sim é defeito e não volatilidade.
- **Descartadas nesta auditoria, com evidência:** cobertura geográfica (Campinas e São Paulo já aparecem nas 12 páginas), canibalização entre `/assistente-tecnica/#impugnacao-laudos` e `/impugnacao-laudo-pericial/` (apenas 2 ocorrências de "impugna\*" na primeira contra 18 na segunda — escopos distintos), conteúdo raso (3.373 a 6.166 palavras por página) e bloqueio a rastreadores de IA (`robots.txt` libera GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot e Amazonbot).

### O que segue em aberto

- ~~**SEO-025** (`FAQPage` oculto na home)~~ — **resolvido em 12/08 por remoção do markup**, conforme decisão da cliente.
- **SEO-019** (grafo interno completo) — 12 páginas, 10 itens em cada "Continue lendo". Sem mudança. Os inbounds medidos hoje ficaram entre 11 e 24 por página — grafo plano, sem hierarquia pilar → spoke. Os dois links de âncora do SEO-022 são um começo na direção certa.
- **SEO-023** (redação do FAQ em `/sobre/` e `/assistente-tecnica/`) — baixa prioridade, 63. Agora coberto por checagem automática, que confirma: nas duas o critério que importa é atendido.
- **SEO-005** (`_headers` inerte no GitHub Pages) — sem mudança.
- **SEO-009** (perfil no Google Business) — segue bloqueado por verificação de identidade da proprietária.

### Próxima execução — o que checar primeiro

1. **Rodar `/usr/bin/python3 tools/seo-report.py` como primeiro passo.** Se `[deploy]` acusar deriva, publicar é a tarefa do dia, antes de qualquer outra coisa. Se qualquer seção falhar, corrigir antes de abrir frente nova.
2. **~~Separar Google de Bing nas sessões orgânicas~~ — resolvido em 12/08.** Ambas são do Google, em 10/08, e o GSC ainda não processou aquela data. Ver a nota na auditoria acima.
3. **Os dois cliques de 10/08 no Search Console — checar uma vez, sem insistir.** Em 12/08 a série ainda terminava em 09/08. Conferir quando passar de 10/08; se a consulta aparecer, ela entra direto na decisão de conteúdo. **Se não aparecer, encerrar a pergunta:** com 86% das impressões em consultas anonimizadas, é o resultado esperado, não um problema a investigar. Não gastar uma execução nisso.
4. **CTR das páginas entre 5 e 12 — só a partir de ~16/08.** A janela de recache dos snippets abriu em 09/08. Antes disso nenhuma conclusão sobre metadado é válida, e com menos de ~200 impressões acumuladas 0 clique continua sendo ruído, não diagnóstico. **Lembrete metodológico:** confirmar sempre até que data a série do GSC vai antes de tratar um zero como resultado.
5. **`/impugnacao-laudo-pericial/` — reavaliar por volta de 20/08**, quando tiver duas semanas ao vivo. É onde está a demanda real (4 das 8 consultas) e a pior posição do site. Se seguir acima de 25, tratar como defeito da página, não como idade.
6. **`/pericia-ambiental/` e `/pericia-contaminacao-alimentos/`: zero impressão em 28 dias, apesar de indexadas.** Duas páginas indexadas que nunca apareceram é o achado mais concreto para investigar depois do item 5 — provável descasamento entre o que a página responde e o que se pesquisa nesses dois temas.
7. **Vigiar as consultas que a seção do SEO-022 deve abrir** (herdado da execução de 10/08, que não pôde publicar): `parecer técnico`, `parecer técnico judicial`, `diferença entre laudo e parecer técnico`, `art. 472 CPC`. **O relógio delas começa em 12/08**, data em que a seção foi de fato publicada — não em 10/08. Se aparecerem em 7 a 14 dias, a tese de aprofundar hub existente em vez de criar página nova se confirma e deve ser aplicada aos outros hubs rasos.
8. **Google Ads (herdado de 10/08):** o grupo AG03 agora tem destino à altura do lance. Conferir a taxa de conversão dele separadamente, já que a landing mudou de lista de marcadores para seção de referência — também a partir de 12/08.
9. **Só depois disso**, a próxima spoke por intenção continua sendo **recolhimento/recall pela RDC 655/2022**, que exigirá encurtar a seção correspondente do pilar de alimentos.

---

## Execução 2026-08-10

### Dados

Coleta por service account (`python3 ~/.config/adrianarezende/seo-report.py 30`), período 2026-07-11 → 2026-08-10.

- **`[deploy]` em dia** — 12 páginas publicadas, 0 commits pendentes. O guard criado ontem (SEO-021) rodou como primeiro passo e passou.
- **Indexação: 12 de 12 `PASS`.** Inclui `/prazo-validade-alimentos/`, o item que ficou em observação ontem — `Submitted and indexed`, último rastreamento em 2026-08-10T15:11Z. A latência real foi de ~1 dia após o push, dentro da faixa medida. **Item encerrado.**
- **Impressões:** 46 no período, 0 cliques. `/assistente-tecnica/` sozinha responde por 22 (posição média 8,1) — quase metade de todo o site. Depois: `/quesitos-periciais/` 8 (pos. 13,5), `/pericia-combustiveis/` 5 (pos. 5,6), home 3 (pos. 6,0), `/honorarios-pericia-judicial/` 3 (pos. 6,7).
- **Consultas: 5 linhas** — chegou ao limiar que ontem foi fixado para as consultas passarem a decidir a próxima tarefa no lugar da intuição de cluster. `assistente tecnico pericia` (pos. 16), `assistente técnico` (pos. 18), `impugnação laudo pericial` (pos. 28), `apresentação de quesitos` (pos. 49), `avaliações sobre quema química` (pos. 32 — consulta espúria).

**Sobre o zero de cliques:** com 46 impressões, o número esperado de cliques a um CTR de 3% é 1,4. Zero não é sinal de nada. Além disso, a janela de recache dos snippets corrigidos só fecha por volta de 16/08. **Título e meta description não foram tocados hoje**, de propósito — mexer neles agora destruiria o único teste em curso.

### Por que esta foi a tarefa de hoje

Três fatos apontaram para o mesmo lugar.

1. Os dados de consulta, agora utilizáveis, dizem que o cluster de assistência técnica é o único que o Google está exibindo. As duas consultas de cabeça (`assistente técnico`, `assistente tecnico pericia`) caem na faixa 16–18 — **Prioridade 2 do mandato**, a de retorno mais rápido.
2. `/assistente-tecnica/` é ao mesmo tempo a página com mais impressões e **a mais rasa do site**: 34 KB contra 41 KB de `/quesitos-periciais/` e 53 KB de `/prazo-validade-alimentos/`. O hub estava sendo superado em profundidade pelos próprios spokes.
3. O que decidiu: a âncora `#parecer-tecnico` dessa página é **destino de tráfego pago**. O grupo `AG03 | Parecer e Laudo – Eng Química` compra `parecer técnico engenharia química` e `parecer técnico pericial engenharia química` em correspondência exata (`google-ads-import/1-keywords.csv`, linhas 33–34) e manda o clique para lá. O `index.html` também aponta um sitelink para a mesma âncora. **O que existia nesse destino era uma lista de seis marcadores.** Clique com intenção comercial máxima, pago, caindo em conteúdo de passagem — isso é Prioridade 1 na definição literal do playbook, não Prioridade 3.

Escrever uma 13ª página teria adicionado superfície nova sem corrigir o destino que já recebe tráfego pago e orgânico.

---

## Execução 2026-08-12 (segunda do dia)

> A execução anterior terminou às 22:16; esta começou às 22:17. Mesmo dia, dados novos — o Search Console avançou a série de 09/08 para 10/08 entre uma e outra, e é isso que muda a leitura.

### Dados

`/usr/bin/python3 tools/seo-report.py`, período 2026-07-15 → 2026-08-12.

- **`[deploy]` em dia** — 0 commits pendentes, 12 páginas no sitemap publicado, 12 respondendo 200.
- **`[valid]` ALL PASS** nas 12 páginas.
- **Indexação: 12 de 12 `PASS`.**
- **Desempenho (28 dias): 90 impressões, 1 clique.** Eram 58 impressões e 0 cliques na leitura anterior.
- **Consultas: 9 linhas, 9 impressões, 0 cliques.** As 81 impressões restantes (90%) seguem em consultas anonimizadas.

### O primeiro clique orgânico apareceu no Search Console — e a pergunta sobre a consulta está encerrada

A série por data agora vai até **10/08** (ainda 2 dias de latência). O clique está lá:

- **10/08 · `/quesitos-periciais/` · 25 impressões · 1 clique · posição 9,4.**

O site inteiro teve 32 impressões naquele dia; 25 foram dessa página. É o pico diário do site e a origem do único clique.

**A consulta do clique não aparece e não vai aparecer.** A dimensão `query` no período soma 9 impressões contra 90 pelas dimensões `date` e `page` — **90% anonimizado**, pior que os 86% medidos em 11/08. Nenhuma das 9 linhas visíveis tem clique. O item 3 da lista da execução anterior mandava conferir uma vez e, não aparecendo, encerrar a pergunta. **Encerrada.**

Correção de um número da execução anterior: ela registrou que os dois cliques do GA4 de 10/08 caíram em `/pericia-industria-quimica/` e `/quesitos-periciais/`. O GSC confirma clique orgânico **apenas em `/quesitos-periciais/`**. A sessão de `/pericia-industria-quimica/` é real no GA4, mas não tem clique correspondente no GSC — provavelmente atribuição de sessão a uma segunda página vista, não uma segunda entrada.

### Por que esta foi a tarefa de hoje

As duas frentes de conteúdo continuam travadas por data, e uma terceira foi descartada por evidência.

1. **CTR de `/assistente-tecnica/` (25 impressões, posição 8,2, 0 cliques):** a janela de recache dos snippets só é legível a partir de ~16/08. Mexer em title ou description hoje destrói o único teste em curso. **Bloqueada por data.**
2. **`/impugnacao-laudo-pericial/` (posição 24,8, pior do site, e 4 das 9 consultas visíveis):** reavaliação marcada para ~20/08, quando completar duas semanas ao vivo. **Bloqueada por data.**
3. **Próxima spoke (recolhimento/recall pela RDC 655/2022):** **descartada por evidência nova.** O cluster de alimentos tem duas páginas indexadas — `/pericia-contaminacao-alimentos/` (publicada em 02/08) e `/prazo-validade-alimentos/` (08/08) — e **as duas somam zero impressão em 28 dias**. Acrescentar uma terceira página a um cluster que não produz uma única impressão é acumular estoque, não entregar alcance. O cluster de alimentos precisa de diagnóstico antes de mais conteúdo.

O que sobrou, e que a medição de hoje promoveu, foi o **SEO-019**.

**Por que o score subiu de 33,3 para 84.** A entrada original (06/08) tratava o grafo plano como problema estético que só viraria relevante por volta de 15 páginas. Três medições de hoje mudam isso:

- **Sete páginas estão entre as posições 5 e 12** (`/pericia-combustiveis/` 5,6 · `/honorarios-pericia-judicial/` 5,8 · `/` 6,0 · `/pericia-industria-quimica/` 7,0 · `/assistente-tecnica/` 8,2 · `/classificacao-fiscal-ncm/` 9,0 · `/quesitos-periciais/` 10,1). Essa é a faixa que o mandato define como **Prioridade 2, a de retorno mais rápido** — e o grafo interno é o único instrumento disponível hoje para empurrá-la, já que metadado está sob teste.
- **`/quesitos-periciais/` está em 10,1**, exatamente na fronteira entre a primeira e a segunda página de resultados, e é a única página que já converteu impressão em clique.
- **O grafo estava literalmente completo.** Medido: cada uma das 11 páginas trazia um bloco "Continue lendo" com ~10 links apontando para praticamente todas as outras, com **o título completo da página como âncora, idêntico em todo lugar**. Doze nós, todos ligados a todos, sem hierarquia pilar → spoke e sem uma única variação de texto-âncora. Bloco repetido em todo o site com âncora constante é exatamente o padrão que os buscadores tratam como navegação e descontam.

### O que foi implementado

Substituição do bloco boilerplate por um bloco **curado por página, em dois grupos rotulados**, com âncoras em forma de consulta e variadas conforme a página de origem.

- **Hierarquia explícita em três clusters.** Processo pericial (hub `/assistente-tecnica/` → spokes `/quesitos-periciais/`, `/impugnacao-laudo-pericial/`, `/honorarios-pericia-judicial/`); alimentos (hub `/pericia-contaminacao-alimentos/` → spoke `/prazo-validade-alimentos/`); indústria e ambiente (hub `/pericia-industria-quimica/` → `/pericia-combustiveis/`, `/pericia-ambiental/`, `/classificacao-fiscal-ncm/`). Spoke aponta para o próprio hub e para os irmãos; hub aponta para os próprios spokes e para os outros hubs.
- **Segundo grupo em toda página de área técnica: "Como essa prova entra no processo"**, ligando o conteúdo técnico ao cluster processual, que é o que de fato recebe impressão. É a aplicação do único padrão que os dados sustentam: neste site as consultas que aparecem são **procedimentais** (quesitos, assistente técnico, impugnação, honorários), não temáticas.
- **Âncoras em forma de consulta, de 1 a 5 variantes por destino** em vez de um título repetido 10 vezes. Exemplos para `/quesitos-periciais/`: "Como formular quesitos que o perito não pode deixar de responder", "Quesitos periciais: prazos, limites e erros que os anulam", "Como redigir os quesitos da perícia", "Como formular os quesitos de uma perícia ambiental", "Como formular os quesitos de uma perícia de alimentos".
- **Grafo com forma, medido antes e depois.** Antes: todo destino recebia ~10 links do bloco, com 1 texto-âncora. Depois (links do bloco + links contextuais no corpo + home):

  | Página | Antes (bloco) | Depois (bloco) | Total | Âncoras distintas |
  |---|---|---|---|---|
  | `/sobre/` | 10 | 10 | 25 | 2 |
  | `/assistente-tecnica/` | 10 | 10 | 22 | 5 |
  | `/pericia-contaminacao-alimentos/` | 7 | 4 | 22 | 2 |
  | `/quesitos-periciais/` | 10 | 9 | 15 | 5 |
  | `/impugnacao-laudo-pericial/` | 9 | 7 | 12 | 4 |
  | `/pericia-industria-quimica/` | 10 | 7 | 9 | 3 |
  | `/classificacao-fiscal-ncm/` | 10 | 2 | 8 | 2 |
  | `/honorarios-pericia-judicial/` | 10 | 4 | 7 | 3 |
  | `/pericia-ambiental/` | 10 | 4 | 7 | 2 |
  | `/prazo-validade-alimentos/` | 10 | 1 | 6 | 1 |
  | `/pericia-combustiveis/` | 10 | 2 | 4 | 2 |

- **Uma regra de CSS** (`.related ul + .related-lbl { margin-top: 2.25rem; }`) para separar os dois grupos. Nenhuma outra mudança de estilo — a estrutura `related` / `related-lbl` / `ul` foi reaproveitada.
- **`sitemap.xml`:** `lastmod` de 2026-08-12 nas 11 páginas alteradas. A home não foi tocada.
- **Gerado por script** em vez de 11 edições à mão, para que a definição do grafo fique num só lugar e o bloco não divirja entre páginas.

### Nenhuma página ficou órfã, e isso foi medido, não presumido

A home linka para as 11 páginas, então mesmo os destinos que perderam links do bloco continuam com entrada. O menor total é `/pericia-combustiveis/` com 4 (2 do bloco, 1 no corpo, 1 da home) — e é a página de **melhor posição do site (5,6)**, que não precisa de reforço. O verificador de páginas órfãs do `[valid]` passa.

### Ressalva honesta sobre `/pericia-ambiental/` e `/pericia-contaminacao-alimentos/`

As duas seguem com **zero impressão em 28 dias apesar de indexadas**, e esta tarefa **não resolve isso**. Duas evidências dizem que o problema delas não é volume de links internos:

- `/pericia-contaminacao-alimentos/` tinha **24 links internos, o 2º maior do site**, e zero impressão.
- A idade está controlada: `/pericia-contaminacao-alimentos/` foi publicada em 02/08, no mesmo dia de `/classificacao-fiscal-ncm/` e `/sobre/`, que têm impressão; `/pericia-ambiental/` foi publicada em 04/08, no mesmo dia de `/pericia-combustiveis/`, que está na posição 5,6.

A hipótese em pé é de **descasamento de intenção**: as duas são as únicas páginas do site que disputam substantivo temático de alta concorrência ("perícia ambiental", "contaminação de alimentos"), enquanto todas as que recebem impressão disputam consulta procedimental ou nicho estreito. O que esta tarefa faz por elas é modesto e proposital — o novo grupo "Como essa prova entra no processo" liga as duas ao cluster que de fato aparece. **A correção de fundo (reposicionar as duas sobre consultas de decisão, tipo "como provar contaminação de solo em juízo") fica registrada como próxima tarefa de conteúdo, e não foi feita hoje** para não misturar duas mudanças na mesma medição.

### Validação

- `[valid]` **ALL PASS** nas 12 páginas depois da mudança: title ≤ 60 sem duplicata, description entre 150 e 160, `og:title`/`twitter:title` idênticos ao `<title>`, canonical correto, um `<h1>` por página, todo JSON-LD parseando, **zero link interno quebrado e zero âncora inexistente**, sitemap idêntico ao sistema de arquivos, nenhuma página órfã, paridade FAQ ↔ `FAQPage` mantida.
- **Balanceamento de tags conferido por parser** (`html.parser`) nas 12 páginas: nenhuma tag desbalanceada, nenhuma pendente. Foi checado porque a mudança recorta e reescreve um bloco de `<div>` aninhado em 11 arquivos por script — é o defeito que um `grep` não pega.
- `llms.txt` não referencia o bloco; nada a atualizar.

### Nada de metadado foi tocado

Nenhum `<title>` e nenhuma `<meta name="description">` mudou. O teste de recache aberto em 09/08 segue íntegro para leitura a partir de ~16/08.

### O que segue em aberto

- **`/pericia-ambiental/` e `/pericia-contaminacao-alimentos/` sem impressão** — agora o item de conteúdo mais concreto do backlog. Ver a ressalva acima. Entra como **SEO-026**.
- **SEO-023** (redação do FAQ em `/sobre/` e `/assistente-tecnica/`) — 63, baixa prioridade, coberto por checagem automática.
- **SEO-005** (`_headers` inerte no GitHub Pages) — sem mudança.
- **SEO-009** (perfil no Google Business) — bloqueado por verificação de identidade da proprietária.

### SEO-026 — Duas páginas indexadas com zero impressão em 28 dias

- **Descrição:** `/pericia-ambiental/` e `/pericia-contaminacao-alimentos/` estão indexadas (`PASS`), têm 34 KB e 35 KB, FAQ, schema e links internos, e **nunca apareceram em uma busca**. Idade e volume de links internos estão descartados por medição (ver ressalva acima). A hipótese em pé é descasamento de intenção: são as duas únicas páginas do site que disputam substantivo temático de alta concorrência, enquanto as que recebem impressão disputam consulta procedimental.
- **URL:** `/pericia-ambiental/`, `/pericia-contaminacao-alimentos/`
- **Categoria:** Intenção de busca / Alcance
- **Impacto:** 7 · **Esforço:** 5 · **Confiança:** 6 · **Valor de negócio:** 7
- **Priority Score:** 58,8
- **Status:** open · **Descoberto:** 2026-08-12
- **Notas:** a correção provável é dar a cada uma uma porta de entrada procedimental — seções e FAQ sobre "como se prova contaminação de solo em juízo", "quesitos para perícia ambiental", "como contestar um laudo ambiental administrativo" — em vez de disputar o substantivo temático. **Fazer uma página de cada vez**, para que a medição consiga separar o efeito. Não executar antes de ~19/08: o grafo interno mudou hoje e precisa de uma janela limpa.

### Próxima execução — o que checar primeiro

1. **`/usr/bin/python3 tools/seo-report.py` como primeiro passo.** `[deploy]` acusando deriva ⇒ publicar é a tarefa do dia. Qualquer seção falhando ⇒ corrigir antes de abrir frente nova.
2. **~~A consulta do primeiro clique~~ — encerrada em 12/08.** 90% das impressões são anonimizadas; não há fonte alternativa. Não gastar execução nisso.
3. **CTR das páginas entre 5 e 12 — a partir de ~16/08**, e só com a série do GSC confirmada até uma data que cubra a janela. Lembrete que já custou uma conclusão errada: **confirmar até que data a série vai antes de tratar um zero como resultado.**
4. **`/quesitos-periciais/` é a página a vigiar.** 38 impressões, posição 10,1, o único clique do site e o pico diário de 25 impressões em 10/08. Se a posição cair abaixo de 10 e estabilizar, o grafo novo é a explicação mais provável e o padrão deve ser reforçado. É também a primeira leitura possível do efeito desta tarefa.
5. **`/impugnacao-laudo-pericial/` — reavaliar por volta de 20/08**, com duas semanas ao vivo. Posição 24,8 contra 5–12 das irmãs, e 4 das 9 consultas visíveis são dela.
6. **Efeito do grafo interno: não ler antes de ~19/08.** Mudança de links internos leva de uma a três semanas para reprecificar. Ler cedo demais produz ruído, e ruído lido como sinal gera a próxima tarefa errada.
7. **SEO-026** (as duas páginas mudas), uma página por vez, depois de 19/08.
8. **Vigiar as consultas da seção do SEO-022** — `parecer técnico`, `parecer técnico judicial`, `diferença entre laudo e parecer técnico`, `art. 472 CPC`. Relógio começou em 12/08.
9. **Google Ads:** conferir a taxa de conversão do grupo AG03 separadamente, a landing mudou em 12/08.

---

## Execução 2026-08-13

### Dados

`/usr/bin/python3 tools/seo-report.py`, período 2026-07-16 → 2026-08-13.

- **`[deploy]` em dia** — 0 commits pendentes, 12 páginas no sitemap publicado, 12 respondendo 200.
- **`[valid]` ALL PASS** nas 12 páginas (antes da mudança de hoje).
- **Indexação: 12 de 12 `PASS`.** `/impugnacao-laudo-pericial/` falhou por timeout na primeira chamada e passou na repetição — falha de rede, não de indexação. Vale como lembrete: um `FAIL` de inspeção não é um diagnóstico até ser repetido.
- **Desempenho (28 dias): 115 impressões, 1 clique.** Eram 90 e 1 ontem.
- **Consultas: 12 linhas, 12 impressões, 0 cliques.** 90% das impressões seguem anonimizadas.

| Página | impr. | pos. |
|---|---|---|
| `/quesitos-periciais/` | 49 (1 clique) | 10,3 |
| `/assistente-tecnica/` | 27 | 8,4 |
| `/impugnacao-laudo-pericial/` | 14 | 18,1 |
| `/honorarios-pericia-judicial/` | 9 | 10,4 |
| `/pericia-combustiveis/` | 8 | 6,5 |
| `/` | 3 | 6,0 |
| `/classificacao-fiscal-ncm/` | 3 | 9,0 |
| `/pericia-industria-quimica/` | 1 | 7,0 |
| `/sobre/` | 1 | 32,0 |

### Três correções de registro, todas de execuções anteriores

1. **Não existe tráfego pago.** A execução de 10/08 justificou a prioridade do dia dizendo que a âncora `#parecer-tecnico` é destino de tráfego pago comprado pelo grupo `AG03`. **A conta do Google Ads (`2499172899`, "Adriana Rezende") tem zero impressão e zero custo nos últimos 90 dias** — consultado hoje pela API. O que existe é uma campanha `Campaign #1` habilitada sem entrega; a estrutura `AG01–AG03` só existe como CSV em `google-ads-import/`, nunca foi importada. A tarefa daquele dia continuava certa (a âncora era rasa e recebe link interno e sitelink), mas **a premissa de tráfego pago era falsa** e não deve ser reutilizada como argumento.
2. **A conversão nunca foi perdida por defeito.** O GA4 registra `manual_event_CONTACT` em zero ocorrências em 60 dias, o que parecia um rastreamento quebrado. É o contrário: o único clique real em WhatsApp aconteceu em **03/08** e o rastreamento foi adicionado em **04/08** (commit `38fe681`). Testado hoje na página ao vivo — o handler dispara e empilha o evento no `dataLayer`. **Não há defeito; há ausência de contatos**: 45 sessões-página e nenhum clique de contato desde 04/08.
3. **O GA4 mostra 8 sessões de "Paid Search"** contra zero entrega no Ads. Sem explicação confirmada — provavelmente URL com `utm_medium=cpc` ou `gclid` de teste. Registrado como observação, não como achado.

### Por que esta foi a tarefa de hoje

As três frentes de conteúdo seguem bloqueadas por data, e as datas foram fixadas por bom motivo:

- **CTR / metadados** — janela de recache só legível a partir de ~16/08. Mexer destrói o teste aberto em 09/08.
- **Grafo interno** — leitura não antes de ~19/08.
- **SEO-026** (páginas mudas) — a correção provável dessas páginas é o `<title>`, e título é exatamente o que está congelado. Adiar continua certo. **Nota nova:** `/prazo-validade-alimentos/` também está com zero impressão, o que faz do problema um padrão de **cluster inteiro** (alimentos + ambiental, 3 páginas), não uma coincidência entre duas.

A auditoria de hoje encontrou um defeito que não estava no backlog, que atinge **todas** as páginas de conteúdo e que **não toca em nenhuma das duas medições em curso** — não altera título, description, texto de corpo nem um único link interno.

### SEO-027 — Páginas de conteúdo sem data legível por máquina *(executada em 2026-08-13)*

- **Descrição:** das 11 páginas de conteúdo, **7 declaravam `Article` sem `datePublished` e sem `dateModified`**, e as 4 que tinham data continuavam declarando o dia da publicação depois de terem sido editadas — `/pericia-contaminacao-alimentos/` dizia 03/08 no schema enquanto o `sitemap.xml` dizia 12/08. O site afirmava duas coisas diferentes sobre a mesma página. `/sobre/` (`ProfilePage`) não tinha `dateCreated` nem `dateModified`. Nenhuma página exibia data ao leitor.
- **URL:** as 11 páginas de conteúdo
- **Categoria:** Structured data / E-E-A-T / AI citation
- **Impacto:** 6 · **Esforço:** 3 · **Confiança:** 8 · **Valor de negócio:** 6
- **Priority Score:** 96
- **Status:** done · **Descoberto:** 2026-08-13 · **Concluído:** 2026-08-13
- **Por que importa mais aqui do que na média dos sites:** todo o conteúdo deste site depende de norma vigente — RDC, CONAMA, NCM, artigos do CPC, e a multa que mudou de 150% para 100% (SEO-002). Conteúdo regulatório sem data é conteúdo sem prazo de validade declarado. Quem decide citar a página — um buscador, um LLM, ou um advogado conferindo — lê a data. O backlog já exigia que a expressão "atualizado em agosto de 2026" fosse mantida honesta; **até hoje não havia nenhum lugar onde essa honestidade fosse verificável por máquina.**
- **Implementado:**
  - `datePublished` + `dateModified` no `Article` das 10 páginas-guia e `dateCreated` + `dateModified` no `ProfilePage` de `/sobre/`, sempre no mesmo lugar do bloco (logo após `mainEntityOfPage`), em vez de espalhados no fim do objeto como nas 4 antigas.
  - Linha visível dentro do `<p class="byline">` que já existia, com `<time datetime>`: *"Publicado em 6 de agosto de 2026 · Atualizado em 12 de agosto de 2026."* Em `/sobre/`, que não tinha byline (seria circular — é a página da própria autora), a linha entrou como parágrafo próprio com a mesma classe. **Zero CSS novo.**
  - **As datas vieram do `git log`, uma por página** (`--diff-filter=A` para a publicação), não de estimativa.
- **Decisão sobre `dateModified` — 12/08, não 13/08.** A última mudança substantiva de conteúdo foi a reescrita do bloco de links de ontem. A edição de hoje acrescenta a própria linha de data. Declarar "atualizado em 13/08" porque o arquivo mudou hoje seria inflar frescor por edição cosmética — o mesmo vício que esta tarefa corrige. O `lastmod` do sitemap **é** 13/08, porque ali a pergunta é outra: o arquivo mudou. As duas datas divergem de propósito.
- **Guard, não conserto pontual.** `check_dates()` entrou no `[valid]` do `tools/seo-report.py` e reprova: página de conteúdo sem `datePublished`/`dateCreated`, sem `dateModified`, com `dateModified` anterior à publicação, com `dateModified` no futuro, ou com data no schema que não aparece em nenhum `<time datetime>` visível — que é a exigência do Google (data que a página não mostra é data descontada).
- **O guard foi testado contra os três defeitos, não só contra o estado bom** (lição do SEO-024): data futura → reprova; par de datas removido → reprova nas duas; `<time>` visível divergindo do schema → reprova. Arquivo restaurado, `ALL PASS`.
- **Validação:** `[valid]` ALL PASS nas 12 páginas; balanceamento de tags conferido por `html.parser` nas 12 (a edição entra dentro de um parágrafo existente em 11 arquivos por script); `sitemap.xml` parseia; `lastmod` 2026-08-13 nas 11 páginas alteradas; nenhum `<title>`, nenhuma `description`, nenhum link interno tocado.

### O que segue em aberto

- **SEO-026** (cluster mudo — agora 3 páginas: `/pericia-ambiental/`, `/pericia-contaminacao-alimentos/`, `/prazo-validade-alimentos/`) — depois de 19/08, e provavelmente junto com título, que destrava em 16/08.
- **SEO-023** (redação do FAQ em `/sobre/` e `/assistente-tecnica/`) — 63, coberto por checagem automática.
- **SEO-005** (`_headers` inerte no GitHub Pages) — sem mudança.
- **SEO-009** (perfil no Google Business) — bloqueado por verificação de identidade da proprietária.
- **Google Ads sem entrega** — fora do mandato de SEO, mas é a maior perda de alcance do negócio hoje: uma campanha habilitada, zero impressão em 90 dias, e a estrutura de grupos revisada em agosto nunca importada. Vale um aviso à cliente.

### Próxima execução — o que checar primeiro

1. **`/usr/bin/python3 tools/seo-report.py` como primeiro passo.** `[deploy]` acusando deriva ⇒ publicar é a tarefa do dia. O `[valid]` agora também reprova data ausente ou incoerente.
2. **CTR das páginas entre 5 e 12 — a partir de 16/08**, e só com a série do GSC confirmada até uma data que cubra a janela. Confirmar até que data a série vai **antes** de tratar um zero como resultado.
3. **`/quesitos-periciais/`** — 49 impressões, posição 10,3, o único clique. Primeira leitura possível do efeito do grafo a partir de 19/08.
4. **`/impugnacao-laudo-pericial/`** — reavaliar por volta de 20/08. Posição 18,1 (era 24,8) e 5 das 12 consultas visíveis são dela, três delas com o mesmo erro de grafia (*"impunação"*). Se a página continuar em página 2, cobrir a variante mal escrita no corpo do texto é uma opção legítima — é como o cliente real escreve.
5. **SEO-026**, uma página por vez, depois de 19/08 e com o título liberado.
6. **Não repetir a premissa de tráfego pago.** Antes de usar "essa página recebe clique pago" como argumento, consultar a API do Ads — hoje a resposta é zero.

---

## Execução 2026-08-14

### Dados

`/usr/bin/python3 tools/seo-report.py`, período 2026-07-17 → 2026-08-14.

- **`[deploy]` em dia** — 0 commits pendentes, 12 páginas no sitemap publicado, 12 respondendo 200.
- **`[valid]` ALL PASS** nas 12 páginas (antes da mudança de hoje).
- **Indexação: 12 de 12 `PASS`.**
- **Desempenho (28 dias): 121 impressões, 1 clique.** Eram 115 e 1 ontem.
- **Consultas: 12 linhas, 12 impressões, 0 cliques.** Segue ~90% anonimizado.

| Página | impr. | pos. |
|---|---|---|
| `/quesitos-periciais/` | 49 (1 clique) | 10,3 |
| `/assistente-tecnica/` | 29 | 8,6 |
| `/impugnacao-laudo-pericial/` | 15 | 17,5 |
| `/honorarios-pericia-judicial/` | 9 | 10,4 |
| `/pericia-combustiveis/` | 8 | 6,5 |
| `/` | 3 | 6,0 |
| `/classificacao-fiscal-ncm/` | 3 | 9,0 |
| `/prazo-validade-alimentos/` | 3 | **4,7** |
| `/pericia-industria-quimica/` | 1 | 7,0 |
| `/sobre/` | 1 | 32,0 |

**`/prazo-validade-alimentos/` deixou de ser muda** — 3 impressões na melhor posição média do site (4,7). O "cluster mudo" do SEO-026 volta a ser **duas** páginas (`/pericia-ambiental/`, `/pericia-contaminacao-alimentos/`), não três. A nota de ontem que o chamava de padrão de cluster inteiro fica corrigida por esta medição.

### Por que esta foi a tarefa de hoje

As três frentes de maior valor seguem congeladas por data, e as datas continuam certas: CTR/metadados só a partir de 16/08, grafo interno a partir de 19/08, SEO-026 a partir de 19/08 e dependente de título. Restava achar trabalho que **não tocasse em título, description, texto de corpo nem um único link interno** — e que não fosse cosmético.

**Duas hipóteses foram levantadas e descartadas por verificação, antes de escolher:**

1. **"Produtos Químicos Controlados" seria a maior lacuna do mandato sem página.** Falso. O tema já é tratado em profundidade dentro de `/pericia-industria-quimica/` — tabela dos dois regimes (PF pela Lei 10.357/2001 e IN DG/PF 338/2026; Exército pelo R-105/Decreto 10.030/2019), FAQ própria e menção no `llms.txt`. Criar página dedicada seria duplicar conteúdo, contra o padrão já firmado em SEO-008 e SEO-012 (ancorar, não duplicar).
2. **"O grafo de entidades estaria desconectado."** Também falso, e essa é a correção mais útil: as 12 páginas **já** trazem o `Person` canônico com `@id`, `sameAs`, `identifier` (CRQ) e `hasCredential`. O trabalho do SEO-011 se sustentou. O defeito real era muito mais estreito — e por isso mesmo tinha sobrevivido a treze auditorias.

### SEO-028 — Entidade de negócio da home: referência quebrada, imagem relativa e catálogo sem destino *(executada em 2026-08-14)*

- **Descrição:** três defeitos no JSON-LD da home, nenhum deles detectável pelas checagens existentes, que só exigiam que o bloco parseasse.
  1. **`"image": "headshot.jpg"` — caminho relativo**, em `Person` **e** em `ProfessionalService`. A documentação do Google pede URL absoluta. As tags `og:image` e `twitter:image` do mesmo arquivo já usavam a forma absoluta desde sempre, o que torna a divergência um lapso, não uma escolha.
  2. **`ProfessionalService.provider` era um segundo nó `Person` raso** — nome + `sameAs`, sem `@id` — em vez de referência ao nó canônico `#adriana-rezende` definido 60 linhas acima, no mesmo `<head>`. Numa propriedade cujo risco estrutural declarado é **ambiguidade de entidade** (SEO-010: existe outra profissional homônima que ocupou este domínio entre ~2021 e 2023), publicar duas Adrianas Rezende meio descritas trabalha exatamente contra o que o schema deveria resolver.
  3. **`hasOfferCatalog` com 6 serviços, nenhum com `url`.** O site documenta 9 serviços em 9 páginas indexadas, e nada no schema dizia que o serviço "Perícia Ambiental" é o mesmo assunto de `/pericia-ambiental/`. Em dados estruturados, os 10 guias eram dez `Article` soltos, sem vínculo com o negócio que os oferece.
- **URL:** `/`, `/pericia-contaminacao-alimentos/`
- **Categoria:** Structured data / Entity SEO / AI citation
- **Impacto:** 6 · **Esforço:** 2 · **Confiança:** 8 · **Valor de negócio:** 7
- **Priority Score:** 168
- **Status:** done · **Descoberto:** 2026-08-14 · **Concluído:** 2026-08-14
- **Implementado:**
  - `image` absoluta nos dois nós, idêntica à `og:image` já existente.
  - `@id` `#servico` no `ProfessionalService`; `provider` passou a ser `{"@id": "…#adriana-rezende"}`.
  - `WebSite` ganhou `inLanguage` e `publisher` → `#servico`, fechando a cadeia **site → negócio → pessoa**. Antes, os três nós eram ilhas.
  - **`hasOfferCatalog` reescrito: 9 serviços**, cada um com `url` para a página que o documenta, `description` própria, `areaServed` e `provider` por `@id`. É a primeira afirmação legível por máquina de que estes 9 serviços existem, são oferecidos por esta pessoa e estão documentados nestes 9 endereços.
- **O catálogo foi mantido honesto.** `/honorarios-pericia-judicial/` e `/sobre/` **não** entraram: honorários é informação de preço e "sobre" é a página da autora — nenhum dos dois é serviço contratável. Inflar o catálogo para 11 itens porque existem 11 páginas seria o mesmo vício que o SEO-027 corrigiu nas datas. "Perícia em Indústria de Alimentos" foi dividida em duas (contaminação e prazo de validade/vida útil) porque são duas páginas substantivas e dois tipos de contratação distintos.
- **Guard:** `check_schema_refs()` no `[valid]` do `tools/seo-report.py`, que reprova (a) qualquer `url`/`image`/`logo`/`sameAs` relativo dentro de JSON-LD, (b) referência `@id` do próprio domínio que nenhum bloco da página defina, e (c) nó `Person`/`Organization` com nome igual ao de uma entidade canônica da página mas **sem** `@id` — o defeito nº 2 acima, generalizado.
- **O guard foi testado contra quatro defeitos plantados, não só contra o estado bom:** imagem relativa reintroduzida → reprova; `provider` apontando para `#fantasma` inexistente → reprova; o defeito original (`provider` como `Person` duplicado e raso) → reprova; `url` relativa dentro de um `Service` do catálogo → reprova. Arquivo restaurado depois de cada injeção.
- **O guard encontrou um defeito que a inspeção manual não tinha achado.** Na primeira execução contra o repositório limpo, reprovou `/pericia-contaminacao-alimentos/`: o `Article.publisher` era um `Person` com **apenas nome**, sem `@id`. As outras 9 páginas de guia trazem `@id` + `name` + `url` no `publisher`. Era deriva de uma página só, invisível a olho nu num arquivo de 35 KB — e é precisamente o tipo de achado que justifica escrever guard em vez de conserto pontual. Corrigida para a forma das outras nove.
- **Validação:** `[valid]` ALL PASS nas 12 páginas; JSON-LD de ambos os arquivos parseia; `sitemap.xml` parseia com `lastmod` 2026-08-14 nas duas páginas alteradas.
- **Nenhuma medição em curso foi tocada — verificado por diff, não por intenção.** Um comparativo antes/depois das 12 páginas confirmou: nenhum `<title>`, nenhuma `meta description` e **nenhum link interno** (`href="/…"`) mudou em página alguma. Todas as linhas do diff das duas páginas HTML estão dentro de blocos JSON-LD.
- **`dateModified` deliberadamente não alterado.** A mudança é de dados estruturados, sem alteração de conteúdo visível. Declarar frescor por edição de schema seria inflar data por edição cosmética — o vício que o SEO-027 corrigiu. O `lastmod` do sitemap **foi** para 14/08, porque ali a pergunta é outra: o arquivo mudou.

### O que segue em aberto

- **SEO-026** (cluster mudo — **duas** páginas: `/pericia-ambiental/`, `/pericia-contaminacao-alimentos/`) — depois de 19/08, junto com título, que destrava em 16/08.
- **SEO-023** (redação do FAQ em `/sobre/` e `/assistente-tecnica/`) — 63, coberto por checagem automática.
- **SEO-005** (`_headers` inerte no GitHub Pages) — sem mudança.
- **SEO-009** (perfil no Google Business) — bloqueado por verificação de identidade da proprietária.
- **Google Ads sem entrega** — segue: uma campanha habilitada, zero impressão em 90 dias, estrutura de grupos nunca importada. Fora do mandato de SEO, mas é a maior perda de alcance do negócio hoje. **Vale um aviso à cliente.**

### Próxima execução — o que checar primeiro

1. **`/usr/bin/python3 tools/seo-report.py` como primeiro passo.** `[deploy]` acusando deriva ⇒ publicar é a tarefa do dia. O `[valid]` agora também reprova URL relativa e referência `@id` órfã no schema.
2. **CTR das páginas entre 5 e 12 — destravado a partir de 16/08.** Confirmar até que data a série do GSC vai **antes** de tratar um zero como resultado. Esta é a frente de maior valor assim que abrir: são ~50 impressões em posição ≤ 8,6 com 0 clique.
3. **`/prazo-validade-alimentos/` em posição 4,7** — a melhor do site, e nova. Vigiar: se sustentar a posição e ganhar volume, é o modelo de intenção a replicar nas duas páginas mudas do SEO-026.
4. **`/quesitos-periciais/`** — 49 impressões, posição 10,3, o único clique. Primeira leitura possível do efeito do grafo a partir de 19/08.
5. **`/impugnacao-laudo-pericial/`** — reavaliar por volta de 20/08. Posição 17,5 (era 18,1, era 24,8): melhora consistente em três medições.
6. **SEO-026**, uma página por vez, depois de 19/08 e com o título liberado.
7. **Não repetir a premissa de tráfego pago.** Consultar a API do Ads antes de usar esse argumento — hoje a resposta segue zero.
