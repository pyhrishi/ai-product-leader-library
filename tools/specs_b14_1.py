import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from specs_b14_0 import *

M = "b-14-1"
SPECS = []
C = "[Claude Code docs, Commands, 2026]"
RC = [("Anthropic", "Commands reference", "Every command, alias, argument and version note", "Current; read via fetch, rows summarised")]
NV = "Availability varies by platform, plan and version; if a command is missing, run `/help` and check `claude --version` before assuming it does not exist."

# ------------------------------------------------------------ 14.1.1
SPECS.append(G(M, "14.1.1", "First session in a repo: /init, /memory, /mcp, /permissions, /doctor, /powerup",
 "A first session in a new repo is a six-command setup sequence, and each command fixes one thing: what Claude knows, what it can reach, what it may do, and whether the install is healthy.",
 "set up a clean repo in the order /init, /memory, /mcp, /permissions, /doctor and show one observable result from each.",
 "run the setup commands in order once per repo, then check each result instead of trusting the command ran.",
 "/init writes a starting CLAUDE.md, not a finished one; a generated file is a draft you must edit and prune " + C + ".",
 20, "2", ["Name what each first-session command changes", "Run the sequence and verify each result", "Standardise a team onboarding sequence"],
 "A first-session log for a real repo: six commands, six observed results, and a pruned CLAUDE.md.",
 [S("Knowledge: /init and /memory", "`/init` initialises the project with a CLAUDE.md guide. Setting `CLAUDE_CODE_NEW_INIT=1` gives an interactive flow that also walks through skills, hooks and personal memory files, and if `/init` finds OpenAI Codex or Google Gemini CLI configuration it offers to carry it over with `/import` " + C + ". `/memory` edits CLAUDE.md files, turns auto memory on or off and shows auto memory entries " + C + ".",
   """
| Command | Changes | Observe |
|---|---|---|
| `/init` | Creates a starter CLAUDE.md | The file exists at the project root |
| `CLAUDE_CODE_NEW_INIT=1 /init` | Interactive flow incl. skills, hooks, memory files | Prompts appear |
| `/memory` | Opens CLAUDE.md files; toggles auto memory | The list of loaded files |

```bash
CLAUDE_CODE_NEW_INIT=1 claude      # then run /init inside the session
```
""", "Draft-as-final", "You run `/init`, accept what it wrote and never prune it, so the file carries generic or wrong lines into every later session.", "Read the generated file line by line, delete anything Claude could infer from the code, and keep only commands and rules that differ from defaults.", "CLAUDE.md design is Module 3.2; the file inventory is Module 14.4.", "the generated file is a draft."),
  S("Reach: /mcp", "`/mcp` manages MCP server connections and OAuth authentication. With no argument it opens the interactive list; `reconnect`, `enable` or `disable` take a server name or `all`, and in non-interactive mode with no argument it prints a text summary of server status " + C + ".",
   """
| You type | Effect |
|---|---|
| `/mcp` | Interactive list and OAuth |
| `/mcp reconnect <server>` | Retry one server |
| `/mcp reconnect all` | Retry every server that failed or needs authentication |
| `/mcp disable all` | Turn servers off for the session's context budget |
| `claude -p "/mcp"` | Text status summary, no UI |
""", "Silent-server", "A server shows as configured but never connected, and you debug the prompt while no tool from it exists in the session.", "Run `/mcp` first, read the status, and use `reconnect` before touching anything else.", "MCP in depth is Module 5.5; the `claude mcp` subcommand is Module 14.3.", "check the server list before blaming the model."),
  S("Control: /permissions", "`/permissions` manages allow, ask and deny rules in an interactive dialog: view rules by scope, add or remove them, manage working directories and review recent auto mode denials. Run while Claude is responding, it opens at once and applies changes from Claude's next tool call in the same turn; before v2.1.234 it queued until the turn ended " + C + ". Alias: `/allowed-tools`.",
   """
| Dialog area | Use |
|---|---|
| Rules by scope | See where each rule lives |
| Add or remove | Edit allow, ask, deny |
| Working directories | Widen or narrow file access |
| Auto mode tab | Review denials and classifier rules |
""", "Prompt-fatigue allowlist", "You approve the same prompt repeatedly and then add a broad allow rule to stop the interruptions, which also permits commands you never meant to.", "Add the narrowest rule that matches the prompt you keep seeing, and confirm its scope in the dialog.", "rule design is Module 4.2; modes are Module 4.3.", "narrow rules, checked in the dialog."),
  S("Health and learning: /doctor and /powerup", "`/doctor` runs a setup checkup that diagnoses installation, settings, extension and CLAUDE.md problems and proposes fixes that Claude applies after you confirm; `/doctor prompt-audit [path]` audits instructions and requires v2.1.283 or later; alias `/checkup` " + C + ". `/powerup` offers quick interactive lessons with animated demos " + C + ".",
   """
| Command | When |
|---|---|
| `/doctor` | After install, after editing settings, when behaviour surprises you |
| `/doctor prompt-audit CLAUDE.md` | Before committing a long instruction file |
| `/powerup` | When you want guided feature discovery |
""" + "\n" + NV, "Fix-without-reading", "You confirm every fix `/doctor` proposes without reading it, and a settings change you did not understand is now in your config.", "Read each proposed change, apply one at a time, and re-run `/doctor` to confirm the finding cleared.", "debugging configuration is Part 12.", "confirm fixes one at a time.")],
 [("Which command creates a starter CLAUDE.md?", "`/init`."), ("Which environment variable gives the interactive `/init` flow?", "`CLAUDE_CODE_NEW_INIT=1`."),
  ("You accept the generated CLAUDE.md untouched. Name the failure mode by its exact label.", "**Draft-as-final.**"),
  ("A server is configured but its tools never appear. Name the failure mode.", "**Silent-server.**"),
  ("What does `/mcp reconnect all` do?", "Retries every server that failed or needs authentication."),
  ("You broaden an allow rule to stop prompts. Name the failure mode and fix.", "**Prompt-fatigue allowlist.** Add the narrowest matching rule."),
  ("From which version does a `/permissions` change apply mid-turn?", "v2.1.234."), ("From which version does `/doctor prompt-audit` work?", "v2.1.283."),
  ("You confirm all `/doctor` fixes unread. Name the failure mode by its exact label.", "**Fix-without-reading.**"),
  ("What is the alias of `/doctor`?", "`/checkup`.")],
 [("Create a throwaway repo and run `/init`", "A CLAUDE.md"), ("Run `/memory` and list which files loaded", "File list"), ("Run `/mcp` and record each server's status", "Status table"),
  ("Run `/permissions`, add one narrow allow rule, trigger it", "Log line"), ("Run `/doctor` and record each finding and your decision", "Findings table"), ("Prune the CLAUDE.md to commands and differing rules", "Diff")],
 """
| Command | Observed result |
|---|---|
| `/init` | 41-line file, pruned to 12 |
| `/mcp` | Two servers connected, one failed, reconnected |
| `/permissions` | `Bash(npm run test)` allow fired once |
| `/doctor` | Three findings, two fixed, one declined with reason |
""", """
| Element | What is wrong |
|---|---|
| CLAUDE.md unchanged from `/init` | **Draft-as-final** |
| `/doctor` fixes all accepted, no reasons | **Fix-without-reading** |
""", "The artifact passes only if every command has an observed result and the CLAUDE.md differs from the generated draft.",
 RES(RC, "none found between the sources read; `/init` behaviour differs when `CLAUDE_CODE_NEW_INIT` is set, so state which flow you ran."),
 RF("first-session setup", "know, reach, control, check", "which commands should I run first?", "which of knowledge, reach, control and health is still unconfigured here?")))

