# Sources and provenance

This edition is based on **dnredson/datum**, commit `3e0baa8f415b822f69eef86c0cbfe2a3681e3a65`, the Phase 114D2 checkpoint. Source review took place on 2026-09-25.

The implementation repository is private. Readers without access can use this site's explanations, but source/ADR links require repository permission. CI does not fetch or publish the private repository.

## Evidence used

The following files were retrieved at the pinned commit. Their Git blob IDs identify source content independently of future branch movement. Source inspection does not establish a fresh runtime test run.

| Source | Git blob ID |
|---|---|
| [dserver/src/main.rs](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/main.rs) | `1da08b3c9699c6b146ca82a4f961a2c949818cf3` |
| [DATUM/src/agent/canonical_dgraph.rs](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/agent/canonical_dgraph.rs) | `11a0a6b534adc1ed670d8edf2069f57503034bef` |
| [DATUM/src/agent/canonical_dcontinuum.rs](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/agent/canonical_dcontinuum.rs) | `8d6115b01c217cb0b084fa1e232e123af4c5c47e` |
| [DATUM/src/agent/canonical_dforward.rs](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/agent/canonical_dforward.rs) | `17b227bdaa84e58dfeed9d550a79c56710e88ebb` |
| [DATUM/src/agent/canonical_dmap_v2.rs](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/agent/canonical_dmap_v2.rs) | `5243e0d4387101d4d4bb03c40adfded5560b3482` |
| [DATUM/src/agent/canonical_dmonitor.rs](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/agent/canonical_dmonitor.rs) | `aea21e92885d17225215fb31995602fb1db02d42` |
| [documentation/adr/ADR-0024-canonical-dmonitor-observation-model.md](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/adr/ADR-0024-canonical-dmonitor-observation-model.md) | `be0dfa88d70a5dced58cdd28a3153ad6fffe57e8` |
| [documentation/adr/ADR-0023-canonical-dforward-diot-dmap-v2.md](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/adr/ADR-0023-canonical-dforward-diot-dmap-v2.md) | `2f76811c13dfe4b7babd873733bd8c6fbbed7047` |
| [documentation/adr/ADR-0010-cross-node-readiness-fresh-evidence.md](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/adr/ADR-0010-cross-node-readiness-fresh-evidence.md) | `6046c32c64713c05293193e1c0634b27f6c22b36` |
| [dserver/Cargo.toml](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/Cargo.toml) | `76916edcc408cf9ec40b7383c31a5b9894b2f0ce` |
| [DATUM/Cargo.toml](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/Cargo.toml) | `0240a8aea5e648ab9894cfafa72ca8057b9b01e8` |
| [dserver/src/core/dmonitor_readiness.rs](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/dmonitor_readiness.rs) | `f8d76528037cf3df3f465e477c06fae8692cd456` |
| [dserver/src/api/dmonitor_readiness.rs](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/api/dmonitor_readiness.rs) | `c5c9ec482837d22642b85a583f855e0a7839ab80` |
| [dserver/src/core/dforward_dependency_readiness.rs](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/dforward_dependency_readiness.rs) | `bdab45d53f83c03db9909e259299241bf74210df` |
| [dserver/src/api/dforward_dependency_readiness.rs](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/api/dforward_dependency_readiness.rs) | `ad4b787d684254b32f5a7f9c7d10b95a90df63e6` |
| [documentation/concepts/datum.md](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/concepts/datum.md) | `2d0e0ccca7128e3c0dbb592a62c8a119d4bf9d1b` |
| [documentation/concepts/iotinuum.md](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/concepts/iotinuum.md) | `36195d4e1ed08c6aad3c90463e7cff35dc590cd0` |
| [documentation/adr/ADR-0001-canonical-datum-vocabulary.md](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/adr/ADR-0001-canonical-datum-vocabulary.md) | `78a5205bed2e43238eb7d9cf2e059a98659d4927` |
| [documentation/reference/glossary.md](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/documentation/reference/glossary.md) | `02a68591f736667f3cb60e0b2e310c6a98db480b` |
| [dserver/src/core/canonical_dgraph.rs](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/canonical_dgraph.rs) | `a4a3c1a913852e9e91372ab222bcfe2469c1457b` |
| [DATUM/tests/dmonitor_d1_readiness_integration.rs](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/tests/dmonitor_d1_readiness_integration.rs) | `ea4377883a254469059c7584b768193f3991a87c` |
| [DATUM/tests/dmonitor_d2_dependency_readiness_integration.rs](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/tests/dmonitor_d2_dependency_readiness_integration.rs) | `e293094dd094f02017f07379d2c0309ab92b5eea` |

Additional source modules were inspected to expand conceptual/API documentation, including D-Deploy, D-Node registry, D-Serv artifact/D-Code, D-Call and DIoT runtime binding. Their links are pinned inline on the pages that derive claims from them.

## Tutorial source trail

The source-to-deploy tutorials additionally inspect and link the current implementation of each operational step rather than deriving a hypothetical workflow. Important inputs include:

- [DServer configuration](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/config.rs) and [SQLite control state](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/storage/control_state.rs);
- [D-Node registry API](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/api/dnode_registry.rs);
- [ServiceArtifact API](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/api/service_artifacts.rs) and [registry/validation](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/service_artifact_registry.rs);
- [D-Deploy API](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/api/ddeploy.rs), [D-Deploy authority](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/ddeploy.rs) and [deterministic placement](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/canonical_placement.rs);
- [canonical D-Serv artifact](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/core/dserv_artifact.rs) and [D-Code registry API](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/api/dcode.rs);
- [D-Code ABI](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/dcode/abi.rs), [runtime](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/dcode/runtime.rs), [module store](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/dcode/module_store.rs), [identity initialization](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/bin/smartsentinel-dcode-init.rs), [module installation](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/bin/smartsentinel-dcode-install.rs) and [governed invocation](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/bin/smartsentinel-dcode-invoke.rs);
- [operational reconciler CLI](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/bin/smartsentinel-operational-reconcile.rs) and [laboratory artifact/bundle status](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/artifacts/README.md).

The tutorials are therefore **source-inspected**, not a fresh clean-host reproduction. This distinction is deliberate and is repeated at the execution boundaries where it matters.

## Reading historical material

Early sections of cumulative ADRs can describe a phase that was later extended. This site uses the D1 implementation plus the D2 dependency-readiness additions at the pinned checkpoint. Older architecture pages are context, not evidence that every statement still describes canonical control-state persistence.

The canonical glossary distinguishes D-Node (runtime) from a continuum element or physical machine. Legacy snapshot terminology must not silently replace the typed canonical contracts.

The DServer router also exposes older and auxiliary subsystems. The [complete HTTP API](http-api.md) records them, while the [core API](core-api.md) identifies the routes most directly tied to current canonical authority/evidence domains.

## Maintaining the baseline

`source-baseline.json` records the source revision and known open boundaries. Update the manifest, source links, visible baseline and affected statements together. The checks detect mixed commit references and missing local links; they cannot automatically verify the truth of an implementation claim.

The brand PNG files are unchanged copies of the project's assets from the documented project lineage. See repository `NOTICE.md`.
