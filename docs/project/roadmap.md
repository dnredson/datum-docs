# Documentation roadmap

This roadmap tracks **DATUM v1 documentation**, not an implementation promise. Runtime capability status remains grounded in implementation source and evidence.

| Increment | Documentation outcome | State |
|---|---|---|
| Foundations | Concepts, architecture, D-Graph/D-Map/DMonitor/readiness and provenance | Complete |
| D-Code / DCompile | WebAssembly background, ABI/runtime, D-Script→D-Compile, immutable revision identity, DServer→D-Node flow | Complete |
| Existing-service modeling | Explain how container/native software becomes a `ServiceArtifact`; concrete catalog examples | Complete |
| End-to-end operational deploy | Model → register/pin → D-Graph → D-Deploy → D-Map → authorize → node execution | Complete as source-derived tutorial |
| Migration lifecycle | Target acceptance/realization, governed source cleanup and rollback as a new transition | Complete |
| Dashboard information model | Map existing authority/evidence domains into UI views without introducing competing persisted truth | **Planned / next major increment** |
| Generated API/schema reference | Machine-generated OpenAPI/schema material tied to implementation | Planned |
| Packaged installation | Distribution/installer workflow beyond source builds | Not implemented yet |
| Fully reproduced multi-machine guide | Captured clean-environment runtime workflow across real nodes | Planned |

## Dashboard preparation already present

The documentation uses a UI-friendly lifecycle vocabulary:

```text
Modeled
→ Registered
→ Execution identity complete
→ Proposed
→ Accepted
→ Assigned
→ Authorized
→ Realized
→ Observed
→ Healthy
→ Ready
```

Migration can additionally expose **cleanup pending/completed** for an old source node.

These are derived documentation concepts, not a new canonical DATUM state enum. The planned dashboard should derive each visual state from its owning source of truth:

- artifact registry for registered/execution identity;
- D-Deploy/D-Map for proposal/acceptance/placement;
- operational authorization/context for reconciliation permission;
- node/runtime reports for physical realization;
- DMonitor/evidence interpretation for observed health/readiness;
- migration history/current authority for source cleanup obligations.

## Documentation evidence rule

Source-inspected tutorials may explain current control flow and commands, but a statement such as “clean-host end-to-end deployment reproduced” requires captured runtime evidence from that scenario. The site must continue distinguishing source-derived instructions from newly executed validation.
