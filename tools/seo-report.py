#!/usr/bin/env python3
"""Daily SEO guard + report for adrianarezende.com.br.

Run this FIRST in every SEO execution:

    /usr/bin/python3 tools/seo-report.py

Sections, in the order the daily mandate needs them:

  [deploy]  Is the repository actually live? Unpushed commits, pages missing
            from the published sitemap, and HTTP status of every live URL.
            The site is served by GitHub Pages from origin/main, so a commit
            without a push is a silent no-op (this is SEO-021).
  [valid]   On-page validation of the local files: title/description length,
            og/twitter parity, canonical, single h1, JSON-LD parses, internal
            links resolve, sitemap matches the filesystem, no orphan pages.
  [gsc]     Search Console: 28-day page/query performance and the index
            coverage state of every page (needs the service account).
  [ga4]     Sessions by page and channel, to tell "nobody arrives" apart from
            "they arrive and leave". Skipped when no GA4 property is resolved.

Pass section names to run a subset: `seo-report.py deploy valid`.

Interpreter: use /usr/bin/python3 — the Google client libraries are installed
there, not in the Homebrew pythons. Only [gsc] needs them; [deploy] and
[valid] are stdlib-only and run anywhere.

Exit code is 1 if any check fails, so this can gate a publish.
"""

import glob
import html
import json
import os
import re
import subprocess
import sys
import urllib.request
from collections import defaultdict

SITE = "https://adrianarezende.com.br"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Service-account keys, in the order to try. Three paths because three separate
# runs each created their own; any one of them works.
CRED_PATHS = [os.path.expanduser(p) for p in (
    "~/.config/claude-seo/google-api.json",
    "~/.config/claude-seo/service-account.json",
    "~/.config/adrianarezende/seo-sa.json",
)]
# GA4 property behind the tag G-NL5HWSTKPF (SEO-007). Override with $GA4_PROPERTY.
GA4_PROPERTY = os.environ.get("GA4_PROPERTY", "548153325")
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly",
          "https://www.googleapis.com/auth/analytics.readonly"]

# SERP display limits. Descriptions shorter than MIN read as truncated stubs;
# longer than MAX get cut mid-sentence. See SEO-016.
TITLE_MAX = 60
DESC_MIN, DESC_MAX = 150, 160

failures = []


def fail(section, msg):
    failures.append(f"[{section}] {msg}")
    print(f"  FAIL  {msg}")


def ok(msg):
    print(f"  ok    {msg}")


def head(title):
    print(f"\n{'=' * 66}\n{title}\n{'=' * 66}")


