import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen import write
from specs_12 import T

M = "b-1-3"
SPECS = []

# ---------------------------------------------------------------- 1.3.1 INSTALL
SPECS.append(dict(
 mod=M, id="1.3.1", title="Requirements and install", short="Requirements and install",
 thesis="A good install is one binary, one install path, a known version and a diagnostic that passes.",
 prove="install on a clean account, run the version and doctor checks, and show that exactly one copy of claude is on the PATH.",
 discipline="pick one install method and prove it with the version and doctor commands.",
 counter="more install options is not more flexibility; mixed methods produce two binaries at different versions and behaviour that depends on which shell you opened.",
 read_min=20, prove_h="2", depth=["Install by the recommended path and verify", "Choose an install method per platform and policy", "Standardise and pin installs across a fleet"],
 deliverable="A clean-install log with version, doctor output and a single-binary proof.",
 sections=[
 dict(title="The install paths", framing="The recommended route is the native installer. Alternatives exist for Homebrew, WinGet and Linux package managers (apt, dnf, apk); native installs auto-update in the background while Homebrew and WinGet do not [Claude Code docs, Overview and Setup, 2026]. Most surfaces need a Claude subscription or Console account; the terminal CLI, VS Code and JetBrains also support third-party providers [Claude Code docs, Overview, 2026].",
  body=T("""
| Platform | Documented route | Updates |
|---|---|---|
| macOS, Linux, WSL | `curl -fsSL https://claude.ai/install.sh \\| bash` | Auto |
| Windows (PowerShell) | `irm https://claude.ai/install.ps1 \\| iex` | Auto |
| macOS | `brew install --cask claude-code` | Manual |
| Windows | `winget install Anthropic.ClaudeCode` | Manual |
| Debian, Fedora, RHEL, Alpine | apt, dnf or apk | Per package manager |

[Claude Code docs, Overview and Setup, 2026; read the exact current line on the Setup page before running]

The native installer places the binary at `~/.local/bin/claude` on macOS and Linux and `%USERPROFILE%\\.local\\bin\\claude.exe` on Windows [Claude Code docs, Troubleshoot install, 2026].
"""),
  fm=[("Copy-pasted installer", "You paste an install one-liner from a blog post or old note and run a script you did not read.", "Take the command only from the official Setup page, read what it does, and verify the version afterward.")],
  xr="sign-in is Module 1.3.2; fleet rollout is in Part 11.", one="official page, one method, verified."),
 dict(title="Platform specifics", framing="Windows has two routes: native (needs Git Bash, with a PowerShell tool) or WSL, where you install and launch `claude` inside the WSL terminal rather than PowerShell or CMD [Claude Code docs, Setup, 2026]. Alpine and other musl distributions need `bash` and `curl` installed first, and Claude Code requires `bash` or `zsh`; set `USE_BUILTIN_RIPGREP=0` there [Claude Code docs, Setup, 2026].",
  body=T("""
| Platform | Gotcha | Fix |
|---|---|---|
| Native Windows | Git Bash not found | Set `CLAUDE_CODE_GIT_BASH_PATH` in settings `env` |
| WSL | Installing from PowerShell | Install inside the WSL terminal |
| Alpine | No bash or curl by default | Install them, set `USE_BUILTIN_RIPGREP=0` |
| IDE extension only | No `claude` on PATH | Run the standalone installer |

```json
{ "env": { "CLAUDE_CODE_GIT_BASH_PATH": "C:\\\\Program Files\\\\Git\\\\bin\\\\bash.exe" } }
```

ripgrep is usually bundled; if search fails see the search troubleshooting section [Claude Code docs, Setup, 2026]. The VS Code extension carries a private CLI copy and does not add `claude` to PATH [Claude Code docs, Troubleshoot install, 2026].
"""),
  fm=[("Wrong-environment install", "You install in PowerShell and then launch from WSL (or the reverse) and cannot find the binary.", "Install and launch in the same environment, and verify with `claude --version` there.")],
  xr="IDE integrations are Module 7.3; troubleshooting is Module 1.3.7.", one="install where you will run it."),
 dict(title="Verify, always", framing="A working installation prints a version number such as 2.1.211 (Claude Code); for a deeper check run `claude doctor` [Claude Code docs, Setup, 2026].",
  body=T("""
```bash
claude --version     # e.g. 2.1.211 (Claude Code)
claude doctor        # detailed installation and configuration check
which -a claude      # list EVERY claude on PATH (Windows: where claude)
```

| Output | Meaning |
|---|---|
| Version prints | Binary and PATH fine |
| `command not found` | PATH problem, see 1.3.7 |
| Two paths from `which -a` | Install-path drift |
"""),
  fm=[("Install-path drift", "You install by one method, later by another, and end up with two binaries at different versions.", "Pick one method, list all copies with `which -a claude`, remove extras and confirm the version.")],
  xr="updating is Module 1.3.5; troubleshooting is Module 1.3.7.", one="`which -a claude` should list exactly one."),
 dict(title="Removing and pinning", framing="Version management is part of install: the native installer accepts a version number or a release channel (latest or stable); `DISABLE_UPDATES` blocks all update paths including manual ones [Claude Code docs, Setup, 2026].",
  body=T("""
| Goal | Mechanism |
|---|---|
| Stay on a stable cadence | `stable` channel |
| Freeze a version | Install a specific version number |
| Block updates entirely | `DISABLE_UPDATES` |
| Uninstall | Per-method (remove native binary, `brew uninstall`, winget uninstall); see Setup |
"""),
  fm=[("Unpinned fleet", "Every developer auto-updates on their own schedule and behaviour differs across the team.", "Pin a version or use the stable channel for fleets and record the version in bug reports.")],
  xr="enterprise rollout is in Part 11; settings are Module 4.1.", one="a team needs a version policy."),
 ],
 retrieval=[
  ("Which install route is recommended and which two do not auto-update?", "Native installer; Homebrew and WinGet do not."),
  ("Where does the native installer place the binary on macOS and Linux?", "`~/.local/bin/claude`."),
  ("You paste an installer from a blog and run it unread. Name the failure mode by its exact label.", "**Copy-pasted installer.**"),
  ("Two claude binaries are on PATH. Name the failure mode and the command that finds them.", "**Install-path drift.** `which -a claude`."),
  ("You install in PowerShell and launch in WSL. Name the failure mode.", "**Wrong-environment install.**"),
  ("What does Alpine need before the installer works?", "bash and curl, plus `USE_BUILTIN_RIPGREP=0`."),
  ("Which variable blocks all updates?", "`DISABLE_UPDATES`."),
  ("Each developer updates on their own schedule. Name the failure mode.", "**Unpinned fleet.**"),
  ("Why does an IDE-only install not give you `claude` in a terminal?", "The extension bundles a private CLI copy and does not add it to PATH."),
 ],
 steps=[("Install by the recommended path on a clean user or container", "Install log"), ("Run `claude --version` and `claude doctor`", "Outputs"),
        ("Run `which -a claude` and confirm one copy", "Output"), ("Install by a second method on purpose and show the drift", "Two paths"),
        ("Remove the extra and re-verify", "Final output"), ("Write the pin or channel policy you would use for a team", "`policy.md`")],
 pass_md=T("""
| Check | Result |
|---|---|
| `claude --version` | A version string |
| `claude doctor` | No unresolved warnings |
| `which -a claude` | One path |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| 'Installed three times, works now' | **Install-path drift** unchecked |
"""),
 verdict="The artifact passes only if `which -a claude` ends with exactly one path.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Advanced setup | Installers, channels, pinning | Current |
| Anthropic | Claude Code overview | Install lines and auto-update behaviour | Current |
| Anthropic | Troubleshoot installation and login | Binary location, IDE caveat | Current |
""") + "\n\n*Disagreement named:* older pages require Node.js 18+ and npm; the current Setup page makes the native installer primary. **The Setup page wins.**",
 reframe="This is the craft of installing: **one method, one binary, one version, verified.** The engineer who understands this does not ask \"did it install?\" — they ask \"which copy am I running, and who controls its version?\"",
))

# ---------------------------------------------------------------- 1.3.2 SIGN-IN
SPECS.append(dict(
 mod=M, id="1.3.2", title="Sign-in options and credential order", short="Sign-in options and credential order",
 thesis="How you sign in decides who pays, which limits apply and which credential wins when several exist.",
 prove="sign in two different ways, show which credential is active, and explain what changed.",
 discipline="choose the account type deliberately and check which credential is active.",
 counter="more credentials in the environment do not add up; Claude Code picks one by a fixed order, and the winner may not be the one you expect [Claude Code docs, Authentication, 2026].",
 read_min=20, prove_h="2", depth=["Name the account types and how to switch", "Predict the active credential from the environment", "Design team authentication with spend controls"],
 deliverable="A credential-precedence worksheet tested against two real configurations.",
 sections=[
 dict(title="The account families", framing="Claude Code supports individual Claude.ai accounts, Claude for Teams or Enterprise, the Claude Console, and cloud providers such as Amazon Bedrock, Google Vertex AI (now named Google Cloud's Agent Platform in some pages) and Microsoft Foundry [Claude Code docs, Authentication, 2026].",
  body=T("""
| Path | How you sign in | Billing |
|---|---|---|
| Claude.ai subscription | Browser login | Included in plan, rolling limits |
| Teams or Enterprise | Org account | Org plan |
| Claude Console | Console credentials; admin invites first | Per-token API billing |
| Cloud provider | Set environment variables before running `claude`; no browser login | Your cloud bill |
| Claude apps gateway | `/login` with enterprise SSO | Gateway to your provider |

Use `/login` inside Claude Code to log in again or switch accounts, and `/logout` to log out and re-authenticate [Claude Code docs, Authentication, 2026].
"""),
  fm=[("Wrong-billing-path surprise", "You sign in with a Console key out of habit and a long session bills per token, or you run CI on a subscription.", "Choose the path deliberately and check the active account and `/usage`.")],
  xr="plans and limits are Module 1.4; provider setup is in Part 11.", one="the login is the billing decision."),
 dict(title="Credential precedence", framing="When several credentials exist, Claude Code selects one in a fixed order. Cloud-provider credentials win when `CLAUDE_CODE_USE_BEDROCK`, `CLAUDE_CODE_USE_VERTEX` or `CLAUDE_CODE_USE_FOUNDRY` is set. A signed Claude apps gateway session sits outside the list and takes precedence over them: when a gateway session exists, the CLI authenticates with the gateway token even if those variables are set [Claude Code docs, Authentication, 2026]. The rest of the order (bearer token, API key, `apiKeyHelper`, subscription) is on the Authentication page; this guide does not reproduce it because it was read via search excerpts.",
  body=T("""
| Mechanism | Purpose |
|---|---|
| `.credentials.json` | Managed by `/login` and `/logout` |
| `ANTHROPIC_BASE_URL` | Route requests through a custom API endpoint |
| `apiKeyHelper` setting | A script that returns an API key |
| Cloud provider env vars | Select Bedrock, Vertex or Foundry |

[Claude Code docs, Authentication and Team, 2026]
"""),
  fm=[("Env-var override", "A leftover provider or API-key environment variable silently overrides your subscription login, and the bill or limits are not what you expected.", "Check the environment (`env | grep -i -E 'anthropic|claude_code_use'`) and `/login` status, and remove stale variables.")],
  xr="settings and environment variables are Modules 4.1 and 4.8.", one="the environment can outrank your login."),
 dict(title="Teams: who holds the key", framing="For teams, per-user accounts or per-workspace keys keep usage attributable and revocable. Shared personal credentials make both impossible.",
  body=T("""
| Pattern | Attribution | Revocation |
|---|---|---|
| Per-user Teams or Enterprise account | Per user | Per user |
| Per-workspace Console key with spend limit | Per workspace | Per key |
| One shared personal login | None | All or nothing |
| Key in repo or shell history | Leaked | Rotate everything |

Store keys in a secrets manager, never in repositories or shell history.
"""),
  fm=[("Shared-credential shortcut", "A team shares one personal login for convenience, so usage cannot be attributed and revoking one person revokes all.", "Use per-user accounts or per-workspace keys with spend limits stored in a secrets manager.")],
  xr="cost governance is in Part 11; spend limits are Module 1.4.", one="one identity per person or per workspace."),
 dict(title="Credential expiry and long-running work", framing="Persistent Remote Control sessions stop making progress when credentials expire and cannot recover until you log in again [Claude Code docs, Authentication, 2026; from the translated page, verify in English].",
  body=T("""
| Situation | What to do |
|---|---|
| Login loop or wrong account | `/logout`, then `/login`, and confirm the account shown |
| Long-running remote session | Check that credentials are valid before leaving |
| Scheduled or CI runs | Use a Console key or provider credentials, not a personal login |
"""),
  fm=[("Expired-credential stall", "A long remote or scheduled session loses credentials and silently stops.", "Refresh login before leaving and use service credentials for unattended runs.")],
  xr="remote control is Module 7.5; CI is Module 7.8.", one="unattended work needs durable credentials."),
 ],
 retrieval=[
  ("Name four sign-in families.", "Claude.ai subscription, Teams or Enterprise, Claude Console, cloud provider."),
  ("Which command switches accounts and which logs out?", "`/login` and `/logout`."),
  ("A stale env var overrides your login. Name the failure mode by its exact label.", "**Env-var override.**"),
  ("What file do /login and /logout manage?", "`.credentials.json`."),
  ("Which variable routes requests through a custom API endpoint?", "`ANTHROPIC_BASE_URL`."),
  ("A team shares one personal login. Name the failure mode and fix.", "**Shared-credential shortcut.** Per-user accounts or per-workspace keys with spend limits."),
  ("You sign in with a Console key out of habit. Name the failure mode.", "**Wrong-billing-path surprise.**"),
  ("What does a cloud-provider login not need?", "A browser login; set environment variables first."),
  ("A remote session stalls after credentials expire. Name the failure mode.", "**Expired-credential stall.**"),
 ],
 steps=[("Run `/login` status or check which account is active", "Observation"), ("Set a provider variable in a throwaway shell and observe the change", "Observation"),
        ("Unset it and confirm the subscription returns", "Observation"), ("Fill the precedence worksheet from the Authentication page", "Worksheet"),
        ("Predict the winner for three env combinations, then test two", "Predictions vs results"), ("Write the team key policy", "`keys.md`")],
 pass_md=T("""
| Environment | Predicted | Observed |
|---|---|---|
| Provider var set | Provider | Provider |
| Only subscription | Subscription | Subscription |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Precedence from a blog | **Env-var override** risk |
"""),
 verdict="The artifact passes only if at least two predictions were tested against real behaviour.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Authentication | Account types, `/login`, provider variables | Current; read via search excerpts |
| Anthropic | Team and IAM pages | Credential management | Current; not fetched in full |
""") + "\n\n*Disagreement named:* some pages say Google Vertex AI and others Google Cloud's Agent Platform. **Both name the same provider route; the current Authentication page wording wins.**",
 reframe="This is the craft of sign-in: **choose the path, know the precedence, and keep unattended work on durable credentials.** The engineer who understands this does not ask \"am I logged in?\" — they ask \"which credential is active, and who pays?\"",
))

