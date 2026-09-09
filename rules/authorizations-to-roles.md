---
name: authorizations-to-roles
type: rule
severity: warning
applies_to: [em]
target_version: 9.0.22
maintained_by: hand
---

# Authorizations are role-based from 9.0.22

**Rule:** From 9.0.22, Control-M authorizations are assigned to **roles only**; users must be members of roles. After the upgrade, review every user's authorizations and assign them to roles.

Post-upgrade EM task; see the "Authorizations" section under Upgrade Requirements and Considerations.

## Sources

- [[em-048-assign-all-user-authorizations-to-roles]]
