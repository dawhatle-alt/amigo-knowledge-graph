---
name: agent-001-fleet-inventory
type: checklist-item
component: agent
section: "Fleet Inventory"
answer_type: free_text
blocking: false
related_rules: []
related_components: []
hcu_sources: ["[[Server-AG_TBL_CTM]]", "[[Server-Artifact-agent-availability]]"]
extractors: [X22, X23, X29]
status: active
maintained_by: hand
source_doc: "BMC Agent Upgrade doc + Agent 9.0.22.100 Release Notes (verified 2026-09)"
---

# What agents are in scope? (name, version, OS, architecture per agent)

## Question

What agents are in scope? (name, version, OS, architecture per agent)

## Customer guidance

Run `ctmgetcm -DISPLAY ALL` from the Server or export the CCM/Web agent list.

## TSA guidance

Cross-check against AGENT_DISCOVERY from the HCU archive when available.
