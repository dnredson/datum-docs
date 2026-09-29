# DATUM documentation

Independent documentation for **DATUM v1**, built with **Zensical + Markdown**.

This repository contains explanatory documentation and publication tooling. Implementation, canonical contracts and Architecture Decision Records remain in `dnredson/datum`.

**DATUM v1 source baseline:** `c08ccc4d715d9eb76644e3f1bd7d80a7945265c4`. This is active development documentation rather than a packaged stable release. See [status](docs/overview/status.md) and [source provenance](docs/reference/sources.md).

The documentation includes a detailed WebAssembly/D-Code guide, the software-component identity model, DServer-to-D-Node governed execution flow, service-to-node deployment tutorials and a DCompile/D-Code API reference. Source links that support implementation claims are pinned to full 40-character commit SHAs so the documented behavior remains auditable as v1 evolves.

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

Open the local URL printed by Zensical. To produce the static site:

```bash
zensical build --clean --strict
python scripts/check_site.py
```

## Publish

The `Documentation` workflow checks pull requests. Pushes to `main` build and publish to GitHub Pages. In repository **Settings → Pages → Build and deployment**, select **GitHub Actions** before the first deployment. The configured destination is `https://dnredson.github.io/datum-docs/`; configuration alone does not mean deployment has succeeded.

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md). Update `source-baseline.json` deliberately when documenting a newer v1 implementation revision and reconcile current-status claims in the same change. Older evidence links may remain at their original immutable SHAs when the page is explicitly describing that evidence.

No new content license is selected in this scaffold. Existing project branding retains its original provenance; see [NOTICE.md](NOTICE.md).
