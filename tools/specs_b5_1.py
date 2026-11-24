from specs_b5_common import *
M = "b-5-1"
SPECS = []
EXT = "Claude Code docs, Extend Claude Code"
R = lambda: res([
 ("Anthropic", "Extend Claude Code (features overview)", "Menu, triggers, comparisons, layering, context cost", "Current"),
 ("Anthropic", "Skills reference", "Frontmatter and invocation fields", "Current"),
 ("Anthropic blog [secondary: linked from the docs, not fetched]", "Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents", "Deeper walkthrough of the same choice", "Not read in full"),
])

# ---------------------------------------------------------------- 5.1.1
SPECS.append(guide(M, "5.1.1", "The menu", 
 thesis="Claude Code's extensions are a small menu in which each item plugs into a different part of the agentic loop, so choosing one is a matter of matching the job to the loop stage, not of taste.",
 prove="given six real needs, name the one extension that fits each and say which loop stage it plugs into.",
 discipline="name the job first (always know, sometimes know, connect, isolate, enforce, package), then pick the feature.",
 counter="skills, not CLAUDE.md, are called the most flexible extension: a skill can be invoked by you, loaded by Claude, or run in an isolated context [Claude Code docs, Extend Claude Code, 2026].",
 read_min=20, prove_h="1.5",
 depth=["Name every extension on the menu and its one-line job", "Match a stated need to the right extension and justify the rejects", "Audit an existing setup for features used for the wrong job"],
 deliverable="A one-page menu card: every extension, its job, its loading behaviour and one example from your own repository.",
 sections=[
  sec("The ten items", "The overview page lists the items that plug into the agentic loop: CLAUDE.md, output styles, skills, code intelligence, MCP, subagents, dynamic workflows, cross-session messaging, hooks, and plugins with marketplaces; artifacts appear in the comparison table as an eleventh row [Claude Code docs, Extend Claude Code, 2026]. Plugins are described as the packaging layer, not a separate capability.",
   """
| Feature | What it does | Use it for |
|---|---|---|
| CLAUDE.md | Persistent context loaded every conversation | Conventions, "always do X" rules |
| Output style | Sets role, tone and response format for a session | A voice or format you want in every response |
| Skill | Instructions, knowledge and workflows | Reusable content, repeatable tasks |
| Subagent | Isolated execution context returning a summary | Context isolation, parallel work |
| Dynamic workflow | A script Claude writes that runs many subagents in the background | Work that outgrows a handful of subagents |
| Cross-session messaging | Claude delivers a message from one of your sessions to another | Sessions that need each other's findings |
| Code intelligence | Language-server navigation and diagnostics | Typed languages, large codebases |
| MCP | Connects external services | External data or actions |
| Hook | Script, HTTP request, MCP tool call, prompt or subagent on an event | Automation that must run on every matching event |
| Artifact | Publishes session output as a private interactive page | Output better seen than read in a terminal |

[Claude Code docs, Extend Claude Code, 2026]
""",
   ("Menu-by-habit", "You reach for the feature you learned first, usually CLAUDE.md or a long prompt, for every need, and a connection problem gets solved with a paragraph of instructions that cannot open a database.", "Say the job in one word (know, connect, isolate, enforce, package) and look that word up in the table before writing anything."),
   "the module-level treatment is Module 5.1; skills are Module 5.2, subagents Module 5.3, hooks Module 5.4, MCP Module 5.5, plugins Module 5.6.", "every extension has one job; match the job before you build."),
  sec("The loop stage each one plugs into", "The overview page opens with the claim that extensions plug into different parts of the agentic loop, and then describes features as ranging from always-on context, through on-demand capabilities, to background automation on events [Claude Code docs, Extend Claude Code, 2026]. That gives a three-tier reading of the menu that is more useful than an alphabetical one.",
   """
| Tier | Features | Who decides it runs |
|---|---|---|
| Always-on | CLAUDE.md, output styles | Nobody; it is loaded |
| On demand | Skills, subagents, workflows, MCP tools, code intelligence | You, or Claude matching a description |
| On event | Hooks | The lifecycle event itself |

```
 gather ──► act ──► verify
   │         │        │
 CLAUDE.md  hooks    hooks (PostToolUse)
 skills     MCP      subagent (independent check)
 LSP        subagent
```
The diagram is a teaching aid built from the tier table, not a figure from the docs.
""",
   ("Tier confusion", "You put a must-happen rule in an always-on or on-demand feature, such as CLAUDE.md, and expect event-level certainty from it.", "If it must happen every time, move it to the on-event tier (a hook); keep always-on tiers for facts and style."),
   "the loop itself is Module 1.2; hooks as the on-event tier are Module 5.4.", "decide whether the thing is always on, on demand or on an event."),
  sec("Skills as the flexible default", "The overview says skills are the most flexible extension: a markdown file of knowledge, workflows or instructions that you can invoke with a command such as `/deploy`, that Claude can load automatically when relevant, and that can run in your conversation or in an isolated context through subagents [Claude Code docs, Extend Claude Code, 2026]. It also separates reference skills (knowledge used throughout a session) from action skills (do something specific).",
   """
| Skill kind | Example | Typical invocation |
|---|---|---|
| Reference | Your API style guide | Claude loads it when relevant |
| Action | `/deploy` runs the deployment checklist | You type the name |
| Forked | A skill with `context: fork` | Runs as a subagent |

When a need does not obviously fit another row, a skill is the usual first try, because it costs little until used: descriptions load at session start and full content loads when invoked [Claude Code docs, Extend Claude Code, 2026].
""",
   ("Skill-for-everything", "A hard guarantee, such as blocking edits to `.env`, is written as a skill instruction, and Claude interprets it rather than obeying it.", "Keep skills for judgement and knowledge; put guarantees in a hook (Module 5.4)."),
   "writing skills is Module 5.2; the hook-versus-skill choice is sub-topic 5.1.5.", "a skill is the default for knowledge and workflows, never for guarantees."),
  sec("Plugins package, they do not add", "The docs describe plugins as the packaging layer: a plugin bundles skills, hooks, subagents and MCP servers into one installable unit, with plugin skills namespaced like `/my-plugin:review` so several plugins can coexist; use one when the same setup is needed across repositories or for distribution through a marketplace [Claude Code docs, Extend Claude Code, 2026].",
   """
| You have | Package as | Reason |
|---|---|---|
| One repo, one team | Files in `.claude/` committed to git | No packaging needed |
| Same setup in a second repo | Plugin | The trigger the docs give |
| Setup for people outside your org | Plugin in a marketplace | Distribution |

A plugin adds no new capability type; each component inside it is one of the menu items above.
""",
   ("Premature packaging", "You build a plugin and marketplace for a setup that exists in one repository and has one user.", "Wait for the stated trigger: a second repository needs the same setup."),
   "plugins are Module 5.6.", "a plugin is a container for menu items, not a menu item."),
 ],
 retrieval=[
  ("Name the packaging layer for the extensions.", "Plugins (with marketplaces for distribution)."),
  ("According to the overview, which extension is the most flexible?", "Skills."),
  ("You wrote 'never edit .env' as a skill instruction and it was ignored. Name the failure mode by its exact label.", "**Skill-for-everything.**"),
  ("Which tier decides when a hook runs, and who or what decides?", "The on-event tier; the lifecycle event itself."),
  ("You build a marketplace for a single-repo, single-user setup. Name the failure mode.", "**Premature packaging.**"),
  ("How many items does the overview's feature table list, counting artifacts?", "Ten rows: CLAUDE.md, output style, skill, subagent, dynamic workflow, cross-session messaging, code intelligence, MCP, hook, artifact."),
  ("A database connection problem is 'solved' with a paragraph in CLAUDE.md. Name the failure mode by its exact label.", "**Menu-by-habit.**"),
  ("What does a plugin's skill namespace look like in the docs' example?", "`/my-plugin:review`."),
  ("What is the context cost of a hook unless it returns output?", "Zero."),
  ("A hard rule is put in an always-on feature. Name the failure mode.", "**Tier confusion.**"),
 ],
 steps=[("List every feature you currently use in one repository", "`inventory.md`"), ("Write its job in one word each", "A job column"), ("Place each on the always-on, on-demand or on-event tier", "A tier column"),
        ("Mark any whose job does not match its feature", "Mismatch list"), ("Choose the right feature for each mismatch", "A replacement column"), ("Write one example per menu row from your own repo", "Ten examples")],
 pass_md="""
| Feature | Job | Tier | Own example | Match? |
|---|---|---|---|---|
| CLAUDE.md | Know | Always-on | "Use pnpm" | Yes |
| Skill | Workflow | On demand | `/release` | Yes |
| Skill | Guarantee (no `.env` edits) | On demand | - | No, move to hook |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Plugin listed as a capability on a par with skills | Plugins package; see **Premature packaging** |
| No tier column | Cannot detect **Tier confusion** |
""",
 verdict="The artifact passes only if every row has a job, a tier and an own-repo example, and at least one mismatch is found and re-homed.",
 resources=R(), 
 reframe="This is the craft of the menu: **one job per feature, three tiers, and packaging as a separate step.** The engineer who understands this does not ask \"how do I make Claude do this?\" — they ask \"what job is this, and which tier owns it?\"",
))