# ------------------------------------------------------------ 14.1.2
SPECS.append(G(M, "14.1.2", "During a task: /plan, /model, /effort, /fast, /advisor, /context, /compact, /btw, /goal, /loop, /diff, /rewind, /clear, /recap",
 "Mid-task commands are steering controls: they change mode, model, effort, context and completion criteria without leaving the session, and each has a cost you can predict.",
 "run one task using /plan, /context, /compact with a focus, /btw and /goal and say what each changed.",
 "check /context before reaching for /compact, and set a goal only when you have a check Claude can run.",
 "changing the model or effort mid-session is not free: each model has its own prompt cache, so the first request after a switch re-reads the whole conversation uncached [Claude Code docs, Settings, 2026].",
 22, "2.5", ["Pick the right mid-task command for a symptom", "Predict the cost of a switch", "Design a steering routine for long tasks"],
 "A steering log: one task, six mid-task commands, each with the symptom that triggered it and the observed change.",
 [S("Mode and capability: /plan, /model, /effort, /fast, /advisor", "`/plan [description]` enters plan mode from the prompt and can start a task immediately, such as `/plan fix the auth bug`. `/model [model]` switches the model and saves it as the default for new sessions; press `s` on a picker row to switch for the current session only. `/effort` sets `low` to `xhigh`, `max` or `auto`, and `max` is session-only. `/fast [on|off]` toggles fast mode, and `/advisor [model|off]` enables a second model consulted at key moments " + C + ".",
   """
| Command | Saves as default? | Note |
|---|---|---|
| `/model sonnet` | Yes | `s` in the picker is session-only |
| `/model` with `-p` | No | Applies to the current session only |
| `/effort max` | No | `max` is session-only |
| `/fast off` | n/a | Toggles mid-turn; the running turn keeps its speed |
| `/advisor off` | n/a | Accepts fable, opus, sonnet or a full ID; fable needs access |
""", "Silent-default-switch", "You switch model to test something and the choice is saved as your default, so tomorrow's sessions start on a model you never meant to keep.", "Use the picker's `s` option for a session-only switch and check `/status` at the next launch.", "model choice is Module 1.4; effort is Module 2.2.", "decide whether a switch should persist before you confirm it."),
  S("Context: /context, /compact, /btw", "`/context [all]` draws context usage as a coloured grid with suggestions for heavy tools and memory bloat; in fullscreen it collapses the per-item breakdown and `all` expands it. `/compact [instructions]` summarises the conversation and accepts focus text. `/btw [question]` asks a side question without adding to the conversation; with no question it shows your latest side question " + C + ".",
   """
```text
/context                         # what is filling the window
/compact keep the migration plan and the failing test names
/btw what does the retry flag do?   # answer is not added to history
```

| Symptom | Command |
|---|---|
| Window filling | `/context`, then `/compact <focus>` |
| Tangent question | `/btw` |
| Task finished, new task | `/clear` |
""", "Compact-by-reflex", "You run `/compact` the moment answers feel slow without looking at `/context`, and the summary drops a constraint while the real bloat (a tool definition) stays.", "Read `/context` first, remove the actual bloat, and pass focus text to `/compact` so the constraint survives.", "context is Module 3.1; compaction survival is Module 1.2.4.", "look before you compact."),
  S("Completion: /goal, /loop, /diff, /rewind, /clear, /recap", "`/goal [condition|clear]` keeps Claude working across turns until the condition is met or the goal clears for another reason; `clear`, `stop`, `off`, `reset`, `none` or `cancel` removes it. `/loop [interval] [prompt]` repeats a prompt while the session stays open, self-pacing if you omit the interval. `/diff` reviews working-tree changes, `/rewind` restores a checkpoint (aliases `/checkpoint`, `/undo`), `/clear [name]` starts a new conversation (aliases `/reset`, `/new`) and `/recap` gives a one-line summary " + C + ".",
   """
| Need | Command |
|---|---|
| Work until a check passes | `/goal all tests in test/auth pass` |
| Poll something | `/loop 5m check if the deploy finished` |
| See what changed | `/diff` |
| Undo code and/or conversation | `/rewind` |
| Name and archive the old run | `/clear auth-spike` |
""", "Unverifiable-goal", "You set a goal whose condition Claude cannot test, so the loop either stops on its own judgement or runs on.", "Phrase the goal as a command and an expected output, such as a named test suite passing.", "goals and loops are Module 6.7; rewind is Module 2.5.", "a goal needs a check Claude can run.")],
 [("Which command asks a side question without adding to the conversation?", "`/btw`."), ("Which `/effort` level is session-only?", "`max`."),
  ("You switch model for a test and it becomes your default. Name the failure mode by its exact label.", "**Silent-default-switch.**"),
  ("What does the `s` key do in the `/model` picker?", "Switches for the current session only."),
  ("You run `/compact` without looking at `/context` and the bloat stays. Name the failure mode.", "**Compact-by-reflex.**"),
  ("A goal has no testable condition. Name the failure mode and fix.", "**Unverifiable-goal.** Phrase it as a command with an expected output."),
  ("Name three aliases of `/rewind` or `/clear`.", "`/checkpoint`, `/undo` for rewind; `/reset`, `/new` for clear."),
  ("Why is a mid-session model switch costly?", "Each model has its own prompt cache, so the first request re-reads the whole conversation uncached."),
  ("What do the words clear, stop, off, reset, none and cancel do to a goal?", "Each removes an active goal early."),
  ("Which version lets `/permissions`-style dialogs and `/fast` apply mid-turn per the docs?", "v2.1.234 for dialogs; v2.1.242 for `/model`, `/effort` and `/fast`.")],
 [("Start a task and run `/plan` first", "Plan text"), ("Run `/context` and record the top consumer", "Note"), ("Ask a `/btw` question and confirm history is unchanged", "Observation"),
  ("Set a `/goal` with a test command", "Goal line"), ("Run `/compact` with focus text and re-ask a constraint", "Result"), ("Run `/diff`, then `/rewind` one step", "Two logs")],
 """
| Command | Symptom | Observed |
|---|---|---|
| `/context` | Slow answers | MCP schemas biggest |
| `/btw` | Tangent | History unchanged |
| `/goal` | Needs tests green | Stopped when suite passed |
""", """
| Element | What is wrong |
|---|---|
| Model switched and forgotten | **Silent-default-switch** |
| `/compact` with no `/context` check | **Compact-by-reflex** |
""", "The artifact passes only if each command is tied to a symptom and an observed change.",
 RES(RC + [("Anthropic", "Settings", "Per-model prompt cache on switch", "Current")], "none found between the sources read."),
 RF("steering a task", "right command, right moment, known cost", "which command should I type?", "what symptom is this and what will the command cost?")))

# ------------------------------------------------------------ 14.1.3
SPECS.append(G(M, "14.1.3", "Parallel and background work: /tasks, /background, /fork, /subtask, /branch, /batch, /workflows, /list-agents, /schedule",
 "Nine commands manage work that runs beside your conversation, and the key skill is telling apart the ones that copy the conversation, the ones that detach it and the ones that fan it out.",
 "use /fork, /subtask and /branch on one conversation and explain where each result lands.",
 "ask where the result should come back before choosing the command.",
 "/fork and /branch both copy a conversation, but /fork keeps you here and runs the copy in the background while /branch switches you into the copy " + C + ".",
 22, "2.5", ["Tell fork, subtask, branch and background apart", "Choose fan-out versus delegation", "Design a parallel-work policy"],
 "A decision table mapping six situations to the right command, each tested once.",
 [S("Copy or detach the conversation", "`/background [prompt]` detaches the current session as a background agent and frees the terminal (alias `/bg`); monitor it with `claude agents`. `/fork [prompt]` copies the conversation into a new background session while you keep working. `/branch [name]` creates a branch of the conversation, switches you into it and preserves the original, which you return to with `/resume` " + C + ".",
   """
| Command | You end up | Original conversation |
|---|---|---|
| `/background` | Terminal freed | Keeps running detached |
| `/fork` | Still in the original | Copy runs in the background |
| `/branch` | Inside the copy | Preserved, reachable via `/resume` |
""", "Copy-confusion", "You use `/branch` expecting the work to continue in the background, and sit in a new conversation while the old one is idle.", "Ask whether you want to stay (`/fork`), move (`/branch`) or leave (`/background`) before you type.", "sessions are Module 2.4; background sessions are Module 6.3.", "stay, move or leave."),
  S("Delegate and watch: /subtask, /tasks, /list-agents", "`/subtask <task>` spawns a forked subagent that inherits the full conversation and returns its result into this conversation; `/tasks` (alias `/bashes`) shows background work, including finished subagents; `/list-agents` (alias `/peers`) lists subagents, agent team teammates and sessions Claude can message, and requires v2.1.224 or later and cross-session messaging " + C + ".",
   """
| Question | Command |
|---|---|
| What is running? | `/tasks` |
| Whom can Claude message? | `/list-agents` |
| Hand a side job back to me when done | `/subtask <task>` |
""" + "\n" + NV, "Orphaned-task", "You launch background work and never check `/tasks`, so a finished or stuck subagent sits unreviewed.", "Check `/tasks` before ending a session and read each finished result.", "subagents are Module 1.2.5; cross-session messaging is Module 6.4.", "background work still needs a review pass."),
  S("Fan out and schedule: /batch, /workflows, /schedule", "`/batch <instruction>` is a bundled skill that researches the codebase, decomposes the work into 5 to 30 independent units, presents a plan and, once approved, spawns one background subagent per unit in an isolated worktree; it needs a git repository or a `WorktreeCreate` hook " + C + ". `/workflows` opens the progress view to watch, pause, resume or save workflows, and `/schedule` creates, updates, lists or runs routines that execute in the cloud (alias `/routines`) " + C + ".",
   """
```text
/batch migrate src/ from JavaScript to TypeScript
```

| Command | Runs where | Use for |
|---|---|---|
| `/batch` | Local worktrees, background subagents | Many independent edits |
| `/workflows` | Progress view | Watching and saving fan-outs |
| `/schedule` | Cloud routines | Recurring work |
""", "Dependent-units", "You run `/batch` on a change whose pieces depend on each other, so units conflict or each rewrites the same shared file.", "Check the plan for independence before approving; split dependent work into an ordered series instead.", "workflows are Module 6.5; scheduled tasks are Module 6.7; worktrees are Module 6.2.", "fan out only independent units.")],
 [("How many independent units does `/batch` decompose into?", "5 to 30."), ("Which command keeps you in the original conversation and copies it to the background?", "`/fork`."),
  ("You used `/branch` expecting background work. Name the failure mode by its exact label.", "**Copy-confusion.**"),
  ("What alias does `/background` have?", "`/bg`."), ("Background work finishes and no one reads it. Name the failure mode.", "**Orphaned-task.**"),
  ("What does `/batch` require besides approval of the plan?", "A git repository or a `WorktreeCreate` hook."),
  ("You run `/batch` on dependent changes. Name the failure mode and fix.", "**Dependent-units.** Check independence in the plan; use an ordered series."),
  ("What is the minimum version for `/list-agents`?", "v2.1.224."), ("Where do `/schedule` routines run?", "In the cloud."),
  ("Which command returns its result into this conversation?", "`/subtask`.")],
 [("Run `/fork` with a prompt and confirm you stayed", "Observation"), ("Run `/branch`, then `/resume` the original", "Two observations"), ("Run `/subtask` and wait for the result", "Result log"),
  ("Open `/tasks` and list the finished subagent", "Task list"), ("Run `/batch` on a tiny change in a git repo and read the plan", "Plan notes"), ("Build the six-row decision table", "Table")],
 """
| Situation | Command | Result lands |
|---|---|---|
| Long test run, keep working | `/fork` | Background session |
| Try another design | `/branch` | New current conversation |
| Side lookup, answer here | `/subtask` | This conversation |
""", """
| Element | What is wrong |
|---|---|
| `/branch` used for background work | **Copy-confusion** |
| `/batch` approved without reading units | **Dependent-units** risk |
""", "The artifact passes only if each command was run once and its landing place observed.",
 RES(RC, "none found between the sources read."),
 RF("parallel work", "know where the result lands", "which parallel command is best?", "do I stay, move, leave or fan out, and where does the answer come back?")))

