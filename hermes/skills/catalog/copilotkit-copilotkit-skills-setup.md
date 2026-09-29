---
title: "CopilotKit Skills - Agent Frontend Stack Setup"
description: "Install CopilotKit agent frontend skills for React, Angular, Mobile, and Slack generative UI; ~34,500 indexed installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/copilotkit-copilotkit-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "agent skill", "skill setup", "generative ui", "ag-ui"]
---

# CopilotKit Skills - Setup Guide

**Source:** [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) (37,596⭐)
**Skill family:** `copilotkit/copilotkit` (6 installable skills)
**Combined Installs:** ~34,500 across indexed listings (Sep 29, 2026 snapshot)
**Category:** Developer Tools
**Quality Tier:** 🟡 Unverified (no skills.sh Trust Hub / Socket / Snyk verdicts published - verified Sep 29, 2026)

CopilotKit — the company behind the AG-UI Protocol — describes this project as the frontend stack for agents and generative UI, spanning React, Angular, Mobile, Slack, and more. The skill family published alongside the SDK covers debugging (`copilotkit-debug`), development (`copilotkit-develop`), the AG-UI protocol (`copilotkit-agui`), React core, and runtime guidance. The main-branch README (MIT license) invites coding agents to onboard via the CopilotKit CLI and install these skills to build features and debug issues.

---

## Installation

```bash
npx skills add copilotkit/copilotkit
```

## Roster - Top Skills

| Skill | Installs | What It Does |
|---|---|---|
| copilotkit-debug | 2,814 | Debugging CopilotKit agent frontends |
| copilotkit-develop | 2,807 | Building features with CopilotKit |
| copilotkit-agui | 2,801 | AG-UI protocol integration |
| react-core | 2,788 | React core generative UI guidance |
| runtime | 2,771 | CopilotKit runtime wiring |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Building an agent chat UI in React | Load react-core and copilotkit-develop to scaffold CopilotKit components and runtime wiring |
| Debugging agent-UI connectivity | Use copilotkit-debug to trace issues between the agent and the frontend |
| Cross-framework agent surfaces | Apply copilotkit-agui when wiring non-CopilotKit agents to a CopilotKit frontend via AG-UI |

## Limitations / Verification

- skills.sh indexed the family on Sep 29, 2026; the snapshot lists 5 skills with published install counts and 0/6 with published verification entries.
- No live install test has been run from Hermes yet.
- The main-branch README was fetched to confirm the skill layout; star and install counts come from the marketplace snapshot.

## Security

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Skills Marketplace](/docs/hermes/skills/marketplace)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
