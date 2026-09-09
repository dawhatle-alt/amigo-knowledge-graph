---
name: amigo-scope
type: rule
severity: blocking
applies_to: [em, server]
maintained_by: hand
---

# What AMIGO covers (and what needs a regular case)

**In scope:** in-place upgrades between supported Control-M versions, planned with the customer through an AMIGO Starter case ([[amigo-starter-case-procedure]]).

**Out of scope — open a regular Support case instead:**

- Source version is unsupported (below the supported floor — see [[direct-upgrade-requires-9020]])
- Fix-pack / patch-only installs
- Migration to a different machine, hostname change, or Data Center rename ([[em-025-are-you-upgrading-control-m-enterprise-m]], [[server-031-will-there-be-any-changes-to-t-he-contro]], [[server-032-is-there-a-change-or-rename-of-the-contr]])
- Control-M for z/OS — separate AMIGO case with the Mainframe team, KA 000318316 ([[em-028-are-you-upgrading-control-m-for-z-os]])
- LDAP / IdP / SSL configuration — new case AFTER the upgrade completes ([[em-022-do-you-plan-to-implement-ldap-for-authen]])
- Live technical help during the production cutover — new **Severity 1** case, never raise the AMIGO case itself to Sev 1 ([[em-050-open-a-new-case-if-you-need-technical-he]], [[server-045-open-a-new-severity-1-ticket-if-facing-a]])

## How the skill should apply it

Whenever an interview answer lands in the out-of-scope list, say so immediately, name the right case type, and continue the plan for the in-scope parts only.
