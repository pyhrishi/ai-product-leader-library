import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from specs_b9_lib import G, write

M = "b-9-3"
BP = "Claude Code docs, Best practices, 2026"
CW = "Claude Code docs, Common workflows, 2026"
MCP = "Claude Code docs, MCP, 2026"
SPECS = []

SPECS.append(G(M, "9.3.1", "Reproduce first",
 "A bug fix without a failing reproduction is a guess; a failing test or script before any fix gives Claude a pass-or-fail check and gives you proof the fix addressed the reported problem.",
 "turn a bug report into a failing test or script, show it fails, then show the fix turns it green.",
 "no fix is attempted until the reproduction fails on demand.",
 "the reproduction is worth more than the fix, because it keeps protecting you after the incident ends.",
 [("From report to reproduction",
   "The docs' contrast is between 'fix the login bug' and a prompt that names the symptom, the code location and asks Claude to write a failing test that reproduces it, then fix it [%s]. Tell Claude the command to reproduce and whether the error is intermittent or consistent [%s]." % (BP, CW),
   """
| Report element | Becomes |
|---|---|
| "Login fails after the session times out" | Test name: `refreshes_token_after_session_timeout` |
| Where | `src/auth/` token refresh |
| Frequency | Consistent or intermittent (say which) |
| Done | The test passes and the neighbouring suite stays green |

```text
users report login fails after the session times out. look at token refresh in src/auth/,
write a failing test that reproduces it, then fix it
```""",
   ("Fix-first guess", "Claude edits code from the description alone, the symptom changes and nobody knows whether the cause was found.", "Require a failing reproduction and its output before the first edit."),
   "prompting craft is Module 2.2; TDD is Module 9.2.1.", "red before any green."),
  ("When a test is the wrong reproduction",
   "Some bugs need a script, a curl sequence or a data fixture rather than a unit test. The reproduction is whatever returns pass or fail reliably; the docs list scripts that diff output against a fixture as valid checks [%s]." % BP,
   """
| Bug type | Reproduction form |
|---|---|
| Logic error | Unit test |
| Wrong HTTP result | curl script with expected status |
| Data-dependent | Fixture file plus test |
| UI | Screenshot compared with expected |
| Intermittent | Loop script with failure count |""",
   ("Unreproducible fix", "You cannot reproduce, so Claude 'fixes' a plausible cause and the report stays open.", "Mark the bug as not reproduced, gather more evidence (Module 9.3.2) and add logging instead of changing logic."),
   "evidence is Module 9.3.2.", "no reproduction, no fix claim."),
  ("Keep the reproduction",
   "After the fix, the test stays in the suite as a regression guard. The docs advise asking for evidence of the passing check [%s]." % BP,
   """
| After the fix | Do |
|---|---|
| Test name | Describes the behaviour, not the ticket number alone |
| Commit | Test and fix together, message cites the report |
| Evidence | Failing output before, passing output after |""",
   ("Throwaway reproduction", "The scratch script is deleted after the fix and the bug returns in a month.", "Convert it into a permanent test before closing the ticket."),
   "root cause is Module 9.3.5.", "a reproduction becomes a regression test."),
 ],
 [("What does the docs' bug prompt ask Claude to write before fixing?", "A failing test that reproduces the problem."),
  ("Claude edits from a description alone. Name the failure mode by its exact label.", "**Fix-first guess.**"),
  ("You could not reproduce but Claude patched a plausible cause. Name the failure mode.", "**Unreproducible fix.**"),
  ("The scratch script was deleted and the bug came back. Name the failure mode by its exact label and fix.", "**Throwaway reproduction.** Convert it to a permanent test."),
  ("What two things should you tell Claude about the failure?", "The command to reproduce it and whether it is intermittent or consistent."),
  ("Name three reproduction forms from the table.", "Unit test, curl script, fixture plus test, screenshot, loop script."),
  ("What evidence pair should you capture?", "Failing output before and passing output after."),
  ("Should the test name cite only a ticket number?", "No; it should describe the behaviour."),
 ],
 ("A bug report, its failing reproduction, the fix and the green rerun, with before and after outputs.",
  [("Write the report as a prompt", "Prompt"), ("Get a failing reproduction", "Red output"), ("Fix", "Diff"), ("Rerun", "Green output"), ("Keep the test", "Commit")]),
 """
| Item | Evidence |
|---|---|
| Red output | assertion on token refresh |
| Green output | same test passes |
""", """
| Element | What is wrong |
|---|---|
| Edit before red | **Fix-first guess** |
| Script deleted | **Throwaway reproduction** |
""",
 "The artifact passes only if the failing output predates the first source edit in the transcript.",
 [("Anthropic", "Best practices: Write a specific prompt", "Failing-test-first prompt", "Current"), ("Anthropic", "Common workflows: Fix bugs efficiently", "Reproduce command and frequency", "Current")],
 "none found between the sources read.",
 "This is the craft of reproduction: **make it fail on demand, then fix, then keep the test.** The engineer who understands this does not ask \"what is the fix?\" — they ask \"what proves the bug exists, and will prove it is gone?\"", read=14, prove_h="1.5"))

