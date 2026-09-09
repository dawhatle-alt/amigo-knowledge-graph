---
name: agent-phase-4-verification-and-release
type: runbook-phase
component: agent
maintained_by: hand
source_doc: "BMC Agent Upgrade doc + Agent 9.0.22.100 Release Notes (verified 2026-09)"
---

# Phase 4 — Verification & release (per wave)

1. `ctmgetcm -DISPLAY ALL` — every wave agent AVAILABLE at target version
2. Test job per agent; sysout retrieval verified
3. One test job per CM/plug-in where feasible
4. Release held jobs; watch first cycles
5. Apply latest agent patch (docs.bmc.com → 9.0.22 Patches)
Rollback: agent downgrade is supported BUT breaks Application Integrator ([[agent-app-pack-prereq]]).
