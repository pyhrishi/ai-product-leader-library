from specs_b2_common import *

M = "b-2-1"
SPECS = []
BP = "Claude Code docs, Best practices, 2026"
PM = "Claude Code docs, Permission modes, 2026"
CW = "Claude Code docs, Common workflows, 2026"
PL = "Claude Code docs, Prompt library, 2026"

# ---------------------------------------------------------------- 2.1.1 EXPLORE
SPECS.append(G(M, "2.1.1", "Explore: read before you change",
 thesis="Exploration is the cheapest phase of any change: you ask questions, Claude reads code, and nothing on disk moves, so every wrong assumption is caught for the price of a few messages instead of a bad diff.",
 prove="run a read-only exploration of a repo you did not write and produce a one-page map whose every claim cites a file you opened yourself.",
 discipline="make exploration read-only by construction (plan mode), not by promise.",
 counter="exploration is not free in a subagent: delegated reads cost tokens and can finish slower than asking in place [Claude Code docs, Best practices, 2026].",
 read_min=20, prove_h="2", depth=["Ask orientation questions and enter plan mode", "Predict what plan mode lets a shell command do in your session", "Route broad searches to the right context and verify the summary"],
 deliverable="A one-page codebase map from a read-only session, with each claim linked to a file you spot-checked.",
 sections=[
 S("Questions a senior engineer would ask",
   "The docs' own recipes for a new codebase start broad and narrow down: an overview, then architecture patterns, data models, and how a concern such as authentication is handled [Claude Code docs, Common workflows, 2026]. The prompt library carries the same shapes as copy-paste prompts, including a change-impact question and a history question [Claude Code docs, Prompt library, 2026].",
   """
| Goal | Prompt shape (from the docs) |
|---|---|
| Orient | `give me an overview of this codebase` |
| Locate | `find the files that handle user authentication` |
| Trace | `trace the login process from front-end to database` |
| Impact | `what would break if I deleted {target}?` |
| History | `look through the commit history of {path} and summarize how it evolved and why` |
| Scope | `which files would I need to touch to {change}?` |

The page's tips: start with broad questions then narrow, use the project's domain language, and request a glossary of project terms [Claude Code docs, Common workflows, 2026].
""",
   "Question-sprawl", "You fire ten unrelated orientation questions in a row, the answers pile up in one context, and none of them converges on the change you actually need.", "Pick the one change you intend to make, then ask the locate, trace and impact questions for that change only.",
   "prompting detail is Module 2.2; context cost is Module 3.1.", "ask about the change you are about to make, not about the whole repo."),
 S("Read-only by construction: plan mode",
   "Plan mode tells Claude to research and propose changes without making them: it reads files, runs shell commands to explore and writes a plan, but does not edit source [Claude Code docs, Permission modes, 2026]. Enter it with `Shift+Tab`, prefix one prompt with `/plan`, or start with `claude --permission-mode plan` [Claude Code docs, Permission modes, 2026].",
   """
What a shell command may do during planning depends on the session, and the first matching case applies [Claude Code docs, Permission modes, 2026]:

| Session | Planning shell commands |
|---|---|
| Interactive terminal, bypass permissions available | Neither classifier nor prompt applies |
| Auto mode available and `useAutoModeDuringPlan` on (the default) | Classifier reviews commands other than critical-path removals |
| Auto mode unavailable, or setting off | Commands outside the built-in read-only set prompt you |

```bash
claude --permission-mode plan      # start read-only
# or inside a session: Shift+Tab until the bar shows  ⏸ plan mode on
```
""",
   "Plan-mode-as-sandbox", "You assume plan mode blocks every side effect, but shell commands still run under the classifier or a prompt, so an exploratory command with a side effect can execute.", "Read the three cases above for your session, and keep deny rules and the sandbox for anything that must never run.",
   "mode cycling is Module 4.3; sandboxing is Module 4.4.", "plan mode blocks source edits, not every command."),
 S("Keeping exploration out of the main window",
   "Broad codebase searches go to the built-in Explore agent, and the subagent keeps long output out of your main conversation. The docs are plain about the price: every subagent sends its own requests against the same usage, and a fresh subagent must gather context your conversation already had, so it can be slower [Claude Code docs, Best practices, 2026].",
   """
| Choose | When |
|---|---|
| Ask in place | The answer needs two or three file reads you will keep using |
| Subagent / Explore | A wide search whose raw output you will not reuse |
| Code intelligence plugin | A typed language where go-to-definition beats text search [Claude Code docs, Common workflows, 2026] |

```text
use a subagent to investigate how our auth system handles token refresh
```
That prompt is the docs' example of delegating research so only the findings return [Claude Code docs, Common workflows, 2026].
""",
   "Explore-tax blindness", "You delegate every question to a subagent assuming it is free, and usage rises while your main window gains nothing you will reuse.", "Delegate only wide, read-heavy searches and check `/usage` to see which subagent types earn their cost.",
   "subagent mechanics are Module 5.3; usage is Module 1.4.", "delegate the search you will not re-read."),
 S("Turning exploration into something you can trust",
   "An exploration summary is a claim about files, and the docs' test for what is worth writing down applies in reverse: if Claude could find it by reading the code, check it there [Claude Code docs, Best practices, 2026]. The useful output of this phase is a short list of facts with paths, because the plan phase consumes exactly that.",
   """
| Artifact | Contents | Checked by |
|---|---|---|
| Map | Entry points, data flow, the files a change would touch | You open three of them |
| Unknowns | What exploration could not answer | Becomes interview questions (guide 2.1.6) |
| Constraints | Conventions, tests, the check command | Goes into the plan |
""",
   "Unchecked-summary", "You accept a fluent overview whose file names you never opened, and the plan inherits a hallucinated entry point.", "Open at least three cited files before planning and ask Claude to correct any path that does not exist.",
   "verification habits are Module 2.3; planning is the next guide.", "a map you did not spot-check is a guess."),
 ],
 retrieval=[
  ("Which three entry points start plan mode?", "`Shift+Tab`, a `/plan` prefix on one prompt, or `claude --permission-mode plan`."),
  ("You assume plan mode stops every shell side effect. Name the failure mode by its exact label.", "**Plan-mode-as-sandbox.**"),
  ("In plan mode with auto mode available and `useAutoModeDuringPlan` on, who reviews shell commands?", "The auto mode classifier reviews them instead of prompting you, except critical-path removals."),
  ("You delegate every question to a subagent and usage rises. Name the failure mode and the first check.", "**Explore-tax blindness.** Check `/usage` by subagent type."),
  ("What does the status bar show in plan mode?", "`⏸ plan mode on`."),
  ("Ten unrelated orientation questions pile up. Name the failure mode.", "**Question-sprawl.**"),
  ("Which built-in agent takes broad codebase searches?", "Explore."),
  ("You build a plan from an overview whose files you never opened. Name the failure mode by its exact label.", "**Unchecked-summary.**"),
  ("How many cited files should you open before planning, per this guide, and why?", "At least three, because a summary is a claim about files and a plan inherits its errors."),
  ("Name the tip that makes orientation questions land better.", "Use the project's domain language and start broad before narrowing."),
 ],
 steps=[("Pick a repo you did not write and a change you could plausibly make", "One-line change statement"), ("Start with `claude --permission-mode plan` and ask the overview question", "Overview transcript"),
        ("Ask locate, trace and impact questions for that change only", "Three answers"), ("Record which mode and rule cases applied to the shell commands Claude ran", "A case label per command"),
        ("Open three cited files and mark each claim true or false", "Verification column"), ("Write the one-page map with unknowns listed", "`map.md`")],
 pass_md="""
| Claim | File | Opened by me | True |
|---|---|---|---|
| Login is handled in the auth middleware | `src/auth/middleware.ts` | Yes | Yes |
| Tokens refresh in a shared helper | `src/auth/refresh.ts` | Yes | Partly: also in a hook |
| Unknown: who owns session expiry | none | n/a | Listed as unknown |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Overview pasted as the map | **Unchecked-summary** |
| No mode noted for shell commands | **Plan-mode-as-sandbox** risk |
""",
 verdict="The artifact passes only if every claim names a file, at least three files were opened by you, and unknowns are listed rather than guessed.",
 res=R([("Anthropic", "Common workflows", "Orientation recipes and tips", "Current; read in full"), ("Anthropic", "Permission modes", "Plan mode and shell-command cases", "Current; first 100,000 of 117,027 characters read"),
        ("Anthropic", "Best practices", "Subagent cost and when delegation pays", "Current; read in full")],
       "the current Best practices page no longer lays out a named explore-plan-implement-commit sequence, while this module and the plan-mode page do. **The plan-mode page and recipes are what this guide relies on.**"),
 reframe="This is the craft of exploring: **ask about the change you intend, keep it read-only, and trust only what you opened.** The engineer who understands this does not ask \"what does this repo do?\" — they ask \"which files does this change touch, and have I seen them?\"",
))

