# amigo-knowledge-graph

Obsidian vault holding the AMIGO (Assisted Migration Offering) Control-M upgrade knowledge: starter checklists, sample runbooks, domain rules, version/path notes, and the TSA case procedure. Companion to `hcu-knowledge-graph`; consumed by the `concierge-upgrade-advisor` skill.

```
rules/        hard guardrails (hand-maintained, highest precedence)
paths/        one note per source→target upgrade path — the skill's entry point
versions/     one note per Control-M version
checklist/    one note per AMIGO Starter checklist question (em/, server/)
runbook/      phase notes + one note per topology variant (em/, server/)
components/   add-on components (BIM, AAPI, MFT, ...) with KA references
procedures/   TSA case-handling procedure
skill/        SKILL.md addendum + loader for the upgrade-advisor skill
tools/        one-shot xlsx converter (seed only — vault is master)
_meta/        source-row map, known issues
```

Read `CLAUDE.md` first.

## Seeding from a spreadsheet (already done)

```
python3 tools/convert_xlsx.py AMIGO_Checklist_V22_20251030.xlsx .
```

Re-running overwrites generated folders. Do not re-run over hand-edited notes.

## Validate links

```
python3 tools/check_links.py .
```
