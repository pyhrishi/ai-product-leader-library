import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen import write
from specs_12 import T

M = "b-8-1"
SPECS = []
D = "Agent SDK docs"

# ------------------------------------------------------------------ 8.1.1
SPECS.append(dict(
 mod=M, id="8.1.1", title="What the Agent SDK is and is not", short="What the Agent SDK is and is not",
 thesis="The Agent SDK is Claude Code's agent loop, tools and context management packaged as a Python and TypeScript library, so you embed an agent in a process you operate instead of writing the loop yourself.",
 prove="given four build scenarios, name the right tool (Agent SDK, CLI, Client SDK or Managed Agents) and say in one sentence what you give up by choosing it.",
 discipline="decide who runs the loop and where it runs before you write any code.",
 counter="the SDK is not a thin API wrapper: it runs the Claude Code binary, so your Python or TypeScript process is a controller around a separate agent process [Agent SDK docs, Overview, 2026].",
 read_min=20, prove_h="2", depth=["Place the SDK against the CLI, Client SDK and Managed Agents", "Explain what runs where and what you inherit from Claude Code", "Defend a boundary: what the SDK will and will not do for a product"],
 deliverable="A one-page comparison matrix for the four options, filled in for a real product you could build, with the deciding row circled.",
 sections=[
 dict(title="The four options differ by who runs the loop", framing="The overview page separates the Agent SDK, the Claude Code CLI, the Client SDK and Managed Agents by who runs the agent, what comes built in and how you reach it [Agent SDK docs, Overview, 2026].",
  body=T("""
| You want to | Use | What you get |
|---|---|---|
| Embed Claude Code's agent in your own Python or TypeScript app, in a process you operate | Agent SDK | A library that runs the Claude Code binary: built-in tools, permissions, sessions, hooks |
| Work interactively or run one-off tasks from a terminal | Claude Code CLI | The terminal interface |
| Call the Claude API directly | Client SDK | Direct API access; you write the tool loop, or use the beta tool runner |
| Have Anthropic host the agent | Managed Agents | A hosted harness with sessions in an Anthropic-managed cloud sandbox or a self-hosted sandbox |

[Agent SDK docs, Overview, 2026]. The loop in the SDK is the same execution loop that powers Claude Code: Claude evaluates the prompt, calls tools, receives results and repeats until the task is complete [Agent SDK docs, How the agent loop works, 2026].
"""),
  fm=[("Four-way blur", "You say 'we use the SDK' when you mean the Client SDK, the CLI or Managed Agents, and the team plans cost, hosting and tool work for the wrong product.", "Write the row from the table above that matches your build, with the owner of the loop named, before the design review.")],
  xr="the loop itself is Module 8.2; hosting is Module 8.7; the Claude Code loop it descends from is Module 1.2.", one="the SDK means you run the loop's host process; the Client SDK means you write the loop."),
 dict(title="What is inside the box", framing="The SDK lists eight capabilities inherited from Claude Code: built-in tools, hooks, subagents, MCP, permissions, sessions, skills/commands/memory and plugins [Agent SDK docs, Overview, 2026]. Both language SDKs bundle a native Claude Code binary, so most installs need no separate Claude Code install [Agent SDK docs, How the agent loop works, 2026].",
  body=T("""
```
your process (Python / TypeScript)
   query(prompt, options) ──►  Claude Code binary (bundled)
        ▲                          │ loop: evaluate → tools → results → repeat
        └── async stream of messages ◄┘
```

| Capability | You configure it with | Module |
|---|---|---|
| Built-in tools (Read, Edit, Bash, Glob, Grep, WebSearch, WebFetch) | allowed and disallowed tool lists | 8.3 |
| Hooks | callbacks at lifecycle points | 8.6 |
| Subagents | agent definitions | 8.3 |
| Sessions | resume, continue, fork | 8.5 |
| Skills, commands, memory | setting sources | 8.2 |

Tool names are listed in [Agent SDK docs, How the agent loop works, 2026].
"""),
  fm=[("Library illusion", "You treat query() as an in-process function call, then are surprised by a subprocess to deploy, a binary to ship and a working directory to manage.", "Draw the process boundary on your architecture diagram: your code, the bundled binary, the model API.")],
  xr="subprocess architecture is Module 8.7; options are Module 8.2.", one="the SDK is a controller for a separate agent process."),
 dict(title="What it is not: the other approaches and their boundaries", framing="Three neighbours are easy to confuse with the SDK: print mode, the Client SDK, and a hosted agent. Print mode is the same engine reached through the CLI: the headless page says it is available 'as a CLI for scripts and CI/CD, or as Python and TypeScript packages' [Claude Code docs, Run Claude Code programmatically, 2026]. For other languages, run the CLI as a subprocess with -p and --output-format json [Agent SDK docs, Overview, 2026].",
  body=T("""
| Boundary | Statement | Source |
|---|---|---|
| Not the raw API | With the Client SDK you write the tool loop yourself | Overview |
| Not a login product | Anthropic does not allow third parties to offer claude.ai login or rate limits for their products unless previously approved; use API keys | Overview, Quickstart |
| Not Claude Code branded | Do not name your product 'Claude Code' or 'Claude Code Agent'; 'Claude Agent' and '{YourAgentName} Powered by Claude' are allowed | Overview |
| Not exempt from terms | Governed by Anthropic's Commercial Terms of Service, including for your end users | Overview |
| Not a default coding prompt | The SDK stopped using Claude Code's system prompt by default in v0.1.0; opt in with the claude_code preset | Migration guide |

All rows: [Agent SDK docs, Overview and Migration guide, 2026].
"""),
  fm=[("Borrowed login", "You plan to let customers sign in with their claude.ai subscription inside your SDK product, and the plan collides with the stated policy.", "Plan for API-key or cloud-provider authentication from the first sketch, and treat anything else as needing prior approval from Anthropic.")],
  xr="authentication setup is Module 8.1.2; system prompts are Module 8.2.", one="the boundaries are policy and process, not only features."),
 dict(title="Reading the stream: what your code receives", framing="The SDK returns an async iterator of messages. Five core types cover the loop: SystemMessage, AssistantMessage, UserMessage, StreamEvent (only with partial messages on) and ResultMessage [Agent SDK docs, How the agent loop works, 2026].",
  body=T("""
```python
async for message in query(prompt="Summarize this project"):
    if isinstance(message, ResultMessage):
        if message.subtype == "success":
            print(message.result)
        else:
            print("Stopped:", message.subtype)
```
[Agent SDK docs, How the agent loop works, 2026]

| Result subtype | Meaning |
|---|---|
| success | Finished normally; `result` available |
| error_max_turns | Hit the turn limit |
| error_max_budget_usd | Hit the budget limit |
| error_during_execution | API failure or cancelled request |
| error_max_structured_output_retries | No valid structured output within the retry limit |

[Agent SDK docs, How the agent loop works, 2026]. The result field exists only on success.
"""),
  fm=[("Result-blind loop", "You print every message and never branch on the ResultMessage subtype, so a turn-limit stop looks like a success to downstream code.", "Branch on subtype before reading result, and treat each error subtype as its own path.")],
  xr="turns, budgets and limits are Module 8.2 and Module 8.6; structured output is Module 8.4.", one="the end of the stream is a ResultMessage, and its subtype is the truth."),
 ],
 retrieval=[
  ("Which of the four options means you write the tool loop yourself?", "The Client SDK (optionally the beta tool runner)."),
  ("A team calls the Client SDK 'the SDK' and plans no process to deploy. Name the failure mode by its exact label.", "**Four-way blur.**"),
  ("What does the SDK bundle with each install, and what follows from it?", "A native Claude Code binary; so most installs need no separate Claude Code install, and the SDK runs as a controller around a separate process."),
  ("A developer expects query() to run in-process and has no binary or working directory plan. Name the failure mode.", "**Library illusion.**"),
  ("How many core message types does the loop produce, and which one marks the end?", "Five; ResultMessage marks the end."),
  ("Which result subtype means the turn limit was hit, and is `result` available?", "error_max_turns; no, `result` exists only on success."),
  ("Your plan lets customers log in with claude.ai subscriptions. Name the failure mode and the fix.", "**Borrowed login.** Plan for API-key or cloud-provider authentication; anything else needs prior approval."),
  ("Which product names are not permitted for an SDK-based product?", "'Claude Code' and 'Claude Code Agent'."),
  ("Your pipeline prints all messages and treats the stream ending as success. Name the failure mode by its exact label.", "**Result-blind loop.**"),
  ("What do you use to reach the same agent loop from a language other than Python or TypeScript?", "Run the CLI as a subprocess with -p and --output-format json."),
 ],
 steps=[("Fill the four-option table for a product you could build", "A 4-row matrix"), ("Circle the row that decides it and write the owner of the loop", "One sentence"),
        ("Draw the process boundary: your code, binary, model API", "A diagram"), ("List the five message types and where each appears", "A 5-row list"),
        ("List the five result subtypes and a handler for each", "A 5-row table"), ("Write the three policy boundaries that apply to your product", "A 3-line note")],
 pass_md=T("""
| Row | Content |
|---|---|
| Product | Nightly PR-review bot run in our CI |
| Option chosen | Agent SDK (we operate the process; loop and tools are inherited) |
| Rejected | Client SDK: we would rebuild file tools and permissions |
| Boundary | API-key auth only; product is named 'ReviewBot, powered by Claude' |
| Stream handling | Branch on all five result subtypes; budget set |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| 'We use the SDK' with no owner of the loop | **Four-way blur** |
| Auth listed as 'user logs in with Claude account' | **Borrowed login** |
| Handler prints the last message | **Result-blind loop** |
"""),
 verdict="The artifact passes only if the owner of the loop is named, a rejected alternative has a reason, and every result subtype has a handler.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Agent SDK overview | Four-way comparison, capabilities, branding | Current |
| Anthropic | How the agent loop works | Message types, result subtypes | Current |
| Anthropic | Run Claude Code programmatically | CLI route for other languages | Current |
""") + "\n\n*Disagreement named:* none found among the docs read; the headless page frames the CLI as one way to use the Agent SDK, while the overview lists the CLI as a separate row. Treat 'CLI' as the same engine reached through a different surface.",
 reframe="This is the craft of choosing the right layer: **the SDK gives you the loop, the tools and the process, and leaves product, hosting and policy to you.** The engineer who understands this stops asking what the SDK can do and asks who runs the loop.",
))

# ------------------------------------------------------------------ 8.1.2
SPECS.append(dict(
 mod=M, id="8.1.2", title="Quickstart and migration", short="Quickstart and migration",
 thesis="A working first agent needs four things in the right order: the package, an API key in the process environment, an options object that names tools and a permission mode, and a loop that handles the final result.",
 prove="from an empty folder, install the SDK, run the bug-fixing agent end to end, and then convert a legacy claude-code-sdk import to the new names without breaking behaviour.",
 discipline="pin every option the old defaults used to supply, then migrate.",
 counter="the migration is a rename plus a behaviour change: after v0.1.0 the SDK no longer uses Claude Code's system prompt by default, so a straight rename silently changes how your agent behaves [Agent SDK docs, Migration guide, 2026].",
 read_min=20, prove_h="2", depth=["Install, authenticate and run the quickstart agent", "Migrate imports and restore old behaviour explicitly", "Diagnose first-run failures by cause (key, binary, settings)"],
 deliverable="A repository with a runnable agent.py or agent.ts, a README of the exact install and run commands, and a migration diff of a legacy script.",
 sections=[
 dict(title="Install and authenticate", framing="Prerequisites are Node.js 18+ or Python 3.10+ and an Anthropic account [Agent SDK docs, Quickstart, 2026]. The package is installed per language and the key is read from the environment of the process that runs your agent.",
  body=T("""
| Language | Install |
|---|---|
| TypeScript | `npm install @anthropic-ai/claude-agent-sdk` (plus tsx to run files) |
| Python (uv) | `uv add claude-agent-sdk` |
| Python (pip) | `pip install claude-agent-sdk` in a virtual environment |

[Agent SDK docs, Quickstart, 2026]

```bash
export ANTHROPIC_API_KEY=your-api-key
```
The SDK does not load .env files automatically, so load the file yourself, for example with dotenv [Agent SDK docs, Quickstart, 2026]. Provider switches: `CLAUDE_CODE_USE_BEDROCK=1`, `CLAUDE_CODE_USE_VERTEX=1`, `CLAUDE_CODE_USE_FOUNDRY=1`, and `CLAUDE_CODE_USE_ANTHROPIC_AWS=1` with `ANTHROPIC_AWS_WORKSPACE_ID` [Agent SDK docs, Quickstart, 2026].
"""),
  fm=[("Dotenv assumption", "You keep the key in a .env file, run the agent, and get 'Not logged in' or 'Invalid API key' because the SDK never read the file.", "Export the variable in the shell that runs the agent, or load the .env explicitly before calling query().")],
  xr="auth and secrets for production are Module 8.7.4; Claude Code setup is Module 1.1.", one="the key must be in the environment of the process that starts the agent."),
 dict(title="The first agent", framing="The quickstart agent reviews utils.py for crash bugs and fixes them using three options: a prompt, allowed tools and a permission mode. `allowed_tools` auto-approves the listed tools and `permission_mode='acceptEdits'` auto-approves file edits [Agent SDK docs, Quickstart, 2026].",
  body=T("""
```python
async for message in query(
    prompt="Review utils.py for bugs that would cause crashes. Fix any issues you find.",
    options=ClaudeAgentOptions(
        allowed_tools=["Read", "Edit", "Glob"],
        permission_mode="acceptEdits",
    ),
):
    ...
```
[Agent SDK docs, Quickstart, 2026]

| Tools allowed | What the agent can do |
|---|---|
| Read, Glob, Grep | Read-only analysis |
| Read, Edit, Glob | Analyze and modify code |
| Read, Edit, Bash, Glob, Grep | Full automation |

[Agent SDK docs, Quickstart, 2026]. A successful run ends with `Done: success`. The seeded file has two bugs: division by zero on an empty list, and a TypeError on a None user.
"""),
  fm=[("Prompt-only safety", "You rely on the prompt ('only edit utils.py') instead of tool and permission options, and the agent edits other files because Edit was allowed everywhere.", "Narrow capability with the tools list and permission rules, and treat the prompt as guidance only.")],
  xr="permissions are Module 8.6.1; the options object is Module 8.2.2.", one="the options object, not the prompt, bounds what the agent can do."),
 dict(title="Migrating from the Claude Code SDK", framing="The Claude Code SDK was renamed the Claude Agent SDK [Agent SDK docs, Migration guide, 2026]. The mapping is mechanical; the behaviour change is not.",
  body=T("""
| Aspect | Old | New |
|---|---|---|
| TS/JS package | `@anthropic-ai/claude-code` | `@anthropic-ai/claude-agent-sdk` |
| Python package | `claude-code-sdk` | `claude-agent-sdk` |
| Python options type | `ClaudeCodeOptions` | `ClaudeAgentOptions` |
| Default system prompt | Claude Code's | Minimal; opt in with `{"type": "preset", "preset": "claude_code"}` |

[Agent SDK docs, Migration guide, 2026]. Settings sources: omitting `settingSources` on query() loads user, project and local settings, matching the CLI; pass `settingSources: []` or `setting_sources=[]` to run isolated. Python SDK 0.1.59 and earlier treated an empty list like omitting the option, so upgrade before relying on it [Agent SDK docs, Migration guide, 2026].

```bash
npm uninstall @anthropic-ai/claude-code
npm install @anthropic-ai/claude-agent-sdk
```
"""),
  fm=[("Rename-only migration", "You change the package and import names, the code runs, and the agent now answers in a different style and skips conventions the old Claude Code prompt supplied.", "Request the claude_code preset explicitly, or write a custom system prompt, and re-run your acceptance tasks.")],
  xr="system prompts are Module 8.2.3; settings sources are Module 8.2.4.", one="a green import is not a finished migration."),
 dict(title="First-run failures by cause", framing="Most first-run failures come from three places: authentication, a missing binary, and unexpected settings. The quickstart names each cause.",
  body=T("""
| Symptom | Cause | Fix | Source |
|---|---|---|---|
| 'Not logged in' or 'Invalid API key' | Key not in process environment | Export ANTHROPIC_API_KEY where the agent runs | Quickstart |
| No binary after pip install on ARM64 Windows | Source distribution installed, no platform wheel | Install Claude Code natively; SDK finds it on PATH | Quickstart |
| No binary after `npm ci --omit=optional` | Binary ships as an optional dependency | Reinstall without skipping optionals, or set `pathToClaudeCodeExecutable` | Quickstart |
| Isolation test still loads local config | Python <= 0.1.59 with empty list | Upgrade, then pass setting_sources=[] | Migration guide |

All rows: [Agent SDK docs, Quickstart and Migration guide, 2026]. The docs also point to a Troubleshooting page for CLI start failures.
"""),
  fm=[("Optional-dependency strip", "A CI image installs with optional dependencies disabled and the TypeScript SDK cannot find its binary, which looks like an SDK bug.", "Keep optional dependencies, or install Claude Code natively and pass pathToClaudeCodeExecutable.")],
  xr="container builds are Module 8.7.2; Claude Code installation is Module 1.1.", one="classify the failure (key, binary, settings) before changing code."),
 ],
 retrieval=[
  ("What are the minimum Node.js and Python versions in the quickstart?", "Node.js 18+ and Python 3.10+."),
  ("The agent says 'Invalid API key' though a .env file has the key. Name the failure mode by its exact label.", "**Dotenv assumption.**"),
  ("Give the old and new Python package names.", "claude-code-sdk becomes claude-agent-sdk."),
  ("After a package rename the agent's style changes. Name the failure mode and the fix.", "**Rename-only migration.** Request the claude_code preset or write a custom prompt, then re-run acceptance tasks."),
  ("What does omitting settingSources do on query()?", "It loads user, project and local settings, matching the CLI."),
  ("Which Python SDK versions treated an empty setting_sources list like omitting it?", "0.1.59 and earlier."),
  ("An agent edits unrelated files though the prompt said not to. Name the failure mode.", "**Prompt-only safety.**"),
  ("A CI install with `npm ci --omit=optional` has no binary. Name the failure mode and fix.", "**Optional-dependency strip.** Reinstall with optionals or set pathToClaudeCodeExecutable."),
  ("What environment variable selects Amazon Bedrock?", "CLAUDE_CODE_USE_BEDROCK=1."),
 ],
 steps=[("Create an empty folder and install the SDK for your language", "Lockfile and package"), ("Export the key and run a one-line agent", "A successful first run"),
        ("Create utils.py with the two bugs and run the quickstart agent", "Fixed file and `Done: success`"), ("Rewrite a legacy script's imports with the new names", "A diff"),
        ("Add the claude_code preset and compare output with and without it", "Two transcripts"), ("Test setting_sources empty vs omitted and record what loads", "A 2-row observation")],
 pass_md=T("""
| Item | Evidence |
|---|---|
| Install | npm shows `added N packages`; lockfile committed |
| First run | Transcript ends `Done: success`; utils.py guards empty list and None |
| Migration diff | Imports renamed; preset requested; ClaudeAgentOptions used |
| Isolation | Output shows project CLAUDE.md loaded when omitted, not when empty |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Key only in .env, no loader | **Dotenv assumption** |
| Diff only renames imports | **Rename-only migration** |
| CI installs with --omit=optional | **Optional-dependency strip** |
"""),
 verdict="The artifact passes only if the run transcript is present, the migration diff states the system prompt decision, and the isolation test records what actually loaded.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Agent SDK quickstart | Install, key, first agent, provider env vars | Current |
| Anthropic | Migrate to Claude Agent SDK | Renames, prompt and settings behaviour | Current |
| npm registry [secondary: npm view output] | @anthropic-ai/claude-agent-sdk | Package exists; version string was 0.3.331 when checked | Changes often |
""") + "\n\n*Disagreement named:* the migration guide says the settings-sources default was changed in v0.1.0 and then reverted, which conflicts with older write-ups that say the SDK loads no filesystem settings by default; follow the current guide and test it.",
 reframe="This is the craft of the first hour: **install, key, options, result.** The engineer who understands this treats a migration as a behaviour change with a test, not a find-and-replace.",
))

