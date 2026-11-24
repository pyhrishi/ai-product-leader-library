# The AI Product Leader Library

One book, three volumes, built to be navigated rather than read straight through.

- **Volume A, AI Product Leader:** 954 topics across AI science, engineering, product craft, safety, industry, leadership and the frontier.
- **Volume B, Claude Code Mastery:** 777 topics from the agentic loop to subagents, hooks, the Agent SDK, security and PM workflows.
- **Volume C, The Elite Layer:** 49 topics on judgment, evals, AI economics, go-to-market, agents in production and public proof of work.

## Features

- Home with two portals (product and builder), a daily mission, goals, progress and an activity heatmap
- One module per page, with search across every topic and micro-topic (`/` or Ctrl+K)
- Tick topics, set a 0 to 5 level per module, keep notes per page
- **Review:** spaced repetition (1, 3, 7, 21, 60, 120 days) on topics you ticked
- **Mock interview:** timed questions scored on claim, reason, example, trade-off
- **Study plan:** three tracks, weekly hour budget, dated schedule, "behind" tracking
- **Gap finder:** ranks the modules that matter most for your goal and that you have mastered least
- **Project board:** 73 projects with status, links and a portfolio export
- **Notes dashboard** and a **cheat sheet** per module from your ticks and notes
- Related topics across volumes, backup and restore, light and dark themes
- Installable on iPhone and Android, works offline

## Install on your phone

- **iPhone:** open the site in Safari, tap Share, then Add to Home Screen.
- **Android:** open the site in Chrome, tap the menu, then Install app.

Progress is saved on the device. Use **Backup** in the top bar to export and restore it.

## Run locally

```
python3 -m http.server 8000
```

Open http://localhost:8000. No build step is needed.

## Edit the content

The curriculum lives in `source/*.md`. After editing, rebuild the data file:

```
cd source && python3 -I build_data.py
```

This rewrites `data.json`. Topic lines use the form `- **4.2.1 Title:** micro-topic, micro-topic`.

## Freshness

Command names, flags, prices and limits change often. Recheck Claude Code details monthly against the official docs.