# ------------------------------------------------------------ 14.1.4
SPECS.append(G(M, "14.1.4", "Before you ship: /diff, /code-review, /simplify, /security-review, /verify, /run, /autofix-pr, /install-github-app",
 "Pre-ship commands split by question: /diff shows what changed, /code-review finds correctness bugs, /simplify finds cleanup, /security-review finds vulnerabilities and /verify checks the app actually runs.",
 "run each pre-ship command on one branch and say which question each answered.",
 "match the command to the question and never treat a clean cleanup review as a correctness review.",
 "/simplify does not look for correctness bugs; a branch can pass /simplify and still be wrong " + C + ".",
 22, "2.5", ["Name the question each command answers", "Run a layered pre-ship pass", "Wire review into a team pipeline"],
 "A pre-ship checklist run on a real branch with the output of each command.",
 [S("Look and review", "`/diff` reviews working-tree changes including Claude's edits. `/code-review [low|medium|high|xhigh|max|ultra] [--fix] [--comment] [--max-findings n|all|default] [pr#|branch|path]` is a bundled skill that reviews the diff, a PR number, a branch or a path for correctness bugs; `--fix` applies findings, `--comment` posts them, `ultra` runs a deep cloud review; alias `/review` " + C + ".",
   """
| Command | Question | Output |
|---|---|---|
| `/diff` | What changed? | Working-tree diff |
| `/code-review high` | Is it correct? | Findings |
| `/code-review high --fix` | Fix what you found | Applied edits |
| `/code-review 1234` | Review PR 1234 | Findings on that PR |
| `/code-review ultra` | Deep review | Cloud multi-agent review |
""", "Review-as-rubber-stamp", "You run `/code-review --fix` and merge the applied edits unread, so the reviewer and the author are the same unchecked process.", "Read the diff of the applied fixes with `/diff` and rerun your check before commit.", "review is Module 2.3 and Module 7.3.", "review the review."),
  S("Cleanup and security", "`/simplify [target]` runs four parallel review agents covering reuse of existing helpers, simplification, efficiency and abstraction level, and applies fixes. `/security-review` analyses the diff against origin's default branch for injection, auth and data-exposure risks, and needs an `origin` remote " + C + ".",
   """
| Command | Looks for | Does not look for |
|---|---|---|
| `/simplify` | Reuse, simplification, efficiency, abstraction | Correctness bugs |
| `/code-review` | Correctness bugs | (cleanup only at some effort levels) |
| `/security-review` | Injection, auth, exposure | General style |
""", "Wrong-question-clean", "You see a clean `/simplify` result and conclude the change is safe, though that review never looked for correctness or security issues.", "Run `/code-review` and `/security-review` for those questions and keep `/simplify` for cleanup.", "security is Module 4.4 and Module 11.1.", "a clean result answers only its own question."),
  S("Prove it runs, then hand off", "`/verify` builds your project's app, runs it and observes the result rather than relying on tests or type checks; `/run` launches and drives the app, and `/verify` runs only when you invoke it (before v2.1.215 Claude could run it itself). `/autofix-pr [prompt]` spawns a cloud session that watches the branch's PR and pushes fixes for CI failures and review comments, needing the `gh` CLI and cloud access. `/install-github-app` installs the GitHub App for github.com repositories only " + C + ".",
   """
```text
/autofix-pr only fix lint and type errors
```

| Step | Command |
|---|---|
| Does the app work? | `/verify` |
| Drive the app manually | `/run` |
| Keep a PR green | `/autofix-pr` |
| Connect GitHub | `/install-github-app` (github.com only) |
""", "Unbounded-autofix", "You start `/autofix-pr` with no instruction and the cloud session tries to fix every CI failure and review comment, including ones you wanted to handle yourself.", "Pass a prompt that bounds scope and review each push.", "CI integration is Module 8.1; Actions are Module 8.2.", "bound the autofix prompt.")],
 [("Which command analyses the diff for injection and auth issues?", "`/security-review`."), ("Which review does not look for correctness bugs?", "`/simplify`."),
  ("You merge `/code-review --fix` edits unread. Name the failure mode by its exact label.", "**Review-as-rubber-stamp.**"),
  ("A clean `/simplify` is read as safe. Name the failure mode.", "**Wrong-question-clean.**"),
  ("How many parallel agents does `/simplify` run?", "Four."), ("What alias does `/code-review` have?", "`/review`."),
  ("You run `/autofix-pr` with no prompt. Name the failure mode and fix.", "**Unbounded-autofix.** Pass a prompt that bounds scope."),
  ("Which effort levels does `/code-review` accept?", "low, medium, high, xhigh, max, ultra."),
  ("What does `/install-github-app` do for a gitlab.com remote?", "Prints a notice and exits."), ("What does `/security-review` need?", "An `origin` remote.")],
 [("Make a small change on a branch", "Diff"), ("Run `/diff` and `/code-review high`", "Findings"), ("Run `/simplify` and record what it changed", "Cleanup diff"),
  ("Run `/security-review` and record result", "Report"), ("Run `/verify` and capture the observed behaviour", "Log"), ("Fill the checklist with the question each answered", "Checklist")],
 """
| Command | Question | Result |
|---|---|---|
| `/diff` | What changed | 3 files |
| `/code-review high` | Correct? | 1 finding fixed |
| `/security-review` | Vulnerable? | None found |
| `/verify` | Runs? | Yes, observed |
""", """
| Element | What is wrong |
|---|---|
| Only `/simplify` run | **Wrong-question-clean** |
| Fixes applied, not re-diffed | **Review-as-rubber-stamp** |
""", "The artifact passes only if each question has its own command and an observed result.",
 RES(RC, "none found between the sources read."),
 RF("pre-ship review", "one command per question", "did the review pass?", "which question did that review actually answer?")))

