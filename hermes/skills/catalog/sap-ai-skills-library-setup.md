---
title: "SAP AI Skills Library - Enterprise Agent Skills Setup"
description: "sap/ai-skills-library: 3.8K combined installs across 16 listings; AI skills for SAP, searchable and installable for your digital assistant."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sap-ai-skills-library-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "sap", "ai core", "enterprise"]
---

# SAP AI Skills Library - Setup Guide

**Source:** [sap/ai-skills-library](https://www.skills.sh/sap/ai-skills-library) via skills.sh - 3.8K combined installs across 16 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 morning sweep)
**GitHub:** 152 stars, Apache-2.0 licence, `main` branch, last pushed 2026-11-11. Skills live under `plugins/<plugin>/skills/<name>/SKILL.md` and `skills/<name>/SKILL.md`, with `scripts/`, `references/`, `knowledge/`, and `evals/` folders; a REUSE.toml tracks licensing.
**Category:** SAP AI Core, SAP Fiori, and Clean Core methodology
**Quality Tier:** 🟡 Yellow - Warns only among 16 sampled skills (aicore-admin-resources Socket, genai-hub-orchestration and genai-hub-prompt-evaluation Snyk); Apache-2.0 licence.

The SAP AI Skills Library is the official SAP collection for discovering, filtering, and installing AI skills that operate SAP AI Core, SAP Fiori design, and the Clean Core methodology. The README describes it as a library for a digital assistant, and points contributors to a bring-your-own-repo model: skill code stays in the contributor's own public repository and is onboarded through a registration issue, with new skills listed on skills.cloud.sap.

The 16 indexed listings split into three clusters: six AI Core skills (foundation models, lifecycle management, admin resources, orchestration, prompt evaluation, and tabular orchestration), seven Clean Core skills (general, extensibility, integration, data, processes, operations, and the ATC assessment dashboard), and three SDK and design skills (aicore-sdk-java, aicore-sdk-js, sap-fiori-guidelines). The tree also holds a `skills/sap-fiori-ios/` directory with its own SKILL.md that skills.sh does not list among the 16 indexed listings.

## Installation

Install all skills:

```bash
npx skills add SAP/ai-skills-library
```

Install a specific skill:

```bash
npx skills add SAP/ai-skills-library --skill <skill-name>
```

List available skills:

```bash
npx skills add SAP/ai-skills-library --list
```

Install a plugin:

```bash
npx skills add SAP/ai-skills-library --plugin aicore-skills
```

The skills CLI supports Claude Code, Codex, Cursor, OpenCode, and other agents.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| sap-fiori-guidelines | 1,484 | Design, build, or review SAP Fiori and SAPUI5 apps against SAP design guidelines. |
| genai-hub-foundation-models | 245 | List and explore foundation models in SAP AI Core GenAI Hub and get executable IDs for deployments. |
| genai-hub-tabular-orchestration | 244 | Manage the Context Registry (data destinations, tabular artifacts, scenario configs) and run tabular prediction. |
| aicore-admin-resources | 243 | Verify and configure AI Core credentials, retrieve tokens, and manage resource groups. |
| aicore-lifecycle-management | 239 | Manage AI Core scenarios, executables, configurations, and deployments. |
| aicore-sdk-js | 178 | Generate TypeScript/JavaScript boilerplate for SAP GenAI Hub with @sap-ai-sdk. |
| genai-hub-orchestration | 178 | Configure the AI Core Orchestration service: prompt templates, content filtering, and RAG grounding. |
| genai-hub-prompt-evaluation | 175 | Benchmark LLMs and prompts against a test dataset with system and custom metrics. |
| aicore-sdk-java | 168 | Generate Java boilerplate for SAP GenAI Hub with the SAP AI SDK for Java. |
| clean-core-integration | 94 | Answer questions on Clean Core integration levels, patterns, and SAP integration technologies. |
| clean-core-extensibility | 94 | Answer questions on Clean Core extensibility, ABAP Cloud, and ATC setup. |
| clean-core-general | 93 | Answer broad Clean Core questions and the RISE with SAP Methodology dashboard. |
| clean-core-extensibility-atc-assessment | 93 | Generate a Clean Core ATC assessment dashboard from an SAP ATC findings ZIP export. |
| clean-core-data | 92 | Answer questions on Clean Core data pillars, master data management, and data KPIs. |
| clean-core-processes | 91 | Answer questions on Clean Core business processes, fit-to-standard, and process KPIs. |
| clean-core-operations | 91 | Answer questions on Clean Core operations, cCOE, and operations KPIs. |

No indexed listings fall below the threshold; all 16 appear above.

## Why This Matters for Hermes Agents

For an agent operating in the SAP estate, these skills turn "talk to AI Core" and "answer a Clean Core question" into concrete, source-backed procedures. The AI Core skills each carry a DO NOT USE FOR clause that routes you to the sibling skill for the adjacent task, which is exactly the routing discipline a multi-skill agent needs: foundation-model listing is separate from lifecycle management, and orchestration is separate from direct SDK inference.

The Clean Core skills are knowledge-heavy rather than command-heavy: each bundles whitepapers, slide decks, SAP notes, and KPI references under `knowledge/`, so an agent answering a RISE with SAP question can cite the deck and note rather than improvise. The ATC assessment skill is the one concrete artifact generator, producing a self-contained HTML dashboard from an ATC findings ZIP.

The licensing is the cleanest part of the set: Apache-2.0 with a REUSE.toml, so the skills and their references are safe to read and reuse under a standard permissive licence.

## Usage

| You say | What happens |
|---|---|
| "Which foundation models can I deploy on AI Core?" | genai-hub-foundation-models lists providers, capabilities, and executable IDs. |
| "Create a deployment for this model" | aicore-lifecycle-management manages configurations and deployments. |
| "Set up AI Core credentials" | aicore-admin-resources verifies credentials, fetches tokens, and manages resource groups. |
| "Give me Java code that calls a GenAI Hub model" | aicore-sdk-java produces boilerplate for the SAP AI SDK for Java. |
| "What is Clean Core and how do I measure it?" | clean-core-general explains the five principles and the RISE dashboard. |
| "Build a dashboard from this ATC findings export" | clean-core-extensibility-atc-assessment generates the HTML report. |

## Verification

Probe one skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/SAP/ai-skills-library/main/skills/sap-fiori-guidelines/SKILL.md
```

Then list the available skills and install the one you need:

```bash
npx skills add SAP/ai-skills-library --list
npx skills add SAP/ai-skills-library --skill sap-fiori-guidelines
```

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| sap-fiori-guidelines | Pass | Pass | Pass |
| genai-hub-foundation-models | Pass | Pass | Pass |
| genai-hub-tabular-orchestration | Pass | Pass | Pass |
| aicore-admin-resources | Pass | Warn | Pass |
| aicore-lifecycle-management | Pass | Pass | Pass |
| aicore-sdk-js | Pass | Pass | Pass |
| genai-hub-orchestration | Pass | Pass | Warn |
| genai-hub-prompt-evaluation | Pass | Pass | Warn |
| aicore-sdk-java | Pass | Pass | Pass |
| clean-core-integration | Pass | Pass | Pass |
| clean-core-extensibility | Pass | Pass | Pass |
| clean-core-general | Pass | Pass | Pass |
| clean-core-extensibility-atc-assessment | not parsed | not parsed | not parsed |
| clean-core-data | Pass | Pass | Pass |
| clean-core-processes | Pass | Pass | Pass |
| clean-core-operations | Pass | Pass | Pass |

The sample covers all 16 indexed listings; clean-core-extensibility-atc-assessment was not parsed by any of the three scanners, so skills.sh publishes no verdict for that skill.

## Limitations

- Snapshot data, verified Nov 19, 2026: 3,802 combined installs across 16 indexed listings; 152 GitHub stars; Apache-2.0 licence; last pushed 2026-11-11. Counts drift over time.
- The tree holds a `skills/sap-fiori-ios/` directory with its own SKILL.md that is not among the 16 indexed listings, so the index undercounts the tree by one.
- skills.sh publishes no security verdict for clean-core-extensibility-atc-assessment; all three scanner cells read `not parsed`, so review that skill's source yourself before relying on it.
- The AI Core skills are procedure wrappers over the SAP AI Core APIs, so they need valid credentials and an AI Core tenant to do anything beyond answering questions.
- Most skills ship Python scripts that call SAP endpoints; review the scripts and the SETUP references before running them against a production tenant.

## Related

- [SAP Skills - BTP, CAP and ABAP Agent Suite](/hermes/skills/catalog/sap-skills-setup)
- [Salesforce Skills Library (sf-skills) - 330+ Agent Skills Setup](/hermes/skills/catalog/salesforce-sf-skills-setup)
- [Oracle Skills - Database, OCI and APEX Guidance](/hermes/skills/catalog/oracle-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the two plugin bundles (`aicore-skills` and `clean-core-skills`) when you want a whole cluster; use `--skill` for a single one.
- Keep aicore-admin-resources as the first install; most other AI Core skills assume credentials are already configured.
- Read the DO NOT USE FOR clauses in each AI Core SKILL.md before routing a request; they prevent the wrong skill from grabbing the task.
- For Clean Core questions, start with clean-core-general and let it hand off to the principle-specific skill for depth.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
