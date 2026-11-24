# The Complete Claude Code Mastery Curriculum

A from-scratch, navigable master map of everything there is to know about Claude Code, from first install to building your own agents and running it across an organisation. No time limit. Jump to any Part, Module, numbered Topic or micro-topic.

**Source and freshness:** built from Anthropic's official Claude Code documentation (code.claude.com/docs) as it stood in autumn 2026. Claude Code ships changes almost weekly, so treat every command, flag and setting as something to verify. The fastest ways to stay current: the weekly What's New digest and the changelog in the docs, the /release-notes command inside Claude Code, and /help. Items the docs mark as research preview or experimental (for example agent view and agent teams) can change or disappear.

## How to use this document

- **Navigation:** open the outline and jump by heading. Numbering runs Part N, Module N.M, Topic N.M.K. Micro-topics sit after the colon on each topic line.
- **Each module has** a depth target, a prove-it exercise, and the official docs pages to read.
- **It is not linear.** Use an entry path below, then follow gaps.
- **Parts 1 to 3** are the foundations. **Parts 4 to 6** are control, extension and scale. **Parts 7 to 8** are surfaces, integrations and the Agent SDK. **Parts 9 to 12** are applied engineering, enterprise, security and troubleshooting. **Parts 13 to 18** are the mastery paths for non-engineers, quick references, projects, a library, drills and the frontier.

### Entry paths

- **Path A, Productive in a week:** Part 1 (1.1 to 1.3), Part 2, Part 3 (3.1 to 3.3), then Part 5.1 and 5.2.
- **Path B, Power user:** Parts 3, 4, 5 and 6 in order, with Part 14 beside you as a reference.
- **Path C, Builder of agents and tools:** Part 5 (skills, hooks, MCP, plugins), Part 8 (Agent SDK), Part 11 (security), Part 15 projects.
- **Path D, Team lead or admin:** Part 10, Part 11, Part 6.5 and 6.6, Part 7.6, Part 9.12.
- **Path E, Product manager or non-engineer:** Part 1, Part 2, Part 3.1, Part 13, then Parts 5 and 9 selectively.

### Mastery levels

- **L1 Aware:** you recognise the term.
- **L2 Conversant:** you can explain it simply and use it with guidance.
- **L3 Fluent:** you use it unprompted in real work and can debug it.
- **L4 Authoritative:** you can configure it for a team, teach it, and critique other setups.
- **L5 Frontier:** you build new tooling on top of it (plugins, mods, SDK products) and your methods get copied.

### The learning method that applies to every topic

1. **Read the official page first,** then try it in a throwaway repository.
2. **Break it on purpose** (a wrong permission, a failing hook, a bloated context) to learn how it fails.
3. **Keep a personal playbook:** every time Claude Code does something wrong twice, decide whether the fix belongs in CLAUDE.md, a skill, a hook, a setting, or your own prompting habit.
4. **Measure:** use /usage, /context and /insights to see where time and tokens go.
5. **Teach it:** write a short guide or demo for a teammate. Gaps appear immediately.
6. **Revisit monthly:** read the What's New digests and delete setup you no longer need.

### Master map

| Part | Name |
| --- | --- |
| 1 | Foundations and mental model |
| 2 | Core workflows |
| 3 | Context engineering and memory |
| 4 | Configuration, permissions and control |
| 5 | The extension layer: skills, subagents, hooks, MCP, plugins |
| 6 | Parallel and autonomous work |
| 7 | Surfaces and integrations |
| 8 | The Agent SDK |
| 9 | Applied engineering with Claude Code |
| 10 | Enterprise, administration and cost |
| 11 | Security and safe operation |
| 12 | Troubleshooting and debugging |
| 13 | Claude Code for product managers and non-engineers |
| 14 | Quick reference: commands, shortcuts, flags, files |
| 15 | Project ladder |
| 16 | Library: docs map, reading and watching |
| 17 | Mastery drills and question banks |
| 18 | The frontier: what comes next |

---

## Part 1: Foundations and mental model

### Module 1.1 What Claude Code is

*Depth target: L3. Prove-it: explain to a colleague, in two minutes, how Claude Code differs from a chatbot and from autocomplete.*

- **1.1.1 Definition:** an agentic coding tool that reads your codebase, edits files, runs commands and integrates with your development tools
- **1.1.2 Chatbot vs agent:** a chatbot answers and waits; an agent plans, acts, observes results and loops until done or blocked
- **1.1.3 Where it runs:** terminal CLI, IDE extensions, desktop app, browser and mobile (cloud sessions), plus integrations such as Chrome, Slack, GitHub Actions and GitLab CI/CD
- **1.1.4 Same engine, many surfaces:** hooks, skills, settings, MCP and CLAUDE.md work across surfaces, with differences in availability (see Part 7 and the feature-availability page)
- **1.1.5 Delegate, do not dictate:** the working relationship the docs recommend: state the outcome and the check, let Claude choose the steps
- **1.1.6 What it is not:** not a replacement for tests, code review, version control or judgement; the model can be confidently wrong

*Read:* Overview, Quickstart, How Claude Code works, Glossary.

### Module 1.2 How Claude Code works: the agentic loop

*Depth target: L3. Prove-it: draw the loop from memory and mark where permissions, hooks and compaction act.*

- **1.2.1 The loop:** gather context, take action, verify results, repeat; you can interrupt at any point
- **1.2.2 Built-in tools:** reading and searching files, editing and writing files, running shell commands (Bash, and PowerShell on Windows), web fetch and search, task tracking, asking you questions, language-server lookups when a code intelligence plugin is installed
- **1.2.3 Tool permissions:** every tool call passes through the permission system (Part 4)
- **1.2.4 The system prompt and tool results:** what the model sees each turn; why long outputs matter
- **1.2.5 Subagents and background work:** separate loops with their own context returning summaries
- **1.2.6 Hooks in the loop:** lifecycle events before and after tool calls, prompts, compaction and stopping
- **1.2.7 Sessions as transcripts:** conversations are saved locally and are resumable and branchable
- **1.2.8 The model layer:** different models and effort levels trade speed, cost and depth (see Module 4.6)

*Read:* How Claude Code works, Tools reference, Explore the context window.

### Module 1.3 Installation, authentication and first run

- **1.3.1 Requirements and install:** follow the Quickstart and Advanced setup pages for the current installer, supported operating systems (macOS, Linux, Windows including native Windows and WSL), version management and uninstall
- **1.3.2 Sign-in options:** a Claude subscription (Pro, Max, Team, Enterprise), the Anthropic Console with API billing, or a cloud provider (Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, Claude Platform on AWS)
- **1.3.3 First session:** open a project folder, run claude, ask it to explain the codebase, make one small change, review the diff
- **1.3.4 Trust dialog:** what workspace trust means and what runs before a folder is trusted
- **1.3.5 Updating:** auto-update behaviour, release channels, checking your version, reading release notes with /release-notes
- **1.3.6 Learning in-product:** /powerup interactive lessons, /help, /doctor for a setup checkup
- **1.3.7 Troubleshooting install and login:** command not found, PATH, permissions, network, authentication errors

### Module 1.4 Plans, limits and billing basics

- **1.4.1 Subscription usage:** plan limits, what counts against them, the /usage breakdown
- **1.4.2 API and provider billing:** per-token pricing, spend limits, usage credits
- **1.4.3 Fast mode and effort:** how they affect cost and speed
- **1.4.4 Feature availability by plan and provider:** some features (for example auto mode, cloud sessions, Code Review) differ by plan or backend; check the feature-availability page
- **1.4.5 Cost control habits:** clear between tasks, scope searches, use subagents for exploration, choose the right model, watch /context

### Module 1.5 The Claude Code vocabulary

*Prove-it: define each term in one sentence without looking.*

- **1.5.1 Core terms:** agentic loop, context window, compaction, CLAUDE.md, auto memory, skill, subagent, hook, MCP, plugin, marketplace, mod, worktree, checkpoint, session, permission mode, sandbox, headless mode, Agent SDK, dynamic workflow, agent view, agent team, channel
- **1.5.2 Where to look:** the Glossary page

---

## Part 2: Core workflows

### Module 2.1 The explore, plan, implement, commit loop

*Depth target: L3 to L4. Prove-it: ship a multi-file feature using all four phases and a written plan.*

- **2.1.1 Explore:** ask questions you would ask a senior engineer; read code before changing it; use plan mode so nothing is edited
- **2.1.2 Plan:** have Claude write a plan, edit the plan in your own editor (the docs describe a shortcut for this), and approve it
- **2.1.3 Implement:** switch out of plan mode, let Claude code against its plan, with tests
- **2.1.4 Commit:** ask for a descriptive commit and a pull request, using the gh CLI where installed
- **2.1.5 When to skip planning:** if you can describe the diff in one sentence, ask for it directly
- **2.1.6 Spec interview pattern:** for larger features, ask Claude to interview you using its question tool, write the result to a spec file, then start a fresh session to execute it
- **2.1.7 Fresh session for execution:** a clean context focused on implementation plus a written spec beats a long meandering session

*Read:* Best practices, Common workflows, Permission modes (plan mode).

### Module 2.2 Prompting Claude Code well

*Depth target: L4.*

- **2.2.1 Be specific upfront:** name files, scenarios, constraints, testing preferences, and what is out of scope
- **2.2.2 Point to sources and patterns:** reference existing code to imitate; ask Claude to read git history for the why
- **2.2.3 Describe symptoms, not just goals:** symptom, likely location, definition of fixed
- **2.2.4 Give rich input:** reference files with the at-sign, paste or drag in screenshots and images, give documentation URLs, pipe data in with cat file piped into claude -p
- **2.2.5 Let Claude fetch:** tell it to use CLI tools, MCP tools or file reads to gather what it needs
- **2.2.6 Vague prompts on purpose:** exploratory questions like what would you improve here can surface unknown unknowns
- **2.2.7 Interrupt and steer:** press Escape to stop mid-action and redirect; correct early rather than late
- **2.2.8 Side questions:** /btw asks something without adding to the conversation history
- **2.2.9 Voice dictation:** hold-to-record or tap-to-record in the CLI via /voice
- **2.2.10 Prompt library:** the docs ship copy-paste prompts tagged by task and role

### Module 2.3 Verification: closing the loop

*Depth target: L4. This is the highest-leverage habit in the docs.*

- **2.3.1 Principle:** give Claude a check it can run (tests, build exit code, linter, script diffing against a fixture, screenshot comparison); without one you become the verification loop
- **2.3.2 Ways to gate completion:** ask in the same prompt; set a session-long /goal condition that a separate evaluator re-checks every turn; use a Stop hook that blocks finishing until a script passes; use a second opinion from a verification subagent or a workflow that tries to refute findings
- **2.3.3 Evidence over assertion:** ask for test output, commands run and screenshots rather than a claim of success
- **2.3.4 Run and verify the app:** the /run and /verify bundled skills launch and drive the project's app to see a change work, beyond tests and type checks
- **2.3.5 Root causes, not symptoms:** instruct Claude not to suppress errors; reproduce with a failing test first
- **2.3.6 Adversarial review:** have a fresh-context subagent review the diff against the plan, and tell it to report only correctness gaps to avoid over-engineering
- **2.3.7 Visual verification:** screenshots via Claude in Chrome or the desktop app preview for UI work
- **2.3.8 If you cannot verify it, do not ship it**

### Module 2.4 Session management

- **2.4.1 Resume and continue:** claude --continue, claude --resume, /resume, --from-pr, resuming by name or pull request link
- **2.4.2 Naming:** /rename, descriptive names like oauth-migration; treat sessions like branches
- **2.4.3 Branching and forking:** /branch to try another direction, /fork to copy into a background session, /subtask to hand a side task to a forked subagent
- **2.4.4 Clearing:** /clear between unrelated tasks, with an optional name for the old conversation; the rewind menu can restore a cleared conversation in the same process
- **2.4.5 Exporting and transcripts:** /export, where transcripts live on disk, privacy considerations
- **2.4.6 Recaps:** /recap and automatic recaps when you return to a terminal
- **2.4.7 Moving work:** /teleport to pull a cloud session into the terminal, /desktop to continue in the desktop app, /remote-control to continue from a phone or browser, /cd to move to another directory

### Module 2.5 Checkpoints, undo and safe experimentation

- **2.5.1 Checkpoints:** every prompt that starts a turn creates one; Claude snapshots files before edits
- **2.5.2 Rewind:** press Escape twice or run /rewind to restore conversation, code, or both, or to summarise from a chosen message
- **2.5.3 Limits:** checkpoints track only edits made through Claude's file tools, not changes made by shell commands or other processes; they do not replace git
- **2.5.4 Experiment freely:** ask for the risky approach, rewind if it fails
- **2.5.5 Git as the real safety net:** branches, small commits, worktrees for parallel attempts

### Module 2.6 Everyday engineering workflows

*Prove-it: complete each workflow once on a real repository.*

- **2.6.1 Understand a new codebase:** overview questions, find relevant code, trace a request, map dependencies
- **2.6.2 Fix bugs:** reproduce, write a failing test, fix, verify, explain the root cause
- **2.6.3 Refactor:** scope, tests first, small steps, /simplify for cleanup review
- **2.6.4 Work with tests:** generate, run, fix flaky tests, coverage gaps, avoiding over-mocking
- **2.6.5 Create pull requests:** commit hygiene, descriptions, linking issues, /autofix-pr to watch CI and reviews from a cloud session
- **2.6.6 Documentation:** READMEs, API docs, architecture notes, changelogs, docstrings
- **2.6.7 Work with images:** screenshots of bugs, design mocks, diagrams
- **2.6.8 Review changes:** /diff, /code-review (local, with an optional fix flag and effort levels), /security-review

---

## Part 3: Context engineering and memory

The docs state the central constraint plainly: Claude's context window fills fast and performance degrades as it fills. Almost every best practice follows from that.

### Module 3.1 The context window

*Depth target: L4. Prove-it: predict, then measure with /context, what a given session loads and what a file read costs.*

