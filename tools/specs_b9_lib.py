import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen import write


def G(mod, id, title, thesis, prove, disc, counter, secs, qs, steps, passmd, failmd, verdict, res, disagree, reframe,
      read=20, prove_h="2", thin=None, depth=None):
    sections = []
    for t, framing, body, fm, xr, one in secs:
        sections.append(dict(title=t, framing=framing, body=body.strip(), fm=[fm], xr=xr, one=one))
    rows = "\n".join("| %s | %s | %s | %s |" % r for r in res)
    resources = "| Source | Title | What it proves | 2026 status |\n|---|---|---|---|\n" + rows + "\n\n*Disagreement named:* " + disagree
    d = depth or ["Describe the core workflow and vocabulary of this topic", "Apply it to a real task and diagnose where it fails", "Set team-level policy and gates for it"]
    s = dict(mod=mod, id=id, title=title, short=title, thesis=thesis, prove=prove, discipline=disc, counter=counter,
             read_min=read, prove_h=prove_h, depth=d, deliverable=steps[0], sections=sections, retrieval=qs,
             steps=steps[1], pass_md=passmd, fail_md=failmd, verdict=verdict, resources=resources, reframe=reframe)
    if thin:
        s["thin"] = thin
    return s