# ------------------------------------------------------------ 14.1.5
SPECS.append(G(M, "14.1.5", "Between sessions: /resume, /rename, /export, /teleport, /remote-control, /desktop, /cd, /add-dir",
 "These eight commands move work between times, devices and directories, and the sharp edge is that moving a directory and adding one are different things.",
 "resume a session, rename it, export it, and show the difference between /cd and /add-dir.",
 "name every session you intend to return to.",
 "/add-dir grants file access but most .claude configuration is not discovered from the added directory " + C + ".",
 20, "2", ["Use the eight commands correctly", "Choose /cd versus /add-dir", "Set a team session-naming rule"],
 "A session handoff note: rename, export, resume and one cross-device move, each shown working.",
 [S("Resume, rename, export", "`/resume [session]` resumes a conversation by ID or name or opens the picker, and background sessions appear marked `bg`. `/rename [name]` renames the session and shows the name on the prompt bar; with no name it generates one from history. `/export [filename]` exports the conversation as plain text, writing to the file if you give a name " + C + ".",
   """
| Command | Input | Output |
|---|---|---|
| `/rename auth-refactor` | Name | Label in prompt bar and picker |
| `/export notes.txt` | File name | Plain-text transcript |
| `/resume auth-refactor` | Name or ID | That conversation |
""", "Unnamed-session", "You leave sessions with auto-generated or no names and cannot find the right one in the picker a week later.", "Run `/rename` as soon as the task has a name and use `/clear <name>` when switching.", "session management is Module 2.4.", "name sessions you will want back."),
  S("Move between devices", "`/teleport` (alias `/tp`) pulls a cloud session into this terminal and requires a claude.ai subscription. `/remote-control` (alias `/rc`) makes this session available from claude.ai. `/desktop` (alias `/app`) continues the session in the Desktop app and requires macOS or x64 Windows and a subscription " + C + ".",
   """
| Direction | Command | Needs |
|---|---|---|
| Cloud to terminal | `/teleport` | claude.ai subscription |
| Terminal to other device | `/remote-control` | claude.ai subscription |
| Terminal to Desktop app | `/desktop` | macOS or x64 Windows, subscription |
""", "Platform-assumption", "You tell a teammate to run `/desktop` and it is missing on their machine because of platform or plan.", "Check the availability note and `/help` before documenting a command in a team guide.", "platforms are Module 9.1 and Module 6.3.", "availability is per platform and plan."),
  S("Move versus add a directory", "`/cd <path>` moves the session to a new working directory and keeps the conversation. `/add-dir <path>` adds a working directory for file access during the session; most `.claude/` configuration is not discovered from the added directory " + C + ". Per the settings docs, after `/cd` Claude Code reads both project settings files from the new directory, which requires v2.1.246 or later [Claude Code docs, Settings, 2026].",
   """
| | `/cd` | `/add-dir` |
|---|---|---|
| Working directory | Changes | Stays; another is added |
| Project settings read from | New directory (v2.1.246+) | Original only |
| Use for | Switching project | Reading a sibling repo |
""", "Config-from-added-dir", "You `/add-dir` a repo expecting its CLAUDE.md, skills and hooks to apply, and none do.", "Use `/cd` to switch projects, or start Claude there.", "memory loading is Module 3.3; permissions are Module 4.2.", "add-dir gives files, not configuration.")],
 [("Which command moves the session to another directory and keeps the conversation?", "`/cd`."), ("Which command adds file access without moving?", "`/add-dir`."),
  ("You expect an added directory's skills to load. Name the failure mode by its exact label.", "**Config-from-added-dir.**"),
  ("Sessions cannot be found a week later. Name the failure mode.", "**Unnamed-session.**"),
  ("Which version reads project settings from the directory after `/cd`?", "v2.1.246 or later."), ("What are the aliases of `/teleport` and `/remote-control`?", "`/tp` and `/rc`."),
  ("A teammate lacks `/desktop`. Name the failure mode and fix.", "**Platform-assumption.** Check availability and `/help`."),
  ("What does `/export` produce?", "A plain-text transcript."), ("Which platforms does `/desktop` need?", "macOS or x64 Windows, with a subscription."),
  ("What marks background sessions in the resume picker?", "`bg`.")],
 [("Rename a session and `/clear` with a name", "Two labels"), ("Resume it by name", "Observation"), ("Export it to a file", "File"), ("Run `/cd` to a sibling repo and check the CLAUDE.md that loads", "Observation"),
  ("Run `/add-dir` on another and check that config does not load", "Observation"), ("Write the team naming rule", "One line")],
 """
| Test | Observed |
|---|---|
| `/cd ../api` | api CLAUDE.md loaded |
| `/add-dir ../api` | Files readable, skills not loaded |
""", """
| Element | What is wrong |
|---|---|
| No names used | **Unnamed-session** |
| Skills expected after add-dir | **Config-from-added-dir** |
""", "The artifact passes only if both the cd and add-dir behaviours were observed.",
 RES(RC + [("Anthropic", "Settings", "Settings read after /cd", "Current")], "none found between the sources read."),
 RF("moving work", "name it, export it, and pick cd or add-dir deliberately", "how do I get back to that?", "did I name it, and does the destination load its own configuration?")))


# ------------------------------------------------------------ 14.1.6
SPECS.append(G(M, "14.1.6", "Configuration commands: /config, /update-config, /output-style, /statusline, /theme, /tui, /keybindings, /terminal-setup, /voice, /sandbox, /autocompact, /privacy-settings",
 "Twelve commands change how Claude Code looks, feels and is bounded; the useful split is between ones that write settings files, ones that only change the session, and ones that need a plan or platform.",
 "change one setting with /config key=value, confirm it with /status and show where it was saved.",
 "after any configuration command, confirm what loaded and where it was written.",
 "/config opens a menu of personal options, not every settings key, and its Config tab is not a view of your settings.json [Claude Code docs, Settings, 2026].",
 20, "2", ["Name which command writes which file", "Change settings by key=value and verify", "Standardise team terminal setup"],
 "A configuration log: six commands run, the file each wrote to, and the verification of each.",
 [S("Settings: /config and /update-config", "`/config [key=value ...]` opens the Settings interface, or sets keys directly such as `/config thinking=false`, `/config theme=dark` or `/config model=sonnet`; the key=value form also works with `-p`, cannot turn on settings that need confirmation such as `autoContinueAtUsageLimit` though it can turn them off, `/config --help` lists accepted keys, and the alias is `/settings` " + C + ". `/update-config` is a bundled skill that edits the matching settings.json from a description such as allowing a command or adding a hook " + C + ".",
   """
| Option saved from `/config` | Written to |
|---|---|
| Most options | `~/.claude/settings.json` |
| A few, such as Show tips | `.claude/settings.local.json` |
| Global config options | `~/.claude.json` |

[Claude Code docs, Settings, 2026]
""", "Wrong-scope-write", "You change a setting expecting the team to get it, but `/config` wrote it to your user file.", "Check the table above, and for team settings edit `.claude/settings.json` and commit it.", "settings are Module 4.1.", "know which file a command writes."),
  S("Look and feel", "`/output-style [style]` lists or switches output styles and needs v2.1.269 or later. `/theme` changes the colour theme, including auto, colourblind-accessible and custom themes. `/statusline` configures the status line, auto-configuring from your shell prompt with no arguments. `/tui [default|fullscreen]` sets the renderer and relaunches with the conversation intact " + C + ". `/keybindings` opens your shortcuts file and `/terminal-setup` installs a Shift+Enter binding for VS Code, Cursor, Devin Desktop, Alacritty or Zed " + C + ".",
   """
| Command | Changes |
|---|---|
| `/output-style concise` | How Claude writes |
| `/theme` | Colours |
| `/statusline` | Bottom status line |
| `/tui fullscreen` | Flicker-free renderer; relaunch |
| `/terminal-setup` | Shift+Enter newline binding |
""" + "\n" + NV, "Cosmetic-first", "You spend setup time on theme and status line before the permissions and memory that change outcomes.", "Do `/init`, `/permissions` and `/memory` first (Module 14.1 first-session) and treat appearance as the last pass.", "terminal setup is Module 9.1.", "outcomes before looks."),
  S("Bounds and voice", "`/sandbox` toggles sandbox mode on supported platforms only. `/autocompact [auto|<tokens>]` sets how full the window gets before automatic compaction, saves it to user settings and applies it now. `/voice [hold|tap|off]` toggles voice dictation and needs a Claude.ai account; `/privacy-settings` is for Pro and Max subscribers only " + C + ".",
   """
```text
/autocompact 500k      # compact earlier than the default window
/autocompact auto      # return to the model-tuned window
/sandbox               # toggle where supported
```
""", "Sandbox-assumed-on", "You assume the sandbox is active on a platform that does not support it, so Bash commands run unbounded.", "Run `/sandbox` and read the result; do not infer protection from the command existing.", "sandboxing is Module 4.4.", "check, do not assume, the sandbox.")],
 [("Which command sets a setting directly from the prompt?", "`/config key=value`."), ("What is `/config`'s alias?", "`/settings`."),
  ("You change a setting for the team but it saved to your user file. Name the failure mode by its exact label.", "**Wrong-scope-write.**"),
  ("Which file stores global config options?", "`~/.claude.json`."),
  ("Which version does `/output-style` need?", "v2.1.269."), ("You tweak themes before permissions. Name the failure mode.", "**Cosmetic-first.**"),
  ("You assume the sandbox is on. Name the failure mode and fix.", "**Sandbox-assumed-on.** Run `/sandbox` and read the result."),
  ("What does `/autocompact 500k` do?", "Sets the auto-compact window to 500k and saves it to user settings."),
  ("Which `/config` setting cannot be turned on by key=value?", "Settings needing confirmation, such as `autoContinueAtUsageLimit`."),
  ("Which plans can use `/privacy-settings`?", "Pro and Max.")],
 [("Run `/config theme=dark`", "Observation"), ("Run `/status` and read the Setting sources line", "Line"), ("Run `/config --help` and list five keys", "Five keys"),
  ("Run `/statusline` with no arguments", "Status line"), ("Run `/sandbox` and record the outcome", "Note"), ("Record where each change was written", "Table")],
 """
| Command | Written to |
|---|---|
| `/config theme=dark` | `~/.claude/settings.json` |
| `/autocompact 500k` | user settings |
| `/sandbox` | platform-dependent note |
""", """
| Element | What is wrong |
|---|---|
| No file column | **Wrong-scope-write** unchecked |
| Sandbox not run | **Sandbox-assumed-on** |
""", "The artifact passes only if every command has a verified write location or a stated no-write.",
 RES(RC + [("Anthropic", "Settings", "Files and scopes", "Current")], "none found between the sources read."),
 RF("configuring Claude Code", "know the write location and verify it loaded", "did the setting stick?", "which file did that write, and does /status show it loaded?"),
 thin="Appearance commands (theme, tui, statusline) are covered at one-line depth because the docs add little beyond their descriptions."))

