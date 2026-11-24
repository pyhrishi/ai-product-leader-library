import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from specs_b14_0 import *
C0 = '[Claude Code docs, Commands, 2026]'

M = "b-14-2"
SPECS = []
I = "[Claude Code docs, Interactive mode, 2026]"
K = "[Claude Code docs, Keybindings, 2026]"
RI = [("Anthropic", "Interactive mode", "Shortcuts, input modes, history, vim", "Current; read via fetch"), ("Anthropic", "Customize keyboard shortcuts", "Contexts, actions, reserved keys", "Current; read via fetch")]
TH = "Thin sub-topic: one shortcut or setting; depth comes from its interactions, not from volume."

SPECS.append(G(M, "14.2.1", "Shift+Tab: cycling permission modes",
 "Shift+Tab is the fastest control over how much Claude may do without asking, and the order it cycles in is the thing to memorise.",
 "cycle through every mode available to you, naming each, and trigger one action in each.",
 "read the mode indicator before you approve or submit anything.",
 "from auto, the first Shift+Tab press goes to default, not onward; the cycle is not a simple loop in every state " + I + ".",
 16, "1.5", ["Name the modes Shift+Tab visits", "Predict the next mode from the current one", "Rebind or script mode switching safely"],
 "A mode map: each mode, what it allows, and one tested action in it.",
 [S("The cycle", "Shift+Tab cycles through `default` (labelled Manual in the indicator), `acceptEdits`, `plan` and, when available, `bypassPermissions` and then `auto`; from `auto` the first press switches to `default`. On Windows without VT input mode the key is `Alt+M` " + I + ".",
   """
| From | Next press |
|---|---|
| default (Manual) | acceptEdits |
| acceptEdits | plan |
| plan | bypassPermissions or auto, when available |
| auto | default |

Modes shown depend on availability; read your indicator rather than assuming the order.
""", "Blind-cycle", "You press Shift+Tab several times without reading the indicator and land in a mode more permissive than you meant.", "Press once, read the indicator, then continue.", "modes in depth are Module 4.3.", "one press, one read."),
  S("A second meaning on prompts", "On a file permission prompt the same key closes an open comment field; with no field open it selects the option allowing the action for the rest of the session, when the prompt offers that option " + I + ". In the keybindings reference this is `confirm:cycleMode` in the `Confirmation` context " + K + ".",
   """
| Where | Shift+Tab does |
|---|---|
| Main prompt | Cycles mode (`chat:cycleMode`) |
| File permission prompt, field open | Closes the comment field |
| File permission prompt, no field | Allows for the rest of the session |
""", "Session-allow-by-habit", "You press Shift+Tab on a permission prompt out of mode-cycling habit and grant the action for the whole session.", "On a prompt, press Enter or the numbered option on purpose and treat Shift+Tab as a grant.", "permissions are Module 4.2.", "on a prompt, Shift+Tab grants."),
  S("Customising it", "`chat:cycleMode` can be rebound in the `Chat` context, and `confirm:cycleMode` in `Confirmation`, through `~/.claude/keybindings.json` " + K + ". Changes apply without a restart.",
   """
```json
{"bindings":[{"context":"Chat","bindings":{"ctrl+g":"chat:cycleMode"}}]}
```

Choose a key you will not press by accident; reserved keys such as Ctrl+C cannot be used.
""", "Reserved-rebind", "You bind a mode switch to a reserved key and the binding never fires.", "Pick an unreserved key and check the debug log for validation warnings.", "keybinding rules are Module 14.2 (customise).", "bind to unreserved keys.")],
 [("What does the first Shift+Tab press do from auto?", "Switches to default."), ("What is default labelled in the indicator?", "Manual."),
  ("You cycle without reading the indicator. Name the failure mode by its exact label.", "**Blind-cycle.**"), ("On Windows without VT input mode, which key replaces Shift+Tab?", "`Alt+M`."),
  ("You press Shift+Tab on a permission prompt by habit. Name the failure mode.", "**Session-allow-by-habit.**"), ("Which action name cycles the mode?", "`chat:cycleMode`."),
  ("A binding on Ctrl+C never fires. Name the failure mode and fix.", "**Reserved-rebind.** Pick an unreserved key."), ("Which mode follows acceptEdits?", "plan."),
  ("Do keybinding changes need a restart?", "No, they apply without restarting."), ("Which context holds `confirm:cycleMode`?", "`Confirmation`.")],
 [("Read your mode indicator at start", "Note"), ("Press Shift+Tab once at a time and record each mode", "Order list"), ("Run one write action in default and one in acceptEdits", "Two logs"), ("Open a permission prompt and press Shift+Tab", "Observation"), ("Rebind to another key and test", "Log"), ("Draw the cycle", "Diagram")],
 """
| Mode | Action | Observed |
|---|---|---|
| default | edit a file | prompted |
| acceptEdits | edit a file | no prompt |
""", """
| Element | What is wrong |
|---|---|
| Order copied from memory | Differs by availability: **Blind-cycle** risk |
""", "The artifact passes only if the order was recorded from your own indicator.",
 RES(RI, "none found between the sources read."), RF("mode cycling", "one press, one read", "which mode am I in?", "what will this key do in this context?"), thin=TH))

