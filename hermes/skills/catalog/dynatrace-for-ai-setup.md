---
title: "Dynatrace for AI - Observability Skills Setup"
description: "Dynatrace official skills: 60.6K combined installs. 34 skills for DQL, logs, traces, Kubernetes and AWS/Azure observability via MCP or dtctl."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/dynatrace-for-ai-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skill setup", "observability", "apm"]
---

# Dynatrace for AI - Setup Guide

**Source:** [Dynatrace/dynatrace-for-ai](https://www.skills.sh/dynatrace/dynatrace-for-ai) via skills.sh - 60.6K combined installs across 39 indexed listings
**GitHub:** [Dynatrace/dynatrace-for-ai](https://github.com/Dynatrace/dynatrace-for-ai) (167 stars; Apache-2.0; pushed 2026-10-23; layout `skills/<dt-name>/SKILL.md` for 34 skills with 346 reference files under them, plus `prompts/`, `llms.txt`, `.mcp.json`, `server.json` and Claude and Cursor plugin manifests)
**Category:** Observability / APM, Security and Platform Telemetry
**Quality Tier:** 🟢 Production - official Dynatrace org publishing from an internal pipeline, Apache-2.0, 34 skills on the progressive-disclosure pattern with 346 reference files, structural tests in-repo, six reusable prompts, plugin manifests and a registry-published remote MCP server, and Pass on all three scanners for three of four sampled skills

Dynatrace publishes this repository as the official knowledge layer for its platform: observability, security and platform skills written to the Agent Skills format, aimed at coding agents that already have access to a Dynatrace tenant. The description on GitHub states the purpose plainly, skills, prompts and instructions for building AI agents on top of Dynatrace production context.

The design is deliberately split. The skills are knowledge only, covering DQL syntax, the semantic dictionary, per-domain query recipes and analysis workflows. Live data comes from a tool you pair them with: the `dtctl` CLI from the separate `dynatrace-oss/dtctl` repository, or the Dynatrace MCP server, which Dynatrace hosts remotely and publishes to the official MCP registry as `io.github.Dynatrace/dynatrace-for-ai`. That means installing this repo alone changes what the agent knows, not what it can reach.

Coverage runs from query language and platform objects through the observability domains (services, traces, logs, hosts, Kubernetes, AWS, Azure, GCP, frontends, network, GenAI), into security (vulnerabilities, runtime protection, IoC hunting, semantic mapping, DORA compliance), mobile and web instrumentation setup, cost analysis and a Smartscape migration path.

## Installation

```bash
npx skills add dynatrace/dynatrace-for-ai
```

```bash
# Claude Code plugin, which bundles the MCP server configuration
claude plugin install dynatrace@claude-plugins-official

# Environment the bundled MCP server needs
export DT_ENVIRONMENT=https://<env>.apps.dynatrace.com
export DT_PLATFORM_TOKEN=<your-platform-token>
claude mcp login plugin:dynatrace:dynatrace
```

```bash
# Or pair the skills with the dtctl CLI
brew install dynatrace-oss/tap/dtctl
dtctl auth login --context my-env --environment "https://<env>.apps.dynatrace.com"
npx skills add dynatrace-oss/dtctl
dtctl doctor
```

The Cursor plugin is marketplace-only: open Customize in the sidebar, find Dynatrace, and install with the same two environment variables set.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| dt-dql-essentials | 2,831 | DQL syntax, pitfalls and cost-aware optimization: fetch commands, field namespaces, time alignment, summarize and makeTimeseries patterns, filter-early tuning, plus an index to the full function reference |
| dt-app-dashboards | 2,767 | Dashboard JSON: tiles, layouts, variables and DQL query tiles, with a mandatory read-current-state-then-modify workflow so UI edits are not overwritten |
| dt-obs-logs | 2,669 | Log search, filtering, pattern analysis, error rates and log-to-trace correlation, including JSON log parsing and per-process-group views |
| dt-obs-problems | 2,668 | Davis problem analysis: root cause, blast radius, affected users, problem history, trending and which entity actually caused an outage |
| dt-app-notebooks | 2,659 | Notebook JSON: ordered sections of markdown and DQL blocks with visualizations, created or updated through the same read-then-modify workflow |
| dt-obs-tracing | 2,631 | Distributed traces and spans: slow requests, failed spans, service dependencies, database and messaging spans, gRPC calls and Lambda cold starts |
| dt-obs-services | 2,626 | Service RED metrics and runtime telemetry for Java, .NET, Node.js, Python, PHP and Go, including GC, heap, CLR and event loop signals |
| dt-obs-kubernetes | 2,598 | Kubernetes clusters, pods, nodes and workloads: OOMKills, restarts, evictions, scheduling, over-provisioning, labels and cluster event history |
| dt-obs-hosts | 2,587 | Host and process metrics: CPU, memory, disk, network, containers, listening ports, process consumption, and OneAgent mode and version |
| dt-obs-frontends | 2,528 | Real User Monitoring on web and mobile: Core Web Vitals, user sessions, page performance, mobile crashes, frontend errors and frontend-to-backend linking |
| dt-obs-aws | 2,500 | AWS inventory and health: EC2, RDS, Lambda, ECS and EKS, VPC, load balancers, security groups, unattached volumes and cost optimization |
| dt-migration | 2,417 | Migrating classic and Gen2 entity-based DQL to Smartscape: dimension filters first, smartscapeNodes for entity lists, plus entityName and classicEntitySelector rewrites |
| dt-obs-predictive-analytics | 2,123 | Forecasting and capacity planning: timeseries-forecast, saturation planning, trend and seasonality detection, and anomaly analysis on hosts and services |
| dt-obs-azure | 2,027 | Azure resources: VMs, VMSS, SQL Database, Storage, AKS, App Service, Functions, VNet, Event Hubs and Key Vault, plus subscription and resource-group hierarchy |

The remaining 25 indexed listings range from 158 to 1,959 installs. They are the rest of the domain coverage rather than older copies: dt-obs-gcp (1,959), dt-alerting (1,828), dt-js-runtime (1,721), dt-platform-costs (1,396), dt-obs-log-semantic-mapping (1,386), the security set starting at dt-sec-insights (1,381) down through dt-sec-ioc-hunting (1,045), the network skills dt-obs-network-flows (912) and dt-obs-network-devices (907), dt-obs-compliance-assistant (889), the five instrumentation setup skills from dt-setup-react-native (860) to dt-setup-oneagent (490), and five mobile observability listings from dt-obs-react-native (431) down to dt-obs-ios (158) that have no directory in the current tree.

## Why This Matters for Hermes Agents

An on-call question is a retrieval problem disguised as a conversation. "Why is checkout slow since Tuesday" needs a problem entity, a service RED metric, a trace sample, the relevant log lines and usually a deployment marker. A model without Dynatrace knowledge writes plausible DQL that fails on a field name, or asks for a table that does not exist. This suite front-loads that: `dt-dql-essentials` carries the syntax pitfalls and the semantic dictionary index, and the domain skills carry the exact `fetch` targets for each data type, so a Hermes session spends its turns on analysis instead of on schema archaeology.

The second gain is cost discipline. DQL bills on scanned data, and the optimization reference is written around that: filter early, bucket filters, narrower time ranges, field selection, sampling and cardinality limits. An agent that internalizes those rules produces cheaper queries by default, which matters when the same session fires dozens of them during an incident.

The third is that the boundaries between domains are written down as routing instructions. Each skill's description carries a trigger list and an explicit "do not use for" clause that points at the sibling skill instead: logs defer to tracing for spans, tracing defers to services for RED metrics, hosts defer to Kubernetes for pod-level questions. That is the difference between an agent that runs one good query and one that runs four overlapping ones and reconciles them badly.

Finally the write paths are constrained by the instructions rather than left to judgement. Dashboards and notebooks both mandate reading the current object first and modifying that file, warning that reconstructing JSON from scratch silently overwrites whatever a human changed in the UI. For an agent operating on production tooling, an explicit "never inject an id" rule is worth more than a permission scope.

## Usage

| You say | What happens |
|---|---|
| "Checkout got slow after the 14:00 deploy, find out why" | Starts from Davis problems, then pulls service RED metrics and a trace sample, and correlates log lines inside the same window |
| "Write a DQL query for error rate by service over the last 24 hours" | Loads `dt-dql-essentials` for `makeTimeseries` and field syntax before writing, so the query parses on the first run |
| "Which pods were OOMKilled overnight?" | Queries Kubernetes events and container metrics for OOMKills and restarts, and names the affected workloads and namespaces |
| "Build me a dashboard of our AWS cost drivers" | Creates dashboard JSON with tiles and variables, reading any existing dashboard before modifying it |
| "Is this query expensive?" | Rewrites the query against the optimization reference: earlier filters, tighter buckets, fewer fields, and reports the savings logic |
| "Migrate these entity-based queries to Smartscape" | `dt-migration` rewrites `fetch dt.entity.*` to `smartscapeNodes` and converts entity subqueries to dimension filters |
| "Hunt these IOCs across the last week of logs" | `dt-sec-ioc-hunting` searches logs and spans for the indicators and produces a threat-exposure score |

## Verification

Confirm what the installer added:

```bash
npx skills list | grep -i dynatrace
dtctl doctor
```

Read the skills before installing. All five URLs below returned HTTP 200 when checked with curl on Oct 26, 2026:

```bash
curl -sL https://raw.githubusercontent.com/Dynatrace/dynatrace-for-ai/main/README.md
curl -sL https://raw.githubusercontent.com/Dynatrace/dynatrace-for-ai/main/skills/dt-dql-essentials/SKILL.md
curl -sL https://raw.githubusercontent.com/Dynatrace/dynatrace-for-ai/main/skills/dt-obs-aws/SKILL.md
curl -sL https://raw.githubusercontent.com/Dynatrace/dynatrace-for-ai/main/skills/dt-app-dashboards/SKILL.md
curl -sL https://raw.githubusercontent.com/Dynatrace/dynatrace-for-ai/main/mcp.json
```

The last of those URLs is the MCP wiring, declared as a remote HTTP server, so there is nothing to install locally.

## Security

skills.sh verdicts for sampled skills (verified Oct 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| dt-dql-essentials | Pass | Pass | Pass |
| dt-app-dashboards | Pass | Pass | Pass |
| dt-obs-aws | Pass | Pass | Pass |
| dt-obs-logs | Pass | Pass | Warn |

The one Warn is inherent to the domain rather than to a defect. Snyk scores `dt-obs-logs` MEDIUM under W011, third-party content exposure, because the skill queries log messages that external users and applications generate, which is an indirect prompt injection surface: log text reaches the model and can contain instructions. Anything that reads production logs has that property, and the mitigation is on the harness side, so treat log content as data and never as instructions.

The credential model is a tenant token and an environment URL. The bundled MCP configuration points at the tenant's `platform-reserved/mcp-gateway/v0.1/servers/dynatrace-mcp/mcp` path, sends the platform token as a Bearer credential in the Authorization header with a `Dt-External-Source` header, and the registry manifest marks that token as secret and required. The token itself is a Dynatrace platform token whose scopes are documented in the Dynatrace MCP server docs, and the README points at the privacy policy for data handling. With `dtctl` instead, `dtctl auth login --context <name> --environment <url>` authenticates one environment per named context.

Write actions are real and they live in the tool layer, not in the markdown. `dt-app-dashboards` and `dt-app-notebooks` create and update platform documents through `dtctl`, `dt-obs-ext-monitors` posts third-party test results to `/platform/ingest/custom/events/{endpoint}` using a token scoped `openpipeline.events.custom` or `openpipeline:events.custom:ingest`, and `dt-alerting` sets up anomaly detectors, problem grouping and workflow notification routing. Scoped tokens are the only real boundary here, so issue read-only tokens to sessions that only investigate.

Two smaller behaviours are worth knowing. A handful of helper scripts ship inside the skills, including `skills/dt-setup-ios/scripts/verify-setup.sh`, `skills/dt-setup-ios/scripts/add_spm_dependency.rb` and two JavaScript extractors under `skills/dt-obs-analytics/scripts/`; read them before letting an agent execute them. And the repository's structural tests (`tests/test-structure.sh`, `tests/test-skill-quality.sh`) are worth running after any manual edit.

## Limitations

- The skills carry no data path on their own. Without `dtctl` or the Dynatrace MCP server, a Hermes session can write perfect DQL and get nothing back, so install one of the two before evaluating skill quality.
- The install index outruns the tree. There are 39 indexed listings and 34 `SKILL.md` directories, and the five missing ones are all mobile observability: dt-obs-react-native, dt-obs-android, dt-obs-flutter, dt-obs-ios-sdk and dt-obs-ios. They still carry install counts from the index but have no directory in the current checkout.
- `dt-obs-frontends` states that it does not cover synthetic monitoring at all, so HTTP, browser and network synthetic checks need a different source.
- Skill content is maintained internally and published periodically. The README says pull requests that modify `skills/` will not be accepted, so fixes have to go through an issue and wait for a release.
- The clone inspected here has a HEAD commit dated 2026-10-01 while GitHub reports the last push as 2026-10-23, so file-level details in this guide may lag the newest commit.
- `dtctl` is a separate repository with its own skill (`npx skills add dynatrace-oss/dtctl`) and is not bundled here. The Claude Code plugin bundles only the MCP server configuration.
- Snapshot data, verified Oct 26, 2026: 60,579 combined installs across 39 indexed listings; 167 GitHub stars; Apache-2.0; last pushed 2026-10-23. Counts drift over time.

## Related

- [Datadog Agent Skills - Observability & Monitoring Setup](/hermes/skills/catalog/datadog-agent-skills-setup) - the same observability-agent pattern for a competing platform, useful for comparing query languages.
- [Langfuse Agent Skills - LLM Observability Setup](/hermes/skills/catalog/langfuse-agent-skills-setup) - observability aimed at model calls rather than infrastructure, which pairs with the GenAI coverage here.
- [Hermes Labyrinth - Observability Dashboard Plugin for Hermes Agent](/hermes/skills/catalog/hermes-labyrinth-observability-setup) - instrumentation for the agent itself, the other half of an on-call setup.
- [OpenClaw Control Center - Agent Monitoring Dashboard for OpenClaw](/hermes/skills/catalog/openclaw-control-center-setup) - monitoring the automation layer that runs the queries.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Load `dt-dql-essentials` before any query, not after it fails. The syntax pitfalls table alone prevents the most common parse errors in `filter`, `by:` and static array literals.
- Give investigation sessions a read-only platform token. Every write capability in this suite comes from the token you issue, so scope is your real blast radius control.
- Ask for the query before the answer. Having the agent show the DQL it intends to run catches a wrong data model in one line instead of after a five minute scan.
- Use the six prompts in `prompts/` as templates. Daily standup, health check, incident response and performance regression already encode the problem, logs, traces sequence the domain skills expect.
- Watch query cost in shared tenants. The optimization reference exists because scanned bytes are billed, and a session that ignores `fieldsKeep` and sampling gets expensive fast on wide log fetches.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
