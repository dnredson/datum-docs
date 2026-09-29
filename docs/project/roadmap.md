# Documentation roadmap

This roadmap tracks **documentation work**, not an implementation promise. Runtime capability status must remain grounded in the implementation repository and its evidence.

| Increment | Documentation outcome | Evidence boundary | State |
|---|---|---|---|
| Foundations | Concepts, architecture, D-Graph/D-Map/DMonitor/readiness and source provenance | Historical pinned source/evidence checkpoints | Complete |
| D-Code / DCompile | WebAssembly background, D-Code ABI/runtime, DScript→DCompile, immutable revision identity, exact DServer→D-Node flow | Phase 119I source + Phase 117 live/closure lineage | Complete |
| Existing-service modeling | Explain how container/native software becomes a `ServiceArtifact`; concrete catalog examples | Phase 119I `ServiceArtifact` schema, native runtime, catalog | Complete |
| End-to-end operational deploy | Model → register/pin → D-Graph → D-Deploy → D-Map → reconcile authorization → node execution | Current Phase 119I source; docs build does not rerun physical deployment | Complete as source-derived tutorial |
| Migration lifecycle | Target acceptance/realization, governed source cleanup, rollback as new transition | Phase 119I independent migration closure | Complete |
| Dashboard information model | Map existing authority/evidence domains into UI views without introducing a competing persisted truth | Dashboard phase implementation/design evidence when available | **Next documentation increment / planned** |
| Generated API/schema reference | Machine-generated OpenAPI/schema material tied to implementation | Generation pipeline + compatibility policy | Planned |
| Release editions | Separate stable/release docs from development baseline | Actual versioned release + compatibility policy | Planned |

## Dashboard preparation already present

The documentation now uses a UI-friendly lifecycle vocabulary:

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

These are **derived documentation concepts**, not a new canonical DATUM state enum. The dashboard phase should preserve the architecture by deriving each visual state from its owning source of truth:

- artifact registry for registered/execution identity;
- D-Deploy/D-Map for proposal/acceptance/placement;
- operational authorization/context for current reconciliation permission;
- node/runtime reports for physical realization;
- DMonitor/evidence interpretation for observed health/readiness;
- migration history/current authority for source cleanup obligations.

That separation should make the dashboard more useful: it can show exactly *where* a deployment is waiting instead of flattening everything into one `deployed` flag.

## Documentation evidence rule

Source-inspected tutorials may explain current control flow and commands, but a statement such as “clean-host end-to-end deployment reproduced” requires captured runtime evidence from that scenario. The documentation site should continue distinguishing source-derived instructions from newly executed validation.
