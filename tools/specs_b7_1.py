from specs_b7_common import G, run, T

M = "b-7-1"
SPECS = []

# ------------------------------------------------------------------ 7.1.1
SPECS.append(G(M, "7.1.1", "The surfaces",
 thesis="Claude Code is one engine with many front ends, so choosing a surface is choosing where the work runs, who can see it and what you review it with, not choosing a different product.",
 prove="name each of the six platforms and six integrations from memory and say, for each, where Claude actually executes.",
 disc="before you start a task, say out loud where the session will run (your machine, Anthropic cloud, or your own infrastructure).",
 counter="the most capable surface is the terminal, and the prettier surfaces are deliberate trade-offs, not upgrades: scripting and the Agent SDK are CLI-only [Claude Code docs, Platforms and integrations, 2026].",
 read=21, prove_h="2",
 depth=["Name the surfaces and the integrations and what each is for", "Choose a surface for a task and predict what you give up", "Design a team setup that mixes surfaces without duplicating configuration"],
 deliverable="A one-page surface map: every platform and integration, where it runs, and one task you would give it.",
 secs=[
 ("Six platforms, one engine",
  "The platforms page says Claude Code runs the same underlying engine everywhere, but each surface is tuned for a different way of working [Claude Code docs, Platforms and integrations, 2026]. The six platforms are the CLI, Desktop, VS Code, JetBrains, Web and Mobile.",
  """
| Platform | Best for (per the docs) | Where Claude runs |
|---|---|---|
| CLI | Terminal workflows, scripting, remote servers | Your machine |
| Desktop | Visual review, parallel sessions, managed setup | Your machine (local), or cloud and SSH from the same app |
| VS Code | Working inside VS Code without a terminal | Your machine |
| JetBrains | IntelliJ, PyCharm, WebStorm and other JetBrains IDEs | Your machine, in the IDE's terminal |
| Web | Long-running tasks that need little steering | Cloud, Anthropic-managed by default |
| Mobile | Starting and monitoring tasks while away | Cloud sessions, or your machine through Remote Control |

The docs call the CLI the most complete surface for terminal-native work: scripting and the Agent SDK are CLI-only, and Desktop and the IDE extensions trade some CLI-only features for visual review and tighter editor integration [Claude Code docs, Platforms and integrations, 2026]. Mobile is described as a thin client into cloud sessions or into a local session through Remote Control.
""",
  ("Surface-as-product", "You treat Desktop, the IDE extension and the CLI as separate tools, so you configure each from scratch and conclude 'it behaves differently' when the real difference is a missing CLI-only feature.", "Start from the engine: check the docs' feature comparison for the specific feature before assuming a bug, and keep shared configuration in the files all local surfaces read."),
  "the module overview is Module 7.1; the extension layer that every surface shares is Module 5.1; cloud sessions in depth are Module 7.4.", "same engine, different trade-offs; the CLI has the most."),
 ("Six integrations and what they connect",
  "Integrations let Claude work with services outside your codebase. The platforms page lists Chrome, GitHub Actions, GitLab CI/CD, Code Review, Slack and Claude Tag, and says MCP servers and connectors cover almost anything else, such as Linear, Notion or Google Drive [Claude Code docs, Platforms and integrations, 2026].",
  """
| Integration | What it does | Use it for |
|---|---|---|
| Chrome | Controls your browser with your logged-in sessions | Testing web apps, filling forms, sites with no API |
| GitHub Actions | Runs Claude in your CI pipeline | PR reviews, issue triage, scheduled maintenance |
| GitLab CI/CD | Same as GitHub Actions for GitLab | CI-driven automation on GitLab |
| Code Review | Reviews every PR automatically | Catching bugs before human review |
| Slack | Responds to `@Claude` mentions | Turning bug reports into pull requests |
| Claude Tag | `@Claude` as the organization's shared identity, admin-configured access | Shared team access on Team and Enterprise plans |

Notice that only Chrome acts on your own machine and browser; the rest run in CI runners or Anthropic's cloud. That difference decides what they can see and what credentials they hold.
""",
  ("Integration-sprawl", "You switch on Chrome, Slack, Actions and Code Review at once for a small team and nobody can say which one posted a given comment or spent a given token.", "Add one integration per workflow, name its owner, and record the trigger and the identity it acts as before adding the next."),
  "Chrome is Module 7.6; Slack and Claude Tag are Module 7.7; Actions, GitLab and Code Review are Module 7.8.", "each integration is a trigger plus an identity; know both."),
 ("What is shared and what is not",
  "You can mix surfaces on the same project: configuration, project memory and MCP servers are shared across the local surfaces [Claude Code docs, Platforms and integrations, 2026]. Cloud and Mobile are different: cloud sessions work from a fresh clone and do not read your local user settings (Module 7.4).",
  """
| Thing | Local surfaces (CLI, Desktop local, IDE) | Cloud session |
|---|---|---|
| CLAUDE.md in the repo | Read | Read from the clone |
| Your user settings | Read | Not read; set environment variables or commit project settings |
| MCP servers added with `claude mcp add` | Read | Not carried; use connectors or a committed `.mcp.json` |
| Local files not committed | Visible | Absent unless bundled by `--cloud` |

Source for the cloud column: [Claude Code docs, Cloud sessions and Scheduled tasks, 2026]. Where a cloud session differs, the docs tell you to commit the setting to the repository or use an environment variable.
""",
  ("Phantom-config", "You tune permissions and MCP servers in your user settings, then start a cloud session and are surprised that none of it applies.", "List what the session needs, and move each item into the repository or the cloud environment before you start it."),
  "settings precedence is Module 4.1; the environment layer is Module 4.5.", "local surfaces share config; cloud sessions need it in the repo or environment."),
 ],
 ret=[
 ("Name the six platforms the docs list.", "CLI, Desktop, VS Code, JetBrains, Web and Mobile."),
 ("Name the six integrations on the platforms page.", "Chrome, GitHub Actions, GitLab CI/CD, Code Review, Slack and Claude Tag."),
 ("Which surface is described as the most complete for terminal-native work, and which two things are CLI-only?", "The CLI; scripting and the Agent SDK."),
 ("You configured permissions in user settings and a cloud session ignored them. Name the failure mode by its exact label.", "**Phantom-config.**"),
 ("You enabled four integrations in a week and cannot tell which one commented. Name the failure mode by its exact label.", "**Integration-sprawl.**"),
 ("You assume Desktop and the CLI are unrelated products and file a bug for a missing feature. Name the failure mode.", "**Surface-as-product.**"),
 ("How many platforms and how many integrations does the page list in its tables?", "Six platforms and six integrations."),
 ("What do the docs call the Mobile surface?", "A thin client into cloud sessions, or into a local session via Remote Control."),
 ("Which integration acts with your logged-in browser sessions?", "Chrome."),
 ("What is shared across the local surfaces?", "Configuration, project memory and MCP servers."),
 ],
 steps=[("List the six platforms and six integrations from memory", "A two-column list"), ("Add a 'where it runs' column and mark which run on your machine", "Annotated table"),
        ("Pick one real task per platform", "Six task lines"), ("Check each claim against the platforms page", "Corrections list"),
        ("Mark which items need config moved into the repo for cloud use", "A config inventory"), ("Write the one-line rule you will use to choose", "Decision sentence")],
 pass_md="""
| Surface | Runs where | Task | Gives up |
|---|---|---|---|
| CLI | My machine | Scripted migration | Visual diffs |
| Web | Anthropic cloud | Overnight test fix | Local MCP servers |
| Chrome | My browser | Verify a login form | Isolation from my sessions |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Says Desktop is 'a different tool' | **Surface-as-product** |
| Cloud row lists my user settings as available | **Phantom-config** |
""",
 verdict="The artifact passes only if every row names where Claude executes and at least one thing given up, with the cloud row listing config that must move into the repo.",
 res=[("Anthropic", "Platforms and integrations", "The six platforms, six integrations, shared config", "Current"), ("Anthropic", "Use Claude Code in the cloud", "Cloud sessions keep running after you disconnect", "Current")],
 dis="none found between the sources read.",
 reframe="This is the craft of choosing a surface: **one engine, many front ends, and a clear answer to where it runs.** The engineer who understands this does not ask \"which app is best?\" — they ask \"where should this session execute, and what does it need to see?\""))

