---
name: server-024-run-the-below-control-m-server-utility-u
type: checklist-item
component: server
section: "Upgrading Control-M/Server Environment"
answer_type: yes-no
answer_options: ["Yes", "No"]
tsa_answer_options: ["Advised", "Not Applicable"]
blocking: false
related_rules: []
related_components: []
hcu_sources: []
extractors: [RUN-ctmsetown, GAP-ctmsetown]
status: active
source_sheet: "AMIGO Server Checklist V22"
source_row: 24
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Run the below Control-M/Server utility using Control-M/Server Administrator Account:

## Question

Run the below Control-M/Server utility using Control-M/Server Administrator Account:
- ctmsetown -action list.
Does  the output show any entry with the NOTIMPL string?
Here's an example:
&ctmagent@FIELD          &bh3jbolpv05@FIELD     &P@FIELD           &NOTIMPL@LINE

## Customer guidance

If Yes (result with an entry with NOTIMPL), review knowledge article 000354649.
Do indicate the SQL Result here

## TSA guidance

If Yes (result with an entry with NOTIMPL), Review KA 000354649 and discuss with customer.
