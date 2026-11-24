import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from specs_b9_lib import G, write

M = "b-9-4"
BP = "Claude Code docs, Best practices, 2026"
CW = "Claude Code docs, Common workflows, 2026"
CMD = "Claude Code docs, Commands, 2026"
HL = "Claude Code docs, Headless, 2026"
WT = "Claude Code docs, Worktrees, 2026"
SPECS = []

SPECS.append(G(M, "9.4.1", "Characterisation tests first",
 "Before changing structure, lock the current behaviour with tests that record what the code does today, so any change in behaviour during a refactor turns a test red.",
 "write characterisation tests for an untested function, show they pass on the current code and fail on a deliberate behaviour change.",
 "pin what the code does, not what it should do, before touching it.",
 "a characterisation test may enshrine a bug, and that is acceptable: it separates 'preserve' decisions from 'fix' decisions.",
 [("What a characterisation test is",
   "A characterisation test records current behaviour, correct or not, as the safety net for restructuring. The docs' test workflow begins by finding functions not covered by tests, then generating scaffolding, then adding edge cases, then running and verifying [%s]." % CW,
   """
| Step | Prompt |
|---|---|
| Find gaps | "find functions in NotificationsService.swift that are not covered by tests" |
| Pin behaviour | "write tests that assert exactly what each function returns today for these inputs; do not fix anything" |
| Edge cases | "add cases for boundary values and error conditions" |
| Verify | "run the new tests and fix any failures" (failures here mean the test is wrong, not the code) |""",
   ("Fixing while pinning", "Claude 'corrects' a bug while writing the test, so the test no longer records current behaviour.", "Say 'do not change source files in this task' and check the diff touches only test files."),
   "test quality is Module 9.2.3; legacy work is Module 9.5.4.", "pin first, judge later."),
  ("Choosing inputs",
   "Characterisation depends on input coverage. Ask Claude to read the code paths and propose inputs that hit each branch, then confirm each branch with the test run. Branch coverage numbers come from your own coverage tool; this guide verified no specific tool.",
   """
| Input class | Examples |
|---|---|
| Typical | Real values from logs |
| Boundary | Empty, zero, max length |
| Error | Invalid type, missing field |
| Historical | Inputs from past bug reports |""",
   ("Happy-path pin", "Only typical inputs are pinned, so a refactor that changes error handling passes.", "Require at least one input per branch and per error path."),
   "reproduction is Module 9.3.1.", "pin the branches you will touch."),
  ("Prove the net holds",
   "Introduce a deliberate behaviour change and confirm the pinned tests catch it. This is the same break-the-code check as in Module 9.2.3, applied before the refactor rather than after.",
   """
| Probe | Expected |
|---|---|
| Change a return value | A pinned test fails |
| Reorder output | A pinned test fails |
| Rename internals only | All tests stay green |""",
   ("Hole in the net", "A probe change stays green, so a refactor could break that behaviour unseen.", "Add a test for the missed behaviour before starting the refactor."),
   "small steps are Module 9.4.2.", "probe the net before relying on it."),
 ],
 [("What does a characterisation test assert?", "What the code does today, correct or not."),
  ("Claude fixed a bug while pinning. Name the failure mode by its exact label.", "**Fixing while pinning.**"),
  ("Only typical inputs were pinned. Name the failure mode.", "**Happy-path pin.**"),
  ("A probe change stayed green. Name the failure mode by its exact label and fix.", "**Hole in the net.** Add a test before refactoring."),
  ("What first prompt does the docs' test workflow use?", "Find functions that are not covered by tests."),
  ("What instruction prevents source edits during pinning?", "'Do not change source files in this task.'"),
  ("Name three input classes for pinning.", "Typical, boundary, error, historical."),
  ("Did this guide verify a coverage tool?", "No."),
 ],
 ("A pinned test file for one untested function and a probe table showing each deliberate change was caught.",
  [("Find an untested function", "Name"), ("Pin with inputs per branch", "Test file"), ("Confirm no source diff", "git diff"), ("Probe three changes", "Probe table"), ("Fill any hole", "Extra tests")]),
 """
| Probe | Result |
|---|---|
| Return value | test fails |
| Reorder | test fails |
""", """
| Element | What is wrong |
|---|---|
| Source edited | **Fixing while pinning** |
| Probe stays green | **Hole in the net** |
""",
 "The artifact passes only if the diff touches only test files and every probe turned a test red.",
 [("Anthropic", "Common workflows: Work with tests", "Gap-finding and edge cases", "Current")],
 "none found; the characterisation-test concept is general practice and not defined in the docs.",
 "This is the craft of pinning: **record, probe, then refactor.** The engineer who understands this does not ask \"is the code right?\" — they ask \"what must not change?\"", read=14, prove_h="1.5", thin="the concept is general practice; only the test workflow prompts are from the docs"))

