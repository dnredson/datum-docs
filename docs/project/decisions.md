# Architecture decisions

ADRs remain authoritative in the implementation repository. The links below target this documentation edition's exact baseline. Access to the private repository is required to open them.

| ADR | Decision area | Reader guide |
|---|---|---|
| [0001](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/adr/ADR-0001-canonical-datum-vocabulary.md) | Canonical vocabulary and legacy graph labels | [Concepts](../concepts/index.md) |
| [0010](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/adr/ADR-0010-cross-node-readiness-fresh-evidence.md) | Fresh provider evidence and D2 cross-node dependency readiness | [Readiness](../operations/readiness.md) |
| [0023](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/adr/ADR-0023-canonical-dforward-diot-dmap-v2.md) | DForward, DIoT, DMap/2 and provider-resolution authority | [Authority and evidence](../architecture/authority-and-evidence.md) |
| [0024](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/adr/ADR-0024-canonical-dmonitor-observation-model.md) | Canonical DMonitor, interpretation, D1 readiness and D2 dependency consumption | [Readiness APIs](../reference/readiness-api.md) |

ADRs are cumulative records. An early paragraph can describe a historical phase boundary later extended by another section. For the current edition, use the D1/D2 sections and implementation at the pinned commit rather than interpreting an original ADR header as a complete current feature list.

This site does not modify, duplicate or silently update the ADRs. A future generated mirror must retain a source commit and be regenerated from that source, not edited independently.
