# Complete DServer HTTP API

This page inventories the HTTP routes mounted by DServer at the Phase 114D2 baseline. It is intentionally broader than the [core control-plane API](core-api.md).

!!! important "How to read this catalog"
    **Existence is not authority.** DServer contains canonical, operational, legacy/compatibility and tooling subsystems from multiple development stages. This catalog documents what is mounted in the router; it does not declare every payload a canonical DATUM contract or every route equally stable.

## Classification

| Label | Meaning |
|---|---|
| **Core** | Current canonical/control-plane authority, execution authorization or canonical evidence/readiness |
| **Operational** | Concrete runtime/deployment/agent records surrounding authority |
| **Legacy** | Earlier graph/topology/snapshot/Controlled-WASM surfaces retained in the prototype |
| **Auxiliary** | Dashboard, analysis, AI, planning/materialization or inspection tooling |

The classification is architectural guidance for readers, not an API support guarantee.

## Service, GraphQL and dashboards

| Method | Path | Class | Purpose |
|---|---|---|---|
| POST | `/graphql` | Auxiliary | GraphQL request endpoint |
| GET | `/graphiql` | Auxiliary | GraphiQL development UI |
| GET | `/health` | Auxiliary | Basic DServer health probe |
| GET | `/api/v1/dashboard` | Auxiliary | Dashboard model |
| GET | `/api/v1/dashboard/live` | Auxiliary | Live dashboard state |
| GET | `/api/v1/graph-overview` | Auxiliary | Graph overview for UI/inspection |
| GET | `/dashboard/live` | Auxiliary | Live dashboard HTML |

## Alternative paths and external AI inference

| Method | Path | Class | Purpose |
|---|---|---|---|
| GET | `/api/v1/alternative-paths` | Auxiliary | Alternative-path planning/analysis view |
| GET | `/api/v1/alternative-paths/inference-request` | Auxiliary | Read external AI inference request |
| POST | `/api/v1/alternative-paths/inference-response` | Auxiliary | Submit external AI inference response |

These are analysis/planning surfaces, not active D-Map placement authority by themselves.

## Reconciliation and deployment preflight

| Method | Path | Class | Purpose |
|---|---|---|---|
| GET | `/api/v1/nodes/:node_id/operational-reconciliation-context` | Operational | Read reconciliation context for a node |
| GET | `/api/v1/nodes/:node_id/governed-deployment-preflight` | Operational | Read governed deployment preflight |
| GET | `/api/v1/nodes/:node_id/deployment-secrets-preflight` | Operational | Secret-resolution preflight |
| GET | `/api/v1/nodes/:node_id/deployment-secrets-contract` | Operational | Secret resolver contract/introspection |

## Legacy `ServiceArtifact` registry

| Method | Path | Class | Purpose |
|---|---|---|---|
| POST | `/api/v1/service-artifacts` | Operational | Create/register legacy/executor service artifact |
| GET | `/api/v1/service-artifacts` | Operational | List service artifacts |
| GET | `/api/v1/service-artifacts/:artifact_id` | Operational | Read service artifact |
| PUT | `/api/v1/service-artifacts/:artifact_id` | Operational | Replace/update service artifact |
| DELETE | `/api/v1/service-artifacts/:artifact_id` | Operational | Delete service artifact |
| POST | `/api/v1/service-artifacts/:artifact_id/image-identity/resolve` | Operational | Resolve container image identity |

Do not confuse this domain with canonical `datum.dserv-artifact/1` D-Code metadata under `/api/v1/dcode/artifacts`.

## Resource registry

| Method | Path | Class | Purpose |
|---|---|---|---|
| GET | `/api/v1/resources` | Operational | List discovered resources |
| GET | `/api/v1/resource-bindings` | Operational | List resource bindings |
| POST | `/api/v1/resources/discovery` | Operational | Submit resource discovery |
| GET | `/api/v1/resources/:resource_id` | Operational | Read resource record |
| POST | `/api/v1/resources/:resource_id/binding` | Operational | Create resource binding |
| GET | `/api/v1/resources/:resource_id/binding` | Operational | Read resource binding |

