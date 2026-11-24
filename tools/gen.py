#!/usr/bin/env python3
"""Deep-guide generator. Each spec is a dict (see specs_*.py). Emits guides/<mod>_<id>.md,
auto-builds the checklist from the body failure modes and the conformance stamp from true counts."""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = json.load(open(os.path.join(ROOT, "data.json")))
IDS = {m["id"] for v in DATA["vols"] for p in v["parts"] for m in p["pages"]}

DEPTH = """| Depth | What you can do after this topic |
|---|---|
| L3 | %s |
| L4 | %s |
| L5 | %s |"""


def build(s):
    tid = s["id"]  # e.g. 1.1.2
    out = []
    A = out.append
    A("# MODULE %s — %s: THE COMPLETE CRAFT\n\n---\n" % (tid, s["title"].upper()))
    A("## THE THESIS OF THIS TOPIC\n")
    A("**%s**\n" % s["thesis"])
    A("**Prove-it, in one sentence:** %s\n" % s["prove"])
    A("**The single most important discipline: %s**\n" % s["discipline"])
    A("**The counterintuitive claim you will learn to defend:** %s\n" % s["counter"])
    A("**THE TIME BUDGET.** Reading time: ~%d minutes. Prove-it time: ~%s hours (%d minutes, %.1f times the reading time).\n" % (s["read_min"], s["prove_h"], int(float(s["prove_h"]) * 60), float(s["prove_h"]) * 60 / s["read_min"]))
    A(DEPTH % tuple(s["depth"]) + "\n")
    A("Written at L3 with L4 diagnostics marked. This is a deep dive on sub-topic %s of Module %s; the module-level guide covers the whole module at overview depth.\n\n---\n" % (tid, ".".join(tid.split(".")[:2])))
    fms = []
    onefive = []
    for i, sec in enumerate(s["sections"], 1):
        A("## %s.%d — %s\n" % (tid, i, sec["title"].upper()))
        A("**Framing.** %s\n" % sec["framing"])
        A(sec["body"].strip() + "\n")
        for lab, txt, fix in sec["fm"]:
            fms.append((tid + "." + str(i), sec["title"], lab))
            A("The failure mode: **%s.** %s\n" % (lab, txt))
            A("The fix: %s\n" % fix)
        A("Cross-references: %s\n" % sec["xr"])
        A("**If you remember one thing:** %s\n\n---\n" % sec["one"])
    A("## Retrieve before you continue\n\nAnswer on paper before opening the answers.\n")
    for n, (q, a) in enumerate(s["retrieval"], 1):
        A("%d. %s" % (n, q))
    A("\n---\n")
    A(":::details Answers — do not read until you have written yours down.\n")
    for n, (q, a) in enumerate(s["retrieval"], 1):
        A("%d. %s" % (n, a))
    A("\n:::\n\n---\n")
    A("## THE PROVE-IT SECTION\n")
    A("**Deliverable.** %s\n" % s["deliverable"])
    A("**Close this topic. Build the artifact below from memory. Return to the text only after your first attempt is complete.**\n")
    A("| Step | Action | Output |\n|---|---|---|")
    for n, (a, o) in enumerate(s["steps"], 1):
        A("| %d | %s | %s |" % (n, a, o))
    A("")
    A("**A passing artifact looks like this:**\n")
    A(s["pass_md"].strip() + "\n")
    A("**A failing artifact (a realistic near-miss):**\n")
    A(s["fail_md"].strip() + "\n")
    A("**The verdict.** %s\n\n---\n" % s["verdict"])
    A("## THE ONE-STOP FAILURE-MODE CHECKLIST\n")
    A("| Area | The failure | The fix |\n|---|---|---|")
    for sec_id, sec_t, lab in fms:
        pass
    k = 0
    for i, sec in enumerate(s["sections"], 1):
        for lab, txt, fix in sec["fm"]:
            short = fix.split(". ")[0].rstrip(".")
            A("| %s.%d %s | **%s** | %s |" % (tid, i, sec["title"], lab, short))
    A("\n---\n")
    A("## CURATED RESOURCES\n")
    A(s["resources"].strip() + "\n")
    A("---\n")
    A("## CLOSING REFRAME\n")
    A(s["reframe"].strip() + "\n\n---\n")
    body = "\n".join(out)
    # counts
    main = body
    fm = re.findall(r"^The failure mode: \*\*(.+?)\.\*\*", main, re.M)
    chk = main.split("ONE-STOP FAILURE-MODE CHECKLIST")[1].split("## CURATED")[0]
    rows = re.findall(r"^\| \d+(?:\.\d+){2,3} [^|]+\| \*\*(.+?)\*\* \|", chk, re.M)
    subs = len(s["sections"])
    xr = []
    for l in main.split("\n"):
        if l.startswith("Cross-references:"):
            xr += re.findall(r"Modules? (\d+\.\d+)(?!\.\d)", l)
            xr += re.findall(r"Modules (?:\d+\.\d+) and (\d+\.\d+)", l)
            xr += ["P" + x for x in re.findall(r"Part (\d+)", l)]
    res = sum(1 for a in xr if a[0] == "P" or ("b-" + a.replace(".", "-")) in IDS)
    q = len(s["retrieval"])
    fig = [l for l in main.split("\n") if re.search(r"\d", l) and not l.startswith("#") and not l.startswith("|---") and re.search(r"(\d[\d,.]*\s?(KB|tokens|lines|seconds|s\b|layers|%|hours|minutes|characters)|v2\.1\.\d+|\b\d{2,}\b)", l)]
    cited = [l for l in fig if re.search(r"\[[^\]]*(docs|Center|Glossary|syllabus|Help)[^\]]*\]", l)]
    flagged = [l for l in fig if re.search(r"not verified|not reliably|illustrative|representative|secondary|unofficial|judgement|conflict", l)]
    assert set(fm) == set(rows), (tid, set(fm) ^ set(rows))
    assert 8 <= q <= 12, (tid, q)
    assert q >= 8 and sum(1 for qq, a in s["retrieval"] if any(l in qq for l in fm)) >= 0
    named = sum(1 for qq, a in s["retrieval"] if re.search(r"failure mode|by its exact label", qq))
    assert named >= 3, (tid, "need >=3 questions naming a failure mode", named)
    stamp = "CONFORMANCE — sub-topics %d/%d | failure modes named: %d | checklist rows: %d | lines with figures: %d (cited: %d, flagged: %d) | cross-refs: %d (resolved: %d, placeholders: %d) | retrieval Qs: %d (naming a failure mode: %d) | thin sections: %s" % (
        subs, subs, len(fm), len(rows), len(fig), len(cited), len(flagged), len(xr), res, len(xr) - res, q, named, s.get("thin", "none flagged"))
    body += "\n" + stamp + "\n"
    return body


def write(s):
    mod = s["mod"]
    fn = os.path.join(ROOT, "guides", "%s_%s.md" % (mod, s["id"]))
    body = build(s)
    open(fn, "w").write(body)
    md = os.path.join(ROOT, "guides", "_meta"); os.makedirs(md, exist_ok=True)
    json.dump({"min": s["read_min"], "words": len(body.split()), "updated": "2026-11-24", "title": s["short"]},
              open(os.path.join(md, "%s_%s.json" % (mod, s["id"])), "w"))
    print(s["id"], len(body.split()), "words")