- **3.1.1 What fills the window:** every message, every file read, every command output, tool schemas, memory files, skill descriptions
- **3.1.2 Observing it:** /context (and its expanded form), the interactive context-window explainer in the docs, a custom status line showing context use
- **3.1.3 Degradation:** why earlier instructions get lost as context fills; why long debugging sessions get worse
- **3.1.4 Cost of features:** CLAUDE.md loads every request; skill descriptions load every request and full skill content only when used; MCP tool names load at start with schemas deferred through tool search; hooks cost nothing unless they return output; subagents run in isolated context
- **3.1.5 Managing it:** clear between tasks, compact with instructions, rewind-and-summarise, offload exploration to subagents, side questions with /btw
- **3.1.6 Auto-compact window:** how full the window gets before automatic compaction; /autocompact and the model-config page cover tuning and extended context
- **3.1.7 What survives compaction:** how rules, skills and memory files are handled; the context-window page explains it

### Module 3.2 CLAUDE.md and project instructions

*Depth target: L4. Prove-it: take a bloated CLAUDE.md, cut it by half, and show Claude's behaviour did not get worse.*

- **3.2.1 What it is:** a file Claude reads at the start of every session, for context it cannot infer from code
- **3.2.2 Where files live:** managed policy, user (home directory), project, and local personal files; nested files in subdirectories load as Claude works in them; additive across levels
- **3.2.3 Generating one:** /init for a starter, with an interactive flow that can also walk through skills, hooks and personal memory; /memory to edit
- **3.2.4 What to include:** commands Claude cannot guess, style rules that differ from defaults, test runners, repo etiquette, architectural decisions, environment quirks, non-obvious gotchas
- **3.2.5 What to exclude:** anything derivable from reading code, standard conventions, long API docs (link instead), frequently changing information, file-by-file descriptions
- **3.2.6 Size and pruning:** keep it short (the docs suggest staying under about 200 lines); for each line ask whether removing it would cause mistakes; /doctor can propose cuts
- **3.2.7 Emphasis:** use sparingly on a line that keeps being skipped; emphasising many lines makes none stand out
- **3.2.8 Imports:** pull other files in with the at-path syntax; AGENTS.md support for repositories that already use it
- **3.2.9 Treat it like code:** review it when things go wrong, check it into git, test changes by watching whether behaviour shifts
- **3.2.10 Compaction instructions:** tell Claude what to preserve when it compacts, such as modified files and test commands
- **3.2.11 Caching note:** edits to CLAUDE.md do not apply mid-session because of prompt caching; start a new session or follow the reload guidance in the docs
- **3.2.12 Prompt audit:** /doctor with the prompt-audit option audits your instructions

### Module 3.3 Rules, auto memory and the .claude directory

- **3.3.1 Rules files:** markdown files under .claude/rules, optionally scoped to file paths with frontmatter so they load only when matching files are touched
- **3.3.2 Auto memory:** Claude accumulates learnings automatically across sessions; enable, disable and inspect it with /memory
- **3.3.3 The .claude directory tour:** project and home-directory locations for CLAUDE.md, settings.json, hooks, skills, commands, subagents, workflows, rules and memory
- **3.3.4 Local versus shared:** what to commit (project settings, skills, agents, rules) and what to keep personal (local settings, personal memory)
- **3.3.5 Session scratchpad:** a per-session directory for temporary working files
- **3.3.6 InstructionsLoaded hook:** audit which instruction files load and why

### Module 3.4 Prompt caching and its consequences

- **3.4.1 What it is:** Claude Code manages prompt caching automatically to cut cost and latency
- **3.4.2 Practical effects:** a model switch triggers a slower uncached turn; compaction has a cost; changing effort level can invalidate cache; CLAUDE.md edits do not apply mid-session
- **3.4.3 Cache lifetime:** resuming an old session can mean paying to re-write context; session-start hooks can warn you
- **3.4.4 Checking your hit rate:** the prompt-caching page explains how

### Module 3.5 Large codebases and monorepos

- **3.5.1 Nested CLAUDE.md files:** per-package guidance loading on demand
- **3.5.2 Per-package skills and rules**
- **3.5.3 Code intelligence:** language-server plugins give symbol navigation and live type errors, reducing broad file reads
- **3.5.4 Sparse worktrees and scoping:** keep Claude focused on the code you are changing
- **3.5.5 Search discipline:** scoped investigations rather than open-ended explore requests
- **3.5.6 Additional directories:** /add-dir grants file access but most configuration is not discovered from added directories

### Module 3.6 Status line, output styles and interface for awareness

- **3.6.1 Custom status line:** show context use, cost, git branch, model, effort; /statusline can configure it from your shell prompt or a description
- **3.6.2 Output styles:** built-in styles such as Concise and Explanatory, and custom styles that set role, tone and format; one active at a time; /output-style
- **3.6.3 Focus and fullscreen views:** flicker-free fullscreen rendering, focus view summarising tool calls
- **3.6.4 Themes and accessibility:** colour themes including colourblind-accessible ones, screen reader mode, reduced motion

---

## Part 4: Configuration, permissions and control

### Module 4.1 Settings files and precedence

*Depth target: L4. Prove-it: for five settings, say which file you would put each in and what wins if two files disagree.*

- **4.1.1 Scopes:** user settings in your home .claude directory, project settings committed in the repo, local project settings that stay out of git, managed policy settings from an administrator, and server-delivered managed settings
- **4.1.2 Precedence:** more specific and more authoritative sources win; managed settings cannot be overridden by users; hooks merge instead of replacing
- **4.1.3 Editing:** /config opens the settings interface; /config with key=value pairs sets values directly (also in non-interactive mode); /update-config lets Claude edit the right file from a description
- **4.1.4 Reference pages:** the settings files page explains precedence; the all-settings page lists every key with type and default; the example settings page has realistic files for a developer, a team and an organisation
- **4.1.5 Checking what is in force:** /status shows setting sources; /doctor diagnoses broken settings; safe mode helps when configuration is broken
- **4.1.6 Plugin-only and strict lockdowns:** enterprise settings that restrict where hooks, skills or other customisation may come from

### Module 4.2 Permissions

*Depth target: L4. Prove-it: write a permission policy for a repository that allows tests and linting, asks for pushes, and denies reading secrets.*

- **4.2.1 The model:** rules evaluate as allow, ask or deny; deny wins; rules are scoped by tool and arguments
- **4.2.2 Rule syntax:** tool name plus optional specifier, for example a Bash command prefix pattern, a file glob for Edit or Read, a domain for web fetch, or an MCP tool name; the permissions page documents matching, including how compound shell commands are checked
- **4.2.3 Matching tool parameters in deny and ask rules** (added in mid-2026): finer control for tools beyond commands
- **4.2.4 Managing rules:** /permissions dialog (view by scope, add, remove, manage directories, review recent auto-mode denials), settings files, command-line allowed-tools flags
- **4.2.5 Reducing prompts safely:** the /fewer-permission-prompts skill scans transcripts for common read-only calls and proposes an allowlist
- **4.2.6 Additional directories:** access versus configuration discovery
- **4.2.7 Workspace trust:** what runs before you trust a folder; why project allow rules are gated by trust
- **4.2.8 Managed policies:** organisation rules that users cannot loosen
- **4.2.9 Permissions are not enforcement against a hostile model:** pair with sandboxing and hooks for hard guarantees

### Module 4.3 Permission modes

*Depth target: L4.*

- **4.3.1 The modes:** Manual (asks before edits and commands, labelled default in code), acceptEdits (auto-accept file edits, with a prompt for files that can run code), plan (read-only analysis), auto (a classifier model reviews actions), dontAsk (only pre-approved tools run, everything else is denied), bypassPermissions (no checks; for isolated environments only)
- **4.3.2 Switching:** Shift+Tab in the CLI, the mode indicator in VS Code, the selector in the desktop app, the command-line permission-mode flag, /plan to enter plan mode with a task
- **4.3.3 Plan mode:** exploring without editing; configure it as the default if you want; editing the plan in your own editor
- **4.3.4 Auto mode:** a separate classifier blocks scope escalation, unknown infrastructure and hostile-content-driven actions while letting routine work proceed; it became the built-in starting mode in interactive terminal and VS Code sessions on recent versions; behaviour differs by plan and provider
- **4.3.5 Tuning auto mode:** tell the classifier which repositories, buckets and domains your organisation trusts; override allow and block rules; hard-deny rules that block unconditionally; /auto-mode-setup drafts environment entries; auto-mode subcommands inspect the effective config
- **4.3.6 Auto mode in headless runs:** what happens when the classifier repeatedly blocks in a non-interactive run, and how it falls back
- **4.3.7 dontAsk for unattended scripts:** pair with an allowed-tools list so only approved actions run
- **4.3.8 Choosing a mode:** match the mode to risk, trust in the environment and whether you are watching

### Module 4.4 Sandboxing and isolation

*Depth target: L3 to L4.*

- **4.4.1 The sandboxed Bash tool:** OS-level restriction of file and network access for shell commands; toggled with /sandbox on supported platforms
- **4.4.2 Setting the boundary:** which paths are writable, which hosts are reachable, what to do when the sandbox breaks a legitimate command
- **4.4.3 Sandbox environments compared:** built-in sandboxed Bash, the sandbox runtime, dev containers, Docker, virtual machines; choosing by threat model
- **4.4.4 Dev containers:** running Claude Code inside a dev container for consistent, isolated team environments
- **4.4.5 Sandboxes plus permissions:** how the two layers combine to allow freer work inside a boundary
- **4.4.6 Network egress control:** why limiting outbound hosts matters for prompt injection and data exfiltration

### Module 4.5 Cloud and self-hosted environments

- **4.5.1 Cloud environments:** network access levels, environment variables, setup scripts and caching for cloud sessions
- **4.5.2 Self-hosted environments:** running cloud sessions on infrastructure you control, with runners, orchestrators, wrapper scripts for per-session credentials, lifecycle hooks, production hardening, metrics and session identity verification
- **4.5.3 Choosing where sessions run:** local for speed and access; cloud for isolation, parallelism and being away from your machine; self-hosted for compliance and internal network access

### Module 4.6 Models, effort and speed

*Depth target: L4. Prove-it: run the same task on two models and two effort levels and compare quality, time and cost.*

- **4.6.1 Choosing a model:** /model opens a picker and saves your default; a switch for the current session only is available in the picker; use aliases or full model IDs; defaults change when new models launch, so check the What's New digests
- **4.6.2 Effort levels:** low, medium, high, xhigh and max (max is session-only); /effort sets or shows the level; auto lets Claude Code choose; unsupported levels fall back to what the model supports
- **4.6.3 Ultracode and deeper modes:** the ultracode option on /effort turns on a more autonomous orchestration style for the session; see the workflows page for what it does
- **4.6.4 Extended thinking:** toggle with settings (for example /config thinking=false) and by effort level
- **4.6.5 Fast mode:** /fast toggles faster responses on supported Opus models at a different price; availability varies
- **4.6.6 Advisor tool:** pair a main model with a stronger advisor model that Claude consults at key moments; /advisor enables or disables it
- **4.6.7 Extended context and auto-compact window:** larger context options and how full the window gets before compaction
- **4.6.8 Pinning models on third-party providers:** setup wizards for Bedrock and Google Cloud's Agent Platform, model pins in settings or environment variables
- **4.6.9 Matching model to task:** cheaper, faster models for exploration and subagents; stronger models for architecture, hard debugging and review
- **4.6.10 Cost visibility:** /usage and /cost, the status line, the plan usage breakdown showing which skills, subagents and MCP servers drive limits

### Module 4.7 Interface, shortcuts and terminal setup

- **4.7.1 Interactive mode essentials:** Shift+Tab cycles permission modes; Escape interrupts; Escape twice opens rewind; Ctrl+G edits a plan or prompt in your editor; Ctrl+R searches command history; the exclamation prefix runs shell commands directly and can feed the output back; at-sign mentions files; paste or drag images; multiline input with Shift+Enter or Option+Enter depending on terminal
- **4.7.2 Terminal setup:** /terminal-setup installs a Shift+Enter binding in common terminals; bell on completion; tmux notes; colour theme matching; Vim editing mode via the editor setting; fullscreen rendering with mouse support via /tui
- **4.7.3 Keybindings:** /keybindings opens the customisable shortcuts file
- **4.7.4 Themes:** built-in, auto, colourblind-accessible and custom themes, including themes shipped in plugins
- **4.7.5 Voice dictation:** /voice
- **4.7.6 Accessibility:** screen reader mode, magnifier-friendly and reduced-motion settings
- **4.7.7 Notifications:** terminal bell and desktop notifications through hooks; mobile push notifications when Claude needs you

### Module 4.8 Command-line flags and environment variables

- **4.8.1 Launch flags worth knowing:** print mode (-p) for non-interactive runs; --continue and --resume; --permission-mode; --allowedTools; --output-format (text, json, stream-json); --verbose; --no-session-persistence; --worktree; --agent; --name; --from-pr; --fork-session; --chrome; --debug and --debug-file; --settings; --init-only
- **4.8.2 Environment variables:** the env-vars page lists variables that control behaviour, including provider selection (for example the Bedrock and Vertex switches), subprocess scrubbing, process wrapping and feature-flag fetching
- **4.8.3 Subcommands:** claude mcp (add, list, login and more), claude plugin (install, eval and more), claude agents (agent view), claude auth login, claude project purge, claude update
- **4.8.4 Reference pages:** the CLI reference, Commands, Environment variables and Tools reference pages are the source of truth; /help shows what your version supports

---

## Part 5: The extension layer: skills, subagents, hooks, MCP, plugins

Extensions plug into different points of the agentic loop. The docs recommend building your setup over time, adding each piece when a recognisable trigger appears, rather than configuring everything up front.

### Module 5.1 Choosing the right extension

*Depth target: L4. Prove-it: given ten scenarios, pick the right mechanism for each and justify it in one sentence.*

