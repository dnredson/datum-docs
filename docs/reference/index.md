# Technical reference

Reference pages describe the pinned prototype baseline. They are not a second source of placement or schema authority.

| Subject | Reference |
|---|---|
| D1 read-only readiness API and findings | [Readiness API](readiness-api.md) |
| Canonical contract families and source revision | [Sources and provenance](sources.md) |
| Architecture decisions | [ADR index](../project/decisions.md) |
| Concept meanings | [Glossary](../concepts/index.md) |

## Contract map

| Contract | Responsibility |
|---|---|
| `datum.dgraph/1` | Placement-free application services and calls |
| `datum.dcontinuum/1` | Continuum configuration represented by the prototype |
| `datum.dmap/1` | Accepted placement contract without canonical DIoT placement |
| `datum.dmap/2` | Placement contract extended with DForward/DIoT realization semantics |
| `datum.dforward/1` | Logical middleware composition |
| `datum.dmonitor-observation/1` | Canonical runtime observation |
| `datum.dmonitor-readiness/1` | Derived server-owned readiness result |

Canonical Rust contracts and ADRs stay in the implementation repository. A complete generated field-level catalog can be added after a pinned extraction workflow is reviewed. This initial site links the authoritative source rather than publishing hand-maintained duplicate schemas.
