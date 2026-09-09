---
name: server-phase-4-control-m-server-upgrade
type: runbook-phase
component: server
phase_order: 4
phase_title: "Control-M/Server Upgrade"
target_version: 9.0.22
related_rules: ["postgres-not-upgraded-in-place"]
source_sheet: "Server V22 Upgrade"
source_row: 23
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Control-M/Server — Phase 4: Control-M/Server Upgrade

- [ ] Perform Control-M/Server Pre-Installation Procedures
    - Doc: Setting the Java Environment Variable (9.0.22)
    - Doc: Changing JRE Package (9.0.22)
- [ ] Set the BMC_INST_CTM_APIGTW_PORT environment variable to 8393
- [ ] Perform Control-M/Server Upgrade Procedures
    - Doc: Upgrading Control-M/Server on UNIX (9.0.22)
    - Doc: Upgrading Control-M/Server on Windows (9.0.22)
- [ ] Upgrade the PostgreSQL Database Server to 11.5
    - Doc: Upgrading the PostgreSQL Database Server (9.0.22)
    - Doc: Upgrading an External Oracle or MSSQL Database Server (9.0.22)
- [ ] Perform the upgrade of the Control-M/Agent as necessary
    - Doc: Upgrading Control-M/Agent on UNIX (9.0.22)
    - Doc: Upgrading Control-M/Agent on Windows (9.0.22)

## Topology-specific sequence

Load exactly one of these based on the customer's topology answer:

- [[server-topology-standalone]] — Standalone
- [[server-topology-ha]] — High Availability

## Related rules

- [[postgres-not-upgraded-in-place]]
