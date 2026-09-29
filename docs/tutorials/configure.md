# Configure DATUM v1 components

This tutorial establishes the identities and structural facts used by later deployment examples.

## Identity map

Keep these concepts separate:

```text
project_id
  └─ operational/control-plane scope

node_id
  └─ canonical structural D-Node identity

D-Continuum
  └─ server-derived structural view of declared D-Nodes

SmartSentinel/Sentinel identity
  └─ agent lifecycle/telemetry identity

local D-Code identity
  └─ persisted node-side identity used for governed D-Code execution
```

A heartbeat cannot create structural capacity. A local runtime identity cannot replace the DServer D-Node registry.

## 1. Set tutorial variables

```sh
export DSERVER_URL=http://127.0.0.1:8080
export PROJECT_ID=tutorial-project
export NODE_ID=tutorial-node
export APPLICATION_ID=app:tutorial
```

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

Publish it:

```sh
curl -fsS -X PUT \
  "$DSERVER_URL/api/v1/dnodes/$NODE_ID" \
  -H 'content-type: application/json' \
  --data-binary @tutorial-node.json
```

The declaration states **structural** facts. CPU/memory are declared capacity, not live free resources.

Inspect it:

```sh
curl -fsS "$DSERVER_URL/api/v1/dnodes/$NODE_ID"
```

## 3. Inspect the authoritative D-Continuum

```sh
curl -fsS \
  "$DSERVER_URL/api/v1/dcontinuum/authoritative" \
  -H "X-Datum-Project: $PROJECT_ID" \
  | tee tutorial-dcontinuum.json
```

DServer derives this project-scoped continuum from structural D-Node authority. Do not substitute generic `/api/v1/nodes` telemetry for it.

## 4. Understand structural updates

DATUM fails closed on conflicting structural declarations. If a D-Node ID already exists with different structural content, review the change explicitly rather than expecting a heartbeat or repeated PUT to silently redefine capacity/capability.

## 5. Initialize local D-Code identity when needed

Canonical D-Code execution uses a node-local persisted identity in addition to DServer structural authority.

```sh
export DNODE_ROOT="$HOME/.datum/$NODE_ID"

cargo run --locked --manifest-path DATUM/Cargo.toml \
  --bin smartsentinel-dcode-init -- \
  --node-id "$NODE_ID" \
  --dnode-root "$DNODE_ROOT"
```

This local identity does not declare the D-Node to DServer and does not prove liveness. It gives the governed node-side D-Code client a stable node identity to present against current server authority.

## 6. Resource binding for operational reconciliation

Container/native-process host mutation requires operational resource/binding state in addition to canonical placement. The reconciliation APIs refuse execution when that prerequisite is missing.

The exact resource-discovery/binding workflow depends on the node environment. The important authority rule is:

```text
accepted D-Map
    ≠ active Resource Registry binding
    ≠ finite reconciliation authorization
```

All applicable gates must agree before host mutation.

## 7. Configuration checklist

Before continuing, verify:

- DServer is reachable;
- `X-Datum-Project` identifies the intended project;
- the structural D-Node exists;
- the authoritative D-Continuum contains that node;
- the node advertises `datum-dnode/0` when D-Code is required;
- local D-Code identity is initialized when using the D-Code path;
- operational resource binding exists before expecting reconciler `--execute` to succeed.

## Next

Continue with [Model an existing service](model-existing-service.md) or [Author software artifacts](artifacts.md).
