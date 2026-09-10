---
name: server-036-are-you-using-control-m-server-ctmldnrs
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
extractors: [X16]
status: active
source_sheet: "AMIGO Server Checklist V22"
source_row: 36
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Are you using Control-M Server ctmldnrs.dat file?

## Question

Are you using Control-M Server ctmldnrs.dat file?

## Customer guidance

Control-M/Server ctmldnrs.dat files are saved to a new location upon upgrade to 9.0.21.100 and later, <Control-M/Server_home>/data.
Refer to below URL for more information on ctmldnrs utility.
https://documents.bmc.com/supportu/9.0.22/en-US/Documentation/Utilities/ctmldnrs.htm?Highlight=ctmldnrs

## TSA guidance

Control-M/Server ctmldnrs.dat files are saved to a new location upon 9.0.21.100 upgrade, <Control-M/Server_home>/data.
Explain to customer what is the ctmldnrs utility and how the ctmldnrs.dat is used, if customer is not familiar with the file.