- **5.1.1 The menu:** CLAUDE.md (always-on facts and rules), output styles (role, tone, format), skills (reusable knowledge and invocable workflows), subagents (isolated workers), dynamic workflows (scripts that run many subagents), cross-session messaging, code intelligence, MCP (external services), hooks (deterministic automation on lifecycle events), artifacts (visual output), plugins (the packaging layer)
- **5.1.2 Triggers to add each:** Claude gets a convention wrong twice, so add it to CLAUDE.md; you keep typing the same prompt, so make a skill; you paste a playbook for the third time, so make a skill; you copy data from a tab Claude cannot see, so connect MCP; a side task floods your context, so use a subagent; something must happen every time, so write a hook; a second repository needs the same setup, so package a plugin
- **5.1.3 Skill vs subagent:** reusable content you load anywhere, vs an isolated worker that returns a summary; they combine (a subagent can preload skills; a skill can run in a forked context)
- **5.1.4 CLAUDE.md vs skill vs rules:** every session vs on demand vs path-scoped
- **5.1.5 Hook vs skill:** deterministic and guaranteed vs interpreted and variable; put guardrails in hooks, not prompts
- **5.1.6 MCP vs skill:** connection and tools vs knowledge about using them; the strongest pattern is both together
- **5.1.7 How features layer:** CLAUDE.md files are additive; skills and subagents override by name with a priority order; MCP servers override by name (local over project over user); hooks merge and all fire
- **5.1.8 Context costs:** each feature loads differently; see Module 3.1

*Read:* Extend Claude Code, and the blog post on steering Claude Code with skills, hooks, rules and subagents.

### Module 5.2 Skills

*Depth target: L4 to L5. Prove-it: write three skills (a reference skill, an action skill with side effects, a skill that forks into a subagent), then measure their context cost.*

- **5.2.1 What a skill is:** a folder with a SKILL.md file containing instructions, knowledge or a workflow; slash commands are now part of the skills system
- **5.2.2 Where skills live:** project (.claude/skills), personal (home .claude/skills), plugins (namespaced, for example plugin-name:skill), and managed locations; priority when names clash
- **5.2.3 Frontmatter:** name, description (what Claude matches against), disable-model-invocation (hide from Claude and run only when you invoke it, essential for workflows with side effects), context fork (run in an isolated subagent context), hooks defined in the skill, tool restrictions and other supported fields in the skills page
- **5.2.4 Writing a good description:** it is the trigger; vague or overlapping descriptions cause missed or wrong skill loads
- **5.2.5 Arguments and dynamic context:** an arguments placeholder for text after the command; injecting live shell output into the skill with the bang-backtick syntax
- **5.2.6 Invocation:** typing slash and the name; Claude loading it automatically when relevant; stacking several skills in one message (up to six)
- **5.2.7 Progressive disclosure:** keep SKILL.md focused and put long references, scripts and examples in files the skill points to
- **5.2.8 Bundled skills:** /code-review (alias /review), /simplify, /batch, /debug, /loop, /verify, /run, /run-skill-generator, /doctor, /update-config, /fewer-permission-prompts, /claude-api, /claude-in-chrome, /dataviz, /design, /design-sync, /slides, /artifact-capabilities and /artifact-diagramming, plus bundled workflows such as /deep-research; availability depends on version, plan and provider
- **5.2.9 Managing skills:** /skills lists and filters them and can change their visibility; /skill-doctor shows each skill's context cost and usage so you can switch off unused ones; /reload-skills rescans without restarting; skillOverrides in settings
- **5.2.10 Skills in subagents:** a subagent's skills field preloads full content at launch
- **5.2.11 Sharing:** commit to the repo, package into a plugin, distribute through a marketplace
- **5.2.12 Troubleshooting:** skill not triggering, frontmatter not parsing, hook limits per skill source, plugin-only lockdowns
- **5.2.13 Skill design patterns:** checklists, decision trees, templates, review rubrics, runbooks, domain glossaries, API conventions, release procedures, data-analysis recipes

*Read:* Skills, Extend Claude Code, Plugins overview.

### Module 5.3 Subagents

*Depth target: L4. Prove-it: build a read-only security-review subagent and a research subagent; compare their context cost with doing the same work in the main session.*

- **5.3.1 What they are:** specialised assistants running their own agent loop in a separate context window, returning a summary to the caller
- **5.3.2 Built-in agents:** a general-purpose agent, Explore (fast read-only codebase search) and Plan (research for plan mode); the last two omit CLAUDE.md and git status to stay lean
- **5.3.3 Custom subagents:** markdown files with frontmatter (name, description, allowed tools, model, preloaded skills, hooks, and other supported fields) in the project agents folder or your personal agents folder; also definable via a command-line flag or by plugins; priority order across scopes
- **5.3.4 Creating them:** ask Claude to create one; the older interactive manager was replaced by plain-file management
- **5.3.5 Delegation:** Claude delegates automatically based on the description, or you ask explicitly, for example use a subagent to investigate token refresh
- **5.3.6 Foreground and background:** subagents run in the background by default on recent versions; /tasks lists background work including finished subagents
- **5.3.7 Forks:** a forked subagent inherits the full conversation; /subtask spawns one; /fork copies the session into a separate background session
- **5.3.8 Nested subagents:** subagents can spawn their own subagents on recent versions
- **5.3.9 Isolation:** run a subagent in its own git worktree so edits do not collide
- **5.3.10 Hooks and permissions in subagents:** settings hooks fire inside subagents with agent identity fields; frontmatter hooks run only while that subagent runs and need workspace trust
- **5.3.11 When to use:** exploration that reads many files, parallel research, independent verification, specialised review personas, anything whose intermediate output you will not reference again
- **5.3.12 Anti-patterns:** too many tiny agents, vague descriptions, giving every agent every tool, using agents when a single grep would do
- **5.3.13 Cost and observability:** subagent tokens count toward usage; the /usage breakdown shows which subagents drive limits

### Module 5.4 Hooks

*Depth target: L4 to L5. Prove-it: build four hooks: format on edit, block a dangerous command, notify when Claude needs you, and a Stop hook that refuses to finish until tests pass.*

- **5.4.1 What hooks are:** user-defined shell commands, HTTP endpoints, MCP tool calls, LLM prompts or subagents that run automatically at lifecycle points; deterministic where CLAUDE.md is advisory
- **5.4.2 Configuration shape:** hook event, then a matcher group, then one or more handlers; set in user, project, local, managed, plugin, skill or subagent files; entries merge across levels
- **5.4.3 Events by cadence:** per session (SessionStart, SessionEnd, Setup); per turn (UserPromptSubmit, UserPromptExpansion, Stop, StopFailure); per tool call (PreToolUse, PermissionRequest, PermissionDenied, PostToolUse, PostToolUseFailure, PostToolBatch); agents and tasks (SubagentStart, SubagentStop, TaskCreated, TaskCompleted, TeammateIdle); environment (InstructionsLoaded, ConfigChange, CwdChanged, DirectoryAdded, FileChanged, WorktreeCreate, WorktreeRemove); compaction and models (PreCompact, PostCompact, PreModelSwitch, PostModelSwitch); MCP (Elicitation, ElicitationResult); display and notifications (Notification, MessageDisplay)
- **5.4.4 Handler types:** command (shell or exec form with an args list), http (POST the event JSON to a URL), mcp\_tool, prompt (single-turn model evaluation), agent (a subagent with tools to verify a condition; experimental)
- **5.4.5 Matchers:** exact names, pipe or comma lists, or regular expressions; what each event matches on (tool name, session start source, notification type, agent type, error type and so on); MCP tool names follow mcp, server, tool naming
- **5.4.6 The if filter:** a permission-rule-style condition on tool events so a handler spawns only when it applies, for example only for git commands or only for TypeScript edits
- **5.4.7 Input and output:** event JSON arrives on stdin (or as the POST body); exit code 0 for success, exit code 2 to block on events that can block, other codes are non-blocking errors; or exit 0 and print JSON
- **5.4.8 JSON control:** universal fields (continue, stopReason, systemMessage, terminalSequence); decision patterns per event (block with a reason; PreToolUse permission decisions of allow, deny, ask or defer; PermissionRequest decisions; PostToolUse output rewriting; input rewriting before a tool runs)
- **5.4.9 Adding context:** additionalContext injects facts into Claude's context, best phrased as plain statements of project state
- **5.4.10 Making hooks fail closed:** an onFailure setting to block the action when a hook crashes, cannot start or times out
- **5.4.11 Async and background hooks:** async and asyncRewake for long-running work that should not block
- **5.4.12 SessionStart patterns:** load issue and branch context, persist environment variables for later shell commands, set a session title, watch files, reload skills
- **5.4.13 Common recipes:** run a formatter or linter after edits; block writes to protected paths such as migrations or env files; reject destructive shell commands; log every tool call for audit; desktop notifications via terminalSequence; run the test suite in a Stop hook; validate prompts; auto-approve known-safe commands
- **5.4.14 Security of hooks:** hooks run with your privileges; review project hooks before trusting a repo; managed-only hook modes; HTTP hook URL and environment-variable allowlists
- **5.4.15 Debugging:** /hooks (read-only browser of what is configured), debug logs, JSON that fails validation, shell profile output polluting stdout, Windows without Git Bash behaviour
- **5.4.16 Performance:** keep per-prompt and per-tool hooks fast; default timeouts differ by event

*Read:* Automate actions with hooks (guide), Hooks reference.

### Module 5.5 MCP: connecting Claude Code to your world

*Depth target: L4. Prove-it: connect an issue tracker and a database, then write a skill that teaches Claude your team's query patterns.*

- **5.5.1 What MCP is:** the Model Context Protocol, an open protocol for exposing tools, resources and prompts to models
- **5.5.2 Adding servers:** claude mcp add with a name and either a URL (remote HTTP transport) or a command (local stdio server); examples include issue trackers, design tools, databases, monitoring, browsers and documentation sources; /mcp shows status
- **5.5.3 Scopes and precedence:** local, project (shared via a committed config file) and user; same-name servers resolve local over project over user
- **5.5.4 Authentication:** OAuth for remote servers from /mcp, shell login with claude mcp login, environment-based secrets for local servers
- **5.5.5 Tool search:** on by default, so idle tools cost little context; per-tool result-size overrides
- **5.5.6 MCP resources and prompts:** reference resources with the at-sign; server prompts appear as slash commands
- **5.5.7 Plugin-provided servers:** scoped naming that matters for hook matchers and permission rules
- **5.5.8 Reconnecting and managing:** automatic reconnection, /mcp reconnect, enable and disable
- **5.5.9 Elicitation:** servers can ask you for input mid-call; hooks can intercept
- **5.5.10 Channels:** an MCP server can push messages, alerts and webhooks into a running session (see Module 6.9)
- **5.5.11 Organisational control:** managed MCP configuration, allowlists and denylists
- **5.5.12 Writing your own server:** when your system has no server, build a small one; use the tool-design guidance from Anthropic's engineering writing
- **5.5.13 Security:** treat third-party servers as code running with your credentials; prompt injection through tool results; least-privilege tokens; read-only credentials by default
- **5.5.14 CLI tools versus MCP:** the docs note CLI tools such as gh, aws, gcloud and sentry-cli are the most context-efficient way to reach services that have them

### Module 5.6 Plugins and marketplaces

*Depth target: L4 to L5. Prove-it: package a skill, a hook and an MCP server into a plugin, install it into a second repository, and write an eval for it.*

- **5.6.1 What a plugin is:** a bundle of skills, hooks, subagents, MCP servers and other components in one installable unit; plugin skills are namespaced
- **5.6.2 When you need one:** reuse across repositories, sharing with a team, distributing publicly
- **5.6.3 Installing and managing:** /plugin menu or subcommands (list, install, enable, disable); install scopes; /reload-plugins applies changes; plugins can load from archives or URLs
- **5.6.4 Marketplaces:** Anthropic's official and community marketplaces, third-party and private ones; a marketplace.json file lists plugins and their sources
- **5.6.5 Creating a plugin:** start from an empty directory, add a manifest (plugin.json), add components, test without a marketplace, or convert an existing .claude setup
- **5.6.6 Components and dependencies:** skills, hooks, MCP servers, language servers, themes, executables on PATH, user configuration options, path variables for plugin root and persistent data, dependency declarations with version ranges
- **5.6.7 Testing with evals:** claude plugin eval runs eval cases for your plugin, grades results, compares against a no-plugin baseline, and can gate CI on the score
- **5.6.8 Publishing and distribution:** your own marketplace or Anthropic's directory; pre-release checklist; how users receive updates
- **5.6.9 Measuring cost and usage:** token cost of a plugin, whether people still use it, telemetry events
- **5.6.10 Recommending your plugin:** hints from your own CLI, relevance blocks so Claude Code suggests plugins when work matches
- **5.6.11 Organisational management:** control which plugins install across an organisation through managed settings; approved version ranges
- **5.6.12 Plugin security and trust:** a plugin can do anything your user can; review before install; the security page explains how
- **5.6.13 Troubleshooting and loading rules:** exact error messages grouped by stage, plugin loading reference

### Module 5.7 Mods

*Depth target: L5. A newer extension surface: plugins that run JavaScript inside Claude Code's own process.*

- **5.7.1 What a mod is:** a plugin that adds panes, commands and tool-call rules and can draw in the interface
- **5.7.2 Capabilities:** observe, rewrite or answer tool calls, prompts and turns; draw panes, bands above the prompt, buttons and text fields; add commands and tools; call a model; run work on a timer; message other sessions
- **5.7.3 Building:** ask Claude to write one from a description (the plugin-authoring skill carries the reference), then use the reload and validate loop
- **5.7.4 Testing and troubleshooting:** tests that fire events and stub answers with no session or network; debug log reading
- **5.7.5 Administration:** managed settings can block user-installed mods or allow only your own

### Module 5.8 Code intelligence plugins

- **5.8.1 What they do:** connect Claude to a language server so it sees type errors after edits and navigates by symbol
- **5.8.2 Why they matter:** precise navigation replaces broad file reads, so they often reduce context use in typed languages and large codebases
- **5.8.3 Setup:** install the plugin for your language; answer the recommendation dialog

### Module 5.9 Artifacts and visual output from Claude Code

