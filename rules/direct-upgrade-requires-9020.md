---
name: direct-upgrade-requires-9020
type: rule
severity: blocking
applies_to: [em, server]
target_version: 9.0.22
maintained_by: hand
---

# Direct upgrade to 9.0.22 requires source ≥ 9.0.20

**Rule:** A Control-M/EM or Control-M/Server can be upgraded directly (single hop) to 9.0.22 only if the source version is **9.0.20 or 9.0.21**.

**9.0.19 is NOT a valid direct source.** A 9.0.19 environment must first upgrade to **9.0.20.200**, then to 9.0.22 — see [[path-9019-to-9022]].

## Why this note exists

The AMIGO checklist spreadsheet contains conflicting information:

- EM checklist row 43 prose says "must be at least 9.0.19 to upgrade directly to 9.0.22" — **wrong / superseded** ([[em-043-control-m-enteprrise-manager-must-be-at]])
- EM and Server checklist row 11 FROM-version dropdown offers only 9.0.20 and 9.0.21 — **correct**

The earlier `concierge-upgrade-advisor` skill read the prose and listed 9.0.19 as a valid direct source. This note is the single point of truth; never derive the floor version from checklist prose.

## How the skill should apply it

1. Get the customer's current EM version and Server version.
2. If either is < 9.0.20 → the plan MUST include an intermediate hop via 9.0.20.200 and the skill must say so explicitly.
3. If either is < 9.0.19 or otherwise unsupported → out of AMIGO scope ([[amigo-scope]]); customer needs a regular case.

## Related

- [[path-9020-to-9022]], [[path-9021-to-9022]], [[path-9019-to-9022]]
- [[v-9-0-20]], [[v-9-0-20-200]], [[v-9-0-21]], [[v-9-0-22]]
