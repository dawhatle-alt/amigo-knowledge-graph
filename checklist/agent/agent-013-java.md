---
name: agent-013-java
type: checklist-item
component: agent
section: Environment
answer_type: yes_no
blocking: false
related_rules: []
related_components: []
hcu_sources: ["[[OS-Java]]"]
extractors: []
status: active
maintained_by: hand
source_doc: "BMC Agent Upgrade doc + Agent 9.0.22.100 Release Notes (verified 2026-09)"
---

# Is a supported Java available on each agent host?

## Question

Is a supported Java available on each agent host?

## Customer guidance

External Java applies product-wide in 9.0.22 — verify per KA 000401084.

## TSA guidance

Auto-checkable from OS/Java when agent archives are collected.
