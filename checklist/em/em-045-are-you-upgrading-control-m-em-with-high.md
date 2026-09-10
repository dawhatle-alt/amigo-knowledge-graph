---
name: em-045-are-you-upgrading-control-m-em-with-high
type: checklist-item
component: em
section: "Important Control-M/Enterprise Manager Reminder"
answer_type: yes-no
answer_options: ["Yes", "No"]
tsa_answer_options: ["Advised", "Not Applicable"]
blocking: false
related_rules: ["ha-distributed-upgrade-order"]
related_components: []
hcu_sources: ["[[EM-ini]]"]
extractors: [X07]
status: active
source_sheet: "AMIGO EM Checklist V22"
source_row: 45
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Are you upgrading Control-M/EM with high availability or distributed configuration?

## Question

Are you upgrading Control-M/EM with high availability or distributed configuration?

## Customer guidance

Refer to knowledge article 000386814 for the recommended upgrade steps.
Please refer to below document for the High Availability requirement.
https://documents.bmc.com/supportu/9.0.22/en-US/Documentation/High_availability_installation.htm?Highlight=high%20availability#HighAvailabilityRequirements

## TSA guidance

Discuss the upgrade steps for HA Secondary and Distributed EM.

## Related

- Rule: [[ha-distributed-upgrade-order]]
