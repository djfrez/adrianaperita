# PPC Playbook — Adriana Rezende
### Google Ads Search | Conta 249-917-2899 | Agosto 2026

---

## 0. Executive summary — leia isto antes de qualquer coisa

Auditei a conta ao vivo antes de escrever uma linha. **A boa notícia: zero impressões, zero cliques, R$ 0,00 gastos.** Nada foi desperdiçado ainda. A má notícia: do jeito que a campanha está configurada agora, ela vai queimar dinheiro assim que começar a servir.

Encontrei **cinco problemas que precisam ser corrigidos antes de qualquer ad group novo entrar no ar.** Construir mais ad groups em cima da configuração atual é construir em cima de areia.

| # | Problema encontrado ao vivo | Risco | Prioridade |
|---|---|---|---|
| 1 | **Todas as 9 keywords estão em BROAD MATCH** | Contradiz a própria regra nº 10 do briefing. Broad + zero negativas = Google vai encontrar formas de gastar R$184/dia em lixo | 🔴 Crítico |
| 2 | **Zero negativas na conta** — nenhuma, em nenhum nível | Sem rede de proteção. Ver §7: existem 3 armadilhas semânticas graves neste nicho | 🔴 Crítico |
| 3 | **Maximize Conversions com 0 conversões de histórico** | Smart bidding sem sinal nenhum gasta o orçamento inteiro "explorando". Combinado com broad match, é o pior cenário possível | 🔴 Crítico |
| 4 | **`manual_event_CONTACT` está em contagem "Every" (MANY_PER_CLICK)** | Eu instalei 3+ gatilhos de WhatsApp só na home. Um visitante pode disparar 3 conversões. O bidding vai otimizar para um número inflado | 🔴 Crítico |
| 5 | **Todos os anúncios apontam para a home** (`final_urls: ["https://adrianarezende.com.br/"]`) | Clique de R$50 em "classificação fiscal NCM" cai numa home genérica. Mata conversão e Quality Score (landing page experience) | 🟠 Alto |

**Estado atual da conta (verificado via API):**

| Campo | Valor ao vivo | Deveria ser |
|---|---|---|
| Campanha | `Campaign #1` | `Search \| High Intent \| BR` |
| Ad group | `Ad group 1` | `AG01 \| Perita Judicial – Eng Química` |
| Match types | 9× BROAD | Exact + Phrase |
| Orçamento | R$ 184,75/dia (≈R$ 5.617/mês) | R$ 120/dia nos primeiros 30 dias |
| Bidding | Maximize Conversions | Manual CPC até ~15 conversões |
| Localização | Brasil (geo 2076) ✅ | manter — mas checar "presença" vs "interesse" |
| Idioma | Português (1014) ✅ | manter |
| Negativas | **nenhuma** | 382 (ver §7) |
| Conversões primárias | **3 marcadas como primária** | 1 |

---

## 1. Desafios às premissas do briefing

Você pediu para eu desafiar premissas. Aqui vão as quatro que eu mudaria, com o raciocínio.

### 1.1 — Três dos dez ad groups sugeridos não devem ser lançados agora

A regra do próprio briefing é: *"Only keep an ad group if the website clearly supports it."* Aplicando isso com rigor:

| Ad group sugerido | Veredicto | Motivo |
|---|---|---|
| **Produtos Químicos Controlados** | ❌ **Não lançar** | Não é um card de expertise no site — aparece só como menção dentro de "Indústrias Químicas" e no `knowsAbout`. Pior: quem busca esse termo no Brasil quase sempre quer **licenciamento junto à Polícia Federal/Exército** (consultoria regulatória), que **não é o serviço da Adriana**. Intenção errada, não só página faltando. |
| **Laudos Técnicos** | ⚠️ **Fundir** com Parecer Técnico | Mesmo buscador, mesma landing page. "Laudo" é o entregável como perita judicial; "parecer" como assistente técnica — distinção que **o cliente não faz na busca**. Separar fragmenta o aprendizado de RSA sem ganho. |
| **Quesitos Periciais** | ⚠️ **Fundir** dentro de Assistente Técnica | Quesitos são um entregável da assistência técnica, não um serviço comprado isoladamente. Volume ≈ zero e alto risco informacional ("modelo de quesitos"). Mantenho as keywords, dentro do AG02. |
| **Engenharia Química** | ❌ **Não é um ad group** | "Engenharia química" sozinho é busca de **estudante**. O termo é o *qualificador* que aparece em todos os outros ad groups, não uma intenção comercial própria. |

### 1.2 — Ad group só entra no ar se tiver landing page à altura

Este é o ponto que mais impacta o retorno e que quase nenhuma estrutura de campanha respeita.

O site tinha **5 páginas** quando esta auditoria começou. **Perícia Ambiental** e **Adulteração de Combustíveis** — dois serviços reais, com card próprio na home — não tinham página de destino. Mandar um clique de R$40 de "perícia contaminação solo" para a home é pagar caro para o visitante ter que procurar, e o Google pune isso via *landing page experience* dentro do Quality Score: você paga duas vezes pelo mesmo erro.

**Resolvido em 04/08/2026.** As duas páginas foram criadas — `/pericia-ambiental/` e `/pericia-combustiveis/` — com o mesmo rigor de verificação normativa das demais. **Os 8 ad groups agora lançam juntos, em onda única.** O site passou a ter 7 páginas.

### 1.3 — O gargalo aqui não é orçamento, é volume de busca

Com Exact + Phrase em cauda longa neste nicho, **você provavelmente não conseguirá gastar R$184,75/dia.** A campanha vai ser limitada por volume, não por verba.

Isso muda a leitura de tudo: o risco não é "acabar o orçamento cedo", é **o Google encontrar formas criativas de gastar a verba** quando você deixa broad match aberto. Corrigir match type é o que realmente controla o gasto aqui — o número do orçamento é secundário.

### 1.4 — A conversão atual mede clique, não lead qualificado

`manual_event_CONTACT` dispara quando alguém **clica** para abrir o WhatsApp. Não sabemos se a pessoa mandou mensagem, nem se era um advogado com um caso real ou um estudante curioso.

Otimizar Smart Bidding para esse sinal ensina o Google a buscar **cliques em botão de WhatsApp** — não clientes. Em §11 há a correção: capturar o `gclid` dentro da mensagem do WhatsApp e fazer *offline conversion import* dos leads que a Adriana qualificar. **Esta é a melhoria de maior alavancagem do plano inteiro.**

---

## 2. Estrutura de campanha e convenção de nomes

### Convenção de campanha
```
Search | <Intenção> | <País>
```
Exemplos: `Search | High Intent | BR` · `Search | Brand | BR`

### Convenção de ad group
```
AG<nn> | <Serviço> – <Qualificador>
```
Prefixo numérico mantém ordenação estável na interface e nos relatórios.

### Estrutura recomendada

**Campanha única: `Search | High Intent | BR`** (conforme briefing — orçamento compartilhado)

| Ad group | Landing page | Onda | Status |
|---|---|---|---|
| `AG01 \| Perita Judicial – Eng Química` | `/sobre/` | 1 | **já existe** — corrigir, não recriar |
| `AG02 \| Assistente Técnica – Eng Química` | `/assistente-tecnica/` | 1 | criar |
| `AG03 \| Parecer e Laudo – Eng Química` | `/assistente-tecnica/#parecer-tecnico` | 1 | criar |
| `AG04 \| Perícia Alimentos` | `/pericia-contaminacao-alimentos/` | 1 | criar |
| `AG05 \| Classificação Fiscal NCM` | `/classificacao-fiscal-ncm/` | 1 | criar |
| `AG06 \| Impugnação de Laudo` | `/assistente-tecnica/#impugnacao-laudos` | 1 | criar |
| `AG07 \| Perícia Ambiental` | `/pericia-ambiental/` | 1 | **desbloqueado** — página criada 04/08 |
| `AG08 \| Adulteração Combustíveis` | `/pericia-combustiveis/` | 1 | **desbloqueado** — página criada 04/08 |

