---
title: Hermes Bible Skill Setup Guide
description: Install and use the 169-page community knowledge base for Hermes Agent — 25+ real-world flows, hidden features, SOUL.md patterns, and operational playbooks
---

# Hermes Bible Skill — Setup Guide

**Repo:** [DeployFaith/hermes-bible-skill](https://github.com/DeployFaith/hermes-bible-skill)
**Created:** June 21, 2026 | **Stars:** 3
**Size:** 169 pages, 25+ flows, 30+ hidden features, 40+ reference pages, 5 skill bundles

The largest single community contribution to the Hermes ecosystem. A comprehensive knowledge base covering real-world operational patterns, undocumented features, and SOUL.md engineering gathered from production Hermes deployments.

---

## Installation

### Via skills.sh (when indexed)
```bash
npx skills add DeployFaith/hermes-bible-skill
```

### Manual install
```bash
git clone https://github.com/DeployFaith/hermes-bible-skill.git /tmp/hermes-bible-skill
cp -r /tmp/hermes-bible-skill/ ~/.hermes/skills/hermes-bible-skill/
```

### Install specific bundles only
```bash
# List available bundles
ls ~/.hermes/skills/hermes-bible-skill/bundles/

# Install a specific bundle
cp -r ~/.hermes/skills/hermes-bible-skill/bundles/research-pipeline/ ~/.hermes/skills/
```

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v0.16.0+ |
| Disk | ~5MB for full skill |
| Python | 3.10+ (for scripts in `scripts/`) |
| Honcho | Optional — for session-analysis flows |

---

## Content Map

### Flows (25+ operational playbooks)

| Flow | Pages | Use Case |
|------|-------|----------|
| Autonomous Coding | 8 | Multi-file refactors, test-driven agent loops |
| Research Pipeline | 6 | Arxiv → synthesis → report generation |
| Email Operations | 5 | Inbound triage, outbound campaigns, monitoring |
| Social Media | 7 | Cross-platform posting, engagement, analytics |
| Infrastructure | 4 | DGX + Mac Mini coordination, cron management |
| Video Production | 5 | HeyGen pipeline, transcription, content extraction |

### SOUL.md Patterns

| Section | Topics |
|---------|--------|
| Profile Architecture | Role isolation, constraint layering, authority scoping |
| Personality Engineering | Tone calibration, aggressiveness tuning, creativity bounds |
| Tool Exclusivity | "Use X only" doctrine, tool routing, model selection |
| Execution Discipline | Preflight gates, governance loops, audit trails |

### Hidden Features (30+ undocumented capabilities)

Covers CLI flags, config tricks, and tool edge cases not in official docs. Examples:
- `hermes config set` advanced options
- `--watch` mode behaviors
- Model routing edge cases
- Session compaction strategies
- Memory system internals

### Bundles (5 pre-packaged skill sets)

| Bundle | Skills | Target |
|--------|--------|--------|
| `research-pipeline` | arxiv, web_search, web_extract, blogwatcher | Autonomous research agents |
| `social-ops` | xurl, browser-use-automation, postiz-cli-social-deployment | Social media automation |
| `email-mastery` | himalaya, corpusiq-email-operating-rules | Full email stack |
| `dev-infra` | github-*, mcp-*, terminal | Development infrastructure |
| `growth-engine` | All growth-operations skills | Growth agent bootstrap |

---

## CLI Reference

The skill acts as a reference lookup — trigger phrases cause Hermes to consult the bible:

| Trigger | Returns |
|---------|---------|
| "How do I set up X flow?" | Full flow documentation + code examples |
| "What are hidden features for Y?" | Curated list of undocumented capabilities |
| "Show me SOUL.md patterns for Z" | Pattern library with examples |
| "Which bundle should I use for W?" | Bundle recommendation with rationale |

---

## CorpusIQ Use Cases

### 1. Agent Bootstrap Acceleration
Instead of writing SOUL.md profiles from scratch, reference the bible's pattern library:
```
"How do I structure a growth agent SOUL.md?" → Returns 7-section template with fill-in blanks
```

### 2. Operational Pattern Discovery
When building a new automation, check if a flow already exists:
```
"Is there a flow for email monitoring + auto-response?" → Returns email-operations flow (5 pages)
```

### 3. Hidden Feature Exploitation
Discover undocumented capabilities that make agents more effective:
```
"Hidden features for memory management" → Returns compaction, pruning, and migration strategies
```

### 4. Training New Agents
Use the bundles as starter packs for new agent roles:
```bash
cp -r ~/.hermes/skills/hermes-bible-skill/bundles/growth-engine/ ~/.hermes/skills/
```
Instant full-stack growth agent skill set.

### 5. SOUL.md Engineering Reference
When tuning agent personalities, reference the pattern library for proven configurations:
- Constraint layering strategies
- Authority scoping patterns
- Tool routing doctrines

---

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| Skill not loading | Wrong install directory | Must be in `~/.hermes/skills/hermes-bible-skill/SKILL.md` |
| References return nothing | Hermes not recognizing trigger phrases | Ensure SKILL.md frontmatter has `trigger:` field |
| Bundles conflict with existing skills | Duplicate skill names | Install bundles one at a time, check for conflicts |
| Large disk usage | Full install includes all bundles + references | Install only needed bundles |

### Verification

```bash
# Confirm installation
ls ~/.hermes/skills/hermes-bible-skill/SKILL.md && echo "✓ Skill installed"

# Check bundle availability
ls ~/.hermes/skills/hermes-bible-skill/bundles/ && echo "✓ Bundles available"

# Count flows
ls ~/.hermes/skills/hermes-bible-skill/references/flows/ 2>/dev/null | wc -l
# Should show 25+ files

# Test a lookup
cat ~/.hermes/skills/hermes-bible-skill/references/flows/*.md | head -20
```

---

*← [Hermes Skill Graph Setup](/hermes/skills/catalog/hermes-skill-graph-setup/) | [Next: Skill Precipitator →](/hermes/skills/catalog/hermes-skill-precipitator-setup/)*
*↑ [Skills Home](/hermes/skills/)*
