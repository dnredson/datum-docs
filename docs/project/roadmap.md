# Documentation roadmap

This roadmap tracks **DATUM v1 documentation**, not an implementation promise. Runtime capability status remains grounded in implementation source and evidence.

| Increment | Documentation outcome | State |
|---|---|---|
| Foundations | Concepts, architecture, D-Graph/D-Map/DMonitor/readiness and provenance | Complete |
| D-Code / DCompile | WebAssembly background, ABI/runtime, D-Script→D-Compile, immutable revision identity, DServer→D-Node flow | Complete |
| Existing-service modeling | Explain how container/native software becomes a `ServiceArtifact`; concrete examples | Complete |
| End-to-end operational deploy | Model → register/pin → D-Graph → D-Deploy → D-Map → authorize → node execution | Complete as source-derived tutorial |
| Migration lifecycle | Target acceptance/realization, governed source cleanup and rollback | Complete |
| DATUM Console foundations | Global overview, projects, scoped workspace and graphical navigation | Complete |
| Logical/runtime graph | Accepted logical graph plus separately typed admitted realization evidence | Complete |
| Service catalog | Immutable reusable atomic/composite definitions with exact artifact pins | Complete |
| Console placement/deploy/runtime/history workspaces | Dedicated graphical operational workflows | Not implemented yet |
| Guided service-modeling provider integration | Assisted draft generation with explicit operator control | Not part of the published source revision |
| Generated API/schema reference | Machine-generated OpenAPI/schema material tied to implementation | Planned |
| Packaged installation | Distribution/installer workflow beyond source builds | Not implemented yet |
| Fully reproduced multi-machine guide | Captured clean-environment runtime workflow across real nodes | Planned |

## Console evolution rule

Future graphical features should continue using the existing authority/evidence domains instead of creating a frontend-owned parallel state model.

A useful UI lifecycle remains:

```text
Modeled
→ Cataloged / artifact identified
→ Proposed
→ Accepted
→ Assigned
→ Authorized
→ Realized
→ Observed
→ Healthy
→ Ready
```

These are presentation concepts. Their facts belong to different registries, D-Deploy/D-Map, runtime authorization and DMonitor/readiness domains.

## Documentation evidence rule

Source-inspected tutorials may explain current control flow and commands, but a statement such as “clean-host end-to-end deployment reproduced” requires captured runtime evidence from that scenario. The site must continue distinguishing source-derived instructions from newly executed validation.
