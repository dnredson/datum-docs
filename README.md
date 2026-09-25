# DATUM documentation

Independent documentation for DATUM, built with **Zensical + Markdown**.

This repository contains explanatory documentation and publication tooling. Implementation, canonical contracts and Architecture Decision Records remain in `dnredson/datum`.

**Development baseline:** `c059c3341c7901eeea77ce4881bbd341580d8aef` (Phase 114D1). This is a feature-branch checkpoint, not a stable release. See [status](docs/overview/status.md) and [source provenance](docs/reference/sources.md).

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

The workflow needs no access token for the private implementation repository. Source links are pinned, but no private checkout or runtime deployment happens in CI.

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md). Update `source-baseline.json` deliberately when documenting a newer implementation revision; reconcile the pages and source links in the same change.

No new content license is selected in this scaffold. Existing project branding retains its original provenance; see [NOTICE.md](NOTICE.md).
