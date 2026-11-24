import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from wk_b1011 import make, run, T, D

M = "b-10-1"
SPECS = []
AS = "Claude Code docs, Set up Claude Code for your organization, 2026"
CO = "Claude Code docs, Manage costs effectively, 2026"
TP = "Claude Code docs, Enterprise deployment overview, 2026"

# ------------------------------------------------------------------ 10.1.1
SPECS.append(make(M, "10.1.1", "The decision map",
 "A Claude Code rollout is five decisions taken in a fixed order, and each later decision is constrained by the earlier ones.",
 "list the five decisions in order and, for your own organisation, write the one-line answer to each.",
 "decide the provider and the delivery mechanism before you write a single policy key.",
 "the provider you pick changes which Claude Code features your developers can use at all, so the provider decision is a product decision, not an infrastructure detail [%s]." % AS,
 [("Five decisions, one order",
   "The admin-setup page is explicitly a decision map that walks deployment decisions in order. Each row names what you are choosing and links to the reference page for that area [%s]." % AS,
   """
| # | Decision | What you are choosing | Where the answer lives |
|---|---|---|---|
| 1 | Choose your API provider | Where Claude Code authenticates and how it is billed | Authentication, Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry |
| 2 | Decide how settings reach devices | How managed policy reaches developer machines | Server-managed settings, delivery mechanisms |
| 3 | Decide what to enforce | Which tools, commands and integrations are allowed | Permissions, Sandboxing |
| 4 | Set up usage visibility | How you track spend and adoption | Analytics, Monitoring, Costs |
| 5 | Review data handling | Retention and compliance posture | Data usage, Security |
""",
   ("Policy-first drafting", "You draft a long list of permission rules before you know which provider and delivery channel you will use, then discover the channel cannot carry some of the keys.", "Do decisions 1 and 2 first; only then write the keys for decision 3."),
   "the module that holds each decision is Module 10.2 for the provider, Module 10.4 for delivery and policy, Module 10.6 for cost and Module 10.7 for data.",
   "decision order matters because the early answers limit the later ones."),
  ("Provider choice gates features",
   "The recommended default is Claude for Teams or Enterprise: one per-seat subscription for Claude Code and claude.ai with no infrastructure to run. Console suits API-first or pay-as-you-go; Bedrock, Google Cloud's Agent Platform and Foundry suit organisations that want to inherit existing cloud compliance controls and billing [%s]. Some features need a claude.ai account: cloud sessions, Routines, Code Review, Remote Control and the Chrome extension are not available through Console API keys or cloud-provider credentials alone [%s]." % (AS, AS),
   """
| Provider | Choose this when |
|---|---|
| Claude for Teams / Enterprise | You want one per-seat subscription and no infrastructure (the default recommendation) |
| Claude Console | You are API-first or want pay-as-you-go billing |
| Amazon Bedrock | You want to inherit existing AWS compliance controls and billing |
| Google Cloud's Agent Platform | You want to inherit existing GCP compliance controls and billing |
| Microsoft Foundry | You want to inherit existing Azure compliance controls and billing |
""",
   ("Seatless cloud rollout", "You deploy through a cloud provider and promise developers cloud sessions or Code Review, but nobody holds a claude.ai seat, so the features are simply absent.", "Before rollout, list the claude.ai-only features you promised and decide who also needs a Teams or Enterprise seat."),
   "the full backend comparison is Module 10.2; plan limits are Module 1.4.",
   "pick the provider by the features you need, not only by the bill you want."),
  ("Four sources, one winner",
   "Managed settings define organisation policy and take precedence over local developer configuration. Claude Code checks four sources in priority order: server-managed first, then plist or registry policy, then file-based managed settings, then the Windows user registry [%s]. By default the first source that delivers a policy key wins and the rest are ignored rather than merged [Claude Code docs, Deploy managed settings, 2026]." % AS,
   """
| Priority | Mechanism | Delivery |
|---|---|---|
| Highest | Server-managed | claude.ai admin console, or a self-hosted Claude apps gateway |
| High | plist / registry policy | macOS `com.anthropic.claudecode`; Windows `HKLM\\SOFTWARE\\Policies\\ClaudeCode` |
| Medium | File-based managed | `/Library/Application Support/ClaudeCode/managed-settings.json`, `/etc/claude-code/managed-settings.json`, `C:\\Program Files\\ClaudeCode\\managed-settings.json` |
| Lowest | Windows user registry | `HKCU\\SOFTWARE\\Policies\\ClaudeCode`, writable without elevation, so a convenience default, not enforcement |

Server-managed settings are fetched at startup and refreshed hourly during the session; delivery through the admin console needs a Teams or Enterprise plan [%s].
""" % AS,
   ("Mixed-provider gap", "Part of the fleet uses Bedrock or Vertex, you configure only server-managed settings, and those developers silently receive no policy.", "Deliver server-managed settings for claude.ai users plus a file-based or plist/registry fallback for everyone else."),
   "delivery detail is Module 10.4; the gateway option is Module 10.5.",
   "the highest source with a policy key wins, so one stray source can hide the rest."),
  ("Verify, then onboard",
   "After configuring managed settings, have a developer run `/status`. On the Status tab the `Setting sources` line shows `Enterprise managed settings` followed by the winning source in parentheses [%s]. For login problems the page lists three common fixes: `/logout` then `/login` to switch accounts, `claude update` if the enterprise auth option is missing, and a terminal restart after updating. A seat without Claude Code access produces the message 'You haven't been added to your organization yet' [%s]." % (AS, AS),
   """
```text
/status  ->  Setting sources: Enterprise managed settings (file)
                 label tells you which of the four sources won
```
""",
   ("Unverified go-live", "You announce the rollout after editing the console, and nobody checks a real machine, so a typo in the policy file means no policy at all.", "Run `/status` on one machine per OS and provider before announcing."),
   "the verification procedure is Module 10.4; first-run login is Module 1.3.",
   "a rollout is not done until `/status` on a real machine names the source you intended."),
 ],
 [("Name the five rollout decisions in order.", "Provider, how settings reach devices, what to enforce, usage visibility, data handling."),
  ("How many managed-settings sources does Claude Code check, and which is highest priority?", "Four; server-managed is highest."),
  ("Developers on Bedrock get no policy because only the console was configured. Name the failure mode by its exact label.", "**Mixed-provider gap.**"),
  ("You promised cloud sessions on a Bedrock rollout but nobody has a claude.ai seat. Name the failure mode.", "**Seatless cloud rollout.**"),
  ("How often are server-managed settings refreshed during a session?", "Hourly (and fetched at startup)."),
  ("Which Windows source is writable without elevation, and what should you treat it as?", "The `HKCU` user registry; a convenience default, not an enforcement channel."),
  ("Name three features that need a claude.ai account and so are unavailable on API keys or cloud credentials alone.", "Any three of: cloud sessions, Routines, Code Review, Remote Control, the Chrome extension."),
  ("You wrote 60 permission rules before choosing a delivery channel. Name the failure mode.", "**Policy-first drafting.**"),
  ("What does `/status` show when managed settings are in force?", "A `Setting sources` line reading `Enterprise managed settings` plus the winning source in parentheses."),
  ("Which plans can use admin-console server-managed settings?", "Claude for Teams or Enterprise."),
 ],
 [("List the five decisions with your answer to each", "`decisions.md`"), ("Mark which of your promised features need a claude.ai seat", "Feature table"),
  ("Pick a delivery mechanism per OS and per provider", "Delivery matrix"), ("Write the intended `Setting sources` value for each cell", "Expected labels"),
  ("Run `/status` on one real machine and paste the line", "Evidence"), ("Note any mismatch and its cause", "Gap list")],
 ("A one-page decision record with a verified `/status` line.", """
| Decision | Answer | Evidence |
|---|---|---|
| Provider | Teams/Enterprise for most devs; Bedrock for the data-residency group | Seat list |
| Delivery | Server-managed + `/etc/claude-code` fallback | `/status` shows `(remote)` and `(file)` |
| Promised features | Cloud sessions, Code Review: need seats | Seat count matches |
"""),
 """
| Element | What is wrong |
|---|---|
| Delivery column says 'console' for every group | **Mixed-provider gap** |
| No `/status` evidence | Unverified go-live |
""",
 "The record passes only if every promised feature maps to a seat or provider that supports it and one real machine shows the expected source label.",
 [("Anthropic", "Set up Claude Code for your organization", "The five-decision map, provider table, four sources", "Current"),
  ("Anthropic", "Enterprise deployment overview", "Provider comparison and best practices", "Current"),
  ("Anthropic", "Deploy managed settings", "How managed sources combine", "Current")],
 "none found between the sources read.",
 "This is the craft of the rollout: **five decisions, taken in order, verified on a real machine.** The administrator who understands this does not ask \"which settings should I write?\" — they ask \"which channel carries them, to whom, and how will I know?\"",
))