# ---------------------------------------------------------------- 5.1.2
SPECS.append(guide(M, "5.1.2", "Triggers to add each",
 thesis="Each extension has a recognisable trigger, so a setup should grow from repeated friction rather than be designed up front.",
 prove="show three real repeated frictions from your own sessions, each mapped to the extension its trigger names.",
 discipline="do not add a feature until its trigger has fired; when it has, add it the same day.",
 counter="the same triggers tell you when to update what you already have: a repeated mistake or recurring review comment is a CLAUDE.md edit, not a one-off correction [Claude Code docs, Extend Claude Code, 2026].",
 read_min=18, prove_h="1.5",
 depth=["Recite the nine triggers and their features", "Spot an untriggered or overdue feature in a real setup", "Run a weekly setup review driven by triggers"],
 deliverable="A friction log of one week with each entry mapped to a trigger row and a done/not-done mark.",
 sections=[
  sec("The nine-row trigger table", "The overview says you do not need to configure everything up front: each feature has a recognisable trigger and most teams add them in roughly the order below [Claude Code docs, Extend Claude Code, 2026].",
   """
| Trigger | Add |
|---|---|
| Claude gets a convention or command wrong twice | CLAUDE.md |
| You keep asking Claude to be shorter, explain more, or answer in the same format | Output style |
| You keep typing the same prompt to start a task | User-invocable skill |
| You paste the same playbook into chat for the third time | Skill |
| You keep copying data from a browser tab Claude cannot see | MCP server |
| Claude reads many files to find where a symbol is defined or used | Code intelligence plugin |
| A side task floods your conversation with output you will not reference again | Subagent |
| You want something to happen every time without asking | Hook |
| A second repository needs the same setup | Plugin |

[Claude Code docs, Extend Claude Code, 2026]
""",
   ("Speculative setup", "You install ten servers, five skills and three hooks in week one because they look useful, and none has a trigger behind it, so you pay context for nothing.", "Add a feature only when its row in the trigger table has fired at least once in your own work."),
   "the menu is sub-topic 5.1.1; context cost of unused features is sub-topic 5.1.8 and Module 3.1.", "the trigger comes first, the feature second."),
  sec("Counting: twice, third time", "Two rows carry numbers: a convention wrong twice, and a playbook pasted for the third time. Numbers matter because they stop you building on a single event, and stop you tolerating a tenth repeat.",
   """
| Event count | What the docs imply |
|---|---|
| 1 | Correct it in chat |
| 2 (convention or command wrong) | Add to CLAUDE.md |
| 3 (playbook pasted) | Capture as a skill |
| Every time, no exceptions | Hook |

```text
# friction log entry
2026-11-24  Claude ran npm instead of pnpm   (2nd time)  -> CLAUDE.md: "Use pnpm, not npm."
2026-11-24  pasted release checklist         (3rd time)  -> /release skill
```
""",
   ("Third-paste tolerance", "You paste the same playbook into chat a fifth and sixth time because writing the skill feels like a detour.", "At the third paste, stop and write the skill; the detour is shorter than every later paste."),
   "writing the skill is Module 5.2.", "count repeats; two means rule, three means skill."),
  sec("Triggers also say when to update", "The docs state that the same triggers tell you when to update what you already have: a repeated mistake or a recurring review comment is a CLAUDE.md edit, and a workflow you keep tweaking by hand is a skill that needs another revision [Claude Code docs, Extend Claude Code, 2026].",
   """
| Signal | Edit |
|---|---|
| Same code-review comment on three pull requests | CLAUDE.md or a rule |
| You hand-edit a skill's output the same way each run | Revise the skill |
| A hook blocks something you now want | Revise the hook |
""",
   ("Chat-only correction", "You fix the same mistake in conversation every session and never write the correction down, so it recurs forever.", "Convert every repeated correction into a file edit the same day."),
   "memory files and rules are sub-topic 5.1.4 and Module 3.2.", "a repeated correction belongs in a file."),
 ],
 retrieval=[
  ("After how many wrong attempts does the table say to add a convention to CLAUDE.md?", "Twice."),
  ("On which paste of a playbook does the table say to capture it as a skill?", "The third."),
  ("You keep fixing the same mistake in chat each session. Name the failure mode by its exact label.", "**Chat-only correction.**"),
  ("Which trigger leads to a subagent?", "A side task floods your conversation with output you will not reference again."),
  ("You installed many servers and hooks with no triggers. Name the failure mode.", "**Speculative setup.**"),
  ("Which trigger leads to an MCP server?", "You keep copying data from a browser tab Claude cannot see."),
  ("You paste a playbook for the fifth time. Name the failure mode by its exact label.", "**Third-paste tolerance.**"),
  ("How many rows does the trigger table have?", "Nine."),
  ("What trigger leads to a plugin?", "A second repository needs the same setup."),
  ("What does a recurring review comment indicate?", "A CLAUDE.md edit."),
 ],
 steps=[("Keep a friction log for one working week", "`friction.md`"), ("Map each entry to a trigger row", "Mapping column"), ("Count repeats per entry", "Counts"), ("Apply the feature for any entry at its threshold", "Edits or new files"),
        ("Re-run the same task once to see if friction dropped", "Before/after note"), ("List features you have with no trigger behind them", "Candidate removals")],
 pass_md="""
| Date | Friction | Count | Trigger row | Action |
|---|---|---|---|---|
| 24 Nov | Used npm not pnpm | 2 | Convention wrong twice | CLAUDE.md line added |
| 24 Nov | Release checklist pasted | 3 | Playbook third time | `/release` skill |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Entries without counts | Cannot tell **Third-paste tolerance** from first occurrence |
| Actions are 'add MCP server' with no friction behind them | **Speculative setup** |
""",
 verdict="The artifact passes only if each action is tied to a counted friction and at least one existing feature without a trigger is flagged.",
 resources=R(),
 reframe="This is the craft of triggers: **friction counted, then one feature added.** The engineer who understands this does not ask \"what should I install?\" — they ask \"what has annoyed me twice?\"",
))

