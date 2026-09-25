# Concepts and vocabulary

The names in DATUM describe responsibilities. Similar-looking identifiers do not make those responsibilities interchangeable.

## Application and execution

| Concept | Meaning | Example |
|---|---|---|
| D-Application | Placement-independent application logic | A sensor-processing application |
| D-Script / D-Function | Source representation and its function units in the reference model | Source functionality before distribution |
| D-Compile | Reference-model compilation into D-Graph and D-Code | The source-to-service mapping responsibility |
| D-Graph | Application graph with D-Serv vertices and D-Call edges | Decoder calls an alerting service |
| D-Serv | Application service that executes D-Code | A decoder service |
| D-Code | Executable of a D-Serv; WebAssembly is the prototype target | Code targeting `datum-dnode/0` |
| D-Call | Semantic invocation between D-Servs | Decoder invokes alerting |
| D-Node | Runtime that executes D-Serv code | A governed application-code host |
| D-Engine | Set of D-Nodes supporting an application | The application's runtime hosts |

Defining a reference-model concept does not establish that its complete implementation exists. In particular, the glossary is not a product feature checklist.

## Placement and middleware

| Concept | Meaning | What it does not establish |
|---|---|---|
| D-Continuum | Supported continuum configuration and constraints for an application | Current runtime health |
| D-Element | Concrete continuum participant; the prototype uses logical `node_id` | A D-Node runtime is not simply its physical machine |
| D-Map | Mapping of application/platform elements onto the continuum | A healthy runtime |
| D-Deploy | Deployment and redeployment responsibility | An accepted proposal is not execution evidence |
| D-Controller | Logically centralized control plane; implemented by DServer | Node-local execution |
| D-Forward | Logical IoT-middleware composition and data paths | Resolved broker addresses or runtime readiness |
| D-IoT | A middleware element of D-Forward | An application D-Serv |

DMap/2 adds DIoT placements and exact DForward references while preserving D-Map as placement authority. One logical middleware identity and one placement identity are different concepts.

## Observation and platform

**D-Monitor** is the monitoring sub-platform and lifecycle process. The canonical observation contract expresses typed runtime evidence. Server-derived readiness is a separate governance result. D2 additionally derives provider-specific readiness for `any_element` DForward dependencies without making D-Monitor a placement authority.

**D-Agent** is a project extension, not a term from the DATUM reference paper. SmartSentinel implements node-local observation, reporting and governed interaction, alongside executor responsibilities.

**D-Platform** groups D-Engine, D-Forward and D-Monitor responsibilities. The grouping should not be assumed to be one first-class runtime object.

## Naming traps

- Canonical D-Graph is placement-free. Legacy structures named `DGraph`, `OperationalDGraph` and observed runtime graphs have different roles.
- A D-Call cycle is communication topology, not a dependency cycle for installation ordering.
- Management WASM used by an agent is not application D-Code.
- An observation may change a derived view without causing a host mutation.
- `project_id` scopes operational state; `application_id` identifies the application. They are not substitutes.

## Sources

[Canonical vocabulary](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/adr/ADR-0001-canonical-datum-vocabulary.md), [glossary](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/reference/glossary.md), [canonical DGraph](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/canonical_dgraph.rs), [DForward and DMap/2](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/adr/ADR-0023-canonical-dforward-diot-dmap-v2.md).
