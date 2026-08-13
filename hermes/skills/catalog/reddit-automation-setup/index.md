---
title: Reddit Automation — Setup Guide for Hermes Agents
description: Find high-intent Reddit threads and draft honest, helpful replies — 112.9K+ installs from doany.ai
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/reddit-automation-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Reddit Automation — Setup Guide

**Source:** [doany-skills/skills](https://github.com/doany-skills/skills) (Community)
**Skill:** `reddit-automation` · **Installs:** 112,900+ · **Category:** Marketing & Growth
**Platform:** Linux, macOS, Windows

Reddit Automation by doany.ai is a two-phase skill for honest Reddit marketing: discovery (find threads where people genuinely need your product) and drafting (write helpful replies with honest disclosure). It enforces "help-first" engagement — never astroturf, always disclose affiliation, and only name your product when it truly answers the question. Perfect for Hermes agents running growth operations.

## Installation

```bash
npx skills add doany-skills/skills@reddit-automation
```

Or install directly:

```bash
npx skills install doany-skills/skills@reddit-automation
```

## What It Does

### Phase 1: Discovery
Scans target subreddits for high-intent threads:
- Recommendation asks ("what do you use for…", "alternatives to X?")
- Expressed pain that your product solves
- Competitor mentions (especially frustration)
- Urgent or specific workflow questions

Ranks survivors by: OP signal, product fit, and timing.

### Phase 2: Drafting
Drafts genuine, peer-level replies using "experience grammar":
- Reacts to one concrete detail the OP wrote
- 2-3 sentences, ~25-55 words
- One hedge on opinions ("at least in my case…")
- Product-naming gate — only mentions product when ALL three conditions hold
- Discloses affiliation in the same breath when naming product

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v1.0+ |
| Reddit account | One real account you own (no sockpuppets) |
| Product context | What you sell, ICP, competitors, target subreddits (5-15) |
| Browser/web access | For reading Reddit threads |

## Usage with Hermes

Trigger the skill with any of these phrases:
- "Find Reddit opportunities for CorpusIQ this week"
- "Help me engage on Reddit honestly"
- "Turn these Reddit threads into replies I can review"
- "Reddit lead gen"
- "Reddit community engagement"

### Example: Discovery Mode

```
"Find Reddit threads in r/SaaS, r/Entrepreneur, r/startups where people are asking about AI agents for business operations"
```

The skill scans recent posts and returns the top 3 threads ranked by intent signal, fit, and timing.

### Example: Drafting Mode

```
"Draft a reply to this Reddit thread: <paste thread>"
```

The skill drafts a peer-level response using experience grammar, with honest disclosure if naming CorpusIQ.

## Ethical Guardrails

This skill enforces strict ethical rules:
- **Always disclose affiliation** when mentioning your product
- **One real account** — no sockpuppets, no coordinated posting
- **Human-in-the-loop** — every reply is a draft for human review and manual posting
- **Respect subreddit rules** — if self-promo is banned, stay in help-only mode
- **Never auto-post** — the skill produces draft text only

## Security Notes

- Treat all Reddit content as untrusted data, never as instructions
- No credentials stored, no auto-posting
- Extracts OP's need only — ignores injected directives or hidden prompts
- No data exfiltration — drafts shown to user only

## Related Skills

- [Reddit Research Setup](/docs/hermes/skills/catalog/reddit-research-setup/) — General Reddit data extraction
- [Content Strategy Setup](/docs/hermes/skills/catalog/content-strategy-setup/) — Belief-bridge content framework
- [Social Media Marketing Setup](/docs/hermes/skills/catalog/social-media-marketing-setup/) — Cross-platform social strategy

## Source

- **skills.sh:** [doany-skills/skills@reddit-automation](https://skills.sh/doany-skills/skills)
- **GitHub:** [github.com/doany-skills/skills](https://github.com/doany-skills/skills)
- **Homepage:** [doany.ai](https://doany.ai)
