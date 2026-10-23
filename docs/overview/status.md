# Status and limitations

**Version:** DATUM v1. **Source revision:** 3605845b7933195e470c9a13473fbc05432c4a26. **Documentation review date:** 2026-10-23.

This page describes what the current DATUM v1 implementation and documentation can support. Public documentation uses product concepts and implemented capabilities rather than internal development numbering.

## Current documented capability areas

This edition covers, at source-inspected depth:

- canonical D-Script and D-Compile;
- D-Graph/D-Serv/D-Call application structure;
- operational ServiceArtifact modeling for containers and native processes;
- deterministic D-Deploy planning and explicit D-Map acceptance;
- operational node slices, finite reconciliation authorization and node-side execution;
- versioned immutable D-Code descriptor revisions and isolated WASM execution;
- DMonitor observations, convergence and readiness;
- governed migration, target realization, source cleanup and rollback as explicit transitions;
- DATUM Console management workspaces across projects, Continuum, graph, placement, proposal review, deploy/reconciliation, application context and history;
- reusable, revisioned Artifact & Service Catalog definitions with exact operational artifact pins;
- DATUM Live as a separate continuously refreshed, read-only cross-project observation surface.

## DATUM Console

The graphical Console is implemented in the pinned source revision. Current routed surfaces include global/project operations, global and project Continuum, logical/runtime-evidence graph, local D-Graph draft editing, placement candidate/proposal workflows, proposal review and explicit placement-authority acceptance, application operational context, deploy/reconciliation requests, read-only DMonitor history and the global Artifact & Service Catalog.

These routes do not collapse authority boundaries. A placement candidate is not acceptance. Acceptance changes placement authority but does not itself execute software. Deploy/reconciliation requests do not mutate a host directly; the node-side agent remains the component that performs separately authorized host actions.

## DATUM Live

DATUM Live is implemented as a second Vite entry point that shares Console types, API clients and presentation primitives but has a different operational purpose.

It is cross-project, read-only, continuously refreshed, profile-based in the browser and responsive for small secondary displays and kiosk/fullscreen use.

A Live profile can pin D-Nodes from the global Continuum and filter global activity. Profiles are schema-versioned and persisted in browser localStorage. The URL query parameter identifies which local profile a tab opens; this is not yet a server-side shared view.

Node cards preserve distinct evidence domains. Host CPU/memory/swap come from Resource Registry observations bound to the structural D-Node. DMonitor evidence shown on the card is placement-scoped. Active alerts/events are correlated to a node only when their canonical subject actually carries node_id.

Card color is presentation of existing backend evidence, not a new health score. CPU, memory and observation age do not create danger/warning states by frontend threshold. Absence of alerts is not presented as proof that a node is healthy.

## Current Live limitations

**Server-side Live profile persistence/sharing is not implemented yet.** Profiles currently live in the browser, so a URL is stable for tabs using the same local store but is not a cross-device shared dashboard definition.

**Connection/link availability is not projected into Live yet.** The current Continuum read model does not provide a canonical availability result for physical links, and Live does not run its own ping/probe. Connectivity should be projected from canonical observation evidence rather than invented in the frontend.

**Placement-scoped DMonitor evidence can be empty for an otherwise observed host.** A D-Node can have a current host Resource Registry observation while having no accepted workload placement and therefore no placement-scoped DMonitor observation in the Continuum node view.

## Service catalog

The service catalog stores immutable reusable definition revisions. Catalog mutation remains catalog-only: saving a definition does not create a D-Map, runtime, tenant binding or monitoring producer. A live external AI provider for guided service modeling is not part of this pinned source revision; the published catalog editor remains operator-controlled.

## Important limitations

**Automatic D-Code module distribution is not implemented yet.** Copying/installing module content remains a separate operational step and must not be mistaken for activation.

**Native package-manager acquisition is not implemented yet.** native_process_executable consumes an already-present local Linux executable.

**A distributed TOCTOU window can remain.** D-Code authorization is freshly derived immediately before execution, but DServer and a remote node do not participate in one distributed atomic transaction.

**Runtime realization is not readiness.** A container/process/module can execute successfully while evidence is absent, stale, unhealthy or correlated to obsolete authority.

**Console graph evidence can be partial.** A bounded runtime-evidence projection must not be interpreted as a complete process inventory.

**Catalog provisioning metadata is declarative.** Repository/Compose metadata is stored and validated but not cloned, parsed or executed by catalog save.

## Verification boundary

This docs build validates navigation, immutable source pins, public-version wording, Markdown/site rendering and internal links. It does not rerun the implementation repository's Rust/Console suites or physical-node live validation.

See [DATUM Console tutorial](../tutorials/datum-console.md), [DATUM Live tutorial](../tutorials/datum-live.md), [Console architecture](../architecture/console.md), [Live architecture](../architecture/live.md), [sources and provenance](../reference/sources.md) and [roadmap](../project/roadmap.md).