- **5.9.1 Artifacts:** turn session output into live, interactive pages on claude.ai that stay private, are shared with your organisation, or get a public link
- **5.9.2 Finding them again:** /artifacts lists, attaches, opens or copies links
- **5.9.3 Templates:** /slides for presentations, /design for UI mockups, screen flows, landing pages and posters on an editable canvas, /design-sync to teach designs your real React components, /dataviz for chart guidance
- **5.9.4 Live data:** artifacts can pull data through MCP connectors and offer file downloads where capabilities are enabled
- **5.9.5 Availability:** depends on account and provider; unavailable on some third-party backends

---

## Part 6: Parallel and autonomous work

Once one Claude is effective, the next lever is running several, and running them without you watching. Several of these features are research preview or experimental in the docs; check availability on your plan and version.

### Module 6.1 Choosing a parallel approach

*Depth target: L4. Prove-it: for five tasks, choose the mechanism and say what you give up by choosing it.*

- **6.1.1 The options:** subagents (Claude spawns workers inside a session), agent view (manage many background sessions from one screen), agent teams (coordinated sessions with a lead, experimental), dynamic workflows (scripts that fan out many subagents), projects (a stream of related tasks run as parallel cloud sessions), worktrees (isolated git checkouts), cross-session messaging, desktop parallel sessions, cloud sessions
- **6.1.2 How much coordination do you want to do yourself:** the spectrum from you juggling sessions, to Claude orchestrating a script, to a team lead agent
- **6.1.3 Quality workflows:** fresh context improves review because the reviewer is not biased toward code it just wrote
- **6.1.4 Costs:** parallelism multiplies token use; watch plan limits
- **6.1.5 Read:** Run agents in parallel (the comparison page)

### Module 6.2 Worktrees

- **6.2.1 What and why:** separate git worktrees let parallel sessions edit without colliding
- **6.2.2 Using them:** the --worktree flag, subagent isolation settings, desktop sessions with git isolation
- **6.2.3 What worktrees share and do not share with the main checkout;** the .worktreeinclude file for untracked files you want copied in
- **6.2.4 Cleanup and branching:** new worktrees from local HEAD or the remote default branch
- **6.2.5 Non-git version control:** WorktreeCreate and WorktreeRemove hooks replace the default git behaviour
- **6.2.6 Hook environment in worktrees:** the project directory variable stays at the original root while the cwd field follows Claude

### Module 6.3 Background sessions and agent view

- **6.3.1 Agent view:** run claude agents to dispatch sessions that keep running in the background and watch them from one screen (research preview)
- **6.3.2 Detaching:** /background (alias /bg) detaches the current session; /exit in an attached session detaches without stopping; /stop stops it
- **6.3.3 Copying work:** /fork copies the conversation into a new background session
- **6.3.4 Peek and reply, attach, resume:** interacting with running sessions; resuming a running one moves your current conversation to the background
- **6.3.5 What needs you:** sessions waiting for input are highlighted; notifications on desktop and mobile
- **6.3.6 Turning it off:** the docs explain disabling agent view and what /fork and /subtask do then

### Module 6.4 Agent teams (experimental)

- **6.4.1 Concept:** several Claude Code instances working as a team with shared tasks, inter-agent messaging and a team lead
- **6.4.2 Enabling:** disabled by default; display modes for teammates
- **6.4.3 Hooks:** TeammateIdle, TaskCreated and TaskCompleted let you enforce standards on team work
- **6.4.4 When it helps:** work that splits into parallel streams with some coordination; otherwise prefer subagents or workflows
- **6.4.5 Caveats:** experimental status, token cost, coordination overhead

### Module 6.5 Dynamic workflows and large-scale change

*Depth target: L4 to L5. Prove-it: run a codebase-wide audit with cross-checked findings, then save and rerun the script.*

- **6.5.1 Concept:** a script Claude writes that orchestrates many subagents in the background and returns one result; the script, not turn-by-turn judgement, decides what runs next
- **6.5.2 When to use:** audits, large migrations, research with cross-checking, plans drafted from several angles
- **6.5.3 Using them:** ask for a workflow in your prompt; /workflows opens the progress view to watch, pause, resume or save runs; saved scripts can be rerun and edited; the workflow-authoring skill documents the script API
- **6.5.4 Bundled workflows:** /deep-research fans out web searches, fetches and cross-checks sources, and synthesises a cited report
- **6.5.5 /batch:** decomposes a codebase-wide change into 5 to 30 independent units, presents a plan, and runs one background subagent per unit in its own worktree, each implementing, testing and publishing its change
- **6.5.6 Ultracode:** an effort-level option that makes the session lean on workflows by default
- **6.5.7 Quality patterns:** independent verifier agents, refutation passes, scoped units, resume behaviour

### Module 6.6 Cross-session messaging

- **6.6.1 What it does:** Claude can list and message your other Claude Code sessions on this machine, and reach sessions on other machines or in the cloud
- **6.6.2 Commands:** /list-agents (also /peers) shows who can be messaged and names to use
- **6.6.3 Use cases:** one session warns another that a change breaks its assumptions; a research session feeds an implementation session
- **6.6.4 Hooks:** UserPromptSubmit also fires when another session sends a message

### Module 6.7 Goals, loops and schedules

*Depth target: L4. Prove-it: set up an unattended run that finishes a task correctly and reports back.*

- **6.7.1 /goal:** set a completion condition; a separate evaluator checks after every turn; Claude keeps working until the goal is met, judged impossible, or an error clears it; /goal clear removes it
- **6.7.2 /loop:** run a prompt repeatedly while the session is open; give an interval or let Claude self-pace; omit the prompt to run a maintenance prompt or your own loop.md
- **6.7.3 Cron tools and reminders within a session:** one-time reminders and polling for status
- **6.7.4 Monitor tool:** watch long-running processes
- **6.7.5 Cloud scheduled tasks (formerly routines):** run Claude in the cloud on a schedule, on API calls or on GitHub events; /schedule creates and manages them conversationally
- **6.7.6 Desktop scheduled tasks:** recurring local runs such as daily reviews, dependency audits or morning briefings
- **6.7.7 Automatic continue after a usage limit resets:** desktop and CLI behaviours; /rate-limit-options
- **6.7.8 Designing safe unattended runs:** narrow permissions, sandbox, dontAsk or auto mode, verification gates, a stop condition, cost ceilings, notification when done

### Module 6.8 Headless and programmatic use

*Depth target: L4. Prove-it: build a script that fans out claude -p over a list of files with structured output.*

- **6.8.1 Print mode:** claude -p with a prompt runs non-interactively; input can be piped
- **6.8.2 Output formats:** plain text, a single JSON object with a result field, and stream-json with one JSON object per line
- **6.8.3 Sessions in print mode:** runs create resumable sessions unless you disable persistence
- **6.8.4 Pre-approving and denying:** allowed-tools lists, dontAsk mode for unattended safety, auto mode with fallbacks
- **6.8.5 Fan-out pattern:** have Claude produce a task list file, loop over it with one call per item, test on a few, then run everything
- **6.8.6 Pipelines:** piping Claude output into other commands; use in CI and pre-commit hooks
- **6.8.7 Setup runs:** --init-only, --init and --maintenance trigger Setup hooks for CI preparation
- **6.8.8 Deep links:** claude-cli links open a session in the right repo with a prompt, useful in runbooks and alerts
- **6.8.9 When to graduate to the Agent SDK:** see Part 8

### Module 6.9 Channels: pushing events into a running session

- **6.9.1 Concept:** an MCP server can push messages, alerts and webhooks into a session so Claude reacts while you are away
- **6.9.2 Examples:** forward CI results, chat messages and monitoring alerts
- **6.9.3 Building one:** the channels reference documents capability declaration, notification events, reply tools, sender gating and permission relay

### Module 6.10 Proven multi-agent patterns

- **6.10.1 Writer and reviewer:** one session implements, a fresh session reviews, the first addresses the findings
- **6.10.2 Tests first, then code:** one agent writes tests, another makes them pass
- **6.10.3 Investigate with subagents, implement in the main session**
- **6.10.4 Fan-out migrations** with per-file prompts and strict success criteria
- **6.10.5 CI repair loop:** /autofix-pr or GitHub Actions responding to failures and review comments
- **6.10.6 Overnight batch work** with goals, worktrees and morning review
- **6.10.7 Beware over-engineering:** reviewers asked to find gaps will find some; scope them to correctness and stated requirements

---

## Part 7: Surfaces and integrations

### Module 7.1 Choosing where to run Claude Code

- **7.1.1 The surfaces:** terminal CLI, desktop app (Code tab), VS Code extension, JetBrains plugin, browser (claude.ai/code) and mobile apps for cloud sessions, plus Chrome, Slack, GitHub Actions and GitLab CI/CD integrations
- **7.1.2 Decision guide:** the platforms and integrations page compares them
- **7.1.3 Moving between them:** /desktop, /teleport, /remote-control, cloud flags, session names and resuming

### Module 7.2 Desktop app

- **7.2.1 Core features:** parallel sessions with git isolation, drag-and-drop pane layout, integrated terminal and file editor, side chats, visual diff review, app previews, PR monitoring, connectors
- **7.2.2 Computer use and the built-in browser:** drive native apps and external sites; background computer use on recent versions
- **7.2.3 Dispatch from your phone:** start and steer desktop sessions remotely
- **7.2.4 Scheduled tasks:** recurring local runs
- **7.2.5 iOS Simulator pane:** run and check iOS apps as Claude builds them
- **7.2.6 Platform notes:** Linux beta (Ubuntu and Debian), WSL 2 on Windows
- **7.2.7 Enterprise configuration:** managed settings apply to desktop sessions

### Module 7.3 IDE integrations

- **7.3.1 VS Code:** extension with inline diffs, at-mentions of files and selections, plan review, keyboard shortcuts, mode indicator, its own feedback dialog
- **7.3.2 JetBrains IDEs:** IntelliJ, PyCharm, WebStorm and others
- **7.3.3 /ide:** manage IDE connections from the terminal
- **7.3.4 When the CLI beats the IDE and the reverse:** diff review and selection context in the IDE; scripting and parallelism in the CLI

### Module 7.4 Cloud sessions (Claude Code on the web)

*Depth target: L3 to L4. Prove-it: submit a task from your phone, review the pull request, and pull the session into your terminal.*

- **7.4.1 Quickstart:** connect a GitHub repository, submit a task, review the PR with no local setup; /web-setup connects GitHub from the terminal using your gh credentials
- **7.4.2 Moving sessions:** --cloud starts one from the terminal; /teleport pulls one back; the desktop app and phone can start them
- **7.4.3 Auto-fix pull requests:** a cloud session watches a PR and pushes fixes when CI fails or reviewers comment (/autofix-pr)
- **7.4.4 Environments:** network access levels, environment variables, setup scripts and caching; choosing a default with /remote-env
- **7.4.5 Scheduled tasks and triggers:** schedules, API calls and GitHub events
- **7.4.6 Projects:** hand Claude a stream of related tasks and let it run them as parallel cloud sessions sharing repositories, instructions and memory
- **7.4.7 Limits and settings:** cloud sessions do not read your local user settings; what carries over is documented
- **7.4.8 GitHub Enterprise Server and GitLab support**

### Module 7.5 Mobile and remote control

- **7.5.1 Mobile app:** start, monitor and steer tasks from the Claude app on iOS and Android; push notifications when Claude needs you
- **7.5.2 Remote Control:** continue a local session from your phone, tablet or any browser through claude.ai/code or the mobile app; /remote-control, /rc
- **7.5.3 Safety of remote access:** what leaves your machine, what stays

### Module 7.6 Browser and computer use

- **7.6.1 Claude in Chrome:** connect Claude Code to your browser to test web apps, read console logs, fill forms and extract data; /chrome and the --chrome flag
- **7.6.2 Computer use in the CLI:** open apps, click, type and see your screen on macOS to test native apps and automate GUI-only tools
- **7.6.3 Visual verification loops:** screenshots compared with designs
- **7.6.4 Risks:** prompt injection through web content; use restricted profiles and narrow permissions

### Module 7.7 Team chat integrations

- **7.7.1 Claude Code in Slack:** delegate coding tasks by mentioning Claude; an earlier version applies to workspaces not connected to Claude Tag
- **7.7.2 Claude Tag:** bring Claude into team Slack channels; setup docs live on claude.com
- **7.7.3 Governance:** who can trigger, which repositories, what is logged

### Module 7.8 CI/CD, code review and security scanning

*Depth target: L4. Prove-it: get a pull request automatically reviewed, then customise what it flags.*

- **7.8.1 GitHub Actions:** respond to mentions, automate tasks, turn issues into pull requests; /install-github-app sets up the app and workflows; use through Bedrock, Google Cloud's Agent Platform or Foundry instead of the Claude API
- **7.8.2 GitLab CI/CD:** pipeline integration and merge-request review
- **7.8.3 Code Review (Team and Enterprise):** reviews each pull request, verifies findings and comments inline; setup connects GitHub and chooses repositories; customise with REVIEW.md and CLAUDE.md (severity, skipped paths, extra checks); request with a mention; costs billed through usage credits with caps
- **7.8.4 Local review:** /code-review with effort levels, a fix flag, a comment flag to post findings, targeting a PR, branch or path
- **7.8.5 Ultrareview:** a deep multi-agent cloud review (/code-review ultra), a research preview with free runs on some plans
- **7.8.6 Security:** /security-review checks the branch diff; the security-guidance plugin has Claude review its own changes for vulnerabilities as it writes; the Claude Security plugin scans the whole codebase and turns findings into patches
- **7.8.7 Designing a review pipeline:** local review before push, automated review on PR, human review for design and risk, security scanning on a schedule

---

## Part 8: The Agent SDK

The Agent SDK is Claude Code as a library in Python and TypeScript: the same agent loop, tools and context management, so you can build production agents.

### Module 8.1 Orientation

*Depth target: L3 to L5 depending on goals. Prove-it: ship a small agent that does a real job end to end.*

