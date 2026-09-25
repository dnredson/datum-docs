# Health, freshness, convergence and readiness

A Healthy observation does not by itself mean a placement is Ready. Each layer answers a different question.

| Layer | Question | Meaning at D2 |
|---|---|---|
| Structural validity | Is this a valid observation document? | Contract validation |
| Freshness | Is this evidence recent enough under the policy? | Time-based evaluation independent of health |
| Correlation and convergence | Does admitted evidence match current desired authority? | Exact identity and current realization checks |
| Current health | What do admitted current observations report? | Healthy, Degraded, Unhealthy, Unknown or Conflicting |
| Placement readiness | Does server governance positively permit this required placement now? | Ready or NotReady |
| Application readiness | Are the application's required realizations Ready? | Aggregate Ready or NotReady |
| `any_element` dependency readiness | Is the exact current provider placement Ready for this dependency? | `satisfied` or `blocked` |

The D1 API serializes readiness as `ready` or `not_ready`. Diagnostic uncertainty stays visible in findings and nested results; there is no third readiness-level Unknown. D2 dependency readiness likewise fails closed to `blocked` when satisfaction cannot be positively established.

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

The endpoints do not accept a caller policy or evaluation time. The versioned D1 policy is server-owned and is reused by D2 when it evaluates the exact provider placement. A heartbeat interval longer than the freshness window can legitimately cause NotReady/blocked periods.

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

## `any_element` dependency readiness

ADR-0010 assigns an `any_element` dependency to the **providing DIoT placement**. Whole-application readiness is not a substitute for that provider-specific decision. An unrelated DServ may block the application aggregate without invalidating an otherwise Ready provider placement.

The authority-only DForward projection intentionally remains `pending_fresh_evidence`; D2 does not mutate that static view. Instead, the dynamic evaluator resolves providers from the current accepted DMap/2/DForward topology and evaluates the exact provider placement under D1 readiness governance.

Only `scope = any_element` enters this D2 gate. `same_element` requirements are excluded from this dynamic cross-node evaluation. For a consumer node, the result is deterministically ordered by consumer placement and interface.

A dependency is `satisfied` only when one canonical provider and one canonical provider placement are resolved and that exact placement is Ready. The evaluator reports `blocked` when positive proof is absent, including these reasons:

| Finding | Meaning |
|---|---|
| `no_active_dmap_v2_authority` | No usable current DMap/2 authority/DForward context |
| `provider_unresolved` | Current topology yields no provider candidate |
| `provider_ambiguous` | More than one provider candidate remains |
| `provider_not_diot` | Resolved provider is not a canonical DIoT |
| `provider_placement_missing` | No current accepted placement exists for the provider |
| `provider_placement_ambiguous` | More than one current provider placement exists |
| `provider_readiness_missing` | Exact provider placement has no D1 readiness result |
| `provider_not_ready` | Exact provider placement is NotReady |
| `satisfied` | Exact provider placement is Ready |

The read-only D2 endpoint accepts no caller-supplied DForward, provider selection, policy or evaluation time. Provider identity comes from current accepted authority.

## Sources

[D1 core](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/dmonitor_readiness.rs), [D2 dependency core](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/dforward_dependency_readiness.rs), [readiness ADR](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/adr/ADR-0024-canonical-dmonitor-observation-model.md), [ADR-0010](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/adr/ADR-0010-cross-node-readiness-fresh-evidence.md).
