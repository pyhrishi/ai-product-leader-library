# Start here

## Part 1: How to use this library

This is one book in three volumes. Volume A is the AI Product Leader curriculum. Volume B is the Claude Code mastery curriculum. Volume C is an elite layer that covers what separates a strong AI product leader from a top 0.1% one. Everything is navigable by Part, Module, numbered Topic and micro-topic. Nothing here is meant to be read straight through.

### The shape of the library

- **Volume A, AI Product Leader:** science, engineering, product craft, safety, industry, leadership and frontier. Seventeen Parts, about 150 modules.
- **Volume B, Claude Code Mastery:** the tool you build and prove things with. Eighteen Parts, from the agentic loop to the Agent SDK, security and PM workflows.
- **Volume C, The Elite Layer:** judgment, evals as a craft, AI economics, distribution, production agents, regional regulation, org design, public proof of work and frontier watch.
- **Bridge:** a map that shows which part of Volume B trains which part of Volume A, and three tracks that combine both.
- **Every topic line** has a numbered title, then micro-topics after the colon. Tick a topic when you can explain it without notes and have used it once.

### Your first 90 minutes

1. Read the Bridge map once, so you know how the volumes connect.
2. Pick one of the three tracks in the Bridge and write its first three modules into the notes box of this page.
3. Open the first module of that track. Read only its depth target and prove-it line.
4. Do the prove-it exercise in Claude Code before reading the rest of the module.
5. Come back, read the topics, and tick the ones you can now explain.
6. Set your self-assessed level for the module. Be strict. Level 3 means you can defend a trade-off in front of engineers.

### A weekly rhythm for 15 to 20 hours

- **Two deep sessions, 4 hours each:** one module from the science or craft side, with a build or a written explanation as output.
- **Three build sessions, 2 hours each:** project ladder work in Claude Code, always with a verifiable check (tests, an eval, a measurement).
- **One review session, 2 hours:** reread your notes, re-answer five question-bank items aloud, update levels, pick next week's modules.
- **One public artifact per month:** a post, a teardown, a demo or a talk. Teaching exposes the holes.

### How progress, levels and notes work

- **Ticks** are per topic and roll up to module, part, volume and library totals.
- **Level** is a self-assessment per module: 0 untouched, 1 aware, 2 conversant, 3 decision-capable, 4 authoritative, 5 frontier.
- **Notes** are per page and stay with the page you wrote them on.
- **Saving:** progress saves in this browser at once. When you are signed in, it also saves to your account so it follows you across devices. Use Export in the menu for a manual backup.

### Freshness protocol

AI and Claude Code change monthly. A curriculum that is not refreshed becomes a museum. Use this protocol.

- **Monthly, 60 minutes:** reread the Claude Code docs changelog and commands reference. Check the model lineup and pricing pages of the three or four labs you track. Note anything that contradicts a topic here in that module's notes.
- **Quarterly, 3 hours:** skim new papers from the Part 16 reading library sources, update your L4 and L5 areas, retire one outdated belief in writing.
- **Rule for volatile facts:** model names, prices, limits, flags, command names and permission modes go stale fastest. Treat any such detail in this book as a pointer to look up, never as the truth.
- **Rule for durable ideas:** the agentic loop, context as a scarce resource, verification-first work, evals, trade-off thinking and unit economics outlive any version. Spend most of your depth there.

## Part 2: The bridge between the volumes

### Bridge map

The left column is what a top AI product leader must master. The right column is where you train it with Claude Code. Use the links to jump.

