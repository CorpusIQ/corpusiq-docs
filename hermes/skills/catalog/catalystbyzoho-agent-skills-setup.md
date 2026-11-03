---
title: "Catalyst by Zoho Skills - Serverless Suite"
description: "catalystbyzoho/agent-skills: 18.0K combined installs. Nineteen Zoho Catalyst skills for serverless functions, data store, auth and deploys."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/catalystbyzoho-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "zoho catalyst", "serverless", "cloud deployment"]
---

# Catalyst by Zoho Skills - Setup Guide

**Source:** [catalystbyzoho/agent-skills](https://www.skills.sh/catalystbyzoho/agent-skills) via skills.sh - 18.0K combined installs across 19 indexed listings; first seen 2026-10-31 (evening sweep)

**GitHub:** [catalystbyzoho/agent-skills](https://github.com/catalystbyzoho/agent-skills) - 70 stars, Apache-2.0, branch main, last pushed 2026-10-28; 19 `SKILL.md` directories under `skills/`, each with its own `references/` folder of one to six files, plus a root `CATALYST.md` routing stub, 37 eval scenarios under `evals/` and one version-check script

**Category:** Zoho Catalyst serverless development for agents: functions, data store, auth and deployment

**Quality Tier:** 🟡 Yellow - the 36-install tail listing catalyst-datastreams carries Socket and Snyk Warns, which holds the pack at Yellow even though every high-install sampled skill is a Pass

Zoho publishes this as the first-party skill set for Catalyst, its full-stack serverless cloud, and the README is blunt about the reason it exists: give a coding agent verified Catalyst knowledge so it writes code that deploys rather than code that merely compiles. Nineteen skills cover the platform, from project scaffolding and all seven function types through Data Store and ZCQL, AppSail containers, Stratus object storage, Signals events, Data Streams WebSockets and the QuickML and Zia AI services.

The structure is the interesting part. `AGENTS.md` documents a three-tier loading model: a routing `SKILL.md` at `skills/catalyst-by-zoho` sends a query to a service skill, and each service skill is a thin entry point (frontmatter, workflow, triggers, a references table) that points at `references/` files loaded only when needed. The repo's own rule is that detailed technical content never goes inline in a `SKILL.md`, because it loads on every match and bloats the context window. For a 19-skill pack, that is the difference between a useful suite and one that crowds out everything else in the profile.

## Installation

The README's first route is the skills CLI, which installs the whole set:

```bash
npx skills add catalystbyzoho/agent-skills
```

Claude Code users get a plugin marketplace instead, with the plugin published as `catalyst-by-zoho` from the same repository:

```
/plugin marketplace add catalystbyzoho/agent-skills
/plugin install catalyst-by-zoho@catalyst-by-zoho
```

Gemini CLI installs it as an extension, Cursor takes a symlink or the shipped `.cursor-plugin` manifest, Copilot appends the routing skill to `.github/copilot-instructions.md` with the frontmatter stripped, and Windsurf copies `skills/` into `.windsurfrules/`. Each of those routes is documented in the README with its own steps. None of them knows about Hermes, so the durable install is a directory copy that keeps every `references/` folder beside its `SKILL.md`:

```bash
git clone --depth 1 https://github.com/catalystbyzoho/agent-skills.git /tmp/catalyst-skills
cp -r /tmp/catalyst-skills/skills/. ~/.hermes/profiles/corpusiq/skills/
```

The optional half of the setup is Zoho MCP. Several skills, notably `catalyst-datastore` and `catalyst-functions`, tell the agent to check for `CatalystbyZoho_*` tools before running an operation, so an MCP connection is what turns them from documentation into an operator. Create a server at `mcp.zoho.com`, add the Catalyst by Zoho tools, set authorization to On Demand, then put the server URL in the placeholder inside `.mcp.json` (or in the profile's MCP configuration, which keeps the token out of the repo).

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| catalyst-by-zoho | 1,103 | The routing entry point for the whole suite: answering any Catalyst question by dispatching to the service skill that covers it, and handling services that only have reference files. |
| catalyst-basics | 1,096 | Starting a project: directory structure, environments, CLI commands, and where each Catalyst ID lives (Project ID, ZAID, Table ID, Segment ID, Org ID). |
| catalyst-appsail | 1,086 | AppSail, the persistent backend PaaS: managed Node.js, Java and Python runtimes, custom Docker containers, listen-port handling and long-running processes. The skill routes stateless handlers back to `catalyst-functions`. |
| catalyst-functions | 1,084 | All seven function types, handler signatures, `catalyst-config.json`, Security Rules, API Gateway routing, multipart uploads, CORS and timeout debugging; it asks for the Zoho MCP connection before operating. |
| catalyst-sdk | 1,082 | SDK initialisation and service access for Node.js, Web, Python, Java, Android, iOS and Flutter. |
| catalyst-datastore | 1,082 | Relational Data Store and ZCQL: table creation, CRUD, permissions, pagination, and the result-wrapping and boolean-as-string behaviour that causes silent bugs. |
| catalyst-zoho-mcp | 1,077 | Running Catalyst infrastructure from the conversation with the `CatalystbyZoho_*` MCP tools: tables, buckets, cache, plus the MCP server setup and config steps. |
| catalyst-authentication | 1,077 | Login and signup, ZAID, Web SDK flows, Connections OAuth, social and third-party identity providers, custom tokens and JWT sign-in. |
| catalyst-slate | 1,068 | Slate frontend hosting: Git-based deploys, previews and `slate-config.toml` for React, Next.js, Vue, Angular, Svelte, Astro and other frameworks. |
| catalyst-cache | 1,062 | In-memory key-value cache segments with TTLs for session state and temporary data. |
| catalyst-stratus | 1,058 | Object storage with uploads, downloads, signed URLs and multipart upload, including migration off S3 or GCS; the skill states Stratus is not S3-API compatible. |
| catalyst-nosql | 1,055 | NoSQL key-value tables with typed items and mandatory partition keys, for flexible schemas without joins. |
| catalyst-zia | 1,051 | Pre-trained Zia APIs: OCR, face analytics, text analytics, object detection, barcode reading and content moderation, with the data centre restrictions spelled out. |
| catalyst-pricing | 1,050 | Free tier limits, pay-as-you-go rates, GB-seconds arithmetic and cost estimation. |
| catalyst-signals | 1,002 | Event bus setup: publishers, webhooks, functions and circuits as targets, filters, transformation, batch dispatch and retry policy. The skill notes Signals is console-only with no SDK. |
| catalyst-smartbrowz | 1,001 | Browser automation and document generation: headless Chrome and Firefox, Browser Logic functions, PDF and screenshot generation, templates, Browser Grid and Dataverse scraping. |
| catalyst-job-scheduling | 583 | Job pools, immediate and background jobs, and crons (Periodic, OneTime, Calendar, CronExpression) that run Job functions, webhooks, circuits or AppSail. |
| catalyst-quickml | 334 | QuickML prediction pipelines, AutoML, LLM Serving, RAG and the Zia Model Library, with per-service data centre availability. |
| catalyst-datastreams | 36 | Real-time publish and subscribe over WebSocket: `publishData`, token pairs, Node, browser, Java and Python subscribers, acknowledgements and 48-hour retention. |

No indexed listings fall below the threshold; all 19 appear above. Every listing has a matching directory in the tree, so there is no index-versus-tree gap here.

## Why This Matters for Hermes Agents

The value of this suite is that Catalyst has enough sharp edges that generic code generation produces plausible code which fails on deploy. The skills name the traps directly: `catalyst-authentication` warns that ZAID differs between Development and Production and calls that the top cause of auth failures after environment promotion, and `catalyst-datastore` warns that ZCQL result wrapping and boolean-as-string storage cause silent bugs when skipped. An agent cannot infer either fact from a public API description, so having them written down changes the output.

The loading model is the second win. Because service skills keep their detail in `references/` and the routing skill above them stays thin, a profile can carry all 19 skills without paying the context cost up front. That is the same discipline the CorpusIQ profile applies to its own skill library, which makes the pack easy to reason about: one routing document, 18 thin workflows, and reference material that loads only on a match.

The eval harness is the part most packs skip. `evals/` holds 37 scenarios, each a `prompt.md` with a turn limit, an allowed-tools list and graders, and the prompts read like a developer asking whether a shortcut is actually safe rather than a feature request. That makes the suite testable after install, which is the difference between a skill pack and a prompt library.

## Usage

| You say | What happens |
|---|---|
| "Start a Catalyst project for a support app" | `catalyst-basics` sets up the structure, environment and CLI commands, then hands off to the service skills the app needs. |
| "Write a function that accepts file uploads behind the API Gateway" | `catalyst-functions` supplies the handler signature, `catalyst-config.json`, Security Rules and the multipart upload path. |
| "This scheduled job never fires" | `catalyst-job-scheduling` checks the job pool, cron expression and the registration step, with `catalyst-basics` confirming which environment the job was deployed to. |
| "Create the table and load sample rows" | `catalyst-zoho-mcp` runs the `CatalystbyZoho_*` tools against the project while `catalyst-datastore` supplies the ZCQL and data type rules. |
| "Why does login break in production but work in development" | `catalyst-authentication` explains the ZAID difference between environments and walks the Connections and token flow. |
| "Will this architecture stay inside the free tier" | `catalyst-pricing` prices the functions, storage and calls involved, and `catalyst-quickml` covers model hosting costs where AI services are in scope. |
| "Which Catalyst service replaces S3 plus Lambda" | `catalyst-by-zoho` maps the services and cites the migration references for the pair. |

## Verification

The raw path for the routing skill returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} catalyst-by-zoho\n" \
  https://raw.githubusercontent.com/catalystbyzoho/agent-skills/main/skills/catalyst-by-zoho/SKILL.md
```

Expect `200`. After the copy lands, confirm the count and that the reference folders came along, since most of the technical content lives there:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/catalyst-*/ | wc -l
head -4 ~/.hermes/profiles/corpusiq/skills/catalyst-by-zoho/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/catalyst-functions/references
```

The count should print 19, the header should show `name: catalyst-by-zoho` followed by a quoted `description:`, and the reference listing should show four files: `api-gateway.md`, `functions-advanced.md`, `functions-basics.md` and `functions-templates.md`.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| catalyst-by-zoho | Pass | Pass | Pass |
| catalyst-sdk | Pass | Pass | Pass |
| catalyst-cache | Pass | Pass | Pass |
| catalyst-signals | Pass | Pass | Pass |
| catalyst-datastreams | Pass | Warn | Warn |

The surface is small: 140 markdown files, five JSON manifests (the Claude plugin and its marketplace index, the Cursor plugin, the Gemini extension and `.mcp.json`), and a single shell script, `scripts/check-versions.sh`, which reads git history to verify skill version bumps. There is no package to install, no build step and no postinstall hook, so the reviewable code is the prompts, the references and that one script.

The credential question is the one worth settling before deployment. `catalyst-by-zoho` talks to Zoho over MCP, and `gemini-extension.json` ships a `<YOUR_ZOHO_MCP_URL>` placeholder rather than a URL, which is the right shape: the MCP server URL carries an auth token in its path, so it belongs in the profile's MCP configuration or an environment variable, never in a prompt, a skill file or a committed `.mcp.json`. The README's own setup step says to copy the authenticated URL from the Zoho console, which is exactly the string that must not be pasted into a conversation log.

The two Warns on `catalyst-datastreams` are the exception worth reading. That skill is the smallest listing at 36 installs and the only one flagged, and its content is WebSocket publish and subscribe material pointing at `@zcatalyst/datastreams` and `zcatalyst_sdk.datastreams`. Treat the warn as a prompt to read the file rather than a blocker, and keep the socket clients off any credential that is not scoped to development.

## Limitations

- Snapshot data, verified 2026-10-31: 17,987 combined installs across 19 indexed listings; 70 GitHub stars; Apache-2.0; last pushed 2026-10-28. Counts drift over time.
- The suite is single-platform by design. Every skill assumes Catalyst, so it earns its context budget only in a profile that deploys to Zoho's cloud.
- Nine topics are covered only through reference files and have no dedicated skill: Circuits, Pipelines, ConvoKraft, Logs, APM, Alerts, GitHub integration, the VS Code extension and the REST APIs. The README says so explicitly, so an agent will find guidance but not a step-by-step workflow for those.
- `catalyst-datastore` and `catalyst-functions` both instruct the agent to confirm the `CatalystbyZoho_*` MCP tools before operating, which means the MCP connection is a hard dependency for the infrastructure half of the suite rather than an optional extra.
- Install counts are flat: the top 16 listings sit between 1,001 and 1,103, and the three below them (583, 334 and 36) are the narrow services, so a low count here reflects a specialist topic rather than a weak skill.
- The routing skill tells agents to fetch individual pages from `docs.catalyst.zoho.com` for edge cases instead of bundling a documentation dump, so answers on unusual topics depend on network access and on the docs site staying reachable.

## Related

- [CloudBase Skills - Tencent Full-Stack Apps Setup](/hermes/skills/catalog/cloudbase-skills-setup)
- [Tigris Data Skills - Object Storage for Agents](/hermes/skills/catalog/tigrisdata-skills-setup)
- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install all 19, not the routing skill alone. `catalyst-by-zoho` routes to service skills that do the actual work, and a profile with only the router answers questions it cannot back up.
- Wire the Zoho MCP connection before the first deployment question. Half the suite is instructions for calling `CatalystbyZoho_*` tools, and without the connection the agent will describe table creation instead of performing it.
- Keep the MCP server URL in the profile configuration, not in `.mcp.json`. The URL embeds an auth token, and a committed copy of that file is a leaked credential.
- When a deploy fails, read the relevant `references/` file before retrying. `catalyst-functions` splits gateway, basics, advanced and template material across four files, and the fix is usually in the one the agent did not open.
- If your platform is not Zoho, read the migration references in `catalyst-by-zoho` before installing the rest. That is where the service mapping lives, and it decides whether the other 18 skills are useful to you.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
