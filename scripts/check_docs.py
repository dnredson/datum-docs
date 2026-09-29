"""Check navigation, immutable source links, DATUM v1 wording and local Markdown links."""
import json
from pathlib import Path
import re
import tomllib
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
config = tomllib.loads((ROOT / 'zensical.toml').read_text())
source_state = json.loads((ROOT / 'source-baseline.json').read_text())
errors = []
seen = set()

# Internal numbered development milestones are intentionally not public reader
# vocabulary. Real API/contract versions such as /api/v1, datum.dgraph/1,
# DMap/1, DMap/2 and D1/D2 are not matched by this rule.
internal_milestone = re.compile(r'\b(?:phase|stage)(?:\s+|-)\d+[a-z0-9._-]*\b', re.I)


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


def check_public_wording(path, label):
    text = path.read_text()
    prose = re.sub(r'```.*?```', '', text, flags=re.S)
    for found in internal_milestone.finditer(prose):
        errors.append(
            f"{label}: internal development label is not DATUM v1 public vocabulary: {found.group(0)!r}"
        )
    return text


visit(config['project']['nav'])
sha = source_state['commit']
if not re.fullmatch(r'[0-9a-f]{40}', sha):
    errors.append('Source revision must be a full commit SHA')
if source_state.get('documentation_version') != 'v1':
    errors.append("source-baseline.json: documentation_version must be 'v1'")

source_prefix = f"https://github.com/{source_state['repository']}/blob/"
for path in DOCS.rglob('*.md'):
    relative = path.relative_to(DOCS).as_posix()
    if relative not in seen:
        errors.append(f'Page not in navigation: {relative}')
    text = check_public_wording(path, relative)
    for found in re.finditer(re.escape(source_prefix) + r'([^/\s)]+)/', text):
        if not re.fullmatch(r'[0-9a-f]{40}', found.group(1)):
            errors.append(f'{relative}: source link is not pinned to a full commit SHA')
    prose = re.sub(r'```.*?```', '', text, flags=re.S)
    for target in re.findall(r'\]\(([^)\s]+)', prose):
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith(('#', '//')):
            continue
        local = (path.parent / unquote(parsed.path)).resolve()
        if not local.is_file():
            errors.append(f'{relative}: missing local link {target}')

for path in [ROOT / 'README.md', ROOT / 'CONTRIBUTING.md']:
    check_public_wording(path, path.name)

for path in [ROOT / 'overrides/main.html', ROOT / 'docs/overview/status.md', ROOT / 'README.md']:
    if sha[:12] not in path.read_text():
        errors.append(f'{path.name}: missing current source revision marker')

if errors:
    raise SystemExit('\n'.join(errors))
print(f'OK: {len(seen)} navigation pages; local Markdown links; immutable source pins; DATUM v1 wording; source revision {sha[:12]}')