SPECS.append(G(M, "14.2.2", "Escape: interrupt, double-Escape, and rewind",
 "Escape does four different things depending on what is on screen, and only one of them is destructive to your draft.",
 "show Escape interrupting a turn, closing a dialog, clearing a draft and opening rewind.",
 "know what is focused before you press Escape twice.",
 "double Escape with text in the prompt clears the draft but saves it so Up recalls it; with an empty prompt it opens rewind " + I + ".",
 16, "1.5", ["Name Escape's four behaviours", "Predict the effect from the screen state", "Recover a cleared draft"],
 "A four-row Escape table with each behaviour observed, plus a draft recovery.",
 [S("Single Escape", "Escape interrupts the current response or tool call mid-turn; Claude keeps the work done so far, and queued messages are sent next. In a dialog it closes the dialog, with a footer item selected it deselects it, and on a permission prompt it declines the action like No " + I + ".",
   """
| State | Escape does |
|---|---|
| Claude responding | Interrupts; work kept |
| Dialog open | Closes dialog |
| Footer row selected | Deselects it |
| Permission prompt | Declines the action |
""", "Wrong-focus-escape", "You press Escape to stop a run while a footer row is selected and only deselect it, so the run continues.", "Press Escape again, or `Ctrl+C`, after checking focus.", "the loop and interrupting are Module 1.2.1.", "check focus first."),
  S("Double Escape", "With text in the prompt, `Esc Esc` clears the draft and saves it to history so Up recalls it. With an empty input it opens the rewind menu to restore or summarise code and conversation from an earlier point " + I + ".",
   """
| Prompt | `Esc Esc` | Recover |
|---|---|---|
| Has text | Clears and saves draft | Press Up |
| Empty | Opens rewind menu | Choose a point |
""", "Draft-wipe", "You double-press Escape on a long draft meaning to open rewind and lose your place.", "Submit or stash with Ctrl+S first, or press Up to recall.", "checkpoints are Module 2.5.", "double Escape reads the prompt state."),
  S("Related keys", "`Ctrl+C` interrupts or clears input, and a second press with nothing running exits; a cleared draft returns with Up on v2.1.288 or later, and the ten most recent cleared drafts are kept for the session from v2.1.292 " + I + ". `Ctrl+S` stashes the prompt.",
   """
| Key | Use |
|---|---|
| `Ctrl+C` | Interrupt or clear |
| `Ctrl+S` | Stash and restore a draft |
| `Up` | Recall cleared draft |
""", "Exit-by-reflex", "You press Ctrl+C twice by reflex and exit the session.", "Press once, read the hint, then decide.", "sessions are Module 2.4.", "one Ctrl+C at a time.")],
 [("What does Escape do while Claude is responding?", "Interrupts; work done so far is kept."), ("What does `Esc Esc` do on an empty prompt?", "Opens the rewind menu."),
  ("You double-press on a long draft and lose it. Name the failure mode by its exact label.", "**Draft-wipe.**"), ("How do you recover a cleared draft?", "Press Up."),
  ("Escape deselects a row instead of interrupting. Name the failure mode.", "**Wrong-focus-escape.**"), ("From which version does Up recover a cleared draft right away?", "v2.1.288."),
  ("How many cleared drafts are kept?", "Ten, for the session, from v2.1.292."), ("You exit by pressing Ctrl+C twice. Name the failure mode and fix.", "**Exit-by-reflex.** Press once and read the hint."),
  ("What does Escape do on a permission prompt?", "Declines the action."), ("Which key stashes a prompt?", "`Ctrl+S`.")],
 [("Interrupt a running turn", "Observation"), ("Type a draft and press `Esc Esc`; recall with Up", "Observation"), ("Press `Esc Esc` on an empty prompt", "Rewind menu"), ("Open a permission prompt and press Escape", "Observation"), ("Stash with Ctrl+S and restore", "Observation"), ("Fill the table", "Table")],
 """
| State | Press | Observed |
|---|---|---|
| Responding | Esc | Stopped, work kept |
| Draft | Esc Esc | Cleared; Up recalled |
| Empty | Esc Esc | Rewind menu |
""", """
| Element | What is wrong |
|---|---|
| No draft recovery shown | **Draft-wipe** unproven |
""", "The artifact passes only if all four behaviours were observed.",
 RES(RI, "none found between the sources read."), RF("Escape", "read the screen before pressing", "how do I stop this?", "what is focused and is a draft at risk?"), thin=TH))

