# DCompile and D-Code API

This reference describes the production compile and governed D-Code surfaces at the Phase 119I baseline.

## Responsibility map

| Operation | Endpoint | Creates authority? |
|---|---|---|
| deterministic compile/lowering | `POST /api/v1/dcompile/compile` | **No** — candidate data only |
| register immutable D-Code descriptor revision | `POST /api/v1/dcode/artifacts` | Registry availability only; **not active execution authority** |
| logical artifact lookup | `GET /api/v1/dcode/artifacts/:application_id/:dserv_id` | No; compatibility/debug, fails 409 if ambiguous |
| exact artifact revision lookup | `GET /api/v1/dcode/artifacts/:application_id/:dserv_id/:descriptor_digest` | No; reads one exact immutable revision |
| fresh execution authorization | `POST /api/v1/dcode/authorize` | Derives permission from current accepted authority; does not mutate placement |

## `POST /api/v1/dcompile/compile`

DCompile is pure, stateless and deterministic. The handler touches no control-state DB, D-Code registry, D-Deploy state, D-Node registry, filesystem or network beyond serving the HTTP request itself.

A successful response means:

> deterministic candidate generated

It does **not** mean:

> registered, deployed, accepted, active, placed, installed or authorized.

### Submission schema

Outer schema:

```text
datum.dcompile-submission/1
```

Fields:

```json
{
  "schema": "datum.dcompile-submission/1",
  "dscript": { "...": "datum.dscript/1" },
  "output_dgraph_id": "dgraph:example",
  "output_dgraph_revision": 1,
  "services": [
    {
      "service_id": "probe",
      "function_ids": ["read", "transform"],
      "resource_requirement": {
        "cpu_cores": 1,
        "memory_bytes": 134217728
      }
    }
  ],
  "dcode_services": [
    {
      "service_id": "probe",
      "artifact_id": "dserv:probe",
      "version": "0.1.0",
      "sha256": "<64 lowercase hex>",
      "size_bytes": 247,
      "ports": {"inputs": [], "outputs": []},
      "limits": {
        "fuel_per_invocation": 5000000,
        "timeout_ms": 200,
        "max_memory_pages": 4,
        "max_message_bytes": 65536,
        "max_emits_per_invocation": 8
      }
    }
  ]
}
```

The outer submission deliberately contains no caller-supplied `dscript_ref`, no `dgraph_ref`, no project/placement/D-Map/proposal fields and no random/timestamp identity. DServer computes the references it can establish honestly.

!!! important "Module bytes are not posted to DCompile"
    `dcode_services[].sha256` and `size_bytes` describe externally produced module content. DCompile does not receive or byte-verify the `.wasm` file. It deterministically constructs the descriptor candidate around the declared content identity. Byte integrity is verified at D-Node installation/load/execution boundaries.

### Candidate response schema

Response schema:

```text
datum.dcompile-candidate/1
```

The response contains:

- `application_id`;
- server-computed `dscript_ref`;
- canonicalized full compile `mapping`;
- `dcompile_request_digest`;
- generated `dgraph`;
- server-computed `dgraph_ref`;
- ordered `dcode_artifacts[]`;
- `dcode_artifact_authority` convenience map.

Each artifact result contains:

```json
{
  "service_id": "probe",
  "artifact": { "schema": "datum.dserv-artifact/1", "...": "..." },
  "descriptor_digest": "sha256:..."
}
```

The `artifact` value is directly POST-able to `/api/v1/dcode/artifacts` without semantic transformation.

### Five identities in the response

| Identity | Ownership |
|---|---|
| D-Script digest | server-computed from submitted canonical D-Script |
| D-Compile request digest | server-computed from canonical compile mapping |
| D-Graph digest | server-computed from generated topology |
| module SHA-256 | externally declared D-Code input; not byte-verified by DCompile |
| descriptor digest | server-computed over the whole canonical D-Serv artifact |

This prevents “source”, “mapping”, “topology”, “executable bytes” and “execution descriptor” from being collapsed into one revision number.