# ---------------------------------------------------------------- 5.1.3
SPECS.append(guide(M, "5.1.3", "Skill vs subagent",
 thesis="A skill is reusable content loaded into a context; a subagent is an isolated worker with its own context; they combine in two documented ways.",
 prove="for three tasks, choose skill, subagent or both and justify the choice by context-window impact.",
 discipline="ask where the intermediate work should live: in your window (skill) or out of it (subagent).",
 counter="a subagent is not simply 'a skill that runs by itself': it has a separate window with its own input and output tokens, which is its whole point [Claude Code docs, Extend Claude Code, 2026].",
 read_min=20, prove_h="2",
 depth=["State the comparison table and the two combine patterns", "Choose between them for a stated task and defend it", "Design a skill that forks and a subagent that preloads skills"],
 deliverable="A decision sheet for five tasks with choice, reason and the combine pattern used (if any).",
 sections=[
  sec("The comparison", "The docs frame the difference as content versus worker: skills are reusable content you can load into any context; subagents are isolated workers that run separately from your main conversation [Claude Code docs, Extend Claude Code, 2026].",
   """
| Aspect | Skill | Subagent |
|---|---|---|
| What it is | Reusable instructions, knowledge or workflows | Isolated worker with its own context |
| Key benefit | Share content across contexts | Context isolation; only a summary returns |
| Context-window impact | Adds to your main window | Separate window with its own input and output tokens |
| Best for | Reference material, invocable workflows | Many-file reads, parallel work, specialised workers |

[Claude Code docs, Extend Claude Code, 2026]
""",
   ("Worker-by-skill", "You write a skill to do a 40-file investigation, and every file read lands in your main window, which fills with material you will never reference again.", "Route many-file investigations through a subagent so only the summary enters your conversation."),
   "subagents are Module 5.3; skills Module 5.2; context windows Module 3.1.", "skills add to your window; subagents keep their work out of it."),
  sec("Reference skills and action skills", "The docs add that skills can be reference (knowledge used throughout a session, such as an API style guide) or action (tell Claude to do something specific, such as `/deploy`) [Claude Code docs, Extend Claude Code, 2026]. A subagent, by contrast, is chosen for isolation.",
   """
| Need | Choice | Why |
|---|---|---|
| Claude should know our API style all session | Reference skill | Knowledge in your window |
| Run the deploy checklist when I say so | Action skill | A workflow you trigger |
| Read 60 files and report where auth is wrong | Subagent | Intermediate output not needed |
| Review a file with a fresh, unbiased reader | Subagent | Separate context |
""",
   ("Reference-as-worker", "You spin up a subagent just to apply a style guide, so the guide, the code and the result are all invisible to your main session and have to be re-explained.", "Use a reference skill when the knowledge must stay in the conversation you are working in."),
   "the choice of when to use subagents is sub-topic 5.3.11.", "if you need to see the work, do not isolate it."),
  sec("The two ways they combine", "The docs give two combinations: a subagent can preload specific skills through its `skills:` field, and a skill can run in an isolated context with `context: fork` [Claude Code docs, Extend Claude Code, 2026]. The skills reference adds that with `context: fork` the `agent` field picks the subagent type, defaulting to general-purpose [Claude Code docs, Skills, 2026].",
   """
```yaml
# skill that forks
---
name: pr-summary
description: Summarize changes in a pull request
context: fork
agent: Explore
allowed-tools: Bash(gh *)
---
```

| Direction | Field | Effect |
|---|---|---|
| Subagent uses skills | `skills:` in the agent file | Full skill content preloaded at launch |
| Skill uses a subagent | `context: fork`, optional `agent:` | Skill body becomes the task for a forked worker |

[Claude Code docs, Skills, 2026 (YAML example shown there)]
""",
   ("Fork-without-task", "You mark a skill `context: fork` but its body is only reference guidelines with no task, so the forked worker has nothing to act on and returns nothing useful.", "Fork only skills whose body contains an explicit task; keep guideline-only skills in the main context."),
   "frontmatter is sub-topic 5.2.3 in Module 5.2; preloading is sub-topic 5.2.10.", "combine by preloading skills into agents or forking skills into agents."),
 ],
 retrieval=[
  ("Which of skill and subagent has its own context window?", "The subagent."),
  ("You wrote a skill that reads 40 files and your window filled. Name the failure mode by its exact label.", "**Worker-by-skill.**"),
  ("Name the frontmatter field by which a subagent preloads skills.", "`skills:`."),
  ("Name the frontmatter setting by which a skill runs isolated.", "`context: fork`."),
  ("A subagent was used only to apply a style guide. Name the failure mode.", "**Reference-as-worker.**"),
  ("What does a forked skill default to for `agent` when none is given?", "general-purpose."),
  ("A forked skill's body has no task. Name the failure mode by its exact label.", "**Fork-without-task.**"),
  ("What returns to the main conversation from a subagent?", "A summary."),
  ("Name the two kinds of skill the docs describe.", "Reference and action."),
  ("How many combine patterns does the comparison give?", "Two."),
 ],
 steps=[("List five tasks from your own work", "Task list"), ("Decide skill, subagent or both for each", "Choice column"), ("Estimate whether the intermediate output matters to you", "Yes/no"), ("Write one forking skill and one agent with `skills:`", "Two files"),
        ("Run each and compare main-window growth with `/context`", "Two measurements"), ("Revise any wrong choice", "Revised sheet")],
 pass_md="""
| Task | Choice | Reason | Window effect |
|---|---|---|---|
| Review PR | Forked skill, Explore | Isolated, read-only | Summary only |
| API style | Reference skill | Needed all session | Adds to window |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| 'Subagent for everything' | **Reference-as-worker** |
| Fork on a guidelines-only skill | **Fork-without-task** |
""",
 verdict="The artifact passes only if each choice cites context impact and you measured at least one window with `/context`.",
 resources=R(),
 reframe="This is the craft of the split: **content you load versus workers you send.** The engineer who understands this does not ask \"skill or agent?\" — they ask \"do I need to see the intermediate work?\"",
))

