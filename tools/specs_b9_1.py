import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from specs_b9_lib import G, write

M = "b-9-1"
BP = "Claude Code docs, Best practices, 2026"
SPECS = []

SPECS.append(G(M, "9.1.1", "The spec-driven workflow",
 "Spec-driven development splits a feature into two sessions: one that interviews you and writes down what to build, and a fresh one that builds from the written file, so the build starts with clean context and a defined finish line.",
 "run the seven steps on a small feature and show the SPEC.md, the fresh-session build, the review against the spec and the commit.",
 "never start building in the same context that did the interviewing.",
 "writing a spec first is not slower for fuzzy ideas: the interview is how you discover what you wanted, and the file is what makes the later review checkable [%s]." % BP,
 [("Interview, then write the spec",
   "When you do not know exactly what you want, you do not have to work it out before prompting. The docs suggest asking Claude to interview you and write SPEC.md; Claude returns multiple-choice questions about the parts you have not pinned down, such as per-user versus per-key limits, behaviour over the limit and what is out of scope [%s]." % BP,
   """
```text
I want to add rate limiting to the public API but haven't thought it through yet.
Interview me until you could write the spec, then write it to SPEC.md.
```

| Step | Who acts | Output |
|---|---|---|
| 1 Interview | Claude asks, you answer | Decisions on the unpinned parts |
| 2 Write SPEC.md | Claude | A file in the repo |
| 3 Review the spec | You (judgement, not from the docs) | Corrections before any code |
| 4 Fresh session | You | Clean context |
| 5 Implement against the spec | Claude | A diff |
| 6 Verify against the spec | A reviewer prompt or subagent | Gap list |
| 7 Commit | You or Claude | A reviewable change |""",
   ("Spec-by-vibes", "You accept the first SPEC.md without reading it, so Claude's guesses about scope become requirements.", "Read the spec as you would a diff, and strike or correct every line you did not decide before opening the build session."),
   "plan mode is Module 2.1; the interview wording is Module 9.1.3.", "the interview turns your unknowns into decisions before code exists."),
  ("Why the build starts in a fresh session",
   "The docs say that once SPEC.md exists you should start a fresh session to build from it, so the build begins with a clean context and a written definition of done. The same file is what you point the reviewer at later [%s]." % BP,
   """
| Property | Same session as interview | Fresh session from SPEC.md |
|---|---|---|
| Context at start | Full of interview turns and rejected options | Only the spec and the repo |
| Definition of done | Remembered, may drift | Written in a file |
| Restart cost | Re-explain | `claude`, then point at SPEC.md |

```bash
claude            # new session
> Implement SPEC.md. Run the checks it lists and show the output.
```""",
   ("Context carry-over", "You build in the interview session, and discarded options and half-decisions steer the code.", "End the interview at the written file, then open a new session and start the build prompt from the file."),
   "context and sessions are Module 2.4; the structure of the file is Module 9.1.2.", "the file, not the chat history, is the contract."),
  ("Review against the spec, then commit",
   "The docs give a review prompt that checks the work against your plan rather than hunting for bugs in general: a subagent reviews the diff against SPEC.md, checks every requirement is implemented and the listed edge cases have tests, and skips style [%s]." % BP,
   """
```text
use a subagent to review the rate limiter diff against SPEC.md, check every requirement
is implemented and the listed edge cases have tests, report gaps that affect correctness
and skip style
```

| Review prompt part | Why |
|---|---|
| "against SPEC.md" | Gives the reviewer a fixed standard |
| "every requirement is implemented" | Catches omissions |
| "edge cases have tests" | Links spec to tests |
| "skip style" | A reviewer asked to find problems will always find something [%s] |""" % BP,
   ("Reviewer-invented work", "You drop the skip-style clause, the reviewer finds something to report, and fixing it adds abstraction layers and tests for impossible cases.", "Keep the 'report gaps that affect correctness and skip style' clause in every spec review."),
   "verification gates are Module 9.13; review of AI code is Module 9.12.", "review for gaps against the spec, not for taste."),
 ],
 [("Name the seven steps of the workflow in order.", "Interview, write SPEC.md, review the spec yourself, start a fresh session, implement against the spec, verify against the spec, commit."),
  ("Why does the docs' workflow start the build in a fresh session?", "So the build begins with clean context and a written definition of done."),
  ("You accepted the first SPEC.md without reading it. Name the failure mode by its exact label.", "**Spec-by-vibes.**"),
  ("Interview debris steers your code because you built in the same chat. Name the failure mode.", "**Context carry-over.**"),
  ("Your spec review produced extra abstraction layers. Name the failure mode by its exact label and the fix.", "**Reviewer-invented work.** Keep the 'skip style' clause."),
  ("What file name does the docs' interview prompt write to?", "SPEC.md."),
  ("What kind of questions does Claude return in the interview?", "Multiple-choice questions about the parts you have not pinned down."),
  ("Which part of the review prompt prevents a reviewer from always finding something?", "'skip style' (report only gaps that affect correctness)."),
  ("Is step 3, reviewing the spec yourself, stated in the docs?", "No. It is this guide's judgement; the docs describe interview, SPEC.md, a fresh session and a review against the spec."),
 ],
 ("A SPEC.md, a transcript of a fresh build session, a spec-review output and a commit for one small feature.",
  [("Pick a feature you have not designed; start an interview prompt", "Interview transcript"), ("Have Claude write SPEC.md", "SPEC.md"), ("Edit the spec by hand and record what you changed", "Edit list"),
   ("Open a fresh session; implement from SPEC.md", "Diff"), ("Run the spec-review prompt with skip style", "Gap list"), ("Fix gaps and commit referencing SPEC.md", "Commit")]),
 """
| Element | Evidence |
|---|---|
| SPEC.md edited by hand | Edit list with 3 changes |
| Build ran in a new session | Session ids differ |
| Review output | Lists gaps by requirement number |
""", """
| Element | What is wrong |
|---|---|
| Spec identical to Claude's first draft | **Spec-by-vibes** |
| Build in the interview chat | **Context carry-over** |
""",
 "The artifact passes only if the build session id differs from the interview session id and the review maps each gap to a requirement in SPEC.md.",
 [("Anthropic", "Best practices: Brainstorm with Claude first; Review against your spec", "Interview prompt, fresh session, spec review", "Current"),
  ("Anthropic", "Permission modes: Plan mode", "Plan mode as an alternative front end", "Current")],
 "plan mode and an interview-to-SPEC.md flow both precede coding; the docs present the interview as the route when you cannot yet specify, and plan mode as the route when you want to review changes before they touch disk.",
 "This is the craft of spec-driven work: **interview, write down, rebuild from the file.** The engineer who understands this does not ask \"what should I tell Claude?\" — they ask \"what must the file say so a stranger could build and check it?\"", read=18, prove_h="2"))

