# Readiness APIs

Both readiness surfaces are read-only, server-owned derivations. Neither endpoint accepts a caller policy, evaluation-time override or replacement authority object.

## D1 application readiness

### Request

```http
GET /api/v1/dmonitor/readiness/:project_id/:application_id
```

| Input | Meaning |
|---|---|
| `project_id` | Project scope used to load/evaluate state |
| `application_id` | Application within that scope |
| Request body | No supported policy input |
| Query parameters | No supported policy or time override |

The handler calls the D1 core directly. It does not initiate runtime operations.

### Result

The response is `DMonitorApplicationReadinessV1`, with schema `datum.dmonitor-readiness/1`. It carries project/application context, evaluation time, server policy, aggregate readiness, findings, and the DServ/DIoT dimension results defined in the pinned core type.

Readiness serializes as `ready` or `not_ready`. A valid read may return NotReady because no active authority exists. State-load or lock failures are internal errors; they should not be mistaken for an ordinary readiness finding.

For the exact field layout, consult the [D1 Rust response types](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/dmonitor_readiness.rs). No illustrative JSON is presented here as a complete contract.

### D1 finding inventory

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

These nine D1 readiness codes are distinct from nested convergence findings.

## D2 `any_element` dependency readiness

### Request

```http
GET /api/v1/dforward/dependency-readiness/:project_id/:application_id/:node_id
```

`node_id` selects the consumer node whose placed DIoT `any_element` requirements are evaluated. It does **not** name or select a provider. Provider resolution is derived from current accepted DMap/2/DForward authority.

The handler accepts no request body and no query parameters. It generates `evaluated_at_utc` on the server and reuses the server-owned D1 readiness policy.

### Result

The top-level response is `DForwardDependencyReadinessV1`, with schema `datum.dforward-dependency-readiness/1`. It contains project/application/node context, evaluation time, policy, optional current DMap/DForward summaries, authority-level findings, and a deterministically ordered `dependencies` array.

Each `DForwardAnyElementDependencyReadinessV1` entry carries the consumer DIoT/placement/node, required interface, optional resolved provider DIoT/placement/node, the exact provider placement's embedded D1 readiness when available, dependency `state`, and per-dependency findings. `state` serializes as `satisfied` or `blocked`.

For the exact field layout and ordering rules, consult the [D2 core response types](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/dforward_dependency_readiness.rs).

### D2 finding inventory

| Code | Meaning |
|---|---|
| `satisfied` | The exact resolved provider placement is Ready |
| `no_active_dmap_v2_authority` | No usable active DMap/2 authority/DForward snapshot exists |
| `provider_unresolved` | No provider can be resolved from current topology |
| `provider_ambiguous` | Provider resolution is not unique |
| `provider_not_diot` | The resolved provider is not a canonical DIoT |
| `provider_placement_missing` | The provider has no current accepted placement |
| `provider_placement_ambiguous` | The provider placement is not unique |
| `provider_readiness_missing` | No D1 readiness entry exists for the exact provider placement |
| `provider_not_ready` | The exact provider placement is NotReady |

Top-level findings carry authority-level issues; dependency-specific reasons remain on each dependency entry. These codes are a third layer, separate from both convergence findings and D1 readiness findings.

## Snapshot and policy

Both handlers acquire transaction locks in the established order: DDeploy, DNode registry, DIoT runtime bindings, DMonitor. They load coherent in-process state and generate server evaluation time. D2 does not acquire DCall state and does not make an internal HTTP call to D1; it calls the shared readiness cores directly.

These reads are not persisted and perform no reconciliation, deployment, binding registration or evidence ingestion. The [operations guide](../operations/readiness.md) lists the fixed D1 policy values consumed by both evaluations.

## Sources

[D1 handler](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/api/dmonitor_readiness.rs), [D1 core](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/dmonitor_readiness.rs), [D2 handler](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/api/dforward_dependency_readiness.rs), [D2 core](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/dforward_dependency_readiness.rs).
