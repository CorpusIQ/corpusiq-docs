---
title: "Elastic Integration Skills - Agent Workflows Setup"
description: "elastic/integration-skills: agent workflows for building, reviewing and maintaining Elastic integrations - 7.3K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/elastic-integration-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "elasticsearch", "kibana", "observability"]
---

# Elastic Integration Skills - Agent Workflows Setup

**Source:** [elastic/integration-skills](https://www.skills.sh/elastic/integration-skills) via skills.sh - 7.3K combined installs across 15 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 morning sweep)
**GitHub:** [elastic/integration-skills](https://github.com/elastic/integration-skills) - 18 stars, Apache-2.0 license, main branch, last pushed Nov 23, 2026; one SKILL.md per skill under skills/<name>/SKILL.md with reference files alongside each skill.
**Category:** Elasticsearch and Kibana Integration Development
**Quality Tier:** 🟠 Orange - 2 Fail cells and 9 Warn cells across the 15-skill sample: Gen Agent Trust Hub Fails on research-integration and Snyk Fails on dashboard-review; Snyk Warns on anonymize-logs, create-integration, dashboard-guidelines, review-integration, package-spec, maintain-integration and entity-mappings, plus a Socket Warn on research-integration and a Gen Agent Trust Hub Warn on dashboard-review.

Elastic's Integration Skills is a public collection of agentic workflows that cover the full lifecycle of building, reviewing and maintaining Elastic integration packages. The skills are LLM-agnostic by design: they work with Cursor, Claude Code, Codex, or any environment that can read skill files from a directory, and the README flags the collection as a Beta release under active development.

The suite is organized around two top-level skills. /research-integration investigates a vendor or product before work starts and writes a structured research document, and /create-integration scaffolds a new integration package end-to-end. A set of domain skills then covers CEL programs, ingest pipelines, ECS field mappings, package spec compliance, testing, and dashboard authoring and review. The README states that the toolkit needs Docker plus the elastic-package, celfmt, stream, mito, ceplx and kbdash Go tools on PATH.

## Installation

Install the full collection through the skills CLI, which launches an interactive prompt to select skills and target agents:

```bash
npx skills add elastic/integration-skills
```

Claude Code users can register the plugin marketplace instead, which keeps the local copy current through auto-updates:

```bash
/plugin marketplace add elastic/integration-skills
/plugin install integration-skills@elastic-integration-skills
```

A local clone path is also documented for environments without Node.js: clone the repository and copy the skills/ folder into the agent config directory. Seven external tools must be present on PATH for the workflows to run - Docker, elastic-package, celfmt, stream, mito, ceplx and kbdash - each installable with go install.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ingest-pipelines | 527 | designing and modifying Elasticsearch ingest pipelines with parsing, branching and on_failure handling |
| integration-testing | 525 | creating and debugging elastic-package tests: pipeline fixtures, system tests and script tests |
| research-integration | 522 | researching a vendor or product before building, outputting a structured research document |
| dashboard-review | 522 | reviewing dashboard JSON changes with kbdash and checking guideline compliance |
| anonymize-logs | 520 | sanitizing customer log files and fixtures line-by-line without reformatting |
| ecs-field-mappings | 519 | defining ECS field mappings and choosing categorization values for data streams |
| create-integration | 519 | scaffolding a new integration package end-to-end across package layout, CEL, pipelines and tests |
| dashboard-guidelines | 518 | creating and reviewing Kibana dashboard assets against Kibana 9.4+ design guidelines |
| elastic-package-cli | 516 | running elastic-package build, check, lint, format, test and stack commands |
| review-integration | 516 | standalone quality review that classifies files by domain and applies checklists and severity rules |
| package-spec | 516 | package specification compliance for package metadata, changelog schema and lint/check errors |
| cel-programs | 514 | writing CEL programs and templates for API data collection with mito mock-first development |
| maintain-integration | 512 | reviewing and fixing an existing integration package |
| input-configurations | 512 | input templates for non-CEL input types and Federated Identity for agentless AWS |
| entity-mappings | 90 | adding and auditing ECS entity.* fields and running entity-coverage gap analysis |

All 15 indexed listings sit at 50 installs or above and appear in the table above.

## Why This Matters for Hermes Agents

A coding agent left to its own memory will write Elastic integrations that fail elastic-package lint and check, misname ECS fields, or mishandle ingest-pipeline errors, and it will not know the package spec rules the Elastic ecosystem enforces. Integration Skills closes that gap with skills whose content encodes the actual repository conventions. The highest-value pair is research-integration and create-integration: the first produces a structured research document and the second consumes it to scaffold a package, so an agent stops guessing and starts from a validated layout. The domain skills then carry the load per area - cel-programs for API data collection logic, ingest-pipelines for processor chains and on_failure handling, ecs-field-mappings and entity-mappings for correct field schemas, and package-spec for metadata and changelog compliance. review-integration is the quality step that classifies files by domain and applies the right checklists and severity rubric before a change ships. For operators, the suite is a single path from vendor research to a reviewed, tested integration package, and it works in whatever coding environment is already in use.

## Usage

| You say | What happens |
|---|---|
| Research a Check Point Harmony Endpoint integration | Runs research-integration to investigate the API, data formats and field schemas, writing a research document |
| Scaffold a new integration package | Runs create-integration with package topology and scaffold commands |
| Add a CEL data stream to an existing package | Routes to cel-programs for CEL program and template authoring |
| My package fails elastic-package lint | Uses package-spec to resolve package metadata and changelog compliance errors |
| Review this integration PR | Runs review-integration to classify files by domain and apply checklists and severity rules |
| Sanitize these customer logs before testing | Runs anonymize-logs to replace sensitive values inline without reformatting |

## Verification

Confirm the top-level lifecycle skill resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/elastic/integration-skills/main/skills/create-integration/SKILL.md | head -40
```

Spot-check the research and CEL skills to confirm the flat skills/ layout:

```bash
curl -sL https://raw.githubusercontent.com/elastic/integration-skills/main/skills/research-integration/SKILL.md | head -30
```

```bash
curl -sL https://raw.githubusercontent.com/elastic/integration-skills/main/skills/cel-programs/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ingest-pipelines | Pass | Pass | Pass |
| integration-testing | Pass | Pass | Pass |
| research-integration | Fail | Warn | Pass |
| dashboard-review | Warn | Pass | Fail |
| anonymize-logs | Pass | Pass | Warn |
| ecs-field-mappings | Pass | Pass | Pass |
| create-integration | Pass | Pass | Warn |
| dashboard-guidelines | Pass | Pass | Warn |
| elastic-package-cli | Pass | Pass | Pass |
| review-integration | Pass | Pass | Warn |
| package-spec | Pass | Pass | Warn |
| cel-programs | Pass | Pass | Pass |
| maintain-integration | Pass | Pass | Warn |
| input-configurations | Pass | Pass | Pass |
| entity-mappings | Pass | Pass | Warn |

The sample carries two Fail cells - Gen Agent Trust Hub on research-integration and Snyk on dashboard-review - and nine Warn cells, all from Snyk except a Socket Warn on research-integration and a Gen Agent Trust Hub Warn on dashboard-review; all 15 indexed listings carry a published verdict.

## Limitations

- Snapshot data, verified Nov 23, 2026: 7,348 combined installs across 15 indexed listings; 18 GitHub stars; Apache-2.0 license; last pushed Nov 23, 2026. Counts drift over time.
- The README marks the collection as a Beta release, so skill names, commands and reference layouts may still change.
- Seven external tools must be present on PATH for the workflows to run: Docker, elastic-package, celfmt, stream, mito, ceplx and kbdash, each installable with go install.
- Several elastic-package commands, including system tests and workspace-aware workflows, need an integrations-style workspace to run correctly.
- Fourteen of the fifteen listings sit in a narrow 512 to 527 install band, with entity-mappings far below at 90, so install counts do not rank the skills' relative importance.

## Related

- [Elastic Agent Skills - Elasticsearch and Kibana Suite](/hermes/skills/catalog/elastic-agent-skills-setup)
- [Grafana Skills - Observability & Monitoring Platform](/hermes/skills/catalog/grafana-skills-setup)
- [Datadog Agent Skills Setup Guide](/hermes/skills/catalog/datadog-agent-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run /research-integration first and feed its output into /create-integration; the build skills are tuned to consume that structured research document format.
- Install with npx skills add elastic/integration-skills and answer the interactive prompt to pick skills and target agents, or use --all for a non-interactive full install.
- Treat the Snyk Fail on dashboard-review and the Gen Agent Trust Hub Fail on research-integration as reasons to read those skill bodies before relying on them.
- If you develop against elastic/integrations, run these skills from a checkout of that repository so the agent sees the real package layout and conventions.
- Use npx skills update periodically; the Claude Code plugin path auto-updates in the background.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
