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

# hops: load every version note on the path (source, intermediates, target) and warn when a
# hop's target has no runbook in this vault (e.g. 9.0.19 -> 9.0.20.200 -> 9.0.22 has none for hop 1)
pmeta, _ = fm(path_note)
hops = [re.findall(r"\d+(?:\.\d+)+", h) for h in pmeta.get("hops", "").split(",")]
hops = [h for h in hops if len(h) == 2] or [[a.source, a.target]]
for v in dict.fromkeys([a.source] + [x for h in hops for x in h] + [a.target]):
    emit(os.path.join(ROOT, "versions", f"v-{v.replace('.', '-')}.md"), seen)
runbook_targets = sorted({fm(r)[0].get("target_version", "") for r in glob.glob(os.path.join(ROOT, "runbook", "*", "*.md"))} - {""})
for i, (h_src, h_tgt) in enumerate(hops, 1):
    if h_tgt not in runbook_targets:
        msg = (f"WARNING: hop {i} of {len(hops)} ({h_src} -> {h_tgt}) has NO runbook in this vault "
               f"(runbooks exist only for target {', '.join(runbook_targets)}). Verify {h_tgt} requirements against BMC docs; "
               f"see the path note and _meta/known-issues.md. Treat each hop as a separate case.")
        print(f"\n<!-- {msg} -->"); print(msg, file=sys.stderr)

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