- **8.1.1 What it is and is not:** a library for building agents on top of the Claude Code runtime; contrast with the plain Messages API (you write the loop) and with print mode (a CLI wrapper)
- **8.1.2 Quickstart and migration:** getting started in either language; migrating from the earlier Claude Code SDK names
- **8.1.3 When to choose it:** you want built-in file, shell and search tools, context management, sessions, permissions and hooks without rebuilding them
- **8.1.4 Examples:** runnable projects and Cookbook recipes

### Module 8.2 The agent loop and configuration

- **8.2.1 Message lifecycle, tool execution, context window and architecture**
- **8.2.2 The options object:** model, environment, limits, working directory, allowed tools and the pages for each feature option
- **8.2.3 System prompts:** the claude\_code preset vs a fully custom prompt; append instructions; CLAUDE.md and output styles in the SDK
- **8.2.4 Using Claude Code features in the SDK:** project instructions, skills, hooks, plugins and settings sources
- **8.2.5 Skills and plugins in the SDK:** control which skills can be invoked, dispatch commands by name, load custom plugins

### Module 8.3 Tools

- **8.3.1 Built-in tools** and permission requirements (see the Tools reference)
- **8.3.2 Custom tools:** define functions as an in-process MCP server so Claude can call your code and APIs
- **8.3.3 External MCP servers:** transports, authentication, error handling
- **8.3.4 Tool search:** scale to thousands of tools by discovering and loading only what is needed
- **8.3.5 Subagents in the SDK:** define and invoke subagents for isolation, parallelism and specialised prompts
- **8.3.6 Tool design:** the same principles as in Part 4.3 of the AI curriculum (clear names, descriptions as prompts, actionable errors, token-efficient output)

### Module 8.4 Input, output and interaction

- **8.4.1 Streaming input vs single-message mode**
- **8.4.2 Streaming output:** text and tool calls in real time for responsive UIs
- **8.4.3 Structured outputs:** validated JSON from multi-turn tool-using runs using JSON Schema, Zod or Pydantic
- **8.4.4 Handling approvals and clarifying questions:** surface requests to users and return their decisions
- **8.4.5 Todo tracking:** render the agent's progress from structured task calls

### Module 8.5 Sessions and state

- **8.5.1 Continue, resume and fork:** returning to a prior run
- **8.5.2 Persisting sessions to external storage:** mirror transcripts to your own object store, key-value store or database so other hosts can resume
- **8.5.3 File checkpointing:** rewind file changes to a prior state

### Module 8.6 Control, cost and observability

- **8.6.1 Permissions:** modes, declarative allow and deny rules, hooks, and a callback for per-request decisions
- **8.6.2 Hooks as callbacks:** intercept and customise behaviour at key execution points; a timed-out callback on policy events can block rather than allow
- **8.6.3 Cost tracking and prompt caching configuration**
- **8.6.4 OpenTelemetry:** export traces, metrics and events to your observability backend
- **8.6.5 Evals for your agent:** build task sets and graders before shipping (see the AI curriculum Module 4.8)

### Module 8.7 Hosting and secure deployment

*Depth target: L4. Prove-it: write a threat model and an isolation plan for a multi-tenant agent service.*

- **8.7.1 Architecture:** the SDK runs the CLI as a subprocess; implications for containers, scaling and session persistence
- **8.7.2 Hosting patterns:** Docker, Kubernetes and sandbox providers; ephemeral per-task containers vs long-running services
- **8.7.3 Multi-tenant isolation:** separate filesystems, credentials and network policies per tenant
- **8.7.4 Secure deployment:** isolation, credential management (never place long-lived secrets where the agent can read them), network egress controls, proxy-injected credentials
- **8.7.5 Failure handling:** crashes, resumability, timeouts, runaway cost guards

### Module 8.8 Product ideas built on the SDK

- **8.8.1 Internal:** code review bots, migration agents, on-call assistants, data analysts, release-note writers, support triage, documentation maintainers
- **8.8.2 External:** vertical agents (legal, finance, research) with file and shell capabilities in a sandbox
- **8.8.3 Decision rule:** if the work is repetitive and verifiable, an SDK agent with a good check is a strong candidate

---

## Part 9: Applied engineering with Claude Code

This part is about outcomes: how to use the tool for each kind of real work, and how to keep quality high when code becomes cheap to produce.

### Module 9.1 Spec-driven development

*Depth target: L4. Prove-it: build a feature from an interview-written spec in a fresh session and show it passes its own end-to-end check.*

- **9.1.1 The workflow:** interview, write SPEC.md, review the spec yourself, start a fresh session, implement against the spec, verify against the spec, commit
- **9.1.2 What makes a spec executable:** names the files and interfaces involved, states what is out of scope, lists edge cases, ends with an end-to-end verification step
- **9.1.3 Interview prompts:** ask Claude to question you about implementation, UI and UX, edge cases, concerns and trade-offs, skipping obvious questions
- **9.1.4 Plan files and task lists:** PLAN.md with checkboxes; Claude tracks progress with its task tool
- **9.1.5 Specs as the review artefact:** reviewers check the diff against the spec
- **9.1.6 Keeping specs alive:** update them when reality changes; store durable decisions in CLAUDE.md or decision records

### Module 9.2 Test-driven and verification-driven development

- **9.2.1 Red, green, refactor with an agent:** write a failing test, confirm it fails for the right reason, implement, confirm it passes, refactor
- **9.2.2 Separate writers:** one session writes tests, another writes code, to avoid tests shaped around the implementation
- **9.2.3 Test quality:** avoid over-mocking, test behaviour, cover edge cases you listed, check that tests fail when the code is broken
- **9.2.4 Beyond unit tests:** integration tests, contract tests, snapshot tests, load tests, accessibility checks, visual regression
- **9.2.5 Verification skills and hooks:** /verify and /run for running the real app; Stop hooks that run the suite
- **9.2.6 Flaky tests and slow suites:** ask Claude to isolate, reproduce and fix; prefer running single tests during development

### Module 9.3 Debugging and incident response

- **9.3.1 Reproduce first:** a failing test or script before any fix
- **9.3.2 Give Claude the evidence:** pasted errors, logs piped in, screenshots, links to dashboards via MCP, git history for regressions
- **9.3.3 Bisecting and blame:** ask Claude to run git bisect with a test, or explain when a behaviour changed
- **9.3.4 Observability access:** error trackers and monitoring through MCP or CLIs; read-only credentials
- **9.3.5 Root cause discipline:** ask for the cause, not a suppression; require an explanation and a regression test
- **9.3.6 Runbooks as skills:** encode your on-call procedures so Claude follows them
- **9.3.7 Production safety:** never give an unattended session write access to production; use read-only tooling and human approval for changes
- **9.3.8 Post-incident work:** timelines, post-mortem drafts, follow-up tickets

### Module 9.4 Refactoring and migrations at scale

*Depth target: L4. Prove-it: migrate a module with characterisation tests, then repeat the migration across many files with /batch or a scripted fan-out.*

- **9.4.1 Characterisation tests first:** lock current behaviour before changing structure
- **9.4.2 Small steps with verification between them**
- **9.4.3 Framework, language and dependency upgrades:** read changelogs, update in stages, run tests, fix deprecations
- **9.4.4 Parallel migration:** /batch decomposes into independent units in worktrees; or loop claude -p over a file list
- **9.4.5 Strangler patterns:** wrap old with new, move traffic gradually
- **9.4.6 Cleanup passes:** /simplify reviews reuse, simplification, efficiency and abstraction level
- **9.4.7 Guarding against churn:** keep diffs reviewable; one concern per pull request

### Module 9.5 Understanding and modernising legacy systems

- **9.5.1 Codebase tours:** ask for architecture overviews, data flow, module boundaries, hot spots
- **9.5.2 Extracting knowledge:** generate documentation, diagrams and decision records from code and history
- **9.5.3 Dependency and risk mapping:** unused code, outdated libraries, security exposure
- **9.5.4 Gradual modernisation:** tests, seams, incremental rewrites
- **9.5.5 Unfamiliar languages and stacks:** learn by building small verified changes with explanations (an explanatory output style helps)

### Module 9.6 Front end, design to code, and UI verification

- **9.6.1 Inputs:** screenshots, Figma through MCP, design-system documentation, existing component patterns
- **9.6.2 Implementation:** follow existing components; build from scratch only when asked
- **9.6.3 Verification:** run the app, take screenshots through Chrome integration or the desktop preview, compare with the design, list differences, fix
- **9.6.4 Accessibility and responsiveness checks**
- **9.6.5 Design artefacts:** /design for mockups and flows; /design-sync so designs use your real React components; /slides for presentations
- **9.6.6 Prototyping:** working clickable prototypes as the fastest way to test an idea

### Module 9.7 Back end, APIs and databases

- **9.7.1 API design:** specs first, OpenAPI documents, consistent errors, pagination, versioning
- **9.7.2 Schema and migrations:** review generated migrations; protect migration folders with hooks; test on copies of data
- **9.7.3 Query work:** explain plans, indexes, N plus one problems
- **9.7.4 Performance:** profile first, then change; verify with benchmarks
- **9.7.5 Integrations:** third-party APIs, webhooks, retries, idempotency
- **9.7.6 Database access safety:** read-only credentials; never point agents at production databases with write rights

### Module 9.8 Data, analytics and scientific work

- **9.8.1 SQL and notebooks:** exploring data, writing queries, documenting assumptions
- **9.8.2 Python data stack:** pandas, polars, plotting, statistical checks
- **9.8.3 Charts and dashboards:** the /dataviz skill for chart form, colour roles, colourblind-safe palettes and accessibility
- **9.8.4 Pipelines:** ETL scripts, schedulers, tests for transformations
- **9.8.5 Reproducibility:** scripts over ad hoc commands, seeds, environment files
- **9.8.6 Verification for analysis:** cross-check numbers independently, sanity-check magnitudes, ask for assumptions in writing

### Module 9.9 DevOps, infrastructure and cloud

- **9.9.1 Infrastructure as code:** Terraform, Pulumi, CloudFormation, Kubernetes manifests, Helm
- **9.9.2 CI/CD pipelines:** writing and repairing workflows; GitHub Actions and GitLab
- **9.9.3 Containers:** Dockerfiles, compose files, dev containers
- **9.9.4 Cloud CLIs:** aws, gcloud, az and kubectl through the shell tool with scoped credentials
- **9.9.5 Discipline:** plan or dry-run before apply; review diffs of infrastructure changes; never auto-apply to production
- **9.9.6 Cost and security reviews of infrastructure code**

### Module 9.10 Security engineering workflows

- **9.10.1 Review:** /security-review on the branch diff; security-guidance plugin during writing; Claude Security plugin for codebase scans
- **9.10.2 Threat modelling:** have Claude draft data-flow diagrams and abuse cases, then review with security staff
- **9.10.3 Dependency audits and secrets scanning**
- **9.10.4 Fixing findings:** patches with tests; verify the exploit no longer works
- **9.10.5 Dual-use caution:** follow your organisation's policy for offensive-security work

### Module 9.11 Documentation, knowledge and onboarding

- **9.11.1 Docs from code:** READMEs, API references, architecture notes, ADRs, changelogs
- **9.11.2 Onboarding:** ask codebase questions the way a new hire would; /team-onboarding generates a guide from your own usage history for teammates
- **9.11.3 Keeping docs honest:** generate docs in CI, flag drift, review as code
- **9.11.4 Knowledge capture:** turn repeated explanations into skills and CLAUDE.md entries

### Module 9.12 Team workflows and operating norms

*Depth target: L4. Prove-it: write a one-page team playbook and get two teammates productive with it in a day.*

- **9.12.1 Shared configuration:** committed CLAUDE.md, rules, skills, agents, hooks and permission settings; personal overrides in local files
- **9.12.2 Conventions for AI-assisted pull requests:** small diffs, a description that states what was verified, link to the spec, disclosure norms
- **9.12.3 Review of AI-written code:** read for intent, check tests, watch for hallucinated APIs, unnecessary dependencies and over-engineering
- **9.12.4 Definition of done:** tests pass, verification evidence attached, no unexplained diffs, docs updated
- **9.12.5 Pairing patterns:** human sets direction and judgement, Claude drives mechanics; swap roles on hard problems
- **9.12.6 Cost and usage norms:** model choice, context hygiene, background work etiquette
- **9.12.7 Skill and hook libraries:** an internal marketplace of vetted plugins
- **9.12.8 Measuring:** analytics dashboard for adoption and velocity, plus quality metrics such as defect escape rate and review time
- **9.12.9 Learning loop:** weekly review of what Claude got wrong and which setup change would have prevented it

### Module 9.13 Quality discipline when code is cheap

- **9.13.1 The new bottleneck:** reviewing, verifying, deciding what to build
- **9.13.2 Failure patterns:** plausible-looking code missing edge cases, tests written to pass rather than to detect, silent scope creep, unrequested abstractions
- **9.13.3 Countermeasures:** specs, verification gates, adversarial review in fresh context, diff size limits, tests as contracts
- **9.13.4 Maintainability:** consistent patterns, deletion of dead code, reasoned dependency choices
- **9.13.5 Taste:** deciding what good looks like remains a human responsibility

---

## Part 10: Enterprise, administration and cost

### Module 10.1 Rollout strategy

*Depth target: L4. Prove-it: write a rollout plan with pilot group, success measures, guardrails and communications.*

- **10.1.1 The decision map:** the admin-setup page covers API providers, managed settings, policy enforcement, usage monitoring and data handling
- **10.1.2 Pilot design:** a small group across seniority levels and stacks, with baseline metrics
- **10.1.3 Champions:** the champion kit is a playbook for engineers who advocate internally
- **10.1.4 Communications:** the communications kit has announcements, drip messages and FAQ answers
- **10.1.5 Training:** in-product lessons (/powerup), workshops, shared prompt libraries, office hours
- **10.1.6 Guardrails before scale:** permission policy, sandboxing defaults, hook baselines, approved plugins

### Module 10.2 Backends and deployment options

