# Documentation roadmap

This roadmap describes the documentation work, not a promise that a runtime capability has been implemented.

| Increment | Outcome | Required evidence | State |
|---|---|---|---|
| Initial edition | Concepts, architecture, D1 readiness, source provenance and local integration entry point | Pinned D1 source inspection | Complete |
| D2 documentation | Provider-specific `any_element` algorithm, findings, API and integration entry point | Accepted/reviewed D2 implementation and source test | Complete in this edition |
| Runtime onboarding | Verified prerequisites and a minimal installation walkthrough | Fresh reproduction in a clean supported environment | Planned |
| Live scenario | Fog/cloud tutorial with current runtime evidence | Completed Phase 114E validation | Gated on 114E; 114E0 preflight is next |
| Expanded reference | More APIs and generated schema material | Pinned extraction and consistency checks | Planned |
| Release editions | Separate release documentation from development | An actual versioned release and compatibility policy | Planned |

The site intentionally keeps source ADRs in their original repository. It can expand the explanation without creating parallel editable contract definitions.

The next runtime-facing documentation gate is Phase 114E: do not publish a live fog/cloud tutorial from D2 fixture evidence alone. Once 114E is validated, add the scenario with the exact source revision, environment, commands and captured evidence used for that validation.
