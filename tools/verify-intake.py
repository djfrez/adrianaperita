# -*- coding: utf-8 -*-
"""Verificação estrita do bloco de intake (SEO-045)."""
import os, re, sys, html as H
sys.path.insert(0, "tools/build")
from intake import PAGES, LEDE, CLOSE

fails = []
for slug, items in sorted(PAGES.items()):
    p = f"{slug}/index.html"
    s = open(p, encoding="utf-8").read()
    cta = re.search(r'<section class="cta-sec">.*?</section>', s, re.S)
    if not cta: fails.append(f"{slug}: sem cta-sec"); continue
    cta = cta.group(0)
    blk = re.search(r'<!-- intake:start -->(.*?)<!-- intake:end -->', cta, re.S)
    if not blk: fails.append(f"{slug}: bloco de intake fora do cta-sec ou ausente"); continue
    blk = blk.group(1)
    # o bloco tem de vir ANTES dos botões
    if cta.index("intake:end") > cta.index('<div class="ctas">'):
        fails.append(f"{slug}: bloco depois dos botões")
    got = re.findall(r'<li>(.*?)</li>', blk, re.S)
    if got != items:
        fails.append(f"{slug}: itens divergem\n    esperado={items}\n    obtido  ={got}")
    for txt in (LEDE, CLOSE):
        if txt not in blk: fails.append(f"{slug}: texto fixo ausente: {txt[:40]}…")
    href = re.search(r'<a href="([^"]+)">Como a intimação', blk)
    if not href: fails.append(f"{slug}: link do andamento ausente"); continue
    h = href.group(1)
    target = "cpc-prova-pericial/index.html" if h.startswith("/cpc") else (
        "cpc-prova-pericial/index.html" if h == "#andamento" else None)
    if slug == "cpc-prova-pericial" and h != "#andamento":
        fails.append(f"{slug}: deve usar âncora local, usou {h}")
    if slug != "cpc-prova-pericial" and h != "/cpc-prova-pericial/#andamento":
        fails.append(f"{slug}: href errado: {h}")
    if 'id="andamento"' not in open(target, encoding="utf-8").read():
        fails.append(f"{slug}: destino #andamento não existe")
    if ".cta-sec .box" not in s:
        fails.append(f"{slug}: CSS .cta-sec .box ausente")

# nenhuma entidade HTML quebrada introduzida
for slug in PAGES:
    s = open(f"{slug}/index.html", encoding="utf-8").read()
    blk = re.search(r'<!-- intake:start -->(.*?)<!-- intake:end -->', s, re.S).group(1)
    for bad in re.findall(r'&(?!amp;|lt;|gt;|quot;|#\d+;|nbsp;|mdash;)\w*;?', blk):
        fails.append(f"{slug}: entidade suspeita {bad!r}")

print(f"páginas verificadas: {len(PAGES)}")
if fails:
    print("REPROVOU:"); [print("  -", f) for f in fails]; sys.exit(1)
print("OK — 20/20 blocos idênticos à fonte, dentro do cta-sec, antes dos botões, link válido")
