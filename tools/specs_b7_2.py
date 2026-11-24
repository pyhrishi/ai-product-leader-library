from specs_b7_common import G, run, T

M = "b-7-2"
SPECS = []
D = "Claude Code docs, Desktop, 2026"

# ------------------------------------------------------------------ 7.2.1
SPECS.append(G(M, "7.2.1", "Core features",
 thesis="The Desktop app's value is the review loop around Claude: isolated parallel sessions, panes for chat, diff, terminal and preview, and PR monitoring that keeps working after you look away.",
 prove="start two isolated sessions on one repository, review a diff with line comments, and turn on PR monitoring, naming each default you relied on.",
 disc="turn Worktree on before you start a session in a Git repository, because it is off by default.",
 counter="a Desktop session is not isolated unless you ask: the Worktree option is off by default, so two parallel sessions can edit the same files [Claude Code docs, Desktop, 2026].",
 read=23, prove_h="3",
 depth=["Name the main panes and the isolation default", "Run parallel sessions safely and review diffs with comments", "Design a team setup with worktree include files, launch.json and auto-fix"],
 deliverable="A walk-through log of two parallel isolated sessions, one reviewed diff with comments, and one monitored PR.",
 secs=[
 ("Parallel sessions and git isolation",
  "Each Desktop session has its own chat history, project folder, context and changes. Isolation is a choice: turn on Worktree before starting a session in a Git repository, because it is off by default [" + D + "].",
  """
| Item | Detail |
|---|---|
| New session | `Cmd+N` / `Ctrl+N` |
| Switch sessions | `Ctrl+Tab` / `Ctrl+Shift+Tab` |
| Split view | Hold Option (Mac) or Alt (Windows) and click a session |
| Worktree location | `<project-root>/.claude/worktrees/` by default |
| Copy ignored files such as `.env` into a new worktree | Add a `.worktreeinclude` file at the project root |
| Archive with uncommitted changes | Desktop asks; **Archive anyway** discards them |
| Cleanup | Local worktrees removed about 30 days after archiving or last opening |

An OS notification fires when a session finishes and you are not viewing it. Claude can also list, read, rename, archive and message your other Desktop sessions (it sees the 20 most recent by default) [" + D + "].
""".replace('" + D + "', D),
  ("Shared-tree collision", "You start two sessions on the same repository with Worktree off and both edit `src/auth.ts`, so each session's diff includes the other's changes.", "Turn Worktree on before the second session starts and add a `.worktreeinclude` for ignored files the app needs."),
  "worktrees themselves are Module 6.2; choosing a parallel approach is Module 6.1.", "Worktree on, or sessions share a tree."),
 ("Panes: chat, diff, terminal, editor, side chat",
  "Layout is a set of panes: chat, diff, browser, terminal, file, plan, tasks, subagent and, on macOS, the iOS Simulator. Pane layout, terminal, file editor and view modes require Desktop v1.2581.0 or later [" + D + "].",
  """
| Pane or tool | Open with | Notes |
|---|---|---|
| Terminal | `Ctrl+` backtick or title-bar button | Runs in the session's working directory; local and SSH sessions |
| File editor | Click a path in chat | Editable in local sessions inside the working directory; view-only in cloud, SSH and WSL; auto save on by default |
| Side chat | `Cmd+;` / `Ctrl+;` or `/btw` | Reads the main thread, adds nothing back, not saved to disk |
| Close focused pane | `Cmd+\\` / `Ctrl+\\` | Panes can pop out to their own window |
| View modes | `Ctrl+O` | Normal, Thinking, Verbose |

`/context` prints a per-category context breakdown and `/compact` summarizes early [" + D + "].
""".replace('" + D + "', D),
  ("Pane-sprawl", "You open every pane at once on a laptop screen, the chat shrinks to a sliver, and you miss a permission prompt that is waiting.", "Keep chat and one working pane visible, and move the rest into the overflow menu or a separate window."),
  "context management is Module 3.1; keyboard shortcuts are Module 14.2.", "side chat reads but never writes the main thread."),
 ("The review loop: diff, preview, PR monitor",
  "Open the diff from the Changes card, hover a line and click the plus to comment, then submit all comments with `Cmd+Enter` / `Ctrl+Enter`; Claude applies them and shows a new diff. Previews use `.claude/launch.json` [" + D + "].",
  """
| Feature | Fact |
|---|---|
| `autoVerify` | Defaults to on: Claude screenshots, checks errors and verifies after edits |
| `launch.json` port | Defaults to 3000; `autoPort: true` picks a free port |
| Secrets in `launch.json` | Do not put them in `env`; the file is committed |
| PR monitoring | Needs `gh` installed and authenticated |
| Auto-fix | From the PR's menu; fixes failing checks and, in local sessions, review comments from owners, members, collaborators or GitHub Apps |
| Merge when ready | Enables GitHub auto-merge; requests a squash merge unless a merge queue is used; needs auto-merge enabled in repo settings; disabled in SSH and WSL |
| `/code-review` | Results arrive as a Code review card with **Walk through in diff** and **Fix this one** |

[" + D + "]
""".replace('" + D + "', D),
  ("Comment-by-comment churn", "You submit diff comments one at a time, so Claude rewrites the same file five times and each rewrite invalidates the next comment.", "Leave all comments first, then submit them together with the keyboard shortcut."),
  "verification is Module 2.3; local review commands are Module 7.8.", "batch your diff comments, then send."),
 ],
 ret=[
 ("What is the default state of the Worktree option, and where do worktrees go?", "Off; `<project-root>/.claude/worktrees/`."),
 ("Which minimum Desktop version does the pane layout, terminal and file editor need?", "v1.2581.0."),
 ("Two sessions edit the same file because Worktree was off. Name the failure mode by its exact label.", "**Shared-tree collision.**"),
 ("You submit diff comments one at a time. Name the failure mode by its exact label.", "**Comment-by-comment churn.**"),
 ("The chat shrinks to a sliver and you miss a prompt. Name the failure mode.", "**Pane-sprawl.**"),
 ("What shortcut submits all diff comments?", "`Cmd+Enter` on Mac, `Ctrl+Enter` on Windows."),
 ("How long until Desktop removes an archived local worktree?", "About 30 days after archiving or last opening."),
 ("Which file copies gitignored files like `.env` into new worktrees?", "`.worktreeinclude` at the project root."),
 ("Which merge method does Merge when ready request?", "Squash, unless the base branch uses a merge queue."),
 ("Where is the side chat saved?", "Nowhere; it is not saved to disk."),
 ],
 steps=[("Turn Worktree on and start two sessions on one repo", "Two worktree paths"), ("Add a `.worktreeinclude` and confirm `.env` appears", "File listing"), ("Make one change per session", "Two diffs"),
        ("Leave three line comments and submit with the shortcut", "Updated diff"), ("Create a PR and turn on Auto-fix", "PR link"), ("Archive one session and note what was asked", "Dialog note")],
 pass_md="""
| Check | Evidence |
|---|---|
| Worktree on before start | Path under `.claude/worktrees/` |
| Comments batched | One submit, one new diff |
| PR monitored | Auto-fix toggle on, `gh auth status` ok |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Both sessions in the repo root | **Shared-tree collision** |
| Five separate comment submits | **Comment-by-comment churn** |
""",
 verdict="The artifact passes only if two distinct worktree paths are shown and the diff comments were submitted in one batch.",
 res=[("Anthropic", "Desktop application", "Sessions, worktrees, panes, diff review, PR monitoring", "Current; the managed-settings section was truncated in my fetch"), ("Anthropic", "Desktop quickstart", "Install and first session", "Not fetched")],
 dis="none found between the sources read.",
 reframe="This is the craft of the Desktop loop: **isolate, review in batches, and let monitoring run.** The engineer who understands this does not ask \"what does Desktop add?\" — they ask \"which default must I flip before I trust two sessions at once?\""))

