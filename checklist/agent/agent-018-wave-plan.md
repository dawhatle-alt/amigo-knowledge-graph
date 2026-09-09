---
name: agent-018-wave-plan
type: checklist-item
component: agent
section: Waves
answer_type: free_text
blocking: false
related_rules: ["[[agent-source-version-floor]]"]
related_components: []
hcu_sources: []
extractors: []
status: active
maintained_by: hand
source_doc: "BMC Agent Upgrade doc + Agent 9.0.22.100 Release Notes (verified 2026-09)"
---

# What is the wave plan? (groups, order, job-hold windows per wave)

## Question

What is the wave plan? (groups, order, job-hold windows per wave)

## Customer guidance

Group agents by criticality/OS; per wave: hold jobs → upgrade → verify → release. Compatible older agents keep working until their wave.

## TSA guidance

Server first, then waves; below-floor agents in dedicated hop waves.
