# DATUM Console architecture

DATUM Console is the graphical **presentation and operator-workspace layer** of DATUM v1. Its central architectural rule is simple:

> The interface may compose facts from several domains, but it must not become a parallel source of authority.

## Components

```mermaid
flowchart LR
    CONTROL["DServer control state\nD-Deploy / D-Map / D-Node"] --> OPS["Operations read models"]
    GRAPH["accepted D-Graph snapshots"] --> OPS
    MON["DMonitor / events / alerts"] --> OPS
    OPS --> API["read-only operations API"]
    CATDB["Service Catalog DB"] --> CATAPI["catalog API"]
    ART["ServiceArtifact registry"] --> CATAPI
    API --> UI["DATUM Console"]
    CATAPI --> UI
```

The operations API is read-only. Catalog write routes mutate **catalog definitions only**; they do not produce placement, runtime mutation or monitoring evidence.

## Frontend stack

The published Console is a lightweight TypeScript/Vite application using:

- TypeScript;
- Vite;
- Bootstrap;
- Bootstrap Icons;
- Cytoscape for graph rendering.

The client has explicit route parsing and validates project identifiers before creating project URLs.

## Route model

~~~text
/
├── projects
│   └── :project_id
│       ├── graph
│       │   └── edit
│       ├── continuum
│       ├── placement
│       ├── history
│       ├── proposals/:proposal_id
│       └── applications/:application_id
│           └── deploy
├── continuum
└── catalog
~~~

The Console now contains both read-only and governed action workspaces. Graph editing creates a draft, placement creates/validates/proposes a candidate, proposal review can explicitly accept placement authority, and deploy/reconciliation creates control-plane requests while host mutation remains a node-side responsibility.

## Read-projection architecture

The operations API reads existing DServer sources and builds bounded projection DTOs. It is designed so that a failing source can remain explicitly unavailable/corrupt rather than poisoning every other dimension or silently becoming an empty successful result.

Project-scoped operations routes require the route project ID and `X-Datum-Project` header to match. This provides scope consistency for the read request; it should not be described as a general authentication mechanism.

## Global and project workspaces

The Console does not synthesize one universal `project.status` value. Instead, the project workspace exposes dimensions such as:

- source coverage;
- known application references and their provenance;
- accepted placement references;
- alerts/attention;
- recent operational events;
- monitoring/temporal context;
- source/read issues.

Keeping dimensions independent avoids turning “one red thing exists” into “the whole project is red”, or “no loaded alert” into “the project is healthy”.

## Logical graph source

The graph uses accepted logical application snapshots. Application grouping in Cytoscape is presentation-only; the canonical D-Graph still contains D-Serv and D-Call semantics, not an extra UI grouping vertex.

```mermaid
flowchart LR
    DG["accepted D-Graph snapshot"] --> ADAPT["typed graph projection"] --> CY["Cytoscape"]
```

The graph can be filtered by included application snapshot and exposes canonical graph IDs/revisions/digests in the details view.

## Runtime evidence source

A separate runtime-graph projection supplies admitted DMonitor D-Serv-realization evidence. The UI may associate evidence to logical D-Servs by exact project/application/service identity.

```mermaid
flowchart LR
    LOG["logical D-Serv"] -->|"presentation association"| EV["admitted realization evidence"]
    EV --> OBS["observation identity / time / collector / health claim"]
```

That association does **not** assert:

- current placement;
- a unique running process;
- convergence;
- current readiness;
- ownership of the runtime by the UI.

A monitor epoch is not an execution-instance identifier. An observed D-Map reference is not a convergence result.

## Bounded previews and completeness

Operational views can be bounded. The runtime graph, for example, reports how many latest subject/monitor-epoch records were included and whether the projection is partial.

The UI therefore carries completeness/availability information alongside data. Operators must be able to distinguish:

```text
empty and complete
partial preview
source unavailable
source corrupt
source not configured
```

These states are semantically different.

## Visual semantic contract

Graph styling classifies presentation:

| Category | Interpretation |
|---|---|
| infrastructure | execution resource, not project ownership |
| logical software | logical D-Serv/component, not runtime instance |
| runtime | realization evidence distinct from logical software |
| storage | explicitly modeled storage |
| IoT/device | explicitly modeled device |

Relations include logical D-Call, realization, placement, physical/network and observation/monitoring semantics. Styling never creates the relationship; a typed source must support it first.

Status overlays are likewise visual tokens. They must retain the underlying entity category and must not invent a new canonical health model.

## Catalog architecture

The catalog has its own persistence (`DATUM_SERVICE_CATALOG_DB_PATH`) and a narrow mutation boundary.

```mermaid
flowchart LR
    REG["ServiceArtifact registry"] --> PIN["verified artifact snapshot"]
    PIN --> DEF["Service Definition revision"]
    DB["Catalog DB"] --> DEF
    DEF -. "does not deploy" .-> DEP["D-Deploy / runtime"]
```

Atomic definitions pin verified artifact identity. Composite definitions describe exact components or declarative discovery/provisioning metadata. Catalog save cannot start software.

## Security/fail-closed principles visible in the UI

- malformed project identifiers are rejected by routing;
- project-scoped reads require matching route/header scope;
- unsafe repository URLs/paths are rejected in catalog definitions;
- secret values are not catalog fields;
- stale catalog revision/artifact identity conflicts rather than silently overwriting;
- unreadable sources remain explicit errors/availability states;
- exact identities are shown rather than replaced by friendly-but-ambiguous names.

## Relationship to DATUM Live

DATUM Live is a separate frontend entry point built from the same TypeScript/Vite project. It shares typed API clients and presentation primitives with the Console but is intentionally GET-only and does not mount the Console router. The Console remains the management surface; Live remains the continuously open observation surface.

See [DATUM Live architecture](live.md) for profile persistence, Area of Interest selection, kiosk behavior and card-state semantics.

## Sources

- [Console router](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/console/src/app/router.ts)
- [project workspace](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/console/src/pages/project-workspace.ts)
- [project graph](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/console/src/pages/project-graph.ts)
- [graph visual semantics](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/console/src/components/graph-visuals.ts)
- [operations API](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/dserver/src/api/operations.rs)
- [catalog API](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/dserver/src/api/service_catalog.rs)
