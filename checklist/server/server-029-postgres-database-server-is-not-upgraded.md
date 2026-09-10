---
name: server-029-postgres-database-server-is-not-upgraded
type: checklist-item
component: server
section: "Control-M/Server Technical Concerns"
answer_type: done
answer_options: ["Done"]
answer_options_alt: ["In-place", "Migration", "Yes", "No"]
answer_options_source_conflict: true
tsa_answer_options: ["Advised", "Not Applicable"]
blocking: false
related_rules: ["postgres-not-upgraded-in-place"]
related_components: []
hcu_sources: ["[[db-postgresql]]"]
extractors: [X05]
status: active
source_sheet: "AMIGO Server Checklist V22"
source_row: 29
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Postgres Database Server is NOT Upgraded during the In-place Upgrade of Control-M/Server.

## Question

Postgres Database Server is NOT Upgraded during the In-place Upgrade of Control-M/Server.
PostgreSQL Database must be on version 11 or higher for upgrading to Control-M/Server version 9.0.22.

## Customer guidance

1. PostgreSQL Database Server is not upgraded during In-place Upgrade
2. Recommend PostgreSQL Server upgrade, please review below documents:
9.0.22.000 : https://documents.bmc.com/supportu/9.0.22/en-US/Documentation/Control-M_upgrade.htm#UpgradingthePostgreSQLDatabaseServer

## Related

- Rule: [[postgres-not-upgraded-in-place]]
