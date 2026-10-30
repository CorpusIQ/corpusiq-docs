---
title: "components.build - UI Component Standards Setup"
description: "vercel/components.build: 14.8K combined installs. One skill that turns the components.build spec into rules for composable, accessible UI components."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/vercel-components-build-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "ui components", "design systems", "accessibility"]
---

# components.build - Setup Guide

**Source:** [vercel/components.build](https://www.skills.sh/vercel/components.build) via skills.sh - 14.8K combined installs across 1 indexed listing; first seen 2026-10-30 (morning sweep)

**GitHub:** [vercel/components.build](https://github.com/vercel/components.build) - 802 stars, Apache-2.0 in the repository LICENSE file while the GitHub API reports NOASSERTION, branch main, last pushed 2026-04-07; a single skill at `skills/building-components/SKILL.md` beside 15 `references/*.mdx` chapters, inside a Next.js and Fumadocs documentation site that carries the same specification in 19 language codes.

**Category:** UI component design standards and implementation rules

**Quality Tier:** 🟡 Beta - license field NOASSERTION rather than a standard OSI id; one mature, fully static specification skill with no bundled scripts and no network surface.

components.build is a formal specification for building modern UI components, published by Vercel and co-authored by Hayden Bleasel and shadcn. The specification itself is short and declarative: it sets out what a component library has to get right to be composable, accessible, customizable, performant, transparent and well documented, and it is framework-agnostic even though every example is React and TypeScript, which is why the README says the principles apply to Vue, Svelte and Angular as well.

For agents the interesting part is the packaging. Rather than twenty narrow skills, the repository ships one skill, `building-components`, whose `SKILL.md` is a router plus a fifteen-chapter reference library covering artifact taxonomy, principles, accessibility, composition, as-child, polymorphism, typing, state, data attributes, design tokens, styling, registry distribution, npm publishing, marketplaces and documentation. That structure is why one listing has drawn 14.8K installs: the skill is small enough to keep resident and deep enough to answer the specific question an agent actually has mid-build.

## Installation

The README documents no skills install path. There is no `npx skills add` example, no `plugin.json` and no skills CLI manifest in the tree, so the durable route for this profile is a directory copy from a clone:

```bash
git clone https://github.com/vercel/components.build.git
cp -R components.build/skills/building-components \
  ~/.hermes/profiles/corpusiq/skills/building-components
```

Copy the whole directory rather than the markdown alone. `SKILL.md` names each reference file by relative path, so a lone `SKILL.md` leaves the agent describing a chapter it cannot open. Nothing in the skill needs installing, building or running, and the surrounding Next.js site is only the documentation front end for the same content.

If you want to refresh the references later, the repository generates them from the docs source with `scripts/sync-skill-docs.sh`, which copies every non-localized `content/docs/*.mdx` except `index.mdx` into the skill directory and strips the `<Video />` components that would not render.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| building-components | 14,813 | The whole specification as one routing skill: artifact taxonomy (primitives, components, blocks, templates), core principles, ARIA and keyboard accessibility, composition, as-child and polymorphism, TypeScript typing, controlled and uncontrolled state, data attributes, design tokens, styling, shadcn-style registry distribution, npm publishing, marketplace distribution and component documentation, with fifteen reference chapters behind it. |

No indexed listings fall below the threshold; all 1 appear above.

## Why This Matters for Hermes Agents

An agent writing UI code optimises for whatever the framework template or the nearest example does, which is how a codebase ends up with five different opinions about where state lives and whether a wrapper should forward props. This specification gives the agent a shared vocabulary and a written rule for each decision, so its output can be reviewed against a named standard instead of taste.

The taxonomy chapter is the highest-leverage part for delegation, because most component mismatches are category errors. Deciding early whether an artifact is a primitive, a component, a block or a template fixes the API surface, the documentation depth and the distribution channel before any code is written.

The single-skill layout also fits how Hermes manages context. `SKILL.md` is about two kilobytes of routing text, and each chapter is opened only when a task reaches accessibility, composition, tokens or publishing, so the profile carries a standards document without paying for it on every turn.

Because the skill is pure markdown, it is safe to run in an unattended cron or subagent: there is nothing to execute, no credential to hold and no network call to make. What it changes is the quality of the diff, not the state of the system.

## Usage

| You say | What happens |
|---|---|
| "Build a combobox primitive we can theme later" | The skill classifies the artifact against `definitions.mdx` first, then uses `accessibility.mdx` for ARIA roles, keyboard navigation and focus handling and `state.mdx` to split controlled from uncontrolled behaviour before any implementation detail. |
| "Our Button needs to render as a link sometimes" | `as-child.mdx` and `polymorphism.mdx` lay out the slot-based as-child pattern against the polymorphic `as` prop, including the typing consequences of each, so the choice is made once rather than per call site. |
| "Should this be a prop or a data attribute?" | `data-attributes.mdx` proposes data attributes for visual state so styles can target selectors, keeping the public prop surface small and the states inspectable in the DOM. |
| "Set up design tokens for our component package" | `design-tokens.mdx` and `styling.mdx` cover token naming, layering and theming so consumers can restyle without forking, and where defaults belong. |
| "Ship this component to our internal registry" | `registry.mdx` covers shadcn-style distribution where source lands in the consumer's repository, `npm.mdx` covers the published package route, and `marketplaces.mdx` covers catalogue distribution, with the tradeoffs named. |
| "Review this component API before we publish it" | The skill walks `principles.mdx` and `composition.mdx` as a checklist: composability over configuration, prop naming, slot shape, escape hatches and whether the component can be understood from its own documentation. |
| "Write the docs for this component" | `docs.mdx` supplies the expected page structure, so examples, props, accessibility notes and customisation guidance arrive in the order a consumer reads them. |

## Verification

Both raw paths below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} skill\n" \
  https://raw.githubusercontent.com/vercel/components.build/main/skills/building-components/SKILL.md
curl -sL -o /dev/null -w "%{http_code} accessibility\n" \
  https://raw.githubusercontent.com/vercel/components.build/main/skills/building-components/references/accessibility.mdx
```

Expect `200` twice. Read the skill file before installing: its frontmatter is the routing contract, and here it is unusually complete, naming the trigger cases (new components, accessibility, composable APIs, design tokens, publishing, documentation) that decide whether the skill fires.

After the copy lands in the profile, confirm the frontmatter and that all fifteen chapters arrived:

```bash
head -3 ~/.hermes/profiles/corpusiq/skills/building-components/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/building-components/references/ | wc -l
```

The header should show `name: building-components` and a populated `description:`, and the count should print `15`. A copy that prints anything less has lost reference files that the router links to by relative path.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| building-components | Pass | Pass | Pass |

The skill is markdown plus MDX references and nothing else: no `scripts/` directory, no executable helper, no MCP endpoint, no credential and no outbound call. The install risk is therefore the ordinary prompt-level one, that guidance shapes generated code, rather than a code execution risk, which is a favourable profile for an unattended agent.

The one metadata item worth care is licensing. The repository LICENSE file is Apache-2.0, the README's own License section says MIT, and the GitHub API returns NOASSERTION because the field is not machine-resolvable. If you redistribute the text, read the LICENSE file in your clone and treat the README line as stale rather than authoritative, and confirm with the publisher before republishing the chapters in another product.

The surrounding Next.js application does carry a normal dependency tree, but it is only the docs front end. Nothing in the skill requires you to install or run it.

## Limitations

- Snapshot data, verified 2026-10-30: 14,813 combined installs across 1 indexed listing; 802 GitHub stars; Apache-2.0; last pushed 2026-04-07. Counts drift over time.
- A single indexed listing means there is nothing to rank. The 14.8K figure measures adoption of the specification as a whole, so it says nothing about which chapter of the fifteen is trusted or used, and it cannot be compared with install counts of per-skill collections.
- The license is unresolved across three sources. The LICENSE file is Apache-2.0, the README says MIT, and the GitHub API says NOASSERTION; the pack records the Apache-2.0 file and the NOASSERTION field. Verify before redistribution.
- The repository is a documentation site, not a component library. It ships no components to install and no linter to satisfy, so compliance with the specification is a review judgement and nothing enforces it.
- `references/*.mdx` are generated, not authored. `scripts/sync-skill-docs.sh` copies them out of `content/docs`, so an edit made in the skill directory is overwritten the next time the maintainers sync, and the same text exists in 304 translated files across 19 language codes.
- The README carries no install instructions of any kind, so there is no supported one-line install and no Claude Code plugin manifest. The copy route above is the only route, and it is manually maintained.

## Related

- [shadcn Skill - shadcn/ui Component Workflows Setup](/hermes/skills/catalog/shadcn-ui-setup)
- [Vercel Agent Skills - Official Vercel Collection Setup](/hermes/skills/catalog/vercel-agent-skills-setup)
- [Extract Design System - UI Token & Component Extraction Setup](/hermes/skills/catalog/extract-design-system-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the whole directory. The router names each of the fifteen chapters by relative path, and an agent that cannot open `accessibility.mdx` will improvise accessibility instead of following the standard.
- Point the skill at your own conventions rather than treating it as law. It is deliberate about distribution, typing and state, and largely silent about visual design, so let your tokens layer supply the aesthetics.
- Use it as the review gate, not the generator. A code-generation skill produces the component, and this one supplies the checklist that catches the category error, the leaking prop or the unreachable keyboard path.
- Edit `content/docs`, never `references/`. Regenerating with `scripts/sync-skill-docs.sh` overwrites the skill directory, and the source of truth is the docs page.
- Pin the commit you cloned. Last push was 2026-04-07, so the specification moves slowly, which makes a pinned copy easy to keep and easy to diff when you next refresh.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
