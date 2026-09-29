# Status and limitations

**Edition:** development. **Current documentation baseline:** Phase 119I, `c08ccc4d715d9eb76644e3f1bd7d80a7945265c4`. **Documentation review date:** 2026-09-29.

Phase 119I is the independent final migration closure review. Its implementation-repository verdict is **PASS WITH NON-BLOCKING LIMITATIONS**. The docs use that closure commit as the current source anchor while preserving immutable older source links where a page documents historical evidence from an earlier checkpoint.

## What materially changed since the previous docs baseline

The earlier site baseline was Phase 114D2. The implementation has since added and closed several major application-code/control-plane layers that are now documented here:

- canonical `datum.dscript/1` as a compile-time source representation;
- production D-Compile at `POST /api/v1/dcompile/compile`;
- deterministic lowering into a D-Graph plus canonical D-Serv artifact candidates;
- versioned, immutable D-Code artifact revisions;
- explicit D-Deploy binding of an active service to an exact descriptor revision;
- exact-revision governed D-Code preflight and execution;
- live H1→H2 evidence showing that registering/installing a new module revision does not activate it;
- governed migration with explicit target acceptance, target realization, source cleanup and rollback as a new transition;
- Phase 119 independent closure of that migration lifecycle.

## Current D-Code boundary

DServer stores canonical descriptors and authority. **It does not store or execute WASM module bytes.** Module bytes remain in the D-Node-local content-addressed store. Distribution/fetching of those bytes onto a node is still explicitly outside D-Code v0.1.

For each governed invocation the node-side client requests a fresh authorization from DServer, then fetches the exact immutable descriptor revision named by that authorization. The authorization binds current D-Map, D-Graph, node, module digest, full descriptor digest and ABI. The client independently cross-checks the response, loads the exact local module bytes by digest, and executes them in an isolated worker process.

## Important limitations

**No automatic D-Code module distribution.** Installing a module on a D-Node remains explicit. A future distribution mechanism must not be confused with D-Deploy authority: copying bytes must never silently activate a revision.

**Residual distributed TOCTOU.** Authorization is freshly derived immediately before execution, but a distributed control-plane state change can still occur after the HTTP response and before guest execution. Immutable revisions eliminate in-place revision mutation, but do not make the control plane and remote guest execution one atomic transaction.

**D-Script is not a general source-language SDK.** `datum.dscript/1` is the canonical compile-time representation: a set of D-Functions with conservative string annotations. It is not a Python/Rust/JavaScript parser and does not itself carry executable bytes, placement, runtime state or control flow.

**D-Compile does not verify submitted WASM bytes.** The production compiler receives declared module content identity/size as D-Code input and generates candidate descriptors deterministically. Byte verification occurs at module installation/load/execution boundaries, not inside the pure compile endpoint.

## Documentation coverage

This edition adds detailed material for WebAssembly, D-Code, software-component identities, DCompile, exact-revision governance, DServer-to-D-Node execution and the Phase 119I baseline. Older readiness/tutorial/reference pages remain valuable but some still describe the exact checkpoint at which their evidence was originally captured; their immutable source links make that provenance visible.

See [WebAssembly and D-Code](../concepts/webassembly-and-dcode.md), [software component model](../architecture/software-components.md), [DServer-to-D-Node execution](../architecture/dserver-dnode-dcode-flow.md), [DCompile and D-Code API](../reference/dcompile-dcode-api.md), and [sources and provenance](../reference/sources.md).
