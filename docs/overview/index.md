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
| D-Node | Runtime abstraction that hosts supported execution contracts |

DATUM is not a synonym for an executor or for one server binary. A read-only observation and a readiness evaluation are useful outcomes even when no deployment occurs.

## Scope of DATUM v1

This edition documents the current v1 architecture and implemented control/runtime paths: application structure, continuum and placement authority, operational artifacts, D-Code, reconciliation, observations and readiness.

Not every reference-architecture idea is implemented yet. Where a capability is missing, this site states that directly and records it as planned rather than referring to an internal development milestone. A fully reproduced multi-machine deployment guide is one example of documentation that will be expanded as validation is completed.

Continue with the [concept glossary](../concepts/index.md), [architecture](../architecture/index.md) and [current limitations](status.md).

## Sources

Current source provenance is maintained in [Sources and provenance](../reference/sources.md).
