#!/usr/bin/env python3
"""SEO-054: every legal claim in /classificacao-fiscal-ncm/#reforma-tributaria
checked against the page and against LC 214/2025 on Planalto (struck text removed).
No network -> SKIP and exit 1."""
import html, re, sys, urllib.request

PAGE = "classificacao-fiscal-ncm/index.html"
PLANALTO = "https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm"

# (article, text that must follow it in the law, annex) — same rows as the page table
ROWS = [
    ("125", "reduzidas a zero as alíquotas do IBS e da CBS", "Anexo I"),
    ("135", "reduzidas em 60% (sessenta por cento)", "Anexo VII"),
    ("136", "reduzidas em 60% (sessenta por cento)", "Anexo VIII"),
    ("148", "reduzidas a zero as alíquotas do IBS e da CBS", "Anexo XV"),
]
LAW_SNIPPETS = [
    "aprovada pela Resolução Gecex nº 272, de 19 de novembro de 2021",   # art. 492, I
    "não afetarão as disposições a eles aplicadas com base na classificação anterior",  # § 2º
    "a CBS será cobrada mediante aplicação da alíquota de 0,9%",       # art. 346
    "o IBS será cobrado mediante aplicação da alíquota estadual de 0,1%",  # art. 343
    "reduzida em 0,1 (um décimo) ponto percentual",                    # art. 347
    "no código 1905.90.90 da NCM/SH",                                  # Anexo I, pão francês
    "Margarina do código 1517.10.00 da NCM/SH",                        # Anexo I
]

errors = []
norm = lambda t: re.sub(r"\s+", " ", t)

page = norm(open(PAGE, encoding="utf-8").read())
sec = page.split('id="reforma-tributaria"', 1)
if len(sec) != 2:
    sys.exit("FAIL: âncora #reforma-tributaria ausente")
sec = sec[1].split("<h2", 1)[0]
cells = re.findall(r"<tr> <td>([^<]*)</td> <td>Art\. (\d+)</td> <td>(Anexo [IVX]+)</td> </tr>", sec)
if [(a, n) for _, a, n in cells] != [(a, n) for a, _, n in ROWS]:
    errors.append(f"tabela da página difere da fonte: {cells}")
for s in ("1905.90.90", "1517.10.00", "0,9%", "0,1%", "Gecex nº 272/2021", 'href="/rotulagem-alimentos/"'):
    if s not in sec:
        errors.append(f"página sem '{s}'")
if '"dateModified": "2026-09-13"' not in page:
    errors.append("dateModified não atualizado")

try:
    req = urllib.request.Request(PLANALTO, headers={"User-Agent": "Mozilla/5.0"})
    raw = urllib.request.urlopen(req, timeout=120).read().decode("cp1252", "replace")
except Exception as e:
    print(f"SKIP: Planalto inacessível ({e})")
    sys.exit(1)
raw = re.sub(r"<strike>.*?</strike>", "", raw, flags=re.S | re.I)
law = norm(html.unescape(re.sub(r"<[^>]+>", " ", raw)))

for art, text, annex in ROWS:
    m = re.search(rf"Art\. {art}\. (.{{0,400}})", law)
    if not m or text not in m.group(1) or f"{annex} desta Lei" not in m.group(1):
        errors.append(f"art. {art}: '{text}' / '{annex}' não confere no Planalto")
for s in LAW_SNIPPETS:
    if norm(s) not in law:
        errors.append(f"Planalto sem: {s}")

if errors:
    print("FAIL"); print("\n".join("  · " + e for e in errors)); sys.exit(1)
print("OK — 4 linhas da tabela e 7 trechos conferidos na página e no Planalto")
