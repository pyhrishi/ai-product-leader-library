import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen import write

M = "b-1-2"
SPECS = []
CC = "Claude Code docs"


def T(rows):
    return rows.strip()


# ------------------------------------------------------------------ 1.2.1 THE LOOP
SPECS.append(dict(
 mod=M, id="1.2.1", title="The loop: gather, act, verify, repeat", short="The loop: gather, act, verify, repeat",
 thesis="Every task runs through one cycle, gather context, take action, verify results, repeat, and every control you will learn later attaches to a specific point in it.",
 prove="draw the loop from memory and mark where a turn begins and ends, where you can interrupt, and where a check closes it.",
 discipline="when behaviour surprises you, locate it on the loop before you touch the prompt.",
 counter="the loop has no 'done' state of its own. Claude stops when the work looks done, so completion is defined by the check you supply, not by the model [Claude Code docs, Best practices, 2026].",
 read_min=22, prove_h="2", depth=["Draw the loop and name the three phases and the turn boundary", "Diagnose a stalled or runaway session by phase", "Design checks and stop conditions for unattended runs"],
 deliverable="An annotated loop diagram plus a three-row diagnosis of past misbehaviour, each placed on a phase.",
 sections=[
 dict(title="Three blended phases", framing="Claude works through every task in three phases: gather context, take action, verify results. They blend: a question may need only gathering, a bug fix cycles through all three repeatedly, a refactor may lean on verification. You can interrupt at any point [Claude Code docs, How Claude Code works, 2026]. The glossary adds that each tool use returns information that informs the next step [Claude Code docs, Glossary, 2026].",
  body=T("""
| Phase | What Claude does | Typical tools | Output into context |
|---|---|---|---|
| Gather context | Find and read what the task needs | Grep, Glob, Read, `git status` | File contents, search hits |
| Take action | Change files, run commands | Edit, Write, Bash | Diffs, command output |
| Verify results | Check the change worked | Bash (tests, build), Read | Pass/fail output |

```
   prompt ──► gather ──► act ──► verify ──┐
                ▲                          │ not done? loop
                └──────────────────────────┘
        you can interrupt at any point (Esc to stop, Enter to steer)
```
"""),
  fm=[("Loop-blind debugging", "You blame the model for a behaviour that was a blocked tool call, stale context or a missing check, and rewrite the prompt for a problem the prompt did not cause.", "Place the symptom on the loop first: was an action blocked, did a result mislead, or did Claude stop with no check; then fix that layer.")],
  xr="the chatbot-versus-agent contrast is Module 1.1; verification is Module 2.3.", one="every misbehaviour has an address in the loop."),
 dict(title="A turn is the unit you can reason about", framing="A turn begins when you send a message and ends when Claude finishes responding, with any number of tool calls in between; a session is many turns, and Stop hooks fire at the end of each turn [Claude Code docs, Glossary, 2026].",
  body=T("""
| Boundary | What fires or changes |
|---|---|
| Start of turn | UserPromptSubmit hooks; a checkpoint is created at each prompt that starts a turn |
| During a turn | Tool calls, permission checks, hooks around each call |
| End of turn | Stop hooks; Claude waits for you |

Checkpoints are created per turn, so `/rewind` moves you between turn boundaries, not inside one [Claude Code docs, Glossary, 2026].
"""),
  fm=[("Turn-blur", "You treat a long multi-step answer as one decision and cannot say which tool call went wrong, so you restart instead of rewinding to the right point.", "Read the transcript tool call by tool call, and use `/rewind` to return to the turn boundary just before the bad step.")],
  xr="checkpoints are Module 2.5; hooks are Module 1.2.6 and Module 5.4.", one="a turn is many tool calls; the transcript tells you which one went wrong."),
 dict(title="Interrupting and steering", framing="You are part of the loop. `Esc` stops Claude mid-action and the context is preserved so you can redirect; typing a correction and pressing `Enter` steers without stopping [Claude Code docs, How Claude Code works, 2026]. Double `Esc` or `/rewind` opens the rewind menu [Claude Code docs, Glossary, 2026].",
  body=T("""
| You want to | Do this | Effect |
|---|---|---|
| Stop a wrong direction now | `Esc` | Action stops, context kept |
| Redirect without stopping | Type and press `Enter` | Correction joins the loop |
| Undo what it did | `Esc Esc` or `/rewind` | Restore code, conversation or both |
| Abandon a cluttered attempt | `/clear` | New session; old one stays resumable |

The docs advise that after more than two failed corrections on the same issue, `/clear` and a better first prompt beat a third correction [Claude Code docs, Best practices, 2026].
"""),
  fm=[("Correction spiral", "You correct the same mistake a third and fourth time inside one context full of failed attempts, and quality keeps dropping.", "After two failed corrections, `/clear` and rewrite the prompt with what you learned.")],
  xr="session management is Module 2.4; prompting after a reset is Module 2.2.", one="interrupt early, and reset instead of arguing."),
 dict(title="Closing the loop: checks and stop conditions", framing="Because Claude stops when the work looks done, a stop condition must be something it can run. The docs list ways to gate completion: a prompt that names the check, `/goal`, a Stop hook, or a verification subagent [Claude Code docs, Best practices, 2026]. The glossary calls the check a verification loop and names it the prerequisite for unattended runs [Claude Code docs, Glossary, 2026].",
  body=T("""
```text
Prompt with a closed loop:
"Run `npm test`. Fix any failures. Repeat until the suite is green or you have
 tried 5 times. Then show me the last test output and `git diff --stat`."
```

| Stop condition | Strength | Weakness |
|---|---|---|
| "Looks done" | None | Claude's own judgement |
| A named command | Good | Only as good as the command |
| `/goal` with a check | Strong for unattended work | Needs a real check |
| Stop hook | Deterministic | Must exit 2 to block |
"""),
  fm=[("Looks-done stop", "Claude ends the turn when the work appears complete and no check was defined, so an incorrect result ships.", "Name the command that proves success and require its output in the final message.")],
  xr="verification is Module 2.3; goals, loops and schedules are Module 6.7; Stop hooks are Module 1.2.6.", one="the loop is only closed by a check Claude can run."),
 ],
 retrieval=[
  ("Name the three phases of the loop in order.", "Gather context, take action, verify results."),
  ("Define a turn and say which hooks fire at its end.", "One complete response from your message until Claude finishes, with tool calls inside; Stop hooks fire at the end."),
  ("A wrong result ships because no check existed. Name the failure mode by its exact label.", "**Looks-done stop.**"),
  ("You blame the model for a blocked tool call and rewrite the prompt. Name the failure mode.", "**Loop-blind debugging.**"),
  ("What stops mid-action and what steers without stopping?", "`Esc` stops; typing and pressing `Enter` steers."),
  ("You have corrected the same mistake four times in one context. Name the failure mode and the fix.", "**Correction spiral.** `/clear` and rewrite the prompt."),
  ("How many failed corrections do the docs say justify `/clear`?", "More than two on the same issue."),
  ("Name two gates the docs list for completion beside a prompt.", "`/goal`, a Stop hook or a verification subagent."),
  ("A long answer's bad step cannot be located. Name the failure mode.", "**Turn-blur.**"),
 ],
 steps=[("Draw the loop from memory", "`loop.png`"), ("Mark turn start and end, hooks that fire and where a checkpoint is made", "Annotations"),
        ("Run a real task with a named check and capture the transcript", "Transcript"), ("Label each tool call as gather, act or verify", "A labelled list"),
        ("Interrupt a run with Esc and steer with Enter; record what changed", "Two observations"), ("Place three past misbehaviours on the diagram", "Three diagnoses")],
 pass_md=T("""
| Past symptom | Phase | Cause | Fix |
|---|---|---|---|
| Edited wrong file | Gather | Unscoped prompt | Name the directory |
| Said done, tests failing | Verify | No check | Name the command |
| Kept repeating a mistake | Loop | Correction spiral | `/clear` |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Diagram has verify before act | The order is gather, act, verify |
| All three diagnoses say 'bad prompt' | **Loop-blind debugging** |
"""),
 verdict="The artifact passes only if every tool call in a real transcript is labelled with its phase and each diagnosis names a phase and a fix.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | How Claude Code works | The loop, interrupting | Current |
| Anthropic | Glossary: Agentic loop, Turn, Verification loop | Definitions | Current |
| Anthropic | Best practices | Gating completion | Current |
""") + "\n\n*Disagreement named:* none found between the sources read.",
 reframe="This is the craft of the loop: **three phases, a turn boundary, and a check that closes it.** The engineer who understands this does not ask \"why did it do that?\" — they ask \"which phase was that, and what would have closed the loop?\"",
))

# ------------------------------------------------------------------ 1.2.2 BUILT-IN TOOLS
SPECS.append(dict(
 mod=M, id="1.2.2", title="Built-in tools: the vocabulary of every control", short="Built-in tools: the vocabulary of every control",
 thesis="Claude's tools are its hands, and their exact names are the keys to permission rules, subagent tool lists and hook matchers.",
 prove="write five permission rules and a hook matcher using exact tool names, and show each fires once.",
 discipline="copy tool names from the Tools reference and test every rule by triggering it.",
 counter="a rule that matches nothing looks identical to a rule that works until the day it matters.",
 read_min=22, prove_h="2", depth=["Name the tool groups and which prompt in Manual mode", "Write and test rules using exact names and patterns", "Design a least-privilege tool set for a subagent or team"],
 deliverable="A tested rule sheet: five permission rules, one hook matcher and one subagent tool list, each with a trigger log.",
 sections=[
 dict(title="The tool groups", framing="Claude Code has built-in tools to understand and modify your codebase. The tool names are the exact strings you use in permission rules, subagent tool lists and hook matchers [Claude Code docs, Tools reference, 2026]. The Permission-required column shows whether each tool prompts in Manual mode for paths inside the working directory; Bash prompts but runs a built-in set of read-only commands without asking; file-access tools marked No still prompt for paths outside the working directory [Claude Code docs, Tools reference, 2026].",
  body=T("""
| Group | Tools | Prompts in Manual mode |
|---|---|---|
| Read and search | Read, Grep, Glob, LSP | No (inside the working directory) |
| Edit | Edit, Write, NotebookEdit | Yes |
| Execute | Bash, PowerShell (Windows), Monitor | Yes; read-only built-ins excepted |
| Web | WebFetch, WebSearch | Yes |
| Orchestrate | Agent, task and ask-user tools | Varies |
| MCP | `mcp__server__tool`, ToolSearch, ListMcpResourcesTool | Follow the permission system |

[Claude Code docs, Tools reference, 2026; the table is a summary of search excerpts, verify rows against the page]
"""),
  fm=[("Tool-name guessing", "You write a rule or matcher with a plausible name that is not a real tool, and it silently matches nothing.", "Copy names from the Tools reference and trigger the action once to confirm the rule fires.")],
  xr="the full control surface is Module 1.2.3; settings are Module 4.1; MCP tools are Module 5.5.", one="tool names are the keys to every control."),
 dict(title="Rule syntax: name plus specifier", framing="Permission rules, subagent lists and hooks all take a `ToolName(specifier)` format, and the specifier depends on the tool [Claude Code docs, Tools reference, 2026].",
  body=T("""
| Rule | Applies to | Matching |
|---|---|---|
| `Bash(npm run *)` | Bash, Monitor | Command pattern |
| `PowerShell(Get-ChildItem *)` | PowerShell | Command pattern |
| `Read(~/secrets/**)` | Read, Grep, Glob, LSP | Path pattern |
| `Edit(/src/**)` | Edit, Write, NotebookEdit | Path pattern |
| `Skill(deploy *)` | Skill | Skill name |
| `Agent(Explore)` | Agent | Subagent type |
| `WebFetch(domain:example.com)` | WebFetch | Domain |
| `WebSearch` | WebSearch | No specifier; allow or deny the whole tool |

Hook matchers use bare tool names, not the parenthesised rule format [Claude Code docs, Tools reference, 2026]. Tools not listed (such as ExitPlanMode) accept only bare names.

Two interactions to remember: a `Read(...)` deny also blocks Edit and Write on that path, including creating a new file there [Claude Code docs, Tools, 2026]; an `Edit(...)` allow also grants read access to that path [Claude Code docs, Tools reference, 2026].
"""),
  fm=[("Deny-rule gap", "You deny one command spelling and assume the secret is protected, while another tool or spelling reaches the same file.", "Write path-level `Read(...)` denies (which also block Edit and Write) and add sandboxing for Bash.")],
  xr="rule design is Module 4.2; sandboxing is Module 4.4; subagent tool lists are Module 5.3.", one="path rules protect paths; command rules protect only the commands they name."),
 dict(title="Bash behaviour you must know", framing="Each Bash command runs in a separate process. A `cd` carries into later commands only while Claude stays inside the project directory or an added directory; if it lands outside, Claude Code resets to the project directory and appends a note to the result. Subagent sessions never carry directory changes [Claude Code docs, Tools reference, 2026]. Suspicious commands need manual approval even if allowlisted (command injection detection) [Claude Code docs, Security, 2026].",
  body=T("""
```bash
# What persists between Bash calls: the working directory (inside the project) and
# files on disk. What does not: shell variables and functions from earlier calls.
cd src && export X=1      # the cd may carry over; X does not
```

| Behaviour | Consequence |
|---|---|
| Separate process per command | Do not rely on exported variables across calls |
| cd outside the project resets | Use absolute paths for outside work |
| Read-only built-ins run without a prompt | `ls`, `cat`, `git status` are cheap to approve |
| Injection detection overrides allowlists | A broad allow rule is not a blank cheque |
"""),
  fm=[("Shell-state assumption", "You expect an exported variable or an environment change from one Bash call to exist in the next, and a later step fails mysteriously.", "Put state in files or repeat it in each command, and use absolute paths when leaving the project directory.")],
  xr="sandboxing is Module 4.4; permissions are Module 4.2.", one="each Bash call is a fresh process; state lives in files."),
 dict(title="Code intelligence and extensions", framing="The code-intelligence category (type errors, go to definition, find references) exists through the LSP tool when a code-intelligence plugin is installed; without it Claude falls back to Grep and Read. Extensions such as skills, MCP, hooks and subagents layer on top of the built-ins [Claude Code docs, How Claude Code works, 2026].",
  body=T("""
```bash
/context   # live breakdown of what is in context, including tool definitions
/mcp       # connected MCP servers and their tools
```

| Need | Without a plugin | With a plugin |
|---|---|---|
| Find all uses of a symbol | Grep text matches | LSP references |
| Check types after an edit | Run the compiler | LSP diagnostics after each edit |
| Jump to a definition | Grep then Read | LSP go to definition |

MCP tool definitions are deferred: only names and server instructions load at startup, full schemas load on demand [Claude Code docs, Glossary, 2026].
"""),
  fm=[("Missing-category blindness", "You expect symbol-aware navigation and Claude uses text search because no code-intelligence plugin is installed.", "Check `/context` and `/mcp`, install the plugin for your language and verify with a find-references test.")],
  xr="code-intelligence plugins are Module 5.8; MCP is Module 5.5.", one="the fifth tool category needs a plugin before it exists."),
 ],
 retrieval=[
  ("Why do exact tool names matter?", "They are the strings used in permission rules, subagent tool lists and hook matchers."),
  ("A rule `Shell(rm *)` never fires. Name the failure mode by its exact label.", "**Tool-name guessing.**"),
  ("Which rule format controls Edit, Write and NotebookEdit?", "`Edit(/src/**)`, a path pattern."),
  ("You deny `Bash(cat .env)` and assume the secret is safe. Name the failure mode and the fix.", "**Deny-rule gap.** Add a path-level `Read(...)` deny and sandboxing."),
  ("What does a `Read(...)` deny also block?", "Edit and Write on that path, including creating a new file there."),
  ("A Bash call expects a variable exported in the previous call. Name the failure mode.", "**Shell-state assumption.**"),
  ("What happens to the working directory if Claude cds outside the project?", "Claude Code resets to the project directory and appends a note to the tool result."),
  ("Symbol navigation falls back to grep. Name the failure mode and the first checks.", "**Missing-category blindness.** `/context` and `/mcp`, then install the plugin."),
  ("Does a hook matcher use `Bash(npm run *)` format?", "No; hook matchers use bare tool names."),
 ],
 steps=[("List the tools in your session with `/context` and `/mcp`", "Tool list"), ("Write five permission rules using exact names (one per format)", "`rules.json`"),
        ("Trigger each once and log whether it prompted, blocked or allowed", "Five log lines"), ("Write a hook matcher for one tool and trigger it", "Hook log"),
        ("Write a read-only subagent tool list", "Subagent frontmatter"), ("Prove the Read-deny-blocks-Edit interaction", "One log line")],
 pass_md=T("""
| Rule | Triggered by | Result |
|---|---|---|
| `Read(./.env)` deny | Ask Claude to read `.env` | Blocked |
| `Bash(npm run test)` allow | Ask it to run tests | No prompt |
| `Edit(/docs/**)` allow | Edit a doc | No prompt |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Rules copied from a blog post, never triggered | **Tool-name guessing** risk |
| Only `Bash(cat .env)` denied | **Deny-rule gap** |
"""),
 verdict="The artifact passes only if every rule has a trigger log showing the rule firing.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Tools reference | Names, rule formats, Bash behaviour | Current; read via search excerpts |
| Anthropic | Permissions | Allow, ask, deny semantics | Current |
| Anthropic | Security | Command injection detection | Current |
""") + "\n\n*Disagreement named:* a third-party mirror lists tool names slightly differently from the official page. **The official Tools reference wins.**",
 reframe="This is the craft of the tool vocabulary: **exact names, specifiers that match, and rules you have seen fire.** The engineer who understands this does not ask \"is this blocked?\" — they ask \"which tool name and pattern does it match, and have I triggered it?\"",
))