Resource-registry records are not the canonical D-Node structural registry. In particular, opaque/operational capacity-profile information must not be silently treated as canonical D-Continuum numeric capacity.

## Operational project and OperationalDGraph surfaces

| Method | Path | Class | Purpose |
|---|---|---|---|
| GET | `/api/v1/projects` | Operational | List operational projects |
| POST | `/api/v1/projects` | Operational | Register operational project |
| PUT | `/api/v1/operational-dgraph` | Operational | Set operational desired graph |
| GET | `/api/v1/operational-dgraph` | Operational | Read operational desired graph |
| GET | `/api/v1/nodes/:node_id/operational-dgraph-slice` | Operational | Read node-scoped slice |
| POST | `/api/v1/nodes/:node_id/operational-reconciliation/authorize` | Operational | Authorize reconciliation |
| POST | `/api/v1/nodes/:node_id/operational-reconciliation/rollback-authorize` | Operational | Authorize reconciliation rollback |
| POST | `/api/v1/operational-evidence` | Operational | Submit operational evidence |
| GET | `/api/v1/operational-evidence` | Operational | List operational evidence |

`OperationalDGraph` is not canonical `datum.dgraph/1`.

## Analysis context and observed graph

| Method | Path | Class | Purpose |
|---|---|---|---|
| POST | `/api/v1/analysis-context/passive/:node_id` | Auxiliary | Acquire passive analysis context |
| POST | `/api/v1/analysis-context/active` | Auxiliary | Acquire active analysis context |
| GET | `/api/v1/observed-dgraph` | Operational | Read legacy/operational observed graph |

## SmartSentinel registration and telemetry

| Method | Path | Class | Purpose |
|---|---|---|---|
| GET | `/api/v1/sentinels` | Operational | List Sentinel registrations |
| GET | `/api/v1/sentinels/:node_id` | Operational | Read Sentinel registration |
| PUT | `/api/v1/sentinels/:node_id/registration` | Operational | Register/re-register Sentinel instance |
| POST | `/api/v1/sentinels/:node_id/heartbeat` | Operational | Submit Sentinel heartbeat |
| GET | `/api/v1/sentinels/telemetry` | Operational | List telemetry |
| POST | `/api/v1/sentinels/:node_id/telemetry` | Operational | Submit telemetry envelope |
| GET | `/api/v1/sentinels/:node_id/telemetry` | Operational | Read latest telemetry |
| GET | `/api/v1/sentinels/:node_id/telemetry/history` | Operational | Read telemetry history |

Sentinel telemetry is not automatically canonical DMonitor evidence. Canonical evidence uses `/api/v1/dmonitor/observations/:project_id` and typed `datum.dmonitor-observation/1`.

## Controlled/Management WASM legacy path

| Method | Path | Class | Purpose |
|---|---|---|---|
| POST | `/api/v1/controlled-wasm/dgraph` | Legacy | Submit Controlled-WASM graph |
| GET | `/api/v1/controlled-wasm/dgraph` | Legacy | Read Controlled-WASM graph |
| GET | `/api/v1/controlled-wasm/observed-dgraph` | Legacy | Read observed Controlled-WASM graph |
| POST | `/api/v1/controlled-wasm/deployment-manifest` | Legacy | Submit deployment manifest |
| GET | `/api/v1/controlled-wasm/deployment-manifest` | Legacy | Read deployment manifest |
| GET | `/api/v1/controlled-wasm/deployment/for-node/:node_id` | Legacy | Read node-scoped deployment |
| POST | `/api/v1/controlled-wasm/live-reports` | Legacy | Submit live report |
| GET | `/api/v1/controlled-wasm/live-reports` | Legacy | List live reports |
| POST | `/api/v1/controlled-wasm/deployment-attempts` | Legacy | Create deployment attempt |
| GET | `/api/v1/controlled-wasm/deployment-attempts` | Legacy | List deployment attempts |
| GET | `/api/v1/controlled-wasm/deployment-attempts/:attempt_id` | Legacy | Read attempt |
| POST | `/api/v1/controlled-wasm/deployment-attempts/:attempt_id/transition` | Legacy | Transition attempt state |
| POST | `/api/v1/controlled-wasm/deployment-attempts/:attempt_id/retry` | Legacy | Retry attempt |

