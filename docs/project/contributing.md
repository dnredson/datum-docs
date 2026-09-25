# Contributing and documentation governance

This documentation has its own repository and publication cycle. Changes to prose, navigation and diagrams should be reviewed here without changing the runtime development worktree.

## Page pattern

A concept page should explain its purpose, represented information, producers/consumers, relationships, a concrete example and the corresponding pinned contract. A task guide should state prerequisites, commands, expected outcomes and validation limits.

Use English for the main pages. Keep canonical terms consistent and write phase-specific status in the status/provenance pages. Diagrams describe explicit relationships, not implied capabilities.

## Validation and publication

Local and CI validation check navigation, Markdown links, baseline references, the Zensical build and rendered internal links. Pull requests validate without publishing. Pushes to `main` publish after validation when GitHub Pages is configured for Actions.

The full contributor procedure lives in the repository's `CONTRIBUTING.md`. No workflow writes to the implementation repository or updates its branches.

## Source updates

A new implementation revision is a deliberate documentation change. Inspect its code and evidence, update `source-baseline.json`, revise affected claims and pinned links, and record what was actually validated. A newer commit alone does not prove a live scenario.