SPECS.append(G(M, "9.4.2", "Small steps with verification between them",
 "Refactoring succeeds as a chain of small changes each followed by a check, so a failure localises to the last step and rewinding costs one step, not a day.",
 "perform a refactor in at least five steps with a recorded green check after each.",
 "never take a second step on a red first step.",
 "the speed of a refactor is the speed of its slowest recovery, so smaller steps are faster overall.",
 [("The step contract",
   "The docs advise doing refactoring in small, testable increments and verifying with tests after each [%s]. Claude Code adds `/rewind` (or double `Esc`) to roll code, conversation or both back to an earlier prompt [%s]." % (CW, BP),
   """
| Step | Check | On red |
|---|---|---|
| Extract function | Pinned tests | `/rewind` to previous prompt |
| Rename | Typecheck plus tests | Revert |
| Move file | Imports resolve, tests | Revert |
| Remove duplicate | Tests | Revert |
| Simplify | Tests, `/simplify` | Revert |

Checkpoints cover files edited with Claude's own file tools; a file touched only by a Bash command is not restored, so commit often [%s].""" % BP,
   ("Step pile-up", "Five changes land before the first check, and a red result cannot be localised.", "One concern per step, a check after each, and a commit on green."),
   "checkpoints are Module 2.5; characterisation is Module 9.4.1.", "check after every step."),
  ("Commit rhythm",
   "A commit per green step makes bisect and revert trivial and keeps diffs reviewable. Ask Claude to commit only after the check passes and to show its output.",
   """
```text
Do step 1 only: extract the validation block into validate().
Run the pinned tests and show output. If green, commit with message "refactor: extract validate()".
Stop and wait.
```

| Practice | Benefit |
|---|---|
| One commit per step | Small revert unit |
| Message names the step | Review by commit |
| Stop after each | Human checkpoint |""",
   ("Mega-commit", "A single commit contains all steps, so nothing can be reverted selectively.", "Commit per green step; squash later only if the team wants."),
   "pull request norms are Module 9.12.2.", "commit per verified step."),
  ("Stopping rules",
   "Define when a step is too big: the check fails twice, or the diff exceeds your review limit. The docs advise after more than two failed corrections to `/clear` and write a better prompt [%s]." % BP,
   """
| Signal | Action |
|---|---|
| Two failed corrections | `/clear`, new prompt with lessons |
| Diff over your size limit | Split the step |
| Check slow | Narrow to one file in the inner loop (Module 9.2.6) |""",
   ("Correction spiral", "You keep correcting a failed step inside one cluttered context.", "After two failed corrections, `/rewind` or `/clear` and restate the step smaller."),
   "the loop is Module 1.2.", "shrink the step when it fails."),
 ],
 [("What does the docs advise about refactoring increments?", "Do it in small, testable increments."),
  ("Five changes landed before the first check. Name the failure mode by its exact label.", "**Step pile-up.**"),
  ("One commit holds every step. Name the failure mode.", "**Mega-commit.**"),
  ("You keep correcting inside one cluttered context. Name the failure mode by its exact label and fix.", "**Correction spiral.** `/rewind` or `/clear`; restate smaller."),
  ("How many failed corrections justify `/clear` per the docs?", "More than two."),
  ("What does `/rewind` roll back?", "Code, conversation or both."),
  ("Which edits do checkpoints not cover?", "Files touched only by a Bash command."),
  ("How many steps does the prove-it require?", "At least five."),
 ],
 ("A five-step refactor log with check output and commit hash per step.",
  [("Choose a refactor", "Plan"), ("Write five steps with checks", "Step list"), ("Run each, commit on green", "5 commits"), ("Force one red and rewind", "Rewind log"), ("Summarise", "Notes")]),
 """
| Step | Result |
|---|---|
| 1 extract | green, abc123 |
| 2 rename | green, def456 |
""", """
| Element | What is wrong |
|---|---|
| One big commit | **Mega-commit** |
| Checks at the end | **Step pile-up** |
""",
 "The artifact passes only if each step has its own check output and commit, including one recovered red.",
 [("Anthropic", "Common workflows: Refactor code", "Small testable increments", "Current"), ("Anthropic", "Best practices: Steer the session", "Rewind and clear", "Current")],
 "none found between the sources read.",
 "This is the craft of small steps: **one concern, one check, one commit.** The engineer who understands this does not ask \"can I do it all at once?\" — they ask \"what is the smallest step I can verify?\"", read=13, prove_h="1.5"))

