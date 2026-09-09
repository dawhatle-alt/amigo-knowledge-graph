---
name: em-043-control-m-enteprrise-manager-must-be-at
type: checklist-item
component: em
section: "Important Control-M/Enterprise Manager Reminder"
answer_type: applicable
answer_options: ["Applicable", "Not Applicable"]
tsa_answer_options: ["Advised", "Not Applicable"]
blocking: true
related_rules: ["direct-upgrade-requires-9020"]
related_components: []
status: superseded
superseded_by: direct-upgrade-requires-9020
source_sheet: "AMIGO EM Checklist V22"
source_row: 43
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Control-M/Enteprrise Manager must be at least 9.0.19 to upgrade directly to 9.0.22.

> [!warning] Superseded — see [[direct-upgrade-requires-9020]]
> Source text says 'at least 9.0.19'. This contradicts the FROM-version dropdown on row 11 (9.0.20, 9.0.21 only) and the AMIGO domain rule. The rule note is authoritative.

## Question

Control-M/Enteprrise Manager must be at least 9.0.19 to upgrade directly to 9.0.22.

## Customer guidance

Control-M/Enteprrise Manager must be at least 9.0.19 to upgrade directly to 9.0.22
Refer to documentation:
Control-M Upgrade
https://documents.bmc.com/supportu/9.0.22/en-US/Documentation/Control-M_upgrade.htm

## TSA guidance

BMC Product Compaitbility
https://docs.bmc.com/docs/display/compatibility/Compatibility+matrix
Control-M 9.0.22 Documentation:
https://documents.bmc.com/supportu/9.0.22/en-US/Documentation/Control-M_upgrade.htm

## Related

- Rule: [[direct-upgrade-requires-9020]]
