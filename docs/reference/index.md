# Technical reference

Reference pages describe the pinned prototype baseline. They are not a second source of placement or schema authority.

| Subject | Reference |
|---|---|
| D1 application readiness and D2 dependency-readiness APIs/findings | [Readiness APIs](readiness-api.md) |
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
| `datum.dmonitor-readiness/1` | Derived server-owned placement/application readiness result |
| `datum.dforward-dependency-readiness/1` | Derived server-owned `any_element` provider dependency readiness result |

Canonical Rust contracts and ADRs stay in the implementation repository. A complete generated field-level catalog can be added after a pinned extraction workflow is reviewed. This site links the authoritative source rather than publishing hand-maintained duplicate schemas.
