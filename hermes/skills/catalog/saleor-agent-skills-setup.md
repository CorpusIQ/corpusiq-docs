---
title: "Saleor Agent Skills - Ecommerce Development Setup"
description: "saleor/agent-skills - 3.9K combined installs: framework-agnostic Saleor skills for building storefronts, apps and backend work."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/saleor-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "saleor", "ecommerce", "graphql"]
---

# Saleor Agent Skills - Setup Guide

**Source:** [saleor/agent-skills](https://www.skills.sh/saleor/agent-skills) via skills.sh - 3.9K combined installs across 5 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 evening sweep)
**GitHub:** [saleor/agent-skills](https://github.com/saleor/agent-skills) - 2 stars, BSD-3-Clause AND CC-BY-4.0 per the README (GitHub metadata reports NOASSERTION), last pushed Aug 6, 2026; each skill lives under skills/<name>/ with a SKILL.md, an AGENTS.md or README, and rules/ plus references/ files.
**Category:** Ecommerce Development
**Quality Tier:** 🟡 Yellow - all 5 sampled skills pass Gen Agent Trust Hub and Socket; saleor-storefront, saleor-app and saleor-core carry Warn cells on Snyk.

saleor/agent-skills publishes universal agent skills for building e-commerce applications on Saleor. The suite is framework-agnostic: the storefront and app skills ship Next.js examples but the patterns apply to any Saleor deployment, and each skill follows the Agent Skills Specification with a SKILL.md quick reference, compiled rules, and references deep dives.

The skills.sh index lists 5 listings at 3.9K combined installs. Four skills are documented in the README's Available Skills table (saleor-app, saleor-configurator, saleor-core, saleor-storefront), while storefront-builder has a SKILL.md in the tree but no row in the README's skill list or install command.

## Installation

The README installs a specific skill with npx skills:

```bash
npx skills add saleor/agent-skills --skill <skill-name>
```

Where <skill-name> is one of saleor-app, saleor-configurator, saleor-core or saleor-storefront (storefront-builder is not named in the README's install list). This drops the skill into .agents/skills/ in your project, where AI agents auto-discover it.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| saleor-storefront | 2,258 | Saleor e-commerce API patterns for building storefronts: GraphQL, products, variants, checkout, channels, permissions |
| saleor-app | 432 | Saleor app development patterns: protocol manifest, registration, webhooks, authentication, payments, Dashboard integration |
| saleor-core | 420 | Saleor backend internals: discount precedence, order discount allocation, stock availability modes, migration footguns |
| saleor-configurator | 409 | managing store configuration as code via config.yml and the deploy/introspect/diff commands |
| storefront-builder | 386 | storefront data and UX playbook: GraphQL query design, channel handling, variant-selection UX |

All 5 indexed listings clear the 1-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Saleor is a GraphQL-first headless commerce platform, and its domain rules (discount precedence, order discount allocation, stock availability modes, checkout lifecycle) are subtle enough that a general-purpose agent gets them wrong without a reference. These skills encode that knowledge as instructions an agent loads on demand, so a Hermes agent building a storefront or an app starts from the correct model instead of guessing at the API. The suite is framework-agnostic, which means the storefront and app patterns transfer to any stack, not just the Next.js examples the docs carry. Each skill is structured per the Agent Skills Specification (SKILL.md plus rules/ and references/), so the layering is portable to other agents too. The configurator skill is the notable one for platform operators: it turns store configuration into code (config.yml with deploy/introspect/diff), a pattern worth studying for any configuration-as-code workflow. Adoption is cheap: one npx command per skill, with no MCP server or token required.

## Usage

| You say | What happens |
|---|---|
| Build me a storefront against Saleor | Uses saleor-storefront to apply the GraphQL API patterns for products, variants, checkout and channels |
| I need to build a Saleor app with webhooks | Uses saleor-app for the app protocol: manifest, registration, webhooks and authentication |
| Explain Saleor discount precedence | Uses saleor-core for backend internals on discount stacking and order discount allocation |
| Manage my store config as code | Uses saleor-configurator for config.yml and the deploy/introspect/diff commands |
| Design the storefront data contracts | Uses storefront-builder for the PLP/PDP/nav/pricing/availability data contracts and variant-selection UX |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/saleor/agent-skills/main/README.md | head -40
```

Confirm a representative skill body before installing:

```bash
curl -sL https://raw.githubusercontent.com/saleor/agent-skills/main/skills/saleor-storefront/SKILL.md | head -30
```

The skills install into .agents/skills/ in your project; confirm that folder exists after running the npx command.

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| saleor-storefront | Pass | Pass | Warn |
| saleor-app | Pass | Pass | Warn |
| saleor-core | Pass | Pass | Warn |
| saleor-configurator | Pass | Pass | Pass |
| storefront-builder | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 24, 2026: 3,905 combined installs across 5 indexed listings; 2 GitHub stars; BSD-3-Clause AND CC-BY-4.0 per the README (GitHub metadata reports NOASSERTION); last pushed Aug 6, 2026. Counts drift over time.
- The license is ambiguous: the README states BSD-3-Clause AND CC-BY-4.0 while GitHub metadata reports NOASSERTION. Review both before redistribution.
- The README and the tree drift: storefront-builder carries an install count and a SKILL.md in the tree but is absent from the README's Available Skills table and install command list.
- The repo is small and low-activity (2 stars, last pushed Aug 6, 2026), so treat it as a young, lightly maintained suite.
- No MCP server or external service is required, but the skills reference Saleor's own API surface, so accuracy depends on the Saleor version you target.

## Related

- [Medusa Agent Skills - Official Ecommerce Platform Setup](/hermes/skills/catalog/medusa-agent-skills-setup)
- [Next.js 16 Agent Skills - Migration and Framework Setup](/hermes/skills/catalog/nextjs16-agent-skills-setup)
- [Supabase Server Skill - Edge Function Auth Setup](/hermes/skills/catalog/supabase-server-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install only the skill you need, for example npx skills add saleor/agent-skills --skill saleor-storefront, and read that skill's own README for its exact install command.
- Treat storefront-builder as available in the tree even though the README's skill list omits it; its SKILL.md sits at skills/storefront-builder/SKILL.md.
- Read each SKILL.md before relying on it; the rules/ and references/ files carry the detailed examples the SKILL.md only summarizes.
- Use saleor-configurator if you want configuration-as-code for a Saleor store; its deploy/introspect/diff workflow is the fastest path to reproducible store config.
- Pair saleor-storefront and storefront-builder when building a storefront: one covers the API patterns, the other the data contracts and UX rules.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
