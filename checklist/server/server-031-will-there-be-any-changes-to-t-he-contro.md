---
name: server-031-will-there-be-any-changes-to-t-he-contro
type: checklist-item
component: server
section: "Control-M/Server Technical Concerns"
answer_type: yes-no
answer_options: ["Yes", "No"]
tsa_answer_options: ["Advised", "Not Applicable"]
blocking: false
related_rules: ["authorizations-to-roles"]
related_components: []
hcu_sources: []
extractors: []
status: active
source_sheet: "AMIGO Server Checklist V22"
source_row: 31
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Will there be any changes to t he Control-M/Server hostname?

## Question

Will there be any changes to t he Control-M/Server hostname?

## Customer guidance

To update the new Control-M/Server “Authorized server host” in the Control-M/Agent’s configuration, it is recommended to export the Control-M/Server while it is running and add the new one when it prompts for the hostname. Do review knowledge article 000308365.

## TSA guidance

Remind customer to answer "Y"  to add the new Control-M/Server as the "Authorised Server" on the Control-M/Agent:
 Do you want to add the destination environment name to the authorized Server for those agents?<YES/NO>

## Related

- Rule: [[authorizations-to-roles]]
