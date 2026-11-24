import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from wk_b1011 import make, run, T, D

M = "b-10-2"
SPECS = []
TPI = "[Claude Code docs, Enterprise deployment overview, 2026]"
AUTH = "[Claude Code docs, Authentication, 2026]"
COST = "[Claude Code docs, Manage costs effectively, 2026]"
FA = "[Claude Code docs, Feature availability, 2026]"
BED = "[Claude Code docs, Claude Code on Amazon Bedrock, 2026]"
VTX = "[Claude Code docs, Claude Code on Google Cloud's Agent Platform, 2026]"
FDY = "[Claude Code docs, Claude Code on Microsoft Foundry, 2026]"
CPA = "[Claude Code docs, Claude Code on Claude Platform on AWS, 2026]"
GHA = "[Claude Code docs, Use Claude Code GitHub Actions with cloud providers, 2026]"

# ------------------------------------------------------------------ 10.2.1
SPECS.append(make(M, "10.2.1", "First-party: subscriptions and the Console",
 "First-party means Anthropic runs inference and billing, through a per-seat subscription or a pay-as-you-go Console organisation, and the two have different controls.",
 "choose between Teams, Enterprise and Console for a named team and justify it against three constraints.",
 "decide first-party versus cloud provider by features and controls, then Teams versus Console by who pays and how.",
 "the Teams and Enterprise allowance is shared with Claude chat and Cowork, so a coding seat drains the same pool as a chat seat " + COST + ".",
 [("Subscriptions: Teams and Enterprise",
   "For most organisations the docs recommend Claude for Teams or Enterprise: one subscription for Claude Code and Claude on the web, centralised billing and no infrastructure. Teams is self-service with admin tools and billing management; Enterprise adds domain capture, role-based permissions, compliance API access and managed policy settings " + TPI + ". Usage draws from a per-seat allowance that resets on a rolling five-hour window and a weekly window, shared with chat and Cowork, sized by seat tier (Standard or Premium) " + COST + ".",
   """
| Item | Teams | Enterprise |
|---|---|---|
| Billing | $150/seat (Premium) with PAYG available | Contact sales |
| Includes Claude on web | Yes | Yes |
| Extras named by the overview | Team management, SSO, usage monitoring | SSO and domain capture, role-based permissions, compliance API, managed policy |
| Allowance windows | Rolling 5-hour and weekly | Rolling 5-hour and weekly |
""",
   ("Chat-seat budgeting", "You size coding seats from chat usage, then developers exhaust the weekly allowance because each Claude Code turn carries file contents, tool calls and multi-step reasoning.", "Budget a coding seat above a chat seat; start from the pilot distribution (Module 10.1)."),
   "pilot sizing is Module 10.1; plan limits are Module 1.4.",
   "the allowance is one shared pool, so coding burns it faster than chat."),
  ("The Console path",
   "Console suits API-first organisations that want pay-as-you-go billing. Invite users from the Members page or set up SSO, then assign a role: the Claude Code role lets users only create Claude Code API keys; the Developer role lets them create any kind of key " + AUTH + ". When you first authenticate with a Console account, a workspace called Claude Code is created automatically for centralised cost tracking; you cannot create API keys for it " + COST + ".",
   """
| Role | Can do |
|---|---|
| Claude Code | Create only Claude Code API keys |
| Developer | Create any kind of API key |

Console sign-in without an API key (Claude Code v2.1.242 or later) stores an OAuth token as an Anthropic profile instead of a static key " + AUTH + ".
""".replace('" + AUTH + "', AUTH),
   ("Over-privileged role", "You invite every engineer as Developer, so anyone can mint production-scoped API keys.", "Assign the Claude Code role by default; grant Developer only to those who build on the API."),
   "key and login precedence is Module 10.3.",
   "least privilege starts at the invitation."),
  ("Console rate limits",
   "The costs page recommends per-user Token Per Minute and Request Per Minute figures by team size, which apply at the organisation level, so individuals can temporarily exceed their share when others are idle " + COST + ". Live training sessions may need more.",
   """
| Team size | TPM per user | RPM per user |
|---|---|---|
| 1-5 | 200k-300k | 5-7 |
| 20-50 | 50k-75k | 1.25-1.75 |
| 100-500 | 15k-20k | 0.37-0.47 |
| 500+ | 10k-15k | 0.25-0.35 |

Worked example from the docs: 200 users at 20k TPM each is 4 million total TPM.
""",
   ("Training-day throttle", "You request limits from the steady-state table and then run a 100-person live workshop, so everyone is rate limited at once.", "Request temporary headroom for concentrated sessions."),
   "cost governance is Module 10.6.",
   "per-user TPM falls as headcount rises, but events break the assumption."),
  ("Choosing first-party",
   "The deployment overview compares six options on billing, regions, authentication and cost tracking; first-party columns use claude.ai SSO or email (subscriptions) or an API key (Console) and track cost in the usage dashboard " + TPI + ". Choose first-party when you want features that need a claude.ai account.",
   """
| Need | First-party answer |
|---|---|
| Cloud sessions, Routines, Code Review | Subscription seat required |
| Pay per token, API-first | Console |
| Inherit AWS/GCP/Azure compliance | Cloud provider instead (Module 10.2.2) |
""",
   ("Console-for-everything", "You choose Console because billing is simpler, then discover cloud sessions and Code Review need a subscription.", "List required features before choosing the billing model."),
   "cloud providers are Module 10.2.2; features matrix is Module 10.2.5.",
   "features pick the account type; billing picks the plan."),
 ],
 [("Over what windows does the seat allowance reset?", "A rolling five-hour window and a weekly window."),
  ("What does the Console Claude Code role let a user do?", "Create only Claude Code API keys."),
  ("What is the Teams Premium seat price in the overview table?", "$150 per seat, with PAYG available."),
  ("Give the recommended TPM per user for a 100-500 user team.", "15k-20k."),
  ("200 users at 20k TPM: what total TPM?", "4 million."),
  ("You sized coding seats from chat usage. Name the failure mode by its exact label.", "**Chat-seat budgeting.**"),
  ("Everyone was invited as Developer. Name the failure mode.", "**Over-privileged role.**"),
  ("A 100-person live workshop was throttled. Name the failure mode.", "**Training-day throttle.**"),
  ("You chose Console and lost cloud sessions. Name the failure mode.", "**Console-for-everything.**"),
 ],
 [("List features you need that require a claude.ai account", "Feature list"), ("Choose plan or Console with reasons", "`choice.md`"), ("If Console, define roles per group", "Role table"),
  ("Compute TPM request from team size", "TPM sheet"), ("Add an event headroom line", "Event plan"), ("Review against pilot spend", "Review note")],
 ("A first-party choice memo with role table and TPM request.", """
| Team | Plan | Role | TPM request |
|---|---|---|---|
| Platform (40) | Enterprise | n/a | n/a |
| Data API (20) | Console | Claude Code | 20 x 60k |
"""),
 """
| Element | What is wrong |
|---|---|
| All users 'Developer' | **Over-privileged role** |
| No event headroom | Training-day throttle |
""",
 "The memo passes only if each choice cites a required feature or a billing constraint and role grants follow least privilege.",
 [("Anthropic", "Enterprise deployment overview", "Plan comparison table", "Current"),
  ("Anthropic", "Authentication", "Console roles and sign-in", "Current"),
  ("Anthropic", "Manage costs effectively", "Allowance windows, TPM table", "Current")],
 "the overview says Enterprise adds SSO, while the authentication page lists SSO under Teams and the feature table marks SSO available on both; treat SSO as available on Team and Enterprise per the feature table.",
 "This is the craft of first-party choice: **features decide the account type, billing decides the plan, roles follow least privilege.** The administrator who understands this does not ask \"which is cheaper?\" — they ask \"what must developers be able to do?\"",
))

