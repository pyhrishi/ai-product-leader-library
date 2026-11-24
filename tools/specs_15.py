import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen import write
from specs_12 import T

M = "b-1-5"
SPECS = []

SPECS.append(dict(
 mod=M, id="1.5.1", title="Core terms: 23 words in five layers", short="Core terms: 23 words in five layers",
 thesis="Every term in Claude Code belongs to a layer of the loop, and knowing the layer is what separates a definition from understanding.",
 prove="define 23 terms from memory, place each on the loop, and score yourself against the Glossary.",
 discipline="attach a loop location and a separating fact to every definition.",
 counter="a glossary is not understanding; a term you can define but cannot place on the loop is a term you will misuse.",
 read_min=25, prove_h="3", depth=["Define every core term in a sentence and name its layer", "Tell apart the look-alike pairs", "Write a team glossary and retire stale names"],
 deliverable="A 23-term sheet with layer, separating fact and a marked self-score.",
 sections=[
 dict(title="Loop and context terms", framing="The terms that describe what happens inside a session [Claude Code docs, Glossary, 2026].",
  body=T("""
| Term | Definition | Separating fact |
|---|---|---|
| Agentic loop | Gather context, act, verify, repeat | A turn is one pass from your message to Claude finishing |
| Context window | Working memory of a session | `/clear` makes a new session with a new window |
| Compaction | Summarising when the window nears its limit | Project-root CLAUDE.md reloads; conversation-only rules may not |
| Session | A conversation tied to a directory, stored under `~/.claude/projects/` | Resumable and forkable |
| Checkpoint | A restore point per turn | Separate from git; misses Bash changes |
"""),
  fm=[("Glossary-as-understanding", "You can recite a definition but cannot say where the term acts in the loop, so you misapply it.", "Attach a loop location to every term as part of its definition.")],
  xr="the loop is Module 1.2.1; context is Module 1.2.4.", one="a term without a loop location is a quote."),
 dict(title="Memory and extension terms", framing="Persistent instructions and the extension surface [Claude Code docs, Glossary, 2026].",
  body=T("""
| Term | Definition | Separating fact |
|---|---|---|
| CLAUDE.md | Instructions you write, loaded at start | You write it; auto memory is what Claude writes |
| Auto memory | Notes Claude writes; first 200 lines or 25 KB of MEMORY.md load | Worktrees of one repo share one memory directory |
| Rules | Files in `.claude/rules/`, optionally path-scoped | Path-scoped rules load when a matching file is read |
| Skill | A `SKILL.md` playbook | Recommended successor to custom commands |
| Subagent | Specialist in its own context | Stays inside the session |
| Hook | Handler at a fixed lifecycle point | CLAUDE.md is advisory; a hook always fires |
| MCP | Open standard for connecting tools and data | A connector is a server added to your claude.ai account |
| Plugin | Bundle of skills, hooks, subagents and MCP servers | Skills are namespaced plugin:skill |
| Marketplace | Catalogue for distributing plugins | Detail in Module 5.6 |
| Mod | A customisation unit | The Glossary page read did not define it; see Module 5.7 |
"""),
  fm=[("Look-alike conflation", "You treat two similar terms as one (cloud session and Remote Control, subagent and agent team) and pick the wrong feature.", "Ask the separating question: who can talk to whom, where does the code run, advisory or deterministic.")],
  xr="memory is Module 3.2; extensions are Part 5.", one="ask the separating question first."),
 dict(title="Safety, scale and automation terms", framing="Control, isolation and multi-session work [Claude Code docs, Glossary, 2026].",
  body=T("""
| Term | Definition | Separating fact |
|---|---|---|
| Permission mode | Baseline approval behaviour | Rules refine it, deny then ask then allow |
| Sandbox | OS-level filesystem and network isolation for Bash | A layer separate from rules |
| Worktree | An isolated git worktree under `.claude/worktrees/` | Separate branch, separate directory |
| Non-interactive mode | Runs with `-p`; formerly headless mode | Renamed; same flag |
| Agent SDK | Python and TypeScript library on the same engine | `claude -p` is scripting; the SDK is code you write |
| Agent team | Several sessions with a shared task list and peer messaging | Experimental, off by default |
| Dynamic workflow | Multi-step automated workflow | Verification loop is its prerequisite |
| Agent view | View for background and parallel sessions | Not defined on the page read; see Module 6.3 |
| Channel | MCP server that pushes events into a running session | Differs from Remote Control |
"""),
  fm=[("Stale-term search", "You search for an old name, get outdated pages and follow them.", "Translate through the renamed-terms table first and search the current name.")],
  xr="automation is Part 6; sandbox is Module 4.4.", one="search the current name."),
 dict(title="Look-alikes and renames", framing="Four pairs cause most mistakes, and four names have changed [Claude Code docs, Glossary, 2026].",
  body=T("""
| Pair | Left | Right | Separator |
|---|---|---|---|
| Cloud vs remote | Cloud session runs on cloud infrastructure | Remote Control drives a local session | Where the code runs |
| Command vs skill | `/name` you type | `SKILL.md` playbook | Skills add invocation control |
| Subagent vs team | Inside one session | Separate sessions | Who can talk to whom |
| CLAUDE.md vs memory | You write | Claude writes | Author |

| Old term | Now called |
|---|---|
| Headless mode | Non-interactive mode |
| Web session | Cloud session |
| Custom commands | Skills |
| Slash commands | Commands |
"""),
  fm=[("Renamed-term lag", "You keep using an old name in prompts, docs and teaching, and teammates search for the wrong thing.", "Use the current name and keep a renames table in the team glossary.")],
  xr="surfaces are Module 7.1; skills are Module 5.2.", one="renames arrive by release."),
 ],
 retrieval=[
  ("Define compaction and say what survives it.", "Summarising when the window nears its limit; project-root CLAUDE.md reloads from disk."),
  ("You recite definitions but misapply terms. Name the failure mode by its exact label.", "**Glossary-as-understanding.**"),
  ("You mix up cloud session and Remote Control. Name the failure mode and separator.", "**Look-alike conflation.** Where the code runs."),
  ("Which term replaced headless mode?", "Non-interactive mode."),
  ("You search an old name and follow outdated pages. Name the failure mode.", "**Stale-term search.**"),
  ("Who writes CLAUDE.md and who writes auto memory?", "You write CLAUDE.md; Claude writes auto memory."),
  ("You still say slash commands in team docs. Name the failure mode.", "**Renamed-term lag.**"),
  ("Which two terms did the Glossary page read not define?", "Mod and agent view."),
  ("What is the separator between subagent and agent team?", "Who can talk to whom."),
 ],
 steps=[("Without looking, write one sentence for each of the 23 terms", "`terms.md`"), ("Draw the loop and place each term", "`loop-terms.png`"), ("Write the separating fact for five pairs", "Five rows"),
        ("Reopen the Glossary and mark each sentence correct, partial or wrong", "Marked copy"), ("Write the four renamed terms with correction sentences", "Four sentences"), ("Redo after a week and compare", "Two scores")],
 pass_md=T("""
| Term | Your sentence | Verdict |
|---|---|---|
| Compaction | Summarises near the limit; root CLAUDE.md reloads | Correct |
| Subagent | Helper in its own context, stays in session | Correct |
"""),
 fail_md=T("""
| Term | Your sentence | What is wrong |
|---|---|---|
| Hook | "Runs sometimes" | Misses determinism: **Glossary-as-understanding** |
| Cloud session | "Remote Control" | **Look-alike conflation** |
"""),
 verdict="The artifact passes only if the first attempt was made without looking and wrong sentences were kept alongside the corrections.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Claude Code Glossary | Definitions and renamed terms | Current |
| Anthropic | How Claude Code works | The loop organising the terms | Current |
""") + "\n\n*Disagreement named:* none found.",
 reframe="This is the craft of vocabulary: **a definition, a layer, a separating fact.** The engineer who understands this does not ask \"what does that word mean?\" — they ask \"where does it act, and what is it not?\"",
))

SPECS.append(dict(
 mod=M, id="1.5.2", title="Where to look: the right source for each question", short="Where to look: the right source for each question",
 thesis="Different questions have different sources of truth, and the product itself outranks any copy of its docs.",
 prove="answer five questions each from the right source and say why the others were wrong.",
 discipline="link to official pages instead of copying text, and date what you copy.",
 counter="the most convenient source is the most likely to be stale; a mirror or blog can be right yesterday and wrong today.",
 read_min=12, prove_h="1.5", depth=["Pick the source for a question type", "Detect a stale or wrong-scope source", "Maintain a team link sheet with review dates"],
 deliverable="A question-to-source table tested on five real questions.",
 sections=[
 dict(title="The source map", framing="Each question type has a primary source.",
  body=T("""
| You need | Go to | Why |
|---|---|---|
| A Claude Code term | Claude Code Glossary | Entries link to deep pages |
| A model-level concept | Platform glossary | Tokens, temperature, RAG |
| Desktop-app terms | Claude Help Center | DXT, MCPB |
| The page list | `code.claude.com/docs/llms.txt` | Docs index |
| Live behaviour | `/help`, `/context`, `/memory`, `claude doctor` | Your version, your session |
| What changed | `/release-notes` | Renames arrive by release |
"""),
  fm=[("Wrong-glossary lookup", "You look up a model concept in the Claude Code glossary or a Desktop term in the platform glossary and find nothing.", "Use the platform glossary for model concepts and the Help Center for Desktop terms.")],
  xr="in-product help is Module 1.3.6.", one="match the question to the glossary."),
 dict(title="Source-of-truth ranking", framing="When sources disagree, rank them: your running product, then official docs, then official blog or help, then secondary sources, then mirrors.",
  body=T("""
| Rank | Source | Use |
|---|---|---|
| 1 | Your running product | Behaviour on your version |
| 2 | Official docs | Definitions, flags, limits |
| 3 | Help Center | Plan and account questions |
| 4 | Secondary articles | Context; verify before use |
| 5 | Mirrors and forums | Leads only |
"""),
  fm=[("Source-of-truth drift", "A copied table in your wiki goes stale and nobody knows which line is current.", "Date entries, review after each release with `/release-notes`, and link to official pages instead of copying text.")],
  xr="release notes are Module 1.3.5.", one="the product beats the page."),
 dict(title="Reading the docs efficiently", framing="The docs index at `code.claude.com/docs/llms.txt` lists pages for discovery, and each Glossary entry links to its deep page.",
  body=T("""
| Task | Method |
|---|---|
| Find a page | Read `llms.txt` and search it |
| Check a flag | Open the CLI reference page |
| Confirm a version note | Read the page's minimum-version line |
"""),
  fm=[("Excerpt-trust", "You rely on a search excerpt of a long page and miss the clause that changes the answer.", "Open the full page for anything you will standardise on.")],
  xr="troubleshooting is Part 12.", one="excerpts find; pages confirm."),
 dict(title="A team link sheet", framing="A short link sheet gives everyone the same sources.",
  body=T("""
| Column | Content |
|---|---|
| Question type | Terms, limits, install, billing |
| Source | Official page URL |
| Last reviewed | Date |
| Version checked | `claude --version` output |
"""),
  fm=[("Link-sheet rot", "The link sheet is created once and never reviewed, so it points at moved pages.", "Add a review date and re-check after each release.")],
  xr="team practice is in Part 11.", one="date it, review it."),
 ],
 retrieval=[
  ("Where do model-level concepts live?", "The platform glossary."),
  ("You search the Claude Code glossary for temperature. Name the failure mode by its exact label.", "**Wrong-glossary lookup.**"),
  ("Where is the docs page index?", "`code.claude.com/docs/llms.txt`."),
  ("A copied wiki table goes stale. Name the failure mode.", "**Source-of-truth drift.**"),
  ("You trust a search excerpt. Name the failure mode.", "**Excerpt-trust.**"),
  ("Which source outranks the docs?", "Your running product."),
  ("A link sheet with no review dates. Name the failure mode.", "**Link-sheet rot.**"),
  ("Which command shows what changed in your version?", "`/release-notes`."),
 ],
 steps=[("Write five real questions you have had", "List"), ("Answer each from the right source", "Five answers"), ("Record which wrong source tempted you", "Notes"),
        ("Check one answer against your running product", "Test"), ("Build a link sheet with review dates", "`links.md`")],
 pass_md=T("""
| Question | Source | Wrong source avoided |
|---|---|---|
| What is compaction? | Glossary | Blog |
| Is my install healthy? | `claude doctor` | Forum |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| All answers from one blog | **Source-of-truth drift** risk |
"""),
 verdict="The artifact passes only if one answer was confirmed against your running product.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Claude Code Glossary | Term definitions | Current |
| Anthropic | Platform glossary | Model terms | Current; not fetched this session |
| Claude Help Center | Desktop terms | DXT, MCPB | Current; not fetched this session |
""") + "\n\n*Disagreement named:* mirrors of the docs sometimes differ from the live pages. **The live official page wins.**",
 reframe="This is the craft of finding answers: **match the question to the source and trust your running product first.** The engineer who understands this does not ask \"what does the internet say?\" — they ask \"which source owns this question?\"",
))

if __name__ == "__main__":
    for s in SPECS:
        write(s)
