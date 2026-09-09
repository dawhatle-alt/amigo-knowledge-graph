---
name: compatibility-mode-irreversible
type: rule
severity: blocking
applies_to: [em]
maintained_by: hand
---

# Compatibility Mode cannot be re-enabled once turned off

**Rule:** After upgrading Control-M/EM, the server runs in Compatibility Mode so older EM clients keep working. Turning Compatibility Mode **off is irreversible**.

## How the skill should apply it

- Ask whether ALL EM clients (GUI, CCM, Workload Automation client) will be upgraded before Compatibility Mode is disabled.
- Disabling Compatibility Mode is the **last** step of the EM runbook ([[em-phase-6-post-upgrade-tasks]]), never earlier.
- If any client stays on the old version, Compatibility Mode must stay on. Warn explicitly.

## Sources

- [[em-020-will-the-control-m-enterprise-manager-cl]]
- [[em-042-compatibility-mode-cannot-be-re-enabled]]