SPECS.append(G(M, "9.1.2", "What makes a spec executable",
 "A spec is executable when Claude can build from it and a reviewer can check the diff against it, which needs files and interfaces named, exclusions stated, edge cases listed and an end-to-end verification step at the end.",
 "take a vague one-paragraph spec and rewrite it so each of the four properties is present and checkable.",
 "every spec ends with a command or action whose output proves the feature works.",
 "an out-of-scope list is a requirement: it is the only part of the spec that stops silent scope creep.",
 [("The four properties",
   "The docs' own spec example asks Claude to capture what is out of scope and the edge cases, and the review prompt checks that every requirement is implemented and the listed edge cases have tests [%s]. Together with the docs' advice to name files and give a pass-or-fail check, those give four properties." % BP,
   """
| Property | What to write | Check that it is present |
|---|---|---|
| Names files and interfaces | `src/api/limiter.ts`, `check(key): Result` | A grep for each path succeeds |
| States out of scope | "No per-tenant limits; no UI" | Section titled Out of scope exists |
| Lists edge cases | "Bucket resets at window edge; clock skew" | Each case has a numbered line |
| Ends with verification | "Run `pnpm test limiter` and a curl loop; expect 429 on the 101st request" | A runnable command with expected output |""",
   ("Unfalsifiable requirement", "A line such as 'should be fast and robust' cannot be checked, so the reviewer cannot report it as a gap.", "Rewrite it as a measurable statement with a command that shows the result."),
   "interview prompts are Module 9.1.3; verification is Module 9.2.", "each property is a thing a reviewer can point at."),
  ("A skeleton you can reuse",
   "The skeleton below is this guide's own template, not an official format. It puts the checkable parts where a reviewer prompt can reference them by number.",
   """
```markdown
# SPEC: rate limiting for the public API
## Goal
One paragraph, user-visible behaviour.
## Files and interfaces
1. src/api/limiter.ts exports check(key): {allowed, retryAfterMs}
2. src/api/middleware.ts calls check before handlers
## Out of scope
- UI, per-tenant plans
## Edge cases
E1 Burst at window boundary  E2 Missing API key  E3 Clock skew
## Verification
V1 pnpm vitest run src/api/limiter.test.ts
V2 curl loop: request 101 returns 429 with Retry-After
```""",
   ("Numberless spec", "Requirements are prose with no ids, so the review cannot say which one is missing.", "Number files, edge cases and verification steps so the review prompt can cite them."),
   "plan files are Module 9.1.4; reviewers are Module 9.1.5.", "numbers make gaps reportable."),
  ("End-to-end verification as the last section",
   "The docs advise giving Claude something that comes back pass or fail, and asking for evidence: the command it ran and its output, or a screenshot [%s]." % BP,
   """
| Verification type | Example line in the spec |
|---|---|
| Test file | `pnpm vitest run path/to/file.test.ts` passes |
| Build exit code | `pnpm tsc --noEmit` exits 0 |
| Script against fixture | `diff out.json fixtures/expected.json` is empty |
| Running app | `/verify` run shows the feature working (Module 9.2.5) |""",
   ("Mocked finish line", "The verification step runs only unit tests with mocks, so the spec passes while the real flow is broken.", "Add at least one step that drives the real entry point and records its output."),
   "running the real app is Module 9.2.5.", "the last line of a spec is the proof."),
 ],
 [("Name the four properties of an executable spec.", "Names files and interfaces, states out of scope, lists edge cases, ends with an end-to-end verification step."),
  ("A line reads 'should be fast and robust'. Name the failure mode by its exact label.", "**Unfalsifiable requirement.**"),
  ("Your review cannot say which requirement is missing because nothing is numbered. Name the failure mode.", "**Numberless spec.**"),
  ("Verification only runs mocked unit tests. Name the failure mode by its exact label and fix.", "**Mocked finish line.** Add a step that drives the real entry point."),
  ("In the skeleton, how many verification steps are listed?", "Two: V1 and V2."),
  ("Which section stops silent scope creep?", "Out of scope."),
  ("Is the skeleton an official Anthropic format?", "No; it is this guide's own template."),
  ("What do the docs say to ask Claude for when it reports done?", "Evidence: the command it ran and its output, or a screenshot."),
  ("Give one example of a pass-or-fail check from the docs.", "A test file, a build exit code, a linter, a diff against a fixture or a browser screenshot next to the mockup."),
 ],
 ("A rewritten spec with all four properties plus a one-line check per property.",
  [("Take a vague paragraph spec", "Original"), ("Name files and interfaces", "Section 1"), ("Add out-of-scope", "Section 2"), ("Add 3 numbered edge cases", "Section 3"),
   ("Add two verification commands with expected output", "Section 4"), ("Run a reviewer prompt that cites ids", "Gap list with ids")]),
 """
| Property | Evidence |
|---|---|
| Files | 2 paths, both exist |
| Out of scope | 2 bullets |
| Edge cases | E1 to E3 |
| Verification | V1 command and expected output |
""", """
| Element | What is wrong |
|---|---|
| "Handle errors well" | **Unfalsifiable requirement** |
| Only unit tests with mocks | **Mocked finish line** |
""",
 "The artifact passes only if a stranger could run V1 and V2 unaided and a reviewer prompt can name a missing item by id.",
 [("Anthropic", "Best practices: Give Claude a check to run", "Pass or fail checks and evidence", "Current"),
  ("Anthropic", "Best practices: Review against your spec", "Edge cases need tests", "Current")],
 "the docs do not prescribe a spec template; the skeleton here is judgement and other teams use different layouts (for example full PRD formats).",
 "This is the craft of the executable spec: **named things, stated limits, numbered cases, and a proof step.** The engineer who understands this does not ask \"is the spec long enough?\" — they ask \"could a reviewer fail this build against it?\"", read=18))

