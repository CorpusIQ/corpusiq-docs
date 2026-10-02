---
title: "Sep 30, 2026 Morning - 8 New Skill Publisher Clusters"
description: "Skills.sh sweep: 8 new publisher guides (Official Google Gemini 47.8K, Assistant UI 89.5K, Dot Skills 30.6K, Claude MPM 26.1K, Meta Quest)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-sep30-2026-skills/"
robots: "index,follow"
last_updated: "2026-09-30"
tags: ["hermes skill", "skill marketplace", "skills.sh"]
---

# Sep 30, 2026 (Morning) - 8 New Skill Publisher Clusters

**Discovered:** 8 new publisher guides (282 skills, ~209K combined installs) - **Roster reconciles:** 1 (Angular deprecated alias)

Morning sweep of the skills.sh REST API across 15 queries (one-pass ripgrep cross-reference on the Mac Mini, ~2 min). 715 unique skills collected, 0 failed queries. Tiered crossref: 32 NEW / 214 PARTIAL. NEW >=100 installs: 9 sources; one of them (analogjs/angular-skills) resolved as a deprecated alias of the already-documented angular/skills, leaving 8 new guides plus 1 stale-name roster note.

## New Publishers at a Glance

| # | Publisher | Top Skill | Installs | Category | Setup Guide |
|---|-----------|-----------|----------|----------|-------------|
| 1 | google-gemini/gemini-skills | gemini-api-dev | 22,386 | AI Development / Gemini | [Guide](/hermes/skills/catalog/gemini-skills-setup) |
| 2 | assistant-ui/skills | assistant-ui | 6,599 | AI Chat UI | [Guide](/hermes/skills/catalog/assistant-ui-skills-setup) |
| 3 | pproenca/dot-skills | zod | 6,564 | Agent Engineering Collection | [Guide](/hermes/skills/catalog/dot-skills-setup) |
| 4 | bobmatnyc/claude-mpm-skills | drizzle | 4,381 | Dev Toolchains | [Guide](/hermes/skills/catalog/claude-mpm-skills-setup) |
| 5 | jamesrochabrun/skills | prd-generator | 1,174 | Creative / Product | [Guide](/hermes/skills/catalog/jamesrochabrun-skills-setup) |
| 6 | gbsoss/skill-from-masters | skill-from-masters | 754 | Skill Authoring | [Guide](/hermes/skills/catalog/skill-from-masters-setup) |
| 7 | linhay/harmony-next.skills | harmony-next | 320 | HarmonyOS NEXT | [Guide](/hermes/skills/catalog/harmony-next-skills-setup) |
| 8 | meta-quest/agentic-tools | portal | 258 | VR Development | [Guide](/hermes/skills/catalog/meta-quest-agentic-tools-setup) |

## Setup Guides Created

1. **[Gemini Skills Setup](/hermes/skills/catalog/gemini-skills-setup)** - official Google skills for Gemini API, Live API, Omni Flash, and Vertex AI (5 skills, 47.8K combined). 4,231 stars, Apache-2.0. The sweep's largest official find. \U0001f7e2 Production.
2. **[Assistant UI Skills Setup](/hermes/skills/catalog/assistant-ui-skills-setup)** - 17 skills for building AI chat interfaces (89.5K combined installs). Official assistant-ui org. \U0001f7e1 Beta, no LICENSE file disclosed.
3. **[Dot Skills Setup](/hermes/skills/catalog/dot-skills-setup)** - 96 skills in the open Agent Skills format (30.6K combined): Zod, Vitest, React Hook Form, clean architecture. MIT. \U0001f7e1 Beta.
4. **[Claude MPM Skills Setup](/hermes/skills/catalog/claude-mpm-skills-setup)** - 96 skills with progressive loading and toolchain detection (26.1K combined): Drizzle, Playwright, tRPC, LangChain. MIT. \U0001f7e1 Beta.
5. **[James Rochabrun Skills Setup](/hermes/skills/catalog/jamesrochabrun-skills-setup)** - 24 creative, product, and teaching skills (7.4K combined): PRD generator, Apple HIG designer, book writing. MIT. \U0001f535 Community.
6. **[Skill From Masters Setup](/hermes/skills/catalog/skill-from-masters-setup)** - 4 skills that convert proven expert methodologies into reusable skills (2.1K combined). 1,586 stars, MIT. \U0001f535 Community.
7. **[Meta Quest Agentic Tools Setup](/hermes/skills/catalog/meta-quest-agentic-tools-setup)** - 39 official Meta skills for Quest and Horizon OS VR development (5.4K combined). Apache-2.0. \U0001f7e1 Beta.
8. **[Harmony Next Skills Setup](/hermes/skills/catalog/harmony-next-skills-setup)** - offline HarmonyOS NEXT developer skill library for AI coding assistants (320 installs). 357 stars, no LICENSE file. \U0001f535 Community.

## Roster Reconcile

- **Angular Skills** - the deprecated analogjs/angular-skills repo (591 stars, ~63K combined across 10 listings) carries a DEPRECATED banner pointing to angular/skills, already documented. Stale-name note added to [Angular Skills Setup](/hermes/skills/catalog/angular-skills-setup) so the sweep cross-reference treats it as covered.

## Skipped / Parks

| Item | Reason parked |
|---|---|
| 23 NEW below floor (<100 installs, max 22) | Below the 100-install guide threshold (standing rule) |
| costrict-plugins-repo Odoo bundle (8 listings, 1 install each) | Below floor + plugin-bundle mirror pattern |
| satnamrsm/https-github.com-sickn33-... (2 listings, 1 install each) | Mirror-copy source names, below floor |

**Reconcile backlog:** 96 PARTIAL rows >=100 installs remain across documented publisher families. Deferred to a dedicated roster-reconcile pass; no new guides required.

## Quick Install

```bash
npx skills add google-gemini/gemini-skills
npx skills add assistant-ui/skills
npx skills add pproenca/dot-skills
npx skills add bobmatnyc/claude-mpm-skills
npx skills add jamesrochabrun/skills
npx skills add gbsoss/skill-from-masters
npx skills add meta-quest/agentic-tools
npx skills add linhay/harmony-next.skills
```

## Why This Matters for Hermes

**Google Gemini Skills** is the sweep's flagship: official, Apache-2.0, 4.2K stars, covering Gemini API, the realtime Live API, Omni Flash, and Vertex AI. **Assistant UI** (89.5K installs) is the strongest frontend suite for AI chat interfaces. **Dot Skills** and **Claude MPM** are the two deepest general collections this cycle (96 skills each), with toolchain detection and progressive loading respectively. **Skill From Masters** offers a reusable methodology-extraction pattern that aligns directly with how CorpusIQ converts operator expertise into catalog content. **Meta Quest** opens VR development to agents for the first time in this catalog.

*\u2190 [Skills Marketplace](/hermes/skills/marketplace) | [Skills Catalog](/hermes/skills/catalog) \u2192*
*Powered by CorpusIQ*
