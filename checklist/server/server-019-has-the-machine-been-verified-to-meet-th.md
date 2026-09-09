---
name: server-019-has-the-machine-been-verified-to-meet-th
type: checklist-item
component: server
section: "Upgrading Control-M/Server Environment"
answer_type: yes-no
answer_options: ["Yes", "No"]
answer_options_alt: ["UNIX", "Linux", "Windows", "Done"]
answer_options_source_conflict: true
tsa_answer_options: ["Advised", "Not Applicable"]
blocking: false
related_rules: []
related_components: []
status: active
source_sheet: "AMIGO Server Checklist V22"
source_row: 19
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Has the machine been verified to meet the minimum requirement for the Control-M/Server installation?

## Question

Has the machine been verified to meet the minimum requirement for the Control-M/Server installation?

## Customer guidance

Recommended to perform the below:
Control-M Compatibility and Pre-requisite Verification are completed for the upgrading Control-M/Server
Refer to Control-M Installation Guide:
https://documents.bmc.com/supportu/9.0.22/en-US/Documentation/Control-M_full_installation.htm

## TSA guidance

Advised customer that it is the customer responsibility to ensure that the machine to be installed with the Control-M/EM meet the minimum requirement for the product.
Review the PAC and run the check_req script to check the OS and kernel requirement.
For SuSE12 Operating System only: Do Review if CTM-3454 is resolved
