---
name: em-topology-distributed-ha
type: runbook-topology
component: em
topology: distributed-ha
target_version: 9.0.22
parent_phase: em-phase-4-control-m-enterprise-manager-upgrade
related_rules: ["ha-distributed-upgrade-order", "postgres-not-upgraded-in-place"]
source_sheet: "EM V22 Upgrade"
source_row: 55
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Control-M/Enterprise Manager upgrade sequence — Distributed + High Availability

_For Control-M/Enterprise Manager with Distributed configured with High Availability  (Primary > Distributed > Secondary)_

## Steps

1. Stop Control-M/Enterprise Manager on Distributed node
2. Stop Control-M/Enterprise Manager Configuration Agent on the Secondary node.
3. Upgrade Primary Control-M/Enterprise Manager
4. Upgrade Distributed Control-M/Enterprise Manager
5. Upgrade Secondary Control-M/Enterprise Manager
6. Verify Control-M/Enterprise Manager is running on Primary node
7. Start the Control-M/Enterprise Manager on Distributed node
8. Verify Control-M/Enterprise Manager with Distributed is running and connected to Primary Control-M/Enterprise Manager
9. Start the Control-M/Enterprise Manager Configuration Agent on the Secondary node
10. Verify Control-M/Enterprise Manager configured with High Availability is connected.

## Related

- Phase: [[em-phase-4-control-m-enterprise-manager-upgrade]]
- Rule: [[ha-distributed-upgrade-order]]
- Rule: [[postgres-not-upgraded-in-place]]