# ------------------------------------------------------------------ 10.2.2
SPECS.append(make(M, "10.2.2", "Cloud providers",
 "Four cloud routes exist, each switched on by one environment variable and each with its own credential model, so confusing them is the commonest setup error.",
 "fill a table of switch variable, credential source, region setting and cost console for all four routes from memory.",
 "set exactly one provider switch and run /status to read back the provider line.",
 "Claude Platform on AWS is not Bedrock: it is the Anthropic-operated API with AWS authentication, and provisioning it creates a new Anthropic organisation separate from any you already have " + CPA + ".",
 [("The four routes",
   "Amazon Bedrock is enabled with `CLAUDE_CODE_USE_BEDROCK=1`; Google Cloud's Agent Platform (formerly Vertex AI) with `CLAUDE_CODE_USE_VERTEX=1`, `CLOUD_ML_REGION` and `ANTHROPIC_VERTEX_PROJECT_ID`; Microsoft Foundry with `CLAUDE_CODE_USE_FOUNDRY=1` and `ANTHROPIC_FOUNDRY_RESOURCE`; Claude Platform on AWS with `CLAUDE_CODE_USE_ANTHROPIC_AWS=1` and the required `ANTHROPIC_AWS_WORKSPACE_ID` " + BED + " " + VTX + " " + FDY + " " + CPA + ".",
   """
| Route | Switch | Auth | Cost console |
|---|---|---|---|
| Amazon Bedrock | `CLAUDE_CODE_USE_BEDROCK=1` | API key or AWS credentials | AWS Cost Explorer |
| Claude Platform on AWS | `CLAUDE_CODE_USE_ANTHROPIC_AWS=1` | API key or AWS credentials (SigV4) | AWS Cost Explorer |
| Google Agent Platform | `CLAUDE_CODE_USE_VERTEX=1` | GCP credentials | GCP Billing |
| Microsoft Foundry | `CLAUDE_CODE_USE_FOUNDRY=1` | API key or Microsoft Entra ID | Azure Cost Management |
""",
   ("Switch collision", "More than one `CLAUDE_CODE_USE_*` variable is set, and the wrong provider wins: Bedrock and Foundry take precedence over Claude Platform on AWS.", "Set one switch per environment and confirm with `/status`."),
   "wizards are Module 10.2.3; pinning is Module 10.2.4.",
   "one switch, one provider, one `/status` check."),
  ("Credentials per route",
   "Bedrock uses the default AWS SDK credential chain, with options from `aws configure` to SSO profiles to `AWS_BEARER_TOKEN_BEDROCK`; resolved credentials are cached until five minutes before expiry and each resolve times out after 60 seconds " + BED + ". Foundry accepts an API key, the Azure default credential chain, or a bearer token in `ANTHROPIC_FOUNDRY_AUTH_TOKEN`, which takes precedence over the key " + FDY + ". Claude Platform on AWS: `ANTHROPIC_AWS_API_KEY` takes precedence over SigV4 " + CPA + ".",
   """
```bash
# Foundry precedence (highest first)
ANTHROPIC_FOUNDRY_AUTH_TOKEN   # bearer
ANTHROPIC_FOUNDRY_API_KEY      # key
# otherwise Azure default credential chain
```
""",
   ("Stale key shadow", "A leftover API key silently overrides your federated credentials, so every request fails with access denied.", "Unset the key variable or regenerate it; verify which credential wins with `/status`."),
   "login and identity are Module 10.3.",
   "the more specific credential wins, even when stale."),
  ("The organisation boundary",
   "Subscribing to Claude Platform on AWS through AWS Marketplace provisions a new Anthropic organisation tied to your AWS account; credentials do not transfer between it and any existing organisation, so use the workspace ID and keys from the AWS-linked one " + CPA + ". Claude Platform on AWS bills through AWS Marketplace and gives the same models and API features as the Claude API on the same release schedule.",
   """
| Question | Bedrock | Claude Platform on AWS |
|---|---|---|
| Who operates inference | AWS | Anthropic |
| Billing | PAYG through AWS | PAYG through AWS Marketplace |
| Needs workspace ID | No | Yes (`ANTHROPIC_AWS_WORKSPACE_ID`) |
""",
   ("Wrong-organisation key", "You paste a Console API key into the AWS route and get 403s, because the keys belong to a different organisation.", "Generate keys in the AWS Console under Claude Platform on AWS, and use the AWS-linked workspace ID."),
   "backend differences are Module 10.2.5.",
   "check which organisation a key belongs to before debugging IAM."),
  ("Operating notes",
   "WebSearch is not available on Bedrock; `/logout` is unavailable on cloud providers because authentication is handled by the cloud credentials; Foundry has no startup model check, so requests fail when the default is unavailable " + BED + " " + FDY + ". Where a Foundry deployment auto-updates to latest, create deployments with an explicit version instead.",
   """
| Route | Notable limit |
|---|---|
| Bedrock | No WebSearch; Invoke API only, not Converse |
| Foundry | No setup wizard; no startup model check |
| Agent Platform | Model availability varies by region type |
""",
   ("Latest-alias outage", "A deployment tracks 'latest', the provider moves it, and a model your account cannot invoke becomes the default.", "Pin model versions (Module 10.2.4) and create versioned deployments."),
   "pinning is Module 10.2.4.",
   "pin before you scale."),
 ],
 [("Which variable switches on Amazon Bedrock?", "`CLAUDE_CODE_USE_BEDROCK=1`."),
  ("Which variable is required on Claude Platform on AWS and is sent as a header on every request?", "`ANTHROPIC_AWS_WORKSPACE_ID`, sent as `anthropic-workspace-id`."),
  ("How long does each Bedrock credential-chain resolve wait before timing out?", "60 seconds."),
  ("Both Bedrock and Platform-on-AWS switches are set. Which wins?", "Bedrock."),
  ("Two switches are set and the wrong provider answers. Name the failure mode by its exact label.", "**Switch collision.**"),
  ("An old API key overrides SSO credentials. Name the failure mode.", "**Stale key shadow.**"),
  ("A Console key is rejected on the AWS Marketplace route. Name the failure mode.", "**Wrong-organisation key.**"),
  ("A 'latest' deployment moved under you. Name the failure mode.", "**Latest-alias outage.**"),
  ("Which cloud route has no interactive setup wizard?", "Microsoft Foundry."),
 ],
 [("Fill the four-route table from memory", "`routes.md`"), ("Set one switch on a test machine", "Env file"), ("Run `/status` and record the provider line", "Evidence"),
  ("Add a second switch and observe precedence", "Observation"), ("Rotate a credential and re-test", "Result"), ("Write the precedence rule in one line", "Rule")],
 ("A four-route table plus a recorded `/status` provider line for each route you use.", """
| Route | Switch | `/status` provider line |
|---|---|---|
| Bedrock | USE_BEDROCK=1 | Amazon Bedrock |
| Foundry | USE_FOUNDRY=1 | Microsoft Foundry |
"""),
 """
| Element | What is wrong |
|---|---|
| Two USE_* variables set in the profile | **Switch collision** |
| Key pasted from Console | Wrong-organisation key |
""",
 "The table passes only if each route has a switch, a credential source and a `/status` line you actually observed.",
 [("Anthropic", "Claude Code on Amazon Bedrock", "Switch, credentials, IAM", "Current"),
  ("Anthropic", "Claude Code on Claude Platform on AWS", "Workspace ID, separate organisation", "Current"),
  ("Anthropic", "Claude Code on Microsoft Foundry", "Three auth methods", "Current"),
  ("Anthropic", "Claude Code on Google Cloud's Agent Platform", "Project, region, IAM role", "Current")],
 "none found between the sources read.",
 "This is the craft of cloud routing: **one switch, one credential path, one organisation boundary, one status check.** The administrator who understands this does not ask \"is IAM wrong?\" — they ask \"which provider and which credential is actually answering?\"",
))