SPECS.append(G(M, "14.2.3", "Ctrl+G: editing prompts and plans in your editor",
 "Ctrl+G hands the prompt to your own text editor, which is the right move for long prompts, plans and structured instructions.",
 "write a multi-paragraph prompt in your editor via Ctrl+G and submit it.",
 "move to the editor when the prompt exceeds a few lines.",
 "the readline binding Ctrl+X Ctrl+E does the same job, and both are bound to chat:externalEditor " + K + ".",
 14, "1", ["Open and return from the external editor", "Use the last-response context option", "Choose editor-based drafting for plans"],
 "A prompt drafted in your editor, submitted, plus the editor setting you used.",
 [S("What it does", "`Ctrl+G` or `Ctrl+X Ctrl+E` opens your prompt or custom response in your default text editor. Turning on **Show last response in external editor** in `/config` prepends Claude's previous reply as `#`-commented context above your prompt, and Claude Code strips that comment block when you save " + I + ".",
   """
| Key | Action |
|---|---|
| `Ctrl+G` | Open in editor |
| `Ctrl+X Ctrl+E` | Same, readline style |
| Save and close | Content returns to the prompt |
""", "Comment-block-edit", "You edit inside the `#` context block and expect your changes to be sent, but the block is stripped on save.", "Write below the comment block only.", "plan editing is Module 2.2.", "write below the comments."),
  S("When it pays", "Use the editor for multi-paragraph prompts, spec interviews and plan edits; the prompt box is better for one-liners. In agent view the dispatch input follows `chat:externalEditor` single-keystroke bindings, so the `Ctrl+X Ctrl+E` chord does not open the editor there " + K + ".",
   """
| Prompt size | Where to write |
|---|---|
| One line | Prompt box |
| A paragraph or more | Editor via Ctrl+G |
| In agent view | `Ctrl+G` only |
""", "Chord-in-agent-view", "You press the chord in agent view and nothing opens.", "Use Ctrl+G there.", "agent view is Module 6.3.", "single key works everywhere."),
  S("Setting it up", "The editor opened is your default text editor; if the wrong one opens, fix the environment your shell exports before launching Claude Code. This guide did not retrieve the editor environment variable name, so confirm it against the docs.",
   """
| Check | How |
|---|---|
| Which editor opens | Press Ctrl+G once |
| Wrong editor | Fix your shell environment and relaunch |
""", "Wrong-editor-surprise", "A blocking GUI editor opens and the session waits on it.", "Choose a terminal editor or one that returns on close.", "terminal setup is Module 9.1.", "test the editor once.")],
 [("Which keys open the external editor?", "`Ctrl+G` or `Ctrl+X Ctrl+E`."), ("What is the action name?", "`chat:externalEditor`."),
  ("You edit inside the commented context and lose it. Name the failure mode by its exact label.", "**Comment-block-edit.**"), ("What does the `/config` option add?", "Claude's previous reply as `#`-commented context."),
  ("The chord does nothing in agent view. Name the failure mode.", "**Chord-in-agent-view.**"), ("Which key works in agent view?", "`Ctrl+G`."),
  ("A GUI editor blocks the session. Name the failure mode and fix.", "**Wrong-editor-surprise.** Choose an editor that returns on close."), ("What happens to the comment block on save?", "Claude Code strips it."),
  ("When is the editor better than the prompt box?", "For multi-paragraph prompts and plans."), ("Is the chord the readline-native binding?", "Yes, `Ctrl+X Ctrl+E`.")],
 [("Press Ctrl+G and note which editor opens", "Note"), ("Write a three-paragraph prompt", "Prompt"), ("Save and submit", "Observation"), ("Turn on the last-response option", "Setting"), ("Edit below the comment block", "Observation"), ("Try the chord", "Observation")],
 """
| Test | Observed |
|---|---|
| Ctrl+G opens editor | yes |
| Edit below comments | sent |
""", """
| Element | What is wrong |
|---|---|
| Edited the comment block | **Comment-block-edit** |
""", "The artifact passes only if the submitted prompt shows your editor text and not the stripped comments.",
 RES(RI, "none found between the sources read; the editor environment variable was not retrieved."), RF("external editing", "long text belongs in an editor", "why is my prompt box awkward?", "should this be drafted in my editor?"), thin=TH))