# ---------------------------------------------------------------- 2.1.2 PLAN
SPECS.append(G(M, "2.1.2", "Plan: write it, edit it, approve it",
 thesis="A plan is a reviewable artifact that sits between exploration and edits, and the approval prompt, the editor shortcut and the context choice are the three controls that decide whether it earns its cost.",
 prove="get a plan from plan mode, edit it in your own editor with Ctrl+G, approve it with a deliberate option, and show what changed in the session mode.",
 discipline="never approve a plan you have not read and edited at least once.",
 counter="approving a plan changes the permission mode of the whole session, so the choice you click is a security decision as well as a workflow one [Claude Code docs, Permission modes, 2026].",
 read_min=20, prove_h="2", depth=["Name the approval options and the editing shortcut", "Predict the mode after each approval choice", "Design a plan-review habit that scales to a team"],
 deliverable="A plan edited by you, the approval option you chose, and a one-line statement of the resulting permission mode.",
 sections=[
 S("What a plan is and where it lives",
   "In plan mode Claude researches and then presents a plan and asks how to proceed; source edits stay blocked until you approve [Claude Code docs, Permission modes, 2026]. The permission-modes page does not give a dedicated plan-file location, it only notes under protected paths that the session's plan files live in `~/.claude/plans/` or in the `plansDirectory` you set [Claude Code docs, Permission modes, 2026].",
   """
| Fact | Detail |
|---|---|
| Entering | `Shift+Tab`, `/plan [description]`, or `--permission-mode plan` |
| Leaving without approving | `Shift+Tab` again |
| Plan file directory | `~/.claude/plans/` or `plansDirectory` [from a protected-paths note, not a dedicated section] |
| Default mode setting | `"permissions": {"defaultMode": "plan"}` in `.claude/settings.json` |

`/plan fix the auth bug` enters plan mode and starts on that task in one step [Claude Code docs, Commands, 2026].
""",
   "Plan-in-chat-only", "You treat the plan as a chat message and never open the file, so a plan that should have been saved and reviewed is lost at the next compaction.", "Open the plan with `Ctrl+G` or find it under the plans directory and keep the final version in the repo when it will guide a later session.",
   "context survival is Module 3.1; repo-level instructions are Module 3.2.", "the plan is a file, so treat it like one."),
 S("Editing the plan yourself",
   "Press `Ctrl+G` to open the proposed plan in your default text editor and edit it directly before Claude proceeds [Claude Code docs, Permission modes, 2026]. The interactive-mode page lists the same key as opening the prompt in your editor, with `Ctrl+X Ctrl+E` as the readline-native binding [Claude Code docs, Interactive mode, 2026].",
   """
Edits worth making, in order of value:

| Edit | Why |
|---|---|
| Delete steps outside scope | Removes the quiet scope creep |
| Reorder so tests come first | Gives the implement phase a check |
| Add the verification command | Closes the loop (Module 2.3) |
| Add a `Do not touch:` list | Turns a convention into a boundary |
""",
   "Rubber-stamp-plan", "You press approve on a plan whose steps you skimmed, and Claude executes a step you would have deleted.", "Make at least one edit, even a deletion, so approval is evidence that you read the plan.",
   "verification is Module 2.3; prompting scope is Module 2.2.", "if you changed nothing, you probably did not read it."),
 S("The approval prompt is a mode switch",
   "When the plan is ready Claude asks how to proceed, and approving exits plan mode and switches the session to the mode the option describes [Claude Code docs, Permission modes, 2026].",
   """
| Option as worded in the docs | Resulting mode |
|---|---|
| Yes, and use auto mode | Auto mode |
| Yes, auto-accept edits (shown when auto is unavailable) | Accept edits |
| Yes, and switch to BYPASS PERMISSIONS ... (shown if the session started with bypass enabled) | Bypass permissions |
| Yes, manually approve edits | Edits prompt one by one |
| No, keep planning | Stay in plan mode |

With `showClearContextOnPlanAccept` enabled the list gains a first option that approves and clears planning context. Accepting also titles the session from the plan unless you already named it [Claude Code docs, Permission modes, 2026].
""",
   "Approve-as-default", "You click the first option every time, and the session quietly moves into a mode with fewer prompts than the work deserves.", "Read the option text, pick the mode on purpose, and choose manual approval for plans that touch migrations or deploy config.",
   "modes are Module 4.3; the mode baseline is Module 1.2.", "the approve button chooses your permission mode."),
 S("Replanning and when planning is overhead",
   "To plan again, cycle back with `Shift+Tab` or prefix the next prompt with `/plan` [Claude Code docs, Permission modes, 2026]. A plan helps most when the path is uncertain or crosses files; for a change you can state in one diff it is overhead (guide 2.1.5).",
   """
```text
/plan the migration touches three services; propose steps, name the tests that prove each step, and list what you will NOT change
```
| Signal | Action |
|---|---|
| Plan keeps growing | Split it; approve step one only |
| Plan contradicts what you learned | `No, keep planning` and say why |
| Plan was approved but implementation drifts | Esc, rewind, re-plan from the checkpoint (Module 2.5) |
""",
   "Plan-sprawl", "The plan grows to dozens of steps nobody can review, so approval becomes a formality and the implement phase runs unattended.", "Split the plan into stages with a check at each boundary and approve only the next stage.",
   "checkpoints are Module 2.5; unattended runs are Module 6.7.", "a plan you cannot review is not a plan."),
 ],
 retrieval=[
  ("Which key opens the proposed plan in your text editor?", "`Ctrl+G`."),
  ("Name the approval option that stays in plan mode.", "`No, keep planning`."),
  ("You approve every plan by clicking the first option. Name the failure mode by its exact label.", "**Approve-as-default.**"),
  ("Which setting adds an approve-and-clear-context option?", "`showClearContextOnPlanAccept`."),
  ("Where do session plan files live by default?", "`~/.claude/plans/` or the `plansDirectory` you set, per a protected-paths note."),
  ("You approve a plan without changing a word. Name the failure mode.", "**Rubber-stamp-plan.**"),
  ("The plan has grown past what you can review. Name the failure mode and fix.", "**Plan-sprawl.** Split into stages and approve only the next."),
  ("What does accepting a plan do to an unnamed session?", "Gives it a generated title based on the plan."),
  ("What does `/plan fix the auth bug` do?", "Enters plan mode and starts on that task immediately."),
  ("You never open the plan file and lose it at compaction. Name the failure mode by its exact label.", "**Plan-in-chat-only.**"),
 ],
 steps=[("Enter plan mode and request a plan for a real change", "Plan v1"), ("Open it with `Ctrl+G`; delete one step, add the check command, add a do-not-touch list", "Plan v2"),
        ("Diff v1 and v2", "Edit list"), ("Pick an approval option on purpose; note the mode shown after", "Mode line"),
        ("Find the plan file on disk", "Path"), ("State what you would choose for a migration and why", "Two sentences")],
 pass_md="""
| Item | Evidence |
|---|---|
| Plan edited | v1 to v2 diff shows 3 edits |
| Check command in plan | `pnpm tsc --noEmit` listed per stage |
| Approval option | Manual edits; status bar confirms |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Plan v1 equals v2 | **Rubber-stamp-plan** |
| Mode after approval not recorded | **Approve-as-default** |
""",
 verdict="The artifact passes only if the plan changed between v1 and v2 and the resulting permission mode is named from the status bar.",
 res=R([("Anthropic", "Permission modes", "Plan mode, approval options, Ctrl+G", "Current; first 100,000 of 117,027 characters read"), ("Anthropic", "Interactive mode", "Editor shortcut bindings", "Current; read via a saved copy"),
        ("Anthropic", "Commands", "`/plan` behaviour", "Current")],
       "none found between the sources read."),
 reframe="This is the craft of planning: **an artifact you edit, an approval that sets your mode, and stages you can review.** The engineer who understands this does not ask \"is the plan good?\" — they ask \"what did I change in it, and what mode did I just grant?\"",
))

