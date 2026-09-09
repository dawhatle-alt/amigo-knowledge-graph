---
name: checklist-server-index
type: index
component: server
---

# Control-M/Server AMIGO Starter Checklist — index

Ordered as in the source spreadsheet. Section headers are preserved in each note's `section` field.

- [[server-011-what-is-the-version-of-the-control-m-ser]] — What is the version of the Control-M/Server that is being upgraded FROM
- [[server-012-what-is-the-fixpack-of-the-control-m-ser]] — What is the fixpack of the Control-M/Server that is being upgraded FROM
- [[server-013-what-is-the-database-server-connected-to]] — What is the Database Server connected to the existing Control-M/Server
- [[server-014-what-is-the-operating-system-of-the-exis]] — What is the Operating System of the existing Control-M/Server
- [[server-016-what-is-the-version-of-the-control-m-ser]] — What is the version of the Control-M/Server that is upgrading TO
- [[server-017-what-is-the-fixpack-of-the-control-m-ser]] — What is the fixpack of the Control-M/Server that is upgrading TO
- [[server-018-are-you-aware-of-the-latest-control-m-se]] — Are you aware of the latest Control-M Server patch available
- [[server-019-has-the-machine-been-verified-to-meet-th]] — Has the machine been verified to meet the minimum requirement for the Control-M/Server installation
- [[server-020-what-is-the-estimated-number-of-daily-jo]] — What is the estimated number of daily jobs expected to be in Control-M/Server Active Environment (Active Job File - AJF)
- [[server-021-is-the-control-m-enterprise-manager-of-t]] — Is the Control-M/Enterprise Manager of the same or higher version to the upgrading Control-M/Server
- [[server-022-are-there-any-control-modules-for-the-co]] — Are there any Control Modules for the Control-M/Server’s local agent that need to be installed
- [[server-023-is-there-at-least-12-gb-of-diskspace-ava]] — Is there at least 12 GB of diskspace available on the Control-M/Server machine to perform the In-place Upgrade
- [[server-024-run-the-below-control-m-server-utility-u]] — Run the below Control-M/Server utility using Control-M/Server Administrator Account:
- [[server-026-are-you-upgrading-the-control-m-agent-co]] — Are you upgrading the Control-M/Agent concurrently
- [[server-027-ensure-that-there-should-be-no-further-c]] — Ensure that there should be no further changes to the job definitions / calendars / services / workload policy until the in-place upgrade completed
- [[server-029-postgres-database-server-is-not-upgraded]] — Postgres Database Server is NOT Upgraded during the In-place Upgrade of Control-M/Server
- [[server-030-is-the-control-m-server-installed-on-nfs]] — Is the Control-M/Server installed on NFS or VXFS file system
- [[server-031-will-there-be-any-changes-to-t-he-contro]] — Will there be any changes to t he Control-M/Server hostname
- [[server-032-is-there-a-change-or-rename-of-the-contr]] — Is there a change or rename of the Control-M/Server Data Center Name
- [[server-033-do-you-have-sufficient-free-disk-space-f]] — Do you have sufficient free disk space for the Control-M/Server upgrade
- [[server-034-are-the-control-m-agents-only-connected]] — Are the Control-M/Agents only connected to a active Control-M/Server at any one time
- [[server-035-ensure-that-the-control-m-server-exe-win]] — Ensure that the Control-M/Server "exe" (Windows) / "script" (UNIX) directory is included in the system PATH variable and Control-M/Server Administrator is able to run "SQL" to access the Control-M/Server Database
- [[server-036-are-you-using-control-m-server-ctmldnrs]] — Are you using Control-M Server ctmldnrs
- [[server-037-are-you-running-timezone-jobs-and-has-ch]] — Are you running timezone jobs and has changed the CTM_GD_FORWARD parameter in CCM, or edited GD_FORWARD parameter in Control-M/Server's config
- [[server-038-are-the-control-m-enterprise-manager-and]] — Are the Control-M/Enterprise Manager and Control-M/Server using different user accounts on UNIX/Linux
- [[server-039-are-the-control-m-agents-connecting-to-c]] — Are the Control-M/Agents connecting to Control-M Server running on Red Hat 8
- [[server-041-do-you-have-more-than-one-control-m-serv]] — Do you have more than one Control-M/Server on this server
- [[server-042-if-you-are-using-bmc-supplied-postgresql]] — If you are using BMC supplied PostgreSQL database 11
- [[server-043-are-you-upgrading-control-m-server-with]] — Are you upgrading Control-M/Server with high availability configuration
- [[server-045-open-a-new-severity-1-ticket-if-facing-a]] — Open a New Severity 1 ticket if facing any issues during production environment upgrade
