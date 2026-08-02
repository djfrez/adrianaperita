# SEO Backlog — adrianarezende.com.br

Priority Score = (Impact × Confidence × Business Value) ÷ Effort

Status: `open` · `in progress` · `done` · `blocked`

---

## Contexto do site (auditoria de 2026-08-01)

- Site estático de **uma única URL** (`/`), hospedado no **GitHub Pages** (confirmado via header `server: GitHub.com`).
- Metadados, Open Graph, canonical, hreflang, robots.txt, sitemap.xml e llms.txt já existem e estão corretos.
- Schema já presente na home: `Person`, `ProfessionalService`, `FAQPage`, `BreadcrumbList`.
- Imagens já em WebP com `width`/`height` e preload do LCP.
- Sem acesso a Google Search Console nesta execução (não autenticado) — priorização feita por intenção comercial e cobertura semântica, não por dados de impressão.

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
- **Status:** blocked
- **Descoberto:** 2026-08-01
- **Bloqueio:** exige autenticação do proprietário (OAuth). Não é executável em sessão não interativa. **É o item de maior score do backlog e deve ser feito manualmente pelo cliente.**

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

---

## Histórico de execuções

| Data | Item executado | Commit |
|---|---|---|
| 2026-08-01 | SEO-001 — página-pilar `/assistente-tecnica/` | `SEO: Add Assistente Técnico pillar page` |
