---
title: "Story Skills - End-to-End Fiction Writing"
description: "danjdewhurst/story-skills on skills.sh: 11.9K combined installs across 24 listings; 24 fiction skills plus a story CLI that checks continuity."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/story-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "fiction writing", "continuity", "markdown"]
---

# Story Skills - Setup Guide

**Source:** [danjdewhurst/story-skills](https://www.skills.sh/danjdewhurst/story-skills) via skills.sh - 11.9K combined installs across 24 indexed listings; first seen 2026-11-06 (Nov 6, 2026 evening sweep)
**GitHub:** 394 stars, MIT, last pushed 2026-11-04, 24 SKILL.md directories, one per skill under `skills/`, with a companion CLI in `bin/`
**Category:** Fiction writing for agents: discovery drafting, character management, chapter craft, editorial review and adaptation passes
**Quality Tier:** 🟢 Green - every sampled skill passes all three scanners, the licence is MIT, and the install path is markdown plus one optional local CLI.

Story Skills gives an agent a shared project format for fiction: a story bible, characters, worldbuilding, plot arcs, scenes, continuity state, promises and payoffs, and chapter drafts. Everything is plain markdown with YAML frontmatter, packaged as Agent Skills and as Codex and Claude Code plugins. The repository's own summary is that it lets you "plan, track, and draft fiction in markdown, with a continuity checker that catches mistakes before readers do".

The set is 24 skills, and the coverage runs from testing a premise to the query letter. A companion `story` CLI does the mechanical work: registries, word counts, link checks, validation, continuity checks and exports. The README describes that split explicitly, and it is the reason the bundle is more than a pile of writing prompts: the skills do the creative work, and the CLI treats the story bible as a checkable contract, flagging a character who died in chapter 2 but appears in chapter 4, or a payoff that lands before its setup.

## Installation

The route the project's getting-started guide documents for any agent the skills CLI supports:

```bash
npx skills add danjdewhurst/story-skills
```

That installs all 24 skills. The guide also documents a narrower install, adding `--skill <name>` for a subset or `--agent <name>` to target one harness.

For Claude Code and Codex, the plugin marketplace is the first-class path, and the getting-started guide shows both forms:

```bash
claude plugin marketplace add danjdewhurst/story-skills
claude plugin install story-skills@story-skills
```

```bash
codex plugin marketplace add danjdewhurst/story-skills
codex plugin add story-skills@story-skills
```

Gemini CLI has its own installer, and the by-hand route copies each folder from `skills/` into the directory your agent scans. Copy whole folders, not just `SKILL.md`, because each skill's `references/` files and the bundled CLI at `story-maintenance/scripts/story.js` have to stay beside it:

```bash
git clone https://github.com/danjdewhurst/story-skills.git
mkdir -p ~/.agents/skills && cp -r story-skills/skills/* ~/.agents/skills/
```

The CLI is optional. The skills work without it, because `story-maintenance` carries its own copy, and it needs Node 18 or newer with no runtime dependencies:

```bash
npm install -g story-skills
```

## What It Provides

Seven listings clear the threshold, and they are the structural core of the set:

| Skill | Installs | Use For |
|---|---|---|
| worldbuilding | 1,040 | Locations, magic and political systems, cultures, calendars, travel times, invented terms and glossaries for the story itself |
| plot-structure | 910 | Arc planning with three-act, hero's journey, Save the Cat and other structures; book-level pacing, foreshadowing and timelines |
| character-management | 895 | Character profiles, relationship graphs, family trees, arcs and character timelines inside the project |
| chapter-writing | 879 | Drafting a chapter or scene from an outline and the story context, and continuing the story in prose |
| story-init | 878 | Scaffolding a new project: story bible, folders and registries, then handing off to the drafting skills |
| revision-continuity | 863 | Revision passes, continuity audits, character state checks, reverse outlines, subplot cuts and length passes |
| story-maintenance | 795 | The deterministic checks: validate, reindex, link check, word counts, exports and builds, run through the bundled CLI |

The remaining 17 indexed listings range from 264 to 376 installs.

Below the table sit the craft skills that do the specialised passes: `scene-craft` for scene structure and chapter openings, `voice-style` for the style sheet and distinct character voices, `line-editing` with a reason per change, `genre-craft` for conventions such as mystery fair play, `theme-craft` for the controlling idea, `reader-panel` for simulated reads, `feedback-triage` for beta feedback, `editorial-review` for sensitivity reads and permissions, `submission` for the query letter, `publishing` for EPUB and print interiors, `adaptation` for audiobook and screenplay work, and `series-continuity` for shared canon across books. Each skill's frontmatter carries an explicit "NOT for" clause routing to the neighbour, which is what keeps an agent from answering a continuity question with a structural rewrite.

## Why This Matters for Hermes Agents

Long fiction is the hardest context problem an agent has: the canon outgrows the window, and every new chapter is written against a summary that drifts. The skill set fixes the format rather than the prose. Because character, place, scene, promise and chapter all live in markdown with YAML frontmatter, the agent can load exactly what a chapter needs, and `story context chapter-03 --budget 6000` packs that material into a token budget instead of dumping the manuscript.

The continuity engine is the part with no equivalent in a writing prompt. Deaths, promises, open questions, and object and knowledge state sit in frontmatter, so contradictions surface as check failures rather than as reader complaints. `story check --strict` runs validation, link checks and continuity in one scan, and `story knowledge sera-voss --at chapter-03` answers what a character knew at a point in the story.

Routing is explicit. The frontmatter of each skill names the cases it refuses and the skill that should handle them, which matters in a 24-skill set where the failure mode is an agent doing a line edit when the chapter needs restructuring, or planning a plot arc when the user asked for a query letter.

Finally, the project is version-control friendly by construction. A story is a folder of markdown files, so diffs, branches and snapshots all work, and a Hermes agent that already lives in git gets change review for prose for free.

## Usage

| You say | What happens |
|---|---|
| "Start a new story called The Last Ember" | `story-init` scaffolds the bible, the folders and the registries, then hands off to premise or drafting work |
| "Create a character, she is the antagonist's sister" | `character-management` writes a profile with relationships, arc fields and a timeline entry, and registers the name |
| "Design a magic system with a real cost" | `worldbuilding` builds the system with rules, costs and limits, and adds glossary terms other chapters can link to |
| "Write the next chapter" | `chapter-writing` loads the outline and the packed story context, drafts the chapter, and leaves the bible untouched |
| "Continuity-check chapter 3" | `revision-continuity` audits canon and character state, then `story-maintenance` runs the CLI check and reports findings |
| "Triage the beta feedback" | `feedback-triage` clusters reader notes into themes and produces a revision plan with an order of work |
| "Make an audiobook narration script" | `adaptation` produces the narration script, pronunciation guide and per-chapter timing from the finished draft |

## Verification

Read one skill before installing. This path returned HTTP 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/danjdewhurst/story-skills/main/skills/story-init/SKILL.md | head -20
```

It should open with `name: story-init` and a description keyed to phrases such as "start a new story" and "initialize a story project", followed by the "NOT for" routing clause that sends sequels to `series-continuity`.

After install, confirm all 24 folders landed, since a partial copy leaves skills that reference neighbours nobody installed:

```bash
ls ~/.agents/skills | wc -l
```

The count should be 24 if that directory held nothing before. Then check the bundled CLI runs from inside a project folder:

```bash
node ~/.agents/skills/story-maintenance/scripts/story.js --help
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| worldbuilding | Pass | Pass | Pass |
| story-maintenance | Pass | Pass | Pass |
| line-editing | Pass | Pass | Pass |
| submission | Pass | Pass | Pass |
| interactive-fiction | Pass | Pass | Pass |

The skills themselves are markdown. The part that executes is the optional `story` CLI, published to npm as `story-skills`, and the getting-started guide is unusually careful about it. It warns that `npx story-skills`, `bunx story-skills` and a Bun run of a clone resolve a local `node_modules/.bin` first, so in a story repository you do not trust you should use a global install or a standalone binary instead. Release binaries ship with a checksums file, and releases after 0.21.0 carry a signed build provenance attestation that `gh attestation verify` can check.

Two smaller notes. The bundled copy at `story-maintenance/scripts/story.js` runs inside your project, so it is code from the same source as the npm package and should be treated the same way. And the README points at Plothold, a paid web app by the same maintainer built on these skills, which stores the book on its servers; that is an alternative product, not part of the install.

## Limitations

- Snapshot data, verified 2026-11-06: 11,914 combined installs across 24 indexed listings; 394 GitHub stars; MIT; last pushed 2026-11-04. Counts drift over time.
- Usage is broad but shallow. The top listing has 1,040 installs and the bottom has 264, so no single skill is heavily exercised, and the tail skills are the least tested part of the set.
- The skills assume the project layout that `story-init` creates. Point them at a folder of loose chapters and the registries, links and continuity checks have nothing to read.
- Craft quality is not the contract. The continuity engine catches a dead character reappearing; it cannot tell you the chapter is dull, and `reader-panel` simulates readers rather than recruiting them.
- The CLI is optional but the deterministic checks live there. Without Node 18 or newer you get the drafting skills only, and `story-maintenance` degrades to its bundled copy.
- One maintainer, and a companion paid product in the same README. Neither is a defect, but the roadmap and the hosted option both run through the same person.

## Related

- [Oh Story ClaudeCode Skills - Long-Form Writing & Browser CDP](/hermes/skills/catalog/oh-story-claudecode-skills-setup)
- [Avoid AI Writing - AI-Pattern Audit & Rewrite Setup](/hermes/skills/catalog/avoid-ai-writing-setup)
- [Ghostwriter - Full Setup Guide for Hermes Agents](/hermes/skills/catalog/ghostwriter-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `story check` after every chapter, not at the end of the draft. The continuity engine is cheap and the findings are specific, and a contradiction found in chapter 4 costs one edit instead of a revision pass.
- Let `story-init` create the project even if you already have prose. `story import draft.md` splits an existing manuscript into the layout and lists recurring names, which is the fastest way to get canon under check.
- Ask which skill applies when you are unsure. `premise-workshop` for an idea, `story-init` for a project, `discovery-drafting` when there is no outline; the frontmatter routing exists so the agent stops guessing.
- Use the context command before drafting a long chapter. `story context chapter-03 --budget 6000` decides what the model sees, which is more reliable than pasting the bible and hoping.
- Pair `voice-style` with `line-editing`. The style sheet records spellings, punctuation and each character's voice, and the line edit then has something objective to enforce.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
