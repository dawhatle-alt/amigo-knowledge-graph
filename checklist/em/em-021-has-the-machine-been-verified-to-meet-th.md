---
name: em-021-has-the-machine-been-verified-to-meet-th
type: checklist-item
component: em
section: "Upgrading Control-M/Enterprise Manager Environment"
answer_type: yes-no
answer_options: ["Yes", "No"]
answer_options_alt: ["UNIX", "Linux", "Windows", "Done"]
answer_options_source_conflict: true
tsa_answer_options: ["Advised", "Not Applicable"]
blocking: false
related_rules: []
related_components: []
hcu_sources: []
extractors: [RUN-check_req]
status: active
source_sheet: "AMIGO EM Checklist V22"
source_row: 21
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Has the machine been verified to meet the minimum requirements for the Control-M/Enterprise Manager installation?

## Question

Has the machine been verified to meet the minimum requirements for the Control-M/Enterprise Manager installation?

## Customer guidance

Recommended to perform the below:
Control-M Compatibility and Pre-requisite Verification are completed for the upgrading Control-M/Enterprise Manager
 Refer to Control-M Installation Guide:
https://documents.bmc.com/supportu/9.0.22/en-US/Documentation/Introduction_to_Control-M_Installation.htm

## TSA guidance

Advised customer that it is the customer responsibility to ensure that the machine to be installed with the Control-M/EM meet the minimum requirement for the product.
Review the PAC and run the check_req script to check the OS and kernel requirement.
For SuSE12 Operating System only: Do Review if CTM-3454 is resolved
