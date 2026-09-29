# Sources and provenance

The current documentation baseline is **dnredson/datum** commit `c08ccc4d715d9eb76644e3f1bd7d80a7945265c4`, the Phase 119I independent migration closure commit. Source review for this documentation increment took place on 2026-09-29.

## Provenance policy

Current claims should be checked against the current baseline. Historical pages are allowed to retain links to earlier evidence checkpoints when those links explain the implementation state that was actually reviewed at the time.

Every implementation source link must therefore be pinned to a **full 40-character commit SHA**. Links to `main`, moving branches or short SHAs are rejected by documentation CI. This preserves historical honesty without making old evidence appear newer than it is.

## Phase 119I current-source trail

The current WebAssembly/D-Code/software-component documentation was inspected against these source files at the Phase 119I baseline:

- [Phase 119I independent closure review](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/documentation/reference/phase119i-independent-final-migration-closure-review.md)
- [canonical D-Script](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/dserver/src/core/canonical_dscript.rs)
- [production DCompile API](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/dserver/src/api/dcompile.rs)
- [DCompile production submission/result](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/dserver/src/core/dcompile_submission.rs)
- [canonical D-Serv artifact](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/dserver/src/core/dserv_artifact.rs)
- [D-Code HTTP API](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/dserver/src/api/dcode.rs)
- [D-Code authorization](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/dserver/src/core/dcode_authorization.rs)
- [D-Code governed client preflight](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/DATUM/src/dcode/client.rs)
- [D-Code ABI](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/DATUM/src/dcode/abi.rs)
- [D-Code Wasmtime runtime](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/DATUM/src/dcode/runtime.rs)
- [D-Code local module store](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/DATUM/src/dcode/module_store.rs)
- [D-Code worker isolation](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/DATUM/src/dcode/worker.rs)

## External standards

WebAssembly background is linked to primary project/specification material:

- [WebAssembly official site](https://webassembly.org/)
- [WebAssembly specifications](https://webassembly.github.io/spec/)
- [WebAssembly Core Specification](https://webassembly.github.io/spec/core/)

These sources define WebAssembly itself. DATUM-specific statements about ABI, zero imports, artifact identity, exact-revision authorization and process isolation come from the pinned implementation sources above.

## Historical source links

Existing DMonitor, DForward, readiness and early source-to-deploy pages include links pinned to the earlier Phase 114D2 commit. Those remain immutable historical references. They are not interpreted as evidence that no implementation work occurred after 114D2.

When a historical page is substantively refreshed for current behavior, its claims and links should be moved to the then-current source baseline together.

## Verification boundary

The documentation build checks navigation, local links, immutable source pins and site rendering. It does not rerun the implementation repository's Rust test suite or physical RPi/fog/cloud evidence. Runtime outcomes referenced from Phase 117/119 are therefore implementation-repository evidence, not new experiments performed by the docs pipeline.

`source-baseline.json` records the current implementation anchor and known open boundaries. The site banner, README and status page carry the same short baseline marker.
