---
title: "n8n Skills — Workflow Automation for Business"
description: "n8n automation skills — czlonkowski/n8n-skills (15 skills, 48.4K installs) plus the official n8n-io/skills (14 skills). Workflow patterns, node configuration, MCP tool integration, JavaScript/Python code nodes, subworkflows, self-hosting, error handling for agents building n8n automations."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/n8n-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-14"
tags: ["hermes skill", "agent skill", "skill setup", "n8n", "workflow automation", "business operations"]
---

# n8n Skills — Setup Guide

**Source:** [czlonkowski/n8n-skills](https://skills.sh/czlonkowski/n8n-skills) · [n8n-io/skills](https://skills.sh/n8n-io/skills) (official)
**GitHub:** [czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · [n8n-io/skills](https://github.com/n8n-io/skills)
**Skills:** 29 skills across both repos (~58K combined installs)
**Category:** Business Automation / Operations
**First Seen:** August 14, 2026 afternoon sweep
**Quality Tier:** 🟢 Production (community suite 48.4K installs + official vendor skills)

n8n is the open-source workflow automation platform business operators use to connect their stack without code. These skills make an agent fluent in building, debugging, and hardening n8n workflows — including MCP tool integration, which bridges directly into the Hermes MCP ecosystem. Two complementary repos: the community suite (15 skills, 48.4K) is broader and workflow-focused; the official repo (14 skills) encodes n8n's own best practices.

---

## Installation

```bash
# Community suite (recommended starting point)
npx skills add czlonkowski/n8n-skills

# Official n8n skills
npx skills add n8n-io/skills
```

No API key required for the skills themselves. Building real workflows needs an n8n instance — cloud (n8n.io), self-hosted (`n8n-self-hosting` skill covers it), or local via Docker/npx.

## What It Provides

### czlonkowski/n8n-skills (15 skills, 48.4K installs)

| Skill | Installs | Purpose |
|---|---|---|
| `n8n-workflow-patterns` | 9.8K | Reusable workflow design patterns |
| `n8n-mcp-tools-expert` | 6.7K | MCP tool integration inside n8n — connects n8n to MCP servers (including Hermes-exposed tools) |
| `n8n-node-configuration` | 6.1K | Correct configuration of n8n nodes |
| `n8n-code-javascript` | 5.7K | JavaScript Code node patterns |
| `n8n-validation-expert` | 5.3K | Workflow validation before activation |
| `n8n-expression-syntax` | 5.1K | n8n expression language mastery |
| `n8n-code-python` | 3.7K | Python Code node patterns |
| `n8n-error-handling` | 832 | Error handling and retry patterns |
| `n8n-agents` | 820 | AI Agent nodes and agentic workflows |
| `n8n-subworkflows` | 804 | Reusable subworkflow architecture |
| `n8n-self-hosting` | 803 | Self-hosted deployment and hardening |
| `n8n-binary-and-data` | 796 | Binary data handling (files, images) |
| `n8n-multi-instance` | 773 | Multi-instance architecture |
| `using-n8n-mcp-skills` | 552 | Meta-skill: driving n8n via MCP |
| `n8n-code-tool` | 537 | Code Tool node usage |

### n8n-io/skills (official, 14 skills)

`n8n-workflow-lifecycle-official`, `n8n-agents-official`, `n8n-debugging-official`, `n8n-code-nodes-official`, `n8n-error-handling-official`, `n8n-credentials-and-security-official`, `using-n8n-skills-official`, `n8n-expressions-official`, `n8n-node-configuration-official`, `n8n-loops-official`, `n8n-subworkflows-official`, `n8n-binary-and-data-official`, `n8n-data-tables-official`, `n8n-extending-mcp-official` — official guidance mirroring the community suite's topics.

## Quick Start

1. `npx skills add czlonkowski/n8n-skills`
2. Stand up a local instance: `docker run -it --rm -p 5678:5678 n8nio/n8n`
3. "Design a workflow that watches a form submission, enriches the lead with web research, and posts a Slack alert"
4. "Review this workflow JSON for errors before I activate it"
5. "Add an MCP tool node that calls a CorpusIQ connector"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Operator enablement** | Business operators live in n8n — these skills let us spec and ship automations for them, strengthening the CorpusIQ operator platform thesis |
| **MCP bridge** | `n8n-mcp-tools-expert` + `n8n-extending-mcp-official` document calling MCP tools from n8n — the same protocol CorpusIQ connectors speak |
| **Internal automations** | Draft and validate n8n workflows for internal ops before handoff to the dev team |
| **Inbound lead answers** | Answer "can CorpusIQ help me automate X in n8n" questions with working workflow designs |

## Limitations / Verification

- Skills are guidance workflows, not an n8n deployment — you need an n8n instance (cloud or self-hosted) for execution
- Community repo is third-party maintained; cross-check against the official repo where topics overlap
- `n8n-self-hosting` assumes Docker or npm hosting experience

```bash
# Verify local n8n instance (default port 5678)
curl -s http://localhost:5678/healthz
```

## Related

- [MCP & API Integration catalog section](/hermes/skills/catalog/)
- [Firecrawl Skills Setup](/hermes/skills/catalog/firecrawl-skills-setup/)
- [n8n documentation](https://docs.n8n.io/)

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