SPECS.append(G(M, "9.4.3", "Framework, language and dependency upgrades",
 "Upgrades go best as staged changes driven by the changelog: read the release notes, update one version step at a time, run tests, fix deprecations, and repeat.",
 "upgrade one dependency across a major version in stages with a green suite after each.",
 "upgrade one major boundary at a time and never in the same change as a feature.",
 "skipping straight to the latest version feels fast and makes every failure ambiguous.",
 [("Changelog-driven plan",
   "Have Claude read the changelogs or migration guide for each version between yours and the target, then produce an ordered plan. The docs' refactor workflow starts by finding deprecated API usage in the codebase [%s]." % CW,
   """
| Step | Prompt |
|---|---|
| Inventory | "find deprecated API usage in our codebase" |
| Read | "read the migration guide for v4 to v5 at <url>; list breaking changes that affect us" |
| Plan | "propose an ordered list of staged upgrades, each green on its own" |
| Execute | One stage per commit |

Give Claude the changelog text or URL; WebFetch is a built-in tool that prompts for permission by default [Claude Code docs, Tools reference, 2026].""",
   ("Memory-based upgrade", "Claude applies breaking-change fixes from training memory, not the actual release notes, and misses a change.", "Provide the changelog or migration guide as input and ask it to cite the entry for each fix."),
   "web tools are Module 1.2; plans are Module 9.1.4.", "work from the document."),
  ("Stage and verify",
   "Each stage ends with install, typecheck, tests and a smoke run. Use `/verify` for the running app when tests are not enough (Module 9.2.5).",
   """
| Stage | Checks |
|---|---|
| Bump version | install succeeds, lockfile diff reviewed |
| Fix compile errors | typecheck 0 errors |
| Fix tests | suite green |
| Remove deprecation warnings | warnings count 0 |
| Smoke run | `/verify` observes the app |""",
   ("Big-bang bump", "Three majors are bumped together and a failure could be any of them.", "Upgrade one major at a time with a green suite between."),
   "small steps are Module 9.4.2.", "stage the upgrade."),
  ("Lockfiles, transitive and security",
   "Review lockfile diffs for unexpected transitive changes. Run your package manager's audit command as a check; this guide verified no specific command.",
   """
| Review item | Action |
|---|---|
| New transitive packages | Confirm each is expected |
| Licence changes | Check policy |
| Peer-dependency warnings | Resolve before merge |
| Audit output | Triage, do not blanket-ignore |""",
   ("Blind lockfile accept", "A huge lockfile diff is accepted without review and pulls in an unwanted package.", "Ask Claude to summarise lockfile changes and flag additions."),
   "dependency audits are Module 9.10.3.", "the lockfile is code."),
 ],
 [("What does the docs' refactor workflow ask first?", "Find deprecated API usage in the codebase."),
  ("Claude fixed breaking changes from memory. Name the failure mode by its exact label.", "**Memory-based upgrade.**"),
  ("Three majors were bumped together. Name the failure mode.", "**Big-bang bump.**"),
  ("A giant lockfile diff was accepted unread. Name the failure mode by its exact label and fix.", "**Blind lockfile accept.** Summarise and flag additions."),
  ("Name the five stage checks in the table.", "Install, typecheck, tests, warning count, smoke run."),
  ("Does WebFetch prompt for permission in Manual mode?", "Yes."),
  ("What skill observes the running app after an upgrade?", "`/verify`."),
  ("Did this guide verify an audit command?", "No."),
 ],
 ("A staged upgrade log: version path, per-stage checks and a lockfile summary.",
  [("Inventory deprecations", "List"), ("Read the guide, list breaking changes", "Notes"), ("Stage 1 bump and check", "Commit"), ("Stage 2 fix and check", "Commit"), ("Lockfile review", "Summary")]),
 """
| Stage | Check |
|---|---|
| bump 4.2 to 5.0 | tests green |
| fix deprecations | 0 warnings |
""", """
| Element | What is wrong |
|---|---|
| Jump 3 majors | **Big-bang bump** |
| No source for fixes | **Memory-based upgrade** |
""",
 "The artifact passes only if each stage is a separate green commit and each fix cites a changelog entry.",
 [("Anthropic", "Common workflows: Refactor code", "Deprecation search", "Current"), ("Anthropic", "Tools reference: WebFetch", "Permission behaviour", "Current")],
 "none found; package-manager audit tooling was not fetched.",
 "This is the craft of upgrades: **document-driven, staged, lockfile-reviewed.** The engineer who understands this does not ask \"what version should we be on?\" — they ask \"which single step is next, and what proves it?\"", read=13, prove_h="1.5", thin="audit tooling unverified; the upgrade method is general practice anchored on the docs' refactor workflow"))

