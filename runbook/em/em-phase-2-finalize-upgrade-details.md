---
name: em-phase-2-finalize-upgrade-details
type: runbook-phase
component: em
phase_order: 2
phase_title: "Finalize upgrade details"
target_version: 9.0.22
related_rules: ["ha-distributed-upgrade-order"]
source_sheet: "EM V22 Upgrade"
source_row: 13
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Control-M/Enterprise Manager — Phase 2: Finalize upgrade details

- [ ] Select the cutover date
- [ ] Determine the outage window.
- [ ] For  Control-M/Enterprise Manager Distributed architecture, all Control-M/Enterprise Manager Servers must be upgraded on the same outage window.
- [ ] Create the back-out plan
- [ ] Open an AMIGO Review issue with BMC Support and include the upgrade plan at least 2 weeks before the cutover date

## Related rules

- [[ha-distributed-upgrade-order]]