> **Sobre AG01:** o briefing diz para não recriar. Concordo — mas ele precisa de três correções: renomear, trocar as 9 keywords de Broad para Exact/Phrase, e trocar a landing page de `/` para `/sobre/` (que é a página que responde "quem é ela e por que confiar nela" — exatamente a dúvida de quem busca "perita judicial engenharia química").

---

## 3. Ad groups — especificação completa

Legenda de match: `[exata]` · `"frase"`

---

### AG01 | Perita Judicial – Eng Química  *(existente — corrigir)*

**Objetivo:** capturar quem procura uma perita judicial nomeável em matéria de engenharia química.
**Landing page:** `https://adrianarezende.com.br/sobre/`
**Intenção de busca:** contratação / verificação de credencial. Advogado ou juízo procurando profissional habilitado.

| Keyword | Match | Por que pertence | Intenção | Conf. |
|---|---|---|---|---|
| `[perita judicial engenharia química]` | Exata | Serviço exato + disciplina exata | Contratação | Alta |
| `[perito judicial engenharia química]` | Exata | Idem, gênero masculino (busca genérica) | Contratação | Alta |
| `[perícia judicial engenharia química]` | Exata | Serviço + disciplina | Contratação | Alta |
| `[perita judicial química]` | Exata | Qualificado por disciplina | Contratação | Alta |
| `[perito judicial químico]` | Exata | Qualificado por disciplina | Contratação | Alta |
| `[engenheira química perita judicial]` | Exata | Ordem invertida, mesma intenção | Contratação | Alta |
| `[contratar perita judicial engenharia química]` | Exata | Verbo de contratação explícito | Contratação | Alta |
| `[perito judicial engenharia de alimentos]` | Exata | Disciplina que ela domina | Contratação | Alta |
| `"perito judicial em engenharia química"` | Frase | Variações com preposição | Contratação | Alta |
| `"perita judicial área química"` | Frase | Variação natural | Contratação | Alta |
| `[perito químico judicial]` | Exata | Variação de ordem | Contratação | Alta |
| `[perícia técnica engenharia química]` | Exata | Sinônimo de serviço | Contratação | Alta |
| `[especialista perícia engenharia química]` | Exata | Busca por especialista | Contratação | Alta |
| `[perito judicial indústria química]` | Exata | Setor específico dela | Contratação | Alta |
| `"perito engenheiro químico judicial"` | Frase | Variação de composição | Contratação | Alta |

---

### AG02 | Assistente Técnica – Eng Química

**Objetivo:** capturar advogado que já tem perícia nomeada e precisa indicar assistente técnico no prazo do art. 465, §1º.
**Landing page:** `https://adrianarezende.com.br/assistente-tecnica/`
**Intenção de busca:** contratação urgente, prazo correndo. **A intenção comercial mais quente de toda a conta.**

> ⚠️ **Armadilha crítica:** "assistente técnica" no Brasil significa majoritariamente **assistência técnica de eletrodoméstico/celular**. Nenhuma keyword deste grupo pode rodar sem os negativos do bloco G (§7).

| Keyword | Match | Por que pertence | Intenção | Conf. |
|---|---|---|---|---|
| `[assistente técnico engenharia química]` | Exata | Serviço + disciplina, sem ambiguidade | Contratação | Alta |
| `[assistente técnica engenharia química]` | Exata | Gênero feminino | Contratação | Alta |
| `[assistente técnico perícia engenharia química]` | Exata | Contexto pericial explícito | Contratação | Alta |
| `[assistente técnico perícia química]` | Exata | Qualificado duplamente | Contratação | Alta |
| `[contratar assistente técnico engenharia química]` | Exata | Verbo de contratação | Contratação | Alta |
| `[indicar assistente técnico perícia química]` | Exata | "Indicar" = ato processual, advogado | Contratação | Alta |
| `[assistente técnico pericial químico]` | Exata | Termo processual + disciplina | Contratação | Alta |
| `[assistente técnico perícia alimentos]` | Exata | Especialidade dela | Contratação | Alta |
| `[assistente técnico contaminação alimentar]` | Exata | Caso concreto da especialidade | Contratação | Alta |
| `"assistente técnico processo judicial química"` | Frase | Contexto judicial explícito | Contratação | Alta |
| `[assistente técnico laudo pericial químico]` | Exata | Entregável + disciplina | Contratação | Alta |
| `[quesitos periciais engenharia química]` | Exata | Entregável dela, intenção de contratar | Contratação | Alta |
| `[elaboração de quesitos periciais química]` | Exata | Verbo de serviço | Contratação | Alta |
| `"quesitos técnicos perícia química"` | Frase | Variação natural | Contratação | Alta |
| `[assistente técnico perícia ambiental química]` | Exata | Duplamente qualificado | Contratação | Alta |
| `[assistente técnico classificação fiscal]` | Exata | Especialidade dela | Contratação | Alta |

---

### AG03 | Parecer e Laudo – Eng Química

**Objetivo:** capturar quem já sabe que precisa de um documento técnico e procura quem o produza.
**Landing page:** `https://adrianarezende.com.br/assistente-tecnica/#parecer-tecnico`
**Intenção de busca:** contratação de entregável específico.

| Keyword | Match | Por que pertence | Intenção | Conf. |
|---|---|---|---|---|
| `[parecer técnico engenharia química]` | Exata | Entregável + disciplina | Contratação | Alta |
| `[parecer técnico pericial engenharia química]` | Exata | Contexto pericial | Contratação | Alta |
| `[laudo técnico engenharia química]` | Exata | Entregável + disciplina | Contratação | Alta |
| `[laudo pericial engenharia química]` | Exata | Entregável processual | Contratação | Alta |
| `[laudo pericial químico]` | Exata | Qualificado por disciplina | Contratação | Alta |
| `[elaboração de parecer técnico químico]` | Exata | Verbo de serviço | Contratação | Alta |
| `[parecer técnico judicial engenharia química]` | Exata | Contexto judicial | Contratação | Alta |
| `[laudo técnico contaminação química]` | Exata | Caso concreto | Contratação | Alta |
| `[parecer técnico contaminação alimentos]` | Exata | Especialidade dela | Contratação | Alta |
| `"parecer técnico engenheiro químico"` | Frase | Variação por profissional | Contratação | Alta |
| `[laudo técnico processo industrial]` | Exata | Setor dela | Contratação | Alta |
| `[parecer técnico produto químico]` | Exata | Objeto da perícia | Contratação | Alta |
| `"laudo pericial engenharia de alimentos"` | Frase | Especialidade dela | Contratação | Alta |
| `[parecer técnico para processo judicial químico]` | Exata | Finalidade explícita | Contratação | Alta |

---

### AG04 | Perícia Alimentos

**Objetivo:** capturar litígios de contaminação, adulteração e autuação sanitária.
**Landing page:** `https://adrianarezende.com.br/pericia-contaminacao-alimentos/`
**Intenção de busca:** empresa autuada, ou advogado com caso de contaminação.

> 🔴 **Armadilha mais grave da conta:** no direito brasileiro, **"alimentos" também significa pensão alimentícia.** "Ação de alimentos", "execução de alimentos", "revisional de alimentos" são direito de família — volume gigantesco, intenção completamente errada. Sem o bloco F de negativas (§7), este ad group sozinho pode consumir o orçamento inteiro em tráfego de direito de família.

