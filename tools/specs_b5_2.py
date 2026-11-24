from specs_b5_common import *
M = "b-5-2"
SPECS = []
SK = "Claude Code docs, Skills"
def R(extra=None, dis="none found between the sources read."):
    rows = [("Anthropic", "Skills (Claude Code)", "Frontmatter, locations, invocation, lifecycle, troubleshooting", "Current; read in two fetches covering the page, though the fetch tool summarised rather than quoted some sections"),
            ("Anthropic", "Commands", "Bundled skills and management commands", "Current")]
    return res(rows + (extra or []), dis)

# ---------------------------------------------------------------- 5.2.1
SPECS.append(guide(M, "5.2.1", "What a skill is",
 thesis="A skill is a directory with a SKILL.md file whose body enters context only when used, and slash commands are now part of the same system.",
 prove="create a skill, run it by name and by automatic match, and show the same procedure no longer needs pasting.",
 discipline="create a skill when you keep pasting the same instructions or a CLAUDE.md section has grown into a procedure.",
 counter="a skill is not loaded at session start: its description is, and its body only when used, which is what separates it from CLAUDE.md [Claude Code docs, Skills, 2026].",
 read_min=20, prove_h="1.5",
 depth=["Describe the anatomy of a skill and how it loads", "Create and test a personal skill end to end", "Migrate a command file and a CLAUDE.md procedure into skills"],
 deliverable="A working personal skill, plus a transcript of it running by slash name and by automatic loading.",
 sections=[
  sec("Anatomy", "A skill is a directory containing a `SKILL.md` file. The file has two parts: YAML frontmatter between `---` markers and markdown instructions; the frontmatter `description` helps Claude decide when to load the skill [Claude Code docs, Skills, 2026].",
   """
```text
~/.claude/skills/summarize-changes/
  SKILL.md        <- frontmatter + instructions
```

```yaml
---
description: Summarizes uncommitted changes and flags anything risky. Use when the user asks what changed, wants a commit message, or asks to review their diff.
---

## Current changes

!`git diff HEAD`

## Instructions
Summarize the changes above in two or three bullet points...
```
[Claude Code docs, Skills, 2026; example abridged]

The `!` line is dynamic context injection: Claude Code runs the command and inlines its output before Claude sees the skill.
""",
   ("Body-in-description", "The whole procedure is crammed into the `description` line, which is truncated in the listing, so the real steps are cut or never load.", "Keep the description to what and when; put the procedure in the body."),
   "the folder and location rules are sub-topic 5.2.2; frontmatter is sub-topic 5.2.3.", "a skill is a folder with SKILL.md; description decides loading, body does the work."),
  sec("Commands became skills", "Custom commands have been merged into skills: `.claude/commands/deploy.md` and `.claude/skills/deploy/SKILL.md` both create `/deploy`, existing command files keep working, and skills add a directory for supporting files, frontmatter controlling invocation, and automatic loading [Claude Code docs, Skills, 2026]. If a skill and a command file share a name, the skill wins [Claude Code docs, Skills, 2026].",
   """
| Old | New | Difference |
|---|---|---|
| `.claude/commands/deploy.md` | `.claude/skills/deploy/SKILL.md` | Skill adds supporting files, invocation control, auto-loading |
| Typing the command | Typing `/deploy` or letting Claude match | Both work for skills |

The Agent Skills open standard underlies this; Claude Code extends it with invocation control, subagent execution and dynamic context injection [Claude Code docs, Skills, 2026].
""",
   ("Command-file inertia", "You keep adding commands as flat files and never gain supporting files or invocation control, then wonder why Claude never picks them up on its own.", "Move the command into a skill directory and add a description Claude can match."),
   "the bundled list is sub-topic 5.2.8.", "slash commands are skills with fewer features."),
  sec("Body loads only when used", "Unlike CLAUDE.md content, a skill's body loads only when used. Once invoked, its rendered SKILL.md enters the conversation as one message and stays across later turns; Claude Code does not re-read the file, so the docs advise standing instructions rather than one-time steps [Claude Code docs, Skills, 2026].",
   """
| Moment | In context |
|---|---|
| Session start | Name and description |
| Invoked (by you or Claude) | Full rendered body, as one message |
| Later turns | Same message; file not re-read |
| After auto-compaction | First 5,000 tokens of each recent skill, within a combined 25,000 |

[Claude Code docs, Skills, 2026]
""",
   ("One-time-step wording", "A skill says 'run the tests' once, in a step list, and Claude treats it as a single action, not a rule for the rest of the session.", "Write standing instructions such as 'run the tests after every edit' when the rule should persist."),
   "compaction detail is sub-topic 5.2.12; context cost is sub-topic 5.1.8.", "a skill is invoked once and then lives in the conversation."),
 ],
 retrieval=[
  ("What file must a skill directory contain?", "`SKILL.md`."),
  ("When does a skill's body load, in contrast to CLAUDE.md?", "Only when used."),
  ("You put the whole procedure in the description line. Name the failure mode by its exact label.", "**Body-in-description.**"),
  ("Which wins when a skill and a command file share a name?", "The skill."),
  ("Name the failure mode of keeping flat command files and never gaining automatic loading.", "**Command-file inertia.**"),
  ("After auto-compaction, how many tokens of each skill are kept, and what is the combined budget?", "The first 5,000 tokens of each; 25,000 combined."),
  ("A skill says 'run the tests' once and Claude treats it as one action. Name the failure mode by its exact label.", "**One-time-step wording.**"),
  ("What does the `!` syntax in a skill body do?", "Runs the shell command and inlines its output before Claude sees the skill."),
  ("How many frontmatter fields are allowed outside Claude Code?", "Six: name, description, license, compatibility, metadata, allowed-tools."),
  ("What open standard do skills follow?", "Agent Skills (agentskills.io)."),
 ],
 steps=[("Pick a procedure you pasted at least twice", "Procedure text"), ("Create `~/.claude/skills/<name>/SKILL.md`", "File"), ("Write what-and-when description", "Description"), ("Run it with `/<name>`", "Transcript A"),
        ("Ask for the task in plain words and see if it loads", "Transcript B"), ("Edit the wording to standing instructions and rerun", "Revised file")],
 pass_md="""
| Check | Result |
|---|---|
| `/summarize-changes` runs | Yes |
| Plain-language request loads it | Yes, description matched |
| Body is standing instructions | Yes |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Steps in `description` | **Body-in-description** |
| Only slash-invocation tested | Auto-loading unproven |
""",
 verdict="The artifact passes only if the skill ran both by slash name and by automatic match.",
 resources=R(),
 reframe="This is the craft of the skill: **a folder, a description that routes, a body that works.** The engineer who understands this does not ask \"where do I paste this?\" — they ask \"is this a procedure worth a folder?\"",
))

