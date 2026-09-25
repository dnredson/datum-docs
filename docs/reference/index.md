# Technical reference

Reference pages describe the pinned Phase 114D2 prototype baseline. They are not a second source of placement or schema authority; authoritative contracts remain in the implementation repository.

## Choose the reference you need

| Need | Page |
|---|---|
| Understand each entity and its authority boundary | [Entity encyclopedia](../concepts/entities.md) |
| Understand IDs, revisions, digests and exact references | [Identity and references](../concepts/identities-and-references.md) |
| See canonical schema fields and invariants | [Canonical contracts](contracts.md) |
| Integrate with the canonical control plane | [Core control-plane API](core-api.md) |
| Find every HTTP route exposed by DServer | [Complete HTTP API](http-api.md) |
| Interpret D1/D2 readiness responses/findings | [Readiness APIs](readiness-api.md) |
| Verify source revision/provenance | [Sources and provenance](sources.md) |
| Trace architectural decisions | [ADR index](../project/decisions.md) |

## Contract map

| Contract | Responsibility |
|---|---|
| `datum.dgraph/1` | Placement-free application services and calls |
| `datum.dcontinuum/1` | Structural continuum inventory |
| `datum.dmap/1` | Accepted D-Serv placement contract |
| `datum.dmap/2` | Placement contract extended with DForward/DIoT realization semantics |
| `datum.dforward/1` | Logical middleware composition |
| `datum.dserv-artifact/1` | Host-independent content-addressed D-Code descriptor |
| `datum.dmonitor-observation/1` | Canonical runtime observation/evidence |
| `datum.ddeploy-proposal/1` | Candidate placement proposal; never active placement by itself |
| `datum.ddeploy-acceptance/1` | Explicit acceptance/governance record |
| `datum.dmonitor-readiness/1` | Derived server-owned placement/application readiness result |
| `datum.dforward-dependency-readiness/1` | Derived server-owned `any_element` provider dependency readiness result |

## Route classification used in this documentation

The DServer route table includes multiple generations/subsystems. The [complete HTTP API](http-api.md) uses these labels:

- **Core canonical/control-plane** — directly operates on current canonical DATUM authority/evidence domains.
- **Operational** — concrete execution/realization/observation support around canonical authority.
- **Legacy/compatibility** — earlier graph/topology/snapshot surfaces retained by the prototype.
- **Auxiliary/tooling** — dashboard, analysis, AI, planning visualization or introspection surfaces.

These labels describe architectural role, not a support/SLA promise.

Canonical Rust contracts and ADRs stay in the implementation repository. A future generated OpenAPI/schema pipeline can complement this reference; until then, field-level prose here stays explicitly pinned to source rather than pretending to be a separately authoritative schema definition.
