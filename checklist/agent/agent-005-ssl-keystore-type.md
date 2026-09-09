---
name: agent-005-ssl-keystore-type
type: checklist-item
component: agent
section: SSL
answer_type: yes_no
blocking: true
related_rules: ["[[agent-kdb-keystore-blocks-upgrade]]"]
related_components: []
hcu_sources: []
extractors: []
status: active
maintained_by: hand
source_doc: "BMC Agent Upgrade doc + Agent 9.0.22.100 Release Notes (verified 2026-09)"
---

# For SSL-mode agents: is the keystore PKCS #12 (not KDB)?

## Question

For SSL-mode agents: is the keystore PKCS #12 (not KDB)?

## Customer guidance

KDB keystores must be replaced with PKCS #12 before the upgrade.

## TSA guidance

Unknown keystore type = collect item, never assumed.