# ---------------------------------------------------------------- 5.2.2
SPECS.append(guide(M, "5.2.2", "Where skills live",
 thesis="A skill's location decides who gets it and which copy wins when names clash, so placement is a sharing and priority decision.",
 prove="place the same skill name at two levels, predict the winner from the priority rules, and confirm it.",
 discipline="choose the location by audience first (you, this repo, everyone) and name by uniqueness second.",
 counter="project skills do not override personal ones: the order is enterprise over personal over project [Claude Code docs, Skills, 2026].",
 read_min=20, prove_h="1.5",
 depth=["List the levels and their paths", "Predict a same-name clash outcome", "Choose placement for a team rollout"],
 deliverable="A placement table for five of your skills with level, path and clash check.",
 sections=[
  sec("The levels", "The skills page lists six filesystem levels, and also notes skills synced from a claude.ai account [Claude Code docs, Skills, 2026].",
   """
| Level | Path | Scope |
|---|---|---|
| Enterprise | `.claude/skills/<name>/SKILL.md` in the managed settings directory | All users in the organisation |
| Personal | `~/.claude/skills/<name>/SKILL.md` | All your projects |
| Project | `.claude/skills/<name>/SKILL.md` | This repository |
| Nested | `<subdir>/.claude/skills/<name>/SKILL.md` | Sessions started in or below `<subdir>` |
| Additional directory | `.claude/skills/` in a `--add-dir` directory | That session |
| Plugin | `<plugin>/skills/<name>/SKILL.md` | Where the plugin is enabled, as `/plugin-name:skill-name` |

Project skills load from the start directory and every parent up to the repository root; nested skills load when Claude first touches a file in that subdirectory [Claude Code docs, Skills, 2026].
""",
   ("Wrong-scope placement", "A team procedure is saved in `~/.claude/skills/`, so only you have it and teammates run something else.", "Put team procedures in the project's `.claude/skills/` and commit them."),
   "sharing is sub-topic 5.2.11; layering across features is sub-topic 5.1.7.", "audience decides the level."),
  sec("Clash resolution", "When names match, enterprise overrides personal and personal overrides project; your skill replaces a bundled skill or built-in command of the same name but not its aliases; plugin skills are namespaced and never conflict; added-directory clashes get a prefix like `/cli:verify` (v2.1.309+) [Claude Code docs, Skills, 2026].",
   """
| Clash | Winner |
|---|---|
| Personal `deploy` vs project `deploy` | Personal |
| Enterprise `deploy` vs personal `deploy` | Enterprise |
| Your `debug` vs bundled `/debug` | Yours |
| Skill vs `.claude/commands/` same name | Skill |
""",
   ("Shadow-by-name", "You name a personal skill `review` and it silently replaces the bundled review behaviour you wanted for the rest of the team's habits.", "Pick a distinctive name, and check `/skills` after adding one."),
   "bundled skills are sub-topic 5.2.8.", "overrides are silent; names are the guard."),
  sec("Monorepos and nested skills", "Because nested skills load only when Claude first touches a file in that subdirectory, a monorepo package can carry its own skills without crowding every session [Claude Code docs, Skills, 2026]. The `paths` field further limits automatic loading to files matching its globs, relative to the working directory; files outside it do not match [Claude Code docs, Skills, 2026].",
   """
```text
repo/
  .claude/skills/release/SKILL.md          # whole repo
  packages/api/.claude/skills/migrate/     # loads when Claude touches packages/api files
```
""",
   ("Out-of-tree paths", "A skill with `paths` never activates for files in a sibling git worktree added with `/add-dir`, because they are outside the working directory.", "Start Claude Code in that worktree, or move the session there with `/cd`."),
   "large codebases are Module 3.5.", "nested placement keeps skills local to the code they serve."),
 ],
 retrieval=[
  ("Which wins: enterprise or personal?", "Enterprise."),
  ("Which wins: personal or project?", "Personal."),
  ("A team procedure sits in your home directory only. Name the failure mode by its exact label.", "**Wrong-scope placement.**"),
  ("What form do plugin skills take?", "`/plugin-name:skill-name`."),
  ("Your skill silently replaces a bundled one. Name the failure mode.", "**Shadow-by-name.**"),
  ("From which version do added-directory clashes get a prefix?", "v2.1.309."),
  ("A `paths` skill never activates in a sibling worktree. Name the failure mode by its exact label.", "**Out-of-tree paths.**"),
  ("When do nested skills load?", "When Claude first touches a file in that subdirectory."),
  ("How many levels does the table list?", "Six."),
  ("What happens when a skill and a commands file share a name?", "The skill wins."),
 ],
 steps=[("List all skills you use and where each lives", "Inventory"), ("Mark each by audience", "Audience column"), ("Move any mismatch", "Moves"), ("Create a deliberate same-name clash at two levels", "Fixtures"),
        ("Predict then observe the winner", "Prediction table"), ("Rename to remove silent shadowing", "Renames")],
 pass_md="""
| Skill | Audience | Level | Clash? |
|---|---|---|---|
| release | Team | Project | None |
| my-notes | Me | Personal | None |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Team skill at personal level | **Wrong-scope placement** |
| Clash predicted after the run | Not a prediction |
""",
 verdict="The artifact passes only if each skill's level matches its audience and the clash prediction was written before the test.",
 resources=R(),
 reframe="This is the craft of placement: **audience picks the level, names avoid the clash.** The engineer who understands this does not ask \"where do I save it?\" — they ask \"who needs it, and what else uses this name?\"",
))

# ---------------------------------------------------------------- 5.2.3
SPECS.append(guide(M, "5.2.3", "Frontmatter",
 thesis="Frontmatter is the control surface of a skill: it decides who can invoke it, what it may do unprompted, where it runs and when it activates.",
 prove="write a side-effecting skill with the right invocation, tool and context fields and show Claude cannot trigger it on its own.",
 discipline="set disable-model-invocation on anything with side effects before writing the body.",
 counter="`allowed-tools` pre-approves; it does not restrict. Tools not listed remain available under your normal permission settings [Claude Code docs, Skills, 2026].",
 read_min=24, prove_h="2",
 depth=["Name the fields and what each controls", "Choose fields for a given workflow", "Combine fork, tools, hooks and paths safely"],
 deliverable="Frontmatter for three skills (reference, side-effecting action, forked review) with a one-line reason per field.",
 sections=[
  sec("The field list", "Field names are lowercase with hyphens except `when_to_use`; all fields are optional though `description` is recommended; unrecognised fields are ignored without an error [Claude Code docs, Skills, 2026].",
   """
| Field | Controls |
|---|---|
| `name` | Command name in the `/` menu; defaults to directory name |
| `description` | What it does and when; used for matching |
| `when_to_use` | Extra trigger text, appended to description |
| `argument-hint`, `arguments` | Autocomplete hint; named positional arguments |
| `disable-model-invocation` | `true` stops Claude loading it automatically |
| `user-invocable` | `false` hides it from the `/` menu |
| `allowed-tools` / `disallowed-tools` | Pre-approve tools for the turn / remove tools while active |
| `model`, `effort` | Model and effort for the turn (`low` to `max`) |
| `context`, `agent`, `background` | Fork into a subagent; type; wait or not (v2.1.218+) |
| `hooks` | Hooks registered while the skill is active |
| `paths` | Globs limiting automatic loading |
| `shell` | `bash` (default) or `powershell` for injected commands |
| `metadata`, `license`, `compatibility` | Accepted, not acted on by Claude Code |

[Claude Code docs, Skills, 2026]
""",
   ("Typo-tolerant ignore", "You write `disable-model-invokation: true`; Claude Code ignores the unknown field without error, and the skill with side effects stays auto-invocable.", "Check fields against the table and confirm in `/skills` how the skill is listed."),
   "invocation semantics are sub-topic 5.2.6; forked execution is sub-topic 5.1.3.", "unknown keys fail silently, so verify behaviour."),
  sec("Who can invoke", "The docs tabulate invocation: by default both you and Claude can invoke and the description is always in context; with `disable-model-invocation: true` only you can invoke and the description is not in context; with `user-invocable: false` only Claude can invoke and the description is still in context [Claude Code docs, Skills, 2026].",
   """
| Frontmatter | You | Claude | Description in context |
|---|---|---|---|
| (default) | Yes | Yes | Always |
| `disable-model-invocation: true` | Yes | No | No |
| `user-invocable: false` | No | Yes | Always |

```yaml
---
name: commit
description: Stage and commit the current changes
disable-model-invocation: true
allowed-tools: Bash(git add *) Bash(git commit *) Bash(git status *)
---
```
""",
   ("Auto-deploy", "A deploy skill keeps the default invocation setting, and Claude loads and runs it because the conversation matched its description.", "Add `disable-model-invocation: true` to any workflow with side effects."),
   "cost effects are sub-topic 5.1.8.", "side effects mean you invoke, not Claude."),
  sec("Scoping what a skill can touch", "`allowed-tools` clears when you send your next message and does not restrict other tools; `disallowed-tools` removes tools from Claude's pool while the skill is active; `paths` limits automatic loading; `context: fork` runs it in a subagent whose agent type comes from `agent` (default general-purpose) [Claude Code docs, Skills, 2026]. You can also deny the Skill tool in `/permissions` or allow or deny single skills with rules such as `Skill(commit)` [Claude Code docs, Skills, 2026].",
   """
| Need | Field |
|---|---|
| Stop prompts for `git commit` while running | `allowed-tools: Bash(git commit *)` |
| Make the skill read-only | `disallowed-tools` (for the active period) |
| Only load for TypeScript work | `paths: "**/*.ts"` |
| Do the work in isolation | `context: fork` + `agent: Explore` |
""",
   ("Pre-approval-as-sandbox", "You list two tools in `allowed-tools` and assume Claude can use nothing else, but every other tool still works under your permission settings.", "Use `disallowed-tools` or permission deny rules to restrict; use `allowed-tools` only to pre-approve."),
   "permissions are Module 4.2; hooks in skills are sub-topic 5.2.12.", "allow is not the same as only."),
 ],
 retrieval=[
  ("Which field stops Claude loading a skill automatically?", "`disable-model-invocation: true`."),
  ("Which field hides a skill from the `/` menu?", "`user-invocable: false`."),
  ("You misspell a frontmatter key and a side-effecting skill stays auto-invocable. Name the failure mode by its exact label.", "**Typo-tolerant ignore.**"),
  ("A deploy skill ran because the conversation matched. Name the failure mode.", "**Auto-deploy.**"),
  ("When does `allowed-tools` clear?", "When you send your next message."),
  ("You assumed `allowed-tools` limits Claude to those tools. Name the failure mode by its exact label.", "**Pre-approval-as-sandbox.**"),
  ("What is the default `agent` with `context: fork`?", "general-purpose."),
  ("How many characters is the combined description and when_to_use truncated at?", "1,536."),
  ("From which version does `background` apply?", "v2.1.218."),
  ("Which effort values can `effort` take?", "`low`, `medium`, `high`, `xhigh`, `max`."),
 ],
 steps=[("Write the commit skill with invocation and tool fields", "`commit/SKILL.md`"), ("Ask Claude in plain words to commit and confirm it does not auto-load", "Observation"), ("Run `/commit`", "Transcript"), ("Misspell one key on purpose and observe", "Evidence of silent ignore"),
        ("Write a forked read-only review skill", "Second file"), ("Write a `paths` reference skill and trigger it", "Third file")],
 pass_md="""
| Skill | Key fields | Verified |
|---|---|---|
| commit | disable-model-invocation, allowed-tools | Not auto-loaded; runs without prompts |
| review | context: fork, agent: Explore | Returned summary only |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Side-effect skill left auto-invocable | **Auto-deploy** |
| Fields not tested | Typos go unnoticed |
""",
 verdict="The artifact passes only if the side-effecting skill was shown not to auto-load.",
 resources=R(),
 reframe="This is the craft of frontmatter: **invocation, tools, context, activation.** The engineer who understands this does not ask \"what does this skill say?\" — they ask \"who can fire it, and what can it touch?\"",
))