# ---------------------------------------------------------------- 1.3.3 FIRST SESSION
SPECS.append(dict(
 mod=M, id="1.3.3", title="The first session: a small, reviewed change", short="The first session: a small, reviewed change",
 thesis="The first session has one job: let you see the whole loop once at low stakes, from question to reviewed diff.",
 prove="complete the five-step first session on a small repo and identify one tool call of each kind in the transcript.",
 discipline="start clean, keep it small, and read the diff before widening the task.",
 counter="the best first task is boring. A showpiece failure teaches you nothing about whether setup, prompt or model was at fault.",
 read_min=20, prove_h="2", depth=["Run the first-session sequence", "Interpret permission prompts and the diff", "Design an onboarding session for a team"],
 deliverable="A first-session transcript with annotated tool calls and a `git diff` under ~30 lines.",
 sections=[
 dict(title="Start clean", framing="Claude Code reads your project files as needed; you do not add context manually [Claude Code docs, Quickstart, 2026]. Start from a project directory with a clean tree so the diff afterwards is only Claude's.",
  body=T("""
```bash
cd ~/projects/small-repo
git status        # clean? if not, commit or stash
git switch -c first-session
claude
```

Starting in a project subdirectory (not your home directory) means workspace trust is saved per directory [Claude Code docs, Security, 2026].
"""),
  fm=[("Dirty-tree start", "You begin with uncommitted work, Claude edits files, and the two sets of changes blur together.", "Commit or stash first, work on a branch and treat `git diff` as the review surface.")],
  xr="git workflows are Module 2.6; trust is Module 1.3.4.", one="a clean tree makes the diff the whole story."),
 dict(title="The five steps", framing="The quickstart sequence: install, start a session, ask a first question, make a first change, use git [Claude Code docs, Quickstart, 2026].",
  body=T("""
| Step | Prompt (examples from the quickstart) | What to watch |
|---|---|---|
| Orient | `give me an overview of this codebase` | Which files it reads |
| Ask | `how is authentication handled?` | Search before guessing |
| Change | `add a hello world function to the main file` | A permission prompt, then an edit |
| Git | `what files have I changed?` then `commit my changes with a descriptive message` | `git` via Bash |
| Review | `git diff` | Scope and surprises |

Press `Shift+Tab` at any time to switch permission mode [Claude Code docs, Quickstart, 2026]. If a change misbehaves, your git history is untouched until you commit, so `git checkout` undoes it [Claude Help Center, Your first day, 2026].
"""),
  fm=[("Showpiece first session", "You open your most important repo and ask for a large refactor on day one, then cannot tell whether a bad result was setup, prompt or model.", "Use a small repo or throwaway branch, one scoped change, and read the diff before widening the task.")],
  xr="the explore, plan, implement, commit loop is Module 2.1; prompting is Module 2.2.", one="boring first tasks teach the most."),
 dict(title="Reading the permission prompt", framing="In Manual mode Claude asks before edits and commands. The prompt offers approve once, approve and do not ask again for edits for the rest of the session, or reject with an explanation [Claude Help Center, Your first day, 2026].",
  body=T("""
| Choice | Effect |
|---|---|
| Yes | Run this action once |
| Yes, don't ask again for edits | Auto-approve edits for the session |
| No (with a comment) | The comment becomes the reason; Claude continues |

If you select No without a comment on a main-conversation prompt, Claude Code stops the turn [Claude Code docs, Permissions, 2026].
"""),
  fm=[("Approve-all-early", "You pick 'don't ask again' on the first prompt and later approve edits you would have rejected.", "Approve once while learning, and widen only when you trust the pattern.")],
  xr="permission modes are Module 4.3; rules are Module 4.2.", one="approve once until you know the pattern."),
 dict(title="Ending well: init, commit or revert", framing="End the session by either committing or reverting. The first-day guide suggests running `/init` once per project to generate a CLAUDE.md capturing codebase conventions [Claude Help Center, Your first day, 2026].",
  body=T("""
```text
/init                     # generate CLAUDE.md from the codebase (once per project)
commit with a descriptive message     # or: git restore .  to revert
```

| Outcome | Action |
|---|---|
| Diff is right | Commit |
| Diff is wrong | `git restore .` and rewrite the prompt |
| Learned a convention | Add it to CLAUDE.md |
"""),
  fm=[("Unreviewed commit", "You let Claude commit without reading the diff, and a stray change lands in history.", "Read `git diff` first and ask for a commit message only after you have reviewed.")],
  xr="CLAUDE.md is Module 3.2; checkpoints are Module 2.5.", one="review, then commit; or revert."),
 ],
 retrieval=[
  ("Why start from a clean tree?", "So the diff afterwards contains only Claude's changes."),
  ("You start your first session by asking for a big refactor. Name the failure mode by its exact label.", "**Showpiece first session.**"),
  ("Uncommitted work blurs with Claude's edits. Name the failure mode.", "**Dirty-tree start.**"),
  ("Which key switches permission mode?", "`Shift+Tab`."),
  ("What does choosing No without a comment do on a main-conversation prompt?", "Claude Code stops the turn."),
  ("You approve all edits on prompt one. Name the failure mode.", "**Approve-all-early.**"),
  ("Which command generates a starter CLAUDE.md?", "`/init`."),
  ("Claude commits and you did not read the diff. Name the failure mode.", "**Unreviewed commit.**"),
  ("How do you revert a bad uncommitted change?", "`git restore .` (or `git checkout`)."),
 ],
 steps=[("Pick a small repo and branch", "Branch"), ("Run orient and ask prompts", "Transcript"), ("Make one small change with tests", "Diff"),
        ("Annotate one read, one search, one edit and one command", "Four references"), ("Review the diff and commit or revert", "Result"), ("Run `/init` and read what it wrote", "CLAUDE.md")],
 pass_md=T("""
| Tool call | Line |
|---|---|
| Read | 4 |
| Grep | 6 |
| Edit | 12 |
| Bash (tests) | 15 |

The diff is under 30 lines on a branch.
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| 400-line diff on main | **Showpiece first session** and no branch |
"""),
 verdict="The artifact passes only if one tool call of each kind is annotated and the change was reviewed before commit.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Quickstart | The first-session sequence | Current |
| Claude Help Center | Your first day in Claude Code | Prompt choices, `/init` | Current |
""") + "\n\n*Disagreement named:* none found.",
 reframe="This is the craft of the first session: **small, clean, reviewed.** The engineer who understands this does not ask \"what impressive thing can I do first?\" — they ask \"which small change lets me see every tool call?\"",
))

# ---------------------------------------------------------------- 1.3.4 TRUST
SPECS.append(dict(
 mod=M, id="1.3.4", title="The trust dialog and what runs before you trust", short="The trust dialog and what runs before you trust",
 thesis="A cloned repository is untrusted input, and the trust dialog is the moment you decide whether to honour the configuration it carries.",
 prove="open an unfamiliar repo, read the trust dialog without accepting, and list what is held back.",
 discipline="read the dialog, and inspect .claude/ in repos you do not control.",
 counter="the dialog does not protect scripted runs: -p shows neither the trust prompt nor the MCP-server prompt [Claude Code docs, Security, 2026].",
 read_min=18, prove_h="2", depth=["Explain what trust does and when it applies", "Evaluate an unfamiliar repo before trusting it", "Set a policy for scripted runs on untrusted code"],
 deliverable="A review checklist for an unfamiliar repo and a test showing the home-directory trust behaviour.",
 sections=[
 dict(title="What trust is", framing="In an interactive session Claude Code shows the workspace trust dialog when you start in a folder you have not trusted. Until you accept, some content the repository supplies, such as project allow rules and marketplaces from `.claude/settings.json`, is held back [Claude Code docs, Security and Glossary, 2026].",
  body=T("""
| Fact | Detail |
|---|---|
| Scope | Acceptance saved per project directory |
| Home directory | Trust held for the current session only, not written to disk; prompt returns each launch |
| MCP servers | Servers in `.mcp.json` have their own approval prompt |
| Non-interactive `-p` | Shows neither prompt |

[Claude Code docs, Security, 2026]
"""),
  fm=[("Reflexive trust", "You accept every folder without reading, including a fresh clone whose `.claude/settings.json` registers a hook.", "Inspect `.claude/` and CLAUDE.md in unfamiliar repos before trusting, or use a disposable environment.")],
  xr="permissions are Module 1.2.3; the security model is Module 11.1.", one="trust means honouring someone else's configuration."),
 dict(title="Inspecting a repo before you trust it", framing="Treat the repo as data until you vouch for it. The files that matter are the ones Claude Code reads.",
  body=T("""
```bash
git clone <url> /tmp/inspect && cd /tmp/inspect
ls -la .claude CLAUDE.md AGENTS.md .mcp.json 2>/dev/null
cat .claude/settings.json 2>/dev/null          # hooks, permissions, marketplaces
cat .mcp.json 2>/dev/null                      # servers it would start
```

| Look for | Why |
|---|---|
| `hooks` in settings | They run shell commands |
| `permissions.allow` entries | Pre-approved actions |
| Marketplaces and plugins | Third-party code |
| `.mcp.json` servers | Processes and network access |
"""),
  fm=[("Unread-config trust", "You trust a repo whose settings define hooks or broad allow rules you never read.", "Read `.claude/settings.json` and `.mcp.json` before accepting, and decline if anything is unexplained.")],
  xr="hooks are Module 1.2.6; MCP is Module 5.5; plugins are Module 5.6.", one="read the config before you vouch for it."),
 dict(title="Home directory and the boundary", framing="Starting in your home directory means trust is not persisted, there is no setting to persist it, and the working-directory boundary covers all of home. Start from a project subdirectory instead [Claude Code docs, Security, 2026].",
  body=T("""
| Start in | Trust | Boundary |
|---|---|---|
| `~/projects/app` | Saved per directory | Project only |
| `~` | Session only | Everything in home |
"""),
  fm=[("Home-directory launch", "You start in home out of habit, the prompt reappears every time, and the boundary is far wider than the task needs.", "cd into the project before running `claude`.")],
  xr="boundaries are Module 1.2.3.", one="cd first, then claude."),
 dict(title="Scripted runs: no dialog", framing="Non-interactive `-p` sessions show neither the trust nor the MCP prompt, and the docs list what a repository's files can run there [Claude Code docs, Security, 2026]. In CI the protection must come from flags, managed settings and isolation, not a dialog.",
  body=T("""
| Control | Use |
|---|---|
| `--bare` | Start without hooks, skills, plugins, MCP, auto memory or CLAUDE.md; consistent CI runs [Claude Code docs, Glossary, 2026] |
| Explicit allowed tools | Limit what `-p` may use |
| Disposable environment | Containers for untrusted checkouts |
| No broad permissions | Never combine `-p` with bypass on unknown code |
"""),
  fm=[("Headless blind spot", "You assume the dialog protects scripted runs and run `-p` against an untrusted checkout with broad permissions.", "Control scripted runs with explicit flags, managed settings, `--bare` and isolated environments.")],
  xr="headless mode is Module 6.8; CI is Module 7.8; sandboxing is Module 4.4.", one="scripts get no dialog; add your own guard."),
 ],
 retrieval=[
  ("When does the trust dialog appear?", "In an interactive session started in a folder you have not trusted."),
  ("How long does trust last in the home directory?", "The current session only; the prompt returns each launch."),
  ("You accept every folder without reading. Name the failure mode by its exact label.", "**Reflexive trust.**"),
  ("Which files do you read before trusting an unfamiliar repo?", "`.claude/settings.json`, `.mcp.json`, CLAUDE.md and AGENTS.md."),
  ("You trust a repo with hooks you never read. Name the failure mode.", "**Unread-config trust.**"),
  ("Does `-p` show the trust dialog?", "No; it shows neither the trust nor the MCP prompt."),
  ("Name the failure mode of relying on the dialog in CI.", "**Headless blind spot.**"),
  ("What does `--bare` skip?", "Hooks, skills, custom commands, subagents, plugins, MCP servers, auto memory and CLAUDE.md."),
  ("You start in home each time. Name the failure mode.", "**Home-directory launch.**"),
 ],
 steps=[("Clone a repo you do not control into a scratch dir", "Clone"), ("Run the inspection commands and list risky entries", "Findings"),
        ("Start Claude Code there and read the dialog without accepting", "Observation"), ("Start in home and observe the trust behaviour twice", "Observation"),
        ("Run a `-p` command with `--bare` and compare with one without", "Two outputs"), ("Write a three-line untrusted-repo policy", "`policy.md`")],
 pass_md=T("""
| Item | Finding |
|---|---|
| Hooks | None; or listed with their commands |
| MCP servers | Two, reviewed |
| Decision | Trust after review, or decline |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Accepted without opening the config | **Reflexive trust** |
"""),
 verdict="The artifact passes only if the config files were read before any acceptance and the home-directory behaviour was observed.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Security | Trust verification, home-directory note, `-p` behaviour | Current |
| Anthropic | Permissions: what runs before you trust a folder | Content held back | Current; not fetched in full |
| Anthropic | Glossary: Project trust, Bare mode | Definitions | Current |
""") + "\n\n*Disagreement named:* a community mirror says the trust decision is persisted and revocable everywhere; the official Security page says the home directory is session-only. **The official page wins.**",
 reframe="This is the craft of trust: **vouch for configuration you have read, and add your own guards where there is no dialog.** The engineer who understands this does not ask \"can I click accept?\" — they ask \"what would this repo run if I did?\"",
))

