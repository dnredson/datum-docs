# DATUM

**Understand the application. Locate its realizations. Evaluate the evidence.**

DATUM is an architectural framework and information model for distributed applications across the **IoTinuum**: heterogeneous resources spanning devices, edge, fog and cloud environments.

It gives application structure, accepted placement and runtime observations distinct meanings. That separation makes it possible to ask both *what is authorized to run* and *what the available evidence proves now*.

!!! info "Development documentation · Phase 114D1 baseline"
    This edition describes checkpoint `c059c3341c79`, not a stable release. DMonitor-backed readiness is implemented at this baseline; dynamic `any_element` consumption and live multinode validation remain open. See [status and limitations](overview/status.md).

<div class="grid cards" markdown>

- **Start with the model**

    Learn what DATUM represents and why application logic, placement and evidence are separate.

    [Read the overview](overview/index.md)

- **Find your way through the architecture**

    Understand DServer, SmartSentinel, the D-Node runtime and the contracts connecting them.

    [Explore the architecture](architecture/index.md)

- **Understand readiness**

    Distinguish health, freshness, convergence and a governed readiness decision.

    [Read the readiness guide](operations/readiness.md)

- **Run the first validation scenario**

    Follow an existing DServer subprocess integration proof in an isolated source checkout.

    [Get started](getting-started/index.md)

</div>

## Three questions, three responsibilities

| Question | Primary representation |
|---|---|
| What does the application contain and call? | D-Graph: D-Serv vertices and D-Call edges |
| Where are the required realizations accepted to run? | D-Map, materialized through governed D-Deploy acceptance |
| What was observed, and does it support use now? | D-Monitor evidence plus server-derived convergence and readiness |

The documentation covers concepts, architecture, task guides, technical reference and the project's validation boundaries. Source links are pinned to the [documented revision](reference/sources.md). Some implementation links require repository access.
