import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen import write

D = "Claude Code docs"


def T(s):
    return s.strip()


def make(mod, id, title, thesis, prove, disc, counter, secs, ret, steps, ok, bad, verdict, res, dis, reframe, thin=None, depth=None, read_min=14, prove_h="2"):
    """secs: list of (title, framing, body, (label,text,fix), xr, one)"""
    sections = []
    for t, fr, body, fm, xr, one in secs:
        sections.append(dict(title=t, framing=fr, body=T(body), fm=[fm], xr=xr, one=one))
    rows = "\n".join("| %s | %s | %s | %s |" % r for r in res)
    resources = "| Source | Title | What it proves | 2026 status |\n|---|---|---|---|\n" + rows + "\n\n*Disagreement named:* " + dis
    s = dict(mod=mod, id=id, title=title, short=title, thesis=thesis, prove=prove, discipline=disc, counter=counter,
             read_min=read_min, prove_h=prove_h,
             depth=depth or ["Name the moving parts and where each setting lives", "Diagnose a misbehaving deployment from its symptoms", "Design the policy and verify it on a real machine"],
             deliverable=ok[0], sections=sections, retrieval=ret, steps=steps, pass_md=T(ok[1]), fail_md=T(bad), verdict=verdict,
             resources=resources, reframe=reframe)
    if thin:
        s["thin"] = thin
    return s


def run(specs, only=None):
    for s in specs:
        write(s)