# ---------------------------------------------------------------- 5.2.4
SPECS.append(guide(M, "5.2.4", "Writing a good description",
 thesis="The description is the trigger: Claude sees only that text until the skill loads, so vague or overlapping descriptions cause missed or wrong loads.",
 prove="write a description, measure its hit rate on should-trigger and should-not-trigger prompts, and improve it.",
 discipline="start the description with the key use case and phrase it as 'use when'.",
 counter="a long, thorough description can be worse than a short one: the combined description and when_to_use is truncated at 1,536 characters, and with many skills descriptions are dropped to fit the listing budget [Claude Code docs, Skills, 2026].",
 read_min=20, prove_h="2.5",
 depth=["State what Claude sees and the limits", "Rewrite a weak description", "Measure trigger rates with a prompt set"],
 deliverable="Three before/after descriptions with a 10-prompt trigger test and hit rates.",
 sections=[
  sec("What Claude sees", "Claude only sees the description until the skill loads, so it decides on that text. The listing always includes every skill name, but with many skills Claude Code drops some descriptions to fit a budget that scales at 1% of the model's context window, dropping the least-invoked first [Claude Code docs, Skills, 2026].",
   """
| Limit | Value |
|---|---|
| Combined `description` + `when_to_use` per entry | 1,536 characters |
| Listing budget | 1% of the model's context window (`skillListingBudgetFraction`) |
| Per-entry cap setting | `skillListingMaxDescChars` |
| Fallback if description omitted | First non-empty line of the body |

[Claude Code docs, Skills, 2026]
""",
   ("Buried key use case", "The trigger phrase sits at the end of a 1,400-character description, and after truncation or budget trimming the use case Claude needed is gone.", "Put the key use case first and keep the combined text short."),
   "context cost is sub-topic 5.1.8.", "the description is all Claude has when deciding."),
  sec("Shape of a good description", "The docs' guidance: put the key use case first, include trigger phrases and example requests (in `description` or `when_to_use`), and use the 'when' form; the example reads 'Use when the user asks what changed, wants a commit message, or asks to review their diff' [Claude Code docs, Skills, 2026].",
   """
| Weak | Better |
|---|---|
| "Helps with git" | "Summarizes uncommitted changes and flags anything risky. Use when the user asks what changed, wants a commit message, or asks to review their diff." |
| "Database stuff" | "Query patterns and schema notes for the orders database. Use when writing or debugging SQL against orders." |
""",
   ("Overlap collision", "Two skills both say 'use for code review', and Claude loads the wrong one or neither.", "Give each a distinct trigger and say what it is not for."),
   "invocation by name is sub-topic 5.2.6.", "distinct triggers beat broad coverage."),
  sec("Testing triggers", "Troubleshooting steps: check the description includes keywords users would naturally say, verify the skill appears when you ask what skills are available, rephrase the request to match, and invoke directly with `/skill-name` [Claude Code docs, Skills, 2026]. For plugin skills, an eval with a `tool_used: Skill` grader run with `claude plugin eval` can measure trigger rate; the skill-creator also tunes descriptions with should-trigger and should-not-trigger prompts [Claude Code docs, Skills, 2026].",
   """
```text
should trigger:     "what did I change?"   "write a commit message"   "review my diff"
should NOT trigger: "explain git rebase"   "what is a diff in math"
hit rate = triggered-as-expected / total
```
""",
   ("One-prompt testing", "You test with the one phrase you wrote the skill for and conclude it triggers, then it misses real users' phrasing.", "Test at least five should-trigger and five should-not-trigger prompts."),
   "plugin evals are sub-topic 5.6.7.", "measure the hit rate, not a single success."),
 ],
 retrieval=[
  ("What is the per-entry character cap for description plus when_to_use?", "1,536."),
  ("What fraction of context does the listing budget scale at?", "1%."),
  ("The key use case sits at the end of a long description. Name the failure mode by its exact label.", "**Buried key use case.**"),
  ("Two skills both say 'use for code review'. Name the failure mode.", "**Overlap collision.**"),
  ("What does Claude use if no description is given?", "The first non-empty line of the body."),
  ("You tested one prompt and declared it working. Name the failure mode by its exact label.", "**One-prompt testing.**"),
  ("Which descriptions are dropped first when the listing overflows?", "Those of the least-invoked skills."),
  ("Which setting raises the listing budget?", "`skillListingBudgetFraction`."),
  ("Which phrase form does the docs' example use?", "'Use when ...'."),
  ("How many should-trigger and should-not-trigger prompts does this guide recommend at minimum?", "At least five of each."),
 ],
 steps=[("Pick one skill with poor triggering", "Skill name"), ("Write 5 should-trigger and 5 should-not prompts", "Prompt set"), ("Run each and record loads", "Baseline hit rate"), ("Rewrite: key use case first, 'use when' form", "New description"),
        ("Rerun the set", "New hit rate"), ("Check for overlap with other skills", "Overlap note")],
 pass_md="""
| Version | Should-trigger hits | Should-not hits |
|---|---|---|
| Before | 2/5 | 1/5 false |
| After | 5/5 | 0/5 false |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Only should-trigger prompts | False positives unmeasured |
| Description over 1,536 characters | Will be cut |
""",
 verdict="The artifact passes only if both prompt sets were run before and after the rewrite.",
 resources=R([("Anthropic", "Skill authoring best practices (linked from the Skills page)", "Cross-product guidance", "Not retrieved: platform.claude.com was not reachable")]),
 reframe="This is the craft of the description: **the trigger, the first words, the hit rate.** The engineer who understands this does not ask \"is my skill good?\" — they ask \"does Claude find it when it should, and not when it shouldn't?\"",
))

# ---------------------------------------------------------------- 5.2.5
SPECS.append(guide(M, "5.2.5", "Arguments and dynamic context",
 thesis="Arguments let one skill serve many calls, and shell injection lets it start from live facts, but a failing injected command aborts the whole skill.",
 prove="write a skill that takes an argument and injects live command output, and show what happens when the command fails.",
 discipline="append `|| true` to injected commands that may exit non-zero, and test the failure path.",
 counter="a non-zero exit from an injected command aborts the entire skill invocation, and Claude never sees the skill content [Claude Code docs, Skills, 2026].",
 read_min=22, prove_h="2",
 depth=["State the substitution variables and injection syntax", "Write a parameterised skill with live context", "Harden injection against failure and permissions"],
 deliverable="A parameterised skill with live injection, a failure-path test and a permissions note.",
 sections=[
  sec("Argument substitution", "Text typed after the slash command becomes arguments. If the skill has no placeholder for them, Claude Code appends `ARGUMENTS: <value>` so the input is still seen [Claude Code docs, Skills, 2026].",
   """
| Variable | Expands to |
|---|---|
| `$ARGUMENTS` | Full argument string |
| `$ARGUMENTS[N]` or `$N` | Argument at 0-based index N |
| `$name` | Named argument from the `arguments` field |
| `${CLAUDE_SKILL_DIR}` | Directory containing SKILL.md |
| `${CLAUDE_PROJECT_DIR}` | Project root |
| `${CLAUDE_SESSION_ID}` | Current session ID |
| `${CLAUDE_EFFORT}` | Current effort level |

Escape a literal dollar sign as `\\$1.00`. [Claude Code docs, Skills, 2026]
""",
   ("Placeholder-less skill", "A skill ignores `$ARGUMENTS`, so the typed value arrives only as an appended `ARGUMENTS:` line and the instructions do not refer to it.", "Reference `$ARGUMENTS` or a named argument where the value belongs."),
   "invocation is sub-topic 5.2.6.", "put the argument where the instruction needs it."),
  sec("Injecting live output", "The `` !`command` `` syntax runs a shell command before the skill content reaches Claude and replaces the placeholder with its output. Inline form is recognised only when `!` starts a line or follows whitespace; substitution runs once; multi-line commands use a fenced block opened with ```` ```! ````; each command has the Bash tool's default 2-minute timeout [Claude Code docs, Skills, 2026].",
   """
```yaml
---
name: pr-summary
description: Summarize changes in a pull request
context: fork
agent: Explore
allowed-tools: Bash(gh *)
---
- PR diff: !`gh pr diff`
- Changed files: !`gh pr diff --name-only`
```
[Claude Code docs, Skills, 2026]
""",
   ("Output-as-instruction", "A command's output contains text that reads like an instruction, and Claude follows it because injection puts it into the skill as if you wrote it.", "Inject only trusted, structured output and keep the instructions below it explicit."),
   "injection and security of project skills are sub-topic 5.2.12.", "injection runs once, before Claude sees anything."),
  sec("Failure and permission behaviour", "A non-zero exit aborts the invocation, except exit code 1 from search and comparison commands such as `grep`. Injected commands are checked against permission rules: a deny rule aborts the invocation, and any non-allow result aborts unless pre-approved with `allowed-tools`. `disableSkillShellExecution: true` in settings replaces each command with `[shell command execution disabled by policy]` for user, project, plugin and additional-directory skills; Claude Code never runs injected commands in skills synced from your claude.ai account [Claude Code docs, Skills, 2026].",
   """
| Situation | Result |
|---|---|
| Command exits 0 | Output substituted |
| `grep` finds nothing (exit 1) | Treated as a normal result |
| Other non-zero exit | Whole invocation aborted |
| Deny rule matches | Aborted |
| Not allowed and not pre-approved | Aborted (auto mode defers to its usual checks) |
| Fix for flaky commands | `command || true` |
""",
   ("Abort-on-exit", "A `git diff` or `gh` call exits non-zero in a repo with no remote, the invocation aborts, and Claude never sees the skill, which looks like a skill that does not work.", "Append `|| true` where failure is acceptable and test the skill in a clean repo."),
   "permissions are Module 4.2.", "design for the command failing."),
 ],
 retrieval=[
  ("What is appended when a skill has no placeholder for typed arguments?", "`ARGUMENTS: <value>`."),
  ("What is the default timeout of an injected command?", "2 minutes."),
  ("An injected command exits non-zero and the skill vanishes. Name the failure mode by its exact label.", "**Abort-on-exit.**"),
  ("Which exit code from `grep` is treated as a normal result?", "1."),
  ("The skill never references the typed value. Name the failure mode.", "**Placeholder-less skill.**"),
  ("Which setting disables injection by policy?", "`disableSkillShellExecution: true`."),
  ("Injected text told Claude to do something and it complied. Name the failure mode by its exact label.", "**Output-as-instruction.**"),
  ("What index base do `$ARGUMENTS[N]` and `$N` use?", "0-based."),
  ("How many skills can you chain at the start of a message?", "Up to six."),
  ("Are injected commands run for skills synced from claude.ai?", "No."),
 ],
 steps=[("Write a skill using `$ARGUMENTS` and one injected command", "SKILL.md"), ("Invoke with an argument", "Transcript"), ("Force the command to fail", "Abort evidence"), ("Add `|| true` and rerun", "Fixed run"),
        ("Check the command against your permission rules", "Permission note"), ("Test in a clean directory", "Second run")],
 pass_md="""
| Test | Expected | Observed |
|---|---|---|
| With argument | Value used | Used |
| Command fails | Skill still loads (with `|| true`) | Loaded |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Failure path untested | **Abort-on-exit** goes unseen |
| Argument not referenced | **Placeholder-less skill** |
""",
 verdict="The artifact passes only if the failing-command case was exercised and produced a loaded skill.",
 resources=R(),
 reframe="This is the craft of dynamic context: **arguments in, live facts in, failure planned for.** The engineer who understands this does not ask \"does it work?\" — they ask \"what does it do when the command fails?\"",
))

