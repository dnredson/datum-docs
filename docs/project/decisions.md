# Architecture decisions

ADRs remain authoritative in the implementation repository. The links below target this documentation edition's exact baseline. Access to the private repository is required to open them.

| ADR | Decision area | Reader guide |
|---|---|---|
| [0001](https://github.com/dnredson/datum/blob/c059c3341c7901eeea77ce4881bbd341580d8aef/documentation/adr/ADR-0001-canonical-datum-vocabulary.md) | Canonical vocabulary and legacy graph labels | [Concepts](../concepts/index.md) |
| [0010](https://github.com/dnredson/datum/blob/c059c3341c7901eeea77ce4881bbd341580d8aef/documentation/adr/ADR-0010-cross-node-readiness-fresh-evidence.md) | Fresh provider evidence for cross-node requirements | [Readiness](../operations/readiness.md) |
| [0023](https://github.com/dnredson/datum/blob/c059c3341c7901eeea77ce4881bbd341580d8aef/documentation/adr/ADR-0023-canonical-dforward-diot-dmap-v2.md) | DForward, DIoT and DMap/2 | [Authority and evidence](../architecture/authority-and-evidence.md) |
| [0024](https://github.com/dnredson/datum/blob/c059c3341c7901eeea77ce4881bbd341580d8aef/documentation/adr/ADR-0024-canonical-dmonitor-observation-model.md) | Canonical DMonitor and subsequent interpretation/readiness layers | [Readiness API](../reference/readiness-api.md) |

ADRs are cumulative records. An early paragraph can describe a historical phase boundary later extended by another section. For D1, use the readiness section and implementation at the pinned commit rather than interpreting the original ADR header as a complete current feature list.

This site does not modify, duplicate or silently update the ADRs. A future generated mirror must retain a source commit and be regenerated from that source, not edited independently.