SPECS.append(G(M, "9.3.2", "Give Claude the evidence",
 "Debugging quality tracks evidence quality: paste errors, pipe logs in, attach screenshots, connect dashboards through MCP, and give git history for regressions, so Claude reasons from facts instead of guessing.",
 "assemble an evidence pack for one bug using four of the five channels and show what each added.",
 "hand over the raw artifact instead of describing it.",
 "describing an error in words discards the information that identifies the cause.",
 [("Five evidence channels",
   "The docs' guidance is to hand Claude the thing you have rather than describe it: `@` a file, paste an image, or pipe command output from your shell [%s]." % BP,
   """
| Channel | How | Source |
|---|---|---|
| Pasted error | Paste stack trace | [%s] |
| Piped logs | `cat error.log \\| claude -p "what's going on here"` | [%s] |
| Screenshot | Drag, paste with `Ctrl+V`, or give a path | [%s] |
| Dashboards | MCP server, for example Sentry | [%s] |
| Git history | `git log`, `git diff`; ask for the change that introduced the bug | general git use |""" % (CW, BP, CW, MCP),
   ("Paraphrased error", "You summarise the error as 'it crashes on login' and Claude proposes a generic fix.", "Paste the exact message and stack trace; attach the log slice around the time of the failure."),
   "MCP is Module 5.5; images in prompts are Module 2.2.", "raw artifacts beat summaries."),
  ("Piping and size limits",
   "Piped stdin is capped at 10MB; larger inputs should be written to a file and referenced by path [Claude Code docs, Headless, 2026]. An `@` file reference includes contents when they fit the Read tool's token limit, 25,000 tokens by default, and a text file over 256KB is not included [%s]." % CW,
   """
| Input size | Move |
|---|---|
| Small error | Paste |
| Log slice | `tail -n 500 app.log \\| claude -p "..."` |
| Over 10MB | Save to file, reference path |
| `@file` over 25,000 tokens | Narrow with grep or a slice first |

Slice before sending: filter to the time window and the request id.""",
   ("Log flood", "You pipe an entire day's log and the relevant lines are drowned or truncated.", "Filter to the request id and time window, then attach the slice."),
   "context cost is Module 3.1.", "send the right 500 lines, not 5 million."),
  ("Evidence from tools and secrets hygiene",
   "Connected servers add their tool names and instructions to the context even when unused, and servers that fetch external content can expose you to prompt injection, so trust matters [%s; %s]. Redact secrets and personal data from evidence before pasting." % (BP, MCP),
   """
| Evidence type | Handling |
|---|---|
| Stack trace | Strip tokens and URLs with credentials |
| Logs with user data | Mask personal fields |
| Screenshot | Check for visible secrets |
| MCP dashboards | Read-only access (Module 9.3.4) |""",
   ("Leaky evidence", "You paste a log containing tokens or customer data into the session.", "Redact first, and keep deny rules for secret files (`Read(./.env)`) as the docs show."),
   "permissions are Module 4.2.", "evidence is data you are responsible for."),
 ],
 [("Name the five evidence channels in the guide.", "Pasted errors, piped logs, screenshots, dashboards through MCP, git history."),
  ("You wrote 'it crashes on login' instead of the trace. Name the failure mode by its exact label.", "**Paraphrased error.**"),
  ("You piped a full day's log. Name the failure mode.", "**Log flood.**"),
  ("You pasted a log with tokens. Name the failure mode by its exact label and fix.", "**Leaky evidence.** Redact first."),
  ("What is the cap on piped stdin?", "10MB."),
  ("Above what size is an `@` text file not included?", "256KB."),
  ("What is the default token limit for an @-referenced file's contents?", "25,000 tokens."),
  ("Which key combination pastes an image into the CLI?", "`Ctrl+V` (`Alt+V` on Windows and WSL)."),
 ],
 ("An evidence pack for one bug: four channels, a note on what each contributed and a redaction log.",
  [("Collect error, log slice, screenshot, history", "Pack"), ("Redact", "Redaction log"), ("Prompt with the pack", "Prompt"), ("Record what each channel changed", "Notes")]),
 """
| Channel | Contribution |
|---|---|
| Log slice | request id found |
| History | commit that changed refresh |
""", """
| Element | What is wrong |
|---|---|
| Summary only | **Paraphrased error** |
| Unredacted tokens | **Leaky evidence** |
""",
 "The artifact passes only if at least four channels are present, each with a recorded contribution, and the redaction log is non-empty or states nothing needed redacting.",
 [("Anthropic", "Common workflows: Work with images; Reference files", "Image paste, @ limits", "Current"), ("Anthropic", "Headless", "Piped stdin cap", "Current"), ("Anthropic", "MCP", "Example integrations, trust warning", "Current")],
 "none found between the sources read.",
 "This is the craft of evidence: **raw, sliced, redacted, from several channels.** The engineer who understands this does not ask \"how do I describe the bug?\" — they ask \"what artifact would let a stranger see it?\"", read=14, prove_h="1.5"))

