from specs_b4_common import *

M = "b-4-1"
SPECS = []
S = "Settings"

SPECS.append(mk(M, "4.1.1", "Scopes",
 thesis="A setting's scope is the file you save it in, and the file decides who it affects: only you, everyone in one folder, you in one project, or a whole organization.",
 prove="given any ten settings, place each in the correct file and say who it reaches, including what a teammate and a cloud session would see.",
 discipline="choose the scope before you write the key, not after it fails to apply.",
 counter="installing Claude Code creates no settings file at all; files appear only when you or an admin put them there, and the local file is written by Claude Code itself when you answer 'Yes, and don't ask again' [Claude Code docs, Settings files and precedence, 2026].",
 depth=["Name the four file scopes and what each reaches", "Choose the right file for a given setting and predict who sees it", "Design a team and organization layout including cloud and trust effects"],
 deliverable="A scope map: ten real settings, each placed in a file with the audience it reaches and the one thing that could stop it applying.",
 sections=[
 ("The four files and their audiences",
  "Claude Code reads JSON settings from four places and an organization can add managed delivery on top. The scope of a file is the set of people and projects a setting saved in it applies to [Claude Code docs, Settings files and precedence, 2026].",
  """
| Scope | File | Who it affects |
|---|---|---|
| User | `~/.claude/settings.json` | You, in every project on this machine |
| Shared project | `.claude/settings.json` | Everyone working in that folder; commit it |
| Project local | `.claude/settings.local.json` | You, in this one project only |
| Managed | `managed-settings.json` and other managed sources | Everyone the organization deploys it to |

On Windows `~/.claude` means `%USERPROFILE%\\.claude`; `CLAUDE_CONFIG_DIR` moves the home-directory files. A fifth file, `~/.claude.json`, is written by Claude Code for itself: account details, MCP server configuration, trust decisions and the global config keys `/config` writes [Claude Code docs, Settings files and precedence, 2026].
""",
  ("Wrong-file save", "You put a personal preference in the committed project file, so every teammate inherits it, or a team rule in your user file, so nobody else gets it.", "Ask who must be affected before choosing the file. Personal and everywhere: user. Team: shared project. Personal for one repo: local.", "A teammate complains about your editor mode appearing in their sessions after you committed it."),
  "the precedence order itself is Module 4.1 sub-topic 4.1.2; managed delivery is Module 4.2.", "the file is the audience."),
 ("Local settings: written by Claude Code, kept out of git",
  "Claude Code writes `.claude/settings.local.json` the first time you give a standing approval such as 'Yes, and don't ask again' for a Bash command. It then adds `**/.claude/settings.local.json` to your global git excludes, so the file stays out of commits [Claude Code docs, Settings files and precedence, 2026].",
  """
| Situation | Where the file lives |
|---|---|
| Start in a subdirectory of a git repo | The repository root (v2.1.211 and later) |
| Worktree | The main checkout's root |
| Outside a repo, repo root is home, Windows, or root/.git/.claude not owned by you | Stays with `.claude/settings.json` |
| You created the file by hand | You must add it to `.gitignore` yourself |

An untracked local file's allow rules apply without the trust step; if git tracks the file, trust applies to it too [Claude Code docs, Permissions, 2026].
""",
  ("Hand-made local file", "You create `settings.local.json` yourself and commit it by accident because Claude Code has not yet written to it and so has not excluded it.", "Add the file to `.gitignore` yourself, or let Claude Code create it through a first approval.", "A hand-created local settings file shows up in `git status` and gets committed."),
  "trust gating of allow rules is Module 4.2 (workspace trust); the rule format is Module 4.2.", "the local file is yours, but only Claude Code's own write keeps it out of git."),
 ("What scope does not reach: teammates, clones and cloud",
  "A scope reaches only the machines that have the file. A committed `.claude/settings.json` reaches teammates and a single-repository cloud session only if you commit it; user and local files are never read in cloud sessions [Claude Code docs, Settings files and precedence, 2026].",
  """
| Surface | Reads |
|---|---|
| Your machine (CLI, VS Code, JetBrains, desktop) | All four scopes |
| Teammate clone | Only what is committed |
| Cloud session, one repo | Committed `.claude/settings.json`; not user or local |
| Cloud, several repos (Anthropic-hosted) | Only `enabledPlugins` and `extraKnownMarketplaces` from each repo |
| Cloud threads in a project | None of the repo's permission rules, hooks or env |

Only server-managed settings reach a cloud session from the managed tier [Claude Code docs, Settings files and precedence, 2026].
""",
  ("Cloud blind spot", "You test a hook or permission in your user settings and assume a cloud session has it, but user and local files are not read there.", "Commit the key to the project file for single-repo cloud sessions, or set an environment variable on the cloud environment.", "A SessionStart hook in `~/.claude/settings.json` does nothing in a cloud session."),
  "cloud environments are Module 4.5.", "scope ends where the file stops being present."),
 ],
 extra_q=[("How many file scopes does Claude Code read, and which sets the audience for a team?", "Four: user, shared project, project local, managed. Shared project (`.claude/settings.json`) reaches the team when committed."),
          ("Which file does 'Yes, and don't ask again' write a Bash rule to?", "`.claude/settings.local.json`, at the git repository root from v2.1.211."),
          ("Which file holds account details, MCP server config and trust decisions?", "`~/.claude.json`, written by Claude Code itself."),
          ("From which version does a subdirectory start still save local rules at the repo root?", "v2.1.211 and later (before it, the starting directory).")],
 steps=[("List ten settings you use or want (theme, model, deny rules, hooks, env vars)", "A raw list"), ("Assign each to user, project, local or managed", "A scope column"),
        ("Name who each reaches: you, teammates, cloud", "An audience column"), ("Create a local file by approving one Bash command and check git status", "Observation"),
        ("Mark the one condition that could stop each applying (trust, cloud, higher level)", "A blocker column"), ("Run /status and match each loaded source to your map", "A verified map")],
 pass_md="""
| Setting | Scope | Reaches | Could stop it |
|---|---|---|---|
| `theme` | User | Me, all projects | Managed override |
| `permissions.deny` for `.env` | Shared project | Whole team once committed | Nothing (deny applies immediately) |
| My `model` for this repo | Local | Me, this repo | Managed or `--settings` |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Team deny rules placed in user file | **Wrong-file save**: teammates never get them |
| Cloud session assumed to see user hooks | **Cloud blind spot** |
""",
 verdict="Passes only if every setting has a scope, an audience that includes teammates and cloud, and a named blocker, and the map was checked with /status.",
 res=[("Anthropic", "Settings files and precedence", "Four scopes, file paths, who each affects, cloud behaviour"), ("Anthropic", "Permissions: Project allow rules and workspace trust", "Local file trust rules"), ("Anthropic", "All settings", "Scope label per key")],
 reframe="This is the craft of scope: **one key, one file, one audience.** The engineer who understands this never says 'it works on my machine' about a setting; they say which file it is in and who that file reaches.",
))

