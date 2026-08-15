---
title: Tiangong AI Skills — Email & Research Data Fetching Suite Setup
description: "tiangong-ai/skills — 58 skills, 9.0K installs: email SMTP send and IMAP fetch, plus a research data-fetching suite over GDELT, regulations.gov, NASA FIRMS, Open-Meteo, EPA AirNow, USGS, Bluesky, YouTube, scientific journals, and Figshare."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/tiangong-ai-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "email", "smtp", "imap", "research", "data fetching"]
---

# Tiangong AI Skills — Setup Guide

**Source:** [tiangong-ai/skills](https://skills.sh/tiangong-ai/skills)
**GitHub:** [tiangong-ai/skills](https://github.com/tiangong-ai/skills)
**Skills:** 58 skills · 9.0K total installs
**Category:** Email Automation & Research Data
**First Seen:** catalogued August 15, 2026 midday sweep
**Quality Tier:** 🟡 Trusted (publisher is the Tiangong national AI platform org, Beijing Academy of AI; suite verified at 9.0K on publisher page)

Tiangong publishes the largest research-data-fetching suite we have catalogued: 58 skills spanning email (SMTP send, IMAP fetch and append), scientific journal search, and a wide net of public data sources — GDELT, regulations.gov, NASA FIRMS fire data, Open-Meteo, EPA AirNow, USGS water data, the Federal Register, Bluesky cascades, YouTube comments, and Figshare datasets.

---

## Installation

```bash
npx skills add tiangong-ai/skills
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **SMTP/IMAP credentials** | For the email skills |
| **API keys where required** | Some sources need provider keys |

## What It Provides (highlights)

| Area | Representative skills (installs) |
|---|---|
| Email | email-smtp-send (6.7K), email-imap-fetch (369), email-imap-append (59), email-imap-full-fetch (91) |
| News & events | ai-tech-rss-fetch (233), gdelt-events-fetch (23), gdelt-gkg-fetch (23), gdelt-doc-search (33), gdelt-mentions-fetch (24) |
| Environmental | nasa-firms-fire-fetch (20), open-meteo-historical-fetch (22), openaq-data-fetch (24), airnow-hourly-obs-fetch (17), usgs-water-iv-fetch (17), open-meteo-flood-fetch (21), open-meteo-air-quality-fetch (19) |
| Policy | regulationsgov-comments-fetch (23), regulationsgov-comment-detail-fetch (23), federal-register-doc-fetch (17) |
| Social & video | bluesky-cascade-fetch (24), youtube-comments-fetch (23), youtube-video-search (22) |
| Science | sci-journals-hybrid-search (78), figshare-data-download (40), academic-paper-download (5) |
| Knowledge base | dify-knowledge-base-search (110), dify-knowledge-base-upload (41), tiangong-kb-* series, fetch-abstract-to-kb (40) |

## Quick Start

1. Install: `npx skills add tiangong-ai/skills`
2. Load email-smtp-send for outbound mail automation, or gdelt-events-fetch for event research
3. Ask: "send this transactional email via SMTP and fetch GDELT events mentioning the topic"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Email automation** | SMTP/IMAP skills compose with our email ops stack as a self-hosted fallback |
| **Research sweeps** | GDELT, regulations.gov, and Federal Register fetching for market research |
| **Brand monitoring** | Bluesky cascade and YouTube comment fetching for channel monitoring |
| **Environmental data** | Open-Meteo, NASA FIRMS, EPA, and USGS skills for data-driven reporting |

## Limitations / Verification

- Multi-skill suite; individual security-audit pages not fetched this sweep
- Long tail is thin (many skills under 100 installs); the email and GDELT skills carry the suite
- Some sources require their own API keys or rate-limit handling

```bash
npx skills add tiangong-ai/skills   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
