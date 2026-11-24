import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from specs_b14_0 import *

M = "b-14-4"
SPECS = []
D = "[Claude Code docs, Explore the .claude directory, 2026]"
MEM = "[Claude Code docs, Memory, 2026]"
ST = "[Claude Code docs, Settings, 2026]"
RD = [("Anthropic", "Explore the .claude directory", "Files, scopes, application data, retention", "Current; read via fetch"), ("Anthropic", "Memory", "CLAUDE.md load order, rules, imports", "Current; read via fetch")]

SPECS.append(G(M, "14.4.1", "Instruction files: CLAUDE.md scopes, AGENTS.md and .claude/rules",
 "Instruction files are concatenated, not overridden, so where a rule lives decides when it loads and what it competes with.",
 "list every instruction file that loaded in one session and justify the load order.",
 "put each rule in the narrowest scope that needs it.",
 "CLAUDE.md files are concatenated rather than overriding each other, so a contradictory line in a broader file does not lose; both are in context " + MEM + ".",
 24, "2.5", ["Name the four scopes and load order", "Use rules and imports correctly", "Design a layered instruction set for a monorepo"],
 "A map of instruction files for one repo with scope, load time and a tested path-scoped rule.",
 [S("Scopes and load order", "Scopes from broadest to most specific: managed policy (for example `/etc/claude-code/CLAUDE.md` on Linux), user `~/.claude/CLAUDE.md`, project `./CLAUDE.md` or `./.claude/CLAUDE.md`, and local `./CLAUDE.local.md` which you add to `.gitignore`. Claude walks up from the working directory and concatenates what it finds, ordered from the filesystem root down, with `CLAUDE.local.md` after `CLAUDE.md` in a directory. Subdirectory files load on demand when Claude reads files there " + MEM + ".",
   """
| Scope | Location | Shared with |
|---|---|---|
| Managed | OS-specific system path | Whole org |
| User | `~/.claude/CLAUDE.md` | You, all projects |
| Project | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Team via git |
| Local | `./CLAUDE.local.md` | You, this project |
""", "Override-assumption", "You expect a project CLAUDE.md to override a contradictory user-level line, but both are in context and Claude may follow either.", "Remove the contradiction rather than relying on precedence.", "memory design is Module 3.2 and Module 3.3.", "concatenated, not overridden."),
  S("Size, imports and AGENTS.md", "The docs target under 200 lines per CLAUDE.md. `@path` imports resolve relative to the importing file, recurse to four hops, and still load at launch, so they organise but do not save context. Claude Code reads CLAUDE.md, not AGENTS.md: import it with `@AGENTS.md` or symlink `ln -s AGENTS.md CLAUDE.md`, and on Windows prefer the import because symlinks need Administrator rights or Developer Mode " + MEM + ".",
   """
```markdown
@AGENTS.md

## Claude Code
Use plan mode for changes under `src/billing/`.
```

| Technique | Saves context? |
|---|---|
| `@import` | No; loads at launch |
| Path-scoped rule | Yes, until matching files are read |
| Shorter file | Yes |
""", "Import-as-saving", "You split a long CLAUDE.md into imported files and expect context to shrink, but imports load at launch.", "Move conditional content into path-scoped rules or skills.", "skills are Module 5.2.", "imports organise, they do not trim."),
  S("Rules and path scopes", "`.claude/rules/*.md` are discovered recursively; rules without `paths` frontmatter load at launch with the priority of `.claude/CLAUDE.md`, and rules with `paths` load only when Claude reads matching files. User rules in `~/.claude/rules/` load before project rules, so project rules have higher priority " + MEM + ".",
   """
```markdown
---
paths:
  - "src/api/**/*.ts"
---
# API rules
- All endpoints validate input
```
""", "Unscoped-rule-bloat", "You add many rules without `paths`, so all of them load at launch and crowd the window.", "Add `paths` frontmatter to rules that matter only for some files.", "context cost is Module 3.1.", "scope rules by path."),
  S("Excludes, comments and the local file", "`claudeMdExcludes` skips ancestor CLAUDE.md files in monorepos by absolute-path glob, arrays merge across layers, and managed CLAUDE.md cannot be excluded. Block-level HTML comments are stripped before injection. `--add-dir` does not load CLAUDE.md unless `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` " + MEM + ".",
   """
| Need | Mechanism |
|---|---|
| Skip a parent team's file | `claudeMdExcludes` |
| Maintainer note not sent to Claude | Block-level HTML comment |
| Load CLAUDE.md from added dir | `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` |
""", "Comment-leak-belief", "You put a secret in an HTML comment believing it is hidden, but the Read tool shows comments and the file is in git.", "Never place secrets in instruction files.", "security is Module 11.1.", "comments are stripped from context, not from the file.")],
 [("Which file holds your private per-project notes?", "`CLAUDE.local.md`."), ("What is the docs' target length for a CLAUDE.md?", "Under 200 lines."),
  ("You expect a project line to override a user line. Name the failure mode by its exact label.", "**Override-assumption.**"), ("How many hops can imports recurse?", "Four."),
  ("You split into imports to save context. Name the failure mode.", "**Import-as-saving.**"), ("How do you make Claude read AGENTS.md?", "Import it with `@AGENTS.md` or symlink it to CLAUDE.md."),
  ("Every rule loads at launch. Name the failure mode and fix.", "**Unscoped-rule-bloat.** Add `paths` frontmatter."), ("Which rules load before project rules?", "User rules in `~/.claude/rules/`."),
  ("You hide a secret in a comment. Name the failure mode.", "**Comment-leak-belief.**"), ("Which setting skips ancestor CLAUDE.md files?", "`claudeMdExcludes`.")],
 [("Run `/memory` and list loaded files", "List"), ("Add a contradictory line at two scopes and observe", "Observation"), ("Create a path-scoped rule", "Rule file"), ("Read a matching file and confirm it loads", "Observation"), ("Import AGENTS.md", "Line"), ("Measure with `/context`", "Numbers")],
 """
| File | Scope | Loads |
|---|---|---|
| `~/.claude/CLAUDE.md` | User | Launch |
| `./CLAUDE.md` | Project | Launch |
| `.claude/rules/api.md` | Path | On matching read |
""", """
| Element | What is wrong |
|---|---|
| Contradiction left in place | **Override-assumption** |
""", "The artifact passes only if the path-scoped rule's on-demand load was observed.",
 RES(RD, "the memory page says Claude Code reads CLAUDE.md, not AGENTS.md, while the .claude directory page says it can read AGENTS.md in place of a CLAUDE.md. **Treat the Memory page's import or symlink method as the tested path and verify with `/memory`.**"),
 RF("instruction files", "scope decides when a rule loads", "why is Claude ignoring my rule?", "which files loaded, in what order, and does a broader one contradict it?")))

