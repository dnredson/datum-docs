# Getting started

Choose between learning the model, following the source-to-deploy tutorial, or reproducing the bounded D1/D2 integration fixtures. DATUM v1 does not yet provide a packaged turnkey production installer or a fully reproduced multi-machine production deployment guide.

## Choose a path

| Goal | Start here |
|---|---|
| Build, configure and perform a basic governed deploy from source | [Tutorials](../tutorials/index.md) |
| Understand DATUM before operating it | [Overview](../overview/index.md) and [concepts](../concepts/index.md) |
| Inspect an existing deployment | [Query readiness](../guides/inspect-readiness.md) |
| Reproduce D1 and D2 governance fixtures | [First integration examples](../examples/first-validation.md) |
| Edit this documentation | Repository README and [contribution guide](../project/contributing.md) |

## What the v1 tutorial covers

1. source installation/build of DServer and the DATUM agent/runtime crate;
2. DServer configuration and isolated SQLite control-state setup;
3. project scope, structural D-Node declaration and authoritative D-Continuum inspection;
4. the distinction between operational `ServiceArtifact` and canonical `datum.dserv-artifact/1` D-Code metadata;
5. creation of a valid `datum.dgraph/1`;
6. deterministic D-Deploy planning, proposal review and explicit D-Map acceptance;
7. operational container/native realization and governed D-Code execution;
8. migration/cleanup semantics;
9. troubleshooting across authority, realization and evidence boundaries.

Accepted D-Map authority does not imply that software was started, and a running process/container does not imply canonical DMonitor readiness.

## Runtime-source prerequisites

The source-derived examples require access to `dnredson/datum`, Git, a Rust/Cargo toolchain compatible with its lockfiles, and the normal host build dependencies. Some operational examples additionally depend on Docker and ordinary shell utilities. `jq` is used only as a convenience.

The D1/D2 integration tests build and start a real DServer subprocess on loopback. They use local temporary state and canonical fixtures; they are not a substitute for a physical multi-node deployment.

## Separate checkouts

Keep `datum-docs` and your implementation worktree separate. To inspect the pinned source revision without switching an existing implementation branch, use a detached or separate checkout as shown in the [installation tutorial](../tutorials/install.md) and [validation example](../examples/first-validation.md).

## Sources

See [Sources and provenance](../reference/sources.md) for the current implementation anchor and immutable source links.
