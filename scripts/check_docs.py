"""Check authored navigation, source baseline and local Markdown link targets."""
import json
from pathlib import Path
import re
import tomllib
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
config = tomllib.loads((ROOT / 'zensical.toml').read_text())
baseline = json.loads((ROOT / 'source-baseline.json').read_text())
errors = []
seen = set()

def visit(value):
    if isinstance(value, str):
        if not urlsplit(value).scheme:
            seen.add(value)
            if not (DOCS / value).is_file():
                errors.append(f'Navigation target missing: {value}')
    elif isinstance(value, list):
        for item in value:
            visit(item)
    elif isinstance(value, dict):
        for item in value.values():
            visit(item)

visit(config['project']['nav'])
sha = baseline['commit']
if not re.fullmatch(r'[0-9a-f]{40}', sha):
    errors.append('Baseline must be a full commit SHA')
source_prefix = f"https://github.com/{baseline['repository']}/blob/"
for path in DOCS.rglob('*.md'):
    relative = path.relative_to(DOCS).as_posix()
    if relative not in seen:
        errors.append(f'Page not in navigation: {relative}')
    text = path.read_text()
    for found in re.finditer(re.escape(source_prefix) + r'([^/\s)]+)/', text):
        if found.group(1) != sha:
            errors.append(f'{relative}: source link does not match baseline')
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    for target in re.findall(r'\]\(([^)\s]+)', text):
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith(('#', '//')):
            continue
        local = (path.parent / unquote(parsed.path)).resolve()
        if not local.is_file():
            errors.append(f'{relative}: missing local link {target}')
for path in [ROOT / 'overrides/main.html', ROOT / 'docs/overview/status.md', ROOT / 'README.md']:
    if sha[:12] not in path.read_text():
        errors.append(f'{path.name}: missing current baseline marker')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'OK: {len(seen)} navigation pages; local Markdown links and baseline {sha[:12]}')
