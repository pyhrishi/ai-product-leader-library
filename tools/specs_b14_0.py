"""Shared helpers for the b-14/16/17/18 spec files (compact spec builders)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen import write


def T(s):
    return s.strip()


def S(title, framing, body, lab, txt, fix, xr, one):
    return dict(title=title, framing=framing, body=T(body), fm=[(lab, txt, fix)], xr=xr, one=one)


def RES(rows, dis):
    head = "| Source | Title | What it proves | 2026 status |\n|---|---|---|---|\n"
    return head + "\n".join("| %s | %s | %s | %s |" % r for r in rows) + "\n\n*Disagreement named:* " + dis


def RF(craft, bold, notask, ask):
    return 'This is the craft of %s: **%s.** The engineer who understands this does not ask "%s" — they ask "%s"' % (craft, bold, notask, ask)


def G(mod, id, title, thesis, prove, discipline, counter, read_min, prove_h, depth, deliverable, sections,
      retrieval, steps, pass_md, fail_md, verdict, resources, reframe, thin=None):
    d = dict(mod=mod, id=id, title=title, short=title, thesis=thesis, prove=prove, discipline=discipline,
             counter=counter, read_min=read_min, prove_h=prove_h, depth=depth, deliverable=deliverable,
             sections=sections, retrieval=retrieval, steps=steps, pass_md=T(pass_md), fail_md=T(fail_md),
             verdict=verdict, resources=resources, reframe=reframe)
    if thin:
        d["thin"] = thin
    return d


def run(SPECS):
    for s in SPECS:
        write(s)
