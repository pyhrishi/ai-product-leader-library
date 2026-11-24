import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen import write

M = "b-1-1"
SPECS = []

# ------------------------------------------------------------------ 1.1.2
SPECS.append(dict(
 mod=M, id="1.1.2", title="Chatbot versus agent: the operational difference", short="Chatbot versus agent: the operational difference",
 thesis="A chatbot answers and waits; an agent plans, acts, observes the result and loops until it is done or blocked. The difference is not intelligence, it is who closes the loop.",
 prove="run one bug through a chat window and through Claude Code, count the copy-paste handoffs in each, and point to the transcript line where the agent verified its own work.",
 discipline="count handoffs. Every time you copy something from the model to your machine or back, you are the loop, and you are the slowest part of it.",
 counter="a chatbot can be smarter than an agent on any single answer and still lose, because the agent's advantage is the verified result, not the quality of one reply [Claude Code docs, How Claude Code works, 2026].",
 read_min=25, prove_h="2", depth=["Contrast autocomplete, chatbot and agent by who runs the code and who closes the loop", "Choose the right mode for a task and defend it with a handoff count", "Set a team standard for when an agent run needs a human gate"],
 deliverable="A side-by-side run log of one task done both ways, with a handoff count, a loop diagram of the agent run and a one-paragraph verdict.",
 sections=[
 dict(title="Three modes, one table", framing="Tools that touch code fall into three modes. **Autocomplete** predicts the next tokens at your cursor. A **chatbot** answers questions about text you give it, then waits. An **agent** acts on your project through tools, reads what happened and decides the next action. The glossary defines agentic coding the same way: the AI reads files, runs commands and makes changes while you watch, redirect or step away, as opposed to chat assistants that only respond with text you must apply yourself [Claude Code docs, Glossary, 2026].",
  body="""
| Mode | Sees | Does | Who runs the code | Who closes the loop |
|---|---|---|---|---|
| Autocomplete | The cursor neighbourhood | Predicts next tokens | You | You, line by line |
| Chatbot | What you paste | One answer, then waits | You, by copy and paste | You, by relaying results |
| Agent | Your project through tools | Acts, observes, repeats | The agent, through tools | The agent, if it has a check |

```
 AUTOCOMPLETE          CHATBOT                      AGENT
 type ► suggestion     paste ► answer ► (wait)      goal ► act ► observe ► decide ► act ...
   ▲        │             ▲                  │                    ▲                    │
   └ accept ┘             └── you run it ◄───┘                    └──── check passes? ─┘
```

The same bug shows the gap. In a chat window you paste the stack trace, read the answer, apply it, run the tests, paste the next error. In Claude Code you state the failing command and the goal; it runs the command, reads the output, edits, and runs again.
""",
  fm=[("Mode confusion", "You use an agent like autocomplete (asking for snippets) or a chatbot like an agent (expecting it to know what your tests did), so you get neither the speed of one nor the verification of the other.", "Decide the mode before you start: snippet at the cursor is autocomplete, advice about pasted text is chat, a task with a check is an agent run.")],
  xr="the loop is Module 1.2; the surfaces you run it on are Module 7.1.", one="the question that separates the modes is who runs the code and reads the result."),
 dict(title="The loop, and where you sit in it", framing="Claude Code works through every task in three blended phases: gather context, take action, verify results. The phases blend into each other, and you can interrupt at any point [Claude Code docs, How Claude Code works, 2026]. A turn is one complete response from your message until Claude finishes, with any number of tool calls in between [Claude Code docs, Glossary, 2026].",
  body="""
| Phase | What happens | Example tool calls | What you can do |
|---|---|---|---|
| Gather context | Search, read files, inspect git state | Grep, Read, `git status` | Point it at the right directory |
| Take action | Edit files, run commands | Edit, Write, Bash | Approve or deny a permission prompt |
| Verify results | Run tests, read output, compare | Bash, Read | Provide the check; interrupt if wrong |

The docs' own example for "fix the failing tests" chains six moves: run the suite, read the errors, find the relevant files, read them, edit, run the tests again [Claude Code docs, How Claude Code works, 2026]. A chatbot can reason through the middle four but cannot do the first and last, so you do them.

You steer in two ways: `Esc` stops immediately, and typing a correction then pressing `Enter` redirects without stopping [Claude Code docs, How Claude Code works, 2026].
""",
  fm=[("Loop-abandonment", "You start an agent run and then do nothing while it goes down a wrong path for ten minutes, because you treated it as fire-and-forget.", "Watch the first few tool calls of any new kind of task, interrupt with Esc at the first sign of a wrong direction, and only walk away once the check is in place.")],
  xr="the loop with its hook points is Module 1.2; session steering is Module 2.4.", one="you are inside the loop, so interrupt early rather than review late."),
 dict(title="Counting handoffs: the metric that makes this concrete", framing="The most useful single measure of whether you are really using an agent is the number of handoffs: times you move information between the model and your machine by hand. Chat workflows pay a handoff on every iteration. An agent run, with a check, pays only at the start and at the review.",
  body="""
```text
Task: make `npm test` pass in a small repo (3 failing tests).

CHAT RUN                                     AGENT RUN
1 paste failing output   -> handoff 1         1 "run npm test, fix failures,
2 apply patch by hand    -> handoff 2             re-run until green. Do not
3 run tests              -> handoff 3             add dependencies."
4 paste new output       -> handoff 4         2 review `git diff` and test output
5 apply patch            -> handoff 5
6 run tests              -> handoff 6         handoffs: 2   (start, review)
handoffs: 6+ (grows per iteration)
```

The counts are illustrative; yours will vary. The point is the shape: chat cost grows with iterations, agent cost stays flat.

| What the handoff count tells you | Reading |
|---|---|
| High and growing | You are the messenger; give Claude the command and the check |
| Low but the result is wrong | The agent had no real check; add one |
| Low and correct | The loop is closed; you only review |
""",
  fm=[("Human-as-messenger loop", "You copy errors into the tool and patches back into the editor, so the model is an agent in capability and a chatbot in practice.", "Give Claude the command that reproduces the problem and the check that proves it fixed, so it can run and read results itself.")],
  xr="verification design is Module 2.3; prompting for outcomes is Module 2.2.", one="count your handoffs; the number is your loop-closing score."),
 dict(title="What an agent costs you: the new risks", framing="Handing the loop to an agent removes handoffs and adds three risks that a chatbot does not have. The agent can take actions with side effects, it can stop when the work only looks done, and it can spend a large amount of context and plan usage on one task. The docs name the verify gap directly: Claude stops when the work looks done, so a check it can run is what makes the difference between a session you watch and one you walk away from [Claude Code docs, Best practices, 2026].",
  body="""
| Risk | Why a chatbot does not have it | Control |
|---|---|---|
| Side effects | It cannot touch your machine | Permission modes and rules, sandboxing, git |
| Looks-done stop | It never claims a result it did not see | A check Claude can run; `/goal` or a Stop hook for unattended runs |
| Context and usage spend | One answer is cheap | `/clear` between tasks, scoped prompts, `/usage` |

In Manual mode Claude Code starts with read-only permissions and asks before edits and commands; it runs a built-in set of read-only commands such as `ls`, `cat` and `git status` without asking [Claude Code docs, Security, 2026]. That posture is the price of agency: more power, more gates.
""",
  fm=[("Autonomy-without-gate", "You give an agent a broad task in a permissive mode with no check and no branch, and find out after the fact what it changed.", "Work on a branch, keep the tree clean at the start, give a check, and review the diff before you commit.")],
  xr="permissions are Modules 4.2 and 4.3; cost control is Module 1.4; checkpoints and undo are Module 2.5.", one="an agent removes the handoffs and adds the review, so keep the check and the gate."),
 ],
 retrieval=[
  ("Name the three modes and say who runs the code in each.", "Autocomplete (you run it), chatbot (you run it, by copy and paste), agent (the agent runs it through tools)."),
  ("You paste each error into the tool, paste its patch into your editor and run the tests. Name the failure mode by its exact label and the single change that removes it.", "**Human-as-messenger loop.** Give Claude the reproducing command and the check so it runs and reads results itself."),
  ("Name the three phases of the loop in order, and the two keys that stop or steer a run.", "Gather context, take action, verify results. `Esc` stops; typing a correction and pressing `Enter` redirects."),
  ("A teammate says the tool is 'just autocomplete but smarter'. Name the failure mode and the verb it ignores.", "**Mode confusion.** It ignores that the agent runs commands and observes the result, which is the loop."),
  ("In the docs' failing-tests example, how many moves are chained, and which two can a chatbot not do?", "Six; running the suite at the start and re-running the tests at the end."),
  ("You start a long run, leave, and return to a wrong, large diff. Name the failure mode and two fixes.", "**Loop-abandonment.** Watch the first tool calls, interrupt early, work on a branch, and add a check before walking away."),
  ("What does Claude do when no check exists, according to the docs?", "It stops when the work looks done, which may not be correct."),
  ("State the handoff count for a six-iteration chat fix versus an agent run with a check, using the illustrative table.", "About 6 or more for chat (it grows per iteration) versus 2 (start and review) for the agent."),
  ("You run a broad task in a permissive mode on your main branch with no check and later cannot say what changed. Name the failure mode.", "**Autonomy-without-gate.**"),
  ("Which built-in commands run without a prompt in Manual mode, as examples?", "A built-in set of read-only commands such as `ls`, `cat` and `git status`."),
 ],
 steps=[("Pick a small repo with a failing test and a clean tree", "`task.md` with the test command"),
        ("Chat run: paste output, apply patches by hand until green; log each handoff", "Handoff log A"),
        ("Reset the repo to the same state", "Clean tree"),
        ("Agent run: state the command, the goal and a constraint; let Claude loop", "Session transcript"),
        ("Count handoffs, tool calls, iterations and wall-clock time for both", "A two-column table"),
        ("Mark the transcript lines for gather, act, verify", "Three line references"),
        ("Write the verdict: which mode fits this task and why, and what risk the agent run added", "One paragraph")],
 pass_md="""
| Metric | Chat run | Agent run |
|---|---|---|
| Handoffs by hand | 6 | 2 |
| Iterations to green | 3 | 2 (internal) |
| Check passed | Yes, because you ran it | Yes, output visible in the transcript |
| Risk noted | Typos when copying | Edits made without per-step review; reviewed `git diff` |

The numbers above are illustrative. A passing log names the phase lines, the handoff count and one risk.
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| "The agent was faster" with no count | No evidence; counting handoffs was the point |
| The agent run had no test command | **Autonomy-without-gate** and no verify phase |
| The verdict says "agents are always better" | **Mode confusion**: a snippet at the cursor is autocomplete territory |
""",
 verdict="The artifact passes only if both runs started from the same repo state, the handoff counts come from your own logs, and the transcript shows the line where the agent ran the check and read the result.",
 resources="""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | How Claude Code works | The three-phase loop, interrupting and steering | Current |
| Anthropic | Glossary: Agentic coding, Agentic loop, Turn | The precise definitions | Current |
| Anthropic | Best practices: give Claude a way to verify its work | The looks-done stop and the check | Current |
| Anthropic | Security | Manual-mode read-only default and built-in read-only commands | Current |

*Disagreement named:* popular posts describe agents as simply "more autonomous chatbots". The docs define the difference by tool use and the loop, not autonomy level. **The docs win.**
""",
 reframe="This is the craft of telling a chatbot from an agent: **who runs the code and who reads the result.** The engineer who understands this does not ask \"is this model smart?\" — they ask \"how many handoffs does my task need, and what check lets the agent close the loop?\"",
))

