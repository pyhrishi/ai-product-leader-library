import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen import write
from specs_12 import T

M = "b-8-2"
SPECS = []
AL = "Agent SDK docs, How the agent loop works, 2026"
CF = "Agent SDK docs, Configure your agent, 2026"
SP = "Agent SDK docs, Modifying system prompts, 2026"
CC = "Agent SDK docs, Use Claude Code features in the SDK, 2026"
SK = "Agent SDK docs, Extend agents with skills, 2026"
PL = "Agent SDK docs, Plugins in the SDK, 2026"

# ------------------------------------------------------------------ 8.2.1
SPECS.append(dict(
 mod=M, id="8.2.1", title="Message lifecycle, tool execution, context window and architecture", short="Loop lifecycle, tools and context",
 thesis="One query() call is a sequence of turns; each turn yields messages, runs tools, and grows a context window that the SDK compacts when it nears its limit, and every limit, hook and result subtype attaches to that sequence.",
 prove="given a transcript of SDK messages, label each turn, name the message type of every item, and predict which result subtype ends the run.",
 discipline="read the message stream as the ground truth of the loop before changing any option.",
 counter="the loop ends when Claude produces a response with no tool calls, not when your task is done, so success means the model stopped, and only your check says the work is right [" + AL + "].",
 read_min=22, prove_h="2", depth=["Label turns and message types in a stream", "Predict tool concurrency, compaction and the ending subtype", "Design limits and context hygiene for a long-running agent"],
 deliverable="An annotated transcript of a real SDK run: turns numbered, message types named, tool calls classed as concurrent or sequential, and the ResultMessage fields recorded.",
 sections=[
 dict(title="The cycle and its messages", framing="Every session follows five steps: receive the prompt (a SystemMessage with subtype init), evaluate and respond (AssistantMessage), execute tools, repeat, and return the result (a final AssistantMessage then a ResultMessage). A turn is one round trip: Claude's output with tool calls, SDK execution, and results fed back without yielding control to your code [" + AL + "].",
  body=T("""
| Message type | Emitted when | Note |
|---|---|---|
| SystemMessage | Session lifecycle: `init`, `compact_boundary`, `informational`, `worker_shutting_down` | Subtype distinguishes them |
| AssistantMessage | After each Claude response, including the final text-only one | Text and tool-call blocks |
| UserMessage | After each tool execution, and for inputs you stream mid-loop | Carries tool results |
| StreamEvent | Only when partial messages are enabled | Raw API streaming events |
| ResultMessage | Marks the end | Final text, usage, cost, session id |

[Agent SDK docs, How the agent loop works, 2026]. Worked example from the docs: 'Fix the failing tests in auth.ts' took four turns, three with tool calls and one final text-only response [same page]. A few system events, such as prompt_suggestion, can arrive after the ResultMessage, so iterate to completion instead of breaking on the result.
"""),
  fm=[("Early-break read", "You break out of the stream on the ResultMessage and miss trailing system events and cleanup, or you never drain the iterator and leak the subprocess.", "Iterate the stream to completion and treat the ResultMessage as the end of the loop, not the end of the stream.")],
  xr="streaming output is Module 8.4.2; the Claude Code loop it mirrors is Module 1.2.", one="a turn is a tool round trip, and the ResultMessage ends the loop."),
 dict(title="Tool execution: concurrency and permission", framing="Tool calls in a turn run concurrently or sequentially depending on the tool: read-only tools such as Read, Glob, Grep and MCP tools marked read-only can run concurrently, while Edit, Write and Bash run sequentially. Custom tools default to sequential unless readOnlyHint is set [" + AL + "].",
  body=T("""
| Option | Effect | Detail |
|---|---|---|
| `allowed_tools` / `allowedTools` | Auto-approves listed tools | Unlisted tools remain available but need permission |
| `disallowed_tools` / `disallowedTools` | Blocks listed tools | Regardless of other settings |
| `permission_mode` / `permissionMode` | Oversight level | default, acceptEdits, plan, dontAsk, auto, bypassPermissions |

[Agent SDK docs, How the agent loop works, 2026]. A denied call returns a rejection message as the tool result, and Claude typically tries another approach or reports it cannot proceed. bypassPermissions cannot run as root on Unix and, in TypeScript, also requires allowDangerouslySkipPermissions: true [same page].
"""),
  fm=[("Allowlist-as-sandbox", "You list three tools in allowed_tools and assume nothing else can run, but unlisted tools stay available and fall through to the permission mode.", "Use disallowed tools or dontAsk mode when you need a hard deny, and keep allowed tools for auto-approval only.")],
  xr="permissions in depth are Module 8.6.1; built-in tools are Module 8.3.1.", one="allowed means pre-approved, not exclusive."),
 dict(title="Limits, effort and the result subtype", framing="Two caps bound a loop: max_turns (tool-use round trips only) and max_budget_usd. Both default to no limit, and hitting one returns a ResultMessage with error_max_turns or error_max_budget_usd [" + AL + "]. The budget cap includes subagent spend and, from Claude Code v2.1.217, spawning another subagent past the cap fails with 'Budget limit reached' [same page].",
  body=T("""
| Subtype | Meaning | `result` present |
|---|---|---|
| success | Finished normally | Yes |
| error_max_turns | Hit turn cap | No |
| error_max_budget_usd | Hit budget cap | No |
| error_during_execution | API failure or cancelled request | No |
| error_max_structured_output_retries | No valid structured output within retry limit | No |

[Agent SDK docs, How the agent loop works, 2026]. A single-shot query() yields the error result and then raises; wrap the loop in try/except. In configuration, max_turns 0 means no limit, while max_budget_usd 0 is rejected by the CLI at startup [Agent SDK docs, Configure your agent, 2026]. The effort option takes low, medium, high, xhigh and max; if unset the SDK defers to the model default.
"""),
  fm=[("Zero-budget trap", "You pass max_budget_usd=0 expecting 'no spend allowed' and the session never starts, while max_turns=0 silently means unlimited.", "Leave options unset to mean no cap, and use a small positive number for a tight budget.")],
  xr="cost tracking is Module 8.6.3; failure handling is Module 8.7.5.", one="every cap has a subtype, and zero does not mean the same thing for both caps."),
 dict(title="The context window and compaction", framing="The context window accumulates across turns: system prompt, tool definitions, conversation history, tool inputs and outputs. Stable content such as system prompt, tool definitions and CLAUDE.md is prompt cached. When the window nears its limit, the SDK compacts: it summarizes older history and emits a SystemMessage with subtype compact_boundary [" + AL + "].",
  body=T("""
| Source | When it loads | Impact |
|---|---|---|
| System prompt | Every request | Small fixed cost |
| CLAUDE.md | Session start, via settingSources | Full content every request (cached) |
| Tool definitions | Every request; MCP schemas deferred by default | Built-in schemas always load |
| Conversation history | Accumulates | Grows each turn |
| Skill descriptions | Session start | Short; full content on invoke |

[Agent SDK docs, How the agent loop works, 2026]. Compaction can drop early instructions, so persistent rules belong in CLAUDE.md, which is re-injected on every request. Customize with a summary-instructions section in CLAUDE.md, a PreCompact hook (trigger is manual or auto), or send /compact as a prompt. Each subagent starts fresh, and only its final response returns to the parent.
"""),
  fm=[("Prompt-borne rules", "You put a hard rule only in the first prompt, a long run compacts, and the rule is summarized away.", "Move persistent rules into CLAUDE.md or the system prompt and add a PreCompact hook to archive the transcript.")],
  xr="system prompts are Module 8.2.3; subagents are Module 8.3.5; hooks are Module 8.6.2.", one="rules that must survive compaction live outside the conversation."),
 ],
 retrieval=[
  ("Name the five core message types.", "SystemMessage, AssistantMessage, UserMessage, StreamEvent and ResultMessage."),
  ("What marks the end of the agent loop, and what can still arrive after it?", "The ResultMessage; trailing system events such as prompt_suggestion can still arrive."),
  ("You break on the ResultMessage and skip the rest of the stream. Name the failure mode by its exact label.", "**Early-break read.**"),
  ("In the docs' auth.ts example, how many turns occurred?", "Four: three with tool calls and one final text-only turn."),
  ("Which tools can run concurrently?", "Read-only tools such as Read, Glob, Grep and MCP tools marked read-only; Edit, Write and Bash run sequentially."),
  ("You list three tools in allowed_tools and assume the rest are blocked. Name the failure mode.", "**Allowlist-as-sandbox.**"),
  ("What happens with max_budget_usd=0 versus max_turns=0?", "max_budget_usd 0 is rejected at startup so the session never runs; max_turns 0 means no limit. This is the Zero-budget trap."),
  ("A rule given only in the first prompt vanishes in a long run. Name the failure mode and fix.", "**Prompt-borne rules.** Put it in CLAUDE.md or the system prompt."),
  ("Which five effort levels exist?", "low, medium, high, xhigh and max."),
  ("A cap is hit by a single-shot query(). What does the SDK do after yielding the error result?", "It raises an error, so wrap the loop in try/except."),
 ],
 steps=[("Run a multi-tool task with include of every message printed", "A raw transcript"), ("Number the turns and label each message with its type", "An annotated transcript"),
        ("Mark each tool call concurrent or sequential", "A labelled list"), ("Record ResultMessage fields: subtype, turns, cost, session id", "A 4-field table"),
        ("Force each cap with a tiny max_turns, then a tiny budget; record the subtypes", "Two observations"), ("Trigger /compact in a session with history and capture compact_boundary", "A boundary message")],
 pass_md=T("""
| Turn | Message | Content |
|---|---|---|
| 0 | SystemMessage init | session id, tools |
| 1 | AssistantMessage + UserMessage | Bash npm test; 3 failures |
| 2 | AssistantMessage + UserMessage | Read x2 (concurrent) |
| 3 | AssistantMessage + UserMessage | Edit then Bash (sequential) |
| 4 | AssistantMessage, ResultMessage | final text; subtype success |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Transcript stops at the ResultMessage | **Early-break read** |
| Edit and Bash marked concurrent | They run sequentially |
| Budget test used 0 | **Zero-budget trap** |
"""),
 verdict="The artifact passes only if every message is typed, concurrency labels match the rules, and both cap subtypes were reproduced rather than assumed.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | How the agent loop works | Messages, caps, compaction, results | Current |
| Anthropic | Configure your agent | Zero-value behaviour of caps | Current |
| Anthropic | Claude Code: How Claude Code works | The loop in the CLI | Current |
""") + "\n\n*Disagreement named:* none found between the pages; the loop page describes turns as tool round trips, while the Claude Code CLI glossary defines a turn as everything between your message and the finished answer. Use the SDK page's definition when setting max_turns.",
 reframe="This is the craft of the loop as an event stream: **turns, messages, caps and a window that compacts.** The engineer who understands this debugs from the transcript and never from guesses.",
))

# ------------------------------------------------------------------ 8.2.2
SPECS.append(dict(
 mod=M, id="8.2.2", title="The options object", short="The options object",
 thesis="The options object is the single place an SDK agent is configured, so every behaviour you want must be traceable to one field, one settings source or one environment variable.",
 prove="write the options object for a read-only reviewer agent and justify each field by what it controls and what its default would have done instead.",
 discipline="set every option that matters explicitly and leave the rest visibly unset.",
 counter="options silently differ between languages: in TypeScript the env option replaces the subprocess environment, in Python it merges over it [" + CF + "].",
 read_min=20, prove_h="2", depth=["Compose an options object and say what each field controls", "Predict behaviour from defaults and cross-language differences", "Change configuration mid-session safely"],
 deliverable="A commented options object in your language plus a table of ten fields: name, purpose, default, and the page that covers it.",
 sections=[
 dict(title="Fields, defaults and where each is documented", framing="Every query() call accepts Options (TypeScript) or ClaudeAgentOptions (Python). Each field is optional, and a session with no options runs with the SDK's defaults [" + CF + "].",
  body=T("""
| TypeScript | Python | Controls |
|---|---|---|
| permissionMode | permission_mode | What the agent can do without approval |
| allowedTools | allowed_tools | Pre-approved tool calls |
| canUseTool | can_use_tool | Your approval callback |
| systemPrompt | system_prompt | Agent instructions |
| settingSources | setting_sources | Which filesystem settings load |
| mcpServers | mcp_servers | External tool servers |
| agents | agents | Subagent definitions |
| hooks | hooks | Lifecycle callbacks |
| outputFormat | output_format | Structured output schema |
| resume / forkSession | resume / fork_session | Session continuation and branching |
| sessionStore | session_store | External persistence |
| enableFileCheckpointing | enable_file_checkpointing | Rewindable edits |
| effort | effort | How much work Claude puts in |
| sandbox | sandbox | Sandbox behaviour for tool execution |

[Agent SDK docs, Configure your agent, 2026]. The temperature, top_p and max_tokens request parameters have no fields; use effort or a spend cap, or call the Messages API [same page].
"""),
  fm=[("Phantom parameter", "You search for a temperature or max_tokens option on the options object, find none, and add a prompt instruction that the model cannot honour.", "Use effort and spend caps, or call the Messages API when you need sampling parameters.")],
  xr="field-by-field depth is Module 8.2.3 to Module 8.2.5 and Module 8.3 to Module 8.6.", one="every option has a page; the table is the map."),
 dict(title="Model, fallback and effort", framing="If you do not set model, a new session uses Claude Code's default model, which depends on settings and environment. Setting model pins one; aliases and full names are accepted. fallbackModel (fallback_model) names a backup used when the primary is overloaded or unavailable, and the primary is retried at the start of each user turn [" + CF + "].",
  body=T("""
```typescript
const options = {
  model: "claude-sonnet-5",
  fallbackModel: "claude-opus-5,claude-sonnet-5",   // single model or comma-separated list
  effort: "medium",
};
```
[Agent SDK docs, Configure your agent, 2026] (illustrative values; use the model ids you have access to). In TypeScript, a fallback equal to model throws at startup. Switching model mid-session recomputes the whole conversation uncached at the new model's rates because each model has its own prompt cache.
"""),
  fm=[("Silent default model", "You never set model, the session picks whatever Claude Code's default resolves to for that account, and costs or behaviour change when the default changes.", "Pin model explicitly in production and log the model from each AssistantMessage.")],
  xr="cost tracking is Module 8.6.3; effort levels are in Module 8.2.1.", one="pin the model, then log which model answered."),
 dict(title="Environment, working directory and settings", framing="The env option sets variables for the Claude Code process. In TypeScript it replaces the subprocess environment, so spread process.env to keep PATH, HOME and ANTHROPIC_API_KEY; in Python your values merge over the inherited ones. If unset, the subprocess inherits your environment in both [" + CF + "].",
  body=T("""
| Option | Behaviour | Gotcha |
|---|---|---|
| env (TS) | Replaces environment | Forgetting `...process.env` drops the API key |
| env (Python) | Merges over inherited | Your values win |
| cwd | Working directory of the session | No setter; start another session to change it |
| additionalDirectories / add_dirs | Extra paths tools can reach | Grants file access, not configuration |
| settings | Path, inline JSON (TS also object) | Overrides user, project and local settings |
| settingSources | [] disables user/project/local | Managed policy still applies |

[Agent SDK docs, Configure your agent, 2026]. cwd decides which project's settings, hooks, skills and stored sessions apply.
"""),
  fm=[("Env wipe", "In TypeScript you pass env with only ANTHROPIC_BASE_URL, the subprocess loses PATH, HOME and the API key, and the agent fails to start or authenticate.", "Spread process.env first, then add your overrides.")],
  xr="multi-tenant isolation with env and cwd is Module 8.7.3.", one="env semantics differ by language; spread in TypeScript."),
 dict(title="Changing configuration mid-session", framing="With streaming input you can switch model and permission mode while the session runs: setModel and setPermissionMode on the Query object in TypeScript, set_model and set_permission_mode on ClaudeSDKClient in Python. Calling setModel with no model switches to Claude Code's default, not your options model [" + CF + "].",
  body=T("""
| Method | TypeScript | Python |
|---|---|---|
| Switch model | `query.setModel()` | `client.set_model()` |
| Switch permission mode | `query.setPermissionMode()` | `client.set_permission_mode()` |
| Apply runtime settings | `applyFlagSettings()` | not listed |
| Write local settings | `updateSettings()` | not listed |

[Agent SDK docs, Configure your agent, 2026]. query() in Python returns a plain iterator without control methods, so use ClaudeSDKClient. Check the reference for which keys applyFlagSettings accepts.
"""),
  fm=[("Cache-reset switch", "You switch models between turns of a long session and the next request pays full uncached cost for the entire history.", "Switch at session boundaries, or accept the one-time recompute and measure it in the cache token fields.")],
  xr="streaming input is Module 8.4.1; prompt caching is Module 8.6.3.", one="mid-session changes are possible, and the cache pays for them."),
 ],
 retrieval=[
  ("What are the options types in TypeScript and Python?", "Options and ClaudeAgentOptions."),
  ("A developer looks for a temperature field on the options object. Name the failure mode by its exact label.", "**Phantom parameter.**"),
  ("Which Messages API parameters have no options field?", "temperature, top_p and max_tokens."),
  ("What does fallbackModel do and when is the primary retried?", "It names a backup used when the primary is overloaded or unavailable; the primary is retried at the start of each user turn."),
  ("You never set model and behaviour changes after a platform update. Name the failure mode.", "**Silent default model.**"),
  ("In TypeScript you set env with one variable and the agent cannot authenticate. Name the failure mode and fix.", "**Env wipe.** Spread process.env first."),
  ("How does env differ between TypeScript and Python?", "TypeScript replaces the subprocess environment; Python merges your values over the inherited ones."),
  ("Is there a setter for cwd?", "No; start another session with the new cwd."),
  ("You switch models mid-session and cost jumps. Name the failure mode by its exact label.", "**Cache-reset switch.**"),
 ],
 steps=[("List ten options with purpose, default and page", "A 10-row table"), ("Write an options object for a read-only reviewer", "A commented object"),
        ("Pin model and set a fallback; log the model per turn", "A log line"), ("Test env in TypeScript with and without the spread", "Two outcomes"),
        ("Switch model mid-session and record cache token fields before and after", "A 2-row table"), ("Document which fields you left unset on purpose", "A short list")],
 pass_md=T("""
| Field | Value | Why |
|---|---|---|
| model | pinned | no silent default |
| allowedTools | Read, Glob, Grep | read-only pre-approval |
| maxTurns / maxBudgetUsd | 20 / small positive | bounded loop |
| settingSources | [] | isolation |
| env | {...process.env, ...} | keeps key and PATH |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| env without spread | **Env wipe** |
| No model set | **Silent default model** |
| budget 0 'to be safe' | CLI rejects it |
"""),
 verdict="The artifact passes only if every field has a reason, model and limits are explicit, and the env behaviour was tested in your language.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Configure your agent | Field map, env, cwd, fallback | Current |
| Anthropic | TypeScript and Python references | Full option types | Current; not read in full |
| Anthropic | Model configuration | Aliases and fallback chains | Referenced, not read |
""") + "\n\n*Disagreement named:* none found; the full option list lives in language references that were not read here, so treat the table as the documented subset.",
 reframe="This is the craft of configuration: **one object, explicit defaults, language-specific traps.** The engineer who understands this can answer why the agent did something from the options alone.",
 thin="Language reference pages (full Options and ClaudeAgentOptions types) were not read; the guide covers the configuration page's documented subset.",
))

