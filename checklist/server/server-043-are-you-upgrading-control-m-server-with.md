---
name: server-043-are-you-upgrading-control-m-server-with
type: checklist-item
component: server
section: "Important Control-M/Server Reminder"
answer_type: done
answer_options: ["Done", "Not Applicable"]
tsa_answer_options: ["Advised", "Not Applicable"]
blocking: false
related_rules: ["ha-distributed-upgrade-order"]
related_components: []
hcu_sources: ["[[Server-Artifact-SYSPRM-csv]]"]
extractors: [X06]
status: active
source_sheet: "AMIGO Server Checklist V22"
source_row: 43
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Are you upgrading Control-M/Server with high availability configuration?

## Question

Are you upgrading Control-M/Server with high availability configuration?

## Customer guidance

Refer to knowledge article 000386814 for the recommended upgrade steps for high availability configuration.

## TSA guidance

Discuss with customer the upgrade steps for Control-M/Server Secondary installation.

## Related

- Rule: [[ha-distributed-upgrade-order]]
