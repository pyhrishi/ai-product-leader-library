import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen import write


def T(rows):
    return rows.strip()


def sec(title, framing, body, fm, xr, one):
    return dict(title=title, framing=framing, body=T(body), fm=[fm], xr=xr, one=one)


def tbl(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    for r in rows:
        out.append("| " + " | ".join(r) + " |")
    return "\n".join(out)


def resources(rows, dis="none found between the sources read."):
    t = tbl(["Source", "Title", "What it proves", "2026 status"], rows)
    return t + "\n\n*Disagreement named:* " + dis


def G(mod, id, title, thesis, prove, discipline, counter, read_min, prove_h, depth, deliverable,
      sections, retrieval, steps, pass_md, fail_md, verdict, res, reframe, thin=None, short=None):
    d = dict(mod=mod, id=id, title=title, short=short or title, thesis=thesis, prove=prove,
             discipline=discipline, counter=counter, read_min=read_min, prove_h=prove_h, depth=depth,
             deliverable=deliverable, sections=sections, retrieval=retrieval, steps=steps,
             pass_md=pass_md, fail_md=fail_md, verdict=verdict, resources=res, reframe=reframe)
    if thin:
        d["thin"] = thin
    return d


def run(SPECS):
    for s in SPECS:
        write(s)