SPECS.append(G(M, "9.4.4", "Parallel migration",
 "`/batch` decomposes a large change into independent units run in isolated worktrees, and a shell loop over `claude -p` does the same for a list of files you control.",
 "migrate a set of files in parallel through /batch or a loop and show per-unit checks and a merged result.",
 "approve the decomposition before any unit runs.",
 "parallelism helps only when units are truly independent; a shared file turns it into merge conflicts.",
 [("/batch",
   "`/batch <instruction>` is a bundled skill that researches the codebase, decomposes the work into 5 to 30 independent units, and presents a plan. Once approved, it spawns one background subagent per unit in an isolated worktree; each implements its unit, runs tests and publishes its change. It requires a git repository or a `WorktreeCreate` hook, and outside a git repository needs v2.1.281 or later [%s]." % CMD,
   """
| Property | Value |
|---|---|
| Example | `/batch migrate src/ from JavaScript to TypeScript` |
| Units | 5 to 30 |
| Isolation | One worktree per unit |
| Gate | You approve the plan first |
| Each unit | Implements, runs tests, publishes |""",
   ("Coupled units", "The plan splits work that touches a shared module, so units conflict when they publish.", "Review the plan for shared files and move them into a prior serial step."),
   "worktrees are Module 6.2; dynamic workflows are Module 6.5.", "approve the split."),
  ("Loop claude -p over a list",
   "When you already have the file list, script it. `claude -p` runs non-interactively; `--allowedTools` pre-approves tools; `--max-turns` and `--max-budget-usd` bound a run, and `--bare` skips auto-discovery for reproducible CI runs [%s; %s]." % (HL, BP),
   """
```bash
while read f; do
  claude -p "Migrate $f from callbacks to async/await. Keep behaviour. Run its tests." \\
    --allowedTools "Read,Edit,Bash(pnpm vitest run *)" --max-turns 20 \\
    >> migrate.log
done < files.txt
```

| Option | Purpose |
|---|---|
| `--allowedTools` | Pre-approve tools |
| `--output-format json` | Parse results including `total_cost_usd` |
| `--permission-mode acceptEdits` | Baseline for edits |
| `--max-budget-usd` | Cap spend with `-p` |""",
   ("Unbounded fan-out", "The loop has no turn or budget cap and one stuck file burns the budget.", "Set `--max-turns` or `--max-budget-usd` and log per-file exit codes."),
   "headless is Module 6.8.", "bound each unit."),
  ("Collecting and verifying results",
   "Per-unit checks do not prove the whole. After merging, run the full suite and the app. Subagent worktrees with changes persist until the sweep can remove them; remove manually with `git worktree remove` [%s]." % WT,
   """
| Phase | Check |
|---|---|
| Per unit | Unit tests in the worktree |
| After each merge | Full suite |
| End | `/verify` on the app |
| Cleanup | `git worktree list`, remove leftovers |""",
   ("Green parts, red whole", "Each unit passed alone but the merged result fails an integration test.", "Merge sequentially and run the full suite after each merge."),
   "verification is Module 9.2.5.", "verify the sum, not only the parts."),
 ],
 [("How many units does /batch decompose into?", "5 to 30."),
  ("What does /batch do after you approve the plan?", "Spawns one background subagent per unit in an isolated worktree."),
  ("The plan split work across a shared module. Name the failure mode by its exact label.", "**Coupled units.**"),
  ("A loop with no cap burned the budget. Name the failure mode.", "**Unbounded fan-out.**"),
  ("Each unit passed but the merge failed. Name the failure mode by its exact label and fix.", "**Green parts, red whole.** Merge sequentially, run the full suite each time."),
  ("Which flags bound a `claude -p` run?", "`--max-turns` and `--max-budget-usd`."),
  ("What does `--bare` do?", "Skips auto-discovery of hooks, skills, plugins, MCP servers, memory and CLAUDE.md."),
  ("Which version does /batch outside a git repo need?", "v2.1.281 or later."),
 ],
 ("A parallel migration of at least eight files with per-unit and merged checks.",
  [("Choose independent files", "List"), ("Run /batch or the loop", "Logs"), ("Review unit results", "Table"), ("Merge sequentially", "Commits"), ("Run full suite and verify", "Output")]),
 """
| Unit | Result |
|---|---|
| a.js | tests green |
| b.js | tests green |
Full suite after merge: green
""", """
| Element | What is wrong |
|---|---|
| Plan not reviewed | **Coupled units** |
| No cap | **Unbounded fan-out** |
""",
 "The artifact passes only if the plan was reviewed before units ran and the merged result passed the full suite.",
 [("Anthropic", "Commands: /batch", "Decomposition and worktrees", "Current"), ("Anthropic", "Headless", "claude -p flags", "Current"), ("Anthropic", "Worktrees", "Cleanup", "Current")],
 "`/batch` and a shell loop overlap: /batch plans and isolates for you, the loop gives exact control; the docs do not rank them.",
 "This is the craft of parallel migration: **independent units, bounded runs, verified sum.** The engineer who understands this does not ask \"how fast can it fan out?\" — they ask \"are these units really independent?\"", read=15))