# ------------------------------------------------------------------ 10.2.3
SPECS.append(make(M, "10.2.3", "Setup wizards",
 "The Bedrock and Vertex wizards configure one developer's user settings; fleets need the manual route, and Foundry has no wizard at all.",
 "run a wizard on a test account, find what it wrote, and translate that block into a managed-settings fragment.",
 "treat wizard output as a template for fleet configuration, never as the fleet configuration.",
 "the wizard writes to the user settings file, which a developer can edit, so it cannot enforce anything [" + "Claude Code docs, Claude Code on Amazon Bedrock, 2026].",
 [("What the wizards are",
   "Run `claude`, choose 3rd-party platform at the login prompt, then Amazon Bedrock or Google Vertex AI (the label the prompt still uses for Agent Platform). If already signed in, `/setup-bedrock` opens the Bedrock wizard and `/setup-vertex` the Vertex one; until `CLAUDE_CODE_USE_BEDROCK=1` is set, Claude Code hides `/setup-bedrock` from the command menu, so type it in full " + BED + " " + VTX + ".",
   """
| Wizard | Opens via | Chooses |
|---|---|---|
| Bedrock | `/setup-bedrock` or login prompt | AWS profile, Bedrock API key, access key, or environment credentials; region; model pins |
| Vertex | `/setup-vertex` or login prompt | ADC from gcloud, service account key, or environment; project; region; model pins |
| Foundry | none | Environment variables only |
""",
   ("Hidden command panic", "You search the command menu for `/setup-bedrock`, do not see it, and conclude the version is too old.", "Type the command in full; it appears in the menu only once the switch variable is set."),
   "the provider routes are Module 10.2.2.",
   "the command exists even when the menu hides it."),
  ("What the wizard writes",
   "The wizard saves its result to the `env` block of your user settings file, so you do not export variables yourself. It writes `~/.claude/settings.json`, or `$CLAUDE_CONFIG_DIR/settings.json` when `CLAUDE_CONFIG_DIR` is set; re-run it any time to change credentials, region or pins " + BED + ".",
   """
```json
// ~/.claude/settings.json (wizard output shape)
{
  "env": {
    "CLAUDE_CODE_USE_BEDROCK": "1",
    "AWS_REGION": "us-east-1",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "us.anthropic.claude-sonnet-4-6"
  }
}
```
""",
   ("Wizard-as-policy", "You tell developers to run the wizard and consider the fleet configured, but each can change it and drift appears within weeks.", "Copy the produced `env` keys into managed settings and treat the wizard as a bootstrap."),
   "managed delivery is Module 10.4.",
   "wizards configure; managed settings enforce."),
  ("Verification inside the wizard",
   "For Bedrock, the wizard verifies which Claude models your account can invoke and lets you pin them, and applies a 60 second limit to each AWS call it makes while verifying credentials; a check that exceeds it fails with a `Timed out after 60s waiting for AWS` message " + BED + ". Behind a TLS-inspecting proxy whose root certificate is only in the OS store, versions before v2.1.261 could show models as `unreachable` while inference worked.",
   """
| Symptom | Likely cause | Fix |
|---|---|---|
| Models show `unreachable` | Old version behind TLS-inspecting proxy | Update to v2.1.261 or later |
| `Timed out after 60s waiting for AWS` | Credential helper stalled | Fix chain or raise `CLAUDE_CODE_AWS_CHAIN_RESOLVE_TIMEOUT_MS` |
""",
   ("Unreachable-model misread", "The wizard marks models unreachable and you conclude the account lacks access, when only the certificate trust was wrong.", "Check the version and the CA configuration before requesting access."),
   "network and certificates are Module 10.5.",
   "read the wizard's failure as a network symptom first."),
  ("From wizard to fleet",
   "For CI or a scripted rollout the Bedrock and Vertex pages give a manual setup; the docs say to pin model versions before rolling out to a team " + BED + ". [Practitioner approach: run the wizard on one machine, diff `settings.json`, and promote the keys to your managed source.]",
   """
| Step | Output |
|---|---|
| Run wizard on a test machine | `env` block |
| Remove personal keys (profiles, secrets) | Clean block |
| Promote to managed settings | Fleet fragment |
| Verify with `/status` | Evidence |
""",
   ("Personal values promoted", "You copy a personal AWS profile name or token into the fleet fragment.", "Strip user-specific values and keep only provider, region and model pins."),
   "managed settings are Module 10.4.",
   "promote the shape, not the secrets."),
 ],
 [("Which command reopens the Bedrock wizard once signed in?", "`/setup-bedrock`."),
  ("Which login-prompt choice leads to the wizards?", "3rd-party platform."),
  ("Where does the wizard save its result by default?", "The `env` block of `~/.claude/settings.json`."),
  ("How many seconds does each wizard AWS call wait before timing out?", "60."),
  ("From which version are the wizard's model checks fixed behind TLS-inspecting proxies?", "v2.1.261."),
  ("You cannot see `/setup-bedrock` in the menu and blame the version. Name the failure mode by its exact label.", "**Hidden command panic.**"),
  ("Developers ran the wizard and drift appeared. Name the failure mode.", "**Wizard-as-policy.**"),
  ("Models show unreachable but inference works. Name the failure mode.", "**Unreachable-model misread.**"),
  ("A personal profile name landed in the fleet block. Name the failure mode.", "**Personal values promoted.**"),
 ],
 [("Run the wizard on a test account", "Screen notes"), ("Diff `settings.json` before and after", "`diff.txt`"), ("Strip personal values", "Clean fragment"),
  ("Place the fragment in managed settings", "Managed file"), ("Run `/status` as a clean user", "Evidence"), ("Document the Foundry exception", "Note")],
 ("A before/after diff and a clean fleet fragment verified with `/status`.", """
| Key | Kept | Reason |
|---|---|---|
| CLAUDE_CODE_USE_BEDROCK | Yes | Provider |
| AWS_PROFILE | No | Personal |
"""),
 """
| Element | What is wrong |
|---|---|
| Fragment includes AWS_PROFILE=alice | **Personal values promoted** |
| No managed delivery | Wizard-as-policy |
""",
 "The artifact passes only if the fleet fragment contains no personal values and a clean user's `/status` shows the provider.",
 [("Anthropic", "Claude Code on Amazon Bedrock", "Wizard steps and timeouts", "Current"),
  ("Anthropic", "Claude Code on Google Cloud's Agent Platform", "Vertex wizard", "Current"),
  ("Anthropic", "Claude Code on Microsoft Foundry", "No wizard", "Current")],
 "the login prompt still says Google Vertex AI while the docs call the product Google Cloud's Agent Platform; the label is a naming lag, not a different route.",
 "This is the craft of setup: **wizards bootstrap, managed settings enforce, `/status` proves.** The administrator who understands this does not ask \"did they run the wizard?\" — they ask \"what keys did it write, and who owns them now?\"",
))

