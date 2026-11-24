import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen import write
from specs_12 import T

CTX = "Claude Code docs, Context window"
MEM = "Claude Code docs, Memory"
CACHE = "Claude Code docs, Prompt caching"
FEAT = "Claude Code docs, Extend Claude Code"
BP = "Claude Code docs, Best practices"
HOW = "Claude Code docs, How Claude Code works"
LARGE = "Claude Code docs, Large codebases"
SL = "Claude Code docs, Status line"
OS = "Claude Code docs, Output styles"
FS = "Claude Code docs, Fullscreen rendering"
AX = "Claude Code docs, Accessibility"
DIR = "Claude Code docs, .claude directory"
MC = "Claude Code docs, Model configuration"


def sec(title, framing, body, lab, txt, fix, xr, one):
    return dict(title=title, framing=framing, body=T(body), fm=[(lab, txt, fix)], xr=xr, one=one)


def tbl(head, rows):
    return "| " + " | ".join(head) + " |\n|" + "---|" * len(head) + "\n" + "\n".join("| " + " | ".join(r) + " |" for r in rows)


def G(mod, id, title, thesis, prove, disc, counter, rmin, ph, depth, deliverable, secs, retr, steps,
      passh, passr, failr, verdict, res, disagree, reframe, thin=None):
    d = dict(mod=mod, id=id, title=title, short=title, thesis=thesis, prove=prove, discipline=disc, counter=counter,
             read_min=rmin, prove_h=ph, depth=depth, deliverable=deliverable, sections=secs, retrieval=retr,
             steps=steps,
             pass_md=tbl(passh, passr),
             fail_md=tbl(["Element", "What is wrong"], failr),
             verdict=verdict,
             resources=tbl(["Source", "Title", "What it proves", "2026 status"], res) + "\n\n*Disagreement named:* " + disagree,
             reframe=reframe)
    if thin:
        d["thin"] = thin
    return d


def run(SPECS):
    for s in SPECS:
        write(s)