# ---------------------------------------------------------------- 2.1.3 IMPLEMENT
SPECS.append(G(M, "2.1.3", "Implement: code against the plan, with tests",
 thesis="Implementation is the phase where Claude edits files, and it goes well when the plan, a test and a check command are all in front of it, and badly when the only definition of done is that it looks finished.",
 prove="implement one planned change test-first, show the failing test, the passing run, and the diff that links them.",
 discipline="start implementation from a check Claude can run.",
 counter="Claude stops when the work looks done, so a plan without a runnable check produces confident, unverified output [Claude Code docs, Best practices, 2026].",
 read_min=19, prove_h="2.5", depth=["Switch out of plan mode and run a staged implementation", "Choose test-first or test-after for a given change", "Design stage boundaries with checks for an unattended run"],
 deliverable="A staged implementation with a failing-then-passing test and a per-stage check log.",
 sections=[
 S("Leaving plan mode deliberately",
   "Approving a plan exits plan mode and switches the session to the mode of the option you chose, after which Claude starts editing [Claude Code docs, Permission modes, 2026]. `Shift+Tab` cycles modes and the status bar shows which is active [Claude Code docs, Permission modes, 2026].",
   """
| Status bar text | Mode |
|---|---|
| `⏸ manual mode on` | `default` (Manual) |
| `⏵⏵ accept edits on` | `acceptEdits` |
| `⏸ plan mode on` | `plan` |
| `⏵⏵ auto mode on` | `auto` |
| `⏵⏵ bypass permissions on` | `bypassPermissions` |

The built-in default is `auto` for interactive terminal and VS Code sessions from v2.1.283; `claude -p` and the Agent SDK default to Manual [Claude Code docs, Permission modes, 2026].
""",
   "Mode-blind-edit", "You begin implementation without looking at the status bar and discover the session is in a more permissive mode than the task deserved.", "Read the status bar after every approval and switch with `Shift+Tab` before the first edit.",
   "the baseline is Module 1.2; mode choice is Module 4.3.", "check the mode before the first edit."),
 S("Test first or check after",
   "The prompt library carries both orders: `write tests for {feature} first, then implement it until they pass` and `write tests for {path}, run them, and fix any failures` [Claude Code docs, Prompt library, 2026]. Best practices lists the checks Claude can read: a test file, a build exit code, a linter, a script diffing against a fixture, a browser screenshot [Claude Code docs, Best practices, 2026].",
   """
| Order | Use when | Risk |
|---|---|---|
| Test first | Behaviour is specifiable now | Tests mirror a wrong spec |
| Check after | Existing behaviour must not change (refactor) | Tests rewritten to pass |
| Screenshot compare | UI work | Compares pixels, not behaviour |

```text
write tests for the rate limiter first, then implement it until they pass. do not edit the tests once they are committed to the plan.
```
""",
   "Test-bending", "Claude edits the failing test to match its code instead of fixing the code, and the suite goes green on a wrong implementation.", "Tell Claude the tests are fixed once planned, review test diffs separately, and run `git diff` on test files before accepting.",
   "test-driven work is Module 9.2; verification is Module 2.3.", "a green suite means nothing if the tests moved."),
 S("Stages and the diff you can read",
   "Implement in stages that match the plan, because every stage boundary is a place to run the check, look at the diff and, if needed, rewind. The `/diff` command shows the working tree including the edits Claude made so far [Claude Code docs, Commands, 2026].",
   """
```text
Stage 1: add the failing test.   Check: the test fails for the right reason.
Stage 2: implement.               Check: `pnpm vitest run path/to/file.test.ts` passes.
Stage 3: typecheck and lint.      Check: `pnpm tsc --noEmit` exits 0.
```
| Boundary action | Command |
|---|---|
| Read the changes | `/diff` |
| Undo a bad stage | `/rewind` (Module 2.5) |
| Record progress | A small commit (guide 2.1.4) |
""",
   "Big-bang-diff", "You let the whole plan run before looking, and a wrong early decision is buried under a large diff that is hard to review or rewind.", "Run each stage to its check, read `/diff`, and only then continue.",
   "checkpoints are Module 2.5; reviews are guide 2.6.8.", "small stages keep every decision reviewable."),
 S("What Claude cannot see while it implements",
   "Best practices says to write down only what Claude cannot find by reading the repo: the exact test, typecheck and lint commands, misleading code, decisions not in the repo and anything you corrected twice [Claude Code docs, Best practices, 2026].",
   """
```markdown
# Commands
- Run one test file: pnpm vitest run path/to/file.test.ts
- Typecheck: pnpm tsc --noEmit
```
That file is the docs' own short example of a CLAUDE.md that passes the test [Claude Code docs, Best practices, 2026]. If a rule must hold every time, it belongs in a hook rather than a prompt (Module 5.4).
""",
   "Hidden-command", "The check command lives in your head, so Claude guesses a test invocation, fails or skips it, and reports success.", "Put the one-test and typecheck commands in CLAUDE.md and name them in the plan.",
   "CLAUDE.md is Module 3.2; hooks are Module 5.4.", "the check command is the most valuable line you can write down."),
 ],
 retrieval=[
  ("Which prompt shape implements test-first, from the prompt library?", "`write tests for {feature} first, then implement it until they pass`."),
  ("Claude edits a failing test to match its code. Name the failure mode by its exact label.", "**Test-bending.**"),
  ("What is the built-in default permission mode for interactive terminal sessions, and from which version?", "`auto`, from v2.1.283."),
  ("You let a whole plan run and cannot review the diff. Name the failure mode.", "**Big-bang-diff.**"),
  ("Which five kinds of check does Best practices list?", "A test file, a build exit code, a linter, a script diffing against a fixture, a browser screenshot."),
  ("The check command exists only in your head. Name the failure mode and the fix.", "**Hidden-command.** Put it in CLAUDE.md and the plan."),
  ("What does the status bar show in accept-edits mode?", "`⏵⏵ accept edits on`."),
  ("You never looked at the mode after approving. Name the failure mode by its exact label.", "**Mode-blind-edit.**"),
  ("Which command shows the working-tree changes including Claude's edits?", "`/diff`."),
 ],
 steps=[("Approve a plan with manual edits and record the mode", "Mode line"), ("Add a failing test; run it; show it fails for the right reason", "Failing log"),
        ("Implement stage two; run the single-test command", "Passing log"), ("Run typecheck and lint", "Exit codes"),
        ("Run `git diff` on the test files to prove they did not move", "Empty test diff"), ("Read `/diff` and write one sentence per stage", "Stage notes")],
 pass_md="""
| Stage | Check | Result |
|---|---|---|
| 1 failing test | `vitest run file.test.ts` | Fails: expected 429, got 200 |
| 2 implement | same command | Passes |
| 3 typecheck | `tsc --noEmit` | Exit 0 |
| Test files in diff | `git diff -- '*.test.ts'` | Unchanged since stage 1 |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Tests edited during stage 2 | **Test-bending** |
| One 600-line diff | **Big-bang-diff** |
""",
 verdict="The artifact passes only if the test failed first, passed later without the test file changing, and each stage has a recorded check.",
 res=R([("Anthropic", "Best practices", "Checks Claude can run; what to write down", "Current; read in full"), ("Anthropic", "Prompt library", "Test-first prompt shapes", "Current; read from page source"),
        ("Anthropic", "Permission modes", "Mode after approval, status bar", "Current; partial read")],
       "none found between the sources read."),
 reframe="This is the craft of implementing: **a mode you chose, a test that failed first, and stages with checks.** The engineer who understands this does not ask \"is it done?\" — they ask \"which command proves each stage, and did the tests stay still?\"",
))

