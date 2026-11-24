import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen import write


def T(s):
    return s.strip()


def G(mod, id, title, thesis, prove, disc, counter, read, prove_h, depth, deliverable, secs, ret, steps,
      pass_md, fail_md, verdict, res, dis, reframe, thin=None):
    sections = []
    for (t, fr, body, fm, xr, one) in secs:
        sections.append(dict(title=t, framing=fr, body=T(body), fm=[fm], xr=xr, one=one))
    rows = "\n".join("| %s | %s | %s | %s |" % r for r in res)
    resources = "| Source | Title | What it proves | 2026 status |\n|---|---|---|---|\n" + rows + "\n\n*Disagreement named:* " + dis
    d = dict(mod=mod, id=id, title=title, short=title, thesis=thesis, prove=prove, discipline=disc, counter=counter,
             read_min=read, prove_h=prove_h, depth=depth, deliverable=deliverable, sections=sections, retrieval=ret,
             steps=steps, pass_md=T(pass_md), fail_md=T(fail_md), verdict=verdict, resources=resources, reframe=reframe)
    if thin:
        d["thin"] = thin
    return d


def run(specs):
    for s in specs:
        write(s)
