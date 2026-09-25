# Canonical contracts

This page is a field-oriented map of the main canonical contracts at the Phase 114D2 baseline. It summarizes source types and invariants; the pinned Rust implementation remains authoritative for exact serialization/validation behavior.

## Common design rules

Several contracts share these properties:

- explicit `schema` version strings;
- non-empty logical identities;
- monotonic/local `revision` values where the object is revisioned;
- canonical JCS + SHA-256 content identity;
- set-like arrays normalized for digest computation where ordering is not semantic;
- fail-closed validation rather than silent repair;
- desired-state contracts do not absorb runtime health/telemetry fields.

## `datum.dgraph/1`

Canonical application-plane graph.

```text
CanonicalDGraphV1
  schema
  application_id
  dgraph_id
  revision
  services[]
  calls[]
```

### D-Serv

```text
CanonicalDServV1
  service_id
  execution_requirement
    dnode_abi
  resource_requirement
    cpu_cores
    memory_bytes
```

At v0.1, `dnode_abi` must be `datum-dnode/0`. Resource requirements are static declared requirements, not measurements.

### D-Call

```text
CanonicalDCallV1
  call_id
  source_service_id
  target_service_id
```

Source/target must reference declared D-Servs. Cycles and self-calls are valid. There are deliberately no placement, network-address or port fields.

## `datum.dcontinuum/1`

Structural continuum contract.

```text
CanonicalDContinuumV1
  schema
  project_id
  dcontinuum_id
  revision
  nodes[]
  links[]
```

### D-Node

```text
CanonicalDNodeV1
  node_id
  platform
    os
    architecture
  capacity
    cpu_cores
    memory_bytes
  capabilities
    dnode_abi_versions[]
```

Capacity is declared/static. `dnode_abi_versions` is semantically a set. Live CPU utilization/free memory never belongs in this canonical type.

### D-Link

```text
CanonicalDLinkV1
  link_id
  from_node_id
  to_node_id
```

Endpoints must reference declared nodes.

## `datum.dmap/1`

Canonical placement contract for D-Servs.

```text
CanonicalDMapV1
  schema
  project_id
  application_id
  dmap_id
  revision
  dgraph_ref {id, revision, digest}
  dcontinuum_ref {id, revision, digest}
  placements[]
    service_id
    node_id
```

Important invariants include exact referenced contract identity/digest, application/project scope agreement, complete service placement, supported D-Node ABI, per-service feasibility and aggregate declared node CPU/memory feasibility.

DMap/1 is a placement result/contract. Validation does not itself choose an optimal node.

## `datum.dforward/1`

Logical IoT middleware composition.

```text
CanonicalDForwardV1
  schema
  project_id
  dforward_id
  revision
  diots[]
  external_endpoints[]
  chains[]
  support_jobs[]
```

### DIoT

```text
CanonicalDIoTV1
  diot_id
  diot_kind
  artifact_requirement
    artifact_id
  provides[]
    interface
  requires[]
    interface
    scope = same_element | any_element
```

### External endpoint

```text
CanonicalExternalEndpointV1
  endpoint_id
  direction = input | output
  interface
```

### Chain/hop

```text
CanonicalDForwardChainV1
  chain_id
  hops[]
    from
    to
    interface
```

Hop endpoints must be declared and interfaces compatible. External endpoint direction/interface is validated against adjacency.

### Support job

```text
CanonicalDForwardSupportJobV1
  job_id
  artifact_requirement.artifact_id
  desired_state
```

Unknown fields are denied by the canonical DForward wire types.

## `datum.dmap/2`

Extended placement authority connecting application, continuum and DForward.

```text
CanonicalDMapV2
  schema
  project_id
  application_id
  dmap_id
  revision
  dgraph_ref {id, revision, digest}
  dcontinuum_ref {id, revision, digest}
  dforward_ref {id, revision, digest}
  placements[]
  diot_placements[]
  dcall_realizations[]
  external_port_bindings[]
```

### D-Serv placement

```text
DServPlacementV2
  service_id
  node_id
```

### DIoT artifact binding

```text
DIoTArtifactBindingV2
  artifact_id
  descriptor_digest
  content_digest? 
```

### DIoT placement

```text
DIoTPlacementV2
  placement_id
  diot_id
  node_id
  artifact_binding
```

### D-Call realization

```text
DCallRealizationV2
  call_id
  realization_kind   # v0.1: via_diot_pubsub
  diot_placement_id
  interface
  channel
```

Channels containing MQTT wildcard `+` or `#` are rejected by v0.1 validation.

### External port binding

```text
ExternalPortBindingV2
  service_id
  port
  endpoint_id
  diot_placement_id?
  interface
  channel
```

## `datum.dserv-artifact/1`

Canonical host-independent D-Code descriptor.