Controlled/Management WASM must not be documented as application D-Code.

## Snapshot, legacy node and capability surfaces

| Method | Path | Class | Purpose |
|---|---|---|---|
| POST | `/api/v1/snapshots` | Legacy | Ingest legacy snapshot |
| GET | `/api/v1/nodes` | Legacy | List legacy snapshot nodes |
| GET | `/api/v1/nodes/:node_id/latest` | Legacy | Read latest legacy node snapshot |
| POST | `/api/v1/nodes/:node_id/capabilities` | Legacy | Publish node capabilities in legacy capability domain |
| GET | `/api/v1/nodes/:node_id/capabilities` | Legacy | Read legacy capabilities |
| GET | `/api/v1/capabilities` | Legacy | List capabilities |

These `/nodes` routes differ from canonical structural `/dnodes` routes.

## Action results and WASM runtime reports

| Method | Path | Class | Purpose |
|---|---|---|---|
| POST | `/api/v1/nodes/:node_id/action-results` | Operational | Submit action execution report |
| GET | `/api/v1/nodes/:node_id/action-results/latest` | Operational | Read latest node action result |
| GET | `/api/v1/action-results/latest` | Operational | List latest action results |
| POST | `/api/v1/nodes/:node_id/wasm-runtime-reports` | Legacy | Submit WASM runtime report |
| GET | `/api/v1/nodes/:node_id/wasm-runtime-reports/latest` | Legacy | Read latest node WASM runtime report |
| GET | `/api/v1/wasm-runtime-reports/latest` | Legacy | List latest WASM runtime reports |
| POST | `/api/v1/wasm-modules` | Legacy | Register WASM module descriptor |
| GET | `/api/v1/wasm-modules` | Legacy | List module descriptors |
| GET | `/api/v1/wasm-modules/:module_id` | Legacy | Read module descriptor |

## Legacy graph/topology/DMap surfaces

| Method | Path | Class | Purpose |
|---|---|---|---|
| GET | `/api/v1/graph/latest` | Legacy | Read latest graph |
| GET | `/api/v1/graph/materialized` | Legacy | Read materialized graph |
| GET | `/api/v1/analysis/latest` | Auxiliary | Analyze latest graph |
| POST | `/api/v1/topology` | Legacy | Set topology |
| GET | `/api/v1/topology` | Legacy | Read topology |
| POST | `/api/v1/dmap` | Legacy | Set older DMap representation |
| GET | `/api/v1/dmap` | Legacy | Read older DMap representation |

These routes predate/are distinct from canonical D-Deploy-owned `datum.dmap/1|2` acceptance. Use `/api/v1/ddeploy/...` for current canonical placement governance.

## Canonical D-Deploy: DMap/1

| Method | Path | Class | Purpose |
|---|---|---|---|
| POST | `/api/v1/ddeploy/proposals/validate` | Core | Validate v1 proposal candidate |
| POST | `/api/v1/ddeploy/proposals` | Core | Create immutable v1 proposal |
| POST | `/api/v1/ddeploy/plan` | Core | Deterministically plan/create candidate path |
| GET | `/api/v1/ddeploy/proposals/:proposal_id` | Core | Read proposal |
| POST | `/api/v1/ddeploy/proposals/:proposal_id/accept` | Core | Explicitly accept/materialize authority |
| GET | `/api/v1/ddeploy/active` | Core | Read active placement |

## Canonical D-Deploy: DMap/2

| Method | Path | Class | Purpose |
|---|---|---|---|
| POST | `/api/v1/ddeploy/v2/proposals/validate` | Core | Validate DMap/2 candidate |
| POST | `/api/v1/ddeploy/v2/proposals` | Core | Create v2 proposal |
| GET | `/api/v1/ddeploy/v2/proposals/:proposal_id` | Core | Read v2 proposal |
| POST | `/api/v1/ddeploy/v2/proposals/:proposal_id/accept` | Core | Accept/materialize DMap/2 authority |
| GET | `/api/v1/ddeploy/v2/authority` | Core | Read current active v2 authority |