SPECS.append(G(M, "9.3.3", "Bisecting and blame",
 "For a regression, ask Claude to find the commit that introduced it by running `git bisect` with your reproduction as the oracle, or to explain when a behaviour changed from history and blame.",
 "bisect a seeded regression to its commit using an automated test as the oracle.",
 "give bisect a command that exits 0 for good and non-zero for bad.",
 "bisect only works if the reproduction is reliable, so flaky tests turn it into a coin flip.",
 [("Bisect with a test as oracle",
   "`git bisect run <command>` automates the search: the command exits 0 for good, 1 to 127 except 125 for bad, and 125 to skip [secondary: git documentation, git-bisect, not fetched for this guide]. Claude Code runs shell commands through its Bash tool and can drive the sequence [Claude Code docs, Tools reference, 2026].",
   """
```bash
git bisect start
git bisect bad HEAD
git bisect good v2.3.0
git bisect run pnpm vitest run path/to/regression.test.ts
git bisect reset
```

| Input | Meaning |
|---|---|
| good commit | Known-working revision |
| bad commit | Known-failing revision |
| run command | Oracle; exit 0 good, non-zero bad, 125 skip |""",
   ("Flaky oracle", "The reproduction passes and fails at random, so bisect lands on an unrelated commit.", "Stabilise the reproduction (Module 9.2.6) or run it several times per step before trusting a verdict."),
   "reproduction is Module 9.3.1.", "bisect is only as good as its oracle."),
  ("Blame and history questions",
   "When a bisect is unnecessary, ask Claude to explain when and why a line changed, using git log and blame. Piping command output is a documented pattern, for example `git log --oneline -20 | claude -p \"summarize these recent commits\"` [%s]." % "Claude Code docs, Common workflows, 2026",
   """
| Question | Prompt |
|---|---|
| Who changed this and why | "Use git blame on lines 40-60 of limiter.ts and the commit messages; explain intent" |
| What changed between releases | "Summarise `git log v2.3.0..HEAD` for changes touching auth" |
| Did this ever work | "Find the earliest commit where this test passes" |""",
   ("Blame as verdict", "You treat the last editor of a line as the cause, though the real change was elsewhere.", "Use blame for questions and bisect for evidence; the committer of a line is not necessarily the origin of the regression."),
   "legacy investigations are Module 9.5.2.", "blame points; bisect proves."),
  ("Run it safely",
   "Bisect checks out many revisions, so run it where a dirty tree cannot be lost. `claude --worktree <name>` creates an isolated checkout on its own branch [Claude Code docs, Worktrees, 2026].",
   """
| Safety step | Why |
|---|---|
| Clean tree before starting | Bisect checks out revisions |
| Work in a worktree | Main checkout untouched |
| `git bisect reset` after | Return to the original branch |
| Dependencies per revision | Install step may be needed in the oracle |""",
   ("Dirty-tree bisect", "You bisect with uncommitted work in the tree and lose or conflict with it.", "Commit or stash first, or bisect in a worktree."),
   "worktrees are Module 6.2.", "isolate the search."),
 ],
 [("What exit code does `git bisect run` treat as skip?", "125."),
  ("Which exit code means good?", "0."),
  ("The reproduction flakes and bisect lands on an unrelated commit. Name the failure mode by its exact label.", "**Flaky oracle.**"),
  ("You blamed the last editor of a line. Name the failure mode.", "**Blame as verdict.**"),
  ("You bisected with uncommitted changes. Name the failure mode by its exact label and fix.", "**Dirty-tree bisect.** Stash, or use a worktree."),
  ("Which command ends a bisect and restores the original branch?", "`git bisect reset`."),
  ("Is the git-bisect exit-code detail from the Claude Code docs?", "No; it is from git documentation, flagged secondary and not fetched here."),
  ("What flag creates an isolated checkout?", "`--worktree` (`-w`)."),
 ],
 ("A bisect log on a seeded regression ending at the culprit commit, with the oracle command shown.",
  [("Seed a regression", "Commit"), ("Write the oracle test", "Test"), ("Start bisect in a worktree", "Log"), ("Run `git bisect run`", "Culprit commit"), ("Reset", "Clean state")]),
 """
| Item | Evidence |
|---|---|
| Culprit | commit hash matches seeded one |
| Oracle runs | 5 steps for 32 commits |
""", """
| Element | What is wrong |
|---|---|
| Flaky test as oracle | **Flaky oracle** |
| Culprit by blame only | **Blame as verdict** |
""",
 "The artifact passes only if bisect identifies the seeded commit and the oracle exit codes are shown.",
 [("Git project", "git-bisect manual", "run and exit codes [secondary: not fetched here]", "Verify locally with `git help bisect`"), ("Anthropic", "Worktrees", "Isolated checkouts", "Current")],
 "none found; the git exit-code detail is flagged as unverified here and should be checked with `git help bisect`.",
 "This is the craft of bisecting: **a reliable oracle, an isolated tree, proof over blame.** The engineer who understands this does not ask \"who broke it?\" — they ask \"which commit flips the oracle?\"", read=13, prove_h="1.5", thin="bisect specifics come from git documentation not fetched in this session; verify with git help bisect"))