# ---------------------------------------------------------------- 5.2.6
SPECS.append(guide(M, "5.2.6", "Invocation",
 thesis="A skill can be fired by you at the start of a message, loaded by Claude from its description, or stacked with others, and which path runs is determined by frontmatter and message position.",
 prove="demonstrate all three paths on one skill and show that a slash name mid-message only grants permission.",
 discipline="put the slash name at the start of the message when you want the skill to run directly.",
 counter="`/name` appearing after plain text does not run the skill directly; it only grants Claude permission to run it for that message [Claude Code docs, Skills, 2026].",
 read_min=18, prove_h="1.5",
 depth=["Name the invocation paths and their rules", "Stack skills with arguments", "Choose which skills Claude may auto-invoke"],
 deliverable="A three-path test log for one skill and a two-skill stacked invocation.",
 sections=[
  sec("Direct invocation", "To run a skill directly, put `/name` at the start of your message, such as `/deploy staging`. A command is only recognised at the start of your message, and text after the name becomes its arguments [Claude Code docs, Skills and Commands, 2026].",
   """
| Message | Effect |
|---|---|
| `/deploy staging` | Runs the skill directly with `staging` |
| `please run /deploy staging` | Does not run directly; permits Claude to run it for this message |
| `/deploy` while Claude is responding | Queued until the turn ends |
""",
   ("Mid-message slash", "You type text then `/deploy` and assume the skill ran, but it only gave Claude permission to run it.", "Start the message with the slash name."),
   "commands are sub-topic 5.2.8.", "start of message means run; elsewhere means permit."),
  sec("Automatic loading", "Claude matches your task to skill descriptions and loads one when relevant, unless `disable-model-invocation: true` hides it. Skills with `user-invocable: false` can only be invoked by Claude [Claude Code docs, Skills, 2026].",
   """
| Path | Who decides | Needs |
|---|---|---|
| You type `/name` | You | Skill is user-invocable |
| Claude loads it | Claude | A matching description; model invocation not disabled |
| `paths` match | Claude, only for matching files | `paths` globs |
""",
   ("Phantom availability", "You expect Claude to use a skill that has `disable-model-invocation: true` and it never does.", "Invoke it yourself or remove the setting if automatic use is wanted."),
   "frontmatter is sub-topic 5.2.3; descriptions are sub-topic 5.2.4.", "three paths, one frontmatter switch each."),
  sec("Stacking skills", "At the terminal prompt you can chain up to six skills at the start of a message, for example `/write-tests /fix-issue 123`; the trailing text becomes `$ARGUMENTS` for each [Claude Code docs, Skills, 2026].",
   """
```text
/write-tests /fix-issue 123
   skill A      skill B   -> "123" becomes $ARGUMENTS for both
```
Each stacked skill's body is loaded into the conversation, so six large skills cost six bodies of context [inference from the lifecycle rule, not stated as a cost in the docs].
""",
   ("Argument-bleed", "You stack skills and the trailing text is passed to every skill, so a skill that expected something else misreads it.", "Stack only skills that accept the same argument, or invoke them one at a time."),
   "context costs are sub-topic 5.1.8.", "stacking shares one argument string."),
 ],
 retrieval=[
  ("How many skills can be chained at the start of a message?", "Six."),
  ("What does a slash name after plain text do?", "Grants Claude permission to run it for that message; it does not run it directly."),
  ("You typed text then a slash name and nothing ran directly. Name the failure mode by its exact label.", "**Mid-message slash.**"),
  ("A model-invocation-disabled skill never loads on its own. Name the failure mode.", "**Phantom availability.**"),
  ("In a stacked message, what happens to trailing text?", "It becomes `$ARGUMENTS` for each skill."),
  ("Two stacked skills misread one argument. Name the failure mode by its exact label.", "**Argument-bleed.**"),
  ("What happens to a command sent while Claude is responding?", "It is queued and runs after the current turn."),
  ("Which frontmatter value makes a skill Claude-only?", "`user-invocable: false`."),
  ("What does `/deploy staging` pass as an argument?", "`staging`."),
  ("How many invocation paths are tested in this guide?", "Three: direct, automatic, stacked."),
 ],
 steps=[("Pick a skill with a clear description", "Skill name"), ("Invoke it directly", "Log 1"), ("Ask in plain words to trigger it automatically", "Log 2"), ("Type text then the slash name", "Log 3"),
        ("Stack two skills with one argument", "Log 4"), ("Record which path ran each time", "Table")],
 pass_md="""
| Path | Ran directly? | Notes |
|---|---|---|
| `/name arg` | Yes | |
| Plain request | Auto-loaded | Matched description |
| Text + `/name` | No | Permission only |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Only one path tried | Cannot tell **Mid-message slash** from a bug |
""",
 verdict="The artifact passes only if the mid-message case was tried and recorded as not direct.",
 resources=R(),
 reframe="This is the craft of invocation: **position decides run versus permit.** The engineer who understands this does not ask \"why didn't it run?\" — they ask \"where was the slash name, and who could load it?\"",
))

