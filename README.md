# DATUM documentation

Independent documentation for DATUM, built with **Zensical + Markdown**.

This repository contains explanatory documentation and publication tooling. Implementation, canonical contracts and Architecture Decision Records remain in `dnredson/datum`.

**DATUM v1 source revision:** `c08ccc4d715d9eb76644e3f1bd7d80a7945265c4`. See [status](docs/overview/status.md) and [source provenance](docs/reference/sources.md).

The documentation is organized around reader tasks and product concepts rather than internal development milestones. Source links are pinned to immutable full commit SHAs for reproducibility. When a capability is not implemented yet, the documentation says so directly instead of referring to an internal roadmap number.

## Preview locally

Python 3.12 is the documentation build environment.

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python scripts/check_docs.py
zensical serve
```

To produce the static site:

```bash
zensical build --clean --strict
python scripts/check_site.py
```

## Publish

The `Documentation` workflow checks pull requests. Pushes to `main` build and publish to GitHub Pages. The configured destination is `https://dnredson.github.io/datum-docs/`.

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md). Update `source-baseline.json` deliberately when documenting a newer implementation revision and reconcile current-status claims in the same change. Historical evidence links may remain pinned to the exact source revision they document.

No new content license is selected in this repository. Existing project branding retains its original provenance; see [NOTICE.md](NOTICE.md).
