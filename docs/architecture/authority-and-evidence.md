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

The authority-only DForward projection describes structural relationships. Its `pending_fresh_evidence` marker does not assert a live decision. D1 readiness adds a governed evidence interpretation, while D2 consumption of that result remains outside this edition's baseline.

## Sources

[Canonical DGraph](https://github.com/dnredson/datum/blob/c059c3341c7901eeea77ce4881bbd341580d8aef/dserver/src/core/canonical_dgraph.rs), [ADR-0023](https://github.com/dnredson/datum/blob/c059c3341c7901eeea77ce4881bbd341580d8aef/documentation/adr/ADR-0023-canonical-dforward-diot-dmap-v2.md), [ADR-0024](https://github.com/dnredson/datum/blob/c059c3341c7901eeea77ce4881bbd341580d8aef/documentation/adr/ADR-0024-canonical-dmonitor-observation-model.md).
