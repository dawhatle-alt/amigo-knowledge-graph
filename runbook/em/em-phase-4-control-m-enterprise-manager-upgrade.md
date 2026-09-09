---
name: em-phase-4-control-m-enterprise-manager-upgrade
type: runbook-phase
component: em
phase_order: 4
phase_title: "Control-M/Enterprise Manager Upgrade"
target_version: 9.0.22
related_rules: ["postgres-not-upgraded-in-place"]
source_sheet: "EM V22 Upgrade"
source_row: 25
source_file: AMIGO_Checklist_V22_20251030.xlsx
---

# Control-M/Enterprise Manager — Phase 4: Control-M/Enterprise Manager Upgrade

- [ ] Verify all scheduling tables are in sync between Control-M/Enterprise Manager and Control-M/Server.
- [ ] Perform Control-M/Enterprise Manager Pre-Installation Procedures On Unix
    - Doc: Setting the Java Environment Variable (9.0.22)
    - Doc: Changing JRE Package (9.0.22)
- [ ] Perform Control-M/Enterprise Manager Upgrade Procedures
    - Doc: Upgrading Control-M/EM on UNIX (9.0.22)
    - Doc: Upgrading Control-M/EM on Windows (9.0.22)
- [ ] Upgrade the PostgreSQL Database Server
    - Doc: Upgrading the PostgreSQL Database Server (9.0.22)
    - Doc: Upgrading an External Oracle or MSSQL Database Server (9.0.22)
- [ ] Launch Control-M Configuration Manager (CCM) and ensure that all Control-M/Enterprise Manager components are defined with the correct hostname, ports and definitions.
- [ ] Upgrade the Control-M/Enterprise Manager Client
    - Doc: Upgrading Control-M Client on Windows from the Full Installation Package (9.0.22)
    - Doc: Upgrading Control-M Client on Windows from the Client Installation Package (9.0.22)
    - Doc: Upgrading Control-M Client from the Control-M Welcome Page (9.0.22)

## Topology-specific sequence

Load exactly one of these based on the customer's topology answer:

- [[em-topology-standalone]] — Standalone
- [[em-topology-ha]] — High Availability
- [[em-topology-distributed]] — Distributed
- [[em-topology-distributed-ha]] — Distributed + High Availability

## Related rules

- [[postgres-not-upgraded-in-place]]
