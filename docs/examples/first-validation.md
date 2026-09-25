# First examples: D1 and D2 readiness governance

**Type:** real DServer subprocess integration fixtures. **Scope:** local governance proofs. **Documentation execution:** source inspected at the pinned checkpoint; runtime tests were not rerun for this documentation edition.

## Obtain an isolated checkout

These commands create a separate directory. They do not switch your existing Phase-114 worktree. GitHub access to the implementation repository is required.

```bash
git clone --no-checkout https://github.com/dnredson/datum.git datum-readiness-example
cd datum-readiness-example
git checkout --detach 3e0baa8f415b822f69eef86c0cbfe2a3681e3a65
cd DATUM
```

## D1: application readiness

Run the existing ignored subprocess proof explicitly:

```bash
cargo test --locked --test dmonitor_d1_readiness_integration -- --ignored --test-threads=1
```

The D1 proof establishes this progression:

| Step | Condition | Expected result |
|---|---|---|
| 1 | Exact-current Healthy DIoT evidence; required canonical DServ evidence absent | Application NotReady |
| 2 | Exact-current Healthy canonical DServ fixtures added for every required placement | Application Ready |
| 3 | Fresh exact-current Unhealthy DIoT observation published | Application NotReady while DIoT convergence remains Converged |

The source constructs current DMap/2, DForward, placement and runtime-binding state through production HTTP flows. It builds DServer, starts an isolated process and publishes the evidence used for the assertions.

## D2: provider-specific `any_element` readiness

Run the D2 subprocess proof separately:

```bash
cargo test --locked --test dmonitor_d2_dependency_readiness_integration -- --ignored --test-threads=1
```

The D2 proof constructs a consumer DIoT on `cloud-01` with an `any_element` requirement and a canonical DForward chain to a provider DIoT on `fog-01`:

| Step | Provider evidence | Expected dependency result |
|---|---|---|
| 1 | No provider DMonitor evidence | `blocked` |
| 2 | Exact-current Healthy provider DIoT evidence | `satisfied`, even while an unrelated required DServ keeps whole-application readiness NotReady |
| 3 | Fresh exact-current Unhealthy provider observation | `blocked` again, even though provider convergence may remain Converged |

This is the key D2 distinction: dependency readiness consumes the exact provider placement's D1 readiness, not whole-application readiness, raw health alone or convergence alone.

## What these examples do not establish

They do not run a live two-machine deployment, demonstrate the full Phase 114E fog/cloud validation, or implement a production DServ collector. D1 canonical DServ evidence in the fixture is intentionally constructed for governance testing.

If a run fails, preserve the command, commit and test output. Diagnose build or environment errors separately from failed governance assertions. Do not alter policy values merely to make a readiness assertion pass.

## Sources

[D1 integration test](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/tests/dmonitor_d1_readiness_integration.rs), [D2 integration test](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/tests/dmonitor_d2_dependency_readiness_integration.rs). Read [status and limitations](../overview/status.md) before extending either result to a live deployment claim.