SPECS.append(G(M, "9.3.4", "Observability access",
 "Claude can read error trackers and monitoring data through MCP servers or command-line tools, and the right default is read-only credentials scoped to what the investigation needs.",
 "connect one observability source read-only, answer a real question from it and show that a write attempt fails.",
 "start with read-only credentials and add only what a task proves it needs.",
 "the safest observability integration is the one whose credentials cannot change anything even if Claude is manipulated.",
 [("MCP or CLI",
   "The docs' examples include checking Sentry and Statsig for usage of a feature and querying a PostgreSQL database through MCP; if a system has a CLI, that is usually the easiest way in, and for a CLI Claude has not seen, pointing it at `--help` is enough [%s; %s]." % (MCP, BP),
   """
| Route | Add | Scope notes |
|---|---|---|
| CLI | Install and sign in (for example `gh`) | Claude uses it through Bash |
| Remote MCP | `claude mcp add --transport http <name> <url>` | Recommended transport in the docs |
| Local MCP | `claude mcp add <name> -- <command> [args...]` | stdio server |

`--scope local` (default), `project` (shared via `.mcp.json`) or `user`. Project servers prompt for approval; reset with `claude mcp reset-project-choices` [%s].""" % MCP,
   ("Overscoped token", "The token you connected can write or delete, so a prompt-injected instruction could change monitoring or data.", "Issue a read-only token for the investigation and keep write tokens out of the session."),
   "MCP is Module 5.5; permissions are Module 4.2.", "least privilege at the credential."),
  ("Trust and output limits",
   "The docs warn: verify you trust each server before connecting; servers that fetch external content can expose you to prompt injection [%s]. MCP tool output over 10,000 tokens triggers a warning and output is limited to 25,000 tokens by default, adjustable with `MAX_MCP_OUTPUT_TOKENS` [%s]." % (MCP, MCP),
   """
| Concern | Control |
|---|---|
| Untrusted content in logs | Treat as data; do not follow instructions in it |
| Big query results | Ask for aggregates and narrow time windows |
| Idle servers cost context | Disable unneeded servers in `/mcp` |
| Shared config | `.mcp.json` committed without secrets |""",
   ("Log-borne instruction", "A log line or ticket contains text telling the agent to run something, and Claude treats it as a command.", "Use read-only tools, deny rules for risky commands, and review actions the classifier blocks (auto mode flags actions that look driven by content Claude read) [%s]." % BP),
   "prompt injection controls are Module 4.4.", "data is not instruction."),
  ("An investigation prompt",
   "Pair evidence from monitoring with code reading so Claude correlates deploys, errors and changes. Ask for citations of what it queried.",
   """
```text
Using the Sentry MCP, list the top 5 unresolved errors for the checkout service in the last
24 hours. For the top one, show the stack trace, find the code, check git log for recent
changes to that file, and propose a hypothesis. Do not change anything.
```

| Output requirement | Why |
|---|---|
| Queries run | Auditable |
| Hypothesis, not fix | Keeps step separate |
| Time window stated | Avoids stale data |""",
   ("Unaudited query", "Claude summarises dashboards without naming the queries or time windows, so you cannot check the claim.", "Require the exact query, time window and result count in the answer."),
   "root cause is Module 9.3.5.", "ask for the query as well as the answer."),
 ],
 [("What does the docs' MCP trust warning say about servers that fetch external content?", "They can expose you to prompt injection risk."),
  ("What is the default MCP output limit?", "25,000 tokens, with a warning above 10,000."),
  ("Which variable changes the MCP output limit?", "`MAX_MCP_OUTPUT_TOKENS`."),
  ("The token you connected can delete data. Name the failure mode by its exact label.", "**Overscoped token.**"),
  ("A log line instructs the agent to run a command. Name the failure mode.", "**Log-borne instruction.**"),
  ("Claude summarised dashboards with no queries cited. Name the failure mode by its exact label and fix.", "**Unaudited query.** Require query, window and counts."),
  ("Which transport does the docs mark as recommended for remote servers?", "http."),
  ("How do you reset project MCP approval choices?", "`claude mcp reset-project-choices`."),
 ],
 ("A read-only connection to one source, a transcript answering a question from it and a failing write attempt.",
  [("Create a read-only token", "Token scope note"), ("Add the server or CLI", "Config"), ("Run the investigation prompt", "Transcript"), ("Try a write", "Failure"), ("Record queries", "Audit list")]),
 """
| Check | Evidence |
|---|---|
| Write attempt | 403 from the service |
| Queries | 3 listed with windows |
""", """
| Element | What is wrong |
|---|---|
| Admin token | **Overscoped token** |
| No query list | **Unaudited query** |
""",
 "The artifact passes only if a write attempt fails at the service and every claim cites a query with a time window.",
 [("Anthropic", "MCP", "Add syntax, scopes, trust warning, limits", "Current"), ("Anthropic", "Best practices: Connect the tools Claude needs", "CLI versus MCP", "Current")],
 "none found between the sources read; vendor-specific read-only token setup was not fetched.",
 "This is the craft of observability access: **least privilege, bounded output, auditable queries.** The engineer who understands this does not ask \"can Claude see prod?\" — they ask \"what can this credential change if everything goes wrong?\"", read=15))

