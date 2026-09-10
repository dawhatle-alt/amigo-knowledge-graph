---
name: em-039-the-postgresql-database-server-is-not-up
type: checklist-item
component: em
section: "Control-M/Enterprise Manager Technical Concerns"
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
source_sheet: "AMIGO EM Checklist V22"
source_row: 39
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# The PostgreSQL database server is not upgraded during an in-place upgrade of Control-M/Enterprise Manager 9.0.22.

## Question

The PostgreSQL database server is not upgraded during an in-place upgrade of Control-M/Enterprise Manager 9.0.22.

## Customer guidance

1. PostgreSQL Database Server is not upgraded during In-place Upgrade
2. Recommend PostgreSQL Server upgrade, please review below documents:
https://documents.bmc.com/supportu/9.0.22/en-US/Documentation/Control-M_upgrade.htm

## TSA guidance

If you are using the BMC-provided PostgreSQL database, after you upgrade Control-M/EM or Control-M/Server, the PostgreSQL database server version remains the same and must be upgraded, as described in Control-M Upgrade.

## Related

- Rule: [[postgres-not-upgraded-in-place]]
