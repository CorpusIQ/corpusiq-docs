---
title: "New Skills - October 28, 2026 Evening"
description: "Skills.sh sweep (Oct 28 evening): 886 skills scanned, 12 publisher guides from the morning queue for 274,742 combined installs across 109 listings."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct28-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 28, 2026 Evening Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window returned 886 unique skills with 0 failed queries: 87 NEW, 268 PARTIAL.

This fire drained the queue the morning fire left behind. The window itself was silent above the 1,000-install trigger for the twentieth consecutive fire, its top row reading 328 installs, and the trending board served 600 entries across 69 sources that the catalog already covers. All nine NEW sources were sized by publisher query first, as the standing rule requires; the largest, `chadboyda/agent-gtm-skills`, read 2,752 combined installs across 18 listings, 55 percent of the 5,000-install floor, and none cleared it.

So the twelve converts come from the morning fire's own carry-over list: publisher-sized clusters that were already above the floor and waiting for a fire with room to draft them. Twelve are documented below for **274,742 combined installs across 109 indexed listings**, from 64,045 installs at the top to 10,499 at the bottom.

Every guide was drafted against a pre-built pack holding the exact per-listing install figures, the repository tree, the row-to-path map and the three-auditor verdicts sampled from skills.sh, then checked with three gates: the format gate, the pack cross-check at a per-guide threshold (50 to 500 depending on the install distribution), and the frontmatter audit. All 36 gate runs passed on the first try, re-run by the orchestrator after an md5 comparison of the three canonical scripts.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected (standing window) | 886 (0 failed queries) |
| NEW (not in catalog) | 87 |
| PARTIAL (source known, skill not cataloged) | 268 |
| Trending board | 600 entries / 69 sources, all covered |
| Above-floor finds in the standing window | 0 (top row 328) |
| NEW sources sized by publisher | 9 (largest 2,752, 55 percent of floor) |
| Queue carried from the morning fire | 22 above-floor clusters, 12 drained |
| New publisher guides | 12 (109 indexed listings, 274,742 combined installs) |
| Marketplace count | 1,205+ to 1,217+ |

## New Publisher Guides

### 1. Pilio Skills (64,045 combined)