## Canonical structural D-Node/D-Continuum

| Method | Path | Class | Purpose |
|---|---|---|---|
| GET | `/api/v1/dnodes` | Core | List structural D-Nodes |
| PUT | `/api/v1/dnodes/:node_id` | Core | Declare structural D-Node |
| GET | `/api/v1/dnodes/:node_id` | Core | Read structural D-Node |
| DELETE | `/api/v1/dnodes/:node_id` | Core | Remove structural D-Node |
| GET | `/api/v1/dcontinuum/authoritative` | Core | Read server-derived authoritative D-Continuum |

## Canonical D-Code

| Method | Path | Class | Purpose |
|---|---|---|---|
| POST | `/api/v1/dcode/artifacts` | Core | Declare canonical D-Serv artifact/D-Code metadata |
| GET | `/api/v1/dcode/artifacts/:application_id/:dserv_id` | Core | Read canonical D-Serv artifact |
| POST | `/api/v1/dcode/authorize` | Core | Authorize D-Code invocation under current authority |

## D-Call

| Method | Path | Class | Purpose |
|---|---|---|---|
| PUT | `/api/v1/dcall/endpoints/:node_id/:transport` | Operational | Register D-Call transport endpoint |
| GET | `/api/v1/dcall/endpoints/:node_id/:transport` | Operational | Read D-Call transport endpoint |
| GET | `/api/v1/dcall/calls/:project_id/:application_id/:source_service_id` | Core | Derive/list calls/routes for source service |
| POST | `/api/v1/dcall/grants` | Core | Request single-use delivery grant |
| POST | `/api/v1/dcall/grants/:grant_id/redeem` | Core | Redeem grant |

## DIoT runtime bindings

| Method | Path | Class | Purpose |
|---|---|---|---|
| PUT | `/api/v1/diot/runtime-bindings/:project_id/:application_id/:placement_id` | Core | Bind accepted DIoT placement to concrete broker URI |
| GET | `/api/v1/diot/runtime-bindings/:project_id/:application_id/:placement_id` | Core | Read binding |
| GET | `/api/v1/diot/runtime-bindings/:project_id/:application_id/:placement_id/current` | Core | Read binding with current-authority semantics |

## Canonical DMonitor and readiness

| Method | Path | Class | Purpose |
|---|---|---|---|
| POST | `/api/v1/dmonitor/observations/:project_id` | Core | Ingest canonical observation |
| GET | `/api/v1/dmonitor/observations/:project_id/streams` | Core | List stream heads |
| GET | `/api/v1/dmonitor/observations/:project_id/by-id/:observation_id` | Core | Read observation by ID |
| GET | `/api/v1/dmonitor/observations/:project_id/:node_id/:monitor_instance_id/head` | Core | Read monitor stream head |
| POST | `/api/v1/dmonitor/convergence/:project_id/:application_id/evaluate` | Core | Derive convergence |
| GET | `/api/v1/dmonitor/readiness/:project_id/:application_id` | Core | Derive D1 readiness |
| GET | `/api/v1/dforward/dependency-readiness/:project_id/:application_id/:node_id` | Core | Derive D2 `any_element` dependency readiness |

## Action/deployment/installation planning

| Method | Path | Class | Purpose |
|---|---|---|---|
| GET | `/api/v1/action-plan/latest` | Auxiliary | Build/read latest action plan |
| GET | `/api/v1/action-plan/materialized` | Auxiliary | Read materialized action plan |
| GET | `/api/v1/deployment-planning/latest` | Auxiliary | Read latest deployment planning |
| GET | `/api/v1/deployment-planning/for-node/:node_id` | Auxiliary | Node-scoped deployment planning |
| GET | `/api/v1/installation-plan/latest` | Auxiliary | Read latest installation plan |
| GET | `/api/v1/installation-plan/for-node/:node_id` | Auxiliary | Node-scoped installation plan |
| POST | `/api/v1/installation-tasks/materialize` | Operational | Materialize installation tasks |
| POST | `/api/v1/installation-tasks/materialize/for-node/:node_id` | Operational | Materialize node tasks |
| GET | `/api/v1/installation-tasks` | Operational | List installation tasks |

