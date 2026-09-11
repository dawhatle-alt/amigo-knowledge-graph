---
name: server-topology-standalone
type: runbook-topology
component: server
topology: standalone
target_version: 9.0.22
parent_phase: server-phase-4-control-m-server-upgrade
related_rules: ["postgres-not-upgraded-in-place"]
source_sheet: "Server V22 Upgrade"
source_row: 35
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Control-M/Server upgrade sequence — Standalone

> [!warning] Stale step — "Upgrade ... Postgres Database Server to 11.5" (known-issues #2)
> PostgreSQL is **not** upgraded during the in-place Control-M upgrade; for BMC-supplied PostgreSQL the target is **15.3** as a separate post-upgrade step. Rule [[postgres-not-upgraded-in-place]] overrides this source text.

_For Standalone Control-M/Server_

## Steps

1. Upgrade Control-M/Server — Upgrade dedicated Control-M/Server Postgres Database Server to 11.5, if applicable.
2. Verify Control-M/Server is running

## Related

- Phase: [[server-phase-4-control-m-server-upgrade]]

- Rule: [[postgres-not-upgraded-in-place]]
