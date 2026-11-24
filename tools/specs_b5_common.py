import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen import write

def T(rows):
    return rows.strip()

def sec(title, framing, body, fm, xr, one):
    return dict(title=title, framing=framing, body=T(body), fm=[fm], xr=xr, one=one)

def res(rows, disagreement="none found between the sources read."):
    head = "| Source | Title | What it proves | 2026 status |\n|---|---|---|---|\n"
    return head + "\n".join("| %s | %s | %s | %s |" % r for r in rows) + "\n\n*Disagreement named:* " + disagreement

def guide(mod, id, title, thesis, prove, discipline, counter, read_min, prove_h, depth, deliverable,
          sections, retrieval, steps, pass_md, fail_md, verdict, resources, reframe, thin=None):
    d = dict(mod=mod, id=id, title=title, short=title, thesis=thesis, prove=prove, discipline=discipline,
             counter=counter, read_min=read_min, prove_h=prove_h, depth=depth, deliverable=deliverable,
             sections=sections, retrieval=retrieval, steps=steps, pass_md=T(pass_md), fail_md=T(fail_md),
             verdict=verdict, resources=resources, reframe=reframe)
    if thin: d["thin"] = thin
    return d

def run(specs):
    for s in specs:
        write(s)
