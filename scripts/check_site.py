"""Validate rendered local URLs and fragment targets, including project subpaths."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
import tomllib

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'
base = tomllib.loads((ROOT / 'zensical.toml').read_text())['project']['site_url']
base_url = urlsplit(base)

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids = set()
        self.urls = []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag == 'a' and attrs.get('href'):
            self.urls.append(attrs['href'])
        if tag in ('img', 'script') and attrs.get('src'):
            self.urls.append(attrs['src'])
        if tag == 'link' and attrs.get('rel') == 'stylesheet' and attrs.get('href'):
            self.urls.append(attrs['href'])

pages = {p: Page(p.read_text()) for p in SITE.rglob('*.html')}
errors = []
if not (SITE / 'index.html').is_file():
    errors.append('No built index.html')
for path, page in pages.items():
    relative = path.relative_to(SITE).as_posix()
    page_url = urljoin(base, relative[:-10] if relative.endswith('index.html') else relative)
    for href in page.urls:
        if href.startswith('#'):
            # Theme controls use same-page # targets that need not be content IDs.
            continue
        url = urlsplit(urljoin(page_url, href))
        if (url.scheme, url.netloc) != (base_url.scheme, base_url.netloc):
            continue
        if not url.path.startswith(base_url.path):
            errors.append(f'{relative}: URL escapes project prefix: {href}')
            continue
        dest = SITE / unquote(url.path[len(base_url.path):])
        if dest.is_dir():
            dest /= 'index.html'
        if not dest.is_file():
            errors.append(f'{relative}: missing built target: {href}')
        elif url.fragment and dest in pages and unquote(url.fragment) not in pages[dest].ids:
            errors.append(f'{relative}: missing target fragment: {href}')
if errors:
    raise SystemExit('\n'.join(sorted(set(errors))))
print(f'OK: local rendered links/assets across {len(pages)} HTML pages')