# ------------------------------------------------------------ 14.1.7
SPECS.append(G(M, "14.1.7", "Extension commands: /skills, /skill-doctor, /reload-skills, /plugin, /reload-plugins, /hooks, /agents, /chrome, /ide, /install-slack-app",
 "Extension commands list, reload and audit what you have installed, and /agents is now a reminder page, not an editor.",
 "list your skills, add one on disk, reload without restarting and show the count change.",
 "reload after changing extensions on disk and audit what each one costs in context.",
 "/agents no longer opens a manager: on v2.1.198 and later it prints a reminder to ask Claude to create subagents or edit the agents directories " + C + ".",
 20, "2", ["Use list, reload and audit commands", "Find unused skills by cost", "Run an extension hygiene routine"],
 "An extension inventory: skills, plugins, hooks and agents, with reload and cost evidence.",
 [S("Skills", "`/skills` lists available skills; press `t` to sort by token count and `Space` or `Enter` to cycle a skill's visibility. `/skill-doctor` shows what each skill costs in context and how often it is used, and needs v2.1.252 or later plus feature-flag fetching. `/reload-skills` re-scans skill and command directories so skills added on disk become available without a restart and reports how many were added or removed " + C + ".",
   """
| Command | Answers |
|---|---|
| `/skills` | What is available? Sort by tokens |
| `/skill-doctor` | Which skills cost most or go unused? |
| `/reload-skills` | Did my new SKILL.md load? |
""", "Phantom-skill", "You add a skill folder mid-session and Claude never uses it because nothing reloaded.", "Run `/reload-skills`, read the added count, then check `/skills`.", "skills are Module 5.2.", "reload, then confirm the count."),
  S("Plugins and hooks", "`/plugin [subcommand]` opens the plugin menu or acts directly with `list`, `install`, `enable` or `disable`; `/reload-plugins [--force]` applies pending changes and warns and skips when the reload would change loaded MCP tools and invalidate the prompt cache unless you pass `--force`. `/hooks` views hook configurations " + C + ".",
   """
| Command | Effect |
|---|---|
| `/plugin install <name>` | Install; the summary says whether it activated |
| `/reload-plugins` | Apply pending changes |
| `/reload-plugins --force` | Reload even if it invalidates the cache |
| `/hooks` | Read-only view of configured hooks |
""", "Forced-reload-habit", "You always pass `--force` and pay for an uncached conversation re-read each time.", "Reload without `--force` first and force only when the warning is acceptable.", "plugins are Module 5.6; hooks are Module 5.4.", "the warning is a cost notice."),
  S("Agents and integrations", "`/agents` prints a reminder to ask Claude to create or manage subagents or to edit `.claude/agents/` or `~/.claude/agents/`; on v2.1.197 and earlier it opened an interface. `/chrome` configures Claude in Chrome, `/ide` manages IDE integrations and shows status and `/install-slack-app` opens a browser for OAuth " + C + ".",
   """
| Command | Today |
|---|---|
| `/agents` | Reminder page |
| `/chrome` | Chrome settings |
| `/ide` | IDE status |
| `/install-slack-app` | OAuth in browser |
""", "Stale-tutorial", "A blog tells you to use the `/agents` interface and you search for a menu that no longer exists.", "Check the Commands page and your `claude --version` before following an older tutorial.", "subagents are Module 5.3; IDE and browser are Module 9.1.", "docs beat tutorials.")],
 [("Which command shows what each skill costs in context?", "`/skill-doctor`."), ("Which command re-scans skills without a restart?", "`/reload-skills`."),
  ("A new skill folder is ignored. Name the failure mode by its exact label.", "**Phantom-skill.**"), ("Which version does `/skill-doctor` need?", "v2.1.252 or later."),
  ("You always pass `--force`. Name the failure mode.", "**Forced-reload-habit.**"), ("What does `/agents` do on v2.1.198 and later?", "Prints a reminder page."),
  ("A tutorial describes the old `/agents` menu. Name the failure mode and fix.", "**Stale-tutorial.** Check the Commands page and your version."),
  ("What key sorts `/skills` by tokens?", "`t`."), ("Why does `/reload-plugins` sometimes skip?", "It would invalidate the prompt cache and you did not pass `--force`."),
  ("Which subcommands does `/plugin` accept directly?", "list, install, enable, disable.")],
 [("Run `/skills` and sort by tokens", "Top three"), ("Add a trivial skill folder and run `/reload-skills`", "Count change"), ("Run `/plugin list`", "List"),
  ("Run `/reload-plugins` and read the output", "Note"), ("Run `/hooks`", "Hook list"), ("Write the inventory", "Table")],
 """
| Extension | Count | Cost evidence |
|---|---|---|
| Skills | 9 (+1 after reload) | `/skills` token sort |
| Plugins | 2 | `/plugin list` |
| Hooks | 3 | `/hooks` |
""", """
| Element | What is wrong |
|---|---|
| Skill added, no reload | **Phantom-skill** |
| Menu steps from an old tutorial | **Stale-tutorial** |
""", "The artifact passes only if the reload delta was observed and costs came from the tools, not memory.",
 RES(RC, "older tutorials describe an interactive `/agents` manager; the Commands page says that applied to v2.1.197 and earlier. **The Commands page wins.**"),
 RF("extension hygiene", "list, reload, audit", "why isn't my skill loading?", "did I reload, and what does it cost?")))