# ------------------------------------------------------------------ 1.1.3
SPECS.append(dict(
 mod=M, id="1.1.3", title="Where it runs: environments and surfaces", short="Where it runs: environments and surfaces",
 thesis="Where Claude Code runs decides what it can touch and whether the task survives you closing the laptop. Execution environment and interface are two separate choices.",
 prove="given three tasks, choose the environment and surface for each and defend the choice in one sentence.",
 discipline="separate where the code runs (local, cloud, remote control) from how you interact (CLI, IDE, desktop, web, mobile).",
 counter="the surface with the most polish is not the best default. The CLI is the most complete surface; scripting and the Agent SDK exist only there [Claude Code docs, Platforms, 2026].",
 read_min=25, prove_h="2", depth=["Name the three environments and the surfaces, and say which survive closing the laptop", "Choose a surface for a task using a decision tree", "Standardise surfaces and away-from-terminal workflows for a team"],
 deliverable="A decision card for three real tasks, each with environment, surface, steering need and fallback.",
 sections=[
 dict(title="Environment versus interface", framing="The docs describe three **execution environments**, which decide where code runs and where files live: **Local** (your machine, the default), **Cloud** (Anthropic-managed virtual machines or self-hosted environments your organisation operates) and **Remote Control** (your machine, driven from a browser). The interface is a separate choice: terminal, IDE, desktop app, browser or mobile. The loop is the same in all of them [Claude Code docs, How Claude Code works, 2026].",
  body="""
| Environment | Code runs on | Survives closing your laptop? | Typical use |
|---|---|---|---|
| Local | Your machine | No | Default; full access to your files and tools |
| Cloud | Anthropic-managed VMs or self-hosted | Yes | Offload tasks; work on repos you do not have locally |
| Remote Control | Your machine | No: your machine must stay on | Drive a local session from the web UI or phone |

The glossary draws the same line: a **cloud session** keeps running after you close your laptop because it runs on cloud infrastructure; **Remote Control** continues a local session from another device while execution and files stay on your machine [Claude Code docs, Glossary, 2026].
""",
  fm=[("Environment-surface conflation", "You treat 'the web app' as the environment and assume work started there runs locally, or that the terminal means local when you launched with a cloud flag.", "Ask two separate questions: where does the code run, and where do I interact; write both down for the task.")],
  xr="choosing where to run is Module 7.1; cloud sessions are Module 7.4; remote control is Module 7.5.", one="two questions, not one: where it runs and where you steer it."),
 dict(title="The surfaces and their trade-offs", framing="The docs list the terminal CLI, VS Code, JetBrains, the desktop app, the web and mobile, plus integrations. Choose by what the task needs from the interface [Claude Code docs, Platforms, 2026].",
  body="""
| Surface | Best for | Trade-off |
|---|---|---|
| CLI | Terminal workflows, scripting, remote servers | The most complete; scripting and the Agent SDK are CLI-only |
| Desktop | Visual diff review, parallel sessions, managed setup | Gives up some CLI-only features |
| VS Code | Inline diffs inside the editor | Gives up some CLI-only features |
| JetBrains | The same inside JetBrains IDEs | The plugin needs the CLI installed separately |
| Web | Long tasks needing little steering; work that continues offline | Cloud; less suited to heavy back-and-forth |
| Mobile | Starting and monitoring tasks away from the computer | A thin client into cloud sessions, Remote Control or Dispatch |

[Claude Code docs, Overview and Platforms, 2026]

Integrations such as Chrome, Slack, GitHub Actions, GitLab CI/CD and Code Review connect to a surface; the glossary notes that Slack and the Chrome extension are integrations rather than surfaces themselves [Claude Code docs, Glossary, 2026].
""",
  fm=[("Wrong-surface choice", "You start a two-hour migration in a local terminal and close the laptop, or run a task that needs constant steering in a cloud session you cannot see.", "Use the decision tree: match the surface to how much steering the task needs and whether it must outlive your machine.")],
  xr="the desktop app is Module 7.2; IDE integrations are Module 7.3; browser and computer use are Module 7.6.", one="pick the surface by the steering the task needs, not by habit."),
 dict(title="A decision tree you can run in 30 seconds", framing="Four questions settle most choices. Run them in order.",
  body="""
```
 1. Needs my local files, tools or secrets?  yes ► Local (CLI, Desktop or IDE)
                                              no  ▼
 2. Long-running, little steering needed?     yes ► Cloud session (check back later)
                                              no  ▼
 3. Want to steer a local session from phone  yes ► Remote Control
    or browser?                               no  ▼
 4. Should it happen on a schedule or event?  yes ► Scheduled task, Channels or CI
```

| Task | Environment | Surface | Why |
|---|---|---|---|
| Fix a bug in the repo on my laptop, review the diff | Local | CLI or IDE | Needs my tools; quick steering |
| Refactor a 200-file module overnight | Cloud | Web | Outlives the laptop; low steering |
| Check on a running local test loop from the sofa | Remote Control | Mobile or browser | Execution stays local |
| Triage every new issue on a schedule | Scheduled or CI | Integration | No human in the loop |
""",
  fm=[("Steering-blind delegation", "You send a task needing frequent human judgment to a cloud session, then discover three hours later that it made a wrong early decision.", "Put judgment-heavy work in a local or Remote Control session and reserve cloud sessions for tasks with a check and little steering.")],
  xr="scheduled tasks and loops are Module 6.7; CI and code review are Module 7.8; Dispatch and channels are in Modules 7.5 and 7.7.", one="four yes/no questions beat a debate about tools."),
 dict(title="Working when you are away", framing="The docs treat away-from-terminal work as its own decision with several mechanisms. Dispatch routes a task from the mobile app to a Claude Code session in the desktop app (Pro and Max plans); Remote Control continues a local session from phone or browser; Channels push events from chat apps into a running session; Slack lets you mention Claude; self-hosted environments and scheduled tasks cover team and recurring work [Claude Code docs, Platforms and Glossary, 2026].",
  body="""
| Mechanism | Trigger | Where it runs | Plan or availability note |
|---|---|---|---|
| Dispatch | Message from the mobile app | Desktop app session | Pro and Max [Claude Code docs, Glossary, 2026] |
| Remote Control | You open claude.ai/code or the app | Your machine | Execution stays local |
| Channels | An event in Telegram, Discord or iMessage | Your running session | Research preview [Claude Code docs, Glossary, 2026] |
| Cloud session | `claude --cloud`, web, mobile | Anthropic or self-hosted VMs | Survives disconnect |
| Teleport | `/teleport` | Pulls a cloud session into your terminal | Reverse is `--cloud` |

A persistent Remote Control session that loses its credentials stops making progress and cannot recover until you log in again [Claude Code docs, Authentication, 2026; wording from the translated page, verify in English].
""",
  fm=[("Offline-assumption", "You leave a Remote Control or local session running and close the laptop, then find nothing happened because execution was on your machine.", "For work that must continue after you disconnect, use a cloud session; for work that stays local, keep the machine awake and signed in.")],
  xr="mobile and remote control are Module 7.5; team chat integrations are Module 7.7; authentication is Module 1.3.", one="away-from-terminal means choosing which machine keeps working."),
 ],
 retrieval=[
  ("Name the three execution environments and say which one needs your machine to stay on after you leave.", "Local, cloud, Remote Control. Local and Remote Control need your machine on; cloud survives."),
  ("You assume work started in the web app runs on your laptop. Name the failure mode by its exact label.", "**Environment-surface conflation.**"),
  ("Which surface has scripting and the Agent SDK, and why does it matter for tooling?", "The CLI; pipelines and scripts can only be built there."),
  ("You start a two-hour migration locally and close the laptop. Name the failure mode and the first question of the decision tree you skipped.", "**Wrong-surface choice.** 'Needs my local files, tools or secrets?' leads to local, but 'long-running, little steering?' leads to cloud; you skipped the survival question."),
  ("A task needs constant judgment and you send it to a cloud session. Name the failure mode and the fix.", "**Steering-blind delegation.** Use local or Remote Control for judgment-heavy work."),
  ("Which plans have Dispatch, and what does it do?", "Pro and Max; it routes a task from the mobile app to a session in the desktop app."),
  ("What does `/teleport` do, and what is the reverse?", "Pulls a cloud session into your local terminal; `--cloud` sends a local task to run in the cloud."),
  ("You close the laptop during a Remote Control session. Name the failure mode.", "**Offline-assumption.**"),
  ("List the four decision-tree questions in order.", "Needs local files/tools? Long-running with little steering? Steer a local session from phone or browser? Scheduled or event-triggered?"),
 ],
 steps=[("Write three real tasks you do or want to do", "`tasks.md`"),
        ("Run the four-question decision tree on each", "Three answers"),
        ("For each, name environment, surface, steering need and a fallback if the first choice fails", "A three-row table"),
        ("Launch one task locally and one in a cloud session (or describe why you cannot)", "Two session references"),
        ("Close the laptop for 10 minutes during the cloud run and record what continued", "Observation"),
        ("Check the platforms page for one feature on your plan and provider", "One verified fact"),
        ("State one task you would never put in the cloud and why", "One sentence")],
 pass_md="""
| Task | Environment | Surface | Steering | Fallback |
|---|---|---|---|---|
| Fix a bug and review the diff | Local | CLI | High | IDE |
| Overnight 200-file refactor with tests | Cloud | Web | Low | Local with `caffeinate` |
| Monitor a local test loop remotely | Remote Control | Mobile | Medium | SSH |

The card also records which feature was verified against your own plan and provider.
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| "CLI for everything" with no reasons | **Wrong-surface choice** by habit |
| Cloud chosen for a judgment-heavy task | **Steering-blind delegation** |
| No observation of what happened when the laptop closed | **Offline-assumption** untested |
""",
 verdict="The artifact passes only if every task has an environment and a surface chosen by the decision tree and at least one claim is verified against your own account rather than assumed.",
 resources="""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | How Claude Code works: execution environments | The three environments | Current |
| Anthropic | Platforms and integrations | Surface trade-offs, shared config, away-from-terminal options | Current |
| Anthropic | Glossary: Cloud session, Remote Control, Dispatch, Teleport, Channel | Precise meanings | Current |
| Anthropic | Feature availability | Which feature exists on which plan and provider | Not fetched this session; check |

*Disagreement named:* older pages call every cloud session 'Claude Code on the web'. The glossary now reserves that name for the browser surface at claude.ai/code and calls the general idea a cloud session. **The glossary wins.**
""",
 reframe="This is the craft of choosing where Claude Code runs: **two separate decisions, environment and interface, made by how much steering the task needs and whether it must outlive your machine.** The engineer who understands this does not ask \"which app should I open?\" — they ask \"where should this code run, and how will I steer it?\"",
))