SPECS.append(G(M, "9.3.5", "Root cause discipline",
 "Ask Claude for the cause, not a suppression, and require an explanation and a regression test, because the cheapest-looking fix to an error is often to hide it.",
 "show a diff where the fix addresses the cause, with an explanation, a regression test and no suppression.",
 "no fix merges without a stated cause and a test that fails without it.",
 "an error that disappears is not a bug that is fixed; suppression looks identical to success until the next incident.",
 [("Cause versus suppression",
   "The docs' bug example compares a vague prompt with one that names the symptom and asks for a reproduction and fix; it also suggests asking Claude for a few ways to fix a `@ts-ignore` [%s]. A `@ts-ignore` is itself a suppression." % CW,
   """
| Suppression | Cause fix |
|---|---|
| `try/catch` that swallows | Handle or prevent the error condition |
| `@ts-ignore` | Correct the type |
| Retry or sleep | Fix the race (Module 9.2.6) |
| Default value hiding null | Make the null impossible or handled explicitly |
| Disable the failing test | Fix the code |""",
   ("Symptom suppression", "The error stops appearing because it is caught and ignored, and the underlying fault persists.", "Prompt: 'explain the root cause before changing anything; do not catch-and-ignore, skip tests or add ts-ignore'."),
   "TDD is Module 9.2.1.", "ask why before how."),
  ("The explanation requirement",
   "Require a short causal chain: trigger, mechanism, why it escaped earlier checks. The docs advise asking for evidence rather than bare claims [%s]." % BP,
   """
| Field | Example |
|---|---|
| Trigger | Session expires between request and refresh |
| Mechanism | Refresh uses stale token after rotation |
| Escape | No test covered timeout during rotation |
| Fix | Rotate-then-refresh ordering |
| Guard | Test `refreshes_after_timeout` |""",
   ("Plausible story", "The explanation is fluent but not tied to evidence, and the fix is not the cause.", "Ask which log line, line of code or test output supports each step and verify one by experiment."),
   "evidence is Module 9.3.2.", "each causal step cites evidence."),
  ("Regression test and the five-whys limit",
   "A regression test fails before the fix and passes after. Asking 'why' repeatedly finds the process cause too, but stop when the next answer is outside your control.",
   """
| Question | Output |
|---|---|
| Why did it fail? | Mechanism |
| Why was it not caught? | Missing test or check |
| What prevents recurrence? | Test, hook or CLAUDE.md line (Module 9.12.9) |

Confirm with: revert the fix, rerun the test, see red.""",
   ("Unverified regression test", "The new test passes with or without the fix.", "Revert the fix on a scratch branch and confirm the test fails."),
   "learning loop is Module 9.12.9.", "prove the guard guards."),
 ],
 [("Name three suppressions from the table.", "Swallowing try/catch, `@ts-ignore`, retry or sleep, default value hiding null, disabling the test."),
  ("The error is caught and ignored. Name the failure mode by its exact label.", "**Symptom suppression.**"),
  ("A fluent explanation had no evidence behind it. Name the failure mode.", "**Plausible story.**"),
  ("The new test passes with or without the fix. Name the failure mode by its exact label and fix.", "**Unverified regression test.** Revert the fix and see red."),
  ("What three fields form the minimal causal chain?", "Trigger, mechanism, why it escaped earlier checks."),
  ("What did the docs suggest asking Claude about a `@ts-ignore`?", "To suggest a few ways to fix it."),
  ("What should you ask Claude to supply instead of 'all tests pass'?", "Evidence: command and output."),
  ("Where might a recurrence guard live besides a test?", "A hook or a CLAUDE.md line."),
 ],
 ("A fix diff with a cause note and a regression test proven red without the fix.",
  [("Ask for cause before change", "Cause note"), ("Cite evidence for each step", "Evidence list"), ("Write the test", "Test"), ("Fix", "Diff"), ("Revert and see red", "Red output")]),
 """
| Item | Evidence |
|---|---|
| Cause note | 3 fields with evidence |
| Test | red without fix |
""", """
| Element | What is wrong |
|---|---|
| Added catch-all | **Symptom suppression** |
| Test never red | **Unverified regression test** |
""",
 "The artifact passes only if the diff contains no suppression and the test was shown red with the fix reverted.",
 [("Anthropic", "Common workflows: Fix bugs efficiently", "Prompt pattern for fix suggestions", "Current"), ("Anthropic", "Best practices", "Evidence request", "Current")],
 "none found between the sources read; the causal-chain template is this guide's own.",
 "This is the craft of root cause: **cause first, evidence per step, a guard that bites.** The engineer who understands this does not ask \"did the error stop?\" — they ask \"what was true that should not have been, and what prevents it now?\"", read=14, prove_h="1.5"))

