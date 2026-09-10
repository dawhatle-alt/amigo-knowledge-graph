---
name: server-041-do-you-have-more-than-one-control-m-serv
type: checklist-item
component: server
section: "Important Control-M/Server Reminder"
answer_type: yes-no
answer_options: ["Yes", "No"]
answer_options_alt: ["Done", "Not Applicable"]
answer_options_source_conflict: true
tsa_answer_options: ["Advised", "Not Applicable"]
blocking: false
related_rules: []
related_components: []
hcu_sources: ["[[Server-CNF_INFO]]", "[[OS-Processes]]"]
extractors: [X09]
status: active
source_sheet: "AMIGO Server Checklist V22"
source_row: 41
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Do you have more than one Control-M/Server on this server?

## Question

Do you have more than one Control-M/Server on this server?

## Customer guidance

Review knowledge article 000406529 for the proposed solution for CTM-7845 - new day does not order any job when having more than one Control-M/Server in same box.

## TSA guidance

Provide and review KA 000406529 with customer toresolve this CAR
CTM-7845 - Successful upgrade/install of 9.0.21 when multiple instances of the CTM Server exist in same box
