#!/usr/bin/env python3
"""SEO-060 — verifica a seção "Surto" de /pericia-contaminacao-alimentos/.

Cada afirmação técnica da seção é conferida contra a fonte primária, ao vivo:
  · manual de vigilância epidemiológica de DTHA (Ministério da Saúde, 2021)
  · RDC nº 216/2004 (ANVISA)
  · Portaria SES/RS nº 799/2023

Sem rede, sai com 1 — a verificação é o ponto, não a conveniência.
"""
import io, json, re, sys, subprocess, tempfile, os, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, "pericia-contaminacao-alimentos", "index.html")
MANUAL = ("https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/"
          "doencas-transmitidas-por-alimentos-dta/manual_dtha_2021_web.pdf")
RDC216 = ("https://www.saude.al.gov.br/wp-content/uploads/2020/06/"
          "RDC-N%C2%B0-216-ANVISA-Ag%C3%AAncia-Nacional-de-Vigil%C3%A2ncia-Sanit%C3%A1ria.pdf")
RS799 = "https://www.estado.rs.gov.br/upload/arquivos/portaria-ses-799-2023.pdf"

fails = []
def fail(m): fails.append(m); print(f"  FAIL  {m}")
def ok(m):   print(f"  ok    {m}")

def norm(t):
    return re.sub(r"\s+", " ", t).strip()

def pdftext(url):
    with urllib.request.urlopen(urllib.request.Request(
            url, headers={"User-Agent": "verify-surto/1.0"}), timeout=90) as r:
        data = r.read()
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
        f.write(data); path = f.name
    try:
        out = subprocess.run(["pdftotext", "-layout", path, "-"],
                             capture_output=True, text=True, check=True).stdout
    finally:
        os.unlink(path)
    return norm(out)

html = io.open(PAGE, encoding="utf-8").read()
flat = norm(re.sub(r"<[^>]+>", " ", html))

# ---------------------------------------------------------------- estrutura
print("\n== estrutura ==")
if '<h2 id="surto">Surto: quando o alimento suspeito já foi comido</h2>' in html:
    ok("seção presente com âncora #surto")
else:
    fail("seção/âncora #surto ausente")

# a seção tem de vir DEPOIS da cadeia de custódia e ANTES das normas
i_cad = html.find("Cadeia de custódia da amostra")
i_sur = html.find('id="surto"')
i_nor = html.find("<h2>Normas técnicas aplicáveis</h2>")
if -1 not in (i_cad, i_sur, i_nor) and i_cad < i_sur < i_nor:
    ok("posição: custódia < surto < normas")
else:
    fail(f"posição errada (cad={i_cad} surto={i_sur} normas={i_nor})")

# FAQ de intake continua sendo a última (invariante das SEO-045/046)
qs = re.findall(r"<h3>([^<]+)</h3>", html)
if qs and qs[-1].startswith("Que documentos são necessários"):
    ok("FAQ de intake segue em último lugar")
else:
    fail(f"FAQ de intake não é a última (última: {qs[-1] if qs else '—'})")

# ------------------------------------------------------------ paridade JSON
print("\n== paridade FAQ visível × JSON-LD ==")
blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
faq = next((json.loads(b) for b in blocks if json.loads(b).get("@type") == "FAQPage"), None)
if faq is None:
    fail("FAQPage ausente")
else:
    vis = dict(re.findall(r"<h3>([^<]+)</h3>\s*<p>(.*?)</p>", html, re.S))
    for q in faq["mainEntity"]:
        name, text = q["name"], q["acceptedAnswer"]["text"]
        if name not in vis:
            fail(f"pergunta só no JSON-LD: {name[:60]}")
        elif norm(re.sub(r"<[^>]+>", "", vis[name])) != norm(text):
            fail(f"resposta divergente visível × JSON-LD: {name[:60]}")
    ok(f"{len(faq['mainEntity'])} perguntas conferidas")