SPECS.append(G(M, "14.2.4", "Ctrl+R: searching command history across projects",
 "Ctrl+R finds earlier prompts, and its scope differs between the classic inline search and the fullscreen dialog.",
 "find a prompt from another project with Ctrl+R in both renderers if available.",
 "know which renderer you are in before relying on its scope.",
 "the classic inline search always searches prompts from all projects, while the fullscreen dialog lets Ctrl+S cycle session, project and all " + I + ".",
 14, "1", ["Run a reverse search and accept a match", "Choose scope", "Combine with Up recall and drafts"],
 "A history search log in both modes, including the scope change.",
 [S("Inline search", "In the classic renderer, `Ctrl+R` starts reverse search: type a query, press `Ctrl+R` again to cycle older matches, `Tab` or `Esc` to accept and keep editing, `Enter` to accept and run, `Ctrl+C` to cancel and restore input. It scans full history newest first with duplicates collapsed " + I + ".",
   """
| Key | Action |
|---|---|
| Ctrl+R | Start, then next older match |
| Tab / Esc | Accept, keep editing |
| Enter | Accept and execute |
| Ctrl+C | Cancel, restore input |
""", "Enter-executes", "You press Enter to accept a match and it runs immediately, not edit first.", "Use Tab or Esc to bring it into the prompt for editing.", "prompt reuse is Module 2.2.", "Tab edits, Enter runs."),
  S("Fullscreen dialog", "In fullscreen rendering `Ctrl+R` opens a dialog: type to filter, Up and Down to move, `Ctrl+S` to cycle scope through session, project and all projects, `Enter` or `Tab` to place the match in the prompt, `Esc` to cancel " + I + ".",
   """
| | Classic | Fullscreen |
|---|---|---|
| Scope | All projects, fixed | session, project, all (Ctrl+S) |
| Enter | Executes | Places in prompt |
""", "Scope-assumption", "You assume a fullscreen search covers all projects and it is still on the session scope.", "Press Ctrl+S and read the scope label.", "fullscreen mode is Module 9.1.", "check the scope label."),
  S("History rules", "Input history is stored per working directory; `/clear` starts a new session with its prompts listed first; a duplicate prompt twice in a row records one entry; history expansion with `!` is off by default " + I + ". Vim NORMAL mode `/` opens history search too " + K + ".",
   """
| Rule | Detail |
|---|---|
| Storage | Per working directory |
| After `/clear` | New session first, earlier after |
| Duplicates | Collapsed |
""", "Wrong-directory-history", "You look for a prompt in a directory that never held it and conclude it was lost.", "Search from the original directory, or use all-projects scope.", "sessions are Module 2.4.", "history follows the directory.")],
 [("Which key cycles scope in the fullscreen dialog?", "`Ctrl+S`."), ("What scopes does it cycle?", "Session, project, all projects."),
  ("You press Enter and the match runs. Name the failure mode by its exact label.", "**Enter-executes.**"), ("What does Tab do on a match in classic search?", "Accepts it and continues editing."),
  ("You assume all-projects scope in fullscreen. Name the failure mode.", "**Scope-assumption.**"), ("How is history stored?", "Per working directory."),
  ("A prompt seems lost. Name the failure mode and fix.", "**Wrong-directory-history.** Search from the original directory."), ("Which key cancels and restores input?", "`Ctrl+C`."),
  ("Is `!` history expansion on by default?", "No."), ("What does vim NORMAL-mode `/` do?", "Opens history search.")],
 [("Run Ctrl+R and find an old prompt", "Observation"), ("Accept with Tab and with Enter on two matches", "Two observations"), ("Open fullscreen and cycle scope", "Observation"), ("Search from another directory", "Observation"), ("Recall a duplicate", "Observation"), ("Write the rule sheet", "Sheet")],
 """
| Test | Observed |
|---|---|
| Tab on match | Placed in prompt |
| Enter on match | Executed |
""", """
| Element | What is wrong |
|---|---|
| Scope not checked | **Scope-assumption** |
""", "The artifact passes only if Tab and Enter behaviours were both observed.",
 RES(RI, "none found between the sources read."), RF("history search", "scope and accept key decide the result", "where did that prompt go?", "which scope am I in, and does Enter run or edit?"), thin=TH))

