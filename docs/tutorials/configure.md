# Configure the control plane and identities

DATUM deliberately uses different identities for different claims. This tutorial configures the minimum set needed to reason about a basic deployment without collapsing structural authority, agent configuration and local execution identity into one object.

## Identity map

| Identity/configuration | Owner | What it proves |
|---|---|---|
| `project_id` / `X-Datum-Project` | Request/control-plane scope | Which project's project-scoped state is being addressed. |
| Structural D-Node declaration | DServer | The logical node exists structurally with declared platform, capacity and supported D-Node ABI versions. |
| Authoritative D-Continuum | DServer-derived | Current structural node inventory stamped for one project scope. |
| `DATUM/config.toml` agent `node_id` | Agent configuration | Which node the agent configuration intends to represent; not by itself canonical D-Node authority. |
| D-Code local identity | Node-local file | Which logical D-Node a governed D-Code installation claims to be at invocation time. |
| Sentinel registration/lease | Sentinel subsystem | Operational agent registration/liveness domain; deliberately not the structural D-Node registry. |

## 1. Choose tutorial identities

```sh
export DSERVER_URL=http://127.0.0.1:8080
export PROJECT_ID=tutorial-project
export NODE_ID=tutorial-node
export APPLICATION_ID=app:tutorial
```

The project and application are not the same identity. The D-Graph is application-plane and deliberately contains `application_id`, not `project_id`.

## 2. Declare a structural D-Node

Create `tutorial-node.json`:

```json
{
  "node_id": "tutorial-node",
  "platform": {
    "os": "linux",
    "architecture": "amd64"
  },
  "capacity": {
    "cpu_cores": 4,
    "memory_bytes": 4294967296
  },
  "capabilities": {
    "dnode_abi_versions": ["datum-dnode/0"]
  }
}
```

Declare it:

```sh
curl -fsS -X PUT \
  "$DSERVER_URL/api/v1/dnodes/$NODE_ID" \
  -H 'content-type: application/json' \
  --data-binary @tutorial-node.json
```

The path `node_id` must match the body `node_id`. An identical redeclaration is idempotent. Changing the existing node's structural facts in place is not the current v0.1 model; remove/redeclare is the explicit path for a genuine structural change.

### What these fields mean

`platform` is declared structure, not an observed kernel probe. `capacity` is static structural capacity used by placement feasibility, not current free CPU/RAM. `dnode_abi_versions` is the set of host-independent D-Node ABI versions the node can host; Phase 114D2 recognizes `datum-dnode/0` for canonical D-Code.

## 3. Inspect the structural registry

```sh
curl -fsS "$DSERVER_URL/api/v1/dnodes"
curl -fsS "$DSERVER_URL/api/v1/dnodes/$NODE_ID"
```

Notice that these are `/dnodes` routes. Earlier `/nodes` routes in DServer belong to a different snapshot/legacy subsystem and must not be substituted for structural D-Node authority.

## 4. Ask DServer for the authoritative D-Continuum

```sh
curl -fsS \
  "$DSERVER_URL/api/v1/dcontinuum/authoritative" \
  -H "X-Datum-Project: $PROJECT_ID" \
  | tee tutorial-dcontinuum.json
```

DServer builds this `datum.dcontinuum/1` from its own structural registry. The `project_id` is a wire scoping label over the server-owned global node set; it is not a new per-project physical-node ownership model.

For the basic deterministic `/ddeploy/plan` workflow you do not send this D-Continuum back: the planner derives the authoritative D-Continuum server-side. Fetching it is nevertheless useful for understanding and debugging what placement sees.

## 5. Understand the DATUM agent config

The repository's `DATUM/config.toml` contains an `[agent]` section with a node ID and many operational collectors/outputs. It also contains HTTP output and dispatch settings from the broader SmartSentinel/DATUM runtime.

Do not treat that TOML as the canonical D-Node declaration. If you configure `[agent].node_id = "tutorial-node"`, that is a node-side operational configuration choice; DServer's structural registry remains the source used to derive the canonical D-Continuum.

## 6. Initialize local D-Code identity when needed

Canonical governed D-Code invocation intentionally does not accept an arbitrary per-call `--node-id`. Instead the node installation has a local identity file.

```sh
export DNODE_ROOT="$HOME/.datum/$NODE_ID"

cargo run --locked --manifest-path DATUM/Cargo.toml \
  --bin smartsentinel-dcode-init -- \
  --node-id "$NODE_ID" \
  --dnode-root "$DNODE_ROOT"
```

The node ID written here must match the structural D-Node identity that DServer will authorize for the service. A different root can represent a different logical D-Node even on the same physical host.

This identity is deliberately separate from Sentinel registration/lease. It exists so governed D-Code execution can bind authorization to the installation's own persisted local identity instead of trusting a command-line claim.

## 7. Persistence and restart behavior

D-Node structural state and several other canonical/control-plane domains are stored in the SQLite database selected by `DATUM_CONTROL_STATE_DB_PATH`. Restarting DServer should therefore not be treated as permission to recreate or silently replace accepted authority.

The state layer uses current/history tables and fails closed on unsupported/corrupt retained state detected by domain loaders.

## Next step

You now have a project scope, a structural D-Node, a server-derived D-Continuum and—if you plan to run D-Code—a node-local execution identity. Continue with [authoring software artifacts](artifacts.md).

## Source trail

- [D-Node registry API](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/api/dnode_registry.rs)
- [D-Node registry core](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/dnode_registry.rs)
- [D-Continuum contract](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/agent/canonical_dcontinuum.rs)
- [DATUM example configuration](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/config.toml)
- [D-Code local identity initializer](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/bin/smartsentinel-dcode-init.rs)