These workflows coexist with canonical D-Deploy; they should not be interpreted as a second canonical D-Map authority unless a specific contract explicitly establishes that relationship.

## Local mapping recommendation/preflight

| Method | Path | Class | Purpose |
|---|---|---|---|
| GET | `/api/v1/local-mapping-recommendations` | Auxiliary | List mapping recommendations |
| GET | `/api/v1/local-mapping-recommendations/for-node/:node_id` | Auxiliary | Node-scoped recommendations |
| GET | `/api/v1/local-mapping-patch-proposals` | Auxiliary | List mapping patch proposals |
| GET | `/api/v1/local-mapping-patch-proposals/for-node/:node_id` | Auxiliary | Node-scoped patch proposals |
| GET | `/api/v1/local-mapping-preflight/latest` | Operational | List latest preflight reports |
| POST | `/api/v1/nodes/:node_id/local-mapping-preflight` | Operational | Submit node preflight report |
| GET | `/api/v1/nodes/:node_id/local-mapping-preflight/latest` | Operational | Read latest node preflight |

## Local DGraph snapshots and materialized DGraph analysis

| Method | Path | Class | Purpose |
|---|---|---|---|
| POST | `/api/v1/nodes/:node_id/dgraph-snapshot` | Operational | Submit local DGraph snapshot |
| GET | `/api/v1/nodes/:node_id/dgraph-snapshot/latest` | Operational | Read latest node snapshot |
| GET | `/api/v1/dgraph-snapshots/latest` | Operational | List latest snapshots |
| GET | `/api/v1/dgraph/materialized` | Auxiliary | Read materialized graph view |
| GET | `/api/v1/dgraph/materialized/summary` | Auxiliary | Read graph summary |
| GET | `/api/v1/dgraph/planner/dry-run` | Auxiliary | Read planner dry-run |
| GET | `/api/v1/dgraph/planner/dry-run/summary` | Auxiliary | Read dry-run summary |
| GET | `/api/v1/dgraph/readiness/summary` | Auxiliary | Read planning/execution readiness summary |

These `dgraph/*` materialized/planner surfaces are separate from the canonical `datum.dgraph/1` contract definition itself.

## DGraph execution contracts/introspection

| Method | Path | Class | Purpose |
|---|---|---|---|
| GET | `/api/v1/dgraph/artifact-integrity` | Auxiliary | Artifact-integrity contract/view |
| GET | `/api/v1/dgraph/capability-negotiation` | Auxiliary | Capability-negotiation contract/view |
| GET | `/api/v1/dgraph/execution-allowlists` | Auxiliary | Execution allowlist contract/view |
| GET | `/api/v1/dgraph/resource-limits` | Auxiliary | Resource-limit contract/view |
| GET | `/api/v1/dgraph/rollback-audit` | Auxiliary | Rollback audit contract/view |
| GET | `/api/v1/dgraph/execution-prerequisites` | Auxiliary | Execution prerequisite contract/view |
| GET | `/api/v1/dgraph/execution-safety` | Auxiliary | Execution-safety contract/view |
| GET | `/api/v1/dgraph/execution-policy` | Auxiliary | Execution-policy contract/view |
| GET | `/api/v1/dgraph/operator-approval` | Auxiliary | Operator-approval contract/view |

## Installation task lifecycle

