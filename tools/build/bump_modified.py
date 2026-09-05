# -*- coding: utf-8 -*-
"""Atualiza `dateModified` (schema) e o "Atualizado em" visível.

`check_dates` do seo-report exige que a data do schema apareça no texto
visível, e a razão registrada em SEO-027 é a que importa aqui: conteúdo que
cita norma vale o que vale a sua data, e um LLM decidindo se cita a página lê o
schema, não o log do git. Toda execução que acrescenta conteúdo tem de mexer
nas duas pontas — foi o que a SEO-045 deixou de fazer.

Uso: bump_modified.py AAAA-MM-DD slug [slug...]
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
       "agosto", "setembro", "outubro", "novembro", "dezembro"]


def extenso(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} de {MES[int(m) - 1]} de {y}"


def bump(slug, iso):
    path = os.path.join(ROOT, slug, "index.html")
    doc = open(path, encoding="utf-8").read()
    doc = re.sub(r'"dateModified": "\d{4}-\d{2}-\d{2}"',
                 f'"dateModified": "{iso}"', doc)
    # Só o <time> que vem depois de "Atualizado em" — o de publicação não muda.
    doc, n = re.subn(r'(Atualizado em <time datetime=")\d{4}-\d{2}-\d{2}("[^>]*>)[^<]*(</time>)',
                     lambda m: m.group(1) + iso + m.group(2) + extenso(iso) + m.group(3),
                     doc)
    if n != 1:
        raise SystemExit(f"{slug}: {n} ocorrências de 'Atualizado em <time>' — esperava 1")
    open(path, "w", encoding="utf-8").write(doc)


if __name__ == "__main__":
    iso, slugs = sys.argv[1], sys.argv[2:]
    for s in slugs:
        bump(s, iso)
        print(f"atualizado {s} → {iso}")