SPECS.append(G(M, "9.1.3", "Interview prompts",
 "An interview prompt makes Claude ask you the questions you have not answered, across implementation, UI and UX, edge cases, concerns and trade-offs, while skipping questions whose answers are obvious from the code.",
 "write an interview prompt, run it, and show that the questions skipped the obvious and covered all five areas.",
 "tell Claude what you will not decide and what the output file must contain.",
 "the questions you do not want to answer are the ones the spec most needs.",
 [("The prompt shape",
   "The docs' interview prompt is short: describe the goal, say you have not thought it through, and ask for questions until Claude could write the spec to a named file. Claude replies with multiple-choice questions [%s]. The tool behind this is `AskUserQuestion`, which asks multiple-choice questions to gather requirements or clarify ambiguity and does not prompt for permission [Claude Code docs, Tools reference, 2026]." % BP,
   """
```text
Interview me about this feature using the AskUserQuestion tool. Cover implementation,
UI and UX, edge cases, concerns and trade-offs. Skip questions whose answer is obvious
from the repo. Keep going until you could write SPEC.md, then write it.
```

| Area | Example question Claude might ask |
|---|---|
| Implementation | Per-user or per-key counters? |
| UI and UX | What does a blocked user see? |
| Edge cases | What happens at the window boundary? |
| Concerns | Does a shared cache add a failure point? |
| Trade-offs | Accuracy versus cost of the counter |""",
   ("Obvious-question flood", "Claude asks which test framework you use, which the repo already shows, and you answer ten trivial questions before the real ones.", "Add 'skip questions whose answer is obvious from the repo' and name the areas you do care about."),
   "the tool list is Module 1.2; plan-mode alternative is Module 2.1.", "ask for the unknowns, not for the knowns."),
  ("Controlling depth and exit",
   "An interview needs an exit condition or it keeps asking. 'Until you could write the spec' is that condition in the docs' example [%s]. Questions stay open until you answer them by default [Claude Code docs, Tools reference, 2026]." % BP,
   """
| Control | Prompt wording |
|---|---|
| Exit | "...until you could write the spec" |
| Output | "...then write it to SPEC.md" |
| Breadth | "cover implementation, UI and UX, edge cases, concerns, trade-offs" |
| Pace | "ask three questions at a time" (this guide's suggestion, not a docs setting) |
| Veto | "if I answer 'your call', choose and note it as an assumption" |""",
   ("Endless interview", "No exit condition is given and Claude keeps asking, so the session ends with no file.", "State the output file and the 'until you could write it' condition in the first prompt."),
   "spec skeleton is Module 9.1.2.", "name the file the interview must produce."),
  ("Assumption logging",
   "'Your call' answers hide decisions. Having Claude record them as numbered assumptions in the spec makes them reviewable in step three of the workflow (Module 9.1.1).",
   """
| Answer you give | Claude should write |
|---|---|
| A choice | Decision D3: per-key limits |
| "Your call" | Assumption A2: sliding window chosen; revisit if cost matters |
| "Not sure" | Open question Q1 with an owner |""",
   ("Silent decision", "You answer 'your call' and the choice never appears in the spec, so nobody reviews it.", "Require an Assumptions section with numbered entries for every delegated answer."),
   "keeping specs alive is Module 9.1.6.", "delegated decisions still get written down."),
 ],
 [("Which tool does Claude use to ask multiple-choice requirement questions?", "`AskUserQuestion`."),
  ("Does AskUserQuestion prompt for permission?", "No, per the Tools reference."),
  ("Claude asks which test framework you use. Name the failure mode by its exact label.", "**Obvious-question flood.**"),
  ("The interview never produces a file. Name the failure mode.", "**Endless interview.**"),
  ("You said 'your call' and the choice vanished. Name the failure mode by its exact label and fix.", "**Silent decision.** Numbered assumptions section."),
  ("What exit condition does the docs' prompt use?", "'Interview me until you could write the spec, then write it to SPEC.md.'"),
  ("Name the five areas this guide asks the interview to cover.", "Implementation, UI and UX, edge cases, concerns, trade-offs."),
  ("How many questions per round does the 'pace' row suggest, and is it a docs setting?", "Three; no, it is this guide's suggestion."),
  ("Why skip obvious questions?", "The docs' test: if Claude could find it by reading the code and would look, leave it out."),
 ],
 ("An interview prompt, the transcript and the SPEC.md it produced, with assumptions listed.",
  [("Write the prompt with exit, output and areas", "Prompt"), ("Run it on a feature", "Transcript"), ("Answer one question 'your call'", "Delegated answer"),
   ("Check the spec has an Assumptions section", "SPEC.md"), ("Count obvious questions asked", "Count"), ("Refine the prompt once", "Prompt v2")]),
 """
| Check | Evidence |
|---|---|
| Areas covered | 5 of 5 |
| Obvious questions | 0 |
| Assumptions | A1 delegated answer recorded |
""", """
| Element | What is wrong |
|---|---|
| No output file named | **Endless interview** |
| 'Your call' not in spec | **Silent decision** |
""",
 "The artifact passes only if the transcript ends with a written SPEC.md and every delegated answer appears as an assumption.",
 [("Anthropic", "Best practices: Brainstorm with Claude first", "Interview prompt", "Current"), ("Anthropic", "Tools reference: AskUserQuestion", "Tool name and permission behaviour", "Current")],
 "none found between the sources read; the five-area wording is this guide's synthesis of the module text rather than a docs quote.",
 "This is the craft of the interview: **ask for unknowns, set an exit, record delegation.** The engineer who understands this does not ask \"what should I specify?\" — they ask \"what have I not decided, and where will that be written?\"", read=16, prove_h="1.5"))

