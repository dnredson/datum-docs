# Status and limitations

**Version:** DATUM v1. **Source revision:** `7a79bd84bc05a1ea18870715cc033567ff472afc`. **Documentation review date:** 2026-10-01.

This page describes what the current DATUM v1 implementation and documentation can support. Public documentation uses product concepts and implemented capabilities rather than internal development numbering.

## Current documented capability areas

This edition covers, at source-inspected depth:

- canonical D-Script and D-Compile;
- D-Graph/D-Serv/D-Call application structure;
- operational `ServiceArtifact` modeling for containers and native processes;
- deterministic D-Deploy planning and explicit D-Map acceptance;
- operational node slices, finite reconciliation authorization and node-side execution;
- versioned immutable D-Code descriptor revisions and isolated WASM execution;
- DMonitor observations, convergence and readiness;
- governed migration, target realization, source cleanup and rollback as explicit transitions;
- DATUM Console global/project operational views;
- accepted logical graph visualization with separately represented DMonitor realization evidence;
- reusable, revisioned Artifact & Service Catalog definitions with exact operational artifact pins.

## DATUM Console

The graphical Console **is implemented** in the pinned source revision.

Current routed surfaces are:

- global overview;
- project navigation;
- read-only project workspace;
- project logical/runtime-evidence graph;
- global Artifact & Service Catalog.

The project workspace presents independent operational dimensions rather than synthesizing one canonical project-health score. The graph uses accepted logical snapshots and can expand admitted D-Serv realization evidence without treating evidence as placement.

Dedicated project pages for Placement, Deploy, Runtime and History are not implemented yet. The current interface is primarily inspection plus catalog authoring; it is not yet a full graphical replacement for every command/API workflow.

## Service catalog

The service catalog stores immutable reusable definition revisions. It supports atomic and composite definitions, exact dependency revisions, tenancy capabilities, resource/capability requirements, monitoring/health intent, secret references and exact artifact snapshots.

Catalog mutation is deliberately **catalog-only**. Saving a definition does not create a D-Map, runtime, tenant binding or monitoring producer.

A live external AI provider for guided service modeling is not part of this pinned source revision; the published catalog editor is operator-authored.

## Current D-Code boundary

DServer stores canonical D-Code descriptors and authority. **It does not store or execute WASM module bytes.** Module bytes remain in the D-Node-local content-addressed store.

For each governed invocation, the node-side client requests fresh DServer authorization, fetches the exact immutable descriptor revision named by that authorization, cross-checks identities and loads the exact local bytes by module digest before isolated execution.

## Important limitations

**Automatic D-Code module distribution is not implemented yet.** Copying/installing module content remains a separate operational step and must not be mistaken for activation.

**Native package-manager acquisition is not implemented yet.** `native_process_executable` consumes an already-present local Linux executable.

**A distributed TOCTOU window can remain.** D-Code authorization is freshly derived immediately before execution, but DServer and a remote node do not participate in one distributed atomic transaction.

**`target_stages` is not authoritative placement data.** Existing artifact metadata can include it, but canonical planning still needs authoritative node eligibility/capability facts.

**Runtime realization is not readiness.** A container/process/module can execute successfully while evidence is absent, stale, unhealthy or correlated to obsolete authority.

**Console graph evidence can be partial.** A bounded runtime-evidence projection must not be interpreted as a complete process inventory.

**Catalog provisioning metadata is declarative.** Repository/Compose metadata is stored and validated but not cloned, parsed or executed by catalog save.

## Verification boundary

This docs build validates navigation, immutable source pins, public-version wording, Markdown/site rendering and internal links. It does not rerun the implementation repository's Rust/Console suites or physical-node live validation.

See [DATUM Console tutorial](../tutorials/datum-console.md), [Console architecture](../architecture/console.md), [service catalog](../concepts/service-catalog.md), [sources and provenance](../reference/sources.md) and [roadmap](../project/roadmap.md).
