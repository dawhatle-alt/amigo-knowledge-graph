---
name: server-022-are-there-any-control-modules-for-the-co
type: checklist-item
component: server
section: "Upgrading Control-M/Server Environment"
answer_type: yes-no
answer_options: ["Yes", "No"]
tsa_answer_options: ["Advised", "Not Applicable"]
blocking: true
related_rules: ["amigo-scope"]
related_components: []
hcu_sources: []
extractors: [X28, GAP-cm-inventory]
status: active
source_sheet: "AMIGO Server Checklist V22"
source_row: 22
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Are there any Control Modules for the Control-M/Server’s local agent that need to be installed?

## Question

Are there any Control Modules for the Control-M/Server’s local agent that need to be installed?

## Customer guidance

Control Module are not part of the Control-M/Server in-place upgrade, do open a case for the Control-M/Agent to be migrated which required to copy the accounts to the new Control-M/Agent

## TSA guidance

Explain that Control-M Module are not upgraded during the in-place upgrade.
Advise customer to open a new case for CM upgrading for further assistance

## Related

- Rule: [[amigo-scope]]