# ------------------------------------------------------------------ 1.2.3 TOOL PERMISSIONS
SPECS.append(dict(
 mod=M, id="1.2.3", title="Tool permissions: modes, rules and sandbox", short="Tool permissions: modes, rules and sandbox",
 thesis="Every tool call passes through the permission system: a mode sets the baseline, rules refine it, and a sandbox bounds what an allowed command can reach.",
 prove="given three actions, predict allow, ask or deny under a stated mode and rule set, then verify each in a session.",
 discipline="use modes for convenience and rules or sandboxing for boundaries.",
 counter="the permission prompt is not a security boundary against what an approved command does; the sandbox is a separate layer from permission rules [Claude Code docs, Glossary, 2026].",
 read_min=22, prove_h="2.5", depth=["Explain modes, rules and sandbox as three layers", "Predict outcomes for a rule set and mode", "Design a team permission baseline"],
 deliverable="A prediction table for six actions under two modes, verified in a live session, plus a baseline settings file.",
 sections=[
 dict(title="Modes: the baseline", framing="A permission mode sets which actions Claude can take without asking. The modes are `default` (shown as Manual in the CLI, IDE extensions and desktop app), `acceptEdits`, `plan`, `auto`, `dontAsk` and `bypassPermissions`; `Shift+Tab` cycles them in the CLI [Claude Code docs, Glossary, 2026].",
  body=T("""
| Mode | Behaviour |
|---|---|
| Manual (`default`) | Asks before edits and commands; read-only built-ins run freely |
| `acceptEdits` | Auto-approves file edits |
| `plan` | Reads and explores, does not edit source |
| `auto` | A classifier model reviews actions instead of you |
| `dontAsk`, `bypassPermissions` | Progressively fewer prompts; bypass for disposable environments |

Auto mode still asks before actions your explicit ask rules match, blocks scope escalation and prompt injection, and strips tool results from what its classifier sees [Claude Code docs, Glossary, 2026].
"""),
  fm=[("Mode-as-policy confusion", "You treat Accept edits or Auto as a security boundary and a command touches something you assumed was protected.", "Use modes for convenience and rules, sandboxing or blocking hooks for boundaries.")],
  xr="permission modes are Module 4.3; auto mode in depth is Module 4.3 too.", one="the mode sets the mood, not the law."),
 dict(title="Rules: allow, ask, deny", framing="Permission rules allow, ask about or deny a tool invocation by tool name and argument pattern. Rules are evaluated deny, then ask, then allow, with the first match winning [Claude Code docs, Glossary, 2026]. `/permissions` lists all rules and the settings file each comes from [Claude Code docs, Permissions, 2026]. A rule you add mid-turn applies from Claude's next tool call (from v2.1.234; earlier versions queued it until the turn ended) [Claude Code docs, Permissions, 2026].",
  body=T("""
```json
{
  "permissions": {
    "allow": ["Bash(npm run test)", "Edit(/src/**)"],
    "ask":   ["Bash(git push *)"],
    "deny":  ["Read(./.env)", "Bash(rm -rf *)"]
  }
}
```

| Question | Answer |
|---|---|
| Does a deny beat an allow? | Yes: deny is evaluated first |
| Where can rules live? | Managed policy, CLI args, local, project, user settings |
| Can a user re-allow a managed deny? | No; managed deny is absolute [secondary: UVM KB article, 2026] |
"""),
  fm=[("Rule-order guess", "You add an allow rule expecting it to override a deny somewhere else, and the action stays blocked.", "Remember deny, ask, allow with first match winning, and use `/permissions` to see which file each rule comes from.")],
  xr="rules in depth are Module 4.2; settings are Module 4.1.", one="deny always wins, and `/permissions` shows who set it."),
 dict(title="Sandbox: what an allowed command can reach", framing="Sandboxing is OS-level filesystem and network isolation for the Bash tool: commands run inside a boundary you define, so Claude can work freely within it without per-command prompts. It is a separate layer from permission rules [Claude Code docs, Glossary, 2026]. Permission modes decide whether Claude asks; the sandbox and outer isolation decide what an action can reach once it runs [Claude Code docs, Permission modes, 2026].",
  body=T("""
| Layer | Decides | Enforced by |
|---|---|---|
| Mode | Whether Claude asks | The harness |
| Rule | Whether this exact call is allowed | The harness |
| Sandbox | What a running Bash command can touch | The OS boundary |

A third-party university guide warns that the most common mistake is assuming the built-in sandbox restricts everything Claude reads; it applies to Bash, not to the file tools [secondary: UVM IT knowledge base, 2026; confirm in Sandboxing docs].
"""),
  fm=[("Sandbox-coverage assumption", "You enable the sandbox and assume file reads through the Read tool are also confined.", "Use `Read(...)` deny rules for file tools and the sandbox for Bash; they are separate layers.")],
  xr="sandboxing is Module 4.4; security posture is Module 11.1.", one="rules gate the call, the sandbox bounds the command."),
 dict(title="Workspace boundary and trust", framing="In Manual mode Claude Code can write only to the folder where it started and its subfolders, and asks before reading outside that boundary with Read, Grep and Glob [Claude Code docs, Security, 2026]. A workspace trust dialog appears for folders you have not trusted [Claude Code docs, Security, 2026].",
  body=T("""
| Situation | Behaviour |
|---|---|
| Edit inside the project | Allowed per mode |
| Write in a parent directory | Needs explicit permission |
| Read outside the boundary | Prompt in Manual mode |
| Start in your home directory | Trust held for the session only; prompt returns each launch |
| `-p` non-interactive run | No trust prompt and no MCP-server prompt |

[Claude Code docs, Security, 2026]
"""),
  fm=[("Home-directory launch", "You start Claude Code in your home directory out of habit, so trust is not saved and the working-directory boundary covers far more than you intend.", "Start Claude Code from a project subdirectory so trust is saved per directory and the boundary is narrow.")],
  xr="trust is Module 1.3; sandbox and isolation are Module 4.4.", one="start in the project, not in home."),
 ],
 retrieval=[
  ("State the rule evaluation order and which match wins.", "Deny, ask, allow; first match wins."),
  ("You treat Accept edits as a security boundary. Name the failure mode by its exact label.", "**Mode-as-policy confusion.**"),
  ("What command lists all permission rules and their source files?", "`/permissions`."),
  ("You add an allow expecting it to beat a deny elsewhere. Name the failure mode.", "**Rule-order guess.**"),
  ("What does the sandbox confine, and what does it not?", "Bash commands; not the built-in file tools."),
  ("You enable the sandbox and assume Read is confined. Name the failure mode and fix.", "**Sandbox-coverage assumption.** Use `Read(...)` denies for file tools."),
  ("What happens to trust when you launch in your home directory?", "Held for the session only; the prompt reappears each launch."),
  ("Name the failure mode of launching Claude Code from home out of habit.", "**Home-directory launch.**"),
  ("From which version does a rule added mid-turn apply to the next tool call?", "v2.1.234."),
  ("Which modes does Shift+Tab cycle in the CLI?", "The modes available in your session, including Manual, Accept edits, Plan and Auto."),
 ],
 steps=[("Write a settings file with allow, ask and deny rules", "`settings.json`"), ("Predict outcome for six actions under Manual and `acceptEdits`", "A 6x2 table"),
        ("Run each in a session and record the actual result", "Observed table"), ("List mismatches and explain each", "Notes"),
        ("Enable the sandbox and test one Bash write outside the boundary and one Read outside", "Two logs"), ("Start once in home and once in a project; compare trust behaviour", "Two observations")],
 pass_md=T("""
| Action | Predicted (Manual) | Observed |
|---|---|---|
| Read `./.env` | Deny | Deny |
| `npm run test` | Allow | Allow |
| `git push` | Ask | Ask |
| Edit `src/a.ts` | Ask | Ask |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Predictions never run | No evidence |
| Sandbox treated as covering Read | **Sandbox-coverage assumption** |
"""),
 verdict="The artifact passes only if every predicted outcome was observed in a live session and every mismatch is explained.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Permissions and Permission modes | Rules, modes, starting mode order | Current |
| Anthropic | Security | Manual-mode behaviour and trust | Current |
| UVM IT | Claude Code Permissions and Sandboxing | Layer warnings | Secondary; verify against official docs |
""") + "\n\n*Disagreement named:* none found between the sources read.",
 reframe="This is the craft of permissions: **a mode for convenience, rules for decisions, a sandbox for reach.** The engineer who understands this does not ask \"should I approve this?\" — they ask \"which layer should have decided this, and is it configured?\"",
))

# ------------------------------------------------------------------ 1.2.4 SYSTEM PROMPT AND TOOL RESULTS
SPECS.append(dict(
 mod=M, id="1.2.4", title="What the model sees: system prompt, context and tool results", short="What the model sees: system prompt, context and tool results",
 thesis="The model has no memory except what is in its context window, so every behaviour traces to what loaded, what grew and what compaction removed.",
 prove="run /context at three points in a session and explain every change.",
 discipline="if an instruction lives only in the conversation, assume compaction will eventually lose it.",
 counter="a longer context window is not a better one; performance degrades as it fills, and the window fills fast [Claude Code docs, Best practices, 2026].",
 read_min=25, prove_h="2.5", depth=["List what loads before you type and what grows afterwards", "Predict what survives compaction", "Design instruction placement and output hygiene for a team"],
 deliverable="Three annotated /context snapshots, a survival table for six instruction types and a hygiene checklist.",
 sections=[
 dict(title="What loads before you type", framing="The context window holds everything Claude knows about your session: instructions, files it reads, its own responses and content that never appears in your terminal [Claude Code docs, Context window, 2026]. Before your first prompt, startup content loads: a system prompt, tool definitions, skill descriptions, your user and project CLAUDE.md files and auto memory.",
  body=T("""
| Startup item | Notes |
|---|---|
| System prompt | About 4,200 tokens in the docs' simulation [representative, not exact; check `/context`] |
| Tool definitions | MCP schemas deferred by default; only names and server instructions load |
| Skill descriptions | Names and descriptions; full content only when used |
| CLAUDE.md files | Concatenated broadest to most specific, loaded as a user message after the system prompt |
| Auto memory | First 200 lines or 25 KB of `MEMORY.md` |

[Claude Code docs, Context window and Glossary, 2026]

Window size depends on model: 200,000 tokens in the docs' simulation; a third-party summary says 1,000,000 on Sonnet 5, Opus 4.6 and later, Sonnet 4.6 and Fable 5 [secondary: dev.to, 2026; confirm in `/context`].
"""),
  fm=[("Startup-bloat", "CLAUDE.md, memory and many skills consume a large share of the window before you type, leaving less room for work.", "Run `/context` at session start, prune CLAUDE.md, and keep skill descriptions short.")],
  xr="the context window in depth is Module 3.1; CLAUDE.md is Module 3.2; skills are Module 5.2.", one="measure startup cost; do not guess it."),
 dict(title="What grows: tool results and file reads", framing="Every tool result stays in context for the rest of the session unless compaction clears it. A read of a large file and a command that prints thousands of lines cost the same kind of tokens, and hook output enters context without truncation [Claude Code docs, Context window, 2026].",
  body=T("""
| Source of growth | Control |
|---|---|
| File reads | Read only what you need; scope the directory |
| Command output | Pipe to a file and read the tail |
| Search hits | Narrow patterns |
| Hook output | Keep `additionalContext` short; it is capped at 10,000 characters [Claude Code docs, Hooks, 2026] |
| Web fetch | Uses a separate context window to limit injection risk [Claude Code docs, Security, 2026] |

```bash
npm test 2>&1 | tail -50          # instead of dumping the whole run into context
```
"""),
  fm=[("Output flood", "A test run or log dump pours thousands of lines into context, pushing out earlier instructions and degrading later answers.", "Pipe to a file and read the tail, run noisy work in a subagent, or add a trimming hook.")],
  xr="subagents are Module 1.2.5; hooks are Module 5.4; large codebases are Module 3.5.", one="what a tool prints, the model reads, and keeps."),
 dict(title="What survives compaction", framing="Compaction summarises the conversation when the window nears its limit: older tool outputs are cleared first, then the conversation is summarised. After compaction, Claude Code re-reads up to five of the most recently modified files from the session [Claude Code docs, Context window, 2026].",
  body=T("""
| Mechanism | After compaction |
|---|---|
| Project-root CLAUDE.md, auto memory | Reloaded fresh from disk |
| Conversation-only instructions | May be lost |
| Path-scoped rules, nested CLAUDE.md | Summarised; reload when a matching file is read |
| Skill listing | Not re-injected; only invoked skills preserved |
| Recently touched files | Up to five re-read |

[Claude Code docs, Context window and Glossary, 2026]

Steer it with a focus: `/compact focus on the auth bug fix` [Claude Code docs, Context window, 2026].
"""),
  fm=[("Chat-only rule", "You state an important rule in conversation and compaction summarises it away.", "Put durable rules in project-root CLAUDE.md or enforce them with a hook or deny rule, and verify with `/memory`.")],
  xr="rules and auto memory are Module 3.3; hooks are Module 5.4.", one="conversation fades; files reload."),
 dict(title="Subagent context and delegation", framing="A subagent starts with a fresh context: its system prompt, the delegation message, CLAUDE.md files and a git status snapshot (Explore and Plan skip the last two). A fork inherits the parent conversation [Claude Code docs, Subagents, 2026]. This is how you keep large reads out of your main window.",
  body=T("""
| Context | Main session | Subagent |
|---|---|---|
| Conversation history | Yes | No (except a fork) |
| CLAUDE.md | Yes | Yes (not Explore or Plan) |
| Files already read | Yes | No |
| Returns | N/A | A summary |
"""),
  fm=[("Context-blind delegation", "You expect a subagent to know earlier constraints and it returns an answer that ignores them.", "Put every constraint, file path and success criterion in the delegation message, or use a fork.")],
  xr="subagent design is Module 5.3; the background of 1.2.5 is next.", one="a subagent is a clean desk; hand it everything."),
 ],
 retrieval=[
  ("Name five items that load before your first prompt.", "System prompt, tool definitions, skill descriptions, CLAUDE.md files, auto memory."),
  ("How much of MEMORY.md loads at start?", "The first 200 lines or 25 KB."),
  ("A long test dump degrades later answers. Name the failure mode by its exact label.", "**Output flood.**"),
  ("A conversation-only rule is lost after compaction. Name the failure mode and fix.", "**Chat-only rule.** Put it in project-root CLAUDE.md or a hook or deny rule."),
  ("How many recently modified files are re-read after compaction?", "Up to five."),
  ("What is not re-injected after compaction among skills?", "The skill listing; only skills you invoked are preserved."),
  ("CLAUDE.md and memory fill half the window at startup. Name the failure mode.", "**Startup-bloat.**"),
  ("Why does a subagent ignore your earlier constraint? Name the failure mode.", "**Context-blind delegation.**"),
  ("What caps hook `additionalContext` output?", "10,000 characters."),
  ("How do you steer what compaction keeps?", "`/compact focus on <topic>`."),
 ],
 steps=[("Run `/context` at session start and record categories", "Snapshot 1"), ("Do a task with two file reads and one noisy command; run `/context` again", "Snapshot 2"),
        ("State a conversation-only rule, run `/compact`, ask about the rule", "Observation"), ("Put the rule in CLAUDE.md, compact again and ask", "Observation"),
        ("Run `/memory` to confirm what loaded", "List"), ("Write a six-row survival table from your observations", "Table")],
 pass_md=T("""
| Item | Survived? | Evidence |
|---|---|---|
| Rule in conversation | No | Claude no longer mentioned it |
| Rule in CLAUDE.md | Yes | Re-read from disk |
| Skill listing | No | Needed a re-invoke |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Survival table copied from docs, never tested | No local evidence |
| No `/context` numbers | **Startup-bloat** invisible |
"""),
 verdict="The artifact passes only if the survival table is backed by your own compaction test with before and after observations.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Explore the context window | Startup load, per-read cost, what survives compaction | Current; numbers representative |
| Anthropic | How Claude Code works: context | Compaction behaviour | Current |
| dev.to (Nishil Bhave) | Context window size 200K vs 1M | Model-dependent window size | Secondary; verify with `/context` |
""") + "\n\n*Disagreement named:* the docs' simulation uses a 200,000-token window while a secondary source says some models run at 1,000,000. **Trust `/context` on your own model.**",
 reframe="This is the craft of context: **know what loaded, what grew and what compaction removes.** The engineer who understands this does not ask \"why did it forget?\" — they ask \"where did that instruction live, and does that location survive compaction?\"",
))

