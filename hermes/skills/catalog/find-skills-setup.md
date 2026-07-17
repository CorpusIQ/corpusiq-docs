---
title: find-skills — Skill Discovery Tool for Hermes Agents
description: Install and use vercel-labs/skills@find-skills (2.5M installs) to search across skills.sh, agentskills.io, npm, and GitHub for Hermes-compatible agent skills in a single query.
---

# find-skills — Setup Guide

**Source:** [vercel-labs/skills](https://github.com/vercel-labs/skills) (2.5M installs)
**Category:** Skill Discovery
**Languages:** JavaScript

The official skill discovery tool from Vercel Labs. Searches across all major agent skill marketplaces — skills.sh, agentskills.io, npm, and GitHub — in a single query. Returns installable skill references with metadata: source repo, install count, category, and Hermes compatibility. At 2.5M installs, this is the most-used skill in the entire ecosystem.

---

## Installation

```bash
npx skills add vercel-labs/skills@find-skills
```

After installation, verify:
```bash
npx skills search find-skills  # Should show the installed skill
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Any version — CLI tool, no integration required |
| **npx skills** | v1.5+ (included with Hermes) |
| **Network** | Outbound HTTPS to skills.sh, GitHub API, npm registry |
| **GitHub Token** | Optional — enables private repo search and higher rate limits |

### Optional: GitHub Token for Higher Rate Limits

Without a token, GitHub API queries are limited to 60/hour. With a token, the limit increases to 5,000/hour:

```bash
export GITHUB_TOKEN=$(cat ~/.hermes/profiles/corpusiq/secrets/github.token)
```

---

## Key Capabilities

### Core Features

| Capability | How to Trigger | Notes |
|---|---|---|
| **Multi-marketplace search** | `find-skills "browser automation"` | Searches skills.sh, agentskills.io, npm, GitHub simultaneously |
| **Install-count ranking** | Results sorted by adoption | Most popular first |
| **Category filtering** | `find-skills "video" --category production` | Narrow by skill category |
| **Hermes compatibility** | `find-skills "memory" --compatible hermes` | Only skills confirmed Hermes-compatible |
| **Direct install path** | Each result includes `npx skills add <ref>` | Copy-paste to install |
| **Source verification** | GitHub stars, last commit, open issues | Quality signals in results |
| **JSON output** | `find-skills "seo" --json` | Programmatic consumption for automation |

### Search Syntax

```bash
# Basic search
find-skills "browser automation"

# Filter by marketplace
find-skills "memory" --source skills.sh

# Hermes-compatible only
find-skills "email" --compatible hermes

# With minimum install threshold
find-skills "monitoring" --min-installs 1000

# JSON output for scripting
find-skills "growth" --json | jq '.results[] | {name, installs, source}'

# Combined filters
find-skills "video production" --compatible hermes --min-installs 5000 --json
```

---

## Hermes/CorpusIQ Relevance

**Skill Catalog Maintenance:** Automates the daily "check skills.sh for new skills" workflow. Instead of running 30+ manual `npx skills search <term>` queries, one `find-skills` call surfaces new additions across all marketplaces.

**Agent Self-Discovery:** Hermes agents can discover and install skills autonomously. A growth agent needing SEO capabilities can `find-skills "seo audit" --compatible hermes` and install the top result without human intervention.

**Quality Filtering:** The `--min-installs` and `--compatible` flags prevent installation of unverified or incompatible skills — critical for autonomous agent operation.

**Integration with skill-creator:** After creating a skill with `anthropics/skills@skill-creator`, use `find-skills` to verify it appears correctly in marketplaces and check install counts.

---

## Example: Daily Skill Discovery Automation

```bash
#!/bin/bash
# Run daily to discover new Hermes-compatible skills
# Save to: ~/.hermes/profiles/corpusiq/cron/daily-skill-discovery.sh

export GITHUB_TOKEN=$(cat ~/.hermes/profiles/corpusiq/secrets/github.token)

# Search across categories
for category in "browser" "marketing" "mcp" "memory" "monitoring" "video" "growth" "security" "email" "social"; do
    echo "=== $category ==="
    find-skills "$category" --compatible hermes --min-installs 500 --json | \
        jq -r '.results[] | "\(.name) — \(.installs) installs — npx skills add \(.ref)"'
    echo ""
done
```

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `find-skills: command not found` | Skill not installed | `npx skills add vercel-labs/skills@find-skills` |
| GitHub results missing | Rate limited (no token) | Set `GITHUB_TOKEN` environment variable |
| Empty results for valid query | `--min-installs` too high | Lower threshold or remove filter |
| Slow response (>10s) | Network latency or large result set | Add `--limit 10` to cap results |
| skills.sh results missing | skills.sh website down (500/Vercel) | CLI falls back to npm + GitHub; retry later |

---

## See Also

- [skill-creator](/hermes/skills/catalog/skill-creator-setup/) — Anthropic's skill creation framework
- [Skills Catalog](/hermes/skills/catalog/) — Browse all documented skills
- [Skill Marketplaces](/hermes/skills/skill-marketplaces/) — Guide to all skill marketplaces
- [Creating Custom Skills](/hermes/skills/creating-skills/) — Author your own skills
