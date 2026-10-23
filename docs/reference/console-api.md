# Console, Live and catalog API

This page summarizes the DServer surfaces used by the current DATUM graphical interfaces. They have different mutation semantics and must not be collapsed into one generic UI API.

## Operations read API

The operations API is read only and capacity-bounded.

| Method | Route | Purpose |
|---|---|---|
| GET | /api/v1/operations/overview | global operational overview used by Console and Live |
| GET | /api/v1/operations/continuum | global physical D-Node/Continuum view used by Console and Live |
| GET | /api/v1/operations/projects/:project_id | project workspace projection |
| GET | /api/v1/operations/projects/:project_id/graph | accepted logical graph projection |
| GET | /api/v1/operations/projects/:project_id/runtime-graph | logical graph plus separately typed realization-evidence projection |
| GET | /api/v1/operations/projects/:project_id/continuum | project overlay on the same global physical node set |

The global Continuum joins structural D-Node facts, accepted placement references, placement-scoped DMonitor interpretation/evidence and optional host resource observation from Resource Registry records currently bound to that D-Node. A project overlay indicates nodes referenced by accepted placements; it does not make nodes project-owned.

Resource Registry host telemetry and DMonitor placement/runtime telemetry remain separate sources and must not be merged into one invented metric.

## DATUM Live usage

DATUM Live uses only:

~~~text
GET /api/v1/operations/overview
GET /api/v1/operations/continuum
~~~

No Live-specific mutation endpoint exists. Alerts/events are correlated to a D-Node only when the canonical subject contains node_id. CPU, memory and age_seconds are displayed metrics and are not thresholded into a new frontend health policy.

## Resource discovery and binding for host observations

| Method | Route | Purpose |
|---|---|---|
| POST | /api/v1/resources/discovery | publish observation-only compute-resource discovery |
| GET | /api/v1/resources | list project-scoped discovered resources |
| GET | /api/v1/resources/:resource_id | read one discovered resource |
| POST | /api/v1/resources/:resource_id/binding | explicitly bind a resource identity to a D-Node |
| GET | /api/v1/resource-bindings | inspect bindings |

Discovery does not automatically assign a resource to a D-Node. Repeated discovery of the same canonical resource updates observation data while preserving the explicit binding.

Generic Sentinel telemetry is a different domain. A node can exist structurally and receive Sentinel/DMonitor traffic while resource_observation remains absent until a Resource Registry record is discovered and bound.

## Management/control APIs used by Console workspaces

The Console also uses governed APIs outside the read-only operations family for D-Graph draft/save flows, placement candidate validation/proposal creation, proposal review/acceptance, reconciliation request/control workflows and catalog definition creation/revision.

Those actions retain their own owner-domain semantics. A browser click does not bypass server validation or node-side execution authorization.

## Service catalog API

The catalog API mutates catalog definitions only.

| Method | Route | Purpose |
|---|---|---|
| GET | /api/v1/catalog/services | list latest reusable definitions |
| POST | /api/v1/catalog/services | create a definition at initial revision |
| GET | /api/v1/catalog/services/:id | read latest revision |
| POST | /api/v1/catalog/services/:id/revisions | create the next immutable revision |
| GET | /api/v1/catalog/services/:id/revisions/:revision | read one exact historical revision |
| GET | /api/v1/catalog/artifacts | list verified operational artifact snapshots available for pinning |
| GET | /api/v1/catalog/artifacts/:snapshot | read one exact captured artifact snapshot |

Catalog writes do not create a D-Graph, accepted D-Map, runtime instance or monitoring producer.

## Sources

- [operations API](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/dserver/src/api/operations.rs)
- [Continuum API](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/dserver/src/api/continuum_view.rs)
- [Continuum composition](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/dserver/src/core/continuum_view.rs)
- [resource registry](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/dserver/src/core/resource_registry.rs)
- [resource binding](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/dserver/src/core/resource_binding.rs)
- [Console router](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/console/src/app/router.ts)
- [Live view](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/console/src/live/live-view.ts)