# ------------------------------------------------------------ 14.1.8
SPECS.append(G(M, "14.1.8", "Diagnostics and help: /help, /status, /debug, /doctor, /heapdump, /bug, /feedback, /release-notes, /insights",
 "Diagnostic commands answer three different questions: what is loaded (/status), what went wrong at runtime (/debug) and what is the install state (/doctor), and they also include a destructive-to-privacy trap in /heapdump.",
 "pick the right diagnostic for three symptoms and run each.",
 "start with /status, then escalate to /doctor or /debug by the kind of symptom.",
 "the .heapsnapshot written by /heapdump contains your full conversation and credentials; only the diagnostics JSON is safe to attach " + C + ".",
 20, "2", ["Choose a diagnostic by symptom", "Report bugs without leaking data", "Make diagnostics a team habit"],
 "A symptom-to-command table with one real run of each command and a safe bug-report checklist.",
 [S("What is loaded, what is wrong", "`/status` opens Settings on the Status tab showing version, model, account and connectivity; its Setting sources line lists the loaded settings files [Claude Code docs, Settings, 2026]. `/doctor` diagnoses installation, settings, extension and CLAUDE.md problems and proposes fixes. `/debug [description]` is a bundled skill that enables debug logging from that point on and reads the session debug log; logging is off unless you started with `claude --debug` " + C + ".",
   """
| Symptom | Start with |
|---|---|
| Wrong model or file loaded | `/status` |
| Install or config looks broken | `/doctor` |
| Odd runtime behaviour | `/debug <description>` |
| Setting ignored in `-p` | `claude doctor` |
""", "Debug-too-late", "You run `/debug` after the failure already happened and expect it to explain history, but logging starts only from that point.", "Start with `claude --debug` for reproducible issues, or rerun the failing step after `/debug`.", "debugging is Part 12.", "logging is forward-only."),
  S("Reporting without leaking", "`/bug [report]` and `/feedback` open a consent screen where you choose how much session history to include; signed in to Anthropic first-party, the report goes to Anthropic, otherwise it is written to a local archive under `~/.claude/feedback-bundles/` for you to forward. `/heapdump` writes a heap snapshot and a diagnostics breakdown to `~/Desktop` or your home directory; attach only the `-diagnostics.json` " + C + ".",
   """
| File | Safe to share? |
|---|---|
| `*-diagnostics.json` | Yes, per the docs |
| `*.heapsnapshot` | No: contains conversation and credentials |
| `feedback-bundles/` archive | Only after you review it |
""", "Snapshot-attached", "You attach the whole heapdump folder to a public issue and publish your conversation and credentials.", "Attach only the diagnostics JSON and review any bundle before forwarding.", "security basics are Module 4.4.", "share the JSON, never the snapshot."),
  S("Learning from usage", "`/help` lists commands, `/release-notes` opens an interactive version picker whose notes stay out of the conversation Claude sees, and `/insights` generates an HTML report analysing recent sessions on this machine, not available in cloud sessions " + C + ".",
   """
| Command | Output |
|---|---|
| `/help` | Command list |
| `/release-notes` | Per-version notes, not sent to Claude |
| `/insights` | HTML report of your sessions |
""" + "\n" + NV, "Untested-upgrade", "You read release notes and assume a new behaviour applies to your version without checking it.", "Check `claude --version` and the version tag in the docs row before relying on a change.", "keeping up is Module 16.3.", "match the version tag to your version.")],
 [("Which command shows which settings files loaded?", "`/status`."), ("Which file from `/heapdump` should you attach to a report?", "The `-diagnostics.json` file."),
  ("You attach a heap snapshot to a public issue. Name the failure mode by its exact label.", "**Snapshot-attached.**"),
  ("You run `/debug` after the failure and expect history. Name the failure mode.", "**Debug-too-late.**"),
  ("Where does a report go on a third-party provider?", "A local archive under `~/.claude/feedback-bundles/`."),
  ("Is debug logging on by default?", "No, unless started with `claude --debug`."),
  ("You assume a release-note feature is in your version. Name the failure mode and fix.", "**Untested-upgrade.** Check the version."),
  ("Which command analyses your recent sessions into an HTML report?", "`/insights`."), ("Is `/insights` available in cloud sessions?", "No."),
  ("Why is `/heapdump` not in the menu?", "It is hidden by design until typed in full.")],
 [("Run `/status` and note the setting sources", "Line"), ("Run `/doctor` and read findings", "Findings"), ("Run `/debug` then repeat a failing step", "Log excerpt"),
  ("Run `/release-notes` for your version", "Note"), ("Draft a bug-report checklist", "Checklist"), ("Write the symptom table", "Table")],
 """
| Symptom | Command | Result |
|---|---|---|
| Hook not firing | `/debug` | Matcher mismatch in log |
| Wrong model | `/status` | Project file set model |
Checklist: attach diagnostics JSON only; never `.heapsnapshot`.
""", """
| Element | What is wrong |
|---|---|
| `/debug` run after the incident | **Debug-too-late** |
| Snapshot in the attachment list | **Snapshot-attached** |
""", "The artifact passes only if every symptom maps to a command that was actually run and the checklist forbids the snapshot.",
 RES(RC + [("Anthropic", "Settings", "Status tab and Setting sources", "Current")], "none found between the sources read."),
 RF("diagnostics", "the right command for the right question", "which diagnostic do I run?", "is this a what-is-loaded, install-state or runtime question?")))

# ------------------------------------------------------------ 14.1.9
SPECS.append(G(M, "14.1.9", "Accounts and usage: /login, /logout, /usage, /usage-credits, /rate-limit-options, /upgrade",
 "Six commands manage identity and quota, and /usage is the single read-out for session cost, plan limits and stats.",
 "read /usage before and after a heavy task and record what changed.",
 "check /usage before heavy work, not after the stall.",
 "/cost and /stats are aliases of /usage, not separate commands " + C + ".",
 18, "1.5", ["Name what each account command does", "Plan around limits", "Set team guidance for limit hits"],
 "A usage log: /usage before and after one heavy task and a limit-hit plan.",
 [S("Identity and quota", "`/login` signs in to your Anthropic account and `/logout` signs out. `/usage` shows session cost, plan usage limits and activity stats; on Pro, Max, Team or Enterprise it includes a breakdown of what counts against plan limits; `/cost` and `/stats` are aliases, and `/stats` opens on the Stats tab " + C + ".",
   """
| Command | Does |
|---|---|
| `/login`, `/logout` | Switch identity |
| `/usage` | Cost, plan limits, stats |
| `/cost` | Same as `/usage` |
| `/stats` | `/usage` on the Stats tab |
""", "Alias-hunting", "You search for a separate cost command and miss that `/cost` and `/stats` are the same panel as `/usage`.", "Use `/usage` and its tabs.", "usage and cost is Module 1.4.", "one read-out, three names."),
  S("When you hit a limit", "`/rate-limit-options` shows ways to keep working when a claude.ai limit blocks a request: wait and continue automatically on reset, add usage credits, or upgrade. `/usage-credits` configures credits or requests them from an admin on Team and Enterprise; `/upgrade` opens the upgrade page and does not show on Enterprise plans " + C + ".",
   """
| Option | Command |
|---|---|
| Wait and auto-continue | `/rate-limit-options` |
| Add credits | `/usage-credits` |
| Higher tier | `/upgrade` |
""" + "\n" + NV, "Mid-task-stall", "You start a long run near a limit and it halts halfway with partial changes.", "Read `/usage` first and size the task to the remaining window, or commit a checkpoint before starting.", "limits and windows are Module 1.4.", "size the task to the window."),
  S("Team handling", "Team and Enterprise members without billing access send a request to their admin through `/usage-credits` " + C + ". `/config` cannot turn on `autoContinueAtUsageLimit` by key=value because it needs confirmation in the panel [Claude Code docs, Commands, 2026].",
   """
| Role | Path |
|---|---|
| Individual | Credits via billing settings |
| Member without billing | Request sent to admin |
| Admin | Approves or buys |
""", "Silent-request", "You request credits and keep working without telling the admin, so the request sits unseen.", "Message the admin as well, and define who approves.", "enterprise rollout is Module 10.1.", "requests need a human owner.")],
 [("Which command shows cost and plan limits?", "`/usage`."), ("Which two commands are aliases of `/usage`?", "`/cost` and `/stats`."),
  ("You search for a separate cost command. Name the failure mode by its exact label.", "**Alias-hunting.**"), ("A long run halts at a limit. Name the failure mode.", "**Mid-task-stall.**"),
  ("What options does `/rate-limit-options` list?", "Wait for reset, add usage credits, upgrade."), ("On which plans does `/upgrade` not show?", "Enterprise."),
  ("You request credits and tell nobody. Name the failure mode and fix.", "**Silent-request.** Tell the admin."), ("Which tab does `/stats` open?", "The Stats tab."),
  ("Can `/config` turn on auto-continue at a usage limit?", "No, it needs panel confirmation."), ("What does `/logout` do?", "Signs out of your Anthropic account.")],
 [("Run `/usage` and record the baseline", "Numbers A"), ("Run one heavy task", "Task"), ("Run `/usage` again", "Numbers B"), ("Write what counted", "Note"), ("Open `/rate-limit-options` and read choices", "List"), ("Write the limit-hit plan", "Plan")],
 """
| Metric | Before | After |
|---|---|---|
| Session cost | recorded | recorded |
| Plan window | recorded | recorded |
Plan: commit first, then choose wait or credits.
""", """
| Element | What is wrong |
|---|---|
| No baseline | Cannot show what counted |
| Task started at limit | **Mid-task-stall** |
""", "The artifact passes only if both readings come from /usage and the plan names an owner for approvals.",
 RES(RC, "none found between the sources read; limit sizes change, so read your own `/usage`."),
 RF("quota", "read first, size the task", "why did it stop?", "what did /usage show before I started?"),
 thin="Plan limit sizes are deliberately not stated; they change and were not retrieved."))

