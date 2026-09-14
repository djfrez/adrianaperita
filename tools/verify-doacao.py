#!/usr/bin/env python3
"""SEO-055: /prazo-validade-alimentos/#doacao checked against the page and
against Lei 15.224/2025 on Planalto (struck text removed). No network -> SKIP, exit 1."""
import html, re, sys, urllib.request

PAGE = "prazo-validade-alimentos/index.html"
PLANALTO = "https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15224.htm"

# (dispositivo shown on the page, text that must be in the law right after it)
ROWS = [
    ("Art. 14, caput", "Art. 14.", "dentro do prazo de validade"),
    ("Art. 14, § 1º", "§ 1º Os bancos de alimentos", "profissional legalmente habilitado que ateste a qualidade nutricional e sanitária"),
    ("Art. 14, § 2º", "§ 2º Os alimentos que não apresentarem", "compostagem agrícola ou à produção de biomassa"),
    ("Arts. 15 e 16", "Art. 16.", "apenas responderão civilmente por danos ocasionados pelos alimentos doados quando houver dolo"),
    ("Art. 17", "Art. 17.", "não configurará, em nenhuma hipótese, relação de consumo"),
]
LAW_SNIPPETS = [
    "LEI Nº 15.224, DE 30 DE SETEMBRO DE 2025",
    "Fica revogada a Lei nº 14.016, de 23 de junho de 2020",
    "exceção ao regime da responsabilidade objetiva disposto no art. 931",
    "arts. 12 e 13 da Lei nº 8.078",
    "nos termos do art. 392",
    "Esta Lei entra em vigor na data de sua publicação",
    "publicado no DOU de 1º.10.2025",
]

errors = []
norm = lambda t: re.sub(r"\s+", " ", t)
page = norm(open(PAGE, encoding="utf-8").read())
sec = page.split('id="doacao"', 1)
if len(sec) != 2:
    sys.exit("FAIL: âncora #doacao ausente")
sec = sec[1].split("<h2", 1)[0]
cells = re.findall(r"<tr> <td>[^<]*</td> <td>([^<]*)</td>", sec)
if cells != [r[0] for r in ROWS]:
    errors.append(f"tabela da página difere da fonte: {cells}")
for s in ('href="#cadeia-de-frio"', 'id="cadeia-de-frio"', 'href="/analise-microbiologica-alimentos/"', "14.016/2020", "art. 931", "dolo"):
    if s not in page:
        errors.append(f"página sem '{s}'")
if page.count("Uma empresa pode doar alimento perto do vencimento") != 2:
    errors.append("FAQ de doação não está no visível e no JSON-LD")
if '"dateModified": "2026-09-14"' not in page:
    errors.append("dateModified não atualizado")

try:
    req = urllib.request.Request(PLANALTO, headers={"User-Agent": "Mozilla/5.0"})
    raw = urllib.request.urlopen(req, timeout=120).read().decode("cp1252", "replace")
except Exception as e:
    print(f"SKIP: Planalto inacessível ({e})"); sys.exit(1)
raw = re.sub(r"<(script|style).*?</\1>|<strike>.*?</strike>", "", raw, flags=re.S | re.I)
law = norm(html.unescape(re.sub(r"<[^>]+>", " ", raw)))

for label, anchor, text in ROWS:
    i = law.find(anchor)
    if i < 0 or text not in law[i:i + 500]:
        errors.append(f"{label}: '{text}' não confere no Planalto")
for s in LAW_SNIPPETS:
    if s not in law:
        errors.append(f"Planalto sem: {s}")

if errors:
    print("FAIL"); print("\n".join("  · " + e for e in errors)); sys.exit(1)
print(f"OK — {len(ROWS)} linhas da tabela e {len(LAW_SNIPPETS)} trechos conferidos na página e no Planalto")
