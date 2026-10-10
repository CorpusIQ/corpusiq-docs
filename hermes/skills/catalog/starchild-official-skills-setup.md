---
title: "Starchild Official Skills - Agent Platform Library Setup"
description: "Setup guide for starchild-ai-agent/official-skills - 179.7K combined installs. Starchild's official skill library for data, trading, and automation."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/starchild-official-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "crypto data", "trading automation", "agent platform"]
---

# Starchild Official Skills - Setup Guide

**Source:** [starchild-ai-agent/official-skills](https://www.skills.sh/starchild-ai-agent/official-skills) via skills.sh - 179.7K combined installs across 96 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [starchild-ai-agent/official-skills](https://github.com/starchild-ai-agent/official-skills) (27 stars, no license file; pushed 2026-10-08; each skill is a top-level directory with a SKILL.md plus optional tool scripts)
**Category:** Agent Platform / Skill Library
**Quality Tier:** 🟡 Beta - Starchild platform-maintained library; low GitHub traction (27 stars); mixed sampled verdicts - see Security

Starchild Official Skills is the platform-maintained skill library for Starchild's agent, with 96 indexed listings on skills.sh covering market data, trading venues, onboarding flows, media generation, and platform automation. The top skills by installs are coinglass (11,466), wallet (8,856), hyperliquid (8,634), coingecko (7,884), and twitter (7,864).

Each skill lives in its own top-level directory and ships a SKILL.md, plus optional Python tool scripts and templates; a GitHub Actions pipeline validates frontmatter and rebuilds skills.json on every push. Install one skill by name, or search the index from inside a Starchild agent conversation.

---

## Installation

Install skills by name through the skills.sh CLI:

```bash
npx skills add Starchild-ai-agent/official-skills --skill hyperliquid
```

Swap --skill hyperliquid for any other skill name from the table below (for example, --skill coinglass). Inside a Starchild agent conversation, the same index is reachable with a single search call that searches and auto-installs:

```text
search_skills(query="hyperliquid")
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| coinglass | 11,466 | Crypto derivatives market data such as open interest and funding rates |
| wallet | 8,856 | Wallet operations for agent accounts |
| hyperliquid | 8,634 | Trade perpetual futures on the Hyperliquid DEX |
| coingecko | 7,884 | Token prices and market metadata from CoinGecko |
| twitter | 7,864 | Twitter/X operations from an agent session |
| skill-creator | 7,755 | Scaffold new skills for the library |
| twelvedata | 7,739 | Market data via the Twelve Data API |
| skillmarketplace | 7,118 | Browse and install skills from the marketplace |
| orderly-onboarding | 7,045 | Guided onboarding for the Orderly venue |
| project-builder | 5,223 | Build and organize projects inside the platform |
| browser-preview | 4,612 | Preview web output in a browser |
| charting | 4,421 | Render charts and visualizations |
| composio | 4,319 | Wire Composio tool integrations into workflows |
| coder | 4,122 | Coding assistance inside the platform |
| slide-creator | 4,104 | Turn results into slide decks |
| wallet-policy | 4,061 | Set policy and guardrails on wallet actions |
| community-publish | 4,027 | Publish work to the community |
| preview-dev | 3,962 | Spin up a development preview |
| web-crawler | 3,927 | Crawl pages for research and data collection |
| chart | 3,921 | Quick chart generation from data |

The remaining 76 indexed listings range from 75 to 2,998 installs.

## Why This Matters for Hermes Agents

Starchild's library is less a course and more a toolbox: one directory per integration, each shipping a SKILL.md contract plus optional Python tool scripts that a platform agent can execute. For builders wiring market and platform data into agent workflows, that means connector logic for exchanges, price feeds, and on-chain analytics is already written and can be pulled in by name. The library also covers agent-platform mechanics, from skill creation and marketplace publishing to charting and media generation, so an agent can produce and ship its own utility skills. Because installs are per skill, a production agent can carry exactly the integrations it needs and nothing more. The caveats weigh here too: low GitHub traction and Warn verdicts on wallet-adjacent skills argue for scoped review before anything touches real funds.

## Usage

| You say | What happens |
|---|---|
| "Pull perpetual futures market data" | coinglass pulls derivatives metrics and hyperliquid covers the venue itself. |
| "What is this token trading at?" | coingecko and twelvedata fetch prices and market metadata. |
| "Chart our portfolio over time" | charting and chart render the visualization. |
| "Add a new skill to the library" | skill-creator scaffolds a SKILL.md with the required frontmatter. |
| "Crawl a page for research" | web-crawler fetches and extracts page content. |
| "Lock down what the agent can do with funds" | wallet-policy sets policy and guardrails on wallet actions. |
| "Turn results into a deck" | slide-creator builds slides from the session output. |

## Verification

Confirm the install by listing what the CLI installed:

```bash
npx skills list | grep -i hyperliquid
```

The repo's auto-generated skills.json index lists the full current library if you want to check what else exists without cloning.

Review a raw SKILL.md before installing (this URL returned 200 when checked on Oct 10, 2026):

```bash
curl -sL https://raw.githubusercontent.com/starchild-ai-agent/official-skills/main/coinglass/SKILL.md
```

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| coinglass | Pass | Pass | Pass |
| wallet | Pass | Warn | Warn |
| hyperliquid | Pass | Warn | Warn |

## Limitations

- No license file in the repository; without an explicit license, reuse and redistribution terms are undefined, so treat it as source-available reference until clarified.
- Low GitHub traction (27 stars) relative to 179.7K combined installs; most usage comes through the Starchild platform rather than open-source discovery.
- Mixed sampled verdicts: wallet and hyperliquid both show Socket Warn and Snyk Warn; treat wallet-adjacent skills as high-scrutiny installs.
- 96 indexed listings is the skills.sh API page cap; the repository may ship more skills than the snapshot shows.
- Several skills operate on live funds or exchange accounts; run them only with scoped keys and small balances, and review wallet-policy first.
- Some skills assume the Starchild agent runtime for their search and auto-install flows.


- Snapshot data, verified Oct 10, 2026: 179,684 combined installs across 96 indexed listings; 27 GitHub stars; no license file; last pushed 2026-10-08. Counts drift over time.

## Related

- [OKX CEX Agent Skills - Exchange Trading Suite Setup](/hermes/skills/catalog/okx-cex-agent-skills-setup) - a second exchange-trading skill suite to compare with the hyperliquid and okx coverage here.
- [OpenAI Agents Python Skills - Multi-Agent Setup](/hermes/skills/catalog/openai-agents-python-skills-setup) - Python agent plumbing that fits Starchild's tool-script layout.
- [Hermes Agent Core - Official Skill Setup Guide](/hermes/skills/catalog/hermes-agent-setup) - the core Hermes skill setup for running these skills on a Hermes host.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install per skill with --skill <name>; pulling the entire library into an agent expands its capability surface for no reason.
- Inside a Starchild agent conversation, search_skills(query="...") searches the index and auto-installs the match.
- Read the raw SKILL.md for anything touching funds before wiring it in; wallet and hyperliquid carry Socket and Snyk Warn verdicts.
- skills.json is the auto-generated index; do not edit it by hand, and check it to see the current library without cloning.
- Multi-file skills copy recursively, so Python tool scripts and templates land alongside SKILL.md when you install.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