# ------------------------------------------------------------ 14.1.10
SPECS.append(G(M, "14.1.10", "Artifacts and design commands: /artifacts, /design, /design-sync, /design-login, /slides, /dataviz",
 "Six commands produce visual outputs, and they depend on versions, accounts and artifact availability more than the core commands do.",
 "state the version and account each command needs and run the ones available to you.",
 "check availability before promising an output to a stakeholder.",
 "/design-sync's first run can take a few hours on a large repo, so it is not a quick command " + C + ".",
 18, "1.5", ["Name what each command produces", "Check availability and versions", "Plan a design-system sync"],
 "A capability sheet: six commands with requirements, plus one produced output.",
 [S("Find and manage artifacts", "`/artifacts` lists artifacts you own or that are shared with you, then attaches one to the session, opens it or copies its link; it needs v2.1.208 or later and attaching with Enter needs v2.1.216, and it is available where artifacts are " + C + ". `/artifact-capabilities` and `/artifact-diagramming` load reference skills; the latter needs v2.1.221 or later " + C + ".",
   """
| Command | Needs |
|---|---|
| `/artifacts` | v2.1.208+; attach needs v2.1.216 |
| `/artifact-capabilities` | Artifact availability |
| `/artifact-diagramming` | v2.1.221+ |
""", "Version-blind", "You tell a teammate to attach an artifact with Enter on a version older than the one that supports it.", "Quote the minimum version next to every command in a team guide.", "artifacts are Module 9.2.", "write the version with the command."),
  S("Design and slides", "`/design [brief]` drafts UI mockups, flows, landing pages or posters as artboards on a canvas published as a Claude Design artifact. `/design-login` authorises design-system access, and `/design-sync [hint]` converts your React design system and uploads it so designs use your components; it needs the Anthropic API. `/slides [brief]` makes a Claude Slides artifact and needs v2.1.265 or later " + C + ".",
   """
| Command | Output | Gate |
|---|---|---|
| `/design a settings screen` | Artboards | Artifact availability |
| `/design-login` | Authorisation | claude.ai account |
| `/design-sync Acme DS` | Uploaded design system | Anthropic API; slow first run |
| `/slides a quarterly review` | Slide artifact | v2.1.265+ |
""", "Sync-on-deadline", "You start `/design-sync` an hour before a review and it is still verifying components.", "Run the first sync well ahead and treat later syncs as incremental.", "prototyping is Module 7.1.", "plan the first sync."),
  S("Charts", "`/dataviz [request]` is a bundled skill giving design guidance for charts: it picks the chart form, assigns colour by role, validates the palette for colour-blind safety and contrast with a bundled script, and uses a brand-neutral placeholder palette you replace " + C + ".",
   """
```text
/dataviz a retention curve by cohort, colour-blind safe
```

| Step | Done by |
|---|---|
| Choose form | Skill |
| Palette validation | Bundled script |
| Brand palette | You replace the placeholder |
""", "Placeholder-palette", "You ship a chart with the placeholder palette and it carries no brand identity.", "Replace the palette values before publishing.", "product communication is Module 7.1.", "swap the palette.")],
 [("Which version does `/artifacts` need?", "v2.1.208 or later."), ("Which version does `/slides` need?", "v2.1.265 or later."),
  ("You cite a command without its minimum version. Name the failure mode by its exact label.", "**Version-blind.**"), ("A sync starts an hour before review. Name the failure mode.", "**Sync-on-deadline.**"),
  ("What does `/design-sync` need?", "Access on the Anthropic API plus design-system authorisation."), ("What does `/dataviz` validate?", "Palette colour-blind safety and contrast."),
  ("A chart ships in placeholder colours. Name the failure mode and fix.", "**Placeholder-palette.** Replace the palette first."), ("Which command authorises design access?", "`/design-login`."),
  ("Which command loads diagramming guidance?", "`/artifact-diagramming`."), ("How long can a first `/design-sync` take?", "A few hours on a large repo.")],
 [("Run `/artifacts` and list one", "Observation"), ("Run `/design` with a one-line brief", "Artboard"), ("Run `/dataviz` for one chart", "Chart"), ("Record each command's gate", "Table"), ("Note which were unavailable", "List"), ("Write the lead-time note for sync", "Line")],
 """
| Command | Gate | Run? |
|---|---|---|
| `/artifacts` | v2.1.208+ | yes |
| `/slides` | v2.1.265+ | no, version too low (stated) |
""", """
| Element | What is wrong |
|---|---|
| No versions listed | **Version-blind** |
| Placeholder colours shipped | **Placeholder-palette** |
""", "The artifact passes only if unavailable commands are stated as unavailable, not assumed to work.",
 RES(RC, "none found between the sources read."),
 RF("visual commands", "gates first, output second", "can I generate this?", "does my version, plan and account allow it?"),
 thin="Thin sub-topic: the docs give one-paragraph descriptions; usage depth lives in Module 9.2."))

# ------------------------------------------------------------ 14.1.11
SPECS.append(G(M, "14.1.11", "Research and API commands: /deep-research, /claude-api",
 "/deep-research is a workflow that fans out web searches into a cited report, and /claude-api loads API reference material in several modes.",
 "run /deep-research on a bounded question and check three citations; run one /claude-api mode.",
 "treat a cited report as leads to verify, not as verified fact.",
 "/deep-research only runs when you invoke it; before v2.1.218 Claude could start it on its own " + C + ".",
 16, "1.5", ["Name both commands and their modes", "Verify a research report", "Choose research versus a single search"],
 "One verified research report and one API-mode run, with a citation check.",
 [S("Deep research as a workflow", "`/deep-research <question>` is a bundled dynamic workflow that fans out web searches, fetches and cross-checks sources and synthesises a cited report; it runs in the background across many subagents " + C + ".",
   """
| Property | Value |
|---|---|
| Type | Workflow, not a plain skill |
| Trigger | You invoke it (since v2.1.218) |
| Output | Cited report |
| Runs | Background, many subagents |
""", "Citation-trust", "You paste the report's claims into a decision memo without opening the sources.", "Open at least three citations and flag any that do not support the claim.", "workflows are Module 6.5.", "citations are leads."),
  S("Claude API reference", "`/claude-api [migrate|upgrade|managed-agents-onboard|prompt-audit|cost-optimize|build-eval|hillclimb|preserved-thinking-migration]` is a bundled skill loading Claude API and Managed Agents reference material for your project's language, and it also activates automatically when relevant " + C + ".",
   """
| Mode | Use |
|---|---|
| `migrate`, `upgrade` | Move code to newer models or API |
| `prompt-audit` | Review prompts |
| `cost-optimize` | Reduce spend |
| `build-eval`, `hillclimb` | Evaluation work |
| `managed-agents-onboard` | Managed Agents |
""", "Mode-guessing", "You invoke `/claude-api` with a mode name that does not exist and get generic output.", "Copy mode names from the argument list above.", "SDK work is Module 8.4; evals are Module 17.3 in spirit and Volume C.", "use listed modes only."),
  S("Choosing the tool", "A single question rarely needs a fan-out workflow; `/deep-research` costs many subagent requests and runs in the background, so use a plain search for lookups.",
   """
| Question type | Tool |
|---|---|
| One fact | Web search |
| Broad, multi-source | `/deep-research` |
| API usage in your code | `/claude-api` |
""", "Fan-out-for-a-fact", "You launch deep research for a one-line fact and burn usage on a workflow.", "Reserve it for questions needing several sources and a synthesis.", "cost control is Module 1.4.", "match the tool to the breadth.")],
 [("Which command produces a cited report from web searches?", "`/deep-research`."), ("Which version stopped Claude starting `/deep-research` itself?", "v2.1.218."),
  ("You paste report claims unchecked. Name the failure mode by its exact label.", "**Citation-trust.**"), ("Name three `/claude-api` modes.", "Any three of migrate, upgrade, prompt-audit, cost-optimize, build-eval, hillclimb."),
  ("You invent a mode name. Name the failure mode.", "**Mode-guessing.**"), ("You run deep research for one fact. Name the failure mode and fix.", "**Fan-out-for-a-fact.** Use a plain search."),
  ("Is `/deep-research` a skill or a workflow?", "A workflow."), ("How many citations should you open at minimum in this guide's pass test?", "Three."),
  ("Does `/claude-api` activate automatically?", "Yes, when relevant."), ("Where does deep research run?", "In the background across many subagents.")],
 [("Pick a bounded question", "Question"), ("Run `/deep-research`", "Report"), ("Open three citations and mark support", "Check table"), ("Run `/claude-api prompt-audit` on one prompt", "Output"), ("Compare against a plain search", "Note"), ("Write the choice rule", "Line")],
 """
| Citation | Supports claim? |
|---|---|
| 1 | Yes |
| 2 | Partly; claim narrowed |
| 3 | No; removed |
""", """
| Element | What is wrong |
|---|---|
| No citation check | **Citation-trust** |
| Used for a one-liner | **Fan-out-for-a-fact** |
""", "The artifact passes only if three citations were opened and the report was edited from what they said.",
 RES(RC, "none found between the sources read."),
 RF("research commands", "breadth decides the tool and citations are leads", "what does the report say?", "which citations did I open?"),
 thin="Thin sub-topic: two commands, little behaviour beyond the description."))

