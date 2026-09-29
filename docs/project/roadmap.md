# DATUM v1 roadmap

This roadmap separates what is already documented/implemented in DATUM v1 from capabilities that are planned. It intentionally avoids internal development milestone numbering.

## Available and documented in v1

| Area | Current documentation status |
|---|---|
| Core concepts | D-Application, D-Graph, D-Serv, D-Call, D-Continuum, D-Node, D-Map, DForward/DIoT, DMonitor and authority/evidence boundaries documented |
| DCompile and D-Code | WebAssembly background, ABI/runtime, D-Script → DCompile, immutable descriptor revisions, exact authorization and DServer → D-Node execution documented |
| Existing-service modeling | Container/native software → `ServiceArtifact`, including Mosquitto, PostgreSQL, local-build and native examples documented |
| Governed deployment | Model → register/pin → D-Graph → proposal → acceptance → D-Map → reconciliation authorization → node execution documented |
| Migration lifecycle | Target transition, source cleanup and rollback-as-new-transition documented |
| API/reference | Canonical contracts, control-plane APIs, complete route catalog and source provenance documented |

## Planned v1 increments

These capabilities or documentation increments are not presented as already complete. They will be added when implemented and/or validated.

| Planned increment | Intended outcome |
|---|---|
| **DATUM Console/dashboard** | Visual management of projects, artifacts, D-Graphs, placement proposals, accepted authority, runtime realization, evidence and readiness without introducing parallel authority |
| **Reproducible live multinode tutorial** | Fresh end-to-end fog/cloud or equivalent multinode validation with captured commands and evidence |
| **Production canonical D-Serv evidence path** | Complete production evidence generation/correlation for long-running D-Serv realizations where gaps remain |
| **Automated D-Code distribution** | Governed delivery of exact WASM content to a target D-Node instead of requiring explicit local installation |
| **Native package-manager acquisition** | Governed acquisition/provenance for packages/repositories such as `apt` rather than treating package installation as external preparation |
| **Authoritative node classification** | A canonical model that can make placement constraints such as fog/cloud classes verifiable instead of relying on free-text labels |
| **Generated API/schema reference** | Machine-generated OpenAPI/schema material tied directly to implementation |
| **Packaged installation/release workflow** | Installer/distribution and release documentation when a stable packaging policy exists |

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

These are **derived documentation concepts**, not a new canonical DATUM state enum. The DATUM Console should preserve the architecture by deriving each visual state from its owning source of truth:

- artifact registry for registered/execution identity;
- D-Deploy/D-Map for proposal/acceptance/placement;
- operational authorization/context for current reconciliation permission;
- node/runtime reports for physical realization;
- DMonitor/evidence interpretation for observed health/readiness;
- migration history/current authority for source cleanup obligations.

That separation should make the dashboard more useful: it can show exactly *where* a deployment is waiting instead of flattening everything into one `deployed` flag.

## Documentation evidence rule

Source-inspected tutorials may explain current control flow and commands, but a statement such as “clean-host end-to-end deployment reproduced” requires captured runtime evidence from that scenario. Planned capabilities are labeled as planned until implementation/evidence exists.