SPECS.append(G(M, "9.1.4", "Plan files and task lists",
 "A PLAN.md with checkboxes is a durable record of progress that survives context resets, while Claude's task tool is the live tracker inside one session; use the file for handoff and the tool for in-session pacing.",
 "build a PLAN.md for a three-step change, run it across a session reset and show checkboxes ticked by evidence.",
 "a box is ticked only after its check has run.",
 "a plan on disk outlives the session, a task list in the session does not; they solve different problems and you want both.",
 [("Task tools and plan mode in Claude Code",
   "Claude Code has task-tracking tools: TaskCreate, TaskGet, TaskList and TaskUpdate. None prompts for permission. TodoWrite is disabled by default in favour of them, and `CLAUDE_CODE_ENABLE_TASKS=0` re-enables it [Claude Code docs, Tools reference, 2026]. The reference says the task tools are provided by default only on the models listed under Task tool availability (it names Opus 4.7, Sonnet 4.6, Haiku 4.5 and earlier), so check your model.",
   """
| Mechanism | Lives | Survives `/clear` | Best for |
|---|---|---|---|
| Task tools (TaskCreate etc.) | In the session | No | Pacing a multi-step run |
| PLAN.md with checkboxes | In the repo | Yes | Handoff, review, resume |
| Plan mode plan file | `~/.claude/plans/` or `plansDirectory` | Yes, outside the repo | Approving an approach before edits |

Plan mode: press `Shift+Tab`, prefix a prompt with `/plan`, or start with `claude --permission-mode plan` [Claude Code docs, Permission modes, 2026].""",
   ("Two sources of truth", "PLAN.md says step 2 is done while the session task list says it is pending, and nobody knows which is right.", "Name one as canonical (the file) and have Claude mirror ticks into it after each verified step."),
   "plan mode is Module 2.1; sessions and resume are Module 2.4.", "file for durability, tool for pace."),
  ("A PLAN.md that resumes cleanly",
   "A plan file helps a fresh session continue. Each step should carry its check so a resumed session can tell done from started. This layout is the guide's own.",
   """
```markdown
# PLAN: rate limiter (from SPEC.md)
- [x] 1 Add limiter.ts with check()          verify: vitest limiter  (green, 14:02)
- [x] 2 Wire middleware                      verify: vitest api       (green, 14:20)
- [ ] 3 Add 429 + Retry-After header          verify: curl loop V2
- [ ] 4 Docs + changelog                      verify: link check
## Notes for next session
Step 3 blocked on header name decision D4.
```""",
   ("Tick-then-check", "Claude ticks a box when it writes the code, not when the check passes, so the plan overstates progress.", "Define the tick as 'check ran and passed', record the evidence beside the box, and reject unticked-by-evidence steps in review."),
   "specs are Module 9.1.2; verification is Module 9.2.", "a tick means the check ran."),
  ("Using it across resets",
   "Starting a session from a file is the same move as the spec workflow: the docs advise a fresh session to build from SPEC.md [%s]. `claude --continue` resumes the most recent session in the directory, and `--resume` picks from a list [Claude Code docs, Common workflows, 2026]." % BP,
   """
| Situation | Move |
|---|---|
| Context bloated mid-plan | `/clear`, then 'continue PLAN.md from the first unticked step' |
| Next day, same work | `claude --continue` or fresh session plus PLAN.md |
| Handoff to a teammate | Commit PLAN.md; they read the notes block |""",
   ("Stale plan", "The plan is never updated after reality changed, so the next session executes dead steps.", "Update PLAN.md in the same commit as the code that changes it (Module 9.1.6)."),
   "keeping specs alive is Module 9.1.6.", "resume from the file, not from memory."),
 ],
 [("Name the four task-tracking tools.", "TaskCreate, TaskGet, TaskList, TaskUpdate."),
  ("Which tool is disabled by default and which variable re-enables it?", "TodoWrite; `CLAUDE_CODE_ENABLE_TASKS=0`."),
  ("PLAN.md and the session list disagree. Name the failure mode by its exact label.", "**Two sources of truth.**"),
  ("Claude ticks boxes when code is written. Name the failure mode.", "**Tick-then-check.**"),
  ("The next session runs steps that no longer apply. Name the failure mode by its exact label and fix.", "**Stale plan.** Update the plan in the same commit as the change."),
  ("Where are plan mode plan files stored by default?", "`~/.claude/plans/`, or `plansDirectory` if set."),
  ("Name three ways to enter plan mode.", "`Shift+Tab`, `/plan` prefix, `claude --permission-mode plan`."),
  ("Do task tools survive `/clear`?", "No; the file does."),
  ("In the example plan, how many steps are ticked?", "Two of four."),
 ],
 ("A PLAN.md with four steps, each with a verify command, and a log showing a session reset mid-plan.",
  [("Write PLAN.md from a spec", "File"), ("Run step 1 and 2 with evidence", "Ticks and logs"), ("`/clear`", "New context"),
   ("Resume from the first unticked step", "Transcript"), ("Finish and commit PLAN.md", "Commit")]),
 """
| Check | Evidence |
|---|---|
| Ticks with evidence | 2 with timestamps |
| Resume from file | Transcript quotes step 3 |
""", """
| Element | What is wrong |
|---|---|
| Ticks without evidence | **Tick-then-check** |
| Plan lists finished work as pending | **Stale plan** |
""",
 "The artifact passes only if every ticked box has evidence and the resumed session started from the first unticked step.",
 [("Anthropic", "Tools reference: task tools", "Names, permissions, availability", "Current"), ("Anthropic", "Permission modes: Plan mode", "Entering plan mode, plan file location", "Current")],
 "the Tools reference limits task tools by model, while other pages assume them everywhere; verify on your model.",
 "This is the craft of plans: **file for memory, tool for pace, evidence for ticks.** The engineer who understands this does not ask \"where is the plan?\" — they ask \"what proves step 3 is done?\"", read=16, prove_h="1.5"))

