# Inspect application readiness

Use this read-only task when DServer is already running with the intended project and application state. It does not register nodes, deploy workloads or publish synthetic observations.

## Query the current result

Replace the three example values with the base URL and identifiers of your test environment. Percent-encode identifiers if they contain URL-reserved characters.

```bash
DSERVER_URL='http://127.0.0.1:8080'
PROJECT_ID='your-project-id'
APPLICATION_ID='your-application-id'

curl --fail-with-body --silent --show-error   "$DSERVER_URL/api/v1/dmonitor/readiness/$PROJECT_ID/$APPLICATION_ID"
```

The address above is an example, not a promised default port. The handler selects policy and evaluation time on the server. Do not attach a freshness override or a replacement DMap/DForward object.

## Read the result in order

1. Confirm the result belongs to the intended project/application and evaluation time.
2. Inspect top-level readiness and findings.
3. Locate the required DServ and DIoT placement results.
4. For a NotReady placement, inspect its current-health assessment and nested convergence diagnostics.
5. Check admitted/excluded evidence and exact authority references before drawing a runtime conclusion.

A successful HTTP request means the read completed. It does not mean the application is Ready.

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

The generic SmartSentinel bridge is not a canonical DServ emitter. Do not resolve that absence by treating a container with a similar name as the required service.

See [readiness semantics](../operations/readiness.md) and the [API reference](../reference/readiness-api.md).
