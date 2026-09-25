# Visual guide to DATUM

This page is a **picture-first introduction** to the Phase 114D2 DATUM model. Use it before the detailed [entity encyclopedia](entities.md) when you want the mental model first and the field-level details second.

!!! tip "How to use this page"
    Read the diagrams from top to bottom. Each picture answers one question. When a term becomes familiar, follow the links to the detailed concept, tutorial or reference page.

## The five verbs

The easiest way to remember DATUM is as five different responsibilities:

```mermaid
flowchart LR
    A["1 · Describe\nWhat is the application?"] --> B["2 · Place\nWhere is it accepted to run?"]
    B --> C["3 · Realize\nWhat does the node actually start or execute?"]
    C --> D["4 · Observe\nWhat did a monitor actually see?"]
    D --> E["5 · Decide\nWhat can DServer derive now?"]

    A --- AG["D-Graph"]
    B --- BM["D-Deploy + D-Map"]
    C --- CR["Reconciliation / D-Code runtime"]
    D --- DO["DMonitor observation"]
    E --- ER["Convergence + readiness"]
```

The most important rule is that **each step is a different claim**. A D-Map can authorize placement without proving the software is running. A running process can exist without fresh canonical evidence. A Healthy observation can become stale and stop supporting readiness.

## The model as layers

```mermaid
flowchart TB
    subgraph L1["Application intent"]
        APP["D-Application"]
        DG["D-Graph"]
        DS["D-Serv"]
        DC["D-Call"]
        APP --> DG
        DG --> DS
        DG --> DC
    end

    subgraph L2["Structural continuum"]
        CONT["D-Continuum"]
        NODE["D-Node"]
        CONT --> NODE
    end

    subgraph L3["Accepted authority"]
        DEP["D-Deploy proposal"] --> ACC["Explicit acceptance"] --> DM["Active D-Map"]
    end

    subgraph L4["Runtime realization"]
        OP["Operational reconciliation"]
        CODE["Governed D-Code invocation"]
    end

    subgraph L5["Evidence and interpretation"]
        OBS["DMonitor observations"] --> CONV["Convergence"] --> READY["Readiness"]
    end

    DG --> DEP
    CONT --> DEP
    DM --> OP
    DM --> CODE
    OP --> OBS
    CODE --> OBS
```

Think of these as **layers of meaning**, not five processes that must live in five different binaries.

## D-Graph: what the application is

A D-Graph is placement-free application topology.

```mermaid
flowchart LR
    SENSOR["D-Serv\nsensor-reader"] -->|"D-Call\nraw-sample"| DECODER["D-Serv\ndecoder"]
    DECODER -->|"D-Call\nclassified-event"| ALERT["D-Serv\nalerting"]
```

This picture means:

- three logical D-Servs exist;
- two semantic D-Calls connect them;
- no node, IP, container, PID or broker address has been chosen yet.

A useful test is: **if moving the service to another host changes the D-Graph, placement has leaked into the wrong contract.**

## D-Continuum + D-Map: where things are accepted to run

The D-Continuum describes structural runtime capacity. D-Map binds application entities to that structure after explicit D-Deploy acceptance.

```mermaid
flowchart TB
    subgraph APPG["D-Graph"]
        S1["sensor-reader"]
        S2["decoder"]
        S3["alerting"]
    end

    subgraph CONTG["D-Continuum"]
        N1["D-Node\nedge-01"]
        N2["D-Node\nfog-01"]
        N3["D-Node\ncloud-01"]
    end

    DM["Accepted D-Map"]

    S1 --> DM
    S2 --> DM
    S3 --> DM
    DM -->|"placement"| N1
    DM -->|"placement"| N2
    DM -->|"placement"| N3
```

The arrows from D-Map are **authority**, not observations. They answer “where is this accepted to run?” rather than “what is running right now?”.

## Proposal is not placement authority

```mermaid
stateDiagram-v2
    [*] --> Pending: D-Deploy creates proposal
    Pending --> Accepted: explicit acceptance
    Accepted --> ActiveDMap: materialize canonical D-Map
```

A planner can recommend a placement. It cannot silently turn that recommendation into active authority.

## Two artifact families at this baseline

This is one of the easiest parts of the current implementation to confuse.

```mermaid
flowchart TB
    SERV["Canonical D-Serv\nservice_id = decoder"]

    SERV --> SA["ServiceArtifact\noperational deployment plane"]
    SERV --> CA["datum.dserv-artifact/1\ncanonical D-Code plane"]

    SA --> ELIG["D-Deploy eligibility\ntarget_nodes"]
    SA --> OP["container / native-process\nreconciliation"]

    CA --> ID["WASM digest + ABI + limits"]
    ID --> STORE["node-local\ncontent-addressed module store"]
    STORE --> INV["governed D-Code invocation"]
```

`ServiceArtifact` and `datum.dserv-artifact/1` **are not aliases**. The first currently serves operational deployment/reconciliation and D-Deploy eligibility. The second describes canonical content-addressed D-Code.

See [Author software artifacts](../tutorials/artifacts.md) for the concrete JSON examples.

## D-Node is not the machine, agent or heartbeat

Several identities may refer to the same physical environment without meaning the same thing.

```mermaid
flowchart LR
    HOST["Physical host / VM"]
    DN["D-Node\nstructural runtime identity"]
    AG["SmartSentinel agent\noperational process"]
    LOC["Local D-Code identity\nnode-side persisted identity"]
    TEL["Telemetry / heartbeat\nobserved operational state"]

    HOST -. may host .-> DN
    HOST -. runs .-> AG
    AG -. uses .-> LOC
    AG -. emits .-> TEL
```

