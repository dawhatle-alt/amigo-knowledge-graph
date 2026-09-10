#!/usr/bin/env python3
"""
Vault loader for the concierge-upgrade-advisor skill.

Prints the minimal set of notes for one upgrade scenario, in precedence order,
so the skill never has to read the whole vault.

usage: vault_loader.py --vault PATH --source 9.0.21 [--target 9.0.22]
                       [--components em,server] [--em-topology standalone|ha|distributed|distributed-ha]
                       [--server-topology standalone|ha] [--addons bim,aapi,...]
                       [--phase interview|plan|all]
"""
import argparse, glob, os, re, sys

# Windows consoles default to cp1252; notes contain non-ASCII (e.g. ≥), so force UTF-8 output.
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8")

def fm(path):
    t = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---", t, re.S)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1); meta[k.strip()] = v.strip().strip('"')
    return meta, t

def emit(path, seen):
    if path in seen or not os.path.exists(path): return
    seen.add(path)
    print(f"\n<!-- note: {os.path.relpath(path, ROOT)} -->\n")
    print(open(path, encoding="utf-8").read())

ap = argparse.ArgumentParser()
ap.add_argument("--vault", default=os.environ.get("AMIGO_VAULT", "."))
ap.add_argument("--source", required=True)
ap.add_argument("--target", default="9.0.22")
ap.add_argument("--components", default="em,server")
ap.add_argument("--em-topology", default=None)
ap.add_argument("--server-topology", default=None)
ap.add_argument("--addons", default="")
ap.add_argument("--phase", default="all", choices=["interview", "plan", "all"])
a = ap.parse_args()
ROOT = os.path.abspath(a.vault); seen = set()
comps = [c.strip() for c in a.components.split(",") if c.strip()]

emit(os.path.join(ROOT, "CLAUDE.md"), seen)
for p in sorted(glob.glob(os.path.join(ROOT, "rules", "*.md"))): emit(p, seen)

# path note
key = a.source.replace(".", "")[:4]  # 9.0.20.200 -> 9020
path_note = os.path.join(ROOT, "paths", f"path-{key}-to-{a.target.replace('.', '')}.md")
if not os.path.exists(path_note):
    print(f"\n<!-- NO PATH NOTE for {a.source} -> {a.target}. Out of scope or not yet authored. See paths/paths-index.md -->")
    emit(os.path.join(ROOT, "paths", "paths-index.md"), seen)
    sys.exit(2)
emit(path_note, seen)
for v in {a.source, a.target}:
    emit(os.path.join(ROOT, "versions", f"v-{v.replace('.', '-')}.md"), seen)

if a.phase in ("interview", "all"):
    for c in comps:
        for p in sorted(glob.glob(os.path.join(ROOT, "checklist", c, "*.md"))):
            meta, _ = fm(p)
            if meta.get("status") == "superseded": continue
            emit(p, seen)

if a.phase in ("plan", "all"):
    topo = {"em": a.em_topology, "server": a.server_topology}
    for c in comps:
        for p in sorted(glob.glob(os.path.join(ROOT, "runbook", c, f"{c}-phase-*.md"))): emit(p, seen)
        if topo[c]:
            emit(os.path.join(ROOT, "runbook", c, f"{c}-topology-{topo[c]}.md"), seen)
        else:
            print(f"\n<!-- {c}: topology not given; ask the customer, then load exactly one {c}-topology-*.md -->")

for ad in [x.strip() for x in a.addons.split(",") if x.strip()]:
    emit(os.path.join(ROOT, "components", f"{ad}.md"), seen)

print(f"\n<!-- loaded {len(seen)} notes -->", file=sys.stderr)
