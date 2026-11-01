---
title: "Full Stack Skills - 788-Skill Catalog for Agents"
description: "partme-ai/full-stack-skills: 14.9K combined installs. A navigation repo for 788 agent skills across 51 separately installable packages."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/full-stack-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "full stack", "frontend", "java"]
---

# Full Stack Skills - Setup Guide

**Source:** [partme-ai/full-stack-skills](https://www.skills.sh/partme-ai/full-stack-skills) via skills.sh - 14.9K combined installs across 102 indexed listings; first seen 2026-11-01 (morning sweep)

**GitHub:** [partme-ai/full-stack-skills](https://github.com/partme-ai/full-stack-skills) - 718 stars, Apache-2.0, branch main, last pushed 2026-10-06; the tree holds only 12 `SKILL.md` files, four OpenSpec skills mirrored across `.agents/`, `.kimi-code/` and `.zcode/`, because the repository is now a catalogue and the installable skills live in 51 separate package repositories

**Category:** Full stack development breadth: frontend frameworks, UI libraries, backend frameworks, cloud, mobile, testing, diagramming and code quality

**Quality Tier:** 🟢 Green - all three sampled listings are a Pass on Gen Agent Trust Hub, Socket and Snyk, and the repository is Apache-2.0

The story here is a migration. What was a single monorepo with more than 460 stars has been split, as of June 2026, into 51 separately installable packages under a `full-stack-skills` GitHub organisation, and this repository is now the directory and navigation hub rather than the place the skills are installed from. The README's own count, dated 2026-10-06, is 788 skill entries across 51 packages, counted from each package's `skills/*/SKILL.md` on `main` and deliberately not de-duplicated by skill name. The stars and history stayed with this repository, which is why it carries far more attention than any single package.

The catalogue's centre of gravity is worth being honest about. Alongside the React, Angular and Next.js entries there is a dense cluster of Chinese-frontend and Java stack material: uni-app and uni-app x, uView, Vant, Element Plus, Ant Design Vue, Spring Boot with Spring Cloud Alibaba, MyBatis-Plus and an Alibaba/Tencent/Azure cloud group. For a team building on that stack the coverage is unusually specific. For a team on a different one, much of the index is noise, which is exactly why the packages are installed one at a time.

The README's framing of the problem is the most useful thing in it: loading every skill at once overflows the context window, so the design answer is per-package and per-skill installation through the skills CLI. That is the same conclusion the rest of this catalogue reaches, stated by the vendor.

## Installation

The README's install section is explicit that this repository is not the install target: install from the package repositories instead, with Node.js and npm available and a terminal open in your project directory. The documented forms are:

```bash
# Preview the skills inside a package without installing anything
npx skills add full-stack-skills/vue-skills --list

# Install one skill for one agent, into the current project
npx skills add full-stack-skills/vue-skills --skill vue3 --agent codex

# Whole package, one command
npx skills add full-stack-skills/vue-skills

# User-level install instead of per-project
npx skills add full-stack-skills/vue-skills --skill vue3 --agent codex --global
```

`npx skills list` shows what is installed. The README's package one-liners include `vue-skills` (7 skills), `tauri-skills` (52), `t2ui-skills` (97), `codeguard-skills` (68) and `codereview-skills` (5), which is a fair illustration of the range: a two-skill component package and a 97-skill design-tool package are both normal here.

The `--agent` flag matters. The README's examples all pass `--agent codex` and never name another host, so the Hermes form is the same command with your own agent identifier, or the interactive prompt if you omit the flag. Treat the flag value as ours to choose, not as something the README documents.

There is a second, narrower route that does live in this tree. Four OpenSpec skills (`openspec-propose`, `openspec-explore`, `openspec-apply-change`, `openspec-archive-change`) are checked in three times, under `.agents/skills/`, `.kimi-code/skills/` and `.zcode/skills/`, so that three different hosts find them without configuration. Cloning this repository gets you those twelve files and nothing else installable, which is worth knowing before you clone 51 package repos by mistake.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| electron | 2,371 | Desktop application work with Electron, from the frontend package group. |
| element-plus-vue3 | 1,903 | Element Plus component work on Vue 3. |
| uniapp-project | 902 | uni-app project structure for cross-platform app and mini-program builds. |
| drawio-flowchart | 676 | Flowcharts produced as diagrams.net files. |
| vue3 | 632 | Vue 3 application and component patterns, shipped in the `vue-skills` package. |
| course-designer | 422 | Course and curriculum design output, from the teaching package group. |
| mybatis-plus-generator | 333 | MyBatis-Plus persistence code generation for Java services. |
| vue2 | 274 | Vue 2 patterns for codebases that have not migrated. |
| drawio-architecture | 216 | Architecture diagrams as diagrams.net files. |
| uniapp-uview | 212 | uView components inside a uni-app project. |
| ant-design-vue | 182 | Ant Design Vue components on Vue 3. |
| vant-vue3 | 164 | Vant mobile components on Vue 3. |
| ant-design-react | 144 | Ant Design components on React. |
| vite | 135 | Vite configuration and build work. |
| appium | 129 | Appium mobile test automation. |
| spring-cloud-alibaba | 119 | Spring Cloud Alibaba service work. |
| processon-mindmap | 119 | Mind maps in ProcessOn format. |
| midjourney | 118 | Midjourney prompt construction. |
| uniappx-project | 117 | uni-app x project structure. |
| teaching-resource-generator | 115 | Teaching material generation. |

The remaining 82 indexed listings range from 52 to 111 installs.

Read the table with one caveat in mind, because it is the largest discrepancy in this guide. Not one of those twenty listings has a directory in this repository. The pack records each of them as an indexed listing with no `SKILL.md` in the tree, so the install counts measure attention on the catalogue entry, and the Use For column is derived from the skill name and the package group it belongs to. The instruction files themselves are in the package repositories the README links, and they are what you get when you install.

## Why This Matters for Hermes Agents

The useful idea in this repository is the split itself. A single skill set that covers frontend, backend, cloud, mobile, testing and diagramming has to be installed selectively or it will not fit in a context window, and the packages give an operator a natural unit to be selective with: install `vue-skills` for a Vue project rather than 788 skills for every project.

The index is also a map of what agents are actually asked to do. Electron and two component libraries lead by a wide margin, then uni-app, then diagramming, then a long tail that thins out fast. For an operator deciding what to add to a profile, that ordering is better evidence than a curated "best of" list, because it reflects what other people installed rather than what a maintainer recommends.

There is a real quality-cost trade-off to hold in view. Breadth comes from 51 independently versioned packages, which is good for freshness and bad for consistency: nothing guarantees that the `vue3` skill and the `vite` skill agree on conventions, and the README's own verification is a count of entries rather than a review pass. A profile that installs three packages should expect three different house styles.

The Green tier is accurate for what was sampled and narrower than it looks. Three listings were checked, all clean, and the repository's own contribution is markdown plus provenance and third-party notice files. The code you actually run comes from the 51 package repos, which were not sampled here, so treat the verdict as a good sign rather than a clean bill.

## Usage

| You say | What happens |
|---|---|
| "Scaffold a Vue 3 page with Element Plus components" | The `element-plus-vue3` and `vue3` skills load from `vue-ui-skills` and `vue-skills`, and the agent works from the package conventions instead of inventing component APIs. |
| "I need a diagram of this service layout" | `drawio-architecture` produces a diagrams.net file, and `drawio-flowchart` covers the flow-style variant. |
| "Generate the mapper and entity layer for this table" | `mybatis-plus-generator` produces the Java persistence scaffolding from the schema. |
| "This is a uni-app codebase, keep the components consistent" | `uniapp-project`, `uniapp-uview` and `uniappx-project` cover structure, components and the newer uni-app x variant. |
| "Design a three-week course on this topic" | `course-designer` and `teaching-resource-generator` produce the outline and the supporting materials. |
| "Write the unit tests for this module" | The testing group, including `junit`, `jest`, `vitest`, `playwright`, `appium` and `detox`, supplies the framework-specific patterns. |
| "What is in the Vue package before I install it" | `npx skills add full-stack-skills/vue-skills --list` prints the skill names without installing anything. |

## Verification

The raw path for the in-tree OpenSpec skill returned HTTP 200 on branch main when this guide was written on 2026-11-01:

```bash
curl -sL -o /dev/null -w "%{http_code} openspec-explore\n" \
  https://raw.githubusercontent.com/partme-ai/full-stack-skills/main/.agents/skills/openspec-explore/SKILL.md
```

Expect `200`. After a clone of the catalogue repository, confirm what is actually here, which is the mirrored OpenSpec set and nothing else:

```bash
git clone --depth 1 https://github.com/partme-ai/full-stack-skills.git /tmp/full-stack-skills
find /tmp/full-stack-skills -name SKILL.md | wc -l
ls /tmp/full-stack-skills/.agents/skills
```

The count should be 12, and the listing should show four directories: `openspec-apply-change`, `openspec-archive-change`, `openspec-explore` and `openspec-propose`. Those twelve are four skills mirrored three times. If you were expecting the index's 102 listings to be present as directories, this is the check that shows why they are not.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-01) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| electron | Pass | Pass | Pass |
| element-plus-vue3 | Pass | Pass | Pass |
| uniapp-project | Pass | Pass | Pass |

What was actually reviewed is narrow relative to what the index advertises. Three of 102 listings were sampled, all three are clean, and this repository's own tree contains nothing executable: twelve markdown files, a `docs/` folder with a catalogue inventory, a handful of READMEs in two languages, and provenance files including `PROVENANCE.md`, `THIRD-PARTY-NOTICES.md` and `EVALUATION_REPORT.md`. The presence of a provenance file and a third-party notices file is a good sign for a catalogue that aggregates other people's work, because it means upstream attribution was treated as a deliverable.

The risk sits one layer down, in the 51 package repositories that the install commands point at. Those are separate `full-stack-skills/*` repos, independently maintained, and none of their contents were sampled for this guide. An agent installing `codeguard-skills` or `tauri-skills` is trusting a package that this snapshot says nothing about, so run the same security check on the package you actually install rather than relying on the catalogue's tier.

Two practical controls follow. Install per package and read what landed, since the CLI will happily pull a 97-skill package into a profile. And keep the package list explicit in your profile notes, because a catalogue of this size makes it easy to lose track of which of the 51 sources a given skill came from.

## Limitations

- Snapshot data, verified 2026-11-01: 14,932 combined installs across 102 indexed listings; 718 GitHub stars; Apache-2.0; last pushed 2026-10-06. Counts drift over time.
- The gap between the index and the tree is the widest in this set: 102 indexed listings against 12 `SKILL.md` files, and those twelve are four OpenSpec skills mirrored across three host folders. The 20 listings shown above all have no directory here at all.
- Install counts are per-listing attention, not package quality. The catalogue's own figure is 788 entries across 51 packages and is explicitly not de-duplicated by skill name, so the same skill can be counted more than once across packages.
- The README and most documentation are in Chinese. `README.en.md`, `AGENTS_EN.md` and `AGENT_PROMPT.md` are the English surfaces, and the English README is shorter than the Chinese one.
- Only three listings were sampled for security, none of them from the 51 package repositories that actually ship the code.
- Commit activity here describes the catalogue, not the packages. Last pushed 2026-10-06 means the navigation page was edited then; a package may be fresher or much older.
- The stack coverage is uneven by design. uni-app, Vue 2, uView, Spring Cloud Alibaba and MyBatis-Plus are covered in depth, while many other ecosystems have a single entry or none.

## Related

- [Developer Kit - Java and TypeScript Skill Suite Setup](/hermes/skills/catalog/developer-kit-setup)
- [ECC Engineering Skills - Enterprise Engineering Suite Setup](/hermes/skills/catalog/ecc-engineering-skills-setup)
- [Frontend God Mode - Design Skills Bundle Setup](/hermes/skills/catalog/frontend-god-mode-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Never install from `partme-ai/full-stack-skills`. Every working command in the README points at a `full-stack-skills/<package>` repository, and installing the catalogue itself gets you four OpenSpec skills and nothing else.
- Run `--list` before `--skill`. A package like `t2ui-skills` has 97 entries, and picking one from a list is cheaper than installing the package and then removing 96 directories.
- Choose the package by ecosystem, not by the index ranking. One package per project keeps the context cost predictable and gives you one house style to reason about.
- Re-check security on the package you install. The Green tier here covers three listings in the catalogue, not the code in `codeguard-skills` or `vue-skills`.
- Expect Chinese-language references in the packages and budget for it. The skills work, but examples and comments often assume a reader of the original documentation.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