# ------------------------------------------------------------------ 10.1.2
SPECS.append(make(M, "10.1.2", "Pilot design",
 "A pilot is a measurement exercise first: a small, deliberately mixed group, a baseline taken before anyone starts, and exit criteria written down in advance.",
 "write a one-page pilot charter with a roster, a baseline table and three exit criteria.",
 "capture the baseline before the first developer opens a session.",
 "cost per developer varies so widely that you cannot estimate your own spend from an average, which is why the pilot exists [%s]." % CO,
 [("Why pilot at all",
   "The costs page says per-developer cost varies widely with model selection, codebase size and usage patterns such as running multiple instances or automation. Across enterprise deployments the average is about $13 per developer per active day and $150-250 per developer per month, with costs below $30 per active day for 90 percent of users. To estimate your own spend, start with a small pilot group and establish a baseline with the tracking tools before wider rollout [%s]." % CO,
   """
| Figure | Value | Source status |
|---|---|---|
| Average per developer per active day | about $13 | Anthropic docs, enterprise average |
| Average per developer per month | $150-250 | Anthropic docs, enterprise average |
| Users below $30 per active day | 90%% | Anthropic docs |

These are Anthropic's published averages, not a forecast for your team [%s].
""" % CO,
   ("Average-as-budget", "You multiply the published $150-250 per month by headcount and present it as the budget, then the real distribution surprises finance.", "Use the pilot's own per-developer distribution, and plan for the tail, not the mean."),
   "cost tracking tools are Module 10.6; measurement is Module 10.8.",
   "the published average is a starting point; your pilot produces your number."),
  ("Who goes in the pilot",
   "The module brief asks for a small group across seniority levels and stacks. The docs advise starting guided: encourage new users to try codebase Q&A or smaller bug fixes, ask Claude Code to make a plan, check its suggestions, and over time let it run more agentically [%s]. [Practitioner heuristic, not in the docs: include at least one sceptic and one team with a hard legacy stack.]" % TP,
   """
| Slot | Why | Example |
|---|---|---|
| Senior engineer | Judges output quality | Staff backend |
| Junior engineer | Tests onboarding path | New hire |
| Different stacks | Finds tool and MCP gaps | Web, data, mobile |
| One sceptic | Surfaces objections early | Chosen by manager |
""",
   ("Volunteer-only pilot", "Only enthusiasts join, results look great, and the rollout stalls on the first sceptical team.", "Fill at least one slot with a sceptic and one with a stack nobody expects to work."),
   "champion selection is Module 10.1.3 in this module's later topic; training is Module 10.1.5 topic.",
   "mix seniority and stack on purpose."),
  ("Baseline before day one",
   "Baselines are only meaningful if taken before the tool is used. The analytics dashboard reports adoption and contribution metrics, and the docs say to use contribution metrics alongside DORA metrics, sprint velocity or other engineering KPIs [Claude Code docs, Track team usage with analytics, 2026]. Contribution metrics are described as deliberately conservative and an underestimate [same source].",
   """
| Baseline | Captured how | Compare at |
|---|---|---|
| PR cycle time | Your git host | Week 4 and 8 |
| Review turnaround | Your git host | Week 4 and 8 |
| Defect escape rate | Incident tracker | Week 8 |
| Developer sentiment | Survey | Day 0 and week 8 |
""",
   ("Retro baseline", "You collect the 'before' numbers after the pilot has started, so they already include Claude Code effects.", "Freeze baseline exports on the day before kickoff and store them with a date."),
   "metrics detail is Module 10.8.",
   "no baseline, no claim."),
  ("Exit criteria",
   "A pilot ends with a decision, so write the decision rule first. [Practitioner heuristic, not from the docs.] Tie each criterion to a number you can pull: adoption from the analytics dashboard, spend from the spend report, quality from your own trackers.",
   """
```text
Exit criteria (example, agree before kickoff)
1. >= 70% of pilot users active in weeks 3-4        (dashboard)
2. Spend per active user within the agreed band       (spend report)
3. No rise in defect escape rate vs baseline          (tracker)
Decision date: fixed, owner: named
```
""",
   ("Moving goalposts", "Criteria are written after seeing results, so the pilot always 'succeeds'.", "Sign the charter before kickoff; changes need a dated amendment."),
   "guardrails to have in place first are Module 10.1.6 topic and Module 10.4.",
   "criteria first, results second."),
 ],
 [("What do the docs say to do before wider rollout to estimate spend?", "Start with a small pilot group and use the tracking tools to establish a baseline."),
  ("Give the published average cost per developer per active day.", "About $13."),
  ("Give the published monthly range per developer.", "$150-250."),
  ("What share of users stay below $30 per active day?", "90 percent."),
  ("Only enthusiasts joined and the rollout stalled on a sceptical team. Name the failure mode by its exact label.", "**Volunteer-only pilot.**"),
  ("You multiplied the published monthly range by headcount and called it a budget. Name the failure mode.", "**Average-as-budget.**"),
  ("The 'before' numbers were exported in week 3. Name the failure mode.", "**Retro baseline.**"),
  ("Criteria were rewritten after results arrived. Name the failure mode.", "**Moving goalposts.**"),
  ("Are contribution metrics an over- or underestimate, per the docs?", "Deliberately conservative: an underestimate."),
 ],
 [("Draft the roster across seniority and stack", "`roster.md`"), ("Export baselines and date-stamp them", "`baseline/`"), ("Write three exit criteria with data sources", "`charter.md`"),
  ("Name decision owner and date", "Charter header"), ("Run the pilot and capture weekly numbers", "Weekly table"), ("Apply the criteria and write the decision", "Decision memo")],
 ("A signed pilot charter and a decision memo that applies it.", """
| Section | Content |
|---|---|
| Roster | 8 people, 3 stacks, 1 sceptic |
| Baseline | Dated exports for cycle time, review time, escapes |
| Criteria | Three numeric, each with a source |
| Decision | Date and owner named |
"""),
 """
| Element | What is wrong |
|---|---|
| Roster is the Slack channel regulars | **Volunteer-only pilot** |
| Baseline dated after kickoff | Retro baseline |
""",
 "The charter passes only if the baseline pre-dates kickoff and every exit criterion names its data source.",
 [("Anthropic", "Manage costs effectively", "Published cost averages and the pilot advice", "Current"),
  ("Anthropic", "Track team usage with analytics", "Adoption and contribution metrics, attribution caveats", "Current"),
  ("Anthropic", "Enterprise deployment overview", "Start with guided usage", "Current")],
 "the docs publish enterprise cost averages while stressing that costs vary widely; treat the averages as a prior, not a plan.",
 "This is the craft of the pilot: **a mixed group, a dated baseline, and rules for the decision written first.** The administrator who understands this does not ask \"did people like it?\" — they ask \"what number would change our decision?\"",
 thin="Seniority and stack mix is a practitioner heuristic; the docs give the pilot-and-baseline instruction but no roster template.",
))

