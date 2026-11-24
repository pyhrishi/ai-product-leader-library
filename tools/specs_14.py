import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen import write
from specs_12 import T

M = "b-1-4"
SPECS = []
NOPR = "Plan prices and window lengths change often; read claude.com/pricing and your Console for current figures."

# ---------------------------------------------------------------- 1.4.1
SPECS.append(dict(
 mod=M, id="1.4.1", title="Subscription usage: windows, pools and what counts", short="Subscription usage: windows, pools and what counts",
 thesis="On a subscription, usage is included but limited by rolling windows, and the context you carry is the main driver of how fast the window drains.",
 prove="read /usage before and after one heavy task and name what counted.",
 discipline="check /usage before heavy work, not after the stall.",
 counter="a subscription is not unlimited; the cost moved from a bill to a window.",
 read_min=18, prove_h="2", depth=["Read /usage and name the limit horizons", "Plan heavy work around windows", "Set team guidance for shared plan pools"],
 deliverable="A before-and-after /usage log for one heavy task with what counted named.",
 sections=[
 dict(title="Included, but windowed", framing="On a subscription, Claude Code usage is included in the plan and limited by rolling windows rather than billed per token [Claude Code docs, Costs, 2026]. Anthropic's help material describes a five-hour session limit and a weekly limit [Claude Help Center, 2026]. " + NOPR,
  body=T("""
| Item | Detail |
|---|---|
| Included | Claude Code on Pro, Max, Team and Enterprise plans |
| Horizons | A session window of about five hours, and a weekly limit |
| Higher tiers | Max in 5x and 20x variants |
| Shared pool | Claude Code and the Claude apps draw on the same plan limits [confirm on your plan page] |
| Subagents | Count toward the same limits as the main conversation [Claude Code docs, Subagents, 2026] |
"""),
  fm=[("Limit-surprise", "You start a large multi-agent task near the end of a window or late in the week, and the run stalls half done.", "Check `/usage` before heavy work, split into resumable chunks with checkpoint commits, and start big runs after a reset.")],
  xr="subagents are Module 1.2.5; session management is Module 2.4.", one="a subscription trades a bill for a window."),
 dict(title="/usage is the instrument", framing="For Pro and Max the session cost figure is not relevant to billing; `/usage` instead shows plan usage bars, activity stats and a breakdown of what counts against your limits [Claude Code docs, Costs, 2026]. The authoritative billing view for API users is the Usage page in the Console.",
  body=T("""
```text
/usage     # plan bars, activity, breakdown of what is counting
/context   # why: where this session's tokens are going now
```

| You see | It means |
|---|---|
| Bars near full | The window is close to its limit |
| Large subagent share | Fan-out is the driver |
| Large context | Re-reads of a big history are the driver |
"""),
  fm=[("Blind-burn session", "A long-lived session accumulates context and background agents, every turn re-reads it, and the bar drains faster than the work justifies.", "`/clear` between tasks, `/compact` with a focus before long new tasks, and read `/usage` hourly during heavy work.")],
  xr="context is Module 3.1; compaction is Module 1.2.4.", one="`/usage` says what, `/context` says why."),
 dict(title="What drives consumption", framing="Anything that makes the model read or write more tokens drains the window: long sessions, many parallel subagents, high effort, large file reads and verbose tool output. The window you hit is a symptom; the context is the cause.",
  body=T("""
| Driver | Control |
|---|---|
| Long history | `/clear`, `/compact focus on ...` |
| Fan-out | Delegate only large read-heavy work |
| High effort | Lower it for mechanical steps |
| Big reads | Scope paths and patterns |
| Noisy output | Pipe to a file, read the tail |
"""),
  fm=[("Driver-blindness", "You blame the plan for the limit and never look at which driver used the window.", "Read `/usage` and `/context` and name the dominant driver before changing anything.")],
  xr="cost habits are Module 1.4.5; effort is Module 1.4.3.", one="name the driver, then change one thing."),
 dict(title="When you hit the wall", framing="Anthropic's help material lists the options: upgrade (Pro to Max 5x, Max 5x to Max 20x), enable usage credits to continue past the limit, switch to a Console account with API credits, or wait for the reset. The Max plan's monthly API credits cannot be used in Claude Code or the Claude apps [Claude Help Center, 2026].",
  body=T("""
| Option | Trade-off |
|---|---|
| Wait for reset | Free, costs time |
| Upgrade tier | Higher fixed cost, more capacity |
| Usage credits | Pay-as-you-go overflow; needs a monthly cap |
| Console account | Per-token billing and workspace limits |
"""),
  fm=[("Panic-upgrade", "You upgrade a tier at the first limit hit without checking whether one habit explains the drain.", "Measure first; upgrade only when a clean, scoped workflow still hits the wall.")],
  xr="API billing is Module 1.4.2.", one="fix the habit before you buy the tier."),
 ],
 retrieval=[
  ("Name the two limit horizons for subscriptions.", "A five-hour session window and a weekly limit."),
  ("A run stalls halfway at the end of a window. Name the failure mode by its exact label.", "**Limit-surprise.**"),
  ("What does /usage show for Pro and Max users?", "Plan usage bars, activity stats and a breakdown of what counts."),
  ("A long session drains the bar faster than the work justifies. Name the failure mode.", "**Blind-burn session.**"),
  ("Do subagent requests count toward your limits?", "Yes, the same limits as the main conversation."),
  ("You blame the plan without checking drivers. Name the failure mode.", "**Driver-blindness.**"),
  ("You upgrade the tier at the first limit hit. Name the failure mode and the fix.", "**Panic-upgrade.** Measure first."),
  ("Can Max monthly API credits be used in Claude Code?", "No."),
  ("Which command shows why tokens are being spent now?", "`/context`."),
 ],
 steps=[("Record `/usage` and `/context` before", "Numbers A"), ("Run one heavy task", "Task"), ("Record both again", "Numbers B"),
        ("Name the dominant driver", "One sentence"), ("Re-run scoped in a fresh session and compare", "Numbers C"), ("Write your pre-flight check for heavy work", "`checklist.md`")],
 pass_md=T("""
| Metric | Cluttered | Scoped fresh |
|---|---|---|
| Context at end | High | Low |
| Plan bar change | Larger | Smaller |
| Dominant driver | History | None |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Claims a saving without numbers | No `/usage` evidence |
"""),
 verdict="The artifact passes only if both runs have `/usage` and `/context` numbers and the driver is named.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Manage costs effectively | Subscription versus API usage, `/usage` | Current |
| Claude Help Center | Usage limit articles | Horizons, options at the limit | Current |
""") + "\n\n*Disagreement named:* one third-party page says limits reset every five hours while Anthropic describes a five-hour session window plus a weekly limit. **Anthropic's wording wins.**",
 reframe="This is the craft of subscription usage: **see the window, name the driver, change one thing.** The engineer who understands this does not ask \"why did I hit the limit?\" — they ask \"what was counting, and which driver was it?\"",
))

# ---------------------------------------------------------------- 1.4.2
SPECS.append(dict(
 mod=M, id="1.4.2", title="API and provider billing: ceilings before keys", short="API and provider billing: ceilings before keys",
 thesis="Per-token billing is controlled by ceilings you set before the first run: workspace limits, provider budgets and credit caps.",
 prove="create a workspace limit or credit cap and show where it appears.",
 discipline="every billing path needs a ceiling set before the first run, not after the first surprise.",
 counter="the cheapest-looking key is the riskiest: with no ceiling, a loop or a CI job turns a bug into an invoice.",
 read_min=18, prove_h="2", depth=["Name the three billing structures and their guardrails", "Set ceilings per path", "Estimate team spend from a pilot"],
 deliverable="A billing-path table with the ceiling you set on each path and where to see it.",
 sections=[
 dict(title="Three structures", framing="Claude Code charges by API token consumption on API or provider billing; subscription pricing is separate [Claude Code docs, Costs, 2026]. " + NOPR,
  body=T("""
| Path | You pay | Guardrails |
|---|---|---|
| Claude Console (API) | Per token | Workspaces with spend limits; Console reports |
| Cloud provider (Bedrock, Google Cloud, Foundry) | Per token on your cloud bill | Provider quotas, budgets, alerts |
| Subscription plus usage credits | Plan, then pay-as-you-go overflow | A monthly credit limit you set |

[Claude Code docs, Costs, 2026]
"""),
  fm=[("Uncapped key", "An API key with no workspace spend limit runs in a loop or CI job and the first signal is the invoice.", "Create a workspace per use case, set a spend limit before issuing the key, and alert on the Usage page.")],
  xr="sign-in paths are Module 1.3.2; enterprise governance is Part 11.", one="ceiling first, key second."),
 dict(title="Workspace limits and reports", framing="For API organisations, spend is managed through workspaces with limits on total Claude Code spend, and admins can view cost and usage reports in the Console [Claude Code docs, Costs, 2026].",
  body=T("""
| Control | Where |
|---|---|
| Workspace spend limit | Console |
| Cost and usage reports | Console |
| Per-key attribution | One key per use case |
| Alerts | Console Usage page or provider budgets |
"""),
  fm=[("Shared-workspace blur", "All projects share one workspace and key, so you cannot tell which one spent what or cap one without capping all.", "One workspace and key per use case.")],
  xr="team spend is in Part 11.", one="one use case, one workspace."),
 dict(title="Usage credits on a subscription", framing="Credits let you continue after plan limits by switching to pay-as-you-go. Set a monthly limit with `/usage-credits`; if you hit it with credits remaining, Claude Code prompts you to raise or remove it, and changing the limit needs billing access [Claude Code docs, Costs, 2026].",
  body=T("""
```text
/usage-credits    # set or review the monthly credit limit
```

A third-party mirror lists `/extra-usage` and `/cost`; command names shift across versions, so run `/help` in your install and confirm on the Costs page.
"""),
  fm=[("Credits-on-autopilot", "You enable usage credits to get past a limit and forget, so every later limit hit becomes spend.", "Set a monthly cap the day you enable credits and review month-to-date spend.")],
  xr="fast mode billing is Module 1.4.3.", one="enable credits and cap them in the same minute."),
 dict(title="Estimating spend", framing="Cost per task is roughly input plus output tokens times the per-token price, with context re-reads dominating long sessions. The docs advise starting with a small pilot group and using tracking tools to build a baseline before wider rollout [Claude Code docs, Costs, 2026].",
  body=T("""
| Step | Output |
|---|---|
| Pilot 3 to 5 users for two weeks | Per-user spend range |
| Break out by task type | Spend per feature, per fix |
| Multiply for rollout, add headroom | Forecast |
| Set workspace limit above forecast | Ceiling |
"""),
  fm=[("Guess-budget", "You set a team budget from intuition and either starve the team or blow through it.", "Run a pilot, measure, then set the ceiling above the measured range.")],
  xr="rollout is in Part 11.", one="measure a pilot, then forecast."),
 ],
 retrieval=[
  ("Name the three billing structures.", "Console API, cloud provider, subscription plus usage credits."),
  ("An API key with no limit runs in a CI loop. Name the failure mode by its exact label.", "**Uncapped key.**"),
  ("Which command sets a monthly usage-credit limit?", "`/usage-credits`."),
  ("You enabled credits and forgot. Name the failure mode.", "**Credits-on-autopilot.**"),
  ("All projects share one key. Name the failure mode.", "**Shared-workspace blur.**"),
  ("How does the docs advise estimating team spend?", "Pilot a small group and use tracking tools to build a baseline."),
  ("You set a team budget from intuition. Name the failure mode.", "**Guess-budget.**"),
  ("Who can change the usage-credit limit?", "Someone with billing access on the account."),
 ],
 steps=[("List the billing paths you use", "Table"), ("Set or locate a ceiling on each", "Screens or settings"), ("Create a workspace per use case if on API", "Workspaces"),
        ("Set a credit cap if you use credits", "Cap"), ("Run a one-week pilot measurement", "Numbers"), ("Write a forecast with headroom", "`forecast.md`")],
 pass_md=T("""
| Path | Ceiling | Where seen |
|---|---|---|
| Console | Workspace limit | Usage page |
| Credits | Monthly cap | `/usage-credits` |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Key issued, limit 'to do' | **Uncapped key** |
"""),
 verdict="The artifact passes only if every path has a ceiling set and a place to see it.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Manage costs effectively | Billing structures, workspaces, credits | Current |
| Claude Help Center | Usage credits articles | Overflow behaviour | Current |
""") + "\n\n*Disagreement named:* a mirror lists `/extra-usage` and `/cost`, the docs list `/usage-credits`. **Check `/help` on your version.**",
 reframe="This is the craft of billing paths: **ceiling before key, cap before credit, pilot before forecast.** The engineer who understands this does not ask \"what will this cost?\" — they ask \"what is the most this can cost, and who is alerted?\"",
))

