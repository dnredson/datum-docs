# Desired state, authority and observed evidence

A useful diagnosis needs three independent answers: what is intended, what is currently accepted, and what the runtime evidence supports.

## Application semantics

D-Graph defines application services and calls. Its canonical shape contains no placement, container identity or observed health. DForward defines logical middleware elements, interfaces and connections, without embedding broker addresses or runtime readiness.

## Accepted placement

D-Map is the authoritative placement carrier in the prototype. DDeploy acceptance establishes the active authority. Derived projections may repeat that placement but must not originate a competing placement decision.

DMap/2 adds DIoT placement and exact references to DForward. DMap/1 remains a separate supported version and has no canonical DIoT placement dimension.

## Operational realization

A DIoT runtime binding records how a governed placement resolves operationally, including its broker URI. Consumers must validate that the binding still matches current authority. Registration is not evidence that the runtime has connected successfully.

## Observed evidence

A canonical observation identifies its subject, provenance and observed condition. Exact references use identity, revision and digest. A hostname, image name, container name or port is not an acceptable substitute for that identity chain.

An old realization may remain healthy after accepted authority advances. Its health claim is still an observation, but it cannot establish readiness for the new authority.

| Situation | Interpretation |
|---|---|
| Binding registered, no admitted observation | Runtime readiness is not proven |
| Fresh evidence matches current authority and reports Healthy | Can support readiness when convergence is also established |
| Healthy evidence references an obsolete binding | Cannot establish current placement readiness |
| Fresh exact-current evidence reports Unhealthy | Convergence may hold while readiness fails |

## Static versus dynamic views

The authority-only DForward projection describes structural relationships. For `scope = any_element`, its `readiness_authority = "dmonitor"` and `readiness_state = "pending_fresh_evidence"` fields deliberately remain a static marker rather than a live decision.

D1 provides the governed evidence interpretation and exact placement readiness. D2 is the separate dynamic counterpart for cross-node `any_element` dependencies: it resolves the provider from the **current accepted** DForward/DMap/2 authority and asks whether that exact provider placement is Ready under D1 governance. It neither rewrites static projection nor promotes an observation into placement authority.

Provider ambiguity, placement ambiguity, absent provider readiness or a provider that is not Ready fail closed as a blocked dependency. A caller cannot supply an alternate provider to the D2 read-only endpoint.

## Sources

[Canonical DGraph](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/canonical_dgraph.rs), [ADR-0023](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/adr/ADR-0023-canonical-dforward-diot-dmap-v2.md), [ADR-0024](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/adr/ADR-0024-canonical-dmonitor-observation-model.md), [D2 dependency core](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/dforward_dependency_readiness.rs).