# ---------------------------------------------------------------- 5.1.4
SPECS.append(guide(M, "5.1.4", "CLAUDE.md vs skill vs rules",
 thesis="CLAUDE.md, path-scoped rules and skills all hold instructions, but they load at different times, so the choice is a decision about when the text should cost you context.",
 prove="move three instructions to the correct home among CLAUDE.md, a rule file and a skill, and show CLAUDE.md is under 200 lines afterwards.",
 discipline="ask 'when does Claude need this?' (always, when touching these files, or on demand) before choosing a file.",
 counter="a CLAUDE.md that keeps growing is a design smell: the docs' rule of thumb is to stay under 200 lines and move reference content out [Claude Code docs, Extend Claude Code, 2026].",
 read_min=20, prove_h="2",
 depth=["State what each file type loads and when", "Place a given instruction correctly and justify", "Refactor an oversized CLAUDE.md into rules and skills"],
 deliverable="A before/after refactor of a real CLAUDE.md, with each moved block labelled by its new home and the reason.",
 sections=[
  sec("Loading is the difference", "All three store instructions; the docs distinguish them by when they load and how they are scoped [Claude Code docs, Extend Claude Code, 2026].",
   """
| Aspect | CLAUDE.md | `.claude/rules/` | Skill |
|---|---|---|---|
| Loads | Every session | Every session, or when matching files are opened | On demand, when invoked or relevant |
| Scope | Whole project | Can be scoped to file paths | Task-specific |
| Best for | Core conventions, build commands | Language- or directory-specific guidelines | Reference material, repeatable workflows |

Rules with `paths` frontmatter load only when Claude works with matching files [Claude Code docs, Extend Claude Code, 2026].
""",
   ("Everything-in-CLAUDE.md", "All guidance, including API reference and a 90-line deploy runbook, sits in one file that loads on every request.", "Keep only always-needed facts in CLAUDE.md; move the rest to rules or skills."),
   "CLAUDE.md loading is Module 3.2 and rules are Module 3.3; context cost is sub-topic 5.1.8.", "the question is when Claude needs the text."),
  sec("What belongs where", "The docs give plain placement advice: CLAUDE.md for instructions every session needs (build commands, test conventions, project architecture); rules to keep CLAUDE.md focused; skills for content Claude needs only sometimes, like API documentation or a deployment checklist triggered with `/<name>` [Claude Code docs, Extend Claude Code, 2026].",
   """
| Instruction | Home | Reason |
|---|---|---|
| "Run `pnpm test` before committing" | CLAUDE.md | Needed every session |
| "In `src/api/`, validate input with zod" | Rule with `paths: src/api/**` | Only relevant when touching those files |
| Full REST error catalogue | Skill (reference) | Needed sometimes |
| "Run the release checklist" | Skill (action) | Triggered with `/release` |
""",
   ("Scope blindness", "A rule about one directory is written into CLAUDE.md, so every session pays for guidance that matters in a small part of the tree.", "Give it a `paths` frontmatter in a rule file so it loads only with matching files."),
   "writing skills is Module 5.2.", "always-needed to CLAUDE.md, path-bound to rules, sometimes-needed to skills."),
  sec("The 200-line rule of thumb", "The docs state the rule of thumb directly: keep CLAUDE.md under 200 lines, and if it grows, move reference content to skills or split into `.claude/rules/` files; `/doctor` can propose trims for a checked-in CLAUDE.md [Claude Code docs, Extend Claude Code, 2026]. The number is a rule of thumb, not a limit enforced by the tool.",
   """
```text
before:  CLAUDE.md  412 lines  (build, style, API catalogue, deploy runbook)
after:   CLAUDE.md  74 lines   (build, test, architecture)
         .claude/rules/api.md  paths: src/api/**   (validation, error shape)
         .claude/skills/deploy/SKILL.md            (runbook, action)
         .claude/skills/api-catalogue/SKILL.md     (reference)
```
The line counts above are illustrative, not measured from a real repository.
""",
   ("Line-count worship", "You cut CLAUDE.md to 199 lines by deleting facts Claude needs every session, rather than by moving the right content out.", "Move content by when it is needed, not by how many lines remain."),
   "rules and the .claude directory are Module 3.3.", "the number is a prompt to move content, not a target to hit."),
 ],
 retrieval=[
  ("What line count does the docs' rule of thumb give for CLAUDE.md?", "Under 200 lines."),
  ("Which file type loads only when matching files are opened?", "A rules file with `paths` frontmatter."),
  ("A directory-specific rule sits in CLAUDE.md. Name the failure mode by its exact label.", "**Scope blindness.**"),
  ("A 412-line CLAUDE.md holds a runbook and API catalogue. Name the failure mode.", "**Everything-in-CLAUDE.md.**"),
  ("Which command proposes trims for a checked-in CLAUDE.md?", "`/doctor`."),
  ("You cut to 199 lines by deleting always-needed facts. Name the failure mode by its exact label.", "**Line-count worship.**"),
  ("Where does a deployment checklist triggered with a slash command belong?", "A skill."),
  ("Where do build commands belong?", "CLAUDE.md."),
  ("When do skills load, by default?", "Descriptions at session start; full content on demand."),
  ("How many homes does this sub-topic compare?", "Three: CLAUDE.md, rules, skills."),
 ],
 steps=[("Count the lines of a real CLAUDE.md", "Number"), ("Label each block: always, path-bound, sometimes", "Labels"), ("Move path-bound blocks to rule files with `paths`", "Rule files"), ("Move sometimes-blocks to skills", "Skill files"),
        ("Recount CLAUDE.md and run `/doctor`", "New count, doctor output"), ("Run one task and confirm Claude still follows the moved rule", "Observation")],
 pass_md="""
| Block | Label | New home | Verified |
|---|---|---|---|
| Build and test | Always | CLAUDE.md | Yes |
| API validation | Path-bound | Rule, `paths: src/api/**` | Yes, loaded on touching a file |
| Deploy runbook | Sometimes | Skill | Invoked once |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Moved blocks never retested | Cannot show the rule still applies |
| Always-needed facts deleted to hit a number | **Line-count worship** |
""",
 verdict="The artifact passes only if every moved block was re-tested and the remaining CLAUDE.md contains only always-needed content.",
 resources=R(),
 reframe="This is the craft of instruction placement: **load time decides the home.** The engineer who understands this does not ask \"how do I shorten this file?\" — they ask \"when does Claude actually need this line?\"",
))