SPECS.append(G(M, "14.4.2", "Configuration files: settings.json, settings.local.json and managed policy",
 "Settings files are layered by scope, and which file you edit decides who is affected.",
 "change one key at each scope and show which wins.",
 "put personal changes in the local file and team changes in the committed file.",
 "a key can be ignored in a repository file entirely, because some keys apply only from user or managed settings " + ST + ".",
 24, "2.5", ["Name the file and its audience", "Predict precedence", "Debug a setting that does not apply"],
 "A precedence experiment: one key set at four levels with the winner observed.",
 [S("Files and audience", "User `~/.claude/settings.json` affects you everywhere; shared project `.claude/settings.json` affects everyone in the folder and should be committed; project local `.claude/settings.local.json` is yours in one project; managed settings from managed sources apply org-wide. `~/.claude.json` is a fifth file Claude Code writes for itself " + ST + ".",
   """
| File | Who | Commit |
|---|---|---|
| `~/.claude/settings.json` | You, every project | n/a |
| `.claude/settings.json` | Everyone in project | Yes |
| `.claude/settings.local.json` | You, one project | No |
| `managed-settings.json` etc. | Organisation | Deployed |
| `~/.claude.json` | App state, MCP personal | Do not edit |
""", "Wrong-audience", "You commit a personal preference in the shared file and change behaviour for the whole team.", "Put personal settings in `settings.local.json`.", "settings are Module 4.1.", "pick the file by audience."),
  S("Precedence", "Highest first: managed, command line (`--settings`), project local, shared project, user. Lists such as `permissions.allow` merge across files; environment variables are not a level and are decided per key pair, for example `ANTHROPIC_MODEL` over the `model` key " + ST + ".",
   """
| Level | Wins over |
|---|---|
| 1 Managed | Everything (narrow exceptions) |
| 2 `--settings` | Files below |
| 3 Local | Shared and user |
| 4 Shared project | User |
| 5 User | n/a |
""", "Env-is-a-level", "You treat an environment variable as another layer in the stack and mis-predict a model choice.", "Check the key's entry for its paired variable.", "env vars are Module 14.6.", "env vars are per-key, not a level."),
  S("Keys that do not apply", "`permissions.defaultMode` values `auto` and `bypassPermissions` do not take effect from project or local settings; `allow` rules and most `env` values from a committed file wait until the folder is trusted, while `deny` and `ask` apply at once " + ST + ".",
   """
| Key | From shared file |
|---|---|
| `permissions.deny`, `ask` | Applies at once |
| `permissions.allow` | After workspace trust |
| `defaultMode: auto` | Ignored in project/local |
""", "Untrusted-allow", "You commit an allow rule and a teammate still gets prompts because trust is not yet accepted.", "Tell teammates to trust the folder, and use deny rules where enforcement is immediate.", "workspace trust is Module 1.3.", "allow waits for trust."),
  S("Verify and recover", "Settings files are strict JSON: a comment or trailing comma is an error. Run `/status` for Setting sources and `claude doctor` for rejected entries; a broken user, project or local file raises a Settings Error dialog, while a bad single entry raises a Settings Warning and is skipped " + ST + ".",
   """
```bash
claude doctor        # lists rejected entries
```
""", "Comment-in-JSON", "You add a `//` comment to settings.json and the file fails to load.", "Remove comments; use `/status` and `claude doctor` to confirm.", "debugging is Part 12.", "settings files are strict JSON.")],
 [("Which file holds personal per-project overrides?", "`.claude/settings.local.json`."), ("Which level has the highest precedence?", "Managed settings."),
  ("You commit a personal preference. Name the failure mode by its exact label.", "**Wrong-audience.**"), ("Do `permissions.allow` lists merge across files?", "Yes."),
  ("You treat an env var as a stack level. Name the failure mode.", "**Env-is-a-level.**"), ("Which rules apply from a shared file before trust?", "`deny` and `ask`."),
  ("A teammate still gets prompts for your allow rule. Name the failure mode and fix.", "**Untrusted-allow.** They must trust the folder."), ("What happens with a `//` comment in settings.json?", "A syntax error and a Settings Error at start."),
  ("You add a comment to JSON. Name the failure mode.", "**Comment-in-JSON.**"), ("Which command lists rejected settings entries?", "`claude doctor`.")],
 [("Set one key at user, shared and local levels", "Three files"), ("Start and read `/status` Setting sources", "Line"), ("Observe which value applies", "Observation"), ("Add an allow rule and test as a fresh clone", "Observation"), ("Break the JSON on purpose and read the dialog", "Observation"), ("Write the table", "Table")],
 """
| Level | Value | Winner? |
|---|---|---|
| User | a | no |
| Shared | b | no |
| Local | c | yes |
""", """
| Element | What is wrong |
|---|---|
| Personal setting in shared file | **Wrong-audience** |
""", "The artifact passes only if the winner at each level was observed in /status and behaviour.",
 RES(RD + [("Anthropic", "Settings", "Scopes and precedence", "Current")], "none found between the sources read."),
 RF("settings files", "audience decides the file and precedence decides the winner", "why didn't my setting apply?", "which file, which level and is trust pending?")))

