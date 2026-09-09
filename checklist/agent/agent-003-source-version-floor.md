---
name: agent-003-source-version-floor
type: checklist-item
component: agent
section: "Version Gates"
answer_type: yes_no
blocking: true
related_rules: ["[[agent-source-version-floor]]"]
related_components: []
hcu_sources: ["[[Server-AG_TBL_CTM]]"]
extractors: [X22, X29]
status: active
maintained_by: hand
source_doc: "BMC Agent Upgrade doc + Agent 9.0.22.100 Release Notes (verified 2026-09)"
---

# Is every in-scope agent at version 9.0.20 or higher (9.0.21+ for a 9.0.22.100 target)?

## Question

Is every in-scope agent at version 9.0.20 or higher (9.0.21+ for a 9.0.22.100 target)?

## Customer guidance

Agents below the floor need an intermediate hop before the target version.

## TSA guidance

Below-floor agents get their own wave with the intermediate hop.
