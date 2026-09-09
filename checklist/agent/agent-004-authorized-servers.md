---
name: agent-004-authorized-servers
type: checklist-item
component: agent
section: "Version Gates"
answer_type: yes_no
blocking: true
related_rules: []
related_components: []
hcu_sources: ["[[Agent-Artifact-CONFIG-dat]]"]
extractors: [X24]
status: active
maintained_by: hand
source_doc: "BMC Agent Upgrade doc + Agent 9.0.22.100 Release Notes (verified 2026-09)"
---

# Is each agent connected to only ONE active Control-M/Server?

## Question

Is each agent connected to only ONE active Control-M/Server?

## Customer guidance

Check CCM → Agent → Properties → Authorized Servers (or CONFIG.dat CTMSHOST/CTMPERMHOSTS). Update per KA 000308365 if the host changes.

## TSA guidance

Multi-server agents are unsupported — resolve before any wave.
