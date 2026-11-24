import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from specs_b14_0 import *

M = "b-14-3"
SPECS = []
CL = "[Claude Code docs, CLI reference, 2026]"
RCL = [("Anthropic", "CLI reference", "Commands, flags, version notes", "Current; read via fetch")]

SPECS.append(G(M, "14.3.1", "Common flags: print mode, sessions, permissions, worktrees, debug",
 "Command-line flags set a session's behaviour before it starts, and the useful ones group into five jobs: scripting, session selection, permission control, isolation and debugging.",
 "run one scripted call with -p and an output format, one resumed-and-forked session, and one debug capture to a file.",
 "pick flags by job, and prefer a narrow permission flag to a broad one.",
 "--bare skips auto-discovery of hooks, skills, plugins, MCP servers, auto memory and CLAUDE.md, so a scripted call behaves differently from your interactive setup " + CL + ".",
 26, "3", ["Name the flags by job", "Compose a scripted call with limits", "Design flag defaults for CI"],
 "Five working command lines, one per job, each run once with its observed output or effect.",
 [S("Scripting: -p and friends", "`-p`/`--print` prints the response without interactive mode. `--output-format` takes `text`, `json` or `stream-json`; `--input-format` takes `text` or `stream-json`; `--max-turns` limits agentic turns and exits with an error at the limit; `--max-budget-usd` stops once estimated spend reaches the amount, checked against a client-side estimate that can differ from your bill; `--no-session-persistence` stops sessions being saved; `--bare` gives minimal startup " + CL + ".",
   """
```bash
claude -p "summarise failing tests" --output-format json --max-turns 5 --max-budget-usd 2
claude --bare -p "explain this stack trace" < trace.txt
```

| Flag | Print mode only? |
|---|---|
| `--max-turns`, `--max-budget-usd` | Yes |
| `--no-session-persistence` | Yes |
| `--output-format` | Yes |
| `--bare` | Works with `-p`; shown with it |
""", "Budget-as-bill", "You treat `--max-budget-usd` as an exact spending ceiling, but it is checked against a client-side estimate and spend can pass it.", "Leave headroom under the real limit and confirm against your billing.", "headless use is Module 8.1; cost is Module 1.4.", "the cap is an estimate."),
  S("Sessions: -c, -r, -n, --fork-session, --from-pr, --teleport, --cloud", "`--continue`/`-c` loads the most recent conversation in the current directory and skips `-p` and SDK sessions unless combined with `-p`; `--resume`/`-r` takes an ID, name or picker; `--name`/`-n` names the session; `--fork-session` with resume creates a new session ID; `--from-pr` filters the picker to a pull request; `--teleport` resumes a cloud session locally; `--cloud` creates a cloud session from a task " + CL + ".",
   """
```bash
claude -n "auth-refactor"
claude --resume auth-refactor --fork-session
claude --from-pr 123
claude --cloud "Fix the login bug"
```

| Need | Flag |
|---|---|
| Latest here | `-c` |
| Specific one | `-r <id or name>` |
| Same history, new ID | `-r X --fork-session` |
| Everything for a PR | `--from-pr` |
""", "Continue-misses-sdk", "You run `claude -c` expecting your last scripted `-p` run and it skips it.", "Use `claude -p --continue` for those, or resume by ID.", "sessions are Module 2.4; cloud is Module 6.3.", "-c skips -p sessions unless -p is also given."),
  S("Control and isolation", "`--permission-mode` begins in a mode (`default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions` or `manual`, which needs v2.1.200 or later). `--allowedTools` lists tools that run without prompting and `--disallowedTools` denies them; a bare name removes the tool from Claude's context while a scoped rule denies only matching calls. `--worktree`/`-w` starts in an isolated git worktree under `<repo>/.claude/worktrees/<name>`; `--agent` selects an agent; `--settings` takes a file or inline JSON up to 2 MiB " + CL + ".",
   """
```bash
claude -w feature-auth --permission-mode plan
claude --allowedTools "Bash(git log *)" "Bash(git diff *)" "Read"
claude --settings '{"model": "claude-opus-5-5"}'
```

| Flag | Scope |
|---|---|
| `--allowedTools` | Run without prompting |
| `--disallowedTools "Edit"` | Remove Edit entirely |
| `--disallowedTools "Bash(rm *)"` | Deny matching calls only |
""", "Allow-is-not-restrict", "You use `--allowedTools` to limit what Claude can use, but it only skips prompts; `--tools` restricts availability.", "Use `--tools` or `--disallowedTools` to restrict, `--allowedTools` to pre-approve.", "permissions are Module 4.2; worktrees are Module 6.2.", "allow skips prompts; it does not restrict."),
  S("Debugging", "`--debug` enables debug mode with optional categories such as `--debug='mcp,startup'`; the filter binds only in the `=` form. `--debug-file <path>` writes logs to a file, implies debug and beats `CLAUDE_CODE_DEBUG_LOGS_DIR`. `--verbose` shows full turn-by-turn output. `--init-only` runs Setup and SessionStart hooks and exits; `--init` and `--maintenance` run Setup hooks with those matchers in print mode " + CL + ".",
   """
```bash
claude --debug='mcp,startup' --debug-file /tmp/claude-debug.log
claude --init-only
```
""", "Space-separated-filter", "You write `--debug mcp` with a space and get unfiltered debug output.", "Use the `=` form for category filters.", "debugging is Part 12; hooks are Module 14.5.", "category filters need an equals sign.")],
 [("Which flag prints and exits?", "`-p` / `--print`."), ("Which output formats does `--output-format` accept?", "text, json, stream-json."),
  ("You treat `--max-budget-usd` as exact. Name the failure mode by its exact label.", "**Budget-as-bill.**"), ("Which flag gives a new session ID when resuming?", "`--fork-session`."),
  ("Your last `-p` run is skipped by `claude -c`. Name the failure mode.", "**Continue-misses-sdk.**"), ("Which flag restricts tools rather than pre-approving them?", "`--tools` (or `--disallowedTools`)."),
  ("You use `--allowedTools` to restrict. Name the failure mode and fix.", "**Allow-is-not-restrict.** Use `--tools` or `--disallowedTools`."), ("What is the size limit of a `--settings` file?", "2 MiB."),
  ("You write `--debug mcp`. Name the failure mode.", "**Space-separated-filter.**"), ("What does `--init-only` do?", "Runs Setup and SessionStart hooks and exits.")],
 [("Run a `-p` call with json output", "Output"), ("Add `--max-turns 2` and hit it", "Error text"), ("Name, resume and fork a session", "Three IDs"), ("Start with `-w` and list the worktree path", "Path"), ("Run with `--debug-file` and grep the log", "Excerpt"), ("Run `--bare` and compare startup", "Note")],
 """
| Job | Command | Observed |
|---|---|---|
| Script | `-p ... --max-turns 2` | Exited with limit error |
| Fork | `-r X --fork-session` | New ID |
| Isolate | `-w feat` | Worktree under .claude/worktrees |
""", """
| Element | What is wrong |
|---|---|
| Flags listed but never run | No evidence |
| `--allowedTools` as restriction | **Allow-is-not-restrict** |
""", "The artifact passes only if every command line was run and its output or effect captured.",
 RES(RCL, "none found between the sources read; the syllabus lists `--allowedTools` as a common flag but `--tools` is the restriction flag per the CLI reference."),
 RF("flags", "choose by job and run before trusting", "which flag do I need?", "what job is this and what did the flag actually do when I ran it?")))