SPECS.append(mk(M, "4.1.2", "Precedence",
 thesis="When one key is set in several places, the highest level wins, lists merge instead of overriding, and managed settings sit above everything a user can touch.",
 prove="given a key set in four places, predict the winning value, and given two lists, predict the merged result.",
 discipline="before debugging a setting that does not apply, name every level that sets that key.",
 counter="a key at a lower level does not 'lose' when you add a list entry above it; for list keys such as permissions.allow the files combine, so a user allow rule survives next to a project one [Claude Code docs, Settings files and precedence, 2026].",
 depth=["State the five-level order and the list-merge rule", "Predict the winner for scalar keys and the union for lists", "Explain exceptions where a stricter lower-level value still counts"],
 deliverable="A precedence worksheet with six key scenarios (scalar, list, env pair, managed, --settings, security exception), each with predicted outcome and the file that supplied it.",
 sections=[
 ("The five levels",
  "Claude Code uses the value from the highest level that sets the key [Claude Code docs, Settings files and precedence, 2026].",
  """
| Rank | Level | Note |
|---|---|---|
| 1 | Managed | Beats user, project, local and `--settings` |
| 2 | Command line (`--settings`) | One session; below managed |
| 3 | Project local | Your personal project overrides |
| 4 | Shared project | Team's committed file |
| 5 | User | Your global defaults |

Environment variables are not a level: `ANTHROPIC_MODEL` beats the `model` key from any file, while `ANTHROPIC_DEFAULT_MODEL` applies only when no file sets `model`. Decided per pair [Claude Code docs, Settings files and precedence, 2026].
""",
  ("Env-var blind spot", "You change `model` in a settings file and nothing changes because `ANTHROPIC_MODEL` is exported in your shell.", "Check the key's pair on the env-vars reference; unset the variable or use `--model`.", "Your `model` edit has no effect and your shell exports ANTHROPIC_MODEL."),
  "scopes are Module 4.1.1; model precedence is Module 4.6.", "levels decide files; env vars decide per pair."),
 ("Lists merge, arrays of model lists do not",
  "Setting the same list key, such as `permissions.allow`, in more than one file combines the lists so each file can add entries without removing another's. Four model-related keys follow their own rules [Claude Code docs, Settings files and precedence, 2026].",
  """
| Key | Merge behaviour |
|---|---|
| `permissions.allow/ask/deny` | Union across files |
| `fallbackModel` | Whole value from highest file that sets it |
| `modelPicker` | Whole value from managed, `--settings` or user; ignored in project/local |
| `availableModels` | Managed list applied as-is; user/project/local entries ignored |
| `sandbox.filesystem` arrays | Merged across scopes |
Within the managed tier by default, `first-wins`: the highest-ranked source with a policy key is used and the rest ignored; `managedSourcesBehavior: merge` (v2.1.242+) combines them [Claude Code docs, Deploy managed settings, 2026].
""",
  ("Replace assumption", "You expect your project allow list to replace the user list, then are surprised an old user allow rule still fires.", "Treat list keys as unions; to remove an entry, delete it from the file that holds it.", "A user-level allow rule keeps approving a command your project file no longer lists."),
  "permission rules combine with deny first in Module 4.2; managed tier is 4.1.6.", "lists add up; scalars override."),
 ("Exceptions: stricter lower values that still count",
  "For a few security keys Claude Code honors a restrictive value from a scope that otherwise could not override managed settings [Claude Code docs, Settings files and precedence, 2026].",
  """
| Key | Honored from lower scope |
|---|---|
| `disableClaudeAiConnectors` | `true` from any scope |
| `permissions.blockReadsOutsideWorkingDirectories` | `true` from any scope (v2.1.257+) |
| `isolatePeerMachines` | `true` from any scope |
| `maxEffortLevel` | Lower cap from any scope (v2.1.267+); lowest applies |
| `remoteControlAtStartup` | `false` from project or local file |

Also `permissions.defaultMode` values `auto` and `bypassPermissions` do not take effect from project or local settings; use user or managed, or `--permission-mode`.
""",
  ("Project mode trap", "You commit `defaultMode: auto` or `bypassPermissions` in the project file and every session starts in Manual.", "Set those values in user or managed settings, or pass `--permission-mode` for one session.", "A committed `defaultMode: \"auto\"` is ignored."),
  "permission modes are Module 4.3.", "the exceptions only ever make things stricter."),
 ],
 extra_q=[("Which level is highest, which is lowest?", "Managed is highest; user is lowest. Between them: command line, project local, shared project."),
          ("`ANTHROPIC_DEFAULT_MODEL` and a `model` key are both set. Which applies?", "The `model` key; the default variable applies only when no file sets `model`."),
          ("From which version does `managedSourcesBehavior: merge` exist?", "v2.1.242."),
          ("Where does `--settings` rank and what size limit applies to its file?", "Above user, project and local, below managed; the file must be a regular file of at most 2 MiB.")],
 steps=[("Pick one scalar key and set it in user, project and local with different values", "Three values"), ("Predict the winner, then run /status and check", "Prediction vs result"),
        ("Add `--settings` with a fourth value and re-predict", "A fourth prediction"), ("Set permissions.allow differently in two files and list the merge", "A merged list"),
        ("Export ANTHROPIC_MODEL and observe against `model`", "Observation"), ("Write the rule you learned for each", "Six rules")],
 pass_md="""
| Scenario | Prediction | Result |
|---|---|---|
| `spinnerTipsEnabled`: user false, project true | project true | matched |
| `permissions.allow` user A, project B | A and B | matched |
| `--settings` true vs local false | true (this session) | matched |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| 'Project replaces user allow list' | **Replace assumption** |
| Ignored env var | **Env-var blind spot** |
""",
 verdict="Passes if each prediction was made before running the check and every mismatch is explained by a named level or exception.",
 res=[("Anthropic", "Settings files and precedence", "Order, list merging, exceptions table"), ("Anthropic", "Deploy managed settings", "Managed tier first-wins vs merge"), ("Anthropic", "Permission modes", "defaultMode restrictions")],
 reframe="This is the craft of precedence: **highest level wins, lists union, strict exceptions flow upward.** The engineer who understands this reads a surprising setting as a question about which levels set the key.",
))

