---
name: agent-014-disk-space
type: checklist-item
component: agent
section: Environment
answer_type: yes_no
blocking: false
related_rules: []
related_components: []
hcu_sources: ["[[OS-Disk]]"]
extractors: [X12]
status: active
maintained_by: hand
source_doc: "BMC Agent Upgrade doc + Agent 9.0.22.100 Release Notes (verified 2026-09)"
---

# Is there sufficient free disk space on each agent host?

## Question

Is there sufficient free disk space on each agent host?

## Customer guidance

Per the agent system requirements for the target version.

## TSA guidance

Snapshot from HCU partitions when available.