# ------------------------------------------------------------------ 10.1.3
SPECS.append(make(M, "10.1.3", "Champions",
 "Champions are engineers who advocate Claude Code internally; they scale adoption only if they have a kit, a channel and protected time.",
 "write a champion charter naming the role, the kit contents, the time budget and one measurable outcome.",
 "give every champion the same written kit so advice is consistent.",
 "the most effective adoption lever in the docs is not a feature but shared configuration: checked-in CLAUDE.md and .mcp.json that every user inherits [%s]." % TP,
 [("What a champion does",
   "The module brief describes a champion kit as a playbook for engineers who advocate internally. I could not retrieve a page of that name in the Claude Code docs index, so the kit contents below are what the docs support rather than a retrieved template. The docs recommend investing in documentation so Claude Code understands your codebase, deploying CLAUDE.md at organisation level and repository level, and having one central team configure MCP servers and check a `.mcp.json` into the codebase [%s]." % TP,
   """
| Responsibility | Docs-supported artefact |
|---|---|
| Keep repo context current | Repository `CLAUDE.md` |
| Share integrations | Checked-in `.mcp.json` |
| Show safe first tasks | Codebase Q&A, small bug fixes, plan first |
| Give a one-click install | An internal install path |
""",
   ("Advocate without artefacts", "Champions give talks but leave no checked-in configuration, so each team rediscovers the same prompts.", "Make every champion output a committed file, not a slide."),
   "configuration scope is Module 3.2; managed policy is Module 10.4.",
   "a champion's output is a committed file."),
  ("Selecting and funding champions",
   "The docs say a one-click install path is key to growing adoption in a custom environment [%s]. [Practitioner heuristic: pick one champion per team, give a named weekly time budget, and rotate yearly.]" % TP,
   """
```text
Champion charter
Role:        one per team, volunteer + manager-approved
Time:        2 h/week protected (example; set your own)
Outputs:     repo CLAUDE.md, .mcp.json, 1 demo per month
Escalation:  admin channel for policy questions
```
""",
   ("Unfunded champion", "Champions are named but given no time, so the role decays within a month.", "Write the hours into the charter and have the manager sign it."),
   "metrics for champions are Module 10.8.",
   "name the hours or the role is decoration."),
  ("The champion kit contents",
   "The module brief lists a playbook; the closest retrievable guidance is the docs' own onboarding resources: the Quickstart, Common workflows, and the Anthropic Academy courses Claude 101 and Claude Code in Action [%s]. [Whether a separate champion kit exists is not verified here.]" % AS,
   """
| Kit item | Source |
|---|---|
| First-session walkthrough | Quickstart |
| Everyday patterns | Common workflows |
| Self-paced courses | Claude 101; Claude Code in Action |
| Login fixes | `/logout` then `/login`; `claude update` |
""",
   ("Kit drift", "Each champion writes their own kit, so teams get contradictory advice on permissions and models.", "Keep one canonical kit in a repository and have champions fork only the team-specific page."),
   "training formats are Module 10.1.5 topic.",
   "one kit, many champions."),
  ("Measuring champions",
   "The analytics leaderboard shows the top 10 users by contribution volume, and the docs suggest using it to find people with high adoption who can share techniques and help onboard others [Claude Code docs, Track team usage with analytics, 2026]. Treat it as a way to find champions, not to rank people.",
   """
| Signal | Where | Caveat |
|---|---|---|
| Top contributors | Analytics leaderboard (top 10) | Volume, not quality |
| Team adoption | Adoption chart | Team-level only |
""",
   ("Leaderboard worship", "You pick champions by raw contribution volume and publish the ranking, which rewards volume over teaching.", "Use the leaderboard to find candidates, then choose by teaching ability."),
   "pitfalls with vanity metrics are Module 10.8.",
   "find champions with data, choose them with judgement."),
 ],
 [("What do the docs say is key to growing adoption in a custom environment?", "A one-click way to install Claude Code."),
  ("How many users does the analytics leaderboard show?", "The top 10."),
  ("Champions give talks but commit nothing. Name the failure mode by its exact label.", "**Advocate without artefacts.**"),
  ("Champions have no protected hours. Name the failure mode.", "**Unfunded champion.**"),
  ("Each champion rewrote the kit and advice conflicts. Name the failure mode.", "**Kit drift.**"),
  ("You published a ranking by contribution volume. Name the failure mode.", "**Leaderboard worship.**"),
  ("Which two Anthropic Academy courses does the admin page name?", "Claude 101 and Claude Code in Action."),
  ("Which two files does the deployment overview say to check in so all users benefit?", "Repository CLAUDE.md and a `.mcp.json`."),
 ],
 [("Write the champion role and time budget", "`charter.md`"), ("Assemble the kit from docs resources", "`kit/`"), ("Name one champion per team", "Roster"),
  ("Set one measurable outcome per champion", "Outcome list"), ("Review after 30 days", "Review note"), ("Refresh the kit", "Kit v2")],
 ("A signed champion charter with hours, kit and outcomes.", """
| Item | Entry |
|---|---|
| Hours | Named, manager-signed |
| Kit | Single canonical repo |
| Output | Committed CLAUDE.md / .mcp.json per team |
"""),
 """
| Element | What is wrong |
|---|---|
| Output column says 'give a demo' | **Advocate without artefacts** |
| No hours | Unfunded champion |
""",
 "The charter passes only if each champion has named hours and a committed-file outcome.",
 [("Anthropic", "Enterprise deployment overview", "CLAUDE.md levels, MCP check-in, one-click install", "Current"),
  ("Anthropic", "Set up Claude Code for your organization", "Onboarding resources", "Current"),
  ("Anthropic", "Track team usage with analytics", "Leaderboard", "Current")],
 "the module brief names a champion kit but no such page was found in the docs index; the docs and the brief therefore differ on whether a kit exists.",
 "This is the craft of champions: **named people, protected hours, committed artefacts.** The administrator who understands this does not ask \"who is enthusiastic?\" — they ask \"what file will this person leave behind?\"",
 thin="The 'champion kit' from the module brief was not found in the retrieved docs; the guide uses docs-supported artefacts and flags the rest as heuristic.",
))