# ------------------------------------------------------------------ 7.1.2
SPECS.append(G(M, "7.1.2", "Decision guide",
 thesis="The platforms page compares the surfaces on four axes (trigger, where Claude runs, setup, best use), and a good choice falls out of answering those four in order.",
 prove="given five tasks, pick a surface for each and justify it using trigger, runs-on, setup and fit.",
 disc="decide by the question 'does this need my machine, or must it survive my laptop closing?' before anything else.",
 counter="more autonomy is not always more distance: Remote Control and Dispatch both leave Claude on your machine, so closing the laptop ends them [Claude Code docs, Mobile, 2026].",
 read=22, prove_h="2",
 depth=["Read the comparison table and say what each column decides", "Choose between surfaces for a given task and defend it", "Design a default routing policy for a team"],
 deliverable="A decision tree on one page, tested against five real tasks from your own recent work.",
 secs=[
 ("The away-from-terminal table",
  "The platforms page has a table for work when you are away from your terminal. Each row differs in what triggers the work, where Claude runs, how much setup it takes, and what it is best for [Claude Code docs, Platforms and integrations, 2026].",
  """
| Option | Trigger | Claude runs on | Best for |
|---|---|---|---|
| Dispatch | Message a task from the mobile app | Your machine (Desktop) | Delegating while away, minimal setup |
| Remote Control | Drive a running session from claude.ai/code or the app | Your machine (CLI, Desktop or VS Code) | Steering in-progress work from another device |
| Channels | Push events from Telegram, Discord or your own server | Your machine (CLI) | Reacting to external events |
| Slack | Mention `@Claude` in a channel | Anthropic cloud | PRs and reviews from team chat |
| Self-hosted environments | Start a cloud session, pick your organization's environment | Your organization's infrastructure | Cloud sessions that must run inside your network |
| Scheduled tasks | Set a schedule | CLI, Desktop or cloud | Recurring automation |

[Claude Code docs, Platforms and integrations, 2026]. Dispatch requires a Pro or Max plan and is not available on Team or Enterprise [Claude Code docs, Mobile, 2026].
""",
  ("Laptop-lid assumption", "You start Remote Control or a Dispatch task, close the laptop and expect work to continue, because the session feels remote.", "If the machine will be off, use a cloud session or a project; if it must stay local, keep the machine on with the app running."),
  "the surfaces themselves are Module 7.1; Remote Control is Module 7.5; scheduled tasks are Module 7.4.", "ask where it runs before asking how you reach it."),
 ("Four questions, in order",
  "The table reduces to four questions. Asked in order, each removes options: does it need local files or tools, must it survive your laptop closing, who triggers it, and who else must see it?",
  """
```text
1. Needs local files, MCP servers or tools only on your machine?
     yes -> CLI / Desktop / IDE; reach it from afar with Remote Control (machine stays on)
     no  -> continue
2. Must keep running with the laptop closed?
     yes -> cloud session (browser, mobile, --cloud) or cloud scheduled task
3. Triggered by an event, not a person?
     yes -> GitHub Actions / GitLab CI, Code Review, API or GitHub trigger on a scheduled task
4. Team must see and steer it in chat?
     yes -> Slack or Claude Tag
```

This tree is a synthesis of the platforms page; the page itself does not publish a tree [secondary: this guide's reading of Claude Code docs, Platforms and integrations, 2026]. Test it against your own cases before adopting it.
""",
  ("Tool-first selection", "You pick a surface because it is the one you have open, and a task that needs your database credentials lands in a cloud sandbox that cannot reach them.", "Answer question 1 and 2 before opening anything, and write the answer in the task's first line."),
  "cloud environments are Module 4.5 and Module 7.4; permission modes are Module 4.3.", "choose by need, not by what is open."),
 ("Default routing for a team",
  "A team decision guide is a default plus exceptions. Three defaults cover most teams: local for exploratory or secret-touching work, cloud for long unattended work on GitHub repositories, CI for event-driven jobs.",
  """
| Task type | Default surface | Exception |
|---|---|---|
| Debugging with prod-like data | CLI or IDE | None; keep it local |
| Overnight refactor on a GitHub repo | Cloud session | Local if it needs private MCP servers |
| Review every PR | Code Review (Team/Enterprise) or Actions | `/code-review` locally for one-offs |
| Bug report in Slack | Slack or Claude Tag | CLI if the fix needs local repro |
| Weekly dependency check | Scheduled task | `/loop` for in-session polling |

Cloud scheduled tasks need no open machine; Desktop tasks run only while the app is open and the computer awake [Claude Code docs, Scheduled tasks and Desktop scheduled tasks, 2026].
""",
  ("Default-drift", "The team's default silently changes as each person picks a favourite, and costs and permissions diverge across surfaces.", "Write the default table into the repository's contributor docs and review it quarterly."),
  "cost governance is Module 10.6; rollout is Module 10.1.", "a default plus named exceptions beats case-by-case choice."),
 ],
 ret=[
 ("Which options in the away-from-terminal table run on your own machine?", "Dispatch, Remote Control and Channels (and local scheduled tasks)."),
 ("Which option runs in Anthropic's cloud and is triggered by a mention?", "Slack."),
 ("You close the lid after starting Remote Control and the work stops. Name the failure mode by its exact label.", "**Laptop-lid assumption.**"),
 ("You picked a surface because it was open and it could not reach your credentials. Name the failure mode.", "**Tool-first selection.**"),
 ("Your team's surface use diverged with no rule. Name the failure mode by its exact label.", "**Default-drift.**"),
 ("On which plans is Dispatch unavailable?", "Team and Enterprise (it requires Pro or Max)."),
 ("How many questions does this guide's decision tree ask?", "Four."),
 ("Which plans does Code Review need?", "Team and Enterprise."),
 ("What does a Desktop local scheduled task need to fire?", "The app open and the computer awake."),
 ("Is the decision tree published on the platforms page?", "No; it is this guide's synthesis, marked secondary."),
 ],
 steps=[("Copy the away-from-terminal table from memory", "Six-row table"), ("Write the four questions", "Decision list"), ("Collect five real tasks", "Task list"),
        ("Run each task through the tree", "Five picks"), ("Mark where the tree failed or needed an exception", "Exception notes"), ("Write the team default table", "Default table")],
 pass_md="""
| Task | Q1 | Q2 | Pick |
|---|---|---|---|
| Fix flaky test overnight | No local need | Must continue | Cloud session |
| Debug with prod data | Needs local | n/a | CLI |
| Triage Slack bug | No | Yes | Slack |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| 'Dispatch, because I will be offline' | **Laptop-lid assumption** |
| Picks by which app is open | **Tool-first selection** |
""",
 verdict="The artifact passes only if every pick cites which question decided it and any pick that leaves Claude on your machine states that the machine must stay on.",
 res=[("Anthropic", "Platforms and integrations", "Away-from-terminal comparison table", "Current"), ("Anthropic", "Claude Code on mobile", "Dispatch plan limits; machine must stay on", "Current")],
 dis="none found between the sources read; the decision tree is this guide's synthesis, not an official artifact.",
 reframe="This is the craft of the decision: **two questions, where does it run and who triggers it.** The engineer who understands this does not ask \"which surface is coolest?\" — they ask \"does this need my machine, and must it outlive my laptop?\""))