SPECS.append(G(M, "9.1.5", "Specs as the review artefact",
 "When a spec exists, a reviewer checks the diff against stated requirements instead of guessing intent, which makes review faster and makes gaps reportable.",
 "review one diff against one spec and produce a gap list that cites requirement ids.",
 "review the diff against the spec first, then for style only if asked.",
 "a reviewer who is told to find problems will always find something, so the spec must bound what counts as a problem [%s]." % BP,
 [("Two reviewers, two questions",
   "The docs describe two review routes. In the terminal, `/code-review` reviews the diff in a fresh subagent that never saw your conversation, so it is not swayed by the reasoning that produced the code [%s]. The spec review is a prompt you write yourself to check the work against your plan [%s]." % (BP, BP),
   """
| Reviewer | Question | Standard |
|---|---|---|
| `/code-review` | Are there correctness bugs? | General correctness |
| Spec-review prompt | Is every requirement built and every edge case tested? | SPEC.md |
| Human | Is this the right thing and is it maintainable? | Judgement |

`/code-review [low|medium|high|xhigh|max|ultra] [--fix] [--comment] [pr#|branch|path]` reviews the current diff, a PR number, a branch or a path; `--comment` posts findings to the PR [Claude Code docs, Commands, 2026].""",
   ("Wrong-standard review", "You run a general bug review and conclude the feature is complete, but a requirement was never built.", "Run the spec-review prompt as well; a bug hunt cannot find an omission."),
   "AI-code review norms are Module 9.12.3; fresh-context review is Module 9.13.3.", "bugs and omissions need different reviewers."),
  ("Writing the spec-review prompt",
   "Use the docs' form: a subagent reviews the diff against SPEC.md, checks every requirement is implemented and the listed edge cases have tests, reports gaps that affect correctness and skips style [%s]." % BP,
   """
| Output column | Meaning |
|---|---|
| Requirement id | R1, E2, V1 from SPEC.md |
| Status | Built, partial, missing |
| Evidence | File:line or test name |
| Severity | Affects correctness or not |

```text
Review the diff against SPEC.md. Table: id, status, evidence. Report only gaps that
affect correctness. Skip style.
```""",
   ("Style-noise review", "Style comments drown the two real gaps and the author fixes the wrong things.", "Keep 'skip style' in the prompt and ask for severity so triage is mechanical."),
   "refactor guard is Module 9.4.7.", "a table keyed to ids makes the review auditable."),
  ("What reviewers do with the result",
   "The finding list is input to a decision, not a to-do list. The docs warn that fixing every finding from a reviewer told to find problems yields extra abstraction layers and tests for cases that cannot happen [%s]." % BP,
   """
| Gap type | Action |
|---|---|
| Requirement missing | Build it, add a test |
| Edge case untested | Add a test (Module 9.2.3) |
| Spec wrong | Edit the spec first (Module 9.1.6), then the code |
| Style only | Ignore unless the team rule says otherwise |""",
   ("Fix-everything reflex", "You fix every finding and the diff grows with defensive code the spec never asked for.", "Triage each finding against the spec; reject any that does not map to a requirement or a real edge case."),
   "diff size limits are Module 9.13.3.", "findings are proposals, not orders."),
 ],
 [("Which review route uses a fresh subagent that never saw your conversation?", "`/code-review`."),
  ("What does `--comment` do on `/code-review`?", "Posts the findings to the GitHub pull request or GitLab merge request."),
  ("A bug-hunt review passed but a requirement was never built. Name the failure mode by its exact label.", "**Wrong-standard review.**"),
  ("Style comments bury two real gaps. Name the failure mode.", "**Style-noise review.**"),
  ("You fix every finding and add unneeded code. Name the failure mode by its exact label and fix.", "**Fix-everything reflex.** Triage each finding against the spec."),
  ("Name the four columns of the spec-review output table.", "Requirement id, status, evidence, severity."),
  ("What does the docs' spec-review prompt tell the reviewer to skip?", "Style."),
  ("Which effort levels can `/code-review` take? Count them.", "Six: low, medium, high, xhigh, max, ultra."),
 ],
 ("A spec-review table for one real diff, with each gap mapped to a requirement id and an action.",
  [("Pick a diff with a SPEC.md", "Inputs"), ("Run the spec-review prompt", "Table"), ("Run `/code-review` separately", "Bug list"), ("Compare which gaps each found", "Comparison"), ("Triage and act", "Action list")]),
 """
| Id | Status | Action |
|---|---|---|
| R2 | missing | Build |
| E1 | untested | Add test |
""", """
| Element | What is wrong |
|---|---|
| Only a bug review | **Wrong-standard review** |
| Every finding fixed | **Fix-everything reflex** |
""",
 "The artifact passes only if at least one finding came from the spec review that the bug review did not report, and each action cites an id.",
 [("Anthropic", "Best practices: Give Claude a check to run", "Fresh-context review; spec review", "Current"), ("Anthropic", "Commands: /code-review", "Flags and levels", "Current")],
 "none found between the sources read.",
 "This is the craft of spec review: **a fixed standard, a table of ids, triage before fixing.** The engineer who understands this does not ask \"did the reviewer find anything?\" — they ask \"which requirement is unmet?\"", read=16, prove_h="1.5"))