# ------------------------------------------------------------------ 10.1.4
SPECS.append(make(M, "10.1.4", "Communications",
 "Rollout communication fails when it says what is available but not what is enforced; the message set must match the actual policy.",
 "write a three-message sequence and an FAQ whose every answer matches a setting you can show.",
 "write each message from the live policy, never from memory.",
 "several of the most common user complaints are policy outcomes the user cannot see, so the FAQ must name them before the user hits them [%s]." % "Claude Code docs, Control MCP server access for your organization, 2026",
 [("What the user cannot see",
   "The module brief mentions a communications kit with announcements, drip messages and FAQ answers. I did not find a page of that name in the docs index, so this guide builds the message set from behaviours the docs describe. Several admin controls remove or block things silently: when MCP policy blocks a previously configured server, it disappears from `/mcp` and `claude mcp list` with no signal that policy is the reason, so the docs advise telling affected users which servers are blocked when you roll out a new restriction [Claude Code docs, Control MCP server access, 2026].",
   """
| Control | What the user sees | Message needed |
|---|---|---|
| MCP restriction | Server vanishes from `/mcp` | Which servers, why |
| Plugin allowlist | `Marketplace ... is not in the allowed marketplace list` | Which marketplaces are approved |
| Login restriction | Claude Code exits at startup on wrong org | Use your work account |
""",
   ("Silent restriction", "You tighten a policy and say nothing, so users file bugs for behaviour that is working as configured.", "Publish a change note before each restriction ships."),
   "policy contents are Module 10.4; troubleshooting is Module 12.5.",
   "every restriction needs a message before it needs a ticket."),
  ("The three-message sequence",
   "[Practitioner structure, not from the docs.] A launch message, a week-one drip and a week-four drip cover the arc. Use the docs' own recommended first tasks in the drip: codebase Q&A, small bug fixes, plan first [Claude Code docs, Enterprise deployment overview, 2026].",
   """
```text
Day 0   Announce: what, who, how to install, where to ask
Day 7   Drip: first safe tasks (Q&A, small fixes, plan first)
Day 28  Drip: what we changed after the pilot, what is blocked and why
```
""",
   ("Feature-list announcement", "The announcement lists features but not limits, so users assume everything works everywhere.", "Include one 'what is not available here' line per message."),
   "training schedule is Module 10.1.5 topic.",
   "announce limits as well as features."),
  ("FAQ built from real messages",
   "Anchor FAQ answers to exact messages the docs document. 'You haven't been added to your organization yet' means the seat lacks Claude Code access [Claude Code docs, Set up Claude Code for your organization, 2026]. A spend-limit message means a usage-credit cap was reached and an admin can raise it under Organization settings > Usage [Claude Code docs, Manage costs effectively, 2026].",
   """
| User sees | Meaning | Who acts |
|---|---|---|
| 'You haven't been added to your organization yet' | Seat has no Claude Code access | Admin updates seat |
| 'You've hit your session limit' | Seat usage window | User waits, or `/usage-credits` |
| Spend limit message | Usage-credit cap reached | Admin raises limit |
""",
   ("Paraphrased FAQ", "The FAQ paraphrases error messages, so users cannot search for the wording they actually see.", "Quote the exact message text."),
   "limits and errors are Module 12.6; plans are Module 1.4.",
   "quote the message, then explain it."),
  ("Keeping it current",
   "[Practitioner heuristic.] Treat communications as versioned documentation: each policy change updates the FAQ in the same change request.",
   """
| Trigger | Update |
|---|---|
| New managed key | FAQ entry + change note |
| New provider | Install page |
| Version floor raised | Update instructions |
""",
   ("Stale FAQ", "Policy changes ship but the FAQ still describes last quarter's setup.", "Make FAQ updates a required checklist item on every policy change."),
   "version floors are Module 10.4.",
   "docs and policy ship together."),
 ],
 [("What happens in `/mcp` when policy blocks a server you had configured?", "It disappears from `/mcp` and `claude mcp list` with no signal that policy is the reason."),
  ("What does the docs advise when rolling out a new MCP restriction?", "Tell affected users which servers are blocked."),
  ("You tightened a policy and told no one. Name the failure mode by its exact label.", "**Silent restriction.**"),
  ("The announcement listed features only. Name the failure mode.", "**Feature-list announcement.**"),
  ("The FAQ rewords error messages. Name the failure mode.", "**Paraphrased FAQ.**"),
  ("The FAQ still describes last quarter's setup. Name the failure mode.", "**Stale FAQ.**"),
  ("How many messages are in the suggested sequence, and on which days?", "Three: day 0, day 7, day 28."),
  ("What does 'You haven't been added to your organization yet' mean?", "The user's seat does not include Claude Code access; an admin must update it."),
 ],
 [("Inventory every restriction users will notice", "`restrictions.md`"), ("Write the three messages", "`messages/`"), ("Draft FAQ with exact error text", "`faq.md`"),
  ("Map each FAQ answer to a setting", "Mapping table"), ("Send and collect questions", "Question log"), ("Update FAQ from the log", "FAQ v2")],
 ("A message set and FAQ where every answer cites a setting.", """
| FAQ item | Quoted message | Setting |
|---|---|---|
| Login exits | Org mismatch error | `forceLoginOrgUUID` |
| Plugin blocked | allowed marketplace list | `strictKnownMarketplaces` |
"""),
 """
| Element | What is wrong |
|---|---|
| FAQ says 'ask IT if something breaks' | **Paraphrased FAQ** |
| Day-28 note missing | Stale FAQ risk |
""",
 "The set passes only if each FAQ answer quotes a real message and names the setting behind it.",
 [("Anthropic", "Control MCP server access", "Silent disappearance of blocked servers", "Current"),
  ("Anthropic", "Manage costs effectively", "Limit messages and who acts", "Current"),
  ("Anthropic", "Set up Claude Code for your organization", "Login fixes and seat message", "Current")],
 "the module brief describes a communications kit; no such page was found, so message structure here is practitioner heuristic.",
 "This is the craft of communication: **say what is limited before the limit is felt.** The administrator who understands this does not ask \"what should we announce?\" — they ask \"what will confuse someone on day three?\"",
 thin="No official communications kit was found; message structure is heuristic, behaviours cited are from the docs.",
))

