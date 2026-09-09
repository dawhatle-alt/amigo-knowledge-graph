# hcu_sources patch set — linking amigo-knowledge-graph ↔ hcu-knowledge-graph

**Status: draft for review — apply per your vault batch protocol, no notes modified by this patch.**

Adds two frontmatter fields to checklist notes so the question → data-source →
extractor → fact chain is traversable:

```yaml
hcu_sources: ["[[Artifact-check_config_report-json]]"]   # hcu-knowledge-graph note(s)
extractors: [X02]                                        # amigo_prefill.py extractor IDs
```

Semantics: `hcu_sources` present + extractor resolves → the question is
auto-answered with provenance. Empty list = interview/decision by design.
`extractors: [GAP-*]` marks a known collectible gap (feeds the PM roadmap).

## EM checklist mappings

| Note | hcu_sources | extractors | Class |
|---|---|---|---|
| em-011 (FROM version) | [[Artifact-check_config_report-json]] | X02 | COVERED |
| em-012 (FROM fixpack) | [[Artifact-check_config_report-json]], [[Server-Artifact-installed-versions]] | X02, X01 | COVERED |
| em-013 (database server) | [[db-postgresql]], [[Server-db-oracle]] | X05 | COVERED / INFERRED for MSSQL |
| em-014 (operating system) | [[OS-Hardware]] | X04 | COVERED |
| em-016 / em-017 (TO version/fixpack) | — | — | DECISION |
| em-018 (aware of latest FP/patch) | — | — | INTERVIEW |
| em-019 (verified requirements) | — | — | INTERVIEW (PAC tool) |
| em-020 (EM clients upgraded) | — | GAP-em-clients | COLLECTIBLE GAP |
| em-021 (machine meets reqs / check_req) | — | RUN-check_req | RUN-COMMAND |
| em-022 (LDAP planned) | [[EM-LDAP]] | X17 | COVERED (current state) |
| em-023 (daily jobs) | [[Artifact-check_config_report-json]] | X10 | COVERED — measured |
| em-025 (different machine?) | — | — | DECISION |
| em-026 (disk space) | [[OS-Disk]] | X12 | COVERED (snapshot) |
| em-027 (latest FP installed) | [[Server-Artifact-installed-versions]] | X01, X02 | COVERED |
| em-028 (z/OS) | — | — | INTERVIEW (scope) |
| em-029 (additional EM components) | [[EM-Services]] | X21 | PARTIAL |
| em-039 (PostgreSQL not upgraded in place) | [[db-postgresql]] | X05 | COVERED (applicability) |
| em-040 (components stop/start verified) | — | — | INTERVIEW |
| em-042 (Compatibility Mode) | — | GAP-X19 | COLLECTIBLE GAP (field unverified) |
| em-043 (version floor) | — | — | RULE ([[direct-upgrade-requires-9020]]) |
| em-044 (AAPI jobs) | [[EM-AAPI]] | X20 | COVERED |
| em-045 (EM HA) | [[EM-ini]] | X07 | COVERED |
| em-046 (BMC PostgreSQL version) | [[db-postgresql]] | X05 | COVERED |
| em-047 (EM+Server same machine) | [[OS-Network]] | X08 | DERIVED |
| em-048 (authorizations to roles) | — | — | POST-TASK ([[authorizations-to-roles]]) |
| em-050 (open new case) | — | — | PROCEDURAL |

## Server checklist mappings

