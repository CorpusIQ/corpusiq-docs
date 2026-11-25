---
title: "WordPress Agent Skills - Audit and Optimize Setup"
description: "respira-press/agent-skills-wordpress - 5.5K combined installs across 56 indexed listings: audit, optimize, fix and migrate WordPress sites."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agent-skills-wordpress-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "wordpress", "woocommerce"]
---

# WordPress Agent Skills - Setup Guide

**Source:** [respira-press/agent-skills-wordpress](https://www.skills.sh/respira-press/agent-skills-wordpress) via skills.sh - 5.5K combined installs across 56 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 morning sweep)
**GitHub:** [respira-press/agent-skills-wordpress](https://github.com/respira-press/agent-skills-wordpress) - 51 stars, MIT license, last pushed Oct 18, 2026, main branch; 55 skills under skills/<name>/SKILL.md plus wordpress-mcp-dev at the repo root.
**Category:** WordPress (Audit, Optimization, Migration)
**Quality Tier:** 🟡 Yellow - six sampled skills carry a Snyk Warn (figma-to-elementor, content-portability, html-to-bricks, prime-the-agent, migrate-elementor-to-gutenberg, migrate-elementor-to-oxygen); the other 9 sampled skills pass all checks.

respira-press/agent-skills-wordpress is a community hub of agent skills for auditing, optimizing, fixing, and migrating WordPress sites, curated by Respira. The skills run inside Claude Code, Codex, Antigravity, Cursor, and any agent that supports Skills plus MCP, and they pair with Respira's plugin to give the agent deep site access through over 220 MCP tools (over 330 with the WooCommerce add-on). The 56 indexed listings span onboarding, audit, editing safety, content and migration work, and a large family of builder-to-builder migrations.

The README lists 55 skills (catalog version 1.16.1) generated from skills.json; the 56th indexed listing, wordpress-mcp-dev, lives at the repo root rather than under skills/ and covers building WordPress plugins and MCP servers. Install counts are tightly clustered around 100 because the skills ship as one catalog.

## Installation

npx skills (recommended) works with Claude Code, OpenCode, Codex, and anything else that reads the Skills format:

```bash
# Install every skill globally
npx skills add respira-press/agent-skills-wordpress -g -a claude-code -y

# Or into the current project only
npx skills add respira-press/agent-skills-wordpress -a claude-code -y

# Update later
npx skills update -g
```

Swap -a claude-code for your agent, for example -a opencode. Installing writes a lock file recording each skill's source, skillPath, and content hash. If you run the Respira plugin, the Skills screen in wp-admin installs and updates these without a terminal. Manual install:

```bash
git clone https://github.com/respira-press/agent-skills-wordpress
cp -r agent-skills-wordpress/skills/* ~/.claude/skills/
```

## What It Provides

skills.sh publishes per-skill descriptions, and each indexed listing maps to a skills/<name>/SKILL.md in the tree (wordpress-mcp-dev lives at the repo root instead).

| Skill | Installs | Use For |
|---|---|---|
| site-onboarding | 120 | first-run primer: verify connectivity, discover site architecture, map tools |
| page-template-library | 119 | capture canonical page patterns as reusable playbooks |
| figma-to-elementor | 119 | rebuild a Figma frame as an Elementor page, writing to a draft |
| custom-post-type-architect | 119 | create a CPT plus taxonomies, ACF field group, samples, and template |
| content-portability | 119 | export pages and posts to portable packages and re-import with ID remapping |
| html-to-bricks | 118 | convert raw HTML/CSS into native Bricks elements with token mapping |
| conversion-audit | 117 | score conversion friction across six dimensions with prioritized fixes |
| activity-report-composer | 117 | turn the audit log into a client report in six framings |
| wordpress-mcp-dev | 116 | build and maintain WordPress plugins and MCP servers |
| prime-the-agent | 115 | session starter: load site, detect builder, enforce no-raw-HTML |
| stale-content-detector | 114 | categorize pages as fresh, aging, stale, or due for archive |
| migrate-elementor-to-gutenberg | 111 | map Elementor widgets to core blocks, draft duplicates for review |
| technical-debt-audit | 110 | find orphaned shortcodes, unused plugins, database bloat, unused media |
| seo-aeo-amplifier | 110 | on-page SEO and AEO audit with schema markup and draft fixes |

The remaining 42 indexed listings range from 36 to 109 installs.

## Why This Matters for Hermes Agents

For a Hermes agent doing WordPress work, these skills replace generic best-practices guidance with site-aware workflows backed by Respira's MCP tools (220 tools, 330 with the WooCommerce add-on). The suite is deliberately safety-first: live pages go through a draft duplicate a person approves, every write is verified, and a failed write is read before retry, so the agent can act on a production site without treating it as a scratch space. The migration family is the standout: skills that move pages between Elementor, Divi, Bricks, Gutenberg, Oxygen, Breakdance, WPBakery, and Beaver Builder, each mapping widgets to native elements and staging draft duplicates for review. For a builder, dropping these in means "audit my site" resolves to concrete technical-debt, conversion, SEO, and performance passes rather than a hand-wavy summary. The main caveat is vendor coupling: many skills assume the Respira plugin and MCP server, and the WooCommerce skills require a paid add-on.

## Usage

| You say | What happens |
|---|---|
| Audit my site for technical debt | Uses technical-debt-audit to find shortcodes, bloat, and unused plugins |
| Migrate this Elementor page to Gutenberg | Uses migrate-elementor-to-gutenberg to map widgets to core blocks |
| Build this Figma design in Bricks | Uses figma-to-bricks to rebuild the frame as a Bricks page |
| Find stale content to refresh | Uses stale-content-detector to categorize pages by age and traffic |
| Make my store AI-discoverable | Uses woo-agent-storefront to set up feeds and a store llms.txt |
| Turn my audit log into a client report | Uses activity-report-composer with one of six framings |

## Verification

Confirm representative skill bodies resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/respira-press/agent-skills-wordpress/main/skills/site-onboarding/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/respira-press/agent-skills-wordpress/main/wordpress-mcp-dev/SKILL.md | head -40
```

Both URLs return 200. Note wordpress-mcp-dev lives at the repo root rather than under skills/. Review each skills/<name>/SKILL.md before use; skills.json is the generated catalog listing every skill.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| site-onboarding | Pass | Pass | Pass |
| page-template-library | Pass | Pass | Pass |
| figma-to-elementor | Pass | Pass | Warn |
| custom-post-type-architect | Pass | Pass | Pass |
| content-portability | Pass | Pass | Warn |
| html-to-bricks | Pass | Pass | Warn |
| conversion-audit | Pass | Pass | Pass |
| activity-report-composer | Pass | Pass | Pass |
| wordpress-mcp-dev | Pass | Pass | Pass |
| prime-the-agent | Pass | Pass | Warn |
| stale-content-detector | Pass | Pass | Pass |
| migrate-elementor-to-gutenberg | Pass | Pass | Warn |
| technical-debt-audit | Pass | Pass | Pass |
| seo-aeo-amplifier | Pass | Pass | Pass |
| migrate-elementor-to-oxygen | Pass | Pass | Warn |

15 of 56 listings were sampled. 9 pass all three checks; the other 6 carry a Snyk Warn.

## Limitations

- Snapshot data, verified Nov 25, 2026: 5,523 combined installs across 56 indexed listings; 51 GitHub stars; MIT license; last pushed Oct 18, 2026. Counts drift over time.
- The README lists 55 skills generated from skills.json; the 56th indexed listing, wordpress-mcp-dev, lives at the repo root and is absent from that list.
- Many skills assume the Respira plugin and MCP server, and the WooCommerce skills require the paid WooCommerce add-on.
- Install counts are tightly clustered around 100 because the skills ship as one catalog; individual counts are not a strong signal of per-skill quality.
- The repo has not been pushed since Oct 18, 2026, so the skills may lag recent WordPress or builder releases.
- The Respira MCP server exposes deep site access, so keep the editing-safety and approval flow in place before letting an agent write to a live site.

## Related

[WordPress Agent Skills - Official WP Development Setup](/hermes/skills/catalog/wordpress-agent-skills-setup) | [Automattic Agent Skills - WordPress Development Setup](/hermes/skills/catalog/automattic-agent-skills-setup) | [Gohypergiant Agent Skills - Engineering Collection](/hermes/skills/catalog/agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install globally with npx skills add respira-press/agent-skills-wordpress -g -a claude-code -y, then npx skills update -g to refresh.
- Run site-onboarding and prime-the-agent first so the agent knows the builder, plugins, and architecture before editing.
- Let migrations write to draft duplicates and keep the approval flow on for live pages.
- Read skills.json for the full catalog and each skill's SKILL.md before relying on it.
- Pair technical-debt-audit, conversion-audit, and seo-aeo-amplifier for a single comprehensive site review.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