SPECS.append(G(M, "9.4.5", "Strangler patterns",
 "The strangler pattern wraps old behaviour behind a new interface, routes a small share of traffic to the new implementation and grows that share while the old path stays available to roll back.",
 "build a routing seam, move one route's traffic to a new implementation behind a flag and show the rollback.",
 "build the seam before the new implementation, and keep rollback a single switch.",
 "the new code is the easy part; the seam, the traffic switch and the comparison are the migration.",
 [("Seam, flag, compare",
   "The pattern is general architecture practice, not from the Claude Code docs. Claude's role is to write the facade, flag and comparison harness from a spec and to run the checks the docs recommend.",
   """
| Element | Purpose |
|---|---|
| Facade | One entry point both paths sit behind |
| Flag or percentage | Chooses old or new |
| Shadow compare | Run both, return old, log differences |
| Rollback | Flip the flag |

```text
Create a facade for pricing.calculate() that calls legacy or new based on flag PRICING_NEW (0 to 100).
In shadow mode call both, return legacy, and log any difference with inputs. Do not change legacy.
```""",
   ("Unreachable rollback", "The old path is deleted or diverges, so a bad rollout cannot be undone.", "Keep the old path untouched until the new one has run clean for your agreed period."),
   "characterisation tests are Module 9.4.1; gradual modernisation is Module 9.5.4.", "keep the exit open."),
  ("Moving traffic gradually",
   "Increase the share in steps and watch comparison logs and error rates between steps; use read-only observability access (Module 9.3.4).",
   """
| Stage | Share | Gate |
|---|---|---|
| Shadow | 0% served by new | Differences understood |
| Canary | small share (your choice) | Error rate flat |
| Majority | increasing | No new differences |
| Full | 100% | Old path removable after soak |""",
   ("Blind ramp", "Share increases on a schedule with nobody reading comparison logs.", "Make each step conditional on a reviewed comparison report."),
   "observability is Module 9.3.4.", "ramp on evidence."),
  ("Deleting the old path",
   "Remove old code only after a soak period and with a deletion PR that stands alone. Cleanup passes (Module 9.4.6) apply after.",
   """
| Check before delete | Evidence |
|---|---|
| No traffic to old | Metrics show 0 |
| No references | `grep` shows none |
| Tests | New path covered |
| Rollback plan | Documented or consciously retired |""",
   ("Zombie legacy", "The old path stays forever because deletion was never scheduled.", "Put the deletion ticket in the plan at the start."),
   "cleanup is Module 9.4.6.", "plan the ending at the start."),
 ],
 [("What are the four elements of the seam table?", "Facade, flag or percentage, shadow compare, rollback."),
  ("The old path was deleted early. Name the failure mode by its exact label.", "**Unreachable rollback.**"),
  ("The share grows on a timer with no review. Name the failure mode.", "**Blind ramp.**"),
  ("The legacy path was never removed. Name the failure mode by its exact label and fix.", "**Zombie legacy.** Schedule the deletion ticket at the start."),
  ("In shadow mode, which path's result is returned?", "The legacy path's."),
  ("Is the strangler pattern described in the Claude Code docs?", "No; it is general practice."),
  ("What flag range does the example use?", "0 to 100."),
  ("What check precedes deleting old code?", "No traffic, no references, new path covered."),
 ],
 ("A facade with flag, a shadow-compare log and a rollback demonstration.",
  [("Write the facade", "Code"), ("Shadow-run", "Compare log"), ("Move one route", "Flag value"), ("Roll back", "Log"), ("Plan deletion", "Ticket")]),
 """
| Stage | Evidence |
|---|---|
| Shadow | 0 diffs in 1000 calls |
| Rollback | flag flip restores legacy |
""", """
| Element | What is wrong |
|---|---|
| No flag | **Unreachable rollback** |
| No review of diffs | **Blind ramp** |
""",
 "The artifact passes only if the rollback was exercised and shadow differences were reviewed before any traffic moved.",
 [("Anthropic", "Common workflows: Refactor code", "Incremental increments", "Current")],
 "none found; the pattern is general architecture practice with no vendor source here.",
 "This is the craft of strangling: **seam first, ramp on evidence, plan the deletion.** The engineer who understands this does not ask \"is the new code done?\" — they ask \"how do I undo this in one switch?\"", read=13, prove_h="2", thin="pattern is general architecture practice; no Claude Code doc covers it"))