# ---------------------------------------------------------------- 5.1.5
SPECS.append(guide(M, "5.1.5", "Hook vs skill",
 thesis="A hook is run by Claude Code at an event whether or not Claude cooperates; a skill is read by Claude and interpreted, so guardrails belong in hooks and judgement belongs in skills.",
 prove="turn a 'never edit .env' skill instruction into a hook that blocks, and show the skill version failing once.",
 discipline="if the rule must hold every time, it is a hook; if it needs reasoning, it is a skill.",
 counter="an instruction in CLAUDE.md or a skill is 'a request, not a guarantee'; a PreToolUse hook that blocks the edit is enforcement [Claude Code docs, Extend Claude Code, 2026].",
 read_min=20, prove_h="2",
 depth=["State the five-row comparison", "Convert a prompt rule into a hook and test it", "Combine a hook that reports with a skill that fixes"],
 deliverable="One guardrail implemented twice (skill instruction and hook) with a test log showing which one held.",
 sections=[
  sec("The five differences", "Claude Code runs a hook at a lifecycle event; it loads a skill into context for Claude to apply [Claude Code docs, Extend Claude Code, 2026].",
   """
| Aspect | Hook | Skill |
|---|---|---|
| Runs | Shell command, HTTP request, MCP tool call, LLM prompt or subagent | Instructions Claude reads and follows |
| Triggered by | Lifecycle events such as `PostToolUse`, `SessionStart` | You typing `/<name>`, or Claude matching the description |
| Determinism | Fires without Claude deciding | Claude interprets; outcome can vary |
| Context cost | Zero unless the hook returns output | Description loads each session; full content when used |
| Best for | Linting after edits, blocking unsafe commands, logging, notifications | Reasoning workflows, reference, multi-step tasks |
""",
   ("Advisory guardrail", "A safety rule lives only as text in a skill, Claude weighs it against the task, and one run proceeds anyway.", "Move the rule to a PreToolUse hook that blocks the call."),
   "hooks in depth are Module 5.4; hooks as a loop-level control are Module 1.2 (sub-topic 1.2.6).", "hooks fire; skills are read."),
  sec("Guardrails are hooks", "The docs say to put guardrails in hooks: if a rule must hold every time, make it a hook rather than a prompt instruction [Claude Code docs, Extend Claude Code, 2026]. The skills page repeats this in troubleshooting: when Claude skips a rule that must hold every time, move it to a hook, optionally defined in the skill's own `hooks` frontmatter so it applies from invocation until the session ends [Claude Code docs, Skills, 2026].",
   """
```bash
#!/usr/bin/env bash
# PreToolUse hook: block edits to .env files
path=$(jq -r '.tool_input.file_path // empty')
case "$path" in
  *.env|*/.env.*) echo "Blocked: .env files are protected." >&2; exit 2 ;;
esac
exit 0
```
Exit code 2 is what blocks on events that can block; other nonzero codes are non-blocking errors [Claude Code docs, Hooks, 2026; see Module 5.4].
""",
   ("Exit-code slip", "Your guardrail hook exits 1, the tool call proceeds, and you assume the rule is enforced.", "Exit 2 (or print a JSON block decision) and test by violating the rule once."),
   "exit-code semantics are sub-topic 5.4.7.", "a guardrail is only real once you have watched it block."),
  sec("Reasoning stays in skills", "Hooks run without Claude thinking, so they suit format-on-save, rejecting `rm -rf /`, and notifying when a session ends. Skills suit a `/release` checklist, an API style guide or a debugging playbook, where Claude decides how to apply the steps [Claude Code docs, Extend Claude Code, 2026].",
   """
| Job | Right tool |
|---|---|
| Run ESLint after every edit | Hook |
| Decide how to resolve the lint results | Skill (`/fix-lint`) |
| Reject destructive shell commands | Hook |
| Walk a release, adapting to what is found | Skill |

Hook output lands in context: a PostToolUse linter hook feeds results back as text Claude reads, and a skill tells Claude how to resolve them [Claude Code docs, Extend Claude Code, 2026].
""",
   ("Script-in-prose", "You describe a deterministic command sequence in a skill and let Claude run it by hand each time, with occasional skipped steps.", "Move the fixed part into a hook or script and leave only the judgement in the skill."),
   "script-bearing skills are sub-topic 5.2.7.", "hooks do the same thing every time; skills do the thinking."),
 ],
 retrieval=[
  ("Which of hook and skill has zero context cost unless it returns output?", "The hook."),
  ("A safety rule written as text was ignored once. Name the failure mode by its exact label.", "**Advisory guardrail.**"),
  ("Which exit code blocks a PreToolUse hook?", "2."),
  ("Your hook exits 1 and the call proceeds. Name the failure mode.", "**Exit-code slip.**"),
  ("Where does the docs' 'put guardrails in' advice point?", "Hooks."),
  ("A deterministic command sequence is left to Claude in prose. Name the failure mode by its exact label.", "**Script-in-prose.**"),
  ("Name two example jobs the docs give for hooks.", "Format on save, rejecting `rm -rf /`, posting a Slack message when a session ends."),
  ("How can a skill carry its own hook?", "Through `hooks` frontmatter; it applies from invocation until the session ends."),
  ("How many hook handler types does the comparison list?", "Five: shell command, HTTP request, MCP tool call, LLM prompt, subagent."),
  ("Which event feeds linter output back to Claude?", "PostToolUse."),
 ],
 steps=[("Write the rule as a skill instruction", "`SKILL.md` line"), ("Provoke the violation five times and record results", "Tally"), ("Write the hook version", "`guard.sh`"), ("Register it on PreToolUse", "Settings entry"),
        ("Provoke the violation the same number of times", "Tally"), ("Record which held and the exit code", "Comparison table")],
 pass_md="""
| Version | Violations tried | Blocked | Notes |
|---|---|---|---|
| Skill text | 5 | 3 | Two slipped through |
| Hook, exit 2 | 5 | 5 | stderr shown to Claude |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Hook exits 1 | **Exit-code slip** |
| Hook never provoked | No evidence it works |
""",
 verdict="The artifact passes only if both versions were provoked the same number of times and the hook's block was observed.",
 resources=R(),
 reframe="This is the craft of enforcement: **requests go in prose, guarantees go in hooks.** The engineer who understands this does not ask \"how do I word this rule?\" — they ask \"what happens if Claude ignores it?\"",
))