Only the D-Node structural registry contributes the structural node facts used to derive the authoritative D-Continuum. A heartbeat cannot invent structural capacity; a hostname cannot be guessed into a canonical node identity.

## Project scope versus application identity

```mermaid
flowchart TB
    P["Project\nproject_id"]
    A1["D-Application A\napplication_id"]
    A2["D-Application B\napplication_id"]
    P -->|"governs operational state for"| A1
    P -->|"governs operational state for"| A2
    A1 --> G1["D-Graph A"]
    A2 --> G2["D-Graph B"]
```

A project can govern multiple applications. The canonical D-Graph carries `application_id`; it deliberately does not carry `project_id`.

## D-Call: semantic edge first, transport later

```mermaid
flowchart LR
    SRC["D-Serv A"] -->|"D-Call\nsemantic invocation"| DST["D-Serv B"]

    DM["Active D-Map"] -. resolves nodes .-> ROUTE["Derived runtime route"]
    ART["D-Serv artifacts"] -. resolve ports .-> ROUTE
    SRC -. call identity .-> ROUTE
    ROUTE --> DELIVERY["local or remote delivery"]
```

The D-Call does not contain a socket address, destination node or broker URI. Runtime routing is derived later from current accepted authority and artifact compatibility.

## D-Forward and DIoT: middleware plane

D-Forward is deliberately separate from the D-Graph application-service plane.

```mermaid
flowchart LR
    EXTIN["External input"] --> BRIDGE["DIoT\nbridge"]
    BRIDGE -->|"interface: telemetry"| BROKER["DIoT\nbroker"]
    BROKER --> EXT["External output"]

    P1["DIoT placement\nbridge @ edge-01"] -. realizes .-> BRIDGE
    P2["DIoT placement\nbroker @ fog-01"] -. realizes .-> BROKER
    BIND["Runtime binding\nmqtt://..."] -. operational endpoint .-> P2
```

Logical middleware identity, placement identity and concrete broker binding are intentionally distinct.

## DMonitor: observation is evidence, not authority

```mermaid
flowchart LR
    REAL["Runtime reality"] --> COL["Collector"]
    COL --> OBS["Canonical DMonitor\nobservation"]
    OBS --> FRESH["Fresh enough?"]
    FRESH --> CORR["Matches exact current authority?"]
    CORR --> CONV["Converged?"]
    CONV --> HEALTH["Healthy under policy?"]
    HEALTH --> READY["Placement readiness"]
```

This explains why `Healthy` and `Ready` are different words:

- `Healthy` is part of what an observation reported;
- readiness is a **current server-derived governance result** over freshness, exact authority correlation, convergence and admitted health.

## Application readiness versus dependency readiness

```mermaid
flowchart TB
    P1["Provider placement\nReady"] --> DEP["any_element dependency\nSatisfied"]
    OTHER["Unrelated required placement\nNot Ready"] --> APP["Application\nNot Ready"]
    P1 --> APP
```

A specific provider dependency can be satisfied while the overall application is still NotReady because another required placement is missing or unhealthy. Phase 114D2 intentionally evaluates these questions separately.

## One complete journey

```mermaid
sequenceDiagram
    actor Dev as Developer / Operator
    participant DS as DServer
    participant Node as D-Node runtime
    participant Mon as DMonitor collector

    Dev->>DS: Declare structural D-Node
    Dev->>DS: Register ServiceArtifact
    Dev->>DS: Submit D-Graph to deterministic planner
    DS-->>Dev: Pending D-Deploy proposal
    Dev->>DS: Explicitly accept proposal
    DS-->>Dev: Active canonical D-Map
    Dev->>Node: Realize accepted software under governed path
    Node-->>Mon: Runtime exists / executes
    Mon->>DS: Canonical observation
    Dev->>DS: Query readiness
    DS-->>Dev: Derived current readiness
```

The sequence is intentionally explicit because DATUM does not collapse governance, execution and observation into one opaque “deploy” operation.

## Common false equivalences

| Tempting shortcut | Correct mental model |
|---|---|
| D-Graph = deployment | D-Graph describes application structure; D-Map establishes accepted placement. |
| proposal = D-Map | A proposal is pending candidate state until explicit acceptance. |
| D-Node = machine | D-Node is a structural logical runtime identity. |
| D-Node = Sentinel | Structural node authority and agent lifecycle are separate domains. |
| container running = Ready | Runtime state still needs fresh, exactly-correlated canonical evidence. |
| Healthy = Ready | Healthy is an observation condition; Ready is a derived governance result. |
| broker URI = broker healthy | Runtime binding gives operational identity, not liveness evidence. |
| ServiceArtifact = D-Code artifact | They are separate artifact families at the current baseline. |
| D-Call = TCP/HTTP endpoint | D-Call is semantic application communication; transport is derived later. |
| `target_nodes` = placement authority | It constrains proposal eligibility; accepted D-Map becomes placement authority. |

## Where to continue

- Want the precise meaning of every object? Read the [entity encyclopedia](entities.md).
- Want IDs, digests and correlation rules? Read [identity and references](identities-and-references.md).
- Want to build and deploy something? Start the [tutorial path](../tutorials/index.md).
- Want the exact contract fields? Open [canonical contracts](../reference/contracts.md).
- Want the end-to-end authority transition? Read [lifecycle and authority flow](../architecture/lifecycle.md).

!!! note "Baseline boundary"
    The pictures summarize the documented Phase 114D2 model. They do not imply that Phase 114E live multinode validation or the canonical production DServ evidence emitter has already closed.
