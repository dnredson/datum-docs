# Documentation roadmap

This roadmap describes the documentation work, not a promise that a runtime capability has been implemented.

| Increment | Outcome | Required evidence | State |
|---|---|---|---|
| Initial edition | Concepts, architecture, D1 readiness, source provenance and local integration entry point | Pinned D1 source inspection | Complete |
| D2 documentation | Provider-specific `any_element` algorithm, findings, API and integration entry point | Accepted/reviewed D2 implementation and source test | Complete in this edition |
| Runtime onboarding | Source installation, component configuration, artifact/D-Graph authoring and basic governed D-Deploy walkthrough | Pinned source inspection now; fresh clean-environment reproduction still required for a runtime-verified claim | Source-derived tutorial complete; reproduction pending |
| Live scenario | Fog/cloud tutorial with current runtime evidence | Completed Phase 114E validation | Gated on 114E; 114E0 preflight is next |
| Expanded reference | Entity/identity encyclopedia, canonical contracts, current control-plane API and complete mounted route catalog | Pinned extraction and consistency checks | Substantial baseline reference complete; generated schemas still planned |
| Release editions | Separate release documentation from development | An actual versioned release and compatibility policy | Planned |

The site intentionally keeps source ADRs and canonical implementation types in their original repository. It expands explanation without creating parallel editable contract definitions.

The runtime-onboarding tutorial deliberately distinguishes three different milestones: **accepted placement authority**, **runtime realization**, and **fresh runtime evidence/readiness**. A successful D-Deploy acceptance is not documented as proof that a container/process/WASM has actually run.

The next runtime-facing evidence gate remains Phase 114E: do not publish a live fog/cloud tutorial from D2 fixture evidence or source inspection alone. Once 114E is validated, add the scenario with the exact source revision, environment, commands and captured evidence used for that validation.