# ---------------------------------------------------------------- 5.1.6
SPECS.append(guide(M, "5.1.6", "MCP vs skill",
 thesis="MCP supplies the connection and the tools; a skill supplies the knowledge of how to use them well; the strongest pattern is both together.",
 prove="pair one MCP server with a skill that documents its schema and query patterns and show a task done better with both than with either alone.",
 discipline="separate 'can Claude reach it' (MCP) from 'does Claude know how we use it' (skill).",
 counter="a skill cannot give Claude access to a system, and an MCP server cannot teach Claude your team's conventions for using it [Claude Code docs, Extend Claude Code, 2026].",
 read_min=18, prove_h="2",
 depth=["State what MCP provides versus a skill", "Decide for a stated integration which part is MCP and which is skill", "Design a Skill + MCP pair and a Hook + MCP pair"],
 deliverable="A paired MCP server and skill for one real system, with a before/after of one task.",
 sections=[
  sec("Different problems", "The docs state it plainly: MCP connects Claude to external services; skills extend what Claude knows, including how to use those services effectively [Claude Code docs, Extend Claude Code, 2026].",
   """
| Aspect | MCP | Skill |
|---|---|---|
| What it is | Protocol for connecting to external services | Knowledge, workflows, reference material |
| Provides | Tools and data access | Knowledge, workflows, reference |
| Examples | Slack integration, database queries, browser control | Code review checklist, deploy workflow, API style guide |
""",
   ("Instructions-as-connector", "You write a long skill explaining how to query the production database but never connect a server, so Claude can describe a query and cannot run one.", "Add the MCP server for access; keep the skill for schema and conventions."),
   "adding servers is Module 5.5; skills are Module 5.2.", "connection is MCP; knowledge is a skill."),
  sec("Both together", "The docs call these complementary: MCP gives purpose-built tools with connection and authentication handled by the server, and a skill might include your team's database schema and query patterns or a `/post-to-slack` workflow with your formatting rules [Claude Code docs, Extend Claude Code, 2026].",
   """
| Layer | Holds |
|---|---|
| MCP server | `query` tool, auth, connection |
| Skill | Table meanings, join patterns, "never SELECT * on events" |
| Result | Claude can run queries and writes them the way your team does |

The combine table lists the pattern as Skill + MCP: MCP provides the connection, a skill teaches Claude to use it well [Claude Code docs, Extend Claude Code, 2026].
""",
   ("Tool-only integration", "A server is connected and nothing teaches the schema, so Claude guesses table names and burns turns on failed queries.", "Write a skill with the schema, naming conventions and two example queries."),
   "tool search and context costs are sub-topic 5.5.5; MCP security is sub-topic 5.5.13.", "ship the skill with the server."),
  sec("Hook plus MCP", "The docs also list Hook + MCP: a hook triggers external actions through MCP, for example a post-edit hook that sends a Slack notification when Claude modifies critical files [Claude Code docs, Extend Claude Code, 2026]. This uses MCP for action, but without the model deciding to act.",
   """
| Pattern | Who decides to act |
|---|---|
| Skill + MCP | Claude, guided by the skill |
| Hook + MCP | The event; no model choice |
""",
   ("Notification-by-hope", "You ask Claude in prose to post to Slack whenever it edits a critical file, and some edits go unannounced.", "Use a hook on the edit event that calls the MCP tool."),
   "hooks are Module 5.4; mcp_tool handler is sub-topic 5.4.4.", "choose Claude-decides or event-decides, then wire MCP accordingly."),
 ],
 retrieval=[
  ("Which of MCP and skill provides tools and data access?", "MCP."),
  ("A skill explains queries but no server is connected. Name the failure mode by its exact label.", "**Instructions-as-connector.**"),
  ("A server is connected but the schema is not documented. Name the failure mode.", "**Tool-only integration.**"),
  ("Name the docs' example of a skill that goes with a Slack server.", "A `/post-to-slack` workflow with your team's message formatting rules."),
  ("Which combine pattern triggers external actions on an event?", "Hook + MCP."),
  ("You rely on a prose instruction to post to Slack on critical edits. Name the failure mode by its exact label.", "**Notification-by-hope.**"),
  ("How many combine patterns does the docs' table list?", "Four: Skill + MCP, Skill + Subagent, CLAUDE.md + Skills, Hook + MCP."),
  ("Who handles authentication in the docs' description of MCP?", "The server."),
  ("Which gives Claude knowledge of how to use a service well?", "A skill."),
  ("What does a database skill typically hold?", "Schema and query patterns."),
 ],
 steps=[("Pick one external system you use", "System name"), ("Connect it with an MCP server", "`claude mcp add` result"), ("Run one task with the server only and log the errors", "Error count"), ("Write the skill: schema, conventions, two queries", "`SKILL.md`"),
        ("Rerun the same task and compare errors", "Second count"), ("Add one hook if an action must always follow", "Hook entry")],
 pass_md="""
| Setup | Failed queries | Turns | Notes |
|---|---|---|---|
| MCP only | 4 | 9 | Guessed table names |
| MCP + skill | 0 | 4 | Used documented joins |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Only a skill, no server | **Instructions-as-connector** |
| Counts are asserted, not logged | No evidence |
""",
 verdict="The artifact passes only if both runs have logged counts and the skill content is specific to the system.",
 resources=R(),
 reframe="This is the craft of pairing: **MCP is the hand, the skill is the know-how.** The engineer who understands this does not ask \"MCP or skill?\" — they ask \"which half is missing?\"",
))

