---
name: agent-008-ctm-databases
type: checklist-item
component: agent
section: Plug-ins
answer_type: yes_no
blocking: false
related_rules: ["[[agent-app-pack-prereq]]"]
related_components: []
hcu_sources: []
extractors: []
status: active
maintained_by: hand
source_doc: "BMC Agent Upgrade doc + Agent 9.0.22.100 Release Notes (verified 2026-09)"
---

# Do any agents have Control-M for Databases connection profiles?

## Question

Do any agents have Control-M for Databases connection profiles?

## Customer guidance

CTM for Databases must reach 9.0.21.100+ before Application Pack can be upgraded.

## TSA guidance

Dependency-chain check before the AP prerequisite.