# ---------------------------------------------------------------- 2.1.4 COMMIT
SPECS.append(G(M, "2.1.4", "Commit: messages, pull requests and the gh CLI",
 thesis="Committing is the point where a session becomes team history, so the discipline is a reviewed diff, a message that explains why, and a pull request linked back to the session that produced it.",
 prove="produce a commit and a pull request from a session, then find the session again from the PR number.",
 discipline="read the diff before asking for the commit, and read the PR text before submitting.",
 counter="a commit message written by Claude describes the diff it saw, not your intent, so intent is the part you must supply [Claude Code docs, Common workflows, 2026].",
 read_min=19, prove_h="2", depth=["Ask for a commit and a PR and name the CLI they use", "Resume a session from its PR", "Design commit and PR rules for a repo"],
 deliverable="One commit, one PR and a transcript showing `claude --from-pr` finding the session.",
 sections=[
 S("Asking for the commit",
   "The prompt library includes `commit these changes with a message that summarizes what I did` and `review my uncommitted changes and flag anything that looks risky before I commit` [Claude Code docs, Prompt library, 2026]. The second prompt is the one that matters first: review precedes commit.",
   """
| Step | Prompt or command |
|---|---|
| Inspect | `/diff` (Module 2.6 covers review in depth) |
| Risk pass | `review my uncommitted changes and flag anything that looks risky before I commit` |
| Commit | `commit these changes with a message that summarizes what I did` |
| Conflicts | `resolve the merge conflicts in this branch and explain what you kept from each side` |

All four prompts are from the prompt library [Claude Code docs, Prompt library, 2026].
""",
   "Commit-blind", "You ask for the commit without reading the diff, and a stray debug edit or a touched generated file lands in history.", "Run the risk-pass prompt and read `/diff` first, then commit.",
   "review tools are guide 2.6.8; keeping to scope is Module 2.2.", "review before you commit, not after."),
 S("Pull requests with gh",
   "You can create a pull request by asking directly (`create a pr for my changes`) or by stepping through summarize, create, then enhance the description; the docs advise reviewing the generated PR and asking Claude to highlight risks [Claude Code docs, Common workflows, 2026]. For CLIs it has not seen, Claude can read `--help`, and with `gh` installed and signed in it opens PRs and reads review comments without explanation [Claude Code docs, Best practices, 2026].",
   """
```text
summarize the changes I've made to the authentication module
create a pr
enhance the PR description with more context about the security improvements
```
| Tool | Role |
|---|---|
| `gh` | GitHub PRs and review comments |
| `glab` | GitLab merge requests |
| MCP server | Systems without a CLI (Module 5.5) |
""",
   "Summary-as-intent", "The PR description restates the diff and omits why the change exists, so reviewers re-derive the reason and the linked issue never gets closed.", "Add the motivation, linked issue and risks yourself before submitting, and ask Claude to tighten rather than invent them.",
   "PR workflows are guide 2.6.5; MCP is Module 5.5.", "you supply the why; Claude supplies the what."),
 S("Linking a session to its PR",
   "Claude Code links the session to the PR when Claude creates it with `gh pr create` or `glab mr create`, and when Claude works on an existing PR. Find it later with `claude --from-pr 1234`, which opens the picker filtered to that PR, or paste the PR URL into the `/resume` picker search [Claude Code docs, Common workflows, 2026; Manage sessions, 2026].",
   """
| Need | Command |
|---|---|
| Sessions for PR 1234 | `claude --from-pr 1234` |
| Search by URL | Paste the PR URL in the `/resume` picker |
| Most recent session here | `claude --continue` |

A session resumed through the picker keeps its transcript, so a reviewer comment a week later can be answered with the original reasoning [Claude Code docs, Manage sessions, 2026].
""",
   "Orphan-session", "You open a PR from a manual `git push` and web form, so the session is not linked and the reasoning behind the change is hard to recover.", "Let Claude create the PR with `gh pr create`, or name the session after the branch so `/resume <name>` finds it.",
   "naming sessions is guide 2.4.2; resume is guide 2.4.1.", "create the PR from the session so the link exists."),
 S("Keeping the safety rails on",
   "Pushes are an irreversible-by-others action, so keep ask rules and branch protection in place. Best practices lists `Bash(git push *)` as an ask rule in its example and says a person approves the merge in unattended runs [Claude Code docs, Best practices, 2026].",
   """
```json
{ "permissions": { "ask": ["Bash(git push *)"] } }
```
| Control | Layer |
|---|---|
| `ask` on `git push` | Harness, deterministic |
| Branch protection | The host, outside Claude |
| Reviewer approval | A person |

Auto mode blocks force pushes over other people's work by default, but deny rules and hooks apply before the classifier [Claude Code docs, Best practices, 2026].
""",
   "Push-without-pause", "A broad allow rule lets Claude push to the shared branch without a prompt, and an unreviewed commit reaches teammates.", "Keep `git push` on an ask rule and protect the default branch on the host.",
   "permissions are Module 4.2; safe autonomy is Module 11.7.", "the merge approval stays with a person."),
 ],
 retrieval=[
  ("Which prompt reviews before commit, per the prompt library?", "`review my uncommitted changes and flag anything that looks risky before I commit`."),
  ("You commit without reading the diff. Name the failure mode by its exact label.", "**Commit-blind.**"),
  ("Which command finds the session for PR 1234?", "`claude --from-pr 1234`."),
  ("Your PR text restates the diff only. Name the failure mode.", "**Summary-as-intent.**"),
  ("Which two commands link a session to a PR when Claude creates it?", "`gh pr create` or `glab mr create`."),
  ("You opened the PR through the web form and lost the link. Name the failure mode and fix.", "**Orphan-session.** Create the PR from the session or name the session."),
  ("Which ask rule does Best practices show for pushes?", "`Bash(git push *)`."),
  ("A broad allow rule pushes to main unprompted. Name the failure mode by its exact label.", "**Push-without-pause.**"),
  ("What should you do with a generated PR before submitting?", "Review it and ask Claude to highlight risks."),
 ],
 steps=[("Finish a small change and read `/diff`", "Diff notes"), ("Run the risk-pass prompt", "Findings list"), ("Commit with the library prompt; edit the message to add the why", "Commit text"),
        ("Create the PR from the session; add motivation and linked issue", "PR text"), ("Exit and run `claude --from-pr <n>`", "Resume log"), ("Show your push rule and branch protection", "Config snippet")],
 pass_md="""
| Item | Evidence |
|---|---|
| Risk pass run | 1 stray log line removed |
| Commit message | States the why and issue number |
| PR linked | `claude --from-pr 87` lists the session |
| Push rule | `ask` on `git push *` |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| PR created from web form | **Orphan-session** |
| Description equals commit list | **Summary-as-intent** |
""",
 verdict="The artifact passes only if `claude --from-pr` returns the session and the PR text contains a reason you wrote.",
 res=R([("Anthropic", "Common workflows", "PR flow and `--from-pr`", "Current; read in full"), ("Anthropic", "Manage sessions", "Picker search by PR URL", "Current; read in full"),
        ("Anthropic", "Best practices", "gh integration, ask rules", "Current; read in full")],
       "none found between the sources read. The docs do not prescribe a commit-message format; this guide does not either."),
 reframe="This is the craft of committing: **a read diff, a why you wrote, and a PR the session is linked to.** The engineer who understands this does not ask \"can Claude push this?\" — they ask \"did I read it, and can I find the session when a reviewer asks?\"",
))