# ------------------------------------------------------------------ 10.2.4
SPECS.append(make(M, "10.2.4", "Model pinning and regional concerns",
 "On a cloud provider, an unpinned alias resolves to Claude Code's built-in default, so the model your developers use, and the price they pay, can change with a client update.",
 "write a pin block for one provider, state the region setting, and predict what each alias resolves to without it.",
 "pin every alias before rollout and record the region prefix or location you intend.",
 "an unpinned Bedrock or Vertex deployment is billed at the Opus rate once it updates to v2.1.207 or later, because the primary model default moved to Opus " + BED + ".",
 [("Pin every alias",
   "Without pinning, aliases such as `sonnet` and `opus` resolve to Claude Code's built-in default for the provider, which can lag the newest release and may not be enabled in your account. Pin with `ANTHROPIC_DEFAULT_FABLE_MODEL`, `ANTHROPIC_DEFAULT_OPUS_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL` and `ANTHROPIC_DEFAULT_HAIKU_MODEL` " + TPI + ".",
   """
```bash
# Bedrock example from the docs
export ANTHROPIC_DEFAULT_OPUS_MODEL='us.anthropic.claude-opus-4-8'
export ANTHROPIC_DEFAULT_SONNET_MODEL='us.anthropic.claude-sonnet-4-6'
export ANTHROPIC_DEFAULT_HAIKU_MODEL='us.anthropic.claude-haiku-4-5-20251001-v1:0'
```
""",
   ("Alias drift", "You rely on `opus` and `sonnet` aliases; a client update moves the alias target and every developer silently changes model.", "Pin each alias to an explicit model ID before rollout and re-pin deliberately on upgrade."),
   "model settings are Module 4.6; cost impact is Module 10.6.",
   "an alias is a moving target."),
  ("The cost trap",
   "On Bedrock the primary model default is Opus 5.5 and the small/fast default is Sonnet 4.5; on Google's Agent Platform the primary default is `claude-opus-5`. The docs warn that Opus has a higher per-token price than Sonnet, so an unpinned deployment is billed at the Opus rate after updating to v2.1.207 or later; to keep Sonnet 4.5, set `ANTHROPIC_MODEL` to its full ID " + BED + " " + VTX + ".",
   """
| Provider | Primary default (no pin) | Small/fast default |
|---|---|---|
| Amazon Bedrock | Opus 5.5 | Sonnet 4.5 |
| Google Agent Platform | `claude-opus-5` | `claude-sonnet-4-5@20250929` |
| Foundry | `opus` alias resolves to Opus 4.6 | Defaults to the primary model |
""",
   ("Silent Opus upgrade", "A routine client update changes the primary model default to Opus and spend jumps with no policy change.", "Set `ANTHROPIC_MODEL` or the alias pins and alert on model mix in telemetry."),
   "telemetry is Module 10.6.",
   "an update can change the bill without changing the policy."),
  ("Regional routing",
   "On Bedrock Claude Code resolves cross-region inference profile prefixes by region: `us-gov.` for `us-gov-*`, `us.` for `us-*`, `eu.` for `eu-*`, `apac.` for `ap-*`, and `global.` otherwise; `ANTHROPIC_BEDROCK_REGION_PREFIX` accepts `us`, `eu`, `apac`, `jp`, `au` and `global` (v2.1.224 or later), and GovCloud always uses `us-gov.` " + BED + ". On the Agent Platform, `CLOUD_ML_REGION` can be `global`, a multi-region such as `eu` or `us`, or a region such as `us-east5`, with `VERTEX_REGION_CLAUDE_*` overrides for models without global endpoints; an invalid region falls back to `us-east5` " + VTX + ".",
   """
| AWS region | Prefix |
|---|---|
| `us-gov-*` | `us-gov.` |
| `us-*` | `us.` |
| `eu-*` | `eu.` |
| `ap-*` | `apac.` |
| other | `global.` |
""",
   ("Prefix mismatch", "You set a prefix for which your account has no inference profiles and requests fail with a 400.", "Run `aws bedrock list-inference-profiles` in the region and choose a prefix you actually have."),
   "data residency is Module 10.7.6 topic and Module 10.7.",
   "a preferred prefix is a preference, not a guarantee."),
  ("Map versions to your own profiles",
   "The `modelOverrides` setting maps Anthropic model IDs to your own inference profile ARNs, so several versions of one family can appear in `/model` without bypassing your profiles; `--model` and `ANTHROPIC_MODEL` values pass through the map from v2.1.200 " + BED + ". Startup checks skip pins that are application inference profile ARNs because administrators manage them.",
   """
```json
{ "modelOverrides": {
  "claude-opus-4-7": "arn:aws:bedrock:us-east-2:123456789012:application-inference-profile/opus-47-prod"
} }
```
""",
   ("ARN as alias", "You set an ARN as the default and expect Claude Code to prompt when a newer model arrives; it never does, because ARN pins are skipped.", "Update ARN mappings on your own release calendar."),
   "cost allocation by profile is Module 10.6.",
   "ARN pins make you the release manager."),
 ],
 [("Name the four pinning environment variables' model families.", "Fable, Opus, Sonnet, Haiku."),
  ("What does Bedrock resolve `opus` to without a pin?", "Opus 5.5."),
  ("What prefix does Claude Code prefer for an `eu-*` region?", "`eu.`"),
  ("Name three valid values for `ANTHROPIC_BEDROCK_REGION_PREFIX`.", "Any three of us, eu, apac, jp, au, global."),
  ("What region does Vertex fall back to when the value is invalid?", "`us-east5`."),
  ("A client update changed the primary model and spend jumped. Name the failure mode by its exact label.", "**Silent Opus upgrade.**"),
  ("Aliases moved after an update. Name the failure mode.", "**Alias drift.**"),
  ("Requests return 400 after setting a prefix. Name the failure mode.", "**Prefix mismatch.**"),
  ("An ARN default never prompts for upgrade. Name the failure mode.", "**ARN as alias.**"),
 ],
 [("Write the four-alias pin block", "`pins.env`"), ("List inference profiles in your region", "Profile list"), ("State prefix or location", "Region note"),
  ("Run `/status` and record resolved model", "Evidence"), ("Predict unpinned behaviour", "Prediction"), ("Set a re-pin calendar", "Calendar")],
 ("A pin block, region note and `/status` evidence.", """
| Alias | Pinned ID | Region prefix |
|---|---|---|
| sonnet | us.anthropic.claude-sonnet-4-6 | us. |
"""),
 """
| Element | What is wrong |
|---|---|
| Only `sonnet` pinned | **Silent Opus upgrade** risk on the `opus` alias |
""",
 "The block passes only if all four aliases are pinned and the prefix was checked against listed profiles.",
 [("Anthropic", "Claude Code on Amazon Bedrock", "Defaults, prefixes, overrides", "Current"),
  ("Anthropic", "Claude Code on Google Cloud's Agent Platform", "Regions and fallbacks", "Current"),
  ("Anthropic", "Enterprise deployment overview", "Pin recommendation", "Current")],
 "Bedrock and Agent Platform pages give different default models; each is per provider and both are current.",
 "This is the craft of pinning: **explicit IDs, a known region, and a calendar for moving on.** The administrator who understands this does not ask \"which model do we have?\" — they ask \"who decided, and when does it change?\"",
))