SPECS.append(G(M, "9.4.6", "Cleanup passes",
 "`/simplify` reviews changed code for reuse, simplification, efficiency and the right level of abstraction and applies the fixes, while `/code-review` is the tool for correctness bugs.",
 "run /simplify on a diff, classify each change it made and confirm tests still pass.",
 "cleanup passes follow green tests and never mix with behaviour changes.",
 "a cleanup pass that is not reviewed can be a rewrite in disguise.",
 [("What /simplify does",
   "`/simplify [target]` reviews changed code for cleanup opportunities and applies fixes. Four review agents run in parallel covering reuse of existing helpers, simplification, efficiency, and whether the change is at the right level of abstraction. It does not look for correctness bugs; use `/code-review` for that. Pass a path or PR reference to review a specific target [%s]." % CMD,
   """
| Command | Looks for | Applies fixes |
|---|---|---|
| `/simplify` | Reuse, simplification, efficiency, abstraction level | Yes |
| `/code-review` | Correctness bugs (and, by model and effort, cleanup) | With `--fix` |

Order: tests green, `/simplify`, tests green, `/code-review`.""",
   ("Cleanup as rewrite", "The pass restructures far beyond the diff, and reviewers cannot tell what changed.", "Scope with a target path, cap the diff size, and commit the cleanup separately."),
   "code review is Module 9.12.3.", "scope the pass."),
  ("Review what it changed",
   "Treat the cleanup like any diff: read it, run the checks and reject changes that alter behaviour. The docs warn that a reviewer asked to find problems will always find something, so fixing every finding adds layers [%s]." % BP,
   """
| Change type | Action |
|---|---|
| Reuses an existing helper | Accept after tests |
| Inlines an abstraction | Accept if clearer |
| New abstraction layer | Question; reject unless needed |
| Behaviour change | Revert |""",
   ("Over-abstraction", "The pass introduces a helper used once, and the codebase gains an indirection.", "Reject abstractions with a single caller unless the spec calls for them."),
   "maintainability is Module 9.13.4.", "cleanup should reduce code."),
  ("When to run it",
   "Run after a feature is green and before the PR so reviewers see clean code. Avoid running it on code you did not change unless you scope it by path.",
   """
| Moment | Run |
|---|---|
| Feature green | `/simplify` |
| Before PR | `/code-review` |
| Legacy cleanup | `/simplify path/to/module` with a scoped PR |""",
   ("Drive-by cleanup", "A feature PR includes unrelated cleanup, so review is noisy.", "One concern per PR (Module 9.4.7)."),
   "churn is Module 9.4.7.", "clean after green, in its own commit."),
 ],
 [("Which four concerns do the /simplify agents cover?", "Reuse, simplification, efficiency, abstraction level."),
  ("Does /simplify look for correctness bugs?", "No; use /code-review."),
  ("The pass restructured far beyond the diff. Name the failure mode by its exact label.", "**Cleanup as rewrite.**"),
  ("It added a helper used once. Name the failure mode.", "**Over-abstraction.**"),
  ("Cleanup arrived inside a feature PR. Name the failure mode by its exact label and fix.", "**Drive-by cleanup.** One concern per PR."),
  ("How many review agents does /simplify run?", "Four, in parallel."),
  ("How do you scope /simplify?", "Pass a path or PR reference."),
  ("What order does the guide give?", "Tests green, /simplify, tests green, /code-review."),
 ],
 ("A /simplify run on a diff with a classified change list and green tests before and after.",
  [("Get tests green", "Output"), ("Run /simplify with a path", "Diff"), ("Classify each change", "Table"), ("Revert behaviour changes", "Reverts"), ("Run tests", "Output")]),
 """
| Change | Class |
|---|---|
| use existing helper | accept |
| new wrapper | reject |
""", """
| Element | What is wrong |
|---|---|
| Unscoped run | **Cleanup as rewrite** |
| Wrapper added | **Over-abstraction** |
""",
 "The artifact passes only if every change is classified, none alters behaviour and the suite is green before and after.",
 [("Anthropic", "Commands: /simplify, /code-review", "Scope and agents", "Current"), ("Anthropic", "Best practices: Review against your spec", "Reviewer finds something", "Current")],
 "none found between the sources read.",
 "This is the craft of cleanup: **after green, scoped, reviewed, separate.** The engineer who understands this does not ask \"can it be tidier?\" — they ask \"does this change make the code smaller without changing it?\"", read=12, prove_h="1"))

