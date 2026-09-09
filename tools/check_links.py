#!/usr/bin/env python3
"""Report [[links]] that don't resolve to a note `name`, and notes whose name != filename."""
import os, re, sys
root = sys.argv[1] if len(sys.argv) > 1 else "."
names, links, bad_names = {}, [], []
for dp, _, fs in os.walk(root):
    for f in fs:
        if not f.endswith(".md"): continue
        p = os.path.join(dp, f); t = open(p, encoding="utf-8").read()
        m = re.search(r"^name:\s*(.+)$", t, re.M)
        n = m.group(1).strip() if m else None
        if n and n != f[:-3]: bad_names.append((p, n))
        if n: names[n] = p
        for l in re.findall(r"\[\[([^\]|#]+)", t): links.append((p, l.strip()))
missing = [(p, l) for p, l in links if l not in names]
for p, l in missing: print(f"BROKEN  {p}  -> [[{l}]]")
for p, n in bad_names: print(f"NAME    {p}  name={n}")
print(f"{len(names)} notes, {len(links)} links, {len(missing)} broken, {len(bad_names)} name mismatches")
sys.exit(1 if missing or bad_names else 0)
