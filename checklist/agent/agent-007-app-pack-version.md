---
name: agent-007-app-pack-version
type: checklist-item
component: agent
section: Plug-ins
answer_type: free_text
blocking: true
related_rules: ["[[agent-app-pack-prereq]]"]
related_components: []
hcu_sources: []
extractors: []
status: active
maintained_by: hand
source_doc: "BMC Agent Upgrade doc + Agent 9.0.22.100 Release Notes (verified 2026-09)"
---

# What Application Pack version is installed on each agent (if any)?

## Question

What Application Pack version is installed on each agent (if any)?

## Customer guidance

AP 9.0.21.000 or lower must go to 9.0.21.100 (or be uninstalled) before the agent upgrade.

## TSA guidance

Gate per agent; record versions in the wave plan.
