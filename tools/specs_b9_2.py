import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from specs_b9_lib import G, write

M = "b-9-2"
BP = "Claude Code docs, Best practices, 2026"
CW = "Claude Code docs, Common workflows, 2026"
SPECS = []

SPECS.append(G(M, "9.2.1", "Red, green, refactor with an agent",
 "Test-driven development maps cleanly onto the agent loop: the failing test is the check Claude can run, so write it first, confirm it fails for the stated reason, implement until it passes, then refactor with the test as a guard.",
 "show a test that failed for the right reason, the minimal change that turned it green, and a refactor that kept it green.",
 "never accept a green run that you did not see red first.",
 "a test that was never red proves nothing, because it may pass for reasons unrelated to the feature [judgement, general practice].",
 [("Red: a failing test for the right reason",
   "Claude stops when the work looks done, so it needs something that returns pass or fail; a test file is the first example of a check the docs list [%s]. Their sample bug prompt asks Claude to write a failing test that reproduces the problem, then fix it [%s]." % (BP, BP),
   """
```text
users report login fails after the session times out. look at token refresh in src/auth/,
write a failing test that reproduces it, then fix it
```

| Red-phase check | How to confirm |
|---|---|
| The test fails | Run it; capture the output |
| It fails for the stated reason | The assertion message names the missing behaviour, not an import error |
| It fails alone | Run only this test file |""",
   ("Wrong-reason red", "The test fails on a typo or missing import, so it turns green after a trivial fix that does not implement the feature.", "Read the failure message; require it to cite the missing behaviour before any implementation starts."),
   "specs name the cases to test: Module 9.1.2; the check concept is Module 2.3.", "red must mean what you think it means."),
  ("Green: smallest change, evidence shown",
   "Once the test is red for the right reason, tell Claude to implement only enough to pass and to show the output. The docs advise asking for evidence rather than a bare 'all tests pass' [%s]." % BP,
   """
| Phase | Prompt | Evidence you require |
|---|---|---|
| Red | "Write the failing test; run it; show the failure" | Failure output |
| Green | "Implement the smallest change that passes; run the test and the neighbouring suite" | Pass output, suite totals |
| Refactor | "Simplify without changing behaviour; rerun" | Same pass output |

Run one file while iterating: `pnpm vitest run path/to/file.test.ts` is the docs' sample single-test command [%s].""" % BP,
   ("Test-editing fix", "Claude makes the test pass by changing the assertion, not the code.", "Say 'do not modify the test' during green, and review the test file diff separately."),
   "separate writers fix this structurally: Module 9.2.2.", "green means the unchanged test passes."),
  ("Refactor with the test as a guard",
   "Refactoring is safe only while the checks stay green. The docs advise small, testable increments when refactoring and running tests for the refactored code [%s]." % CW,
   """
| Refactor step | Guard |
|---|---|
| Rename, extract | Test file still green |
| Remove duplication | Neighbouring suite green |
| Simplify | `/simplify` pass, then rerun (Module 9.4.6) |

`/simplify` reviews changed code for reuse, simplification, efficiency and abstraction level; it does not look for correctness bugs [Claude Code docs, Commands, 2026].""",
   ("Refactor with no guard", "You refactor at the end of a long session without rerunning the red-green test, and a behaviour change slips in.", "Make 'rerun the test after each refactor step' part of the prompt and the Stop hook (Module 9.2.5)."),
   "refactoring at scale is Module 9.4.", "refactor only while green."),
 ],
 [("What are the three phases, in order?", "Red, green, refactor."),
  ("The test fails on a missing import. Name the failure mode by its exact label.", "**Wrong-reason red.**"),
  ("Claude changes the assertion to pass. Name the failure mode.", "**Test-editing fix.**"),
  ("You refactored at session end without rerunning. Name the failure mode by its exact label and fix.", "**Refactor with no guard.** Rerun after each step."),
  ("What does the docs' bug prompt ask Claude to write before fixing?", "A failing test that reproduces the problem."),
  ("What single-test command does the docs' CLAUDE.md sample show?", "`pnpm vitest run path/to/file.test.ts`."),
  ("Does `/simplify` look for correctness bugs?", "No; it reviews reuse, simplification, efficiency and abstraction level."),
  ("How many review agents does `/simplify` run in parallel?", "Four."),
  ("Why require evidence rather than 'all tests pass'?", "A bare claim tells you little; the command and output can be read quickly."),
 ],
 ("A transcript of one red-green-refactor cycle with outputs at each phase and a test diff showing no assertion edits during green.",
  [("Write a failing test", "Test file"), ("Run it and read the failure", "Red output"), ("Implement minimally", "Diff"), ("Run test and suite", "Green output"), ("Refactor in two steps", "Two diffs"), ("Rerun after each", "Two outputs")]),
 """
| Phase | Evidence |
|---|---|
| Red | Failure cites missing behaviour |
| Green | Test file unchanged in diff |
| Refactor | 2 reruns, both green |
""", """
| Element | What is wrong |
|---|---|
| Red is an ImportError | **Wrong-reason red** |
| Assertion edited | **Test-editing fix** |
""",
 "The artifact passes only if the red output names the missing behaviour and the test diff is empty during the green phase.",
 [("Anthropic", "Best practices: Write a specific prompt", "Failing-test-first bug prompt", "Current"), ("Anthropic", "Common workflows: Work with tests; Refactor", "Small increments", "Current")],
 "the docs do not prescribe TDD; red-green-refactor here is general engineering practice applied to the docs' check-first guidance.",
 "This is the craft of TDD with an agent: **a red you understand, a green you watched, a refactor under guard.** The engineer who understands this does not ask \"do the tests pass?\" — they ask \"did they fail first, and for the right reason?\"", read=16))