# ------------------------------------------------------------------ 7.1.3
SPECS.append(G(M, "7.1.3", "Moving between them",
 thesis="Sessions move between surfaces through a small set of commands, and each move has a direction, a requirement and something that does not come along.",
 prove="perform or describe each move (/desktop, --cloud, /teleport, /remote-control, --resume) and state what is copied and what is left behind.",
 disc="before moving a session, check the three preconditions: same account, branch pushed or clean, and the right direction.",
 counter="from the CLI, handoff is one-way: you can pull a cloud session into the terminal with --teleport, but you cannot push an existing terminal session to the cloud [Claude Code docs, Claude Code in the cloud, 2026].",
 read=22, prove_h="2.5",
 depth=["Name the commands and the direction each moves a session", "Predict what carries over and what is lost on each move", "Design a hand-off routine between laptop, cloud and phone"],
 deliverable="A movement matrix of from-surface by to-surface with the command, requirement and loss for each cell.",
 secs=[
 ("The command set",
  "Five commands do almost all moving. The commands reference describes each in one line [Claude Code docs, Commands, 2026].",
  """
| Command | What it does | Requires |
|---|---|---|
| `/desktop` (alias `/app`) | Continue the current session in the Desktop app | macOS or x64 Windows, claude.ai subscription |
| `/teleport` (alias `/tp`) | Pull a cloud session into this terminal | claude.ai subscription |
| `/remote-control` (alias `/rc`) | Make this session available from claude.ai | claude.ai subscription |
| `claude --cloud "task"` | Start a new cloud session for the current repository | claude.ai account, GitHub remote or bundle |
| `claude --resume` | Reopen a conversation from this machine's local history | Same machine |

`--remote` still works as a deprecated alias for `--cloud` [Claude Code docs, Claude Code in the cloud, 2026]. `/desktop` appears only on macOS and x64 Windows when signed in with a subscription [Claude Code docs, Commands, 2026].
""",
  ("Alias-blur", "You use `--remote` and `--remote-control` interchangeably, then wonder why one created a cloud session and the other exposed a local one.", "Remember that `--cloud` creates cloud sessions and `--remote-control` only lets you monitor and steer a local CLI session from claude.ai or the app."),
  "commands by moment are Module 14.1; Remote Control detail is Module 7.5.", "cloud makes a new remote session; remote-control exposes a local one."),
 ("Cloud to terminal: teleport",
  "`claude --teleport` opens a session picker, and `claude --teleport <session-id>` resumes one directly. Inside a CLI session, `/teleport` or `/tp` opens the same picker; `/tasks` then `t` also works [Claude Code docs, Claude Code in the cloud, 2026].",
  """
| Requirement | Detail |
|---|---|
| Clean git state | No uncommitted changes; teleport offers to stash |
| Correct repository | Same repository, not a fork |
| Branch available | The session's branch must be pushed |
| Same account | Same claude.ai account as the cloud session |

Teleport verifies the repository, fetches and checks out the branch, and loads the full history. The terminal gets its own copy: new work there stays local and does not appear in the cloud session. To keep steering from a phone, start `/remote-control` in the local session [Claude Code docs, Claude Code in the cloud, 2026].

`--teleport` is distinct from `--resume`: `--resume` reopens local history and does not list cloud sessions.
""",
  ("Fork-and-diverge", "You teleport a session, keep working locally, and expect the phone to show your new work, but the cloud copy and the local copy have diverged.", "After teleporting, start `/remote-control` if you need the phone to follow, or treat the cloud session as finished."),
  "cloud sessions are Module 7.4; git hygiene before moving is Module 2.5.", "teleport copies; it does not link."),
 ("Terminal to cloud, and the follow-up path",
  "To start cloud work from the terminal use `claude --cloud \"task\"`. The cloud VM clones your GitHub remote at your current branch, not your local checkout, so push first [Claude Code docs, Claude Code in the cloud, 2026].",
  """
```bash
git push                         # cloud clones the remote branch, not your working tree
claude --cloud "Fix the flaky test in auth.spec.ts"
claude -p "also update the changelog" --cloud session_01ABC...   # queue a follow-up
claude --teleport                # later: pull a finished session back
```

If the repository has no GitHub remote or the Claude GitHub App is not installed, Claude Code bundles and uploads your local repository instead; the bundle must be under 100 MB and uncommitted changes to credential-like files such as `.env` are left out on macOS, Linux and WSL [Claude Code docs, Claude Code in the cloud, 2026]. The Desktop app can send a local session to the cloud from its Open in menu, carried over as a summary [Claude Code docs, Desktop, 2026].
""",
  ("Unpushed-branch launch", "You run `--cloud` with local commits that were never pushed and the cloud session starts from an older commit, so it solves a problem you already fixed.", "Push first, and read the `Branch <name> is not on GitHub` notice if it prints."),
  "cloud environments are Module 4.5; session management is Module 2.4.", "push before you launch; teleport to come back."),
 ],
 ret=[
 ("Which command pulls a cloud session into your terminal, and what is its alias?", "`/teleport`, alias `/tp`."),
 ("Which flag starts a new cloud session, and what deprecated alias still works?", "`--cloud`; `--remote`."),
 ("After teleporting, you work locally and the phone shows nothing new. Name the failure mode by its exact label.", "**Fork-and-diverge.**"),
 ("You launched --cloud before pushing and the session lacks your fix. Name the failure mode by its exact label.", "**Unpushed-branch launch.**"),
 ("You confuse --remote-control with --cloud. Name the failure mode.", "**Alias-blur.**"),
 ("What is the size limit for a bundled repository upload?", "Under 100 MB."),
 ("List the four teleport requirements.", "Clean git state, correct repository, branch available, same account."),
 ("Can you push an existing terminal session to the cloud from the CLI?", "No; handoff is one-way via --teleport; Desktop can send a session via Open in."),
 ("Which platforms does `/desktop` appear on?", "macOS and x64 Windows."),
 ("What does `--resume` list that `--teleport` does not, and vice versa?", "--resume lists local history only; --teleport lists cloud sessions."),
 ],
 steps=[("Draw the from-to movement matrix", "Empty matrix"), ("Fill each cell with the command", "Command per cell"), ("Add requirement and loss per cell", "Filled matrix"),
        ("Perform a --cloud then --teleport round trip on a scratch repo", "Terminal log"), ("Record what the cloud copy and local copy each contain after", "Two lists"), ("Write your hand-off checklist", "Checklist")],
 pass_md="""
| From | To | Command | Loss |
|---|---|---|---|
| Terminal | Cloud | `claude --cloud` (new session) | Uncommitted work; local MCP |
| Cloud | Terminal | `/teleport` | Cloud copy stops following |
| Terminal | Phone | `/remote-control` | Machine must stay on |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Terminal to cloud lists 'teleport' | Teleport pulls cloud to terminal, not the reverse |
| No push step before --cloud | **Unpushed-branch launch** |
""",
 verdict="The artifact passes only if every cell states direction, command, requirement and loss, and a round trip was actually performed.",
 res=[("Anthropic", "Use Claude Code in the cloud", "--cloud, --teleport, requirements, bundling limit", "Current"), ("Anthropic", "Commands", "/desktop, /teleport, /remote-control one-liners", "Current"), ("Anthropic", "Remote Control", "Local session stays local; names and resume window", "Current")],
 dis="none found between the sources read.",
 reframe="This is the craft of moving sessions: **a direction, a command, a precondition, a loss.** The engineer who understands this does not ask \"can I move it?\" — they ask \"which way, what must be true first, and what stays behind?\""))

if __name__ == "__main__":
    run(SPECS)