# ------------------------------------------------------------------ 10.1.5
SPECS.append(make(M, "10.1.5", "Training",
 "Training works when it is short, task-shaped and backed by shared prompts and office hours rather than one long workshop.",
 "design a four-week training plan with one format per week and a success check for each.",
 "teach the loop and the controls together, never the prompts alone.",
 "the module brief lists in-product lessons (/powerup), but I could not verify that command in the retrieved docs, so a training plan should not depend on it [Claude Code docs index, 2026].",
 [("What can be cited",
   "The docs name concrete training resources: a Quickstart first-session walkthrough, Common workflows for everyday tasks like code review, refactoring and debugging, and the self-paced Anthropic Academy courses Claude 101 and Claude Code in Action [Claude Code docs, Set up Claude Code for your organization, 2026]. A search of the docs index for a `/powerup` page found nothing, so it is treated as unverified.",
   """
| Resource | Format | Source |
|---|---|---|
| Quickstart | Self-paced | Docs |
| Common workflows | Reference | Docs |
| Claude 101 | Course | Anthropic Academy |
| Claude Code in Action | Course | Anthropic Academy |
| `/powerup` | In-product lessons | **Not verified** in docs index |
""",
   ("Phantom curriculum", "You build the plan around a command or page that does not exist in your version, and week one fails.", "Run each command on the version you deploy before it enters the plan."),
   "version floors are Module 10.4; command lists are Module 14.1.",
   "teach only what you have run."),
  ("Four formats, four weeks",
   "[Practitioner structure.] Mix a workshop, shared prompts, office hours and paired sessions so people with different styles all have a route. Anchor week one on the docs' own advice to start with codebase Q&A and small fixes, and to ask for a plan first [Claude Code docs, Enterprise deployment overview, 2026].",
   """
| Week | Format | Check |
|---|---|---|
| 1 | 60-minute workshop on the loop and `/status` | Everyone runs a plan-first task |
| 2 | Shared prompt library | Each team adds 3 prompts |
| 3 | Office hours | Questions logged |
| 4 | Pair on a real ticket | Ticket merged |
""",
   ("Marathon workshop", "One four-hour session covers everything and nothing is retained.", "Keep sessions to an hour and attach a hands-on check to each."),
   "the loop itself is Module 1.2; prompting is Module 2.2.",
   "short sessions with a task each."),
  ("Shared prompt libraries",
   "Prompts should live with the code. The docs recommend repository-level CLAUDE.md files holding architecture, build commands and contribution guidelines, checked into source control so all users benefit [Claude Code docs, Enterprise deployment overview, 2026]. Reusable procedures can become skills [see Module 5.2].",
   """
```text
repo/
  CLAUDE.md            architecture, build, conventions
  .claude/skills/...   reusable procedures
  docs/prompts.md      team prompt examples with outcomes
```
""",
   ("Wiki-rot prompts", "Prompts live on a wiki, drift from the code, and nobody trusts them.", "Store prompts in the repository and review them in pull requests."),
   "CLAUDE.md is Module 3.2; skills are Module 5.2.",
   "prompts belong in version control."),
  ("Teaching the controls",
   "Training must include what Claude Code is not allowed to do. Teach `/permissions` to inspect effective rules, `/status` to see which settings sources apply, and Esc plus `/rewind` for recovery [Claude Code docs, Server-managed settings, 2026; Claude Code docs, Manage costs effectively, 2026].",
   """
| Command | Teach it as |
|---|---|
| `/permissions` | See your effective rules |
| `/status` | See which managed source applies |
| `Esc`, `/rewind` | Stop and undo |
| `/usage` | See your session spend and plan usage |
""",
   ("Prompt-only training", "People learn prompts but not the controls, then blame the tool when a policy blocks them.", "Spend a third of every session on controls and diagnostics."),
   "diagnostics are Module 12.1.",
   "teach the controls with the craft."),
 ],
 [("Name the two Anthropic Academy courses on the admin page.", "Claude 101 and Claude Code in Action."),
  ("Which in-product command from the module brief could not be verified in the docs index?", "/powerup."),
  ("How long is the suggested week-1 workshop?", "60 minutes."),
  ("You built week one around a command that does not exist in your version. Name the failure mode by its exact label.", "**Phantom curriculum.**"),
  ("A four-hour session is forgotten. Name the failure mode.", "**Marathon workshop.**"),
  ("Prompts drift on a wiki. Name the failure mode.", "**Wiki-rot prompts.**"),
  ("Trainees can prompt but are confused by blocks. Name the failure mode.", "**Prompt-only training.**"),
  ("Which command shows which managed settings source applies?", "`/status`."),
 ],
 [("Run every planned command on your deployed version", "Verified list"), ("Draft four weekly formats with checks", "`plan.md`"), ("Create the prompt library in a repo", "`docs/prompts.md`"),
  ("Add a controls segment to each session", "Agenda"), ("Pilot with one team", "Feedback"), ("Revise the plan", "Plan v2")],
 ("A four-week plan whose every command was run on the deployed version.", """
| Week | Format | Verified commands |
|---|---|---|
| 1 | Workshop | `/status`, `/permissions` |
| 2 | Prompt library | n/a |
"""),
 """
| Element | What is wrong |
|---|---|
| Week 1 depends on `/powerup` unverified | **Phantom curriculum** |
| One 4-hour session | Marathon workshop |
""",
 "The plan passes only if every command in it has been run on the version the organisation deploys.",
 [("Anthropic", "Set up Claude Code for your organization", "Onboarding resources and courses", "Current"),
  ("Anthropic", "Enterprise deployment overview", "Guided usage and CLAUDE.md", "Current"),
  ("Anthropic", "Manage costs effectively", "/usage and recovery habits", "Current")],
 "the module brief lists `/powerup`; the docs index does not, so the sources disagree on whether it is an official in-product lesson command.",
 "This is the craft of training: **short sessions, committed prompts, and the controls taught beside the craft.** The administrator who understands this does not ask \"how much training?\" — they ask \"what can each person do and check by Friday?\"",
 thin="`/powerup` could not be verified; session lengths and week structure are practitioner heuristics.",
))