```text
CanonicalDServArtifactV1
  schema
  artifact_id
  version
  application_id
  dserv_id
  dcode
  abi
  ports
  limits
  safety
  state_model
  instantiation
  constraints
  qos
  provenance
  probes
  signature_ref?
```

### D-Code content identity

```text
DServArtifactDCodeV1
  uri               # datum-blob://sha256/<digest>
  sha256
  content_id         # sha256:<digest>
  size_bytes
```

The URI digest, `sha256` and `content_id` must agree.

### ABI

```text
DServArtifactAbiV1
  name
  version
  required_exports[]
  allowed_imports[]
```

For v0.1 the ABI resolves to `datum-dnode/0`. The required export semantic set is:

```text
memory
datum_abi_version
datum_alloc
datum_dealloc
datum_handle
```

`allowed_imports` must be empty.

### Ports

```text
DServArtifactPortsV1
  inputs[]  {port, payload_schema, external}
  outputs[] {port, payload_schema, external}
```

### Limits

```text
fuel_per_invocation
timeout_ms
max_memory_pages
max_message_bytes
max_emits_per_invocation
```

All must be non-zero in v0.1.

### Safety/state invariants

The zero-import v0.1 model requires filesystem/network/host-command/Docker/side-effect safety booleans to be false. `state_model` is `stateless`; `instantiation` is `fresh_instance_per_invocation`.

## `datum.dmonitor-observation/1`

One canonical observation artifact.

```text
CanonicalDMonitorObservationV1
  schema
  observation_id
  project_id?
  node_id
  monitor_instance_id
  sequence
  observed_at_utc
  cycle_id?
  collector
  subject
  health
  facts
```

`sequence` is 1-based and monotonic per monitor-instance epoch. `facts` is JSON evidence payload but must not be used to smuggle desired-state authority.

### Health enum

```text
unknown
healthy
degraded
unhealthy
```

Health is observation-time condition, independent of freshness.

### Contract reference

```text
DMonitorContractRefV1
  id
  revision
  digest
```

### Runtime-binding reference

```text
DMonitorRuntimeBindingRefV1
  binding_id
  binding_revision
  descriptor_digest
```

This separate type reflects the fact that runtime binding is operational authority, not a desired-state canonical contract.

### Typed subjects

| `kind` | Key correlation fields |
|---|---|
| `dnode` | `node_id` |
| `runtime_process` | `node_id`, opaque `runtime_ref` |
| `dserv_realization` | project/application/service/node + optional DMap ref |
| `dcode_execution` | project/application/service/node + optional D-Code evidence digest |
| `dcall_delivery` | project/application/call + optional grant/delivery evidence refs |
| `diot_realization` | project/application/DIoT/placement/node + optional DMap/DForward/runtime-binding refs |
| `network_reachability` | node + operational target |
| `unbound` | node + optional description |

## D-Deploy proposal and acceptance

These are governance records rather than application/placement contracts themselves.

### `datum.ddeploy-proposal/1`

A proposal includes identity/scope, source (`operator`, `deterministic`, `ai`), creation time, optional expected active DMap revision, exact source refs and candidate placements. It remains immutable after creation.

### `datum.ddeploy-acceptance/1`

Acceptance records the explicit transition that creates/activates authoritative D-Map state. The caller-supplied `accepted_by` field is audit provenance in the current prototype, not a cryptographically authenticated operator identity.

## Server-owned operational record: DIoT runtime binding

Not a `datum.*` desired-state schema, but important enough to document beside the contracts:

```text
DIoTRuntimeBindingV1
  binding_id
  binding_revision
  project_id
  application_id
  placement_id
  diot_id
  node_id
  dmap_id/revision/digest
  dforward_id/revision/digest
  artifact_id
  execution_generation
  execution_projection_digest
  transport
  broker_uri
  registered_at_utc
  descriptor_digest
```

All identity/authority fields except the concrete broker URI are derived from current accepted authority during registration.

## Derived result schemas

These schemas describe server-derived decisions, not desired-state authority:

| Schema | Meaning |
|---|---|
| `datum.dmonitor-readiness/1` | D1 placement/application readiness |
| `datum.dforward-dependency-readiness/1` | D2 `any_element` dependency readiness |

See [Readiness APIs](readiness-api.md) for response semantics/findings.

## Sources

[DGraph](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/agent/canonical_dgraph.rs), [DContinuum](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/agent/canonical_dcontinuum.rs), [DMap/1](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/agent/canonical_dmap.rs), [DForward](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/agent/canonical_dforward.rs), [DMap/2](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/agent/canonical_dmap_v2.rs), [D-Serv artifact](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/dserv_artifact.rs), [DMonitor observation](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/agent/canonical_dmonitor.rs), [D-Deploy](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/ddeploy.rs), [DIoT runtime binding](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/diot_runtime_binding.rs).
