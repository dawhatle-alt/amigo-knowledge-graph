# concierge-upgrade-advisor — vault integration (addendum to SKILL.md)

This is the vault-side copy of the "Vault Knowledge Source" section that ships inside
`concierge-upgrade-advisor.skill` (bundle at the vault root). Keep the two in step: when
this file changes, splice the same text into the bundle's SKILL.md and re-upload the
skill; when the bundle changes, update this file. The vault replaces every hardcoded
version rule, checklist question, and runbook step previously embedded in the skill.

## Vault Knowledge Source — amigo-knowledge-graph (AUTHORITATIVE)

All AMIGO version rules, checklist questions, runbook steps, and scope boundaries come
from the amigo-knowledge-graph vault. Do NOT answer version, prerequisite, sequencing, or
scope questions from memory or from the skill's `references/` summaries alone.

### Session start (before Phase 2) — locate the vault, in this order

1. `$AMIGO_VAULT` — if the environment variable is set and the directory contains
   `CLAUDE.md`, use it. (Claude Code / Desktop: set it in `~/.claude/settings.json`
   under `"env"`; other runtimes: export it.)
2. A local clone already on this machine, e.g. `~/repos/amigo-knowledge-graph` or the
   Projects folder — use it if found.
3. Otherwise clone (network required):
   ```
   git clone --depth 1 https://github.com/dawhatle-alt/amigo-knowledge-graph.git "$HOME/amigo-vault"
   ```
   and use that path (in the claude.ai sandbox this is `/home/claude/amigo-vault`).

Set `AMIGO_VAULT` to the resolved path for the rest of the session. Read
`$AMIGO_VAULT/CLAUDE.md` and obey it. If no vault can be located (offline and no local
copy), fall back to the skill's `references/` copies and TELL the user the vault was
unreachable — never present references/ content as vault-cited.

### Load order (implemented by `tools/vault_loader.py` — use it, don't glob)

```
python3 "$AMIGO_VAULT/tools/vault_loader.py" --vault "$AMIGO_VAULT" --source <from-version> --target <to-version> --components em,server,agent --em-topology <t> --server-topology <t> --addons <list> --phase interview|plan
```

`vault_loader.py` also reads `AMIGO_VAULT` itself when `--vault` is omitted. On Windows
shells use `python` and keep the quotes — the path contains spaces.

1. `rules/*.md` — all, every session (highest precedence)
2. `paths/` — the ONE path note matching source→target; no match = say so and stop,
   never improvise a path
3. checklist indexes then individual notes as the interview reaches them
   (skip `status: superseded`)
4. runbook phase notes in order + exactly ONE topology note per component
5. `components/*.md` only for confirmed add-ons

### Checklist provenance fields (added Sep 2026)

Every active checklist note carries `hcu_sources` (hcu-knowledge-graph notes the answer
comes from) and `extractors` (amigo_prefill.py extractor IDs; `GAP-*` = known collectible
gap, `RUN-*` = customer must run a command). When HCU facts are available, a note whose
extractor resolved is pre-answered WITH that provenance; `GAP-*` notes go straight to the
COLLECT list; empty lists mean interview/decision by design. `tools/coverage_report.py`
rolls these up; `_meta/hcu-sources-patch.md` is the mapping source of truth.

### Behavior rules from the vault

- Direct 9.0.22 floor is **9.0.20** (`rules/direct-upgrade-requires-9020`); 9.0.19 = two
  hops via **9.0.20.200** as separate cases — never collapsed. This corrects the earlier
  skill bug that listed 9.0.19 as a valid direct source.
- Every plan step and every "you must" statement names its vault note.
- Anything outside `rules/amigo-scope.md` is called out as needing a regular case,
  immediately.
- Notes flagged in `_meta/known-issues.md` → surface the flag to the TSA, never silently
  pick a value.
- Precedence when sources conflict: user's live statement > parser facts > vault rules >
  vault checklist notes > the skill file.
