---
name: server-030-is-the-control-m-server-installed-on-nfs
type: checklist-item
component: server
section: "Control-M/Server Technical Concerns"
answer_type: yes-no
answer_options: ["Yes", "No"]
tsa_answer_options: ["Advised", "Not Applicable"]
blocking: false
related_rules: []
related_components: []
status: active
source_sheet: "AMIGO Server Checklist V22"
source_row: 30
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Is the Control-M/Server installed on NFS or VXFS file system?

## Question

Is the Control-M/Server installed on NFS or VXFS file system?

## Customer guidance

If Control-M/Server is installed on the NFS or VXFS file system, the Control-M Modules will not be supported on local Control-M/Agent. Control-M Module is not supported on NFS or VXFS file system.

## TSA guidance

Control-M/Agent installed on NFS or VXFS do not support using any Control-M module (SAP, Database, Peoplesoft etc). Remind customer to open new case if they have any questions for the Control-M Control Module
