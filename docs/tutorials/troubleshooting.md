# Tutorial troubleshooting

Use failures to identify **which authority boundary rejected the operation**. Avoid fixing one layer by weakening another.

## DServer does not start

### `dserver config not found`

Set an explicit path:

```sh
export DATUM_DSERVER_CONFIG_PATH="$PWD/dserver/config.tutorial.toml"
```

### Control-state database errors

Use a writable, isolated path for tutorials:

```sh
export DATUM_CONTROL_STATE_DB_PATH="$PWD/.local/datum-control-plane.db"
```

Do not delete retained state as a generic cure for validation errors. Use a disposable tutorial database when you genuinely want a clean environment.

## D-Node declaration fails

### Path/body node mismatch

For:

```text
PUT /api/v1/dnodes/tutorial-node
```

the JSON `node_id` must also be `tutorial-node`.

### `dnode_structural_conflict`

A node with that ID already exists with different structural platform/capacity/ABI data. DATUM v1 does not silently redefine structural authority. Review the change and use the explicit structural lifecycle intended by the implementation.

### Invalid ABI

The current canonical D-Code ABI is `datum-dnode/0`. A made-up ABI value is not accepted merely because it is syntactically non-empty.

## D-Continuum is unavailable or incomplete

DServer derives the authoritative D-Continuum from structural D-Node declarations. Declare the required nodes first and verify:

```sh
curl -fsS \
  "$DSERVER_URL/api/v1/dcontinuum/authoritative" \
  -H "X-Datum-Project: $PROJECT_ID"
```

## ServiceArtifact creation fails

### Missing eligibility scope

A ServiceArtifact must declare an allowed scope. For the simple tutorial:

```json
"target_nodes": ["tutorial-node"],
"target_stages": []
```

### `target_stage_constraint_unverifiable`

The current canonical D-Continuum does not provide authoritative node-to-stage mapping. Non-empty `target_stages` constraints therefore fail closed in canonical planning. Use explicit structural node eligibility when following the v1 tutorial.

### Container fields rejected

Check:

- `runtime.kind == "container"`;
- non-empty container name and image;
- supported `image_source_kind`;
- valid port protocols;
- supported execution/health/availability probes.

### `resolved_image_identity is server-owned`

Do not paste a resolved OCI identity into ordinary artifact create/update requests. Use:

```text
POST /api/v1/service-artifacts/:artifact_id/image-identity/resolve
```

DServer owns the resolution record and associated execution projection/generation transition.

## D-Deploy planning fails

### `artifact_not_found`

The D-Graph service has no uniquely resolvable project-scoped ServiceArtifact. Register a matching artifact.

### `artifact_ambiguous`

More than one ServiceArtifact resolves the same D-Serv. D-Deploy refuses to choose by ordering. Remove the ambiguity.

### No feasible placement

Check:

- `target_nodes` eligibility;
- D-Node ABI capabilities;
- per-service CPU/memory requirements;
- structural node capacity;
- capacity already committed by accepted deployments.

The deterministic planner uses structural facts, not current free RAM/CPU telemetry.

## Acceptance fails after planning succeeded

This can be correct. Acceptance revalidates current authority and can reject a formerly valid proposal when:

- structural D-Node facts changed;
- project capacity commitments changed;
- expected active D-Map revision became stale;
- ServiceArtifact eligibility/content changed;
- proposal digest does not match.

Re-plan against current state instead of manually constructing placement authority.

## Accepted D-Map exists, but no process/container appears

D-Deploy acceptance establishes placement authority. Runtime realization is separate.

Check:

- operational resource binding;
- node-specific operational slice;
- required-complete artifact identity/pinning;
- finite reconciliation authorization;
- local policy;
- whether `--execute` was intentionally requested.

A turnkey packaged deployment orchestrator is not implemented yet; the current path intentionally exposes these governance boundaries.

## D-Code registration/lookup issues

### Content identity mismatch

`dcode.uri`, `dcode.sha256` and `dcode.content_id` must identify the same bytes.

### ABI failure

The supported ABI is `datum-dnode/0` and the required exports are:

```text
memory
datum_abi_version
datum_alloc
datum_dealloc
datum_handle
```

The current D-Code runtime accepts no host imports.

### Multiple revisions exist

This is valid. The registry identity is:

```text
(application_id, dserv_id, descriptor_digest)
```

Multiple immutable descriptor revisions may coexist for the same logical D-Serv. Therefore the logical GET can fail with `409 dserv_artifact_lookup_ambiguous`; governed execution uses the exact descriptor digest selected by current authority.

Registration of a new revision does not activate it.

## D-Code install fails

The local installer recomputes module SHA-256 and refuses mismatched bytes. Rebuild the descriptor from the exact WASM you are installing rather than changing a digest merely to make strings agree.

Automatic D-Code module distribution is not implemented yet; module bytes must reach the node through a separate operational process before governed invocation.

## Governed D-Code invocation fails

Check these identities together:

1. local D-Node identity;
2. active D-Map placement;
3. exact descriptor digest bound by current authority;
4. locally installed module content digest;
5. currently declared D-Node ABI support.

A stale placement or stale revision must fail closed instead of executing authority that is no longer current.

## Service is running but readiness is `not_ready`

Running software and canonical readiness are different facts. D1 readiness requires fresh evidence correlated to exact current authority.

```sh
curl -fsS \
  "$DSERVER_URL/api/v1/dmonitor/readiness/$PROJECT_ID/$APPLICATION_ID"
```

Inspect the finding codes rather than inferring readiness from Docker/process status.

For DForward `any_element` dependencies, query the D2 dependency-readiness endpoint for the consumer node and inspect provider-specific findings separately.

## Migration cleanup fails

Cleanup is not ordinary rollback. A vacated source node can receive a dedicated governed cleanup directive and requires cleanup-specific authorization before host mutation.

Use the current `--cleanup` path only for derived source-cleanup directives. Do not reuse ordinary reconcile/rollback semantics to remove arbitrary services.

## When something is genuinely missing

Do not invent fields, bypass current authority through an unrelated or auxiliary route, or reinterpret telemetry as canonical state. If a required capability is not implemented yet, keep that boundary explicit and document it as planned.

## Source trail

See [sources and provenance](../reference/sources.md), [core control-plane API](../reference/core-api.md) and [HTTP API catalog](../reference/http-api.md).