# ------------------------------------------------------------------ 8.1.3
SPECS.append(dict(
 mod=M, id="8.1.3", title="When to choose the SDK", short="When to choose the SDK",
 thesis="Choose the Agent SDK when you want Claude Code's built-in tools, context management, sessions, permissions and hooks inside a process you operate, and choose something else when you do not need that harness or do not want to run it.",
 prove="produce a decision record for one real workload that names the chosen option, two rejected options with reasons, and the cost you accept.",
 discipline="count what you would have to rebuild before you count what you would save.",
 counter="the best reason to pick the SDK is what you refuse to write, and the best reason to refuse it is also what you refuse to run: the SDK means you operate a process and a binary [Agent SDK docs, Overview, 2026].",
 read_min=19, prove_h="1.5", depth=["Apply the decision table to a workload", "Quantify what you would rebuild with the Client SDK", "Recognise when the CLI or Managed Agents wins"],
 deliverable="A decision record (one page) for a workload of your choice with chosen option, two rejected options, the hosting owner and the exit criterion.",
 sections=[
 dict(title="What the harness gives you", framing="The SDK's value is the harness it inherits: tools, loop, context management, permissions, sessions and hooks [Agent SDK docs, Overview, 2026]. With the Client SDK, you write the tool loop yourself, or use the beta tool runner [Agent SDK docs, Overview, 2026].",
  body=T("""
| Concern | Agent SDK | Client SDK |
|---|---|---|
| Tool loop | Provided | You write it (or tool runner) |
| File, shell, search tools | Built in | You implement |
| Context compaction | Automatic; PreCompact hook | You build |
| Permissions | Modes, allow/deny rules, callback | You build |
| Sessions | Resume, continue, fork | You build |
| Hooks | Lifecycle callbacks | You build |

Compaction and tool lists: [Agent SDK docs, How the agent loop works, 2026]. Rows for sessions and hooks: [Agent SDK docs, Overview, 2026]. 'You build' reflects the docs' description that you write the loop; it is not a line-by-line comparison.
"""),
  fm=[("Rebuild blindness", "You choose the Client SDK for control and then spend weeks recreating file tools, permission prompts and compaction that the SDK already had.", "List the six concerns above, estimate each, and pick the SDK unless the list is empty.")],
  xr="the loop internals are Module 8.2.1; Part 4.3 of the AI curriculum covers tool-loop design for the Client SDK route.", one="the SDK is chosen by the code you will not write."),
 dict(title="When the SDK is the wrong layer", framing="Three situations point away: the work is interactive and personal, you do not want to operate a process, or you only need one model call.",
  body=T("""
| Situation | Better fit | Reason |
|---|---|---|
| Interactive terminal work | CLI | Built for daily interactive use [Overview] |
| A single prompt with schema output from a shell script | `claude -p` with --json-schema | Same engine, no code [Headless page] |
| No process to operate; Anthropic should host | Managed Agents | Hosted harness [Overview] |
| One model call, no tools | Client SDK | No loop needed |
| A language other than Python or TypeScript | CLI as subprocess with -p | Documented route [Overview] |

Sources: [Agent SDK docs, Overview, 2026] and [Claude Code docs, Run Claude Code programmatically, 2026]. The no-tools row is a judgement, not a quote.
"""),
  fm=[("Harness for a prompt", "You stand up a subprocess-driven agent service for a task that is one model call with a schema.", "Use the Client SDK or `claude -p --json-schema` for single-shot extraction, and reserve the SDK for multi-step tool use.")],
  xr="Managed Agents is outside this volume; hosting trade-offs are Module 8.7.", one="if there is no loop, there is no reason to buy the harness."),
 dict(title="Operating cost of choosing the SDK", framing="Choosing the SDK means you operate a process. The agent loop page says that the loop can run long on open-ended prompts and that a budget is a good default for production agents [Agent SDK docs, How the agent loop works, 2026].",
  body=T("""
| Operating item | What to decide | Source |
|---|---|---|
| Limits | `max_turns` and `max_budget_usd`; default no limit | Agent loop |
| Auth | API key or cloud provider; not claude.ai login | Quickstart |
| Isolation | `settingSources: []` for CI, multi-tenant, deployed apps | Migration guide |
| Permissions | A mode, rules, or a callback | Agent loop |
| Billing | Costs are client-side estimates; reconcile with the console | Headless page |

Sources: [Agent SDK docs, How the agent loop works, 2026]; [Agent SDK docs, Migration guide, 2026]; [Claude Code docs, Run Claude Code programmatically, 2026].
"""),
  fm=[("Unbounded launch", "You deploy an open-ended agent with no turn or budget limit and a surprise bill is your first signal.", "Set max turns and a max budget in the launch checklist, and branch on both error subtypes.")],
  xr="cost tracking is Module 8.6.3; failure handling is Module 8.7.5.", one="choose the SDK with the limits already written."),
 dict(title="The decision rule in practice", framing="A decision record forces the reasoning into one page. This guide's rule is: pick the highest layer that does not hide something you must control.",
  body=T("""
```text
Workload: nightly dependency-update PRs
Loop needs files, shell, tests, retries        -> harness wanted
We can operate a container per run             -> SDK OK
Verifiable by `npm test`                       -> good agent candidate
Rejected: Client SDK (rebuild tools), Managed Agents (data must stay on our infra)
Accepted cost: we own the container and the key
Exit criterion: if pass rate < target after 4 weeks, revisit
```
Module 8.8.3 states the product rule: repetitive and verifiable work with a good check is a strong candidate. The target pass rate is yours to set; no benchmark is claimed here.
"""),
  fm=[("Unrecorded choice", "The reason for choosing the SDK lives in one person's head, and a later owner moves the work to a different layer without knowing what was traded.", "Write the decision record with rejected options and the exit criterion, and keep it next to the code.")],
  xr="product fit is Module 8.8; evals are Module 8.6.5.", one="write the rejected options down."),
 ],
 retrieval=[
  ("Name three concerns the SDK provides that you would build with the Client SDK.", "Any three of: tool loop, file/shell/search tools, context compaction, permissions, sessions, hooks."),
  ("A team chooses the Client SDK and rebuilds file tools and permission prompts. Name the failure mode by its exact label.", "**Rebuild blindness.**"),
  ("What does the docs' agent loop page recommend as a good default for production agents?", "Setting a budget."),
  ("What is the default for max_turns and max_budget_usd?", "No limit for both."),
  ("A single-shot extraction is built as an SDK service. Name the failure mode.", "**Harness for a prompt.**"),
  ("What would you use from a language other than Python or TypeScript?", "The CLI as a subprocess with -p and --output-format json."),
  ("An open-ended agent launches with no limits. Name the failure mode and the fix.", "**Unbounded launch.** Set turn and budget limits and branch on both error subtypes."),
  ("Why should deployed or multi-tenant SDK apps pass an empty settings sources list?", "So local customizations do not leak in."),
  ("The reason for choosing the SDK is lost when its author leaves. Name the failure mode by its exact label.", "**Unrecorded choice.**"),
  ("What is the fixed cap on piped stdin for claude -p?", "10MB."),
 ],
 steps=[("Describe one real workload in three lines", "A workload brief"), ("Fill the six-concern rebuild table with an estimate for each", "A 6-row table"),
        ("Check each 'wrong layer' situation against the workload", "5 yes/no answers"), ("List limits, auth and isolation decisions", "A launch checklist"),
        ("Write the decision record with two rejected options", "A one-page record"), ("Set an exit criterion and a review date", "A dated line")],
 pass_md=T("""
| Field | Content |
|---|---|
| Chosen | Agent SDK, container per run |
| Rejected 1 | Client SDK: rebuild six concerns, ~weeks of work (estimate) |
| Rejected 2 | CLI in cron: no callbacks for approvals |
| Limits | max_turns 30, budget set, error subtypes handled |
| Exit | Review after four weeks |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| 'Use the SDK, it is newest' | No rejected options: **Unrecorded choice** |
| No limits listed | **Unbounded launch** |
"""),
 verdict="The record passes only if two alternatives are rejected with reasons, limits are specified and an exit criterion exists.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Agent SDK overview | Option table | Current |
| Anthropic | How the agent loop works | Limits, budgets, context | Current |
| Anthropic | Run Claude Code programmatically | CLI route, 10MB stdin cap | Current |
""") + "\n\n*Disagreement named:* the headless page says --bare is recommended for scripted and SDK calls and will become the default for -p; the SDK docs show settings loading by default. Both can be true because they describe different surfaces; verify the one you run.",
 reframe="This is the craft of the choice: **name what you refuse to build and what you agree to operate.** The engineer who understands this writes the decision record before the first query() call.",
))

# ------------------------------------------------------------------ 8.1.4
SPECS.append(dict(
 mod=M, id="8.1.4", title="Examples: demos and cookbook recipes", short="Examples: demos and cookbook recipes",
 thesis="The fastest route from quickstart to a real agent is to run the nearest official example, then change one thing at a time against a check you wrote first.",
 prove="run one official example locally, record what it needs, change exactly one option, and write down what changed and how you measured it.",
 discipline="treat an example as a hypothesis about your use case, not as production code.",
 counter="demos are for local development, not for deployment: the docs call the demo repository 'demos for local development', so copy their shape, not their security posture [Agent SDK docs, Examples, 2026].",
 read_min=17, prove_h="2", depth=["Find the right official example for a build", "Run it, instrument it and change one variable", "Convert an example into a tested internal prototype"],
 deliverable="A lab notebook: example chosen, setup steps, one-change experiment, and a list of production gaps found.",
 thin="The demos repository itself could not be fetched in this session (host not on the allowlist), so only the descriptions on the official Examples page are used; contents of individual demos are not described. Cookbook recipe contents beyond titles were not read.",
 sections=[
 dict(title="Where official examples live", framing="The Examples page routes to four sources: the quickstart, a Hello World project, demo applications in the claude-agent-sdk-demos repository and Python recipes in the Claude Cookbook [Agent SDK docs, Examples, 2026].",
  body=T("""
| Source | What it is | Use it when |
|---|---|---|
| Agent SDK quickstart | First working agent, with setup steps | You have built nothing yet |
| hello-world (demos repo) | Minimal TypeScript project to clone | You want repo code to start from |
| claude-agent-sdk-demos | Demos 'from an email client to a multi-agent research system' | A demo's shape matches your product |
| Claude Cookbook, Agent SDK series | Python notebooks from a simple research agent to multi-agent systems; each builds on the previous | You learn by sequence |
| Claude for commerce reference implementation | Shopping or merchant agent with the Python SDK | You build a commerce agent |

All rows: [Agent SDK docs, Examples, 2026].
"""),
  fm=[("Example hoarding", "You clone four demos, run none to completion, and cannot say which one fits.", "Pick one by the shape of your product, run it, and write what it needs before cloning the next.")],
  xr="options are Module 8.2; product shapes are Module 8.8.", one="choose by product shape, then finish one."),
 dict(title="The cookbook path", framing="The Cookbook's Agent SDK series is a sequence of Python notebooks. The Examples page says to start with the one-liner research agent and work forward [Agent SDK docs, Examples, 2026]. The migration page also links a recipe that maps OpenAI Agents SDK primitives onto the Claude Agent SDK through one worked example [Agent SDK docs, Migration guide, 2026].",
  body=T("""
| Recipe (as named in docs) | Role |
|---|---|
| claude-agent-sdk-00-the-one-liner-research-agent | Start here |
| claude-agent-sdk-04-migrating-from-openai-agents-sdk | Migration from another framework |
| Series as a whole | Simple research agent to multi-agent systems |

[Agent SDK docs, Examples and Migration guide, 2026]. Names of recipes 01 to 03 and 05 onward were not retrieved; do not assume them.
"""),
  fm=[("Skip-ahead recipe", "You open the multi-agent recipe first, copy its structure, and cannot explain which parts are needed for your simple task.", "Work the series in order until your task's complexity is reached, then stop.")],
  xr="subagents are Module 8.3.5; migration is Module 8.1.2.", one="each recipe adds one idea; take them in order."),
 dict(title="Running an example as an experiment", framing="Treat the example as a hypothesis. Run it unchanged, record the result, change one option, and compare. The result message gives you cost, usage, number of turns and a session id for each run [Agent SDK docs, How the agent loop works, 2026].",
  body=T("""
```text
Run A: unchanged         turns=?  cost=?  subtype=?
Run B: effort="low"      turns=?  cost=?  subtype=?
Run C: max_turns=5       turns=?  cost=?  subtype=?
```

| Variable you can change | Option | Effect named in docs |
|---|---|---|
| Reasoning depth | effort (low to max) | Fewer tokens per turn at low [Agent loop] |
| Loop length | max_turns | Stops tool-use round trips; error_max_turns [Agent loop] |
| Spend | max_budget_usd | error_max_budget_usd [Agent loop] |
| Tools | allowed_tools | Auto-approves listed tools [Agent loop] |

Sources: [Agent SDK docs, How the agent loop works, 2026]. Costs are estimates: the headless page calls them client-side estimates that can differ from the bill [Claude Code docs, Run Claude Code programmatically, 2026].
"""),
  fm=[("Multi-change run", "You change effort, tools and prompt together, the result improves, and you cannot say which change caused it.", "Change one variable per run and keep the runs in a table.")],
  xr="options are Module 8.2.2; cost tracking is Module 8.6.3; evals are Module 8.6.5.", one="one change per run, recorded."),
 dict(title="From demo to prototype: the gap list", framing="A demo skips what production needs. The gap list is the work between the two. Items come from the docs: permissions, limits, isolation and hosting are separate pages because they are separate jobs.",
  body=T("""
| Gap | Question to ask | Module |
|---|---|---|
| Permissions | What can it run unattended? | 8.6.1 |
| Limits | What stops a runaway loop? | 8.6.3 |
| Isolation | What does it read from the host? | 8.7.3 |
| Secrets | Where do keys live? | 8.7.4 |
| Check | What proves a run was right? | 8.6.5 |
| Failure | What happens on crash? | 8.7.5 |

The mapping of gaps to modules is this curriculum's own structure, not a docs list.
"""),
  fm=[("Demo-to-prod copy", "You deploy a demo with broad permissions and no budget because it worked on your laptop.", "Fill the gap list before the first deployment and treat any unanswered row as a blocker.")],
  xr="security is Module 8.7; evals are Module 8.6.", one="the gap list is the plan."),
 ],
 retrieval=[
  ("What repository holds the demo applications?", "claude-agent-sdk-demos."),
  ("What do the docs call the demos' intended purpose?", "Demos for local development."),
  ("You clone four demos and finish none. Name the failure mode by its exact label.", "**Example hoarding.**"),
  ("Which recipe does the Examples page say to start with?", "The one-liner research agent."),
  ("You start from the multi-agent recipe for a simple task. Name the failure mode.", "**Skip-ahead recipe.**"),
  ("Why change one variable per run?", "So the effect can be attributed; changing several is the Multi-change run failure mode."),
  ("You change effort, tools and prompt in one run. Name the failure mode by its exact label.", "**Multi-change run.**"),
  ("Which result fields give per-run cost, turns and session?", "total_cost_usd, num_turns, session_id on the ResultMessage."),
  ("A demo is deployed with no budget. Name the failure mode and the fix.", "**Demo-to-prod copy.** Fill the gap list first and treat unanswered rows as blockers."),
 ],
 steps=[("Pick one example by product shape and write why", "A choice note"), ("Run it unchanged three times and record turns, cost and subtype", "A 3-row table"),
        ("Change exactly one option and run three more times", "A second table"), ("Write what the change did, with numbers", "A paragraph"),
        ("Fill the six-row gap list for the example", "A gap list"), ("Decide: adopt, adapt or discard", "A decision line")],
 pass_md=T("""
| Run | Change | Turns | Cost | Subtype |
|---|---|---|---|---|
| A1-A3 | none | recorded | recorded | success |
| B1-B3 | effort low | recorded | recorded | success |

Gap list: six rows, two marked blocker. Decision: adapt.
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| One run, no numbers | No comparison possible |
| Three options changed at once | **Multi-change run** |
| Gap list absent | **Demo-to-prod copy** |
"""),
 verdict="The notebook passes only if each run has numbers, exactly one variable differs between tables, and the gap list is complete.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Agent SDK Examples | Routes to demos and recipes | Current |
| Anthropic | Claude Cookbook (platform.claude.com/cookbook) | Python recipe series | Listed by docs; contents not read |
| Anthropic | Migration guide | Link to OpenAI Agents SDK migration recipe | Current |
""") + "\n\n*Disagreement named:* none found; the demos are described as local-development demos while the commerce page is described as a reference implementation to fork, so the two have different production intent.",
 reframe="This is the craft of learning from examples: **run, change one thing, measure, list the gaps.** The engineer who understands this ships a tested prototype, not a copied demo.",
))

if __name__ == "__main__":
    for s in SPECS:
        write(s)