SPECS.append(G(M, "9.1.6", "Keeping specs alive",
 "A spec that is not updated when reality changes becomes a false standard, so update it in the same change as the code and move durable decisions into CLAUDE.md or decision records.",
 "show a diff where code and spec change together, and a decision moved from SPEC.md into a durable home.",
 "no code change that contradicts the spec merges without a spec edit.",
 "most of what a spec says should die with the feature; only decisions that guide future work deserve a permanent home.",
 [("Update the spec in the same change",
   "When implementation discovers the spec was wrong, edit the spec first, then the code, so review still has a true standard. This guide treats that as judgement; the docs only establish that the spec is the file reviewers check against [%s]." % BP,
   """
| Discovery | Edit |
|---|---|
| Edge case not in spec | Add E-number, then test |
| Requirement impossible | Strike with a reason, note in PR |
| Scope grew | Move to Out of scope or a new spec |

```bash
git diff --stat   # SPEC.md and the code appear in the same commit
```""",
   ("Spec drift", "The code changed and SPEC.md still states the old behaviour, so the next review fails correct work or passes wrong work.", "Make 'SPEC.md updated or no behavioural change' a line in the definition of done (Module 9.12.4)."),
   "definition of done is Module 9.12.4.", "the spec changes in the same commit."),
  ("Where durable decisions live",
   "The docs say CLAUDE.md should hold only what Claude cannot work out from the code: commands, misleading places, decisions not in the repo, anything corrected twice. Keep it short; `/init` output should be trimmed and the memory guide recommends staying under 200 lines [%s]." % BP,
   """
| Content | Home |
|---|---|
| This feature's requirements | SPEC.md (delete or archive after merge) |
| A team-wide decision ('use errors.ts helpers') | CLAUDE.md |
| Rule for one directory | `.claude/rules/*.md` with `paths:` |
| Why we chose X over Y | Decision record (ADR) in docs/ |
| Procedure | A skill |""",
   ("Spec hoarding", "Every old SPEC.md stays in the repo and in CLAUDE.md, the file balloons and relevant lines get lost.", "Promote only decisions that will guide future work; archive or delete the rest at merge."),
   "CLAUDE.md craft is Module 3.2; decision records are Module 9.11.1.", "promote decisions, retire requirements."),
  ("Specs and path-scoped rules",
   "A rule that matters in one part of the code belongs in `.claude/rules/` with a `paths:` filter so it loads only there [%s]. The docs example loads a rule for `src/api/**/*.ts`." % BP,
   """
```markdown
---
paths:
  - "src/api/**/*.ts"
---
- Every new endpoint needs an entry in openapi.yaml, CI fails without it
```""",
   ("Global rule for local fact", "A rule about one directory sits in the root CLAUDE.md and loads for every task.", "Move it to a path-scoped rules file."),
   "rules files are Module 3.3.", "scope rules to where they apply."),
 ],
 [("Where do durable team decisions go according to the docs' CLAUDE.md guidance?", "CLAUDE.md (only what Claude cannot work out from the code)."),
  ("What line count does the memory guide recommend staying under for CLAUDE.md?", "Under 200 lines."),
  ("SPEC.md says X, code does Y. Name the failure mode by its exact label.", "**Spec drift.**"),
  ("Old specs bloat CLAUDE.md. Name the failure mode.", "**Spec hoarding.**"),
  ("A directory rule loads for every task. Name the failure mode by its exact label and fix.", "**Global rule for local fact.** Use `.claude/rules/` with `paths:`."),
  ("What frontmatter key scopes a rules file?", "`paths:`."),
  ("Which command generates a starting CLAUDE.md?", "`/init`."),
  ("What does `/doctor prompt-audit` flag?", "Instructions written for older models, pointers to missing files, and contradictions."),
 ],
 ("A commit diff changing code and SPEC.md together, plus one decision promoted to CLAUDE.md or a rules file.",
  [("Find a spec contradicted by the build", "Evidence"), ("Edit spec first", "Spec diff"), ("Edit code", "Code diff"), ("Promote one decision", "CLAUDE.md or ADR diff"), ("Archive the spec", "Move or delete")]),
 """
| Item | Evidence |
|---|---|
| Spec edit in same commit | yes |
| Promoted decision | 1 line in rules file |
""", """
| Element | What is wrong |
|---|---|
| Code only changed | **Spec drift** |
| Whole spec pasted in CLAUDE.md | **Spec hoarding** |
""",
 "The artifact passes only if the commit touches both SPEC.md and code and at most one durable line is promoted.",
 [("Anthropic", "Best practices: Keep CLAUDE.md short; Scope rules", "What belongs in CLAUDE.md and rules files", "Current")],
 "the docs do not give an update protocol for specs; same-commit updating is this guide's recommendation.",
 "This is the craft of living specs: **same-commit edits, promote decisions, retire requirements.** The engineer who understands this does not ask \"where do I keep this spec?\" — they ask \"which of these lines will still matter in a year?\"", read=15, prove_h="1.5"))

if __name__ == "__main__":
    for s in SPECS:
        write(s)
