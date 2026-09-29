# Status and limitations

**Edition:** DATUM v1 development documentation. **Current source baseline:** `c08ccc4d715d9eb76644e3f1bd7d80a7945265c4`. **Documentation review date:** 2026-09-29.

The docs use that implementation commit as the current source anchor while preserving immutable older source links where a page documents evidence produced by an earlier implementation revision. Internal development milestone numbering is intentionally not part of the public documentation model.

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
- DMonitor/readiness concepts and APIs;
- governed migration, target realization, source cleanup and rollback-as-new-transition.

## Practical service examples

The tutorial set includes a source-grounded progression from real software to node execution:

- a real checked-in Mosquitto container artifact, including port 1883, configuration mount and runtime probes;
- a full Mosquitto walk-through from artifact registration through D-Deploy acceptance and governed `--execute` reconciliation;
- PostgreSQL as an example of persistent volume + configuration + secret references;
- a locally built LoRa simulator as an example of `local_build`, dependencies and secrets;
- a current-compatible native-process Mosquitto shape showing how a repository-installed executable can be frozen by local path + SHA-256 after the external package-manager step.

The documentation explicitly does **not** claim that current native acquisition executes `apt`/`dnf`/`yum`. Package-manager installation is external preparation in DATUM v1; DATUM native acquisition begins from an existing absolute local executable and exact digest.

## Current D-Code boundary

DServer stores canonical D-Code descriptors and authority. **It does not store or execute WASM module bytes.** Module bytes remain in the D-Node-local content-addressed store. Automated distribution/fetching of those bytes onto a node is not implemented yet.

For each governed invocation the node-side client requests fresh DServer authorization, fetches the exact immutable descriptor revision named by that authorization, cross-checks the identities and loads the exact local bytes by module digest before isolated execution.

## Important limitations

**No automatic D-Code module distribution.** Copying/installing module content remains a separate operational step and must not be mistaken for activation. Automated distribution will be implemented separately.

**No native package-manager acquisition primitive.** `native_process_executable` consumes an already-present local Linux executable. A package/repository acquisition feature will need its own governed content/provenance model rather than being simulated with arbitrary lifecycle shell commands.

**Residual distributed TOCTOU.** D-Code authorization is freshly derived immediately before execution, but DServer and a remote node do not participate in one distributed atomic transaction. Immutable revisions prevent in-place artifact mutation but do not remove every authority-movement race after response delivery.

**`target_stages` is not canonical placement authority.** Existing catalog metadata can include `target_stages`, but current canonical D-Continuum does not provide the authoritative node-to-stage mapping required to verify those values during canonical planning. Tutorial paths use explicit node eligibility where necessary.

**Runtime realization is not readiness.** A container/process/module can execute successfully while evidence is absent, stale, unhealthy or correlated to obsolete authority.

## Dashboard preparation

The DATUM Console/dashboard is planned and will be implemented separately. The service lifecycle pages intentionally expose a UI-friendly set of **derived facts** — Modeled, Registered, Execution identity complete, Proposed, Accepted, Assigned, Authorized, Realized, Observed, Healthy, Ready, Cleanup pending — because these correspond to existing authority/evidence boundaries.

Those labels are documentation concepts, not a new persisted canonical state enum. The dashboard should read/derive current truth from the existing domains instead of becoming another source of placement/runtime authority.

## Verification boundary

This docs build validates navigation, immutable source pins, Markdown/site rendering and internal links. It does not rerun the implementation repository's Rust suites or physical-node live proofs.

The deployment examples are **source-derived and artifact-grounded**, not a claim that the documentation workflow itself launched Mosquitto on a clean machine. Reproducible live multinode examples will be added when that validation has been completed and captured.

See [service modeling](../tutorials/model-existing-service.md), [Mosquitto end to end](../tutorials/mosquitto-end-to-end.md), [service-to-node lifecycle](../tutorials/service-to-node.md), [sources and provenance](../reference/sources.md) and [roadmap](../project/roadmap.md).