# ---------------------------------------------------------------- 5.2.7
SPECS.append(guide(M, "5.2.7", "Progressive disclosure",
 thesis="Keep SKILL.md short and put long references, scripts and examples in files the skill points to, so Claude reads them only when needed.",
 prove="split an oversized skill into a focused SKILL.md under 500 lines plus linked files, and show Claude loads a reference file only when relevant.",
 discipline="every supporting file must be mentioned from SKILL.md with a line saying when to read it.",
 counter="a script in the skill folder is executed, not loaded: it costs no context until its output appears [Claude Code docs, Skills, 2026].",
 read_min=18, prove_h="2",
 depth=["State the folder layout and the 500-line tip", "Split a bloated skill", "Bundle a script that produces output"],
 deliverable="A before/after skill folder with line counts and a test showing the reference file loaded on demand.",
 sections=[
  sec("The layout", "Skills can bundle other files so SKILL.md stays focused. The docs' layout has `SKILL.md` as the required overview and navigation, `reference.md` and `examples.md` loaded when needed, and `scripts/helper.py` executed rather than loaded; the tip is to keep SKILL.md under 500 lines and move detailed material to separate files [Claude Code docs, Skills, 2026].",
   """
```text
my-skill/
  SKILL.md        required: overview and navigation
  reference.md    detailed API docs, loaded when needed
  examples.md     usage examples, loaded when needed
  scripts/helper.py   executed, not loaded
```
""",
   ("Orphan file", "A reference file sits in the skill folder but SKILL.md never mentions it, so Claude never knows when to read it.", "Reference every file from SKILL.md with a when-to-read line."),
   "context cost is sub-topic 5.1.8.", "SKILL.md navigates; files hold the depth."),
  sec("Why short matters", "A skill's rendered body enters the conversation as one message and stays across turns; after compaction only the first 5,000 tokens of each recently invoked skill are re-attached, within a combined 25,000 [Claude Code docs, Skills, 2026]. A short body stays complete; a long one is cut.",
   """
| Size | Consequence |
|---|---|
| Under 500 lines | Fits the tip; stays whole after compaction if within the token budget |
| Long body | Persistent cost in every later turn; truncated on re-attach |
| Instructions near the top | Survive truncation |
""",
   ("Tail-loaded rules", "The most important rule sits at the bottom of a long SKILL.md and is lost when compaction keeps only the first 5,000 tokens.", "Put the critical instructions first and the detail in linked files."),
   "compaction behaviour is Module 3.1 and sub-topic 5.2.12.", "the top of the file is the safe place."),
  sec("Scripts and visual output", "The docs show a skill that bundles a script: its SKILL.md tells Claude to run `python3 ${CLAUDE_SKILL_DIR}/scripts/visualize.py .`, which writes an interactive HTML file and opens it; `${CLAUDE_SKILL_DIR}` resolves at personal, project or plugin level, and `allowed-tools: Bash(python3 *)` pre-approves the call [Claude Code docs, Skills, 2026].",
   """
| Job | Where it lives |
|---|---|
| Choosing when and how | SKILL.md prose |
| Deterministic work | `scripts/` |
| Long reference | `reference.md` |
| Output for you | Generated file, path printed |
""",
   ("Hard-coded path", "A skill calls its script by an absolute path on your machine and breaks for teammates or after a plugin install.", "Use `${CLAUDE_SKILL_DIR}` in every script path."),
   "plugin install is sub-topic 5.6.3.", "scripts do the deterministic part; SKILL.md decides when."),
 ],
 retrieval=[
  ("What line count does the docs' tip give for SKILL.md?", "Under 500 lines."),
  ("How many tokens of each skill survive auto-compaction?", "The first 5,000."),
  ("A reference file is never read. Name the failure mode by its exact label.", "**Orphan file.**"),
  ("The key rule sits at the bottom of a long skill. Name the failure mode.", "**Tail-loaded rules.**"),
  ("What is the combined re-attach budget?", "25,000 tokens."),
  ("A script path works only on your machine. Name the failure mode by its exact label.", "**Hard-coded path.**"),
  ("Is a bundled script loaded into context or executed?", "Executed."),
  ("Which variable gives the skill's directory?", "`${CLAUDE_SKILL_DIR}`."),
  ("Which file is required in a skill folder?", "`SKILL.md`."),
  ("How many supporting-file types does the docs' layout show besides SKILL.md?", "Three: reference, examples and scripts."),
 ],
 steps=[("Choose a skill over 300 lines or create a long one", "Baseline file"), ("Move reference to `reference.md`", "Linked file"), ("Move deterministic steps to a script", "`scripts/` file"), ("Add when-to-read lines in SKILL.md", "Navigation"),
        ("Run a task needing the reference and confirm it was read", "Transcript"), ("Count lines before and after", "Two numbers")],
 pass_md="""
| Item | Before | After |
|---|---|---|
| SKILL.md lines | 640 | 120 |
| Files referenced | 0 | 3 |
| Reference read on demand | n/a | Yes |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Files not linked from SKILL.md | **Orphan file** |
| No test of on-demand read | Unproven |
""",
 verdict="The artifact passes only if every supporting file is linked and a run showed the reference read only when relevant.",
 resources=R(),
 reframe="This is the craft of disclosure: **a short front door and deep rooms.** The engineer who understands this does not ask \"what else should I put in?\" — they ask \"what can Claude fetch only when it needs it?\"",
))

# ---------------------------------------------------------------- 5.2.8
SPECS.append(guide(M, "5.2.8", "Bundled skills",
 thesis="Claude Code ships prompt-based skills for common jobs, and knowing each one's job saves you from rebuilding them and from using the wrong one.",
 prove="run /code-review and /simplify on the same diff and explain why they report different things.",
 discipline="pick the bundled skill by job (bugs, cleanup, scale, verify, debug) before writing your own.",
 counter="`/simplify` does not look for correctness bugs; `/code-review` does [Claude Code docs, Commands, 2026].",
 read_min=22, prove_h="2",
 depth=["Name the bundled skills and their jobs", "Choose the right one for a task", "Replace or supplement one with your own"],
 deliverable="A table of eight bundled skills with job, trigger task from your work and one run result.",
 sections=[
  sec("What makes a skill bundled", "Bundled skills are prompt-based: they give Claude detailed instructions and let it orchestrate the work with its tools, whereas most built-in commands execute fixed logic directly [Claude Code docs, Skills, 2026]. In the commands reference they are marked as skills.",
   """
| Skill | Job |
|---|---|
| `/code-review [level] [--fix] [--comment] [target]` | Review the diff, a PR, branch or path for correctness bugs; alias `/review` |
| `/simplify [target]` | Four parallel review agents for cleanup (reuse, simplification, efficiency, abstraction level); applies fixes; no bug hunt |
| `/batch <instruction>` | Decompose into 5 to 30 independent units, plan, then one background subagent per unit in an isolated worktree |
| `/debug [description]` | Enable debug logging and read the session debug log |
| `/loop [interval] [prompt]` | Re-run a prompt while the session stays open; alias `/proactive` |
| `/verify` | Build and run your app to confirm a change, not only tests |
| `/run`, `/run-skill-generator` | Launch and drive the app; write a per-project run skill |
| `/doctor` | Setup checkup, proposes fixes applied after confirmation |
| `/update-config [request]` | Edit settings.json from a description |
| `/fewer-permission-prompts` | Scan transcripts and add a read-only allowlist to project settings |
| `/claude-api`, `/claude-in-chrome`, `/dataviz`, `/design`, `/design-sync`, `/slides` | API reference, browser tasks, chart guidance, design canvases, design-system sync, slide decks |

[Claude Code docs, Commands, 2026; table abridged. The list changes by version, so check `/` in your own build.]
""",
   ("Reinvented bundle", "You write your own review skill that duplicates `/code-review` and maintain it forever.", "Run the bundled one first; write your own only for what it does not cover."),
   "subagents are Module 5.3; worktrees are Module 6.2; large-scale change is Module 6.5.", "check the bundle before building."),
  sec("Review versus simplify", "These two are easy to confuse. `/code-review` looks for correctness bugs and, depending on model and effort, cleanup opportunities; `--fix` applies findings, `--comment` posts to a GitHub PR or GitLab merge request, and `ultra` runs a deeper cloud review. `/simplify` runs four agents for cleanup and explicitly does not look for correctness bugs [Claude Code docs, Commands, 2026].",
   """
| Question | Use |
|---|---|
| Is this change wrong? | `/code-review` |
| Is this change messy or duplicated? | `/simplify` |
| Is it safe to ship? | `/verify` after both |
""",
   ("Cleanup-as-correctness", "You run `/simplify`, see a clean result and assume the logic was reviewed.", "Run `/code-review` for bugs; treat `/simplify` as cleanup only."),
   "verification is Module 2.3.", "cleanup is not correctness."),
  sec("Run, verify and scale", "`/run` and `/verify` work without setup but inference becomes unreliable for projects needing more than a standard launch; `/run-skill-generator` records the recipe as a per-project skill at `.claude/skills/run-<name>/`, to be run once per project and again if the build or launch changes [Claude Code docs, Skills, 2026]. `/batch` needs a git repository or a `WorktreeCreate` hook; outside git it needs v2.1.281 or later [Claude Code docs, Commands, 2026].",
   """
| Task | Skill chain |
|---|---|
| Prove a change works in the running app | `/run-skill-generator` once, then `/verify` |
| Migrate 200 files | `/batch migrate src/ from JavaScript to TypeScript` |
| Watch a deploy | `/loop 5m check if the deploy finished` |
""",
   ("Batch-without-plan", "You launch a batch of dozens of parallel units without reading the proposed plan, and approve decomposition that overlaps.", "Read the plan before approving; `/batch` presents one first."),
   "dynamic workflows are Module 6.5; loops are Module 6.7.", "approve the plan, not just the command."),
 ],
 retrieval=[
  ("Between how many and how many units does `/batch` decompose work?", "5 to 30."),
  ("How many review agents does `/simplify` run in parallel?", "Four."),
  ("You ran `/simplify` and assumed correctness was reviewed. Name the failure mode by its exact label.", "**Cleanup-as-correctness.**"),
  ("You maintain a skill duplicating a bundled one. Name the failure mode.", "**Reinvented bundle.**"),
  ("Which skill writes a per-project run recipe?", "`/run-skill-generator`."),
  ("You approved a batch plan without reading it. Name the failure mode by its exact label.", "**Batch-without-plan.**"),
  ("Which alias does `/code-review` have?", "`/review`."),
  ("What version does `/batch` need outside a git repository?", "v2.1.281 or later."),
  ("Which flag posts review findings to a PR?", "`--comment`."),
  ("Do bundled skills execute fixed logic?", "No; they are prompt-based, unlike most built-in commands."),
 ],
 steps=[("List the skills visible in `/` in your build", "Inventory"), ("Run `/code-review` on a small diff", "Findings"), ("Run `/simplify` on the same diff", "Cleanup list"), ("Compare the two lists", "Difference note"),
        ("Run `/verify` on the change", "Run evidence"), ("Pick one bundled skill to customise by override", "Plan")],
 pass_md="""
| Skill | Result on same diff |
|---|---|
| /code-review | 1 bug found |
| /simplify | 3 cleanup edits, no bug |
| /verify | Ran app, confirmed fix |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Only `/simplify` run | **Cleanup-as-correctness** |
| No run evidence | Verification claimed, not shown |
""",
 verdict="The artifact passes only if both reviews ran on the same diff and their different outputs are explained.",
 resources=R(),
 reframe="This is the craft of the bundle: **ten ready tools, each with one job.** The engineer who understands this does not ask \"can I write a review skill?\" — they ask \"which bundled one already does this?\"",
))