SPECS.append(mk(M, "4.1.3", "Editing",
 thesis="You can change settings through /config, by editing JSON, per session on the command line, or by describing the change to /update-config; each has a different durability and a different failure.",
 prove="change one setting four ways and state, for each, where it was saved and when it takes effect.",
 discipline="pick the editing path by how long the change should last, not by what is closest to hand.",
 counter="settings files are strict JSON: a `//` comment or a trailing comma is a syntax error, and Claude Code reports a Settings Error at next start [Claude Code docs, Settings files and precedence, 2026].",
 depth=["Use /config, direct edit, --settings and /update-config appropriately", "Predict where each save lands and whether it persists", "Recover from a broken file and know which edits need a restart"],
 deliverable="A four-row log of the same change made four ways, each with save location, persistence and effect time.",
 sections=[
 ("Interactive paths: /config and /update-config",
  "`/config` opens the Settings interface; passing `key=value` sets a value directly, such as `/config verbose=true` or `/config thinking=false`. `/update-config [request]` is a bundled skill: you describe the change and Claude edits the matching settings.json file; for options such as theme and model, use `/config` [Claude Code docs, Commands, 2026].",
  """
| Option saved from /config | Lands in |
|---|---|
| Most options (theme, editor mode) | `~/.claude/settings.json` |
| A few, such as Show tips | `.claude/settings.local.json` |
| Global config options | `~/.claude.json` |

`/config` is part of the terminal interface; the VS Code chat panel and desktop app do not open it. In a cloud session in the browser it opens your claude.ai settings page instead of changing a value [Claude Code docs, Settings files and precedence, 2026].
""",
  ("Wrong-surface /config", "You run /config in VS Code or a cloud session expecting it to change a value, and nothing is saved.", "Edit the settings file directly, or in cloud set an environment variable on the environment.", "You typed /config in the VS Code panel and no menu opened."),
  "scopes are Module 4.1.1.", "/config saves for you; /update-config edits for you."),
 ("Direct edits and when they take effect",
  "Open the file for the scope you want and add the key. Add `$schema` for editor validation. Claude Code watches the files and reloads most edits without restart, including `permissions`, `hooks` and credential helpers such as `apiKeyHelper` [Claude Code docs, Settings files and precedence, 2026].",
  """
```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": { "allow": ["Bash(npm run lint)"], "deny": ["Read(./.env)"] }
}
```

| Fails as | Cause |
|---|---|
| Settings Error dialog | Invalid JSON or schema-rejected value in user/project/local file |
| Settings Warning | Single bad entry; Claude Code skips it and keeps the rest |
| Configuration error | `~/.claude.json` unparseable; copied to `~/.claude/backups/.claude.json.corrupted.<timestamp>` |

The ConfigChange hook runs for each file change but not for MDM or console-delivered managed settings.
""",
  ("Comment in JSON", "You add a `//` comment or a trailing comma to settings.json and the whole file fails to load.", "Remove it, then run /status and claude doctor to confirm what loaded and what was dropped.", "A commented settings.json produces a Settings Error at startup."),
  "diagnostics are sub-topic 4.1.5; hooks are Module 5.4.", "strict JSON; reload is automatic for most keys."),
 ("One-session changes and the lasting ones",
  "To try a value without saving it: `--settings` with inline JSON or a file, a per-key flag such as `--model` or `--effort`, or the paired environment variable [Claude Code docs, Settings files and precedence, 2026].",
  """
| Method | Persists? | Notes |
|---|---|---|
| `claude --settings '{"model":"claude-opus-5-5"}'` | No | Above user/project/local, below managed; cannot set Managed or Global config keys |
| `/model` Enter | Yes | Saved to `model` in user settings |
| `/model` then `s` | No | Session only |
| `/effort` Enter vs `s` | Yes vs no | `s` needs v2.1.257+ |
| `/config key=value` | Yes | Written to the matching file |

If you cannot write `~/.claude/settings.json` (generated or read-only), a saved choice applies only to the current session.
""",
  ("Silent session-only", "You switch model with `s` or a flag and assume it is your new default, then the next session starts on the old model.", "Use Enter in the picker or edit the file for a lasting default.", "Your model choice reverts the next day."),
  "model and effort choices are Module 4.6.", "decide persistence first, then the tool."),
 ],
 extra_q=[("What are the three save locations for /config options?", "`~/.claude/settings.json`, `.claude/settings.local.json`, and `~/.claude.json`."),
          ("What size limit applies to a `--settings` file?", "2 MiB, and it must be a regular file."),
          ("How many recent backups of ~/.claude.json does Claude Code keep for recovery?", "Five most recent `.claude.json.backup.<timestamp>` files in `~/.claude/backups/`."),
          ("Which command do you describe a settings change to in plain language?", "`/update-config [request]`, a bundled skill.")],
 steps=[("Change theme via /config and note the file", "Location"), ("Change a permission rule by editing JSON; confirm reload without restart", "Observation"),
        ("Start a session with --settings to change one value", "Observation"), ("Ask /update-config for a hook or env var", "A diff"),
        ("Introduce a trailing comma and observe the dialog, then fix", "Dialog and fix"), ("Tabulate persistence per path", "Table")],
 pass_md="""
| Path | Saved to | Persists | Effect |
|---|---|---|---|
| /config theme | user file | yes | immediate |
| --settings model | nowhere | no | this session |
| Edit allow rule | project file | yes | reload on save |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Used `s` and called it default | **Silent session-only** |
| Settings file with comments | **Comment in JSON** |
""",
 verdict="Passes if all four paths were executed once, each with observed location and persistence, and the broken-file recovery was shown.",
 res=[("Anthropic", "Settings files and precedence: Change a setting", "Paths, reload, error types"), ("Anthropic", "Commands", "/config, /update-config definitions"), ("Anthropic", "All settings", "$schema and key entries")],
 reframe="This is the craft of editing: **choose the path by lifetime.** The engineer who understands this knows, before pressing Enter, whether the change will exist tomorrow.",
))