# ---------------------------------------------------------------- 5.1.7
SPECS.append(guide(M, "5.1.7", "How features layer",
 thesis="The same feature defined at several levels resolves by one of three rules, additive, override-by-name or merge, and you must know which rule applies before you debug a conflict.",
 prove="predict the outcome of a same-name conflict for a skill, a subagent, an MCP server and a hook, then confirm each in a real session.",
 discipline="before debugging a 'wrong version' problem, name the feature's layering rule.",
 counter="hooks do not override: all registered hooks fire for matching events regardless of source, so a project hook cannot cancel a user hook [Claude Code docs, Extend Claude Code, 2026].",
 read_min=22, prove_h="2.5",
 depth=["State the layering rule for each feature", "Predict a conflict outcome including priority order", "Design a team setup that avoids silent shadowing"],
 deliverable="A conflict matrix for four features with predicted and observed winners.",
 sections=[
  sec("Four rules", "The docs describe layering for features defined at user, project, plugin or managed levels [Claude Code docs, Extend Claude Code, 2026].",
   """
| Feature | Rule | Detail |
|---|---|---|
| CLAUDE.md files | Additive | All levels contribute at once; conflicts are reconciled by Claude's judgement |
| Skills | Override by name | Managed > user > project; plugin skills are namespaced |
| Subagents | Override by name | Managed > CLI flag > project > user > plugin |
| MCP servers | Override by name | Local > project > user |
| Hooks | Merge | All registered hooks fire |

[Claude Code docs, Extend Claude Code, 2026]
""",
   ("Rule-swap", "You assume subagents rank like MCP servers (local over project over user) and debug a shadowed agent for an hour.", "Look up the rule for that feature specifically; the orders differ."),
   "scopes in settings are Module 4.1; MCP scopes are sub-topic 5.5.3.", "each feature has its own rule; look it up."),
  sec("Skill priority in detail", "The skills reference gives a fuller table: enterprise, personal, project, nested, additional-directory and plugin levels, with enterprise overriding personal and personal overriding project; your skill replaces a bundled skill or built-in command of the same name but not its aliases; added-directory clashes get a prefix such as `/cli:verify` (v2.1.309+) [Claude Code docs, Skills, 2026]. The overview's shorter statement is 'managed > user > project'; the two are consistent, with the skills page adding the nested and added-directory cases.",
   """
| Clash | Winner |
|---|---|
| Personal `deploy` vs project `deploy` | Personal |
| Your `review` vs bundled skill of same name | Yours |
| Skill vs `.claude/commands/` file, same name | The skill |
| Two plugins both ship `review` | No clash: `/a:review`, `/b:review` |
""",
   ("Silent shadowing", "A personal skill with the same name as a project skill quietly replaces it for you, so you and your teammates run different procedures under one name.", "Give team skills distinctive names or ship them in a plugin, and check with `/skills`."),
   "skills are Module 5.2 (sub-topic 5.2.2 covers locations).", "same name means one wins; know which."),
  sec("MCP and hook conflicts", "Same-name MCP servers resolve local over project over user [Claude Code docs, Extend Claude Code, 2026]. Hooks differ: they all fire. If two hooks both match, both run, so a blocking one still blocks even when another allows.",
   """
```text
settings.json (user)     PreToolUse: Bash -> audit.sh        # runs
.claude/settings.json    PreToolUse: Bash -> block-rm.sh     # runs too
```
Both run; if `block-rm.sh` exits 2, the call is blocked regardless of `audit.sh`.
""",
   ("Cancel-by-override", "You expect a project hook to replace a user hook on the same event and are surprised when both fire.", "Remove or edit the unwanted hook at its own level; overriding does not apply to hooks."),
   "hook configuration is sub-topic 5.4.2.", "hooks add up; they never cancel each other."),
 ],
 retrieval=[
  ("What is the skills priority order in the overview?", "Managed > user > project."),
  ("What is the subagent priority order?", "Managed > CLI flag > project > user > plugin."),
  ("What is the MCP server resolution order?", "Local > project > user."),
  ("You expect a project hook to replace a user hook. Name the failure mode by its exact label.", "**Cancel-by-override.**"),
  ("You applied the MCP order to subagents. Name the failure mode.", "**Rule-swap.**"),
  ("Teammates run different procedures under one skill name. Name the failure mode by its exact label.", "**Silent shadowing.**"),
  ("Which feature's files are additive?", "CLAUDE.md."),
  ("How do plugin skills avoid conflicts?", "They are namespaced, e.g. `/my-plugin:review`."),
  ("From which version does the added-directory prefix (e.g. `/cli:verify`) apply?", "v2.1.309+."),
  ("Which feature merges?", "Hooks."),
 ],
 steps=[("Create same-name items at two levels for a skill, an MCP server and a hook", "Test fixtures"), ("Predict each winner from the docs", "Prediction table"), ("Run and observe", "Observed table"), ("Explain any mismatch", "Notes"),
        ("Rename to remove shadowing", "Renames"), ("Record the rule per feature on one card", "Layering card")],
 pass_md="""
| Feature | Predicted | Observed | Match |
|---|---|---|---|
| Skill `deploy` (user vs project) | User | User | Yes |
| MCP `db` (local vs project) | Local | Local | Yes |
| Hook (user + project) | Both fire | Both fired | Yes |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Prediction column filled after observing | Not a prediction |
| Hook row says 'project wins' | **Cancel-by-override** |
""",
 verdict="The artifact passes only if predictions were written before the run and every mismatch is explained.",
 resources=res([
  ("Anthropic", "Extend Claude Code", "Layering summary", "Current"),
  ("Anthropic", "Skills reference", "Fine-grained skill priority", "Current"),
 ], "the overview gives skills priority as managed > user > project, while the skills page lists six levels; they are consistent, the skills page is more detailed."),
 reframe="This is the craft of layering: **additive, override, merge.** The engineer who understands this does not ask \"why is the wrong one running?\" — they ask \"which rule does this feature follow?\"",
))

