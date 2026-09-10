#!/usr/bin/env python3
"""
Coverage report: roll up hcu_sources / extractors across active checklist notes.

Implements item 2 of _meta/hcu-sources-patch.md — the COVERED / PARTIAL / GAP
classes become reproducible from the vault. Reads only frontmatter; no parser
needed. Also serves as a schema check: every active checklist note in
checklist/{em,server,agent} must carry both fields (empty lists allowed).

usage: coverage_report.py [--vault PATH] [--components em,server,agent] [--json]

Classes (derived purely from the two fields):
  COVERED            hcu_sources present AND at least one X* extractor
  PENDING-EXTRACTOR  hcu_sources present, no X* extractor yet (extractor TBD)
  PARTIAL            no hcu_sources, but an X* extractor (e.g. agent-archive data)
  GAP                no hcu_sources, no X*, at least one GAP-* token (collectible)
  RUN-COMMAND        no hcu_sources, no X*, no GAP-*, at least one RUN-* token
  INTERVIEW          both lists empty — answered by interview / decision by design
  UNMAPPED           one or both fields absent (schema violation for em/server/agent)

Exit code 1 if any note is UNMAPPED or has an unparseable field.
"""
import argparse, glob, json, os, re, sys
from collections import defaultdict

if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8")

ORDER = ["COVERED", "PENDING-EXTRACTOR", "PARTIAL", "GAP", "RUN-COMMAND", "INTERVIEW", "UNMAPPED"]

def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    if not m: return {}
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            k, v = line.split(":", 1); out[k.strip()] = v.strip()
    return out

def parse_list(raw):
    """'["[[A]]", "[[B]]"]' -> ['A','B'];  '[X02, GAP-x]' -> ['X02','GAP-x'];  '[]' -> []"""
    if raw is None: return None
    raw = raw.strip()
    if not (raw.startswith("[") and raw.endswith("]")): raise ValueError(raw)
    inner = raw[1:-1].strip()
    if not inner: return []
    items = []
    for tok in inner.split(","):
        tok = tok.strip().strip('"').strip("'")
        tok = re.sub(r"^\[\[(.+?)\]\]$", r"\1", tok)  # unwrap wikilink
        if tok: items.append(tok)
    return items

def classify(sources, extractors):
    if sources is None or extractors is None: return "UNMAPPED"
    x = [e for e in extractors if re.match(r"^X\d+", e)]
    gap = [e for e in extractors if e.startswith("GAP-")]
    run = [e for e in extractors if e.startswith("RUN-")]
    if sources: return "COVERED" if x else "PENDING-EXTRACTOR"
    if x: return "PARTIAL"
    if gap: return "GAP"
    if run: return "RUN-COMMAND"
    return "INTERVIEW"

ap = argparse.ArgumentParser()
ap.add_argument("--vault", default=os.environ.get("AMIGO_VAULT", "."))
ap.add_argument("--components", default="em,server,agent")
ap.add_argument("--json", action="store_true", help="emit machine-readable JSON instead of markdown")
a = ap.parse_args()
ROOT = os.path.abspath(a.vault)
comps = [c.strip() for c in a.components.split(",") if c.strip()]

rows, errors = [], []
for comp in comps:
    for p in sorted(glob.glob(os.path.join(ROOT, "checklist", comp, "*.md"))):
        fm = frontmatter(open(p, encoding="utf-8").read())
        if fm.get("type") != "checklist-item": continue          # skips *-index notes
        if fm.get("status") == "superseded": continue             # never a fact source
        name = fm.get("name", os.path.basename(p)[:-3])
        try:
            sources, extractors = parse_list(fm.get("hcu_sources")), parse_list(fm.get("extractors"))
        except ValueError as e:
            errors.append(f"{name}: unparseable list {e}"); sources = extractors = None
        cls = classify(sources, extractors)
        if cls == "UNMAPPED": errors.append(f"{name}: missing hcu_sources and/or extractors")
        rows.append({"component": comp, "note": name, "class": cls,
                     "hcu_sources": sources or [], "extractors": extractors or []})

by_class = defaultdict(list)
for r in rows: by_class[r["class"]].append(r)
by_comp = defaultdict(lambda: defaultdict(int))
for r in rows: by_comp[r["component"]][r["class"]] += 1
collect = defaultdict(list)     # GAP-* token -> notes (the PM roadmap list)
run_cmds = defaultdict(list)    # RUN-* token -> notes
ext_index = defaultdict(list)   # X* extractor -> notes (what the parser must provide)
src_index = defaultdict(list)   # hcu note -> checklist notes (what the hcu vault must contain)
for r in rows:
    for e in r["extractors"]:
        (collect if e.startswith("GAP-") else run_cmds if e.startswith("RUN-") else ext_index)[e].append(r["note"])
    for s in r["hcu_sources"]: src_index[s].append(r["note"])

if a.json:
    print(json.dumps({"notes": rows, "summary": {k: len(v) for k, v in by_class.items()},
                      "by_component": {c: dict(v) for c, v in by_comp.items()},
                      "collect_list": collect, "run_commands": run_cmds,
                      "extractor_index": ext_index, "hcu_source_index": src_index, "errors": errors},
                     indent=2))
    sys.exit(1 if errors else 0)

total = len(rows)
print("# AMIGO checklist coverage report\n")
print(f"Active checklist notes scanned: {total} (components: {', '.join(comps)})\n")
print("## Summary by class\n")
print("| Class | " + " | ".join(comps) + " | Total | % |")
print("|---|" + "---|" * (len(comps) + 2))
for cls in ORDER:
    n = len(by_class.get(cls, []))
    if not n: continue
    cells = [str(by_comp[c].get(cls, 0)) for c in comps]
    print(f"| {cls} | " + " | ".join(cells) + f" | {n} | {100 * n // total}% |")
auto = len(by_class.get("COVERED", [])) + len(by_class.get("PARTIAL", []))
print(f"\nAuto-answerable from HCU data (COVERED + PARTIAL): **{auto} / {total}**\n")

print("## Collect list (GAP-* tokens → PM roadmap)\n")
for tok in sorted(collect): print(f"- `{tok}` ← " + ", ".join(f"[[{n}]]" for n in collect[tok]))
print("\n## Run-command items (RUN-* tokens)\n")
for tok in sorted(run_cmds): print(f"- `{tok}` ← " + ", ".join(f"[[{n}]]" for n in run_cmds[tok]))

print("\n## Extractor index (what amigo_prefill.py must provide)\n")
print("| Extractor | Notes |\n|---|---|")
for tok in sorted(ext_index, key=lambda t: int(re.sub(r"\D", "", t) or 0)):
    print(f"| {tok} | " + ", ".join(f"[[{n}]]" for n in ext_index[tok]) + " |")

print("\n## HCU source index (what hcu-knowledge-graph must contain)\n")
print("| hcu note | Referenced by |\n|---|---|")
for s in sorted(src_index): print(f"| [[{s}]] | {len(src_index[s])} |")

print("\n## Notes by class\n")
for cls in ORDER:
    if not by_class.get(cls): continue
    print(f"### {cls} ({len(by_class[cls])})\n")
    for r in by_class[cls]:
        ex = ", ".join(r["extractors"]) or "—"
        src = ", ".join(f"[[{s}]]" for s in r["hcu_sources"]) or "—"
        print(f"- [[{r['note']}]] — sources: {src}; extractors: {ex}")
    print()

if errors:
    print("## Schema errors\n")
    for e in errors: print(f"- {e}")
    sys.exit(1)
