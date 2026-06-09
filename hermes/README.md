# CorpusIQ Hermes Knowledge Repository

The definitive resource for building, deploying, and operating autonomous AI agents with [Hermes Agent](https://hermes-agent.nousresearch.com). Production-tested on a live 24-agent deployment. 32 pages, 1,700+ lines, 158 cataloged skills.

## Quick Links

- [Complete Table of Contents](/hermes/) — every page linked
- [Skills Marketplace](/hermes/skills/marketplace/) — 85+ curated skills from skills.sh
- [Architecture Overview](/hermes/architecture) — six-layer agent architecture
- [Setup Guide](/hermes/setup/) — installation and configuration
- [MCP Integration](/hermes/mcp/) — 30+ connected data sources

## What This Covers

- **Multi-machine deployment** — DGX Spark + Mac Mini Worker, 24 cron jobs
- **Agent orchestration** — Hermes, CrewAI, LangGraph, Reflexion
- **Persistent knowledge** — GBrain (729 files), GraphRAG, Dream Cycle, Honcho
- **73+ executable skills** — Marketing, development, operations
- **85+ marketplace skills** — Curated from skills.sh with install guides
- **53+ MCP server guides** — GA4, Stripe, Shopify, QuickBooks, and more
- **Browser automation** — Playwright with stealth patterns, OAuth lifecycle
- **Multi-model routing** — Cost-optimized model selection, ~65% savings
- **Content operations** — HeyGen video, Postiz publishing, engagement engines
- **Governance** — Seven rules, monitoring, drift detection, auditing

## Structure

| Section | Pages | Highlights |
|---------|-------|-----------|
| [Architecture](/hermes/architecture) | 1 | Six-layer design, deployment topology |
| [Setup](/hermes/setup/) | 1 | Linux, macOS, API configuration |
| [Orchestration](/hermes/orchestration/) | 4 | Hermes, CrewAI, LangGraph, Reflexion |
| [Knowledge](/hermes/knowledge/) | 1 | GBrain, GraphRAG, Dream Cycle, Honcho |
| [Skills](/hermes/skills/) | 4 | Marketplace (85+), Marketing (45), Dev (12), Ops (16) |
| [MCP](/hermes/mcp/) | 2 | Overview, 30+ server guides |
| [Infrastructure](/hermes/infrastructure/) | 5 | DGX, Mac Mini, Browser, Auth, Routing |
| [Governance](/hermes/governance/) | 4 | Registry, Email, Scheduling, Monitoring |
| [Content Ops](/hermes/content-ops/) | 3 | Video, Social, Engagement |
| [Outputs](/hermes/outputs/) | 1 | SEO, PRs, marketplace, recruiting |

## Install

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
npx skills add vercel-labs/agent-browser
npx skills add anthropics/skills@mcp-builder
```

## Contribute

This repo auto-updates via 3 monitoring crons that check for new Hermes releases, MCP servers, and skills. PRs welcome.

---

*Powered by CorpusIQ — the operating system for business agents*
