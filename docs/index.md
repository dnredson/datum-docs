# DATUM

**Understand the application. Locate its realizations. Evaluate the evidence.**

DATUM is an architectural framework and information model for distributed applications across the **IoTinuum**: heterogeneous resources spanning devices, edge, fog and cloud environments.

It gives application structure, accepted placement and runtime observations distinct meanings. That separation makes it possible to ask both *what is authorized to run* and *what the available evidence proves now*.

!!! info "Development documentation · Phase 114D2 baseline"
    This edition describes checkpoint `3e0baa8f415b`, not a stable release. DMonitor-backed application readiness and provider-specific `any_element` dependency readiness are implemented at this baseline; Phase 114E live multinode validation remains open. See [status and limitations](overview/status.md).

<div class="grid cards" markdown>

- **Start with the model**

    Learn what DATUM represents and why application logic, placement and evidence are separate.

    [Read the overview](overview/index.md)

- **Find your way through the architecture**

    Understand DServer, SmartSentinel, the D-Node runtime and the contracts connecting them.

    [Explore the architecture](architecture/index.md)

- **Understand readiness**

    Distinguish health, freshness, convergence, application readiness and provider-specific dependency readiness.

    [Read the readiness guide](operations/readiness.md)

- **Run the first validation scenarios**

    Follow the existing D1 and D2 DServer subprocess integration proofs in an isolated source checkout.

    [Get started](getting-started/index.md)

</div>

## Three questions, three responsibilities

| Question | Primary representation |
|---|---|
| What does the application contain and call? | D-Graph: D-Serv vertices and D-Call edges |
| Where are the required realizations accepted to run? | D-Map, materialized through governed D-Deploy acceptance |
| What was observed, and does it support use now? | D-Monitor evidence plus server-derived convergence and readiness |

The documentation covers concepts, architecture, task guides, technical reference and the project's validation boundaries. Source links are pinned to the [documented revision](reference/sources.md). Some implementation links require repository access.
