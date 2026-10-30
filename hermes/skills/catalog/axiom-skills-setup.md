---
title: "Axiom Skills - Observability and Event Queries Setup"
description: "axiomhq/skills: 23.9K combined installs. Official Axiom agent skills for APL log and event queries, dashboards, alerts and cost control."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/axiom-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "observability", "logs", "metrics", "apl", "mcp"]
---

# Axiom Skills - Setup Guide

**Source:** [axiomhq/skills](https://www.skills.sh/axiomhq/skills) via skills.sh - 23.9K combined installs across 15 indexed listings; first seen 2026-10-30 (morning sweep)

**GitHub:** [axiomhq/skills](https://github.com/axiomhq/skills) - 17 stars, MIT License, branch main, last pushed 2026-10-29; 8 `SKILL.md` files, one per skill directory at `skills/<name>/SKILL.md` for axiom-alerting, axiom-build-dashboard, axiom-control-costs, axiom-create-org, axiom-ingest, axiom-metrics-chart and axiom-spl-to-apl plus `sre` (folder name `sre`, frontmatter name `axiom-sre`), beside `.mcp.json`, client manifests for Codex, Claude Code, Cursor and Grok Build plus `gemini-extension.json`, `eval-tooling/`, `scripts/` and `version.txt`

**Category:** Log and event observability, query languages and incident diagnosis

**Quality Tier:** 🟡 Beta - 5 sampled Warn verdicts (four Socket, one Snyk) across the sampled five; MIT, hosted MCP endpoint, live API writes against dashboards and monitors

Axiom is an observability platform for logs, metrics and traces, and this repository is its official agent plugin. The plugin bundles eight skills with a hosted Model Context Protocol endpoint at `https://mcp.axiom.co/mcp`, declared in `.mcp.json` and shipped to Codex, Claude Code, Cursor, Gemini CLI and Grok Build through a manifest per client. The coverage is deliberately operational: hypothesis-driven incident investigation, Splunk SPL to APL translation, dashboard construction, monitor and notifier management through the v2 public API, query-pattern cost analysis, metric chart rendering, data ingest and throwaway org provisioning. The install index names 15 listings against 8 skill directories, most of the surplus being older un-prefixed names for the same skills, which the changelog records as a rename that prefixed the remaining skills with `axiom-`.

The README states the design constraint that matters most: the skills depend on each other, naming `axiom-control-costs` as depending on `axiom-sre` for queries and `axiom-build-dashboard` for deployment, so the installer's advice to install all of them is a correctness statement rather than a completeness one. Credentials are split by design. SRE reads `~/.config/axiom-sre/config.toml` with `[axiom.deployments.<name>]` sections, while dashboard, alerting and metrics scripts read a separate `~/.axiom.toml`, and the README says plainly that MCP OAuth does not configure those script credentials. Script dependencies are `jq`, `curl`, `bc` for cost analysis, and `timeout` or `gtimeout` for the SRE scripts.

## Installation

The repository's own installer is the shortest route, and the README recommends installing everything because of those cross-skill dependencies:

```bash
npx skills add axiomhq/skills
```

The plugin route is documented per client. Codex registers the marketplace first, then installs the plugin, where the first name is the plugin and the second is the marketplace:

```bash
codex plugin marketplace add axiomhq/skills
codex plugin add axiom@axiom
```

Claude Code uses the same marketplace, then a restart and `/mcp` authorization, and Gemini CLI installs the repository as an extension:

```bash
claude plugin marketplace add axiomhq/skills
claude plugin install axiom@axiom
```

```bash
gemini extensions install https://github.com/axiomhq/skills
```

Cursor imports the repository as a local plugin, which requires an admin to enable local plugin imports on Teams or Enterprise:

```bash
git clone https://github.com/axiomhq/skills.git ~/.cursor/plugins/local/axiom
```

Hermes is not one of the five client manifests this repository ships, so the durable route for this profile is a directory copy. Copy each `skills/<name>/` from a checkout into `~/.hermes/profiles/corpusiq/skills/<name>/`, and copy the whole directory rather than the markdown alone, because the helpers are the part that does the work: `axiom-build-dashboard` ships `scripts/`, `reference/` and `tests/`, `axiom-control-costs` ships `scripts/` and `templates/`, `axiom-spl-to-apl` ships `reference/` and `tests/`, `axiom-alerting` ships `scripts/`, `axiom-metrics-chart` ships `scripts/` and `examples/`, and `sre` ships `scripts/`, `reference/` and `templates/`. Note the name difference on the SRE skill: the folder is `skills/sre` and its frontmatter name is `axiom-sre`, so name the copy after whichever identifier your routing rules key on.

SRE needs one initialization step before first use, run from the installed skill directory or from a checkout:

```bash
./skills/sre/scripts/init
```

That writes configuration and investigation memory under `~/.config/axiom-sre/`. Edit the generated `config.toml` to add your deployments, then run the initializer again.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| axiom-sre | 5,195 | Hypothesis-driven incident investigation and root cause triage: a systematic triage loop, Axiom log and metric queries when a deployment is configured, and investigation memory kept locally under `~/.config/axiom-sre/`. |
| building-dashboards | 4,543 | Designing and building Axiom dashboards through the API: chart types, APL and metrics/MPL query patterns, SmartFilters, layout, chart configuration and Splunk migration. The current tree ships this skill as axiom-build-dashboard, with `mpl-validate-chart` and `layout-pack` helpers. |
| query-metrics | 3,787 | Metrics queries against Axiom MetricsDB through bundled scripts, including discovery of available metrics, tags and tag values before a query runs. No directory of this name exists in the current skills tree. |
| controlling-costs | 2,752 | Analyzing query patterns to find unused data, unqueried columns and ingest waste, then building the dashboards and monitors that track cost. The README names it as depending on axiom-sre and axiom-build-dashboard. |
| spl-to-apl | 2,636 | Translating Splunk SPL queries to Axiom APL: command mappings, function equivalents and syntax transformations for a migration. |
| axiom-alerting | 2,523 | Creating and managing Axiom monitors and notifiers through the v2 public API: routing notifications, validating monitor behavior and maintaining alert configuration end to end. |
| writing-evals | 2,194 | Scaffolding evaluation suites for the Axiom AI SDK: eval files, scorers, flag schemas and config generated from a plain-language description. No directory of this name exists in the current skills tree. |

The remaining 8 indexed listings range from 1 to 199 installs.

## Why This Matters for Hermes Agents

Observability is the domain where an agent is most tempted to improvise: the request arrives as a symptom, and answering it needs a query language, a dataset name and a result shape that a model cannot guess correctly. These skills carry that vocabulary, APL for logs and MPL for metrics, so a Hermes job emits a query the API accepts rather than one the model wished existed.

`axiom-sre` changes behaviour rather than only supplying knowledge. It encodes a hypothesis-driven investigation loop with systematic triage and keeps investigation memory locally, which is exactly the state a cron or subagent run lacks when it wakes up without conversational history.

The read-then-write split is clean enough to test. Queries, chart rendering and SPL translation run against a token; dashboards, monitors and notifiers are writes against a live organization, and the dashboard skill ships validation helpers that check a chart payload before it is created, which gives a review step before anything lands in production.

The two credential files also bound the blast radius. `~/.axiom.toml` holds `url`, `token` and `org_id` per deployment, and the README asks for an advanced API token with minimal privileges, so a profile can be pointed at a staging deployment or a read-scoped token while the write skills stay installed but unused.

Cost control shows why the collection is packaged as a set. `axiom-control-costs` queries through `axiom-sre` and deploys through the dashboard scripts, so the answer to "what are we paying for that nobody reads" comes from three skills cooperating rather than one skill reasoning alone.

Finally, `axiom-metrics-chart` renders saved metrics v2 or v3 JSON as charts in a terminal or transcript with no dependencies, and only reaches for gnuplot when PNG, SVG or sixel output is asked for, which means a scheduled job can put a chart into its own report without an image pipeline.

## Usage

| You say | What happens |
|---|---|
| "Checkout started returning 500s an hour ago, find the cause" | The SRE skill runs its triage loop: states a hypothesis, queries the error logs and related metrics through APL, narrows the timeline, and records the investigation so a later session can pick it up. |
| "Why is our ingest bill climbing while traffic is flat?" | Cost-control analysis looks for unused columns, field values and datasets nobody queries, then builds the dashboards and monitors that keep watching the waste. |
| "Convert this Splunk search into something Axiom can run" | SPL to APL translation maps each command and function to its APL equivalent, then checks the transformed query against the mappings it carries. |
| "Build an on-call dashboard for the payments service" | The dashboard skill picks chart types, writes the APL or MPL queries behind each chart, lays the panels out, and validates the payload before creating anything. |
| "Page me in Slack when the error rate crosses two percent" | The alerting skill creates the monitor and the notifier through the v2 API, then reads the configuration back to confirm the threshold, the window and the routing. |
| "Plot this saved metrics query as a chart" | The metrics chart skill renders the saved v2 or v3 JSON as an ASCII chart in the transcript, or as PNG, SVG or sixel when gnuplot output is requested. |
| "Load this CSV of events into a new dataset" | The ingest skill resolves an org from `~/.axiom.toml`, or provisions a temporary one when nothing is configured, creates the dataset, ingests the file and confirms with a query. |

## Verification

The raw paths below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} sre\n" \
  https://raw.githubusercontent.com/axiomhq/skills/main/skills/sre/SKILL.md
curl -sL -o /dev/null -w "%{http_code} alerting\n" \
  https://raw.githubusercontent.com/axiomhq/skills/main/skills/axiom-alerting/SKILL.md
curl -sL -o /dev/null -w "%{http_code} dashboards\n" \
  https://raw.githubusercontent.com/axiomhq/skills/main/skills/axiom-build-dashboard/SKILL.md
```

Expect `200` three times. Read the frontmatter before installing, because the description is the whole routing contract: a useful Axiom skill description names the trigger phrases, the API surface it will call and the neighbouring skill it should hand off to.

After a copy lands in the profile, confirm the frontmatter and the shape of the directory:

```bash
head -4 ~/.hermes/profiles/corpusiq/skills/axiom-sre/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/axiom-build-dashboard/
ls ~/.hermes/profiles/corpusiq/skills/axiom-sre/scripts/
```

A good copy shows only `name:` and `description:` in the frontmatter, and the directory listing shows `scripts/`, `reference/` and `templates/` for the SRE skill and `scripts/`, `reference/` and `tests/` for the dashboard skill. If `scripts/` is empty, the copy took the markdown and left the tooling behind, which is the failure mode that matters here.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| axiom-sre | Pass | Warn | Pass |
| building-dashboards | Pass | Warn | Pass |
| query-metrics | Pass | Warn | Warn |
| controlling-costs | Pass | Warn | Pass |
| axiom-agent-created-orgs | n/a | Pass | Pass |

The sampled five carry 5 Warn verdicts and no Fail: Socket warns on four of them and Snyk warns on `query-metrics`. The pack records the verdict rather than the finding behind it, so read those entries on skills.sh before installing. A Warn on this repository most plausibly tracks what the skills are built to do: they instruct an agent to run bundled `jq`, `curl` and shell scripts against a live API, and half of them write to dashboards, monitors and notifiers in a production organization.

The write surface is the part to review, not the markdown. Alerting and dashboard skills create and update real resources, and the README notes that the skills use your configured credentials to query Axiom and optional Grafana, Pyroscope, Sentry, Slack and Kubernetes connections. Authentication has two independent paths: the hosted MCP server uses OAuth through the client at `https://mcp.axiom.co/mcp`, while the scripts read bearer tokens from `~/.axiom.toml` and `~/.config/axiom-sre/config.toml`. The README's own guidance is to mint an advanced API token with minimal privileges, and since MCP OAuth does not configure the script credentials, the token you place in those files sets what the scripted half can reach.

## Limitations

- Snapshot data, verified 2026-10-30: 23,872 combined installs across 15 indexed listings; 17 GitHub stars; MIT License; last pushed 2026-10-29. Counts drift over time.
- The index outruns the tree. skills.sh indexes 15 listings while the checkout holds 8 skill directories, and the surplus is mostly older un-prefixed names for the same skills: `building-dashboards`, `controlling-costs`, `spl-to-apl` and `metrics-chart` are the pre-rename listings of `axiom-build-dashboard`, `axiom-control-costs`, `axiom-spl-to-apl` and `axiom-metrics-chart`, which the changelog records as a change that prefixed the remaining skills with `axiom-`.
- Two indexed listings have no counterpart in the current tree at all. `query-metrics` and `writing-evals` carry install counts in the index but no directory of that name exists in `skills/` on branch main or on the v1.1.2 and v1.2.0 tags, so their descriptions here come from their skills.sh pages rather than from a `SKILL.md` you can read in the checkout.
- Install counts split by name rather than by capability. The same dashboard skill appears as `building-dashboards` at 4,543 and `axiom-build-dashboard` at 1, and four prefixed listings sit between 1 and 16 installs, so table position reflects listing history and rename drift rather than adoption.
- Half the collection is inert without a live Axiom organization. Queries, dashboards, monitors, ingest and cost analysis need a deployment in `~/.axiom.toml` with `url`, `token` and `org_id`, or an authorized MCP connection for the hosted path, and MCP OAuth does not configure the script credentials. Without that, the skills can explain a query but not run it.
- The SRE skill is not usable on a fresh copy until `scripts/init` has run and `~/.config/axiom-sre/config.toml` names at least one deployment, and the README lists `jq`, `curl`, `bc`, and `timeout` or `gtimeout` as prerequisites that the skill will not install for you. Writes to dashboards, monitors and notifiers are direct API calls with no documented undo.

## Related

- [Coralogix cx CLI - Observability Agent Skills Setup](/hermes/skills/catalog/coralogix-cx-cli-setup)
- [Vectorize Hindsight Skills - Agent Memory Setup](/hermes/skills/catalog/vectorize-hindsight-skills-setup)
- [OpenAI Agents Python Skills - Multi-Agent Setup](/hermes/skills/catalog/openai-agents-python-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install all eight skills, not the two you think you need. The README names `axiom-control-costs` as depending on `axiom-sre` and `axiom-build-dashboard`, so a partial install produces a cost workflow that cannot run its queries or deploy its dashboards.
- Copy directories, never lone `SKILL.md` files. The validation helpers in `axiom-build-dashboard/scripts/` and the reference trees in `axiom-spl-to-apl/reference/` are the parts that make the instructions executable.
- Run `skills/sre/scripts/init` before the first SRE session, then edit the generated `config.toml` and run it again. A missing deployment entry looks like a skill failure rather than a configuration gap.
- Keep the two credential files straight: `~/.config/axiom-sre/config.toml` for investigation, `~/.axiom.toml` for dashboard, alerting and metrics scripts. An MCP authorization does not populate either one.
- If Axiom MCP was already added to the client by hand, remove one connection after installing the plugin. The README warns that two connections surface duplicate tools, which makes routing noisier without adding capability.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