# ---------------------------------------------------------------- 5.2.9
SPECS.append(guide(M, "5.2.9", "Managing skills",
 thesis="Skills accumulate cost and drift, so you need the commands that list them, price them, hide them and refresh them.",
 prove="run /skill-doctor, hide one unused skill with skillOverrides, and show the listing cost fell.",
 discipline="review skill cost and usage whenever you add several skills.",
 counter="`/reload-skills` is not needed for ordinary edits: Claude Code watches skill directories, and the rescan matters mainly for a top-level skills directory created after the session started [Claude Code docs, Skills, 2026].",
 read_min=20, prove_h="1.5",
 depth=["Name the management commands and settings", "Find and disable unused skills", "Decide when to reload"],
 deliverable="A before/after listing of skill costs and a `skillOverrides` block you committed to.",
 sections=[
  sec("List and price", "`/skills` lists available skills; synced claude.ai skills appear under `claude.ai sync`. `/skill-doctor` (v2.1.252+, not available in sessions that skip feature-flag fetching) reports each skill's context cost and usage, flags never-invoked skills and where to turn them off; it covers your skills other than bundled and enterprise ones [Claude Code docs, Skills, 2026]. `/doctor` estimates the listing's context cost.",
   """
| Command | Does |
|---|---|
| `/skills` | List, filter and change visibility |
| `/skill-doctor` | Context cost and usage per skill |
| `/doctor` | Listing cost estimate and biggest contributors |
| `/context` | Skills row shows the listing size after budget |

[Claude Code docs, Skills and Commands, 2026]
""",
   ("Never-reviewed pile", "You add skills for months and never run `/skill-doctor`, so unused skills keep costing context on every turn.", "Review cost and usage after adding skills and switch off the never-invoked ones."),
   "context costs are sub-topic 5.1.8.", "list, price, then prune."),
  sec("Hide without editing", "`skillOverrides` sets visibility from settings: states are `on`, `name-only`, `user-invocable-only` and `off`; plugin skills are not affected, manage those via `/plugin` [Claude Code docs, Skills, 2026]. In the `/skills` editor, press Space to cycle states and Esc to save.",
   """
```json
{
  "skillOverrides": {
    "legacy-context": "name-only",
    "deploy": "off"
  }
}
```
| State | Effect |
|---|---|
| `on` | Normal |
| `name-only` | Listed without description |
| `user-invocable-only` | You can invoke; Claude cannot auto-load |
| `off` | Hidden |
""",
   ("Plugin-skill override", "You add a plugin skill's name to `skillOverrides` expecting it to change, and nothing happens.", "Manage plugin skills through `/plugin`."),
   "plugins are Module 5.6; settings precedence is Module 4.1.", "overrides change visibility without editing the file."),
  sec("Refreshing", "Claude Code watches the skill directories, so adding, editing or removing a skill under `~/.claude/skills/`, the project `.claude/skills/` or an `--add-dir` directory takes effect without a restart. The skills page says `/reload-skills` is needed only after you create a top-level skills directory that did not exist at session start; plugin changes to `hooks/`, `.mcp.json`, `agents/` and `output-styles/` need `/reload-plugins` [Claude Code docs, Skills, 2026]. The commands reference describes `/reload-skills` more broadly, as a rescan so skills added or changed on disk during the session become available [Claude Code docs, Commands, 2026].",
   """
| Change | Needed |
|---|---|
| Edit an existing skill | Nothing (live detection) |
| Create `~/.claude/skills/` for the first time mid-session | `/reload-skills` |
| Edit a plugin's hooks | `/reload-plugins` |
""",
   ("Reload-reflex", "You restart the session after every skill edit, losing context, when live detection would have applied it.", "Edit and retry; reload only for a new top-level directory."),
   "plugins reload is sub-topic 5.6.3.", "most edits apply live."),
 ],
 retrieval=[
  ("From which version is `/skill-doctor` available?", "v2.1.252."),
  ("How many states does `skillOverrides` take?", "Four: on, name-only, user-invocable-only, off."),
  ("Months of skills, never reviewed. Name the failure mode by its exact label.", "**Never-reviewed pile.**"),
  ("You list a plugin skill in skillOverrides and nothing changes. Name the failure mode.", "**Plugin-skill override.**"),
  ("What do you run after changing a plugin's hooks?", "`/reload-plugins`."),
  ("You restart after each edit. Name the failure mode by its exact label.", "**Reload-reflex.**"),
  ("Which key cycles states in the `/skills` editor?", "Space."),
  ("What does `name-only` do?", "Lists the skill without its description."),
  ("What do the two pages disagree on about `/reload-skills`?", "The skills page says it is needed only for a newly created top-level directory; the commands page describes a broader rescan."),
  ("Which skills does `/skill-doctor` exclude?", "Bundled and enterprise skills."),
 ],
 steps=[("Run `/context` and note the Skills row", "Baseline"), ("Run `/skill-doctor`", "Report"), ("Choose three low-use skills", "Candidates"), ("Set two to `name-only` and one to `off`", "Settings diff"),
        ("Rerun `/context`", "New number"), ("Edit a skill and confirm it applies without reload", "Observation")],
 pass_md="""
| Step | Result |
|---|---|
| Skills row | Down after overrides |
| Override file | Committed |
| Edit applied live | Yes |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| No before/after number | Cannot show savings |
| Plugin skill in overrides | Does nothing |
""",
 verdict="The artifact passes only if the Skills row measured smaller after the overrides.",
 resources=R([], "the skills page says `/reload-skills` is needed only for a newly created top-level skills directory, while the commands page describes it as a general rescan so added or changed skills become available; treat the skills page as the more specific and test in your build."),
 reframe="This is the craft of management: **list, price, hide, refresh.** The engineer who understands this does not ask \"how many skills can I have?\" — they ask \"what is each one costing me every turn?\"",
))

# ---------------------------------------------------------------- 5.2.10
SPECS.append(guide(M, "5.2.10", "Skills in subagents",
 thesis="A subagent's skills field preloads full skill content at launch, so the subagent starts already knowing what a normal session would load only on demand.",
 prove="preload one skill into a subagent and show the subagent applies it without an invocation step.",
 discipline="preload only the skills the subagent always needs; leave the rest discoverable.",
 counter="a skill with `disable-model-invocation: true` cannot be preloaded into a subagent [Claude Code docs, Skills, 2026].",
 read_min=16, prove_h="1.5",
 depth=["State how preload differs from on-demand loading", "Write a subagent that preloads skills", "Pick preload versus discovery"],
 deliverable="A subagent definition with a `skills:` list and a test showing the skill content was applied.",
 sections=[
  sec("Preload versus on-demand", "In a regular session only the description is in context until a skill is used. For a subagent with a `skills` field, the full skill content is injected at startup. The subagent can still discover and invoke unlisted project, user and plugin skills through the Skill tool [Claude Code docs, Extend Claude Code and Skills, 2026].",
   """
| Context | What the skill looks like |
|---|---|
| Normal session | Description only until used |
| Subagent with `skills:` listed | Full content from the start |
| Subagent, unlisted skill | Discoverable via the Skill tool |
""",
   ("Preload-everything", "You list a dozen skills in a subagent's `skills` field, so its fresh context starts with every body loaded and little room for the actual task.", "Preload only skills it needs on every run."),
   "subagent definitions are sub-topic 5.3.3.", "preload for always, discover for sometimes."),
  sec("The two combine directions", "The docs list two ways skills and subagents combine: a subagent's `skills` field preloads skills; a skill's `context: fork` runs the skill as a task in a subagent, where the subagent does not see your conversation history, so the skill's instructions must stand alone [Claude Code docs, Skills, 2026].",
   """
| Direction | Instructions come from | Task comes from |
|---|---|---|
| Subagent + `skills:` | Subagent body + preloaded skills | Delegation message |
| Skill + `context: fork` | The skill body (becomes the task) | The skill body |

A forked skill with only guidelines and no task returns without meaningful output [Claude Code docs, Skills, 2026].
""",
   ("History-assuming skill", "A forked skill refers to 'the file we just discussed', but the subagent never saw that conversation.", "Write forked skills so the instructions stand alone."),
   "forks of the whole conversation are sub-topic 5.3.7.", "forked agents start without your history."),
  sec("Invocation control and preload", "The docs state that `disable-model-invocation` also prevents a skill from being preloaded into subagents. A side-effecting skill therefore cannot be handed to a subagent as ambient knowledge, which is usually the point [Claude Code docs, Skills, 2026].",
   """
```yaml
# .claude/agents/reviewer.md
---
name: reviewer
description: Review changes against our API conventions
skills: api-conventions
---
```
[Frontmatter field `skills` as named in the docs; example constructed for illustration]
""",
   ("Disabled-and-expected", "You mark a skill `disable-model-invocation: true`, list it under a subagent's `skills`, and expect it preloaded.", "Remove the setting for knowledge skills, or invoke the action skill from the main session."),
   "frontmatter is sub-topic 5.2.3.", "preload works for knowledge skills, not manual-only ones."),
 ],
 retrieval=[
  ("Which subagent field preloads skills?", "`skills`."),
  ("What does a regular session hold of a skill before use?", "Only its description."),
  ("A subagent starts with a dozen bodies and no room. Name the failure mode by its exact label.", "**Preload-everything.**"),
  ("A forked skill refers to 'the file we just discussed'. Name the failure mode.", "**History-assuming skill.**"),
  ("Can a `disable-model-invocation` skill be preloaded?", "No."),
  ("You listed a manual-only skill under `skills` and it did not preload. Name the failure mode by its exact label.", "**Disabled-and-expected.**"),
  ("Does a forked skill's subagent see your conversation history?", "No."),
  ("Can a subagent invoke unlisted skills?", "Yes, through the Skill tool."),
  ("How many combine directions are described?", "Two."),
  ("What does a guidelines-only forked skill return?", "Nothing meaningful."),
 ],
 steps=[("Pick one knowledge skill", "Skill name"), ("Create a subagent with `skills:` listing it", "Agent file"), ("Delegate a task needing the skill", "Transcript"), ("Check the output follows the skill", "Observation"),
        ("Try preloading a manual-only skill", "Failure evidence"), ("Fork a skill that includes a task", "Forked run")],
 pass_md="""
| Test | Result |
|---|---|
| Preloaded skill applied | Yes |
| Manual-only skill preloaded | No, as documented |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Dozen skills preloaded | **Preload-everything** |
""",
 verdict="The artifact passes only if the preloaded skill's content visibly shaped the subagent's output.",
 resources=R([("Anthropic", "Extend Claude Code", "Skills in subagents loading rule", "Current")]),
 thin="The dedicated preload section of the subagents page (sub-agents#preload-skills-into-subagents) was not fetched; this guide rests on the Skills and Extend pages.",
 reframe="This is the craft of preload: **agents that start knowing.** The engineer who understands this does not ask \"how do I teach the agent?\" — they ask \"what should it always know on arrival?\"",
))

