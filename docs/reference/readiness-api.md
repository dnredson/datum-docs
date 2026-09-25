# Readiness API

## Request

```http
GET /api/v1/dmonitor/readiness/:project_id/:application_id
```

| Input | Meaning |
|---|---|
| `project_id` | Project scope used to load/evaluate state |
| `application_id` | Application within that scope |
| Request body | No supported policy input |
| Query parameters | No supported policy or time override |

The handler calls the D1 core directly. It does not call another readiness HTTP endpoint or initiate runtime operations. Query/body values are not a policy control surface; the implementation signature does not extract them.

## Result

The response is `DMonitorApplicationReadinessV1`, with schema `datum.dmonitor-readiness/1`. It carries the project/application context, evaluation time, server policy, aggregate readiness, findings, and the DServ/DIoT dimension results defined in the pinned core type.

Readiness serializes as `ready` or `not_ready`. A valid read may return NotReady because no active authority exists. State-load or lock failures are handled as internal errors; they should not be mistaken for an ordinary readiness finding.

For the exact field layout, consult the [Rust response types](https://github.com/dnredson/datum/blob/c059c3341c7901eeea77ce4881bbd341580d8aef/dserver/src/core/dmonitor_readiness.rs). No illustrative JSON is presented here as a complete contract.

## Finding inventory

| Code | Meaning |
|---|---|
| `ready` | Readiness requirements are satisfied |
| `no_active_placement_authority` | No current accepted placement authority is available |
| `no_required_runtime_realizations` | Neither dimension requires a runtime realization |
| `dserv_not_converged` | Required DServ convergence conditions fail |
| `diot_not_converged` | Required DIoT convergence conditions fail |
| `health_unknown` | Current health is not established |
| `health_degraded` | Admitted current health is Degraded |
| `health_unhealthy` | Admitted current health is Unhealthy |
| `conflicting_current_health` | Admitted current health claims disagree |

These nine readiness codes are distinct from nested convergence findings.

## Snapshot and policy

The handler acquires transaction locks in this order: DDeploy, DNode registry, DIoT runtime bindings, DMonitor. It loads one coherent state snapshot, creates one server evaluation timestamp, and invokes the core with `dmonitor-readiness-v1`.

The read is not persisted and performs no reconciliation, deployment, binding registration or evidence ingestion. The [operations guide](../operations/readiness.md) lists the fixed D1 policy values.

## Sources

[Handler](https://github.com/dnredson/datum/blob/c059c3341c7901eeea77ce4881bbd341580d8aef/dserver/src/api/dmonitor_readiness.rs), [core and result model](https://github.com/dnredson/datum/blob/c059c3341c7901eeea77ce4881bbd341580d8aef/dserver/src/core/dmonitor_readiness.rs).
