# DATUM Live tutorial

DATUM Live is the read-only, continuously refreshed operational display for DATUM v1. Use it when you want a screen that can remain open all day without turning the browser into a second control plane.

## 1. Build the frontend

~~~sh
git clone https://github.com/dnredson/datum.git
cd datum
git checkout --detach 3605845b7933195e470c9a13473fbc05432c4a26
cd console
npm ci
npm test
DATUM_CONSOLE_URL="https://server.datumlab.net" npm run build
~~~

The build contains:

~~~text
dist/index.html   -> DATUM Console
dist/live.html    -> DATUM Live
~~~

The hostname above is the current datumlab deployment example, not a required DATUM hostname.

## 2. Serve Console and Live separately

A practical layout serves the same static build from two virtual hosts:

~~~text
server.datumlab.net -> index.html
live.datumlab.net   -> live.html
~~~

Live can additionally be restricted to GET/HEAD at the reverse proxy.

## 3. Create a Live profile and Area of Interest

Profiles are browser-local. Use **Manage nodes** to select D-Nodes from the global Continuum.

A project filter means that accepted placements from that project reference the node; it does not mean the node belongs to the project. Live does not infer node type from names such as fog-01 or cloud-01.

## 4. Make a structural D-Node visible

The picker is backed by the structural D-Node Registry:

~~~text
GET /api/v1/dnodes
PUT /api/v1/dnodes/:node_id
~~~

Structural capacity is declared capacity, not current CPU/memory usage.

## 5. Publish host resource observation

Host CPU/memory/swap comes from a Resource Registry observation bound to the D-Node.

Build the observation-only discovery binary:

~~~sh
cd DATUM
cargo build --release --bin smartsentinel-resource-discovery
~~~

Collect and publish one report:

~~~sh
smartsentinel-resource-discovery \
  --config /path/to/smartsentinel.toml \
  --out /tmp/datum-resource.json

curl -fsS \
  -X POST \
  -H 'Content-Type: application/json' \
  -H 'X-Datum-Project: <project_id>' \
  --data-binary @/tmp/datum-resource.json \
  http://127.0.0.1:8081/api/v1/resources/discovery
~~~

Discovery is observation-only and does not automatically assign a resource to a D-Node.

## 6. Bind the resource explicitly

After identifying the exact resource_id:

~~~sh
curl -fsS \
  -X POST \
  -H 'Content-Type: application/json' \
  -H 'X-Datum-Project: <project_id>' \
  --data '{
    "node_id": "<node_id>",
    "transition_kind": "initial_assignment"
  }' \
  "http://127.0.0.1:8081/api/v1/resources/<resource_id>/binding"
~~~

Repeated discovery of the same canonical resource updates its observation while preserving the binding. For a continuous display, run discovery/publish periodically with your service manager or agent lifecycle.

## 7. Verify the Continuum first

~~~sh
curl -fsS http://127.0.0.1:8081/api/v1/operations/continuum
~~~

For a node, distinguish:

- structure — declared platform/capacity;
- resource_observation — host-level CPU/memory/swap;
- accepted_placements — current placement references;
- observations — placement-scoped DMonitor interpretation/evidence.

If resource_observation is absent, fix discovery/binding instead of adding a frontend workaround.

## 8. Read the card correctly

**Observed** means observation exists; it does not mean Healthy.

Card tone can reflect existing active alert severity or DMonitor convergence/health/freshness. CPU/memory values and browser-defined sample age do not create warning/danger thresholds.

A host can legitimately have resource observation while accepted placements and placement-scoped DMonitor evidence are empty.

## 9. Use Attention / Alarms and Recent Activity

Node correlation exists only when the canonical alert/event subject carries node_id. Live does not guess a physical node from project/application identity.

## 10. Use kiosk/fullscreen mode

The responsive layout wraps CPU/memory metric rows instead of creating horizontal scroll and keeps node identity/state visible on small displays. Test the actual display size when deciding how many nodes to pin.

## 11. Know current limitations

Live profiles are browser-local; cross-device shared dashboards are not implemented yet.

Live also does not currently provide a canonical "connection up/down" target for Continuum links. Do not add a browser ping and treat its timeout as DATUM authority; connectivity should arrive through canonical evidence/read projection.

## Sources

- [Live view](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/console/src/live/live-view.ts)
- [Live profiles](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/console/src/live/live-profile.ts)
- [node picker](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/console/src/live/live-node-picker.ts)
- [Continuum API](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/dserver/src/api/continuum_view.rs)
- [Resource Registry](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/dserver/src/core/resource_registry.rs)
- [resource binding](https://github.com/dnredson/datum/blob/3605845b7933195e470c9a13473fbc05432c4a26/dserver/src/core/resource_binding.rs)