SPECS.append(G(M, "14.4.3", "Extension files: skills, agents, hooks, MCP config and plugin manifests",
 "Each extension type has a home directory and a frontmatter schema, and project-versus-global scope decides who gets it.",
 "place one skill, one agent, one rule and one MCP entry in the right files and verify each loads.",
 "use the file reference table instead of memory when placing a file.",
 "`.mcp.json` is project-only and `~/.claude.json` holds personal MCP servers, so the same server can be shared or private depending on the file " + D + ".",
 24, "2.5", ["Place each extension in the right file", "Read frontmatter schemas", "Design a shareable plugin layout"],
 "A placement table with each extension file created and verified loaded.",
 [S("Where each thing lives", "Per the file reference: `skills/<name>/SKILL.md` and `commands/*.md` (project and global), `agents/*.md`, `output-styles/*.md`, `workflows/*.js`, `agent-memory/<name>/`, project-only `.mcp.json`, and hooks defined in `settings.json` " + D + ".",
   """
| You want | File | Scope |
|---|---|---|
| Reusable prompt | `skills/<name>/SKILL.md` | Project or global |
| Subagent | `agents/*.md` | Project or global |
| Team MCP server | `.mcp.json` | Project only |
| Personal MCP server | `~/.claude.json` | Global |
| Hook | `settings.json` `hooks` | Project or global |
| Saved workflow | `workflows/*.js` | Project or global |
""", "Misfiled-extension", "You put a team MCP server in your personal config and teammates never get it.", "Use the table to choose project or global before creating the file.", "extension choice is Module 5.1.", "scope is part of the path."),
  S("Frontmatter fields", "Skills accept `name`, `description`, `when_to_use`, `disable-model-invocation`, `allowed-tools`, `model`, `paths`, `hooks` and more; subagents accept `name`, `description`, `tools`, `disallowedTools`, `model`, `permissionMode`, `maxTurns`, `skills`, `mcpServers`, `memory`, `isolation` and more; rules accept only `paths` " + D + ".",
   """
| File | Notable fields |
|---|---|
| SKILL.md | name, description, disable-model-invocation, allowed-tools, paths |
| agents/*.md | name, description, tools, model, permissionMode, maxTurns, isolation |
| rules/*.md | paths |
| output-styles/*.md | name, description, keep-coding-instructions |
""", "Field-guessing", "You invent a frontmatter field name, and it is silently ignored.", "Copy field names from the frontmatter table.", "skills are Module 5.2; subagents are Module 5.3.", "unknown fields do nothing."),
  S("Plugins and marketplaces", "Installed plugins live under `~/.claude/plugins` with an `installed_plugins.json` record; plugins synced from claude.ai download into `~/.claude/plugins/synced/`; the `command` marketplace source needs v2.1.229 or later " + D + ". Plugin manifests (`plugin.json`, `marketplace.json`) are described in the plugin reference, which this guide did not read.",
   """
| Path | Contents |
|---|---|
| `~/.claude/plugins/` | Marketplaces, installed versions, install record |
| `~/.claude/plugins/synced/` | Synced from claude.ai |
""", "Hand-edited-install-record", "You edit `installed_plugins.json` by hand and Claude Code sets aside a copy and rewrites it.", "Use `claude plugin` commands.", "plugins are Module 5.6.", "let the CLI manage plugin state."),
  S("Verify the load", "After adding files, reload without restart where available (`/reload-skills`, `/reload-plugins`), and confirm with `/skills`, `/hooks`, `/mcp` and `/status` [Claude Code docs, Commands, 2026].",
   """
| Added | Check |
|---|---|
| Skill | `/reload-skills`, `/skills` |
| Hook | `/hooks` |
| MCP server | `/mcp` |
| Plugin | `/reload-plugins` |
""", "Create-and-hope", "You create a file and assume it loaded.", "Run the matching check command.", "diagnostics are Module 14.1.", "every file gets a check.")],
 [("Which file is project-only for MCP servers?", "`.mcp.json`."), ("Where do personal MCP servers live?", "`~/.claude.json`."),
  ("You put a team server in a personal file. Name the failure mode by its exact label.", "**Misfiled-extension.**"), ("Which frontmatter field do rules accept?", "`paths`."),
  ("You invent a frontmatter field. Name the failure mode.", "**Field-guessing.**"), ("Where does the install record live?", "`~/.claude/plugins/installed_plugins.json`."),
  ("You hand-edit the install record. Name the failure mode and fix.", "**Hand-edited-install-record.** Use `claude plugin`."), ("Which version added the `command` marketplace source?", "v2.1.229."),
  ("You create a file and assume it loaded. Name the failure mode.", "**Create-and-hope.**"), ("Where do synced plugins download?", "`~/.claude/plugins/synced/`.")],
 [("Create a skill, an agent and a rule", "Three files"), ("Run `/reload-skills` and `/skills`", "Evidence"), ("Add an `.mcp.json` entry and run `/mcp`", "Evidence"), ("Add a hook and run `/hooks`", "Evidence"), ("Write the placement table", "Table"), ("Note one field you verified against the schema", "Line")],
 """
| Extension | File | Verified by |
|---|---|---|
| Skill | `.claude/skills/x/SKILL.md` | `/skills` |
| Server | `.mcp.json` | `/mcp` |
""", """
| Element | What is wrong |
|---|---|
| No verification column | **Create-and-hope** |
""", "The artifact passes only if every file has a verification command and observed result.",
 RES(RD, "none found between the sources read; the plugin manifest reference was not read in this pass."),
 RF("extension placement", "scope and schema are part of the path", "where does this go?", "project or global, and which schema fields exist?"),
 thin="Plugin manifest details (plugin.json, marketplace.json) were not retrieved; read the plugin reference before relying on them."))

