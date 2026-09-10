---
name: server-039-are-the-control-m-agents-connecting-to-c
type: checklist-item
component: server
section: "Control-M/Server Technical Concerns"
answer_type: yes-no
answer_options: ["Yes", "No"]
tsa_answer_options: ["Advised", "Not Applicable"]
blocking: false
related_rules: []
related_components: []
hcu_sources: ["[[Server-AG_TBL_CTM]]", "[[Server-CNF_INFO-SSL]]"]
extractors: [X25]
status: active
source_sheet: "AMIGO Server Checklist V22"
source_row: 39
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Are the Control-M/Agents connecting to Control-M Server running on Red Hat 8.5 or higher and in SSL mode?

## Question

Are the Control-M/Agents connecting to Control-M Server running on Red Hat 8.5 or higher and in SSL mode?

## Customer guidance

If the answer is YES, please review knowledge article 000419757 before upgrading Control-M/Server to 9.0.21 or higher.