# ---------------------------------------------------------------- 1.4.3
SPECS.append(dict(
 mod=M, id="1.4.3", title="Fast mode and effort: buying speed and depth", short="Fast mode and effort: buying speed and depth",
 thesis="Speed and depth are purchasable meters; open them on purpose and close them after.",
 prove="run one mechanical task at two effort levels and show no quality difference with a usage difference.",
 discipline="set a moderate default and raise it deliberately.",
 counter="more thinking is not always better thinking; on mechanical work it is pure cost.",
 read_min=15, prove_h="2", depth=["Name the levers and their effect", "Pick settings per step", "Set team defaults"],
 deliverable="A lever table with measured usage for two settings on one task.",
 sections=[
 dict(title="The levers", framing="Effort controls adaptive reasoning: higher effort means more thinking tokens and deeper reasoning, lower is faster and cheaper; it is supported on Fable models, Opus 4.6 and later, and Sonnet 4.6 and later [Claude Code docs, Glossary, 2026].",
  body=T("""
| Lever | Speed | Cost | Use for |
|---|---|---|---|
| Lower effort | Faster | Cheaper | Renames, formatting |
| Default effort | Balanced | Balanced | Most feature work |
| Higher effort | Slower | More thinking tokens | Architecture, hard bugs, security review |
| Fast mode | Faster output | Usage credits on individual plans | Interactive latency pain |
| Smaller model | Faster | Cheaper | Search subagents |

The exact fast-mode multiplier is not reliably established here; check the Costs page.
"""),
  fm=[("Effort-as-default", "You leave effort at maximum for everything and the plan bar empties on routine edits.", "Set a moderate default, raise it for hard steps, lower it for batch mechanical work.")],
  xr="models, effort and speed are Module 4.6; model layer is Module 1.2.8.", one="effort is a meter, not a mood."),
 dict(title="Fast mode", framing="Fast mode is billed through usage credits on individual plans, so it shows up in your credit total rather than the plan bar [Claude Code docs, Costs, 2026].",
  body=T("""
| Habit | Why |
|---|---|
| Turn on per task | Latency matters now |
| Turn off after | Credits keep draining otherwise |
| Check month-to-date credit spend weekly | Catch drift |
"""),
  fm=[("Fast-mode forgetting", "You enable fast mode for an afternoon and discover the credit spend a month later.", "Treat fast mode as a per-task switch and review credit spend weekly.")],
  xr="credits are Module 1.4.2.", one="open it, use it, close it."),
 dict(title="Thinking tokens count", framing="Thinking tokens count against limits. A session on maximum effort pays for deep reasoning on steps that did not need it, and on a subscription that spends your window. Extended thinking can be capped on models with a fixed budget through `MAX_THINKING_TOKENS` [Claude Code docs, Glossary, 2026].",
  body=T("""
| Symptom | Likely cause |
|---|---|
| Plan bar drains on small edits | High effort default |
| Slow answers on trivial tasks | High effort default |
| Shallow answers on hard tasks | Effort too low |
"""),
  fm=[("Shallow-default regret", "You drop effort to save usage and then accept a shallow answer on a genuinely hard step.", "Raise effort for planning and review steps and keep it low for mechanical ones.")],
  xr="planning is Module 2.1.", one="cut thinking where it adds nothing; keep it where it earns."),
 dict(title="Per-step settings", framing="A pragmatic pattern is a stronger model and higher effort for planning and review, default for implementation, and a small model for search subagents.",
  body=T("""
| Step | Setting |
|---|---|
| Plan | Strong, high |
| Implement | Default |
| Search subagent | Small |
| Review | Strong, high |

[Judgement-based pattern; measure with `/usage`.]
"""),
  fm=[("Single-setting habit", "One model and effort for the whole task overspends on easy steps or underpowers hard ones.", "Switch per step with `/model` and set subagent models in frontmatter.")],
  xr="subagents are Module 1.2.5.", one="settings follow the step."),
 ],
 retrieval=[
  ("Which models support effort?", "Fable models, Opus 4.6 and later, Sonnet 4.6 and later."),
  ("Maximum effort for routine edits. Name the failure mode by its exact label.", "**Effort-as-default.**"),
  ("Where does fast mode spend show up on individual plans?", "In usage credits."),
  ("You forgot fast mode. Name the failure mode.", "**Fast-mode forgetting.**"),
  ("You cut effort and accepted a shallow plan. Name the failure mode.", "**Shallow-default regret.**"),
  ("Which variable caps thinking tokens on fixed-budget models?", "`MAX_THINKING_TOKENS`."),
  ("One setting for the whole task. Name the failure mode.", "**Single-setting habit.**"),
  ("Do thinking tokens count against limits?", "Yes."),
 ],
 steps=[("Pick a mechanical task", "Task"), ("Run at low and high effort; record `/usage` deltas", "Two numbers"), ("Rate results blind", "Ratings"),
        ("Pick a hard task and repeat", "Two numbers"), ("Write your default and escalation rule", "`rule.md`")],
 pass_md=T("""
| Task | Effort | Quality | Usage |
|---|---|---|---|
| Mechanical | Low | Same | Lower |
| Mechanical | High | Same | Higher |
| Hard | Low | Missed case | Lower |
| Hard | High | Caught case | Higher |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Quality judged knowing the setting | Biased |
"""),
 verdict="The artifact passes only if quality ratings were blind and usage numbers come from `/usage`.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Glossary: Effort level, Extended thinking | Definitions and support | Current |
| Anthropic | Manage costs effectively | Fast mode billing | Current |
""") + "\n\n*Disagreement named:* none found.",
 reframe="This is the craft of speed and depth: **open the meter on purpose and close it after.** The engineer who understands this does not ask \"what is the best setting?\" — they ask \"what does this step earn?\"",
))

# ---------------------------------------------------------------- 1.4.4
SPECS.append(dict(
 mod=M, id="1.4.4", title="Feature availability by plan, provider and version", short="Feature availability by plan, provider and version",
 thesis="A documented feature is not an entitled feature until you have checked plan, provider and version.",
 prove="pick five features your runbook uses and record plan, provider and minimum version for each.",
 discipline="put the three-way check in the runbook.",
 counter="the docs describe the product, not your account; the same page can be right and not apply to you.",
 read_min=15, prove_h="2", depth=["Check one feature on three axes", "Audit a runbook", "Maintain an availability matrix for a team"],
 deliverable="A five-feature availability matrix with plan, provider and version for each.",
 sections=[
 dict(title="Three axes", framing="Some features, for example auto mode, cloud sessions and Code Review, differ by plan or backend; the docs maintain a feature-availability page for this [syllabus Module 1.4.4]. That page was not fetched in full for this guide; read it before standardising a workflow.",
  body=T("""
| Axis | Question |
|---|---|
| Plan | Pro, Max, Team or Enterprise? |
| Provider | Anthropic, Bedrock, Vertex, Foundry? |
| Version | Does `claude --version` meet the minimum? |
"""),
  fm=[("Doc-as-entitlement", "You read a feature in the docs, build a workflow on it, and a teammate on another plan or provider cannot run it.", "Check plan, provider and version for each team member and put the check in the runbook.")],
  xr="surfaces are Module 7.1; versions are Module 1.3.5.", one="three axes, every feature."),
 dict(title="Examples from the docs", framing="Examples show how much varies.",
  body=T("""
| Example | What the docs say |
|---|---|
| Auto mode | Built-in starting mode on Pro, Max and Team for interactive terminal and VS Code; from v2.1.283 more broadly |
| Computer use, Dispatch | Desktop, on Pro and Max |
| Third-party providers | CLI and IDE extensions support them |
| Artifact sharing | Public link on Pro and Max; organisation sharing on Team and Enterprise |
| Agent teams | Experimental, off by default |

[Claude Code docs, 2026; verify each row on its own page]
"""),
  fm=[("Default-mode mismatch", "Your session starts in a different permission mode than a colleague's and you debug a difference that is only the starting mode.", "Compare `/permissions` and starting mode before debugging behaviour.")],
  xr="permission modes are Module 4.3.", one="starting state differs by plan and version."),
 dict(title="The working method", framing="Before writing a team runbook, list the features it uses, then check plan, provider and version for each and record `claude --version`.",
  body=T("""
| Feature | Plan | Provider | Min version | Verified by |
|---|---|---|---|---|
| (fill in) | | | | |
"""),
  fm=[("Matrix-drift", "The availability matrix is written once and never updated, so it slowly becomes wrong.", "Date each row and review after each release with `/release-notes`.")],
  xr="release notes are Module 1.3.5.", one="a dated matrix beats a remembered one."),
 dict(title="Provider-route limits", framing="Third-party provider users are limited to the CLI and IDE extensions in several docs examples, so surfaces such as the desktop app or web may not be available on that route [Claude Code docs, Overview, 2026].",
  body=T("""
| Route | Surfaces |
|---|---|
| Anthropic subscription or Console | All surfaces per plan |
| Bedrock, Vertex, Foundry | Terminal CLI, VS Code, JetBrains |
"""),
  fm=[("Provider-blind plan", "You plan a desktop or web workflow for a team that runs Bedrock and discover the surface is not offered.", "List surfaces per provider before choosing a workflow.")],
  xr="surfaces are Module 7.1; providers are in Part 11.", one="the provider constrains the surface."),
 ],
 retrieval=[
  ("Name the three axes of availability.", "Plan, provider and version."),
  ("A teammate cannot run a feature you can. Name the failure mode by its exact label.", "**Doc-as-entitlement.**"),
  ("Sessions start in different modes. Name the failure mode.", "**Default-mode mismatch.**"),
  ("A matrix written once and never updated. Name the failure mode.", "**Matrix-drift.**"),
  ("You plan a desktop workflow for Bedrock users. Name the failure mode.", "**Provider-blind plan.**"),
  ("Which surfaces do third-party provider users get?", "Terminal CLI, VS Code and JetBrains."),
  ("Is agent teams enabled by default?", "No; it is experimental and off by default."),
  ("What do you record in the runbook for each feature?", "Plan, provider, minimum version and how you verified it."),
 ],
 steps=[("List five features your workflow uses", "List"), ("Look up each in the docs", "Notes"), ("Record plan, provider, minimum version", "Matrix"),
        ("Verify two by trying them", "Two results"), ("Date the matrix and set a review reminder", "Matrix")],
 pass_md=T("""
| Feature | Plan | Provider | Min version | Verified |
|---|---|---|---|---|
| Hooks onFailure block | All | All | 2.1.295 | Yes |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| No version column | **Doc-as-entitlement** risk |
"""),
 verdict="The artifact passes only if at least two rows were verified by trying the feature.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Feature availability page | Plan and provider differences | Current; not fetched in full |
| Anthropic | Overview | Provider route surfaces | Current |
""") + "\n\n*Disagreement named:* none found.",
 reframe="This is the craft of availability: **plan, provider, version, verified, dated.** The engineer who understands this does not ask \"does the docs page say it exists?\" — they ask \"does it exist for everyone on this team?\"",
))