SPECS.append(G(M, "14.4.4", "Other files: REVIEW.md, loop.md, .worktreeinclude, transcripts and feedback bundles",
 "Four small files and two data directories shape reviews, loops, worktrees and privacy, and the data directories are plaintext.",
 "show what lives in .worktreeinclude, where transcripts are stored and how long they are kept.",
 "treat ~/.claude as sensitive data and set retention deliberately.",
 "transcripts and history are not encrypted at rest, and anything a tool reads, including a .env file, is written to the transcript " + D + ".",
 22, "2", ["Name the file and its purpose", "Set retention", "Purge safely"],
 "A data-handling note: where sessions are stored, the retention setting, one purge dry-run.",
 [S("Small project files", "`.worktreeinclude` lists gitignored files to copy into new worktrees; `REVIEW.md` customises Code Review and `loop.md` sets default loop prompts per the syllabus. This guide retrieved the `.worktreeinclude` entry from the file reference; REVIEW.md and loop.md detail were not read " + D + ".",
   """
| File | Purpose | Source |
|---|---|---|
| `.worktreeinclude` | Gitignored files copied into worktrees | Directory reference |
| `REVIEW.md` | Review customisation | Syllabus; not read |
| `loop.md` | Default loop prompt | Commands page mentions it |
""", "Missing-env-in-worktree", "A new worktree lacks your gitignored `.env` and tests fail for a reason that looks like code.", "List needed gitignored files in `.worktreeinclude`.", "worktrees are Module 6.2.", "worktrees do not carry ignored files by default."),
  S("Transcripts and history", "Transcripts live at `~/.claude/projects/<project>/<session>.jsonl`; `history.jsonl` stores prompts; `file-history/<session>/` holds pre-edit snapshots for checkpoints (the 100 most recent). They are plaintext, and cleanup removes transcript files older than `cleanupPeriodDays`, default 30 days, minimum 1 " + D + ".",
   """
| Path | Retention |
|---|---|
| `projects/<project>/<session>.jsonl` | `cleanupPeriodDays` (30 default) |
| `file-history/` | 100 most recent checkpoints |
| `history.jsonl` | Kept until deleted |
| `projects/<project>/memory/` | Not swept |
""", "Plaintext-blindness", "You assume transcripts are protected, but a command that printed a credential wrote it to disk.", "Deny reads of credential files and shorten retention.", "security is Module 11.1.", "transcripts are plaintext."),
  S("Reducing exposure", "Options: lower `cleanupPeriodDays`; set `CLAUDE_CODE_SKIP_PROMPT_HISTORY`; use `--no-session-persistence` with `-p`; deny reads of credential files; run `claude purge` (previously `claude project purge` before v2.1.288) with `--dry-run` first " + D + ".",
   """
```bash
claude purge ~/work/my-repo --dry-run
```
""", "Heapdump-leftover", "You purge a project but leave a `.heapsnapshot` that contains the full conversation and credentials.", "Delete snapshot files by hand; neither the sweep nor purge touches them.", "diagnostics are Module 14.1.", "purge does not cover heap snapshots."),
  S("Feedback bundles", "`feedback-bundles/` holds redacted transcript archives written by `/feedback` on third-party providers or without Anthropic credentials, for you to forward " + D + ".",
   """
| Path | Keep or delete |
|---|---|
| `feedback-bundles/` | Delete after sending |
| `feedback/drafts/` | Review then send or discard |
""", "Unsent-bundle", "A bundle sits unsent and your report never reaches anyone.", "Forward it to your account team and then delete it.", "support routes are Module 10.1.", "writing a bundle is not sending it.")],
 [("What is the default `cleanupPeriodDays`?", "30."), ("Where are transcripts stored?", "`~/.claude/projects/<project>/<session>.jsonl`."),
  ("A worktree lacks your .env. Name the failure mode by its exact label.", "**Missing-env-in-worktree.**"), ("How many recent checkpoints keep snapshots?", "100."),
  ("You assume transcripts are protected. Name the failure mode.", "**Plaintext-blindness.**"), ("Which command was `claude project purge` before v2.1.288?", "`claude purge`."),
  ("You purge but keep a heap snapshot. Name the failure mode and fix.", "**Heapdump-leftover.** Delete snapshot files by hand."), ("Which env var skips writing transcripts and history?", "`CLAUDE_CODE_SKIP_PROMPT_HISTORY`."),
  ("A feedback bundle is never sent. Name the failure mode.", "**Unsent-bundle.**"), ("What is the minimum `cleanupPeriodDays`?", "1.")],
 [("Find your newest transcript file", "Path"), ("Grep it for a string you typed", "Result"), ("Run `claude purge --dry-run`", "Plan"), ("Check `cleanupPeriodDays` in settings", "Value"), ("Create a `.worktreeinclude` and test", "Result"), ("Write the data-handling note", "Note")],
 """
| Item | Finding |
|---|---|
| Transcript | found, plaintext |
| Retention | set to 14 |
| Purge plan | 3 items |
""", """
| Element | What is wrong |
|---|---|
| No retention value | **Plaintext-blindness** |
""", "The artifact passes only if the transcript was located and retention set or consciously left default.",
 RES(RD, "none found between the sources read; REVIEW.md and loop.md semantics were not retrieved."),
 RF("local files and data", "know what is written and how long it stays", "is my data safe?", "where is it, in plaintext, and for how many days?"),
 thin="REVIEW.md and loop.md were not read in this pass; their guidance is flagged as unverified."))

if __name__ == "__main__":
    run(SPECS)
