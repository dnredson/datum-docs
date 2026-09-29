# DCompile and D-Code API

This reference describes the **DATUM v1** compile and governed D-Code surfaces.

## Responsibility map

| Operation | Endpoint | Creates authority? |
|---|---|---|
| deterministic compile/lowering | `POST /api/v1/dcompile/compile` | **No** — candidate data only |
| register immutable D-Code descriptor revision | `POST /api/v1/dcode/artifacts` | Registry availability only; **not active execution authority** |
| logical artifact lookup | `GET /api/v1/dcode/artifacts/:application_id/:dserv_id` | No; fails closed if more than one revision exists |
| exact artifact revision lookup | `GET /api/v1/dcode/artifacts/:application_id/:dserv_id/:descriptor_digest` | No; reads one exact immutable revision |
| fresh execution authorization | `POST /api/v1/dcode/authorize` | Derives permission from current accepted authority; does not mutate placement |

## `POST /api/v1/dcompile/compile`

DCompile is pure, stateless and deterministic. It produces candidate canonical objects; it does not register, deploy, place, install or authorize them.

### Submission

The request schema is:

```text
datum.dcompile-submission/1
```

It contains a canonical D-Script, output D-Graph identity/revision, service mapping and optional D-Code service descriptions. Module SHA-256/size are externally produced content identity; DCompile does not receive the `.wasm` bytes themselves.

### Candidate response

The response schema is:

```text
datum.dcompile-candidate/1
```

It includes:

- `application_id`;
- server-computed `dscript_ref`;
- canonical compile mapping;
- `dcompile_request_digest`;
- generated D-Graph and `dgraph_ref`;
- ordered D-Code artifact candidates;
- descriptor digests.

A returned D-Serv artifact can be submitted to the D-Code artifact registry without changing its semantics.

## `POST /api/v1/dcode/artifacts`

Registers one immutable canonical D-Serv artifact revision.

Registry identity is:

```text
(application_id, dserv_id, descriptor_digest)
```

Re-declaring the same descriptor digest is idempotent. A different descriptor digest for the same logical D-Serv is another immutable revision, not an in-place replacement.

Registration does **not** change active D-Map/D-Deploy authority.

## Logical versus exact lookup

Logical lookup:

```text
GET /api/v1/dcode/artifacts/:application_id/:dserv_id
```

- zero revisions → `404`;
- one revision → returns it;
- multiple revisions → `409 dserv_artifact_lookup_ambiguous`.

Exact lookup:

```text
GET /api/v1/dcode/artifacts/:application_id/:dserv_id/:descriptor_digest
```

This is the form used by governed execution. It returns the precise immutable revision or `404`; there is no implicit “latest” choice.

## `POST /api/v1/dcode/authorize`

Example request:

```json
{
  "project_id": "proj:example",
  "application_id": "app:example",
  "service_id": "probe",
  "node_id": "rpi-01"
}
```

DServer derives authorization from current authority. It checks, among other things:

1. the application has a current accepted D-Map;
2. the requested service exists in the accepted D-Graph snapshot;
3. the D-Graph requires a supported D-Node ABI;
4. the active D-Map places the service on the requested node;
5. the node declares the required ABI;
6. the exact D-Code descriptor revision bound by current authority exists and validates;
7. constraints that cannot be verified fail closed.

A successful response binds exact D-Map, D-Graph, node, artifact content and descriptor identities.

## Governed client sequence

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

No caller-selected “latest”, arbitrary artifact filename or local path decides which revision is authorized.

## Common authorization findings

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
- `stale_dcode_authorization` when an older authorization is re-verified after authority moved.

## Sources

See [Sources and provenance](sources.md) for immutable links to DCompile, the D-Code registry, authorization core and governed client.