# ---------------------------------------------------------------- 1.4.5
SPECS.append(dict(
 mod=M, id="1.4.5", title="Cost control habits: five habits and one rule", short="Cost control habits: five habits and one rule",
 thesis="All five cost habits do one thing: carry fewer tokens per turn and waste fewer turns, and the one rule is to measure before and after.",
 prove="change exactly one habit, measure with /usage and /context, and log the effect.",
 discipline="one task per session, scoped searches, and a measurement before and after.",
 counter="applying every tip at once teaches you nothing; the log of one change at a time is the real asset.",
 read_min=18, prove_h="2", depth=["Apply the five habits", "Rank habits by measured effect", "Embed habits in a team runbook"],
 deliverable="A two-line-per-change log showing which habit moved the numbers.",
 sections=[
 dict(title="The five habits", framing="The syllabus lists five habits and the mechanism behind them is shared: fewer tokens per turn and fewer wasted turns [syllabus Module 1.4.5; Claude Code docs, Best practices, Context window and Costs, 2026].",
  body=T("""
| Habit | Why it works | Practice |
|---|---|---|
| Clear between tasks | Stops re-reading irrelevant history | `/clear` |
| Scope searches | Limits what lands in context | "Search `src/payments/` for X" |
| Subagents for exploration | Keeps big reads out of the main window | Accept the summary |
| Right model for the step | No depth bought for mechanical work | `/model`, subagent `model:` |
| Watch `/context` | Makes bloat visible early | Check at task boundaries |
"""),
  fm=[("Kitchen-sink session", "One session carries a feature, a bug fix and a docs edit, so every turn re-reads all three.", "One task per session, `/clear` between tasks, `/compact` with a focus when a long task must continue.")],
  xr="context is Module 3.1; subagents are Module 1.2.5.", one="one task, one session."),
 dict(title="Scoping and delegation", framing="Open-ended exploration fills the window. Name a directory, a symptom and a stopping condition, or delegate to a subagent and keep only the summary.",
  body=T("""
```text
Weak:  "Investigate why this is slow."
Strong: "In src/checkout/, find why submitOrder takes >2s. Profile with
         `npm run bench`. Stop after naming the top two causes."
```
"""),
  fm=[("Unscoped exploration", "'Investigate why this is slow' with no boundary makes Claude read dozens of files and fill the window.", "Name the directory, symptom and stopping condition, or delegate to a subagent.")],
  xr="prompting is Module 2.2; large codebases are Module 3.5.", one="a boundary and a stop condition."),
 dict(title="Compaction and tool output", framing="`/compact focus on the auth bug fix` yields a summary biased to what you still need [Claude Code docs, Context window, 2026]. MCP tool schemas are deferred, so idle servers cost little. Preprocessing hooks can trim noisy tool output before it reaches the model. After more than two failed corrections, `/clear` and rewrite the prompt [Claude Code docs, Best practices, 2026].",
  body=T("""
| Lever | Effect |
|---|---|
| `/compact focus on ...` | Keeps what you still need |
| Pipe noisy output to a file | Keeps the window small |
| Trimming hook | Removes noise before the model reads it |
| `/clear` after two failed corrections | Drops failed attempts |
"""),
  fm=[("Output flood", "A test run or log dump fills context and degrades later answers.", "Pipe to a file and read the tail, or trim with a hook.")],
  xr="hooks are Module 1.2.6; context hygiene is Module 1.2.4.", one="trim what the model must read."),
 dict(title="Measure one change at a time", framing="A rough ranking by judgement, not measured data: clearing between tasks and scoping searches usually matter most; model choice matters most on subagent-heavy work; effort matters most on reasoning-heavy work.",
  body=T("""
| Change | Before | After | Verdict |
|---|---|---|---|
| (one change) | `/usage`, `/context` | `/usage`, `/context` | Kept or dropped |
"""),
  fm=[("Optimising blind", "You apply every tip at once and cannot say which helped.", "Read `/usage` and `/context` before and after one change at a time and keep a two-line log.")],
  xr="usage reading is Module 1.4.1.", one="one change, two readings, one line."),
 ],
 retrieval=[
  ("List the five cost habits.", "Clear between tasks; scope searches; subagents for exploration; right model for the step; watch `/context`."),
  ("One session holds a feature, a fix and a docs edit. Name the failure mode by its exact label.", "**Kitchen-sink session.**"),
  ("'Investigate why this is slow.' Name the failure mode and fix.", "**Unscoped exploration.** Name directory, symptom and stop condition."),
  ("You applied six tips at once. Name the failure mode.", "**Optimising blind.**"),
  ("A test dump fills context. Name the failure mode.", "**Output flood.**"),
  ("After how many failed corrections do you `/clear`?", "More than two."),
  ("What does `/compact focus on X` do?", "Biases the summary toward X."),
  ("Do idle MCP servers cost much?", "Little; schemas are deferred."),
 ],
 steps=[("Pick a repeatable task", "Task"), ("Run it in a cluttered session; record numbers", "Numbers A"), ("Reset the repo", "Clean tree"),
        ("Run it fresh with a scoped prompt; record numbers", "Numbers B"), ("Name the habit responsible", "Two sentences"), ("Write a runbook line", "One line")],
 pass_md=T("""
| Metric | A (cluttered) | B (fresh, scoped) |
|---|---|---|
| Files read | 14 | 4 |
| Correction rounds | 3 | 0 |
| Failure modes | Kitchen-sink session, Unscoped exploration | None |

Numbers illustrative; yours will differ.
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Six habits changed together | **Optimising blind** |
"""),
 verdict="The artifact passes only if the two runs started from the same repo state and the numbers come from `/usage` and `/context`.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Best practices | Clear and compact guidance | Current |
| Anthropic | Explore the context window | Per-read costs | Current |
| Anthropic | Manage costs effectively | Tracking tools | Current |
""") + "\n\n*Disagreement named:* none found.",
 reframe="This is the craft of cost control: **fewer tokens per turn, fewer wasted turns, measured one change at a time.** The engineer who understands this does not ask \"which tip is best?\" — they ask \"what did this one change move?\"",
))

if __name__ == "__main__":
    for s in SPECS:
        write(s)
