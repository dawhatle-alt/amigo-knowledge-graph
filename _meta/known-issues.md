---
name: known-issues
type: meta
---

# Known issues in source content

| # | Where | Issue | Status |
|---|---|---|---|
| 1 | EM checklist row 43 | Prose says floor is 9.0.19; dropdown and domain rule say 9.0.20 | Superseded by [[direct-upgrade-requires-9020]] |
| 2 | EM/Server sample-plan topology steps | "Upgrade Postgres to 11.5" is stale; checklist says 15.3 | Documented in [[postgres-not-upgraded-in-place]] |
| 3 | Server V22 Upgrade sheet title | Says "9.0.21.100 Sample Upgrade Plan" | Cosmetic; ignored |
| 4 | EM checklist rows 18, 19, 21 | Two conflicting dropdowns on the same cells (Yes/No and UNIX/Linux/Windows) | Both captured; `answer_options_source_conflict: true` |
| 5 | EM row 23 / Server row 20 | Job-count buckets duplicated with different spacing | Harmless |
| 6 | Server V22 Upgrade row 44 | Duplicate of row 43 | Dropped by converter |
| 7 | Vault | No 9.0.20.200 runbook for hop 1 of [[path-9019-to-9022]] | **Open — needs authoring** |