# ------------------------------------------------------------------ 1.2.5 SUBAGENTS AND BACKGROUND
SPECS.append(dict(
 mod=M, id="1.2.5", title="Subagents and background work", short="Subagents and background work",
 thesis="A subagent is a separate loop with its own context that returns a summary, which protects your main window but not your usage budget.",
 prove="delegate one broad search to a subagent and show the main context stayed small while the answer improved.",
 discipline="delegate large, read-heavy, summarisable work and keep small edits in the main session.",
 counter="subagents do not reduce cost; their requests count toward the same limits as the main conversation [Claude Code docs, Subagents, 2026].",
 read_min=22, prove_h="2.5", depth=["Define a subagent and list the built-ins and limits", "Decide when delegating pays off", "Design a subagent set with tool and model scoping"],
 deliverable="A before-and-after context comparison for one delegated search, plus one custom subagent file with scoped tools and model.",
 sections=[
 dict(title="What a subagent is", framing="A subagent is a specialised assistant that runs in its own context window with a custom system prompt, specific tool access and independent permissions. Claude delegates to it when a task matches its description; it works independently and returns a summary, so verbose output stays out of your main conversation [Claude Code docs, Subagents, 2026].",
  body=T("""
| Fact | Detail |
|---|---|
| Starts fresh | No conversation history and no files already read |
| Initial context | System prompt, delegation message, CLAUDE.md, git status snapshot (not for Explore and Plan) |
| Fork | The exception: inherits the parent conversation |
| Scope | Stays inside the session that spawned it |
| Counts toward limits | Yes, the same usage limits |

[Claude Code docs, Subagents and Glossary, 2026]
"""),
  fm=[("Context-blind delegation", "The subagent starts fresh and answers a question missing the key constraint.", "Put every constraint, path and success criterion in the delegation message, or use a fork.")],
  xr="subagent design is Module 5.3; context behaviour is Module 1.2.4.", one="a subagent is a clean desk with only what you hand it."),
 dict(title="Built-ins, limits and background mode", framing="Claude Code ships built-in subagents and sets defaults on nesting and concurrency [Claude Code docs, Subagents, 2026].",
  body=T("""
| Built-in | Purpose |
|---|---|
| Explore | Fast read-only codebase search; Write and Edit denied; quick, medium or very thorough |
| Plan | Read-only research during plan mode |
| General-purpose | Multi-step tasks with exploration and action; all subagent tools |
| statusline-setup, claude-code-guide | Helpers for `/statusline` and feature questions |

| Limit | Default | Change with |
|---|---|---|
| Nesting depth | 3 layers below the main conversation | `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` (1 turns nesting off) |
| Concurrent subagents | 20 | `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` (v2.1.217+) |
| Description size warning | 15,000 tokens combined for non-built-in subagents | Keep descriptions short |

Subagents that Claude spawns from the main conversation start in the background by default; permission prompts surface in your main session; press `Ctrl+B` to background a waiting task [Claude Code docs, Subagents, 2026]. To block a built-in type add `Agent(Explore)` to `permissions.deny`.
"""),
  fm=[("Subagent sprawl", "You spawn many subagents for small tasks, each rebuilding context, and usage climbs with no better results.", "Delegate only large, read-heavy, summarisable work and keep small edits in the main session.")],
  xr="parallel approaches are Module 6.1; background sessions are Module 6.3; usage limits are Module 1.4.", one="20 concurrent and 3 deep are defaults, not goals."),
 dict(title="A custom subagent", framing="A subagent is a Markdown file with frontmatter. Scope it with the tools field and pick a cheaper model for search work [Claude Code docs, Subagents, 2026].",
  body=T("""
```markdown
---
name: code-improver
description: Scans files and suggests improvements for readability, performance, and best practices. Use after writing or modifying code.
tools: Read, Grep, Glob
model: sonnet
---
You are a code improvement specialist. For each issue you find, explain the problem,
show the current code, and provide an improved version.
```

Scope priority when names collide, highest first: managed settings, `--agents` CLI flag, `.claude/agents/` (project), `~/.claude/agents/` (user), plugin `agents/` [Claude Code docs, Subagents, 2026]. Invoke with: `Use the code-improver agent to suggest improvements in this project`.
"""),
  fm=[("Over-broad subagent", "A subagent gets every tool and a huge description, so it can do more than intended and bloats the startup context.", "Grant only the tools the job needs, keep the description short and move detail into the system prompt.")],
  xr="subagents in depth are Module 5.3; tool names are Module 1.2.2.", one="least privilege applies to subagents too."),
 dict(title="Subagents versus agent teams and workflows", framing="A subagent stays inside one session and reports to its parent. Agent teams are separate sessions with their own context, a shared task list and peer messaging, experimental and disabled by default [Claude Code docs, Glossary, 2026].",
  body=T("""
| Aspect | Subagent | Agent team |
|---|---|---|
| Sessions | One | Several |
| Reports to | Parent only | Peers via shared task list |
| You can talk to it | Not directly | Yes, to any teammate |
| Status | Stable | Experimental, off by default |
"""),
  fm=[("Look-alike conflation", "You configure a subagent when you needed an agent team (or the reverse) and spend an hour on the wrong feature.", "Ask who must talk to whom: parent-only means subagent, peers means team.")],
  xr="agent teams are Module 6.4; dynamic workflows are Module 6.5.", one="who talks to whom decides the feature."),
 ],
 retrieval=[
  ("State the default nesting depth and concurrency limits.", "3 layers; 20 concurrent."),
  ("A subagent ignores your earlier constraint. Name the failure mode by its exact label.", "**Context-blind delegation.**"),
  ("What does a fork inherit that a normal subagent does not?", "The parent conversation."),
  ("Many small subagents raise usage with no gain. Name the failure mode and fix.", "**Subagent sprawl.** Delegate only large read-heavy work."),
  ("Do subagent requests count toward limits?", "Yes, the same limits as the main conversation."),
  ("How do you block the Explore subagent?", "Add `Agent(Explore)` to `permissions.deny`."),
  ("Which subagent skips CLAUDE.md and git status?", "Explore and Plan."),
  ("A subagent has all tools and a huge description. Name the failure mode.", "**Over-broad subagent.**"),
  ("You build a subagent when peers needed to talk. Name the failure mode.", "**Look-alike conflation.**"),
  ("What is the description-size warning threshold?", "15,000 tokens combined for non-built-in subagents."),
 ],
 steps=[("Run a broad search in the main session and record `/context` before and after", "Numbers A"), ("Reset and delegate the same search to Explore; record `/context`", "Numbers B"),
        ("Compare main-context growth and answer quality", "Comparison"), ("Write a custom subagent with scoped tools and a model", "Agent file"),
        ("Invoke it once and confirm it ran with restricted tools", "Log"), ("Check `/usage` for the difference", "Note")],
 pass_md=T("""
| Metric | Main session | Delegated |
|---|---|---|
| Main context growth | Large | Small |
| Answer quality | Same | Same or better |
| Usage | Lower | Higher or equal |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Claims delegation 'saves tokens' | Subagents count toward limits |
| Subagent given all tools | **Over-broad subagent** |
"""),
 verdict="The artifact passes only if both runs started from the same state and the usage comparison does not claim savings that `/usage` does not show.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Create custom subagents | Built-ins, limits, frontmatter, scope priority | Current; fork details truncated |
| Anthropic | Glossary: Subagent, Agent teams | Differences | Current |
""") + "\n\n*Disagreement named:* none found between the sources read.",
 reframe="This is the craft of subagents: **a clean context for big reads, a summary back, and the discipline to delegate only what pays.** The engineer who understands this does not ask \"can I spawn more agents?\" — they ask \"does this task need its own context, and what must I hand it?\"",
))

# ------------------------------------------------------------------ 1.2.6 HOOKS
SPECS.append(dict(
 mod=M, id="1.2.6", title="Hooks in the loop: deterministic control", short="Hooks in the loop: deterministic control",
 thesis="A hook is a user-defined handler that runs at a fixed lifecycle point, so it fires every time regardless of what the model decides, which makes it the right tool for rules that must hold.",
 prove="write a blocking hook, show it blocks with exit 2, and show that exit 1 does not.",
 discipline="if it must happen every time, it belongs in a hook, and the hook must exit 2.",
 counter="a hook that exits 1 on violation does not enforce anything; only exit 2 blocks [Claude Code docs, Hooks, 2026].",
 read_min=25, prove_h="3", depth=["Name events, handlers and exit codes", "Write and test a blocking hook", "Design a hook policy layered with permissions"],
 deliverable="A tested blocking hook with transcripts for exit 2 and exit 1, plus an event map of where it sits in the loop.",
 sections=[
 dict(title="Events, matchers, handlers", framing="A hook has three levels: the event (the lifecycle point), a matcher that filters when it fires, and a handler that runs. Hooks are deterministic: they fire at fixed lifecycle points rather than at the model's discretion [Claude Code docs, Glossary, 2026].",
  body=T("""
| Group | Events (of 33 listed) |
|---|---|
| Session | SessionStart, SessionEnd, Setup |
| Prompt | UserPromptSubmit, UserPromptExpansion |
| Tool call | PreToolUse (can block), PermissionRequest, PermissionDenied, PostToolUse, PostToolUseFailure, PostToolBatch |
| Subagents, tasks | SubagentStart, SubagentStop, TaskCreated, TaskCompleted, TeammateIdle |
| Turn end | Stop, StopFailure |
| Context | PreCompact, PostCompact, InstructionsLoaded |
| Environment | ConfigChange, CwdChanged, DirectoryAdded, FileChanged, WorktreeCreate, WorktreeRemove |
| Model | PreModelSwitch, PostModelSwitch |
| MCP | Elicitation, ElicitationResult |

[Claude Code docs, Hooks, 2026; the page was truncated at 100,000 of 282,608 characters, so per-event input schemas are not reproduced]
"""),
  fm=[("Event-guessing", "You register a hook on an event that does not fire at the point you assumed, and the policy never runs.", "Check the event table for exactly when it fires and test by triggering the situation once.")],
  xr="hooks in depth are Module 5.4; settings that register hooks are Module 4.1.", one="pick the event by when it fires, then test it."),
 dict(title="Handler types and exit codes", framing="Handlers can be a shell command (input on stdin), an HTTP POST, an MCP tool call, a prompt to a Claude model for a single-turn decision, or an agent that spawns a subagent to verify conditions (experimental) [Claude Code docs, Hooks, 2026].",
  body=T("""
| Exit code (command hook) | Meaning |
|---|---|
| 0 | Success; JSON on stdout is applied |
| 2 | Blocking error; action stops and stderr is the reason, even if JSON said allow |
| Any other | Non-blocking; action proceeds with a notice |

Exit 2 has no effect on some events such as PermissionRequest, PostToolUse and Notification; use the JSON `decision` object there. `onFailure: "block"` (v2.1.295+) makes a failed, timed-out or invalid hook block the action [Claude Code docs, Hooks, 2026].

```bash
#!/usr/bin/env bash
path=$(jq -r '.tool_input.file_path // empty')
if [[ "$path" == *"/migrations/"* ]]; then
  echo "Migrations are frozen. Create a new migration instead." >&2
  exit 2          # exit 2 blocks; exit 1 would only warn
fi
exit 0
```
"""),
  fm=[("Exit-1 illusion", "Your policy hook exits 1 on violation, the action proceeds, and you believe the rule is enforced.", "Use exit 2 or a JSON block decision, add onFailure block where supported, and test by violating the rule once.")],
  xr="permissions interplay is Module 1.2.3; debugging configuration is Part 12.", one="exit 2 blocks; exit 1 only warns."),
 dict(title="Numbers to know", framing="Defaults and caps shape reliable hooks [Claude Code docs, Hooks, 2026].",
  body=T("""
| Item | Value |
|---|---|
| Default timeout, command, http, mcp_tool | 600 s |
| Default timeout, prompt | 30 s |
| Default timeout, agent | 60 s |
| UserPromptSubmit, PreModelSwitch, PostModelSwitch | 30 s for command, http, mcp_tool |
| MessageDisplay | 10 s |
| SessionEnd shared budget | 1.5 s, raisable to 60 s per hook |
| Concurrency | More than 12 prompt or agent hooks on one event run 12 at a time |
| Output cap | `additionalContext`, `systemMessage`, plain stdout: 10,000 characters each; larger output saved to a file with a 2,000-character preview |
| Skill hooks | At most 1,024 per skill source per session (v2.1.304+) |
| Duplicates | An identical handler in several settings files runs once |
"""),
  fm=[("Slow-hook stall", "A hook with a long default timeout blocks every tool call or prompt for many seconds, and the session feels frozen.", "Set a short explicit timeout, keep hooks fast and move heavy work to async or a subagent.")],
  xr="performance and costs are Module 1.4; hook design is Module 5.4.", one="short timeouts, short output."),
 dict(title="Hooks versus CLAUDE.md and permissions", framing="CLAUDE.md is advisory; hooks are deterministic. Permission rules are also deterministic but only decide allow, ask or deny. A PreToolUse hook runs before the permission check and can block, and an exit 2 blocks even if the JSON said allow [Claude Code docs, Hooks and Best practices, 2026].",
  body=T("""
| Need | Use |
|---|---|
| Guidance and conventions | CLAUDE.md |
| Never allow X | Deny rule |
| Run a formatter after every edit | PostToolUse hook |
| Block edits to a path with a custom message | PreToolUse hook, exit 2 |
| Stop Claude ending the turn early | Stop hook |
"""),
  fm=[("Advisory-for-mandatory", "A rule that must hold lives only in CLAUDE.md, so it holds most of the time.", "Convert must-hold rules into hooks or deny rules and keep CLAUDE.md for guidance.")],
  xr="CLAUDE.md is Module 3.2; extension choice is Module 5.1.", one="advice goes in CLAUDE.md; guarantees go in hooks."),
 ],
 retrieval=[
  ("What exit code blocks, and what does exit 1 do?", "Exit 2 blocks; exit 1 is non-blocking."),
  ("Your hook exits 1 and the edit proceeds. Name the failure mode by its exact label.", "**Exit-1 illusion.**"),
  ("Name the five handler types.", "command, http, mcp_tool, prompt, agent."),
  ("Default timeout for prompt hooks and command hooks?", "30 seconds and 600 seconds."),
  ("A rule that must hold lives only in CLAUDE.md. Name the failure mode.", "**Advisory-for-mandatory.**"),
  ("What is the SessionEnd shared budget?", "1.5 seconds, raisable to 60 s per hook."),
  ("Output size caps for additionalContext?", "10,000 characters; larger output saved with a 2,000-character preview."),
  ("A hook on an event you misread never runs. Name the failure mode.", "**Event-guessing.**"),
  ("A slow hook freezes the session. Name the failure mode and fix.", "**Slow-hook stall.** Set short timeouts and keep hooks fast."),
  ("Which version adds onFailure block?", "v2.1.295 or later."),
 ],
 steps=[("Write a PreToolUse command hook that blocks edits to one path", "`block.sh`"), ("Register it in project settings", "Settings snippet"),
        ("Ask Claude to edit the path; capture the block", "Transcript A"), ("Change to exit 1 and repeat", "Transcript B"),
        ("Add a PostToolUse hook that logs file edits", "Log file"), ("Time the hook and set an explicit timeout", "Timing note")],
 pass_md=T("""
| Variant | Result |
|---|---|
| exit 2 | Edit refused, stderr text shown |
| exit 1 | Edit proceeds, notice only |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Hook tested by reading the script | **Exit-1 illusion** unproven |
| No timeout set | **Slow-hook stall** risk |
"""),
 verdict="The artifact passes only if you triggered both exit codes and captured both outcomes.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Hooks reference | Events, handlers, exit codes, limits | Current; per-event schemas not read |
| Anthropic | Get started with hooks | Setup flow | Current; not fetched this session |
| Anthropic | Best practices | Hooks are deterministic, CLAUDE.md advisory | Current |
""") + "\n\n*Disagreement named:* none found between the sources read.",
 reframe="This is the craft of hooks: **fixed points in the loop where your code decides, enforced by exit 2.** The engineer who understands this does not ask \"can I tell Claude to always do X?\" — they ask \"which event guarantees X, and have I seen it block?\"",
))

