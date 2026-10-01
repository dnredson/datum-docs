# Getting started

Choose between using the graphical Console, learning the model, following the source-to-deploy tutorial, or reproducing bounded readiness integration fixtures. DATUM v1 does not yet provide a packaged turnkey production installer or a fully reproduced multi-machine production deployment guide.

## Choose a path

| Goal | Start here |
|---|---|
| Use the graphical operator interface | [DATUM Console tutorial](../tutorials/datum-console.md) |
| Build, configure and perform a governed deploy from source | [Tutorials](../tutorials/index.md) |
| Model reusable services and understand catalog identity | [Service catalog](../concepts/service-catalog.md) |
| Understand DATUM before operating it | [Overview](../overview/index.md) and [concepts](../concepts/index.md) |
| Inspect an existing deployment programmatically | [Query readiness](../guides/inspect-readiness.md) |
| Reproduce D1 and D2 governance fixtures | [First integration examples](../examples/first-validation.md) |
| Edit this documentation | Repository README and [contribution guide](../project/contributing.md) |

## What the graphical path covers

The DATUM Console tutorial shows how to:

1. run the TypeScript/Vite Console against a DServer instance;
2. use the global operational overview;
3. browse discovered project contexts;
4. inspect a project workspace without confusing route scope with authorization;
5. read accepted logical D-Graph structure;
6. expand D-Servs into admitted runtime-realization evidence while keeping evidence separate from placement;
7. recognize partial/unavailable/corrupt read projections instead of treating missing data as healthy state;
8. create and revise reusable service definitions in the catalog without triggering deployment.

## What the source-to-deploy path covers

1. source installation/build of DServer and DATUM/SmartSentinel tooling;
2. DServer configuration and isolated control-state setup;
3. project scope, structural D-Node declaration and authoritative D-Continuum inspection;
4. operational `ServiceArtifact` versus canonical `datum.dserv-artifact/1` D-Code metadata;
5. creation of a valid `datum.dgraph/1`;
6. deterministic D-Deploy planning, proposal review and explicit D-Map acceptance;
7. operational container/native realization and governed D-Code execution;
8. migration/cleanup semantics;
9. troubleshooting across authority, realization and evidence boundaries.

Accepted D-Map authority does not imply that software was started, and a running process/container does not imply canonical DMonitor readiness.

## Runtime-source prerequisites

The source-derived examples require access to `dnredson/datum`, Git, a Rust/Cargo toolchain compatible with its lockfiles, and normal host build dependencies. Console development additionally requires Node.js `>=22.12.0`. Some operational examples depend on Docker and ordinary shell utilities.

## Separate checkouts

Keep `datum-docs` and your implementation worktree separate. To inspect the pinned source revision without switching an existing implementation branch, use a detached or separate checkout as shown in the [installation tutorial](../tutorials/install.md).

## Sources

See [Sources and provenance](../reference/sources.md) for the current implementation anchor and immutable source links.