| Method | Path | Class | Purpose |
|---|---|---|---|
| GET | `/api/v1/installation-tasks/for-node/:node_id` | Operational | List node installation tasks |
| GET | `/api/v1/installation-tasks/for-node/:node_id/:task_id` | Operational | Read task |
| PATCH | `/api/v1/installation-tasks/for-node/:node_id/:task_id/status` | Operational | Change task status |
| POST | `/api/v1/installation-tasks/for-node/:node_id/:task_id/approval` | Operational | Submit task approval |
| GET | `/api/v1/installation-tasks/for-node/:node_id/:task_id/approval/latest` | Operational | Read latest approval |
| GET | `/api/v1/installation-tasks/for-node/:node_id/:task_id/readiness` | Operational | Read task readiness |
| GET | `/api/v1/installation-tasks/for-node/:node_id/:task_id/assisted-execution-state` | Operational | Read assisted-execution state |
| POST | `/api/v1/installation-tasks/for-node/:node_id/:task_id/assisted-execution-request` | Operational | Create assisted-execution request |
| GET | `/api/v1/installation-tasks/for-node/:node_id/:task_id/assisted-execution-request/latest` | Operational | Read latest request |
| POST | `/api/v1/installation-tasks/for-node/:node_id/:task_id/assisted-execution-request/:request_id/claim` | Operational | Create execution claim |
| GET | `/api/v1/installation-tasks/for-node/:node_id/:task_id/assisted-execution-request/:request_id/claim/latest` | Operational | Read latest claim |
| PATCH | `/api/v1/installation-tasks/for-node/:node_id/:task_id/assisted-execution-request/:request_id/claim/status` | Operational | Update claim status |
| POST | `/api/v1/installation-tasks/for-node/:node_id/:task_id/assisted-execution-request/:request_id/claim/:claim_id/attempt` | Operational | Submit execution attempt |
| GET | `/api/v1/installation-tasks/for-node/:node_id/:task_id/assisted-execution-request/:request_id/claim/:claim_id/attempt/latest` | Operational | Read latest attempt |

## Installation lifecycle aggregate views

| Method | Path | Class | Purpose |
|---|---|---|---|
| GET | `/api/v1/installation-task-approvals/for-node/:node_id` | Operational | List approvals |
| GET | `/api/v1/installation-task-readiness/for-node/:node_id` | Operational | List task-readiness views |
| GET | `/api/v1/assisted-execution-requests/for-node/:node_id` | Operational | List assisted-execution requests |
| GET | `/api/v1/assisted-execution-claims/for-node/:node_id` | Operational | List claims |
| GET | `/api/v1/assisted-execution-attempts/for-node/:node_id` | Operational | List attempts |
| GET | `/api/v1/assisted-execution-state/for-node/:node_id` | Operational | Aggregate assisted-execution state |

## Dispatch, materialized analysis and events

| Method | Path | Class | Purpose |
|---|---|---|---|
| GET | `/api/v1/dispatch/latest` | Operational | Publish/read latest dispatch view |
| GET | `/api/v1/dispatch/for-node/:node_id` | Operational | Node-scoped dispatch |
| GET | `/api/v1/dispatch/materialized` | Operational | Materialized dispatch |
| GET | `/api/v1/analysis/materialized` | Auxiliary | Materialized analysis |
| GET | `/api/v1/events/latest` | Auxiliary | Build/read latest global events |
| GET | `/api/v1/events/materialized` | Auxiliary | Materialized global events |

## Related naming collisions

The following similarly named paths represent different domains and should be checked carefully during debugging:

| Names | Distinction |
|---|---|
| `/api/v1/nodes` vs `/api/v1/dnodes` | legacy snapshot nodes vs canonical structural D-Nodes |
| `/api/v1/dmap` vs `/api/v1/ddeploy/...` | older DMap surface vs canonical D-Deploy-owned placement authority |
| `/api/v1/graph/*`, `/api/v1/dgraph/*`, canonical `datum.dgraph/1` | historical/materialized views vs canonical application contract |
| `/api/v1/service-artifacts` vs `/api/v1/dcode/artifacts` | executor/container artifact domain vs canonical D-Code descriptor |
| Sentinel telemetry vs DMonitor observations | generic/legacy agent telemetry vs typed canonical evidence |
| Controlled WASM vs D-Code | management/executor WASM path vs application D-Serv code |

## Source

All paths and methods above are transcribed from the pinned [DServer Axum router](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/main.rs). Consult the individual API/core modules before relying on request/response field details that are not explicitly documented on this page.