SPECS.append(G(M, "14.2.5", "@ mentions, ! shell mode, and pasted images",
 "Three input prefixes put things into context directly: @ for files, ! for shell commands whose output Claude sees, and image paste.",
 "reference a file with @, run a command with !, and paste an image, then show each in context.",
 "remember that shell mode bypasses Claude's approval and the sandbox.",
 "commands typed in shell mode run outside the sandbox even when sandboxing is on, because the sandbox applies to commands Claude runs " + I + ".",
 18, "1.5", ["Use the three prefixes correctly", "Control response cost of shell mode", "Set rules for what gets pasted"],
 "A demonstration of each prefix with the context effect observed, plus the shell-mode caveat.",
 [S("@ file mentions", "`@` triggers file path autocomplete. In sessions with cross-session messaging, typing at least one letter after `@` also suggests other live sessions on the machine; that requires v2.1.232 or later " + I + ".",
   """
```text
Explain the retry logic in @src/net/client.ts
```

| Typed | Effect |
|---|---|
| `@src/` | Path autocomplete |
| `@` plus a letter, with messaging on | Also suggests live sessions |
""", "Whole-repo-mention", "You mention a very large file or a broad directory and spend context on content you did not need.", "Mention the specific file or range and check `/context`.", "context cost is Module 3.1.", "mention precisely."),
  S("! shell mode", "A leading `!` runs a command directly, adds the command and output to the conversation and shows live progress; it supports Ctrl+B backgrounding, Tab completion from previous `!` commands and exits with Escape, Backspace or Ctrl+U on an empty prompt. Claude responds to the output automatically at the cost of a normal prompt; set `respondToBashCommands` to false to add the output without a response " + I + ".",
   """
```text
! npm test
```

| Property | Value |
|---|---|
| Needs Claude approval | No |
| Sandboxed | No (outside strict sandbox mode sessions) |
| Costs a response | Yes, unless `respondToBashCommands` is false |
""", "Unsandboxed-shell", "You type a risky command in shell mode assuming the sandbox protects it, and it runs with your full access.", "Treat shell mode as your own terminal and check commands before pressing Enter.", "sandboxing is Module 4.4.", "shell mode is you, not Claude."),
  S("Images", "`Ctrl+V` (`Cmd+V` in iTerm2, `Alt+V` on Windows and WSL) pastes an image and inserts an `[Image #N]` chip you can reference by number in the prompt " + I + ".",
   """
| Platform | Paste key |
|---|---|
| Most terminals | Ctrl+V |
| iTerm2 | Cmd+V |
| Windows, WSL | Alt+V (WSL binds both) |
""", "Sensitive-screenshot", "You paste a screenshot that contains secrets or customer data into a session that is stored as a transcript.", "Crop or redact before pasting.", "transcript privacy is Module 11.1.", "screenshots are stored too.")],
 [("What prefix runs a shell command directly?", "`!`."), ("Does shell mode run inside the sandbox?", "No, outside strict sandbox sessions."),
  ("You type a risky command in shell mode expecting protection. Name the failure mode by its exact label.", "**Unsandboxed-shell.**"), ("Which setting stops Claude responding to shell output?", "`respondToBashCommands` false."),
  ("A huge file is mentioned and context balloons. Name the failure mode.", "**Whole-repo-mention.**"), ("Which key pastes an image on Windows?", "`Alt+V`."),
  ("You paste a screenshot with secrets. Name the failure mode and fix.", "**Sensitive-screenshot.** Redact first."), ("What appears when you paste an image?", "An `[Image #N]` chip."),
  ("From which version does `@` suggest other sessions?", "v2.1.232."), ("How do you exit shell mode?", "Escape, Backspace or Ctrl+U on an empty prompt.")],
 [("Mention one file with @ and ask about it", "Observation"), ("Run `! git status` and read the reply", "Observation"), ("Set `respondToBashCommands` false and repeat", "Observation"), ("Paste a small image", "Chip"), ("Check `/context` after each", "Three numbers"), ("Write the caveats", "List")],
 """
| Prefix | Context effect |
|---|---|
| @file | File content added |
| ! cmd | Output added; reply generated |
""", """
| Element | What is wrong |
|---|---|
| Sandbox assumed for `!` | **Unsandboxed-shell** |
""", "The artifact passes only if the context effect of each prefix was measured with /context.",
 RES(RI, "none found between the sources read."), RF("input prefixes", "each prefix puts something in context and has its own trust level", "how do I show Claude this?", "what will this cost in context and who approves it?")))

