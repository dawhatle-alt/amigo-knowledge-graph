---
name: server-021-is-the-control-m-enterprise-manager-of-t
type: checklist-item
component: server
section: "Upgrading Control-M/Server Environment"
answer_type: yes-no
answer_options: ["Yes", "No"]
tsa_answer_options: ["Advised", "Not Applicable"]
blocking: true
related_rules: ["compatibility-mode-irreversible", "em-before-server"]
related_components: []
status: active
source_sheet: "AMIGO Server Checklist V22"
source_row: 21
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Is the Control-M/Enterprise Manager of the same or higher version to the upgrading Control-M/Server?

## Question

Is the Control-M/Enterprise Manager of the same or higher version to the upgrading Control-M/Server?

## Customer guidance

If No, Control-M/Server will be running in Compatibility Mode with all the new feature being disabled.
The Compaitbility Mode will be disable only when  the Control-M/Enterprise Manager is on same or higher version then the Control-M/Server.

## TSA guidance

Explain that the new features will be available only after disabling compatibility mode.

## Related

- Rule: [[compatibility-mode-irreversible]]
- Rule: [[em-before-server]]
