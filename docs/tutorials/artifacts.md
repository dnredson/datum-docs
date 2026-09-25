# Author software artifacts

The current baseline contains two artifact families with different authority and execution roles. Learning this distinction is essential: **a `ServiceArtifact` and a canonical `datum.dserv-artifact/1` are not interchangeable representations of the same object.**

## Quick comparison

| Question | `ServiceArtifact` | `datum.dserv-artifact/1` |
|---|---|---|
| Primary role | Operational deployment/reconciliation descriptor | Canonical host-independent D-Code descriptor |
| Scope | Project-scoped in DServer | Application + D-Serv identity |
| Runtime data | Container/native-process realization, acquisition, probes, lifecycle, bindings | Content-addressed WASM, ABI, ports, limits, safety |
| Used by D-Deploy v1 today | Yes — service resolution and node eligibility | Not as a replacement for ServiceArtifact |
| Stores WASM bytes in DServer | No | No — only canonical metadata/digest identity |
| Where D-Code bytes live | Not applicable | D-Node-local content-addressed module store |

## Part A — create an operational `ServiceArtifact`

The basic deployment tutorial uses one container-shaped artifact for `hello-service`. This artifact lets current D-Deploy resolve the canonical service and determine which structural D-Nodes are eligible.

Create `hello-service-artifact.json`:

```json
{
  "schema_version": "0.2.0",
  "artifact_id": "artifact:hello-service",
  "service_id": "hello-service",
  "runtime": {
    "kind": "container",
    "container": {
      "container_name": "datum-hello-service",
      "image": "docker.io/library/hello-world:latest",
      "ports": [],
      "network": null,
      "network_aliases": [],
      "volumes": [],
      "configuration_mounts": [],
      "command": [],
      "image_source_kind": "registry"
    }
  },
  "probes": {
    "execution": {
      "kind": "docker_container_running",
      "params": {
        "container_name": "datum-hello-service"
      },
      "vantage_point": "local_host"
    },
    "health": null,
    "availability": null
  },
  "metadata": {
    "tutorial": true
  },
  "control_plane": {
    "project_id": "",
    "name": "Hello service",
    "version": "1.0.0",
    "artifact_kind": "container",
    "target_nodes": ["tutorial-node"],
    "target_stages": [],
    "dependencies": [],
    "acquisition": {
      "kind": "image",
      "source": null,
      "revision": "latest",
      "sha256": null
    },
    "lifecycle": {
      "pre_install": [],
      "install": [],
      "configure": [],
      "start": [],
      "stop": [],
      "post_install": [],
      "rollback": []
    },
    "health_checks": [],
    "wasm_decision": {
      "explicit_invocation_required": true,
      "module_id": "reconcile_service",
      "function_name": "decide",
      "host_imports_allowed": false,
      "side_effects_allowed": false,
      "safe_to_auto_execute": false,
      "max_fuel": 1000000,
      "timeout_ms": 1000
    },
    "bindings": {},
    "secret_refs": [],
    "secret_bindings": [],
    "created_at_utc": "",
    "updated_at_utc": ""
  }
}
```

!!! note "Server-owned fields"
    DServer replaces `control_plane.project_id` with the project header, fills/normalizes selected metadata, and owns `execution_generation` and `execution_projection_digest`. A client must not fabricate `runtime.container.resolved_image_identity`; image pinning has its own explicit server operation.

Register the artifact:

```sh
curl -fsS -X POST \
  "$DSERVER_URL/api/v1/service-artifacts" \
  -H "X-Datum-Project: $PROJECT_ID" \
  -H 'content-type: application/json' \
  --data-binary @hello-service-artifact.json \
  | tee registered-service-artifact.json
```

Inspect the registry:

```sh
curl -fsS \
  "$DSERVER_URL/api/v1/service-artifacts" \
  -H "X-Datum-Project: $PROJECT_ID"
```

### Why `target_nodes` matters

For current D-Deploy v1, `target_nodes` is an **eligibility constraint**. The deterministic planner filters candidate nodes against it. It never becomes placement authority: after explicit acceptance, D-Map is the placement truth.

An empty `target_nodes` set makes no node eligible for that service under the current per-node eligibility semantics.

### Why `target_stages` is empty

Do not add `target_stages` to this basic flow. The canonical D-Continuum does not contain an authoritative node-to-stage mapping at this baseline. Therefore a non-empty `target_stages` constraint is rejected fail-closed with `target_stage_constraint_unverifiable` rather than silently ignored.

### Image identity and reproducibility

The example intentionally demonstrates artifact creation, not a release-grade reproducibility claim. Registry images can be resolved/pinned through:

```text
POST /api/v1/service-artifacts/:artifact_id/image-identity/resolve
```

That operation resolves platform-specific OCI identity server-side. Runtime reconciliation may require pinned execution identity depending on the project's pinning mode. **D-Deploy acceptance itself is not proof that a container image has been pulled or started.**

## Part B — create a canonical D-Code artifact

Canonical D-Code uses `datum.dserv-artifact/1`. It binds a D-Serv to exact WASM content and the `datum-dnode/0` ABI.

