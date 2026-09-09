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

_For Standalone Control-M/Server_

## Steps

1. Upgrade Control-M/Server — Upgrade dedicated Control-M/Server Postgres Database Server to 11.5, if applicable.
2. Verify Control-M/Server is running

## Related

- Phase: [[server-phase-4-control-m-server-upgrade]]

- Rule: [[postgres-not-upgraded-in-place]]