# ------------------------------------------------------------------ 7.2.2
SPECS.append(G(M, "7.2.2", "Computer use and the built-in browser",
 thesis="Desktop gives Claude two ways onto screens, the built-in Browser pane for web pages and computer use for native apps, and both are last-resort tools gated by per-app or per-site approval.",
 prove="state the tool priority order, the three app tiers, and the approval choices, then run one browser task and one native-app task safely.",
 disc="use the most precise tool first: a connector, then Bash, then Chrome, and only then computer use.",
 counter="computer use acts on your real desktop, unlike the sandboxed Bash tool, so approving an app is closer to handing over a session than to enabling a feature [Claude Code docs, Computer use, 2026].",
 read=22, prove_h="2.5",
 depth=["Name the priority order, tiers and approval prompts", "Choose between the built-in Browser, Chrome and computer use", "Set denied apps and managed controls for a team"],
 deliverable="A tool-choice table for six tasks plus a record of one approval flow, showing which approval option you chose and why.",
 secs=[
 ("The tool priority order",
  "Claude tries the most precise tool first. In Desktop the order is connector, then Bash, then Claude in Chrome, then iOS Simulator, then computer use, which is the last resort [" + D + "].",
  """
| Rank | Tool | Use when |
|---|---|---|
| 1 | Connector (MCP) | A service has a structured integration |
| 2 | Bash | The task is a shell command |
| 3 | Claude in Chrome | Browser work as yourself, in logged-in sessions |
| 4 | iOS Simulator pane | Simulated iOS device (macOS) |
| 5 | Computer use | Native apps and GUI-only tools |

Computer use needs a Pro or Max plan (not Team or Enterprise), is a research preview, and requires macOS 14 or later or Windows. Enable it under Settings, This computer, System. On macOS, grant Accessibility and Screen Recording [" + D + "].
""".replace('" + D + "', D),
  ("Screen-first reflex", "You ask for computer use on a task a connector or shell command could do, and it takes minutes to click through what a command does in seconds.", "State the precise tool in the prompt, or ask Claude which of the five it will use before it starts."),
  "MCP connectors are Module 5.5; the CLI version of computer use is Module 7.6.", "last resort means last."),
 ("Approval tiers and what they permit",
  "App access is fixed by category, and you approve per app. The prompt offers Allow for this session or Deny; approvals last the session, or 30 minutes for Dispatch-spawned sessions [" + D + "].",
  """
| Tier | Capability | Typical apps |
|---|---|---|
| View only | Screenshots only | Browsers, trading platforms |
| Click only | Click and scroll; no typing or shortcuts | Terminals, IDEs |
| Full control | Click, type, drag, shortcuts | Everything else |

Settings include Denied apps (rejected without prompting) and Unhide apps when Claude finishes. On macOS, computer use can run in the background while you work in other apps. Claude flags possible prompt injection from on-screen content [" + D + "]. The docs for this guide do not state which Desktop version first shipped background computer use; check the changelog [not verified].
""".replace('" + D + "', D),
  ("Blanket-approval habit", "You click Allow for every prompt without reading which app is requested, including a terminal, which is equivalent to shell access.", "Read the app name and its warning, deny anything you did not expect, and add sensitive apps to Denied apps."),
  "least privilege is Module 11.3; prompt injection is Module 11.2.", "an approval is a delegation of your desktop."),
 ("The built-in Browser pane",
  "Open it with `Cmd+Shift+B` / `Ctrl+Shift+B` or the title-bar button. It uses a clean profile with no logins, and Google OAuth sign-in flows work. For logged-in sessions use the Chrome extension instead [" + D + "].",
  """
| Behavior | Detail |
|---|---|
| Write actions (click, type) on external pages | Reviewed by classifiers in every mode |
| Domain allowlist | Also checked in non-Auto, non-Bypass modes |
| First action on a site | Allow once, Always allow (per site, subdomains separate) or Deny |
| Localhost and project files | No approval needed |
| Claude will not | Buy things, create accounts or bypass CAPTCHAs without you |
| Managed control | `browserExternalPageTools` disables Claude's tools on external pages; `disableBrowserExternalNavigation` blocks external navigation |

[" + D + "]
""".replace('" + D + "', D),
  ("Always-allow creep", "You choose Always allow on a site once for convenience and later forget that Claude can now act there with no prompt.", "Use Allow once for sites you do not own, and review saved allowances periodically."),
  "Chrome is Module 7.6; managed settings are Module 10.4.", "the Browser is clean; Chrome is you."),
 ],
 ret=[
 ("Give the computer-use tool priority order.", "Connector, Bash, Claude in Chrome, iOS Simulator, computer use."),
 ("Which plans can use computer use in Desktop?", "Pro and Max, not Team or Enterprise."),
 ("You click Allow on every prompt including a terminal. Name the failure mode by its exact label.", "**Blanket-approval habit.**"),
 ("You use computer use for a task a command could do. Name the failure mode by its exact label.", "**Screen-first reflex.**"),
 ("You granted Always allow once and forgot. Name the failure mode.", "**Always-allow creep.**"),
 ("How long do approvals last in Dispatch-spawned sessions?", "30 minutes."),
 ("What is the minimum macOS version for Desktop computer use?", "macOS 14."),
 ("Which tier covers terminals and IDEs?", "Click only."),
 ("Which shortcut opens the built-in Browser?", "`Cmd+Shift+B` (Mac) or `Ctrl+Shift+B` (Windows)."),
 ("Does the Browser share your logged-in sessions?", "No; it uses a clean profile. Use the Chrome extension for logged-in sessions."),
 ],
 steps=[("Write the five-tool priority order", "Ranked list"), ("Enable computer use and grant both macOS permissions", "Settings screenshot"), ("Run a native-app task and read the approval prompt", "Prompt text"),
        ("Deny one app deliberately and observe the result", "Observation"), ("Run a Browser task with Allow once", "Transcript"), ("Write your Denied apps list", "List")],
 pass_md="""
| Task | Tool chosen | Approval |
|---|---|---|
| Read an API | Connector | n/a |
| Test a local web app | Browser pane | localhost, none |
| Drive a native app | Computer use | Allow for this session |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Computer use for a shell task | **Screen-first reflex** |
| Always allow on an external site by default | **Always-allow creep** |
""",
 verdict="The artifact passes only if each task names the tool by rank and the approval option chosen, with a denied-apps list included.",
 res=[("Anthropic", "Desktop application", "Computer use, tiers, Browser, approvals", "Current"), ("Anthropic", "Computer use (CLI)", "Same engine; safety model; lock file", "Current"), ("Anthropic", "Claude in Chrome", "Logged-in alternative", "Current")],
 dis="none found; the CLI page omits the iOS Simulator step from its order but otherwise matches the Desktop page.",
 reframe="This is the craft of screen control: **precise tools first, approvals as delegation.** The engineer who understands this does not ask \"can it click this?\" — they ask \"which tool is least powerful that still does the job?\""))

