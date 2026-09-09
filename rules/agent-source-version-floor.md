---
name: agent-source-version-floor
type: rule
severity: blocking
applies_to: [agent]
target_version: "9.0.22"
maintained_by: hand
source_doc: "BMC Agent Upgrade doc + Agent 9.0.22.100 Release Notes (verified 2026-09)"
---

# Agent upgrade version floors

**Rule:** Agent to 9.0.22 requires source **9.0.20+**. Agent to **9.0.22.100** requires **9.0.21+** — agents at 9.0.20.200 or lower must step through 9.0.21–9.0.22 first. Agent version must never exceed its Server ([[em-before-server]] extends to EM ≥ Server ≥ Agent; Server upgrades before agents, always).

## Skill behaviour
Check every agent's version from the fleet inventory. Below-floor agents get an explicit intermediate hop in the wave plan.
