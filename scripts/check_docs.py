"""Check authored navigation, immutable source links, public version language and local links."""
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
if baseline.get('version') != 'v1':
    errors.append("source-baseline.json must expose public version 'v1'")
if 'checkpoint' in baseline:
    errors.append("source-baseline.json must not expose an internal checkpoint label")

# Internal development numbering is intentionally not part of public DATUM
# vocabulary. Catch prose forms ("Phase 119I"), compact source-link/file forms
# ("phase119i"), and equivalent Stage spellings. Technical schema/version
# identifiers such as datum.dgraph/1 or schema_version=0.2.0 are unaffected.
internal_milestone = re.compile(r'\b(?:phase|stage)[ _-]?\d+[A-Za-z0-9._-]*', re.IGNORECASE)

source_prefix = f"https://github.com/{baseline['repository']}/blob/"
for path in DOCS.rglob('*.md'):
    relative = path.relative_to(DOCS).as_posix()
    if relative not in seen:
        errors.append(f'Page not in navigation: {relative}')
    text = path.read_text()
    for match in internal_milestone.finditer(text):
        errors.append(f"{relative}: internal milestone label is public: {match.group(0)!r}")
    # Every implementation link must remain immutable. Branch names such as
    # main or feature refs are rejected; only full 40-character SHAs are
    # accepted as source provenance.
    for found in re.finditer(re.escape(source_prefix) + r'([^/\s)]+)/', text):
        if not re.fullmatch(r'[0-9a-f]{40}', found.group(1)):
            errors.append(f'{relative}: source link is not pinned to a full commit SHA')
    text_without_code = re.sub(r'```.*?```', '', text, flags=re.S)
    for target in re.findall(r'\]\(([^)\s]+)', text_without_code):
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith(('#', '//')):
            continue
        local = (path.parent / unquote(parsed.path)).resolve()
        if not local.is_file():
            errors.append(f'{relative}: missing local link {target}')

# Check other public/user-facing repository surfaces too, so the site banner,
# repository landing page and contribution material cannot reintroduce internal
# milestone labels even if they are outside docs/*.md.
public_extra_files = [
    ROOT / 'README.md',
    ROOT / 'CONTRIBUTING.md',
    ROOT / 'NOTICE.md',
    ROOT / 'source-baseline.json',
    ROOT / 'zensical.toml',
]
public_extra_files.extend((ROOT / 'overrides').rglob('*.html'))
for path in public_extra_files:
    if not path.is_file():
        continue
    text = path.read_text()
    for match in internal_milestone.finditer(text):
        errors.append(
            f"{path.relative_to(ROOT).as_posix()}: internal milestone label is public: {match.group(0)!r}"
        )

for path in [ROOT / 'overrides/main.html', ROOT / 'docs/overview/status.md', ROOT / 'README.md']:
    if sha[:12] not in path.read_text():
        errors.append(f'{path.name}: missing current baseline marker')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'OK: DATUM v1; {len(seen)} navigation pages; local links; immutable source pins; no internal milestones; baseline {sha[:12]}')