# ------------------------------------------------------------------ 8.2.3
SPECS.append(dict(
 mod=M, id="8.2.3", title="System prompts: preset, append and custom", short="System prompts in the SDK",
 thesis="The SDK starts with a minimal system prompt, and you choose among the claude_code preset, the preset plus append, or a fully custom prompt, with CLAUDE.md and output styles layered alongside.",
 prove="pick a starting point for four agents, justify each against the comparison table, and demonstrate which safety and tool guidance each one keeps.",
 discipline="choose the starting point by how closely your agent resembles Claude Code, not by which is shortest.",
 counter="CLAUDE.md is not part of the system prompt: the SDK injects it into the conversation, which is why it survives any prompt choice and does not affect the system prompt cache [" + SP + "].",
 read_min=21, prove_h="2", depth=["Choose among preset, append and custom", "Predict what each choice keeps or loses", "Tune prompt caching across users and machines"],
 deliverable="A decision table for four agents with the exact systemPrompt value, plus a measured cache comparison with and without excludeDynamicSections.",
 sections=[
 dict(title="Three starting points", framing="Without systemPrompt the SDK uses a minimal prompt that covers tool calling but omits the claude_code preset's security instructions and working-directory context; this differs from claude -p, which uses the Claude Code prompt by default [" + SP + "].",
  body=T("""
| You are building | Use | You get |
|---|---|---|
| CLI/IDE-like coding tool, human steering | claude_code preset | Tool guidance, safety rules, environment context |
| Same plus product rules | preset with `append` | Everything, with your text after it; lowest risk |
| Different surface, identity or permission model; non-coding | Custom string | Only what you write; you replace tool guidance and safety |
| Thin tool-calling loop | No systemPrompt | Minimal default |

```python
system_prompt={"type": "preset", "preset": "claude_code", "append": "Always include type hints."}
```
[Agent SDK docs, Modifying system prompts, 2026]. Unattended coding automation, such as a CI job fixing lint, still fits the preset [same page].
"""),
  fm=[("Bare-prompt assumption", "You leave systemPrompt unset, expect CLI-like behaviour, and the agent lacks the preset's safety and environment guidance.", "Set the claude_code preset explicitly, or write a custom prompt that replaces what you need.")],
  xr="migration default is Module 8.1.2.", one="the default is minimal; opt in to the preset."),
 dict(title="CLAUDE.md and output styles", framing="CLAUDE.md is read when the matching setting source is enabled: project loads CLAUDE.md or .claude/CLAUDE.md from the working directory; user loads ~/.claude/CLAUDE.md. It is not loaded with an empty settingSources array [" + SP + "].",
  body=T("""
| Feature | Persistence | Default tools | Built-in safety | Customization |
|---|---|---|---|---|
| CLAUDE.md | Per-project file | Preserved | Maintained | Additions only |
| Output styles | Saved files | Preserved | Maintained | Replace or extend default |
| systemPrompt + append | Session only | Preserved | Maintained | Additions only |
| Custom systemPrompt | Session only | Lost unless included | Must be added | Complete |

[Agent SDK docs, Modifying system prompts, 2026]. An output style is a markdown file in ~/.claude/output-styles/ or .claude/output-styles/; a custom style drops the preset's software engineering instructions unless keep-coding-instructions: true is set. In TypeScript, outputStyle goes inside the settings object; Python has no programmatic option to select one.
"""),
  fm=[("Style-in-code assumption", "In Python you expect to select an output style by option, find none, and ship an agent with the wrong persona.", "Use append or a custom string in Python, or write the style into settings the session loads.")],
  xr="settings sources are Module 8.2.4.", one="CLAUDE.md and styles ride on settings sources; append and custom ride in code."),
 dict(title="Custom prompts and their limits", framing="A custom string replaces the default entirely: the SDK sends only what you provide. In Python, a large prompt can fail at process spawn because the string is passed as one command-line argument; the docs recommend system_prompt={'type':'file','path':...}, and on Linux the error is 'Argument list too long' [" + SP + "].",
  body=T("""
| Form | Language | Note |
|---|---|---|
| String | Both | Replaces the default |
| `{type: preset, preset: claude_code, append}` | Both | Keeps preset |
| `{type: file, path}` | Python | Avoids argument-length failure |
| Array with `SYSTEM_PROMPT_DYNAMIC_BOUNDARY` | TypeScript | Splits static from per-request text, each with its own cache breakpoint |

[Agent SDK docs, Modifying system prompts, 2026]. The split applies only when the SDK calls the Claude API directly or runs on Claude Platform on AWS; elsewhere the whole prompt is sent as one block.
"""),
  fm=[("Argument-length crash", "A 200-line Python prompt string exceeds the OS argument limit and fails at spawn before any API request.", "Load large prompts from a file with the file form.")],
  xr="hosting differences are Module 8.7.", one="size and cache shape belong in the design of a custom prompt."),
 dict(title="Prompt caching and prompt changes in resumed sessions", framing="Two sessions with the same preset and append still miss the cache from different working directories, because the preset embeds working directory, git status, platform, shell, OS version and auto-memory paths. excludeDynamicSections: true (exclude_dynamic_sections in Python) moves that context into the first user message so identical configurations share a cache entry [" + SP + "].",
  body=T("""
| Version floor | Feature |
|---|---|
| @anthropic-ai/claude-agent-sdk 0.2.98 / claude-agent-sdk 0.1.58 | excludeDynamicSections |
| TypeScript SDK 0.3.257 | `snapshot` field on systemPrompt |
| Claude Code 2.1.265 (bundled from TS SDK 0.3.265) | Recording append or custom prompt by default |

[Agent SDK docs, Modifying system prompts, 2026]. Tradeoff: instructions in the user message carry marginally less weight. By default the prompt is built once on a session's first request and recorded; a different append passed on resume takes effect after compaction or in a new session. Set snapshot: false to rebuild every request.
"""),
  fm=[("Ignored resume prompt", "You change append on a resumed call and the old prompt still governs, so a hot fix does not take effect.", "Start a new session, wait for compaction, or set snapshot false while iterating.")],
  xr="sessions are Module 8.5; caching metrics are Module 8.6.3.", one="a recorded prompt outlives the code that built it."),
 ],
 retrieval=[
  ("What does the SDK use when systemPrompt is unset?", "A minimal prompt covering tool calling, without the preset's safety and environment content."),
  ("You expect CLI-like behaviour with no systemPrompt. Name the failure mode by its exact label.", "**Bare-prompt assumption.**"),
  ("Which choice is called the lowest-risk customization?", "The claude_code preset with append."),
  ("Is CLAUDE.md part of the system prompt?", "No; the SDK injects it into the conversation, so it does not affect the system prompt cache."),
  ("A Python team wants to select an output style by option. Name the failure mode.", "**Style-in-code assumption.**"),
  ("What does a large Python custom prompt risk and how do you avoid it?", "An 'Argument list too long' failure at spawn (Argument-length crash); use the file form."),
  ("Which flag lets identical preset and append share a cache across directories?", "excludeDynamicSections (exclude_dynamic_sections in Python)."),
  ("You edit append on resume and nothing changes. Name the failure mode by its exact label.", "**Ignored resume prompt.**"),
  ("What SDK versions are needed for excludeDynamicSections?", "TypeScript 0.2.98 or later; Python 0.1.58 or later."),
 ],
 steps=[("List four agents and the surface, identity and permission model of each", "A 4-row brief"), ("Choose a starting point per agent and write the exact option value", "A decision table"),
        ("Run each with a hostile prompt and record what safety guidance holds", "Four observations"), ("Run two sessions from different cwds with and without excludeDynamicSections", "Cache token counts"),
        ("Change append on resume and record the effect", "One observation"), ("Write the CLAUDE.md summary instructions section", "A snippet")],
 pass_md=T("""
| Agent | Value | Reason |
|---|---|---|
| PR reviewer in CI | preset + append, exclude dynamic | Unattended coding; shared cache |
| Support bot | custom string | Different identity and surface |
| Data analyst | custom from file | Large prompt, non-coding |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| No prompt option set 'because default is fine' | **Bare-prompt assumption** |
| Custom prompt of 400 lines inline in Python | **Argument-length crash** |
"""),
 verdict="The artifact passes only if each choice cites the comparison table and the cache claim is backed by measured token fields.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Modifying system prompts | Preset, append, custom, caching | Current |
| Anthropic | Output styles / How Claude remembers your project | Style files and CLAUDE.md | Referenced, not read |
| Anthropic | Migration guide | Default prompt change | Current |
""") + "\n\n*Disagreement named:* the CLI's claude -p uses the Claude Code prompt by default while the SDK uses a minimal one; the system prompts page states the difference directly.",
 reframe="This is the craft of the prompt layer: **a minimal default, an opt-in preset, and persistent context that rides in the conversation.** The engineer who understands this says exactly what the agent was told.",
))

# ------------------------------------------------------------------ 8.2.4
SPECS.append(dict(
 mod=M, id="8.2.4", title="Using Claude Code features in the SDK", short="Claude Code features in the SDK",
 thesis="settingSources decides which filesystem features reach your agent, and a handful of inputs ignore it, so knowing both lists is what makes an SDK agent predictable.",
 prove="given a settingSources value and a directory tree, list exactly which CLAUDE.md files, skills, hooks and settings load, and name three inputs that load anyway.",
 discipline="state settingSources explicitly in any deployed agent.",
 counter="settingSources: [] is not isolation: managed policy settings, ~/.claude.json, auto memory and claude.ai connectors can still load, so the docs warn against default options for multi-tenant isolation [" + CC + "].",
 read_min=21, prove_h="2", depth=["Predict what each settingSources value loads", "List the inputs settingSources does not control", "Choose the right feature for a goal"],
 deliverable="A load-map table for three settingSources values over a sample repository, and a list of the five always-read inputs with how to disable each.",
 sections=[
 dict(title="What each source loads", framing="Omitting settingSources is equivalent to ['user', 'project', 'local'], and query() then reads the same filesystem settings as the CLI. Passing [] disables user, project and local settings. cwd determines where project inputs are found [" + CC + "].",
  body=T("""
| Source | Loads | Location |
|---|---|---|
| project | settings.json and hooks; CLAUDE.md and rules; skills, commands, subagents | <cwd>/.claude/ for settings and hooks; cwd and every parent for CLAUDE.md and rules; cwd and parents up to repo root for skills, commands, agents |
| user | user settings.json, CLAUDE.md, rules, skills, commands, subagents | ~/.claude/ |
| local | CLAUDE.local.md, .claude/settings.local.json | <cwd>/.claude/; CLAUDE.local.md in cwd and parents |

[Agent SDK docs, Use Claude Code features in the SDK, 2026]. Project settings.json loads from <cwd>/.claude/ with no parent fallback. Child-directory CLAUDE.md files load on demand.
"""),
  fm=[("Wrong-cwd silence", "The agent runs from a different directory than the repo root and silently loads none of your project settings or hooks.", "Set cwd explicitly and verify the init message lists the skills and hooks you expect.")],
  xr="skills are Module 8.2.5; the CLI's equivalent is Module 1.2.", one="the sources are a union; cwd picks the project."),
 dict(title="What settingSources does not control", framing="Five inputs are read regardless of settingSources: managed policy settings, the global ~/.claude.json, auto memory at ~/.claude/projects/<project>/memory/, claude.ai MCP connectors (when authenticated with claude.ai login), and sandbox credentials deny and mask entries [" + CC + "].",
  body=T("""
| Input | How to disable |
|---|---|
| Managed policy settings | Remove the managed file/plist/registry policy; server-managed settings are controlled by an org Owner |
| ~/.claude.json | Relocate with CLAUDE_CONFIG_DIR in env |
| Auto memory | `autoMemoryEnabled: false` or CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 |
| claude.ai connectors | strictMcpConfig: true, disableClaudeAiConnectors: true, or ENABLE_CLAUDEAI_MCP_SERVERS=false; mcpServers: {} does not suppress them |
| sandbox credentials entries | Remove from ~/.claude/settings.json |

[Agent SDK docs, Use Claude Code features in the SDK, 2026]. The docs' multi-tenant recipe: each tenant in its own filesystem, settingSources [] and CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 in env.
"""),
  fm=[("Empty-list isolation", "You pass settingSources: [] and believe the agent is isolated, but it still loads auto memory from the host and any claude.ai connectors.", "Also disable auto memory, set strictMcpConfig, and give each tenant a separate filesystem.")],
  xr="multi-tenant isolation is Module 8.7.3; secure deployment is Module 8.7.4.", one="empty settingSources narrows loading; it does not isolate."),
 dict(title="Project instructions: levels and conflicts", framing="CLAUDE.md levels are additive: project, project rules, parent directories, local and user. There is no hard precedence rule, so conflicting instructions are resolved by how Claude interprets them; the docs advise non-conflicting rules or explicit precedence [" + CC + "].",
  body=T("""
| Level | Location | Loaded when |
|---|---|---|
| Project | <cwd>/CLAUDE.md or .claude/CLAUDE.md | project source |
| Project rules | .claude/rules/*.md in cwd and parents | project source |
| Parent dirs | CLAUDE.md above cwd | project source, at start |
| Child dirs | CLAUDE.md in subdirectories | project source, on demand |
| Local | CLAUDE.local.md | local source |
| User | ~/.claude/CLAUDE.md and rules | user source |

[Agent SDK docs, Use Claude Code features in the SDK, 2026]. State precedence in the specific file, for example 'These project instructions override any conflicting user-level defaults'.
"""),
  fm=[("Layered contradiction", "A user-level CLAUDE.md says one thing and the project file says another, and the agent obeys a different one on different runs.", "Remove the conflict or state precedence explicitly in the more specific file.")],
  xr="memory in Claude Code is Module 1.2; compaction and CLAUDE.md are in Module 8.2.1.", one="levels add up; they do not override."),
 dict(title="Hooks and choosing the right feature", framing="Two hook types run side by side: filesystem hooks in settings.json (command, http, mcp_tool, prompt, agent), and programmatic callbacks passed to query(). Both fire inside subagents; callback input carries agent_id and agent_type [" + CC + "].",
  body=T("""
| Goal | Use | SDK surface |
|---|---|---|
| Conventions the agent always follows | CLAUDE.md | settingSources project |
| Reference material loaded when relevant | Skills | settingSources + skills |
| Isolated subtask in a fresh context | Subagents | agents + allowedTools Agent |
| Deterministic logic on tool calls | Hooks | hooks callbacks or settings.json |
| Structured access to an external service | MCP | mcpServers |

[Agent SDK docs, Use Claude Code features in the SDK, 2026]. For PreToolUse, return {} for no decision; to block, return hookSpecificOutput with permissionDecision 'deny' and a reason that is sent to Claude. Python supports fewer hook events than TypeScript. Agent teams are a CLI feature not configured through SDK options [same page].
"""),
  fm=[("Hook-for-everything", "You encode a convention as a hook that blocks and retries when a line in CLAUDE.md would have done.", "Use CLAUDE.md for guidance and hooks for rules that must be enforced deterministically.")],
  xr="hooks as callbacks are Module 8.6.2; subagents are Module 8.3.5; MCP is Module 8.3.3.", one="guidance goes in files, enforcement goes in hooks."),
 ],
 retrieval=[
  ("What does omitting settingSources equal?", "['user', 'project', 'local']."),
  ("Which source loads CLAUDE.local.md?", "local."),
  ("The agent runs from the wrong directory and loads none of your config. Name the failure mode by its exact label.", "**Wrong-cwd silence.**"),
  ("Name three inputs read regardless of settingSources.", "Any three of: managed policy settings, ~/.claude.json, auto memory, claude.ai connectors, sandbox credentials entries."),
  ("You pass [] and think you are isolated. Name the failure mode.", "**Empty-list isolation.**"),
  ("How do you disable auto memory?", "autoMemoryEnabled false in settings, or CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 in env."),
  ("Does mcpServers: {} suppress claude.ai connectors?", "No."),
  ("User and project CLAUDE.md files disagree. Name the failure mode and fix.", "**Layered contradiction.** Remove the conflict or state precedence in the specific file."),
  ("Which two hook styles exist in the SDK?", "Filesystem hooks in settings.json and programmatic callbacks."),
  ("You wrote a blocking hook for a style preference. Name the failure mode by its exact label.", "**Hook-for-everything.**"),
 ],
 steps=[("Build a sample repo with user, project and local CLAUDE.md files", "A tree"), ("Run with three settingSources values and read the init message", "Three init dumps"),
        ("Record which CLAUDE.md, skills and hooks loaded in each", "A load-map"), ("Set up auto memory and verify it loads with []", "One observation"),
        ("Disable auto memory and connectors and re-run", "One observation"), ("Write the isolation recipe for one tenant", "A 5-line recipe")],
 pass_md=T("""
| settingSources | CLAUDE.md loaded | Skills | Hooks |
|---|---|---|---|
| omitted | user, project, local | user, project | settings.json |
| ["project"] | project only | project | project |
| [] | none | none | none (managed policy still) |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Claims [] is full isolation | **Empty-list isolation** |
| Runs from a parent dir | **Wrong-cwd silence** |
"""),
 verdict="The artifact passes only if the load-map was observed from init output, not inferred, and the always-read inputs are each paired with a disable method.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Use Claude Code features in the SDK | Sources, exceptions, hooks | Current |
| Anthropic | Hosting / Secure deployment | Multi-tenant recipe | Referenced, not read in full |
| Anthropic | Settings reference | Settings keys | Referenced, not read |
""") + "\n\n*Disagreement named:* the migration guide says the default briefly changed to load nothing and was reverted, while older sources describe a no-settings default; the current features page says omitting it loads all three.",
 reframe="This is the craft of inheritance: **what the SDK inherits from the host is a design decision.** The engineer who understands this lists inputs, not hopes.",
))

# ------------------------------------------------------------------ 8.2.5
SPECS.append(dict(
 mod=M, id="8.2.5", title="Skills and plugins in the SDK", short="Skills and plugins in the SDK",
 thesis="Skills are filesystem artifacts you scope with the skills option and dispatch by name, and plugins are local directories you load by path, which together let you package reusable behaviour without code.",
 prove="create a skill, scope it with the skills option, dispatch it with /name, package it in a plugin, and verify both through the init message.",
 discipline="verify every skill and plugin from the init message, never from the file tree.",
 counter="restricting the skills list does not restrict dispatch by name: sending /<name> runs a user-invocable skill even if skills omits it [" + SK + "].",
 read_min=20, prove_h="2", depth=["Create, scope and dispatch a skill", "Load and verify a plugin", "Diagnose missing skills and plugins"],
 deliverable="A plugin directory with one skill, a script that loads it, and the init-message output proving it loaded and was dispatched as /plugin:skill.",
 sections=[
 dict(title="Skills: discovery and scoping", framing="Skills are SKILL.md files under .claude/skills/<name>/, discovered through settingSources; the SDK has no programmatic API for registering them. Discovered skills are enabled by default, and the skills option takes 'all', a list of names, or [] [" + SK + "].",
  body=T("""
| skills value | Effect |
|---|---|
| omitted | Discovered user and project skills enabled; Skill tool available |
| "all" | Every discovered skill invocable |
| ["pdf", "docx"] | Only these; unlisted are invisible to the model and rejected by the Skill tool |
| [] | None invocable |

[Agent SDK docs, Extend agents with skills, 2026]. Setting skills adds the Skill tool to allowedTools; with an explicit tools list, include 'Skill'. Names must be exact: wildcards and padded names make query() reject the list (TypeScript 0.3.221 or later, Python 0.2.129 or later). Plugin skills use plugin:skill.
"""),
  fm=[("Hidden-file illusion", "You restrict skills to a list and assume the other skills are unreachable, yet their files stay readable through Read and Bash.", "Treat the list as scoping what the model sees; protect sensitive skills with permissions or by not placing them on the filesystem.")],
  xr="allowed tools and permissions are Module 8.6.1; skills in Claude Code are Module 1.2.", one="the skills list scopes invocation, not file access."),
 dict(title="Commands and dispatch by name", framing="A command is anything you run by sending /<name> in a prompt: built-in commands such as /compact, bundled skills such as /code-review, your skills, and older .claude/commands/ files. The init message's slash_commands field lists the available ones [" + SK + "].",
  body=T("""
```python
async for m in query(prompt="/security-check", options=ClaudeAgentOptions(max_turns=10)):
    ...
```
| Case | Result |
|---|---|
| /name matches a command | Runs, even if skills omits it |
| /name matches nothing | Sent to Claude as an ordinary message with a note it did not run; costs a model turn (since v2.1.274) |
| /theme (unavailable built-in) | Returns '/theme isn't available in this environment.' with no model turn |
| /compact with no history | success result, no compact_boundary; reason in result text |
| /clear in one-shot query | No practical effect |

[Agent SDK docs, Extend agents with skills, 2026]. A command can hit max_turns like any prompt. A user-invocable: false skill does not appear in skills or slash_commands.
"""),
  fm=[("Typo burns a turn", "You dispatch /secuirty-check, no command matches, and the SDK silently spends a model turn answering a plain message.", "Check the name against slash_commands from the init message before dispatching.")],
  xr="context and compaction are Module 8.2.1.", one="check slash_commands before you dispatch."),
 dict(title="Plugins: load by path and verify", framing="plugins takes a list of {type: 'local', path}; local is the only accepted type. Relative paths resolve against cwd; the path must be the plugin root, the parent of skills/, agents/, hooks/, commands/ or .claude-plugin/. Marketplace plugins must be downloaded first [" + PL + "].",
  body=T("""
| Plugin component | Location in plugin |
|---|---|
| Skills | skills/<name>/SKILL.md (invoked as /plugin-name:skill-name) |
| Commands | commands/*.md (flat files; use skills/ for new plugins) |
| Agents | agents/*.md |
| Hooks | hooks/hooks.json |
| MCP servers | .mcp.json |
| Manifest | .claude-plugin/plugin.json (optional) |

[Agent SDK docs, Plugins in the SDK, 2026]. The SDK does not expand ~ in paths. A nonexistent path is skipped and the session continues, so check the plugins list in init, and plugin_errors for load failures. TypeScript reloadPlugins() applies changes; addPlugins needs TypeScript SDK 0.3.301 or later; Python sends /reload-plugins as a prompt.
"""),
  fm=[("Skipped-plugin success", "A plugin path with ~ or a typo is skipped, the run succeeds, and nobody notices the plugin never loaded.", "Assert on init plugins and plugin_errors in CI and fail the job if a plugin is absent.")],
  xr="plugins in the CLI are Module 1.2; deployment of plugin files is Module 8.7.2.", one="a plugin that did not load looks exactly like a plugin that did."),
 dict(title="Pre-approving tools and troubleshooting", framing="Skills run with the session's tools. For project and personal skills Claude Code applies the allowed-tools frontmatter in SDK sessions, and you can also pre-approve via allowedTools. Pre-approval does not restrict other tools [" + SK + "].",
  body=T("""
| Symptom | Check | Fix |
|---|---|---|
| Skills not found | settingSources excludes user and project | Include them, or load via plugins |
| Skills not found | cwd outside the repo containing .claude/skills | Point cwd at or below it |
| Skill not used | Name missing from skills list: 'Skill <name> is not in this session's skills allowlist' | Add it, or dispatch /name |
| Skill not used | Vague description | Make description specific |
| Plugin not loading | Wrong root, invalid plugin.json, unreadable, missing dir | Check plugin_errors in init |

[Agent SDK docs, Extend agents with skills and Plugins in the SDK, 2026].
"""),
  fm=[("Empty-sources skills", "You set settingSources to [] for isolation and skills: 'all', and no skill ever loads.", "Load skills through a plugin path when you need both isolation and skills.")],
  xr="isolation is Module 8.2.4 and Module 8.7.3.", one="skills need a source; isolation needs a plugin path."),
 ],
 retrieval=[
  ("Where does a skill live on disk?", ".claude/skills/<name>/SKILL.md."),
  ("Can the SDK register skills programmatically?", "No; skills are filesystem artifacts (subagents can be defined in code)."),
  ("You list two skills and assume the rest cannot be reached. Name the failure mode by its exact label.", "**Hidden-file illusion.**"),
  ("What happens when /name matches nothing?", "It is sent to Claude as an ordinary message with a note, spending a model turn."),
  ("You dispatch /secuirty-check and burn a turn. Name the failure mode.", "**Typo burns a turn.**"),
  ("What is the only plugin type accepted?", "local."),
  ("A plugin path uses ~ and the run succeeds without it. Name the failure mode and fix.", "**Skipped-plugin success.** Assert on init plugins and plugin_errors."),
  ("Which init fields confirm skills, commands and plugins?", "skills, slash_commands and plugins."),
  ("You set settingSources [] and skills 'all' and nothing loads. Name the failure mode by its exact label.", "**Empty-sources skills.**"),
  ("What SDK versions added invalid-skill-name checks?", "TypeScript 0.3.221 and Python 0.2.129."),
 ],
 steps=[("Create .claude/skills/security-check/SKILL.md with name and description", "A skill file"), ("Run with skills 'all' and read skills and slash_commands in init", "An init dump"),
        ("Dispatch /security-check and record the result", "A transcript"), ("Move the skill into a plugin and load by absolute path", "A plugin dir"),
        ("Dispatch /my-plugin:security-check", "A transcript"), ("Break the path on purpose and record plugin_errors", "An error observation")],
 pass_md=T("""
| Check | Evidence |
|---|---|
| Skill discovered | init skills includes security-check |
| Dispatched | /security-check returns success |
| Plugin loaded | plugins lists my-plugin; skills has my-plugin:security-check |
| Failure path | bad path gives absence plus plugin_errors |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Loads plugin with ~/ path | **Skipped-plugin success** |
| Uses [] sources and skills all | **Empty-sources skills** |
"""),
 verdict="The artifact passes only if the init message proves load, dispatch is demonstrated, and a deliberate failure was observed.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Extend agents with skills | skills option, commands, troubleshooting | Current |
| Anthropic | Plugins in the SDK | Loading, namespacing, structure | Current |
| Anthropic | Agent Skills overview and best practices | Authoring | Referenced, not read |
""") + "\n\n*Disagreement named:* the plugins page says the commands/ directory holds skills as flat files and recommends skills/ for new plugins, while the skills page calls command files an older form; both agree skills are the successor.",
 reframe="This is the craft of packaging: **files for behaviour, options for scope, init for proof.** The engineer who understands this ships agents whose capabilities can be listed.",
))

if __name__ == "__main__":
    for s in SPECS:
        write(s)
