# Status and limitations

**Edition:** development. **Documented implementation:** Phase 114D2 checkpoint, `3e0baa8f415b822f69eef86c0cbfe2a3681e3a65`. **Documentation review date:** 2026-09-25.

The baseline is an explicit historical feature-branch checkpoint. It does not track the implementation branch automatically and does not claim to describe changes after that revision.

## Capability status at the baseline

| Capability | Status | Evidence boundary |
|---|---|---|
| Canonical DMonitor observations and ingestion | Implemented | Typed wire contract, ingestion/state modules and ADR-0024 |
| Freshness and authority correlation | Implemented | Server-derived interpretation |
| DIoT runtime evidence production | Implemented | Governed listener emitter described in ADR-0024 |
| Placement and application readiness | Implemented | D1 core and read-only API retained at the D2 checkpoint |
| Dynamic `any_element` dependency readiness | Implemented | D2 core, read-only API and dedicated integration proof inspected |
| Phase 114 live multinode validation | Open | Next source work begins with 114E0 preflight; a live scenario is not closed by D2 |
| Canonical DServ production evidence emitter | Open | The generic telemetry bridge does not infer DServ identity |
| Automatic correction driven by readiness | Outside D2 | No readiness-triggered restart, redeployment or placement mutation |

## Validation claims

The earlier D1 checkpoint report supplied by the maintainer records 30 focused D1 core/API tests, 181 DServer DMonitor tests, one explicitly executed D1 integration proof, 39 DATUM canonical-DMonitor tests and 54 projection tests passing. Those figures remain historical **reported checkpoint results**, not new executions performed while building this documentation.

For D2, this edition inspected the accepted core, handler and dedicated subprocess integration proof. The D2 integration source explicitly exercises blocked-before-evidence, satisfied-with-exact-provider-Healthy evidence while whole-application readiness remains NotReady, and blocked-again-after-fresh-provider-Unhealthy evidence. The documentation build did not rerun that runtime test suite.

## Practical limitations

An application with required DServ placements can remain `not_ready` when only generic SmartSentinel telemetry is available. The D1 integration proof supplies canonical DServ fixtures to exercise governance. That fixture is not a production collector.

A broker URI or runtime-binding registration alone does not prove runtime liveness. Healthy evidence can age out or refer to obsolete authority. The readiness policy does not accept those observations as proof of current readiness.

Static DForward projection still uses `pending_fresh_evidence` for `any_element`: it is an authority-only view and does not become a live health assertion. D2 adds a separate dynamic, evidence-aware dependency-readiness evaluation against the exact current provider placement.

D2 does not by itself establish a live fog/cloud deployment. Phase 114E validation and its tutorial remain intentionally pending.

## Documentation coverage

Conceptual introduction, authority boundaries, D1 readiness policy/findings, D2 provider-specific dependency readiness, both read-only API surfaces and integration-test entry points are included. A turnkey runtime installation guide, complete API catalog, generated schemas and reproduced live multinode tutorial remain editorial work.

See [source provenance](../reference/sources.md) and [roadmap](../project/roadmap.md).