# ---------------------------------------------------------------- 2.1.5 WHEN TO SKIP PLANNING
SPECS.append(G(M, "2.1.5", "When to skip planning",
 thesis="Planning is a tool with a cost, and the decision to skip it should come from how well you can specify the change and how cheaply you can undo it, not from habit in either direction.",
 prove="classify ten changes as plan or skip with a stated reason each, then run two of them the opposite way and compare cost.",
 discipline="decide plan or skip from specifiability and reversibility, and write the reason down.",
 counter="the current Best practices page says your first plain prompt in a fresh session already does the right thing in most cases, so heavy ceremony is the exception, not the default [Claude Code docs, Best practices, 2026].",
 read_min=17, prove_h="2", depth=["State the one-sentence-diff rule and its source status", "Classify changes by specifiability and reversibility", "Set team defaults for when a plan is required"],
 deliverable="A ten-row decision table with reasons, plus two runs done the opposite way and their cost notes.",
 sections=[
 S("The one-sentence rule and what the docs say",
   "This module's item says that if you can describe the diff in one sentence you should ask for it directly. I did not find that sentence on the current Best practices page; what the page says is that in most cases the first plain prompt in a fresh session already does the right thing without setup [Claude Code docs, Best practices, 2026]. Treat the one-sentence test as a useful heuristic, not a quotation.",
   """
| Source | Claim | Status |
|---|---|---|
| Best practices | First plain prompt usually right | Verified on the page |
| Common workflows | Plan mode is for changes you want to review before they touch disk | Verified [Claude Code docs, Common workflows, 2026] |
| One-sentence diff test | Skip planning if you can state the diff in a sentence | Heuristic from this module, not found verbatim |
""",
   "Source-laundering", "You cite the one-sentence rule to a team as an official instruction, and the docs do not say it, so the rule loses credibility the first time someone checks.", "Label it a heuristic and cite the verified statements instead.",
   "the extra-careful sourcing habit is Module 16.1.", "label heuristics as heuristics."),
 S("Specifiability and reversibility",
   "Common workflows describes plan mode as the choice for changes you want to review before they touch disk [Claude Code docs, Common workflows, 2026]. Two questions decide it: can you state what done looks like, and can you undo the change cheaply? Checkpoints make undoing cheap for file edits, though not for shell side effects [Claude Code docs, Checkpointing, 2026].",
   """
| Specifiable | Reversible | Decision |
|---|---|---|
| Yes | Yes | Skip planning; ask directly |
| Yes | No (migration, deploy config) | Plan, approve manually |
| No | Yes | Explore, then interview (guide 2.1.6) |
| No | No | Explore, interview, plan, stage |
""",
   "Reversibility-assumption", "You skip planning because edits are undoable, but the change runs a shell command or migration that rewind does not restore.", "Treat any change with shell side effects as not reversible and plan it.",
   "limits of rewind are guide 2.5.3; git as the net is guide 2.5.5.", "undo covers file edits, not side effects."),
 S("Plan fatigue and the cost of ceremony",
   "Every plan round costs tokens and your attention. The docs warn about over-correction in a different place, `What you can stop doing`, which lists advice that current models made unnecessary, such as telling Claude to keep going or to be thorough [Claude Code docs, Best practices, 2026]. Apply the same scepticism to rituals you add.",
   """
| Ritual | Keep if |
|---|---|
| Plan every change | Never as a blanket rule |
| Interview before every feature | The feature has unstated tradeoffs |
| Fresh session per task | Context is unrelated (guide 2.1.7) |
| A `/goal` for every small fix | The end state is verifiable and long-running |
""",
   "Ritual-planning", "You plan every change, including typo fixes, because planning feels safe, and the loop slows without catching more mistakes.", "Reserve plans for uncertain or multi-file or irreversible changes and measure whether plans caught anything.",
   "goals are Module 6.7; session hygiene is Module 2.4.", "ceremony should earn its place."),
 S("Skipping safely: the minimum viable direct prompt",
   "Skipping the plan does not mean skipping the check. A direct prompt should still name the file, the symptom or behaviour, and what done looks like; that is the table Best practices gives for specific prompts [Claude Code docs, Best practices, 2026].",
   """
```text
users report login fails after the session times out. look at token refresh in src/auth/, write a failing test that reproduces it, then fix it
```
That example, from the docs, names the symptom, the location and a check in one sentence [Claude Code docs, Best practices, 2026].
""",
   "Direct-and-blind", "You skip planning and the prompt too, so Claude spends turns rediscovering which file you meant and may edit the wrong one.", "Even a direct prompt names the file or directory and the check.",
   "prompt detail is Module 2.2; verification is Module 2.3.", "skip the plan, never the check."),
 ],
 retrieval=[
  ("Is the one-sentence-diff rule a verified quotation from the current docs?", "No; it is this module's heuristic, and the Best practices page says the first plain prompt usually does the right thing."),
  ("You cite the heuristic as official. Name the failure mode by its exact label.", "**Source-laundering.**"),
  ("Specifiable but not reversible: plan or skip?", "Plan and approve manually."),
  ("You skip planning because edits are undoable, but the change runs a migration. Name the failure mode.", "**Reversibility-assumption.**"),
  ("You plan a typo fix. Name the failure mode by its exact label.", "**Ritual-planning.**"),
  ("What three things should a direct prompt name?", "The file or directory, the symptom or behaviour, and what done looks like."),
  ("Your skip-the-plan prompt names no file. Name the failure mode.", "**Direct-and-blind.**"),
  ("What does Common workflows say plan mode is for?", "Changes you want to review before they touch disk."),
  ("What does checkpointing restore, and what does it miss?", "File edits through Claude's tools; not shell-command changes or other processes."),
 ],
 steps=[("List ten recent changes", "Ten-row list"), ("Mark each specifiable and reversible, yes or no", "Two columns"), ("Assign plan, skip, interview or full path with a reason", "Decision column"),
        ("Run one skip-eligible change with a plan and note extra turns", "Cost note A"), ("Run one plan-eligible change without a plan and note errors", "Cost note B"), ("Write your team default in three lines", "Policy")],
 pass_md="""
| Change | Specifiable | Reversible | Decision |
|---|---|---|---|
| Rename a variable | Yes | Yes | Skip |
| Add a DB column | Yes | No | Plan |
| New billing flow | No | No | Interview, plan, stage |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| All ten rows say plan | **Ritual-planning** |
| Policy cites the sentence rule as official | **Source-laundering** |
""",
 verdict="The artifact passes only if the table has both outcomes, each decision has a reason, and at least one run was done against the table to test it.",
 res=R([("Anthropic", "Best practices", "First plain prompt usually right; specific-prompt table", "Current; read in full"), ("Anthropic", "Common workflows", "Plan mode purpose", "Current; read in full"),
        ("Anthropic", "Checkpointing", "What rewind restores", "Current; read in full")],
       "this module's one-sentence rule is not on the current Best practices page. **Use the verified statements and call the rule a heuristic.**"),
 reframe="This is the craft of skipping: **specifiability, reversibility and a check you still name.** The engineer who understands this does not ask \"should I always plan?\" — they ask \"can I state the diff, and can I undo it?\"",
 thin="The one-sentence rule is unverified in the current docs; the guide says so rather than inventing a source.",
))