| Note | hcu_sources | extractors | Class |
|---|---|---|---|
| server-011 / 012 (FROM version/fixpack) | [[Server-Artifact-installed-versions]] | X01 | COVERED |
| server-013 (database) | [[db-postgresql]], [[Server-db-oracle]] | X05 | COVERED / INFERRED |
| server-014 (OS) | [[OS-Hardware]] | X04 | COVERED |
| server-016 / 017 (TO version) | — | — | DECISION |
| server-018 (aware latest FP) | — | — | INTERVIEW |
| server-019 (machine reqs) | — | RUN-check_req | RUN-COMMAND |
| server-020 (daily jobs / AJF) | [[Server-Artifact-jobs_count-csv]] | X11 | COVERED |
| server-021 (EM ≥ Server) | [[Artifact-check_config_report-json]], [[Server-Artifact-installed-versions]] | X02+X01 | DERIVED |
| server-022 (Control Modules local agent) | — | X28 / GAP-cm-inventory | PARTIAL (agent archive) → COLLECTIBLE |
| server-023 / 033 (disk) | [[OS-Disk]] | X12 | COVERED |
| server-024 (ctmsetown utility) | — | RUN-ctmsetown / GAP-ctmsetown | RUN-COMMAND → COLLECTIBLE |
| server-026 (agents upgraded concurrently) | — | — | DECISION (wave plan) |
| server-027 (change cutoff) | — | — | DECISION |
| server-029 / 042 (PostgreSQL) | [[db-postgresql]] | X05 | COVERED |
| server-030 (NFS/VXFS) | [[OS-Disk]] | X12 (fs_flags) | COVERED (UNIX) |
| server-031 (hostname change) / 032 (DC rename) | — | — | DECISION |
| server-034 (agents one server only) | [[Server-AG_TBL_CTM]], [[Agent-Artifact-CONFIG-dat]] | X22, X24 | PARTIAL (agent-side authoritative) |
| server-035 (exe dir in PATH) | — | RUN-path-check | RUN-COMMAND |
| server-036 (ctmldnrs) | [[Server-CNF_INFO]] | X16 | COVERED (presence) |
| server-037 (timezone / GD_FORWARD) | [[Server-CNF_INFO]] | X15 | COVERED |
| server-038 (same host) | [[OS-Network]] | X08 | DERIVED |
| server-039 (RHEL 8.5+ SSL agents) | [[Server-AG_TBL_CTM]], [[Server-CNF_INFO-SSL]] | X25 | DERIVED (flag) |
| server-041 (multiple servers on box) | [[Server-CNF_INFO]], [[OS-Processes]] | X09 | PARTIAL |
| server-043 (Server HA) | [[Server-Artifact-SYSPRM-csv]] | X06 | COVERED |
| server-045 (SEV-1 procedure) | — | — | PROCEDURAL |

## Agent checklist mappings (patch notes ship pre-linked)

| Note | hcu_sources | extractors |
|---|---|---|
| agent-001 fleet inventory | [[Server-AG_TBL_CTM]], [[Server-Artifact-agent-availability]] | X22, X23, X29 |
| agent-004 authorized servers | [[Agent-Artifact-CONFIG-dat]] | X24 |
| agent-006 RHEL 8.5 SSL | join | X25 |
| agent-012 control modules | agent cm/ tree | X28 |
| agent-013 java | [[OS-Java]] | (agent-archive Java — extractor TBD) |
| agent-014 disk | [[OS-Disk]] | X12 |
| agent-020 AV exclusions | [[OS-Processes]] | X27 (detection only) |
| all others | — | interview / run-command / decision |

## Example patched note (frontmatter only)

```yaml
---
name: em-023-what-is-the-estimated-total-number-daily
type: checklist-item
component: em
section: "Existing Control-M/Enterprise Manager Environment"
answer_type: choice
blocking: false
related_rules: []
related_components: []
hcu_sources: ["[[Artifact-check_config_report-json]]"]
extractors: [X10]
status: active
source_sheet: "AMIGO EM Checklist V22"
source_row: 23
source_file: AMIGO_Checklist_V22_20251030.xlsx
---
```

## Application semantics for the agent (all runtimes)

1. TRIAGE: for each active checklist note in scope — if `extractors` resolve to
   a fact → pre-answered with provenance; if `GAP-*` → 🟡 collect item citing
   the note; empty → 🟠/⚪ per note type. The gap list becomes *generated from
   the vault*, not hardcoded in the parser.
2. Coverage reporting: COVERED/PARTIAL/GAP classes roll up automatically —
   the PM coverage analysis becomes reproducible from the vault at any time.
3. Maintenance: new extractor in the parser → add its ID here; new checklist
   version → converter carries these fields forward (add to convert_xlsx.py's
   preserved-fields list).

## Suggested apply order (per your batch protocol)

1. Batch 1: rules/ + the 6 blocking agent notes — review gate
2. Batch 2: remaining agent checklist + runbook/agent — gate
3. Batch 3: hcu_sources fields on EM notes (this table) — gate
4. Batch 4: Server notes — gate; then run `tools/check_links.py`
   (links resolve only if the hcu-knowledge-graph vault is opened in the same
   Obsidian workspace — otherwise they are documented dangling by design)
