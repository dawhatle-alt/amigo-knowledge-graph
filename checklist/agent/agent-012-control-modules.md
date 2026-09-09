---
name: agent-012-control-modules
type: checklist-item
component: agent
section: Plug-ins
answer_type: free_text
blocking: false
related_rules: []
related_components: []
hcu_sources: []
extractors: [X28]
status: active
maintained_by: hand
source_doc: "BMC Agent Upgrade doc + Agent 9.0.22.100 Release Notes (verified 2026-09)"
---

# What Control Modules / plug-ins are installed on each agent, and are they compatible with the target agent version?

## Question

What Control Modules / plug-ins are installed on each agent, and are they compatible with the target agent version?

## Customer guidance

List via CCM → Agent → plug-ins or the `<agent_home>/cm/` directory.

## TSA guidance

CM compatibility drives per-wave verification steps.
