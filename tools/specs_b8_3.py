import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen import write
from specs_12 import T

M = "b-8-3"
SPECS = []
AL = "Agent SDK docs, How the agent loop works, 2026"
CT = "Agent SDK docs, Give Claude custom tools, 2026"
MC = "Agent SDK docs, Connect to external tools with MCP, 2026"
TS = "Agent SDK docs, Scale to many tools with tool search, 2026"
SA = "Agent SDK docs, Subagents in the SDK, 2026"
HR = lambda: "\n\n*Disagreement named:* "

# ------------------------------------------------------------------ 8.3.1
SPECS.append(dict(
 mod=M, id="8.3.1", title="Built-in tools and permission requirements", short="Built-in tools and permissions",
 thesis="The SDK ships the same built-in tools as Claude Code in six families, and what the agent can actually do is the product of two separate layers: which tools are available and which calls are approved.",
 prove="for a given agent spec, write the tools, allowed and disallowed lists that give exactly the required capability and show which layer each entry acts on.",
 discipline="separate availability from permission every time you write a tool list.",
 counter="allowedTools does not restrict anything: it only pre-approves, so a read-only agent is built with the tools option or a bare disallowed name, not with an allow list [" + CT + "].",
 read_min=20, prove_h="2", depth=["Name the built-in tool families and what each is for", "Predict availability versus permission for any list entry", "Design a least-privilege tool set for a task"],
 thin="The Claude Code Tools reference page (per-tool permission requirements, timeouts, output limits) was not read in this session; permission requirements below come from the Agent SDK pages only. Read the Tools reference before relying on per-tool details.",
 deliverable="A tool matrix for three agents (reviewer, tester, editor) showing every tool, its layer (availability or permission) and the exact option that sets it, verified against the init message.",
 sections=[
 dict(title="The six families", framing="The SDK includes the tools that power Claude Code, grouped by what they do. Tools are how an agent acts: without them Claude can only respond with text [" + AL + "].",
  body=T("""
| Category | Tools | What they do |
|---|---|---|
| File operations | Read, Edit, Write | Read, modify and create files |
| Search | Glob, Grep | Find files by pattern; search content with regex |
| Execution | Bash | Shell commands, scripts, git |
| Web | WebSearch, WebFetch | Search the web; fetch and parse pages |
| Discovery | ToolSearch | Find and load tools on demand |
| Orchestration | Agent, Skill, AskUserQuestion, TaskCreate, TaskUpdate | Spawn subagents, invoke skills, ask the user, track tasks |

[Agent SDK docs, How the agent loop works, 2026]. The task-tracking tools are only provided automatically on some models; elsewhere you opt in. In `tool_use` blocks the subagent tool is named Agent, but it appears as Task in the system:init tools list [Agent SDK docs, Subagents in the SDK, 2026].
"""),
  fm=[("Name drift", "Your detection code looks for a tool named Task or Agent only, and misses subagent calls on a version that uses the other name.", "Match both names when detecting subagent invocation.")],
  xr="subagents are Module 8.3.5; todo tools are Module 8.4.5; tool search is Module 8.3.4.", one="six families, and Agent is also called Task in the init list."),
 dict(title="Two layers: availability and permission", framing="The tools option and allowed or disallowed lists act on two layers. Availability decides whether a tool appears in Claude's context; permission decides whether a call is approved when Claude attempts it [" + CT + "].",
  body=T("""
| Option | Layer | Effect |
|---|---|---|
| `tools: ["Read","Grep"]` | Availability | Only these built-ins are in context; MCP tools unaffected |
| `tools: []` | Availability | All built-ins removed; only your MCP tools remain |
| allowed tools | Permission | Listed tools run without a prompt; others stay available |
| disallowed, bare name `"Bash"` | Both | Removes the tool from context |
| disallowed, scoped `"Bash(rm *)"` | Permission | Tool stays in context; matching calls denied |

[Agent SDK docs, Give Claude custom tools, 2026]. A scoped deny leaves the tool visible, so Claude may waste a turn trying it.
"""),
  fm=[("Visible-but-denied", "You block rm with a scoped deny, Claude keeps trying Bash variants, and turns are wasted on denials.", "Remove the tool with a bare name or the tools list when it should never be attempted.")],
  xr="rule evaluation order is Module 8.6.1.", one="availability hides a tool; permission only gates a call."),
 dict(title="Permission modes and what they auto-approve", framing="permission_mode sets the oversight level. In default mode, tools not covered by allow rules go to your canUseTool callback and no callback means deny [" + AL + "].",
  body=T("""
| Mode | Behaviour |
|---|---|
| default | Uncovered tools go to canUseTool; none means deny |
| acceptEdits | Auto-approves file edits and common filesystem commands (mkdir, touch, mv, cp); other Bash follows default rules |
| plan | Explores and plans; edits never auto-approved |
| dontAsk | Never prompts; only pre-approved tools run, everything else denied |
| auto | A model classifier approves or denies prompts |
| bypassPermissions | Runs allowed tools without asking, except explicit ask rules; TypeScript also needs allowDangerouslySkipPermissions: true; not as root on Unix |

[Agent SDK docs, How the agent loop works, 2026]. acceptEdits does not auto-approve MCP tools; use allowedTools wildcards for those [Agent SDK docs, Connect to external tools with MCP, 2026].
"""),
  fm=[("Mode-as-allowlist", "You use acceptEdits expecting MCP and Bash calls to be approved too, and the unattended run stalls or denies them.", "List MCP and Bash needs in allowedTools, or choose dontAsk for a fixed surface.")],
  xr="modes in depth are Module 8.6.1; secure deployment is Module 8.7.4.", one="a mode sets a baseline; lists add exceptions."),
 dict(title="Designing a least-privilege tool set", framing="Start from the task's verbs. A reviewer reads, a tester runs commands, an editor writes. The docs give combinations for subagents that apply equally to a main agent [" + SA + "].",
  body=T("""
| Use case | Tools |
|---|---|
| Read-only analysis | Read, Grep, Glob |
| Test execution | Bash, Read, Grep |
| Code modification | Read, Edit, Write, Grep, Glob |
| Full access | All tools (omit the tools field) |

[Agent SDK docs, Subagents in the SDK, 2026]. A tool left out is not in the session at all: Claude works without it, with no prompt or error. Verify the result from the init message's tools array.
"""),
  fm=[("Unverified surface", "You assume the tool set from your options and never read the init message, so a missing or extra tool goes unnoticed.", "Assert on the init tools array in a test.")],
  xr="agent evals are Module 8.6.5; subagent scoping is Module 8.3.5.", one="the init message is the proof of what the agent can do."),
 ],
 retrieval=[
  ("Name the six built-in tool families.", "File operations, search, execution, web, discovery and orchestration."),
  ("Which tool searches content with regex?", "Grep."),
  ("Your detector misses subagent calls because of the tool's name. Name the failure mode by its exact label.", "**Name drift.**"),
  ("What does `tools: []` do?", "Removes all built-ins; only your MCP tools remain."),
  ("Which layer does a scoped disallowed rule act on?", "Permission only; the tool stays in context."),
  ("Claude keeps retrying a denied Bash command. Name the failure mode and fix.", "**Visible-but-denied.** Remove the tool by bare name or the tools list."),
  ("Does acceptEdits approve MCP tools?", "No."),
  ("You use acceptEdits and the unattended MCP calls stall. Name the failure mode by its exact label.", "**Mode-as-allowlist.**"),
  ("What extra requirement does bypassPermissions have in TypeScript and on Unix?", "allowDangerouslySkipPermissions: true in TypeScript; it cannot run as root on Unix."),
  ("How do you prove which tools a session has?", "Read the init message's tools array; skipping this is the Unverified surface failure mode."),
 ],
 steps=[("Write three agent specs: reviewer, tester, editor", "A 3-row brief"), ("For each, choose tools, allowed and disallowed entries", "A tool matrix"),
        ("Label every entry availability or permission", "A labelled matrix"), ("Run each and print the init tools array", "Three dumps"),
        ("Attempt a forbidden action per agent and record the result", "Three observations"), ("Note which entries a scoped deny leaves visible", "A short list")],
 pass_md=T("""
| Agent | tools | allowed | disallowed | Init tools |
|---|---|---|---|---|
| reviewer | Read, Grep, Glob | same | Bash | matches |
| tester | Bash, Read, Grep | Bash(npm test) | - | matches |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| allowed list used as restriction | It only pre-approves |
| Never checked init | **Unverified surface** |
"""),
 verdict="The artifact passes only if each entry is labelled with its layer and the init output matches the matrix.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | How the agent loop works | Tool families, modes | Current |
| Anthropic | Give Claude custom tools | Availability vs permission | Current |
| Anthropic | Tools reference (Claude Code) | Per-tool requirements | Not read |
""") + HR() + "none found among pages read; per-tool permission details live on the Tools reference page, which should be read before an audit.",
 reframe="This is the craft of the tool surface: **what exists, what is approved, and proof from init.** The engineer who understands this writes two lists, not one.",
))

# ------------------------------------------------------------------ 8.3.2
SPECS.append(dict(
 mod=M, id="8.3.2", title="Custom tools as an in-process MCP server", short="Custom tools",
 thesis="A custom tool is a name, a description, an input schema and a handler, registered through an in-process MCP server, and how the handler reports errors decides what Claude reads next.",
 prove="build a two-tool server, call it with a wildcard permission, force an error and show the message Claude received.",
 discipline="return failures as results with isError set instead of letting exceptions escape.",
 counter="a thrown exception does not stop the agent: the in-process server converts it to an error result with the raw message, so the loop continues on whatever text the exception carried [" + CT + "].",
 read_min=22, prove_h="2.5", depth=["Define and register a custom tool and call it", "Control errors, parallelism and approvals", "Return images, resources and structured data correctly"],
 deliverable="A working server with two tools (one read-only, one that can fail), an allowedTools wildcard, an error test, and a transcript showing the model's reaction to the error.",
 sections=[
 dict(title="The four parts and registration", framing="A tool has a name, a description Claude reads to decide when to call it, an input schema and an async handler. TypeScript uses a Zod schema; Python uses a dict of types or full JSON Schema. The server is created with createSdkMcpServer or create_sdk_mcp_server and runs inside your application, not as a separate process [" + CT + "].",
  body=T("""
```python
@tool("get_temperature", "Get the current temperature at a location",
      {"latitude": float, "longitude": float})
async def get_temperature(args):
    return {"content": [{"type": "text", "text": "..."}]}

server = create_sdk_mcp_server(name="weather", version="1.0.0", tools=[get_temperature])
options = ClaudeAgentOptions(mcp_servers={"weather": server},
                             allowed_tools=["mcp__weather__get_temperature"])
```
[Agent SDK docs, Give Claude custom tools, 2026]. The tool name is `mcp__{server_name}__{tool_name}` where the server name is the key in mcpServers, and characters like `.` or spaces become `_`. A wildcard `mcp__weather__*` covers every tool on the server.
"""),
  fm=[("Unlisted custom tool", "You register the server but omit the tool's full name from allowedTools, and Claude sees the tool but the call needs approval or is denied in an unattended run.", "List the exact mcp__server__tool name or the server wildcard in allowedTools.")],
  xr="tool design principles are Module 8.3.6; permissions are Module 8.6.1.", one="register the server, then permit the fully qualified name."),
 dict(title="Handlers: errors, content blocks and structured data", framing="A handler returns content (an array of text, image, audio, resource or resource_link blocks), optionally structuredContent and isError [" + CT + "].",
  body=T("""
| Situation | What Claude sees |
|---|---|
| Handler throws | Error result carrying the raw exception message; loop continues |
| Handler returns isError true | The message you composed |
| structuredContent set | The JSON plus image/resource blocks; text blocks in content are not forwarded |
| Python @tool | Forwards only content and is_error; no structuredContent |
| Audio block (TypeScript) | Saved to disk; Claude gets a text block with the path |
| Audio or binary resource (Python) | Dropped with a warning |

[Agent SDK docs, Give Claude custom tools, 2026]. An image block takes base64 data without a data: prefix and a required mimeType; PNG, JPEG, GIF and WebP reach Claude as visual input, other types are saved to disk and the path is given as text.
"""),
  fm=[("Raw-exception reply", "Your handler lets an HTTP failure throw, and Claude reads a bare 'Unexpected token' string with no hint what to retry.", "Catch in the handler and return isError true with the status, the request and a next step.")],
  xr="actionable error design is Module 8.3.6.", one="you compose the failure message or the exception does."),
 dict(title="Parallelism, annotations and approvals", framing="Custom tools default to sequential execution. readOnlyHint: true lets Claude batch the tool with other read-only calls. Annotations are metadata, not enforcement [" + CT + "].",
  body=T("""
| Annotation | Default | Meaning |
|---|---|---|
| readOnlyHint | false | No environment changes; enables parallel calls |
| destructiveHint | true | May perform destructive updates |
| idempotentHint | false | Repeat calls have no extra effect; informational |
| openWorldHint | true | Reaches outside your process; informational |

[Agent SDK docs, Give Claude custom tools, 2026]. TypeScript only, v0.3.301 or later: a permission_policy of always_ask or always_deny in a tools array on the server config. In auto or plan mode, also set destructiveHint: true so always_ask calls still reach your callback, because an unset hint counts as false for always_ask.
"""),
  fm=[("Lying hint", "You mark a tool readOnlyHint true because it is usually read-only, and a parallel call performs a write.", "Keep the annotation accurate to the handler; split read and write into separate tools.")],
  xr="approval callbacks are Module 8.4.4.", one="annotations describe; they do not enforce."),
 dict(title="Schemas, optional parameters and deferral", framing="TypeScript makes a parameter optional with .optional(); Python's dict schema requires every key, so use JSON Schema, leave the key out of required and read it with args.get() [" + CT + "]. Tool search is on by default and defers SDK MCP tools, so each tool's schema loads on demand.",
  body=T("""
| Need | TypeScript | Python |
|---|---|---|
| Enum | z.enum([...]) | Full JSON Schema with enum |
| Optional | .optional() | Omit from required; args.get() |
| Keep schema in prompt | `alwaysLoad: true` in extras or server options | not documented here |
| Unconvertible schema | Tool omitted from the list with a process warning CLAUDE_SDK_MCP_TOOL_SCHEMA_UNCONVERTIBLE | n/a |

[Agent SDK docs, Give Claude custom tools and Connect to external tools with MCP, 2026]. Before TypeScript SDK v0.3.286, one unconvertible schema made the whole listing fail without a warning.
"""),
  fm=[("Vanishing tool", "A tool's schema cannot be converted, the tool is silently left out, and Claude never calls it.", "Watch for the process warning and test that every tool appears in the init tools list.")],
  xr="tool search is Module 8.3.4.", one="assert every custom tool shows up in init."),
 ],
 retrieval=[
  ("List the four parts of a tool definition.", "Name, description, input schema and handler."),
  ("What is the full name of tool `get_temperature` on server key `weather`?", "mcp__weather__get_temperature."),
  ("You registered a server but calls need approval in an unattended run. Name the failure mode by its exact label.", "**Unlisted custom tool.**"),
  ("What happens if a handler throws?", "The in-process server converts it to an error result with the raw message and the loop continues."),
  ("Claude gets a bare 'Unexpected token' string. Name the failure mode and fix.", "**Raw-exception reply.** Catch and return isError with context."),
  ("What does readOnlyHint control?", "Whether the tool can be called in parallel with other read-only tools."),
  ("A tool marked read-only performs a write. Name the failure mode by its exact label.", "**Lying hint.**"),
  ("Which permission policies exist, and which version is required?", "always_ask and always_deny; TypeScript SDK v0.3.301 or later."),
  ("A tool never appears to Claude after a schema change. Name the failure mode.", "**Vanishing tool.**"),
  ("Does Python's @tool forward structuredContent?", "No; only content and is_error."),
 ],
 steps=[("Define two tools in one server, one with readOnlyHint", "A server file"), ("Call with a wildcard allowedTools entry", "A success transcript"),
        ("Make the second tool fail by throwing; record what Claude says", "A transcript"), ("Change it to return isError with context; record the difference", "A second transcript"),
        ("Print init tools and confirm both appear", "A dump"), ("Add an always_ask policy (TypeScript) and observe the callback", "A log line")],
 pass_md=T("""
| Check | Evidence |
|---|---|
| Both tools in init | mcp__weather__* present |
| Throw vs isError | Two transcripts; second names the failing request |
| Parallelism | read-only tool batched with Read |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Handler throws on 500 | **Raw-exception reply** |
| Write tool marked readOnly | **Lying hint** |
"""),
 verdict="The artifact passes only if both error styles were observed and init lists every tool.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Give Claude custom tools | Definition, errors, annotations | Current |
| MCP specification | Tools, annotations | Origin of annotations | Referenced, not read |
| Anthropic | Connect to external tools with MCP | Naming, deferral | Current |
""") + HR() + "none found; note the Python and TypeScript SDKs differ on structuredContent, audio and binary resources, so confirm per language.",
 reframe="This is the craft of the handler: **a description Claude reads, a schema, and an error you wrote.** The engineer who understands this treats the tool result as the next prompt.",
))

