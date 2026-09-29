# Getting started

Choose between learning the model, following the source-to-deploy tutorial, or reproducing the bounded D1/D2 integration proofs. DATUM v1 does not yet provide a packaged/turnkey production installer or a fully reproduced live multinode tutorial; those will be added when implemented and validated.

## Choose a path

| Goal | Start here |
|---|---|
| Build, configure and perform a basic governed deploy from source | [Tutorials](../tutorials/index.md) |
| Understand DATUM before operating it | [Overview](../overview/index.md) and [concepts](../concepts/index.md) |
| Inspect an existing deployment | [Query readiness](../guides/inspect-readiness.md) |
| Reproduce D1 and D2 governance proofs | [First integration examples](../examples/first-validation.md) |
| Edit this documentation | Repository README and [contribution guide](../project/contributing.md) |

## What the tutorial covers now

The DATUM v1 tutorial covers:

1. source installation/build of DServer and the DATUM agent/runtime crate;
2. DServer configuration and isolated SQLite control-state setup;
3. project scope, structural D-Node declaration and authoritative D-Continuum inspection;
4. the distinction between operational `ServiceArtifact` and canonical `datum.dserv-artifact/1` D-Code metadata;
5. creation of a valid `datum.dgraph/1`;
6. deterministic D-Deploy planning, proposal review and explicit acceptance into an active canonical D-Map;
7. the separate operational-reconciliation and D-Code realization paths;
8. troubleshooting across authority, realization and evidence boundaries.

The tutorial intentionally does not claim a reproduced live multi-machine deployment. Accepted D-Map authority does not imply that software was started, and a running process/container does not imply canonical DMonitor readiness.

## Runtime-source prerequisites

The source-derived examples require access to the `dnredson/datum` repository, Git, a Rust/Cargo toolchain compatible with its lockfiles, and the host build dependencies for both Rust crates. The manifests use Rust edition 2021; this documentation does not invent a minimum Rust version absent from the inspected manifests.

Some operational examples additionally depend on Docker and ordinary shell utilities. The canonical D-Code runtime uses Wasmtime through the DATUM package. `jq` is used only as a convenience in tutorial commands.

The dedicated D1/D2 integration tests build and start a real DServer subprocess on loopback. They use local temporary state and canonical fixtures, not live fog/cloud VMs or a production external MQTT deployment.

A successful documentation build says nothing about runtime build prerequisites. Tutorial commands are traced to pinned source; they were not rerun during authoring of this edition unless a page explicitly says otherwise.

## Separate checkouts

Keep `datum-docs` and your implementation worktree separate. To inspect the pinned DATUM v1 source without switching an existing implementation branch, use a detached or separate checkout as shown in the [installation tutorial](../tutorials/install.md) and [validation example](../examples/first-validation.md).

## Sources

[DServer manifest](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/dserver/Cargo.toml), [DATUM manifest](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/DATUM/Cargo.toml), [D1 integration test](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/tests/dmonitor_d1_readiness_integration.rs), [D2 integration test](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/tests/dmonitor_d2_dependency_readiness_integration.rs).