# ------------------------------------------------------------------- fontes
print("\n== fontes primárias (ao vivo) ==")
try:
    man = pdftext(MANUAL)
except Exception as e:
    fail(f"manual DTHA inacessível: {e}"); man = None

if man:
    # 1) a ressalva que sustenta o box "O ponto que decide muitos casos"
    if ("inconclusivos para encerramento dos surtos" in man
            and "alimentos similares preparados nas mesmas condições" in man):
        ok("manual: amostra similar é inconclusiva para encerramento do surto")
    else:
        fail("manual: ressalva sobre amostra similar NÃO encontrada")
    if "inconclusivos para o encerramento do surto" not in flat:
        fail("página não traz a ressalva de inconclusividade")
    else:
        ok("página declara a inconclusividade")

    # 2) hierarquia de amostras alternativas
    for termo in ("amostras de controle de qualidade armazenadas no local de produção",
                  "embalagens e utensílios"):
        if termo in man: ok(f"manual: '{termo[:46]}'")
        else: fail(f"manual: '{termo[:46]}' não encontrado")

    # 3) risco relativo e taxas de ataque
    if "Taxa de ataque" in man and "Risco relativo" in man:
        ok("manual: taxa de ataque e risco relativo")
    else:
        fail("manual: medidas de associação não encontradas")
    for leitura in ("RR =1: ausência de associação",
                    "RR <1: sugere que o fator estudado não apresenta risco",
                    "RR >1: sugere que há associação"):
        if leitura in man: ok(f"manual: {leitura[:40]}")
        else: fail(f"manual: leitura de RR ausente — {leitura[:40]}")
    # a página tem de reproduzir a MESMA leitura, com o MESMO significado.
    # Conferir só a presença de "RR > 1" deixaria passar a leitura invertida
    # (controle negativo 2 de 19/09, que o verificador não pegou na 1ª versão).
    leituras = ((r"RR &gt; 1:\s*associação, fator de risco", "RR > 1 = associação/fator de risco"),
                (r"RR = 1:\s*ausência de associação",        "RR = 1 = ausência de associação"),
                (r"RR &lt; 1:\s*fator de proteção",          "RR < 1 = fator de proteção"))
    for rx, rotulo in leituras:
        if re.search(rx, html): ok(f"página: {rotulo}")
        else: fail(f"página: leitura errada ou ausente — {rotulo}")
    # e não pode afirmar o contrário em lugar nenhum
    for rx, rotulo in ((r"RR &gt; 1:\s*ausência", "RR > 1 descrito como ausência de associação"),
                       (r"RR &lt; 1:\s*fator de risco", "RR < 1 descrito como fator de risco"),
                       (r"RR = 1:\s*(associação|fator)", "RR = 1 descrito como associação")):
        if re.search(rx, html): fail(f"leitura de RR invertida: {rotulo}")
    # fórmula do RR
    if "TA1 ÷ TA2" in flat: ok("página: RR = TA1 ÷ TA2")
    else: fail("página não traz a fórmula do RR")

# 4) definição de surto — duas ou mais pessoas, mesma origem.
# Exigida nos DOIS lugares: corpo visível e JSON-LD. O controle negativo 4 de
# 19/09 alterou só uma das cópias e a 1ª versão do verificador não acusou.
corpo = norm(re.sub(r"<[^>]+>", " ", html[html.find('id="surto"'):html.find("Perguntas frequentes")]))
if "duas ou mais pessoas" in corpo and "mesma origem" in corpo:
    ok("corpo: definição de surto (2+ pessoas, mesma origem)")
else:
    fail("corpo: definição de surto incompleta")
if faq is not None:
    jtxt = norm(" ".join(q["acceptedAnswer"]["text"] for q in faq["mainEntity"]))
    if "duas ou mais pessoas" in jtxt and "mesma origem" in jtxt:
        ok("JSON-LD: definição de surto (2+ pessoas, mesma origem)")
    else:
        fail("JSON-LD: definição de surto incompleta")