# ---------------------------------------------------------------- 5.2.11
SPECS.append(guide(M, "5.2.11", "Sharing",
 thesis="A skill reaches other people by being committed to the repo, packaged in a plugin, or deployed through managed settings, and each route has its own audience and update path.",
 prove="share one skill through the repo and confirm a clean checkout runs it.",
 discipline="share through version control first; package into a plugin only when a second repository needs it.",
 counter="personal skills are scoped to you: `~/.claude/skills/` serves 'all your projects' but lives on your machine, not in the repository [Claude Code docs, Skills, 2026].",
 read_min=16, prove_h="1.5",
 depth=["Name the three sharing routes", "Share a skill via the repo and verify", "Decide when to plugin-ise"],
 deliverable="A shared project skill committed to a repo and a clean-clone test.",
 sections=[
  sec("Three routes", "The skills page lists three scopes: project skills by committing `.claude/skills/` to version control, plugins by creating a `skills/` directory in a plugin, and managed deployment organisation-wide through managed settings [Claude Code docs, Skills, 2026].",
   """
| Route | Audience | Update path |
|---|---|---|
| Commit `.claude/skills/` | Everyone who clones the repo | Pull request |
| Plugin `skills/` directory | Anyone who installs the plugin | New plugin version |
| Managed settings | Whole organisation | Admin deployment |
""",
   ("Works-on-my-machine skill", "A skill lives in your home folder; teammates never see it.", "Commit it under the project's `.claude/skills/`."),
   "plugins are Module 5.6; managed settings are Module 4.1.", "pick the narrowest route that reaches the audience."),
  sec("Clone and sync behaviour", "Project skills are committed with the repository, so they arrive with a clone; personal skills live under your home directory and serve only your own projects. Skills synced from your claude.ai account download into a separate `synced` subfolder of `~/.claude/skills/`, and Claude Code never runs injected shell commands in them; project skills committed to a repo also load when that repo is used in a Claude Tag channel [Claude Code docs, Skills, 2026]. How cloud sessions treat each location was not verified for this guide.",
   """
| Where the skill is | Who gets it |
|---|---|
| Repo `.claude/skills/` | Everyone who clones the repo |
| `~/.claude/skills/` | You, across your projects |
| claude.ai-synced skills | You, in `~/.claude/skills/synced`, without shell injection |
""",
   ("Secrets-in-skill", "A shared skill embeds a token in a script or injected command, and it is committed with the repo.", "Read secrets from the environment and never commit them in skill files."),
   "security of project config is sub-topic 5.2.12.", "if it is committed, everyone with access can read it."),
  sec("Naming for shared use", "Plugin skills are namespaced so they cannot clash; project skills can be shadowed by a teammate's personal skill of the same name because personal overrides project [Claude Code docs, Skills, 2026]. Names for shared skills should therefore be distinctive.",
   """
| Choice | Effect |
|---|---|
| Generic name `review` in project | A personal `review` shadows it |
| Distinct name `acme-review` | Hard to shadow by accident |
| Plugin skill | `/acme:review`, never clashes |
""",
   ("Shadowed share", "You share a project skill named `deploy` and teammates with a personal `deploy` run theirs instead.", "Use distinctive names or ship via plugin."),
   "priority rules are sub-topic 5.2.2.", "shared names must survive personal overrides."),
 ],
 retrieval=[
  ("Name the three sharing routes.", "Commit to the repo, package into a plugin, deploy through managed settings."),
  ("Do `~/.claude/skills/` skills travel with a repository clone?", "No; they live on your machine."),
  ("A skill sits only in your home folder. Name the failure mode by its exact label.", "**Works-on-my-machine skill.**"),
  ("A token was committed inside a skill script. Name the failure mode.", "**Secrets-in-skill.**"),
  ("Why can a shared project skill be shadowed?", "Personal skills override project skills of the same name."),
  ("Teammates run their own `deploy` instead of yours. Name the failure mode by its exact label.", "**Shadowed share.**"),
  ("How do plugin skills avoid clashes?", "Namespacing, e.g. `/acme:review`."),
  ("Can injected shell commands run in skills synced from claude.ai?", "No."),
  ("How many routes does this guide cover?", "Three."),
  ("Which route reaches the whole organisation?", "Managed settings."),
 ],
 steps=[("Choose a skill worth sharing", "Name"), ("Move it to `.claude/skills/` in the repo", "Commit"), ("Review it for secrets and absolute paths", "Review note"), ("Clone fresh to a new directory", "Clean clone"),
        ("Run the skill there", "Transcript"), ("Rename if shadowing risk exists", "Rename")],
 pass_md="""
| Check | Result |
|---|---|
| Fresh clone runs the skill | Yes |
| No secrets or absolute paths | Verified |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Skill tested only on your machine | **Works-on-my-machine skill** |
""",
 verdict="The artifact passes only if a fresh clone ran the skill successfully.",
 resources=R(),
 thin="Cloud-session behaviour for each skill location was not verified; the guide says so rather than assert it.",
 reframe="This is the craft of sharing: **commit it, name it, test it fresh.** The engineer who understands this does not ask \"is it saved?\" — they ask \"does a stranger's clone run it?\"",
))

