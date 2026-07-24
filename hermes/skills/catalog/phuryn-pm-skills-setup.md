---
title: Phuryn PM Skills — Competitive Strategy for Hermes Agents
description: Competitive analysis, business model generation, and privacy policy creation with 7K+ combined installs. Structured competitive intelligence with differentiation mapping and strategic synthesis.
---

# Phuryn PM Skills — Setup Guide

**Source:** [phuryn/pm-skills](https://skills.sh/phuryn/pm-skills) (7K+ combined installs)
**Category:** Product & Strategy
**Quality Tier:** 🟡 Beta

Product strategy toolkit for agents conducting competitive analysis, business model design, and compliance documentation. The competitor analysis skill stands out — 5-competitor structured profiles with strengths, weaknesses, differentiation mapping, and strategic synthesis. Built for agents that need to produce professional-grade competitive intelligence.

---

## Installation

```bash
npx skills add phuryn/pm-skills --skill competitor-analysis
npx skills add phuryn/pm-skills --skill business-model
npx skills add phuryn/pm-skills --skill privacy-policy
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **competitor-analysis** | 2.4K | 5-competitor structured analysis — profiles, strengths, weaknesses, pricing, differentiation, strategic synthesis |
| **business-model** | 2.4K | Business model canvas generation and analysis |
| **privacy-policy** | 2.2K | Privacy policy and compliance documentation generation |

---

## Key Capabilities

### Competitive Analysis (Standout Skill)
- **Market Overview**: Size, growth trends, customer segments, success factors, competitive intensity
- **5-Competitor Deep Dive**: For each competitor:
  - Company profile (founding, funding, market focus, positioning)
  - Core product strengths (features, advantages, value prop, technology moats)
  - Product weaknesses & gaps (missing features, limitations, customer pain points)
  - Business model & pricing (structure, price points, GTM channels, revenue model)
  - Competitive threats (customer base, switching costs, partnerships, recent moves)
- **Differentiation Mapping**: Unmet needs, feature/pricing/UX gaps, underserved segments, channel opportunities
- **Strategic Synthesis**: Competitive dynamics, future threats, partnership opportunities

### Business Model
- Business model canvas generation
- Revenue stream analysis
- Cost structure and unit economics

### Privacy Policy
- Compliance-ready privacy policy generation
- GDPR/CCPA considerations
- Data handling documentation

---

## Quick Start

```bash
# Run competitive analysis
npx skills use phuryn/pm-skills@competitor-analysis
# Then: "Analyze the competitive landscape for AI-powered data analytics tools targeting mid-market companies"
```

The skill produces a 5-competitor structured report with:
- Market overview and definition
- Individual competitor profiles (strengths, weaknesses, pricing, threats)
- Differentiation opportunities with specific actionable gaps
- Strategic synthesis and recommendations

---

## Verification

```bash
npx skills list | grep phuryn/pm-skills
```

---

## Notes

- Competitive analysis is the most polished skill — structured, thorough, and actionable
- 5-competitor format is ideal for board decks, investor updates, and strategic planning
- Business model skill uses standard Business Model Canvas framework
- Privacy policy skill useful for compliance documentation but verify output against legal requirements
- Complements `deanpeters/product-manager-skills` (PRDs, user stories) and `refoundai/lenny-skills` (PM methodology)
- Directly useful for CorpusIQ competitive intelligence and market positioning work
