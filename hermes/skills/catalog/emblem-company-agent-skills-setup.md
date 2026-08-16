---
title: "Emblem Company Agent Skills — Portfolio & Market Research Setup"
description: "emblemcompany/agent-skills — 9 skills, 78.6K installs: portfolio tracking, market research, AI agent wallet, and token operations from the Emblem platform team."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/emblem-company-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "portfolio", "market research", "fintech"]
---

# Emblem Company Agent Skills — Setup Guide

**Source:** [emblemcompany/agent-skills](https://skills.sh/emblemcompany/agent-skills)
**GitHub:** [emblemcompany/agent-skills](https://github.com/emblemcompany/agent-skills)
**Skills:** 9 skills · 78.6K total installs
**Category:** Fintech / Portfolio & Market Research
**First Seen:** catalogued August 15, 2026 evening sweep
**Quality Tier:** 🟡 Trusted (crypto wallet and token-trading skills — verify transaction boundaries before any autonomous use)

Emblem's agent skills cover portfolio tracking, market research, an AI agent wallet, token swaps, and DeFi yield — the operational layer for an agent that manages crypto positions. Queued in prior sweeps at an 8.8K API-sum estimate; the publisher page shows 78.6K across 9 skills — a 9x jump, the second-largest underestimate of this sweep.

---

## Installation

```bash
npx skills add emblemcompany/agent-skills
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Emblem platform access** | For wallet, portfolio, and trading skills |
| **Funded wallet** | For any live token operations — and strong guardrails |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| emblem-portfolio-tracker | 8.9K | Track portfolio positions and performance |
| emblem-market-research | 8.8K | Market research workflows |
| emblem-ai-agent-wallet | 8.8K | Agent-managed wallet operations |
| emblem-ai-prompt-examples | 8.8K | Prompt patterns for the platform |
| emblem-ai-react | 8.8K | React integration |
| emblem-ai | 8.7K | Core platform interaction |
| emblem-defi-yield | 8.7K | DeFi yield strategies |
| emblem-memecoin-scout | 8.6K | Memecoin discovery |
| emblem-token-swap | 8.6K | Token swap execution |

## Quick Start

1. Install: `npx skills add emblemcompany/agent-skills`
2. Start read-only: `emblem-portfolio-tracker` and `emblem-market-research` need no transaction authority
3. Gate any wallet or swap skill behind human approval before first live use

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Market research pattern** | emblem-market-research as a reference workflow for our own research sweeps |
| **Portfolio reporting** | Tracker-style aggregation for investment reporting |
| **Fintech client work** | Reference architecture for clients building agent-managed finance products |
| **Guardrail study** | A real-world case of agent wallet skills — useful when advising on AI finance safety |

## Limitations / Verification

- Publisher-page install counts verified; individual skill audit pages were not fetched for this multi-skill suite
- Wallet and token-swap skills can move real value — never run them without explicit transaction limits and human approval
- Emblem platform account and possibly a funded wallet required for full functionality

```bash
npx skills add emblemcompany/agent-skills   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
