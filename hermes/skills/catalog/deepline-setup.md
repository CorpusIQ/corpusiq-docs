---
title: Deepline — GTM Platform Skills for Hermes Agents
description: Six GTM platform skills for TAM building, portfolio prospecting, niche signal discovery, LinkedIn URL lookup, feedback analysis, and Clay integration. 92K+ combined installs across 6 skills.
---

# Deepline — Setup Guide

**Source:** [code.deepline.com](https://skills.sh/code.deepline.com) (92K+ combined installs)
**Category:** Go-to-Market / Prospecting
**Quality Tier:** 🟢 Production

Deepline is a GTM platform that provides six skills for go-to-market research, prospecting, and pipeline building — all accessible as agent skills. High install counts (14-15K each) indicate a mature, well-adopted ecosystem. These skills give Hermes agents structured access to TAM analysis, prospect discovery, and market signal detection.

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **niche-signal-discovery** | 15.5K | Find emerging market signals and niche opportunities |
| **build-tam** | 15.4K | Build Total Addressable Market analyses with data |
| **portfolio-prospecting** | 15.3K | Discover and qualify prospects at portfolio scale |
| **deepline-feedback** | 15.3K | Analyze customer feedback and market signals |
| **clay-to-deepline** | 15.3K | Bridge Clay.com enrichment data into Deepline |
| **linkedin-url-lookup** | 15.3K | Resolve and enrich LinkedIn profile/company URLs |

---

## Installation

```bash
npx skills add code.deepline.com --skill niche-signal-discovery
npx skills add code.deepline.com --skill build-tam
npx skills add code.deepline.com --skill portfolio-prospecting
npx skills add code.deepline.com --skill deepline-feedback
npx skills add code.deepline.com --skill clay-to-deepline
npx skills add code.deepline.com --skill linkedin-url-lookup
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Deepline Account** | Sign up at [deepline.com](https://deepline.com) |
| **API Key** | Available in Deepline dashboard settings |

---

## Key Capabilities

### Niche Signal Discovery (15.5K)
Identify emerging market signals before they become saturated. Detects early-stage trends, underserved niches, and competitor weak spots across industries.

### TAM Builder (15.4K)
Build data-backed Total Addressable Market analyses with structured methodologies. Generates TAM/SAM/SOM breakdowns with source attribution.

### Portfolio Prospecting (15.3K)
Discover and qualify prospects at portfolio scale — ideal for outbound campaigns, partnership development, and ecosystem mapping.

### LinkedIn URL Lookup (15.3K)
Resolve and enrich LinkedIn URLs for companies and individuals. Useful for prospect research, job change alerts, and company growth tracking.

### Feedback Analysis (15.3K)
Analyze customer feedback, reviews, and market signals across platforms to identify product improvement opportunities and competitive weaknesses.

### Clay-to-Deepline Bridge (15.3K)
Pipe Clay.com enrichment data directly into Deepline workflows — unified data pipeline for GTM operations.

---

## Quick Start — Hermes Agent

```bash
# Install all six skills
for skill in niche-signal-discovery build-tam portfolio-prospecting \
    deepline-feedback clay-to-deepline linkedin-url-lookup; do
    npx skills add code.deepline.com --skill "$skill"
done

# Verify
npx skills list | grep deepline
```

---

## Verification

```bash
# List installed deepline skills
npx skills list | grep "code.deepline.com"

# Should show 6 skills installed
```

---

## Notes

- **Mature ecosystem**: 92K+ combined installs across 6 skills — production-grade reliability
- **Use case for CorpusIQ**: TAM analysis for market sizing, portfolio prospecting for lead generation, signal discovery for identifying operator pain points
- **Clay integration**: If using Clay.com for data enrichment, the clay-to-deepline bridge unifies the pipeline
- **LinkedIn skill**: No LinkedIn API auth needed — resolves public URLs and enriches with available data
- **Related skills**: prospect-research-personalization, inbound-lead-analysis-domain-first