### The current ABI

A v0.1 D-Code module must export exactly the semantic required set:

```text
memory
datum_abi_version
datum_alloc
datum_dealloc
datum_handle
```

The runtime requires these signatures:

```text
datum_abi_version: () -> i32        # returns 0
datum_alloc:       i32 -> i32
datum_dealloc:     (i32, i32) -> ()
datum_handle:      (i32, i32) -> i64
```

D-Code v0.1 permits **zero host imports**. No WASI filesystem, environment, clock, socket or other host import is exposed.

A minimal WAT smoke-test module can look like:

```wat
(module
  (memory (export "memory") 1)
  (global $heap (mut i32) (i32.const 1024))

  (func (export "datum_abi_version") (result i32)
    i32.const 0)

  (func (export "datum_alloc") (param $len i32) (result i32)
    global.get $heap)

  (func (export "datum_dealloc") (param i32) (param i32))

  (func (export "datum_handle") (param i32) (param i32) (result i64)
    i64.const 0)
)
```

This is an ABI teaching/smoke-test example, not a first-class DATUM SDK. The baseline does not yet ship a project scaffolder that turns arbitrary application source into a D-Code project.

Compile your real module to `build/hello.wasm`, then calculate its identity:

```sh
SHA256=$(sha256sum build/hello.wasm | awk '{print $1}')
SIZE_BYTES=$(wc -c < build/hello.wasm | tr -d ' ')
printf 'sha256=%s size=%s\n' "$SHA256" "$SIZE_BYTES"
```

Create a descriptor using those exact values:

```json
{
  "schema": "datum.dserv-artifact/1",
  "artifact_id": "dserv:app:dcode-tutorial:hello-dcode",
  "version": "0.1.0",
  "application_id": "app:dcode-tutorial",
  "dserv_id": "hello-dcode",
  "dcode": {
    "uri": "datum-blob://sha256/<SHA256>",
    "sha256": "sha256:<SHA256>",
    "content_id": "sha256:<SHA256>",
    "size_bytes": 1234
  },
  "abi": {
    "name": "datum-dnode",
    "version": "0",
    "required_exports": [
      "memory",
      "datum_abi_version",
      "datum_alloc",
      "datum_dealloc",
      "datum_handle"
    ],
    "allowed_imports": []
  },
  "ports": {
    "inputs": [
      {
        "port": "input",
        "payload_schema": "datum.tutorial.input/1",
        "external": true
      }
    ],
    "outputs": []
  },
  "limits": {
    "fuel_per_invocation": 1000000,
    "timeout_ms": 100,
    "max_memory_pages": 4,
    "max_message_bytes": 4096,
    "max_emits_per_invocation": 1
  },
  "safety": {
    "filesystem_access": false,
    "network_access": false,
    "host_command_access": false,
    "docker_access": false,
    "side_effects_allowed": false
  },
  "state_model": "stateless",
  "instantiation": "fresh_instance_per_invocation",
  "constraints": {
    "allowed_stages": []
  },
  "qos": null,
  "provenance": {
    "tutorial": true
  },
  "probes": null,
  "signature_ref": null
}
```

Replace `<SHA256>` and `size_bytes` with the actual module identity before submitting.

Register canonical metadata with DServer:

```sh
curl -fsS -X POST \
  "$DSERVER_URL/api/v1/dcode/artifacts" \
  -H 'content-type: application/json' \
  --data-binary @hello-dcode-artifact.json
```

This registry is keyed by `(application_id, dserv_id)`. In v0.1 one immutable descriptor occupies that key: byte-identical redeclaration is idempotent, while conflicting replacement fails. Artifact replacement/version transition is future work.

### Install the module bytes on the D-Node

DServer never stores or executes the WASM bytes. Install them explicitly in the D-Node-local store:

```sh
export DNODE_ROOT="$HOME/.datum/tutorial-node"

cargo run --locked --manifest-path DATUM/Cargo.toml \
  --bin smartsentinel-dcode-install -- \
  --module-path build/hello.wasm \
  --declared-sha256 "$SHA256" \
  --store-root "$DNODE_ROOT"
```

The installer verifies the actual bytes against the declared digest before atomically writing them under the content-addressed store path.

## Transitional overlap at this baseline

A service intended for governed D-Code execution still participates in the current D-Deploy v1 workflow, and that workflow resolves `ServiceArtifact` records for placement eligibility. Therefore a canonical D-Code descriptor does **not** remove the current requirement for a matching project-scoped `ServiceArtifact` when using this D-Deploy path.

That is a real boundary of the current implementation, not something the tutorial hides or smooths over.

## Source trail

- [ServiceArtifact registry](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/service_artifact_registry.rs)
- [ServiceArtifact API](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/api/service_artifacts.rs)
- [D-Deploy artifact eligibility](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/ddeploy.rs)
- [Canonical D-Serv artifact](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/dserv_artifact.rs)
- [D-Code registry API](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/api/dcode.rs)
- [D-Code ABI](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/dcode/abi.rs)
- [D-Code runtime](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/dcode/runtime.rs)
- [Local module store](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/dcode/module_store.rs)