---
name: server-topology-ha
type: runbook-topology
component: server
topology: ha
target_version: 9.0.22
parent_phase: server-phase-4-control-m-server-upgrade
related_rules: ["ha-distributed-upgrade-order", "postgres-not-upgraded-in-place"]
source_sheet: "Server V22 Upgrade"
source_row: 38
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Control-M/Server upgrade sequence — High Availability

> [!warning] Stale step — "Upgrade ... Postgres Database Server to 11.5" (known-issues #2)
> PostgreSQL is **not** upgraded during the in-place Control-M upgrade; for BMC-supplied PostgreSQL the target is **15.3** as a separate post-upgrade step. Rule [[postgres-not-upgraded-in-place]] overrides this source text.

_For Control-M/Server configured with High Availability (Primary > Secondary)_

## Steps

1. Stop Control-M/Server Configuration Agent on the Secondary node.
2. Upgrade Primary Control-M/Server — Upgrade dedicated Control-M/Server Postgres Database Server to 11.5, if applicable.
3. Upgrade Secondary Control-M/Server — Re-do the full replication from Primary if  Postgres Database Server is upgraded 11.5 for Primary Control-M Server
4. Verify Control-M/Server is running on Primary node
5. Start the Control-M/Server Configuration Agent on the Secondary node
6. Verify Control-M/Server configured with High Availability is connected

## Related

- Phase: [[server-phase-4-control-m-server-upgrade]]
- Rule: [[ha-distributed-upgrade-order]]
- Rule: [[postgres-not-upgraded-in-place]]