| Keyword | Match | Por que pertence | Intenção | Conf. |
|---|---|---|---|---|
| `[perícia contaminação alimentos]` | Exata | Serviço exato dela | Contratação | Alta |
| `[perícia contaminação alimentar]` | Exata | Variação natural | Contratação | Alta |
| `[perito contaminação alimentos]` | Exata | Profissional + caso | Contratação | Alta |
| `[laudo contaminação alimento]` | Exata | Entregável + caso | Contratação | Alta |
| `[perícia judicial alimentos contaminados]` | Exata | Contexto judicial explícito | Contratação | Alta |
| `[laudo pericial alimento contaminado]` | Exata | Entregável processual | Contratação | Alta |
| `[perícia corpo estranho alimento]` | Exata | Contaminação física — caso clássico | Contratação | Alta |
| `[perito engenharia de alimentos]` | Exata | Disciplina dela | Contratação | Alta |
| `[perícia alimento impróprio consumo]` | Exata | Caso concreto | Contratação | Alta |
| `[perícia técnica indústria alimentícia]` | Exata | Setor dela | Contratação | Alta |
| `[laudo técnico segurança alimentar judicial]` | Exata | Qualificado por "judicial" | Contratação | Alta |
| `[perícia autuação vigilância sanitária]` | Exata | Caso administrativo dela | Contratação | Alta |
| `[assistente técnico alimento contaminado]` | Exata | Serviço + caso | Contratação | Alta |
| `[perícia recall alimentos]` | Exata | Coberto na landing page | Contratação | Alta |
| `"perícia adulteração de alimentos"` | Frase | Serviço listado no site | Contratação | Alta |
| `[perícia ração animal contaminada]` | Exata | Caso citado no site | Contratação | Alta |

---

### AG05 | Classificação Fiscal NCM

**Objetivo:** capturar importador/exportador autuado pela Receita por reclassificação.
**Landing page:** `https://adrianarezende.com.br/classificacao-fiscal-ncm/`
**Intenção de busca:** empresa com auto de infração na mão, prazo de 30 dias correndo.

> ⚠️ **Armadilha:** a maioria das buscas por "NCM" quer **consultar um código** (ferramenta gratuita), não contratar laudo. Bloco H de negativas é obrigatório.

| Keyword | Match | Por que pertence | Intenção | Conf. |
|---|---|---|---|---|
| `[laudo técnico classificação fiscal]` | Exata | Entregável + serviço | Contratação | Alta |
| `[laudo técnico ncm]` | Exata | Entregável + serviço | Contratação | Alta |
| `[laudo merceológico]` | Exata | **Termo técnico exato do setor** — quem busca sabe o que quer | Contratação | Alta |
| `[laudo merceológico importação]` | Exata | Contexto aduaneiro | Contratação | Alta |
| `[análise merceológica produto]` | Exata | Serviço técnico | Contratação | Alta |
| `[perícia classificação fiscal]` | Exata | Serviço + contexto | Contratação | Alta |
| `[parecer técnico ncm]` | Exata | Entregável + serviço | Contratação | Alta |
| `[parecer técnico classificação fiscal]` | Exata | Entregável + serviço | Contratação | Alta |
| `[contestar classificação fiscal receita federal]` | Exata | Verbo + órgão = litígio | Contratação | Alta |
| `[impugnação auto de infração classificação fiscal]` | Exata | Ato processual exato | Contratação | Alta |
| `[laudo para reclassificação fiscal]` | Exata | Finalidade explícita | Contratação | Alta |
| `[perito classificação fiscal ncm]` | Exata | Profissional + serviço | Contratação | Alta |
| `[assistente técnico auto de infração aduaneiro]` | Exata | Serviço + contexto | Contratação | Alta |
| `"laudo técnico para contestar ncm"` | Frase | Finalidade explícita | Contratação | Alta |
| `[perícia técnica classificação mercadoria]` | Exata | Serviço + objeto | Contratação | Alta |

---

### AG06 | Impugnação de Laudo

**Objetivo:** capturar advogado que recebeu um laudo desfavorável e quer atacá-lo tecnicamente.
**Landing page:** `https://adrianarezende.com.br/assistente-tecnica/#impugnacao-laudos`
**Intenção de busca:** urgência alta, insatisfação com laudo existente. Volume baixo, intenção altíssima.

| Keyword | Match | Por que pertence | Intenção | Conf. |
|---|---|---|---|---|
| `[impugnação laudo pericial engenharia química]` | Exata | Ato + disciplina | Contratação | Alta |
| `[impugnar laudo pericial químico]` | Exata | Verbo + disciplina | Contratação | Alta |
| `[contestar laudo pericial engenharia química]` | Exata | Verbo + disciplina | Contratação | Alta |
| `[impugnar laudo pericial alimentos]` | Exata | Verbo + especialidade | Contratação | Alta |
| `[análise crítica laudo pericial químico]` | Exata | Serviço exato dela | Contratação | Alta |
| `[parecer contra laudo pericial químico]` | Exata | Entregável + finalidade | Contratação | Alta |
| `[assistente técnico para impugnar laudo]` | Exata | Serviço + finalidade | Contratação | Alta |
| `"contestar laudo perícia judicial química"` | Frase | Variação natural | Contratação | Alta |
| `[refutar laudo pericial técnico]` | Exata | Verbo técnico | Contratação | Alta |
| `[erro metodológico laudo pericial]` | Exata | Ângulo técnico — coberto na página | Contratação | Alta |

---

### AG07 | Perícia Ambiental  ✅ *desbloqueado — página criada em 04/08/2026*

**Objetivo:** passivos ambientais industriais, contaminação de solo/água, efluentes.
**Landing page:** `https://adrianarezende.com.br/pericia-ambiental/` — **criada em 04/08/2026.**
**Intenção de busca:** empresa com passivo ou litígio ambiental.

> ⚠️ "Perícia ambiental" atrai fortemente engenheiros ambientais, biólogos e geólogos. Toda keyword precisa do qualificador *química / industrial / contaminação*.

| Keyword | Match | Por que pertence | Intenção | Conf. |
|---|---|---|---|---|
| `[perícia ambiental contaminação solo]` | Exata | Caso técnico dela | Contratação | Alta |
| `[perícia contaminação solo e água]` | Exata | Serviço listado no site | Contratação | Alta |
| `[perito contaminação química ambiental]` | Exata | Duplamente qualificado | Contratação | Alta |
| `[perícia passivo ambiental industrial]` | Exata | Termo do site | Contratação | Alta |
| `[laudo técnico contaminação solo industrial]` | Exata | Entregável + caso | Contratação | Alta |
| `[perícia judicial contaminação ambiental industrial]` | Exata | Contexto judicial | Contratação | Alta |
| `[assistente técnico perícia ambiental industrial]` | Exata | Serviço + contexto | Contratação | Alta |
| `[perícia efluentes industriais]` | Exata | Experiência do site | Contratação | Alta |
| `[laudo técnico resíduos perigosos]` | Exata | ABNT/CONAMA, citado no site | Contratação | Alta |
| `[perícia aterro sanitário]` | Exata | Caso citado no site | Contratação | Alta |

---

### AG08 | Adulteração Combustíveis  ✅ *desbloqueado — página criada em 04/08/2026*

**Objetivo:** litígios de adulteração/contaminação de combustível, conformidade ANP.
**Landing page:** `https://adrianarezende.com.br/pericia-combustiveis/` — **criada em 04/08/2026.**
**Intenção de busca:** posto, distribuidora ou advogado em litígio de qualidade de combustível.

