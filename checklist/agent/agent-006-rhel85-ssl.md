---
name: agent-006-rhel85-ssl
type: checklist-item
component: agent
section: SSL
answer_type: yes_no
blocking: false
related_rules: []
related_components: []
hcu_sources: ["[[Server-AG_TBL_CTM]]", "[[Server-CNF_INFO-SSL]]"]
extractors: [X25]
status: active
maintained_by: hand
source_doc: "BMC Agent Upgrade doc + Agent 9.0.22.100 Release Notes (verified 2026-09)"
---

# Are any agents on RHEL 8.5+ running in SSL mode?

## Question

Are any agents on RHEL 8.5+ running in SSL mode?

## Customer guidance

If yes, review KA 000419757 before the Server/agent upgrades.

## TSA guidance

Auto-flagged from the HCU fleet join when archives are provided.
