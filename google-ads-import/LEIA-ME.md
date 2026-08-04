# Como aplicar as correções — conta 249-917-2899

> **Importante:** eu não consegui aplicar nada diretamente. Os conectores de Google Ads
> desta sessão são **somente leitura** (só `search` e `metadata`; nenhuma ferramenta de
> escrita/mutate). Estes arquivos existem para você aplicar em minutos em vez de horas.

---

## ⚠️ ORDEM IMPORTA — faça o Passo 0 primeiro

O Google Ads Editor **casa registros pelo nome**. Se a campanha ainda se chamar
`Campaign #1` quando você importar os CSVs, o Editor **criará uma campanha nova**
em vez de atualizar a existente. Renomeie antes.

---

## Passo 0 — Renomear (2 minutos, na interface web)

| De | Para |
|---|---|
| `Campaign #1` | `Search \| High Intent \| BR` |
| `Ad group 1` | `AG01 \| Perita Judicial – Eng Química` |

---

## Passo 1 — 🔴 Correções críticas ANTES de servir qualquer impressão

Nenhuma delas está nos CSVs — todas são configuração, feitas na interface.

### 1.1 Trocar a estratégia de lances
`Campanha → Configurações → Lances` → mudar de **Maximizar conversões** para
**CPC manual**, com lance padrão de **R$ 25–40**.
*Motivo: Smart Bidding com zero conversões de histórico gasta o orçamento explorando.*

### 1.2 Reduzir o orçamento
`Campanha → Orçamento` → de **R$ 184,75** para **R$ 120/dia** nos primeiros 30 dias.

### 1.3 Corrigir a contagem da conversão
`Ferramentas → Conversões → manual_event_CONTACT → Editar configurações → Contagem`
→ mudar de **Todas (Every)** para **Uma (One)**.
*Motivo: existem 3+ gatilhos de WhatsApp só na home. Um visitante indeciso pode
disparar 3 conversões e inflar o número que o bidding usa para aprender.*

### 1.4 Deixar só uma conversão primária
`Ferramentas → Conversões` → manter **apenas `manual_event_CONTACT`** como primária.
Rebaixar `SUBMIT_LEAD_FORM` e `Lead form - Submit` para **secundária**
(as duas nem contam para a métrica de conversões hoje — são ruído).

### 1.5 Pausar as keywords em Broad do AG01
As 9 keywords atuais estão em **Broad Match**. O arquivo `1-keywords.csv` já traz as
mesmas em Exact/Phrase. Depois de importar, **pause as 9 originais em Broad**.

### 1.6 Segmentação por presença
`Campanha → Configurações → Locais → Opções de local` →
selecionar **"Presença: pessoas que estão no local incluído"**
(o padrão inclui "interesse", que traz curioso de fora do Brasil).

### 1.7 Desmarcar redes
`Campanha → Configurações → Redes` → desmarcar **Rede de Display** e
**Parceiros de pesquisa** no lançamento.

---

## Passo 2 — Importar os CSVs (Google Ads Editor)

`Conta → Importar → Importar de arquivo`, um de cada vez, **nesta ordem**:

| Ordem | Arquivo | Conteúdo |
|---|---|---|
| 1 | `2-negative-keywords.csv` | **382 negativas** — importe primeiro, é a rede de proteção |
| 2 | `1-keywords.csv` | 86 keywords em Exact/Phrase, AG01–AG06 |
| 3 | `3-responsive-search-ads.csv` | 5 RSAs (AG02–AG06), 15 headlines + 4 descrições cada |
| 4 | `4-callouts.csv` | 8 callouts |
| 5 | `5-sitelinks.csv` | 6 sitelinks |
| 6 | `6-structured-snippets.csv` | 2 headers |

Revise no Editor antes de **Publicar**.

> Os ad groups AG02–AG06 são criados automaticamente pela importação das keywords.
> **AG07 (Ambiental) e AG08 (Combustíveis) ficaram de fora de propósito** — não têm
> landing page ainda. Ver §1.2 do playbook.

---

## Passo 3 — Ajustar o AG01 manualmente

O anúncio existente do AG01 aponta para a home. Trocar a **URL final** para:

```
https://adrianarezende.com.br/sobre/
```

E definir os caminhos de exibição: `Pericia` / `Eng-Quimica`.

---

## Passo 4 — Final URL Suffix (opcional, recomendado)

`Campanha → Configurações → Configurações de URL → Sufixo de URL final`:

```
utm_source=google&utm_medium=cpc&utm_campaign=search_high_intent&utm_content={creative}&utm_term={keyword}
```

> ⚠️ **Mantenha o auto-tagging (GCLID) LIGADO.** É ele que faz a importação de
> conversões do GA4 funcionar. Os UTMs são só para legibilidade nos relatórios.

---

## Conferência final antes de publicar

- [ ] Campanha e ad group renomeados (Passo 0)
- [ ] Lances em **CPC manual**
- [ ] Orçamento em **R$ 120/dia**
- [ ] `manual_event_CONTACT` em contagem **Uma**
- [ ] Só **uma** conversão primária
- [ ] **382 negativas** importadas
- [ ] 9 keywords Broad originais **pausadas**
- [ ] Cada ad group aponta para **sua** landing page
- [ ] Rede de Display e parceiros **desmarcados**
- [ ] Segmentação por **presença**

---

## Depois do lançamento

**Dias 1–7:** relatório de termos de busca **todo dia**. Toda busca irrelevante vira
negativa no mesmo dia. É a fase em que mais se economiza dinheiro.

**Próximo passo de maior impacto:** implementar o *offline conversion import* (§11 do
playbook) — capturar o `gclid` na mensagem do WhatsApp para o bidding otimizar para
**lead qualificado** em vez de clique em botão. Posso implementar a parte do site
quando você quiser.
