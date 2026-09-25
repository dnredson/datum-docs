# Getting started

Start with the model, then reproduce a bounded integration scenario. This edition does not yet provide a turnkey production installer.

## Choose a path

| Goal | Start here |
|---|---|
| Understand DATUM | [Overview](../overview/index.md) and [concepts](../concepts/index.md) |
| Inspect an existing deployment | [Query readiness](../guides/inspect-readiness.md) |
| Reproduce D1 governance | [First integration example](../examples/first-validation.md) |
| Edit this documentation | Repository README and [contribution guide](../project/contributing.md) |

## Runtime-source prerequisites

The integration example requires access to the private `dnredson/datum` repository, Git, a Rust/Cargo toolchain compatible with its lockfiles, and the host build dependencies for both Rust crates. The manifests use Rust edition 2021; this documentation does not invent a minimum Rust version absent from the inspected manifests.

The integration test builds and starts a real DServer subprocess on loopback. Use an isolated development checkout. The test uses local temporary state and canonical fixtures, not live fog/cloud VMs or an external MQTT broker.

A successful documentation build says nothing about runtime build prerequisites. Runtime commands below are traced to the source test; they were not rerun during authoring of this site.

## Separate checkouts

Keep `datum-docs` and your implementation worktree separate. To inspect the pinned runtime baseline without switching an existing implementation branch, use a new checkout as shown in the [example](../examples/first-validation.md).

## Sources

[DServer manifest](https://github.com/dnredson/datum/blob/c059c3341c7901eeea77ce4881bbd341580d8aef/dserver/Cargo.toml), [DATUM manifest](https://github.com/dnredson/datum/blob/c059c3341c7901eeea77ce4881bbd341580d8aef/DATUM/Cargo.toml), [D1 integration test](https://github.com/dnredson/datum/blob/c059c3341c7901eeea77ce4881bbd341580d8aef/DATUM/tests/dmonitor_d1_readiness_integration.rs).
