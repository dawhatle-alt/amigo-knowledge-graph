# concierge-upgrade-advisor — vault integration (addendum to SKILL.md)

Paste this section into the skill's SKILL.md and set `AMIGO_VAULT` to the local clone path of `amigo-knowledge-graph`. The vault replaces every hardcoded version rule, checklist question, and runbook step previously embedded in the skill.

## Knowledge source

All AMIGO facts come from the Obsidian vault at `$AMIGO_VAULT` (default `~/repos/amigo-knowledge-graph`). Read `$AMIGO_VAULT/CLAUDE.md` before anything else and obey it. Do not answer version, prerequisite, sequencing, or scope questions from memory.

## Load order

1. `rules/*.md` — all of them, every session (they are short).
2. `paths/paths-index.md` → pick the one `paths/path-*.md` matching the customer's source → target. If no path note matches, say so and stop; do not improvise a path.
3. `checklist/em/checklist-em-index.md` and/or `checklist/server/checklist-server-index.md`, then individual checklist notes as the interview reaches them. Skip notes with `status: superseded`.
4. `runbook/{em,server}/runbook-*-index.md` → phase notes in order.
5. Exactly one `runbook/*/*-topology-*.md` per component, chosen from the customer's HA/Distributed answer.
6. `components/*.md` only for add-ons the customer confirmed.

`tools/vault_loader.py` implements this and prints the concatenated notes; call it instead of globbing by hand.

## Behaviour changes from the vault

- Version floor for direct 9.0.22 upgrade is **9.0.20** (`rules/direct-upgrade-requires-9020.md`). 9.0.19 → two hops via 9.0.20.200. This corrects the earlier skill bug.
- Every plan step and every "you must" statement names the note it came from.
- Anything outside `rules/amigo-scope.md` is called out as needing a regular case, immediately.
- If a vault note is flagged in `_meta/known-issues.md`, surface the flag to the TSA rather than silently choosing a value.
