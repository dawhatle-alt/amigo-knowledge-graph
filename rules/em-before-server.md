---
name: em-before-server
type: rule
severity: blocking
applies_to: [em, server]
maintained_by: hand
---

# EM is always upgraded before Server

**Rule:** Control-M/Enterprise Manager must be at the same or a higher version than any Control-M/Server it manages. Therefore the EM upgrade always completes before the Server upgrade starts.

## How the skill should apply it

- When both EM and Server are in scope, the generated plan sequences the entire EM runbook ([[runbook-em-index]]) before the Server runbook ([[runbook-server-index]]).
- If the customer wants to upgrade Server first, refuse the sequence and explain why.
- Agents are upgraded after Server ([[server-phase-4-control-m-server-upgrade]]).

## Sources

- [[server-021-is-the-control-m-enterprise-manager-of-t]]