# ------------------------------------------------------------------ 8.3.3
SPECS.append(dict(
 mod=M, id="8.3.3", title="External MCP servers: transports, authentication, errors", short="External MCP servers",
 thesis="An external MCP server is configured by transport, permitted by fully qualified tool names, authenticated by environment or headers, and trusted only after you read its status from the init message.",
 prove="connect a stdio and an HTTP server, authenticate one with a header, and make your CI fail when any server is failed or needs-auth.",
 discipline="never trust a server because the run succeeded; read each server's status.",
 counter="a server that fails to connect does not raise: the run continues without its tools, and Claude may fall back to built-in tools, so success does not mean the server worked [" + MC + "].",
 read_min=22, prove_h="2.5", depth=["Choose transport and write the config", "Authenticate and permit tools correctly", "Detect, retry and bound server failures"],
 deliverable="A config and test that connects two servers, asserts status in init, and reproduces failed, needs-auth and timeout cases.",
 sections=[
 dict(title="Transports and where to configure", framing="Pick transport by what the server documents: a command to run means stdio, a URL means HTTP or SSE, tools in your own code mean an SDK server. Configure in code through mcpServers or in a .mcp.json file loaded through the project setting source [" + MC + "].",
  body=T("""
| Transport | Config shape | Notes |
|---|---|---|
| stdio | `{command, args, env}` | Local process |
| HTTP | `{type: "http", url, headers}` | Streamable HTTP; 'streamable-http' accepted only in JSON files |
| SSE | `{type: "sse", url, headers}` | Remote |
| SDK | createSdkMcpServer result | In-process |

[Agent SDK docs, Connect to external tools with MCP, 2026]. In .mcp.json, `${VAR}` expands environment variables. Tools are named mcp__<server>__<tool>; use `mcp__github__*` in allowedTools. Prefer allowedTools over permission modes: acceptEdits does not approve MCP tools and bypassPermissions is broader than needed.
"""),
  fm=[("Silent skip", "A .mcp.json entry fails validation or settingSources omits project, and the server is never loaded while the run still succeeds.", "Include the project source, and check init mcp_servers for every expected server.")],
  xr="settings sources are Module 8.2.4; custom servers are Module 8.3.2.", one="transport follows the docs: command is stdio, URL is HTTP or SSE."),
 dict(title="Authentication", framing="Pass credentials through env for stdio servers and headers for HTTP and SSE. The SDK does not open a browser or run an interactive OAuth flow; complete OAuth in your own application and pass the access token in headers [" + MC + "].",
  body=T("""
| Status | Meaning | What to do |
|---|---|---|
| needs-auth | No usable sign-in for the server | Pass a token in headers, or sign in from an interactive Claude Code session on the machine first |
| failed with 'Couldn't read the stored credentials' | Credential store unreadable | See the errors page; before Claude Code v2.1.307 a locked Mac keychain showed needs-auth |

[Agent SDK docs, Connect to external tools with MCP, 2026]. In either case the run continues without that server's tools. Poll mcpServerStatus() (TypeScript) or get_mcp_status() (Python).
"""),
  fm=[("Expired bearer", "A short-lived access token placed in headers expires mid-run and the server flips to needs-auth while the agent keeps going.", "Refresh tokens in your app and check status before long runs; reconnect with reconnectMcpServer.")],
  xr="secret handling is Module 8.7.4.", one="the SDK carries your token; it does not fetch one."),
 dict(title="Connection timing and statuses", framing="Claude Code starts connecting at session start. stdio and uncached HTTP/SSE servers in mcpServers delay the first turn until they connect, up to MCP_TIMEOUT (30 seconds by default). Statuses are pending, connected, failed, needs-auth and disabled [" + MC + "].",
  body=T("""
| Setting | Effect |
|---|---|
| MCP_TIMEOUT | Connection limit in ms; default 30 seconds |
| MCP_TOOL_TIMEOUT | How long a tool call may run |
| CLAUDE_CODE_MCP_STARTUP_WAIT_MS | First-turn wait; needs Claude Code v2.1.274 or later; 0 skips waiting for most servers |
| MCP_CONNECTION_NONBLOCKING=0 | Startup waits up to 5 seconds by default for the batch |
| alwaysLoad: true | Startup waits for that server's tools and exempts it from deferral |

[Agent SDK docs, Connect to external tools with MCP, 2026]. Pending is not failure: it can mean not connected yet, served from a cached tool list, or an expired deadline. After five failed reconnection attempts a dropped remote server reports failed.
"""),
  fm=[("Pending-as-failed", "Your gate treats pending at init as failure and blocks healthy runs whose servers use a cached tool list.", "Fail on failed or needs-auth at init, and re-check pending servers later with the status call.")],
  xr="failure handling is Module 8.7.5.", one="pending is a question, not an answer."),
 dict(title="Output limits and safe use", framing="MCP output beyond a limit is saved to a file: a successful result over 25,000 tokens with no image is replaced by an error naming the file path, and a text result over 50,000 characters is saved regardless of the token limit unless the tool declares anthropic/maxResultSizeChars. MAX_MCP_OUTPUT_TOKENS changes the token limit [" + MC + "].",
  body=T("""
| Risk | Control |
|---|---|
| SQL tool runs writes | Server-side read-only (the docs' DBHub example sets readonly = true) |
| Broad permission | Allow specific tools, not the whole server, when only one is needed |
| Large output | Paginate in the server; raise MAX_MCP_OUTPUT_TOKENS only deliberately |
| Server missing at startup | Check status, because Claude can fall back to built-ins |

[Agent SDK docs, Connect to external tools with MCP, 2026]. The read-only control belongs in the server, not in the prompt.
"""),
  fm=[("Prompt-only read-only", "You tell the agent 'do not write' while the database tool accepts writes.", "Enforce read-only in the server configuration.")],
  xr="tool design is Module 8.3.6; secure deployment is Module 8.7.4.", one="enforce limits where the data lives."),
 ],
 retrieval=[
  ("Which transport do you use when a server documents a command to run?", "stdio."),
  ("What is the default MCP connection timeout?", "30 seconds (MCP_TIMEOUT)."),
  ("The run succeeds but the server never loaded. Name the failure mode by its exact label.", "**Silent skip.**"),
  ("Does the SDK run an interactive OAuth flow?", "No; complete OAuth in your app and pass the token in headers."),
  ("A short-lived token expires mid-run. Name the failure mode.", "**Expired bearer.**"),
  ("List the five server statuses.", "pending, connected, failed, needs-auth, disabled."),
  ("Your gate fails healthy runs at init. Name the failure mode and fix.", "**Pending-as-failed.** Fail only on failed or needs-auth."),
  ("What token threshold turns MCP output into a file?", "25,000 tokens (and 50,000 characters for text unless declared otherwise)."),
  ("The prompt says 'do not write' to a writable SQL tool. Name the failure mode by its exact label.", "**Prompt-only read-only.**"),
  ("After how many failed reconnection attempts does a dropped server report failed?", "Five."),
 ],
 steps=[("Configure a stdio server and an HTTP server", "A config"), ("Permit with wildcards and run a task using each", "Two transcripts"),
        ("Print mcp_servers statuses from init", "A dump"), ("Break the token; record needs-auth or failed", "An observation"),
        ("Write the CI gate on failed and needs-auth", "A script"), ("Call a tool returning more than the limit and record the file path message", "An observation")],
 pass_md=T("""
| Server | Transport | Status | Gate |
|---|---|---|---|
| filesystem | stdio | connected | pass |
| github | http + header | connected | pass |
| broken | http, bad token | needs-auth | job fails |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Gate fails on pending | **Pending-as-failed** |
| 'Read only' in prompt | **Prompt-only read-only** |
"""),
 verdict="The artifact passes only if statuses come from init, one failure case was reproduced, and the gate distinguishes pending from failed.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Connect to external tools with MCP (SDK) | Transports, auth, timing | Current |
| Anthropic | Claude Code MCP page | Scopes, caches, limits | Referenced, not read |
| MCP project | Specification | Protocol | Referenced, not read |
""") + HR() + "none found; the SDK page says the SDK does no interactive OAuth while the CLI page covers interactive sign-in, so credentials from a CLI sign-in may be usable on the same machine.",
 reframe="This is the craft of integration: **configure, permit, authenticate, verify.** The engineer who understands this reads the status, not the result.",
))

# ------------------------------------------------------------------ 8.3.4
SPECS.append(dict(
 mod=M, id="8.3.4", title="Tool search at scale", short="Tool search",
 thesis="Tool search withholds tool definitions from context and loads only what a turn needs, trading one extra round trip per search for a much smaller context on every turn.",
 prove="measure context use with tool search on and off for a 50-tool server and decide the ENABLE_TOOL_SEARCH setting with numbers.",
 discipline="name and describe tools for search, because the search matches names and descriptions.",
 counter="more tools are not free even when idle: the docs say tool selection accuracy degrades with more than 30-50 tools loaded at once, which is why deferral exists, but with fewer than about 10 small tools, loading upfront is typically faster [" + TS + "].",
 read_min=18, prove_h="2", depth=["Explain what tool search does and costs", "Choose an ENABLE_TOOL_SEARCH value", "Write names and descriptions that search well"],
 deliverable="A measurement table of context tokens and turns for three ENABLE_TOOL_SEARCH settings on a real tool catalogue, with the decision.",
 sections=[
 dict(title="What it does and what it costs", framing="Tool search lets an agent work with hundreds or thousands of tools: definitions are withheld, the agent gets a summary and searches when it needs a capability. Fifty tools can use 10-20K tokens, and selection accuracy degrades with more than 30-50 loaded at once [" + TS + "].",
  body=T("""
| Property | Value | Source |
|---|---|---|
| Default | On | Tool search page |
| Tools loaded per search | Up to 5 most relevant | Tool search page |
| Persistence | Loaded tools stay until the messages where they were found are compacted | Tool search page |
| Catalogue limit | 10,000 tools | Tool search page |
| Cost | One extra round trip per search | Tool search page |
| Not supported | Models earlier than Opus 4 / Sonnet 4; Microsoft Foundry deployments hosted on Azure | Tool search page |

[Agent SDK docs, Scale to many tools with tool search, 2026]. Core built-in tools such as Bash, Read and Edit load upfront.
"""),
  fm=[("Post-compaction amnesia", "After compaction the discovered tools leave context, Claude must search again, and a fixed workflow suddenly takes an extra round trip.", "Name key tools in the system prompt and use alwaysLoad for the few that every turn needs.")],
  xr="compaction is Module 8.2.1; MCP servers are Module 8.3.3.", one="deferral saves context and costs round trips."),
 dict(title="Configuring ENABLE_TOOL_SEARCH", framing="You control deferral with the ENABLE_TOOL_SEARCH environment variable, set through the env option [" + TS + "].",
  body=T("""
| Value | Behaviour |
|---|---|
| unset | On, with fallbacks to upfront loading on unsupported models and some platforms |
| true | On, same fallbacks |
| auto | Off until deferrable definitions reach 10% of the context window, then on |
| auto:N | Same with N percent; auto:5 activates sooner |
| false | Off; all definitions load every turn |

[Agent SDK docs, Scale to many tools with tool search, 2026]. CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS keeps it off, and a HIPAA configuration turns it off. In TypeScript, env replaces the subprocess environment, so spread process.env. Behind an ANTHROPIC_BASE_URL gateway it is on by default; before Claude Code v2.1.304 it was disabled there unless set.
"""),
  fm=[("Env replacement", "In TypeScript you set only ENABLE_TOOL_SEARCH in env and drop PATH and the API key.", "Spread process.env and add the variable.")],
  xr="env semantics are Module 8.2.2.", one="auto:N is a threshold on deferrable definitions, not on total context."),
 dict(title="Writing tools that search finds", framing="The search matches queries against tool names and descriptions. Names like search_slack_messages surface for a wider range of requests than query_slack, and a description such as 'Search Slack messages by keyword, channel, or date range' beats 'Query Slack' [" + TS + "].",
  body=T("""
| Weak | Strong |
|---|---|
| query_slack | search_slack_messages |
| 'Query Slack' | 'Search Slack messages by keyword, channel, or date range' |
| Catalogue unknown to the agent | System prompt line: 'You can search for tools to interact with Slack, GitHub, and Jira.' |

[Agent SDK docs, Scale to many tools with tool search, 2026]. Use the claude_code preset with append so the line adds to the preset.
"""),
  fm=[("Generic name", "Two tools called run and query both match many requests and the agent loads the wrong one.", "Use verb-object names and keyword-rich descriptions.")],
  xr="tool design principles are Module 8.3.6.", one="a name is a search key."),
 dict(title="Deciding with numbers", framing="The decision is empirical: compare context tokens, turns and success for your catalogue under each setting. The docs give the thresholds; your tools give the numbers.",
  body=T("""
| Setting | Context tokens (turn 1) | Extra round trips | Success on task set |
|---|---|---|---|
| false | measure | 0 | measure |
| unset | measure | measure | measure |
| auto:5 | measure | measure | measure |

Figures are to be measured; none are claimed here. Use the usage fields on the ResultMessage and run each setting on the same tasks.
"""),
  fm=[("Setting by folklore", "You pick auto:5 because a blog said so and never measure on your catalogue.", "Measure all three settings on your task set.")],
  xr="evals are Module 8.6.5; cost tracking is Module 8.6.3.", one="measure before you configure."),
 ],
 retrieval=[
  ("How many tools does one search load by default?", "Up to five."),
  ("What is the catalogue limit?", "10,000 tools."),
  ("After compaction a workflow gains a round trip. Name the failure mode by its exact label.", "**Post-compaction amnesia.**"),
  ("What does ENABLE_TOOL_SEARCH=auto:5 mean?", "Off until deferrable definitions reach 5% of the context window, then on."),
  ("Why spread process.env in TypeScript?", "env replaces the subprocess environment; see the Env replacement failure mode."),
  ("Which name searches better, query_slack or search_slack_messages?", "search_slack_messages."),
  ("Two vague tool names load the wrong tool. Name the failure mode and fix.", "**Generic name.** Verb-object names and keyword-rich descriptions."),
  ("When is loading upfront typically faster?", "With fewer than about 10 tools that fit comfortably in context."),
  ("You choose a setting from a blog post. Name the failure mode by its exact label.", "**Setting by folklore.**"),
  ("Roughly how much context can 50 tools use?", "10-20K tokens."),
 ],
 steps=[("Build or pick a catalogue of 30+ tools", "A tool list"), ("Run a fixed task set with false, unset and auto:5", "Three runs"),
        ("Record context tokens, round trips and success", "A table"), ("Rename five tools and rewrite descriptions; re-run", "A second table"),
        ("Add the catalogue line to the system prompt; re-run", "A third table"), ("Write the decision", "A paragraph")],
 pass_md=T("""
| Setting | Turn-1 tokens | Round trips | Success |
|---|---|---|---|
| false | recorded | 0 | recorded |
| unset | recorded | recorded | recorded |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| No measurements | **Setting by folklore** |
| Names unchanged | **Generic name** |
"""),
 verdict="The artifact passes only if every cell is measured and the decision follows from the table.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Scale to many tools with tool search (SDK) | Behaviour, settings, limits | Current |
| Anthropic | Tool search in the API | Mechanism | Referenced, not read |
""") + HR() + "none found; the 30-50 tool accuracy figure is the docs' own statement and is not independently verified here.",
 reframe="This is the craft of scale: **defer what is idle, name what must be found.** The engineer who understands this budgets context per tool.",
))

