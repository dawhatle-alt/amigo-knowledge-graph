---
name: agent-016-windows-service-account
type: checklist-item
component: agent
section: Method
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

# For Windows agents with service Log on as 'This account': will the upgrade run AS that account?

## Question

For Windows agents with service Log on as 'This account': will the upgrade run AS that account?

## Customer guidance

The upgrade must be performed with the configured service account.

## TSA guidance

Capture the account per Windows agent.
