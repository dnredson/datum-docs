# Identity, scope, revisions and exact references

DATUM deliberately avoids treating human-readable names as sufficient authority. The control plane repeatedly uses the pattern **identity + revision + digest** so a consumer can prove that it refers to the exact object/revision it expects.

## The four identity questions

When reading any DATUM record, ask four separate questions:

1. **Scope:** which project and/or application does this record belong to?
2. **Logical identity:** which semantic object is this (`service_id`, `diot_id`, `call_id`)?
3. **Realization identity:** which placement/binding/runtime realization is involved?
4. **Version identity:** which exact revision/content is referenced?

Collapsing these questions is a common source of incorrect implementations.

## `project_id` versus `application_id`

| Identifier | Primary role | Important examples |
|---|---|---|
| `project_id` | Operational/control-plane scope | D-Continuum, D-Map, DForward, DMonitor project ingestion, DIoT runtime binding |
| `application_id` | Placement-independent application identity | D-Graph, D-Map, D-Serv artifact, D-Call governance |

Canonical D-Graph intentionally carries `application_id` and **does not carry `project_id`**. D-Continuum carries `project_id`. D-Map is where the two scopes meet: it references an application graph and a project continuum and states the accepted mapping between them.

## Logical identity versus placement identity

A logical object answers *what is it?* A placement answers *which accepted realization of it, where?*

| Logical entity | Logical key | Placement/realization key |
|---|---|---|
| D-Serv | `service_id` | DMap placement `(service_id, node_id)` |
| DIoT | `diot_id` | DMap/2 `placement_id` + `node_id` |
| D-Call | `call_id` | DMap/2 D-Call realization and later route/grant |
| D-Code | `(application_id, dserv_id)` plus content identity | Invocation evidence / authorized D-Node execution |

For DIoT in particular, `diot_id` and `placement_id` must not be interchanged. Phase 114D2 evaluates provider readiness by the **exact provider placement**, not merely by logical `diot_id`.

## Canonical references

DMap/1 uses canonical references shaped as:

```text
{id, revision, digest}
```

DMap/2 uses the same semantic shape through `ContractRefV2`. DMonitor uses its own mirrored `DMonitorContractRefV1` for evidence correlation. They are separate Rust types because ownership domains are separate, but the semantic requirement is the same: an exact revision/content reference, never name-only correlation.

### Why all three fields matter

`id` answers which logical contract instance. `revision` makes monotonic/control-plane version transitions visible. `digest` binds the actual canonical content so the same ID/revision cannot silently mean different bytes/content.

A reference that matches ID but not digest is not “close enough.” Authority continuity checks fail closed.

## Canonical digest convention

Canonical contracts use deterministic JSON canonicalization and SHA-256. The common external form is:

```text
sha256:<64 lowercase hexadecimal characters>
```

Collections that are semantically sets are sorted in a deterministic copy before hashing. Reordering `services[]`, `calls[]`, nodes, placements or other declared unordered sets therefore does not create a different semantic digest.

The wire document itself does not need to be rewritten into sorted order merely to compute the digest.

## Revision semantics

A revision is meaningful only within the entity/domain that owns it.

Examples:

- D-Graph has its own `revision`.
- D-Continuum has its own structural `revision`.
- D-Map has its own accepted placement revision.
- DForward has its own `revision`.
- DIoT runtime binding has `binding_revision`.
- D-Node registry has an internal registry revision used to derive authoritative D-Continuum revision.

Never compare unrelated revision numbers as if they shared a global counter.

## D-Node identity and Sentinel identity

`node_id` is the canonical structural/runtime node identity used throughout D-Continuum, placement and observation. A Sentinel process additionally has its own registration/process identity. The two can correlate, but one does not replace the other.

A D-Node declaration proves structural facts: platform, static capacity and ABI capabilities. A Sentinel heartbeat proves an agent-lifecycle event. Neither proves what the other proves.

## D-Serv artifact identity

`datum.dserv-artifact/1` binds several related identities:

- `artifact_id` and `version` identify the descriptor at a human/control-plane level;
- `(application_id, dserv_id)` identifies which logical D-Serv executable the registry entry belongs to;
- `dcode.sha256`, `dcode.content_id` and the digest in `dcode.uri` must agree on module content;
- the canonical descriptor itself can be digested for exact metadata identity.

DServer's DCode registry stores descriptor identity, not the executable bytes. Bytes are retrieved/verified through the node-local content-addressed module store.

## D-Call authority continuity

D-Call deliberately avoids trusting caller-selected destinations. Route derivation starts from current accepted D-Graph/D-Map authority and resolves destination service/node plus compatible artifact port.

A real source execution can carry a source-execution binding containing DGraph, DMap and D-Serv artifact identities. Grant issuance compares that binding exactly against current route authority. If the topology changed after execution, the old emit does not silently gain authority under the new topology.

## DIoT runtime-binding identity

`DIoTRuntimeBindingV1` has a separate operational identity:

```text
binding_id + binding_revision + descriptor_digest
```

DMonitor's `runtime_binding_ref` references those fields rather than pretending the binding is a canonical desired-state contract. This distinction matters: a runtime binding is server-owned **operational** authority describing a concrete realization, while DMap/DForward are accepted desired-state/control-plane authority.

## Monitor instance identity and sequence

A DMonitor observation is uniquely identified by `observation_id`, but stream ordering is governed by `(node_id, monitor_instance_id, sequence)` semantics.

For a given `monitor_instance_id`, `sequence` is monotonic. Restarting while preserving the same monitor instance ID requires preserving/continuing the sequence. A genuinely new monitor instance ID creates a new sequence epoch.

This prevents a restarted collector from making old sequence numbers appear newer than already-ingested evidence.

## Honest unbound evidence

If a collector cannot establish exact canonical correlation, DATUM provides an `unbound` DMonitor subject. This is an intentional safety mechanism.

Do **not** manufacture canonical identity from:

- container name;
- process name;
- hostname;
- image tag;
- port number;
- broker URI;
- a similar-looking service label.

Those values can be useful facts or operational labels, but they are not canonical authority unless an explicit contract binds them.

## Authority-reference matrix

| Consumer | Authority it should use | Authority it must not invent |
|---|---|---|
| D-Deploy acceptance | exact validated DGraph/DContinuum (+ DForward for v2) snapshots | caller-computed “trusted” digest alone |
| D-Code authorization | active DMap + DGraph + DNode + D-Serv artifact | requested target node as authority |
| D-Call route | active DMap/DGraph + artifact ports | caller destination service/node/port |
| DIoT runtime binding | active DMap/2 + DForward + accepted artifact authority | caller-supplied DIoT/node/DMap refs |
| DMonitor convergence | current accepted authority + exact observation refs | hostname/container-name matching |
| D1 readiness | convergence + admitted current health + server policy | caller policy/time override |
| D2 dependency readiness | current provider resolution + exact provider placement D1 readiness | caller-selected provider |

## Sources

[DMap/1 exact references](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/agent/canonical_dmap.rs), [DMap/2 references](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/agent/canonical_dmap_v2.rs), [DMonitor correlation references](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/agent/canonical_dmonitor.rs), [D-Call authority continuity](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/dcall.rs), [DIoT runtime binding](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/diot_runtime_binding.rs).
