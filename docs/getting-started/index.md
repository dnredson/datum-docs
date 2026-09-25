# Getting started

Start with the model, then reproduce a bounded integration scenario. This edition does not yet provide a turnkey production installer.

## Choose a path

| Goal | Start here |
|---|---|
| Understand DATUM | [Overview](../overview/index.md) and [concepts](../concepts/index.md) |
| Inspect an existing deployment | [Query readiness](../guides/inspect-readiness.md) |
| Reproduce D1 and D2 governance | [First integration examples](../examples/first-validation.md) |
| Edit this documentation | Repository README and [contribution guide](../project/contributing.md) |

## Runtime-source prerequisites

The integration examples require access to the private `dnredson/datum` repository, Git, a Rust/Cargo toolchain compatible with its lockfiles, and the host build dependencies for both Rust crates. The manifests use Rust edition 2021; this documentation does not invent a minimum Rust version absent from the inspected manifests.

The integration tests build and start a real DServer subprocess on loopback. Use an isolated development checkout. The tests use local temporary state and canonical fixtures, not live fog/cloud VMs or a production external MQTT deployment.

A successful documentation build says nothing about runtime build prerequisites. Runtime commands below are traced to the source tests; they were not rerun during authoring of this site.

## Separate checkouts

Keep `datum-docs` and your implementation worktree separate. To inspect the pinned runtime baseline without switching an existing implementation branch, use a new checkout as shown in the [example](../examples/first-validation.md).

## Sources

[DServer manifest](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/Cargo.toml), [DATUM manifest](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/Cargo.toml), [D1 integration test](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/tests/dmonitor_d1_readiness_integration.rs), [D2 integration test](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/tests/dmonitor_d2_dependency_readiness_integration.rs).