SPECS.append(G(M, "9.2.2", "Separate writers",
 "When one session writes the tests and another writes the code, the tests cannot be shaped around the implementation, because the second session meets them as fixed requirements.",
 "run two sessions with disjoint roles and show the second never edited the first's tests.",
 "the session that writes the code does not get to change the tests.",
 "the model that wrote the code is the worst reviewer of tests written to fit it, because it carries the reasoning that produced both.",
 [("Why separate",
   "The docs note that a reviewer which has not seen how the code was written is a reason to use a subagent, and that `/code-review` runs in a fresh subagent that never saw your conversation and so is not swayed by the reasoning that produced the code [%s]. The same logic applies to tests." % BP,
   """
| Setup | Risk |
|---|---|
| One session writes both | Tests mirror the implementation's assumptions |
| Two sessions, tests first | The second session meets tests as given |
| Subagent with read-only tools | Reviewer cannot edit (`tools: Read, Grep, Glob`) [%s] |""" % BP,
   ("Mirror test", "Tests assert what the code does, including its bugs, because the same context wrote both.", "Write tests from the spec in a session that has not seen the implementation."),
   "specs are Module 9.1; separate-context review is Module 9.13.3.", "separate context breaks the mirror."),
  ("Mechanics of two sessions",
   "Use a fresh session for each role, committing the tests between them. `claude --worktree <name>` gives each session its own checkout and branch if you want them parallel [Claude Code docs, Worktrees, 2026].",
   """
```bash
# Session A: tests from the spec only
claude --worktree tests-a   # prompt: write tests for SPEC.md, do not look at src/
# Session B: implementation against committed tests
claude --worktree impl-b    # prompt: make tests/ pass; do not edit tests/
```

| Guard | How |
|---|---|
| B cannot edit tests | A PreToolUse hook that exits 2 for `tests/` paths (Module 5.4) |
| A cannot see src | Instruction only; not enforced (judgement) |""",
   ("Unenforced separation", "The rule 'do not edit tests' lives only in the prompt, and the implementer edits an assertion under pressure.", "Enforce it with a PreToolUse hook that exits 2 for test paths, since only hooks and deny rules are deterministic [%s]." % BP),
   "hooks are Module 5.4; worktrees are Module 6.2.", "enforce what must hold."),
  ("What to hand across the boundary",
   "The only things that cross are the spec, the committed tests and the command that runs them. Anything else leaks the implementation's assumptions.",
   """
| Crosses | Does not cross |
|---|---|
| SPEC.md | Chat history |
| Committed tests | Drafts and rejected ideas |
| The run command | Implementation notes |""",
   ("Leaky handoff", "You paste the implementation plan into the test session, so the tests inherit its blind spots.", "Hand over the spec and only the spec."),
   "context sessions are Module 2.4.", "narrow the interface between sessions."),
 ],
 [("Why do separate writers help?", "The code-writing session meets the tests as fixed requirements, so tests are not shaped around the implementation."),
  ("Tests assert the code's own bugs. Name the failure mode by its exact label.", "**Mirror test.**"),
  ("'Do not edit tests' is only in the prompt. Name the failure mode.", "**Unenforced separation.**"),
  ("You pasted the plan into the test session. Name the failure mode by its exact label and fix.", "**Leaky handoff.** Hand over the spec only."),
  ("Which tool allow-list makes a read-only reviewer subagent in the docs?", "`tools: Read, Grep, Glob`."),
  ("What exit code makes a PreToolUse hook block?", "Exit code 2."),
  ("Which flag gives each session its own checkout?", "`--worktree <name>` (or `-w`)."),
  ("Where are worktrees created by default?", "Under `.claude/worktrees/<name>/`."),
 ],
 ("Two session logs, a test commit and an implementation commit, with a hook log showing a blocked edit to tests.",
  [("Session A writes tests from the spec", "Test commit"), ("Session B implements", "Impl commit"), ("Try editing a test in B", "Hook block log"), ("Compare test diff", "Empty diff"), ("Run suite", "Green")]),
 """
| Check | Evidence |
|---|---|
| Hook blocked | stderr reason shown |
| Test diff in B | empty |
""", """
| Element | What is wrong |
|---|---|
| Same session wrote both | **Mirror test** |
| No hook | **Unenforced separation** |
""",
 "The artifact passes only if the second session's commit touches no test file and the block was triggered at least once on purpose.",
 [("Anthropic", "Best practices: Know what subagents cost", "Fresh-eyes reviewer, read-only tools", "Current"), ("Anthropic", "Worktrees", "Isolated parallel sessions", "Current")],
 "teams differ on whether the same person should write both sides; the docs do not take a position and this guide's recommendation is judgement.",
 "This is the craft of separate writers: **tests as a given, enforced boundary, narrow handoff.** The engineer who understands this does not ask \"did Claude write tests?\" — they ask \"could these tests have disagreed with the code?\"", read=15))