# ------------------------------------------------------------------ 10.2.5
SPECS.append(make(M, "10.2.5", "Feature availability matrix",
 "Not every feature exists on every backend; the matrix, not memory, decides what you can promise a team.",
 "produce a one-page matrix for your backend listing what is missing, the alternative, and who needs a separate seat.",
 "read the provider tab before promising a feature.",
 "the CLI and everything local work on every provider, but cloud sessions, Routines, Remote Control and the Chrome extension need a claude.ai sign-in " + FA + ".",
 [("What works everywhere",
   "These work on every provider: CLI and Agent SDK, VS Code and JetBrains extensions, subagents, hooks, commands, skills, CLAUDE.md, plugins, MCP servers, checkpoints, sandboxing, workflows, OpenTelemetry metrics and the managed settings file " + FA + ".",
   """
| Always available | Needs care |
|---|---|
| CLI, Agent SDK, IDE extensions | MCP connectors from claude.ai need a subscription login |
| Subagents, hooks, skills, plugins | Tool search varies by provider and model generation |
| Checkpoints, sandboxing, workflows | `/design-sync`, `/import` unavailable off first-party |
""",
   ("Everything-works assumption", "You assume local features imply cloud features, and promise scheduled routines on Bedrock.", "Read the subscription-required list before promising anything remote."),
   "backend routes are Module 10.2.2.",
   "local works everywhere; remote needs a seat."),
  ("The claude.ai-only list",
   "Features that require a claude.ai account and are unreachable from a Console key or cloud provider: cloud sessions, mobile and Slack, Desktop, Routines (`/schedule`), Ultrareview, Code Review (Team and Enterprise), Remote Control, the Chrome extension, computer use (Pro and Max), Artifacts and voice dictation " + FA + ".",
   """
| Needs claude.ai | Plan note |
|---|---|
| Cloud sessions | Enterprise: premium or Chat + Claude Code seat |
| Code Review | Team and Enterprise |
| Computer use | Pro and Max only |
| Remote Control, Channels | Admin-enabled on Team/Enterprise |
""",
   ("Seat-gap surprise", "A Bedrock team expects Code Review and finds no route; the seat was never purchased.", "Decide which groups also need claude.ai seats before announcing features."),
   "plans are Module 1.4; cloud sessions are Module 4.5.",
   "some features follow the seat, not the cloud."),
  ("Per-backend gaps",
   "Bedrock lacks web search, fast mode, advisor, channels, analytics dashboard, server-managed settings and `/design-sync`/`/import`; Claude Platform on AWS adds web search back but lacks GitHub Actions; Google's platform supports web search on Claude 4 models and later; Foundry supports web search only on Anthropic-hosted deployments and lacks GitLab CI/CD. Auto mode on cloud providers supports only Sonnet 5 or later, Opus 4.7 or later and Fable models " + FA + ".",
   """
| Feature | Bedrock | Platform on AWS | Agent Platform | Foundry |
|---|---|---|---|---|
| Web search | No | Yes | Claude 4+ | Anthropic-hosted only |
| GitHub Actions | Yes | No | Yes | Yes |
| GitLab CI/CD | Yes | Yes | Yes | No |
| Server-managed settings | No | No | No | No |
""",
   ("Matrix memorisation", "You memorise last quarter's matrix and miss a change.", "Re-read the page at every client version upgrade and date your copy."),
   "managed settings delivery alternatives are Module 10.4 and Module 10.5.",
   "date-stamp your copy of the matrix."),
  ("Gateways and alternatives",
   "For an LLM gateway, availability matches the underlying provider except what Claude Code turns off: a non-default host in `ANTHROPIC_BASE_URL` switches off Remote Control and server-managed settings " + FA + ". On gateway sessions through Claude apps gateway, WebSearch is disabled and the 1-hour cache TTL is unavailable [Claude Code docs, Claude apps gateway, 2026]. The page lists alternatives: `/loop` instead of `/schedule`, GitHub Actions or GitLab CI/CD for cloud sessions, WebFetch with a URL for web lookups.",
   """
| Missing | Alternative the docs name |
|---|---|
| `/schedule` | `/loop` |
| Cloud sessions | GitHub Actions or GitLab CI/CD |
| Web search (Bedrock) | WebFetch with a specific URL |
""",
   ("Gateway blind spot", "You route through a gateway and assume nothing changes, but Claude Code disables features whenever the base URL is non-Anthropic.", "Test the feature list through the gateway, not through the provider."),
   "gateways are Module 10.5.",
   "a gateway can remove features the provider supports."),
 ],
 [("Name three features that require a claude.ai account.", "Any three of cloud sessions, Routines, Remote Control, Code Review, Chrome extension, Desktop."),
  ("Which backend lacks web search entirely?", "Amazon Bedrock."),
  ("Which backend lacks GitHub Actions?", "Claude Platform on AWS."),
  ("Which backend lacks GitLab CI/CD?", "Microsoft Foundry."),
  ("Which models does auto mode support on Bedrock, Agent Platform and Foundry?", "Sonnet 5 or later, Opus 4.7 or later and the Fable models."),
  ("You promised Routines on Bedrock. Name the failure mode by its exact label.", "**Everything-works assumption.**"),
  ("A Bedrock team lacks the seat for Code Review. Name the failure mode.", "**Seat-gap surprise.**"),
  ("A gateway silently disabled features. Name the failure mode.", "**Gateway blind spot.**"),
  ("Last quarter's matrix missed a change. Name the failure mode.", "**Matrix memorisation.**"),
 ],
 [("Copy the provider tab for your backend", "`matrix.md`"), ("List the features you promised", "Promise list"), ("Mark each: ok, partial, missing", "Marked list"),
  ("Name the alternative for each missing item", "Alternatives"), ("List seat purchases needed", "Seat list"), ("Date and version-stamp the page", "Stamp")],
 ("A dated matrix with every promised feature marked and an alternative named.", """
| Promised | Status | Alternative |
|---|---|---|
| Scheduled agents | Missing on Bedrock | `/loop` |
| Code Review | Needs Team seat | Seat order |
"""),
 """
| Element | What is wrong |
|---|---|
| No date or version | **Matrix memorisation** |
| Remote features listed as ok on Bedrock | Everything-works assumption |
""",
 "The matrix passes only if every promised feature is marked against the current provider tab and dated.",
 [("Anthropic", "Feature availability", "Provider tabs and plan table", "Current"),
  ("Anthropic", "Claude apps gateway", "Gateway-specific limits", "Current"),
  ("Anthropic", "Enterprise deployment overview", "Provider comparison", "Current")],
 "the feature page says SSO is available on Team, while the overview groups SSO under Enterprise; the matrix is the more detailed source.",
 "This is the craft of availability: **read the tab, name the gap, name the alternative.** The administrator who understands this does not ask \"does Claude Code have X?\" — they ask \"does it have X on our backend, for our seats, through our gateway?\"",
))

