"""Merge guides/_meta/*.json into guides/index.json. Safe to run any time; run before every commit."""
import json, os, glob
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "guides")
gi = os.path.join(R, "index.json")
g = json.load(open(gi))
for f in glob.glob(os.path.join(R, "_meta", "*.json")):
    g[os.path.basename(f)[:-5]] = json.load(open(f))
g = {k: v for k, v in g.items() if os.path.exists(os.path.join(R, k + ".md"))}
json.dump(g, open(gi, "w"), indent=1)
print(len(g), "guides indexed")