if man and "duas ou mais pessoas" not in man.lower():
    fail("manual: definição de 2+ pessoas não confirmada na fonte")
elif man:
    ok("manual: definição de 2+ pessoas confirmada na fonte")
if "botulismo e cólera" in flat.lower() and "um único caso" in flat:
    ok("página: exceção de botulismo e cólera (caso único)")
else:
    fail("página: exceção de caso único ausente ou incompleta")

# 5) terminologia atual DTHA
if "DTHA" in flat and "Doenças de Transmissão Hídrica e Alimentar" in flat:
    ok("página: terminologia atual DTHA")
else:
    fail("página: terminologia DTHA ausente")

# 6) RDC 216/2004 — NÃO exige guarda de amostra; registros por 30 dias
try:
    rdc = pdftext(RDC216)
except Exception as e:
    fail(f"RDC 216 inacessível: {e}"); rdc = None
if rdc:
    if "amostra" not in rdc.lower():
        ok("RDC 216/2004: a palavra 'amostra' realmente não aparece")
    else:
        fail("RDC 216/2004 MENCIONA amostra — a afirmação da página caiu")
    if "mantidos por período mínimo de 30 (trinta) dias" in rdc:
        ok("RDC 216/2004, 4.11.3: registros por no mínimo 30 dias")
    else:
        fail("RDC 216/2004: prazo de 30 dias não confirmado")
    if "não exige guarda de amostras" in flat:
        ok("página: RDC 216 não exige guarda de amostras")
    else:
        fail("página não declara que a RDC 216 dispensa guarda de amostras")
    # O prazo tem de bater com a fonte em TODAS as ocorrências. Conferir só a
    # presença de "30 dias" deixaria passar uma cópia alterada (controle
    # negativo 5 de 19/09, não pego pela 1ª versão).
    achados = re.findall(r"(?:período |no )mínimo (?:de )?(\d+) dias", flat)
    if set(achados) == {"30"} and achados:
        ok(f"página: prazo de registros = 30 dias nas {len(achados)} ocorrências")
    else:
        fail(f"prazo de registros diverge da RDC 216 (encontrado: {sorted(set(achados)) or 'nenhum'}; esperado 30)")

# 7) Portaria SES/RS 799/2023 — 100 g/100 mL, 72 h, < 5 °C, item 10.17
try:
    rs = pdftext(RS799)
except Exception as e:
    fail(f"Portaria RS 799 inacessível: {e}"); rs = None
if rs:
    if "10.17. A coleta de amostras de todos os alimentos preparados e bebidas deve ser de 100g ou 100mL" in rs:
        ok("RS 799/2023, item 10.17: 100 g ou 100 mL")
    else:
        fail("RS 799/2023: item 10.17 não confere")
    if "armazenadas por 72 horas, sob refrigeração, em temperatura inferior a 5º C" in rs:
        ok("RS 799/2023: 72 h sob refrigeração < 5 °C")
    else:
        fail("RS 799/2023: prazo/temperatura não conferem")
    for frag in ("100 g ou 100 mL", "72 horas", "5 °C", "10.17"):
        if frag not in flat: fail(f"página não traz '{frag}'")
    if all(f in flat for f in ("100 g ou 100 mL", "72 horas", "5 °C", "10.17")):
        ok("página reproduz os parâmetros da RS 799/2023")

# 8) data de modificação coerente
print("\n== datas ==")
if '"dateModified": "2026-09-19"' in html and 'datetime="2026-09-19"' in html:
    ok("dateModified e <time> em 2026-09-19")
else:
    fail("datas de modificação inconsistentes")

print("\n" + "=" * 60)
if fails:
    print(f"{len(fails)} falha(s)"); sys.exit(1)
print("OK"); sys.exit(0)
