# Technical reference

Reference pages describe the current **DATUM v1** implementation. They are not a second source of placement or schema authority; authoritative contracts remain in the implementation repository.

## Choose the reference you need

| Need | Page |
|---|---|
| Use the graphical interface | [DATUM Console tutorial](../tutorials/datum-console.md) |
| Integrate with Console read projections or catalog APIs | [Console and catalog API](console-api.md) |
| Understand reusable service definitions | [Service catalog](../concepts/service-catalog.md) |
| Understand each entity and its authority boundary | [Entity encyclopedia](../concepts/entities.md) |
| Understand IDs, revisions, digests and exact references | [Identity and references](../concepts/identities-and-references.md) |
| See canonical schema fields and invariants | [Canonical contracts](contracts.md) |
| Integrate with the canonical control plane | [Core control-plane API](core-api.md) |
| Find broader HTTP routes exposed by DServer | [Complete HTTP API](http-api.md) |
| Interpret D1/D2 readiness responses/findings | [Readiness APIs](readiness-api.md) |
| Verify source revision/provenance | [Sources and provenance](sources.md) |

## New operator-facing surfaces

DATUM v1 now includes two important non-canonical-but-governed surfaces:

- **Operations read API** — bounded read-only projections for the Console;
- **Service catalog API** — versioned reusable modeling definitions whose writes remain catalog-only.

Neither surface replaces canonical placement or runtime authority.

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
| catalog Service Definition | Reusable versioned service modeling; not deployment authority |

Canonical Rust contracts remain in the implementation repository. A generated OpenAPI/schema pipeline is planned; until then, field-level prose remains explicitly source-grounded.