| Keyword | Match | Por que pertence | Intenção | Conf. |
|---|---|---|---|---|
| `[perícia adulteração combustível]` | Exata | Serviço exato do site | Contratação | Alta |
| `[laudo adulteração combustível]` | Exata | Entregável + caso | Contratação | Alta |
| `[perícia contaminação combustível]` | Exata | Serviço do site | Contratação | Alta |
| `[perito combustível adulterado]` | Exata | Profissional + caso | Contratação | Alta |
| `[laudo técnico qualidade combustível]` | Exata | Entregável técnico | Contratação | Alta |
| `[perícia judicial posto de combustível]` | Exata | Contexto judicial + setor | Contratação | Alta |
| `[assistente técnico adulteração combustível]` | Exata | Serviço + caso | Contratação | Alta |
| `[perícia conformidade anp]` | Exata | Órgão citado no site | Contratação | Alta |
| `[laudo pericial combustível]` | Exata | Entregável + objeto da perícia | Contratação | Alta |
| `"perícia qualidade combustível judicial"` | Frase | Objeto + contexto judicial | Contratação | Alta |

---

## 4. Keywords rejeitadas — e por quê

Estas foram avaliadas e **descartadas**. O teste aplicado: *"eu pagaria R$50 do meu bolso por este clique?"*

| Keyword rejeitada | Motivo da rejeição | Regra violada |
|---|---|---|
| `perícia judicial` | Genérica — 90% é outra especialidade (médica, civil, veicular) | 7 — broad demais |
| `perito judicial` | Idem | 7 |
| `laudo técnico` | Sem disciplina, pode ser qualquer engenharia | 7 |
| `parecer técnico` | Idem | 7 |
| `assistente técnica` | **Majoritariamente eletrodoméstico/celular no Brasil** | 2, 7 |
| `perícia` | Absurdamente genérica | 7 |
| `laudo` | Idem | 7 |
| `engenharia química` | Intenção de estudante | 3, 5 |
| `engenheiro químico` | Busca por profissão/carreira | 6 |
| `o que faz um perito judicial` | Informacional puro | 4 |
| `como ser perito judicial` | Intenção de carreira | 6 |
| `curso de perícia judicial` | Educacional | 5 |
| `quanto ganha um perito judicial` | Carreira/salário | 6 |
| `cadastro perito judicial tribunal` | Quer *ser* perito, não contratar | 6 |
| `perito judicial vagas` | Emprego | 6 |
| `modelo de quesitos periciais` | Quer template grátis, não contratar | 3, 4 |
| `modelo de parecer técnico` | Idem | 3, 4 |
| `impugnação de laudo pericial modelo` | Quer peça pronta | 3, 4 |
| `perícia médica` | Outra profissão | 2 |
| `perícia criminal` | Outra especialidade | 2 |
| `perícia veicular` | Outra especialidade | 2 |
| `perícia grafotécnica` | Outra especialidade | 2 |
| `perícia contábil` | Outra profissão | 2 |
| `perícia previdenciária` / `perícia inss` | Outra especialidade | 2 |
| `perícia engenharia civil` | Outra engenharia | 2 |
| `perícia trabalhista insalubridade` | Exige eng. de segurança do trabalho — **site não reivindica** | 1, 2 |
| `laudo de periculosidade` | Idem — não é serviço dela | 1 |
| `perícia imobiliária` / `avaliação de imóveis` | Outra especialidade | 2 |
| `perícia informática` / `forense digital` | Outra especialidade | 2 |
| `ação de alimentos` | **Direito de família** — armadilha semântica | 2 |
| `pensão alimentícia` | Direito de família | 2 |
| `laboratório análise de alimentos` | **Ela não é laboratório** | 1 |
| `análise microbiológica preço` | Serviço de laboratório | 1 |
| `onde fazer análise de água` | Serviço de laboratório | 1 |
| `consulta ncm` | Quer ferramenta gratuita | 3, 4 |
| `tabela ncm` | Ferramenta gratuita | 3, 4 |
| `qual o ncm do produto` | Informacional | 4 |
| `ncm nota fiscal` | Operacional/fiscal, não litígio | 3 |
| `curso classificação fiscal` | Educacional | 5 |
| `licenciamento ambiental` | Consultoria regulatória — **não é serviço dela** | 1 |
| `estudo de impacto ambiental` | Consultoria ambiental, não perícia | 1 |
| `registro de produto anvisa` | Assuntos regulatórios — não é serviço dela | 1 |
| `rotulagem nutricional consultoria` | Consultoria regulatória | 1 |
| `licença polícia federal produtos químicos` | **Consultoria de licenciamento** — não é o serviço | 1 |
| `perito judicial gratuito` | Busca por gratuidade | 3 |
| `assistente técnico barato` | Busca por preço mínimo — lead ruim | 3 |
| `perícia judicial preço` | Pesquisa de preço sem caso definido | 3 (baixa qualificação) |

---

## 5. Anúncios responsivos (RSA)

Todos validados: headlines ≤30 caracteres, descrições ≤90.

### Diretrizes aplicadas
- Autoridade usada com naturalidade (UNICAMP, CRQ-IV, +20 anos) — todos **verificáveis no site**
- Zero hype, zero promessa de resultado (proibido em serviço técnico-jurídico)
- Sem afirmação de prazo de resposta (não verificável)
- Fixar (*pin*) apenas a headline 1 quando o ad group exigir correspondência exata de termo

---

### RSA — AG02 | Assistente Técnica

**Headlines (15)**
| # | Texto | Chars |
|---|---|---|
| 1 | Assistente Técnica Química | 26 |
| 2 | Assistente Técnico Pericial | 27 |
| 3 | Eng. Química UNICAMP | 20 |
| 4 | Apoio Técnico a Advogados | 25 |
| 5 | Perícia em Engenharia Química | 29 |
| 6 | Análise Crítica de Laudos | 25 |
| 7 | Quesitos Técnicos Precisos | 26 |
| 8 | +20 Anos de Experiência | 23 |
| 9 | CRQ-IV SP nº 04341673 | 21 |
| 10 | Atendimento em Todo o Brasil | 28 |
| 11 | Prazo do Art. 465 do CPC | 24 |
| 12 | Parecer Técnico Fundamentado | 28 |
| 13 | Indústria, Alimentos e Meio | 27 |
| 14 | Adriana Rezende | 15 |
| 15 | Acompanhamento de Perícia | 25 |

**Descrições (4)**
| # | Texto | Chars |
|---|---|---|
| 1 | Assistente técnica em perícias de engenharia química, alimentos e meio ambiente. | 80 |
| 2 | Engenheira química pela UNICAMP, CRQ-IV SP. Mais de 20 anos de atuação técnica. | 79 |
| 3 | Quesitos, acompanhamento de vistoria e análise crítica do laudo pericial. | 73 |
| 4 | Apoio a escritórios e departamentos jurídicos. Atendimento em todo o Brasil. | 76 |

---

### RSA — AG04 | Perícia Alimentos

**Headlines (15)**
| # | Texto | Chars |
|---|---|---|
| 1 | Perícia em Contaminação | 23 |
| 2 | Perícia em Alimentos | 20 |
| 3 | Contaminação Alimentar | 22 |
| 4 | Eng. Química UNICAMP | 20 |
| 5 | Laudo de Contaminação | 21 |
| 6 | Perita Judicial Alimentos | 25 |
| 7 | Investigação de Causa Raiz | 26 |
| 8 | Normas ANVISA e APPCC | 21 |
| 9 | +20 Anos em Indústria | 21 |
| 10 | Cadeia de Custódia | 18 |
| 11 | Apoio Técnico a Advogados | 25 |
| 12 | CRQ-IV SP nº 04341673 | 21 |
| 13 | Física, Química ou Biológica | 28 |
| 14 | Atendimento Nacional | 20 |
| 15 | Adriana Rezende | 15 |

**Descrições (4)**
| # | Texto | Chars |
|---|---|---|
| 1 | Investigação técnica de contaminação física, química e biológica em alimentos. | 78 |
| 2 | Cadeia de custódia, normas ANVISA, APPCC e apuração de responsabilidade. | 72 |
| 3 | Engenheira química pela UNICAMP com 14 anos em indústria de alimentos. | 70 |
| 4 | Perícia judicial e assistência técnica. Atendimento em todo o território. | 73 |

