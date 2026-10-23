# DATUM Live architecture

DATUM Live is the continuously open **read-only presentation surface** of DATUM v1. It is intentionally separate from the management Console.

> Live may make existing evidence easy to notice, but it must not become a new health, placement or runtime authority.

## Purpose and data flow

The Console is optimized for management workflows. Live is optimized to remain visible on a secondary display and answer which D-Nodes the operator chose to watch, what host observation is available, what active attention is associated with a node and what placement-scoped DMonitor evidence exists.

~~~mermaid
flowchart LR
    OPS["GET operations/overview"] --> LIVE["DATUM Live"]
    CONT["GET operations/continuum"] --> LIVE
    LIVE --> PROFILE["local Live profile"]
    LIVE -. "navigation" .-> CONSOLE["DATUM Console"]
~~~

No Live-specific backend endpoint is required.

## Read-only boundary

Live consumes only global operations/overview and operations/continuum reads. It does not accept proposals, reconcile workloads, edit D-Graphs or write operational state. A deployment can additionally restrict the Live reverse proxy to GET/HEAD as defense in depth.

## Global Area of Interest

A Live profile stores an ordered list of pinned D-Node identifiers. The node picker discovers from the global Continuum, not by iterating projects.

A project filter means "nodes referenced by accepted placements from this project"; it does not mean node ownership. The selector uses existing structural/observational fields and never infers fog/edge/cloud from node names.

If a pinned node disappears from the current Continuum response, the profile keeps the identifier and renders an unavailable state instead of silently deleting it.

## Host resource observation

~~~mermaid
flowchart LR
    DISC["SmartSentinel resource discovery"] --> REG["Resource Registry"]
    REG --> BIND["explicit resource -> D-Node binding"]
    DN["D-Node Registry"] --> VIEW["Continuum view"]
    BIND --> VIEW
    VIEW --> LIVE["DATUM Live"]
~~~

Host CPU/memory/swap comes from the Resource Registry path above. Declared capacity, current host usage, placement authority and DMonitor runtime usage remain distinct domains.

Generic Sentinel telemetry and a Resource Registry observation are not interchangeable. A structural D-Node can appear in Live while host resource observation is absent.

## Placement-scoped DMonitor evidence

Continuum observations are attached per accepted placement. A node can legitimately have a current host resource observation while having no accepted workload placement and therefore no placement-scoped DMonitor evidence in its Continuum entry.

Per-placement runtime usage and host Resource Registry usage are never averaged or summed into one metric.

## Attention and card color

Live makes state glanceable with a border/status rail, tint and text badge. The tone can use existing active alert severity and DMonitor placement convergence/health/freshness.

It does not use CPU, memory, observation-age thresholds, node-name heuristics or absence of alerts as proof of health.

A node can be labeled **Observed** when evidence is present without claiming Healthy.

## Alert/event correlation

Alerts and events are associated with a node only when their canonical subject contains node_id. Live does not guess from project/application IDs, hostnames or naming conventions.

## Local profiles and polling

Profiles are schema-versioned browser-local data containing profile identity/name, pinned nodes, refresh interval, kiosk/display preferences and activity filters. Multiple profiles can coexist; a view query parameter selects which local profile a tab opens.

That query parameter is not server-side persistence. Sharing the URL to another device does not transfer the profile definition.

Overview and Continuum fetch independently. A failure in one does not discard the latest valid result from the other. Polling cycles do not overlap and stale requests are aborted.

## Responsive and kiosk design

The Area of Interest uses a responsive grid and wrapping terminal-style metrics. Narrow cards stack metric rows instead of introducing internal horizontal scroll.

Kiosk/fullscreen mode reduces secondary chrome while retaining node identity, explicit card state, CPU/memory when available and evidence/attention information. Reduced-motion preferences are respected.

## Current connectivity limitation

The current Continuum read model does not project canonical link availability into a form Live can display as a connection target. Live therefore does not run ping or probing by itself.

The desired direction is:

~~~text
observation producer
    -> canonical reachability evidence
    -> DServer read model
    -> DATUM Live connection target
~~~

## Sources

- [Live entry point](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/console/src/live/main.ts)
- [Live view](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/console/src/live/live-view.ts)
- [Live profile model](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/console/src/live/live-profile.ts)
- [node picker](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/console/src/live/live-node-picker.ts)
- [responsive/kiosk CSS](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/console/src/live/live.css)
- [Continuum composition](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/dserver/src/core/continuum_view.rs)
