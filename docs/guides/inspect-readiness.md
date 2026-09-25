# Inspect readiness

Use these read-only tasks when DServer is already running with the intended project and application state. They do not register nodes, deploy workloads or publish synthetic observations.

## Query application readiness

Replace the example values with the base URL and identifiers of your test environment. Percent-encode identifiers if they contain URL-reserved characters.

```bash
DSERVER_URL='http://127.0.0.1:8080'
PROJECT_ID='your-project-id'
APPLICATION_ID='your-application-id'

curl --fail-with-body --silent --show-error \
  "$DSERVER_URL/api/v1/dmonitor/readiness/$PROJECT_ID/$APPLICATION_ID"
```

The address above is an example, not a promised default port. The handler selects policy and evaluation time on the server. Do not attach a freshness override or a replacement DMap/DForward object.

Read the result in this order: confirm project/application and evaluation time; inspect top-level readiness/findings; locate required DServ and DIoT placements; then inspect current health, convergence, admitted/excluded evidence and exact authority references for any NotReady placement.

A successful HTTP request means the read completed. It does not mean the application is Ready.

## Query `any_element` dependency readiness

For D2, add the consumer node whose placed DIoTs should be evaluated:

```bash
NODE_ID='cloud-01'

curl --fail-with-body --silent --show-error \
  "$DSERVER_URL/api/v1/dforward/dependency-readiness/$PROJECT_ID/$APPLICATION_ID/$NODE_ID"
```

The server resolves providers from current accepted DMap/2/DForward authority. There is no request body or query parameter for selecting a provider, changing policy or supplying evaluation time.

Inspect top-level authority findings first. Then inspect each dependency's consumer placement/interface, resolved provider DIoT/placement/node, embedded provider placement readiness, `state`, and findings. A dependency can be `satisfied` while whole-application readiness is `not_ready` because unrelated required placements are evaluated separately.

## Common diagnoses

| Finding | What to inspect next |
|---|---|
| `no_active_placement_authority` | Whether the intended application has accepted placement authority |
| `no_required_runtime_realizations` | Whether the accepted map requires any realizations |
| `dserv_not_converged` | Canonical DServ evidence and its authority correlation |
| `diot_not_converged` | Current DIoT placement, binding and admitted evidence |
| `health_unknown` | Whether usable current health evidence exists |
| `health_degraded` / `health_unhealthy` | The admitted observations and runtime condition |
| `conflicting_current_health` | Disagreeing admitted observations and their provenance |
| `no_active_dmap_v2_authority` | Whether current accepted authority is DMap/2 and carries accepted DForward context |
| `provider_unresolved` / `provider_ambiguous` | Current DForward chains/hops and provider candidates for the required interface |
| `provider_placement_missing` / `provider_placement_ambiguous` | Current accepted DIoT placement authority for the provider |
| `provider_readiness_missing` / `provider_not_ready` | The exact provider placement's D1 readiness and evidence |

The generic SmartSentinel bridge is not a canonical DServ emitter. Do not resolve that absence by treating a container with a similar name as the required service.

See [readiness semantics](../operations/readiness.md) and the [API reference](../reference/readiness-api.md).
