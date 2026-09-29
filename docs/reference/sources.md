# Sources and provenance

The current DATUM v1 documentation baseline is **dnredson/datum** commit `c08ccc4d715d9eb76644e3f1bd7d80a7945265c4`. Source review for the current documentation edition took place on 2026-09-29.

## Provenance policy

Current claims should be checked against the current baseline. Older pages may retain links to earlier evidence commits when those links explain the implementation state that was actually reviewed at the time.

Every implementation source link must be pinned to a **full 40-character commit SHA**. Links to `main`, moving branches or short SHAs are rejected by documentation CI. This preserves historical honesty without exposing internal development milestone numbering as part of the public product model.

## DATUM v1 source trail — software model and D-Code

Current WebAssembly/D-Code/software-component documentation was inspected against:

- [canonical D-Script](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/dserver/src/core/canonical_dscript.rs)
- [production DCompile API](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/dserver/src/api/dcompile.rs)
- [DCompile submission/result](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/dserver/src/core/dcompile_submission.rs)
- [canonical D-Serv artifact](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/dserver/src/core/dserv_artifact.rs)
- [D-Code HTTP API](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/dserver/src/api/dcode.rs)
- [D-Code authorization](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/dserver/src/core/dcode_authorization.rs)
- [D-Code governed client](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/DATUM/src/dcode/client.rs)
- [D-Code ABI](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/DATUM/src/dcode/abi.rs)
- [D-Code runtime](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/DATUM/src/dcode/runtime.rs)
- [local module store](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/DATUM/src/dcode/module_store.rs)
- [worker isolation](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/DATUM/src/dcode/worker.rs)

## DATUM v1 source trail — ServiceArtifact and node realization

The service-modeling/end-to-end tutorials additionally inspect:

- [ServiceArtifact registry, schema and validation](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/dserver/src/core/service_artifact_registry.rs)
- [ServiceArtifact HTTP API and OCI pinning route](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/dserver/src/api/service_artifacts.rs)
- [DServer route surface](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/dserver/src/main.rs)
- [operational D-Graph/authorization contract](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/dserver/src/core/operational_dgraph.rs)
- [operational reconciliation HTTP API](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/dserver/src/api/operational_dgraph.rs)
- [node reconciliation engine](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/DATUM/src/agent/operational_reconciliation.rs)
- [node reconciliation CLI](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/DATUM/src/bin/smartsentinel-operational-reconcile.rs)
- [native executable acquisition/materialization](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/DATUM/src/agent/native_process_acquisition.rs)
- [native process runtime](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/DATUM/src/agent/native_process_runtime.rs)
- [artifact bundle documentation](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/artifacts/README.md)

Concrete catalog examples cited by the tutorials:

- [Mosquitto](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/artifacts/catalog/mosquitto.json)
- [Mosquitto lab configuration](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/artifacts/config/mosquitto/mosquitto.conf)
- [ChirpStack PostgreSQL](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/artifacts/catalog/chirpstack-postgres.json)
- [LoRa device simulator](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/artifacts/catalog/lora-device-simulator.json)

## External standards

WebAssembly background uses primary project/specification material:

- [WebAssembly official site](https://webassembly.org/)
- [WebAssembly specifications](https://webassembly.github.io/spec/)
- [WebAssembly Core Specification](https://webassembly.github.io/spec/core/)

These sources define WebAssembly itself. DATUM-specific statements about ABI, zero imports, artifacts, authorization and process isolation come from the pinned implementation source.

## Older source links

Existing DMonitor, DForward, readiness and early source-to-deploy pages may include links pinned to implementation commit `3e0baa8f415b822f69eef86c0cbfe2a3681e3a65`. Those are immutable historical references to the code that supported those pages; they are not a separate public product version.

When an older page is substantively refreshed for current behavior, its claims and source links should be moved to the then-current DATUM v1 source baseline together.

## Verification boundary

The documentation build checks navigation, local links, immutable implementation source pins, public version terminology and static site rendering. It does **not** rerun the implementation repository's Rust test suite or physical RPi/fog/cloud evidence.

The service tutorials are source-derived. Their commands reflect current source contracts and checked-in artifacts, but the docs CI did not itself perform a fresh host deployment while publishing this edition.

`source-baseline.json` records the current implementation anchor and known open/planned boundaries. The site banner, README and status page carry the same baseline marker.