| AI Product Leader topic | Claude Code training ground | What to do |
| --- | --- | --- |
| [Applied AI engineering](#a-4) | [Context engineering and memory](#b-3) | Treat CLAUDE.md and context hygiene as a live lab for prompt and context engineering. Run the same task with and without good context and measure. |
| [Applied AI engineering: tools and agents](#a-4) | [The extension layer](#b-5) and [The Agent SDK](#b-8) | Build an MCP server, a subagent and a hook. Then build the same agent loop with the SDK. |
| [Data, analytics and experimentation](#a-6) | [Applied engineering with Claude Code](#b-9) | Make every change verifiable: tests, evals, before-and-after measurements. |
| [AI product craft](#a-8) | [Claude Code for PMs and non-engineers](#b-13) | Prototype each product idea end to end, then write the PRD from what the prototype taught you. |
| [Safety, security, ethics, law and governance](#a-10) | [Security and safe operation](#b-11) and [Configuration, permissions and control](#b-4) | Study prompt injection, permission modes and sandboxing as real product safety decisions. |
| [Software, systems and infrastructure](#a-5) | [Enterprise, administration and cost](#b-10) | Learn how cost, rate limits, gateways and managed settings shape an AI product at scale. |
| [Frontier and futures](#a-13) | [The frontier](#b-18) | Track where autonomy, parallel agents and scheduled work are heading. |
| [Project ladder](#a-15) | [Project ladder](#b-15) | Pair each AI project with the Claude Code project that builds it fastest. |

### Three tracks that combine both volumes

- **Track 1, Fluency in 8 weeks:** Volume A Part 3 modules 3.1 to 3.4, then Part 4, then Part 8, in parallel with Volume B Parts 1 to 3 and Part 13. Output: you hold an informed conversation with any engineer and ship a working prototype weekly.
- **Track 2, Builder-PM in 6 months:** Volume B Parts 1 to 9 and 15, with Volume A Parts 4 to 6 and the Tier 1 to 3 projects. Output: three shipped projects with evals and write-ups.
- **Track 3, Leader in 24 months:** all of Volume A, Volume B Parts 10 to 13 and 18, and every Volume C part. Output: L4 in five areas, L5 in one or two, a public body of work.

### How to pick your L4 and L5 areas

- Choose areas where your job gives you real reps. For an AI product leader that is usually evals, agent products and AI economics.
- Choose one area that the market undervalues today and will want in two years.
- Write the choice in your notes. Revisit it every quarter.

# The Elite Layer

## Part 1: Judgment and taste

Judgment is the scarcest skill in AI product work, because models make generation cheap and choice expensive. These modules train it deliberately.

### Module 1.1 Product taste for AI

- **1.1.1 Reading model output like an editor:** spotting subtle errors, fluent nonsense, overconfidence, missing caveats, generic filler, tone mismatches, and the difference between impressive and useful.
- **1.1.2 Trust calibration design:** how much a user should trust the output, signals that earn trust, signals that mislead, when to show uncertainty, when to hide it, and the cost of both mistakes.
- **1.1.3 The last 20 percent problem:** why demos look finished at 80 percent, how long-tail failures dominate user experience, and how to scope work to what is actually reliable.
- **1.1.4 Deleting features:** removing AI where a rule works better, where a button is clearer, or where users do not want automation.
*Depth target: L4.*
*Prove-it: review ten real AI product teardowns and write what you would cut, with the reason for each.*

### Module 1.2 Decision quality under uncertainty

- **1.2.1 Reversible versus irreversible calls:** one-way and two-way doors for models, vendors, architectures and launches.
- **1.2.2 Pre-mortems and kill criteria:** writing the failure story first, setting measurable stop conditions before building.
- **1.2.3 Base rates for AI projects:** how often prototypes reach production, typical timelines, common reasons for failure, and how to use that as a prior.
- **1.2.4 Writing decisions down:** decision records, the options considered, what would change your mind, and reviewing them after six months.
*Depth target: L4.*
*Prove-it: keep a decision log for 90 days and score your own calibration.*

## Part 2: Evals as a core competence

Evals are the single biggest differentiator between teams that ship reliable AI products and teams that ship demos. Treat this as a first-class craft.

### Module 2.1 Designing an eval program

- **2.1.1 From failure analysis to eval set:** reading hundreds of real traces, open coding failure modes, clustering them, and turning each into a test.
- **2.1.2 Golden sets and their rot:** building, versioning, refreshing, balancing coverage against cost, and detecting when the set stopped representing production.
- **2.1.3 Graders you can trust:** code checks, rubric graders, LLM judges, pairwise comparison, human review, and the validation of the grader itself against human labels.
- **2.1.4 Online and offline loops:** shadow mode, sampling production, thumbs signals, implicit signals, and how offline scores predict online outcomes.
- **2.1.5 Eval-driven development:** writing the eval before the prompt, gating releases on it, and tracking regressions per model and per prompt change.
*Depth target: L4 to L5.*
*Prove-it: build an eval for a RAG or agent product with at least 100 labeled cases, a validated judge, and a regression gate in CI.*

### Module 2.2 Evals for agents and long tasks

- **2.2.1 Trajectory evaluation:** judging outcomes versus steps, tool-call correctness, recovery from errors, cost and latency per task.
- **2.2.2 Environments and simulators:** sandboxed tasks, replayable states, user simulators, and the limits of simulation.
- **2.2.3 Reliability metrics:** pass rate versus pass-all-of-k rate, variance across runs, and why averages hide the failures users remember.
*Depth target: L4.*
*Prove-it: write a report that shows how reliability changes across ten runs of the same agent task.*

## Part 3: AI economics and business models

### Module 3.1 Unit economics of an AI feature

- **3.1.1 Cost per successful task:** tokens, retries, tool calls, retrieval, review labor, and cost per outcome rather than per request.
- **3.1.2 Margin under model price changes:** how falling prices help and hurt, the cost of being locked to one vendor, routing across models, and caching strategy.
- **3.1.3 Pricing models:** seats, usage, credits, outcomes and hybrids, and which to choose for which product shape.
- **3.1.4 Build, buy or partner:** the real cost of owning a capability, switching costs, and when a wrapper is a business.
*Depth target: L4.*
*Prove-it: build a model of a real AI feature with cost per task, price, margin and three sensitivity cases.*

### Module 3.2 Competitive position

- **3.2.1 Moats that survive model upgrades:** proprietary data, workflow depth, distribution, trust, integrations, switching costs and network effects.
- **3.2.2 Platform risk:** when labs and incumbents ship your feature, how to read that risk early, and how to build where the platform will not go.
- **3.2.3 Market structure:** how value splits across chips, clouds, labs, tooling and apps, and where margins sit today and may sit next.
*Depth target: L4.*
*Prove-it: write a one-page defensibility analysis of two AI products and argue which survives the next two model generations.*

## Part 4: Distribution and go-to-market

### Module 4.1 Getting AI products adopted

- **4.1.1 Activation in AI products:** the first successful outcome, time to value, setup friction, and designing a first-run experience around a real result.
- **4.1.2 Enterprise sales motion:** pilots, security reviews, procurement, champion building, and turning a pilot into a contract.
- **4.1.3 Product-led growth with AI:** free tiers and their cost, virality, templates, and community.
- **4.1.4 Positioning and narrative:** explaining value without hype, handling skepticism, and category creation.
*Depth target: L3 to L4.*
*Prove-it: write a launch plan for an AI feature with activation metrics, pricing, and objections with responses.*

## Part 5: Operating agents in production

### Module 5.1 Reliability and operations

- **5.1.1 Observability for agents:** traces, spans, tool logs, cost dashboards, replay, and alerting on quality as well as errors.
- **5.1.2 Failure containment:** timeouts, budgets, step limits, circuit breakers, human escalation, and safe defaults.
- **5.1.3 Permissions and blast radius:** least privilege for tools, approval gates, audit logs, and reversible actions.
- **5.1.4 Incident response for AI:** bad output incidents, prompt injection incidents, data leakage, postmortems, and communication.
- **5.1.5 Change management:** model upgrades, prompt versioning, canaries, rollbacks, and user communication.
*Depth target: L4.*
*Prove-it: write a runbook for an agent product and run a tabletop exercise against it.*

## Part 6: Regulation and regional context

Treat every legal detail as a pointer to verify. Rules change and differ by jurisdiction. This is knowledge for product decisions, not legal advice.

### Module 6.1 The regulatory map

- **6.1.1 The EU AI Act in product terms:** risk tiers, general-purpose model duties, documentation, transparency, and how it affects a product's launch scope.
- **6.1.2 India context:** the Digital Personal Data Protection Act, sector regulators such as the banking and securities regulators, the IndiaAI Mission, and local model and compute efforts.
- **6.1.3 US landscape:** state-level rules, sector guidance, procurement requirements, and litigation trends around data and copyright.
- **6.1.4 Compliance as product work:** consent, retention, audit trails, model documentation, vendor due diligence, and customer security questionnaires.
*Depth target: L3.*
*Prove-it: map the obligations for one AI feature in a regulated domain such as banking, and list the product changes they require.*

## Part 7: The AI-native organization

### Module 7.1 Teams, roles and ways of working

- **7.1.1 The AI-native PM:** prototyping as a core skill, evals ownership, writing specs that agents can execute, and shrinking the idea-to-test cycle to hours.
- **7.1.2 Team shape:** roles for evals, applied AI, data, design and safety, and when to hire versus upskill.
- **7.1.3 Working with agents as teammates:** delegation patterns, review load, shared context files, and accountability.
- **7.1.4 Culture of experimentation:** rapid prototypes, honest postmortems, demo days, and measuring learning velocity.
*Depth target: L4.*
*Prove-it: redesign one team's weekly workflow around agents and measure cycle time before and after.*

## Part 8: Public proof of work and career

### Module 8.1 Becoming visible and hireable

- **8.1.1 A portfolio that proves judgment:** three case studies with problem, decision, evidence, result and what you would change.
- **8.1.2 Writing in public:** one clear post a month, teardown format, original measurement, and opinions backed by data.
- **8.1.3 Interview mastery for AI PM roles:** product sense for AI, technical depth rounds, eval and metric design, estimation, strategy, and behavioral stories.
- **8.1.4 Network and reputation:** communities, open-source contributions, talks, mentoring, and referrals.
- **8.1.5 Negotiation and role choice:** evaluating AI-native roles, equity, scope, mentors and learning rate.
*Depth target: L4.*
*Prove-it: publish three case studies and run five mock interviews with feedback.*

## Part 9: Frontier watch

### Module 9.1 A permanent radar

- **9.1.1 Signals worth tracking:** model releases, agent capabilities, long-horizon task results, inference cost curves, safety findings and enterprise adoption data.
- **9.1.2 Forming and revising theses:** write five falsifiable predictions per year, score them, and update your worldview.
- **9.1.3 Staying calm in hype cycles:** separating demo, benchmark, product and business, and asking what evidence would change the claim.
- **9.1.4 Long-term bets:** which skills compound regardless of model progress: judgment, taste, systems thinking, communication and domain depth.
*Depth target: L4.*
*Prove-it: publish a dated list of predictions and review them after 12 months.*