---

### RSA — AG05 | Classificação Fiscal NCM

**Headlines (15)**
| # | Texto | Chars |
|---|---|---|
| 1 | Laudo Técnico de NCM | 20 |
| 2 | Classificação Fiscal NCM | 24 |
| 3 | Laudo Merceológico | 18 |
| 4 | Contestar Auto de Infração | 26 |
| 5 | Eng. Química UNICAMP | 20 |
| 6 | Prova Técnica de Composição | 27 |
| 7 | Impugnação na Receita | 21 |
| 8 | Regras Gerais do SH | 19 |
| 9 | +20 Anos de Experiência | 23 |
| 10 | CRQ-IV SP nº 04341673 | 21 |
| 11 | Apoio a Importadores | 20 |
| 12 | Prazo de 30 Dias | 16 |
| 13 | Reclassificação Fiscal | 22 |
| 14 | Atendimento Nacional | 20 |
| 15 | Adriana Rezende | 15 |

**Descrições (4)**
| # | Texto | Chars |
|---|---|---|
| 1 | Laudo técnico para contestar reclassificação fiscal em auto de infração. | 72 |
| 2 | Composição, função e processo de obtenção do produto frente às RGI do SH. | 73 |
| 3 | Engenheira química pela UNICAMP, CRQ-IV SP. Mais de 20 anos de atuação. | 71 |
| 4 | Apoio a importadores, exportadores e departamentos jurídicos no Brasil. | 71 |

---

### RSA — AG03 | Parecer e Laudo

**Headlines (15)**
| # | Texto | Chars |
|---|---|---|
| 1 | Parecer Técnico Químico | 23 |
| 2 | Laudo Pericial Químico | 22 |
| 3 | Parecer em Eng. Química | 23 |
| 4 | Eng. Química UNICAMP | 20 |
| 5 | Fundamentação Científica | 24 |
| 6 | Apoio Técnico a Advogados | 25 |
| 7 | +20 Anos de Experiência | 23 |
| 8 | CRQ-IV SP nº 04341673 | 21 |
| 9 | Linguagem Acessível ao Juízo | 28 |
| 10 | Perita Judicial | 15 |
| 11 | Alimentos, Química, Meio Amb | 28 |
| 12 | Análise Crítica de Laudos | 25 |
| 13 | Atendimento Nacional | 20 |
| 14 | Adriana Rezende | 15 |
| 15 | Parecer para Processo | 21 |

**Descrições (4)**
| # | Texto | Chars |
|---|---|---|
| 1 | Parecer e laudo técnico em engenharia química, alimentos e meio ambiente. | 73 |
| 2 | Fundamentação científica em linguagem acessível a quem julga o processo. | 72 |
| 3 | Engenheira química pela UNICAMP, CRQ-IV SP nº 04341673. +20 anos. | 65 |
| 4 | Apoio a escritórios, departamentos jurídicos e indústrias no Brasil. | 68 |

---

### RSA — AG06 | Impugnação de Laudo

**Headlines (15)**
| # | Texto | Chars |
|---|---|---|
| 1 | Impugnação de Laudo | 19 |
| 2 | Contestar Laudo Pericial | 24 |
| 3 | Análise Crítica de Laudo | 24 |
| 4 | Eng. Química UNICAMP | 20 |
| 5 | Falha Metodológica | 18 |
| 6 | Parecer Divergente | 18 |
| 7 | Apoio Técnico a Advogados | 25 |
| 8 | +20 Anos de Experiência | 23 |
| 9 | CRQ-IV SP nº 04341673 | 21 |
| 10 | Art. 479 do CPC | 15 |
| 11 | Perícia em Eng. Química | 23 |
| 12 | Amostragem e Custódia | 21 |
| 13 | Atendimento Nacional | 20 |
| 14 | Adriana Rezende | 15 |
| 15 | Assistente Técnica | 18 |

**Descrições (4)**
| # | Texto | Chars |
|---|---|---|
| 1 | Análise crítica fundamentada de laudo pericial em matéria química. | 66 |
| 2 | Amostragem, cadeia de custódia, norma aplicada e limite de quantificação. | 73 |
| 3 | Engenheira química pela UNICAMP, CRQ-IV SP. Mais de 20 anos de atuação. | 71 |
| 4 | O juiz aprecia o método empregado (art. 479 do CPC). Apoio a advogados. | 71 |

---

### RSA — AG07 | Perícia Ambiental

**Headlines (15)**
| # | Texto | Chars |
|---|---|---|
| 1 | Perícia Ambiental | 17 |
| 2 | Contaminação de Solo e Água | 27 |
| 3 | Passivo Ambiental Industrial | 28 |
| 4 | Eng. Química UNICAMP | 20 |
| 5 | Laudo de Área Contaminada | 25 |
| 6 | CONAMA 420 e NBR 10004 | 22 |
| 7 | Apoio Técnico a Advogados | 25 |
| 8 | +20 Anos de Experiência | 23 |
| 9 | CRQ-IV SP nº 04341673 | 21 |
| 10 | Nexo Causal Demonstrado | 23 |
| 11 | Perita Judicial Ambiental | 25 |
| 12 | Efluentes e Resíduos | 20 |
| 13 | Atendimento Nacional | 20 |
| 14 | Adriana Rezende | 15 |
| 15 | Assistente Técnica | 18 |

**Descrições (4)**
| # | Texto | Chars |
|---|---|---|
| 1 | Perícia em contaminação de solo e água, passivos ambientais e resíduos. | 71 |
| 2 | Valores orientadores da CONAMA 420/2009 e classificação pela NBR 10004. | 71 |
| 3 | Engenheira química pela UNICAMP, CRQ-IV SP. Mais de 20 anos de atuação. | 71 |
| 4 | Apoio a escritórios e departamentos jurídicos em todo o território. | 67 |

---

### RSA — AG08 | Adulteração Combustíveis

**Headlines (15)**
| # | Texto | Chars |
|---|---|---|
| 1 | Perícia em Combustíveis | 23 |
| 2 | Adulteração de Combustível | 26 |
| 3 | Laudo de Qualidade ANP | 22 |
| 4 | Eng. Química UNICAMP | 20 |
| 5 | Conformidade ANP | 16 |
| 6 | Adulteração ou Contaminação | 27 |
| 7 | Apoio Técnico a Advogados | 25 |
| 8 | +20 Anos de Experiência | 23 |
| 9 | CRQ-IV SP nº 04341673 | 21 |
| 10 | Marcador de Solvente | 20 |
| 11 | Cadeia de Custódia | 18 |
| 12 | Perícia em Postos | 17 |
| 13 | Atendimento Nacional | 20 |
| 14 | Adriana Rezende | 15 |
| 15 | Assistente Técnica | 18 |

**Descrições (4)**
| # | Texto | Chars |
|---|---|---|
| 1 | Perícia técnica em adulteração e contaminação de combustíveis. | 62 |
| 2 | Especificações da ANP, marcador de solvente e cadeia de custódia. | 65 |
| 3 | Engenheira química pela UNICAMP, CRQ-IV SP. Mais de 20 anos de atuação. | 71 |
| 4 | Apoio a postos, distribuidoras e departamentos jurídicos no Brasil. | 67 |

---

## 6. Assets

### Display Path (15 caracteres por campo)

| Ad group | Path 1 | Path 2 |
|---|---|---|
| AG01 | `Pericia` | `Eng-Quimica` |
| AG02 | `Assistente` | `Tecnica` |
| AG03 | `Parecer` | `Tecnico` |
| AG04 | `Pericia` | `Alimentos` |
| AG05 | `Classificacao` | `NCM` |
| AG06 | `Impugnacao` | `Laudo` |

