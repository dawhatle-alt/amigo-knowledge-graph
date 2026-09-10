---
name: em-020-will-the-control-m-enterprise-manager-cl
type: checklist-item
component: em
section: "Upgrading Control-M/Enterprise Manager Environment"
answer_type: yes-no
answer_options: ["Yes", "No"]
answer_options_alt: ["Fixpack 1", "Fixpack 2", "Fixpack 3", "Fixpack 4", "Fixpack 5"]
answer_options_source_conflict: true
tsa_answer_options: ["Advised", "Not Applicable"]
blocking: false
related_rules: ["compatibility-mode-irreversible"]
related_components: []
hcu_sources: []
extractors: [GAP-em-clients]
status: active
source_sheet: "AMIGO EM Checklist V22"
source_row: 20
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Will the Control-M/Enterprise Manager clients be upgraded as well?

## Question

Will the Control-M/Enterprise Manager clients be upgraded as well?

## Customer guidance

Control-M/Enterprise Manager Server will be running in Compatibility Mode until all Control-M/Enteprise Manager Client are upgraded.

## TSA guidance

Discuss Control-M/Enteprise Manager Compatibility Mode with customer

## Related

- Rule: [[compatibility-mode-irreversible]]
