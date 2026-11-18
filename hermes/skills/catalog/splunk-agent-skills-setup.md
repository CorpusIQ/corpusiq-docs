---
title: "Splunk Agent Skills - Splunk Operations Suite Setup"
description: "splunk/splunk-agent-skills: 4.7K combined installs across 32 indexed listings; enterprise-ready AI skills for Splunk search and administration."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/splunk-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "splunk", "observability", "search"]
---

# Splunk Agent Skills - Setup Guide

**Source:** [splunk/splunk-agent-skills](https://www.skills.sh/splunk/splunk-agent-skills) via skills.sh - 4.7K combined installs across 32 indexed listings; first seen Nov 18, 2026 (this sweep)
**GitHub:** 69 stars, Apache-2.0 license, `main` branch, last pushed 2026-09-11. The 32 skills each live under `skills/<name>/SKILL.md`, most with an `agents/openai.yaml` manifest and reference markdown files.
**Category:** Splunk operations / enterprise search and administration
**Quality Tier:** 🟠 Orange - 52 Pass, 7 Warn and 1 Fail across the 60 sampled verdict cells; Apache-2.0 licence.

Splunk Agent Skills is Splunk's open source, enterprise-ready collection of AI skills for Splunk use cases. The 32 skills cover search, dashboard conversion, field extraction and CIM mapping, search performance, and a long tail of read-only administration and readiness advisors. Most skills are advisory and evidence-bounded: they read supplied evidence about a deployment and cite public Splunk documentation rather than mutating the environment.

## Installation

List the skills before installing, then copy all 32 for the selected agent from a project root:

```bash
npx skills add splunk/splunk-agent-skills --list
npx skills add splunk/splunk-agent-skills --skill '*' --agent claude-code --copy --yes
npx skills add splunk/splunk-agent-skills --skill '*' --agent codex --copy --yes
```

Project scope is the default; add `--global` to install into the agent's user-level skills directory instead. To copy a single skill, name it with `--skill`, for example:

```bash
npx skills add splunk/splunk-agent-skills --skill splunk-search --agent codex --copy --yes
```

For a manual install, clone or download the repository and copy the desired directory from `skills/` into the skills directory configured for the agent. The `skills` CLI installs skill directories, not external executables: `splunk-cloud-admin-copilot` needs the separately installed `acs` CLI, and the `splunk-search` live SPL path needs [splunkctl](https://github.com/splunk/splunkctl). SPL authoring and explanation remain available without it.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| splunk-search | 226 | Runs bounded, read-only Splunk SPL searches through splunkctl and returns compact, evidence-backed results without exposing credentials. |
| custom-visualization-builder | 193 | Scaffolds, builds and installs a custom visualization into Splunk using the dashboard-studio-extension framework. |
| splunk-dashboard-converter | 181 | Converts classic Splunk Simple XML dashboards into Dashboard Studio, preserving every SPL query verbatim. |
| search-performance-optimizer | 181 | Diagnoses and improves one slow Splunk search from SPL and runtime evidence with query tuning and acceleration-fit analysis. |
| field-extraction-and-cim-mapping | 181 | Authors, explains, diagnoses, and validates search-time field extractions and mappings to Splunk Common Information Model datasets. |

The remaining 27 indexed listings range from 117 to 164 installs.

## Why This Matters for Hermes Agents

The suite's design is advisory and evidence-bounded: each skill reads supplied evidence about a deployment, cites public Splunk documentation, and hands ownership of writes and live changes to a specific owning workflow. For a Hermes agent this matters because a Splunk environment is production infrastructure; the skills let an agent produce bounded findings, upgrade plans, and diagnosis handoffs without mutating the deployment. The one scoped exception is `splunk-cloud-admin-copilot`, which can add or remove a single IPv4 CIDR on an IP allowlist only after explicit approval.

## Usage

| You say | What happens |
|---|---|
| "Run a search for failed logins in the last hour" | splunk-search runs a bounded, read-only SPL search through splunkctl and returns compact results. |
| "Convert my classic Simple XML dashboard to Dashboard Studio" | splunk-dashboard-converter parses the XML, preserves every SPL query verbatim, and returns the Studio JSON. |
| "Build a custom visualization for this app" | custom-visualization-builder scaffolds, builds and installs a custom viz with the dashboard-studio-extension framework. |
| "Why is this saved search so slow?" | search-performance-optimizer reads the SPL and runtime evidence and returns query tuning and acceleration-fit analysis. |
| "Map these sample events to the CIM" | field-extraction-and-cim-mapping authors and validates search-time extractions and CIM mappings from the events. |

## Verification

List the available skills, then confirm the repository is reachable:

```bash
npx skills add splunk/splunk-agent-skills --list
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/splunk/splunk-agent-skills/main/skills/splunk-search/SKILL.md
```

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| splunk-search | Pass | Pass | Warn |
| custom-visualization-builder | Pass | Pass | Pass |
| splunk-dashboard-converter | Pass | Pass | Fail |
| search-performance-optimizer | Pass | Pass | Pass |
| field-extraction-and-cim-mapping | Pass | Pass | Pass |
| splunk-product-question-navigator | Pass | Pass | Warn |
| hec-setup-and-troubleshooting | Pass | Pass | Pass |
| splunk-cloud-admin-copilot | Pass | Pass | Pass |
| splunk-identity-saml-readiness-advisor | Pass | Pass | Warn |
| knowledge-object-governance | Pass | Pass | Pass |
| splunk-health-monitoring-and-diagnostic-collection | Pass | Pass | Pass |
| deployment-server-and-forwarder-fleet-management | Pass | Pass | Pass |
| app-and-add-on-lifecycle-advisor | Pass | Pass | Warn |
| upgrade-planning-and-execution-readiness | Pass | Pass | Warn |
| vulnerability-remediation-and-compliance-readiness | Pass | Pass | Warn |
| search-and-dashboard-troubleshooter | Pass | Pass | Warn |
| data-model-and-search-acceleration | Pass | Pass | Pass |
| alerting-and-notable-workflows | Pass | Pass | Pass |
| dashboard-report-alert-performance-advisor | Pass | Pass | Pass |
| incident-diagnosis-specialist | Pass | Pass | Pass |

The sample covers 20 of the 32 indexed listings. The single Fail is a Snyk flag on splunk-dashboard-converter, and the seven Warn cells are all Snyk flags.

## Limitations

- Snapshot data, verified Nov 18, 2026: 4,650 combined installs across 32 indexed listings; 69 GitHub stars; Apache-2.0 license; last pushed 2026-09-11. Counts drift over time.
- These skills are experimental and are not covered by existing Splunk support contracts; review SUPPORT.md before relying on them.
- Meaningful use requires a Splunk instance or Splunk Cloud tenant: the skills read and reason about a deployment, and the splunk-search live execution path needs splunkctl pointed at a reachable Splunk environment.
- The skills CLI installs skill directories, not external executables. splunk-cloud-admin-copilot needs the separately installed acs CLI, and splunk-search live SPL execution needs splunkctl.
- The five skills shown above carry most of the install volume; the other 27 indexed listings range from 117 to 164 installs and are long-tail.

## Related

- [Trailofbits Security Setup](/hermes/skills/catalog/trailofbits-security-setup)
- [Security Hardening - AI Agent Security Setup](/hermes/skills/catalog/security-and-hardening-setup)
- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `npx skills add splunk/splunk-agent-skills --list` first; it prints the 32 skill IDs without copying anything.
- Treat the skills as read-only by default; they route writes and live changes to the owning workflow, and only splunk-cloud-admin-copilot performs a scoped write.
- Install splunkctl before relying on splunk-search for live SPL; SPL authoring and explanation work without it.
- For a single workflow, install just that skill with `--skill`, for example splunk-search or field-extraction-and-cim-mapping, instead of all 32.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
