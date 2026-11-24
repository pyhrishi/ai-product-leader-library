import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen import write

D = "Claude Code docs"


def T(x):
    return x.strip()


def mk(mod, id, title, thesis, prove, discipline, counter, sections, extra_q, steps, pass_md, fail_md, verdict,
       res, reframe, deliverable, depth, read_min=22, prove_h="2", disagree="none found between the sources read.", thin=None, short=None):
    secs, qs = [], []
    for (st, fr, body, fm, xr, one) in sections:
        lab, txt, fix, sym = fm
        secs.append(dict(title=st, framing=fr, body=T(body), fm=[(lab, txt, fix)], xr=xr, one=one))
        qs.append((sym + " Name the failure mode by its exact label.", "**%s.** %s" % (lab, fix.split(". ")[0].rstrip("."))))
    qs += extra_q
    for (st, fr, body, fm, xr, one) in sections:
        if len(qs) >= 11:
            break
        qs.append(("State the fix for the failure mode labelled \"%s\"." % fm[0], fm[2]))
    rows = "\n".join("| %s | %s | %s |" % r for r in res)
    resources = "| Source | Title | What it proves |\n|---|---|---|\n" + rows + "\n\n*Disagreement named:* " + disagree
    s = dict(mod=mod, id=id, title=title, short=short or title, thesis=thesis, prove=prove, discipline=discipline,
             counter=counter, read_min=read_min, prove_h=prove_h, depth=depth, deliverable=deliverable, sections=secs,
             retrieval=qs, steps=steps, pass_md=T(pass_md), fail_md=T(fail_md), verdict=verdict, resources=resources, reframe=reframe)
    if thin:
        s["thin"] = thin
    return s


def run(SPECS):
    for s in SPECS:
        write(s)
