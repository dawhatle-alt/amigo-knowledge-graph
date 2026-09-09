---
name: agent-010-aapi-python
type: checklist-item
component: agent
section: "Automation API"
answer_type: yes_no
blocking: true
related_rules: ["[[agent-aapi-python-prereq]]"]
related_components: []
hcu_sources: []
extractors: []
status: active
maintained_by: hand
source_doc: "BMC Agent Upgrade doc + Agent 9.0.22.100 Release Notes (verified 2026-09)"
---

# On agents using Automation API CLI: are Python ≥ 3.8.4 and pip ≥ 20.1.1 installed?

## Question

On agents using Automation API CLI: are Python ≥ 3.8.4 and pip ≥ 20.1.1 installed?

## Customer guidance

Run `python3 --version` and `pip --version` on each such agent — the upgrade fails without them.

## TSA guidance

Run-command gate; capture outputs.
