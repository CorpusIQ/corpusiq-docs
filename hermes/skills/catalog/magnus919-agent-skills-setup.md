---
title: "Engineering Agent Skills - Product, QA and Governance"
description: "magnus919/agent-skills: 13.2K combined installs across 96 listings of engineering, product, QA and agent-governance workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/magnus919-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "software engineering", "qa", "agent governance", "observability"]
---

# Engineering Agent Skills - Setup Guide

**Source:** [magnus919/agent-skills](https://www.skills.sh/magnus919/agent-skills) via skills.sh - 13.2K combined installs across 96 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 evening sweep)

**GitHub:** 182 stars, MIT licence, main branch, last pushed Nov 20, 2026. Skills live as top-level `<name>/SKILL.md` directories at the repository root, with `.claude-plugin/`, `.codex-plugin/` and `.agents/` manifests, plus `references/`, `docs/` and a Ruby and Python `scripts/` validation layer.

**Category:** Software engineering and agent governance skill library

**Quality Tier:** 🟡 Yellow - 3 Warn and 0 Fail among the 16 sampled skills.sh verdicts (all three Warn cells sit in Snyk); MIT licence.

magnus919/agent-skills is a curated collection of agent skills in the open Agent Skills format, covering software engineering, product work, quality assurance, and the operational and governance questions that come up when agents do real work. Each skill is a folder with a `SKILL.md` playbook plus supporting references, templates and scripts, loaded on demand by any harness that supports the standard.

The repository is broader than the index suggests: the skills.sh listing caps at 96 rows, while the tree holds 188 top-level skill directories. Alongside the engineering skills it codifies patterns for making agents governable, observable and trustworthy, including evaluations, production operations, AI governance and multi-agent coordination.

## Installation

Install the full catalog for Hermes with the open skills CLI (requires Node.js 22.20+ and Git):

```bash
npx skills add magnus919/agent-skills --skill '*' --agent hermes-agent --global --yes
```

For other harnesses, swap the `--agent` value for codex, claude-code, opencode, github-copilot, cursor, gemini-cli or openclaw. Omit `--global` for a project-scoped install.

Alternatively mount the repository as an external skill directory in `~/.hermes/config.yaml`:

```bash
git clone https://github.com/magnus919/agent-skills.git "$HOME/agent-skills"
```

```yaml
skills:
  external_dirs:
    - ~/agent-skills
```

Or add it as a tap and cherry-pick individual skills:

```bash
hermes skills tap add magnus919/agent-skills
hermes skills search <query>
hermes skills install <skill-name>
```

Claude Code can also use the bundled plugin marketplace:

```
/plugin marketplace add magnus919/agent-skills
/plugin install cli-builder@magnus-agent-skills
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| product-design-and-ux | 272 | Define user-facing product behavior from evidence and approved scope |
| ffmpeg | 262 | Local media inspection, transcoding, filtering and cleanup |
| web-accessibility | 217 | Accessible web interfaces with WCAG 2.2-informed evidence |
| backend-engineering | 198 | Design and implement backend services and APIs |
| software-architecture | 190 | Design and review architectures from drivers to evolution |
| secure-software-engineering | 187 | Security requirements, threat modeling and secure defaults |
| qa-methodology | 184 | Test strategy, quality gates and agentic eval design |
| software-architecture-analysis | 177 | Reverse-engineer a system and map architecture, data flow and coupling |
| playwright | 175 | Browser automation, E2E tests and headless scraping |
| esp32-development | 165 | Build and flash firmware for ESP32-family boards |
| technical-documentation | 158 | READMEs, API references and agent-facing instructions |
| anydoc | 158 | Convert office documents, ebooks and PDFs to Markdown |
| frontend-engineering | 157 | Build and maintain web frontends, framework agnostic |
| docker-compose | 155 | Define, run, debug and harden multi-container apps |
| agent-evals-and-observability | 154 | Vendor-neutral evals and observability for AI agents |
| api-design-and-evolution | 150 | Design, govern and evolve consumer-facing APIs |
| adr-authoring | 149 | Preserve the reasoning behind consequential architecture choices |
| product-discovery | 146 | External problem evidence before committing to requirements |

The remaining 78 indexed listings range from 118 to 145 installs.

## Why This Matters for Hermes Agents

This is a reference collection for builders who want skills that carry boundaries, not just capabilities. Each skill states what it does and explicitly routes unrelated requests to a neighboring specialist, which is what keeps a large skill library from turning into a pile of overlapping instructions that fight each other at routing time.

The governance layer is the most reusable part. Skills such as ai-governance, agent-evals-and-observability and agent-production-operations encode scoped earned-autonomy decisions, release gates, and monitor independence as reusable playbooks, so the question of whether an agent may act becomes a documented process instead of an ad hoc judgment.

The engineering coverage is broad enough to serve as a baseline for a general-purpose agent: backend, frontend, architecture, QA, security, documentation and API design all have dedicated skills, so a single checkout can cover most of a software delivery lifecycle.

## Usage

| You say | What happens |
|---|---|
| "Plan the implementation of this approved spec" | The implementation-planning skill lays out dependencies and verification steps |
| "Review this pull request" | An evidence-backed change review is produced without implementing the fix |
| "Why did this agent fail, and may it resume?" | Failure diagnosis, containment and renewed authority are handled as separate decisions |
| "Is this customer problem worth building?" | product-discovery gathers external evidence before any requirement is written |
| "Define this feature's UX" | product-design-and-ux specifies behavior, state and recovery models |
| "Check this page for WCAG issues" | web-accessibility reviews semantics, keyboard, focus and motion against WCAG 2.2 |

## Verification

Confirm the skills land in your harness's discovery directory (for Hermes, the tap installs into `~/.hermes/skills/`, and a mounted checkout makes every top-level folder available next session). To review one skill before relying on it, fetch its definition directly:

```bash
curl -sL https://raw.githubusercontent.com/magnus919/agent-skills/main/product-design-and-ux/SKILL.md
```

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| product-design-and-ux | Pass | Pass | Warn |
| ffmpeg | Pass | Pass | Pass |
| web-accessibility | Pass | Pass | Pass |
| backend-engineering | Pass | Pass | Pass |
| software-architecture | Pass | Pass | Pass |
| secure-software-engineering | Pass | Pass | Pass |
| qa-methodology | Pass | Pass | Pass |
| software-architecture-analysis | Pass | Pass | Warn |
| playwright | Pass | Pass | Warn |
| esp32-development | Pass | Pass | Pass |
| technical-documentation | Pass | Pass | Pass |
| anydoc | Pass | Pass | Pass |
| frontend-engineering | Pass | Pass | Pass |
| docker-compose | Pass | Pass | Pass |
| agent-evals-and-observability | Pass | Pass | Pass |
| api-design-and-evolution | Pass | Pass | Pass |

No sampled skill fails a verdict. Three carry a single Warn in Snyk: product-design-and-ux, software-architecture-analysis and playwright.

## Limitations

- Snapshot data, verified Nov 19, 2026: 13,218 combined installs across 96 indexed listings; 182 GitHub stars; MIT licence; last pushed Nov 20, 2026. Counts drift over time.
- The 96-row skills.sh API cap means both the listing count and the combined install figure are floors, not totals. The repository tree holds 188 top-level skill directories, far more than the index surfaces.
- Install counts reflect skills.sh telemetry, not downloads of this repository alone, so they trail actual usage.
- Skills follow the open Agent Skills format, but each harness controls discovery, activation and update behavior; installing the files alone does not always activate them.
- Several skills assume external runtimes or accounts (anydoc runs a local CLI, playwright drives a browser, agent-council is a pip package), so review each skill's tool and dependency requirements before use.

## Related

- [Agentic Awesome Skills - 2,000+ Skill Catalog Setup](/hermes/skills/catalog/agentic-awesome-skills-setup)
- [Alireza Rezvani Claude Skills - 341 Engineering & Marketing Skills Setup](/hermes/skills/catalog/alirezarezvani-claude-skills-setup)
- [Awesome AI Agent Skills - 103-Skill Agent Library](/hermes/skills/catalog/awesome-ai-agent-skills-setup)
- [AI Agent Skills - Skill Package Manager and Library](/hermes/skills/catalog/ai-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Keep the quotes around `'*'` so your shell passes the wildcard to the CLI rather than expanding it.
- For Hermes, keep `--global` on the full-catalog install: its project-scoped `.hermes/skills/` target is not auto-discovered.
- Refresh weekly by rerunning your harness's full-catalog command, then start a new agent session.
- Install one method per harness; mixing a CLI install with a mounted checkout duplicates skills.
- Use the "Find a workflow" table in the README to pick a starting skill from the job you actually have.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