SPECS.append(G(M, "9.2.3", "Test quality",
 "A test suite is only as good as its ability to fail when the code is wrong, so avoid over-mocking, test behaviour not structure, cover the edge cases you listed, and prove the tests fail when you break the code.",
 "break the code on purpose in three ways and show the suite catches each.",
 "no test is trusted until it has failed against a deliberately broken implementation.",
 "a high pass rate says nothing about test quality; only failures on broken code do (general practice, not from the Claude Code docs).",
 [("Behaviour over mocks",
   "The docs advise being specific about what behaviour you want to verify when asking for tests; Claude examines existing test files to match style, frameworks and assertion patterns [%s]. Over-mocking is a general-practice hazard: a test that mocks the unit under test asserts the mock." % CW,
   """
| Smell | What it tests | Better |
|---|---|---|
| Mock returns the expected value | The mock | Real collaborator or a fake with logic |
| Asserts call counts only | Wiring | Assert outputs and effects |
| Snapshot of everything | Today's output | Targeted assertions |
| Tests private helpers | Structure | Test through the public interface |""",
   ("Mock-the-subject", "The test replaces the code under test or its decisive collaborator with a mock, so it passes whatever the code does.", "Allow mocks only at process boundaries (network, clock), and require one real-path assertion per test."),
   "integration tests are Module 9.2.4.", "assert behaviour a user would notice."),
  ("Cover the listed edge cases",
   "The docs' review prompt checks that listed edge cases have tests [%s]. So map each edge-case id in the spec to at least one test name." % BP,
   """
| Edge id | Test name |
|---|---|
| E1 window boundary | `allows_request_after_window_resets` |
| E2 missing key | `rejects_missing_key_with_401` |
| E3 clock skew | `tolerates_5s_skew` (the 5 s is an example value) |

Ask Claude to identify edge cases you missed: error conditions, boundary values and unexpected inputs [%s].""" % CW,
   ("Orphan edge case", "A spec edge case has no test, so a regression passes unnoticed.", "Keep a table of edge ids to test names and have the spec review fail on any empty cell."),
   "spec edge cases are Module 9.1.2.", "every listed case has a named test."),
  ("Mutation by hand: do tests fail when code breaks?",
   "Break the implementation deliberately and confirm the suite goes red. Automated mutation tools exist but this guide did not verify any specific tool, so use manual breaks.",
   """
| Break | Expected |
|---|---|
| Flip a comparison (`>` to `>=`) | At least one boundary test fails |
| Return a constant | Behaviour tests fail |
| Delete a branch | Its edge test fails |
| Skip the call to a dependency | An integration test fails |

```text
Introduce each of these four bugs one at a time on a scratch branch, run the suite after
each, and report which tests failed. Revert after each.
```""",
   ("Green-on-broken", "The suite stays green after you break the code, and nobody notices because it was never tried.", "Run the four breaks above on a scratch branch and fix every uncaught one before merging."),
   "adversarial review in fresh context is Module 9.13.3.", "tests earn trust by failing."),
 ],
 [("What is the most reliable evidence of test quality in this guide?", "A deliberately broken implementation makes the suite fail."),
  ("The test mocks the unit under test. Name the failure mode by its exact label.", "**Mock-the-subject.**"),
  ("A spec edge case has no test. Name the failure mode.", "**Orphan edge case.**"),
  ("The suite stays green after you flip a comparison. Name the failure mode by its exact label and fix.", "**Green-on-broken.** Run the four breaks on a scratch branch."),
  ("How many deliberate breaks does the guide's table list?", "Four."),
  ("What does the docs say Claude does when asked to write tests?", "Examines existing test files to match style, frameworks and assertion patterns."),
  ("Name three input categories the docs say to ask Claude to cover for edge cases.", "Error conditions, boundary values, unexpected inputs."),
  ("Did this guide verify a specific mutation-testing tool?", "No; it recommends manual breaks and says so."),
 ],
 ("A table of four deliberate breaks with the tests that failed, and an edge-id to test-name table with no empty cells.",
  [("List the spec's edge ids", "Table"), ("Map each to a test", "Table filled"), ("Break the code four ways on a scratch branch", "Run logs"), ("Record failing tests", "Table"), ("Fix any uncaught break", "New tests")]),
 """
| Break | Failing test |
|---|---|
| `>` to `>=` | allows_request_after_window_resets |
| Constant | 3 tests |
""", """
| Element | What is wrong |
|---|---|
| Every break leaves suite green | **Green-on-broken** |
| Mocks everywhere | **Mock-the-subject** |
""",
 "The artifact passes only if each of the four breaks fails at least one test, or a new test was added for it.",
 [("Anthropic", "Common workflows: Work with tests", "Edge case guidance", "Current"), ("Anthropic", "Best practices: Review against your spec", "Edge cases need tests", "Current")],
 "the docs do not discuss mocking or mutation testing; those sections are general engineering practice and unverified against vendor sources.",
 "This is the craft of test quality: **behaviour, listed cases, proof of failure.** The engineer who understands this does not ask \"is coverage high?\" — they ask \"what breaks this suite?\"", read=16, thin="mocking and mutation advice is general practice; the Claude Code docs only cover edge-case prompts"))