# ------------------------------------------------------------ 14.1.12
SPECS.append(G(M, "14.1.12", "Setup for providers: /setup-bedrock, /setup-vertex, /remote-env, /web-setup",
 "Provider setup commands are hidden until a provider variable is set, so they exist but do not appear until you set the switch.",
 "set the Bedrock switch, see the wizard command appear and explain why it was hidden before.",
 "set the provider switch first, then type the full command name.",
 "/setup-bedrock and /setup-vertex are hidden from the command menu until CLAUDE_CODE_USE_BEDROCK=1 or CLAUDE_CODE_USE_VERTEX=1 is set, and you must type them in full " + C + ".",
 16, "1.5", ["Name the four commands and their gates", "Run a provider wizard", "Document the setup for a team"],
 "A provider-setup note: the variable, the command, what it configured and one verified call.",
 [S("Bedrock and Vertex wizards", "`/setup-bedrock` configures Amazon Bedrock authentication, region and model pins through a wizard and is hidden until `CLAUDE_CODE_USE_BEDROCK=1` is set; `/setup-vertex` does the same for Google Cloud's Agent Platform with `CLAUDE_CODE_USE_VERTEX=1`; both must be typed in full " + C + ".",
   """
```bash
CLAUDE_CODE_USE_BEDROCK=1 claude     # then type /setup-bedrock in full
```

| Command | Hidden until | Configures |
|---|---|---|
| `/setup-bedrock` | `CLAUDE_CODE_USE_BEDROCK=1` | Auth, region, model pins |
| `/setup-vertex` | `CLAUDE_CODE_USE_VERTEX=1` | Auth, project, region, model pins |
""", "Missing-command-panic", "You cannot find `/setup-bedrock` in the menu and conclude your version lacks it.", "Set the provider variable and type the command in full.", "providers are Module 10.2.", "hidden is not absent."),
  S("Cloud sessions from the CLI", "`/remote-env` chooses the default cloud environment for cloud sessions started from the CLI. `/web-setup` connects your GitHub account for cloud sessions using your local `gh` CLI credentials " + C + ".",
   """
| Command | Does |
|---|---|
| `/remote-env` | Pick the default cloud environment |
| `/web-setup` | Connect GitHub via local `gh` credentials |
""", "Credential-reuse-surprise", "You run `/web-setup` without realising it reuses your local `gh` credentials, which may be broader than the cloud task needs.", "Check the `gh` token scope first and use a narrower account if required.", "cloud sessions are Module 6.3; security is Module 11.1.", "know whose credentials it uses."),
  S("Team documentation", "A team guide should state the variable, the command, the model pins chosen and the verification, because the wizard output is per user. Environment variables for providers are listed in the environment variable reference (see Module 14.6).",
   """
| Doc line | Example |
|---|---|
| Switch | `CLAUDE_CODE_USE_BEDROCK=1` |
| Command | `/setup-bedrock` |
| Verification | One request succeeds; `/status` shows provider |
""", "Undocumented-pin", "Model pins chosen in the wizard are never recorded, so a teammate runs a different model.", "Write the pins into the team guide and check `/status`.", "settings are Module 4.1.", "record the pins.")],
 [("Which variable reveals `/setup-bedrock`?", "`CLAUDE_CODE_USE_BEDROCK=1`."), ("Which variable reveals `/setup-vertex`?", "`CLAUDE_CODE_USE_VERTEX=1`."),
  ("You decide your version lacks the command. Name the failure mode by its exact label.", "**Missing-command-panic.**"), ("Which command reuses local gh credentials?", "`/web-setup`."),
  ("A teammate runs a different model than you. Name the failure mode and fix.", "**Undocumented-pin.** Record pins in the guide."), ("Which command picks the default cloud environment?", "`/remote-env`."),
  ("What must you do to run a hidden command?", "Type it in full."), ("You run `/web-setup` with a broad token. Name the failure mode.", "**Credential-reuse-surprise.**"),
  ("What does `/setup-vertex` configure besides auth?", "Project, region and model pins."), ("How do you confirm the provider afterwards?", "`/status` and one successful request.")],
 [("Run claude with the Bedrock variable set", "Observation"), ("Type `/setup-bedrock` and read the first prompt", "Note"), ("Write the doc lines", "Doc"), ("Check `/status`", "Line"), ("Review `gh auth status` scopes", "Note"), ("Write the pin record", "Line")],
 """
| Item | Value |
|---|---|
| Variable | set |
| Command | typed in full |
| Pins recorded | yes |
""", """
| Element | What is wrong |
|---|---|
| Command searched in menu | **Missing-command-panic** |
| Pins not recorded | **Undocumented-pin** |
""", "The artifact passes only if the hidden-until-set behaviour was observed.",
 RES(RC, "none found between the sources read; provider guides were not read in this pass."),
 RF("provider setup", "variable first, then command, then record", "where is the command?", "did I set the switch and record the pins?"),
 thin="Thin sub-topic: wizard internals are not described in the Commands page; read the provider pages before relying on specifics."))

# ------------------------------------------------------------ 14.1.13
SPECS.append(G(M, "14.1.13", "Rare or hidden commands and MCP prompts",
 "The command list you see is filtered by platform, plan, version, policy and hiding rules, and MCP servers add their own prompts as commands.",
 "explain why a command is missing for three different causes and show an MCP prompt appearing.",
 "diagnose a missing command by cause before concluding it does not exist.",
 "after a typo the menu highlights nothing and Enter submits your text as typed, reporting Unknown command " + C + ".",
 16, "1.5", ["List the reasons a command can be missing", "Diagnose a missing command", "Document availability for a team"],
 "A missing-command decision tree tested against three real cases.",
 [S("Why a command is missing", "Claude Code leaves unavailable commands out of the menu; most return Unknown command on submit, a few answer with their own availability message (such as `/schedule` on a Console API key), and some answer with a policy message " + C + ". Examples: `/desktop` only shows on macOS and x64 Windows with a subscription, and `/upgrade` does not show on Enterprise plans.",
   """
| Cause | Example |
|---|---|
| Platform | `/desktop` on Linux |
| Plan | `/upgrade` on Enterprise |
| Version | `/list-agents` before v2.1.224 |
| Policy | Admin disabled |
| Hidden by design | `/heapdump` |
""", "Typo-submit", "You mistype a command, press Enter and send the text as a message instead of running anything.", "After a typo pick the suggestion with Tab or the arrow keys.", "troubleshooting is Part 12.", "Enter after a typo submits text."),
  S("Menu matching", "The menu highlights its top suggestion only when your letters match a command name or alias, from the start or from a word within it, ignoring `:`, `_` and `-`; `/adddir` highlights `/add-dir` and `/new` highlights `/clear` through its alias. These highlighting rules need v2.1.236 or later " + C + ".",
   """
| Typed | Highlights |
|---|---|
| `/adddir` | `/add-dir` |
| `/new` | `/clear` (alias) |
| `/heapd` | Nothing; hidden commands need the full name |
""", "Partial-hidden", "You type part of a hidden command's name and conclude it does not exist.", "Type the full name; partial names never reveal hidden commands.", "command reference is Module 14.1.", "hidden commands need full names."),
  S("MCP prompts and skills as commands", "MCP servers can expose prompts that appear as commands " + C + ". A command is recognised only at the start of the message, and at the terminal prompt up to six skills can be chained in one message " + C + ".",
   """
```text
/skill-a /skill-b do XYZ     # loads both; text after goes to each as arguments
```

| Source | Appears as |
|---|---|
| Built-in | `/name` |
| Skill | `/skill-name` |
| MCP prompt | A command from the server |
""", "Mid-message-command", "You type text first and a command after, and the command is treated as plain text.", "Put the command first on the line.", "MCP is Module 5.5; skills are Module 5.2.", "a command must lead the message.")],
 [("Why does `/heapdump` not appear in the menu?", "It is hidden by design until typed in full."), ("What happens on Enter after a typo?", "Your text is submitted as typed and Unknown command is reported."),
  ("You press Enter after a typo. Name the failure mode by its exact label.", "**Typo-submit.**"), ("You type a partial hidden name and give up. Name the failure mode.", "**Partial-hidden.**"),
  ("Up to how many skills can chain in one message?", "Six."), ("Which version added the highlighting rules?", "v2.1.236."),
  ("You put a command after text. Name the failure mode and fix.", "**Mid-message-command.** Put the command first."), ("Which command does `/new` highlight?", "`/clear`."),
  ("Name three reasons a command can be missing.", "Platform, plan, version, policy or hiding."), ("How do MCP prompts appear?", "As commands.")],
 [("Type `/adddir` and observe the highlight", "Observation"), ("Type `/heapd` and observe", "Observation"), ("Type a typo and press Tab, not Enter", "Observation"), ("Check an MCP prompt appears", "Observation"), ("Build the decision tree", "Tree"), ("Test it on three cases", "Three results")],
 """
| Case | Cause found |
|---|---|
| `/desktop` missing | Platform |
| `/list-agents` unknown | Version |
| `/heapdump` not in menu | Hidden |
""", """
| Element | What is wrong |
|---|---|
| Concludes command does not exist | **Partial-hidden** |
| Enter after a typo | **Typo-submit** |
""", "The artifact passes only if each case has a named cause tested, not guessed.",
 RES(RC, "none found between the sources read."),
 RF("command availability", "a missing command has a cause", "does this command exist?", "which of platform, plan, version, policy or hiding explains it?")))

if __name__ == "__main__":
    run(SPECS)
