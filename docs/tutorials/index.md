# Tutorials

These tutorials turn the Phase 114D2 model into concrete operator/developer workflows. They intentionally describe **only what exists at the documented baseline**. Later phases can extend this section without rewriting the authority model introduced here.

!!! important "What 'deploy' means in this edition"
    DATUM currently separates **accepted placement authority** from **runtime realization**. D-Deploy creates and explicitly accepts a canonical D-Map; acceptance does not, by itself, copy a WASM module to a D-Node, pull/start a container, or prove runtime health. Those are separate operational steps with separate evidence.

## Recommended path

1. [Install from source](install.md) — build DServer and the DATUM agent/runtime tools.
2. [Configure the control plane and identities](configure.md) — DServer configuration, SQLite state, project scope, structural D-Nodes and local runtime identity.
3. [Author software artifacts](artifacts.md) — understand the two artifact families currently present and create/register them correctly.
4. [Create a valid D-Graph](dgraph.md) — describe application services and calls without embedding placement.
5. [Perform a basic governed deploy](basic-deploy.md) — derive a deterministic placement proposal, review it and explicitly accept it.
6. [Realize the accepted deployment](runtime-realization.md) — understand the operational reconciler and the governed D-Code execution path.
7. [Troubleshoot common failures](troubleshooting.md) — map errors/findings back to the authority boundary that produced them.

## The components you will meet

| Component | Role in the tutorial |
|---|---|
| **DServer** | Server-owned control plane: structural D-Node authority, ServiceArtifact registry, D-Deploy proposals/acceptances, D-Code metadata, DMonitor evidence and derived readiness. |
| **DATUM / SmartSentinel agent crate** | Node-side collectors, reconciliation tooling and canonical D-Code runtime tools. |
| **Project** | Operational scope used by several DServer domains. Passed by `X-Datum-Project` on project-scoped APIs. |
| **D-Node** | Structural logical runtime node. Its declaration is not liveness telemetry. |
| **D-Continuum** | Server-derived structural view of the declared D-Nodes for a project scope. |
| **D-Graph** | Placement-free application graph: D-Serv vertices and D-Call edges. |
| **D-Serv** | Logical application service in the D-Graph. |
| **D-Call** | Logical call from one D-Serv to another. |
| **ServiceArtifact** | Current project-scoped operational/deployment descriptor used by D-Deploy eligibility and the reconciliation plane. |
| **`datum.dserv-artifact/1`** | Canonical, host-independent descriptor of a D-Serv's content-addressed D-Code WASM. It is a different domain from ServiceArtifact. |
| **D-Deploy proposal** | Candidate placement. Never authority by itself. |
| **D-Map** | Canonical accepted placement authority, materialized only after explicit acceptance. |
| **Operational reconciliation** | Node-side realization path for operational artifacts such as containers/native processes. |
| **D-Code module store** | Node-local content-addressed store of canonical D-Code WASM bytes. |
| **DMonitor** | Runtime evidence. It describes what was observed, not what should run. |

## Two software paths exist today

The baseline has two intentionally distinct software-description/execution families.

### Operational software: `ServiceArtifact`

A `ServiceArtifact` is project-scoped and can describe container or native-process realization. D-Deploy currently also consults these records when validating/planning D-Serv placement: exactly one artifact must resolve each canonical service, and its `target_nodes` constrain placement eligibility.

The artifact is **not** the canonical D-Serv D-Code contract. Its lifecycle, container/native-process data, probes, acquisition information, bindings and reconciliation policy belong to the operational deployment plane.

### Application D-Code: `datum.dserv-artifact/1`

A canonical D-Serv artifact describes a content-addressed WASM module for a D-Serv. DServer stores/verifies descriptor metadata and digest identity; module bytes themselves are installed explicitly in each D-Node's local content-addressed store. Governed invocation asks DServer for current authorization immediately before local execution.

At this baseline the two families coexist. Do not silently substitute one for the other.

## What this tutorial does not claim

This is not yet a packaged installer, a stable release guide, or a closed live fog/cloud deployment recipe. Phase 114E live multinode validation remains open. The existing laboratory bundles are useful implementation material but are not promoted here into a reproduced 114E tutorial.

Likewise, accepted placement does not imply readiness. D1/D2 readiness requires fresh canonical DMonitor evidence correlated to current authority. The canonical production DServ evidence emitter is still an open boundary at this checkpoint.

## Source baseline

All implementation links in these tutorials are pinned to `3e0baa8f415b822f69eef86c0cbfe2a3681e3a65` (Phase 114D2). The commands are source-derived; this documentation build does not claim to have rerun the runtime workflow in a clean environment.

See [sources and provenance](../reference/sources.md) and [status and limitations](../overview/status.md).