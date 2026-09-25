# Tutorial troubleshooting

Use failures to identify **which authority boundary rejected the operation**. Avoid fixing one layer by weakening another.

## DServer does not start

### `dserver config not found`

Set an explicit path:

```sh
export DATUM_DSERVER_CONFIG_PATH="$PWD/dserver/config.tutorial.toml"
```

The process otherwise searches its documented local candidates.

### Control-state database errors

Confirm `DATUM_CONTROL_STATE_DB_PATH` points to a writable tutorial location:

```sh
export DATUM_CONTROL_STATE_DB_PATH="$PWD/.local/datum-control-plane.db"
```

Do not delete retained state as a generic cure for validation errors: proposals, acceptances and other authority records are intentionally durable. Use a disposable tutorial database when you genuinely want a clean environment.

## D-Node declaration fails

### Path/body node mismatch

For:

```text
PUT /api/v1/dnodes/tutorial-node
```

the JSON `node_id` must also be `tutorial-node`.

### `dnode_structural_conflict`

A node with that ID already exists with different structural platform/capacity/ABI data. The v0.1 registry does not silently edit structural facts in place. Review the change and use the explicit remove/redeclare lifecycle if that is genuinely intended.

### Invalid ABI

The current canonical D-Code ABI is `datum-dnode/0`. A made-up `datum-dnode/1` capability is not accepted merely because the string is syntactically non-empty.

## Authoritative D-Continuum is unavailable

If no structural D-Node has been declared, DServer cannot derive an authoritative `datum.dcontinuum/1` for placement. Declare at least one valid D-Node first.

## ServiceArtifact creation fails

### `at least one control_plane.target_nodes or target_stages entry is required`

The artifact must declare an eligibility scope. For this tutorial use:

```json
"target_nodes": ["tutorial-node"],
"target_stages": []
```

### `target_stage_constraint_unverifiable`

This arises later in D-Deploy if the artifact declares non-empty `target_stages`. Current canonical D-Continuum authority has no node-stage mapping, so D-Deploy rejects the constraint fail-closed. Use structural node eligibility for the current basic flow instead of pretending self-reported stage metadata is authoritative.

### Container fields rejected

Check `runtime.kind == "container"`, a non-empty container name/image, supported `image_source_kind`, valid port protocols and a supported execution probe.

### `resolved_image_identity is server-owned`

Do not paste resolved image identity into ordinary create/update requests. Use the explicit image-identity resolve endpoint so DServer owns the resolution record and related generation/digest transition.

### WASM decision fields rejected

The current ServiceArtifact policy requires an explicit decision module/function and requires explicit invocation while forbidding imports, effects and auto-execution in this management-decision surface.

## D-Deploy planning fails

### `artifact_not_found`

The canonical D-Graph service has no resolvable project-scoped ServiceArtifact. Register exactly one artifact whose `service_id`, `artifact_id` or declared alias resolves that canonical service.

### `artifact_ambiguous`

More than one artifact resolves the same D-Serv. D-Deploy refuses to guess which artifact is intended. Remove the ambiguity instead of relying on ordering.

### `node_not_eligible` / no feasible placement

Check the ServiceArtifact `target_nodes`, D-Node ABI capabilities, per-service CPU/memory requirements, node structural capacity and capacity already committed by other active applications.

The deterministic planner uses structural facts, not current telemetry. Freeing live RAM does not fix a declared structural-capacity mismatch.

### D-Graph validation findings

Common causes include duplicate IDs, revision 0, a dangling D-Call endpoint, invalid `datum-dnode/0` requirement or zero resource requirements. See [Create a valid D-Graph](dgraph.md).

## Acceptance fails after planning succeeded

This can be correct behavior.

A pending proposal is not a reservation against a frozen world. Acceptance rechecks load-bearing current authority. Failures can include:

- the authoritative D-Node registry changed after planning;
- another accepted deployment changed project capacity commitments;
- the currently active D-Map revision no longer matches what the proposal expected;
- ServiceArtifact eligibility/content changed;
- the submitted proposal digest does not match the immutable proposal.

Do not bypass this by constructing a D-Map manually. Re-plan against current state.

## Accepted D-Map exists, but no container appears

That is not evidence that D-Deploy failed. D-Deploy acceptance establishes placement authority; runtime reconciliation is a distinct plane.

Check whether the node has the operational resource/binding/context needed by `smartsentinel-operational-reconcile`, whether execution authorization/pinning prerequisites are satisfied, and whether you intentionally requested `--execute`. The base tutorial does not claim a turnkey 114E live runtime bridge yet.

## D-Code descriptor registration fails

### Content identity mismatch

`dcode.uri`, `dcode.sha256` and `dcode.content_id` must identify the same content. The URI form is:

```text
datum-blob://sha256/<64 lowercase hex>
```

Do not hash the filename/path; hash the actual WASM bytes.

### ABI failure

The current supported descriptor ABI is `datum-dnode/0` with the required export set:

```text
memory
datum_abi_version
datum_alloc
datum_dealloc
datum_handle
```

`allowed_imports` must be empty in v0.1.

### Safety/state-model failure

The zero-import model requires the host capability booleans to be false. The current artifact supports `state_model = "stateless"` and `instantiation = "fresh_instance_per_invocation"`.

### Conflict on the same application/service

The v0.1 D-Code registry is immutable per `(application_id, dserv_id)`. Changing artifact content at the same key is not implemented as an in-place version transition.

## D-Code install fails

The local installer recomputes the module SHA-256 and refuses a declared digest mismatch. Rebuild the descriptor from the exact bytes you are installing; do not alter one side merely to make the strings agree.

The module store also verifies already-present content rather than trusting a digest-shaped filename.

## Governed D-Code invocation fails

Check all four identities together:

1. local D-Node identity;
2. active D-Map placement for the service;
3. DServer canonical D-Serv artifact metadata/digest;
4. locally installed module bytes.

A stale placement or stale artifact must fail instead of executing historical authority.

The governed invocation path intentionally does not accept a normal caller-chosen `--node-id` override.

## Service is running but readiness is `not_ready`

Running software and canonical readiness are different facts. D1 readiness requires fresh DMonitor evidence correlated to exact current placement/runtime authority. Generic SmartSentinel telemetry is not automatically canonical DServ realization evidence.

Check:

```sh
curl -fsS \
  "$DSERVER_URL/api/v1/dmonitor/readiness/$PROJECT_ID/$APPLICATION_ID"
```

Then inspect the finding codes and the placement-level reason rather than assuming runtime health from a container/process check.

For DForward `any_element` dependencies, query the D2 endpoint for the consumer node and inspect provider-resolution/readiness findings separately.

## When not to “fix” the tutorial

Do not paper over a missing implementation by adding undocumented fields, treating `/api/v1/dmap` as canonical D-Deploy authority, using `/api/v1/nodes` as the structural D-Node registry, or equating Sentinel liveness with DMonitor canonical readiness.

If a required step is genuinely absent at Phase 114D2, preserve that boundary in the documentation and extend the tutorial only when the corresponding implementation/evidence lands.

## Source trail

See [sources and provenance](../reference/sources.md), [core control-plane API](../reference/core-api.md), [complete HTTP API](../reference/http-api.md) and the source links embedded throughout the preceding tutorial pages.