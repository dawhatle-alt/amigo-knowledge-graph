---
name: agent-002-os-supported
type: checklist-item
component: agent
section: "Fleet Inventory"
answer_type: yes_no
blocking: false
related_rules: []
related_components: []
hcu_sources: []
extractors: []
status: active
maintained_by: hand
source_doc: "BMC Agent Upgrade doc + Agent 9.0.22.100 Release Notes (verified 2026-09)"
---

# Is each agent's operating system supported for the target version?

## Question

Is each agent's operating system supported for the target version?

## Customer guidance

Check the PAC tool / Agent compatibility list. AIX end of support is planned for end of 2026 — plan AIX agents accordingly.

## TSA guidance

Flag any OS on the dropped list early.
