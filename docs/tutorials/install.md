# Install DATUM v1 from source

DATUM v1 is currently documented as a **source build**. A packaged production installer is not implemented yet and will be documented when available.

## Prerequisites

You need Git, a Rust/Cargo toolchain compatible with the repository lockfiles, Python only for documentation/tooling tasks, and normal host build dependencies. Docker is required for container-realization tutorials.

## 1. Clone the implementation repository

```sh
git clone https://github.com/dnredson/datum.git
cd datum
```

For reproducible documentation examples, inspect the exact source revision used by this site:

```sh
git checkout --detach c08ccc4d715d9eb76644e3f1bd7d80a7945265c4
```

A detached checkout is useful for documentation reproduction because it does not alter your normal development branch.

## 2. Build DServer

```sh
cargo build --locked --manifest-path dserver/Cargo.toml
```

## 3. Build DATUM/SmartSentinel node-side tools

```sh
cargo build --locked --manifest-path DATUM/Cargo.toml
```

This crate contains node-side observation/reconciliation tools and the D-Code runtime utilities used later in the tutorials.

## 4. Isolate control-plane state

Use a disposable state path for tutorial work:

```sh
mkdir -p .local
export DATUM_CONTROL_STATE_DB_PATH="$PWD/.local/datum-control-plane.db"
```

Do not point experiments at an existing production/control-plane database unless you intentionally want to operate on that state.

## 5. Create a tutorial DServer configuration

```sh
cp dserver/config.toml dserver/config.tutorial.toml
export DATUM_DSERVER_CONFIG_PATH="$PWD/dserver/config.tutorial.toml"
```

Review the copied configuration before starting DServer. The server still carries configuration used by older/auxiliary subsystems in addition to the canonical DATUM control-plane paths documented here.

## 6. Start DServer

```sh
cargo run --locked --manifest-path dserver/Cargo.toml --bin DServer
```

In another terminal:

```sh
export DSERVER_URL=http://127.0.0.1:8080
curl -fsS "$DSERVER_URL/health"
```

A healthy server only proves that DServer is reachable. It does not declare a D-Node, create a D-Graph or activate any deployment.

## 7. What is installed where?

```text
DServer
  └─ control-plane authority and registries

DATUM / SmartSentinel tools
  └─ node-side observation, reconciliation and D-Code execution

Docker / native executable / WASM bytes
  └─ actual runtime content, governed separately
```

DServer and D-Node responsibilities are intentionally separate.

## Next

Continue with [Configure components](configure.md), then [Model an existing service](model-existing-service.md).

## Source boundary

The commands above are source-derived from DATUM v1 revision `c08ccc4d715d9eb76644e3f1bd7d80a7945265c4`. This documentation build does not rerun the full runtime build or deployment workflow.