**Source:** [pilioai/skills](https://www.skills.sh/pilioai/skills), 7 indexed listings, top skill `gpt-image-2` at 20,348; 44 stars; MIT; branch main; 6 `SKILL.md` directories.

A thin wrapper suite over the Pilio CLI for image and PDF utility work: generation through `gpt-image-2`, the Nano Banana image path, background removal, image watermark removal, upscaling and PDF watermark removal. The suite earns its place on distribution rather than repository size, with unglamorous file chores carrying most of the install volume.

The index outruns the tree in one place: `nano-banana-2` holds 13,485 installs but has no `SKILL.md` anywhere in the clone, so the guide names it as an index listing with nothing to review rather than describing behaviour it could not read.

### 2. QianWen AI Skills (56,229 combined)

**Source:** [qianwen-ai/qianwen-ai](https://www.skills.sh/qianwen-ai/qianwen-ai), 11 indexed listings, top skill `qianwen-update-check` at 5,769; 115 stars; Apache-2.0; branch main; 11 `SKILL.md` directories.

The Alibaba Qwen (QianWen) API as eleven narrow skills: text, vision, image generation, video generation, text to speech, model selection, usage accounting, ops authentication, payment, an update check and a skill finder. Every listing has a directory and every listing sits in a tight 2,718 to 5,769 band, which is the shape of vendor distribution rather than organic adoption.

The suite assumes a QianWen CLI and an API key with a documented precedence chain, and two of the skills touch credentials and billing, which the guide says plainly instead of burying in a prerequisites line.

### 3. NestJS Best Practices (30,694 combined)

**Source:** [kadajett/agent-nestjs-skills](https://www.skills.sh/kadajett/agent-nestjs-skills), 1 indexed listing (`nestjs-best-practices`); 292 stars; no LICENSE file at the repository root while the `SKILL.md` frontmatter claims MIT; branch main.

One skill, 40 rules across 10 categories, covering the parts of NestJS that agents usually get wrong: module boundaries, dependency injection, DTO validation, error handling, security, testing and the request lifecycle. It carries more installs than every other entry except the top two, which makes it the clearest case in this batch of a single deep file beating a wide collection.

The licence mismatch is the adoption risk and is stated in four places in the guide: GitHub reports no standard licence at the root, the skill file claims MIT, and a reader should treat the repository as unspecified until the publisher adds a licence file.

### 4. Ejiro Agent Skills (18,886 combined)

**Source:** [ejirocodes/agent-skills](https://www.skills.sh/ejirocodes/agent-skills), 8 indexed listings, top skill `svelte5-best-practices` at 17,221; 6 stars; MIT; branch main; 7 `SKILL.md` directories.

Framework conventions for Svelte 5 runes, Vue 3 with TypeScript and NestJS 11, with an Exa block for web research, entity lookup, search and retrieval-augmented answers plus a meta skill for authoring new skills. One listing, `skill-creator`, has no directory in the tree and the guide says so.

Three of the six sampled skills carry a Snyk `W011` warning on the Exa listings, which is a structural consequence of a skill that sends queries to a third-party API rather than a defect of this repository.

### 5. Java Development Plugin (17,533 combined)

**Source:** [pluginagentmarketplace/custom-plugin-java](https://www.skills.sh/pluginagentmarketplace/custom-plugin-java), 12 indexed listings, top skill `java-spring-boot` at 11,783; 41 stars; licence field NOASSERTION with no standard licence file at the root; branch main; 12 `SKILL.md` directories.

A Java engineering pack organised by task: Spring Boot scaffolding, testing, Maven, JPA and Hibernate, microservices, performance, concurrency, Gradle, Docker and language fundamentals. `java-spring-boot` alone accounts for two thirds of the combined installs, and the skill takes parameters for Java version (8, 11, 17, 21) and Spring version rather than assuming a stack.

It is the only Java suite in the catalog besides Developer Kit, and its install profile suggests the demand is specifically for Spring Boot rather than for language fundamentals.

### 6. Proactive Agent (15,165 combined)

**Source:** [halthelobster/proactive-agent](https://www.skills.sh/halthelobster/proactive-agent), 1 indexed listing (`proactive-agent`); 22 stars; no LICENSE file at the repository root while the `SKILL.md` claims MIT; branch main.

A behaviour specification rather than a tool: one markdown file of roughly 17 KB at the repository root, version 3.0.0, with no README, no scripts, no manifest and no assets. It prescribes a write-ahead log for corrections, preferences and decisions, a working buffer that engages once context passes 60 percent, a compaction recovery routine, self-improvement guardrails with weighted scoring, a heartbeat checklist and a fixed workspace file layout.

It is worth reading for the memory architecture even by people who never install it, and the guide notes the gap between what the file assumes and what the repository ships: its quick start refers to `assets/` and `scripts/` directories that do not exist in the tree.

### 7. Kami (13,398 combined)

**Source:** [tw93/kami](https://www.skills.sh/tw93/kami), 1 indexed listing (`kami`); 12,119 stars; MIT; branch main; two identical `SKILL.md` copies at `skills/kami/` and `plugins/kami/skills/kami/`.

A layout skill that gives an agent document design rules and templates for PDF, PNG and editable PowerPoint output, with eight document types (one-pager, long document, letter, portfolio, resume, slides, equity report, changelog) plus a landing page system, each in English, Chinese and Korean variants, and eighteen inline SVG diagram types. The author positions it as the delivery piece of a trilogy alongside Kaku and Waza.

The thesis is that good content deserves good paper, and the implementation backs it with a fixed palette, a type scale, a build script with content and rhythm checks and a verification path for the rendered output rather than a prompt that says make it pretty.

### 8. ego lite (13,216 combined)

**Source:** [citrolabs/ego-lite](https://www.skills.sh/citrolabs/ego-lite), 3 indexed listings, top skill `ego-browser` at 13,209; 20,467 stars; MIT; branch main; 3 `SKILL.md` directories.

A packaged browser for agents to run web automation, shipped as a desktop application with installers for Apple Silicon, Intel and Windows, plus skills that drive it. It migrates a Chrome profile so the agent works inside real logged-in sessions, which is the capability and the risk in the same sentence.

The security section leads the guide rather than following it: Gen Agent Trust Hub fails `ego-browser`, Snyk records `W011` and `W012`, and Socket passes, while the two supporting listings carry warnings of their own. The guide reads that as the expected verdict on a moving binary with a live network surface and turns it into a scoping rule about which profile the agent is allowed to use.

### 9. Refero Design (12,163 combined)

**Source:** [referodesign/refero_skill](https://www.skills.sh/referodesign/refero_skill), 1 indexed listing (`refero-design`); 328 stars; MIT; branch master; 1 `SKILL.md` directory.

One design skill plus a read-only MCP connection. The skill makes research mandatory before implementation, and the connection supplies curated visual styles, a large library of real application screens and documented user flows, so an agent cites an existing pattern instead of inventing one. Live research requires a paid Refero account, and there is a plugin listing for ChatGPT and Codex plus a plugin marketplace route for Codex.

It is the only entry in this batch whose core mechanism is a paid data source behind a free skill, which the guide states as a dependency rather than a footnote.

### 10. OpenCode Workflows (12,015 combined)

**Source:** [igorwarzocha/opencode-workflows](https://www.skills.sh/igorwarzocha/opencode-workflows), 38 indexed listings, top skill `powerpoint` at 6,007; 122 stars; no LICENSE file at the repository root; branch master; 51 `SKILL.md` directories.

Command templates, global agent prompts and workflow patterns for OpenCode, organised around a configurator meta-agent that answers configuration questions and installs the pieces: eight `security-*` review skills, document skills for PowerPoint, Word, Excel and PDF, plugin and MCP installers, a skill creator, an agent architect and a set of standard operating procedures. The repository is archived and read-only, last pushed in February 2026, which the guide records with the counts.

The wide tail matters here: 30 of the 38 listings sit between 92 and 184 installs, so the suite reads as one author's working toolkit that other people sample rather than a product with a roadmap.

### 11. Fallow Skills (10,899 combined)

**Source:** [fallow-rs/fallow-skills](https://www.skills.sh/fallow-rs/fallow-skills), 6 indexed listings, top skill `fallow` at 9,765; 137 stars; MIT; branch main; 5 `SKILL.md` directories with CI validation.

The agent layer for fallow, a TypeScript and JavaScript codebase intelligence tool that reports changed-code risk, dead code, circular dependencies, duplication, complexity hotspots and design-system drift in milliseconds without configuration. The skills teach the commands, the flags and how to read the output, and a `PreToolUse` hook guards the Bash calls they generate. Fallow Cloud is an optional paid tier that adds production coverage.

The reframing is the interesting part: linters enforce style and formatters enforce consistency, and neither builds a module graph, so neither can tell you what nothing depends on.

### 12. Composio (10,499 combined)

**Source:** [composiohq/composio](https://www.skills.sh/composiohq/composio), 20 indexed listings, top skill `composio` at 8,266; 30,796 stars; MIT; branch next; 20 `SKILL.md` directories.

The skills that ship inside Composio's own monorepo, which are engineering guidance for working on the Composio SDK rather than a catalogue of its integrations: TypeScript and Python testing, bug fixing, CLI command authoring, provider patterns, repository guidance, documentation decisions and an effects skill. Developers evaluating Composio as an integration layer will find the SDK shape documented here in the form an agent can follow.

The distinction is worth making explicit because the install counts invite the wrong assumption: these are not connectors, and the guide says so in the intro, the Limitations and the Quality Tier note.