SPECS.append(G(M, "14.3.2", "Subcommands: mcp, plugin, agents, auth, purge, update and more",
 "Subcommands manage things outside a conversation: servers, plugins, background sessions, accounts and local state, and several are scriptable.",
 "run claude doctor, claude auth status and a dry-run purge and explain each result.",
 "dry-run anything destructive first.",
 "the old name claude project purge in some notes is claude purge in the CLI reference; always confirm names against the current page " + CL + ".",
 24, "2.5", ["Name subcommands by area", "Script them safely", "Plan state cleanup"],
 "A subcommand sheet with a dry-run, a status JSON and a doctor result captured.",
 [S("Accounts and health", "`claude auth login` supports `--email`, `--sso` and `--console`; `claude auth logout`; `claude auth status` prints JSON (or text with `--text`), exits 0 if logged in and 1 if not, with `authMethod` one of none, claude.ai, oauth_token, api_key, api_key_helper or third_party. `claude doctor` prints read-only installation and settings diagnostics without starting a session. `claude setup-token` generates a long-lived OAuth token for CI and needs a subscription " + CL + ".",
   """
```bash
claude auth status --text
claude doctor
```

| Command | Mutates? |
|---|---|
| `claude auth status` | No |
| `claude doctor` | No (read-only) |
| `claude setup-token` | Prints token; not saved |
""", "Token-in-log", "You run `claude setup-token` in a CI log or shared terminal and the printed token ends up stored.", "Run it locally, copy to a secret store and never echo it in logs.", "CI auth is Module 8.1; security is Module 11.1.", "treat the token as a secret."),
  S("Extensions and servers", "`claude mcp` configures MCP servers; `claude mcp login <name>` runs OAuth for HTTP, SSE and connector servers and `--no-browser` prints the URL over SSH; `claude mcp logout <name>` clears credentials. `claude plugin` manages plugins (alias `claude plugins`), for example `claude plugin install code-review@claude-plugins-official`. `claude update` updates and `claude install [version]` installs a version, `stable` or `latest` " + CL + ".",
   """
```bash
claude mcp login sentry --no-browser
claude plugin install code-review@claude-plugins-official
claude install stable
```
""", "Unpinned-install", "You install `latest` on a team machine and versions drift between teammates.", "Pin with `claude install <version>` where reproducibility matters.", "MCP is Module 5.5; plugins are Module 5.6; admin rollout is Module 10.1.", "pin versions for teams."),
  S("Background sessions", "`claude agents` opens agent view (`--json` for scripting, `--json --all` including completed); `claude attach <id|name>`, `claude logs <id|name>`, `claude respawn <id>`, `claude stop <id>` (also `claude kill`) and `claude rm <id>` manage background sessions; `claude daemon status|logs|run|stop` manage the supervisor. Name matching in attach and logs needs v2.1.290 or later " + CL + ".",
   """
| Need | Command |
|---|---|
| List | `claude agents --json` |
| Read output | `claude logs <id>` |
| Resume work | `claude attach <id>` |
| Restart all | `claude respawn --all` |
| Stuck supervisor | `claude daemon status`, then `stop` |
""", "Orphan-sessions", "You leave background sessions running and later cannot tell which are alive or consuming usage.", "List with `claude agents` and stop what you do not need.", "background sessions are Module 6.3.", "list before you leave."),
  S("State cleanup", "`claude purge [path]` deletes all local state for a project: transcripts, task lists, debug logs, file-edit history, prompt history lines and the project's entry in `~/.claude.json`; flags are `--dry-run`, `-y`, `-i` and `--all` " + CL + ".",
   """
```bash
claude purge --dry-run
claude purge ./old-project -i
```
""", "Purge-without-preview", "You run `claude purge --all -y` and delete transcripts you needed.", "Always run `--dry-run` first and use `-i` to confirm items.", "transcript retention is Module 11.1.", "preview before you purge.")],
 [("Which command prints read-only install diagnostics?", "`claude doctor`."), ("What exit code does `claude auth status` return when not logged in?", "1."),
  ("A setup-token value ends up in a log. Name the failure mode by its exact label.", "**Token-in-log.**"), ("Which flag prints an OAuth URL over SSH?", "`--no-browser` on `claude mcp login`."),
  ("You install latest on every machine. Name the failure mode.", "**Unpinned-install.**"), ("Which version enables name matching for attach and logs?", "v2.1.290."),
  ("Background sessions pile up unseen. Name the failure mode and fix.", "**Orphan-sessions.** List with `claude agents` and stop."), ("Which flag previews a purge?", "`--dry-run`."),
  ("You purge everything with -y. Name the failure mode.", "**Purge-without-preview.**"), ("What is the alias of `claude plugin`?", "`claude plugins`.")],
 [("Run `claude auth status --text`", "Output"), ("Run `claude doctor`", "Output"), ("Run `claude agents --json`", "Output"), ("Run `claude purge --dry-run`", "Preview"), ("Check `claude --help` for any renamed subcommand", "Note"), ("Write the sheet", "Table")],
 """
| Command | Result |
|---|---|
| `claude auth status` | api_key, exit 0 |
| `claude doctor` | No errors |
| `claude purge --dry-run` | 3 projects listed |
""", """
| Element | What is wrong |
|---|---|
| Purge run live first | **Purge-without-preview** |
""", "The artifact passes only if destructive commands were previewed and names were checked against the current CLI reference.",
 RES(RCL, "the syllabus lists `claude project purge` while the CLI reference lists `claude purge`. **The CLI reference wins; confirm with `claude --help`.**"),
 RF("subcommands", "preview, pin and list", "what does this subcommand do?", "does it mutate state, and have I previewed it?")))

if __name__ == "__main__":
    run(SPECS)
