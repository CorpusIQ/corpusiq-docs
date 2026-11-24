---
title: "UI/UX Agent Skill System - Vendor-Neutral Skill Suite Setup"
description: "sergekostenchuk/ui-ux-agent-skill-system - 4.4K combined installs: a vendor-neutral UI/UX skill system with Codex, Claude and other agent adapters."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ui-ux-agent-skill-system-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "ui-ux", "design", "figma"]
---

# UI/UX Agent Skill System - Setup Guide

**Source:** [sergekostenchuk/ui-ux-agent-skill-system](https://www.skills.sh/sergekostenchuk/ui-ux-agent-skill-system) via skills.sh - 4.4K combined installs across 68 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 morning sweep)
**GitHub:** [sergekostenchuk/ui-ux-agent-skill-system](https://github.com/sergekostenchuk/ui-ux-agent-skill-system) - 37 stars, Apache-2.0, main branch, last pushed Sep 13, 2026; skills under core/skills/ with prebuilt per-runtime output under dist/ (codex, claude, qwen-code, copilot-vscode, gemini-cli, glm-zai, kimi, generic-agent).
**Category:** UI/UX Design and Frontend Skill System
**Quality Tier:** 🟠 Orange - ui-ux-pro-max carries a Fail cell (Gen Agent Trust Hub); several other sampled skills carry Snyk Warn.

This is sergekostenchuk's vendor-neutral UI/UX agent skill system, an orchestrated suite of 68 indexed skills spanning product UX architecture, Figma workflows, design intelligence, marketing sites, admin UI, SEO and LLM site structure, infrastructure and launch. A main control layer (senior-ui-ux-orchestrator as the central chair, task-plan-v2-orchestrator, workflow-compliance-supervisor and agent-progress-visualizer) routes work to specialist skills, and the repository ships prebuilt output folders for eight agent runtimes including Codex, Claude, Qwen Code, Copilot, Gemini CLI, GLM/Z.ai and Kimi.

The suite is notable for a flat install band: every indexed skill sits between 61 and 113 installs because a single install pulls the whole suite rather than individual skills. The Apache-2.0 repository is distributed as an npm CLI (@mlllm/ui-ux-agent-skill-system) alongside per-runtime dist folders, with docs/skill-map.md as the canonical skill list.

## Installation

The README documents an npm CLI plus per-runtime copy commands:

```bash
npm install -g @mlllm/ui-ux-agent-skill-system
uiux-skills list
uiux-skills install codex
```

Or with npx:

```bash
npx @mlllm/ui-ux-agent-skill-system install codex
```

The same CLI installs for other runtimes (qwen-code, copilot-vscode, claude, gemini-cli), with a destination override for Claude and Gemini. You can also copy a prebuilt dist folder directly, for example into a Claude skills directory:

```bash
cp -R dist/claude/skills/* /path/to/claude/skills/
```

The README recommends loading senior-ui-ux-orchestrator first unless the task names a specialist skill.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| webapp-ui-skill | 113 | building and auditing dense web app UI (SaaS dashboards, admin panels, tables, forms) |
| ux-audit-skill | 79 | auditing UI screens for UX, accessibility and responsive behavior |
| design-critic-skill | 79 | visual critique and design review against observable criteria |
| senior-ui-ux-orchestrator | 77 | the central chair routing UI/UX work to specialist skills |
| ui-ux-llm-product-architect | 75 | product UX architecture for sites, apps and design systems |
| admin-ui-builder | 72 | building admin and back-office screens (tables, forms, dashboards) |
| ui-ux-pro-max | 70 | searchable design intelligence across 67 UI styles and 15+ stacks |

The remaining 61 indexed listings range from 61 to 68 installs. The full catalogue is a flat band from 61 to 113 installs, because one install pulls the entire suite rather than individual skills.

## Why This Matters for Hermes Agents

This is a complete orchestration layer for UI and UX work, which matters because agents asked to build a polished dashboard or audit a landing page otherwise improvise. senior-ui-ux-orchestrator is a single entry point that routes to the right specialist, so an agent gets a consistent routing and evidence policy instead of ad hoc behavior. The Figma subsystem (senior-figma-orchestrator plus context-reader, design-to-code bridge, code-to-canvas, design-system sync and workflow auditor) covers the full design-to-code and back loop, the part most agents do badly without structured guidance. The SEO and LLM layer is a useful differentiator: information-architecture-seo, semantic-core-builder and technical-seo-schema-engineer treat a site as something both humans and LLMs must read. workflow-compliance-supervisor is worth attention on its own because it verifies that promised journeys, task plans and evidence artifacts actually line up, guarding against an agent claiming work it did not do. The tradeoff is scale: 68 skills with prebuilt output for eight runtimes is a lot to audit, and the flat install counts mean there is no per-skill popularity signal to guide selection.

## Usage

| You say | What happens |
|---|---|
| Build a premium landing page for a cottage village | senior-ui-ux-orchestrator routes to marketing-site-skill for the public page |
| Audit this dashboard screenshot and code | ux-audit-skill returns severity-ranked findings and an actionable fix plan |
| Critique this interface for visual polish | design-critic-skill reviews hierarchy, spacing, typography and contrast |
| Read this Figma frame and prepare a handoff | senior-figma-orchestrator maps the frame to code components |
| Build the admin screens for my back office | admin-ui-builder covers tables, forms, dashboards and CRUD surfaces |
| Check my project plan and evidence are consistent | workflow-compliance-supervisor validates the journey against artifacts |

## Verification

Confirm a core skill body resolves on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/sergekostenchuk/ui-ux-agent-skill-system/main/core/skills/webapp-ui-skill/SKILL.md | head -30
```

After an npm install, confirm the CLI is present and lists the bundled skills:

```bash
uiux-skills list
```

Then confirm the skills landed in the agent skills directory you targeted (for example ~/.claude/skills for Claude Code, or the dist/claude/skills projection).

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| webapp-ui-skill | Pass | Pass | Warn |
| ux-audit-skill | Pass | Pass | Warn |
| design-critic-skill | Pass | Pass | Pass |
| senior-ui-ux-orchestrator | Pass | Pass | Pass |
| ui-ux-llm-product-architect | Pass | Pass | Warn |
| admin-ui-builder | Pass | Pass | Pass |
| ui-ux-pro-max | Fail | Pass | Pass |
| ux-journey-architect | Pass | Pass | Pass |
| figma-design-system-sync | Pass | Pass | Pass |
| senior-figma-orchestrator | Pass | Pass | Pass |
| marketing-site-skill | Pass | Pass | Warn |
| figma-context-reader | Pass | Pass | Pass |
| figma-design-to-code-bridge | Pass | Pass | Pass |
| figma-workflow-auditor | Pass | Pass | Pass |
| workflow-compliance-supervisor | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 24, 2026: 4,379 combined installs across 68 indexed listings; 37 GitHub stars; Apache-2.0 license; last pushed Sep 13, 2026. Counts drift over time.
- Install counts are a flat band from 61 to 113 across all 68 listings, because one install pulls the whole suite; there is no per-skill popularity signal to guide selection.
- The install index ships no per-skill descriptions, so every Use For cell is grounded in the skill name and the core/skills SKILL.md descriptions only.
- The repository has not been pushed since Sep 13, 2026, so the suite is not seeing active maintenance at snapshot time.
- The optional Next Move Theory / AJTBD product-strategy source is not bundled under the Apache-2.0 license, so treat any connection to it as a separate integration boundary.

## Related

- [Cuellar Design Skills - UX and Design Skills Setup](/hermes/skills/catalog/cuellarfr-design-skills-setup)
- [Interface Design Skill - Non-Templated Product UI Setup](/hermes/skills/catalog/interface-design-skill-setup)
- [Bergside Design Skills - Design Systems Setup](/hermes/skills/catalog/bergside-awesome-design-skills-setup)
- [Apple Design Skill - HIG Review Across Frameworks](/hermes/skills/catalog/apple-design-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Load senior-ui-ux-orchestrator first; it is the single chair that routes to specialists and resolves conflicts.
- Install only the runtime projection you actually use (codex, claude, qwen-code, copilot-vscode, gemini-cli, glm-zai, kimi, or generic-agent) rather than all eight.
- Reach for webapp-ui-skill for dense app surfaces and marketing-site-skill for public pages; do not mix them.
- Run workflow-compliance-supervisor before declaring a UI task done, since it checks evidence artifacts against the plan.
- Check docs/skill-map.md for the canonical skill list when the index and the tree disagree.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