SPECS.append(G(M, "14.2.6", "Multiline input: Shift+Enter, Option+Enter and friends",
 "Newlines in the prompt are terminal-dependent, and a backslash-Enter or Ctrl+J works everywhere.",
 "enter a three-line prompt using at least two methods.",
 "know the always-working fallback before configuring anything.",
 "Shift+Enter is native in some terminals but needs /terminal-setup in others " + I + ".",
 14, "1", ["Name the methods and where each works", "Fix a terminal that submits on Shift+Enter", "Document a team default"],
 "A table of newline methods tested in your terminal.",
 [S("The methods", "Methods: `\\` then Enter works in all terminals; `Option+Enter` after enabling Option as Meta on macOS; `Shift+Enter` natively in iTerm2, WezTerm, Ghostty, Kitty, Warp, Apple Terminal and Windows Terminal; `Ctrl+J` in any terminal without configuration; and pasting directly for code blocks and logs " + I + ".",
   """
| Method | Works |
|---|---|
| `\\` + Enter | Everywhere |
| `Ctrl+J` | Any terminal, no setup |
| `Shift+Enter` | Native in listed terminals |
| `Option+Enter` | macOS with Option as Meta |
| Paste | Code and logs |
""", "Shift-Enter-submits", "You press Shift+Enter in an unconfigured terminal and the prompt submits half-written.", "Use `\\` + Enter or Ctrl+J, then run `/terminal-setup`.", "terminal setup is Module 9.1.", "keep the universal fallback in mind."),
  S("Setup command", "`/terminal-setup` installs a Shift+Enter binding for VS Code, Cursor, Devin Desktop, Alacritty or Zed; in Apple Terminal it enables Option+Enter and turns off the audible bell; in iTerm2 it enables clipboard access so `/copy` works " + I + ".",
   """
| Terminal | /terminal-setup does |
|---|---|
| VS Code, Cursor, Alacritty, Zed | Installs Shift+Enter |
| Apple Terminal | Option+Enter and bell off |
| iTerm2 | Clipboard access for /copy |
""", "Setup-skipped", "You never run the setup command and live with accidental submits.", "Run it once per terminal.", "terminal config is Module 14.1 (configuration).", "run it once."),
  S("Rebinding", "`chat:newline` is bound to Ctrl+J by default and can be rebound in the `Chat` context; `chat:submit` is Enter, and `chat:queueSubmit` submits while marking the message to wait its turn " + K + ".",
   """
```json
{"bindings":[{"context":"Chat","bindings":{"enter":"chat:newline","ctrl+enter":"chat:submit"}}]}
```
This swap is an example of the syntax, not a recommendation; test before relying on it.
""", "Swap-and-stuck", "You swap Enter and Ctrl+Enter, then your terminal does not report Ctrl+Enter and you cannot submit.", "Keep a working submit key and test the new one before saving.", "keybindings are Module 14.2 (customise).", "never remove your only submit key.")],
 [("Which newline method works in all terminals?", "`\\` followed by Enter."), ("Which needs no configuration in any terminal?", "`Ctrl+J`."),
  ("Shift+Enter submits. Name the failure mode by its exact label.", "**Shift-Enter-submits.**"), ("What does `/terminal-setup` do in Apple Terminal?", "Enables Option+Enter and turns off the audible bell."),
  ("You never run the setup command. Name the failure mode.", "**Setup-skipped.**"), ("Which action inserts a newline?", "`chat:newline`."),
  ("You cannot submit after a rebind. Name the failure mode and fix.", "**Swap-and-stuck.** Keep a working submit key."), ("Name three terminals with native Shift+Enter.", "Any three of iTerm2, WezTerm, Ghostty, Kitty, Warp, Apple Terminal, Windows Terminal."),
  ("What does the iTerm2 setup enable?", "Clipboard access so `/copy` works."), ("What is the pasted-block method for?", "Code blocks and logs.")],
 [("Try each method in your terminal", "Table"), ("Run `/terminal-setup`", "Observation"), ("Retry Shift+Enter", "Observation"), ("Check `chat:newline` default", "Note"), ("Write the team default", "Line"), ("Test the fallback", "Observation")],
 """
| Method | Worked? |
|---|---|
| Backslash+Enter | yes |
| Ctrl+J | yes |
| Shift+Enter | after setup |
""", """
| Element | What is wrong |
|---|---|
| Only Shift+Enter tested | **Shift-Enter-submits** unhandled |
""", "The artifact passes only if every method was tested in your own terminal.",
 RES(RI + [("Anthropic", "Commands", "/terminal-setup", "Current")], "none found between the sources read."), RF("multiline input", "know the universal fallback first", "why did it submit?", "which newline method does my terminal support?"), thin=TH))

