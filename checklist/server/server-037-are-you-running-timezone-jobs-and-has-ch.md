---
name: server-037-are-you-running-timezone-jobs-and-has-ch
type: checklist-item
component: server
section: "Control-M/Server Technical Concerns"
answer_type: yes-no
answer_options: ["Yes", "No"]
tsa_answer_options: ["Advised", "Not Applicable"]
blocking: false
related_rules: []
related_components: []
hcu_sources: ["[[Server-CNF_INFO]]"]
extractors: [X15]
status: active
source_sheet: "AMIGO Server Checklist V22"
source_row: 37
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Are you running timezone jobs and has changed the CTM_GD_FORWARD parameter in CCM, or edited GD_FORWARD parameter in Control-M/Server's config.dat file?

## Question

Are you running timezone jobs and has changed the CTM_GD_FORWARD parameter in CCM, or edited GD_FORWARD parameter in Control-M/Server's config.dat file?

## Customer guidance

From Control-M 9.0.21, forward ordering functionality cannot be disabled when Folder Timezone is specified.
Review knowledge article 000267902 for more information.

## TSA guidance

GD_FORWARD is depecated in version 9.0.21 and by default will forward order TZ jobs.
If customer has GD_FORWARD=N defined on earlier version, please advise customer to remove the timezone selection from the job definition to avoid forward ordering of the TZ jobs.
