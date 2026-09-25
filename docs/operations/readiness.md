# Health, freshness, convergence and readiness

A Healthy observation does not by itself mean a placement is Ready. Each layer answers a different question.

| Layer | Question | Meaning at D1 |
|---|---|---|
| Structural validity | Is this a valid observation document? | Contract validation |
| Freshness | Is this evidence recent enough under the policy? | Time-based evaluation independent of health |
| Correlation and convergence | Does admitted evidence match current desired authority? | Exact identity and current realization checks |
| Current health | What do admitted current observations report? | Healthy, Degraded, Unhealthy, Unknown or Conflicting |
| Readiness | Does server governance positively permit current use? | Ready or NotReady |

The API serializes readiness as `ready` or `not_ready`. Diagnostic uncertainty stays visible in findings and nested results; there is no third readiness-level Unknown.

## Placement rule

A required DServ or DIoT placement is Ready only when its convergence is Converged and its admitted current health is Healthy. DIoT convergence already includes the required freshness and exact-current DMap, DForward and runtime-binding checks. D1 consumes that interpretation rather than duplicating it.

Health assessment uses admitted evidence only. Conflicting current health claims fail closed. There is no monitor leader election or majority vote.

## Server-owned policy

| Field | Value |
|---|---|
| Policy ID | `dmonitor-readiness-v1` |
| Maximum observed age | 90 seconds |
| Maximum received age | 90 seconds |
| Maximum future clock skew | 10 seconds |
| Accepted health | Healthy only |

The endpoint does not accept a caller policy or evaluation time. The versioned policy is fixed in the D1 implementation. A heartbeat interval longer than the freshness window can legitimately cause NotReady periods.

## Application aggregation

Application Ready requires active authority, at least one required runtime realization, every required DServ and DIoT placement Ready, and neither dimension's convergence Diverged.

DMap/1 has no DIoT dimension. DMap/2 with zero desired DIoT placements does not require DIoT readiness merely because the schema supports it. A proven unexpected realization can still make a dimension Diverged and block application readiness. Zero required realizations across both dimensions gives `not_ready` with `no_required_runtime_realizations`.

## Examples

| Evidence or state | Placement readiness |
|---|---|
| Converged and admitted current Healthy | Ready |
| Converged but Unhealthy | NotReady |
| Last observation Healthy but stale | NotReady |
| Healthy session still using an obsolete binding | NotReady |
| Conflicting admitted current health | NotReady |

## The any_element boundary

ADR-0010 assigns `any_element` dependency readiness to the **providing DIoT placement**. Whole-application readiness is not a substitute for that provider-specific decision. An unrelated DServ may block the application aggregate without invalidating an otherwise Ready provider placement.

Dynamic dependency consumption is not implemented in this edition's D1 baseline. Provider and placement multiplicity must be resolved under accepted contracts, not by inventing a first-provider or healthiest-provider rule in documentation.

## Sources

[D1 core](https://github.com/dnredson/datum/blob/c059c3341c7901eeea77ce4881bbd341580d8aef/dserver/src/core/dmonitor_readiness.rs), [readiness section of ADR-0024](https://github.com/dnredson/datum/blob/c059c3341c7901eeea77ce4881bbd341580d8aef/documentation/adr/ADR-0024-canonical-dmonitor-observation-model.md#dmonitor-backed-readiness-governance-phase-114d1), [ADR-0010](https://github.com/dnredson/datum/blob/c059c3341c7901eeea77ce4881bbd341580d8aef/documentation/adr/ADR-0010-cross-node-readiness-fresh-evidence.md).
