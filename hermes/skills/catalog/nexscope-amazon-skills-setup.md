---
title: Nexscope Amazon Skills — E-Commerce Product Research for Hermes Agents
description: Amazon product research, listing optimization, and keyword analysis skills with 77K+ combined installs. Research product opportunities, analyze competition, and optimize listings across 12 Amazon marketplaces.
---

# Nexscope Amazon Skills — Setup Guide

**Source:** [nexscope-ai/amazon-skills](https://skills.sh/nexscope-ai/amazon-skills) (77K+ combined installs)
**Category:** Growth Operations / E-Commerce
**Quality Tier:** 🟢 Production

Comprehensive Amazon seller toolkit for agents. Research product opportunities with deep market analysis, optimize listings for conversion, and discover high-value keywords. Supports 12 Amazon marketplaces (US, UK, DE, FR, IT, ES, JP, CA, AU, IN, MX, BR) with structured competitive intelligence workflows.

---

## Installation

```bash
npx skills add nexscope-ai/amazon-skills --skill amazon-product-research
npx skills add nexscope-ai/amazon-skills --skill amazon-listing-optimization
npx skills add nexscope-ai/amazon-skills --skill amazon-keyword-research
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **amazon-product-research** | 77.1K | Full product opportunity analysis — market demand, competition density, profit potential, risk evaluation |
| **amazon-listing-optimization** | 929 | Optimize product listings for conversion — titles, bullets, descriptions, A+ content |
| **amazon-keyword-research** | 877 | Discover high-value search terms, keyword difficulty scoring, indexing strategies |

---

## Key Capabilities

### Product Research
- **Market Intelligence**: Search volume trends, market size indicators, category positioning, seasonal patterns
- **Competition Deep Dive**: Total competitor count, market concentration, review distribution, price range mapping
- **Demand Validation**: Google Trends analysis, Amazon autocomplete, related searches, social validation
- **Competition Scoring (1-10)**: Structured scoring system from highly fragmented (9-10) to monopolized (1-2)
- **Risk Evaluation**: Market risks, regulatory issues, trend sustainability
- **Multi-Marketplace**: Research across US, UK, DE, FR, IT, ES, JP, CA, AU, IN, MX, BR

### Listing Optimization
- Title optimization with keyword placement
- Bullet point structure for conversion
- A+ Content recommendations
- Backend search term strategy

### Keyword Research
- High-value search term discovery
- Keyword difficulty assessment
- Indexing strategy and tracking

---

## Quick Start

Natural language queries supported:

```
Research "wireless earbuds" as a product opportunity on Amazon
Analyze the market for "smart water bottles" — demand, competition, profit potential
Should I sell "phone cases" or "phone stands"? Compare both opportunities
Research "Hundehalsbänder" on Amazon Germany — full market analysis
```

---

## Verification

```bash
npx skills list | grep nexscope-ai/amazon-skills
```

---

## Notes

- Most-installed Amazon research skill on skills.sh (77K+)
- Uses web_search-based workflows — no API keys required
- Multi-marketplace support is rare and valuable for international sellers
- Competition scoring system provides structured decision-making framework
- Relevant for CorpusIQ e-commerce operator workflows and competitive analysis