### Callouts (≤25 caracteres) — nível de campanha

| Callout | Chars |
|---|---|
| Eng. Química UNICAMP | 20 |
| CRQ-IV SP nº 04341673 | 21 |
| +20 Anos de Experiência | 23 |
| Atendimento Nacional | 20 |
| Apoio a Advogados | 17 |
| Base em Campinas/SP | 19 |
| Perícia e Assistência | 21 |
| Análise Preliminar | 18 |

### Structured Snippets (≤25 caracteres por valor)

**Header: Serviços**
`Perícia Judicial` · `Assistência Técnica` · `Parecer Técnico` · `Laudo Pericial` · `Quesitos Técnicos` · `Impugnação de Laudo`

**Header: Tipos**
`Contaminação Alimentar` · `Classificação Fiscal NCM` · `Perícia Ambiental` · `Combustíveis` · `Produtos Químicos`

### Sitelinks

| # | Título (≤25) | Descrição 1 (≤35) | Descrição 2 (≤35) | URL |
|---|---|---|---|---|
| 1 | Assistente Técnica | Apoio técnico em processos | judiciais de matéria química | `/assistente-tecnica/` |
| 2 | Perícia em Alimentos | Contaminação, ANVISA e APPCC | Apuração de responsabilidade | `/pericia-contaminacao-alimentos/` |
| 3 | Classificação Fiscal | Laudo técnico para contestar | auto de infração da Receita | `/classificacao-fiscal-ncm/` |
| 4 | Quem é Adriana Rezende | Eng. química UNICAMP, CRQ-IV | Mais de 20 anos de atuação | `/sobre/` |
| 5 | Fale por WhatsApp | Análise preliminar do caso | Atendimento em todo o Brasil | `/#contact` |
| 6 | Impugnar um Laudo | Análise crítica fundamentada | de laudo pericial existente | `/assistente-tecnica/#impugnacao-laudos` |

**Recomendação de UTM:** **não** colocar UTM em cada sitelink individualmente. Use o **Final URL Suffix no nível da campanha**:

```
utm_source=google&utm_medium=cpc&utm_campaign=search_high_intent&utm_content={creative}&utm_term={keyword}&utm_adgroup={adgroupid}
```

> ⚠️ Mantenha o **auto-tagging (GCLID) LIGADO**. O GCLID é o que faz a ligação Ads↔GA4 funcionar — os UTMs são só para legibilidade nos relatórios do GA4. Se o auto-tagging for desligado em favor de UTM manual, a importação de conversões do GA4 quebra e o `manual_event_CONTACT` para de creditar.

---

## 7. Lista de negativas compartilhada (382)

Criar como **listas compartilhadas separadas por tema** (Ferramentas → Listas de exclusão de palavras-chave), para poder aplicar seletivamente por campanha no futuro.

### Bloco A — Carreira e emprego (38)
`vaga` `vagas` `emprego` `empregos` `salário` `salario` `quanto ganha` `quanto custa ser` `piso salarial` `remuneração` `concurso` `concurso público` `edital` `carreira` `como ser` `como se tornar` `como virar` `quero ser` `formação para` `cadastro` `cadastro perito` `credenciamento` `credenciar` `inscrição` `nomeação como perito` `ser perito` `virar perito` `trabalhar como` `contratação clt` `estágio` `estagiário` `trainee` `freelance` `freelancer` `home office` `indeed` `catho` `glassdoor`

### Bloco B — Educação e cursos (42)
`curso` `cursos` `faculdade` `graduação` `graduacao` `pós` `pós-graduação` `posgraduacao` `mba` `especialização` `especializacao` `mestrado` `doutorado` `certificação` `certificacao` `treinamento` `capacitação` `capacitacao` `aula` `aulas` `apostila` `apostilas` `pdf` `download` `ebook` `e-book` `livro` `livros` `material` `slides` `videoaula` `tutorial` `passo a passo` `aprenda` `aprender` `estudar` `estudo dirigido` `resumo` `monografia` `tcc` `artigo científico` `dissertação`

### Bloco C — Informacional e DIY (32)
`o que é` `o que e` `o que faz` `oque e` `significado` `definição` `definicao` `conceito` `exemplo` `exemplos` `modelo` `modelos` `template` `formulário` `formulario` `planilha` `wikipedia` `wiki` `como fazer` `como funciona` `como elaborar` `como redigir` `como escrever` `quais são` `diferença entre` `diferenca entre` `para que serve` `vantagens` `desvantagens` `história` `resumo de` `pesquisa sobre`

### Bloco D — Outras engenharias (26)
`civil` `engenharia civil` `estrutural` `mecânica` `mecanica` `engenharia mecânica` `elétrica` `eletrica` `engenharia elétrica` `eletrônica` `produção` `engenharia de produção` `agronômica` `agronomia` `agrônomo` `florestal` `naval` `aeronáutica` `minas` `petróleo` `software` `computação` `telecomunicações` `segurança do trabalho` `engenheiro de segurança` `cipa`

### Bloco E — Outras especialidades de perícia (44)
`médica` `medica` `perícia médica` `perito médico` `odontológica` `odontologia` `dentista` `psicológica` `psicologia` `psiquiátrica` `veterinária` `criminal` `perícia criminal` `papiloscopia` `balística` `datiloscopia` `grafotécnica` `grafotecnica` `grafoscopia` `documentoscopia` `documentoscópica` `veicular` `automotiva` `perícia veicular` `sinistro` `seguradora` `imobiliária` `imobiliario` `avaliação de imóveis` `avaliação de imovel` `engenharia diagnóstica` `patologia das construções` `infiltração` `contábil` `contabil` `perícia contábil` `previdenciária` `previdenciaria` `inss` `auxílio doença` `aposentadoria` `informática` `forense digital` `perícia digital`

### Bloco F — 🔴 Direito de família ("alimentos" ≠ comida) (24)
`pensão` `pensao` `pensão alimentícia` `pensao alimenticia` `ação de alimentos` `acao de alimentos` `execução de alimentos` `revisional de alimentos` `revisional` `alimentos gravídicos` `exoneração de alimentos` `guarda` `guarda compartilhada` `divórcio` `divorcio` `separação` `união estável` `paternidade` `dna` `visitação` `desconto em folha` `prisão civil` `inadimplemento pensão` `vara de família`

### Bloco G — 🔴 Assistência técnica de produto (34)
`autorizada` `assistência autorizada` `assistencia autorizada` `conserto` `consertar` `reparo` `manutenção` `manutencao` `celular` `smartphone` `iphone` `notebook` `computador` `tv` `televisão` `geladeira` `fogão` `máquina de lavar` `micro-ondas` `ar condicionado` `eletrodoméstico` `eletrodomestico` `eletrônico` `samsung` `lg` `brastemp` `consul` `electrolux` `philips` `sony` `motorola` `xiaomi` `garantia` `troca de tela`

### Bloco H — Ferramentas e consulta de NCM (28)
`consulta` `consultar` `consulta ncm` `tabela` `tabela ncm` `lista` `lista ncm` `código` `codigo` `código ncm` `buscar` `busca ncm` `pesquisar ncm` `qual ncm` `qual o ncm` `ncm de` `nfe` `nota fiscal` `sped` `sintegra` `cest` `cfop` `siscomex` `simples nacional` `mei` `emissor` `sistema` `software fiscal`

### Bloco I — Serviços de laboratório (ela não é laboratório) (18)
`laboratório` `laboratorio` `análise laboratorial` `analise laboratorial` `onde analisar` `onde fazer análise` `exame` `exames` `ensaio` `coleta de amostra preço` `análise de água preço` `análise microbiológica preço` `bromatológica` `cromatografia preço` `espectrometria` `acreditado perto de mim` `laboratório credenciado` `enviar amostra`

