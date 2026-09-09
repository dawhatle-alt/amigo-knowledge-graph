---
name: em-044-do-you-have-automation-api-jobs-running
type: checklist-item
component: em
section: "Important Control-M/Enterprise Manager Reminder"
answer_type: yes-no
answer_options: ["Yes", "No"]
tsa_answer_options: ["Advised", "Not Applicable"]
blocking: true
related_rules: ["amigo-scope"]
related_components: ["aapi"]
status: active
source_sheet: "AMIGO EM Checklist V22"
source_row: 44
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Do you have Automation API jobs running on the Control-M/Agent?

## Question

Do you have Automation API jobs running on the Control-M/Agent?

## Customer guidance

AAPI CLI is no longer supported on following OSes:
Amazon Linux 2, SUSE Linux 12, Red Hat 7, Oracle Linux 7, CentOS 7
Please refer to knowledge article 000419428 for more details.

## TSA guidance

Advise customers to migrate the AAPI jobs to Control-M/Agents that run on OSes that support Node.js v18 or later.

## Related

- Rule: [[amigo-scope]]
- Component: [[aapi]]