# ------------------------------------------------------------------ 8.3.5
SPECS.append(dict(
 mod=M, id="8.3.5", title="Subagents in the SDK", short="Subagents in the SDK",
 thesis="A subagent is a separate agent instance with its own context, tools and prompt, defined in code and invoked through the Agent tool, and its power comes from isolation and bounded spend, not from extra intelligence.",
 prove="define two subagents with different tool sets, prove delegation from the stream, and cap depth, concurrency and spend.",
 discipline="put everything a subagent needs in the Agent tool's prompt, because that string is the only thing passed down.",
 counter="a subagent does not see the parent's conversation: the only content passed from parent to subagent is the Agent tool's prompt string [" + SA + "].",
 read_min=22, prove_h="2.5", depth=["Define, invoke and detect subagents", "Predict what a subagent inherits", "Bound depth, concurrency and spend"],
 deliverable="A two-subagent orchestration with delegation proof from parent_tool_use_id, a resumed subagent, and limits tested against a runaway prompt.",
 sections=[
 dict(title="Defining subagents", framing="Define subagents with the agents parameter, with filesystem files in .claude/agents/, or rely on the built-in general-purpose agent. Programmatic definitions are recommended for SDK applications and take precedence over filesystem agents of the same name. Include Agent in allowed tools [" + SA + "].",
  body=T("""
| AgentDefinition field | Required | Notes |
|---|---|---|
| description | Yes | When to use the agent; Claude matches tasks by it |
| prompt | Yes | The agent's system prompt |
| tools | No | Omitted means all tools available to subagents |
| disallowedTools | No | Remove tools; accepts mcp__server patterns |
| model | No | Alias (sonnet, opus, haiku, inherit) or full ID |
| skills | No | Preload up to the first 32 distinct names |
| maxTurns | No | Output marked partial at the limit (Claude Code v2.1.246 or later) |
| background | No | Run as non-blocking task |
| effort, permissionMode, memory, mcpServers | No | Per-agent overrides |

[Agent SDK docs, Subagents in the SDK, 2026]. By default a spawned subagent runs in the background and the Agent result has status async_launched; Claude waits when its next action needs the report. In Python, multi-word fields keep camelCase.
"""),
  fm=[("Missing Agent tool", "You define agents but leave Agent out of allowed tools, and delegation needs approval or never happens.", "Include Agent in allowedTools and mention the subagent by name when you need a guarantee.")],
  xr="tool lists are Module 8.3.1; permissions are Module 8.6.1.", one="description routes; prompt defines; tools restrict."),
 dict(title="What a subagent inherits", framing="A non-fork subagent starts fresh: no parent conversation, no parent system prompt. It gets its own system prompt, the Agent tool's prompt, project CLAUDE.md (unless omitClaudeMd), and its tool definitions [" + SA + "].",
  body=T("""
| Receives | Does not receive |
|---|---|
| AgentDefinition.prompt and the Agent tool prompt | Parent history and tool results |
| Project CLAUDE.md via settingSources | Preloaded skill content unless listed in skills |
| Tool definitions (inherited or subset) | Parent's system prompt |

[Agent SDK docs, Subagents in the SDK, 2026]. Only the final message returns to the parent, which may summarize it; ask for verbatim output in your prompt if needed. From Claude Code v2.1.210 the final message is scanned for control-tag imitation and turn markers, which are neutralized in place, never removed. Forks copy the conversation and are available from v2.1.302; deny them with Agent(fork).
"""),
  fm=[("Context assumption", "You write 'fix the bug we discussed' in the Agent prompt and the subagent has no idea what was discussed.", "Pass file paths, error text and decisions explicitly in the prompt string.")],
  xr="context management is Module 8.2.1.", one="the prompt string is the whole handoff."),
 dict(title="Detecting delegation and resuming", framing="Claude invokes subagents through the Agent tool; detect tool_use blocks named Agent, and Task on older versions. Messages from inside a subagent carry parent_tool_use_id [" + SA + "].",
  body=T("""
| Need | How |
|---|---|
| Detect invocation | tool_use name in ("Task","Agent") |
| Know a message is inside a subagent | parent_tool_use_id set |
| Identify the subagent (TypeScript) | agent_id, v0.3.292 or later |
| Resume | Capture session_id and agentId from the Agent result; pass resume with the same agents definition |

[Agent SDK docs, Subagents in the SDK, 2026]. The built-in Explore and Plan agents are one-shot and return no agentId. Resume needs the same session; each query() starts a new session by default.
"""),
  fm=[("Fresh-session resume", "You try to resume a subagent in a new query without resume: session_id, and its transcript is not found.", "Pass the first query's session_id and the same agent definitions.")],
  xr="resume is Module 8.5.1.", one="to resume a subagent, resume the session."),
 dict(title="Capping depth, concurrency and spend", framing="Claude decides how many subagents to spawn, and subagents can spawn subagents, so one prompt can grow into a tree. Three caps bound it; the section applies from TypeScript SDK v0.3.219 and Python SDK v0.2.127 [" + SA + "].",
  body=T("""
| Limit | Set with | Default | At the limit |
|---|---|---|---|
| Depth | CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH | 3 layers; 1 stops nesting | Bottom-layer subagent cannot spawn |
| Concurrency | CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS | 20 | 'Concurrent subagent limit reached' |
| Spend | maxBudgetUsd / max_budget_usd | None | 'Budget limit reached', background agents stopped, error_max_budget_usd |

[Agent SDK docs, Subagents in the SDK, 2026]. Opus 5 delegates more readily; the claude_code preset adds a line telling it not to call the Agent tool unless asked, but a custom prompt does not, so set the limits as well.
"""),
  fm=[("Agent tree blowup", "An open-ended audit prompt spawns many subagents, each with its own requests, and spend balloons before the budget is noticed.", "Set depth to 1, a small concurrency cap and a budget before launch.")],
  xr="cost is Module 8.6.3; failure handling is Module 8.7.5.", one="limits are enforced by Claude Code, whatever Claude decides."),
 ],
 retrieval=[
  ("Which field tells Claude when to use a subagent?", "description."),
  ("You define agents but nothing delegates. Name the failure mode by its exact label.", "**Missing Agent tool.**"),
  ("What is the only content passed from parent to subagent?", "The Agent tool's prompt string."),
  ("A prompt says 'fix the bug we discussed'. Name the failure mode.", "**Context assumption.**"),
  ("How do you detect that a message is inside a subagent?", "parent_tool_use_id is set."),
  ("A resume attempt cannot find the transcript. Name the failure mode and fix.", "**Fresh-session resume.** Pass session_id and the same agents."),
  ("What are the default depth and concurrency limits?", "3 layers of subagents and 20 concurrent."),
  ("An open-ended prompt multiplies spend. Name the failure mode by its exact label.", "**Agent tree blowup.**"),
  ("How many skills does the skills field preload at most?", "The first 32 distinct names."),
  ("What does the Agent tool result status async_launched mean?", "The subagent runs in the background and the report arrives in a later turn."),
 ],
 steps=[("Define a read-only reviewer and a Bash-enabled tester", "Two definitions"), ("Prompt by name and capture the Agent tool_use", "A stream excerpt"),
        ("Log parent_tool_use_id for inner messages", "A log"), ("Capture agentId and session_id and resume", "A resumed answer"),
        ("Run an audit prompt with depth 1, concurrency 5, a budget", "Result subtype and cost"), ("Record what a subagent did not know", "One observation")],
 pass_md=T("""
| Check | Evidence |
|---|---|
| Delegation | Agent tool_use for code-reviewer |
| Isolation | inner messages carry parent_tool_use_id |
| Resume | follow-up answered with prior context |
| Caps | error_max_budget_usd at the budget |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Agent not in allowed tools | **Missing Agent tool** |
| Vague prompt to subagent | **Context assumption** |
"""),
 verdict="The artifact passes only if delegation is proven from the stream and each cap was reached at least once.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Subagents in the SDK | Definition, inheritance, caps | Current |
| Anthropic | Claude Code subagents | Filesystem agents, forks | Referenced, not read |
""") + HR() + "none found; the SDK page says programmatic agents override filesystem agents with the same name.",
 reframe="This is the craft of delegation: **fresh context, narrow tools, a prompt that carries everything, and caps.** The engineer who understands this treats a subagent as a function call.",
))

# ------------------------------------------------------------------ 8.3.6
SPECS.append(dict(
 mod=M, id="8.3.6", title="Tool design principles for agents", short="Tool design principles",
 thesis="A tool is a prompt the model reads at the moment of decision, so a clear name, a description written for the model, actionable errors and bounded output matter more than the implementation.",
 prove="rewrite a poor tool (vague name, generic error, unbounded output) into a good one and show the behaviour change on a fixed task set.",
 discipline="design the result Claude will read, not only the function you will run.",
 counter="the description is the interface: Claude reads it to decide when to call the tool, so a correct implementation behind a vague description is a tool that is not used [" + CT + "].",
 read_min=19, prove_h="2", depth=["Apply the four principles to a tool", "Measure the effect of a redesign", "Choose between one broad and several narrow tools"],
 thin="This guide applies principles the SDK pages state (descriptions as model-read text, actionable errors, output limits, naming for search). The AI curriculum's Part 4.3 is the source of the general principles; its content is not reproduced here and the pages read do not name a fixed set of 'tool design rules'.",
 deliverable="A before/after tool pair with a task-set comparison (selection rate, error recovery, tokens per result).",
 sections=[
 dict(title="Names and descriptions", framing="The docs state that the description tells Claude what the tool does so it can decide when to call it, that `.describe()` on a Zod field or Annotated in Python gives a field description Claude sees, and that names and descriptions are what tool search matches [" + CT + "; " + TS + "].",
  body=T("""
| Element | Weak | Strong |
|---|---|---|
| Name | query_slack | search_slack_messages |
| Tool description | 'Query Slack' | 'Search Slack messages by keyword, channel, or date range' |
| Field description | none | 'Latitude coordinate' via .describe() or Annotated |
| Enum | free string | constrained with z.enum or JSON Schema enum |

[Agent SDK docs, Give Claude custom tools and tool search pages, 2026]. Constraining with enums turns invalid inputs into schema errors before they reach your handler.
"""),
  fm=[("Implementation-first description", "You describe how the tool works internally, not when to use it, and Claude never picks it.", "Write the description as 'when and for what', with the key inputs named.")],
  xr="tool search naming is Module 8.3.4; custom tools are Module 8.3.2.", one="name and describe for the decision, not the code."),
 dict(title="Actionable errors", framing="A failing handler should compose the message Claude reads. The docs' example returns the status, a reason and isError, and notes that an uncaught exception reaches Claude as the raw string with no context [" + CT + "].",
  body=T("""
| Error style | What Claude can do |
|---|---|
| Raw exception 'Unexpected token <' | Guess |
| 'API error: 404 Not Found' with isError | Retry with a different endpoint or report |
| 'Unsupported conversion: furlongs to miles' with isError | Tell the user, pick a supported unit |

Pattern from [Agent SDK docs, Give Claude custom tools, 2026]. Add what to try next when you know it, such as the list of valid values.
"""),
  fm=[("Dead-end error", "The error says 'failed' with no cause, so Claude retries the identical call until max turns.", "Include the cause and one next step in every error result.")],
  xr="turn limits are Module 8.2.1.", one="an error is the next prompt."),
 dict(title="Token-efficient output", framing="Tool output consumes context every turn. MCP results over 25,000 tokens are saved to a file and the result replaced by an error naming the path; a text result over 50,000 characters is saved regardless, unless the tool declares anthropic/maxResultSizeChars [" + MC + "]. structuredContent returns exact fields, and when set, text blocks in content are not forwarded [" + CT + "].",
  body=T("""
| Technique | Effect |
|---|---|
| Paginate and summarize | Smaller results per call |
| Return fields, not prose, via structuredContent | Claude reads exact values |
| Return an image plus its data points | Visual and exact |
| Raise MAX_MCP_OUTPUT_TOKENS | Last resort; costs context |
"""),
  fm=[("Dump-everything result", "A search tool returns every row and the output exceeds the limit, so the agent reads a file path instead of the data.", "Return a page with a count and a cursor, and let Claude ask for more.")],
  xr="context window is Module 8.2.1.", one="return what the next decision needs."),
 dict(title="Scope: one broad tool or several narrow ones", framing="Tool count has a cost: 50 tools can use 10-20K tokens and accuracy degrades past 30-50 loaded tools [" + TS + "]. Annotations help too: readOnlyHint lets the loop run read-only tools in parallel [" + CT + "].",
  body=T("""
| Choice | Benefit | Cost |
|---|---|---|
| Few broad tools | Fewer definitions | Complex schemas; harder to annotate |
| Many narrow tools | Clear names; precise annotations | Context cost; use tool search |
| Split read and write | Parallel reads; clear approvals | More tools |

Rule from the docs' annotations: split so the read-only hint is truthful.
"""),
  fm=[("Swiss-army tool", "One tool does read, write and delete by a mode argument, so it cannot be marked read-only and every call needs approval.", "Split by side effect.")],
  xr="subagent tool scoping is Module 8.3.5.", one="scope tools by side effect."),
 ],
 retrieval=[
  ("What does Claude read to decide when to call a tool?", "The tool's description."),
  ("Which name is better for search: query_slack or search_slack_messages?", "search_slack_messages."),
  ("A description explains internals, not use. Name the failure mode by its exact label.", "**Implementation-first description.**"),
  ("What does an uncaught exception look like to Claude?", "The raw exception message with no context."),
  ("Claude retries an identical failing call. Name the failure mode and fix.", "**Dead-end error.** Add cause and next step."),
  ("At what size are MCP results saved to a file?", "Over 25,000 tokens (no image) or over 50,000 characters of text."),
  ("A search tool returns every row. Name the failure mode by its exact label.", "**Dump-everything result.**"),
  ("What happens to text blocks when structuredContent is set?", "They are not forwarded; Claude gets the JSON plus image/resource blocks."),
  ("One tool with a mode argument does reads and deletes. Name the failure mode.", "**Swiss-army tool.**"),
 ],
 steps=[("Pick a weak tool and write its flaws", "A critique"), ("Rewrite name, description, schema", "A new definition"),
        ("Make errors actionable", "Three error cases"), ("Bound the output", "A paginated result"),
        ("Run 10 tasks before and after; record selection, recovery, tokens", "A comparison table"), ("Split any mixed read/write tool", "Two tools")],
 pass_md=T("""
| Metric | Before | After |
|---|---|---|
| Selected when needed | recorded | recorded |
| Recovered from error | recorded | recorded |
| Tokens per result | recorded | recorded |
"""),
 fail_md=T("""
| Element | What is wrong |
|---|---|
| Only the name changed | **Implementation-first description** remains |
| No numbers | Cannot show improvement |
"""),
 verdict="The artifact passes only if the comparison table is measured on the same task set before and after.",
 resources=T("""
| Source | Title | What it proves | 2026 status |
|---|---|---|---|
| Anthropic | Give Claude custom tools | Descriptions, errors, annotations | Current |
| Anthropic | Scale to many tools with tool search | Naming for search, tool counts | Current |
| AI curriculum | Part 4.3 | General tool principles | Internal; not reproduced |
""") + HR() + "none found among the pages read; the principles here come from SDK documentation rather than a single design guide.",
 reframe="This is the craft of the interface: **the model is the user of every tool.** The engineer who understands this tests tools with a task set, not with a demo.",
))

if __name__ == "__main__":
    for s in SPECS:
        write(s)