# ------------------------------------------------------------------ 10.1.6
SPECS.append(make(M, "10.1.6", "Guardrails before scale",
 "Put the permission lockdown, sandbox baseline, hook policy and plugin allowlist in place before the second team joins, because retrofitting policy onto habits is harder than shipping with it.",
 "assemble a managed-settings document with four guardrail groups and prove each takes effect on a test machine.",
 "ship the guardrails with the first wave, not after the first incident.",
 "a deny rule is not a security boundary around a program: it matches the command text Claude writes, so network enforcement needs the sandbox, not only rules [Claude Code docs, Configure permissions, 2026].",
 [("Four guardrail groups",
   "The admin-setup page lists the controls and their keys. For this module's four groups: permission lockdown (`allowManagedPermissionRulesOnly`, `permissions.disableBypassPermissionsMode`), sandboxing (`sandbox.enabled`, `sandbox.network.allowedDomains`), hook restrictions (`allowManagedHooksOnly`, `allowedHttpHookUrls`) and plugin marketplace control (`strictKnownMarketplaces`, `blockedMarketplaces`, `disableSideloadFlags`) [%s]." % AS,
   """
| Group | Keys | Effect |
|---|---|---|
| Permission lockdown | `allowManagedPermissionRulesOnly`, `permissions.disableBypassPermissionsMode` | Managed rules only; disable bypass mode |
| Sandbox | `sandbox.enabled`, `sandbox.network.allowedDomains` | OS-level filesystem and network isolation |
| Hooks | `allowManagedHooksOnly`, `allowedHttpHookUrls` | Restrict which hooks run |
| Plugins | `strictKnownMarketplaces`, `blockedMarketplaces`, `disableSideloadFlags` | Restrict sources and sideloading |
""",
   ("Rules-as-boundary", "You deny `Bash(curl *)` and believe network egress is closed, but `/usr/bin/curl` or `sh -c 'curl ...'` still run.", "Add the sandbox network allowlist; use rules for intent, the sandbox for enforcement."),
   "rule syntax is Module 4.2; sandboxing is Module 4.4; hooks are Module 5.4.",
   "rules express intent; the sandbox enforces."),
  ("A starter document",
   "The server-managed settings page gives a worked example that denies `Bash(curl *)` and reads of `.env` and `secrets`, sets `permissions.disableBypassPermissionsMode` to `disable`, and sets `allowManagedPermissionRulesOnly` to true. Array settings such as `permissions.allow` and `permissions.deny` merge from all sources, so developers can extend managed lists but not remove from them [%s; Claude Code docs, Configure server-managed settings, 2026]." % AS,
   """
```json
{
  "permissions": {
    "deny": ["Bash(curl *)", "Read(./.env)", "Read(./.env.*)", "Read(./secrets/**)"],
    "disableBypassPermissionsMode": "disable"
  },
  "allowManagedPermissionRulesOnly": true,
  "sandbox": { "enabled": true, "failIfUnavailable": true, "allowUnsandboxedCommands": false }
}
```
""",
   ("Unsandboxed fallback", "The sandbox is enabled but cannot start on some machines, and Claude runs commands unsandboxed.", "Set `failIfUnavailable` and `allowUnsandboxedCommands: false` in managed settings [Claude Code docs, Sandboxed Bash tool, 2026]."),
   "the sandbox page is Module 4.4; managed delivery is Module 10.4.",
   "set fail-closed sandbox keys, or the sandbox is advisory."),
  ("Test on a real machine",
   "Verification is `/status` for the `Setting sources` line and `/permissions` for effective rules. Server-managed settings with shell-command or hook content trigger a security approval dialog, and a user who rejects the settings makes Claude Code exit [Claude Code docs, Configure server-managed settings, 2026]. Plan for the dialog in your rollout messages.",
   """
| Check | Command | Expect |
|---|---|---|
| Source | `/status` | `Enterprise managed settings (...)` |
| Rules | `/permissions` | Managed deny rules visible |
| Bypass | `claude --dangerously-skip-permissions` | Refused or disabled |
| Network | `curl` inside sandbox to unlisted host | Blocked |
""",
   ("Admin-only testing", "You test policy as an administrator account that is exempt or differently configured, and ordinary users see something else.", "Test with a normal user account on a clean machine."),
   "verification detail is Module 10.4.",
   "test as the user, not as the admin."),
 ],
 [("Name the key that makes managed settings the only source of permission rules.", "`allowManagedPermissionRulesOnly`."),
  ("Which key disables bypass mode in managed settings, and to what value?", "`permissions.disableBypassPermissionsMode` set to `disable`."),
  ("You denied `Bash(curl *)` and assumed egress was closed. Name the failure mode by its exact label.", "**Rules-as-boundary.**"),
  ("The sandbox could not start and commands ran unsandboxed. Name the failure mode.", "**Unsandboxed fallback.**"),
  ("Policy tested only from an admin account. Name the failure mode.", "**Admin-only testing.**"),
  ("Can developers remove entries from managed `permissions.deny`?", "No; array settings merge from all sources so they can extend but not remove."),
  ("Which two sandbox keys appear in the admin-setup table?", "`sandbox.enabled` and `sandbox.network.allowedDomains`."),
  ("What happens if a user rejects a server-managed settings security dialog?", "Claude Code exits."),
 ],
 [("Draft the four guardrail groups as one document", "`managed-settings.json`"), ("Deploy to a test machine", "Machine log"), ("Run the four checks in the table", "Check results"),
  ("Attempt each bypass as a normal user", "Bypass attempts"), ("Record the `/status` line", "Evidence"), ("Fix gaps and re-test", "Re-test log")],
 ("A managed-settings document with check results for each guardrail.", """
| Guardrail | Test | Result |
|---|---|---|
| Deny `.env` read | Ask Claude to read `.env` | Denied |
| Bypass disabled | Start with skip flag | Refused |
| Sandbox network | `curl` unlisted host | Blocked |
"""),
 """
| Element | What is wrong |
|---|---|
| Only deny rules, no sandbox | **Rules-as-boundary** |
| `failIfUnavailable` absent | Unsandboxed fallback risk |
""",
 "The document passes only if each guardrail group has a recorded test run as a normal user.",
 [("Anthropic", "Set up Claude Code for your organization", "Control and key table", "Current"),
  ("Anthropic", "Configure permissions", "Rule limits and sandbox interaction", "Current"),
  ("Anthropic", "Sandboxed Bash tool", "failIfUnavailable, managed enforcement", "Current; page truncated at end")],
 "none found between the sources read.",
 "This is the craft of guardrails: **intent in rules, enforcement in the sandbox, proof on a real machine.** The administrator who understands this does not ask \"what did we deny?\" — they ask \"what stops it if the rule is bypassed?\"",
))

if __name__ == "__main__":
    run(SPECS)
