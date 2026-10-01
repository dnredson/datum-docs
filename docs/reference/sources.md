# Sources and provenance

The current DATUM v1 documentation is grounded in **dnredson/datum** commit `7a79bd84bc05a1ea18870715cc033567ff472afc`. Source review for this documentation revision took place on 2026-10-01.

## Provenance policy

Current claims should be checked against the current source revision. Evidence pages may retain links to earlier immutable revisions when those links document a validation that was actually produced against that source.

Every implementation source link must be pinned to a **full 40-character commit SHA**. Links to `main`, moving branches or short SHAs are rejected by documentation CI.

## v1 source trail — DATUM Console

- [Console package/runtime requirements](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/console/package.json)
- [Vite configuration](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/console/vite.config.ts)
- [client router](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/console/src/app/router.ts)
- [project workspace](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/console/src/pages/project-workspace.ts)
- [project graph](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/console/src/pages/project-graph.ts)
- [runtime graph model](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/console/src/pages/runtime-graph-model.ts)
- [graph visual semantics](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/console/src/components/graph-visuals.ts)
- [operations read API](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/dserver/src/api/operations.rs)

## v1 source trail — service catalog

- [catalog UI](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/console/src/pages/catalog.ts)
- [catalog API](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/dserver/src/api/service_catalog.rs)
- [catalog model and validation](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/dserver/src/core/service_catalog.rs)
- [ServiceArtifact registry](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/dserver/src/core/service_artifact_registry.rs)

## v1 source trail — software model and D-Code

- [canonical D-Script](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/dserver/src/core/canonical_dscript.rs)
- [DCompile API](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/dserver/src/api/dcompile.rs)
- [canonical D-Serv artifact](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/dserver/src/core/dserv_artifact.rs)
- [D-Code HTTP API](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/dserver/src/api/dcode.rs)
- [D-Code authorization](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/dserver/src/core/dcode_authorization.rs)
- [D-Code governed client](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/DATUM/src/dcode/client.rs)
- [D-Code runtime](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/DATUM/src/dcode/runtime.rs)

## v1 source trail — ServiceArtifact and node realization

- [ServiceArtifact HTTP API and OCI pinning](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/dserver/src/api/service_artifacts.rs)
- [operational reconciliation API](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/dserver/src/api/operational_dgraph.rs)
- [node reconciliation engine](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/DATUM/src/agent/operational_reconciliation.rs)
- [native executable acquisition](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/DATUM/src/agent/native_process_acquisition.rs)
- [native process runtime](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/DATUM/src/agent/native_process_runtime.rs)

Concrete artifact examples remain available in the implementation repository, including Mosquitto, PostgreSQL and the LoRa simulator.

## External standards

WebAssembly background uses primary project/specification material:

- [WebAssembly official site](https://webassembly.org/)
- [WebAssembly specifications](https://webassembly.github.io/spec/)
- [WebAssembly Core Specification](https://webassembly.github.io/spec/core/)

## Verification boundary

The documentation build checks navigation, local links, immutable implementation source pins, DATUM v1 public wording and static site rendering. It does **not** rerun the implementation repository's Rust or Console test suites or physical-node evidence.

The Console tutorial is source-derived from the pinned frontend/backend contracts. The docs CI does not start DServer and a browser during publication.

`source-baseline.json` records the current implementation anchor and open boundaries. The site banner, README and status page carry the same source revision marker.
