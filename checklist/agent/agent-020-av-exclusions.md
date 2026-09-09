---
name: agent-020-av-exclusions
type: checklist-item
component: agent
section: Environment
answer_type: yes_no
blocking: false
related_rules: []
related_components: []
hcu_sources: ["[[OS-Processes]]"]
extractors: [X27]
status: active
maintained_by: hand
source_doc: "BMC Agent Upgrade doc + Agent 9.0.22.100 Release Notes (verified 2026-09)"
---

# Are antivirus/monitoring exclusions configured on each agent host?

## Question

Are antivirus/monitoring exclusions configured on each agent host?

## Customer guidance

Exclude Control-M users, processes, ports, files and directories from scanning.

## TSA guidance

Detected products from HCU process lists seed this check.