# ------------------------------------------------------------------ 1.1.4
SPECS.append(dict(
 mod=M, id="1.1.4", title="Same engine, many surfaces: what carries over", short="Same engine, many surfaces: what carries over",
 thesis="Because every surface runs the same engine, your configuration travels with you; because features differ by surface, plan and provider, availability does not.",
 prove="list five things that carry across surfaces and five that do not, each with a source you verified.",
 discipline="put shared rules in files the engine reads, and verify a feature exists on every surface and plan before you depend on it.",
 counter="more surfaces do not mean more consistency. A convenience feature on one surface can be the exact thing a teammate on another plan cannot use.",
 read_min=20, prove_h="2", depth=["State what is shared and what differs across surfaces", "Audit a workflow for surface and plan dependencies", "Write the team runbook with an availability check built in"],
 deliverable="A two-column table of what carries over versus what does not, plus a runbook line with an availability check.",
 sections=[
 dict(title="What is shared", framing="Each surface connects to the same underlying engine, so the files that configure Claude Code work across all of them: the docs say your CLAUDE.md files, settings and MCP servers carry over between local surfaces [Claude Code docs, Overview and Platforms, 2026].",
  body="""
| Shared across local surfaces | Where it lives | Why it carries |
|---|---|---|
| Project instructions | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Read from disk by the engine |
| Settings | `~/.claude/settings.json`, `.claude/settings.json` | Same layered hierarchy everywhere |
| MCP servers | `.mcp.json`, user config | Same server connection layer |
| Skills, hooks, subagents | `.claude/` | Same extension loader |
| Auto memory | `~/.claude/projects/` | Keyed by repository |

The settings hierarchy, highest to lowest, is managed policy, command-line arguments, local settings, project settings, then user settings; arrays merge across layers and scalars at a higher layer override lower ones [Claude Code docs, Glossary, 2026].
""",
  fm=[("Habit-over-file", "A rule lives in your terminal habits ('I always run X first') rather than in a file, so a teammate on another surface never gets it.", "Move the rule into CLAUDE.md, settings or a hook, and commit it.")],
  xr="settings are Module 4.1; CLAUDE.md is Module 3.2; the `.claude` directory is Module 3.3.", one="if a rule must apply on every surface, put it in a file the engine reads."),
 dict(title="What is not shared", framing="Availability differs by surface and by account. Cloud sessions are the sharpest case: the glossary says cloud sessions start from a fresh clone of your repository and do not read `~/.claude/` on your machine [Claude Code docs, Glossary, 2026].",
  body="""
| Differs | Example | Source |
|---|---|---|
| Scripting and the Agent SDK | CLI only | Platforms |
| Visual diff viewer, app preview, parallel sessions | Desktop | Platforms |
| Computer use and Dispatch | Desktop, Pro and Max | Platforms, Glossary |
| Third-party providers | CLI, VS Code, JetBrains (Desktop has its own provider path) | Overview, Platforms |
| User-level config in cloud sessions | Cloud starts from a fresh clone, no `~/.claude/` | Glossary |
| Artifacts sharing | Pro and Max: public link; Team and Enterprise: organisation sharing | Glossary |

[Claude Code docs, Overview, Platforms and Glossary, 2026]

The practical consequence: anything in your user-level `~/.claude/` (personal CLAUDE.md, personal skills) will not exist in a cloud session. Project-level files, committed to the repository, will.
""",
  fm=[("Assumed parity", "You write a runbook around a command or feature seen on one surface, and a teammate on another surface or plan cannot do it.", "Check the platforms and feature-availability pages for every surface, plan and provider your team uses, and keep the check in the runbook.")],
  xr="surfaces compared in depth are Module 7.1; cloud environments are Module 4.5; plans and availability are Module 1.4.", one="user-level config does not travel to the cloud; project files do."),
 dict(title="Designing for portability", framing="Treat your repository as the portable unit. Anything that must work for every teammate and every surface goes in committed project files; anything personal stays in `~/.claude/`.",
  body="""
```
 repo/
 ├─ CLAUDE.md                    # conventions, commands, architecture notes (committed)
 ├─ .mcp.json                    # project MCP servers (committed; has its own approval prompt)
 └─ .claude/
    ├─ settings.json             # team permissions and hooks (committed)
    ├─ settings.local.json       # personal overrides (gitignored)
    ├─ skills/  agents/  rules/  # extensions (committed)
 ~/.claude/                      # personal: CLAUDE.md, skills, settings (NOT in cloud sessions)
```

A short portability checklist: list the features your workflow uses, tag each with the surfaces, plans and providers it needs, record `claude --version`, and put the list at the top of the runbook.

Servers in a project's `.mcp.json` have their own approval prompt, so a committed server is not silently trusted [Claude Code docs, Security, 2026].
""",
  fm=[("Personal-config dependency", "Your workflow depends on a personal skill or setting in `~/.claude/`, and it breaks in a cloud session or for a new teammate.", "Move shared skills and settings into the repository's `.claude/` and commit them.")],
  xr="skills are Module 5.2; plugins and marketplaces for sharing are Module 5.6; managed settings for orgs are in Part 11.", one="the repo is the portable unit; `~/.claude/` is yours alone."),
 ],
 retrieval=[
  ("Name four things that carry across local surfaces.", "CLAUDE.md, settings, MCP servers, skills and hooks (also auto memory)."),
  ("Your team runbook uses a feature a teammate on another plan cannot run. Name the failure mode by its exact label.", "**Assumed parity.**"),
  ("Does a cloud session read `~/.claude/` on your machine?", "No; it starts from a fresh clone of your repository."),
  ("Name the failure mode in which your workflow breaks in the cloud because a personal skill is missing, and the fix.", "**Personal-config dependency.** Commit shared skills and settings into the repo's `.claude/`."),
  ("State the settings precedence from highest to lowest, and which merge.", "Managed policy, command-line arguments, local settings, project settings, user settings. Arrays merge; higher scalars override."),
  ("Where does scripting with the Agent SDK exist?", "CLI only."),
  ("A rule only lives in one person's terminal habits. Name the failure mode.", "**Habit-over-file.**"),
  ("Which plans get the public artifact link, and which get organisation sharing?", "Pro and Max: public link; Team and Enterprise: organisation sharing, plus public links once an Owner enables them."),
 ],
 steps=[("List five things you configure in Claude Code today", "`config.md`"),
        ("Tag each as shared, surface-specific or personal and cite the doc line", "A five-row table"),
        ("Find one of your workflow steps that depends on `~/.claude/`", "One finding"),
        ("Move it into the repo's `.claude/` and prove it loads from a fresh clone", "Clone log"),
        ("Check one feature against the platforms page for your plan and provider", "One verified line"),
        ("Write the runbook header: surfaces, plans, providers, version", "Four-line header")],
 pass_md="""
| Item | Class | Evidence |
|---|---|---|
| Team CLAUDE.md | Shared | Loaded in CLI and Desktop sessions |
| Personal skill | Personal | Not present in a cloud session; moved to repo `.claude/skills/` |
| Computer use | Surface-specific (Desktop, Pro/Max) | Platforms page |

The header names surfaces, plans, providers and `claude --version`.
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| "Everything carries over" | **Assumed parity** |
| A skill still in `~/.claude/` after the exercise | **Personal-config dependency** |
| No version recorded | The availability claim cannot be re-checked |
""",
 verdict="The artifact passes only if you proved one item loads from a fresh clone and every surface-specific claim has a doc citation.",
 resources="""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Platforms and integrations | Shared config across local surfaces | Current |
| Anthropic | Glossary: Surface, Settings layers, Cloud session | Precise definitions | Current |
| Anthropic | Cloud environments: what carries over | Cloud session start state | Current; not fetched this session |
| Anthropic | Feature availability | Per-plan, per-provider table | Not fetched this session; check before standardising |
""" + "\n*Disagreement named:* none found between the sources read.",
 reframe="This is the craft of portability: **one engine, shared files, and an explicit list of what does not travel.** The engineer who understands this does not ask \"does it work on my machine?\" — they ask \"which surface, plan and version does each step need, and is that written down?\"",
))

