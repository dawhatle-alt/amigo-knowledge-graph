---
name: server-042-if-you-are-using-bmc-supplied-postgresql
type: checklist-item
component: server
section: "Important Control-M/Server Reminder"
answer_type: done
answer_options: ["Done", "Not Applicable"]
tsa_answer_options: ["Advised", "Not Applicable"]
blocking: false
related_rules: ["postgres-not-upgraded-in-place"]
related_components: []
hcu_sources: ["[[db-postgresql]]"]
extractors: [X05]
status: active
source_sheet: "AMIGO Server Checklist V22"
source_row: 42
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# If you are using BMC supplied PostgreSQL database 11.5, please upgrade the PostgreSQL database to 15.3 soon after Control-M Server upgrade.

## Question

If you are using BMC supplied PostgreSQL database 11.5, please upgrade the PostgreSQL database to 15.3 soon after Control-M Server upgrade.

## Customer guidance

Refer to documentation:
https://documents.bmc.com/supportu/9.0.22/en-US/Documentation/Control-M_upgrade.htm?Highlight=PostgreSQL#UpgradingthePostgreSQLDatabaseServer

## TSA guidance

PostgreSQL 11.5 may be not supported on 9.22.100, so recommends customer to upgrade the PostgreSQL 11.5 to 15.3 soon after Control-M server upgrade.

## Related

- Rule: [[postgres-not-upgraded-in-place]]