SPECS.append(mk(M, "4.1.4", "Reference pages",
 thesis="Four pages answer different questions: the settings-files page explains precedence, the all-settings page is the key index, the example-settings page shows realistic files, and the managed-settings page covers deployment.",
 prove="given a settings question, name the one page that answers it and the section within it.",
 discipline="look a key up in the reference before you guess its scope, type or default.",
 counter="the all-settings page marks keys that never apply from the shared project file; a key can be valid JSON, schema-clean and still silently inert in the place you put it [Claude Code docs, Settings files and precedence, 2026].",
 depth=["Locate the right reference page for a question", "Read a key entry: scope, type, default, overrides", "Spot keys that need user or managed scope"],
 deliverable="A lookup card of eight questions mapped to a page and section, with the answer retrieved.",
 thin="This sub-topic is a navigation skill; the material is a map of four pages rather than a mechanism, so the guide stays short on mechanism and long on lookup practice.",
 sections=[
 ("Which page answers which question",
  "The docs split settings knowledge four ways. The settings page opens with a tip pointing to All settings for any single key [Claude Code docs, Settings files and precedence, 2026].",
  """
| Question | Page |
|---|---|
| Which file? Who wins? Why ignored? | Settings files and precedence |
| Type, default, scope, per-session overrides of one key | All settings (settings reference) |
| What do a real developer, team and organization file look like? | Example settings files |
| How do I deliver policy to every machine? | Deploy managed settings |
| What does allow/ask/deny syntax look like? | Configure permissions |

The reference lists the scope labels User, Project, Local, Managed, Any file and Global config (`~/.claude.json`) [Claude Code docs, All settings, 2026].
""",
  ("Page roulette", "You read the permissions page to learn why a `model` key is ignored, and the answer is on a different page.", "Route by question type using the table, then read only that section.", "You spent an hour on the wrong page for a precedence question."),
  "managed delivery is sub-topic 4.1.6; permissions syntax is Module 4.2.", "route by question, not by keyword."),
 ("Reading a key entry",
  "Each entry in All settings gives the file you set it in, the type, the default and an example, plus per-session overrides and which one wins [Claude Code docs, Settings files and precedence, 2026].",
  """
| Field | Example: `effortLevel` |
|---|---|
| Type | `"low"`, `"medium"`, `"high"`, `"xhigh"` |
| Default | unset |
| Override | `--effort` for one session; `CLAUDE_CODE_EFFORT_LEVEL` overrides both |
| Note | In user settings applies to Opus 5 and earlier; in project/local/managed/`--settings` applies to every model |

Other examples: `availableModels` default unset (all allowed); `fallbackModel` keeps at most three distinct allowed models; `alwaysThinkingEnabled` false turns thinking off [Claude Code docs, All settings, 2026].
""",
  ("Default guessing", "You assume a key's default instead of reading it, such as expecting thinking off or effort low.", "Open the key's entry and read Default before changing it.", "You set a key to its existing default and see no change."),
  "model keys are Module 4.6.", "defaults live in the entry, not in memory."),
 ("The example files and the index",
  "The example page shows three commented files: a personal file, a team's shared settings and an organization's managed file [Claude Code docs, Settings files and precedence, 2026]. The all-settings index tells you per key whether it applies from the shared file.",
  """
| Scope column says | Meaning |
|---|---|
| `User, local, or managed` | Never applies from the shared project file (a few can be switched off there) |
| `Managed` | Only a managed source honors it |
| `Global config` | Only `~/.claude.json` |
| `Any file` | All four files |

The published JSON schema can lag the newest CLI, so a validation warning on a recently documented key does not mean your config is invalid.
""",
  ("Schema trust", "You delete a valid new key because the editor's schema flags it as unknown.", "Check the key on the settings reference before removing it; run claude doctor for real rejection.", "The editor underlines a documented key and you remove it."),
  "diagnostics are sub-topic 4.1.5.", "the schema lags; the reference leads."),
 ],
 extra_q=[("Which scope label means the key applies only from `~/.claude.json`?", "Global config."),
          ("What file size limit applies to `--settings` per the CLI reference?", "2 MiB."),
          ("How many distinct allowed models does `fallbackModel` keep at most?", "Three."),
          ("Which page lists every key with default and example?", "All settings (settings reference).")],
 steps=[("Write eight settings questions you have had", "Question list"), ("Map each to one of the four pages", "Page column"),
        ("Retrieve each answer and record the section anchor", "Anchor column"), ("Find three keys whose scope is not Any file", "Three keys"),
        ("Read one key's override line and test it", "Test result"), ("Note one place the schema lags", "Observation")],
 pass_md="""
| Question | Page | Answer |
|---|---|---|
| Why is my `model` ignored | Settings precedence | `ANTHROPIC_MODEL` set |
| Default of `availableModels` | All settings | unset, all allowed |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Answers without page citations | **Page roulette** |
| Assumed default | **Default guessing** |
""",
 verdict="Passes if every question has a page, a section and a retrieved answer, and three non-Any-file keys are identified.",
 res=[("Anthropic", "Settings files and precedence", "The navigation tips and the scope model"), ("Anthropic", "All settings", "Per-key entries and scope index"), ("Anthropic", "Example settings files", "Developer, team and organization files [not retrieved in full]")],
 reframe="This is the craft of looking things up: **know which page owns which question.** The engineer who understands this stops memorising keys and starts retrieving them.",
 read_min=15, prove_h="1",
))

