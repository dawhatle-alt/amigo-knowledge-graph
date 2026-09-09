---
name: ha-distributed-upgrade-order
type: rule
severity: blocking
applies_to: [em, server]
maintained_by: hand
---

# HA / Distributed upgrade order

**Rule:** Non-standalone topologies have a fixed node order. Load exactly one topology note and follow it step by step:

| Component | Topology | Note |
|---|---|---|
| EM | Standalone | [[em-topology-standalone]] |
| EM | HA (Primary > Secondary) | [[em-topology-ha]] |
| EM | Distributed (Primary > Distributed) | [[em-topology-distributed]] |
| EM | Distributed + HA | [[em-topology-distributed-ha]] |
| Server | Standalone | [[server-topology-standalone]] |
| Server | HA (Primary > Secondary) | [[server-topology-ha]] |

Common pattern: stop Secondary's Configuration Agent and/or the Distributed node first → upgrade Primary → upgrade Distributed → upgrade Secondary → verify Primary → restart the others → verify connectivity.

For EM Distributed, all EM servers must be upgraded in the **same outage window** ([[em-phase-2-finalize-upgrade-details]]). KA 000386814 covers the recommended HA/Distributed steps ([[em-045-are-you-upgrading-control-m-em-with-high]]).