# ------------------------------------------------------------------ 7.2.3
SPECS.append(G(M, "7.2.3", "Dispatch from your phone",
 thesis="Dispatch lets you message a task from your phone and have it become a Code session on your Desktop, which makes it the lowest-setup way to delegate while away and the one most dependent on your computer staying on.",
 prove="state what Dispatch is, what it requires, where the work runs, and how it differs from Remote Control and cloud sessions.",
 disc="before you leave, confirm the Desktop app is running, the computer is awake and your plan is Pro or Max.",
 counter="Dispatch feels like a cloud feature because you use it from a phone, but the work runs on your machine through Desktop [Claude Code docs, Platforms and integrations, 2026].",
 read=16, prove_h="1.5",
 depth=["State what Dispatch is and where it runs", "Choose Dispatch versus Remote Control versus cloud", "Set up pairing and notification expectations for a delegate-while-away routine"],
 deliverable="A one-page comparison of Dispatch, Remote Control and cloud sessions with a rule for which you use when you leave your desk.",
 thin="The Claude Code docs describe Dispatch in only a few lines and link to a support article for pairing; I did not retrieve that article, so setup steps are not stated here.",
 secs=[
 ("What Dispatch is",
  "Dispatch is a persistent conversation in Cowork that can spawn Code sessions from your phone, with push notifications when a session finishes or needs approval. It requires a Pro or Max plan and is not available on Team or Enterprise [" + D + "].",
  """
| Property | Value |
|---|---|
| Trigger | Message a task from the Claude mobile app |
| Runs on | Your machine, through the Desktop app |
| Setup | Pair the mobile app with Desktop |
| Plans | Pro and Max only |
| Notifications | Sent when a spawned Code session finishes or needs approval |
| Computer-use approvals in Dispatch-spawned sessions | Last 30 minutes |

[Claude Code docs, Platforms and integrations and Desktop, 2026]. Pairing steps live in a support article that I did not retrieve [not verified].
""",
  ("Cloud-by-feel", "You treat a Dispatch task as a cloud task, shut the laptop and find nothing done on return.", "Dispatch runs on your machine; keep Desktop running and the computer awake, or use a cloud session instead."),
  "the surfaces are Module 7.1; mobile is Module 7.5.", "phone is the remote; the computer is the worker."),
 ("Dispatch versus Remote Control versus cloud",
  "All three let you act from a phone, but they differ in what is already running and where it executes [Claude Code docs, Mobile, 2026].",
  """
| | Dispatch | Remote Control | Cloud session / project |
|---|---|---|---|
| Starts from | A message to Dispatch | A session already running on your machine | A repository and a prompt |
| Runs on | Desktop on your machine | Your machine (CLI, Desktop or VS Code) | Anthropic cloud |
| Needs machine on | Yes | Yes | No |
| Plans | Pro, Max | Pro, Max, Team, Enterprise | Pro, Max, Team, Enterprise with seat conditions |

If your machine sleeps during Remote Control, Claude Code reconnects when it comes back online [Claude Code docs, Mobile, 2026].
""",
  ("Wrong-remote", "You choose Dispatch for a task that needs an already-open terminal session, when Remote Control would have continued that session in place.", "Use Remote Control to continue a session you already have, and Dispatch to start new work with minimal setup."),
  "Remote Control is Module 7.5; cloud sessions are Module 7.4.", "continue with Remote Control, delegate with Dispatch, offload with cloud."),
 ("Governance and approval load",
  "Dispatch-spawned Code sessions can ask for approvals, and sending one task from a phone can trigger computer use. Treat the delegation as granting a short-lived session on your desktop.",
  """
| Control | Where |
|---|---|
| Computer use in Dispatch sessions | Approval for 30 minutes per app [Claude Code docs, Desktop, 2026] |
| Block all Remote Control | `disableRemoteControl: true` in user settings stops sessions connecting to Remote Control (this setting is about Remote Control, not Dispatch) |
| Admin availability | Dispatch and computer use unavailable on Team and Enterprise |

I did not find a documented managed setting that disables Dispatch alone on plans where it is available [not verified].
""",
  ("Unattended-approval gap", "You dispatch a task that requests computer use, are not watching, and either it stalls or you approve from a phone prompt without reading it.", "Prefer tasks that need no screen control when you are away, and read the approval card before accepting."),
  "permission modes are Module 4.3; safety of remote access is Module 7.5.", "decide in advance what you will approve from a phone."),
 ],
 ret=[
 ("Which plans can use Dispatch?", "Pro and Max, not Team or Enterprise."),
 ("Where does a Dispatch task run?", "On your machine, through the Desktop app."),
 ("You shut the laptop expecting a Dispatch task to finish. Name the failure mode by its exact label.", "**Cloud-by-feel.**"),
 ("You used Dispatch where Remote Control would have continued an open session. Name the failure mode by its exact label.", "**Wrong-remote.**"),
 ("You approve a computer-use prompt from a phone unread. Name the failure mode.", "**Unattended-approval gap.**"),
 ("How long do computer-use approvals last in a Dispatch-spawned session?", "30 minutes."),
 ("When does Dispatch send a notification?", "When a spawned Code session finishes or needs your approval."),
 ("What is Dispatch described as living in?", "A persistent conversation in Cowork."),
 ("What does the guide say is not verified about Dispatch setup?", "The pairing steps, which live in a support article not retrieved."),
 ],
 steps=[("Write the Dispatch, Remote Control and cloud comparison from memory", "Three-column table"), ("Confirm your plan supports Dispatch", "Plan note"), ("Pair the app following the support article", "Pairing log"),
        ("Dispatch one harmless task and note the notification", "Notification time"), ("Close Desktop and note what happens", "Observation"), ("Write your leave-the-desk rule", "Rule")],
 pass_md="""
| Situation | Use |
|---|---|
| Continue open terminal session | Remote Control |
| Start new local work from phone | Dispatch |
| Laptop will be off | Cloud session |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Dispatch for an offline laptop | **Cloud-by-feel** |
| Plan Team listed as supported | Dispatch is Pro and Max only |
""",
 verdict="The artifact passes only if the rule says Dispatch needs the machine on and lists the plan limit.",
 res=[("Anthropic", "Desktop application", "Dispatch overview, approvals, plan limits", "Current; pairing steps not retrieved"), ("Anthropic", "Claude Code on mobile", "Where each remote option runs", "Current")],
 dis="none found between the sources read.",
 reframe="This is the craft of delegating from a phone: **know which machine does the work.** The engineer who understands this does not ask \"can I start it from here?\" — they ask \"will the worker still be on?\""))

