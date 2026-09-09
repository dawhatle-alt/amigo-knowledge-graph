---
name: agent-kdb-keystore-blocks-upgrade
type: rule
severity: blocking
applies_to: [agent]
target_version: "9.0.22"
maintained_by: hand
source_doc: "BMC Agent Upgrade doc + Agent 9.0.22.100 Release Notes (verified 2026-09)"
---

# KDB keystores block the agent upgrade

**Rule:** An SSL-mode agent using a **KDB keystore cannot upgrade to 9.0.22**. Deploy a **PKCS #12** keystore first. The upgrade attempts KDB→PKCS #12 conversion; if conversion fails the upgrade ABORTS.

## Skill behaviour
For every SSL agent, keystore type is a pre-wave gate. Unknown type = a collect item, never assumed.
