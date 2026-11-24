# Worker brief: deep sub-topic guides

Repo: /home/claude/repo (shared working tree, remote origin/main). You own ONE part of data.json (given in your task). For EVERY sub-topic item (ids like `2.1.3`, found in data.json `vols[*].parts[*].pages[*].blocks` items with `id` matching `^\d+(\.\d+){2,3}$`) write a deep guide.

## Method
1. Read `tools/gen.py` (generator + assertions) and `tools/specs_12.py` (the canonical spec example; `T()` helper is imported from it) and one rendered output, e.g. `guides/b-1-2_1.2.6.md`.
2. Extract your part's modules and sub-topic items (id + title + the text `x`) with a small python script.
3. For each module, research with WebSearch/WebFetch (official docs: code.claude.com/docs for Claude Code; official vendor docs/papers for AI topics). Only state facts you retrieved. Cite as "[Source, page, 2026]". Flag secondary sources "[secondary: ...]" and anything unverified. Never invent numbers, flags, versions or commands; if you cannot verify, say so in the guide.
4. Write `tools/specs_<part>_<n>.py` per module (copy the specs_12.py skeleton: `SPECS` list + `write`). Spec `mod` is the module page id (e.g. `b-2-1`), `id` the sub-topic id. Each guide: 3-4 sections, each with a framing paragraph, a table/code/diagram, one failure mode (label,text,fix) unique to the guide, cross-references to real module ids ("Module x.y"), a one-line takeaway; 8-12 retrieval questions (>=3 naming "by its exact label"/failure mode, >=2 needing a number); steps; pass/fail artifacts; verdict; resources with a named disagreement; reframe. 1300-2000 words. No filler. Quality over speed: if a sub-topic is thin, say so in a `thin` note rather than padding.
5. Run `python3 tools/specs_<...>.py`; fix assertion errors. Do NOT edit gen.py, index.html, sw.js, data.json, or guides/index.json.
6. Save work every ~5 guides:
   `flock /tmp/git.lock sh -c 'cd /home/claude/repo && git add guides/*_<yourprefix>* guides/_meta tools/specs_<yourprefix>* && git commit -q -m "Deep guides <part> batch" -m "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>" -m "Claude-Session: https://claude.ai/code/session_01UjUDBo1pm8YhJPUzLWJZco" && git push -q origin HEAD:main'`
   (use `git add` on explicit paths only; never `git add -A`; never touch other workers' files). If push fails, retry once after `git pull --rebase origin main` inside the same flock.
7. Finish with a final push and report: guides written, any thin/unverified spots. Do not publish artifacts. Keep your final report under 150 words.
