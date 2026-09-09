---
name: em-048-assign-all-user-authorizations-to-roles
type: checklist-item
component: em
section: "Important Control-M/Enterprise Manager Reminder"
answer_type: applicable
answer_options: ["Applicable", "Not Applicable"]
answer_options_alt: ["Yes", "No"]
answer_options_source_conflict: true
tsa_answer_options: ["Advised", "Not Applicable"]
blocking: false
related_rules: ["authorizations-to-roles"]
related_components: []
status: active
source_sheet: "AMIGO EM Checklist V22"
source_row: 48
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Assign all user authorizations to roles after upgrading to 9.0.22.

## Question

Assign all user authorizations to roles after upgrading to 9.0.22.

## Customer guidance

Refer to Auhtorizations under Upgrade Requirements and Considerations:
https://documents.bmc.com/supportu/9.0.22/en-US/Documentation/Control-M_upgrade.htm#UpgradeRequirementsandConsiderations

## TSA guidance

Control-M authorizations are assigned to roles only, and user access is set only when the user is associated to a role.

## Related

- Rule: [[authorizations-to-roles]]
