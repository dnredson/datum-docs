# Core control-plane API

This page selects the HTTP surfaces most directly tied to the current canonical DATUM control plane. For every route exposed by DServer, including legacy/operational/tooling families, see the [complete HTTP API](http-api.md).

!!! warning "Route does not equal canonical contract"
    HTTP is an implementation surface. The canonical authority rules come from contracts/ADRs and server-owned state transitions. A route can expose a canonical object, a derived result, an operational record or an older compatibility model.

## Base behavior

DServer's configured bind address defaults to `0.0.0.0:8080` when no explicit server bind is supplied. Examples in this documentation use `http://127.0.0.1:8080` only as a local example.

`GET /health` is the minimal service health route. `/graphql` and `/graphiql` are also mounted but are not substitutes for the canonical REST control-plane workflows documented below.

## D-Node structural registry

| Method | Path | Purpose | Mutation |
|---|---|---|---:|
| GET | `/api/v1/dnodes` | List server-owned structural D-Node declarations | No |
| PUT | `/api/v1/dnodes/:node_id` | Declare/idempotently redeclare one structural D-Node | Yes |
| GET | `/api/v1/dnodes/:node_id` | Read one structural D-Node declaration | No |
| DELETE | `/api/v1/dnodes/:node_id` | Remove a structural declaration | Yes |
| GET | `/api/v1/dcontinuum/authoritative` | Derive/read server-authoritative structural D-Continuum view | No |

A D-Node declaration is platform + static capacity + D-Node ABI capability set. It is independent of Sentinel registration/liveness.

## D-Deploy / active placement authority

### DMap/1 workflow

| Method | Path | Purpose |
|---|---|---|
| POST | `/api/v1/ddeploy/proposals/validate` | Validate a v1 candidate without activation |
| POST | `/api/v1/ddeploy/proposals` | Create immutable v1 proposal |
| POST | `/api/v1/ddeploy/plan` | Produce deterministic proposal/planning result through the current planner path |
| GET | `/api/v1/ddeploy/proposals/:proposal_id` | Read proposal record |
| POST | `/api/v1/ddeploy/proposals/:proposal_id/accept` | Explicitly accept/materialize active DMap/1 |
| GET | `/api/v1/ddeploy/active` | Read active v1-compatible placement view |

### DMap/2 workflow

| Method | Path | Purpose |
|---|---|---|
| POST | `/api/v1/ddeploy/v2/proposals/validate` | Validate DMap/2 candidate with DForward/DIoT semantics |
| POST | `/api/v1/ddeploy/v2/proposals` | Create immutable v2 proposal |
| GET | `/api/v1/ddeploy/v2/proposals/:proposal_id` | Read v2 proposal |
| POST | `/api/v1/ddeploy/v2/proposals/:proposal_id/accept` | Explicitly accept/materialize DMap/2 authority |
| GET | `/api/v1/ddeploy/v2/authority` | Read current active DMap/2 authority view |

Creating/validating a proposal never changes placement authority. Acceptance is the authority transition.

## D-Code artifact and invocation authorization

| Method | Path | Purpose |
|---|---|---|
| POST | `/api/v1/dcode/artifacts` | Declare canonical `datum.dserv-artifact/1` metadata/identity |
| GET | `/api/v1/dcode/artifacts/:application_id/:dserv_id` | Read registered artifact for one D-Serv |
| POST | `/api/v1/dcode/authorize` | Evaluate current authority for a D-Code invocation |

The artifact registry is separate from legacy `ServiceArtifact`. D-Code bytes themselves are not stored in this registry.

## D-Call endpoints, route authority and grants

