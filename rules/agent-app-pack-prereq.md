---
name: agent-app-pack-prereq
type: rule
severity: blocking
applies_to: [agent]
target_version: "9.0.22"
maintained_by: hand
source_doc: "BMC Agent Upgrade doc + Agent 9.0.22.100 Release Notes (verified 2026-09)"
---

# Application Pack prerequisite for agent 9.0.22

**Rule:** If Application Pack **9.0.21.000 or lower** is installed, upgrade AP to **9.0.21.100** or uninstall it BEFORE upgrading the agent to 9.0.22. All Application Integrator jobs must be COMPLETED first. CTM for Databases profiles require CTM-DB 9.0.21.100+ before AP moves. CAUTION: rolling the agent back breaks Application Integrator (App Pack uninstall + reinstall required).

## Skill behaviour
AP version is a pre-wave gate per agent; the rollback caveat appears in every agent runbook.