- **10.2.1 First-party:** Claude subscriptions and the Anthropic Console
- **10.2.2 Cloud providers:** Amazon Bedrock, Claude Platform on AWS (Anthropic-operated API with AWS auth and Marketplace billing), Google Cloud's Agent Platform (formerly Vertex AI), Microsoft Foundry
- **10.2.3 Setup wizards:** /setup-bedrock and /setup-vertex appear when the provider switch is set
- **10.2.4 Model pinning and regional concerns**
- **10.2.5 Feature availability matrix:** not all features exist on all backends; auto mode, artifacts, cloud sessions and some commands differ
- **10.2.6 GitHub Actions through cloud providers**

### Module 10.3 Authentication and identity

- **10.3.1 Login methods** for individuals, teams and organisations; paste-code login when the browser callback cannot reach localhost
- **10.3.2 Single sign-on and organisation restriction**
- **10.3.3 API keys and helper scripts for credentials** (see the authentication page)
- **10.3.4 Identity inside agents:** session identity verification for self-hosted environments

### Module 10.4 Managed settings and policy

*Depth target: L4 to L5. Prove-it: deploy a managed policy that locks permissions and hooks, and verify enforcement on a test machine.*

- **10.4.1 Delivery mechanisms:** files per operating system and MDM tooling; server-managed settings delivered from Anthropic's console without device management; how sources combine
- **10.4.2 What to enforce:** permission rules, allowed and denied tools, sandbox requirements, model restrictions, disabled features, managed-only hooks, strict plugin-only customisation, allowed marketplaces and plugin version ranges
- **10.4.3 Managed MCP:** provide servers to every user or restrict what users may add with allowlists and denylists
- **10.4.4 Auto mode configuration:** declare trusted repositories, buckets and domains; override block and allow rules
- **10.4.5 Verification:** check which settings are in force; test with a normal user account; watch for silent overrides
- **10.4.6 Mods and plugins governance:** block user-installed mods or allow only your own

### Module 10.5 Gateways, networks and launchers

- **10.5.1 Why a gateway:** centralised credentials, usage tracking, cost controls, per-group model access
- **10.5.2 Claude apps gateway:** self-hosted, SSO sign-in, per-group model routing, spend limits by day, week or month, OTLP telemetry; deploy on Kubernetes or Cloud Run; worked examples for AWS and Google Cloud; gateway.yaml configuration reference
- **10.5.3 Other LLM gateways:** connect Claude Code to a gateway you already run; compatibility requirements for forwarding headers and body fields
- **10.5.4 Enterprise networking:** proxy servers, custom certificate authorities, mutual TLS
- **10.5.5 Corporate launchers:** route processes Claude Code starts through a required wrapper using a process wrapper setting or environment variable

### Module 10.6 Cost and usage governance

*Depth target: L4.*

- **10.6.1 Visibility:** /usage, plan usage breakdown, status line, the analytics dashboard for adoption and velocity, OpenTelemetry metrics and events through monitoring settings
- **10.6.2 Controls:** spend limits, usage credits and requests to admins, gateway-enforced limits, model policy, effort defaults
- **10.6.3 Reducing spend without reducing value:** context hygiene, subagents for exploration, cheaper models for simple tasks, caching awareness, hooks that preprocess large outputs, avoiding wasteful loops
- **10.6.4 Background token usage:** features that consume tokens in the background and how to see them
- **10.6.5 Plugin and skill costs:** /skill-doctor and plugin measurement guidance
- **10.6.6 Reviewing cost per merged change** rather than cost per session

### Module 10.7 Data handling and compliance

- **10.7.1 Data usage policies** for each plan and backend; telemetry and what is sent
- **10.7.2 Zero data retention** for qualified Enterprise accounts: scope, disabled features, requesting enablement
- **10.7.3 HIPAA-ready setup** for local mode: versions, network access, managed settings, local data, credentials removed from subprocess environments
- **10.7.4 Legal and compliance page:** agreements, certifications and security information
- **10.7.5 Transcripts and local data:** where conversation history lives and how to purge it (for example the project purge command)
- **10.7.6 Regional and sovereignty questions:** choose backends and regions accordingly

### Module 10.8 Measuring impact

- **10.8.1 Adoption:** active users, sessions, features used, skills and plugins in use
- **10.8.2 Velocity:** cycle time, pull-request throughput, time to first contribution for new hires
- **10.8.3 Quality:** defect escape rate, incident rate, review rework, test coverage trends, security findings
- **10.8.4 Experience:** developer satisfaction surveys, qualitative interviews
- **10.8.5 Pitfalls:** lines of code and prompt counts are vanity metrics; compare against baselines; watch for review bottlenecks moving downstream

---

## Part 11: Security and safe operation

### Module 11.1 The threat model of a coding agent

*Depth target: L4. Prove-it: draw the trust boundaries of your own setup and list the three most likely failures.*

- **11.1.1 What the agent can reach:** your filesystem, shell, credentials in environment variables, network, git remotes, cloud accounts, connected MCP servers
- **11.1.2 Who controls its inputs:** you, but also repository files, issue text, web pages, tool results and any third-party server
- **11.1.3 Main risk classes:** prompt injection, destructive commands, data exfiltration, credential leakage, supply-chain compromise through plugins, MCP servers and dependencies, over-broad permissions
- **11.1.4 Defence layers:** model behaviour, permission rules, auto mode classifier, sandbox, hooks, isolation, credential scoping, review gates, monitoring

### Module 11.2 Prompt injection and hostile content

- **11.2.1 Where it comes from:** web fetches, README and issue text, pull-request comments, files in untrusted repositories, MCP results, emails or documents read by tools
- **11.2.2 The dangerous combination:** private data access plus untrusted content plus an outbound channel; break at least one leg
- **11.2.3 Practical defences:** restrict network egress, deny sensitive file reads, avoid mixing browsing and credentials in one session, review before running unfamiliar commands, use auto mode's classifier for hostile-content-driven actions
- **11.2.4 Treat any content Claude fetches as untrusted data**

### Module 11.3 Least privilege and isolation

- **11.3.1 Permissions:** narrow allow rules, explicit deny rules for secrets and destructive commands
- **11.3.2 Sandboxing:** the built-in sandbox, dev containers, Docker and virtual machines, chosen by threat model
- **11.3.3 Credentials:** read-only tokens by default; separate credentials per environment; short-lived tokens; never production write access for unattended sessions
- **11.3.4 Git safeguards:** protected branches, required reviews, no force-push rights, signed commits where required
- **11.3.5 bypassPermissions only in disposable environments**

### Module 11.4 Secrets

- **11.4.1 Keep secrets out of reach:** deny rules for env files and key directories, hooks that block reads and writes of sensitive paths, secret managers
- **11.4.2 Keep secrets out of context:** do not paste them; they can persist in transcripts
- **11.4.3 Scanning:** pre-commit secret scanners and CI checks
- **11.4.4 Rotation:** assume anything that entered a session may need rotating after an incident
- **11.4.5 Subprocess environment scrubbing and credential removal options** in sensitive configurations

### Module 11.5 Supply chain: plugins, MCP servers and dependencies

- **11.5.1 Plugins:** can run code with your privileges; review contents, source and maintainers; pin versions; prefer vetted internal marketplaces
- **11.5.2 MCP servers:** treat as third-party code with network and token access
- **11.5.3 Dependencies Claude adds:** check necessity, maintainers, licence and typosquatting; review lockfile changes
- **11.5.4 Organisational controls:** allowlists, managed plugin lists, approved version ranges

### Module 11.6 Untrusted repositories and workspace trust

- **11.6.1 What can run on opening a folder:** project settings, hooks, MCP configuration and skills; the docs list what runs before trust
- **11.6.2 Safe handling:** inspect unfamiliar repositories before trusting them; use a throwaway container or VM; start in plan mode; disable hooks for one run with a settings override
- **11.6.3 Print mode and trust:** non-interactive runs do not count as accepting the trust dialog

### Module 11.7 Safe autonomy patterns

- **11.7.1 Choose the mode to match risk:** Manual for unfamiliar work, auto for trusted routine work, dontAsk with an allowlist for scripts
- **11.7.2 Branch and PR gates:** autonomous work lands on branches and merges only after review and checks
- **11.7.3 Budgets and stop conditions:** step limits, goals with clear completion, spend ceilings
- **11.7.4 Observability:** transcripts, OpenTelemetry events, hook-based audit logs
- **11.7.5 Kill switches:** stop commands, revoking tokens, disabling features in managed settings

### Module 11.8 Incident playbooks

- **11.8.1 Destructive command ran:** stop the session, restore from git or backups, review audit logs, add a deny rule or hook
- **11.8.2 Secret exposed:** rotate immediately, purge transcripts if needed, add scanning
- **11.8.3 Malicious plugin or MCP server suspected:** disable, review what it could access, rotate credentials, report
- **11.8.4 Prompt injection suspected:** capture the transcript, identify the source, add egress and read restrictions, report the vector

*Read:* Security, Data usage, Securely deploying AI agents, Plugin security and trust, Sandboxing and sandbox environments.

---

## Part 12: Troubleshooting and debugging

### Module 12.1 The diagnostic toolkit

*Prove-it: break each of five things on purpose (a setting, a hook, an MCP server, a skill, CLAUDE.md) and diagnose it using only the tools below.*

- **12.1.1 /doctor:** setup checkup for installation, settings, extensions and CLAUDE.md, proposing fixes you confirm
- **12.1.2 /status:** version, model, account, connectivity and settings sources
- **12.1.3 /context:** what is loaded and what it costs
- **12.1.4 /hooks, /mcp, /permissions, /skills, /plugin list:** what is configured, connected and in force
- **12.1.5 /debug and the debug flags:** turn on debug logging and read the log; --debug and --debug-file at launch
- **12.1.6 Safe mode:** troubleshoot a broken configuration
- **12.1.7 The debug-your-config page:** diagnoses why CLAUDE.md, settings, hooks, MCP servers or skills are not taking effect

### Module 12.2 Installation and login

- **12.2.1 Common failures:** command not found, PATH issues, permission errors, network and proxy problems, authentication errors, wrong organisation
- **12.2.2 Windows specifics:** native Windows without Git Bash, PowerShell tool, hooks running in different shells, WSL
- **12.2.3 Corporate networks:** proxies, custom certificates, mutual TLS

### Module 12.3 Performance problems

- **12.3.1 High CPU or memory, hangs, auto-compact thrashing, slow search**
- **12.3.2 Remedies:** clear or compact, narrow search scope, exclude huge directories, restart, update, fullscreen rendering for stable memory in long sessions
- **12.3.3 /heapdump** for memory diagnostics (share only the diagnostics file, never the heap snapshot)

### Module 12.4 Behaviour playbook

- **12.4.1 Claude ignores an instruction:** CLAUDE.md too long or ambiguous; convert to a hook if it must always happen
- **12.4.2 Claude keeps making the same mistake:** after two failed corrections, clear and rewrite the prompt with what you learned
- **12.4.3 Claude loops or stalls:** interrupt, narrow the task, supply a failing check
- **12.4.4 Wrong skill loaded or none:** fix descriptions, use explicit invocation
- **12.4.5 Hallucinated files, functions or flags:** ask it to read the real source, give documentation links, add code intelligence
- **12.4.6 Context bloat:** inspect with /context, move reference to skills, use subagents
- **12.4.7 Quality drops late in a session:** clear and restart with a summary or spec

### Module 12.5 Extension failures

- **12.5.1 Hooks:** not firing (matcher, if condition, shell form quoting, limits), JSON ignored (extra stdout text), blocking unexpectedly (exit code 2 semantics), timeouts, Windows shell differences
- **12.5.2 MCP:** server failed or needs auth (/mcp reconnect, login), schema or result-size issues, scope confusion
- **12.5.3 Plugins and marketplaces:** install errors by stage, loading rules, blocked by enterprise policy
- **12.5.4 Skills:** frontmatter parse errors, plugin-only locks, hook limits

### Module 12.6 Errors, limits and cost surprises

- **12.6.1 The error reference:** runtime messages and fixes; rate limits, overloaded errors, authentication and organisation errors, model not found, context exceeded, credential failures
- **12.6.2 Usage limits:** wait and continue automatically, usage credits, plan upgrade options
- **12.6.3 Unexpected cost:** check background features, long contexts, many subagents, loops, model and effort choices

### Module 12.7 Reporting and keeping up

- **12.7.1 Reporting bugs:** /bug and /feedback with consent screens; local feedback bundles on third-party providers
- **12.7.2 Release notes:** /release-notes, the changelog and the weekly What's New digests
- **12.7.3 Community:** the public GitHub repository for issues, and Anthropic's engineering blog for practices

---

## Part 13: Claude Code for product managers and non-engineers

Claude Code is not only for people who write code. For a product manager, technical program manager or founder it can be the fastest way to prototype, analyse, automate and read systems you could not read before. This part is a ladder from zero.

### Module 13.1 Why a PM should use it

- **13.1.1 Read the system:** ask questions about how the product actually behaves, with answers grounded in the code rather than in someone's memory
- **13.1.2 Prototype ideas:** a working clickable prototype often beats a document for testing an idea with users and stakeholders
- **13.1.3 Analyse data yourself:** queries, charts and cross-checks without waiting for an analyst
- **13.1.4 Build small internal tools:** dashboards, scripts and automations for your own workflow
- **13.1.5 Write better specs:** requirements that reference real files, real constraints and real edge cases
- **13.1.6 Debug with engineers:** reproduce issues, gather evidence and propose likely causes before the first meeting
- **13.1.7 Boundaries:** prototypes are not production; engineers own production changes, review and release

### Module 13.2 The ladder: seven rungs

*Each rung has a deliverable. Do not move up until you can do the current rung without help.*