| Method | Path | Purpose |
|---|---|---|
| PUT | `/api/v1/dcall/endpoints/:node_id/:transport` | Register/update transport endpoint metadata for a D-Node |
| GET | `/api/v1/dcall/endpoints/:node_id/:transport` | Read endpoint metadata |
| GET | `/api/v1/dcall/calls/:project_id/:application_id/:source_service_id` | Derive/list canonical calls/routes available from a source service |
| POST | `/api/v1/dcall/grants` | Request short-lived delivery grant under current authority |
| POST | `/api/v1/dcall/grants/:grant_id/redeem` | Atomically redeem one grant |

The caller never supplies an arbitrary destination service/node/port as route authority. DServer derives the destination from active canonical state and artifact port compatibility.

## DIoT runtime binding

| Method | Path | Purpose |
|---|---|---|
| PUT | `/api/v1/diot/runtime-bindings/:project_id/:application_id/:placement_id` | Register/re-register concrete broker URI for an accepted DIoT placement |
| GET | `/api/v1/diot/runtime-bindings/:project_id/:application_id/:placement_id` | Read stored binding, including its recorded authority |
| GET | `/api/v1/diot/runtime-bindings/:project_id/:application_id/:placement_id/current` | Read a binding through current-authority validation semantics |

Binding registration is operational identity, not broker liveness. DMonitor evidence supplies observation.

## DMonitor observation ingestion and stream inspection

| Method | Path | Purpose |
|---|---|---|
| POST | `/api/v1/dmonitor/observations/:project_id` | Ingest one canonical observation |
| GET | `/api/v1/dmonitor/observations/:project_id/streams` | List current stream heads for a project |
| GET | `/api/v1/dmonitor/observations/:project_id/by-id/:observation_id` | Retrieve one observation by ID |
| GET | `/api/v1/dmonitor/observations/:project_id/:node_id/:monitor_instance_id/head` | Read one monitor stream head |

Observation ingestion never changes D-Map desired placement.

## Convergence and D1 readiness

| Method | Path | Purpose |
|---|---|---|
| POST | `/api/v1/dmonitor/convergence/:project_id/:application_id/evaluate` | Derive convergence/interpretation against current authority |
| GET | `/api/v1/dmonitor/readiness/:project_id/:application_id` | Derive D1 placement/application readiness |

The readiness endpoint is read-only, uses server-owned policy/evaluation time and does not accept a caller policy override.

## D2 DForward dependency readiness

| Method | Path | Purpose |
|---|---|---|
| GET | `/api/v1/dforward/dependency-readiness/:project_id/:application_id/:node_id` | Evaluate all `any_element` requirements of DIoTs placed on the consumer node |

The provider is resolved by the server from current DMap/2/DForward authority. `node_id` scopes consumer placements; it does not select a provider.

## Typical canonical workflow

A simplified shell-level sequence looks conceptually like:

```text
PUT  /api/v1/dnodes/:node_id
GET  /api/v1/dcontinuum/authoritative
POST /api/v1/dcode/artifacts
POST /api/v1/ddeploy/v2/proposals/validate
POST /api/v1/ddeploy/v2/proposals
POST /api/v1/ddeploy/v2/proposals/:proposal_id/accept
PUT  /api/v1/diot/runtime-bindings/:project/:application/:placement
POST /api/v1/dmonitor/observations/:project
GET  /api/v1/dmonitor/readiness/:project/:application
GET  /api/v1/dforward/dependency-readiness/:project/:application/:consumer_node
```

This is an authority/evidence progression, not a guarantee that every deployment needs every endpoint. A DMap/1 application, for example, has no canonical DIoT placement dimension.

## Error semantics: interpret domain failure separately from transport failure

A successful HTTP read can legitimately return a negative governance result such as NotReady/Blocked. That is different from a lock/storage/internal server error.

Similarly, proposal validation findings are expected domain outputs; they should not be “fixed” by bypassing acceptance gates. Preserve the finding code and exact source revision when diagnosing a failed workflow.

## Source

The route inventory is taken from the pinned [DServer router](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/main.rs). Domain semantics are defined by the corresponding core modules and ADRs linked throughout the [contract reference](contracts.md).
