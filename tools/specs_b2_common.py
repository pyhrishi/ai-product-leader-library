import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen import write
from specs_12 import T


def S(title, framing, body, label, ftxt, fix, xr, one):
    return dict(title=title, framing=framing, body=T(body), fm=[(label, ftxt, fix)], xr=xr, one=one)


def R(rows, disagree):
    out = ["| Source | Title | What it proves | 2026 status |", "|---|---|---|---|"]
    for a, b, c, d in rows:
        out.append("| %s | %s | %s | %s |" % (a, b, c, d))
    return "\n".join(out) + "\n\n*Disagreement named:* " + disagree


def G(mod, id, title, thesis, prove, discipline, counter, read_min, prove_h, depth, deliverable,
      sections, retrieval, steps, pass_md, fail_md, verdict, res, reframe, thin="none flagged"):
    return dict(mod=mod, id=id, title=title, short=title, thesis=thesis, prove=prove, discipline=discipline,
                counter=counter, read_min=read_min, prove_h=prove_h, depth=depth, deliverable=deliverable,
                sections=sections, retrieval=retrieval, steps=steps, pass_md=T(pass_md), fail_md=T(fail_md),
                verdict=verdict, resources=res, reframe=reframe, thin=thin)


def run(specs):
    for s in specs:
        write(s)
