# Console and catalog API

This page summarizes the DServer surfaces used by the current DATUM Console. They fall into two groups with different mutation semantics.

## Operations read API

The operations API is **read only** and capacity-bounded. It builds projections from existing DServer sources rather than maintaining a second operations database.

| Method | Route | Purpose |
|---|---|---|
| GET | `/api/v1/operations/overview` | global operational overview |
| GET | `/api/v1/operations/projects/:project_id` | project workspace projection |
| GET | `/api/v1/operations/projects/:project_id/graph` | accepted logical graph projection |
| GET | `/api/v1/operations/projects/:project_id/runtime-graph` | logical graph plus separately typed realization-evidence projection |

Responses use `Cache-Control: no-store`.

### Project scope rule

Project-scoped operations routes require:

```text
route :project_id
=
X-Datum-Project header
```

The value must be non-empty, bounded, trimmed and free of control characters. A mismatch is rejected rather than silently projecting another scope.

This is request-scope consistency, not a complete authentication/authorization system.

### Source failures

Projection sources can be independently unavailable or corrupt. The API is designed to preserve safe source issues/availability states where the DTO allows it instead of leaking internal storage paths or inventing healthy data.

### Runtime graph semantics

`runtime-graph` exposes admitted D-Serv realization evidence separately from the accepted logical graph. It is read-only and cannot create placement.

The runtime source kind identifies admitted realization evidence, not an execution-instance registry. A POST to the read route is not allowed.

## Service catalog API

The catalog API mutates **catalog definitions only**.

| Method | Route | Purpose |
|---|---|---|
| GET | `/api/v1/catalog/services` | list latest reusable definitions |
| POST | `/api/v1/catalog/services` | create a definition at initial revision |
| GET | `/api/v1/catalog/services/:id` | read latest revision |
| POST | `/api/v1/catalog/services/:id/revisions` | create the next immutable revision |
| GET | `/api/v1/catalog/services/:id/revisions/:revision` | read one exact historical revision |
| GET | `/api/v1/catalog/artifacts` | list verified operational artifact snapshots available for pinning |
| GET | `/api/v1/catalog/artifacts/:snapshot` | read one exact captured artifact snapshot |

There is no delete route in the current catalog API.

## Save request

Catalog create/revise uses a body shaped as:

```json
{
  "definition": { "...": "service definition draft" },
  "expected_revision": 0
}
```

For creation, `expected_revision` must be `0`. For a new revision, it must match the current expected revision. Conflicts fail closed.

## Catalog definition fields

A definition can include:

- stable definition ID and name;
- `atomic` or `composite` shape;
- exact operational artifact reference for atomic services;
- static or declarative-discovered composition for composites;
- tenancy capability and optional tenant unit;
- CPU/memory/storage requirements;
- physical capability requirements;
- HTTP/TCP health-check intent;
- monitoring cadence intent;
- secret references/version/target environment variable;
- exact dependency revisions;
- required/provided service capabilities;
- immutable repository/Compose metadata for declarative composite provisioning.

See [Service catalog](../concepts/service-catalog.md) for semantics.

## Exact artifact pinning

The catalog does not duplicate ServiceArtifact resolution. When an atomic definition is saved, DServer re-reads the referenced operational artifact and captures a narrow verified snapshot.

Reference identity includes:

```text
project_id
artifact_id
execution_generation
execution_projection_digest
```

Container snapshots require valid resolved OCI identity. Native-process snapshots require an exact executable SHA-256.

If the referenced artifact changed since the editor loaded it, save conflicts instead of repinning silently.

## Catalog persistence

The catalog database path is configured with:

```text
DATUM_SERVICE_CATALOG_DB_PATH
```

DServer refuses to initialize the catalog on the configured control-state or event/alert database path. If persistence is absent/unavailable, the API returns a safe `catalog_unavailable` response; it does not fall back to transient process memory.

## What catalog POST does not do

A successful catalog write does not:

- create a D-Graph;
- create a D-Deploy proposal;
- accept a D-Map;
- pull/start a container;
- spawn a native process;
- install/execute D-Code;
- create tenant or requirement bindings;
- emit monitoring evidence;
- clone a repository or run a provisioning command.

That boundary is intentional.

## Sources

- [operations API](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/dserver/src/api/operations.rs)
- [catalog API](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/dserver/src/api/service_catalog.rs)
- [catalog model/validation](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/dserver/src/core/service_catalog.rs)
- [Console catalog client/view](https://github.com/dnredson/datum/blob/7a79bd84bc05a1ea18870715cc033567ff472afc/console/src/pages/catalog.ts)