# ------------------------------------------------------------------ 7.2.4
SPECS.append(G(M, "7.2.4", "Scheduled tasks",
 thesis="Desktop scheduled tasks run a fresh session on your machine on a timetable, with full local access, but only while the app is open and the computer is awake.",
 prove="create a local scheduled task, state what happens when the machine sleeps through a run, and choose between local, cloud and /loop for three jobs.",
 disc="write the prompt so it is correct even if the run starts hours late.",
 counter="a missed run is not retried many times: after sleep Desktop runs exactly one catch-up for the most recently missed time and discards older misses [Claude Code docs, Desktop scheduled tasks, 2026].",
 read=22, prove_h="2",
 depth=["Name the three scheduling options and the local task's constraints", "Write a prompt robust to late starts and permission prompts", "Design a schedule portfolio across local, cloud and loop"],
 deliverable="A local scheduled task with a late-start-safe prompt, a Run now test log, and a comparison of local, cloud and /loop for your jobs.",
 secs=[
 ("Local versus cloud versus loop",
  "Claude Code offers three ways to schedule work, and the Desktop page compares them [Claude Code docs, Desktop scheduled tasks, 2026].",
  """
| | Cloud | Desktop | `/loop` |
|---|---|---|---|
| Runs on | Cloud | Your machine | Your machine |
| Machine on required | No | Yes | Yes |
| Open session required | No | No | Yes |
| Local files | No (fresh clone) | Yes | Yes |
| Permission prompts | Auto mode by default | Configurable per task | Inherits session |
| Minimum interval | 1 hour | 1 minute when Claude sets it; 1 hour in the forms | 1 minute |

Local tasks need Claude Desktop 1.1.5368 or later. By default they run against whatever state the working directory is in, including uncommitted changes; select **Worktree** in the Edit form for an isolated worktree [Claude Code docs, Desktop scheduled tasks, 2026].
""",
  ("Wrong-timer", "You schedule a job that must run at 3 a.m. as a Desktop task, and the laptop is asleep so it never fires.", "Use a cloud scheduled task for work that must run with the machine off; use Desktop only when you need local files."),
  "cloud scheduled tasks are Module 7.4; loops and goals are Module 6.7.", "pick the scheduler by whether the machine will be on."),
 ("Creating and running a task",
  "Create one from the Scheduled page in the Code tab, or by describing it in a session, such as 'set up a daily code review that runs every morning at 9am'. A request like 'remind me at 3pm tomorrow' creates a one-time task [Claude Code docs, Desktop scheduled tasks, 2026].",
  """
| Option | Meaning |
|---|---|
| Hourly, Daily, Weekdays, Weekly | Presets; Desktop adds a small deterministic delay of a few minutes to stagger traffic |
| Manual | Runs only on **Run now** |
| Custom | Cron in local time; Sunday is `0`; names not accepted; forms reject more often than hourly |

Desktop checks the schedule every minute while the app is open. The task's name becomes a kebab-case folder; the prompt lives in `~/.claude/scheduled-tasks/<task-name>/SKILL.md`, with schedule, folder, model and enabled state kept elsewhere [Claude Code docs, Desktop scheduled tasks, 2026].
""",
  ("Silent-sleep skip", "The computer sleeps through the scheduled time, the run is skipped, and you assume the task ran.", "Turn on Keep computer awake under Settings, This computer, System, and read the History list, which shows skipped runs and why."),
  "skills and SKILL.md are Module 5.2; time-based work is Module 6.7.", "check History, not your memory."),
 ("Missed runs, permissions and prompt design",
  "When the app starts or the computer wakes, Desktop looks back seven days; if a task missed runs it starts exactly one catch-up for the most recently missed time. A task scheduled for 9am might run at 11pm [Claude Code docs, Desktop scheduled tasks, 2026].",
  """
```text
Prompt with guardrails:
Review only commits since the last run's timestamp in REVIEW_LOG.md.
If the current local time is after 17:00, skip the review and write
"missed run" with the date to REVIEW_LOG.md instead.
```

| Permission fact | Detail |
|---|---|
| Per-task permission mode | Set at creation or edit |
| Allow rules in `~/.claude/settings.json` | Also apply |
| Manual mode and an unapproved tool | The run stalls until you approve in the run's session |
| Fix | Click **Run now** after creating, approve with always allow, review in the Always allowed panel |
| Tools marked `requiresUserInteraction` | Prompt every call; runs stall each time |
""",
  ("Stale-run assumption", "The prompt says 'review today's commits' and a catch-up run at night reviews the wrong day or finds nothing.", "Anchor the prompt on a recorded timestamp or file, and add an explicit late-start rule."),
  "permissions are Module 4.2; MCP approval is Module 5.5.", "one catch-up, so write for lateness."),
 ],
 ret=[
 ("What minimum Desktop version do local scheduled tasks need?", "Claude Desktop 1.1.5368."),
 ("How many days back does Desktop check for missed runs, and how many catch-up runs does it start?", "Seven days; exactly one."),
 ("A 3 a.m. job never fired because the laptop slept. Name the failure mode by its exact label.", "**Wrong-timer.**"),
 ("The computer slept and you assumed the task ran. Name the failure mode by its exact label.", "**Silent-sleep skip.**"),
 ("A catch-up run reviewed the wrong day. Name the failure mode.", "**Stale-run assumption.**"),
 ("What is the minimum interval in the Desktop forms, and when can it be shorter?", "1 hour; 1 minute when Claude sets the schedule."),
 ("Where is a local task's prompt stored?", "`~/.claude/scheduled-tasks/<task-name>/SKILL.md`."),
 ("What does **Worktree** in the Edit form do?", "Gives each run its own isolated Git worktree."),
 ("What does cron `0` mean for day of week in a Desktop custom schedule?", "Sunday."),
 ("What setting stops idle sleep?", "Keep computer awake, under Settings, This computer, System."),
 ],
 steps=[("Create a local task for a harmless daily job", "Task page"), ("Write a prompt with a late-start rule", "Prompt text"), ("Run now and approve with always allow", "Allowed panel"),
        ("Sleep the machine across a scheduled time", "History entry"), ("Wake and observe catch-up", "Notification"), ("Compare to a cloud task for the same job", "Comparison")],
 pass_md="""
| Check | Evidence |
|---|---|
| Prompt has late-start rule | Quoted line |
| Run now tested | Approvals saved |
| Skipped run explained | History hover text |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| 'Review today's commits' with no anchor | **Stale-run assumption** |
| 3 a.m. job on a sleeping laptop | **Wrong-timer** |
""",
 verdict="The artifact passes only if the prompt survives a late start and a real skipped or caught-up run was observed in History.",
 res=[("Anthropic", "Desktop scheduled tasks", "Local tasks, missed runs, permissions", "Current"), ("Anthropic", "Automate work with scheduled tasks", "Cloud tasks, limits, triggers", "Current")],
 dis="none found between the sources read.",
 reframe="This is the craft of local schedules: **a machine that must be awake, a prompt that survives lateness.** The engineer who understands this does not ask \"did it run?\" — they ask \"what does History say, and what would the prompt do at 11pm?\""))

