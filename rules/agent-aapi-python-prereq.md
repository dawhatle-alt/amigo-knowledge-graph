---
name: agent-aapi-python-prereq
type: rule
severity: blocking
applies_to: [agent]
target_version: "9.0.22"
maintained_by: hand
source_doc: "BMC Agent Upgrade doc + Agent 9.0.22.100 Release Notes (verified 2026-09)"
---

# Python prerequisite for agents using AAPI CLI

**Rule:** On agents where Automation API CLI is in use, **Python ≥ 3.8.4 and pip ≥ 20.1.1** are required or the agent upgrade **FAILS**. Without CLI, missing Python only warns. Related: AAPI CLI needs Node.js v18+ — RHEL7 / CentOS7 / OracleLinux7 / SUSE12 / AmazonLinux2 dropped (KA 000419428).

## Skill behaviour
`python3 --version && pip --version` is a run-command gate on every AAPI-CLI agent.