SPECS.append(mk(M, "4.1.5", "Checking what is in force",
 thesis="Three tools answer 'what is actually loaded': /status names the loaded sources, claude doctor lists what was rejected, and --safe-mode proves whether customization is the cause.",
 prove="given a setting that does not apply, run the right three checks in order and name the cause.",
 discipline="verify what loaded before changing what you wrote.",
 counter="/status shows which files were read, not which file supplied each key; the Config tab is not a view of your settings.json contents [Claude Code docs, Settings files and precedence, 2026].",
 depth=["Use /status, claude doctor and --safe-mode", "Interpret Setting sources and Organization policy lines", "Distinguish a dropped entry from a lower-priority one"],
 deliverable="A diagnostic transcript for one deliberately broken setting, with each tool's finding and the fix.",
 sections=[
 ("/status: which sources loaded",
  "Run /status; the Status tab's `Setting sources` line lists each settings file loaded this session, such as `User settings` or `Project local settings`. With managed settings active, the managed entry shows in parentheses how they reached the machine [Claude Code docs, Settings files and precedence, 2026].",
  """
| You see | It means |
|---|---|
| `User settings`, `Project local settings` | Those files loaded |
| Managed entry with delivery in parentheses | Which managed source won |
| Different managed source than admin changed | A higher-priority source applies |
| `Organization policy` line (v2.1.261+, in `claude doctor`; in /status only when policy did not load) | Where policy loaded from or why not |

By default the highest-ranked managed source wins and others are skipped silently; /status names the source used and those skipped [Claude Code docs, Deploy managed settings, 2026].
""",
  ("Source-for-key confusion", "You read Setting sources and conclude which file set a key, but the line only says files loaded.", "Check each loaded file's contents and the precedence order to find the winner.", "You blame the wrong file after reading Setting sources."),
  "precedence is sub-topic 4.1.2; managed combining is 4.1.6.", "/status lists files, not winners."),
 ("claude doctor: what was dropped",
  "`claude doctor` prints read-only diagnostics without starting a session: install health, settings validation errors and Remote Control eligibility. After a `-p` run that ignores a setting, run it to see what was dropped [Claude Code docs, CLI reference, 2026].",
  """
| Symptom | Likely `claude doctor` finding |
|---|---|
| `mcp__` rule with parentheses in settings | Skipped rule listed |
| Bad permission rule | Settings Warning: entry skipped, file kept |
| Invalid JSON | Settings Error: file skipped |
| IPv6 entry unbracketed | `Sandbox network domain entries have unreliable spellings` |
| Managed entry invalid | Dropped; some keys fall back to stricter values |

`/doctor` (in-session skill) additionally proposes fixes that Claude applies after you confirm.
""",
  ("Print-mode blindness", "A `-p` run shows no dialog, so you never see the broken entry that was silently skipped.", "Run `claude doctor` after any headless run that ignored a setting.", "A CI run ignores your rule and no error appears."),
  "headless flags are Module 4.8.", "no dialog does not mean no problem."),
 ("--safe-mode and the clean test",
  "`--safe-mode` starts with all customizations disabled: CLAUDE.md, skills, plugins, hooks, MCP servers, custom commands and agents, output styles, workflows, custom themes, custom keybindings, status line and file-suggestion commands, LSP servers and auto memory. Authentication, model selection, built-in tools and permissions still work [Claude Code docs, CLI reference, 2026].",
  """
| Test | Reading |
|---|---|
| Symptom gone in --safe-mode | A customization causes it; bisect |
| Symptom remains | Core, auth, permission or managed policy |
| Compare with `--bare` | `--bare` skips discovery for speed; safe mode is for debugging |

Permissions keep working in safe mode, so an over-restrictive rule will still reproduce.
""",
  ("Bisect by hunch", "You disable hooks, then plugins, then MCP one at a time by memory instead of using --safe-mode first.", "Run --safe-mode first; if the symptom disappears, re-enable one category at a time.", "You spend an afternoon toggling categories one by one."),
  "plugins are Module 7; hooks are Module 5.4.", "prove whether customization is the cause first."),
 ],
 extra_q=[("What does the `Setting sources` line show and not show?", "Which files loaded; not which file supplied each key."),
          ("Name a version that added the `Organization policy` line to `claude doctor`.", "v2.1.261."),
          ("Which still work in --safe-mode: permissions or hooks?", "Permissions work; hooks do not load."),
          ("How many recent .claude.json backups exist for recovery?", "Five.")],
 steps=[("Introduce a bad permission rule and a trailing comma in separate files", "Two faults"), ("Start Claude and screenshot the dialogs", "Dialogs"),
        ("Run /status; record sources", "Sources"), ("Run claude doctor; record dropped entries", "Findings"),
        ("Run with --safe-mode and compare", "Comparison"), ("Fix both faults and re-verify", "Clean run")],
 pass_md="""
| Tool | Finding | Action |
|---|---|---|
| /status | User and Project local loaded | n/a |
| claude doctor | Entry `Bash(` malformed, skipped | Fix syntax |
| --safe-mode | Hook not loaded; symptom gone | Bisect hooks |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Concluded key winner from Setting sources | **Source-for-key confusion** |
| Ignored headless failure | **Print-mode blindness** |
""",
 verdict="Passes if the three tools were used in order and each finding is tied to a specific fix that was verified.",
 res=[("Anthropic", "Settings files and precedence: Confirm what loaded", "/status and doctor roles"), ("Anthropic", "CLI reference", "--safe-mode and claude doctor"), ("Anthropic", "Deploy managed settings: Check that a policy is in force", "Managed source reading")],
 reframe="This is the craft of verification: **loaded, rejected, isolated.** The engineer who understands this never edits a file twice before checking /status once.",
))