# ------------------------------------------------------------------ 1.1.5
SPECS.append(dict(
 mod=M, id="1.1.5", title="Delegate, do not dictate", short="Delegate, do not dictate",
 thesis="You get the best result by stating the outcome, the constraints and the check, and letting Claude choose the steps. Dictating the steps caps the result at the quality of your plan.",
 prove="rewrite three step-by-step prompts as outcome, constraint and check prompts, and run one of each to compare the results.",
 discipline="every prompt carries an outcome, the constraints that matter, and a check Claude can run.",
 counter="more detail is not always better. Specificity belongs in the outcome and the check; spelling out the steps removes exactly the adaptation that makes an agent worth using [Claude Code docs, How Claude Code works, 2026].",
 read_min=25, prove_h="2.5", depth=["Convert a step-by-step instruction into a delegated prompt", "Decide when to be directive (plan first) versus when to delegate", "Write the team's prompt template and review standard for delegated work"],
 deliverable="Three paired prompts (dictated versus delegated) for real tasks, one executed pair with results, and a one-page prompt template.",
 sections=[
 dict(title="What delegating looks like", framing="The docs recommend treating Claude Code like a capable colleague: give context and direction, then trust it to work out the details. Their example states the symptom and the location (checkout fails for users with expired cards, the code is in `src/payments/`) and asks Claude to investigate and fix it, without naming files or commands [Claude Code docs, How Claude Code works, 2026].",
  body="""
```text
# DICTATED (caps the result at your plan)
Open src/payments/charge.ts, find validateCard, add a check on the expiry month,
then open the test file and add a test for expired cards...

# DELEGATED (outcome + constraint + check)
Checkout fails for users with expired cards. Relevant code is in src/payments/.
Write a failing test that reproduces it, fix it, and run the payments tests.
Do not add dependencies.
```

| Part | What it carries | If missing |
|---|---|---|
| Outcome | What "done" means | Claude optimises for something else |
| Location | Where to look | Exploration spreads across the repo |
| Constraint | What not to do | Surprises in the diff |
| Check | How Claude knows it worked | It stops when the work looks done |
""",
  fm=[("Dictating the steps", "You write the exact edits you want, Claude follows them literally, and the result is only as good as your plan, which was the thing you wanted to delegate.", "State the outcome, the location and the constraints, add a check, and let Claude choose the route.")],
  xr="prompting craft is Module 2.2; the explore, plan, implement, commit loop is Module 2.1.", one="the prompt is an outcome, a boundary and a check, not a recipe."),
 dict(title="Specific where it counts", framing="Delegation is not vagueness. The best-practices guidance asks for specificity in the places that matter: scope the task, point to sources, reference existing patterns, describe the symptom and what fixed looks like [Claude Code docs, Best practices, 2026].",
  body="""
| Vague | Specific, still delegating |
|---|---|
| "Fix the login bug" | "Users report login fails after session timeout. Look at `src/auth/`, especially token refresh. Write a failing test, then fix it." |
| "Add tests for foo.py" | "Write tests for foo.py covering the edge case where the user is logged out. Avoid mocks." |
| "Add a calendar widget" | "Look at how existing widgets are implemented on the home page, follow that pattern, and add a calendar widget without new libraries." |

[Prompt shapes follow the Best practices page's specificity table; the wording here is paraphrased.]
""",
  fm=[("Delegating without a check", "You say 'fix the login bug' with no failing test, no command and no definition of fixed, and Claude stops when the work merely looks done.", "Attach a check Claude can run, such as a reproduction test, a build exit code or a screenshot comparison.")],
  xr="verification is Module 2.3; sessions are Module 2.4.", one="be specific about outcome and check, silent about steps."),
 dict(title="When to be directive: plan first", framing="Delegation has a limit. When the approach is uncertain, the change spans several files or you do not know the code, ask Claude to plan before editing. The docs' rule of thumb: if you could describe the diff in one sentence, skip the plan [Claude Code docs, Best practices, 2026].",
  body="""
```
 Could you describe the diff in one sentence?
 ├─ yes ──► delegate directly (outcome + check)
 └─ no  ──► Explore (read-only) ► Plan (review it) ► Implement ► Commit
```

Plan mode is a permission mode where Claude researches and proposes changes without editing your source files; enter with `/plan` or `Shift+Tab` [Claude Code docs, Glossary, 2026]. For tasks too large to describe in a sentence, an interview prompt that asks Claude to question you and write a spec first is the docs' suggested route [Claude Code docs, Best practices, 2026].
""",
  fm=[("Plan-skipping", "You delegate a multi-file change with an unclear approach directly, and the diff touches the wrong abstraction.", "Use plan mode first for multi-file or unfamiliar work, review the plan, then switch to implementation.")],
  xr="plan mode is Module 4.3; the explore, plan, implement loop is Module 2.1.", one="a one-sentence diff is delegated; anything bigger is planned first."),
 dict(title="Reviewing delegated work", framing="Delegation moves your effort from typing to reviewing. A delegated task is not finished when Claude says so; it is finished when you have read evidence.",
  body="""
| Review step | What you read |
|---|---|
| The check | The test or build output in the transcript |
| The diff | `git diff` for scope, unrelated edits and removed code |
| The constraint | Whether any forbidden dependency or pattern appears |
| The summary | Whether Claude's description matches the diff |

If more than two corrections on the same issue fail, the docs advise `/clear` and a rewritten prompt that includes what you learned, because the context is cluttered with failed attempts [Claude Code docs, Best practices, 2026].
""",
  fm=[("Summary-trust", "You accept Claude's description of what it did without opening the diff or the test output.", "Read the diff and the check output before accepting, and ask for the command and its result if either is missing.")],
  xr="checkpoints and undo are Module 2.5; code review workflows are Module 2.6.", one="review evidence, not the summary."),
 ],
 retrieval=[
  ("State the four parts of a delegated prompt.", "Outcome, location, constraint, check."),
  ("You write the exact edits and Claude follows them literally. Name the failure mode by its exact label.", "**Dictating the steps.**"),
  ("'Fix the login bug' with no test or command. Name the failure mode and the fix.", "**Delegating without a check.** Attach a reproduction test, build or screenshot check."),
  ("What is the docs' rule of thumb for skipping the plan?", "If you could describe the diff in one sentence, skip it."),
  ("Which key cycles into plan mode, and which command enters it?", "`Shift+Tab`; `/plan`."),
  ("You accept Claude's summary without reading the diff. Name the failure mode.", "**Summary-trust.**"),
  ("After how many failed corrections do the docs advise `/clear`?", "More than two on the same issue."),
  ("A multi-file refactor delegated with no plan produces the wrong abstraction. Name the failure mode.", "**Plan-skipping.**"),
  ("Why does a missing check make Claude stop early?", "Claude stops when the work looks done; without a check there is no evidence to continue."),
 ],
 steps=[("Take three tasks you would normally script step by step", "`dictated.md`"),
        ("Rewrite each as outcome, location, constraint and check", "`delegated.md`"),
        ("Run the dictated version of one in a fresh session on a branch", "Result A"),
        ("Reset, run the delegated version", "Result B"),
        ("Compare diff size, correctness, tool calls and time", "A comparison table"),
        ("Decide for each task whether to plan first, using the one-sentence rule", "Three verdicts"),
        ("Write your one-page prompt template", "`template.md`")],
 pass_md="""
| Metric | Dictated | Delegated |
|---|---|---|
| Diff correct | Yes, but missed a related call site | Yes, found the related call site |
| Tool calls | 9 | 14 |
| Check passed | Only the one you named | Full suite |

Numbers are illustrative; the template contains outcome, location, constraint and check fields.
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Delegated prompt has no check line | **Delegating without a check** |
| The 'delegated' prompt lists file paths and line edits | **Dictating the steps** in disguise |
| No comparison, only 'felt better' | Nothing demonstrated |
""",
 verdict="The artifact passes only if both runs started from the same state, each delegated prompt contains all four parts, and the comparison cites diffs and test output.",
 resources="""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | How Claude Code works: work with Claude Code | The delegate-do-not-dictate framing | Current |
| Anthropic | Best practices | Specific prompts, explore-plan-implement-commit, failure patterns | Current |
| Anthropic | Glossary: Plan mode, Verification loop | Definitions | Current |
""" + "\n*Disagreement named:* older blog advice recommends long step lists in prompts; the current Best practices page recommends outcome and check. **The docs win.**",
 reframe="This is the craft of delegation: **an outcome, a boundary and a check, with the route left to the agent.** The engineer who understands this does not ask \"what exact steps should I tell it?\" — they ask \"what does done look like, what must not change, and how will Claude prove it?\"",
))

