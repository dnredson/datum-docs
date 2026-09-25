# First example: D1 readiness governance

**Type:** real DServer subprocess integration fixture. **Scope:** local governance proof. **Source execution:** reported passing at the pinned checkpoint; not rerun for this documentation edition.

## Obtain an isolated checkout

These commands create a separate directory. They do not switch your existing Phase-114 worktree. GitHub access to the implementation repository is required.

```bash
git clone --no-checkout https://github.com/dnredson/datum.git datum-readiness-example
cd datum-readiness-example
git checkout --detach c059c3341c7901eeea77ce4881bbd341580d8aef
cd DATUM
```

## Execute the existing integration test

```bash
cargo test --locked --test dmonitor_d1_readiness_integration -- --ignored --test-threads=1
```

The `--ignored` argument is necessary because the source marks this subprocess test ignored for ordinary runs. A successful explicit run is expected to report one passing test and zero filtered out; an ordinary test invocation that skips it is not evidence of success.

## What the test establishes

| Step | Condition | Expected result |
|---|---|---|
| 1 | Exact-current Healthy DIoT evidence; required canonical DServ evidence absent | Application NotReady |
| 2 | Exact-current Healthy canonical DServ fixtures added for every required placement | Application Ready |
| 3 | Fresh exact-current Unhealthy DIoT observation published | Application NotReady while DIoT convergence remains Converged |

The source constructs current DMap/2, DForward, placement and runtime-binding state through production HTTP flows. It builds DServer, starts an isolated process and publishes the evidence used for the assertions.

## What it does not establish

It does not run a live two-machine deployment, demonstrate an external MQTT session, implement a production DServ collector, or close `any_element` dependency consumption. The DServ evidence is intentionally constructed as a fixture.

If the run fails, preserve the command, commit and test output. Diagnose build or environment errors separately from failed governance assertions. Do not alter policy values merely to make a readiness assertion pass.

## Source

[Full integration test](https://github.com/dnredson/datum/blob/c059c3341c7901eeea77ce4881bbd341580d8aef/DATUM/tests/dmonitor_d1_readiness_integration.rs). Read [status and limitations](../overview/status.md) before extending the result to a live deployment claim.
