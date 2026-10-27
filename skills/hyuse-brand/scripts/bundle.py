"""Inline local CSS and images so each brand page opens as one self-contained file.

Usage: python3 bundle.py <brand dir> <output dir> [--embed-fonts]

With --embed-fonts, remote stylesheets (Google Fonts, icon fonts) are fetched once
and inlined with their font files as data URIs, so a page renders the brand type
even where the viewer cannot reach the network. Only the latin, latin-ext, and
vietnamese subsets of Google Fonts are kept.
"""
import base64, os, re, sys, urllib.parse, urllib.request

MIME = {".svg": "image/svg+xml", ".png": "image/png", ".woff2": "font/woff2"}
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
KEEP_SUBSETS = {"latin", "latin-ext", "vietnamese"}
_cache = {}


def fetch(url):
    if url not in _cache:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            _cache[url] = r.read()
    return _cache[url]


def data_uri(path):
    ext = os.path.splitext(path)[1]
    return f"data:{MIME[ext]};base64," + base64.b64encode(open(path, "rb").read()).decode()


def remote_css(url):
    """A remote stylesheet with its fonts inlined as woff2 data URIs."""
    css = fetch(url).decode("utf-8")
    if "fonts.googleapis.com" in url:
        blocks = re.findall(r"/\* ([\w-]+) \*/\s*(@font-face \{.*?\})", css, re.S)
        css = "\n".join(b for subset, b in blocks if subset in KEEP_SUBSETS)
    # keep only the woff2 source in multi format src lists
    css = re.sub(r'src:\s*(url\([^)]*\.woff2[^)]*\)\s*format\(["\']woff2["\']\))(?:\s*,\s*url\([^)]*\)\s*format\([^)]*\))*',
                 r"src: \1", css)
    def font(m):
        u = urllib.parse.urljoin(url, m.group(1).strip("'\""))
        return "url(data:font/woff2;base64," + base64.b64encode(fetch(u)).decode() + ")"
    return re.sub(r"url\(([^)]+\.woff2[^)]*)\)", font, css)


def css_text(path, remote):
    """Read a stylesheet, inlining local @imports and collecting remote ones."""
    text = open(path, encoding="utf-8").read()
    def imp(m):
        url = m.group(1)
        if url.startswith("http"):
            remote.append(url); return ""
        return css_text(os.path.normpath(os.path.join(os.path.dirname(path), url)), remote)
    text = re.sub(r'@import url\("([^"]+)"\);', imp, text)
    def local_url(m):
        u = m.group(1)
        if u.startswith(("data:", "http")): return m.group(0)
        p = os.path.normpath(os.path.join(os.path.dirname(path), u))
        return f'url("{data_uri(p)}")' if os.path.exists(p) else m.group(0)
    return re.sub(r'url\(([^)"\']+\.(?:svg|png))\)', local_url, text)


def flat(href):
    """Links between pages point at the flattened copies in OUT."""
    return "templates.html" if href.endswith("templates/index.html") else os.path.basename(href)


def bundle(src, out_dir, name, embed):
    base = os.path.dirname(src)
    html = open(src, encoding="utf-8").read()
    remote = []
    def link(m):
        href = m.group(1) or m.group(2)
        if href.startswith("http"):
            remote.append(href); return ""
        return f"<style>\n{css_text(os.path.normpath(os.path.join(base, href)), remote)}\n</style>"
    html = re.sub(r'<link rel="stylesheet" href="([^"]+)">|<link href="([^"]+)" rel="stylesheet">', link, html)
    html = re.sub(r'<link rel="preconnect"[^>]*>\n?', "", html)
    urls = list(dict.fromkeys(remote))
    if embed:
        head = "".join(f"<style>\n{remote_css(u)}\n</style>\n" for u in urls)
    else:
        head = "".join(f'<link rel="stylesheet" href="{u}">\n' for u in urls)
    html = html.replace("<style>", head + "<style>", 1)
    def img(m):
        p = os.path.normpath(os.path.join(base, m.group(2)))
        return f'{m.group(1)}="{data_uri(p)}"' if os.path.exists(p) else m.group(0)
    html = re.sub(r'(src|href)="((?:\.\./)?(?:logo/)[^"]+\.(?:svg|png))"', img, html)
    html = re.sub(r'href="((?:\.\./)?(?:templates/)?[a-z-]+\.html)"', lambda m: f'href="{flat(m.group(1))}"', html)
    out = os.path.join(out_dir, name)
    open(out, "w", encoding="utf-8").write(html)
    external = re.findall(r'(?:src|href)="(https?:[^"]+)"|url\((https?:[^)]+)\)', html)
    print(f"{name}: {os.path.getsize(out)//1024} KB, external refs: {len(external)}")


def main(argv):
    if len(argv) < 2:
        print(__doc__.strip()); return 1
    brand, out_dir, embed = argv[0], argv[1], "--embed-fonts" in argv
    os.makedirs(out_dir, exist_ok=True)
    bundle(os.path.join(brand, "board.html"), out_dir, "board.html", embed)
    tdir = os.path.join(brand, "templates")
    for f in sorted(os.listdir(tdir)):
        if f.endswith(".html"):
            bundle(os.path.join(tdir, f), out_dir, "templates.html" if f == "index.html" else f, embed)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
