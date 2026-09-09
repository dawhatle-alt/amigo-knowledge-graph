# AMIGO Knowledge Graph — governance

This vault is the **source of truth** for the AMIGO (Assisted Migration Offering) Control-M upgrade program. The original spreadsheet (`AMIGO_Checklist_V22_*.xlsx`) was converted once by `tools/convert_xlsx.py`; from now on edits happen here, not in the spreadsheet.

## Note types (frontmatter `type`)

| type | folder | maintained by |
|---|---|---|
| `checklist-item` | `checklist/{em,server}/` | generated, then hand-edited |
| `runbook-phase`, `runbook-topology` | `runbook/{em,server}/` | generated, then hand-edited |
| `component` | `components/` | generated, then hand-edited |
| `procedure` | `procedures/` | generated, then hand-edited |
| `rule` | `rules/` | **hand only** — overrides any checklist prose |
| `version`, `upgrade-path` | `versions/`, `paths/` | **hand only** |
| `meta`, `index` | `_meta/`, `*-index.md` | generated |

Precedence when notes disagree: **rule > path > version > runbook > checklist prose**. A checklist note with `status: superseded` must never be used as a fact source; follow its `superseded_by` link.

## Rules for any AI reading this vault

1. **No invented prerequisites.** Every step, version floor, port, or KA number in an answer must trace to a note. If the vault has no note, say so and point to BMC docs — do not fill the gap from memory.
2. **Cite the note.** When giving guidance, name the note it came from (`per em-045-…`) so wrong answers are traceable.
3. **Load narrowly.** Start from `paths/paths-index.md`, pick the path note, follow links. Load exactly one `runbook-topology` note per component. Do not read the whole vault into context.
4. **Rules first.** Before producing any plan, read every note in `rules/` — they are short and they are the guardrails.
5. **Flag stale text rather than fix it silently.** Known stale items live in `_meta/known-issues.md`. When you find another, add a `> [!warning]` callout to the note and a row to that table.
6. **Never edit `rules/`, `paths/`, or `versions/` from a chat session without the human confirming.** Checklist/runbook wording fixes are fine.

## Rules for humans editing

- Keep frontmatter keys; add new ones freely. `name` must equal the filename stem — it is what wiki-links resolve against.
- When a new AMIGO spreadsheet version arrives, do **not** re-run the converter over hand-edited notes. Run it into a scratch folder, diff against `_meta/source-map.md`, merge by hand.
- Adding a new target version (e.g. 9.0.23): add `versions/`, `paths/`, new `runbook/` phase notes, and a new `direct-upgrade-requires-*` rule. Version-agnostic checklist items stay shared.