SPECS.append(G(M, "9.3.6", "Runbooks as skills",
 "A runbook saved as a skill gives Claude your on-call procedure on demand, and `disable-model-invocation: true` keeps side-effecting steps behind a human typing the command.",
 "write one runbook skill with a safe read-only diagnosis and a gated action and show both invocation modes.",
 "diagnosis can be automatic; actions with side effects are manual.",
 "a runbook in a wiki is read by humans under stress; the same runbook as a skill is executed consistently and costs almost no context until it is needed.",
 [("What a skill is",
   "A skill is a procedure or piece of team knowledge saved at `.claude/skills/<name>/SKILL.md`. For a skill Claude can start on its own, Claude sees the name and description in every session and reads the full file only when the task calls for it; so a long procedure does not weigh on unrelated work like a CLAUDE.md entry would [%s]." % BP,
   """
| Frontmatter field | Use for runbooks |
|---|---|
| `name` | Command name, e.g. `db-failover` |
| `description` | When to use; put key use case first (combined `description` and `when_to_use` truncated at 1,536 characters) |
| `disable-model-invocation: true` | Claude cannot start it; you type `/name` |
| `allowed-tools` | Tools usable without asking during the turn |
| `context: fork` | Run in a forked subagent |
| `paths` | Limit automatic activation to matching files |

Keep `SKILL.md` under 500 lines; move reference material into separate files [Claude Code docs, Skills, 2026].""",
   ("Description overflow", "The key trigger sits past character 1,536 of description and when_to_use, so Claude never matches the skill to an incident.", "Put the key use case first and keep the combined text short."),
   "skills are Module 5.2.", "front-load the trigger."),
  ("Split diagnosis from action",
   "The docs' release example uses `disable-model-invocation: true` for a workflow with side effects, so it runs only when you type `/release` [%s]. Apply that to remediation steps." % BP,
   """
```markdown
---
name: api-5xx-diagnose
description: Diagnose a spike in API 5xx errors. Read-only: queries logs and dashboards, never changes anything.
allowed-tools: Read, Grep
---
1. Ask for the time window.
2. Query error rate and top error classes through the monitoring MCP.
3. Map the top class to code; check git log for recent changes.
4. Report hypothesis and evidence. Stop.
```

```markdown
---
name: api-rollback
description: Roll back the API to the previous release.
disable-model-invocation: true
---
1. Confirm the target version with the user.
2. ... (steps) ...
```""",
   ("Auto-fired remediation", "The rollback skill can be started by Claude, so a hallucinated diagnosis triggers a production change.", "Set `disable-model-invocation: true` on every skill with side effects."),
   "production safety is Module 9.3.7.", "automatic diagnosis, manual action."),
  ("Lifecycle and maintenance",
   "Invoked skill content enters the conversation as one message and stays across later turns; `allowed-tools` grants clear on your next message; after auto-compaction the most recent invocation of each skill is re-attached, first 5,000 tokens each, within a combined 25,000-token budget [Claude Code docs, Skills, 2026].",
   """
| Fact | Implication |
|---|---|
| Content stays in context | Do not invoke needlessly mid-session |
| allowed-tools grant clears | Re-invoke or approve again next turn |
| 5,000 tokens kept per skill after compaction | Put critical steps first |
| 25,000-token shared budget | Older skills may drop |""",
   ("Stale runbook", "The procedure no longer matches infrastructure and Claude follows it faithfully into an error.", "Review the skill after every incident and date its last verification."),
   "learning loop is Module 9.12.9.", "a runbook is code; maintain it."),
 ],
 [("Where is a project skill saved?", "`.claude/skills/<name>/SKILL.md`."),
  ("What field stops Claude from starting a skill on its own?", "`disable-model-invocation: true`."),
  ("At what length are description and when_to_use truncated?", "1,536 characters."),
  ("The trigger text was cut off and the skill never matched. Name the failure mode by its exact label.", "**Description overflow.**"),
  ("Claude started the rollback skill from a wrong diagnosis. Name the failure mode.", "**Auto-fired remediation.**"),
  ("The runbook no longer matches reality. Name the failure mode by its exact label and fix.", "**Stale runbook.** Review it after every incident."),
  ("How many lines should SKILL.md stay under?", "500."),
  ("After compaction, how many tokens of each re-attached skill are kept, and what is the combined budget?", "5,000 tokens each; 25,000 combined."),
 ],
 ("Two skills, one read-only diagnosis and one manual action, with transcripts of each invocation mode.",
  [("Write diagnose skill", "SKILL.md"), ("Write action skill with disable flag", "SKILL.md"), ("Trigger diagnosis by description", "Transcript"), ("Try to trigger action automatically", "Refusal"), ("Run it by hand", "Transcript")]),
 """
| Check | Evidence |
|---|---|
| Diagnose auto-matched | description matched incident |
| Action manual only | not offered to Claude |
""", """
| Element | What is wrong |
|---|---|
| Rollback auto-invocable | **Auto-fired remediation** |
| Trigger past 1,536 chars | **Description overflow** |
""",
 "The artifact passes only if the action skill cannot be started by Claude and the diagnosis skill performs no write.",
 [("Anthropic", "Skills: frontmatter, lifecycle, budget", "Fields and numbers", "Current"), ("Anthropic", "Best practices: Put team procedures in skills", "Release example", "Current")],
 "none found between the sources read.",
 "This is the craft of runbook skills: **front-loaded triggers, split diagnosis from action, maintained like code.** The engineer who understands this does not ask \"where is the runbook?\" — they ask \"which steps may Claude start by itself?\"", read=15))

