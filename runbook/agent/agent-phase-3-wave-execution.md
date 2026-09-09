---
name: agent-phase-3-wave-execution
type: runbook-phase
component: agent
maintained_by: hand
source_doc: "BMC Agent Upgrade doc + Agent 9.0.22.100 Release Notes (verified 2026-09)"
---

# Phase 3 — Wave execution

Per agent in the wave: stop agent → upgrade (per method note) → start agent.
Windows service 'This account' agents: run AS the service account.
On failure: capture installer log; do not proceed to the next agent in the group until triaged; production impact → NEW Severity 1 case.
