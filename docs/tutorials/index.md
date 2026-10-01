# Tutorials

These tutorials describe the current **DATUM v1** implementation and keep **modeling, authority, realization, evidence and presentation** as separate steps.

!!! important "What the graphical interface means"
    The DATUM Console is a presentation/composition layer. It can show accepted authority, catalog definitions and runtime evidence together, but it does not make a visual edge, badge or page into new canonical authority.

## Recommended paths

### Graphical operator path

1. [DATUM Console](datum-console.md) — run the interface, browse projects, inspect logical/runtime graph views and use the catalog.
2. [Model an existing service](model-existing-service.md) — understand the operational facts behind a service before cataloging or deploying it.
3. [Service model to node execution](service-to-node.md) — understand what must happen after modeling before software actually runs.
4. [Troubleshoot common failures](troubleshooting.md) — map failures to the authority/identity gate that refused them.

### Control-plane/runtime path

1. [Install from source](install.md).
2. [Configure components](configure.md).
3. [Author software artifacts](artifacts.md).
4. [Create a D-Graph](dgraph.md).
5. [Perform a basic governed deploy](basic-deploy.md).
6. [Follow Mosquitto end to end](mosquitto-end-to-end.md).
7. [Understand runtime realization](runtime-realization.md).

## Full lifecycle

```mermaid
flowchart LR
    M["Model"] --> C["Catalog / artifact identity"]
    C --> G["D-Graph"]
    G --> P["Propose"]
    P --> A["Accept D-Map"]
    A --> AU["Authorize realization"]
    AU --> R["Realize"]
    R --> E["Evidence"]
    E --> Q["Readiness"]
    C --> UI["Console"]
    G --> UI
    A --> UI
    E --> UI
    Q --> UI
```

The Console can visualize several boxes at once, but the boxes remain separate claims.

## Pick the right software path

```mermaid
flowchart TB
    SW["Software you want DATUM to govern"] --> Q{"What is it?"}
    Q -->|"long-running container"| C["ServiceArtifact\nruntime.kind=container"]
    Q -->|"long-running executable"| N["ServiceArtifact\nruntime.kind=native_process"]
    Q -->|"application function / D-Code"| D["D-Script/D-Compile\n+ datum.dserv-artifact/1"]
    C --> OP["Operational reconciliation"]
    N --> OP
    D --> DC["Exact-revision D-Code authorization\n+ isolated Wasmtime invocation"]
```

## Source and evidence boundary

Current v1 material is grounded in implementation revision `7a79bd84bc05a1ea18870715cc033567ff472afc`. The documentation build validates links/navigation/rendering; it does not rerun the implementation test suite or physical-node validation.

See [sources and provenance](../reference/sources.md) and [status and limitations](../overview/status.md).