# ---------------------------------------------------------------- 5.2.12
SPECS.append(guide(M, "5.2.12", "Troubleshooting skills",
 thesis="Skill problems fall into four classes, not triggering, triggering too often, stopped following, and descriptions cut, and each has a specific diagnostic.",
 prove="diagnose four seeded skill faults using the documented checks, one per class.",
 discipline="classify the symptom first, then apply that class's checks in order.",
 counter="malformed frontmatter does not make a skill disappear: the body still loads with empty metadata, so `/skill-name` works but Claude cannot match the description [Claude Code docs, Skills, 2026].",
 read_min=22, prove_h="2.5",
 depth=["Name the four problem classes and their checks", "Diagnose a failing skill step by step", "Handle hook-limit and plugin-only lockdowns"],
 deliverable="A diagnosis log for four seeded faults with class, check and fix for each.",
 sections=[
  sec("Not triggering", "The documented steps: check the description has keywords users would say; verify the skill appears when you ask what skills are available; rephrase; invoke with `/skill-name`; if that is not recognised, check whether Claude Code refused the name; if `paths` is set, check the files are inside the working directory [Claude Code docs, Skills, 2026]. Run with `--debug` to see a YAML parse error, and `claude plugin validate .claude/skills` (v2.1.233+) finds files whose frontmatter does not parse.",
   """
| Step | Check |
|---|---|
| 1 | Keywords in description |
| 2 | Skill listed? |
| 3 | Rephrase request |
| 4 | `/skill-name` directly |
| 5 | Name accepted? |
| 6 | `paths` inside working directory |
| 7 | `--debug`, `claude plugin validate` |
""",
   ("Skip-the-checklist", "You rewrite the whole skill when the real fault was a `paths` glob outside the working directory.", "Walk the checks in order before editing the body."),
   "descriptions are sub-topic 5.2.4.", "diagnose before rewriting."),
  sec("Too often, and stops following", "If a skill triggers too often: make the description more specific or add `disable-model-invocation: true`. If Claude stops following it: a must-hold rule belongs in a hook (possibly in the skill's own `hooks` frontmatter); judgement guidance should be worded for the whole task; after compaction, invoke the skill again, because only its start may be kept [Claude Code docs, Skills, 2026].",
   """
| Symptom | Cause | Fix |
|---|---|---|
| Fires on unrelated requests | Broad description | Narrow it or disable model invocation |
| Followed once, then ignored | Rule must always hold | Hook |
| Ignored after a long session | Compaction kept only the start | Re-invoke; put key rules first |
""",
   ("Compaction-blindness", "Claude follows the skill early, then drifts after a long session, and you blame the wording rather than the 5,000-token re-attach limit.", "Re-invoke after compaction and keep critical instructions near the top."),
   "compaction is Module 3.1; hooks are Module 5.4.", "long sessions truncate skills."),
  sec("Descriptions cut, hooks limits, lockdowns", "When the listing overflows its budget, descriptions are dropped starting with least-invoked skills; run `/doctor`. If managed settings list `hooks` in `strictPluginOnlyCustomization`, personal and project skills that declare hooks lose their `allowed-tools` pre-approval; remove `hooks` from the frontmatter or move the skill into a plugin [Claude Code docs, Skills, 2026]. Before v2.1.280 a `manifest.json` in `~/.claude/skills/` could cause listed skill folders to be moved to `~/.claude/skills/.trash/` (default retention 30 days) [Claude Code docs, Skills, 2026].",
   """
| Symptom | Look at |
|---|---|
| Skill listed without description | `/doctor`, `skillListingBudgetFraction` |
| Pre-approval vanished | `strictPluginOnlyCustomization` includes `hooks` |
| Personal skills gone | `~/.claude/skills/.trash/` |
""",
   ("Policy-blind skill", "A hook-bearing skill prompts for every tool in your org while working elsewhere, because managed policy removed its pre-approval.", "Check managed settings; move the skill into a plugin or drop its hooks."),
   "managed settings are Module 4.1; hooks in skills are sub-topic 5.4.2.", "some failures come from policy, not the skill."),
 ],
 retrieval=[
  ("With malformed frontmatter, does `/skill-name` still work?", "Yes; the body loads with empty metadata."),
  ("Which flag shows a YAML parse error?", "`--debug`."),
  ("You rewrote a skill when a `paths` glob was the fault. Name the failure mode by its exact label.", "**Skip-the-checklist.**"),
  ("Claude drifts from a skill after a long session. Name the failure mode.", "**Compaction-blindness.**"),
  ("From which version does `claude plugin validate` find unparseable frontmatter?", "v2.1.233 or later."),
  ("A hook-bearing skill lost its pre-approval org-wide. Name the failure mode by its exact label.", "**Policy-blind skill.**"),
  ("Where do trashed skill folders go, and for how long by default?", "`~/.claude/skills/.trash/`, 30 days."),
  ("Which setting in managed config removes pre-approval for skills that declare hooks?", "`strictPluginOnlyCustomization` listing `hooks`."),
  ("How many problem classes does this guide use?", "Four."),
  ("What is the fix when a rule must hold every time?", "Move it to a hook."),
 ],
 steps=[("Seed four faults in four skills", "Fixtures"), ("Classify each symptom", "Class column"), ("Apply the documented checks in order", "Check log"), ("Fix each", "Diffs"),
        ("Retest", "Pass evidence"), ("Write a one-page runbook", "Runbook")],
 pass_md="""
| Fault | Class | Check that found it | Fix |
|---|---|---|---|
| Wrong glob | Not triggering | Step 6 | Corrected glob |
| Rule ignored late | Stops following | Compaction | Hook |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| Fix applied without a check | **Skip-the-checklist** |
""",
 verdict="The artifact passes only if every fault was classified before it was fixed and retested.",
 resources=R([("Anthropic", "Debug your configuration", "Linked from Skills page", "Not fetched")]),
 reframe="This is the craft of troubleshooting: **class, check, fix, retest.** The engineer who understands this does not ask \"why is this skill broken?\" — they ask \"which of the four classes is this?\"",
))

# ---------------------------------------------------------------- 5.2.13
SPECS.append(guide(M, "5.2.13", "Skill design patterns",
 thesis="Good skills fall into recognisable shapes, reference or task at the top level, with checklists, runbooks and rubrics as the common bodies, and choosing the shape first makes the file easy to write.",
 prove="write two skills of different shapes for the same domain and show how invocation and body style differ.",
 discipline="decide whether the skill is reference or task before writing a line.",
 counter="the docs themselves name only two content types, reference and task; the longer list of patterns is a working taxonomy, not an official catalogue.",
 read_min=18, prove_h="2",
 depth=["Name the two documented content types", "Pick a body pattern for a given job", "Combine patterns without bloat"],
 deliverable="Two skills (one reference, one task) with a note on which pattern each body follows.",
 thin="The docs distinguish reference content from task content; the pattern names beyond that (checklist, decision tree, template, rubric, runbook, glossary, conventions, release procedure, analysis recipe) come from this syllabus and from common practice, not from a documented catalogue. Anthropic's skill best-practices page was unreachable. Treat the pattern table as a judgement-based taxonomy.",
 sections=[
  sec("Reference versus task", "The skills page states two content types. Reference content adds knowledge Claude applies to current work (conventions, patterns, style guides, domain knowledge) and runs inline. Task content gives step-by-step instructions for a specific action such as deployments, commits or code generation, and is often best invoked directly with `/skill-name` [Claude Code docs, Skills, 2026].",
   """
| Type | Invocation | Frontmatter hint | Body style |
|---|---|---|---|
| Reference | Claude loads when relevant | Default, descriptive `description` | Facts and conventions |
| Task | You type `/name` | `disable-model-invocation: true` if side effects | Numbered steps |
""",
   ("Mixed-type skill", "One skill holds both the style guide and the deploy steps, so loading it for style also loads and risks the deploy procedure.", "Split into a reference skill and a task skill."),
   "frontmatter is sub-topic 5.2.3; skill-vs-subagent is sub-topic 5.1.3.", "decide reference or task before writing."),
  sec("Body patterns", "Within those types the same bodies recur. These names are a working taxonomy [judgement, not an official list].",
   """
| Pattern | Suits | Shape |
|---|---|---|
| Checklist | Pre-merge, pre-release | Tick list with pass/fail |
| Decision tree | Choosing among options | If/then branches |
| Template | Repeated outputs (ADR, PR description) | Fill-in skeleton |
| Review rubric | Consistent critique | Criteria with scoring |
| Runbook | Operations, incident response | Ordered commands and checks |
| Domain glossary | Terms Claude keeps misusing | Term, meaning, not-to-confuse |
| API conventions | Team code style | Rules plus examples |
| Release procedure | Shipping | Steps with side effects: manual invocation |
| Data-analysis recipe | Repeatable analysis | Query, transform, chart steps |
""",
   ("Pattern-by-fashion", "You write a decision tree for a job that is really a template, and Claude branches where it should have filled in.", "Name the job's output first (a list, a choice, a document) and match the pattern to it."),
   "descriptions are sub-topic 5.2.4; disclosure is sub-topic 5.2.7.", "the output shape picks the pattern."),
  sec("Where side effects belong", "Skills with side effects such as release procedures should set `disable-model-invocation: true`; the docs recommend it for workflows like `/deploy` and the overview tip says to use it for skills with side effects, which saves context and ensures they run only when named [Claude Code docs, Skills and Extend Claude Code, 2026]. A rule that must hold every time belongs in a hook instead.",
   """
| Pattern | Auto-load OK? |
|---|---|
| Glossary, conventions, rubric | Yes |
| Template | Usually yes |
| Release procedure, runbook with actions | No: manual |
| Checklist | Depends on whether it runs commands |
""",
   ("Auto-run runbook", "A runbook that restarts services is left auto-invocable and a loosely matched request triggers it.", "Mark it manual-only."),
   "hooks for guarantees are Module 5.4.", "side effects mean manual invocation."),
 ],
 retrieval=[
  ("What two content types does the skills page name?", "Reference and task."),
  ("One skill holds a style guide and deploy steps. Name the failure mode by its exact label.", "**Mixed-type skill.**"),
  ("A decision tree is used for a fill-in job. Name the failure mode.", "**Pattern-by-fashion.**"),
  ("Which frontmatter setting suits release procedures?", "`disable-model-invocation: true`."),
  ("A service-restarting runbook fired from a loose match. Name the failure mode by its exact label.", "**Auto-run runbook.**"),
  ("How many body patterns does this guide's table list?", "Nine."),
  ("Which pattern suits repeated outputs like a PR description?", "Template."),
  ("Is the nine-pattern list official?", "No; it is a working taxonomy."),
  ("Where does a must-hold rule belong?", "In a hook."),
  ("Which type is best invoked directly with a slash name?", "Task content."),
 ],
 steps=[("Pick a domain you work in", "Domain"), ("Write a reference skill (glossary or conventions)", "Skill 1"), ("Write a task skill (runbook or checklist)", "Skill 2"), ("Set invocation fields for each", "Frontmatter"),
        ("Test both paths", "Two transcripts"), ("Note which pattern each follows", "Pattern note")],
 pass_md="""
| Skill | Type | Pattern | Invocation |
|---|---|---|---|
| acme-glossary | Reference | Glossary | Auto |
| acme-release | Task | Release procedure | Manual |
""",
 fail_md="""
| Element | What is wrong |
|---|---|
| One file for both types | **Mixed-type skill** |
""",
 verdict="The artifact passes only if the two skills differ in type, pattern and invocation, and each was exercised.",
 resources=R([("Anthropic", "Skill authoring best practices (linked from Skills page)", "Cross-product writing guidance", "Not retrieved")]),
 reframe="This is the craft of skill shape: **reference or task, then the body that fits the output.** The engineer who understands this does not ask \"what should the skill say?\" — they ask \"what shape is this job?\"",
))

if __name__ == "__main__":
    run(SPECS)
