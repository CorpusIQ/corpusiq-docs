---
title: "Layers Skills - Design System Agent Pack"
description: "jamiemill/layers-skills: 17.8K combined installs. Nine design skills that walk a product through seven layers of product design."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/layers-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "product design", "design system", "ux"]
---

# Layers Skills - Setup Guide

**Source:** [jamiemill/layers-skills](https://www.skills.sh/jamiemill/layers-skills) via skills.sh - 17.8K combined installs across 18 indexed listings; first seen 2026-10-31 (evening sweep)

**GitHub:** [jamiemill/layers-skills](https://github.com/jamiemill/layers-skills) - 314 stars, MIT, branch main, last pushed 2026-05-30; 9 `SKILL.md` files, one per directory under `skills/`, each a single markdown file with no `references/` folder, and a 59-line README that is the only documentation

**Category:** Design system work for agents: layered UI components, tokens and documentation-first patterns

**Quality Tier:** 🟢 Green - every sampled verdict is a Pass on Gen Agent Trust Hub, Socket and Snyk, and the repository is MIT

This is a small, disciplined pack: nine skills that encode a framework for product design rather than a pile of component recipes. The framework has seven layers, three in the problem space (observed behaviour, the domain, user needs) and four in the solution space (product and service strategy, conceptual model, interaction structure and flow, surface), plus an introduction and a diagnostic that audits all seven at once. Lower layers are treated as foundations, so weak work at the bottom shows up as UX debt further up.

Each skill does the same three things at its own layer: explains the layer's nature, names the decisions that have to be made there, and offers a structured working session using a named method. The outputs are concrete rather than stylistic. The domain layer produces a concept map, terminology conflicts and a noun harvest. The interaction layer produces a breadboard with edge cases and open decisions. The surface layer produces audit findings and a decision inventory. For an agent that is usually asked to "make this page better", that is a different and more useful question.

## Installation

The README documents no install command at all. There is no skills CLI line, no plugin manifest and no clone step in the repository: it tells the reader to load `/layers-intro` at the start of a session and then either run `/layers-orient` or jump to the layer in question. That convention comes from the author's own working setup, so treat the clone and copy below as the Hermes route rather than something the project ships:

```bash
git clone --depth 1 https://github.com/jamiemill/layers-skills.git /tmp/layers-skills
cp -r /tmp/layers-skills/skills/. ~/.hermes/profiles/corpusiq/skills/
```

Because no CLI or marketplace route is documented for this repo, `npx skills add` is not available here and there is nothing to add to a plugin market. The copy is the install, and it is small: nine directories, nine markdown files, no scripts, no dependencies and nothing to build.

The one behavioural instruction worth carrying over from the README is the load order. `layers-intro` supplies the framework context that the other eight depend on, so it should be loaded first in any session that uses the pack, and `layers-orient` is the entry point when the question is "where should we be working" rather than "work on this layer".

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| layers-conceptual-model | 2,002 | Defining the product's objects, relationships, states and vocabulary independently of any interface: object maps, state diagrams and a ubiquitous language. |
| layers-intro | 1,983 | Framework orientation for the seven layers; the skill the other eight assume has been loaded, and the place to start a session. |
| layers-interaction-flow | 1,978 | Mapping interaction structure without committing to visual form: places, affordances, edge cases and failure paths, output as a breadboard. |
| layers-surface | 1,975 | Auditing the surface against the layers beneath it: vocabulary, object consistency, completeness, feedback, hierarchy and accessibility. |
| layers-product-strategy | 1,975 | Connecting user opportunities to business outcomes and solution bets, with cheap tests for the riskiest assumptions and an Opportunity Solution Tree. |
| layers-orient | 1,970 | A diagnostic audit across all seven layers that names the bottleneck layer and recommends where to focus. |
| layers-domain | 1,967 | Mapping a domain's concepts, terminology conflicts and bounded contexts, producing a concept map and a noun harvest. |
| layers-user-needs | 1,964 | Eliciting and prioritising needs, pains and desires as job stories, the opportunities that feed strategy. |
| layers-observed-behaviour | 1,952 | Planning user research and synthesising it into confidence-rated job stories about what users actually do. |
| user-needs | 2 | No directory in the current tree; the layer is covered by `layers-user-needs`, which is the only skill for it. |
| surface | 1 | No directory in the current tree; the layer is covered by `layers-surface`. |
| product-strategy | 1 | No directory in the current tree; the layer is covered by `layers-product-strategy`. |
| orient | 1 | No directory in the current tree; the diagnostic lives in `layers-orient`. |
| observed-behaviour | 1 | No directory in the current tree; the layer is covered by `layers-observed-behaviour`. |
| intro | 1 | No directory in the current tree; the orientation skill is `layers-intro`. |
| interaction-flow | 1 | No directory in the current tree; the layer is covered by `layers-interaction-flow`. |
| domain | 1 | No directory in the current tree; the layer is covered by `layers-domain`. |
| conceptual-model | 1 | No directory in the current tree; the layer is covered by `layers-conceptual-model`. |

No indexed listings fall below the threshold; all 18 appear above. The nine bare-name listings at 1 or 2 installs are an index artefact: the tree holds only the nine `layers-` prefixed directories, so those rows have no counterpart to install.

## Why This Matters for Hermes Agents

Most agent design failures are not visual. An agent asked to improve a screen will reach for spacing, colour and copy, because those are the parts of design that appear in code, while the decisions that make the screen coherent sit one layer down in objects, states and vocabulary. This pack exists to move the conversation to that layer, and it does it by making each layer a separate skill with its own deliverable, so the agent has to name what it is deciding rather than restyle what is already there.

The dependency model is the part that transfers to engineering work. The README's claim is that weak lower layers create UX debt that propagates upward, which is the same shape as a bad data model producing expensive queries, and it is a claim an agent can act on: run `layers-orient`, find the bottleneck layer, and work there instead of at the surface where the symptom appeared.

The framework also gives a profile a shared vocabulary for review work. "This is a conceptual model problem, not a surface problem" is a sentence that ends a circular design argument, and the pack supplies the supporting method for each of the seven layers, so a review can ask for the object map or the breadboard rather than a list of opinions.

## Usage

| You say | What happens |
|---|---|
| "Users keep getting lost in this app and I do not know why" | `layers-orient` audits all seven layers and names the bottleneck, rather than starting from the screen that looks wrong. |
| "We need to redesign onboarding" | `layers-intro` loads the framework, then `layers-interaction-flow` maps places, affordances and failure paths before any visual work starts. |
| "Our team keeps arguing about what a project is" | `layers-conceptual-model` builds the object map and state diagram and pins the vocabulary, which is where that argument usually lives. |
| "The design review turned into a colour debate" | `layers-surface` runs the audit against the layers below and returns findings and a decision inventory instead of preferences. |
| "We have research but no priorities" | `layers-observed-behaviour` and `layers-user-needs` turn the research into confidence-rated job stories and then rank them. |
| "Which of these three opportunities should we build" | `layers-product-strategy` builds the Opportunity Solution Tree and identifies the riskiest assumption to test first. |

## Verification

The raw path for the entry skill returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} layers-intro\n" \
  https://raw.githubusercontent.com/jamiemill/layers-skills/main/skills/layers-intro/SKILL.md
```

Expect `200`. After the clone, confirm that all nine directories arrived and that each one is a single self-contained file:

```bash
ls /tmp/layers-skills/skills | wc -l
find /tmp/layers-skills/skills -name SKILL.md | wc -l
head -6 /tmp/layers-skills/skills/layers-intro/SKILL.md
```

Both counts should print 9, and the header should show `name: layers-intro` with a `description:` line before the closing frontmatter and an H1 of `/layers-intro`. There is no `references/` folder to check in this repo, which is also why the copy is a straight directory move.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| layers-conceptual-model | Pass | Pass | Pass |
| layers-product-strategy | Pass | Pass | Pass |
| user-needs | Pass | Pass | Pass |
| observed-behaviour | Pass | Pass | Pass |
| conceptual-model | Pass | Pass | Pass |

This is close to the smallest attack surface a skill pack can have. The repository contains ten markdown files (nine skills and a README) plus the LICENSE, with no scripts, no package manifest, no dependencies and no build step. Nothing in the pack can execute, fetch a URL or read a file on its own, so the review question is entirely about the instructions: whether the framework and the working sessions it describes are sound, and whether the agent applying them stays inside its remit.

The one thing to watch is scope rather than security. These skills are written to run structured working sessions, which means an agent that loads `layers-product-strategy` may decide to interrogate the user about business outcomes when the request was a layout change. That is a useful behaviour in a design conversation and an annoying one mid-deploy, so scope the invocation in the prompt rather than relying on the skill to infer it.

Attribution is the only other consideration, and MIT makes it simple: the README asks for attribution but does not require it, so keep the LICENSE file with the copy and cite the framework when a deliverable leans on it.

## Limitations

- Snapshot data, verified 2026-10-31: 17,776 combined installs across 18 indexed listings; 314 GitHub stars; MIT; last pushed 2026-05-30. Counts drift over time.
- The index lists 18 skills but the tree holds 9 directories. The nine extra listings are bare names (`intro`, `domain`, `surface`, `user-needs`, `conceptual-model`, `product-strategy`, `interaction-flow`, `observed-behaviour`, `orient`) at 1 or 2 installs with no directory in the current tree, so only the `layers-` prefixed pack is installable.
- Install counts are effectively uniform: the nine real skills sit between 1,952 and 2,002, a spread of 50 installs, so ordering in the index says nothing about which skill is most useful.
- There is no install documentation to follow. The README describes how to use the skills and never how to get them, so the clone and copy route here is inferred from the repository layout rather than quoted.
- Each skill is a single markdown file with no supporting references, which keeps the pack light and also means depth is bounded by what one document can hold. Packs with `references/` folders carry more method per skill.
- Last pushed 2026-05-30, about five months before this snapshot, and the framework is deliberately stable rather than tracking a tool version, so there is little drift risk but also no sign of active maintenance.

## Related

- [Podo Design Agent Skills - 151-Skill Design Catalog Setup](/hermes/skills/catalog/podo-design-agent-skills-setup)
- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)
- [Bergside Design Skills - Design Systems Setup](/hermes/skills/catalog/bergside-awesome-design-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Load `layers-intro` first, every time. The other eight assume its framework context, and a session that starts at `layers-surface` will audit a design against a model nobody agreed on.
- Use `layers-orient` as a triage step rather than a design step. It is cheap, it names the bottleneck layer, and it stops the common failure of polishing a surface that has a conceptual model problem underneath it.
- Point a review at one layer at a time. "Run `layers-conceptual-model` and give me the object map" produces a usable artifact, while "review this design" produces the colour debate the pack was written to avoid.
- Pair it with a component library pack rather than replacing one. These skills decide what to build and why; a styling pack decides how it looks, and the two answer different questions.
- Keep the whole nine-skill set together if you install any of it. The value is the dependency chain between layers, and a single layer on its own is a method without the framework that motivates it.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