# ------------------------------------------------------------------ 1.2.7 SESSIONS
SPECS.append(dict(
 mod=M, id="1.2.7", title="Sessions as transcripts: resume, fork, rewind", short="Sessions as transcripts: resume, fork, rewind",
 thesis="A session is a stored conversation tied to a directory, so you can resume it, fork it, rewind it and audit it, and you must also treat it as sensitive data.",
 prove="resume, fork and rewind a session and say what each changes and what it leaves untouched.",
 discipline="start fresh for new tasks and resume only when the old context is the asset.",
 counter="a session is a file on disk, so convenience features double as privacy exposure.",
 read_min=20, prove_h="2", depth=["Use resume, fork, clear and rewind correctly", "Choose between resume and fresh start by context value", "Set team rules for transcript retention"],
 deliverable="A demonstration log of resume, fork and rewind, plus a transcript-hygiene rule.",
 sections=[
 dict(title="What a session is", framing="A session is a conversation tied to your current directory with its own independent context window. It can be resumed with `claude -c`, forked with `--fork-session` to preserve history under a new session ID, or run in parallel across terminals; `/clear` starts a new session while the previous one stays stored and available via `/resume`; each transcript is stored under `~/.claude/projects/` [Claude Code docs, Glossary, 2026].",
  body=T("""
| Action | Command | Effect |
|---|---|---|
| Resume latest | `claude -c` | Continue the most recent session |
| Resume by pick | `/resume` | Choose a stored session |
| Fork | `--fork-session` or `/branch` | New ID, history kept |
| Fresh start | `/clear` | New session; old one stays resumable |
| One-shot | `claude -p` | Saved unless `--no-session-persistence` |
"""),
  fm=[("Zombie session", "You resume a days-old session with a cluttered context and wonder why quality dropped.", "Start fresh for a new task and resume only when the prior context is the asset.")],
  xr="session management is Module 2.4; headless runs are Module 6.8.", one="resume for continuity, clear for a new task."),
 dict(title="Checkpoints and rewind", framing="A checkpoint is created at each prompt that starts a turn; Claude Code snapshots files before every edit. `Esc Esc` or `/rewind` restores code, conversation or both, or summarises part of the conversation from a chosen message. Checkpoints are saved with the conversation and survive resume, but are separate from git and do not track Bash changes [Claude Code docs, Glossary, 2026].",
  body=T("""
| You rewind | Restores |
|---|---|
| Code | Files changed through file tools |
| Conversation | History to that turn |
| Both | Both |
| Not restored | Bash-made changes, remote effects |
"""),
  fm=[("Checkpoint-as-git assumption", "You rely on rewind to undo a Bash change or a database write and it does not cover it.", "Keep work in git, commit often and use permission rules for remote effects.")],
  xr="checkpoints are Module 2.5.", one="rewind covers edits, not the world."),
 dict(title="Transcripts as sensitive data", framing="Transcripts are stored as plain files under `~/.claude/projects/` (plaintext JSONL per earlier research on sessions [Claude Code docs, 2026; confirm on the sessions page]). Anything pasted or printed in a session, including secrets, sits in that file.",
  body=T("""
| Risk | Control |
|---|---|
| Secret pasted in a prompt | Do not paste secrets; use env vars |
| Secret printed by a command | Deny reads on secret paths |
| Shared machine or backup | Exclude `~/.claude/projects/` or delete sensitive sessions |
| `-p` runs | Pass `--no-session-persistence` when you do not want a stored session |
"""),
  fm=[("Transcript leak", "A token appears in a prompt or tool output and persists in plaintext, then lands in a backup or shared image.", "Keep secrets out of prompts, deny secret paths, and delete or exclude sensitive transcripts.")],
  xr="security is Module 11.1; privacy settings are Module 4.1.", one="a session is a file; treat secrets accordingly."),
 dict(title="Sessions, worktrees and parallel work", framing="Parallel sessions in separate terminals each have their own context. For file isolation, worktree isolation runs Claude in a separate git worktree under `.claude/worktrees/`, enabled with `-w` or `isolation: worktree` in subagent config [Claude Code docs, Glossary, 2026].",
  body=T("""
| Need | Use |
|---|---|
| Two tasks on the same repo | Two worktrees, two sessions |
| Explore a different approach | Fork the session |
| Hand a task to another device | Cloud session or Remote Control |
"""),
  fm=[("Shared-tree collision", "Two sessions edit the same working tree and overwrite each other's files.", "Use worktree isolation so each session works on its own branch and directory.")],
  xr="worktrees are Module 6.2; parallel approaches are Module 6.1.", one="one tree per active session."),
 ],
 retrieval=[
  ("Where are transcripts stored?", "Under `~/.claude/projects/`."),
  ("You resume a three-day-old cluttered session. Name the failure mode by its exact label.", "**Zombie session.**"),
  ("What does `--fork-session` do?", "Preserves history under a new session ID."),
  ("A token shows up in a backup. Name the failure mode.", "**Transcript leak.**"),
  ("Does rewind undo a Bash deletion? Name the failure mode of assuming so.", "No. **Checkpoint-as-git assumption.**"),
  ("What flag stops `-p` from persisting a session?", "`--no-session-persistence`."),
  ("Two sessions overwrite each other's files. Name the failure mode and fix.", "**Shared-tree collision.** Use worktree isolation."),
  ("What does `/clear` do to the old session?", "It stays stored and resumable via `/resume`."),
  ("When are checkpoints created?", "At each prompt that starts a turn."),
 ],
 steps=[("Start a session, make a file edit, and exit", "Transcript"), ("Resume with `claude -c` and confirm context continued", "Observation"),
        ("Fork it and diverge; confirm the original is unchanged", "Two session ids"), ("Edit via file tool then via Bash; `/rewind`; note which is restored", "Log"),
        ("Find the transcript file and check for any secret", "Finding"), ("Write a three-line transcript hygiene rule", "`hygiene.md`")],
 pass_md=T("""
| Action | Result |
|---|---|
| `claude -c` | Continued with context |
| Fork | New id, original intact |
| Rewind | File-tool edit restored; Bash change not |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Hygiene rule says 'be careful' | No control named |
| Rewind assumed to cover Bash | **Checkpoint-as-git assumption** |
"""),
 verdict="The artifact passes only if you observed the Bash-versus-file-tool difference and found where transcripts live on your machine.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Glossary: Session, Checkpoint | Definitions and commands | Current |
| Anthropic | How Claude Code works: sessions | Resume, fork | Current |
| Anthropic | Checkpointing | Limits of checkpoints | Current; not fetched in full |
""") + "\n\n*Disagreement named:* none found between the sources read.",
 reframe="This is the craft of sessions: **resume for continuity, fork to explore, rewind edits, clear for new work, and treat the file as sensitive.** The engineer who understands this does not ask \"can I get that conversation back?\" — they ask \"is that context an asset, and what does it contain?\"",
))

# ------------------------------------------------------------------ 1.2.8 MODEL LAYER
SPECS.append(dict(
 mod=M, id="1.2.8", title="The model layer: models, effort and speed", short="The model layer: models, effort and speed",
 thesis="The model is a setting, not an identity: models and effort levels trade speed, cost and depth, and the right default is mid-tier with deliberate escalation.",
 prove="run one hard and one mechanical task at two settings and show where depth paid and where it did not.",
 discipline="match model and effort to the difficulty of the step, not the importance of the project.",
 counter="the strongest model at maximum effort is not the safest default; it spends your limits on steps that did not need it.",
 read_min=20, prove_h="2", depth=["Name the levers and what each costs", "Choose settings per task and defend with evidence", "Set team defaults for models, effort and subagents"],
 deliverable="A two-task, two-setting comparison with measured usage and a default-settings policy.",
 sections=[
 dict(title="Models in the harness", framing="The same harness drives whichever model you choose. The docs say Sonnet handles most coding tasks well, Opus gives stronger reasoning for complex architectural decisions, and you switch with `/model` or `claude --model <name>` [Claude Code docs, How Claude Code works, 2026].",
  body=T("""
| Lever | Command or setting |
|---|---|
| Switch model | `/model`, `claude --model <name>` |
| Subagent model | `model:` in subagent frontmatter; `CLAUDE_CODE_SUBAGENT_MODEL` for general-purpose |
| Effort | Effort level setting; supported on Fable models, Opus 4.6 and later, Sonnet 4.6 and later |
| Thinking cap | `MAX_THINKING_TOKENS` on models with a fixed thinking budget |

[Claude Code docs, Glossary and Subagents, 2026]
"""),
  fm=[("Max-everything default", "You run the strongest model at the highest effort for every task and hit plan limits on routine edits.", "Default to a mid-tier model and moderate effort, escalate for hard steps and de-escalate for mechanical ones.")],
  xr="models, effort and speed are Module 4.6; costs are Module 1.4.", one="the harness is constant; the model is a dial."),
 dict(title="Effort and extended thinking", framing="Effort controls adaptive reasoning: the model decides whether and how much to think on each step. Higher effort means more thinking tokens and deeper reasoning; lower is faster and cheaper. Extended thinking is the visible step-by-step reasoning before a response, shown in grey italic text in the terminal [Claude Code docs, Glossary, 2026].",
  body=T("""
| Task type | Effort guidance |
|---|---|
| Rename, format, mechanical edits | Low |
| Typical feature work | Default |
| Architecture, hard debugging, security review | High |

[Guidance is judgement, not an official table; test on your own tasks.]
"""),
  fm=[("Effort-as-default", "You leave effort at maximum for everything because it feels safer, and the plan bar drains on routine work.", "Set a moderate default and raise it deliberately for hard steps.")],
  xr="effort settings are Module 4.6; plan usage is Module 1.4.", one="thinking tokens are spent, not free."),
 dict(title="Speed and cost levers", framing="Fast mode trades cost for speed on individual plans and is billed through usage credits [Claude Code docs, Costs, 2026]. Other levers: scoped context, fewer subagents and cheaper models for search workers.",
  body=T("""
| Lever | Speeds up | Costs |
|---|---|---|
| Fast mode | Output | Usage credits on individual plans |
| Smaller model | Everything | Depth |
| Smaller context | Everything | Nothing, if scoped well |
| Fewer subagents | Total cost | Parallelism |

The exact fast-mode multiplier is not reliably established here; treat any figure as order-of-magnitude and read the Costs page.
"""),
  fm=[("Fast-mode forgetting", "You enable fast mode for an afternoon, forget it, and find the extra credit spend later.", "Treat fast mode as a per-task switch and check month-to-date credit spend weekly.")],
  xr="costs and limits are Module 1.4; fast mode in depth is Module 4.6.", one="speed is a per-task purchase."),
 dict(title="Choosing per step", framing="A single task often has hard and easy steps. The practical pattern is a strong model for planning, a default model for implementation and a cheap model for search subagents.",
  body=T("""
| Step | Model and effort |
|---|---|
| Plan a multi-file change | Stronger model, higher effort |
| Implement against the plan | Default |
| Broad search or log scan (subagent) | Cheap model |
| Final review | Stronger model |

[Judgement-based pattern; measure on your own repos with `/usage`.]
"""),
  fm=[("Single-setting habit", "You use one model and effort for a whole task, overspending on easy steps or underpowering hard ones.", "Switch per step with `/model` and set subagent models in frontmatter.")],
  xr="subagents are Module 1.2.5; planning is Module 2.1.", one="switch settings per step, not per project."),
 ],
 retrieval=[
  ("Which command switches model in a session?", "`/model`."),
  ("You run maximum effort for routine edits. Name the failure mode by its exact label.", "**Max-everything default** (and **Effort-as-default** at the effort level)."),
  ("Which models support effort per the glossary?", "Fable models, Opus 4.6 and later, Sonnet 4.6 and later."),
  ("You forget fast mode is on. Name the failure mode.", "**Fast-mode forgetting.**"),
  ("What caps thinking on fixed-budget models?", "`MAX_THINKING_TOKENS`."),
  ("Why set a subagent `model:` field?", "Use a cheaper model for search workers."),
  ("You use one setting for the whole task. Name the failure mode.", "**Single-setting habit.**"),
  ("Where is fast mode billed on individual plans?", "Through usage credits."),
 ],
 steps=[("Pick a hard task and a mechanical task", "`tasks.md`"), ("Run each at default and at a higher setting; record `/usage` deltas", "Four runs"),
        ("Judge result quality blind (rate each without looking at settings)", "Ratings"), ("Decide where depth paid", "Two sentences"),
        ("Set a subagent model for a search worker and run it", "Frontmatter"), ("Write your default-settings policy", "`policy.md`")],
 pass_md=T("""
| Task | Setting | Quality | Usage |
|---|---|---|---|
| Mechanical | Default | Same | Lower |
| Mechanical | High | Same | Higher |
| Hard | Default | Missed a case | Lower |
| Hard | High | Caught the case | Higher |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Quality rated knowing the setting | Bias |
| Policy says 'always high' | **Max-everything default** |
"""),
 verdict="The artifact passes only if quality ratings were blind and usage numbers come from `/usage`.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Model configuration | Effort, switching | Current; not fetched in full |
| Anthropic | Glossary: Effort level, Extended thinking | Definitions | Current |
| Anthropic | Manage costs | Fast mode billing | Current |
""") + "\n\n*Disagreement named:* none found between the sources read.",
 reframe="This is the craft of the model layer: **a dial for depth, a dial for speed, and a default that is neither maximum nor minimum.** The engineer who understands this does not ask \"which model is best?\" — they ask \"how hard is this step, and what setting does it earn?\"",
))

if __name__ == "__main__":
    for s in SPECS:
        write(s)
