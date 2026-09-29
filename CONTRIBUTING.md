# Contributing to DATUM documentation

Write the main documentation in English. Use canonical DATUM terminology and distinguish architecture, current implementation behavior, validation evidence and planned work.

## Editorial rules

- Organize navigation around reader tasks and concepts.
- Present the product/documentation line as **DATUM v1**. Do not expose internal numbered development phases or stages in public prose.
- Preserve version identifiers that are part of real contracts or APIs, such as `/api/v1`, `datum.dgraph/1`, DMap/1, DMap/2, D1/D2 readiness and `datum-dnode/0`.
- When something does not exist yet, say **not implemented yet**, **planned**, or **will be added**.
- Explain a concept before listing its wire fields. Prefer practical examples linked to pinned source.
- State whether an example is conceptual, source-derived, an integration fixture or a reproduced live scenario.
- Never infer readiness from a configured broker, a running container or an old Healthy observation.
- Preserve D-Graph as the placement-free application graph, D-Map as placement authority, and DMonitor as observation/evidence.
- Keep implementation secrets, credentials, internal-only data and machine-specific logs out of published pages.
- Do not copy ADRs into a second editable source. Add pinned links and explanations instead.

## Updating the source revision

1. Inspect the target commit in the implementation repository.
2. Review the code, relevant ADRs and associated validation evidence.
3. Change `source-baseline.json`, then update affected pinned source links and claims in the same pull request.
4. Label unexecuted tests as source-inspected or previously reported; never claim a fresh run.
5. Run the validation commands below. CI must pass before merging the documentation change.

```bash
python scripts/check_docs.py
zensical build --clean --strict
python scripts/check_site.py
```

Documentation changes do not require modifying the runtime repository. Maintainers review content through this repository's pull requests.