SPECS.append(G(M, "9.4.7", "Guarding against churn",
 "Keep diffs reviewable: one concern per pull request, bounded size, and explicit limits in the prompt, because an agent will happily touch every file that looks related.",
 "set a diff-size policy, apply it to one task and show that scope stayed within it.",
 "state the scope boundary in the prompt and check the diff against it before review.",
 "cheap code makes big diffs easy, which moves the cost to reviewers; the limit protects them.",
 [("Cause of churn",
   "Claude tends to read a request conservatively, but the docs also note that when you want the fuller version you should say so; the reverse holds: when you want less, bound it [%s]. Unscoped prompts and broad `/simplify` runs create churn." % BP,
   """
| Cause | Control |
|---|---|
| Vague prompt | Name files and out-of-scope |
| Reformat on save | Formatter hook runs only on touched files (docs example: PostToolUse on Edit or Write) |
| Broad refactor | One module per task |
| Generated code | Exclude from edits via deny rule |""",
   ("Scope creep diff", "The diff touches 40 files for a 3-file task because the prompt did not set limits.", "Add 'touch only these files; list anything else you think should change instead of changing it'."),
   "quality discipline is Module 9.13.2.", "ask for suggestions, not edits, outside scope."),
  ("Measuring and limiting",
   "Check `git diff --stat` before asking for review. Define a limit for your team; the number is a policy choice and the docs give none.",
   """
```bash
git diff --stat main...HEAD | tail -1
```

| Policy | Example (illustrative) |
|---|---|
| Max changed files | 15 |
| Max changed lines | 400 |
| Split rule | Separate refactor from behaviour change |
| Exempt | Generated files, lockfiles (reviewed by summary) |""",
   ("Unmeasured diff", "Nobody looks at the stat, and a 3,000-line diff goes to review.", "Add the stat to the PR template and the Stop hook for large diffs."),
   "PR conventions are Module 9.12.2.", "measure before asking for review."),
  ("Splitting after the fact",
   "When a diff is too big, ask Claude to propose a split into commits or PRs by concern, then apply it with interactive-free commands. Keep each piece green.",
   """
| Split by | Result |
|---|---|
| Mechanical (renames) | One PR, reviewed by summary |
| Behaviour | One PR with tests |
| Cleanup | One PR |
| Docs | One PR |""",
   ("Mixed-concern PR", "Renames, features and docs sit in one PR, so reviewers miss the behaviour change.", "Split by concern and keep each branch green."),
   "pairing patterns are Module 9.12.5.", "one concern, one PR."),
 ],
 [("Name two causes of churn in the table.", "Vague prompts, reformat on save, broad refactors, generated code."),
  ("A 3-file task produced a 40-file diff. Name the failure mode by its exact label.", "**Scope creep diff.**"),
  ("Nobody checked the diff size. Name the failure mode.", "**Unmeasured diff.**"),
  ("Renames, features and docs share a PR. Name the failure mode by its exact label and fix.", "**Mixed-concern PR.** Split by concern."),
  ("Does the docs give a diff-size limit?", "No; it is a policy choice."),
  ("What command shows the diff summary?", "`git diff --stat main...HEAD`."),
  ("What do you ask Claude to do with out-of-scope ideas?", "List them instead of changing them."),
  ("What hook event runs a formatter after edits in the docs?", "PostToolUse with matcher Edit|Write."),
 ],
 ("A written diff-size policy and one task's diff stat within it, plus a split of an oversized diff.",
  [("Write the policy", "Policy"), ("Prompt with scope", "Prompt"), ("Check the stat", "Output"), ("Split if over", "PRs"), ("Review", "Notes")]),
 """
| Metric | Result |
|---|---|
| Files | 6 of 15 |
| Lines | 210 of 400 |
""", """
| Element | What is wrong |
|---|---|
| 40 files | **Scope creep diff** |
| Mixed PR | **Mixed-concern PR** |
""",
 "The artifact passes only if the diff stat is within the stated policy and every out-of-scope idea is listed rather than applied.",
 [("Anthropic", "Best practices: Write a specific prompt; hooks", "Scope and formatter hook", "Current")],
 "none found; limits are team policy, not documented.",
 "This is the craft of anti-churn: **state scope, measure, split.** The engineer who understands this does not ask \"how much can Claude change?\" — they ask \"how much can a reviewer hold?\"", read=12, prove_h="1"))

if __name__ == "__main__":
    for s in SPECS:
        write(s)