- **13.2.1 Rung 0, Set up and stay read-only:** install, sign in, open a repository in plan mode, ask questions only; deliverable: a one-page summary of how a feature works
- **13.2.2 Rung 1, Interrogate a codebase:** trace a user journey through the code, list the services and data stores involved, find where a metric is computed; deliverable: an architecture note an engineer confirms is accurate
- **13.2.3 Rung 2, Small safe changes:** copy edits, config values, documentation, test data, on a branch with a pull request; deliverable: a merged documentation or copy change
- **13.2.4 Rung 3, Prototype in a sandbox repository:** build a clickable prototype from a sketch or a screenshot; deliverable: a prototype you demo to users
- **13.2.5 Rung 4, Internal tool or analysis:** a script, dashboard or report people actually use; deliverable: something a teammate uses weekly
- **13.2.6 Rung 5, Automate your workflow:** skills for recurring documents, scheduled tasks, connections to your tools through MCP; deliverable: a weekly update that largely writes itself
- **13.2.7 Rung 6, Contribute production code with engineers:** pair on a real ticket with tests and review; deliverable: a reviewed, merged change you can explain line by line

### Module 13.3 Product tasks Claude Code can do

- **13.3.1 Code-grounded PRDs:** run the spec interview, have Claude check each requirement against the codebase, and list impacted components and risks
- **13.3.2 Feasibility and impact analysis:** what would change if we alter this behaviour, which teams and services are touched, what is risky
- **13.3.3 Release notes and changelogs:** from commits and pull requests, written for customers or for support
- **13.3.4 Bug triage and reproduction:** read an issue, reproduce it, find the likely area, draft a precise ticket
- **13.3.5 Data and metrics:** write and explain SQL, build charts, validate numbers independently, document definitions
- **13.3.6 Research synthesis:** process interview transcripts, survey exports and support tickets into themes with supporting quotes (paraphrased) and counts
- **13.3.7 Competitive and market research:** the deep-research workflow fans out searches, cross-checks sources and writes a cited report
- **13.3.8 Stakeholder artefacts:** slides (/slides), design mockups and flows (/design), live dashboards as shareable artifacts
- **13.3.9 Experiment support:** instrumentation plans, event schemas, analysis scripts, sample-size calculations
- **13.3.10 Documentation and onboarding guides**

### Module 13.4 Prototyping workflows

*Prove-it: go from a one-paragraph idea to a prototype five people can click through, with feedback captured.*

- **13.4.1 Start with the user job and the key screen,** not the technology
- **13.4.2 Ask Claude to propose a plan,** then approve it in plan mode before it builds
- **13.4.3 Use your design inputs:** screenshots, a design system synced with /design-sync, an existing component library
- **13.4.4 Build the smallest thing that answers the question:** one flow, fake data, no login
- **13.4.5 Verify in a browser:** run it, screenshot it, compare with the intent, iterate
- **13.4.6 Share it:** publish as an artifact or deploy to a preview host
- **13.4.7 Hand off:** a README, a list of what is faked, and a clear statement of what would change for production
- **13.4.8 Know the limits:** security, scale, accessibility, data and compliance are not solved by a prototype

### Module 13.5 Working safely as a non-engineer

- **13.5.1 Start in plan mode or Manual mode;** read every permission prompt until you understand what it asks
- **13.5.2 Use a branch for everything,** commit often, never work directly on the main branch
- **13.5.3 Prefer a sandbox repository or cloud session** so your laptop is not the blast radius
- **13.5.4 Never connect to production** databases or services with write access
- **13.5.5 Keep secrets out of prompts and files**
- **13.5.6 Ask Claude to explain every change** in plain language, and ask what could go wrong
- **13.5.7 Learn the minimum git:** status, diff, branch, commit, push, pull request, revert
- **13.5.8 Ask for review:** an engineer reviews anything that touches a shared codebase

### Module 13.6 Automating a PM's recurring work

- **13.6.1 Skills for recurring documents:** weekly update, PRD template, launch checklist, release notes, meeting-notes processing, customer-call summaries
- **13.6.2 Connect your tools through MCP:** issue trackers, wikis, chat, calendars, analytics, with read access first
- **13.6.3 Scheduled tasks:** a Monday-morning brief, a daily metrics check, a weekly backlog hygiene report
- **13.6.4 Headless scripts:** claude -p over exported data for repeatable processing
- **13.6.5 Hooks for guardrails:** notify when a long task finishes
- **13.6.6 Measure the time saved** and review monthly

### Module 13.7 Collaborating with engineers

- **13.7.1 Bring prototypes and specs, not demands;** respect that engineers own production design
- **13.7.2 Use Claude to understand code before asking questions,** and ask better ones
- **13.7.3 Share your setup:** useful skills and prompts go into the team's repository
- **13.7.4 Pull requests from PMs:** small, tested, clearly described, labelled as such
- **13.7.5 Join code review as a learner,** with Claude explaining diffs, never as an approver of technical safety

### Module 13.8 Building AI features with Claude Code

- **13.8.1 The /claude-api skill:** loads API and managed-agent reference for your project's language, and offers subcommands for migrating, upgrading, prompt audits, cost optimisation, building evals and iterating a prompt against an eval
- **13.8.2 Scaffolding AI features:** prompts, structured outputs, tool definitions, retrieval, evaluation harnesses
- **13.8.3 Evals first:** build the task set and graders before polishing prompts
- **13.8.4 Cost and latency checks as part of development**
- **13.8.5 Prototype to production path:** engineering review, security review, privacy and safety review, monitoring

### Module 13.9 The technical literacy to build on the side

- **13.9.1 Terminal and git basics**
- **13.9.2 HTTP, APIs, JSON and authentication concepts**
- **13.9.3 SQL for analysis**
- **13.9.4 Reading Python and TypeScript** well enough to follow a diff
- **13.9.5 How a web app is structured:** front end, back end, database, deployment
- **13.9.6 Testing concepts and CI**
- **13.9.7 Use Claude itself as the tutor:** ask it to teach with the code in front of you, and to quiz you afterwards

---

## Part 14: Quick reference

Commands, flags and settings change often. Use this as a map, then confirm with /help, the Commands page and the CLI reference.

### Module 14.1 Slash commands by moment

- **14.1.1 First session in a repo:** /init (starter CLAUDE.md), /memory (edit memory files), /mcp (servers), /permissions (rules), /doctor (checkup), /powerup (lessons)
- **14.1.2 During a task:** /plan (enter plan mode), /model, /effort, /fast, /advisor, /context, /compact, /btw (side question), /goal, /loop, /diff, /rewind, /clear, /recap
- **14.1.3 Parallel and background work:** /tasks, /background (/bg), /fork, /subtask, /branch, /batch, /workflows, /list-agents (/peers), /schedule
- **14.1.4 Before you ship:** /diff, /code-review (alias /review) with effort levels and flags, /simplify, /security-review, /verify, /run, /autofix-pr, /install-github-app
- **14.1.5 Between sessions:** /resume, /rename, /export, /teleport, /remote-control (/rc), /desktop, /cd, /add-dir
- **14.1.6 Configuration:** /config (settings or key=value), /update-config, /output-style, /statusline, /theme, /tui, /keybindings, /terminal-setup, /voice, /sandbox, /autocompact, /privacy-settings
- **14.1.7 Extensions:** /skills, /skill-doctor, /reload-skills, /plugin, /reload-plugins, /hooks, /agents (reminder page), /chrome, /ide, /install-slack-app
- **14.1.8 Diagnostics and help:** /help, /status, /debug, /doctor, /heapdump, /bug, /feedback, /release-notes, /insights
- **14.1.9 Accounts and usage:** /login, /logout, /usage (aliases /cost, /stats), /usage-credits, /rate-limit-options, /upgrade
- **14.1.10 Artifacts and design:** /artifacts, /design, /design-sync, /design-login, /slides, /dataviz
- **14.1.11 Research and APIs:** /deep-research, /claude-api
- **14.1.12 Setup for providers:** /setup-bedrock, /setup-vertex (shown when the provider switch is set), /remote-env, /web-setup
- **14.1.13 Rare or hidden:** /heapdump is hidden until typed in full; some commands appear only on certain platforms, plans or versions; MCP server prompts become commands too

### Module 14.2 Keyboard and input

- **14.2.1 Shift+Tab:** cycle permission modes
- **14.2.2 Escape:** interrupt; Escape twice opens rewind
- **14.2.3 Ctrl+G:** edit a plan or prompt in your text editor
- **14.2.4 Ctrl+R:** search command history across projects
- **14.2.5 At-sign:** reference files; **exclamation prefix:** run a shell command and share the output; paste or drag images
- **14.2.6 Multiline:** Shift+Enter after /terminal-setup, or Option+Enter in Apple Terminal
- **14.2.7 Vim mode:** set through /config editor mode
- **14.2.8 Customise:** /keybindings

### Module 14.3 Command-line flags and subcommands

- **14.3.1 Common flags:** -p (print mode), --continue, --resume, --permission-mode, --allowedTools, --output-format, --verbose, --no-session-persistence, --worktree, --agent, --name, --from-pr, --fork-session, --chrome, --debug, --debug-file, --settings, --init-only, --init, --maintenance, --cloud, --teleport
- **14.3.2 Subcommands:** claude mcp (add, list, login and more), claude plugin (install, eval and more), claude agents, claude auth login, claude project purge, claude update; the CLI reference lists everything

### Module 14.4 Files and directories

- **14.4.1 Instruction files:** CLAUDE.md (managed, user, project, local, nested), AGENTS.md support, .claude/rules
- **14.4.2 Configuration:** settings.json at user and project level, settings.local.json for personal project overrides, managed policy locations
- **14.4.3 Extensions:** .claude/skills, .claude/agents, hooks defined in settings or plugin hooks.json, .mcp.json style project MCP config, plugin directories with plugin.json, marketplace.json
- **14.4.4 Other:** REVIEW.md for Code Review, loop.md for default loop prompts, .worktreeinclude, session transcripts under the home .claude directory, feedback bundles for third-party providers

### Module 14.5 Hook events cheat sheet

- **14.5.1 Session:** SessionStart, Setup, SessionEnd
- **14.5.2 Prompt and turn:** UserPromptSubmit, UserPromptExpansion, Stop, StopFailure
- **14.5.3 Tool loop:** PreToolUse, PermissionRequest, PermissionDenied, PostToolUse, PostToolUseFailure, PostToolBatch
- **14.5.4 Agents and tasks:** SubagentStart, SubagentStop, TaskCreated, TaskCompleted, TeammateIdle
- **14.5.5 Environment:** InstructionsLoaded, ConfigChange, CwdChanged, DirectoryAdded, FileChanged, WorktreeCreate, WorktreeRemove
- **14.5.6 Model and context:** PreCompact, PostCompact, PreModelSwitch, PostModelSwitch
- **14.5.7 MCP and display:** Elicitation, ElicitationResult, Notification, MessageDisplay
- **14.5.8 Blocking rule of thumb:** exit code 2 blocks on events that can block (PreToolUse, UserPromptSubmit, Stop, SubagentStop, TaskCreated, TaskCompleted, PreCompact, PreModelSwitch and others); it only shows feedback on events that already happened

### Module 14.6 Settings and environment variables worth knowing

- **14.6.1 Settings keys seen in the docs:** hooks, permissions, enabledPlugins, statusLine, fileSuggestion, subagentStatusLine, viewMode, skillOverrides, disableAllHooks, allowManagedHooksOnly, strictPluginOnlyCustomization, allowedHttpHookUrls, httpHookAllowedEnvVars, disableCommandPluginSources, processWrapper, autoMode.environment, ultracode, autoContinueAtUsageLimit; the All settings page is the source of truth
- **14.6.2 Environment variables seen in the docs:** CLAUDE\_ENV\_FILE (SessionStart and related hooks), CLAUDE\_PROJECT\_DIR, CLAUDE\_PLUGIN\_ROOT, CLAUDE\_PLUGIN\_DATA, CLAUDE\_CODE\_USE\_BEDROCK, CLAUDE\_CODE\_USE\_VERTEX, CLAUDE\_CODE\_NEW\_INIT, CLAUDE\_CODE\_PROCESS\_WRAPPER, CLAUDE\_CODE\_SUBPROCESS\_ENV\_SCRUB, CLAUDE\_CODE\_GIT\_BASH\_PATH, CLAUDE\_CODE\_REMOTE, CLAUDE\_EFFORT, ANTHROPIC\_MODEL, MCP\_TIMEOUT

### Module 14.7 Starter templates (write them in your own words and adapt)

- **14.7.1 CLAUDE.md skeleton:** project purpose in two lines; build, test and lint commands; code style rules that differ from defaults; repo etiquette (branches, commit format, PR rules); architecture decisions and gotchas; what to preserve when compacting
- **14.7.2 Skill skeleton:** a folder with SKILL.md; frontmatter with a name and a specific description; a body with purpose, steps, checks, output format; set model invocation off for anything with side effects; link longer references
- **14.7.3 Subagent skeleton:** a markdown file in the agents folder; frontmatter with name, a precise description of when to delegate, minimal tools, optional model; a body that defines the role, what to check and how to report
- **14.7.4 Hook skeleton:** event, matcher, optional if condition, handler type with a script path, a clear exit-code contract; set fail-closed behaviour for policy hooks
- **14.7.5 Spec-interview prompt:** state the feature in one line, ask Claude to interview you about implementation, UX, edge cases, concerns and trade-offs using its question tool, skip obvious questions, then write a complete spec file
- **14.7.6 Verification prompt:** implement, run the named check, show the output, fix failures at the root cause, repeat until the check passes, then summarise what changed and what was not tested
- **14.7.7 Adversarial review prompt:** use a fresh-context subagent to review the diff against the plan; report only gaps affecting correctness or stated requirements

---

## Part 15: Project ladder

Each project has a deliverable. Do them roughly in order, skip freely, and write a short note after each one: what worked, what failed, what you changed in your setup.

### Tier 1: Foundations

- **P1 First-session tour:** run the first-session routine in a repository, generate and prune a CLAUDE.md
- **P2 Codebase explainer:** produce an architecture overview and have an engineer correct it
- **P3 Bug fix with a failing test:** reproduce, test, fix, verify, commit, open a PR
- **P4 Small CLI tool:** built from a spec you wrote through the interview pattern
- **P5 Screenshot to site:** a static page built from a design image and checked in a browser
- **P6 Notes to PRD workflow:** turn raw notes into a spec checked against code

### Tier 2: Configuration and extension

