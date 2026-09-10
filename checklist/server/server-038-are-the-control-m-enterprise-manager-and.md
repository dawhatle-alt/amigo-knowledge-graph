---
name: server-038-are-the-control-m-enterprise-manager-and
type: checklist-item
component: server
section: "Control-M/Server Technical Concerns"
answer_type: yes-no
answer_options: ["Yes", "No"]
tsa_answer_options: ["Advised", "Not Applicable"]
blocking: false
related_rules: []
related_components: []
hcu_sources: ["[[OS-Network]]"]
extractors: [X08]
status: active
source_sheet: "AMIGO Server Checklist V22"
source_row: 38
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Are the Control-M/Enterprise Manager and Control-M/Server using different user accounts on UNIX/Linux?

## Question

Are the Control-M/Enterprise Manager and Control-M/Server using different user accounts on UNIX/Linux?

## Customer guidance

Reviewknowledge article 000374213 for CTM-5074 - MS - Kafka services fail to start when failover to Secondary EM.
The kafka and zookeeper micro services ports should be different for Enterprise Manager and Control-M Server installation on Unix/Linux.

## TSA guidance

If EM and Server exist on the same Unix/Linux host, and it is not a one installation, review KA 000374213 to ensure kafka and zookeeper are using different ports for EM and Server.