## `POST /api/v1/dcode/artifacts`

Registers one immutable canonical D-Serv artifact revision.

Current registry identity is:

```text
(application_id, dserv_id, descriptor_digest)
```

Response:

```json
{
  "artifact_id": "dserv:probe",
  "descriptor_digest": "sha256:...",
  "inserted": true
}
```

Re-declaring the exact same digest is idempotent (`inserted: false`). A different descriptor digest for the same logical service is a new immutable revision, not an in-place replacement.

### Registration does not switch execution

This endpoint does not edit the active D-Map or the D-Deploy binding. It only makes a descriptor revision available to governed workflows.

## Logical versus exact lookup

### Logical lookup

```text
GET /api/v1/dcode/artifacts/:application_id/:dserv_id
```

Behavior:

- zero revisions → `404`;
- exactly one revision → returns it;
- two or more revisions → `409 dserv_artifact_lookup_ambiguous`.

The 409 is intentional fail-closed behavior.

### Exact lookup

```text
GET /api/v1/dcode/artifacts/:application_id/:dserv_id/:descriptor_digest
```

This is the lookup governed execution uses. It either returns the precise immutable revision or `404`; there is no “latest” resolution.

## `POST /api/v1/dcode/authorize`

Request:

```json
{
  "project_id": "proj:example",
  "application_id": "app:example",
  "service_id": "probe",
  "node_id": "rpi-01"
}
```

The server derives current authority under a stable DDeploy → DNode → DCode view. It verifies, among other things:

1. the application has a current accepted D-Map;
2. the requested service exists in the accepted D-Graph snapshot;
3. the D-Graph requires the supported D-Node ABI;
4. the active D-Map places that service on the requested node;
5. that node currently declares support for `datum-dnode/0`;
6. the exact registered artifact revision selected by current D-Deploy authority exists and validates;
7. its ABI matches;
8. any constraint that cannot be verified is failed closed rather than ignored.

Successful response fields:

```json
{
  "authorization_id": "...",
  "project_id": "...",
  "application_id": "...",
  "service_id": "...",
  "node_id": "...",
  "dmap_ref": {"id": "...", "revision": 2, "digest": "..."},
  "dgraph_ref": {"id": "...", "revision": 1, "digest": "..."},
  "dserv_artifact_id": "...",
  "dserv_artifact_digest": "<module content digest>",
  "dserv_artifact_descriptor_digest": "<whole descriptor digest>",
  "dnode_abi": "datum-dnode/0"
}
```

### Important authorization findings

Examples include:

- `dcode_application_not_active`;
- `dcode_service_not_in_dgraph`;
- `dcode_service_not_placed_on_node`;
- `dcode_execution_requirement_unsupported`;
- `dcode_node_unknown`;
- `dcode_node_abi_unsupported`;
- `dcode_artifact_not_found`;
- `dcode_artifact_abi_mismatch`;
- `dcode_artifact_invalid`;
- `dcode_artifact_stage_constraint_unverifiable`;
- `dcode_active_binding_missing`;
- `stale_dcode_authorization` on explicit re-verification of an older authorization.

## Client governed preflight

The production client sequence is:

```text
fresh authorize
    ↓
authorization.descriptor_digest
    ↓
exact descriptor GET
    ↓
request/auth/descriptor cross-check
    ↓
local module load by module digest
    ↓
isolated invocation
```

No caller-supplied `artifact_id`, local filename, `version` or “latest” preference participates in selecting the governed revision.

## Sources

- [production DCompile API](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/dserver/src/api/dcompile.rs)
- [production DCompile submission/result](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/dserver/src/core/dcompile_submission.rs)
- [D-Code HTTP API](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/dserver/src/api/dcode.rs)
- [D-Code authorization core](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/dserver/src/core/dcode_authorization.rs)
- [governed client](https://github.com/dnredson/datum/blob/c08ccc4d715d9eb76644e3f1bd7d80a7945265c4/DATUM/src/dcode/client.rs)
