---
name: agent-phase-2-pre-wave-gates
type: runbook-phase
component: agent
maintained_by: hand
source_doc: "BMC Agent Upgrade doc + Agent 9.0.22.100 Release Notes (verified 2026-09)"
---

# Phase 2 — Pre-wave gates (per wave)

All BLOCKING before the wave starts:
1. Server already at target version ([[em-before-server]])
2. Keystores PKCS #12 on SSL agents ([[agent-kdb-keystore-blocks-upgrade]])
3. App Pack ≥ 9.0.21.100 or removed; AI jobs completed ([[agent-app-pack-prereq]])
4. Python/pip present on AAPI-CLI agents ([[agent-aapi-python-prereq]])
5. Backups of agent directories taken
6. Jobs on wave agents HELD / drained
