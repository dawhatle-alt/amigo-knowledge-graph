---
name: java17-and-api-gateway-port
type: rule
severity: blocking
applies_to: [server]
target_version: 9.0.22
maintained_by: hand
---

# External Java 17 and API gateway port before the Server upgrade

**Rule:** Before running the Control-M/Server 9.0.22 upgrade:

1. Set the Java environment variable to an external **Java 17** JRE ("Setting the Java Environment Variable" / "Changing JRE Package" docs).
2. Set `BMC_INST_CTM_APIGTW_PORT=8393` (or the port the customer has reserved) — the sample plan hardcodes 8393.

Both appear as pre-installation steps in [[server-phase-4-control-m-server-upgrade]]. The EM runbook has the Java step only ([[em-phase-4-control-m-enterprise-manager-upgrade]]).

## How the skill should apply it

- Include both steps verbatim in any Server plan targeting 9.0.22.
- Ask whether port 8393 is free / allowed through firewalls; if not, the customer must choose another and the env var must match.
