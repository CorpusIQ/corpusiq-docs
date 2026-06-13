---
title: Community Standalone Skills — Setup Guides (June 13 Update 2)
description: Setup guides for 5 new community standalone Hermes skills: wihy/hermes-agent-skill, aradotso/marketing-skills, aradotso/ai-agent-skills, hermess/ppt-director.
---

# Community Standalone Skills — Setup (June 13 Update 2)

## hermes-agent (wihy/hermes-agent-skill) — 493 installs

Third-party Hermes Agent wrapper providing configuration utilities and agent lifecycle management.

**Install:**
```bash
npx skills add wihy/hermes-agent-skill --skill hermes-agent
```

**Prerequisites:** Hermes Agent installed. No additional API keys.

**Verification:**
```bash
# The skill should be listed in available skills
hermes skills list | grep hermes-agent
```

---

## hermes-marketing-dashboard (aradotso/marketing-skills) — 414 installs

Marketing analytics dashboard for Hermes agents. Tracks campaign performance, social metrics, and growth KPIs from within the agent interface.

**Install:**
```bash
npx skills add aradotso/marketing-skills --skill hermes-marketing-dashboard
```

**Prerequisites:**
- Marketing API keys (Google Analytics, Meta Ads, etc.) for data sources
- Hermes Agent configured with web access

**Verification:**
```bash
hermes skills list | grep hermes-marketing-dashboard
```

**Key features:**
- Multi-channel campaign tracking
- Real-time dashboard generation
- Growth metric visualization
- ROAS and CPA calculations

---

## hermes-agent-framework (aradotso/ai-agent-skills) — 146 installs

Alternative Hermes agent framework with broader AI agent compatibility. Provides adapters for multiple agent runtimes while maintaining Hermes-native integration.

**Install:**
```bash
npx skills add aradotso/ai-agent-skills --skill hermes-agent-framework
```

**Prerequisites:** Hermes Agent. Optional: other agent runtimes for multi-framework orchestration.

**Verification:**
```bash
hermes skills list | grep hermes-agent-framework
```

**Key differences from aradotso/hermes-skills version:**
- Broader AI agent compatibility (not exclusively Hermes)
- Multi-framework orchestration patterns
- Cross-platform agent communication

---

## hermes-agent-self-evolution (aradotso/ai-agent-skills) — 130 installs

Self-improvement loops compatible with multiple agent frameworks. Implements automated capability discovery, skill gap analysis, and continuous improvement cycles.

**Install:**
```bash
npx skills add aradotso/ai-agent-skills --skill hermes-agent-self-evolution
```

**Prerequisites:** Hermes Agent (or compatible agent runtime). Access to skills.sh for capability discovery.

**Verification:**
```bash
hermes skills list | grep hermes-agent-self-evolution
```

**Key features:**
- Automated skill discovery from skills.sh
- Capability gap analysis
- Self-patching and improvement tracking
- Cross-framework evolution patterns

---

## ppt-director (hermess/ppt-director) — 84 installs

Programmatic PowerPoint presentation creation and management. Generate slide decks from data, templates, or natural language descriptions.

**Install:**
```bash
npx skills add hermess/ppt-director --skill ppt-director
```

**Prerequisites:** None. Works with python-pptx library (auto-installed).

**Verification:**
```bash
hermes skills list | grep ppt-director
```

**Use cases:**
- Automated report generation
- Data-driven presentation creation
- Template-based slide assembly
- Batch presentation processing

---

## Summary

| Skill | Source | Installs | Key Dependency |
|-------|--------|----------|---------------|
| hermes-agent | wihy/hermes-agent-skill | 493 | Hermes Agent |
| hermes-marketing-dashboard | aradotso/marketing-skills | 414 | Marketing APIs |
| hermes-agent-framework | aradotso/ai-agent-skills | 146 | Hermes Agent |
| hermes-agent-self-evolution | aradotso/ai-agent-skills | 130 | Hermes Agent |
| ppt-director | hermess/ppt-director | 84 | python-pptx |

*All install with `npx skills add <repo> --skill <skill-name>`.*

*← [Main Setup Guide](/hermes/skills/catalog/hermes-agent-nousresearch-full-setup/) | [Discovery Report](/hermes/skills/marketplace/new-june13-2026-update2/) →*

*Powered by CorpusIQ*