def get(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": "seo-report/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read().decode("utf-8", "replace")


def status(url, timeout=20):
    req = urllib.request.Request(url, method="HEAD",
                                 headers={"User-Agent": "seo-report/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return f"ERR {e}"


def local_pages():
    """Every page in the repo as a site-root path: '/', '/sobre/', ..."""
    pages = ["/"] if os.path.exists(os.path.join(ROOT, "index.html")) else []
    for p in sorted(glob.glob(os.path.join(ROOT, "*", "index.html"))):
        d = os.path.basename(os.path.dirname(p))
        if d in ("tools", "google-ads-import", "Google Ads", ".git", ".claude"):
            continue
        pages.append(f"/{d}/")
    return pages


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def page_file(page):
    return os.path.join(ROOT, "index.html" if page == "/" else page.strip("/"), "index.html") \
        if page != "/" else os.path.join(ROOT, "index.html")


# --------------------------------------------------------------------------
# [deploy]
# --------------------------------------------------------------------------

def section_deploy():
    head("[deploy] repositório × site publicado")

    fetch = subprocess.run(["git", "fetch", "-q", "origin"], cwd=ROOT,
                           capture_output=True, text=True)
    if fetch.returncode != 0:
        fail("deploy", f"git fetch falhou: {fetch.stderr.strip() or fetch.returncode}")

    log = subprocess.run(["git", "log", "--oneline", "origin/main..HEAD"],
                         cwd=ROOT, capture_output=True, text=True)
    if log.returncode != 0:
        # Never report "em dia" because git itself broke — that is the exact
        # silent success this guard exists to prevent (SEO-021).
        fail("deploy", f"git log falhou, estado de publicação DESCONHECIDO: "
                       f"{log.stderr.strip() or log.returncode}")
    elif log.stdout.strip():
        for line in log.stdout.strip().splitlines():
            fail("deploy", f"commit sem push: {line}")
        print("        → publicar com: git push origin main")
    else:
        ok("0 commits pendentes de push")

    dirty = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT,
                           capture_output=True, text=True).stdout.strip()
    tracked = [l for l in dirty.splitlines() if not l.startswith("??")]
    if tracked:
        fail("deploy", f"{len(tracked)} arquivo(s) rastreado(s) modificado(s) sem commit")

    try:
        _, xml = get(f"{SITE}/sitemap.xml")
    except Exception as e:
        fail("deploy", f"sitemap publicado inacessível: {e}")
        return
    live = {u.replace(SITE, "") or "/" for u in re.findall(r"<loc>([^<]+)</loc>", xml)}
    repo = set(local_pages())

    for p in sorted(repo - live):
        fail("deploy", f"página no repositório e ausente do sitemap publicado: {p}")
    for p in sorted(live - repo):
        fail("deploy", f"URL no sitemap publicado sem página no repositório: {p}")
    if repo == live:
        ok(f"sitemap publicado em dia — {len(live)} páginas")

    bad = [(p, s) for p in sorted(live) if (s := status(SITE + p)) != 200]
    for p, s in bad:
        fail("deploy", f"{p} responde {s} (esperado 200)")
    if not bad:
        ok(f"{len(live)} URLs respondendo 200 ao vivo")


# --------------------------------------------------------------------------
# [valid]
# --------------------------------------------------------------------------

def meta(doc, **attrs):
    for tag in re.findall(r"<meta\b[^>]*>", doc, re.I):
        if all(re.search(rf'{k}\s*=\s*"{re.escape(v)}"', tag, re.I) for k, v in attrs.items()):
            m = re.search(r'content\s*=\s*"([^"]*)"', tag, re.I)
            if m:
                return html.unescape(m.group(1))
    return None


def text_of(fragment):
    """Visible text. Drops <script>/<style> bodies first — stripping only the
    tags would leave the JSON-LD itself in the text, which makes any
    "is this in the visible text?" check pass unconditionally."""
    fragment = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", " ", fragment, flags=re.S | re.I)
    return " ".join(html.unescape(re.sub(r"<[^>]*>", " ", fragment)).split())


def check_faq_parity(label, doc, parsed):
    """Every visible FAQ question must exist in FAQPage, and vice versa.

    A schema question with no visible counterpart is what Google treats as
    hidden structured data; a visible question missing from the schema simply
    forfeits the rich result. The site has required this parity since SEO-003,
    but it was verified by throwaway scripts — so a FAQ could be extended
    without the schema and nothing would notice.
    """
    entries = []
    def walk(node):
        if isinstance(node, list):
            for n in node:
                walk(n)
        elif isinstance(node, dict):
            if node.get("@type") == "FAQPage":
                for e in node.get("mainEntity", []) or []:
                    if isinstance(e, dict) and e.get("name"):
                        ans = (e.get("acceptedAnswer") or {}).get("text", "")
                        entries.append((" ".join(html.unescape(e["name"]).split()),
                                        text_of(html.unescape(ans))))
            for v in node.values():
                if isinstance(v, (list, dict)):
                    walk(v)
    walk(parsed)

    # The visible FAQ runs from the container to the end of its <section>.
    # Slice by index rather than a non-greedy regex: the container holds nested
    # <div>s, and `.*?</div>` stops at the first one, silently under-counting.
    start = doc.find('<div class="faq">')
    visible = []
    if start != -1:
        end = doc.find("</section>", start)
        block = doc[start:end if end != -1 else len(doc)]
        visible = [text_of(q) for q in re.findall(r"<h3[^>]*>(.*?)</h3>", block, re.S)]

    if not entries and not visible:
        return

    # What Google actually requires: the question and its answer must be on the
    # page. Match on a prefix — whitespace and inline markup make a full-string
    # comparison brittle. This direction is the one that carries a penalty, so
    # it runs on every page regardless of how the FAQ is marked up.
    # Fail only when NEITHER the question nor the answer is on the page — that
    # is hidden structured data. A heading worded more briefly than the schema
    # question ("Em que tipos de processo atua?" vs "...Adriana Rezende atua?")
    # is normal copywriting, not a defect, so requiring both to match would
    # bury the real finding under noise.
    page_text = text_of(doc)
    for name, answer in entries:
        if name[:40] not in page_text and not (answer[:60] and answer[:60] in page_text):
            fail("valid", f"{label}: FAQPage oculto — nem a pergunta nem a resposta "
                          f"aparecem na página: {name[:55]!r}")

    # The reverse direction — a FAQ extended in the HTML but not in the schema —
    # only forfeits a rich result, and can only be counted where the markup
    # actually delimits the FAQ. The home page renders its FAQ without the
    # container, so counting there would be a false alarm, not a finding.
    if visible and len(visible) != len(entries):
        fail("valid", f"{label}: {len(visible)} perguntas visíveis × {len(entries)} no FAQPage")


def section_valid():
    head("[valid] validação on-page dos arquivos locais")

    pages = local_pages()
    titles = defaultdict(list)
    all_targets = set()

    for page in pages:
        doc = read(page_file(page))
        label = page

        m = re.search(r"<title>(.*?)</title>", doc, re.S | re.I)
        title = html.unescape(m.group(1).strip()) if m else None
        if not title:
            fail("valid", f"{label}: sem <title>")
        else:
            titles[title].append(label)
            if len(title) > TITLE_MAX:
                fail("valid", f"{label}: title com {len(title)} caracteres (máx {TITLE_MAX})")

        desc = meta(doc, name="description")
        if not desc:
            fail("valid", f"{label}: sem meta description")
        elif not (DESC_MIN <= len(desc) <= DESC_MAX):
            fail("valid", f"{label}: description com {len(desc)} caracteres "
                          f"(faixa {DESC_MIN}–{DESC_MAX})")

        for prop, attrs in (("og:title", {"property": "og:title"}),
                            ("twitter:title", {"name": "twitter:title"})):
            val = meta(doc, **attrs)
            if val is None:
                fail("valid", f"{label}: sem {prop}")
            elif title and val != title:
                fail("valid", f"{label}: {prop} difere do <title>")

        m = re.search(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"', doc, re.I)
        expected = SITE + page
        if not m:
            fail("valid", f"{label}: sem canonical")
        elif m.group(1) != expected:
            fail("valid", f"{label}: canonical {m.group(1)} (esperado {expected})")

        h1 = re.findall(r"<h1\b", doc, re.I)
        if len(h1) != 1:
            fail("valid", f"{label}: {len(h1)} elementos <h1> (esperado 1)")

        blocks = re.findall(
            r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>', doc, re.S | re.I)
        if not blocks:
            fail("valid", f"{label}: sem JSON-LD")
        parsed = []
        for i, b in enumerate(blocks, 1):
            try:
                parsed.append(json.loads(b))
            except json.JSONDecodeError as e:
                fail("valid", f"{label}: JSON-LD #{i} não parseia — {e}")

        check_faq_parity(label, doc, parsed)

        for href in re.findall(r'href="(/[^"#?]*)', doc):
            all_targets.add(href if href.endswith("/") or "." in os.path.basename(href)
                            else href + "/")

    for title, where in titles.items():
        if len(where) > 1:
            fail("valid", f"title duplicado em {', '.join(where)}: {title!r}")

    known = set(pages)
    for t in sorted(all_targets):
        if t in known:
            continue
        if os.path.exists(os.path.join(ROOT, t.strip("/"))):
            continue
        fail("valid", f"link interno quebrado: {t}")

    linked = {t for t in all_targets if t in known}
    for p in pages:
        if p != "/" and p not in linked:
            fail("valid", f"página órfã (nenhum link interno aponta para ela): {p}")

    xml = read(os.path.join(ROOT, "sitemap.xml"))
    in_map = {u.replace(SITE, "") or "/" for u in re.findall(r"<loc>([^<]+)</loc>", xml)}
    for p in sorted(set(pages) - in_map):
        fail("valid", f"página fora do sitemap.xml local: {p}")
    for p in sorted(in_map - set(pages)):
        fail("valid", f"sitemap.xml local aponta para página inexistente: {p}")

    if not failures:
        ok(f"{len(pages)} páginas — todas as checagens passaram")
    else:
        print(f"  ({len(pages)} páginas verificadas)")


# --------------------------------------------------------------------------
# [gsc]
# --------------------------------------------------------------------------

def credentials():
    """Service-account credentials, or None with the reason printed."""
    try:
        from google.oauth2 import service_account
    except ImportError:
        print("  pulado — bibliotecas Google ausentes neste interpretador.")
        print("  Rode com /usr/bin/python3 (é onde elas estão instaladas).")
        return None
    for path in CRED_PATHS:
        if os.path.exists(path):
            data = json.load(open(path))
            if data.get("type") == "service_account":
                return service_account.Credentials.from_service_account_info(
                    data, scopes=SCOPES)
    print("  pulado — nenhuma service account em: " + ", ".join(CRED_PATHS))
    return None


def gsc_property(sc):
    """Ask Search Console which property this account can read, instead of
    assuming the sc-domain: form — assuming it caused a 403 on 2026-08-05."""
    host = SITE.split("//", 1)[1]
    for e in sc.sites().list().execute().get("siteEntry", []):
        if host in e["siteUrl"]:
            print(f"  propriedade: {e['siteUrl']} ({e['permissionLevel']})")
            return e["siteUrl"]
    fail("gsc", f"a service account não tem acesso a nenhuma propriedade de {host}")
    return None


def section_gsc(days=28):
    head(f"[gsc] Search Console — últimos {days} dias")
    creds = credentials()
    if not creds:
        return
    from googleapiclient.discovery import build

    import datetime
    sc = build("searchconsole", "v1", credentials=creds, cache_discovery=False)
    site = gsc_property(sc)
    if not site:
        return
    end = datetime.date.today()
    start = end - datetime.timedelta(days=days)

    def query(dims, limit=100):
        body = {"startDate": str(start), "endDate": str(end),
                "dimensions": dims, "rowLimit": limit, "type": "web"}
        return sc.searchanalytics().query(siteUrl=site, body=body).execute().get("rows", [])

    for label, dims in (("páginas", ["page"]), ("consultas", ["query"])):
        rows = query(dims)
        clicks = sum(r["clicks"] for r in rows)
        impr = sum(r["impressions"] for r in rows)
        print(f"\n  -- {label}: {len(rows)} linhas · {clicks} cliques · {impr} impressões --")
        for r in sorted(rows, key=lambda r: -r["impressions"])[:25]:
            key = " | ".join(r["keys"]).replace(SITE, "")
            print(f'    {key:52.52} c={r["clicks"]:<4} i={r["impressions"]:<5} '
                  f'ctr={r["ctr"] * 100:5.1f}%  pos={r["position"]:5.1f}')

    print("\n  -- indexação --")
    for page in local_pages():
        try:
            r = sc.urlInspection().index().inspect(body={
                "inspectionUrl": SITE + page, "siteUrl": site,
                "languageCode": "pt-BR"}).execute()
            idx = r["inspectionResult"]["indexStatusResult"]
            state, verdict = idx.get("coverageState"), idx.get("verdict")
            line = f"    {page:36.36} {verdict:6} {state}"
            print(line)
            if verdict != "PASS":
                fail("gsc", f"{page} não indexada: {state}")
        except Exception as e:
            fail("gsc", f"{page}: inspeção falhou — {e}")


# --------------------------------------------------------------------------
# [ga4]
# --------------------------------------------------------------------------

def section_ga4(days=28):
    head(f"[ga4] sessões — últimos {days} dias")
    if not GA4_PROPERTY:
        print("  pulado — nenhuma propriedade GA4 configurada ($GA4_PROPERTY)")
        return
    creds = credentials()
    if not creds:
        return

    import datetime
    import google.auth.transport.requests as gt
    s = gt.AuthorizedSession(creds)
    end = datetime.date.today()
    start = end - datetime.timedelta(days=days)
    r = s.post(
        f"https://analyticsdata.googleapis.com/v1beta/properties/{GA4_PROPERTY}:runReport",
        json={"dateRanges": [{"startDate": str(start), "endDate": str(end)}],
              "dimensions": [{"name": "pagePath"}, {"name": "sessionDefaultChannelGroup"}],
              "metrics": [{"name": "sessions"}], "limit": 50})
    if r.status_code != 200:
        fail("ga4", f"HTTP {r.status_code}: {r.text[:200]}")
        return
    rows = r.json().get("rows", [])
    total = sum(int(x["metricValues"][0]["value"]) for x in rows)
    # pagePath, not landingPage: this shows which content gets consumed. One
    # session that views three pages produces three rows, so DO NOT read the
    # row count or this total as a session count — it double-counts. Use
    # landingPagePlusQueryString when you need sessions. (Misread on 2026-08-11:
    # 4 pagePath rows were reported as "4 organic sessions"; there were 2.)
    print(f"  {len(rows)} linhas · {total} sessões-página (≠ sessões)")
    for row in rows:
        page, channel = (v["value"] for v in row["dimensionValues"])
        print(f'    {page:40.40} {channel:22.22} {row["metricValues"][0]["value"]:>5}')
    if not rows:
        print("    (nenhuma sessão — consistente com 0 cliques no Search Console)")


# --------------------------------------------------------------------------

SECTIONS = {"deploy": section_deploy, "valid": section_valid,
            "gsc": section_gsc, "ga4": section_ga4}

if __name__ == "__main__":
    wanted = [a for a in sys.argv[1:] if a in SECTIONS] or list(SECTIONS)
    for name in wanted:
        SECTIONS[name]()

    head("resumo")
    if failures:
        print(f"{len(failures)} falha(s):")
        for f in failures:
            print(f"  · {f}")
        sys.exit(1)
    print("ALL PASS")
