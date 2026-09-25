# DATUM

**Understand the application. Locate its realizations. Evaluate the evidence.**

DATUM is an architectural framework and information model for distributed applications across the **IoTinuum**: heterogeneous resources spanning devices, edge, fog and cloud environments.

It gives application structure, accepted placement and runtime observations distinct meanings. That separation makes it possible to ask both *what is authorized to run* and *what the available evidence proves now*.

!!! info "Development documentation · Phase 114D2 baseline"
    This edition describes checkpoint `3e0baa8f415b`, not a stable release. DMonitor-backed application readiness and provider-specific `any_element` dependency readiness are implemented at this baseline; Phase 114E live multinode validation remains open. See [status and limitations](overview/status.md).

<div class="grid cards" markdown>

- **Follow the source-to-deploy tutorial**

    Build DServer and DATUM, configure identities, declare a D-Node, author artifacts and a D-Graph, create a deterministic proposal, explicitly accept a D-Map, then understand the separate runtime-realization paths.

    [Start the tutorials](tutorials/index.md)

- **Learn the vocabulary and entities**

    Start from D-Application, D-Graph, D-Serv, D-Call, D-Node, D-Map, D-Forward, D-IoT, D-Monitor and their concrete identities.

    [Open the entity encyclopedia](concepts/entities.md)

- **Understand authority**

    Follow the distinction between desired state, accepted authority, operational binding, observed evidence, convergence and readiness.

    [Read the lifecycle](architecture/lifecycle.md)

- **Read the contracts**

    Inspect canonical schemas, important fields, invariants and cross-contract relationships.

    [Open the contract reference](reference/contracts.md)

- **Use the API**

    Start with the canonical control-plane surfaces, then use the complete route catalog when debugging or integrating older subsystems.

    [Open the core API](reference/core-api.md)

- **Understand readiness**

    Distinguish health, freshness, convergence, application readiness and provider-specific dependency readiness.

    [Read the readiness guide](operations/readiness.md)

- **Run validation scenarios**

    Follow the existing D1 and D2 DServer subprocess integration proofs in an isolated source checkout.

    [Open the validation examples](examples/first-validation.md)

</div>

## Three questions, three responsibilities

| Question | Primary representation |
|---|---|
| What does the application contain and call? | D-Graph: D-Serv vertices and D-Call edges |
| Where are the required realizations accepted to run? | D-Map, materialized through governed D-Deploy acceptance |
| What was observed, and does it support use now? | D-Monitor evidence plus server-derived convergence and readiness |

A fourth question appears when D-Forward crosses elements: *is the exact provider placement for this dependency usable now?* Phase 114D2 answers it with provider-specific dependency readiness, without replacing D-Map placement authority.

The documentation covers concepts, architecture, source-derived tutorials, contracts, API surfaces, task guides, technical reference and validation boundaries. Source links are pinned to the [documented revision](reference/sources.md). Some implementation links require repository access.
