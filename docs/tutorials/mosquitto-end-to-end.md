# Mosquitto end to end: artifact → D-Map → running node

This tutorial follows one real checked-in service through the DATUM v1 operational path.

```text
Mosquitto software
→ ServiceArtifact
→ DServer registry
→ execution identity/pinning
→ D-Graph
→ D-Deploy proposal
→ explicit acceptance
→ active D-Map
→ node operational slice
→ finite reconciliation authorization
→ preview
→ --execute
→ container on node
→ evidence/readiness
```

The purpose is to make every authority transition visible. DATUM does not treat “deploy” as one opaque operation.

## 1. Start from the real Mosquitto artifact

The implementation repository includes a Mosquitto ServiceArtifact with these operational facts:

```text
artifact_id            mosquitto
service_id             mqtt
runtime.kind           container
container_name         datum-mosquitto
image                  eclipse-mosquitto, content-pinned
port                   1883/tcp
configuration mount    mosquitto/mosquitto.conf
execution probe        docker_container_running
health probe           tcp_connect 127.0.0.1:1883
availability probe     tcp_connect 127.0.0.1:1883
```

The checked-in lab configuration uses an anonymous listener. Treat that as isolated laboratory configuration, not a production security recommendation.

## 2. Adapt eligibility to your node

The checked-in catalog can contain environment-specific node or stage constraints. For this tutorial, make the eligible node explicit and avoid relying on stage labels when no authoritative node-to-stage mapping is available.

Conceptually:

```json
"target_nodes": ["tutorial-node"],
"target_stages": []
```

Do not change the logical `service_id` merely because the target machine changed.

## 3. Register the ServiceArtifact

```sh
curl -fsS -X POST \
  "$DSERVER_URL/api/v1/service-artifacts" \
  -H "X-Datum-Project: $PROJECT_ID" \
  -H 'content-type: application/json' \
  --data-binary @mosquitto.json \
  | tee registered-mosquitto.json
```

Registration means DServer now has the project-scoped operational descriptor. It does **not** start Docker and does not create placement authority.

## 4. Resolve immutable OCI identity when required

For a registry-backed image, DServer can resolve platform-specific OCI identity through:

```text
POST /api/v1/service-artifacts/mosquitto/image-identity/resolve
```

Example request body:

```json
{
  "target_platforms": [
    {"os": "linux", "architecture": "amd64"}
  ],
  "resolved_by": "tutorial-operator"
}
```

`resolved_by` is an audit/provenance label, not an authenticated identity.

The resolved identity is server-owned and becomes part of the execution-relevant artifact projection.

## 5. Model the logical service in a D-Graph

Create a D-Graph containing logical service `mqtt`:

```json
{
  "schema": "datum.dgraph/1",
  "application_id": "app:mqtt-tutorial",
  "dgraph_id": "dgraph:mqtt-tutorial",
  "revision": 1,
  "services": [
    {
      "service_id": "mqtt",
      "execution_requirement": {"dnode_abi": "datum-dnode/0"},
      "resource_requirement": {
        "cpu_cores": 1,
        "memory_bytes": 134217728
      }
    }
  ],
  "calls": []
}
```

Notice what is **not** in the D-Graph: Docker image, port 1883, configuration path and node ID. Those belong to other domains.

## 6. Ask D-Deploy to plan placement

```sh
curl -fsS -X POST \
  "$DSERVER_URL/api/v1/ddeploy/plan" \
  -H "X-Datum-Project: $PROJECT_ID" \
  -H 'content-type: application/json' \
  --data-binary @plan-request.json \
  | tee plan-response.json
```

The planner uses structural D-Continuum facts, current project commitments and ServiceArtifact eligibility to derive a **proposal**.

A proposal is not placement authority.

## 7. Review and explicitly accept

Capture proposal ID/digest and accept only after reviewing the candidate placement:

```sh
curl -fsS -X POST \
  "$DSERVER_URL/api/v1/ddeploy/proposals/$PROPOSAL_ID/accept" \
  -H "X-Datum-Project: $PROJECT_ID" \
  -H 'content-type: application/json' \
  --data-binary @accept-request.json \
  | tee acceptance.json
```

Now the materialized D-Map is placement authority.

Verify:

```sh
curl -fsS -G \
  "$DSERVER_URL/api/v1/ddeploy/active" \
  -H "X-Datum-Project: $PROJECT_ID" \
  --data-urlencode "application_id=app:mqtt-tutorial"
```

## 8. Inspect the node operational slice

For the accepted target node:

```text
GET /api/v1/nodes/:node_id/operational-dgraph-slice
```

The slice is derived from current authority. It tells the node which services are currently desired there; the node does not invent placement from local configuration.

## 9. Obtain finite reconciliation authorization

Real host mutation needs more than a D-Map. The node must also have the required operational resource binding and a finite authorization bound to the current graph/artifact snapshot.

Conceptual body:

```json
{
  "dgraph_id": "<current operational graph id>",
  "dgraph_revision": 1,
  "authorized_by": "tutorial-operator",
  "allow_host_mutation": true,
  "operation": "reconcile",
  "persistence_scope": "durable",
  "valid_for_seconds": 900
}
```

Submit to:

```text
POST /api/v1/nodes/:node_id/operational-reconciliation/authorize
```

Authorization can fail closed if resource binding, pinning completeness, persistence alignment or current authority no longer matches. Fix the prerequisite instead of weakening the contract.

## 10. Preview reconciliation

Run without `--execute` first:

```sh
cargo run --locked --manifest-path DATUM/Cargo.toml \
  --bin smartsentinel-operational-reconcile -- \
  --config DATUM/config.toml \
  --node-id "$NODE_ID" \
  --dserver-url "$DSERVER_URL" \
  --project-id "$PROJECT_ID" \
  --out mosquitto-preview.json
```

Review the report before allowing host mutation.

## 11. Execute

When the preview, authorization and local policy all match the intended action:

```sh
cargo run --locked --manifest-path DATUM/Cargo.toml \
  --bin smartsentinel-operational-reconcile -- \
  --config DATUM/config.toml \
  --node-id "$NODE_ID" \
  --dserver-url "$DSERVER_URL" \
  --project-id "$PROJECT_ID" \
  --execute \
  --out mosquitto-execution.json
```

The exact node-side outcome remains subject to current authorization, execution pinning and local prerequisites.

## 12. Verify physical realization

On the target node, operationally inspect the container:

```sh
docker ps --filter name=datum-mosquitto
```

and the listener/health contract appropriate to the environment.

This proves an operational runtime fact. It does not by itself make the application Ready.

## 13. Inspect evidence and readiness

Query canonical readiness separately:

```sh
curl -fsS \
  "$DSERVER_URL/api/v1/dmonitor/readiness/$PROJECT_ID/app:mqtt-tutorial"
```

A running container can still be NotReady if canonical evidence is missing, stale, unhealthy or correlated to obsolete authority.

## End-to-end mental model

```text
software modeled       ServiceArtifact
logical app modeled    D-Graph
placement candidate    D-Deploy proposal
placement authority    accepted D-Map
mutation permission    reconciliation authorization
physical reality       Docker container
observed reality       evidence/DMonitor
current usability      readiness
```

This separation is what the planned dashboard should visualize.

## Sources

See [Sources and provenance](../reference/sources.md) for the real Mosquitto artifact/configuration and current operational reconciliation source anchors.
