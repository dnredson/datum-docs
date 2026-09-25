# Contributing to DATUM documentation

Write the main documentation in English. Use canonical terminology and distinguish the reference model, the prototype contract, implementation status and validation evidence.

## Editorial rules

- Organize navigation around reader tasks and concepts. Keep phase numbers in status and provenance pages.
- Explain a concept before listing its wire fields. Use one practical example and link to the pinned contract.
- State whether an example is conceptual, an integration fixture or a reproduced live scenario.
- Never infer readiness from a configured broker, a running container or an old Healthy observation.
- Preserve D-Graph as the placement-free application graph, D-Map as placement authority, and D-Monitor as observation.
- Keep implementation secrets, credentials, internal endpoints, personal data and machine-specific logs out of published pages.
- Do not copy ADRs into a second editable source. Add pinned links and explanations instead.

## Updating the source baseline

1. Inspect the target commit in the implementation repository.
2. Review the code, relevant ADR sections and associated validation evidence.
3. Change `source-baseline.json`, then update every pinned source link and affected page in the same pull request.
4. Label unexecuted tests as source-inspected or previously reported; never claim a fresh run.
5. Run the validation commands below. CI must pass before merging the documentation change.

```bash
python scripts/check_docs.py
zensical build --clean --strict
python scripts/check_site.py
```

Documentation changes do not require a branch, commit or push in the runtime repository. Maintainers review content through this repository's pull requests. GitHub branch protection must be configured separately if mandatory review is desired.