# ------------------------------------------------------------------ 10.2.6
SPECS.append(make(M, "10.2.6", "GitHub Actions through cloud providers",
 "The GitHub Action calls the Claude API by default; to use your own cloud it takes one provider input plus an OIDC trust you configure on the cloud side, so no long-lived cloud key lives in the repository.",
 "write a workflow with the correct provider input, permissions and OIDC step, and name the cloud-side trust it needs.",
 "scope the cloud trust to one repository and verify the commenter before any credential step.",
 "on public repositories a comment containing the trigger phrase from any user starts the workflow, and credential steps run before the action checks the commenter's write access " + GHA + ".",
 [("Provider input and OIDC",
   "Set one input in the `anthropics/claude-code-action` step: `use_bedrock: \"true\"`, `use_vertex: \"true\"` or `use_foundry: \"true\"`. The workflow needs the `id-token: write` permission so GitHub issues the OIDC token your cloud exchanges for short-lived credentials " + GHA + ".",
   """
```yaml
permissions: { contents: write, pull-requests: write, issues: write, id-token: write }
...
- uses: aws-actions/configure-aws-credentials@v4
  with: { role-to-assume: ${{ secrets.AWS_ROLE_TO_ASSUME }}, aws-region: us-west-2 }
- uses: anthropics/claude-code-action@v1
  with: { github_token: ${{ steps.app-token.outputs.token }}, use_bedrock: "true",
          claude_args: '--model us.anthropic.claude-sonnet-4-6' }
```
""",
   ("Missing id-token", "The workflow omits `id-token: write`, no OIDC token is issued, and authentication fails.", "Add the permission; check trust repository conditions and secret names match."),
   "cloud setup is Module 10.2.2; CI is Module 7.8.",
   "no id-token permission, no federation."),
  ("Cloud-side trust",
   "On AWS, add a GitHub OIDC provider (URL `https://token.actions.githubusercontent.com`, audience `sts.amazonaws.com`), create a role with the Bedrock invocation policy and limit trust to your repository, for example `repo:your-org/your-repo:*`. On Google Cloud, enable IAM Credentials, STS and the Agent Platform API, create a Workload Identity Pool with an attribute condition for your repository, and a service account with only `roles/aiplatform.user`. On Azure, register an Entra application with a federated credential and assign `Foundry User` on the resource " + GHA + ".",
   """
| Cloud | Secrets | Least-privilege role |
|---|---|---|
| AWS | `AWS_ROLE_TO_ASSUME` | Bedrock invoke policy |
| Google | `GCP_WORKLOAD_IDENTITY_PROVIDER`, `GCP_SERVICE_ACCOUNT` | `roles/aiplatform.user` |
| Azure | `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID` | `Foundry User` |
""",
   ("Org-wide trust", "The trust policy allows `repo:your-org/*`, so any repository in the organisation can assume the Claude role.", "Pin the subject or attribute condition to the one repository."),
   "least privilege is Module 11.3.",
   "scope the trust to one repository."),
  ("The public-repository trap",
   "The docs warn that credential steps run before the action checks the commenter's write access, so an unauthorised commenter can trigger an App token and a cloud sign-in, leaving audit-log entries and consuming Actions minutes. Add a step that verifies the commenter's write access before the credential steps. Bound cost with `--max-turns` in `claude_args` " + GHA + ".",
   """
```text
trigger comment
  -> [verify commenter has write access]   <- add this first
  -> generate App token
  -> cloud OIDC sign-in
  -> claude-code-action (--max-turns N)
```
""",
   ("Credentials-before-check", "Anyone can comment and force a cloud sign-in on a public repository.", "Verify write access before the credential steps and cap turns."),
   "prompt injection through comments is Module 11.2.",
   "authorise the commenter before spending credentials."),
  ("GitHub identity choices",
   "Choose the GitHub identity: the official Claude GitHub App, a custom app with only Contents, Issues and Pull requests read and write permissions, or the automatic `GITHUB_TOKEN`, which does not trigger your CI workflows on commits it makes " + GHA + ". Bedrock cross-region model IDs need access granted in every region of the region group. The feature table marks GitHub Actions available on Bedrock, Agent Platform and Foundry but not Claude Platform on AWS " + FA + ".",
   """
| Identity | Trade-off |
|---|---|
| Official Claude GitHub App | Full official permission set |
| Custom GitHub App | Only three permissions; you maintain it |
| `GITHUB_TOKEN` | No app; does not trigger CI on its commits |
""",
   ("Silent CI skip", "You use `GITHUB_TOKEN`, Claude pushes fixes, and your CI never runs on them.", "Use an App token when downstream workflows must run."),
   "CI patterns are Module 7.8.",
   "choose the identity by what must trigger next."),
 ],
 [("Which input selects Bedrock in the action?", "`use_bedrock: \"true\"`."),
  ("Which workflow permission lets GitHub issue the OIDC token?", "`id-token: write`."),
  ("What audience does the AWS GitHub OIDC provider use?", "`sts.amazonaws.com`."),
  ("Which role should the Google service account hold?", "`roles/aiplatform.user`."),
  ("Which three repository permissions does a custom GitHub App need?", "Contents, Issues and Pull requests, all read and write."),
  ("Any user's comment started a credential flow on a public repo. Name the failure mode by its exact label.", "**Credentials-before-check.**"),
  ("No OIDC token was issued. Name the failure mode.", "**Missing id-token.**"),
  ("The trust policy allowed the whole organisation. Name the failure mode.", "**Org-wide trust.**"),
  ("CI did not run on Claude's commits. Name the failure mode.", "**Silent CI skip.**"),
 ],
 [("Choose a provider input and identity", "`choice.md`"), ("Write cloud trust limited to one repo", "Trust policy"), ("Add secrets", "Secret list"),
  ("Write the workflow with commenter check", "`claude.yml`"), ("Test with a non-writer comment", "Test log"), ("Add `--max-turns` and review spend", "Cost note")],
 ("A workflow, a one-repo trust policy and a negative test log.", """
| Control | Evidence |
|---|---|
| Trust condition | `repo:your-org/this-repo:*` |
| Commenter check | Non-writer comment rejected before sign-in |
| Turn cap | `--max-turns 10` |
"""),
 """
| Element | What is wrong |
|---|---|
| Trust `repo:your-org/*` | **Org-wide trust** |
| No commenter check | Credentials-before-check |
""",
 "The workflow passes only if a non-writer comment is rejected before any cloud sign-in and the trust names one repository.",
 [("Anthropic", "Use Claude Code GitHub Actions with cloud providers", "Provider inputs, OIDC, secrets, warning", "Current"),
  ("Anthropic", "Feature availability", "Which backends support GitHub Actions", "Current"),
  ("Anthropic", "Claude Code on Amazon Bedrock", "IAM policy", "Current")],
 "none found between the sources read.",
 "This is the craft of CI on your cloud: **federation instead of keys, trust scoped to one repo, and authorise before you authenticate.** The administrator who understands this does not ask \"does it run?\" — they ask \"who can make it run?\"",
))

if __name__ == "__main__":
    run(SPECS)
