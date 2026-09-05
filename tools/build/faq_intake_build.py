# -*- coding: utf-8 -*-
"""Insere (ou reescreve) a entrada de FAQ de intake — visível e em JSON-LD.

Idempotente nas duas pontas:
  - no HTML, o bloco vive entre marcadores e é substituído em cada execução;
  - no JSON-LD, a entrada é localizada pelo `name` da pergunta e substituída;
    se não existir, é acrescentada ao fim de `mainEntity`.

As duas pontas saem da MESMA string (`faq_intake.answer`). É a décima aplicação
do método da SEO-037, e a razão de ele existir: paridade de FAQ garantida por
construção, não por conferência posterior.
"""
import html as _html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from faq_intake import ENTRIES, answer, question

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MARK_A, MARK_B = "<!-- faqintake:start -->", "<!-- faqintake:end -->"


def close_of_container(doc, start):
    """Índice do `</div>` que fecha `<div class="faq">`, contando aninhamento.

    Regex não serve: o contêiner guarda um `<div>` por pergunta, e `.*?</div>`
    para no primeiro deles — o mesmo erro que a SEO-039 encontrou no contador
    de perguntas do seo-report.
    """
    depth = 0
    for m in re.finditer(r"<div\b[^>]*>|</div>", doc[start:]):
        depth += 1 if m.group(0) != "</div>" else -1
        if depth == 0:
            return start + m.start()
    raise SystemExit("contêiner .faq sem fechamento")


def visible_block(slug):
    return (f'{MARK_A}\n'
            f'      <div>\n'
            f'        <h3>{question(slug)}</h3>\n'
            f'        <p>{answer(slug)}</p>\n'
            f'      </div>\n'
            f'      {MARK_B}\n      ')


def json_entry(slug):
    """A mesma pergunta e a mesma resposta, sem entidades HTML e com escape JSON."""
    name = json.dumps(_html.unescape(question(slug)), ensure_ascii=False)
    text = json.dumps(_html.unescape(answer(slug)), ensure_ascii=False)
    return ('      {\n'
            '        "@type": "Question",\n'
            f'        "name": {name},\n'
            '        "acceptedAnswer": {\n'
            '          "@type": "Answer",\n'
            f'          "text": {text}\n'
            '        }\n'
            '      }')


def apply_visible(doc, slug):
    if MARK_A in doc:
        return re.sub(re.escape(MARK_A) + r".*?" + re.escape(MARK_B) + r"\n      ",
                      lambda _: visible_block(slug), doc, flags=re.S)
    start = doc.find('<div class="faq">')
    if start == -1:
        raise SystemExit(f"{slug}: contêiner <div class=\"faq\"> não encontrado")
    end = close_of_container(doc, start)
    return doc[:end] + visible_block(slug) + doc[end:]


def mainentity_close(block, start):
    """Índice do `]` que fecha `mainEntity`, por balanceamento de colchetes.

    Procurar o fecho por texto (`\n    ]`) reprova em página cuja indentação de
    JSON-LD é diferente — quatro das vinte usam outra —, e o erro é silencioso:
    a entrada nova cai FORA do objeto e o JSON deixa de ser parseável.
    """
    depth = 0
    for i in range(start, len(block)):
        if block[i] == "[":
            depth += 1
        elif block[i] == "]":
            depth -= 1
            if depth == 0:
                return i
    raise SystemExit("mainEntity sem fechamento")


def apply_json(doc, slug):
    i = doc.find('"@type": "FAQPage"')
    if i == -1:
        raise SystemExit(f"{slug}: FAQPage não encontrado")
    j = doc.find("</script>", i)
    block = doc[i:j]
    entry = json_entry(slug)
    name_key = '"name": ' + json.dumps(_html.unescape(question(slug)), ensure_ascii=False)
    if name_key in block:
        # Entrada já existe: substituir do `{` que a abre até o `}` que a fecha.
        k = block.rfind("      {\n", 0, block.find(name_key))
        end = block.find("\n      }", k) + len("\n      }")
        new_block = block[:k] + entry + block[end:]
    else:
        open_at = block.index("[", block.index('"mainEntity"'))
        tail = mainentity_close(block, open_at)
        # Recuar até o início da linha do `]`, para preservar a indentação dela.
        line = block.rfind("\n", 0, tail)
        new_block = block[:line] + ",\n" + entry + block[line:]
    return doc[:i] + new_block + doc[j:]


def apply(slug):
    path = os.path.join(ROOT, slug, "index.html")
    doc = open(path, encoding="utf-8").read()
    out = apply_json(apply_visible(doc, slug), slug)
    # Nunca escrever JSON-LD quebrado: os quatro layouts de indentação do site
    # não são iguais, e um erro de inserção só apareceria no Rich Results.
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', out, re.S):
        try:
            json.loads(b)
        except Exception as e:
            raise SystemExit(f"{slug}: JSON-LD inválido após a inserção — {e}")
    if out == doc:
        return False
    open(path, "w", encoding="utf-8").write(out)
    return True


if __name__ == "__main__":
    for slug in sorted(ENTRIES):
        print(("escrito     " if apply(slug) else "sem mudança ") + slug)
