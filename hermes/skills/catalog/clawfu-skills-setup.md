---
title: ClawFu Skills — Full Setup Guide for Hermes Agents
description: Install and use ClawFu's 175 expert marketing methodologies for AI agents. MCP-native. Dunford, Schwartz, Cialdini, Ogilvy, Hormozi — encoded as agent-readable skills.
---

# ClawFu Skills — Setup Guide

**Source:** [guia-matthieu/clawfu-skills](https://github.com/guia-matthieu/clawfu-skills) (134⭐)
**Category:** Marketing
**Language:** Python (MCP Server)

175 expert marketing methodologies for AI agents. The world's best marketing thinkers — Dunford on positioning, Schwartz on copywriting, Cialdini on persuasion, Ogilvy on advertising, Hormozi on offers, Voss on negotiation — encoded as structured, agent-readable instructions. Free, open source, MIT licensed. Delivered as an MCP server.

---

## Installation

### MCP Server (Claude Desktop / Claude Code / Copilot / Hermes)

```bash
npx @clawfu/mcp-skills
```

### Hermes MCP Config

Add to `~/.hermes/config.yaml`:

```yaml
mcp:
  servers:
    clawfu:
      command: npx
      args: ["@clawfu/mcp-skills"]
```

### Clone as Skills Directory

```bash
git clone https://github.com/guia-matthieu/clawfu-skills.git
# Point Hermes to the cloned directory
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js** | Required for npx MCP server |
| **Hermes Agent** | MCP support required for MCP server mode |
| **No API key** | Completely free, no account needed |

---

## Key Capabilities

### Skill Categories (28 total, 175 skills)

| Category | Count | Highlights |
|---|---|---|
| **Content** | 24 | Copywriting (Schwartz), Storytelling (StoryBrand), Persuasion (Cialdini), SEO writing |
| **Strategy** | 17 | Positioning (Dunford), Competitive Analysis (Porter), JTBD, Cognitive Biases |
| **Audio** | 16 | Podcast Production (Ira Glass), Sonic Branding, Sound Design (Murch) |
| **Automation** | 10 | Workflow Builder, Data Visualizer, Report Generator |
| **SEO Tools** | 8 | Schema Markup, Lighthouse Audit, Link Checker, Keyword Clustering |
| **RevOps** | 8 | Pipeline Forecasting, Forecast Scenarios, Revenue Attribution |
| **Validation** | 8 | Mom Test, Customer Discovery, Lean Canvas, Pricing Validation |
| **Sales** | 6 | Sales Narrative (Dunford), SPIN Selling, MEDDIC, Negotiation (Voss) |
| **SDR Automation** | 6 | Lead Enrichment, Outbound Sequencer, ICP Scoring |
| **Growth** | 4 | Growth Loops (Reforge), PLG (Wes Bush), Referral Systems |
| **Product** | 3 | Product Discovery (Cagan), Design Sprint (GV), Shape Up |
| **Leadership** | 3 | High-Output Management (Grove), Radical Candor, One-on-Ones |
| **Funnels** | 3 | DotCom Secrets (Brunson), Launch Formula, Nurture Sequences |
| **Startup** | 3 | YC Pitch Deck, Startup Metrics, Fundraising Narrative |
| **Crisis** | 4 | Crisis Detector, Response Coordinator, Reputation Recovery |

### Top Skills for Growth Agents

| Skill | Framework/Method | Best For |
|---|---|---|
| **Positioning** | April Dunford's "Obviously Awesome" | Market positioning, competitive differentiation |
| **Copywriting** | Eugene Schwartz's "Breakthrough Advertising" | Landing pages, ads, email sequences |
| **Persuasion** | Robert Cialdini's 7 Principles | Conversion optimization, sales copy |
| **Growth Loops** | Reforge | Sustainable growth systems vs. funnels |
| **Mom Test** | Rob Fitzpatrick | Customer discovery without bias |
| **Sales Narrative** | April Dunford + Bob Moesta | Pitch decks, demo scripts |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Landing page copy** | Load Schwartz copywriting + Cialdini persuasion skills to draft high-converting landing pages |
| **Market positioning** | Use Dunford positioning framework to refine CorpusIQ messaging against competitors |
| **Customer discovery** | Apply Mom Test methodology when interviewing operators about pain points |
| **Pitch deck creation** | Combine YC pitch deck + Dunford sales narrative for investor/partner presentations |
| **Growth strategy** | Use Reforge growth loops to design acquisition and retention systems |
| **Content marketing** | Load SEO writing + content strategy skills for blog and social content planning |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| **MCP connection refused** | Verify npx is available: `which npx` — install Node.js if missing |
| **Skill not loading** | Check MCP server is in config.yaml and Hermes has restarted |
| **Too many skills** | Use skill orchestrator (included) to chain relevant skills for complex tasks |

## Verification

```bash
# Verify MCP server starts
npx @clawfu/mcp-skills --help 2>&1 | head -5

# Verify skill installed in Hermes
hermes mcp list | grep clawfu

# Quick test — ask Hermes to use a ClawFu skill
# In session: "Use the ClawFu positioning framework to analyze our competitor messaging"
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Discovery Page](/hermes/skills/marketplace/new-july16-2026/) →*
*Powered by CorpusIQ*