### Bloco J — Consultoria regulatória (não é perícia) (24)
`licenciamento` `licenciamento ambiental` `licença ambiental` `licenca ambiental` `outorga` `condicionantes` `eia` `rima` `estudo de impacto` `registro anvisa` `registro de produto` `regularização` `regularizacao` `alvará` `alvara` `rotulagem` `rotulagem nutricional` `tabela nutricional` `boas práticas implantação` `implantar appcc` `certificação iso` `selo` `licença polícia federal` `certificado de registro cadastral`

### Bloco K — Gratuidade e preço mínimo (16)
`grátis` `gratis` `gratuito` `gratuita` `free` `de graça` `sem custo` `barato` `mais barato` `preço baixo` `desconto` `promoção` `orçamento grátis` `consulta gratuita` `defensoria` `justiça gratuita`

### Bloco L — Institucional e órgãos (22)
`telefone` `endereço` `endereco` `horário de atendimento` `protocolo` `2ª via` `segunda via` `boleto` `pagamento` `login` `entrar` `portal` `gov.br` `receita federal telefone` `anvisa telefone` `crq telefone` `tribunal` `processo consulta` `andamento processual` `jusbrasil` `diário oficial` `publicação`

### Bloco M — Marketplaces e diretórios (14)
`getninjas` `99freelas` `workana` `olx` `mercado livre` `linkedin` `facebook` `instagram` `youtube` `reclame aqui` `melhores` `ranking` `lista de peritos` `diretório`

### Bloco N — Diversos fora de escopo (20)
`receita` `receitas` `culinária` `restaurante` `nutricionista` `dieta` `suplemento` `cosmético` `farmacêutico` `medicamento` `agrotóxico venda` `fertilizante venda` `comprar` `venda` `fornecedor` `distribuidor` `atacado` `franquia` `abrir empresa` `cnpj`

> **Total: 382 negativas**, todas únicas (verificado). Aplicar todas antes do primeiro impression. Blocos F, G e H são os que mais protegem verba neste nicho específico.

---

## 8. Estratégia de match type

| Fase | Recomendação |
|---|---|
| **Lançamento** | **Exact (~70%) + Phrase (~30%).** Zero broad. |
| **Por que não broad** | Broad match depende de sinais de conversão para se comportar. Com 0 conversões de histórico, o Google adivinha — e adivinha caro. |
| **Broad no futuro** | Só depois de ~30 conversões reais **e** com a lista de negativas madura. Mesmo assim, em ad group isolado com orçamento próprio, nunca misturado. |
| **Correção imediata** | As 9 keywords do AG01 estão em Broad hoje. Duplicar em Exact, pausar as Broad. |

**Regra operacional:** revisar o **relatório de termos de busca 2× por semana** nas primeiras 4 semanas. Todo termo irrelevante vira negativa no mesmo dia.

---

## 9. Estratégia de lances

| Fase | Gatilho | Estratégia | Racional |
|---|---|---|---|
| **Fase 1** — semanas 1–4 | Agora | **Manual CPC**, teto R$ 25–40 | Zero histórico. Manual dá controle total enquanto a lista de negativas amadurece. |
| **Fase 2** — semanas 5–10 | ≥ 15 conversões em 30 dias | **Maximize Conversions** (sem tCPA) | Sinal suficiente para o algoritmo aprender. |
| **Fase 3** — semana 11+ | ≥ 30 conversões em 30 dias | **Maximize Conversions com tCPA** | Só então faz sentido impor um alvo de custo. |
| **Fase 4** — futuro | OCI de leads qualificados rodando | **tCPA sobre lead qualificado** | O salto de qualidade real. Ver §11. |

> 🔴 **Ação imediata:** a campanha está em **Maximize Conversions com zero conversões**. Trocar para Manual CPC **hoje**, antes de servir a primeira impressão.

---

## 10. Orçamento e economia unitária

### Recomendação
| Período | Orçamento/dia | Mês (≈30,4d) |
|---|---|---|
| Dias 1–30 | **R$ 120** | R$ 3.650 |
| Dias 31–90 | R$ 150–185 | R$ 4.560–5.620 |
| Após validação | escalar conforme CPA | — |

> Atenção: com Exact/Phrase em cauda longa, **a campanha provavelmente não gastará o teto** — será limitada por volume de busca, não por verba. Isso é esperado e saudável. Se o gasto vier bem abaixo do teto, **não relaxe o match type para compensar** — em vez disso, adicione ad groups da Onda 2 (com landing pages novas).

### Economia unitária — o cálculo que importa

Premissa: CPC médio R$ 35 (cauda longa, concorrência baixa).

| Taxa de conversão (clique → contato) | Custo por contato |
|---|---|
| 4% | R$ 875 |
| 8% | R$ 437 |
| 12% | R$ 291 |

Agora o funil completo, com taxa de fechamento sobre contatos:

| Conv. do site | Fechamento | **Custo por caso fechado** |
|---|---|---|
| 4% | 10% | R$ 8.750 |
| 8% | 20% | **R$ 2.187** |
| 12% | 30% | R$ 971 |

**Leitura:** no cenário central (8% / 20%), cada caso conquistado custa ≈ **R$ 2.187** em mídia. Como um único caso pericial de complexidade média em matéria química vale um múltiplo disso, **a campanha se paga com folga desde que a qualificação do lead seja real.** Por isso §11 é mais importante que qualquer ajuste de lance.

> Não estimei honorários da Adriana porque o site não os publica — e eu não invento número que não posso verificar. Preencha o valor médio de contrato e o ponto de equilíbrio se resolve sozinho.

---

## 11. Rastreamento de conversão — a maior alavanca do plano

### Situação atual (auditada ao vivo)

| Ação de conversão | Status | Primária? | Contagem | Conta em "Conversões"? |
|---|---|---|---|---|
| `manual_event_CONTACT` | ENABLED | ✅ sim | ⚠️ **Every** | ✅ sim |
| `SUBMIT_LEAD_FORM` | ENABLED | ✅ sim | Every | ❌ não |
| `Lead form - Submit` | ENABLED | ✅ sim | One | ❌ não |

### Correções obrigatórias

**1. 🔴 Trocar `manual_event_CONTACT` de "Every" para "One" (por clique).**
Eu instalei o disparo em **três pontos só na home** (link da seção de contato, rodapé, e o submit do formulário) mais os botões de CTA nas quatro páginas de conteúdo. Um mesmo visitante indeciso pode disparar 3–4 conversões. O Smart Bidding otimizaria para um número inflado, aprendendo a comprar cliques de gente que hesita — exatamente o oposto do desejado.

**2. Deixar apenas UMA ação como primária.**
Três estão marcadas como primária. As duas de lead form nem contam para a métrica de conversões — são ruído que confunde relatório e futuras automações. Manter só `manual_event_CONTACT` como primária; rebaixar as outras para secundária.

**3. 🎯 Implementar Offline Conversion Import (OCI) — a mudança de patamar.**

Hoje a conversão mede *clique em WhatsApp*. Não distingue um sócio de escritório com um caso de R$ 40 mil de um estudante curioso. Otimizar para esse sinal ensina o Google a trazer volume, não qualidade.

**A solução aproveita algo que já construímos:** a mensagem do WhatsApp já vai pré-preenchida. Basta anexar o `gclid` a ela.

Fluxo proposto:
1. Capturar o `gclid` do parâmetro de URL e guardar em `localStorage` (persiste na sessão)
2. Anexar um código curto ao final da mensagem pré-preenchida — ex.: `[ref: Cj0KCQ...]`
3. A Adriana recebe a mensagem no WhatsApp **com o código embutido**
4. Quando ela qualifica o lead (caso real, cliente potencial), registra em planilha: `gclid` + data + status
5. Upload periódico dessa planilha em *Conversões → Importar* como conversão offline "Lead Qualificado"
6. Passar o Smart Bidding a otimizar para **Lead Qualificado**, não para clique