# ------------------------------------------------------------------ 7.2.5
SPECS.append(G(M, "7.2.5", "iOS Simulator pane",
 thesis="The iOS Simulator pane streams a per-session simulator next to the chat so Claude can build, install, tap and read your app while you watch, without taking over your screen.",
 prove="state the requirements, how the pane opens, the consent model, and the device lifecycle, and run a build-and-verify loop in a simulator.",
 disc="name the device and the goal in the prompt ('run it on the iPhone SE simulator and check onboarding') so the pane opens on the right target.",
 counter="the pane does not use computer use and needs no Accessibility or Screen Recording permission, because it drives the simulator directly [Claude Code docs, iOS Simulator, 2026].",
 read=19, prove_h="2",
 depth=["Name requirements, limits and consent rules", "Run and verify an iOS change through the pane", "Set org policy keys and decide when to fall back to CLI computer use"],
 deliverable="A verified-change log: a UI change built, run on a named simulator, checked by Claude, and re-checked by you with a screenshot saved.",
 secs=[
 ("Requirements and when it opens",
  "The pane is in public beta on macOS, available on Pro, Max, Team and Enterprise plans, except Enterprise organizations with a HIPAA configuration. It needs Claude Desktop v1.24012.0 or later and Xcode with the iOS platform installed [Claude Code docs, iOS Simulator, 2026].",
  """
| Requirement | Detail |
|---|---|
| Desktop version | v1.24012.0 or later |
| OS | macOS only |
| Xcode | Use Xcode 26.x; the pane does not yet work with Xcode 27 (Device Hub) |
| Session type | Local sessions only; not cloud or SSH |
| Opens when | Claude builds, installs, launches or checks the app in a simulator |
| Manual open | Views menu, iOS Simulator entry, once a session has a simulator or edited Swift files |

If `xcode-select` points at Xcode 27, select a 26.x install with `sudo xcode-select -s /Applications/Xcode-26.4.app` and confirm with `xcode-select -p` [Claude Code docs, iOS Simulator, 2026].
""",
  ("Xcode-27 mismatch", "The pane reports no simulators although devices exist, because `xcode-select` points at Xcode 27.", "Install Xcode 26.x alongside and point `xcode-select` at it, then restart the session."),
  "desktop basics are Module 7.2; the CLI route to the simulator is Module 7.6.", "match the Xcode, then ask in terms of running the app."),
 ("Consent and who drives the device",
  "The first time Claude uses a simulator, Desktop asks you to allow it. Consent is once per device, not per session, and covers controlling the device and taking screenshots [Claude Code docs, iOS Simulator, 2026].",
  """
| Action | Governed by |
|---|---|
| Tap, type, launch, screenshot on an allowed device | One-time device consent |
| Opening a URL on the device | Your session permission mode |
| Building the app (`xcodebuild`) | Your session permission mode |
| Turn off Claude's access | Desktop settings, or managed `disableMobileSimulatorTools` |
| Disable the pane entirely | `requireCoworkFullVmSandbox` policy key |

Claude's screenshots of the device are sent to Anthropic and kept under your normal retention settings, so do not sign in to real accounts on a device Claude uses. While Claude drives, a **Claude is using this device** badge shows; wait for it to clear before tapping [Claude Code docs, iOS Simulator, 2026].
""",
  ("Real-account leak", "You sign in to a personal Apple or app account on a simulator Claude controls, and screenshots of it are sent to Anthropic.", "Use test accounts and seeded data on any device Claude uses."),
  "data handling is Module 10.7; secrets are Module 11.4.", "treat the device as a shared screen."),
 ("Device lifecycle and the verify loop",
  "Each device belongs to the session that launched it, so parallel sessions do not share a device. Up to 4 devices can open per session. Desktop shuts down simulators it booted when you quit, archive the session, or 10 minutes after you detach a device; devices you booted yourself are never shut down automatically [Claude Code docs, iOS Simulator, 2026].",
  """
```text
Prompt: Build the app, run it on the iPhone SE simulator, tap through
onboarding, and tell me if any screen takes longer than one second to load.
Then screenshot the failing screen. After you fix it, relaunch and verify.
```

| Control | Shortcut |
|---|---|
| Home | `Cmd+Shift+H` |
| Lock | `Cmd+L` |
| Rotate | `Cmd+Right Arrow` |
| Screenshot / recording | `Cmd+S` / `Cmd+R`, saved to Desktop |

Claude drives simulated devices only; it cannot control a physical iPhone [Claude Code docs, iOS Simulator, 2026].
""",
  ("Tap-collision", "You tap through the app while Claude is mid-test, so the app state Claude reads is not the state its steps produced.", "Wait for the badge to clear, or tap to a state first and then ask Claude to check it."),
  "verification loops are Module 7.6 and Module 2.3.", "one driver at a time."),
 ],
 ret=[
 ("What minimum Desktop version does the pane need?", "v1.24012.0."),
 ("Which Xcode line works and which does not yet?", "Xcode 26.x works; Xcode 27 does not yet."),
 ("The pane shows no simulators with Xcode 27 selected. Name the failure mode by its exact label.", "**Xcode-27 mismatch.**"),
 ("You sign into your real account on the simulator. Name the failure mode by its exact label.", "**Real-account leak.**"),
 ("You tap while Claude is testing. Name the failure mode.", "**Tap-collision.**"),
 ("How many devices can open per session?", "Up to 4."),
 ("After how long does Desktop shut down a simulator you detached?", "10 minutes."),
 ("Does the pane need Accessibility or Screen Recording?", "No; it drives the simulator directly."),
 ("Which managed key blocks Claude's simulator tools?", "`disableMobileSimulatorTools`."),
 ("Is the pane available in cloud or SSH sessions?", "No; local sessions only."),
 ],
 steps=[("Check Xcode version and `xcode-select -p`", "Command output"), ("Open an iOS project in a local session and ask Claude to run it", "Pane screenshot"), ("Grant device consent and note the prompt", "Consent note"),
        ("Introduce a bug, ask Claude to find it", "Finding"), ("Fix and relaunch; verify", "Second screenshot"), ("Detach and note shutdown timing", "Timing note")],
 pass_md="""
| Check | Evidence |
|---|---|
| Xcode 26.x selected | `xcode-select -p` path |
| Named device | iPhone SE in prompt |
| Verify after fix | Before and after screenshots |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Real Apple ID signed in | **Real-account leak** |
| Verified once, before fix | No post-fix check |
""",
 verdict="The artifact passes only if before and after screenshots come from the same named device and no real account appears.",
 res=[("Anthropic", "Test iOS apps in the simulator", "Requirements, consent, lifecycle, policy keys", "Current; public beta"), ("Anthropic", "Computer use (CLI)", "CLI route to the simulator", "Current")],
 dis="none found between the sources read.",
 reframe="This is the craft of the simulator pane: **a per-session device, one-time consent, one driver at a time.** The engineer who understands this does not ask \"can it tap?\" — they ask \"which device, which Xcode, and who is driving right now?\""))

