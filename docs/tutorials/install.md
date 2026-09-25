# Install DATUM from source

The Phase 114D2 repository does not expose a packaged `apt`, Homebrew, container-image or one-command production installer for DATUM itself. The supported documentation claim here is therefore **source installation**: obtain the pinned source, build the two Rust crates, configure DServer, then run the required binaries.

## What you are installing

The repository contains two Rust packages with different responsibilities:

- `dserver/` — DServer, the central HTTP/control-plane service.
- `DATUM/` — the DATUM/SmartSentinel agent and node-side runtime/tooling binaries, including the D-Code tools and operational reconciler.

Both manifests use Rust edition 2021. The inspected manifests do not declare a minimum Rust compiler version, so this guide deliberately does not invent one.

## Prerequisites

You need Git, a Rust/Cargo toolchain capable of building the checked-in lockfiles, and the normal native build dependencies required by the Rust dependency graph on your host. Some later operational examples additionally use Docker and common shell utilities; they are not required merely to compile both crates.

`jq` is used in examples only as a convenience for extracting JSON fields. It is not a DATUM runtime dependency.

## 1. Obtain the documented revision

```sh
git clone https://github.com/dnredson/datum.git
cd datum
git checkout --detach 3e0baa8f415b822f69eef86c0cbfe2a3681e3a65
```

A detached checkout is useful for following this documentation because every source claim is pinned to exactly this revision. Normal development should happen on an appropriate branch instead.

## 2. Build DServer

```sh
cargo build --locked --manifest-path dserver/Cargo.toml
```

`--locked` asks Cargo to use the checked-in lockfile resolution rather than silently updating dependency selection.

## 3. Build the DATUM agent/runtime tools

```sh
cargo build --locked --manifest-path DATUM/Cargo.toml
```

This builds the package that contains the main DATUM binary and node-side utilities such as:

- `smartsentinel-operational-reconcile`;
- `smartsentinel-dcode-init`;
- `smartsentinel-dcode-install`;
- `smartsentinel-dcode-invoke`;
- the isolated `smartsentinel-dcode-worker` used by the governed D-Code invocation path.

## 4. Prepare an isolated DServer state path

Many current canonical/control-plane domains use one SQLite control-state database. The path is selected by `DATUM_CONTROL_STATE_DB_PATH`; otherwise DServer uses `datum-control-plane.db` relative to its working context.

For a tutorial checkout, keep state isolated:

```sh
mkdir -p .local
export DATUM_CONTROL_STATE_DB_PATH="$PWD/.local/datum-control-plane.db"
```

The control-state layer creates its parent directory and initializes the SQLite schema when needed.

!!! warning
    Do not point a tutorial session at a production or shared control-state database. D-Node declarations, ServiceArtifacts, proposals, acceptances, D-Code descriptors and DMonitor evidence are persistent control-plane state.

## 5. Prepare DServer configuration

DServer first honors `DATUM_DSERVER_CONFIG_PATH`; otherwise it searches common `config.toml` locations. Start from the repository's development configuration rather than modifying it in place:

```sh
cp dserver/config.toml dserver/config.tutorial.toml
export DATUM_DSERVER_CONFIG_PATH="$PWD/dserver/config.tutorial.toml"
```

The current application config contains a `[server]` section, a required `[firebase]` section and optional CORS configuration. The checked-in example binds `0.0.0.0:8080` and contains project/collection names used by older snapshot/analysis surfaces.

This tutorial's canonical D-Node/D-Deploy/D-Code control-state workflow is primarily SQLite-backed, but DServer still initializes its broader Firebase client because the process also exposes earlier/auxiliary APIs. Treat the checked-in configuration as a development example, not a production security template.

## 6. Start DServer

```sh
cargo run --locked --manifest-path dserver/Cargo.toml --bin DServer
```

If `server.bind` is absent, the source defaults to `0.0.0.0:8080`. The rest of this tutorial uses loopback explicitly:

```sh
export DSERVER_URL=http://127.0.0.1:8080
```

In a second shell, verify the minimal health endpoint:

```sh
curl -fsS "$DSERVER_URL/health"
```

## 7. Keep implementation roles separate

A running DServer is not a D-Node. A D-Node is a structural logical runtime identity that must be declared separately. Likewise, the main DATUM agent configuration, Sentinel registration and D-Code local identity are different records with different authority.

The next tutorial performs those configuration steps explicitly: [configure the control plane and identities](configure.md).

## Source trail

- [DServer manifest](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/Cargo.toml)
- [DATUM manifest](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/DATUM/Cargo.toml)
- [DServer configuration loader](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/config.rs)
- [DServer startup/router](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/main.rs)
- [SQLite control state](https://github.com/dnredson/datum/blob/3e0baa8f415b822f69eef86c0cbfe2a3681e3a65/dserver/src/storage/control_state.rs)