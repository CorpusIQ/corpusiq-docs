---
title: "CrewAI Skills - Official Agent Design Suite Setup"
description: "Setup guide for crewAIInc/skills - 4 official CrewAI skills for AI agents: scaffolding, agent design, task design, and docs lookup. ~29.7K installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/crewai-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-04"
tags: ["hermes skill", "agent skill", "skill setup", "crewai", "agent framework", "multi-agent"]
---

# CrewAI Skills - Setup Guide

**Source:** [crewAIInc/skills](https://github.com/crewAIInc/skills) (44⭐, no LICENSE file; last push Jun 16, 2026)
**Skill family:** `crewAIInc/skills` (4 SKILL.md files in-repo; 4 indexed listings)
**Publisher:** CrewAI (crewAIInc) - the team behind the [CrewAI framework](https://github.com/crewAIInc/crewAI) (59.3K⭐)
**Category:** AI Agent Frameworks / Agent Design
**Quality Tier:** 🟡 Beta (official publisher; low repo stars, no LICENSE file, and no upstream pushes since Jun 16, 2026 - verify terms before production reliance; verified Oct 4, 2026)

Four official skills that teach AI coding agents how to build with CrewAI, the role-playing multi-agent framework. The set covers architecture decisions and project scaffolding (getting-started), agent configuration (design-agent), task design (design-task), and a live documentation lookup (ask-docs). Each skill ships extra reference files for progressive disclosure, and the repo registers a Claude Code plugin marketplace alongside the standard Agent Skills layout used by Hermes.

---

## Installation

```bash
# Full suite
npx skills add crewAIInc/skills

# Or install a single skill
npx skills add crewAIInc/skills --skill design-agent
```

Claude Code also supports the repo's built-in plugin marketplace:

```
/plugin marketplace add crewAIInc/skills
/plugin install crewai-skills@crewai-plugins
```

## Roster - All 4 Skills

| Skill | Installs | Does |
|---|---|---|
| getting-started | 7,521 | Architecture decisions + scaffolding: when to use LLM.call / Agent.kickoff / Crew.kickoff / Flow, `crewai create flow`, YAML config (agents.yaml, tasks.yaml), @CrewBase wiring, @start / @listen Flows, conversational Flows, variable interpolation |
| design-agent | 7,469 | Agent design: Role-Goal-Backstory framework, LLM selection, tool assignment, execution tuning (max_iter, max_rpm, max_execution_time), memory + knowledge sources, guardrails, YAML vs code config |
| ask-docs | 7,350 | Documentation lookup: queries the official docs at docs.crewai.com for API details, advanced features, troubleshooting, enterprise features, and tool references beyond the other three skills |
| design-task | 7,326 | Task design: descriptions + expected_output, context dependencies, structured output (output_pydantic / output_json / output_file), guardrails, human-in-the-loop review, async execution |

Reference files: `getting-started` ships conversational-flows / flow-routing / mcp-servers / tools-catalog; `design-agent` ships custom-tools + memory-and-knowledge; `design-task` ships structured-output.

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Agent architecture reference** | The getting-started decision tree (call vs kickoff vs flow) is a compact framework for scoping multi-agent builds, including CorpusIQ's own automations |
| **Skill authoring pattern** | The family is a clean reference implementation of progressive disclosure (main SKILL.md + `references/`) and multi-host packaging (`.claude-plugin` marketplace + portable Agent Skills layout) |
| **Agent config checklists** | design-agent / design-task work as ready-made review checklists for any CrewAI-style setup: role clarity, tool scoping, output schemas, guardrails |

## Limitations / Verification

- Verified Oct 4, 2026: 4 indexed listings on skills.sh; 4 SKILL.md files confirmed via the GitHub trees API (branch `main`); ~29,666 combined installs.
- No LICENSE file in the repo (GitHub license API returns 404, checked Oct 4, 2026) - confirm terms before commercial use.
- The skills repo is small (44⭐, 20 forks) next to the main CrewAI framework repo (59.3K⭐); last upstream push Jun 16, 2026.
- The skills teach CrewAI project patterns rather than running standalone tasks; `ask-docs` needs access to docs.crewai.com.
- No live install test performed; install counts are from the Oct 4, 2026 sweep snapshot.

## Security

skills.sh security verdicts (verified Oct 4, 2026) - all four skills pass all three checks:

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Pass |
| Socket | Pass |
| Snyk | Pass |

## Related

- [Hermes Agent Official Skills - Bundled Batch Setup](/hermes/skills/catalog/hermes-agent-official-skills-batch-setup)
- [Skills Catalog](/hermes/skills/catalog)
- [Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
