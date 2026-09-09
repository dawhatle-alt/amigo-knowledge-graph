---
name: em-topology-ha
type: runbook-topology
component: em
topology: ha
target_version: 9.0.22
parent_phase: em-phase-4-control-m-enterprise-manager-upgrade
related_rules: ["ha-distributed-upgrade-order", "postgres-not-upgraded-in-place"]
source_sheet: "EM V22 Upgrade"
source_row: 40
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Control-M/Enterprise Manager upgrade sequence — High Availability

_For Control-M/Enterprise Manager configured with High Availability (Primary > Secondary)_

## Steps

1. Stop Control-M/Enterprise Manager Configuration Agent on the Secondary node.
2. Upgrade Primary Control-M/Enterprise Manager
3. Upgrade Secondary Control-M/Enterprise Manager
4. Verify Control-M/Enterprise Manager is running on Primary node
5. Start the Control-M/Enterprise Manager Configuration Agent on the Secondary node
6. Verify Control-M/Enterprise Manager configured with High Availability is connected

## Related

- Phase: [[em-phase-4-control-m-enterprise-manager-upgrade]]
- Rule: [[ha-distributed-upgrade-order]]
- Rule: [[postgres-not-upgraded-in-place]]
