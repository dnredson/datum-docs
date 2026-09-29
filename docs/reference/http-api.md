# HTTP API catalog

This page groups the HTTP routes exposed by the current **DATUM v1** DServer implementation. Route existence does not by itself make a route canonical authority: the tables classify each surface by architectural role.

## Health and UI/tooling

| Method | Route | Role |
|---|---|---|
| GET | `/health` | server health |
| GET | `/api/v1/dashboard` | auxiliary dashboard data |
| GET | `/api/v1/dashboard/live` | auxiliary live dashboard data |
| GET | `/dashboard/live` | auxiliary HTML dashboard |
| GET | `/api/v1/graph-overview` | graph introspection |
| GET | `/api/v1/alternative-paths` | analysis/tooling |

The existing dashboard routes are auxiliary implementation surfaces. The new DATUM management dashboard described in the roadmap is **not implemented yet**.

## Structural D-Node and D-Continuum authority

| Method | Route |
|---|---|
| GET | `/api/v1/dnodes` |
| PUT | `/api/v1/dnodes/:node_id` |
| GET | `/api/v1/dnodes/:node_id` |
| DELETE | `/api/v1/dnodes/:node_id` |
| GET | `/api/v1/dcontinuum/authoritative` |

These are the structural node/continuum surfaces used by canonical placement. Legacy `/api/v1/nodes...` telemetry/snapshot routes are a different domain.

## ServiceArtifact and operational realization

| Method | Route |
|---|---|
| POST/GET | `/api/v1/service-artifacts` |
| GET/PUT/DELETE | `/api/v1/service-artifacts/:artifact_id` |
| POST | `/api/v1/service-artifacts/:artifact_id/image-identity/resolve` |
| GET | `/api/v1/nodes/:node_id/operational-reconciliation-context` |
| GET | `/api/v1/nodes/:node_id/governed-deployment-preflight` |
| GET | `/api/v1/nodes/:node_id/deployment-secrets-preflight` |
| GET | `/api/v1/nodes/:node_id/deployment-secrets-contract` |
| GET | `/api/v1/nodes/:node_id/operational-dgraph-slice` |
| POST | `/api/v1/nodes/:node_id/operational-reconciliation/authorize` |
| POST | `/api/v1/nodes/:node_id/operational-reconciliation/rollback-authorize` |
| POST | `/api/v1/nodes/:node_id/operational-reconciliation/cleanup-authorize` |
| POST/GET | `/api/v1/operational-evidence` |

Operational reconciliation turns current accepted authority plus exact artifact snapshots into governed node-side actions. Acceptance itself does not execute software.

## Resources and operational project state

| Method | Route |
|---|---|
| GET | `/api/v1/resources` |
| POST | `/api/v1/resources/discovery` |
| GET | `/api/v1/resources/:resource_id` |
| GET | `/api/v1/resource-bindings` |
| POST/GET | `/api/v1/resources/:resource_id/binding` |
| GET/POST | `/api/v1/projects` |
| PUT/GET | `/api/v1/operational-dgraph` |

These operational domains support node binding and reconciliation. They do not replace accepted canonical D-Map placement when canonical authority is active.

## D-Deploy v1

| Method | Route |
|---|---|
| POST | `/api/v1/ddeploy/proposals/validate` |
| POST | `/api/v1/ddeploy/proposals` |
| POST | `/api/v1/ddeploy/plan` |
| GET | `/api/v1/ddeploy/proposals/:proposal_id` |
| POST | `/api/v1/ddeploy/proposals/:proposal_id/accept` |
| GET | `/api/v1/ddeploy/active` |

Planning/proposal creation produces candidate state. Explicit acceptance materializes active D-Map authority.

## D-Deploy v2

| Method | Route |
|---|---|
| POST | `/api/v1/ddeploy/v2/proposals/validate` |
| POST | `/api/v1/ddeploy/v2/proposals` |
| GET | `/api/v1/ddeploy/v2/proposals/:proposal_id` |
| POST | `/api/v1/ddeploy/v2/proposals/:proposal_id/accept` |
| GET | `/api/v1/ddeploy/v2/authority` |

DMap/2 extends placement authority with DForward/DIoT realization semantics.

## D-Compile and D-Code

| Method | Route |
|---|---|
| POST | `/api/v1/dcompile/compile` |
| POST | `/api/v1/dcode/artifacts` |
| GET | `/api/v1/dcode/artifacts/:application_id/:dserv_id` |
| GET | `/api/v1/dcode/artifacts/:application_id/:dserv_id/:descriptor_digest` |
| POST | `/api/v1/dcode/authorize` |

DCompile is candidate generation, registration stores immutable descriptor revisions, and authorization derives exact execution permission from current authority.

## D-Call

| Method | Route |
|---|---|
| PUT/GET | `/api/v1/dcall/endpoints/:node_id/:transport` |
| GET | `/api/v1/dcall/calls/:project_id/:application_id/:source_service_id` |
| POST | `/api/v1/dcall/grants` |
| POST | `/api/v1/dcall/grants/:grant_id/redeem` |

D-Call routing derives destination identity from current accepted authority rather than trusting caller-selected targets.

## DIoT runtime bindings

| Method | Route |
|---|---|
| PUT/GET | `/api/v1/diot/runtime-bindings/:project_id/:application_id/:placement_id` |
| GET | `/api/v1/diot/runtime-bindings/:project_id/:application_id/:placement_id/current` |

The binding is operational realization identity/configuration. It does not prove transport health.

## DMonitor, convergence and readiness

| Method | Route |
|---|---|
| POST | `/api/v1/dmonitor/observations/:project_id` |
| GET | `/api/v1/dmonitor/observations/:project_id/streams` |
| GET | `/api/v1/dmonitor/observations/:project_id/by-id/:observation_id` |
| GET | `/api/v1/dmonitor/observations/:project_id/:node_id/:monitor_instance_id/head` |
| POST | `/api/v1/dmonitor/convergence/:project_id/:application_id/evaluate` |
| GET | `/api/v1/dmonitor/readiness/:project_id/:application_id` |
| GET | `/api/v1/dforward/dependency-readiness/:project_id/:application_id/:node_id` |

These routes ingest evidence or derive current interpretations. DMonitor observations are evidence, not desired-state authority.

## Sentinel/telemetry compatibility surfaces

The implementation also exposes Sentinel registration, heartbeat, telemetry, snapshot, capability and materialized-graph APIs such as:

```text
/api/v1/sentinels/...
/api/v1/snapshots
/api/v1/nodes/...
/api/v1/capabilities
/api/v1/graph/...
/api/v1/dgraph/...
```

These surfaces support observation, compatibility or tooling. Do not substitute `/api/v1/nodes` for the structural `/api/v1/dnodes` registry or infer canonical readiness from generic telemetry.

## Controlled-WASM and installation tooling

Additional route families exist for controlled-WASM, deployment planning, installation plans/tasks, local mapping recommendations/preflight, dispatch, analysis and action results. They remain available to their implementation consumers but are not replacements for the canonical D-Graph/D-Map/D-Code/DMonitor authority chain documented above.

For the exact mounted route list, the implementation source is authoritative.

## Legacy D-Map route

`GET/POST /api/v1/dmap` is retained as an older compatibility surface. New canonical placement workflows should use D-Deploy proposal/acceptance authority rather than treating that route as a parallel source of truth.

## Sources

See [Sources and provenance](sources.md) for the pinned DServer route-table source and implementation anchors.