# ------------------------------------------------------------------ 1.1.6
SPECS.append(dict(
 mod=M, id="1.1.6", title="What Claude Code is not: limits and safeguards", short="What Claude Code is not: limits and safeguards",
 thesis="Claude Code is not a replacement for tests, review, version control or judgment, and the model can be confidently wrong. Safe use is a set of layers, each covering a gap the others leave.",
 prove="for five realistic mishaps, name which layer catches it (tests, review, git, permissions or checkpoints) and which does not.",
 discipline="never ship what you cannot verify, and never rely on one safeguard to cover another's job.",
 counter="the safeguard people trust most, checkpoints, covers the least. They snapshot edits made through file tools and do not track Bash changes or remote effects [Claude Code docs, Glossary, 2026].",
 read_min=25, prove_h="3", depth=["Name the limits and which safeguard covers each", "Design a layered safeguard set for a task type", "Set the team's verify-before-ship policy"],
 deliverable="A five-row mishap matrix with the catching layer, a demonstration that a checkpoint does not undo a Bash change, and a verify-before-ship policy.",
 sections=[
 dict(title="The trust-then-verify gap", framing="The best-practices page names the first failure pattern directly: Claude produces a plausible-looking implementation that does not handle edge cases. The fix is to provide verification (tests, scripts, screenshots) and, if you cannot verify it, not to ship it [Claude Code docs, Best practices, 2026].",
  body="""
| Looks fine | Can still be wrong |
|---|---|
| Compiles and runs | Edge cases, concurrency, error paths |
| Tests pass | The tests were weakened or do not cover the change |
| Summary reads well | Summary and diff disagree |
| Confident tone | Confidence is not evidence |

A verification loop is how a session knows the work is done rather than plausible: a check Claude can run, such as tests, a build or a screenshot comparison. The glossary names it the prerequisite for `/goal`, unattended runs and dynamic workflows [Claude Code docs, Glossary, 2026].
""",
  fm=[("Trust-then-verify gap", "The diff looks right, the tests were never run, and an edge case ships.", "Provide verification every time (tests, scripts, screenshots), ask Claude to show evidence, and do not ship what you cannot verify.")],
  xr="verification is Module 2.3; the security threat model is Module 11.1.", one="plausible is not verified."),
 dict(title="Checkpoints are not git", framing="A checkpoint is a restore point created at each prompt that starts a turn; Claude Code snapshots files before every edit. Press `Esc` twice or run `/rewind` to restore code, conversation or both. Checkpoints are saved with the conversation, so a resumed session can still rewind, but they are separate from git and do not track changes made through the Bash tool [Claude Code docs, Glossary, 2026]. Actions that affect remote systems such as databases, APIs and deployments cannot be checkpointed [Claude Code docs, How Claude Code works, 2026].",
  body="""
| Mishap | Checkpoint helps? | What does |
|---|---|---|
| Bad edit through the file tools | Yes | `/rewind` |
| `rm -rf build/` run through Bash | No | Git, backups, deny rules and sandbox |
| A migration applied to a database | No | Migration rollback, permission rules |
| A bad commit | No | Git |
| Wrong direction in conversation | Yes (conversation rewind) | `/rewind` or `/clear` |

```bash
# Prove it yourself in a scratch repo:
echo hi > scratch.txt && git add scratch.txt && git commit -m scratch
# Ask Claude: "delete scratch.txt using the shell, not the edit tool"
# Then /rewind: the file is not restored by the checkpoint. `git restore scratch.txt` does.
```
""",
  fm=[("Checkpoint-as-git assumption", "You rely on `Esc Esc` to undo a Bash-made change or a database write, and the checkpoint does not cover it.", "Keep work in git, commit often, and use permission rules for anything that touches remote systems.")],
  xr="checkpoints are Module 2.5; sandboxing is Module 4.4; permissions are Module 4.2.", one="git protects files, permissions protect the world, checkpoints protect edits."),
 dict(title="Permissions as the second safety layer", framing="Permission modes set what Claude may do without asking. In Manual mode it starts with read-only permissions and asks before edits and commands, running a built-in set of read-only commands such as `ls`, `cat` and `git status` without asking [Claude Code docs, Security, 2026]. It can write only to the folder where it started and its subfolders and asks before reading outside that boundary with Read, Grep and Glob [Claude Code docs, Security, 2026]. Suspicious Bash commands require manual approval even if previously allowlisted [Claude Code docs, Security, 2026].",
  body="""
| Mode | Behaviour | Right when |
|---|---|---|
| Manual (`default`) | Asks before edits and commands | New repos, unknown tasks |
| Accept edits | Auto-approves file edits | You review diffs afterwards |
| Plan | Explores, no source edits | Uncertain approach |
| Auto | A classifier reviews actions | Trusted tasks with a check, on eligible plans |
| `bypassPermissions` | Skips prompts | Isolated, disposable environments only |

[Claude Code docs, Glossary and Permission modes, 2026]

Which mode a new terminal session starts in comes from, in order, the `--permission-mode` flag, then `permissions.defaultMode` in a settings file, then the built-in default; setting `"auto"` in project settings does not take effect [Claude Code docs, Permission modes, 2026].
""",
  fm=[("Bypass-by-default", "You run with prompts disabled on your real machine because it is faster, and a single bad command touches files you did not intend.", "Reserve bypass mode for disposable environments, and use rules and sandboxing for everything else.")],
  xr="permission modes are Module 4.3; sandboxing is Module 4.4; enterprise policy is in Part 11.", one="a mode is a convenience; a rule or a sandbox is a boundary."),
 dict(title="The context limit behind most bad behaviour", framing="Most best practices follow from one constraint: the context window fills fast and performance degrades as it fills [Claude Code docs, Best practices, 2026]. The docs name recurring patterns and their fixes.",
  body="""
| Pattern | Symptom | Fix named in the docs |
|---|---|---|
| Kitchen-sink session | Unrelated tasks in one context | `/clear` between tasks |
| Correcting over and over | Same mistake corrected 3+ times | `/clear` and a better first prompt |
| Over-specified CLAUDE.md | Important rules lost in noise | Prune hard; turn reliable rules into hooks |
| Infinite exploration | Unscoped investigate fills context | Scope narrowly or use subagents |

[Claude Code docs, Best practices, 2026]

Hooks are deterministic while CLAUDE.md is advisory: if something must happen every time, use a hook [Claude Code docs, Best practices, 2026].
""",
  fm=[("Advisory-for-mandatory", "A rule that must hold every time lives only in CLAUDE.md, so it holds most of the time.", "Convert any rule you cannot tolerate breaking into a hook or deny rule.")],
  xr="the context window is Module 3.1; hooks are Module 5.4; large codebases are Module 3.5.", one="when quality drops, suspect the context before the model."),
 ],
 retrieval=[
  ("The diff looks right and the tests were never run. Name the failure mode by its exact label.", "**Trust-then-verify gap.**"),
  ("You press Esc twice after a Bash `rm`. What happens, and which failure mode is it?", "The checkpoint does not restore it. **Checkpoint-as-git assumption.**"),
  ("What cannot be checkpointed according to the docs?", "Actions affecting remote systems such as databases, APIs and deployments."),
  ("Which built-in commands run without a prompt in Manual mode, give two examples.", "`ls`, `cat`, `git status`."),
  ("You run with prompts disabled on your real machine. Name the failure mode and the fix.", "**Bypass-by-default.** Reserve bypass for disposable environments and use rules and sandboxing."),
  ("Order the sources that set a terminal session's starting permission mode.", "`--permission-mode` flag, then `permissions.defaultMode`, then the built-in default."),
  ("A rule that must hold every time lives only in CLAUDE.md. Name the failure mode and fix.", "**Advisory-for-mandatory.** Make it a hook or deny rule."),
  ("Name the docs' fix for correcting the same mistake repeatedly.", "`/clear` and write a better initial prompt."),
  ("Which writes does Manual mode restrict to the starting folder?", "File writes: only the folder where Claude Code started and its subfolders."),
  ("Why does a Bash-made change slip past a checkpoint?", "Checkpoints snapshot files before edits made through the file tools and do not track changes made through Bash."),
 ],
 steps=[("In a scratch repo, commit a file, then ask Claude to delete it via the shell", "Transcript"),
        ("Run `/rewind` and record that the file is not restored", "Observation"),
        ("Restore it with git and note the difference", "Command log"),
        ("Write five realistic mishaps and the layer that catches each", "A five-row matrix"),
        ("Pick one mishap and add the missing layer (rule, hook or sandbox)", "A config snippet"),
        ("Trigger it once to confirm the layer works", "Evidence"),
        ("Write a three-line verify-before-ship policy", "`policy.md`")],
 pass_md="""
| Mishap | Catching layer | Evidence |
|---|---|---|
| Bash deletes a tracked file | Git | `git restore` returned it; checkpoint did not |
| Edit breaks a function | Checkpoint | `/rewind` restored it |
| Weak tests pass | Review | Reviewer found the assertion removed |
| Migration applied | Migration rollback | Documented rollback tested |
| Secret read | Deny rule | Deny rule fired on `Read(.env)` |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Matrix lists only 'checkpoints' for every row | **Checkpoint-as-git assumption** |
| No row tested | The layer is untested; same as no layer |
| Policy says 'review everything carefully' | No evidence standard; **Trust-then-verify gap** remains |
""",
 verdict="The artifact passes only if you personally demonstrated that a checkpoint does not undo a Bash change and triggered one added layer to prove it fires.",
 resources="""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Best practices | Failure patterns and fixes, verify-your-work | Current |
| Anthropic | Checkpointing | What checkpoints track and do not | Current; read via the glossary summary |
| Anthropic | Security | Permission-based architecture, read-only default, injection defences | Current |
| Anthropic | Permission modes | Which mode a session starts in | Current; read via search excerpt |
""" + "\n*Disagreement named:* none found between the sources read.",
 reframe="This is the craft of knowing the limits: **layered safeguards, each covering a gap the others leave, with evidence required before anything ships.** The engineer who understands this does not ask \"can I trust the agent?\" — they ask \"which layer catches this mistake, and have I seen it fire?\"",
))

if __name__ == "__main__":
    for s in SPECS:
        write(s)
