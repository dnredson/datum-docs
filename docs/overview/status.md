# Status and limitations

**Edition:** development. **Documented implementation:** Phase 114D1 checkpoint, `c059c3341c7901eeea77ce4881bbd341580d8aef`. **Documentation review date:** 2026-09-25.

The baseline is an explicit historical feature-branch checkpoint. It does not track the implementation branch automatically and does not claim to describe changes after that revision.

## Capability status at the baseline

| Capability | Status | Evidence boundary |
|---|---|---|
| Canonical DMonitor observations and ingestion | Implemented | Typed wire contract, ingestion/state modules and ADR-0024 |
| Freshness and authority correlation | Implemented | Server-derived interpretation |
| DIoT runtime evidence production | Implemented | Governed listener emitter described in ADR-0024 |
| Placement and application readiness | Implemented | D1 core and read-only API inspected |
| Dynamic `any_element` dependency consumption | Open at this baseline | D2 work is not included in this commit |
| Phase 114 live multinode validation | Open | Deferred to 114E; earlier transport evidence does not close this gate |
| Canonical DServ production evidence emitter | Open | The generic telemetry bridge does not infer DServ identity |
| Automatic correction driven by readiness | Outside D1 | No readiness-triggered restart, redeployment or placement mutation |

## Validation claims

The checkpoint report supplied by the maintainer records 30 focused D1 core/API tests, 181 DServer DMonitor tests, one explicitly executed D1 integration proof, 39 DATUM canonical-DMonitor tests and 54 projection tests passing. These are **reported checkpoint results**, not new executions performed while building this documentation.

The source of the readiness core, handler and integration test was inspected for this edition. Building the documentation verifies documentation tooling and links; it does not rerun the DATUM runtime suite.

## Practical limitations

An application with required DServ placements can remain `not_ready` when only generic SmartSentinel telemetry is available. The D1 integration proof supplies canonical DServ fixtures to exercise governance. That fixture is not a production collector.

A broker URI or runtime-binding registration alone does not prove runtime liveness. Healthy evidence can age out or refer to obsolete authority. The readiness policy does not accept those observations as proof of current readiness.

At this baseline, static DForward projections can still expose `pending_fresh_evidence` for `any_element`. Do not document a proposed D2 API or provider-selection rule as available functionality.

## Documentation coverage

Conceptual introduction, authority boundaries, readiness policy and findings, read-only API usage, and an integration-test entry point are included. A turnkey runtime installation guide, complete API catalog, generated schemas and reproduced live multinode tutorial remain editorial work.

See [source provenance](../reference/sources.md) and [roadmap](../project/roadmap.md).
