# DATUM documentation

Independent documentation for DATUM, built with **Zensical + Markdown**.

This repository contains explanatory documentation and publication tooling. Implementation, canonical contracts and Architecture Decision Records remain in `dnredson/datum`.

**Development baseline:** `c08ccc4d715d9eb76644e3f1bd7d80a7945265c4` (Phase 119I independent migration closure). This is a development checkpoint, not a stable release. See [status](docs/overview/status.md) and [source provenance](docs/reference/sources.md).

The documentation now includes a detailed WebAssembly/D-Code guide, the software-component identity model, DServer-to-D-Node governed execution flow, and a DCompile/D-Code API reference. Older pages may retain immutable links to historical source checkpoints when they document evidence from those checkpoints; CI requires every implementation link to be pinned to a full 40-character commit SHA.

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

Read [CONTRIBUTING.md](CONTRIBUTING.md). Update `source-baseline.json` deliberately when documenting a newer implementation revision and reconcile current-status claims in the same change. Historical evidence links may remain at their original immutable SHAs.

No new content license is selected in this scaffold. Existing project branding retains its original provenance; see [NOTICE.md](NOTICE.md).