# ------------------------------------------------------------------ 7.2.6
SPECS.append(G(M, "7.2.6", "Platform notes",
 thesis="Desktop runs everywhere but not identically: macOS and Windows are first-class, Linux is a Debian-family beta, and WSL sessions trade several features for a Linux toolchain.",
 prove="state the install path and the missing features for macOS, Windows, Linux beta and WSL 2, and choose the right route for a given machine.",
 disc="before relying on a Desktop feature, check the platform page's list of what is missing on your platform.",
 counter="Desktop on Linux is supported only on Debian-based distributions; Fedora, RHEL and Arch users are told to use the CLI instead [Claude Code docs, Desktop on Linux, 2026].",
 read=21, prove_h="2",
 depth=["Name install routes and the missing features per platform", "Decide between Windows native, WSL 2 and the CLI for a project", "Plan a mixed-OS team rollout"],
 deliverable="A platform matrix of install route, missing features and fallback for macOS, Windows, Linux beta and WSL 2.",
 secs=[
 ("Install routes",
  "Installs differ by platform [" + D + "]; the Linux page gives the apt route [Claude Code docs, Desktop on Linux, 2026].",
  """
| Platform | Install | Updates |
|---|---|---|
| macOS | Universal `.dmg` (Intel and Apple Silicon) | Claude, Check for Updates |
| Windows | x64 installer; ARM64 installer is separate | Help, Check for Updates |
| Linux (beta) | Anthropic apt repository, or a downloaded `.deb` | Your system's regular package updates (`sudo apt update && sudo apt upgrade`); the app does not update itself |

Linux requirements: Ubuntu 22.04 or later, or Debian 12 or later, on x86_64 or arm64. Verify the repository signing key fingerprint `31DDDE24DDFAB679F42D7BD2BAA929FF1A7ECACE` before installing [Claude Code docs, Desktop on Linux, 2026].
""".replace('" + D + "', D),
  ("Distro-blind install", "You try the apt route on Fedora or Arch and the package never appears.", "Use the CLI on non-Debian distributions, which the docs say supports a wider range."),
  "installation overall is Module 1.3; the CLI fallback is Module 7.1.", "Debian family for Desktop, anything for the CLI."),
 ("Linux beta: what is missing",
  "The Linux beta gives parallel sessions, visual diff review, an integrated terminal and editor, and live preview, but several things are absent [Claude Code docs, Desktop on Linux, 2026].",
  """
| Missing on Linux beta | Detail |
|---|---|
| Computer Use | Not available |
| Dictation | Not available; use CLI voice dictation |
| Quick Entry global hotkey | Works on X11; native Wayland needs the GlobalShortcuts portal |
| Fedora and RHEL | Unsupported today |
| Cowork (for Dispatch) | Needs KVM, QEMU and UEFI firmware, and `kvm` group membership; checked once at launch |

Common fixes: sign-in not saved means a locked or missing keyring (install `gnome-keyring` or avoid having both keyrings under KDE Plasma); running as root without `--no-sandbox` is not supported [Claude Code docs, Desktop on Linux, 2026].
""",
  ("Cowork-prereq miss", "Dispatch or Cowork reports it needs QEMU or KVM because you installed with `--no-install-recommends` or never joined the `kvm` group.", "Install the recommended QEMU packages, enable virtualization in firmware, add your user to `kvm`, then log out and in and restart the app."),
  "Dispatch is covered earlier in Module 7.2; remote access is Module 7.5.", "check the requirements once at launch, restart after fixing."),
 ("WSL 2 sessions",
  "On Windows, the Code tab can run a session inside a WSL 2 distribution: Claude Code, its tools and git all run in the distribution, with Linux paths [Claude Code docs, Desktop in WSL, 2026].",
  """
| Fact | Detail |
|---|---|
| Requirements | Windows 10 or 11 with WSL 2 (WSL 1 unsupported); a distribution; git inside it |
| Trust | Granted per distribution and folder |
| Works | Parallel sessions, side chats, diff review, PR status, worktrees |
| Missing | Integrated terminal, connectors and plugins, session forking, file browser pane, `@` file suggestions |
| Merge when ready | Disabled in WSL |
| Editor | Open in editor uses VS Code Remote - WSL |

Use WSL when your repo lives in the distribution's filesystem; working on it from Windows goes through a network filesystem that is slow and breaks file watching [Claude Code docs, Desktop in WSL, 2026]. On managed devices WSL sessions may be unavailable.
""",
  ("Cross-filesystem slog", "You keep the repository on the Windows side and run a WSL session on it, so file watching breaks and everything is slow.", "Keep the repository inside the distribution and open it with a WSL session."),
  "IDE use under WSL is Module 7.3; sandboxing is Module 4.4.", "repo and session in the same filesystem."),
 ],
 ret=[
 ("Which Linux distributions does the Desktop beta support?", "Ubuntu 22.04 or later and Debian 12 or later."),
 ("Which CPU architectures does it support?", "x86_64 and arm64."),
 ("You tried the apt route on Fedora. Name the failure mode by its exact label.", "**Distro-blind install.**"),
 ("Cowork reports it needs QEMU or KVM. Name the failure mode by its exact label.", "**Cowork-prereq miss.**"),
 ("The repo is on the Windows side and the WSL session is slow. Name the failure mode.", "**Cross-filesystem slog.**"),
 ("Does Desktop update itself on Linux?", "No; updates arrive through the system's package updates."),
 ("Which WSL version is supported?", "WSL 2 only."),
 ("Name three features missing in WSL sessions.", "Any of: integrated terminal, connectors and plugins, session forking, file browser pane, `@` file suggestions."),
 ("Is Computer Use available on Linux?", "No."),
 ("Is the ARM64 Windows installer the same as x64?", "No; it is separate."),
 ],
 steps=[("Make the four-column matrix", "Blank matrix"), ("Fill install route per platform", "Routes"), ("Fill missing features per platform", "Gaps"), ("Fill the fallback per platform", "Fallbacks"),
        ("Verify each cell against the linked page", "Corrections"), ("Choose a route for your own machine", "Decision")],
 pass_md="""
| Platform | Route | Gap | Fallback |
|---|---|---|---|
| Linux beta | apt | No computer use | CLI |
| WSL 2 | WSL session | No terminal pane | VS Code remote |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Fedora listed as supported | **Distro-blind install** |
| WSL 1 listed | Not supported |
""",
 verdict="The artifact passes only if every platform's gap list matches the docs and a fallback is named for each.",
 res=[("Anthropic", "Desktop on Linux (beta)", "apt install, requirements, gaps", "Current"), ("Anthropic", "Desktop in WSL", "WSL 2 sessions and gaps", "Current"), ("Anthropic", "Desktop application", "macOS and Windows installers", "Current")],
 dis="none found between the sources read.",
 reframe="This is the craft of platform fit: **the same app, different gaps.** The engineer who understands this does not ask \"does Desktop work on my OS?\" — they ask \"which features vanish there, and what is my fallback?\""))