SPECS.append(G(M, "9.2.4", "Beyond unit tests",
 "Different failures need different checks: integration and contract tests for boundaries, snapshot and visual tests for output, load tests for capacity and accessibility checks for users, and each can be a pass-or-fail check Claude runs.",
 "choose the right check for five failure types and run one non-unit check end to end.",
 "match each risk to the cheapest check that can detect it.",
 "a unit suite can be fully green while the product is unusable, because units never exercise the seams.",
 [("Match risk to check",
   "The docs' list of checks is broad: a test file, a build exit code, a linter, a script that diffs output against a fixture, or a browser screenshot next to the mockup [%s]. The table maps common risks to those and to other test types." % BP,
   """
| Risk | Check | Runs as |
|---|---|---|
| Logic bug | Unit test | `pnpm vitest run file` |
| Two components disagree | Integration test | Test with real DB or fake |
| API shape drifts | Contract test (consumer expectations vs provider) | Pact-style tool (not verified here) |
| Output formatting changes | Snapshot test | Diff vs stored snapshot |
| Capacity | Load test | Tool of your choice (not verified here) |
| UI regression | Screenshot compared with design | Browser integration (Module 7.6) |
| Accessibility | Automated audit plus manual check | See Module 9.6.4 |""",
   ("One-check-fits-all", "The team has hundreds of unit tests and no integration test, so a broken wiring ships.", "For each module, name the cheapest check per risk and add the missing type."),
   "verifying UI is Module 9.6; browser integration is Module 7.6.", "different risks need different instruments."),
  ("Snapshot and visual tests need review discipline",
   "A snapshot test passes when output equals the stored snapshot, so updating the snapshot to make it pass erases the signal. Ask Claude to explain every snapshot diff before accepting it.",
   """
| Action | Rule |
|---|---|
| Snapshot fails | Read the diff; classify intended or regression |
| Intended | Update snapshot in its own commit with the reason |
| Regression | Fix the code, leave the snapshot |

```text
The snapshot test failed. Show the diff, say whether each hunk is intended per SPEC.md,
and do not update the snapshot until I agree.
```""",
   ("Blind snapshot update", "Claude runs the update flag and the test turns green with the regression baked in.", "Forbid snapshot updates in the prompt and review snapshot diffs as code."),
   "reviewing AI diffs is Module 9.12.3.", "a snapshot update is a code change."),
  ("Slow checks and when to run them",
   "Heavier checks should run where they cost little: in CI or on demand, not in every loop. The docs say hooks give deterministic control and warn to keep the enforced set small [%s]." % BP,
   """
| Check | Where |
|---|---|
| Unit, single file | Every iteration |
| Integration | Before commit, via Stop hook or CI |
| Load, long visual suites | CI or scheduled |

Stop hook example from the docs: `pnpm tsc --noEmit 1>&2 || exit 2`; exit 2 blocks the stop, and after eight blocked stops in a row with no tool call between them Claude Code overrides the next block [%s].""" % BP,
   ("Slow-loop stall", "A 20-minute suite runs in the Stop hook on every turn and the session crawls.", "Keep the Stop hook to fast checks and push heavy suites to CI."),
   "Stop hooks are Module 9.2.5; CI is Module 9.9.2.", "put each check where its cost is lowest."),
 ],
 [("Name three pass-or-fail checks the docs list besides a test file.", "A build's exit code, a linter, a script diffing output against a fixture, or a browser screenshot next to the mockup."),
  ("Hundreds of unit tests, no integration test. Name the failure mode by its exact label.", "**One-check-fits-all.**"),
  ("Claude updated the snapshot to turn green. Name the failure mode.", "**Blind snapshot update.**"),
  ("A 20-minute suite sits in the Stop hook. Name the failure mode by its exact label and fix.", "**Slow-loop stall.** Keep the hook fast; use CI for heavy suites."),
  ("After how many consecutive blocked stops does Claude Code override the next block?", "Eight."),
  ("What environment variable raises that cap?", "`CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`."),
  ("Did this guide verify a contract or load-testing tool?", "No; it says so in the table."),
  ("What exit code blocks a Stop?", "2."),
 ],
 ("A risk-to-check table for one service and the output of one non-unit check run end to end.",
  [("List five risks for a service", "Table"), ("Choose a check per risk", "Table"), ("Implement one non-unit check", "Test file"), ("Run it and capture output", "Output"), ("Decide where it runs", "Placement")]),
 """
| Risk | Check | Where |
|---|---|---|
| Wiring | Integration | pre-commit |
""", """
| Element | What is wrong |
|---|---|
| Unit only | **One-check-fits-all** |
| Heavy suite in Stop hook | **Slow-loop stall** |
""",
 "The artifact passes only if at least one non-unit check ran with captured output and every risk row names a check and a place.",
 [("Anthropic", "Best practices: Give Claude a check to run; Stop hook", "Check types, Stop hook cap", "Current")],
 "the docs do not name contract or load tools; this guide leaves tool choice open rather than invent a recommendation.",
 "This is the craft of broader checks: **risk-matched, reviewed, placed by cost.** The engineer who understands this does not ask \"are there tests?\" — they ask \"which failure would still get through?\"", read=16, thin="contract and load testing tools were not verified; only the docs' check list and Stop hook facts are sourced"))