**Impacto:** o Google deixa de perseguir cliques e passa a perseguir advogados com casos reais. Em nicho B2B de ticket alto, esta é tipicamente a diferença entre uma campanha que empata e uma que multiplica.

> Posso implementar os passos 1 e 2 no site quando você quiser — é uma alteração pequena no JS que já escrevi para o WhatsApp.

**4. Definir valor de conversão.** Mesmo estimado (ex.: valor médio de contrato × taxa de fechamento), habilita bidding por valor no futuro.

---

## 12. Quality Score — plano de defesa

QS alto = CPC menor pelo mesmo posicionamento. Três componentes:

| Componente | Ação |
|---|---|
| **Relevância do anúncio** | Ad groups temáticos apertados (é por isso que a estrutura tem 6 grupos, não 1). Headline 1 de cada RSA espelha o tema do ad group. |
| **CTR esperado** | Termo da busca aparece literalmente na headline e no display path. Sitelinks e callouts aumentam a área do anúncio e o CTR. |
| **Experiência na landing page** | 🔴 **Aqui está o problema atual.** Todo anúncio aponta para `/`. Corrigir para landing page temática — já mapeado em §2. |

**Ações concretas:**
1. Trocar a final URL de cada ad group para sua página temática (tabela §2)
2. Não lançar AG07/AG08 sem página própria — a home derruba o QS desses grupos
3. Manter velocidade: o site é estático no GitHub Pages, LCP com preload — já está bom
4. Revisar QS por keyword no dia 30; qualquer keyword com QS ≤ 4 vira candidata a pausa ou reescrita de anúncio

---

## 13. Checklist de lançamento

**🔴 Bloqueadores — fazer antes de qualquer impressão**
- [ ] Trocar bidding de Maximize Conversions → **Manual CPC** (teto R$ 25–40)
- [ ] Converter as 9 keywords do AG01 de **Broad → Exact/Phrase**
- [ ] Subir as **382 negativas** (§7), com prioridade absoluta nos blocos F, G, H
- [ ] Trocar contagem de `manual_event_CONTACT` de **Every → One**
- [ ] Deixar **uma única** ação de conversão como primária
- [ ] Reduzir orçamento para **R$ 120/dia** nos primeiros 30 dias

**🟠 Estrutura**
- [ ] Renomear campanha → `Search | High Intent | BR`
- [ ] Renomear ad group 1 → `AG01 | Perita Judicial – Eng Química`
- [ ] Criar AG02 a AG06 com keywords e RSAs deste documento
- [ ] Apontar cada ad group para sua landing page temática
- [ ] Configurar Display Paths por ad group

**🟡 Assets**
- [ ] Subir 8 callouts (nível campanha)
- [ ] Subir 2 structured snippets (Serviços, Tipos)
- [ ] Subir 6 sitelinks
- [ ] Configurar Final URL Suffix com UTMs
- [ ] Confirmar **auto-tagging LIGADO**

**🟢 Configuração**
- [ ] Localização: Brasil — mudar para **"Presença: pessoas no local"** (evita curioso no exterior)
- [ ] Idioma: Português ✅ (já está)
- [ ] Rede: **desmarcar Rede de Display e parceiros de pesquisa** no lançamento
- [ ] Rotação de anúncios: otimizar
- [ ] Agendamento: considerar horário comercial (advogado busca em horário útil) — avaliar após 30 dias com dados

---

## 14. Plano de 30 dias

| Dias | Foco | Ações |
|---|---|---|
| **1–2** | Correção estrutural | Todos os bloqueadores do §13. Nada serve até isso estar feito. |
| **3–7** | Vigilância de termos | Relatório de termos de busca **diariamente**. Toda busca irrelevante vira negativa no mesmo dia. É aqui que se salva mais dinheiro. |
| **8–14** | Estabilização | Termos 2×/semana. Ajustar CPC por keyword: subir onde há impressão sem posição, cortar onde há clique sem engajamento. |
| **15–21** | Qualidade | Revisar QS por keyword. Pausar QS ≤ 4. Checar taxa de conversão por ad group no GA4. |
| **22–30** | Primeira leitura real | Avaliar: quais ad groups geram contato? Qual CPA? Iniciar OCI (§11). Decidir sobre Onda 2. |

**Metas realistas de 30 dias** (nicho de baixo volume, domínio novo):
- 200–500 impressões qualificadas
- 25–60 cliques
- 2–6 contatos por WhatsApp
- Lista de negativas expandida de 382 → 430+
- **Objetivo real do mês 1: aprender quais termos convertem. Não é lucro — é sinal.**

---

## 15. Plano de 90 dias

| Fase | Semanas | Foco |
|---|---|---|
| **Consolidação** | 5–6 | Migrar para Maximize Conversions se ≥15 conversões. Congelar negativas que provaram valor. |
| **Onda 2** | 7–8 | Criar `/pericia-ambiental/` e `/pericia-combustiveis/` no site → lançar AG07 e AG08. (Já está no backlog de SEO — mesma tarefa, dois benefícios.) |
| **Qualificação** | 9–10 | OCI rodando com dados reais. Passar bidding a otimizar Lead Qualificado. Aqui a campanha muda de patamar. |
| **Expansão controlada** | 11–12 | Testar 1 ad group de Broad Match isolado, orçamento próprio, só se o resto estiver estável. Considerar ad group de Marca (barato, defende o nome). |
| **Revisão estratégica** | 13 | CPA por ad group vs. valor de caso. Cortar o que não paga. Dobrar no que paga. Decidir sobre escala de orçamento. |

**Critérios de decisão no dia 90:**

| Cenário | Ação |
|---|---|
| CPA por caso < 15% do valor médio de contrato | Escalar orçamento agressivamente |
| CPA entre 15–35% | Manter, otimizar qualificação |
| CPA > 35% | Reduzir aos 2–3 ad groups de melhor desempenho |
| Zero conversões em 90 dias com estrutura correta | **Problema não é a campanha** — é demanda de busca ou proposta. Reavaliar canal (LinkedIn/parcerias com escritórios podem ser superiores). |

---

## 16. O que eu faria diferente se fosse meu dinheiro

1. **Não subiria nenhum ad group novo antes de corrigir os 5 bloqueadores.** Estrutura boa em cima de configuração errada só faz perder dinheiro mais rápido e de forma mais organizada.

2. **Trataria a lista de negativas como o ativo mais valioso da conta** — mais que as keywords. Neste nicho, as três armadilhas semânticas (pensão alimentícia, assistência técnica de eletrodoméstico, consulta de NCM) podem consumir sozinhas todo o orçamento.

3. **Priorizaria o OCI acima de qualquer otimização de lance.** Otimizar para clique em WhatsApp é otimizar para a métrica errada. Todo o resto é ajuste fino comparado a isso.

4. **Aceitaria gastar pouco no início.** Uma campanha que gasta R$ 40/dia com 3 leads qualificados vale infinitamente mais que uma que gasta R$ 184/dia com 15 cliques de estudante. **O objetivo não é gastar o orçamento — é não desperdiçá-lo.**

5. **Construiria as duas landing pages que faltam antes de expandir keywords.** Elas destravam dois ad groups, melhoram o QS e servem ao SEO orgânico ao mesmo tempo.

---

*Documento gerado em 2026-08-04. Auditoria da conta 249-917-2899 feita ao vivo via Google Ads API. Todas as alegações de credencial usadas nos anúncios são verificáveis em adrianarezende.com.br.*
