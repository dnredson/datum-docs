# Realize an accepted deployment

Accepted authority and running software are intentionally different facts. This page explains the two realization paths currently visible in the repository and what can—and cannot—be claimed from each.

## Authority versus realization versus evidence

Keep this sequence explicit:

```text
accepted DMap
  = where DATUM authorizes a D-Serv to be placed

runtime realization
  = what the node actually starts/executes under governed operational rules

DMonitor evidence
  = what an observer actually saw

readiness
  = what DServer can currently derive from fresh, exactly-correlated evidence
```

No arrow in this sequence is logically automatic just because the previous object exists.

## Path A — operational reconciliation

The DATUM package includes `smartsentinel-operational-reconcile`. Its own CLI description is precise: it resolves a bound role, fetches an operational D-Graph slice, runs sandboxed WASM reconciliation, and **optionally** executes governed host actions.

A dry-run-shaped invocation is:

```sh
cargo run --locked --manifest-path DATUM/Cargo.toml \
  --bin smartsentinel-operational-reconcile -- \
  --config DATUM/config.toml \
  --node-id tutorial-node \
  --dserver-url "$DSERVER_URL" \
  --project-id "$PROJECT_ID" \
  --out reconcile-report.json
```

Without `--execute`, the CLI does not request host mutation execution.

### Why the basic tutorial stops short of `--execute`

The operational reconciliation plane has more prerequisites than “an active D-Map exists.” It uses operational resource/role binding, a node-specific operational D-Graph slice, governed reconciliation context, management WASM decision logic, authorization and local execution policy.

The repository's `artifacts/prepare.py` can build node-specific laboratory bundles, but its own documentation explicitly states that preparation does **not** publish artifacts, authorize a D-Graph, pull images or start containers. Existing lab evidence is not promoted into a new Phase 114E proof here.

Therefore this edition explains the real reconciler entry point and safe dry-run boundary without inventing a one-command bridge that the current canonical onboarding path does not yet expose.

### When execution is eventually requested

`--execute` is a meaningful side-effect boundary. Before using it, an operator must satisfy the current operational authorization/pinning/prerequisite path for that node and review the proposed actions. The reconciler reports whether control-plane authorization/local execution were permitted and whether host mutation occurred.

The live fog/cloud sequence will be added after Phase 114E closes with captured evidence.

## Path B — governed canonical D-Code

D-Code has a more self-contained current execution path once its placement and content authority are established.

### Prerequisites

For one D-Code service you need all of the following:

1. a structural D-Node declaration in DServer;
2. an accepted D-Map placing the D-Serv on that exact node;
3. a canonical `datum.dserv-artifact/1` registered for `(application_id, dserv_id)`;
4. the exact WASM bytes installed in that node's local content-addressed store;
5. a local D-Node identity matching the node that DServer will authorize.

In the current D-Deploy v1 workflow, the service also still needs the matching project-scoped `ServiceArtifact` used by proposal/acceptance eligibility.

### Initialize local identity

If not already done:

```sh
export NODE_ID=tutorial-node
export DNODE_ROOT="$HOME/.datum/$NODE_ID"

cargo run --locked --manifest-path DATUM/Cargo.toml \
  --bin smartsentinel-dcode-init -- \
  --node-id "$NODE_ID" \
  --dnode-root "$DNODE_ROOT"
```

The governed invocation CLI intentionally reads this identity instead of accepting a normal `--node-id` override.

### Install exact module bytes

```sh
SHA256=$(sha256sum build/hello.wasm | awk '{print $1}')

cargo run --locked --manifest-path DATUM/Cargo.toml \
  --bin smartsentinel-dcode-install -- \
  --module-path build/hello.wasm \
  --declared-sha256 "$SHA256" \
  --store-root "$DNODE_ROOT"
```

The module store is operational and local. The path is derived from content digest; the digest, not the filesystem path, is canonical identity.

### Governed invocation

Prepare an input payload:

```sh
printf '{}\n' > input.json
```

Then invoke:

```sh
cargo run --locked --manifest-path DATUM/Cargo.toml \
  --bin smartsentinel-dcode-invoke -- invoke \
  --dserver-url "$DSERVER_URL" \
  --project-id "$PROJECT_ID" \
  --application-id "app:dcode-tutorial" \
  --service-id "hello-dcode" \
  --input-port input \
  --dnode-root "$DNODE_ROOT" \
  --input-path input.json \
  --evidence-out dcode-evidence.json
```

The governed path obtains fresh DServer authorization rather than treating the local module's presence as permission to execute it.

DServer itself does not execute guest bytes. The node-side path loads the exact authorized artifact/module identity and executes D-Code in an isolated short-lived worker using Wasmtime. The v0.1 runtime creates a fresh store/instance per invocation and rejects host imports.

### Authorization is current-state dependent

A module that was once valid is not necessarily currently authorized. Authorization binds to active canonical authority such as the current D-Map/D-Graph placement and the currently registered artifact identity. If placement or artifact authority no longer matches, execution must fail closed rather than silently running historical content.

## Runtime success is still not application readiness

A successful invocation or a running container is not automatically D1 readiness. Canonical readiness is derived from DMonitor observations with freshness and exact current-authority correlation.

At Phase 114D2:

```text
GET /api/v1/dmonitor/readiness/:project_id/:application_id
```

derives placement/application readiness, and:

```text
GET /api/v1/dforward/dependency-readiness/:project_id/:application_id/:node_id
```

derives dynamic provider-specific `any_element` dependency readiness for DMap/2/DForward flows.

The generic telemetry bridge is not a production canonical DServ evidence emitter. Do not turn absence of that collector into a false claim that a newly reconciled service is canonically ready.

## Source trail

- [Operational reconciler CLI](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/bin/smartsentinel-operational-reconcile.rs)
- [Laboratory artifact/bundle status](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/artifacts/README.md)
- [D-Code init](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/bin/smartsentinel-dcode-init.rs)
- [D-Code install](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/bin/smartsentinel-dcode-install.rs)
- [D-Code invoke](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/bin/smartsentinel-dcode-invoke.rs)
- [D-Code worker](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/src/bin/smartsentinel-dcode-worker.rs)