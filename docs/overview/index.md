# What is DATUM?

DATUM models distributed applications and their relationship with the computing continuum. A sensor-processing application may use a fog-hosted decoder, a cloud-hosted service and an IoT broker between them. Its logical application structure should remain understandable when machines, addresses or runtime realizations change.

## The problem

A deployment description expresses intent. A registered runtime binding identifies an operational realization. An observation reports a fact at a particular time. These statements support different conclusions: none can stand in for the others.

DATUM keeps those responsibilities separate so planning, execution and diagnosis can use explicit contracts and evidence.

## The IoTinuum

The IoTinuum is the heterogeneous environment spanning devices and edge resources through fog and cloud systems. It is not a requirement to use one machine for each layer. Nodes can differ in capabilities, resource capacity and runtime support, while retaining logical identities independent of addresses.

## Model and implementation

| Name | Meaning |
|---|---|
| DATUM | Architecture and information model |
| DServer | Current D-Controller implementation |
| SmartSentinel | Distributed agent implementing D-Agent responsibilities and governed executor paths |
| D-Node | Runtime that executes application D-Code according to its execution contract |

DATUM is not a synonym for an executor or for one server binary. A read-only observation and a readiness evaluation are useful outcomes even when no deployment occurs.

## Scope of this edition

This edition introduces canonical vocabulary and the evidence path through Phase 114D2. It explains both application readiness and provider-specific `any_element` dependency readiness and points to reproducible integration fixtures. It does not present the entire reference architecture as fully implemented, and it does not claim Phase 114E live multinode validation.

Continue with the [concept glossary](../concepts/index.md), [architecture](../architecture/index.md) and [current limitations](status.md).

## Sources

[DATUM concept](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/concepts/datum.md), [IoTinuum](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/concepts/iotinuum.md), and [canonical vocabulary](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/adr/ADR-0001-canonical-datum-vocabulary.md).