SPECS.append(mk(M, "4.1.6", "Plugin-only and strict lockdowns",
 thesis="Managed-only keys let an organization restrict where customization may come from, but each key is a lock on a surface, not a general kill switch, and delivery rules decide whether it even applies.",
 prove="given a policy goal, choose the managed keys, deliver them, and state what a developer can still do.",
 discipline="state the surface you are locking before you pick the key.",
 counter="a managed `model` is only a starting default; `--model` and `ANTHROPIC_MODEL` still pick a model, so the lock is `availableModels` and `deniedModels` [Claude Code docs, Deploy managed settings, 2026].",
 depth=["Name the managed-only lock keys and the surface each governs", "Choose delivery and predict how multiple managed sources combine", "Identify what developers can still change"],
 deliverable="A policy plan: three goals, the keys that enforce them, the delivery mechanism, and what remains developer-controlled.",
 sections=[
 ("Managed-only keys are locks",
  "Claude Code reads a set of keys only from a managed source; in user or project files they have no effect. Most are locks: the governed value (permission rules, `sandbox.network.allowedDomains`) is an ordinary key any level can set, and the lock tells Claude Code to honor only the managed value [Claude Code docs, Deploy managed settings, 2026].",
  """
| Key | What it locks |
|---|---|
| `strictPluginOnlyCustomization` | Skills, agents, hooks, MCP from user and project sources; `true` locks all four, an array names which (`.agents`, `.hooks`, `.mcp`, `.skills`) |
| `strictKnownMarketplaces` / `blockedMarketplaces` | Which marketplace sources users may add |
| `allowManagedHooksOnly` | Which hooks run |
| `allowManagedPermissionRulesOnly` | Permission rules only from managed |
| `allowManagedMcpServersOnly` | Only managed `allowedMcpServers` respected; `deniedMcpServers` still merges |
| `disableSideloadFlags` | Rejects `--plugin-dir`, `--plugin-url`, `--agents`, `--mcp-config` (v2.1.193+) |
| `disableCommandPluginSources` | Blocks `command` plugin sources (v2.1.229+) |
""",
  ("Lock-less policy", "You deploy `permissions.deny` but not the lock, so users still add their own allow rules beside it.", "Add `allowManagedPermissionRulesOnly` when only managed rules should count; remember deny always wins anyway.", "A user adds allow rules next to your managed ones and you did not expect it."),
  "permission rules are Module 4.2; plugins are covered in the plugin modules.", "a lock governs one surface."),
 ("Delivery and combining managed sources",
  "A managed settings file, MDM profile or claude.ai console applies one policy to everyone it reaches. When several deliver to one machine, the default `first-wins` uses the highest-ranked source with at least one policy key and ignores the rest [Claude Code docs, Deploy managed settings, 2026].",
  """
| Rank | Source | Read |
|---|---|---|
| 1 | Server-managed (claude.ai console or gateway) | Fetched at startup, polled hourly |
| 2 | MDM/OS policy (macOS plist, HKLM) | Read at startup, checked every 30 minutes |
| 3 | `managed-settings.json` + `managed-settings.d/*.json` | Reloaded on file change |
| 4 | HKCU registry | Only when no admin document above it |

File paths: `/Library/Application Support/ClaudeCode/` (macOS), `/etc/claude-code/` (Linux, WSL), `C:\\Program Files\\ClaudeCode\\` (Windows). Drop-ins merge alphabetically; later single values win, lists union.
""",
  ("Shadowed source", "You change the managed file but the console already delivers a policy, so first-wins ignores the file with no warning.", "Run /status to see which source is used and skipped; set `managedSourcesBehavior: merge` (v2.1.242+) if you want all composed.", "Your managed file edit has no effect."),
  "precedence is sub-topic 4.1.2.", "ranking decides which source speaks."),
 ("What a developer can still change",
  "Managed settings bind Claude Code only and not the developer's other tools; some items sit outside the lock [Claude Code docs, Deploy managed settings, 2026].",
  """
| Still possible | Why |
|---|---|
| Pick a model with `--model` / `ANTHROPIC_MODEL` | Managed `model` is a default; use `availableModels`/`deniedModels` |
| Edit the managed file as local admin | MDM can redeploy on a schedule |
| Edit server-managed cache | Lasts until next successful fetch |
| Call the API from another tool | Settings bind Claude Code only |
| Cloud sessions | Device files do not reach them; only server-managed does |

`forceRemoteSettingsRefresh` blocks CLI startup until remote settings are freshly fetched and exits if fetch fails (fail-closed). `requiredMinimumVersion` blocks an outdated binary but does not end a running session.
""",
  ("Lock overconfidence", "You report the model as locked because you set a managed `model`, then a developer runs `--model` and uses another.", "Deploy `availableModels` (and `deniedModels`, v2.1.283+) for a real lock.", "A developer uses a different model after your managed `model` default."),
  "models are Module 4.6; cloud is Module 4.5.", "a default is not a lock."),
 ],
 extra_q=[("Which values may `strictPluginOnlyCustomization` take, and how many surfaces does `true` lock?", "`true` or an array naming surfaces; true locks all four (skills, agents, hooks, MCP)."),
          ("How often are MDM policies checked for changes, and server-managed polled?", "MDM every 30 minutes; server-managed polled hourly."),
          ("From which version does `deniedModels` exist?", "v2.1.283."),
          ("Where does Linux read managed-settings.json?", "`/etc/claude-code/`.")],
 steps=[("Write three policy goals (e.g. no user hooks, only approved marketplaces, no sideload)", "Goals"), ("Map each to a key", "Key column"),
        ("Choose delivery and predict the winning source", "Delivery plan"), ("Draft the managed-settings.json", "JSON"),
        ("List what a developer can still do", "Residual list"), ("Plan verification with /status and claude doctor", "Check plan")],
 pass_md="""
| Goal | Key | Delivery | Residual |
|---|---|---|---|
| No user hooks | `allowManagedHooksOnly: true` | MDM | local admin can edit file |
| Approved marketplaces | `strictKnownMarketplaces` | server-managed | none for users |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Set managed `model` as a lock | **Lock overconfidence** |
| Edited file under an active console policy | **Shadowed source** |
""",
 verdict="Passes if every goal maps to a lock key, the winning source is predicted, and residual developer powers are listed.",
 res=[("Anthropic", "Deploy managed settings", "Managed-only keys, delivery, combining"), ("Anthropic", "All settings: Strict plugin lockdowns", "strictPluginOnlyCustomization and marketplaces keys"), ("Anthropic", "Settings files and precedence", "Exceptions table")],
 reframe="This is the craft of lockdown: **a key per surface, a source per machine.** The engineer who understands this can say exactly what an organization has fixed and what it has merely suggested.",
))

if __name__ == "__main__":
    run(SPECS)