SPECS.append(G(M, "9.2.5", "Verification skills and hooks",
 "Tests and type checks miss problems that appear only in the running app, so `/run` and `/verify` drive the real application, and a Stop hook turns a fast check into a gate that Claude Code, not Claude, enforces.",
 "run /verify on a change, record the recipe it writes, and add a Stop hook that blocks completion on a failing check.",
 "close the loop with a command the harness enforces, then add the running app as a second check.",
 "a passing test suite is evidence about code, not about the product, and the docs ship a separate skill for the second kind of evidence.",
 [("/run, /verify and /run-skill-generator",
   "Three bundled skills launch your app and confirm a change against the running app. `/run` launches and drives the app, `/verify` builds and runs it to confirm a change does what it should without falling back to tests or type checks, and `/run-skill-generator` teaches both how to build and launch your project [Claude Code docs, Skills, 2026].",
   """
| Skill | Does | Writes |
|---|---|---|
| `/run` | Launch and drive the app | Nothing by default |
| `/verify` | Build, run, observe the result | May record `.claude/skills/verify/SKILL.md` |
| `/run-skill-generator` | Capture install commands, env vars and launch script | `.claude/skills/run-<name>/` |

`/run` and `/verify` work without setup by inferring the launch from the project type and from README, `package.json` or `Makefile`; that is unreliable when a project needs a database, env file, graphical session or multi-step build. `/verify` runs only when you invoke it [Claude Code docs, Skills, 2026].""",
   ("Inferred launch", "You rely on /verify's inference for an app needing a database and env file, and it verifies a broken or empty app.", "Run `/run-skill-generator` once per project, commit the generated skill, and rerun it when the build changes."),
   "skills are Module 5.2; real-app verification in UI work is Module 9.6.3.", "teach the launch once, commit it."),
  ("The recorded recipe",
   "When `/verify` has to build and drive the app without a recipe, it can record one. At the repo root the recorded skill replaces the bundled `/verify`; Claude edits the file only when it steered a run wrong, so it can be committed without per-session diffs [Claude Code docs, Skills, 2026].",
   """
| Fact | Detail |
|---|---|
| Path | `.claude/skills/verify/SKILL.md` at repo root; touched package dir in a monorepo |
| Effect at root | Replaces the bundled `/verify` |
| Edit rule | Only when a run was steered wrong |
| Commit it? | Yes; no per-session diffs expected |""",
   ("Shadowed bundled skill", "A recorded verify skill at the repo root silently replaces the bundled one and nobody reviews it.", "Review the recorded file in a PR like any code and keep it current."),
   "plugins and shared skills are Module 9.12.7.", "a recorded recipe is code under review."),
  ("Stop hooks as gates",
   "A Stop hook runs your script whenever Claude tries to end its turn, and sends Claude back to work if it exits with code 2, so the turn does not end until the check passes or the block limit is reached [%s]." % BP,
   """
```json
{
  "hooks": {
    "Stop": [
      { "hooks": [ { "type": "command", "command": "pnpm tsc --noEmit 1>&2 || exit 2" } ] }
    ]
  }
}
```

| Fact | Detail |
|---|---|
| Block signal | Exit code 2; stderr goes back to Claude |
| Cap | Override after eight blocked stops in a row with no tool call between |
| Env var to raise | `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` |
| Alternative | `/goal <condition>`, checked by a separate model each turn |""",
   ("Exit-1 gate", "The Stop hook exits 1 on failure; only exit 2 blocks, so Claude finishes with a failing check.", "End the command with `|| exit 2` and test it by breaking a type on purpose."),
   "hooks are Module 5.4; goals are Module 6.7.", "gates need exit 2."),
 ],
 [("What does /verify do that tests and type checks do not?", "Builds and runs the app and observes the result."),
  ("Where does /run-skill-generator write its skill?", "`.claude/skills/run-<name>/`."),
  ("You relied on inference for an app needing a database. Name the failure mode by its exact label.", "**Inferred launch.**"),
  ("A recorded verify skill replaced the bundled one unreviewed. Name the failure mode.", "**Shadowed bundled skill.**"),
  ("Your Stop hook exits 1 and Claude finishes anyway. Name the failure mode by its exact label and fix.", "**Exit-1 gate.** End with `|| exit 2`."),
  ("After how many consecutive blocked stops does Claude Code override a block?", "Eight."),
  ("Which exit code blocks in a Stop hook?", "2."),
  ("Does Claude invoke /verify automatically?", "No; it runs only when you invoke it."),
  ("When does Claude edit the recorded verify file?", "Only when it steered a run wrong."),
 ],
 ("A recorded verify recipe committed to the repo plus a Stop hook transcript where a deliberately broken type blocked completion.",
  [("Run /run-skill-generator once", "run skill"), ("Run /verify on a change", "Output"), ("Add the Stop hook", "settings.json"), ("Break a type on purpose", "Blocked stop"), ("Fix and finish", "Clean stop")]),
 """
| Check | Evidence |
|---|---|
| Hook blocked | stderr shows compiler error |
| Verify output | screenshot or response captured |
""", """
| Element | What is wrong |
|---|---|
| `or exit 1` ending | **Exit-1 gate** |
| No generated skill | **Inferred launch** |
""",
 "The artifact passes only if the broken type blocked the stop and /verify output shows the running app, not just test results.",
 [("Anthropic", "Skills: Run and verify your app", "/run, /verify, /run-skill-generator", "Current"), ("Anthropic", "Best practices: Enforce the check with a Stop hook", "Exit 2, cap of eight", "Current")],
 "the docs offer `/goal` and Stop hooks as alternatives for gating completion; goals are model-judged while Stop hooks are deterministic, so pick by whether the check needs judgement.",
 "This is the craft of verification skills and hooks: **a running-app check plus a harness-enforced gate.** The engineer who understands this does not ask \"did the tests pass?\" — they ask \"did the app work, and could the turn have ended if it hadn't?\"", read=17))