# ---------------------------------------------------------------- 5.1.8
SPECS.append(guide(M, "5.1.8", "Context costs",
 thesis="Every extension spends some of Claude's context, each in a different way, so a setup is judged by what it loads at start and on every request, not by how many features it has.",
 prove="measure your setup with /context and trim one item without losing a needed capability.",
 discipline="treat context as a budget and ask what each feature costs on every request.",
 counter="too much configuration does not just fill the window; it adds noise that makes Claude less effective, so skills may not trigger and conventions may be lost [Claude Code docs, Extend Claude Code, 2026].",
 read_min=22, prove_h="2",
 depth=["State when each feature loads and what it loads", "Measure and rank your setup's costs", "Trim a setup to its triggered features"],
 deliverable="A cost table for your own setup with measured sizes from `/context` and a trimmed version.",
 sections=[
  sec("The cost table", "The docs give each feature a loading strategy and a cost [Claude Code docs, Extend Claude Code, 2026].",
   """
| Feature | When it loads | What loads | Cost |
|---|---|---|---|
| CLAUDE.md | Session start | Full content | Every request |
| Output styles | Session start, and on switch | Active style's instructions (nothing for Default) | Every request |
| Skills | Session start, and when used | Descriptions at start; full content when used | Low (descriptions every request) |
| MCP servers | Session start | Tool names; full schemas on demand | Low until a tool is used |
| Code intelligence | After edits, on demand | Diagnostics; symbol locations | Low; can reduce file reads |
| Subagents | When spawned | Fresh context with specified skills (or the parent conversation for a fork) | Isolated from main session |
| Hooks | On trigger | Nothing | Zero unless output is returned |
""",
   ("Free-feature assumption", "You treat skills and MCP servers as free because they load on demand, then add forty skills whose descriptions all load every request.", "Count descriptions and tool names as a standing cost and prune with `/skill-doctor` and `/context`."),
   "context windows are Module 3.1; managing sessions is Module 2.4.", "descriptions and names are a standing cost."),
  sec("What you can switch off", "Setting `disable-model-invocation: true` in a skill keeps its description out of Claude's context, so a user-only skill costs nothing until invoked; for a skill you did not write, `skillOverrides` in settings does the same [Claude Code docs, Extend Claude Code, 2026]. The skills page adds that the listing has a budget of 1% of the model's context window, descriptions are dropped starting from least-invoked skills when it overflows, and each entry's combined `description` and `when_to_use` is capped at 1,536 characters [Claude Code docs, Skills, 2026].",
   """
| Knob | Effect |
|---|---|
| `disable-model-invocation: true` | Description not loaded; you invoke manually |
| `skillOverrides` set to `"name-only"` | Listed without description |
| `skillListingBudgetFraction` | Raises or lowers the 1% listing budget |
| `/doctor` | Estimates listing cost and biggest contributors |
| `/context all` | Shows tokens per loaded MCP tool |
""",
   ("Silent description loss", "You install many skills and the listing overflows, so Claude Code drops descriptions and the skills you rarely use stop matching without any error.", "Run `/doctor`, trim or hide low-value skills and put the key use case first in each description."),
   "skill management is sub-topic 5.2.9.", "overflow removes descriptions, not names."),
  sec("Isolation and zero-cost features", "Subagents run in fresh context and the docs say their isolation keeps your main session lean; hooks cost nothing unless they return output [Claude Code docs, Extend Claude Code, 2026]. Code intelligence is described as low cost because symbol lookups often replace broad file reads, so net context can go down.",
   """
| If you want to cut cost, prefer | Because |
|---|---|
| Subagent for noisy side tasks | Work stays out of the main window |
| Hook for side effects | Nothing loads |
| Code intelligence plugin in typed codebases | Lookups replace file reads |
| `/mcp` disconnect for idle servers | Fewer tool names loaded |
""",
   ("Chatty hook", "A hook prints a long report on every tool call and that output becomes messages in your conversation, defeating the zero-cost property.", "Return output only when action is needed; log elsewhere."),
   "hooks are Module 5.4; code intelligence is Module 5.8.", "isolation and silence are the cheapest features."),
 ],
 retrieval=[
  ("What share of the model's context window is the skills listing budget, per the skills page?", "1%."),
  ("What is the per-entry cap on combined description and when_to_use text?", "1,536 characters."),
  ("You added 40 skills and rarely-used ones stopped matching. Name the failure mode by its exact label.", "**Silent description loss.**"),
  ("Which setting keeps a skill's description out of context?", "`disable-model-invocation: true`."),
  ("A hook prints a long report on every call. Name the failure mode.", "**Chatty hook.**"),
  ("You believed on-demand features are free. Name the failure mode by its exact label.", "**Free-feature assumption.**"),
  ("What loads for MCP servers at session start?", "Tool names and server instructions; full schemas are deferred."),
  ("Which command shows tokens per loaded MCP tool?", "`/context all`."),
  ("Which feature is isolated from the main session's context?", "Subagents."),
  ("Which command estimates the skill listing's context cost?", "`/doctor`."),
 ],
 steps=[("Run `/context` in a fresh session", "Baseline numbers"), ("Run `/doctor` and note the listing cost", "Doctor output"), ("Rank features by size", "Ranking"), ("Trim one: hide a skill, disconnect a server or shorten CLAUDE.md", "Change"),
        ("Rerun `/context`", "New numbers"), ("Confirm the removed capability was not needed this week", "Note")],
 pass_md="""
| Item | Before | After | Action |
|---|---|---|---|
| CLAUDE.md | 5.1k tok | 1.4k tok | Moved reference to skill |
| Skills listing | 3.0k tok | 1.9k tok | 6 skills name-only |
(figures illustrative of the format, not measured)
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| No before/after numbers | Cannot show a saving |
| Removed a skill still in weekly use | Cost saved, value lost |
""",
 verdict="The artifact passes only if both numbers come from `/context` or `/doctor` runs on your own setup.",
 resources=R(),
 reframe="This is the craft of the context budget: **standing costs versus on-demand costs.** The engineer who understands this does not ask \"what else can I add?\" — they ask \"what is this already costing every request?\"",
))

if __name__ == "__main__":
    run(SPECS)