# ------------------------------------------------------------------ 7.2.7
SPECS.append(G(M, "7.2.7", "Enterprise configuration",
 thesis="Managed settings reach Desktop sessions through a short list of named keys, and an administrator can restrict permission modes, browser tools, remote access and SSH hosts without touching each user's machine.",
 prove="name the managed keys that affect Desktop and state what each one blocks, plus the plan limits that no key can change.",
 disc="separate what a managed key can switch off from what a plan simply does not include.",
 counter="some Desktop features are unavailable on Team and Enterprise by plan, not by policy: computer use and Dispatch need Pro or Max, so no setting turns them on for an enterprise [Claude Code docs, Desktop, 2026].",
 read=21, prove_h="2",
 depth=["Name the managed keys and what each controls", "Map a security requirement to the right key", "Design a Desktop policy bundle for a regulated team"],
 deliverable="A policy table mapping five security requirements to the exact managed key, with the user-visible effect and the failure when it is missing.",
 thin="The Desktop page's full managed-settings section was truncated in my fetch, so the key list below covers only keys named elsewhere on the page; other keys may exist.",
 secs=[
 ("The keys the Desktop page names",
  "Managed settings apply to Desktop sessions through named keys. The page names the following [" + D + "].",
  """
| Key | Effect |
|---|---|
| `disableAutoMode` | Turns off Auto permission mode |
| `browserExternalPageTools` | Disables Claude's tools on external pages; users can still browse |
| `disableBrowserExternalNavigation` | Blocks all external navigation in the Browser; localhost still works |
| `disableSideloadFlags` | Withholds some local skills and plugins, blocks local skill loading |
| `disableRemoteControl` | Stops sessions connecting to Remote Control |
| `remoteControlAtStartup` | Default for new sessions; overridden once the user saves a Desktop setting |
| `crossSessionInbound` | `refuse` drops inbound cross-session messages |
| `sshHostAllowlist` | Restricts which SSH hosts users can connect to |

Admins can also restrict available permission modes, and local sessions can be disabled per device, shown as **Disabled by your organization** [" + D + "]. The iOS Simulator adds `disableMobileSimulatorTools` and `requireCoworkFullVmSandbox` [Claude Code docs, iOS Simulator, 2026].
""".replace('" + D + "', D),
  ("Key-from-memory", "You write a policy using a key name you half-remember and it silently does nothing.", "Copy key names from the settings reference and test each one by trying the blocked action as a user."),
  "managed settings are Module 10.4; the settings reference is Module 14.6.", "a misspelled key is a policy that does not exist."),
 ("Plan limits versus policy",
  "Not every gap is a policy. Some features are simply not offered on some plans, and a key cannot add them.",
  """
| Feature | Availability |
|---|---|
| Computer use (Desktop) | Pro and Max only; not Team or Enterprise |
| Dispatch | Pro and Max only |
| Bypass permissions mode | Pro and Max: enable in Settings; Team and Enterprise: org policy |
| Auto mode | Needs a supported model on the Anthropic API; admins can disable with `disableAutoMode` |
| Enterprise providers | Desktop supports Google Cloud's Agent Platform and gateway providers; Amazon Bedrock or Microsoft Foundry need the CLI, an IDE extension or Claude Desktop on 3P |

[" + D + "]. The iOS Simulator pane is available on Team and Enterprise except Enterprise organizations with HIPAA configuration [Claude Code docs, iOS Simulator, 2026].
""".replace('" + D + "', D),
  ("Policy-for-a-plan-gap", "You search for a managed key to enable computer use for your Enterprise team and conclude the product is broken.", "Check the plan table first; if the plan excludes the feature, no key changes that."),
  "plans and limits are Module 1.4; backends are Module 10.2.", "plan first, policy second."),
 ("Designing a policy bundle",
  "Group keys by the risk they close, then test each as an ordinary user.",
  """
| Requirement | Key or control | User sees |
|---|---|---|
| No unattended classifier-driven actions | `disableAutoMode` | Auto absent from the selector |
| No remote steering of local sessions | `disableRemoteControl: true` | Sessions cannot connect |
| No browsing of arbitrary sites | `disableBrowserExternalNavigation` | External navigation blocked, localhost works |
| SSH only to approved hosts | `sshHostAllowlist` | Others rejected; allowlist jump hosts too |
| No local third-party skills | `disableSideloadFlags` | Local skills withheld |

For SSH, the docs say jump hosts and proxied hosts must appear in `sshHostAllowlist`; run `ssh -G <host>` to get the hostname to allowlist [" + D + "].
""".replace('" + D + "', D),
  ("Untested-policy", "You ship a policy bundle and never try the blocked actions, so one key is mistyped and the control is absent for months.", "After each change, attempt every blocked action as a normal user and record the refusal."),
  "rollout is Module 10.1; incident response is Module 11.8.", "every key gets a user-side test."),
 ],
 ret=[
 ("Which key turns off Auto permission mode?", "`disableAutoMode`."),
 ("Which key stops sessions connecting to Remote Control?", "`disableRemoteControl`."),
 ("You wrote a policy with a misremembered key and nothing happened. Name the failure mode by its exact label.", "**Key-from-memory.**"),
 ("You hunted for a key to enable computer use on Enterprise. Name the failure mode by its exact label.", "**Policy-for-a-plan-gap.**"),
 ("You never tested a shipped bundle. Name the failure mode.", "**Untested-policy.**"),
 ("Which plans can use Dispatch and computer use?", "Pro and Max only."),
 ("What must appear in `sshHostAllowlist` besides destination hosts?", "Jump hosts and proxied hosts."),
 ("What does `crossSessionInbound` set to `refuse` do?", "Drops inbound cross-session messages."),
 ("What does a disabled local session show?", "Disabled by your organization."),
 ("What does the guide say is not covered in the retrieved text?", "The full managed-settings section of the Desktop page."),
 ],
 steps=[("List five security requirements for a team", "Requirement list"), ("Map each to a key or plan fact", "Map"), ("Write the bundle as JSON for managed settings", "Draft JSON"), ("Confirm key names against the settings reference", "Corrections"),
        ("Test each as an ordinary user", "Refusal log"), ("Record what no key can change", "Plan-limit list")],
 pass_md="""
| Requirement | Control | Tested |
|---|---|---|
| No Auto mode | `disableAutoMode` | Selector lacks Auto |
| No remote | `disableRemoteControl` | Connect fails |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Key 'disableComputerUse' | **Key-from-memory** (not a documented key here) |
| Never tested | **Untested-policy** |
""",
 verdict="The artifact passes only if every key appears in the docs, every row has a refusal log, and plan limits are listed separately.",
 res=[("Anthropic", "Desktop application", "Named managed keys and plan limits", "Current; managed section truncated in retrieval"), ("Anthropic", "iOS Simulator", "Simulator policy keys", "Current")],
 dis="none found between the sources read.",
 reframe="This is the craft of Desktop policy: **named keys, tested refusals, and honesty about plan limits.** The engineer who understands this does not ask \"what can I lock down?\" — they ask \"which key does that, and did I watch it refuse?\""))

if __name__ == "__main__":
    run(SPECS)