# ---------------------------------------------------------------- 2.1.6 SPEC INTERVIEW
SPECS.append(G(M, "2.1.6", "The spec interview pattern",
 thesis="When you do not yet know what you want, you can have Claude interview you with structured questions and write the answers into a spec file, which turns a vague idea into a definition of done that a fresh session can execute.",
 prove="run an interview for a real feature, get a SPEC.md, and show three decisions the interview forced that you had not made.",
 discipline="let the interview end in a file, and read the file before you build from it.",
 counter="the interview works because it asks you things the code cannot answer; a spec that only restates the code is a sign the interview asked the wrong questions [Claude Code docs, Best practices, 2026].",
 read_min=19, prove_h="2.5", depth=["Run the interview prompt and produce a spec file", "Judge a spec for gaps and out-of-scope clarity", "Turn the spec into the reviewer's checklist"],
 deliverable="A SPEC.md from a real interview, annotated with the three decisions the interview forced.",
 sections=[
 S("The prompt and what comes back",
   "Best practices gives the pattern verbatim: ask Claude to interview you until it could write the spec and write it to a file. Claude responds with multiple-choice questions on the parts you have not pinned down, such as per-user versus per-key limits, behaviour over the limit and what is out of scope, and keeps asking until the answers add up to a spec [Claude Code docs, Best practices, 2026].",
   """
```text
I want to add rate limiting to the public API but haven't thought it through yet. Interview me until you could write the spec, then write it to SPEC.md.
```
The prompt library has a variant naming the coverage areas: implementation, UX, edge cases and tradeoffs [Claude Code docs, Prompt library, 2026].

| Component | Detail |
|---|---|
| Question format | Multiple choice, per the docs |
| Stop condition | Claude could write the spec |
| Output | A file such as `SPEC.md` |
""",
   "Interview-to-nowhere", "The interview ends with answers in chat and no file, so the decisions vanish at the next compaction or session.", "State the output file in the prompt and confirm it exists before you close the session.",
   "context survival is Module 3.1; spec-driven development is Module 9.1.", "the interview must end in a file."),
 S("Why the question tool makes it better",
   "The pattern relies on Claude's question tool, which presents choices rather than open prose. The interactive-mode page notes that when you type your own answer in the `Other` row of such a question, pressing `Esc` twice cancels it [Claude Code docs, Interactive mode, 2026]. The tools reference documents its behaviour under an AskUserQuestion entry that I linked to but did not read [Claude Code docs, Best practices, 2026; page not fetched].",
   """
| Question style | Strength | Weakness |
|---|---|---|
| Multiple choice | Fast, forces a decision | Options may omit your case; use `Other` |
| Open prose | Captures nuance | Easy to leave tradeoffs unstated |

Answer the tradeoff questions slowly. The cheapest place to change your mind is the interview.
""",
   "Option-capture", "You pick from the offered options even when none fits, and the spec encodes a compromise nobody wanted.", "Use the `Other` row and write your own answer whenever the options miss the case.",
   "prompting is Module 2.2; the tool name list is Module 1.2.", "answer in your own words when the options are wrong."),
 S("What a good spec contains",
   "Best practices says the written spec is also the file you point the reviewer at later, and shows a review prompt that checks every requirement is implemented and the listed edge cases have tests, reporting correctness gaps only [Claude Code docs, Best practices, 2026]. A spec that cannot be checked that way is too vague.",
   """
| Section | Test of quality |
|---|---|
| Behaviour | A reviewer could write a test from each line |
| Edge cases | Each has an expected result |
| Out of scope | Names at least two tempting extras |
| Check command | The exact command that proves done |
| Open questions | Marked, not hidden |
""",
   "Untestable-spec", "The spec says things like handle errors gracefully, so neither the build nor the review has anything concrete to check.", "Rewrite each line so a test or a command could fail it.",
   "review against a spec is guide 2.3.6; specification craft is Module 9.1.", "a spec line you cannot test is a wish."),
 S("Interview versus plan mode",
   "Plan mode proposes an implementation of a decided task; the interview decides the task. The prompt library separates them: `plan how to refactor ... don't edit anything yet` is planning, while the interview prompt writes SPEC.md [Claude Code docs, Prompt library, 2026].",
   """
| Question you cannot answer | Tool |
|---|---|
| What should it do? | Interview |
| How should it be built? | Plan mode |
| Did we build it? | Review against the spec |
""",
   "Phase-swap", "You use plan mode to decide product behaviour, and the plan quietly invents requirements that you then approve as implementation detail.", "Decide behaviour in the interview and let the plan only decide the build.",
   "planning is guide 2.1.2; product framing for non-engineers is Module 13.3.", "interview decides what; plan decides how."),
 ],
 retrieval=[
  ("What format of questions does Claude ask in the interview, per Best practices?", "Multiple-choice questions."),
  ("The interview ends with answers only in chat. Name the failure mode by its exact label.", "**Interview-to-nowhere.**"),
  ("Which file name does the docs' example write to?", "`SPEC.md`."),
  ("None of the options fits and you pick one anyway. Name the failure mode.", "**Option-capture.**"),
  ("A spec line says handle errors gracefully. Name the failure mode by its exact label.", "**Untestable-spec.**"),
  ("You use plan mode to decide behaviour. Name the failure mode and the fix.", "**Phase-swap.** Decide behaviour in the interview."),
  ("What key sequence cancels a question while typing in the Other row?", "`Esc` twice."),
  ("What does the review prompt in Best practices tell the reviewer to skip?", "Style; report only correctness gaps."),
  ("Which areas does the prompt-library variant list?", "Implementation, UX, edge cases and tradeoffs."),
 ],
 steps=[("Pick a feature you have not thought through", "One-line feature"), ("Run the interview prompt naming the output file", "Transcript"), ("Answer using `Other` at least once", "Marked answers"),
        ("Read the SPEC.md and rewrite two untestable lines", "Edits"), ("List three decisions the interview forced", "Three lines"), ("Write the review prompt that uses the spec", "Prompt text")],
 pass_md="""
| Spec element | Present |
|---|---|
| 429 response with Retry-After header | Yes, testable |
| Out of scope: per-endpoint tiers, admin override | Yes |
| Check: `pnpm vitest run rate-limit` | Yes |
| Open question: shared limits across keys | Marked |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Spec says handle limits gracefully | **Untestable-spec** |
| No file on disk | **Interview-to-nowhere** |
""",
 verdict="The artifact passes only if SPEC.md exists, every behaviour line could fail a test, and three interview-forced decisions are named.",
 res=R([("Anthropic", "Best practices", "Interview pattern and review-against-spec prompt", "Current; read in full"), ("Anthropic", "Prompt library", "Interview variant", "Current; read from page source"),
        ("Anthropic", "Interactive mode", "Esc behaviour in question prompts", "Current; partial read")],
       "none found between the sources read; the tools-reference page on the question tool was not fetched."),
 reframe="This is the craft of the interview: **questions only you can answer, ending in a file a reviewer can test against.** The engineer who understands this does not ask \"how do I describe the feature?\" — they ask \"what has Claude not yet made me decide?\"",
 thin="The question tool's own reference page was linked but not fetched; behaviour beyond the Esc note is unverified.",
))

