---
name: em-topology-standalone
type: runbook-topology
component: em
topology: standalone
target_version: 9.0.22
parent_phase: em-phase-4-control-m-enterprise-manager-upgrade
related_rules: ["postgres-not-upgraded-in-place"]
source_sheet: "EM V22 Upgrade"
source_row: 37
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Control-M/Enterprise Manager upgrade sequence — Standalone

_For Standalone Control-M/Enterprise Manager_

## Steps

1. Upgrade Control-M/Enterprise Manager — Upgrade dedicated Control-M/Enterprise Manager Postgres Database Server to 11.5, if applicable.
2. Verify Control-M/Enterprise Manager is running

## Related

- Phase: [[em-phase-4-control-m-enterprise-manager-upgrade]]

- Rule: [[postgres-not-upgraded-in-place]]
