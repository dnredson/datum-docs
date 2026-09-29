# Status and limitations

**Version:** DATUM v1. **Source revision:** `c08ccc4d715d9eb76644e3f1bd7d80a7945265c4`. **Documentation review date:** 2026-09-29.

This page describes what the current v1 implementation and documentation can support. Internal development milestone numbers are intentionally not part of the public documentation vocabulary.

## Current documented capability areas

This edition covers, at source-inspected depth:

- canonical D-Script and D-Compile;
- D-Graph/D-Serv/D-Call application structure;
- operational `ServiceArtifact` modeling for containers and native processes;
- server-owned execution projection/generation and OCI image identity;
- deterministic D-Deploy planning and explicit D-Map acceptance;
- operational node slices, finite reconciliation authorization and node-side execution;
- versioned immutable D-Code descriptor revisions;
- exact-revision D-Code authorization and isolated WASM execution;
- DMonitor observations, convergence and readiness;
- governed migration, target realization, source cleanup and rollback as an explicit new transition.

## Practical service examples

The tutorial set includes a source-grounded progression from real software to node execution:

- Mosquitto as a real checked-in container artifact, including port 1883, configuration mount and runtime probes;
- a full Mosquitto walk-through from artifact registration through D-Deploy acceptance and governed reconciliation;
- PostgreSQL as an example of persistent volume, configuration and secret references;
- a locally built LoRa simulator as an example of `local_build`, dependencies and secrets;
- native-process modeling that freezes an existing Linux executable by local path + SHA-256.

## Current D-Code boundary

DServer stores canonical D-Code descriptors and authority. **It does not store or execute WASM module bytes.** Module bytes remain in the D-Node-local content-addressed store.

For each governed invocation, the node-side client requests fresh DServer authorization, fetches the exact immutable descriptor revision named by that authorization, cross-checks identities and loads the exact local bytes by module digest before isolated execution.

## Important limitations

**Automatic D-Code module distribution is not implemented yet.** Copying/installing module content remains a separate operational step and must not be mistaken for activation.

**Native package-manager acquisition is not implemented yet.** `native_process_executable` consumes an already-present local Linux executable. A future package/repository acquisition capability will need its own governed content/provenance model rather than arbitrary shell execution.

**A distributed TOCTOU window can remain.** D-Code authorization is freshly derived immediately before execution, but DServer and a remote node do not participate in one distributed atomic transaction. Immutable revisions prevent in-place artifact mutation but do not eliminate every authority-movement race after response delivery.

**`target_stages` is not authoritative placement data.** Existing artifact metadata can include `target_stages`, but the current canonical D-Continuum does not provide the authoritative node-to-stage mapping required to verify those values during canonical planning. Tutorial paths use explicit node eligibility where necessary.

**Runtime realization is not readiness.** A container/process/module can execute successfully while evidence is absent, stale, unhealthy or correlated to obsolete authority.

## Dashboard

The management dashboard is **not implemented yet**. It is the next major usability increment planned for DATUM v1.

The service lifecycle pages already expose UI-friendly derived facts — Modeled, Registered, Execution identity complete, Proposed, Accepted, Assigned, Authorized, Realized, Observed, Healthy, Ready and Cleanup pending. These are documentation/UI concepts, not a new persisted canonical state enum.

The dashboard should derive each view from the existing authority and evidence domains rather than becoming another source of placement/runtime truth.

## Verification boundary

This docs build validates navigation, immutable source pins, public-version wording, Markdown/site rendering and internal links. It does not rerun the implementation repository's Rust suites or physical-node live validation.

The deployment examples are **source-derived and artifact-grounded**. They should not be read as a claim that the documentation workflow itself launched every example on a clean machine.

See [service modeling](../tutorials/model-existing-service.md), [Mosquitto end to end](../tutorials/mosquitto-end-to-end.md), [service-to-node lifecycle](../tutorials/service-to-node.md), [sources and provenance](../reference/sources.md) and [roadmap](../project/roadmap.md).