SPECS.append(G(M, "9.3.7", "Production safety",
 "Never give an unattended session write access to production: use read-only tooling, put never-rules in deny rules and hooks, and require human approval for changes.",
 "configure a session so a production write is blocked by a rule, not by a prompt, and show the block.",
 "anything that must never happen belongs in a deny rule, a hook or managed settings, not in the prompt.",
 "auto mode is a judgement, not a wall; the docs say 'never' rules belong in deny rules or hooks.",
 [("Layers of control",
   "The docs separate non-deterministic instructions (prompt, CLAUDE.md, skills, auto mode's classifier) from deterministic ones (hooks, deny rules, sandbox, managed settings); for rules that cannot have exceptions use the second kind [%s]." % BP,
   """
| Layer | Kind | Use |
|---|---|---|
| Prompt, CLAUDE.md | Non-deterministic | Guidance |
| Auto mode classifier | Non-deterministic | Blocks risky actions such as production deploys and force pushes by default |
| Deny rule | Deterministic | `Read(./.env)`, `Bash(kubectl delete *)` (pattern is an example) |
| PreToolUse hook | Deterministic | Exit 2 blocks |
| Sandbox | Deterministic OS-level | Confines shell commands |
| Managed settings | Deterministic, org-wide | Policy no personal file can override |

Deny rules hold in every permission mode including auto and `bypassPermissions` [%s].""" % BP,
   ("Prompt-only guard", "The only protection against touching production is a sentence in CLAUDE.md or the prompt, and context compaction loses it.", "Move it to a deny rule or a PreToolUse hook and test that it blocks."),
   "permissions are Module 4.2; sandboxing is Module 4.4.", "never-rules are configuration."),
  ("Credentials and modes",
   "`bypassPermissions` approves everything your deny and ask rules do not cover and only makes sense in a disposable container. After three blocks in a row or twenty in total, auto mode pauses and goes back to asking [%s]." % BP,
   """
| Session type | Credentials |
|---|---|
| Interactive investigation | Read-only observability tokens |
| Unattended `claude -p` | `--permission-mode dontAsk` or `auto` with `--permission-prompts none`; no prod write tokens |
| Disposable container | May use bypassPermissions; still no prod secrets |
| Change to production | Human runs it, or approves each step |""",
   ("Ambient credential", "Your shell has a production admin profile exported, and Claude inherits it.", "Run investigations in an environment with only scoped, read-only credentials."),
   "headless is Module 6.8; cloud environments are Module 4.5.", "credentials define the maximum damage."),
  ("Human approval for changes",
   "Changes to production should pass a human gate. Keep `ask` rules for risky commands so the permission prompt is the gate, and keep the final merge or deploy with a person [%s]." % BP,
   """
```json
{
  "permissions": {
    "ask":  ["Bash(git push *)"],
    "deny": ["Read(./.env)", "Read(./secrets/**)"]
  }
}
```

| Gate | Owner |
|---|---|
| Diff review | Human |
| Deploy approval | Human or protected pipeline |
| Rollback | Human, using a manual skill (Module 9.3.6) |""",
   ("Approval fatigue", "After ten routine prompts you approve a dangerous one without reading it.", "Allowlist the safe read-only commands (`/fewer-permission-prompts`) so prompts that remain are meaningful."),
   "norms are Module 9.12.", "keep prompts rare and real."),
 ],
 [("Which kinds of control are deterministic according to the docs?", "Hooks, deny rules, the sandbox and managed settings."),
  ("The only guard is a CLAUDE.md sentence. Name the failure mode by its exact label.", "**Prompt-only guard.**"),
  ("Your shell exports a prod admin profile. Name the failure mode.", "**Ambient credential.**"),
  ("You approved a dangerous prompt without reading. Name the failure mode by its exact label and fix.", "**Approval fatigue.** Allowlist safe commands."),
  ("After how many consecutive blocks does auto mode pause?", "Three in a row (or twenty in total)."),
  ("Where does `bypassPermissions` make sense?", "Only in a disposable container."),
  ("Do deny rules hold in auto mode?", "Yes; they hold in every permission mode."),
  ("Which command scans transcripts to add a read-only allowlist?", "`/fewer-permission-prompts`."),
 ],
 ("A settings file with deny and ask rules plus a transcript showing a blocked production write.",
  [("List 'never' actions", "List"), ("Write deny rules or a hook", "settings.json"), ("Remove ambient prod credentials", "Env note"), ("Attempt the action", "Block log"), ("Confirm human gate for changes", "Process note")]),
 """
| Check | Evidence |
|---|---|
| Block | deny rule message in transcript |
| Credentials | read-only token only |
""", """
| Element | What is wrong |
|---|---|
| Rule only in CLAUDE.md | **Prompt-only guard** |
| Admin profile in shell | **Ambient credential** |
""",
 "The artifact passes only if the blocked action was stopped by configuration and the session held only read-only credentials.",
 [("Anthropic", "Best practices: Enforce the rules that can't have exceptions; Change a default", "Layers, auto mode limits", "Current")],
 "none found between the sources read; specific cloud IAM setup was not fetched.",
 "This is the craft of production safety: **deterministic never-rules, scoped credentials, human gates.** The engineer who understands this does not ask \"will Claude behave?\" — they ask \"what can happen if it does not?\"", read=15))