SPECS.append(G(M, "14.2.7", "Vim mode: editing the prompt with modal keys",
 "Vim mode is a setting in /config that turns the prompt into a modal editor, and its Escape behaves differently from the default.",
 "enable vim mode, edit a prompt in NORMAL mode and remap jj to Escape.",
 "enable it only if you already think in vim motions.",
 "in vim mode Escape switches INSERT to NORMAL and does not trigger chat:cancel " + K + ".",
 16, "1.5", ["Enable and use modes", "Remap INSERT sequences", "Avoid Escape conflicts"],
 "A short vim-mode session log with mode switches, one text object edit and one remap.",
 [S("Enable and modes", "Vim-style editing is enabled via `/config` then Editor mode; Claude Code keeps your mode and cursor position when you toggle the transcript viewer or open a panel. `Esc` or `Ctrl+[` enters NORMAL mode, and `i`, `I`, `a`, `A`, `o`, `O` enter INSERT; `v` and `V` start visual selection " + I + ". The older `/vim` command was removed in v2.1.92 " + C0 + ".",
   """
| Key (NORMAL) | Action |
|---|---|
| `i` / `I` | Insert before cursor / at line start |
| `a` / `A` | Insert after cursor / at line end |
| `o` / `O` | Open line below / above |
| `v` / `V` | Visual char / line |
""", "Escape-expectation", "You press Escape expecting to cancel and instead enter NORMAL mode, then type text that acts as commands.", "Check the mode indicator, and in NORMAL mode press Escape again where the context cancels.", "terminal setup is Module 9.1.", "Escape changes mode first."),
  S("Remapping", "Vim keys are not remappable through keybindings.json. To map a two-key INSERT sequence such as `jj` to Escape, use the `vimInsertModeRemaps` setting " + K + " " + I + ".",
   """
| Want | Use |
|---|---|
| `jj` to leave INSERT | `vimInsertModeRemaps` setting |
| Rebind Ctrl keys | keybindings.json |
""", "Wrong-remap-file", "You put a vim remap in keybindings.json and it never fires.", "Use the `vimInsertModeRemaps` setting.", "settings are Module 4.1.", "vim keys live in settings."),
  S("Interactions", "In vim NORMAL mode `?` shows the help menu and `/` opens history search. In the `Other` row of a question, Escape does not cancel at once: it switches mode or drops a half-typed command, and a second Escape in NORMAL mode cancels; binding a Ctrl key to `select:cancel` in `Select` cancels with one press " + K + ".",
   """
```json
{"bindings":[{"context":"Select","bindings":{"ctrl+q":"select:cancel"}}]}
```
""", "Stuck-question", "You cannot dismiss a question in vim mode because Escape only changes mode.", "Press Escape twice, or bind a Ctrl key to `select:cancel`.", "agent questions are Module 2.2.", "two Escapes in vim mode.")],
 [("Where do you enable vim mode?", "`/config`, Editor mode."), ("What does Escape do in vim mode?", "Enters NORMAL mode; it does not trigger `chat:cancel`."),
  ("You press Escape expecting a cancel. Name the failure mode by its exact label.", "**Escape-expectation.**"), ("Which setting remaps `jj`?", "`vimInsertModeRemaps`."),
  ("Your remap in keybindings.json never fires. Name the failure mode.", "**Wrong-remap-file.**"), ("What does `/` do in NORMAL mode?", "Opens history search."),
  ("You cannot dismiss a question. Name the failure mode and fix.", "**Stuck-question.** Escape twice or bind a Ctrl key to select:cancel."), ("Which version removed `/vim`?", "v2.1.92."),
  ("What does `?` do in NORMAL mode?", "Shows the help menu."), ("Which key opens a line below?", "`o`.")],
 [("Enable vim mode in /config", "Setting"), ("Switch modes with Escape and i", "Log"), ("Edit a prompt with o and A", "Log"), ("Add a `vimInsertModeRemaps` entry for jj", "Setting"), ("Test it", "Observation"), ("Bind Ctrl+Q to select:cancel and test in a question", "Observation")],
 """
| Test | Observed |
|---|---|
| Esc | NORMAL mode |
| jj remap | Leaves INSERT |
""", """
| Element | What is wrong |
|---|---|
| Remap in keybindings.json | **Wrong-remap-file** |
""", "The artifact passes only if the remap was set in settings and observed working.",
 RES(RI + [("Anthropic", "Commands", "/vim removal", "Current")], "none found between the sources read; the `vimInsertModeRemaps` value format was not retrieved."), RF("vim mode", "modal editing with its own Escape", "why did Escape not cancel?", "which mode am I in?"), thin=TH))

