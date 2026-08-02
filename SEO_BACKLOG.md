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
4. **Inconsistência de E-E-A-T no llms.txt** — dizia "8 anos de experiência" enquanto o site diz "+20 anos técnicos / +8 anos em perícia". (corrigido em 2026-08-01)

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
- **URL:** `/classificacao-fiscal-ncm/` (a criar)
- **Categoria:** Conteúdo / Autoridade tópica
- **Impacto:** 9 · **Esforço:** 4 · **Confiança:** 8 · **Valor de negócio:** 9
- **Priority Score:** 162
- **Status:** open
- **Descoberto:** 2026-08-01

### SEO-003 — Página-pilar: Perícia em Contaminação Alimentar
- **Descrição:** Metodologia de investigação de contaminação (física, química, biológica), cadeia de custódia, normas ANVISA aplicáveis, BPF/APPCC, recall e apuração de responsabilidade.
- **URL:** `/pericia-contaminacao-alimentos/` (a criar)
- **Categoria:** Conteúdo / Autoridade tópica
- **Impacto:** 8 · **Esforço:** 4 · **Confiança:** 8 · **Valor de negócio:** 9
- **Priority Score:** 144
- **Status:** open
- **Descoberto:** 2026-08-01

### SEO-004 — Página "Sobre" dedicada (E-E-A-T)
- **Descrição:** Página própria de biografia profissional com trajetória detalhada, setores atendidos, formação, normas de domínio e tipos de processo — hoje esse conteúdo está comprimido em duas seções da home. Fortalece a entidade "Adriana Rezende" para o Knowledge Graph e para citação por LLMs.
- **URL:** `/sobre/` (a criar)
- **Categoria:** E-E-A-T / Entity SEO
- **Impacto:** 7 · **Esforço:** 3 · **Confiança:** 8 · **Valor de negócio:** 8
- **Priority Score:** 149,3
- **Status:** open
- **Descoberto:** 2026-08-01

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
- **Status:** open
- **Descoberto:** 2026-08-01
- **Notas:** Alto valor de conversão, mas exige decisão do cliente sobre serviço de terceiros e privacidade dos dados enviados. Não executável de forma autônoma.

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
- **Status:** open
- **Descoberto:** 2026-08-01

### SEO-009 — Perfil no Google Business e citações locais
- **Descrição:** Nenhum sinal de perfil GBP para "perita judicial Campinas". Criar/reivindicar perfil, padronizar NAP e buscar citações (CREA-SP, associações de peritos, diretórios jurídicos).
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
- **Status:** in progress
- **Descoberto:** 2026-08-02
- **Feito em 2026-08-02:** `sameAs` com o LinkedIn (`adriana-rezende-5992554a`) adicionado ao `Person` da home, ao `provider` do `ProfessionalService` e ao `author` do Article. Corroborado por links visíveis na seção de contato e no rodapé — `sameAs` sem link real na página é sinal fraco.
- **Pendente — registro no CRQ:** confirmado que a profissional é registrada no **CRQ** (Conselho Regional de Química), conselho pertinente para perícia em composição, contaminação e classificação fiscal. Falta o **número e a região** (ex.: CRQ IV Região — SP) para publicar. Registro de conselho de classe é informação pública por construção — o próprio CRQ mantém consulta aberta — e a exibição é prática padrão em perícia, onde habilitação é pressuposto. Implementar como `hasCredential` (`EducationalOccupationalCredential`) mais menção visível junto às qualificações.
- **Ainda úteis, se existirem:** currículo Lattes, ORCID, publicações, associações de peritos.

---

## Histórico de execuções

| Data | Item executado | Commit |
|---|---|---|
| 2026-08-01 | SEO-001 — página-pilar `/assistente-tecnica/` | `SEO: Add Assistente Técnico pillar page` |
