---
name: server-phase-1-actions-prior-to-the-control-m-serve
type: runbook-phase
component: server
phase_order: 1
phase_title: "Actions prior to the Control-M/Server pre-upgrade"
target_version: 9.0.22
related_rules: []
source_sheet: "Server V22 Upgrade"
source_row: 2
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Control-M/Server — Phase 1: Actions prior to the Control-M/Server pre-upgrade

- [ ] Review the Upgrade Requirements and Considerations of the new Control-M/Server
    - Doc: Upgrade Requirements and Considerations (9.0.22)
    - Doc: Review Upgrade Scenarios (9.0.22)
- [ ] Verify Control-M/Server System Requirement
    - Doc: Control-M/Server System Requirements (9.0.22)
- [ ] Ensure existing machine has met the requirement for the System, Operating System and Database requirement for new Control-M/Server
- [ ] Install the latest fixpack on the existing Control-M/Server 9.0.21
- [ ] Run the below utility on the existing Control-M/Server using Control-M/Server Administrator Account:  
      - ctmsetown -action list.  
      Does  the output show any entry with the NOTIMPL string?  
      Here's an example:  
      &ctmagent@FIELD          &bh3jbolpv05@FIELD     &P@FIELD           &NOTIMPL@LINE  
      If Yes (result with an entry with NOTIMPL), review KA 000354649.
- [ ] Verify Upgrade Readiness