SPECS.append(G(M, "14.2.8", "/keybindings: customising shortcuts",
 "Keybindings are a JSON file of context blocks mapping keystrokes to named actions, validated at load, hot-reloaded, with a short list of keys you cannot touch.",
 "bind one key, unbind one default and trigger a validation warning on purpose.",
 "run Claude Code with --debug after editing so validation warnings are visible.",
 "a misspelled modifier does not fail loudly: ctl+k is silently reduced to k, and the warning only shows in the debug log " + K + ".",
 22, "2", ["Write a valid bindings file", "Predict conflicts and reserved keys", "Standardise team bindings safely"],
 "A working keybindings.json with one bind, one unbind, one chord, and a captured validation warning.",
 [S("File and structure", "`/keybindings` creates or opens `~/.claude/keybindings.json`. The file is an object with a `bindings` array; each block names a `context` and a map of keystrokes to actions, and changes are detected and applied without a restart " + K + ".",
   """
```json
{
  "$schema": "https://www.schemastore.org/claude-code-keybindings.json",
  "bindings": [
    { "context": "Chat",
      "bindings": { "ctrl+e": "chat:externalEditor", "ctrl+s": null } }
  ]
}
```

| Part | Meaning |
|---|---|
| `context` | Where the block applies (Global, Chat, Autocomplete, Confirmation, Transcript, HistorySearch, Select and others) |
| `"action"` | Namespace:action such as `chat:submit` |
| `null` | Unbinds a default |
""", "Wrong-context", "You bind a key in `Chat` for an action that belongs to `Confirmation` or `Select`, and it never fires where you expect.", "Look up the action's context in the reference and put the block there.", "settings files are Module 4.1.", "an action lives in one context."),
  S("Syntax", "Modifiers are `ctrl`, `shift`, `alt`/`opt`/`option`/`meta` and `cmd`/`command`/`super`/`win`; key names are case-insensitive; chords are space-separated and each keystroke must follow within 3 seconds; the `cmd` group is detected only in terminals that report Super, so prefer `ctrl` or `meta` for portable bindings " + K + ".",
   """
```text
ctrl+k ctrl+s     chord: press within 3 seconds
meta+p            Option+P on macOS, Alt+P elsewhere
ctrl+ k           BROKEN: a space next to + makes a chord of "ctrl+" then "k"
```
""", "Spaced-plus", "You write `ctrl+ k` and Claude Code reads it as a chord whose first stroke never matches, so the binding never fires.", "Remove spaces around `+` and check the debug log.", "terminal behaviour is Module 9.1.", "no spaces next to plus."),
  S("Reserved keys and prefixes", "Ctrl+C, Ctrl+D, Ctrl+M, Ctrl+[, Ctrl+I, Ctrl+H and Caps Lock cannot be rebound. Default chords share the `ctrl+x` prefix, and unbinding only some of them leaves the prefix in chord-wait mode " + K + ".",
   """
| Reserved | Why |
|---|---|
| Ctrl+C | Hard-coded interrupt |
| Ctrl+D | Hard-coded exit |
| Ctrl+M, I, [ | Arrive as Enter, Tab, Escape |
| Ctrl+B, Ctrl+A, Ctrl+Z | Not reserved, but conflict with tmux, screen and suspend |
""", "Half-freed-prefix", "You unbind a few ctrl+x chords hoping to use ctrl+x alone and it still waits for a second key.", "Unbind every chord on the prefix, in each context that defines it.", "terminal conflicts are Module 14.2 (multiline).", "free a prefix all at once."),
  S("Validation and team use", "Claude Code writes warnings to the debug log for parse errors, misspelled modifiers, spaced `+`, invalid contexts, unknown actions, reserved-key conflicts and duplicates; start with `--debug` to see them " + K + ". An unknown action name skips the binding and keeps the default for that key.",
   """
| Problem | Result |
|---|---|
| Invalid JSON | Warning, file not applied |
| Unknown action | Binding skipped, default stays |
| Reserved key | Warning |
| Duplicate in context | Warning |
""", "Silent-typo", "You mistype an action name and believe your binding is live because nothing visibly failed.", "Launch with `--debug`, trigger the key and read the log.", "debugging is Part 12.", "typos only show in the debug log.")],
 [("Where is the keybindings file?", "`~/.claude/keybindings.json`."), ("What value unbinds a default?", "`null`."),
  ("You write `ctrl+ k`. Name the failure mode by its exact label.", "**Spaced-plus.**"), ("How long do you have between chord keystrokes?", "3 seconds."),
  ("You mistype an action and see no error. Name the failure mode.", "**Silent-typo.**"), ("Name three reserved keys.", "Any three of Ctrl+C, Ctrl+D, Ctrl+M, Ctrl+[, Ctrl+I, Ctrl+H, Caps Lock."),
  ("You bind an action in the wrong context. Name the failure mode and fix.", "**Wrong-context.** Put the block in the action's own context."), ("Is a restart needed after editing the file?", "No."),
  ("You unbind some ctrl+x chords and the prefix still waits. Name the failure mode.", "**Half-freed-prefix.**"), ("What does an unknown action do?", "The binding is skipped and the default stays.")],
 [("Run /keybindings and read the file", "File"), ("Bind one key and test", "Log"), ("Unbind ctrl+s and confirm stash is gone", "Log"), ("Add a chord and test within 3 seconds", "Log"), ("Add a typo on purpose and read the --debug warning", "Warning text"), ("List five reserved keys", "List")],
 """
| Change | Observed |
|---|---|
| ctrl+e bound | Editor opened |
| ctrl+s null | Stash disabled |
| ctl+k typo | Debug warning shown |
""", """
| Element | What is wrong |
|---|---|
| No --debug run | **Silent-typo** untested |
""", "The artifact passes only if one validation warning was captured from the debug log.",
 RES(RI, "none found between the sources read."), RF("keybindings", "contexts, actions and a debug log", "why didn't my key work?", "which context, which action name, and what did --debug say?")))

if __name__ == "__main__":
    run(SPECS)
