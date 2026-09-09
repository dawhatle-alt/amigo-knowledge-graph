---
name: agent-phase-1-wave-planning
type: runbook-phase
component: agent
maintained_by: hand
source_doc: "BMC Agent Upgrade doc + Agent 9.0.22.100 Release Notes (verified 2026-09)"
---

# Phase 1 — Wave planning

1. Freeze the fleet inventory (name, version, OS, SSL, plug-ins per agent)
2. Group into waves by criticality/OS; below-floor agents ([[agent-source-version-floor]]) get dedicated hop waves
3. Define per-wave job-hold windows and owners
4. Stage packages (centralized) or distribute media (local)
