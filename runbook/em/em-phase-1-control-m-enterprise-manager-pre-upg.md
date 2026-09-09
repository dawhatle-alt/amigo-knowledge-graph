---
name: em-phase-1-control-m-enterprise-manager-pre-upg
type: runbook-phase
component: em
phase_order: 1
phase_title: "Control-M/Enterprise Manager pre-upgrade"
target_version: 9.0.22
related_rules: []
source_sheet: "EM V22 Upgrade"
source_row: 2
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Control-M/Enterprise Manager — Phase 1: Control-M/Enterprise Manager pre-upgrade

- [ ] Review the Upgrade Requirement and Considerations of the new Control-M/Enterprise Manager 9.0.22
    - Doc: Upgrade Requirements and Considerations (9.0.22)
    - Doc: Review Upgrade Scenarios (9.0.22)
    - Doc: Review Compatbility Mode (9.0.22)
- [ ] Verify Control-M/Enterprise Manager System Requirements
    - Doc: Control-M/EM System Requirements (9.0.22)
- [ ] Ensure existing Control-M/Enterprise Manager machine has met the requirement for the System, Operating System and Database requirement.
- [ ] Install the latest fixpack on the existing Control-M/Enterprise Manager 9.0.22 ( If applicable)
- [ ] Run the below utility on the existing Control-M/Enterprise Manager using Control-M/Enterprise Manager Administrator Account:  
      - ctmsetown -action list.  
      Does  the output show any entry with the NOTIMPL string?  
      Here's an example:  
      &ctmagent@FIELD          &bh3jbolpv05@FIELD     &P@FIELD           &NOTIMPL@LINE  
      If Yes (result with an entry with NOTIMPL), review KA 000354649.
- [ ] Verifying Upgrade Readiness