# ---------------------------------------------------------------- 1.3.5 UPDATING
SPECS.append(dict(
 mod=M, id="1.3.5", title="Updating and version control", short="Updating and version control",
 thesis="Updates change behaviour and features are version-gated, so your version is part of every bug report and every runbook.",
 prove="show your version, update, read the release notes and name one behaviour that depends on a minimum version.",
 discipline="know your version and control how it changes.",
 counter="auto-update is a convenience for individuals and a hazard for teams.",
 read_min=15, prove_h="2", depth=["Check, update and read release notes", "Choose a channel or pin per team", "Run a fleet update policy"],
 deliverable="A version-policy note and a log of one update with release-note findings.",
 sections=[
 dict(title="Auto-update and manual update", framing="Native installs auto-update in the background; Homebrew and WinGet do not. Run `claude update` to apply an update immediately [Claude Code docs, Setup, 2026]. If already current, native installs report that Claude Code is up to date with the version; Homebrew, WinGet and apk installs report 'Claude is up to date!' [Claude Code docs, Installation, 2026].",
  body=T("""
| Task | Command |
|---|---|
| Show version | `claude --version` |
| Update now | `claude update` |
| Read what changed | `/release-notes` |
| Block all updates | `DISABLE_UPDATES` |
"""),
  fm=[("Stale package-manager install", "You installed with Homebrew or WinGet, assume it self-updates, and months later a documented feature is missing.", "Update on a schedule and compare `claude --version` with what the docs require.")],
  xr="install paths are Module 1.3.1; environment variables are Module 4.8.", one="check, then update, then read the notes."),
 dict(title="Channels and pinning", framing="The native installer accepts a specific version number or a release channel, latest or stable [Claude Code docs, Setup, 2026].",
  body=T("""
| Need | Choice |
|---|---|
| Newest features | `latest` |
| Fewer surprises | `stable` |
| Reproducibility | A pinned version |
| Locked fleet | Pin and set `DISABLE_UPDATES` |
"""),
  fm=[("Silent-update regression", "An auto-update changes a behaviour your team relied on and no one can say which version it started on.", "Record the version in bug reports, read `/release-notes`, and pin via stable or a version for fleets.")],
  xr="enterprise version control is in Part 11.", one="reproducibility needs a pin."),
 dict(title="Version-gated features", framing="Features have minimum versions, so documentation can be correct and still not apply to you. Examples from the docs: reading AGENTS.md directly needs v2.1.277 or later; `onFailure: \"block\"` for hooks needs v2.1.295; subagent concurrency override needs v2.1.217; spend-limit dialogs need v2.1.208; auto mode became the built-in starting mode from v2.1.283; `/powerup` arrived in v2.1.90 [Claude Code docs and community sources, 2026].",
  body=T("""
| Feature | Minimum version |
|---|---|
| `/powerup` | v2.1.90 (community sources; no official docs page found) |
| Spend-limit dialogs | v2.1.208 |
| Concurrency override | v2.1.217 |
| AGENTS.md direct read | v2.1.277 |
| Auto mode built-in start | v2.1.283 |
| Hook `onFailure: "block"` | v2.1.295 |
"""),
  fm=[("Version-blind doc use", "You follow a docs example on a version older than the feature and conclude it is broken.", "Check the minimum version in the docs and update before debugging.")],
  xr="troubleshooting is Module 1.3.7; settings are Module 4.1.", one="a feature note without a version is half a note."),
 dict(title="Release notes as a habit", framing="`/release-notes` shows what changed. A team habit of reading them after each update catches renamed features and changed defaults before they cause incidents.",
  body=T("""
| Step | When |
|---|---|
| Record `claude --version` | Before and after update |
| Read `/release-notes` | After update |
| Re-test your runbook's top three commands | After update |
"""),
  fm=[("Release-note skipping", "You never read the notes and learn a rename or default change from a failing script.", "Read `/release-notes` after each update and re-test the top three runbook commands.")],
  xr="the vocabulary and renames are Module 1.5.", one="read the notes after the update, not after the incident."),
 ],
 retrieval=[
  ("Which installs auto-update?", "Native installs; Homebrew and WinGet do not."),
  ("A feature you rely on stopped working after an auto-update. Name the failure mode by its exact label.", "**Silent-update regression.**"),
  ("What command applies an update immediately?", "`claude update`."),
  ("Which variable blocks all updates?", "`DISABLE_UPDATES`."),
  ("Your Homebrew install is months old. Name the failure mode.", "**Stale package-manager install.**"),
  ("Minimum version for reading AGENTS.md directly?", "v2.1.277."),
  ("A docs example fails on an old version. Name the failure mode.", "**Version-blind doc use.**"),
  ("Minimum version for hook onFailure block?", "v2.1.295."),
  ("What do you record in every bug report?", "The output of `claude --version`."),
 ],
 steps=[("Record your version", "Version"), ("Read `/release-notes`", "Three changes noted"), ("Update and record the new version", "Log"),
        ("Re-test three commands from your own workflow", "Results"), ("Find one feature in the docs with a minimum version and compare", "Comparison"), ("Write the version policy for a team", "`policy.md`")],
 pass_md=T("""
| Item | Value |
|---|---|
| Before | 2.1.xxx |
| After | 2.1.yyy |
| Notable change | One item from the notes |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| No version recorded | **Silent-update regression** unanswerable |
"""),
 verdict="The artifact passes only if before and after versions are recorded and at least one release-note item was re-tested.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Advanced setup: update | Update commands, channels, pinning | Current |
| Anthropic | Installation | Up-to-date messages per method | Current |
| Community | Posts on /powerup versions | When it shipped | Secondary |
""") + "\n\n*Disagreement named:* none found.",
 reframe="This is the craft of updating: **know the version, control the cadence, read the notes.** The engineer who understands this does not ask \"is it updated?\" — they ask \"which version is this, and what changed since the last one?\"",
))

# ---------------------------------------------------------------- 1.3.6 LEARNING IN PRODUCT
SPECS.append(dict(
 mod=M, id="1.3.6", title="Learning in-product: powerup, help, doctor", short="Learning in-product: powerup, help, doctor",
 thesis="The product teaches and diagnoses itself, which is faster than searching the web.",
 prove="use /help, /powerup, /doctor, /context and /memory once each and say what question each answers.",
 discipline="run the diagnostic before you search the web.",
 counter="the in-product lesson list is not stable; counts quoted online differ, so the product itself is the authority.",
 read_min=15, prove_h="1.5", depth=["Use the six in-product commands", "Choose the right command for a symptom", "Build a team onboarding path using them"],
 deliverable="A command-to-question table verified in a live session.",
 sections=[
 dict(title="Commands that answer questions", framing="Six commands cover most self-service: `/help`, `/powerup`, `claude doctor`, `/context`, `/memory` and `/release-notes`.",
  body=T("""
| Command | Answers |
|---|---|
| `/help` | What commands and shortcuts exist |
| `/powerup` | Guided interactive lessons |
| `claude doctor` or `/doctor` | Is my installation and configuration healthy |
| `/context` | What is in my context right now |
| `/memory` | Which CLAUDE.md and memory files loaded |
| `/release-notes` | What changed in this version |
"""),
  fm=[("Docs-first debugging", "You spend half an hour searching the web for a symptom that `claude doctor` would diagnose in seconds.", "Run `claude doctor` first, then search with the exact error string.")],
  xr="context inspection is Module 3.1; memory is Module 3.2.", one="ask the product before the internet."),
 dict(title="/powerup: what is verified and what is not", framing="`/powerup` opens short interactive lessons with animated demos inside the terminal. Community sources date it to v2.1.90, released 1 April 2026 [secondary: dev.to and community pages, 2026]. Sources disagree on the lesson count: some say 10 lessons, others 18, and one notes there is no dedicated Anthropic docs page or announcement [secondary, 2026].",
  body=T("""
| Claim | Status |
|---|---|
| Interactive lessons with animated demos | Consistent across sources |
| Introduced in v2.1.90 | Consistent across sources |
| 10 lessons | Reported by some sources |
| 18 lessons | Reported by others |
| Official docs page | Not found in this research |

Treat the lesson list as version-dependent: open `/powerup` and read it.
"""),
  fm=[("Lesson-count assumption", "You plan an onboarding around a specific number or list of lessons quoted online, and your version shows something different.", "Open `/powerup` in your version and build the plan from what it shows.")],
  xr="the Anthropic Academy courses are linked from the overview; feature modules are Part 5.", one="the menu in your terminal is the source of truth."),
 dict(title="Inspection commands in practice", framing="`/context` shows live usage by category with optimisation suggestions, and `/memory` shows which CLAUDE.md and auto-memory files loaded at startup [Claude Code docs, Context window, 2026].",
  body=T("""
| Symptom | First command |
|---|---|
| Answers getting worse in a long session | `/context` |
| Claude ignores a project rule | `/memory` |
| Command not found or odd behaviour after install | `claude doctor` |
| Something changed after an update | `/release-notes` |
"""),
  fm=[("Blind-session", "You keep working in a degraded session without looking at context or memory.", "Run `/context` at task boundaries and `/memory` whenever a rule seems ignored.")],
  xr="the context window is Module 3.1.", one="look before you theorise."),
 dict(title="Building an onboarding path", framing="For a team, a short path using in-product commands gives every member the same baseline.",
  body=T("""
| Day | Activity |
|---|---|
| 1 | Install, `claude doctor`, first session on a throwaway branch |
| 2 | `/powerup` lessons on context, plan mode and CLAUDE.md |
| 3 | `/init`, `/memory`, a scoped real task |
| 4 | `/context` habit, `/usage`, cost habits |
"""),
  fm=[("Onboarding-by-link", "New teammates get a list of links and no structured practice, so habits diverge.", "Give a 4-day path with verifiable outputs from the product itself.")],
  xr="cost habits are Module 1.4; first session is Module 1.3.3.", one="structure beats a link list."),
 ],
 retrieval=[
  ("Which command diagnoses installation and configuration?", "`claude doctor` or `/doctor`."),
  ("You search the web for an hour instead of running doctor. Name the failure mode by its exact label.", "**Docs-first debugging.**"),
  ("Which command shows what loaded from CLAUDE.md and memory?", "`/memory`."),
  ("Which version introduced /powerup according to community sources?", "v2.1.90."),
  ("You plan onboarding around 'the 10 lessons'. Name the failure mode.", "**Lesson-count assumption.**"),
  ("Do sources agree on the lesson count?", "No; some say 10 and others 18."),
  ("You never check context in a long session. Name the failure mode.", "**Blind-session.**"),
  ("What does /release-notes show?", "What changed in the current version."),
 ],
 steps=[("Run each of the six commands once", "Six outputs"), ("Write the question each answered", "Table"), ("Open /powerup and record the lessons shown in your version", "List"),
        ("Induce a PATH issue and use doctor to diagnose", "Log"), ("Write a four-day onboarding path", "Plan")],
 pass_md=T("""
| Command | Output captured |
|---|---|
| /context | Categories and counts |
| /memory | Loaded files |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Lesson list copied from a blog | **Lesson-count assumption** |
"""),
 verdict="The artifact passes only if the lesson list and every command output comes from your own session.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Community | /powerup guides (dev.to, claudefa.st and others) | Interactive lessons, v2.1.90 | Secondary |
| Anthropic | Context window and Setup pages | /context, /memory, doctor | Current |
""") + "\n\n*Disagreement named:* lesson counts of 10 versus 18 are reported by different community pages. **Your own `/powerup` menu wins.**",
 reframe="This is the craft of learning in-product: **diagnose with the tool, learn with the tool.** The engineer who understands this does not ask \"where is the tutorial?\" — they ask \"what does the product say about itself, right now?\"",
))

