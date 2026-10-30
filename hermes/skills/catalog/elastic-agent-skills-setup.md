---
title: "Elastic Agent Skills - Elasticsearch and Kibana Suite"
description: "elastic/agent-skills: 128.9K combined installs. Official Elastic skills for Elasticsearch, Kibana, Observability, Security and Cloud operations."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/elastic-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skill setup", "elasticsearch", "kibana", "observability", "elastic security"]
---

# Elastic Agent Skills - Setup Guide

**Source:** [elastic/agent-skills](https://www.skills.sh/elastic/agent-skills) via skills.sh - 128.9K combined installs across 54 indexed listings; first seen 2026-10-29 (evening sweep)

**GitHub:** [elastic/agent-skills](https://github.com/elastic/agent-skills) - 603 stars, Apache-2.0 License, branch main, last pushed 2026-10-29; 62 SKILL.md files in the tree as two identical mirrors, `plugins/<group>/skills/<name>/SKILL.md` for the Claude Code and Copilot plugin marketplaces and `skills/<group>/<name>/SKILL.md` for everything else, across five groups (cloud, elasticsearch, kibana, observability, security); package and marketplace version 0.7.0

**Category:** Search, observability, security and cloud platform skills for Elasticsearch, Kibana, Elastic Observability, Elastic Security and Elastic Cloud

**Quality Tier:** 🟡 Beta - first-party Elastic repository, Apache-2.0, 603 stars, 62 skill directories and a commit on 2026-10-29, but marked Technical Preview upstream and carrying Warn verdicts from Socket on one sampled skill and Snyk on two

Elastic Agent Skills is Elastic's own skills library, published first-party at `elastic/agent-skills` and described in its README as built by the people who built Elastic. It covers five product groups in one repository: Elasticsearch (10 skills), Kibana (7), Elastic Observability (6), Elastic Security (6) and Elastic Cloud (2), which is 31 skills in tree, each a folder holding a SKILL.md plus, where needed, a `references/`, `assets/` or `scripts/` directory. The skills follow the agentskills.io open standard, and the README names Cursor, GitHub Copilot, Windsurf, Gemini CLI and Claude Code as targets, with native plugin marketplaces for the last two. Upstream labels the whole library a Technical Preview and asks you to expect changes.

What makes this repository worth a guide rather than a one-line install is the gap between what skills.sh indexes and what `main` contains. The index lists 54 skill names totalling 128,923 installs, but only 31 of those names have a SKILL.md directory in the tree as of 2026-10-29. The other 23 are skills the v0.6.0 CHANGELOG removed, and each of them still shows 2,691 to 3,152 installs, so the most-installed delisted names outrank most of the current library. The plugin metadata has not caught up either: `marketplace.json` still advertises Kibana connectors, Vega, streams, per-language EDOT skills, log search, SLOs and service health, and the Elasticsearch plugin description still lists authn, authz and audit. Install by name from the current tree, not from the index.

## Installation

The README's Getting Started section gives three install paths and calls the `skills` CLI the fastest. That is the skills.sh convention, and it is the same CLI this catalog uses elsewhere:

```bash
npx skills add elastic/agent-skills --list
npx skills add elastic/agent-skills
npx skills add elastic/agent-skills --skill elasticsearch-esql
npx skills add elastic/agent-skills@elasticsearch-esql
npx skills add elastic/agent-skills -a claude-code -a cursor
npx skills add elastic/agent-skills --all
```

The bare form opens an interactive prompt for skills and target agents; `--list` shows available names without installing, `-a` targets specific agents, `-g` installs into your home instead of the project, and `--all` installs everything non-interactively. The CLI copies each skill folder and records source and content hash in a lock file, so `npx skills check` and `npx skills update` keep it current. For Claude Code and Copilot CLI the README prefers the native plugin marketplace:

```bash
claude plugin marketplace add https://github.com/elastic/agent-skills
claude plugin install elastic-elasticsearch@elastic-agent-skills
```

```bash
copilot plugin marketplace add elastic/agent-skills
copilot plugin install elasticsearch@elastic-agent-skills
```

Plugin names are `elastic-cloud`, `elastic-elasticsearch`, `elastic-kibana`, `elastic-observability` and `elastic-security`; Claude Code needs a session restart after install. There is also a bundled bash installer for environments without Node, which copies from the local `skills/` tree:

```bash
git clone https://github.com/elastic/agent-skills.git
cd agent-skills
./scripts/install-skills.sh list
./scripts/install-skills.sh add -a <agent>
```

For a Hermes profile, the skills CLI or a direct fetch of the folder is the predictable route. The skills CLI copies the whole folder; a manual fetch starts with the SKILL.md and should add `references/` whenever the skill cites it, because elasticsearch-esql alone ships ten reference files including the version history it gates on:

```bash
mkdir -p ~/.hermes/profiles/corpusiq/skills/elasticsearch-esql/references
curl -sL -o ~/.hermes/profiles/corpusiq/skills/elasticsearch-esql/SKILL.md \
  https://raw.githubusercontent.com/elastic/agent-skills/main/plugins/elasticsearch/skills/elasticsearch-esql/SKILL.md
curl -sL -o ~/.hermes/profiles/corpusiq/skills/elasticsearch-esql/references/esql-version-history.md \
  https://raw.githubusercontent.com/elastic/agent-skills/main/plugins/elasticsearch/skills/elasticsearch-esql/references/esql-version-history.md
```

One README warning is worth repeating: do not install all 31. Each installed skill adds routing context the agent evaluates on every request, and the README's own tip says to install the Cloud skills and the Elasticsearch auth skills first because most others depend on them. The auth skills were removed at v0.6.0, so on `main` the equivalent starting set is `cloud-onboarding`, `cloud-provisioning` and `elasticsearch-onboarding`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| elasticsearch-esql | 4,901 | Writing and running ESQL through the `elastic` CLI with `stack es` support: discover the schema, pick the ESQL feature for the task, generate the simplest correct query, run it, and turn results into charts or dashboards. Needs Elasticsearch 8.14 or later. |
| elasticsearch-onboarding | 4,432 | Getting a developer from zero intent to a working search experience: understand what they are building, map the data, then build search with current patterns instead of legacy examples. |
| kibana-dashboards | 4,362 | Creating and updating Kibana dashboards and standalone Lens visualizations through the 9.4+ Dashboards and Visualizations APIs, with minimal diffable JSON, inline panels and design guidance from its `references/` files. |
| security-case-management | 4,193 | Creating, searching and updating SOC cases through the Kibana Cases API, linking alerts to cases, adding investigation notes and managing triage output. Ships two Node.js helper scripts. |
| kibana-alerting-rules | 4,089 | Creating and managing Kibana alerting rules: metric threshold rule types and params, lifecycle changes (enable, disable, mute, snooze), and read-only find and list with tag filters. |
| kibana-agent-builder | 4,044 | Creating, updating, deleting, testing and inspecting Kibana Agent Builder agents and custom tools, and answering what agents or tools already exist. |
| observability-llm-obs | 3,962 | Answering LLM and agent questions from data already in Elastic: latency and error rate, token and cost utilization, guardrail events, and how an agent's tool-call chain ran. |
| security-alert-triage | 3,918 | Ranking the Elastic Security alert queue by weighted risk (base score, MITRE tactic boost, entity risk, asset criticality) and clustering alerts into entity groups before investigation. |
| security-detection-rule-management | 3,901 | Creating, tuning and managing SIEM and Endpoint detection rules: false positives, exceptions, new coverage, noisy rules, rule changes through the Kibana API. Ships six helper scripts. |
| security-generate-security-sample-data | 3,847 | Generating sample security events, attack scenarios and synthetic alerts for demos, dashboard population, detection rule testing and proofs of concept. Ships four helper scripts. |
| observability-logs-search | 3,152 | Delisted. The changelog removes `skills/observability/logs-search` at v0.6.0, so there is no SKILL.md on main; log digging now appears inside observability-sre-triage, which funnels logs down to the failures behind a symptom. |
| kibana-anomaly-detection | 3,145 | ML anomaly investigation end to end: what broke and which entity, why a score is high or low, datafeed and memory-limit failures, reading `.ml-anomalies-*` and job state from the ML APIs. |
| observability-k8s-investigation | 3,106 | Kubernetes triage over OTel/EDOT telemetry: CrashLoopBackOff, OOMKilled, node pressure, image pull failures, admission rejections, autoscaling anomalies, correlated with application signals. |
| elasticsearch-authn | 3,045 | Delisted. Removed with the Elasticsearch security group at v0.6.0 and absent from main, even though the plugin description still advertises authentication work. |
| elasticsearch-file-ingest | 2,979 | Delisted. Its bulk file loading intent now sits in elasticsearch-ingest, which converts CSV and JSON to NDJSON, applies explicit mappings and verifies document counts. |
| elasticsearch-authz | 2,942 | Delisted. Removed at v0.6.0 with authn and audit; role and privilege guidance survives only in the plugin keywords, not as an installable skill on main. |
| elasticsearch-audit | 2,939 | Delisted. Removed at v0.6.0; the Elasticsearch plugin description and marketplace entry still list audit, which is why the listing keeps its installs. |
| kibana-streams | 2,931 | Delisted. Removed at v0.6.0 with the rest of the old Kibana group; `marketplace.json` still names streams in the Kibana plugin description. |
| kibana-connectors | 2,914 | Delisted. Removed at v0.6.0; connector work is not in the current tree despite the Kibana plugin metadata still advertising connectors. |
| kibana-vega | 2,912 | Delisted. Removed with the Kibana group at v0.6.0, so Vega chart guidance is gone; kibana-dashboards covers Lens visualizations instead. |
| elasticsearch-security-troubleshooting | 2,909 | Delisted. Removed with authn, authz and audit at v0.6.0; nothing in the current tree replaces it by name. |
| observability-service-health | 2,863 | Delisted. Health questions now route to observability-sre-triage, which reads SLO status and burn rate across APM, OTel and logs. |
| kibana-audit | 2,849 | Delisted. Removed at v0.6.0 with no successor named in the changelog. |
| observability-manage-slos | 2,803 | Delisted. SLO work moved into observability-service-reliability, which picks an SLI and target, creates SLOs through the Kibana API and attaches burn-rate alerts. |
| cloud-network-security | 2,769 | Delisted. Traffic filters, IP restrictions and PrivateLink now sit in cloud-provisioning, whose description covers network security for projects and deployments. |
| cloud-manage-project | 2,751 | Delisted. Day-2 operations moved into cloud-provisioning, which creates, connects to, updates and deletes Serverless projects. |
| cloud-setup | 2,744 | Delisted. Organization setup moved into cloud-onboarding, which configures the `elastic` CLI Cloud context and API key and sets a default region. |
| observability-edot-python-instrument | 2,730 | Delisted. Per-language EDOT skills were removed at v0.6.0; observability-onboarding now routes on language and runtime and applies the OTLP configuration. |
| cloud-create-project | 2,711 | Delisted. Project creation is part of cloud-provisioning rather than a standalone skill. |
| observability-edot-java-instrument | 2,710 | Delisted. Same removal as the other EDOT instrument skills; the routing decision now lives in observability-onboarding. |
| observability-edot-dotnet-instrument | 2,708 | Delisted. No .NET specific skill remains in the tree at 2026-10-29. |
| observability-edot-dotnet-migrate | 2,702 | Delisted. The APM-to-EDOT migration path is described in observability-onboarding, which detects and replaces a classic Elastic APM agent. |
| cloud-access-management | 2,701 | Delisted. Users, roles and Cloud API keys moved into cloud-onboarding. |
| observability-edot-python-migrate | 2,695 | Delisted. Migration guidance is now generic in observability-onboarding rather than per language. |
| observability-edot-java-migrate | 2,691 | Delisted. Removed at v0.6.0 with the rest of the EDOT migration set. |

The remaining 19 indexed listings range from 29 to 1,299 installs.

## Why This Matters for Hermes Agents

The useful thing here is not that Elastic published skills, it is that the instructions are version-aware in a way a model's memory is not. Each SKILL.md carries a `compatibility:` block naming the deployment types it applies to and the CLI surface it assumes: Elasticsearch 8.x or 9.x with `elastic` CLI >= 0.2 and `stack es`, Kibana 9.4 or later with `stack kb`, Cloud work with `cloud serverless` and `cloud hosted`, and an explicit note that cluster and shard APIs do not apply to Serverless. That is the kind of detail an agent gets wrong from memory, and it is the commonest cause of an assistant confidently issuing a call the target deployment does not support.

The trigger model matters for planning. In this format the `description` field is the only signal an agent runtime reads when deciding whether a skill applies, so a vague description is a skill that never loads and a broad one is a skill that loads when it should not. Elastic's descriptions are written as task statements with an explicit "use when", which is why the suite routes cleanly, and also why installing all 31 is a bad idea: every installed skill adds routing context that gets evaluated on each request, and the README says so directly.

The economics are worth stating plainly. Twenty-three of the 54 indexed listings, every one of them above the 2,000 install threshold, describe skills that no longer exist on main. An agent that installs by name from the index will pull a delisted listing or fail, and a human reading install counts will overestimate how much of this suite is live. Read the tree, not the index.

Finally, this is a set of instructions, not a sandbox. Twelve Node.js helper scripts live under `scripts/` in three security skills, everything else is markdown, and the operational risk is that a well-written skill makes the agent more willing to act on a live cluster. Elastic's own README says to scope API keys to minimum privileges, keep read-only access until behaviour is validated, and start on a Serverless trial or isolated Kibana space, which is the right default for any profile that can reach production.

## Usage

| You say | What happens |
|---|---|
| "Query the nginx logs for our ten slowest requests" | elasticsearch-esql maps the schema first, writes ESQL for the aggregation, runs it through the `elastic` CLI and returns the result set or a chart definition built from it. |
| "Which alerts should I work first this morning?" | security-alert-triage ranks the queue by base risk, MITRE tactic boost, entity risk and asset criticality, then clusters the alerts into entity groups to investigate together. |
| "Why is this cluster yellow?" | elasticsearch-cluster-health runs read-only triage, classifies the allocation deciders, names the single most likely cause and gives the remediation, with replica versus primary impact spelled out. |
| "Build a latency dashboard for the checkout service" | kibana-dashboards writes declarative dashboard and Lens JSON against the Kibana 9.4 APIs, keeps panels inline, and follows its own dashboard and chart design references. |
| "Checkout is slow, find out why" | observability-sre-triage reads SLO status and burn rate, checks active rules and ML anomalies, measures latency and error rate, assesses dependency health, then funnels logs down to the failures that explain the symptom. |
| "Turn this runbook into a Kibana workflow" | kibana-workflows authors Workflow YAML from the description, validates the triggers and steps, then runs a quick test loop against a real Kibana. |
| "Open a case for these three alerts" | security-case-management creates the case through the Kibana Cases API, links the alerts, adds notes and records observables such as IOCs. |

## Verification

The sample paths below returned 200 on branch `main` when this guide was written on 2026-10-29:

```bash
for p in \
  plugins/cloud/skills/onboarding/SKILL.md \
  plugins/cloud/skills/provisioning/SKILL.md \
  plugins/elasticsearch/skills/elasticsearch-esql/SKILL.md \
  plugins/elasticsearch/skills/elasticsearch-cluster-health/SKILL.md \
  plugins/elasticsearch/skills/elasticsearch-index-design/SKILL.md \
  plugins/elasticsearch/skills/elasticsearch-ingest/SKILL.md \
  plugins/elasticsearch/skills/elasticsearch-anomaly-detection/SKILL.md \
  plugins/elasticsearch/skills/elasticsearch-anomaly-detection-explainer/SKILL.md ; do
  printf "%s " "$(curl -s -o /dev/null -w '%{http_code}' \
    https://raw.githubusercontent.com/elastic/agent-skills/main/$p)"
  echo "$p"
done
```

Expect eight lines of `200`. The `plugins/` mirror and the `skills/` mirror are byte-identical for all 31 skills, which was checked by diffing every pair in the checkout, so either path fetches the same file. A delisted name is easy to spot the same way: substitute `plugins/elasticsearch/skills/elasticsearch-authn/SKILL.md` and the probe returns 404.

Confirm what the index would install before installing it:

```bash
npx skills add elastic/agent-skills --list
```

After install, read the frontmatter rather than trusting the summary. Every skill in this repository has the same four keys, `name`, `description`, `metadata` (author, version, and a `universal` flag) and `compatibility`:

```bash
sed -n '1,16p' ~/.hermes/profiles/corpusiq/skills/elasticsearch-esql/SKILL.md
```

To review a skill before it goes anywhere near a cluster, read three things: the `description` (it is the trigger, so check it fires on the tasks you want), the `compatibility` block (deployment types and CLI version), and the folder listing, because three security skills ship executable helper scripts:

```bash
curl -sL https://raw.githubusercontent.com/elastic/agent-skills/main/plugins/elasticsearch/skills/elasticsearch-anomaly-detection/SKILL.md | sed -n '1,12p'
```

## Security

skills.sh verdicts for sampled skills (verified 2026-10-29) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| elasticsearch-esql | Pass | Pass | Pass |
| elasticsearch-onboarding | Pass | Warn | Pass |
| kibana-dashboards | Pass | Pass | Pass |
| security-case-management | Pass | Pass | Warn |
| kibana-alerting-rules | Pass | Pass | Pass |
| observability-csp-investigation | Pass | Pass | Warn |

Nothing in the sample fails. Two auditors pass on all six; Socket records one Warn, on elasticsearch-onboarding, and Snyk records two, on security-case-management and observability-csp-investigation. A Warn is a flagged pattern that wants a human read, not a proven exploit, and this pack does not carry the finding text behind those verdicts, so open the three security pages on skills.sh and read them before install. What those warnings are judging is real capability: the ES and Kibana skills drive the `elastic` CLI against a live cluster with whatever privileges the configured API key holds, three security skills ship 12 Node.js helper scripts under `scripts/`, and Elastic's README states directly that these agents process attacker-controlled input, since alert fields and event contents are strings written by an adversary, and that prompt injection is an inherent property of the operating environment rather than a theoretical risk.

## Limitations

- Snapshot data, verified 2026-10-29: 128,923 combined installs across 54 indexed listings; 603 GitHub stars; Apache-2.0; last pushed 2026-10-29. Counts drift over time.
- The listing count and the tree disagree badly. skills.sh indexes 54 names, but the tree has 62 SKILL.md files that resolve to 31 skills in two identical mirrors, and 23 of the indexed names are skills the v0.6.0 CHANGELOG removed. All 23 delisted names sit above the 2,000 install threshold, so most of the table above describes skills you cannot install from `main`.
- Metadata lags the tree. `marketplace.json`, `plugin.json` and the README tip still advertise connectors, Vega, streams, per-language EDOT skills, log search, SLOs, service health, authn, authz and audit, and the README's advice to install the Elasticsearch auth skills first cannot be followed on `main`.
- Upstream calls this a Technical Preview. Per-skill versions in frontmatter do not move with the repository version (0.7.0 in `package.json` and `marketplace.json`), so elasticsearch-esql is 0.10.0 and kibana-dashboards is 0.4.0 at the same commit; pin by commit SHA if exact flag behaviour matters.
- Everything assumes the `elastic` CLI. Stack skills want >= 0.2 with `stack es`, dashboards want >= 0.4 with `stack kb`, Cloud skills want `cloud serverless` and `cloud hosted`, and Kibana dashboards additionally want Kibana 9.4 or later. Without the CLI the skills tell the agent to stop rather than fall back to raw HTTP.
- The files are instructions, not enforcement. Nothing in a SKILL.md stops a mutation against a production cluster, and the only guardrail is the privilege of the API key the CLI is configured with.

## Related

- [Datadog Agent Skills - Observability & Monitoring Setup](/hermes/skills/catalog/datadog-agent-skills-setup)
- [Sentry AI Monitoring - Agent Error Tracking Setup](/hermes/skills/catalog/sentry-ai-monitoring-setup)
- [ClickHouse Agent Skills - Official Analytics Suite Setup](/hermes/skills/catalog/clickhouse-agent-skills-setup)
- [Monitoring Expert - Observability & Monitoring Setup](/hermes/skills/catalog/monitoring-expert-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install five to eight skills, not thirty-one. Routing context is paid on every request, so start with `cloud-onboarding`, `elasticsearch-esql` and whichever single group you actually operate, then add.
- Resolve the name against `main` before you install. Twenty-three counted names have no directory in the tree, and `curl -o /dev/null -w "%{http_code}"` against the raw path is the fastest check that a listing is live.
- Read the `compatibility:` block first. It tells you which `elastic` CLI subcommand tree the skill drives and the stack floor, which is what decides whether a skill can touch your deployment at all.
- Copy folders, not single files. elasticsearch-esql cites `references/esql-version-history.md` for version gating and kibana-dashboards carries its own dashboard and chart design references; a lone SKILL.md loses those.
- Keep mutations behind a read-only key until behaviour is validated, and verify the write with a follow-up read (a count query, a `_cat` call, or the dashboard GET) rather than accepting the agent's own summary.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