- **P7 CLAUDE.md pruning experiment:** measure behaviour and context before and after a 50 percent cut
- **P8 Three skills:** a reference skill, an action skill with side effects, and a forked-context skill; compare costs with the skill doctor
- **P9 Two subagents:** a read-only security reviewer and a research agent; compare against main-session work
- **P10 Hooks pack:** format on edit, block dangerous commands, notify on completion, a Stop gate that runs tests
- **P11 MCP integration:** connect an issue tracker and a database read-only, then write a skill teaching your conventions
- **P12 Plan-mode feature:** spec interview, plan, implement, verify in a fresh session
- **P13 Permission and sandbox policy:** allow tests, ask for pushes, deny secrets; test it by trying to break it
- **P14 Personalised interface:** status line, output style, keybindings and a custom theme

### Tier 3: Scale and autonomy

- **P15 Batch migration:** migrate a module and then many files using /batch or a scripted fan-out
- **P16 Headless pipeline:** a script that runs claude -p over a list with JSON output and a results report
- **P17 PR automation:** GitHub Actions with mention-triggered work and automated review customised with REVIEW.md
- **P18 Unattended run:** a goal-driven task with a verification gate, a budget and a notification at the end
- **P19 Scheduled audit:** a daily or weekly scheduled task such as a dependency or security audit
- **P20 Dynamic workflow:** a codebase-wide audit with cross-checking, saved and rerun
- **P21 Worktree race:** three parallel attempts at a feature in separate worktrees, compared
- **P22 Phone to PR:** start a cloud session from your phone, review the pull request, teleport it to your terminal
- **P23 Browser verification loop:** a UI change checked through Chrome integration with screenshot comparison

### Tier 4: Building on Claude Code

- **P24 Plugin with an eval:** package a skill, a hook and an MCP server, then write evals and compare with a no-plugin baseline
- **P25 Team marketplace and rollout kit:** an internal plugin marketplace, onboarding guide and champion materials
- **P26 Managed-policy lab:** deploy a managed settings file on a test machine and verify enforcement
- **P27 Agent SDK service:** a code-review or triage agent with structured output, custom tools and tests
- **P28 Isolated SDK deployment:** containerised, per-tenant isolation, scoped credentials, egress controls
- **P29 Channel server:** an MCP channel pushing CI or monitoring alerts into a running session
- **P30 Mod:** a plugin that adds a pane or command inside Claude Code
- **P31 Usage observability:** OpenTelemetry export into a dashboard of cost, adoption and outcomes
- **P32 Gateway deployment (admins):** a gateway with SSO, per-group model access and spend limits

### Tier 5: Authority

- **P33 Public plugin or skill pack** others install and use
- **P34 Writing series** on practical Claude Code methods, with measurements
- **P35 Talk or workshop** teaching a team to use it
- **P36 A measured ROI study** inside your organisation with baselines and honest caveats
- **P37 Upstream contributions:** bug reports with clear reproductions, documentation fixes, example plugins

---

## Part 16: Library

### Module 16.1 The official documentation map (code.claude.com/docs)

- **16.1.1 Getting started:** Overview, Quickstart, Changelog, How Claude Code works, Extend Claude Code, Explore the .claude directory, Explore the context window, How Claude Code uses prompt caching, How Claude remembers your project, Manage sessions, Common workflows, Prompt library, Best practices
- **16.1.2 Platforms:** Platforms and integrations, Remote Control, Projects, Mobile, Chrome, Computer use, VS Code, JetBrains, Slack, Claude Tag; cloud sessions (quickstart, full guide, scheduled tasks); desktop (quickstart, full guide, Linux, WSL, scheduled tasks, iOS Simulator)
- **16.1.3 Review and CI:** Review locally with /code-review, Ultrareview, GitHub Enterprise Server, Code Review (overview, setup, customisation, pull requests, costs, troubleshooting), security guidance and Claude Security plugins, GitHub Actions, GitHub Actions with cloud providers, GitLab CI/CD
- **16.1.4 Build with Claude Code:** Run agents in parallel, Subagents, Agent view, Agent teams, Cross-session messaging, Dynamic workflows, Worktrees, MCP quickstart and MCP, Skills, Artifacts, Hooks guide, Channels, Scheduled tasks, Goal, Headless, Deep links, Large codebases, Troubleshooting pages, Debug your configuration, Error reference
- **16.1.5 Plugins:** overview, install, marketplaces, code intelligence, security, create, components, dependencies, evals, publish, measure, CLI hints, mods (overview, create, reference, interface, gallery, events, API, test, troubleshoot, admin), marketplace creation and hosting, org management, manifest and marketplace references
- **16.1.6 Administration:** Admin setup, Advanced setup, Authentication, Managed settings, Server-managed settings, Managed MCP, Auto mode config, Enterprise deployment overview, Feature availability, Bedrock, Claude Platform on AWS, Google Cloud Agent Platform, Microsoft Foundry, Network config, Corporate launcher, Dev containers, Gateways (Claude apps gateway pages and other gateways), Monitoring, Costs, Analytics, Security, Data usage, Zero data retention, HIPAA setup, Communications kit, Champion kit
- **16.1.7 Configuration:** Settings, All settings, Example settings, Permissions, Permission modes, Auto mode classifier billing, Sandboxing, Sandbox environments, Cloud environments, Self-hosted environments (several pages), Model configuration, Fast mode, Advisor, Output styles, Terminal config, Fullscreen, Accessibility, Voice dictation, Status line, Keybindings
- **16.1.8 Reference:** CLI reference, Commands, Environment variables, Tools reference, Interactive mode, Checkpointing, Hooks reference, Channels reference, Glossary
- **16.1.9 Agent SDK:** overview, quickstart, migration, troubleshooting, configuration, examples, agent loop, Claude Code features in the SDK, sessions, session storage, streaming input and output, approvals and user input, structured outputs, custom tools, MCP, tool search, subagents, modifying system prompts, skills, plugins, permissions, hooks, file checkpointing, cost tracking, observability, todo tracking, hosting, secure deployment, TypeScript and Python references
- **16.1.10 What's New:** weekly digests; a machine-readable index of all pages at the docs llms.txt file

### Module 16.2 Anthropic writing worth reading

- **16.2.1 Engineering and research posts** on building effective agents, writing effective tools for agents, effective context engineering for agents, how a multi-agent research system was built, and best practices for agentic coding
- **16.2.2 Product blog:** posts on steering Claude Code with skills, hooks, rules and subagents, and release announcements
- **16.2.3 Documentation for the underlying platform:** Claude API, tool use, MCP, prompt caching, the Claude Cookbook

### Module 16.3 Communities and ways to keep up

- **16.3.1 The public GitHub repository** for issues, discussions and example hooks such as the Bash command validator
- **16.3.2 Weekly habit:** read the What's New digest, try one new feature in a throwaway repo, delete one piece of setup that is no longer needed
- **16.3.3 Share learnings:** internal channels, short Loom-style demos, a living team playbook

---

## Part 17: Mastery drills and question banks

### Module 17.1 Explain-it drills

For each, give a 30-second answer for a non-engineer and a 3-minute answer for an engineer.

- **17.1.1 Concepts:** the agentic loop; why context is the scarce resource; CLAUDE.md vs skills vs rules; hooks vs prompts; subagents vs skills; MCP; permission modes and the auto mode classifier; worktrees; checkpoints and their limits; prompt caching effects
- **17.1.2 Practices:** explore, plan, implement, commit; verification gates; spec interviews; writer and reviewer; fan-out migrations
- **17.1.3 Organisation:** managed settings; gateways; cost governance; measuring impact

### Module 17.2 Scenario questions

Answer in two minutes each, naming the mechanism you would use and why.

- **17.2.1 Setup and context:**
  - Claude keeps using npm when you use pnpm. What do you change and where?
  - Your CLAUDE.md is 600 lines and behaviour is getting worse. What do you do?
  - A procedure matters only for release work. Where does it live?
  - Sessions get worse after an hour. Why, and what do you change in your habits?
- **17.2.2 Control and safety:**
  - You want Claude to run tests and lint without asking but never read env files. Write the policy.
  - A repository you do not trust must be inspected. How do you open it safely?
  - Unattended nightly runs must not push to main. How do you enforce that?
  - Someone puts instructions in a GitHub issue that Claude reads. What defences apply?
- **17.2.3 Extension design:**
  - You need code formatted after every edit. Prompt, skill or hook?
  - You want a reviewer that is not biased toward code it just wrote. How do you set it up?
  - Your database schema knowledge is needed in many sessions. MCP, skill or CLAUDE.md?
  - A teammate wants your setup in three repositories. What do you package, and how do you test it?
- **17.2.4 Scale:**
  - Migrate 2,000 files to a new API. Choose the mechanism and the verification.
  - A long task must finish correctly while you sleep. Which features do you combine?
  - Three teams need different model access and spend caps. What architecture?
- **17.2.5 Troubleshooting:**
  - A hook does not fire. List your diagnostic steps in order.
  - An MCP server shows needs authentication. What do you do?
  - Costs doubled this month. Where do you look first?
- **17.2.6 Organisation and leadership:**
  - How do you prove Claude Code is improving quality, not only speed?
  - How do you roll it out to 500 engineers with minimal risk?
  - What review norms change when most code is AI-written?

### Module 17.3 Break-it drills

- **17.3.1 Misconfigure on purpose:** wrong matcher, missing exit code, invalid JSON output, a skill with a vague description, an MCP server with wrong scope; diagnose each with the Part 12 toolkit
- **17.3.2 Stress the context:** load a huge file and watch behaviour; compare with a subagent doing the same read
- **17.3.3 Red-team your own setup:** plant a hostile instruction in a file and see what your permissions, sandbox and hooks stop

### Module 17.4 Progress tracker

| Part | Area | Current level | Target level | Evidence | Next module |
| --- | --- | --- | --- | --- | --- |
| 1 | Foundations |  | L3 |  |  |
| 2 | Core workflows |  | L4 |  |  |
| 3 | Context and memory |  | L4 |  |  |
| 4 | Configuration and control |  | L4 |  |  |
| 5 | Extensions |  | L4 to L5 |  |  |
| 6 | Parallel and autonomous |  | L3 to L4 |  |  |
| 7 | Surfaces and integrations |  | L3 |  |  |
| 8 | Agent SDK |  | L3 to L5 |  |  |
| 9 | Applied engineering |  | L4 |  |  |
| 10 | Enterprise and cost |  | L3 to L4 |  |  |
| 11 | Security |  | L4 |  |  |
| 12 | Troubleshooting |  | L4 |  |  |

### Module 17.5 Suggested pacing, not a deadline

- **17.5.1 First week:** Part 1, Part 2, Part 3.1 to 3.3; projects P1 to P4
- **17.5.2 First month:** Parts 3, 4 and 5.1 to 5.4; projects P7 to P13
- **17.5.3 Months two and three:** Parts 5.5 to 5.6, Part 6, Part 7; projects P15 to P23
- **17.5.4 Months four to six:** Parts 8 to 12; projects P24 to P32 as your role requires
- **17.5.5 Ongoing:** weekly What's New, monthly setup pruning, quarterly rebuild of your playbook

---

## Part 18: The frontier: what comes next

### Module 18.1 Where the tool is heading

- **18.1.1 Longer autonomy:** goals, workflows, background agents, scheduled and event-driven runs; the human role moves from driving to specifying and verifying
- **18.1.2 More surfaces, one engine:** terminal, desktop, web, mobile, chat and CI as interchangeable ways to reach the same agents
- **18.1.3 Extensibility as a platform:** skills, hooks, MCP, plugins, mods and the SDK turn Claude Code into a harness you can shape
- **18.1.4 Automated review and security** as standard pipeline stages
- **18.1.5 Enterprise-grade control:** policy, gateways, telemetry and data-handling options as table stakes

### Module 18.2 Elite practices

*Depth target: L5.*

- **18.2.1 Evaluate your own setup:** run the same tasks with claude -p under different CLAUDE.md, skill and hook configurations, and compare success rate, cost and time; treat configuration like code under test
- **18.2.2 Harness engineering:** designing the environment, tools, checks and feedback an agent works within, so the same model performs far better
- **18.2.3 Context engineering at scale:** layered instructions, path-scoped rules, on-demand skills, tool search, subagent isolation, compaction policy
- **18.2.4 Verification infrastructure:** fast reliable test suites, deterministic environments, visual checks and golden files that let agents self-correct
- **18.2.5 Multi-agent economics:** when parallelism pays for itself, how to cap runaway cost, how to design independent units
- **18.2.6 Cross-checking:** independent verifier agents that try to refute findings before humans see them
- **18.2.7 Agent-ready codebases:** modular structure, clear conventions, fast tests, good docs, typed interfaces and language servers
- **18.2.8 Spec-driven organisations:** specs and acceptance checks as the main artefacts engineers and PMs review

### Module 18.3 Open questions to think about

- **18.3.1 What happens to review** when code volume rises faster than reviewer attention?
- **18.3.2 How do teams keep skills and understanding** when agents do the routine work?
- **18.3.3 What is the right permission model** for agents that run for hours?
- **18.3.4 Where do liability and accountability sit** for AI-authored changes?
- **18.3.5 How should PM and engineering roles blur,** and where must they stay distinct?
- **18.3.6 What new bottlenecks appear:** product judgement, data, environments, compliance, customer feedback

### Module 18.4 Staying ahead

- **18.4.1 Weekly:** read What's New; try one feature
- **18.4.2 Monthly:** run your own benchmark tasks on the latest version and model; prune setup
- **18.4.3 Quarterly:** rewrite your playbook, update your team's shared configuration, and retire obsolete workarounds
- **18.4.4 Yearly:** decide where you want to be L5, and build and publish something in that area

### Closing principles

1. Context is the scarce resource; protect it.
2. Give Claude a check it can run, and make the check strong.
3. Put guarantees in hooks, sandboxes and permissions, not in polite instructions.
4. Start simple, and add each extension only when a real trigger appears.
5. Keep humans responsible for direction, review and risk.
6. Treat your configuration as code: version it, test it, prune it.
7. Re-read the docs every month; the tool will have changed.
