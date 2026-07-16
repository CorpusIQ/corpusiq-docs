---
title: New Skills — July 15, 2026 (Supplement)
description: 5 additional OpenClaw ecosystem skills discovered in follow-up sweep — Grok search, release maintenance, skill vetting, and Apple Calendar integration.
---

# New Skills Discovery — July 15, 2026 (Supplement)

**Time:** 12:03 PM MST — follow-up sweep after the [main July 15 sweep](/hermes/skills/marketplace/new-july15-2026/).

A targeted sweep of the OpenClaw ecosystem surfaced **5 additional skills** not captured by the earlier 18-query sweep. Combined install base: **1,305+ installs**.

## Skills Discovered

| Skill | Installs | Source | Category |
|-------|----------|--------|----------|
| [apple-calendar](#apple-calendar) | 662 | sundial-org/awesome-openclaw-skills | Productivity |
| [openclaw-release-maintainer](#openclaw-release-maintainer) | 174 | steipete/clawdis | DevOps |
| [openclaw-skill-vetter-1-0-0](#openclaw-skill-vetter) | 171 | skills.volces.com | Quality Assurance |
| [openclaw-skill-vetter](#openclaw-skill-vetter) | 168 | skills.volces.com | Quality Assurance |
| [openclaw-grok-search](#openclaw-grok-search) | 130 | stemmaker/openclaw-grok-search | Search |

---

## apple-calendar

**Source:** [sundial-org/awesome-openclaw-skills](https://github.com/sundial-org/awesome-openclaw-skills) · **662 installs**

Apple Calendar integration for OpenClaw agents — create, read, update, and delete calendar events. Manage schedules, set reminders, and coordinate meetings directly through agent commands.

### Capabilities
- Create/read/update/delete calendar events
- Set reminders and alerts
- Query availability and find open slots
- Multi-calendar support (iCloud, Exchange, Google via CalDAV)
- Natural language event creation ("Schedule a meeting tomorrow at 2pm")

### Installation
```bash
npx skills add sundial-org/awesome-openclaw-skills/apple-calendar
```

### Hermes/CorpusIQ Relevance
Enables Hermes agents to manage scheduling autonomously — coordinate team meetings, set deadlines, and manage the CorpusIQ content calendar. The CalDAV protocol support means it works across iCloud, Exchange, and Google Calendar.

**Setup guide:** [apple-calendar-setup.md](/hermes/skills/catalog/apple-calendar-setup/)

---

## openclaw-release-maintainer

**Source:** [steipete/clawdis](https://github.com/steipete/clawdis) · **174 installs**

Automated release maintenance for OpenClaw projects — version bumping, changelog generation, tag creation, and GitHub release publishing. Part of the Clawdis ecosystem of development tools.

### Capabilities
- Semantic version bumping (major/minor/patch)
- Auto-generated changelogs from commit history
- Git tag creation and pushing
- GitHub release creation with release notes
- Pre-release checklist verification

### Installation
```bash
npx skills add steipete/clawdis/openclaw-release-maintainer
```

### Hermes/CorpusIQ Relevance
Useful for teams maintaining multiple Hermes/OpenClaw skill packages. Automates the release workflow for skill repositories — ensuring consistent versioning and changelog quality across the CorpusIQ ecosystem.

**Setup guide:** [openclaw-release-maintainer-setup.md](/hermes/skills/catalog/openclaw-release-maintainer-setup/)

---

## openclaw-skill-vetter / openclaw-skill-vetter-1-0-0

**Source:** [skills.volces.com](https://skills.volces.com) · **168 + 171 installs** · Two versions of the same skill.

Automated skill quality validation — scans installed skills for common issues: missing dependencies, broken triggers, incompatible tool requirements, and security anti-patterns. The v1.0.0 variant includes stricter validation rules.

### Capabilities
- Dependency validation (checks all required tools are available)
- Trigger conflict detection (multiple skills with same keyword)
- Tool compatibility matrix checking
- Security anti-pattern scanning
- Skill structure validation (YAML frontmatter, required sections)
- Version compatibility checking (v1.0.0 only)

### Installation
```bash
# Standard version
npx skills add skills.volces.com/openclaw-skill-vetter

# Stricter v1.0.0 version
npx skills add skills.volces.com/openclaw-skill-vetter-1-0-0
```

### Hermes/CorpusIQ Relevance
Directly applicable to CorpusIQ's 133+ skill library. Automated vetting prevents broken or incompatible skills from being loaded by production agents. The security scanning is particularly valuable for skills sourced from the marketplace.

**Setup guide:** [openclaw-skill-vetter-setup.md](/hermes/skills/catalog/openclaw-skill-vetter-setup/)

---

## openclaw-grok-search

**Source:** [stemmaker/openclaw-grok-search](https://github.com/stemmaker/openclaw-grok-search) · **130 installs**

Integrates xAI's Grok search capabilities into OpenClaw agents. Provides real-time web search with Grok's reasoning capabilities — combining search retrieval with AI analysis.

### Capabilities
- Real-time web search via Grok API
- AI-powered result analysis and synthesis
- Configurable search depth (quick vs deep research)
- Source citation in responses
- Rate limit handling and fallback strategies

### Installation
```bash
npx skills add stemmaker/openclaw-grok-search
```

### Hermes/CorpusIQ Relevance
Provides an alternative search backend for Hermes agents beyond DuckDuckGo and Firecrawl. Grok's reasoning layer can synthesize search results into actionable insights — useful for competitive research, market analysis, and trend monitoring.

**Setup guide:** [openclaw-grok-search-setup.md](/hermes/skills/catalog/openclaw-grok-search-setup/)

---

*Discovered via targeted OpenClaw ecosystem sweep — cross-referenced against the main July 15 sweep and all existing docs at corpusiq-docs/hermes/skills/.*