# ---------------------------------------------------------------- 2.1.7 FRESH SESSION
SPECS.append(G(M, "2.1.7", "Fresh session for execution",
 thesis="After a spec or plan exists as a file, the best execution starts from a clean context that holds the spec and the code and nothing else, because the written document carries the decisions and the old conversation carries only noise.",
 prove="execute a spec in a fresh session and show that the first prompt plus the file was enough, with context contents checked by /context.",
 discipline="move decisions into files, then clear.",
 counter="clearing is not free of consequence in either direction: it saves tokens and focus, but a cold cache means the first turn is full price [Claude Code docs, Best practices, 2026].",
 read_min=18, prove_h="2", depth=["Use /clear and /resume to switch tasks", "Judge clear versus compact versus continue", "Design a handoff file that survives sessions"],
 deliverable="A handoff file, a fresh-session first prompt, and a `/context` snapshot proving the context held only what you intended.",
 sections=[
 S("Why a clean context wins",
   "Best practices says that after the spec exists you should start a fresh session so the build begins with a clean context and a written definition of done [Claude Code docs, Best practices, 2026]. It also says `/clear` between unrelated tasks costs nothing and keeps the next task from paying for the previous one's history, because every request sends the whole conversation [Claude Code docs, Best practices, 2026].",
   """
| Keep going | Clear |
|---|---|
| Same task, context is the asset | Spec or plan is written |
| Mid-debug with evidence in context | Corrected the same thing twice |
| Short follow-up | Unrelated next task |

The page also notes that most current models have a 1M-token window with automatic compaction, so running out is rare, but `/clear` between tasks is still worth doing for focus and cost [Claude Code docs, Best practices, 2026].
""",
   "Marathon-session", "One session accumulates three unrelated tasks, and each later turn re-reads all of them at cost while old details compete with the current task.", "Clear between unrelated tasks and name the old session so you can return.",
   "context mechanics are Module 3.1; cost is Module 3.4.", "one task, one context."),
 S("The mechanics of clearing safely",
   "`/clear [name]` starts a new conversation with empty context; pass a name to label the previous conversation in the `/resume` picker. The previous session is saved and can be resumed, and within the same process the rewind menu shows a previous-session entry [Claude Code docs, Commands and Checkpointing, 2026].",
   """
```text
/clear oauth-migration     # new session; old one labelled oauth-migration
/resume oauth-migration    # come back later
```
| Behaviour | Detail |
|---|---|
| Aliases | `/reset`, `/new` |
| Name kept | A name from `--name` or `/rename` survives; an AI-generated title does not |
| Active goal | `/clear` also removes it [Claude Code docs, Goal, 2026] |
""",
   "Unnamed-clear", "You clear without naming the old session and cannot tell it apart in the picker a day later.", "Pass a name to `/clear` or `/rename` before clearing.",
   "naming is guide 2.4.2; resume is guide 2.4.1.", "name what you leave."),
 S("The handoff file",
   "A fresh session knows only what loads at startup (CLAUDE.md, memory) and what you tell it. The handoff is therefore a file: the spec from guide 2.1.6, or a plan, plus the check command. Best practices says only to write down what Claude cannot find by reading the repo [Claude Code docs, Best practices, 2026].",
   """
```text
Read SPEC.md and implement it in stages. Run `pnpm vitest run rate-limit` after each stage. Stop and ask if the spec and the code disagree.
```
| Handoff content | Why |
|---|---|
| Spec path | Definition of done |
| Check command | Closes the loop |
| Stop rule | Prevents silent divergence |
| Branch name | Ties work to history |
""",
   "Lossy-handoff", "The handoff is a chat summary that omits a decision, and the fresh session rebuilds the feature with the omitted choice reversed.", "Put decisions in the file, not the summary, and point the first prompt at the file.",
   "CLAUDE.md is Module 3.2; spec-driven work is Module 9.1.", "the file carries the decisions."),
 S("Compact, rewind or clear",
   "Three tools reduce context differently. `/compact [instructions]` replaces history with a summary, the rewind menu can summarize from or up to a chosen message without changing files, and `/clear` starts over [Claude Code docs, Manage sessions and Checkpointing, 2026].",
   """
| Tool | Effect | Use when |
|---|---|---|
| `/compact keep the API changes and the test commands` | Summarizes the whole conversation | Same task, noisy history |
| Rewind: Summarize from here | Compresses from a point forward | A verbose debug midstream |
| `/clear` | New context | Task done or spec written |

Compaction is itself a large request on a long session, more so once the cache expires [Claude Code docs, Best practices, 2026].
""",
   "Compact-reflex", "You compact whenever the session feels heavy, paying for a big summarizing request, when the task is done and a clear would cost nothing.", "Clear when the task ended, compact only when the same task must continue.",
   "compaction survival is Module 3.1; checkpoints are Module 2.5.", "finished tasks get cleared, not compacted."),
 ],
 retrieval=[
  ("Which command labels the previous conversation as it clears?", "`/clear <name>`."),
  ("Three unrelated tasks in one session re-read on every turn. Name the failure mode by its exact label.", "**Marathon-session.**"),
  ("What are the aliases of `/clear`?", "`/reset` and `/new`."),
  ("You clear and cannot find the old session. Name the failure mode.", "**Unnamed-clear.**"),
  ("Which prompt cache lifetimes does Best practices give?", "About an hour on a subscription, five minutes on an API key, cloud provider or usage credits."),
  ("The handoff was a chat summary that dropped a decision. Name the failure mode by its exact label.", "**Lossy-handoff.**"),
  ("You compact after the task is done. Name the failure mode and the fix.", "**Compact-reflex.** Clear instead."),
  ("What does `/clear` do to an active goal?", "Removes it."),
  ("How large is the window on most current models, per Best practices?", "1M tokens."),
 ],
 steps=[("Finish a SPEC.md from the interview and commit it", "Spec in repo"), ("Name and clear the old session", "Picker entry"), ("Start fresh with the handoff prompt", "First prompt"),
        ("Run `/context` before the first edit", "Snapshot"), ("Implement one stage; confirm the check", "Log"), ("Resume the old session by name once, to prove it", "Resume log")],
 pass_md="""
| Item | Evidence |
|---|---|
| Old session | Named `rate-limit-spec`; `/resume rate-limit-spec` works |
| Fresh context | `/context` shows CLAUDE.md, tools and no old conversation |
| Handoff | First prompt names SPEC.md and the check |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Handoff pasted as chat summary | **Lossy-handoff** |
| Old session never named | **Unnamed-clear** |
""",
 verdict="The artifact passes only if `/context` shows no leftover conversation and the build followed the file rather than memory of the old chat.",
 res=R([("Anthropic", "Best practices", "Fresh session after spec; clear costs", "Current; read in full"), ("Anthropic", "Manage sessions", "Clear and resume mechanics", "Current; read in full"),
        ("Anthropic", "Checkpointing", "Summarize options", "Current; read in full")],
       "none found between the sources read."),
 reframe="This is the craft of the fresh start: **decisions in a file, a named session left behind, and a clean desk for execution.** The engineer who understands this does not ask \"why did it forget?\" — they ask \"what did I put in the file, and why was the chat still open?\"",
))

if __name__ == "__main__":
    run(SPECS)
