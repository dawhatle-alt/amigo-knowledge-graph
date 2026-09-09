---
name: em-topology-distributed
type: runbook-topology
component: em
topology: distributed
target_version: 9.0.22
parent_phase: em-phase-4-control-m-enterprise-manager-upgrade
related_rules: ["ha-distributed-upgrade-order", "postgres-not-upgraded-in-place"]
source_sheet: "EM V22 Upgrade"
source_row: 47
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Control-M/Enterprise Manager upgrade sequence — Distributed

_For Control-M/Enterprise Manager with Distributed (Primary > Distributed)_

> [!note] Note: If Control-M Workload Archiving is installed on Distributed node, it will be upgraded automatically)

## Steps

1. Stop Control-M/Enterprise Manager on Distributed node
2. Verify all Control-M/Enterprise Manager processes are down on Distributed node
3. Upgrade Primary Control-M/Enterprise Manager — Upgrade dedicated Control-M/Enterprise Manager Postgres Database Server to 11.5, if applicable.
4. Upgrade Distributed Control-M/Enterprise Manager — Upgrade dedicated Control-M/Enterprise Manager Postgres Database Server to 11.5, if applicable.
5. Verify Control-M/Enterprise Manager is running on Primary node
6. Start the Control-M/Enterprise Manager on Distributed node
7. Verify Control-M/Enterprise Manager with Distributed is running and connected to Primary Control-M/Enterprise Manager

## Related

- Phase: [[em-phase-4-control-m-enterprise-manager-upgrade]]
- Rule: [[ha-distributed-upgrade-order]]
- Rule: [[postgres-not-upgraded-in-place]]
