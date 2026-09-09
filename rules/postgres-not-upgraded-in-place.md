---
name: postgres-not-upgraded-in-place
type: rule
severity: warning
applies_to: [em, server]
maintained_by: hand
---

# PostgreSQL is not upgraded during an in-place Control-M upgrade

**Rule:** An in-place upgrade of Control-M/EM or Control-M/Server does **not** upgrade the BMC-supplied PostgreSQL database server. It is a separate step performed after the Control-M upgrade.

## Version caution

- The checklist (rows [[em-046-if-you-are-using-bmc-supplied-postgresql]], [[server-042-if-you-are-using-bmc-supplied-postgresql]]) says customers on PostgreSQL **11.5** should upgrade to **15.3** after moving to 9.0.22; 11.5 may not be supported on 9.0.22.100.
- The sample upgrade plan sheets still say "upgrade to 11.5" in the topology steps — that text is **stale**. Treat 15.3 as the target when the customer is on the BMC-supplied PostgreSQL; verify against the current BMC compatibility matrix if unsure.

## How the skill should apply it

- Ask which database the customer uses ([[em-013-what-is-the-database-server-connected-to]] / [[server-013-what-is-the-database-server-connected-to]]).
- If BMC-supplied PostgreSQL (dedicated): add the PostgreSQL upgrade as a post-upgrade step and, for HA, remind that replication must be redone from Primary after the DB upgrade ([[server-topology-ha]]).
- If external Oracle/MSSQL or existing PostgreSQL: point to the "Upgrading an External ... Database Server" doc instead.

## Sources

- [[em-039-the-postgresql-database-server-is-not-up]]
- [[server-029-postgres-database-server-is-not-upgraded]]