# ---------------------------------------------------------------- 1.3.7 TROUBLESHOOTING
SPECS.append(dict(
 mod=M, id="1.3.7", title="Troubleshooting install and login", short="Troubleshooting install and login",
 thesis="Most install and login failures fall into a handful of buckets, and each has an ordered check.",
 prove="reproduce a PATH failure and fix it with the ordered checks, ending with one binary.",
 discipline="match your exact error string, then check the binary, then PATH, then duplicates, before reinstalling anything.",
 counter="reinstalling is the slowest fix and often makes things worse by adding a second copy.",
 read_min=18, prove_h="2", depth=["Fix a PATH problem in order", "Diagnose login loops and duplicates", "Write a team troubleshooting runbook"],
 deliverable="A reproduced and fixed PATH failure with before-and-after output.",
 sections=[
 dict(title="Find your error", framing="The Troubleshoot install page is organised by error string. `command not found: claude` or `'claude' is not recognized` means the install directory is not on PATH; a PowerShell installer that finishes but shows no `claude` or an old version means restart the terminal and verify PATH [Claude Code docs, Troubleshoot install, 2026].",
  body=T("""
| Symptom | Likely cause | First action |
|---|---|---|
| `command not found: claude` | Not on PATH | Verify `~/.local/bin` on PATH; new terminal or `source ~/.zshrc` |
| `A parameter cannot be found that matches parameter name 'fsSL'` | Linux curl command in PowerShell | Use the PowerShell installer |
| Installer cannot download | Network, proxy or firewall | Check connectivity; set proxy variables |
| Crash or hang though `--version` prints | Corrupt or conflicting installs | `claude doctor`; list all copies |
| Old version | Multiple installs, legacy `~/.claude/local` | Keep one |

[Claude Code docs and Claude Help Center, 2026]
"""),
  fm=[("Guess-and-reinstall loop", "You reinstall repeatedly when the binary was fine and PATH was the problem, adding a second copy each time.", "Check the binary, then PATH, then `which -a claude`, before reinstalling.")],
  xr="install is Module 1.3.1; updating is Module 1.3.5.", one="match the string, then check in order."),
 dict(title="The PATH sequence", framing="Installers detect the PATH case and report it under Setup notes, for example that `~/.local/bin` is not in your PATH [Claude Code docs, Troubleshoot install, 2026].",
  body=T("""
```bash
ls -l ~/.local/bin/claude                          # 1. is the binary there?
echo "$PATH" | tr ':' '\\n' | grep -n 'local/bin'   # 2. is its folder on PATH?
export PATH="$HOME/.local/bin:$PATH"               # 3. fix now; persist in ~/.zshrc or ~/.bashrc
claude --version && which -a claude                # 4. confirm and list all copies
```

Three places a binary can come from: `~/.local/bin/claude` (native), `~/.claude/local/` (legacy local npm install) and the global npm list [Claude Code docs, Troubleshoot install, 2026].
"""),
  fm=[("Wrong-shell fix", "You fix PATH in one shell's profile while using another, so the fix never applies.", "Identify the shell with `echo $SHELL`, edit the matching profile and open a new terminal.")],
  xr="shell setup is general; environment variables are Module 4.8.", one="binary, PATH, copies, in that order."),
 dict(title="Login and authentication errors", framing="If you cannot sign in, see the login section of the troubleshooting page; first confirm which account `/login` shows, then check the environment for credentials that override it [Claude Code docs, Authentication and Troubleshoot install, 2026].",
  body=T("""
| Symptom | Check |
|---|---|
| Login loop | `/logout` then `/login`; clear stale credentials |
| Wrong account | `/login` to switch |
| Provider errors | Provider env vars set correctly; no browser login needed |
| Intermittent network | Wait a few minutes; the docs note failures are often temporary |
"""),
  fm=[("Cached-credential confusion", "A cached credential for another account keeps you in the wrong plan or provider.", "`/logout`, `/login` and confirm the active account.")],
  xr="sign-in is Module 1.3.2; Part 12 covers runtime troubleshooting.", one="log out cleanly before debugging further."),
 dict(title="Writing a team runbook", framing="Turn the table into a runbook so teammates fix common issues in minutes.",
  body=T("""
| Runbook line | Content |
|---|---|
| Symptom | Exact error string |
| First check | The one command to run |
| Fix | The smallest change |
| Escalate | Who to ask and what to attach (`claude --version`, doctor output) |
"""),
  fm=[("Runbook-by-memory", "Every incident is solved from memory by whoever is nearby and the knowledge never lands anywhere.", "Write the symptom, check, fix and escalation attachments and keep it in the repo.")],
  xr="incident handling is Part 12.", one="write the fix once."),
 ],
 retrieval=[
  ("State the ordered PATH checks.", "Binary exists, folder on PATH, list all copies with `which -a claude`, fix in the correct shell profile."),
  ("You reinstall repeatedly. Name the failure mode by its exact label.", "**Guess-and-reinstall loop.**"),
  ("What does the `fsSL` parameter error mean?", "You ran the Linux curl command in PowerShell."),
  ("You edit `.bashrc` but use zsh. Name the failure mode.", "**Wrong-shell fix.**"),
  ("Where might a legacy npm install live?", "`~/.claude/local/`."),
  ("A stale credential keeps you in the wrong account. Name the failure mode.", "**Cached-credential confusion.**"),
  ("Who solves incidents from memory? Name the failure mode.", "**Runbook-by-memory.**"),
  ("What two things attach to a bug report?", "`claude --version` and doctor output."),
 ],
 steps=[("Remove the install folder from PATH in one shell", "Setup"), ("Reproduce `command not found`", "Output"), ("Run the four ordered checks", "Log"),
        ("Fix it, persist in the right profile, open a new terminal", "Log"), ("Confirm one copy with `which -a claude`", "Output"), ("Write a four-line runbook entry", "Entry")],
 pass_md=T("""
| Step | Output |
|---|---|
| Before | command not found |
| After | version printed; one path |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Fixed by reinstalling | **Guess-and-reinstall loop** |
"""),
 verdict="The artifact passes only if the failure was reproduced and fixed with the four checks in order.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Troubleshoot installation and login | Error strings, PATH, duplicates | Current |
| Claude Help Center | Setup troubleshooting article | New-terminal and source fixes | Current |
""") + "\n\n*Disagreement named:* none found.",
 reframe="This is the craft of troubleshooting setup: **match the string, check in order, and never reinstall first.** The engineer who understands this does not ask \"how do I reinstall?\" — they ask \"which layer failed: binary, PATH, copies or credentials?\"",
))

if __name__ == "__main__":
    for s in SPECS:
        write(s)