SPECS.append(G(M, "9.3.8", "Post-incident work",
 "After an incident Claude can draft the timeline, a post-mortem and follow-up tickets from evidence you provide, with a human owning the conclusions.",
 "produce a timeline, a post-mortem draft and three follow-up tickets from one incident's logs and chat export, with every claim cited.",
 "every statement in the draft cites a source artifact or is labelled a hypothesis.",
 "the valuable part of a post-mortem is the follow-up that changes the system, which Claude can write but only a human can commit the team to.",
 [("Timeline from evidence",
   "Feed Claude the raw sources: alerts, logs, chat export and the git history. Piping command output into `claude -p` is a documented pattern, for example summarising recent commits [%s]." % CW,
   """
```bash
git log --since="2026-11-10 13:00" --until="2026-11-10 18:00" --oneline \\
  | claude -p "list these as timeline entries with timestamps"
```

| Timeline field | Source |
|---|---|
| Detected | Alert timestamp |
| Mitigated | Deploy or rollback record |
| Resolved | Error rate back to baseline |
| Actions | Chat export lines |""",
   ("Invented timeline", "Claude fills gaps with plausible times and events that are not in the sources.", "Require a source for each timeline row and 'unknown' where there is none."),
   "evidence is Module 9.3.2.", "no source, no row."),
  ("Post-mortem draft",
   "Ask for a blameless structure: impact, timeline, root cause, contributing factors, what went well, what did not, action items. Judge each against evidence; the causal chain from Module 9.3.5 is the core.",
   """
| Section | Check |
|---|---|
| Impact | Numbers match monitoring |
| Root cause | Has a regression test or guard |
| Contributing factors | Process, tooling, alerts |
| Action items | Owner, due date, ticket |""",
   ("Blame drift", "The draft names individuals as the cause and hides systemic factors.", "Prompt for blameless wording and review for people-as-cause language before sharing."),
   "root cause is Module 9.3.5.", "systems fail, not people."),
  ("Follow-up tickets",
   "Turn action items into tickets through a connected tracker only with human approval. Without a tracker, produce the text and file it yourself. Connected servers carry trust risks [%s]." % MCP,
   """
| Ticket field | Rule |
|---|---|
| Title | Verb plus object |
| Acceptance | A check that can pass or fail |
| Owner | A named human |
| Link | Post-mortem section |""",
   ("Orphan action item", "Actions have no owner or check, so nothing happens.", "Reject any item lacking an owner and a pass-or-fail acceptance line."),
   "learning loop is Module 9.12.9.", "an action without an owner is a wish."),
 ],
 [("What source rule applies to every timeline row?", "Each row cites a source, or says unknown."),
  ("Claude filled gaps with plausible times. Name the failure mode by its exact label.", "**Invented timeline.**"),
  ("The draft names an individual as the cause. Name the failure mode.", "**Blame drift.**"),
  ("Action items have no owner or check. Name the failure mode by its exact label and fix.", "**Orphan action item.** Require owner and pass-or-fail acceptance."),
  ("Which command pattern pipes git history into Claude?", "`git log ... | claude -p \"...\"`."),
  ("How many follow-up tickets does the prove-it ask for?", "Three."),
  ("Who commits the team to action items?", "A human."),
  ("Name two post-mortem sections.", "Impact, timeline, root cause, contributing factors, what went well, what did not, action items."),
 ],
 ("An incident bundle: timeline with sources, post-mortem draft and three tickets with owners and checks.",
  [("Collect sources", "Folder"), ("Generate timeline with citations", "Timeline"), ("Draft post-mortem", "Draft"), ("Review for blame and invention", "Review notes"), ("Write tickets", "3 tickets")]),
 """
| Item | Evidence |
|---|---|
| Timeline rows | 12, all sourced |
| Tickets | 3, each with owner |
""", """
| Element | What is wrong |
|---|---|
| Unsourced rows | **Invented timeline** |
| No owners | **Orphan action item** |
""",
 "The artifact passes only if every timeline row has a source and every ticket has an owner and an acceptance check.",
 [("Anthropic", "Common workflows: Pipe Claude into scripts", "Piping output", "Current"), ("Anthropic", "MCP", "Connected tools and trust", "Current")],
 "none found; blameless post-mortem structure is general practice, not from the docs.",
 "This is the craft of post-incident work: **sourced timelines, blameless drafts, owned actions.** The engineer who understands this does not ask \"can Claude write the report?\" — they ask \"can each line be traced and each action owned?\"", read=13, prove_h="1.5", thin="post-mortem structure is general practice; only piping and MCP trust are sourced"))

if __name__ == "__main__":
    for s in SPECS:
        write(s)