SPECS.append(G(M, "9.2.6", "Flaky tests and slow suites",
 "Flaky and slow tests are diagnosed by isolating and reproducing them first, and managed by running single tests during development, so Claude fixes the cause instead of adding retries.",
 "isolate one flaky test, reproduce the flake, fix the cause and show repeated passes.",
 "reproduce the flake before changing anything.",
 "retrying a flaky test hides a real race condition, and retries are what an agent will add if you ask it to 'make it pass'.",
 [("Isolate and reproduce",
   "The docs' bug advice is to tell Claude the command that reproduces the issue and to say whether the error is intermittent or consistent [%s]. For flaky tests, raising effort helps: the docs list 'a flaky test' among cases where getting it right depends on cases that are quick to overlook, and suggest `/effort high` or `xhigh` [%s]." % (CW, BP),
   """
| Step | Command or prompt |
|---|---|
| Run alone | `pnpm vitest run path/to/flaky.test.ts` (sample command from the docs) |
| Repeat | Loop it 20 times in a shell (the 20 is an example) |
| Randomise order | Use your runner's shuffle option (runner-specific, not verified) |
| Raise effort | `/effort high` |

```text
This test fails about 1 in 10 runs. Run it 30 times alone, record failures, then 30 times
with the whole file, and tell me which condition produces the flake before you change code.
```""",
   ("Retry patch", "Claude adds a retry or a sleep and the flake becomes rarer, not gone.", "Prohibit retries and sleeps in the prompt; require a root cause statement and a failing reproduction."),
   "root-cause discipline is Module 9.3.5; reasoning effort is Module 4.6.", "reproduce, then fix the cause."),
  ("Common causes and fixes",
   "Most flakes come from shared state, time, ordering, concurrency or the network. This table is general practice, not from the Claude Code docs.",
   """
| Cause | Symptom | Fix |
|---|---|---|
| Shared state | Passes alone, fails in suite | Isolate fixtures; reset per test |
| Real clock | Fails near boundaries | Inject a fake clock |
| Async race | Fails under load | Await the condition, not a delay |
| Test order | Fails when shuffled | Remove inter-test dependencies |
| Network | Fails in CI | Fake the boundary |""",
   ("Sleep-for-sync", "A fixed sleep waits for an async result and fails on slow machines.", "Wait on the event or condition with a bounded timeout instead."),
   "test quality is Module 9.2.3.", "match the fix to the cause."),
  ("Slow suites: run the narrowest check",
   "During development run single tests and keep the full suite for the gate. The docs' CLAUDE.md sample lists how to run one test file, and `/usage` shows where time and tokens went [%s]." % BP,
   """
| Loop | What runs |
|---|---|
| Inner (seconds) | One test file |
| Middle (per step) | Changed module's tests |
| Outer (gate) | Full suite in Stop hook or CI |

Ask Claude to profile the suite (slowest tests) and propose fixes, then verify the total time before and after.""",
   ("Full-suite inner loop", "Every edit runs the entire suite, so a 10-minute run is paid dozens of times.", "Put the single-test command in CLAUDE.md and the full suite in the gate only."),
   "CI is Module 9.9.2.", "the inner loop should take seconds."),
 ],
 [("What do the docs say to tell Claude about a bug's reproduction?", "The command to reproduce it, and whether it is intermittent or consistent."),
  ("Claude added a retry to a flaky test. Name the failure mode by its exact label.", "**Retry patch.**"),
  ("A fixed sleep waits for async. Name the failure mode.", "**Sleep-for-sync.**"),
  ("Every edit runs the whole suite. Name the failure mode by its exact label and fix.", "**Full-suite inner loop.** Put single-test commands in CLAUDE.md."),
  ("Which effort levels does the docs suggest raising to for flaky tests?", "`high` or `xhigh`."),
  ("In the example prompt, how many runs alone and with the whole file?", "30 each."),
  ("Which command shows where usage went?", "`/usage`."),
  ("Are the shuffle-option details verified in this guide?", "No; they are runner-specific and flagged unverified."),
 ],
 ("A reproduction log for one flaky test, a root-cause note and 30 consecutive green runs after the fix.",
  [("Pick a flaky test", "Name"), ("Run alone 30 times", "Log"), ("Run with file 30 times", "Log"), ("State the cause", "Note"), ("Fix without retries", "Diff"), ("Rerun 30 times", "Green log")]),
 """
| Check | Evidence |
|---|---|
| Reproduction | 3 failures of 30 |
| Fix | no retry or sleep in diff |
| Rerun | 30 of 30 |
""", """
| Element | What is wrong |
|---|---|
| `retry(3)` added | **Retry patch** |
| `sleep(2000)` | **Sleep-for-sync** |
""",
 "The artifact passes only if the flake was reproduced before the fix and the fix diff contains no retry or sleep.",
 [("Anthropic", "Common workflows: Fix bugs efficiently", "Reproduce, intermittent or consistent", "Current"), ("Anthropic", "Best practices: Change the model and effort", "Effort for flaky tests", "Current")],
 "the cause table is general practice rather than vendor documentation.",
 "This is the craft of flaky and slow tests: **reproduce, root-cause, narrow the loop.** The engineer who understands this does not ask \"how do I make it pass?\" — they ask \"under what condition does it fail?\"", read=15, thin="cause table is general engineering practice; only the reproduce and effort advice is from the docs"))

if __name__ == "__main__":
    for s in SPECS:
        write(s)
