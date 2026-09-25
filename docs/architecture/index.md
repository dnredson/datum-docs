# Architecture overview

The architecture separates application semantics, accepted placement, operational bindings and runtime evidence. DServer evaluates these together without making an observation into a new placement authority.

## Responsibilities

| Component | Responsibility |
|---|---|
| Canonical contracts | Describe application, continuum, placement and middleware semantics |
| DServer | Govern acceptance, retain operational state, ingest evidence and derive views |
| SmartSentinel / node-side producers | Observe local runtime state and publish evidence through supported paths |
| D-Node execution paths | Run governed application D-Code and support D-Call realization |
| Deployment executor | Perform concrete authorized lifecycle operations |

## The readiness relationship

```mermaid
flowchart TD
    A["Accepted D-Map"] --> C["Convergence interpretation"]
    B["Operational binding"] --> C
    E["DMonitor evidence"] --> F["Freshness and exact correlation"]
    F --> C
    F --> H["Admitted current health"]
    C --> R["Placement readiness"]
    H --> R
    R --> G["Application aggregation"]
    A --> P["Current DForward provider resolution"]
    P --> D["any_element dependency readiness"]
    R --> D
```

This is a dependency diagram for interpretation, not a network topology or an automatic remediation loop. The D2 dependency result consumes the exact provider placement's D1 readiness; it does not substitute whole-application readiness.

## State ownership

Accepted DDeploy state exposes the active placement authority. DMap/2 additionally carries the accepted DForward context and DIoT placements. Operational runtime bindings attach realization details to that authority. DMonitor records facts about observations; it cannot choose placement.

D1 readiness uses one coherent in-process snapshot and one server-owned evaluation time. D2 resolves `any_element` providers from current accepted DMap/2/DForward authority and evaluates their exact placement readiness using the same server-owned governance. Both results are derived on read rather than persisted as independent booleans.

Canonical control-state domains use the existing control-state persistence mechanisms. Legacy compatibility surfaces also exist; they should not be presented as the authority for every canonical subsystem.

## Observation and correction

SmartSentinel's broader responsibilities can be described as preventive governance, detective observation and explicitly governed corrective execution. Canonical DMonitor itself is **detective**: observing divergence does not authorize or execute a correction.

Continue with [desired state, authority and evidence](authority-and-evidence.md).

## Sources

[ADR-0023](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/adr/ADR-0023-canonical-dforward-diot-dmap-v2.md), [ADR-0024](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/adr/ADR-0024-canonical-dmonitor-observation-model.md), [D1 handler](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/api/dmonitor_readiness.rs), [D2 dependency handler](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/api/dforward_dependency_readiness.rs).
