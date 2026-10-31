---
title: "Jwynia Agent Skills - Presentation and Writing Suite"
description: "jwynia/agent-skills: 65.4K combined installs. 119 agent skills for presentations, documents and fiction writing, plus research and Godot tooling."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/jwynia-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "presentations", "fiction writing", "documents", "godot"]
---

# Jwynia Agent Skills - Setup Guide

**Source:** [jwynia/agent-skills](https://www.skills.sh/jwynia/agent-skills) via skills.sh - 65.4K combined installs across 119 indexed listings; first seen 2026-10-30 (evening sweep)

**GitHub:** [jwynia/agent-skills](https://github.com/jwynia/agent-skills) - 180 stars, no LICENSE file at the repository root, branch main, last pushed 2026-02-24; 119 `SKILL.md` files in five trees under `skills/`: `creative/` 57, `general/` 32, `tech/` 28, `development/` 1, `education/` 1

**Category:** Presentation, document and long-form fiction skills, with research, security and game development tooling

**Quality Tier:** 🟡 Yellow - three of four sampled skills Pass every auditor and one carries a Snyk Warn, and the repository ships no LICENSE file at its root even though 117 of the 119 skills declare MIT in their own frontmatter

Jwynia publishes `jwynia/agent-skills` as a single repository of Agent Skills for AI coding assistants, organised into three browsable categories rather than shipped as a product. The largest block is fiction: story diagnostics, worldbuilding systems, character arc and dialogue craft, chapter drafting, and a set of generators that take a premise to an outline. Around that sit document skills that write PDF, DOCX, PPTX, XLSX and RevealJS output, research and verification skills, and a technical tail covering Godot, Electron, TypeScript, shadcn layouts, security scanning and agile workflow.

The notable thing is the split of labour inside the fiction set. The skills are diagnostic rather than generative by design: `story-coach` is explicitly forbidden from writing prose and only asks questions, `story-sense` routes a draft to whichever specialist it needs, and `fact-check` is built as a separate pass that must run after generation rather than during it. For a suite with 65,356 combined installs across 119 indexed listings, that discipline is unusual, and it is what makes the collection usable as a review layer rather than a content mill.

## Installation

The README installs whole categories with the skills CLI, no npm install and no build step:

```bash
# Creative and narrative skills, 57 in the tree
npx skills add https://github.com/jwynia/agent-skills/tree/main/skills/creative

# Technical and development skills, 28 in the tree
npx skills add https://github.com/jwynia/agent-skills/tree/main/skills/tech

# General utilities, 32 in the tree
npx skills add https://github.com/jwynia/agent-skills/tree/main/skills/general
```

A single skill can be pulled by its full path, which is the route worth using when you only want the document or presentation pieces:

```bash
npx skills add https://github.com/jwynia/agent-skills/tree/main/skills/general/meta/skill-builder
```

Installing everything is also a documented one-liner:

```bash
npx skills add https://github.com/jwynia/agent-skills/tree/main/skills
```

The checkout holds 119 `SKILL.md` files, which is the count to trust over the 112 the top-level README claims and the 114 that `skills/README.md` claims. Two skills sit outside the three advertised categories, `product-analysis` in `skills/development/architecture/` and `document-to-narration` in `skills/education/`, so the three category commands above do not cover the whole tree and those two need their own path. The repository also ships `scripts/install-skills.sh`, which flattens the nested tree into `.claude/skills/` and skips name collisions:

```bash
bash scripts/install-skills.sh
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| presentation-design | 2,568 | Designing and auditing a deck or a talk against one main message, with audience planning, cognitive load limits and an assertion-evidence check that catches slide walls of text. |
| frontend-design | 2,323 | Building a distinctive web interface with palette, typography, design token and component generation, plus an audit pass over existing React, Vue, Svelte or plain CSS work. |
| requirements-analysis | 2,255 | Turning a vague build request into validated needs, separating stated wants from the underlying problem before any code is written. |
| godot-best-practices | 2,057 | Writing Godot 4.x GDScript that follows scene, signal and resource conventions, including state machine, object pooling and save and load patterns. |
| web-search-tavily | 1,132 | Running filtered web searches through the Tavily API with domain scoping, relevance scores and AI-written answer summaries; needs `TAVILY_API_KEY`. |
| godot-asset-generator | 1,007 | Generating sprites, tilesets and UI art through DALL-E, Replicate or fal.ai, then preparing sprite sheets, style guides and import settings for a Godot project. |
| document-to-narration | 979 | Converting an essay, blog post or article into a narrated video script with TTS audio and word-level VTT timings. |
| pdf-generator | 918 | Creating PDFs from scratch or from templates, filling forms, merging documents, adding watermarks and extracting text. |
| story-coach | 889 | Coaching a writer through questions and diagnosis while never generating prose, for work that has to stay the author's own. |
| electron-best-practices | 824 | Structuring an Electron and React desktop app with contextBridge IPC, packaging, code signing, notarization and Playwright coverage. |
| web-search | 777 | Searching through the agent's own built-in web search when no API key is available. |
| fact-check | 752 | Running a separate verification pass over generated text to catch claims the sources do not support. |
| worldbuilding | 738 | Diagnosing a setting that feels thin, including institutions that read as designed rather than evolved and economies that do not add up. |
| docx-generator | 736 | Producing Word documents from a branded template or from scratch, including reports, contracts and letters. |
| summarization | 712 | Choosing the right summary shape for the purpose, from a TLDR through an abstract to an executive summary. |
| joke-engineering | 693 | Diagnosing why a joke or a comedic passage falls flat and rebuilding the connection it depends on. |
| story-analysis | 691 | Evaluating a finished story or chapter against its own narrative goals, with strengths and weaknesses named rather than graded. |
| novel-revision | 683 | Managing a multi-level novel revision so a change at one level does not break continuity at another. |
| dialogue | 682 | Fixing wooden dialogue, characters who all sound alike, and scenes where the conversation only does one thing. |
| story-idea-generator | 672 | Generating genre-first story concepts and strengthening a premise so emotional impact drives the plot. |

The remaining 99 indexed listings range from 1 to 653 installs.

That tail is not filler. It is where the specialist fiction and worldbuilding skills live: `scene-sequencing` at 501, `cliche-transcendence` at 469, `reverse-outliner` at 444, `sensitivity-check` at 420, `conlang` at 413, and the security scanners `secrets-scan` at 375 and `dependency-scan` at 359. The index sorts by installs, and installs track broad appeal rather than usefulness for a particular job.

## Why This Matters for Hermes Agents

Most of the failure modes in agent-assisted writing are not failures of prose quality, they are failures of process: the draft is generated before the requirements are understood, the fact pass happens in the same breath as the invention, and the revision at chapter level quietly breaks the timeline two chapters back. This suite encodes the opposite sequencing, and it does so as separate skills that a Hermes agent can be routed into one at a time. `requirements-analysis` runs before the build, `fact-check` runs after the draft and is documented as unreliable when combined with generation, and `novel-revision` exists specifically to manage the cascade.

The diagnostic split also gives a Hermes profile a review layer to point at its own output. Asked to check a deck, `presentation-design` returns a specific problem list with names such as wall of text, bullet point disease and kitchen sink rather than a general opinion, which is the kind of structured feedback that can be looped back into another edit pass. The same holds for `story-analysis` and `worldbuilding`: they produce findings an agent can act on without a human adjudicating adjectives.

The document skills are the practical half. `pdf-generator`, `docx-generator` and the PPTX, XLSX and RevealJS equivalents give an agent real file output instead of markdown that somebody has to reformat, and `document-to-narration` chains a written piece into a script, TTS audio and word-level VTT, which is the tedious part of turning a post into a video. These ship Deno scripts, so the capability is executable rather than advisory.

Finally, the routing metadata is honest. Skill frontmatter carries a `type` field such as diagnostic, generator, utility or orchestrator, and a `mode` field, so an agent harness that reads frontmatter can tell a skill that writes from a skill that only reviews. That is what makes a 119 skill library tractable rather than a pile of prompts with a shared folder name.

## Usage

| You say | What happens |
|---|---|
| "Review this deck before I present it Thursday" | `presentation-design` walks the audience, the one main message and the supporting points, then reports slide level problems by name, with the assertion-evidence fix for each slide that is carrying paragraphs. |
| "This story is 40,000 words, what is actually wrong with it?" | `story-sense` diagnoses what the draft needs and routes to a specialist such as `story-analysis` for a full read, `outline-coach` for structure, or `character-arc` for transformation problems. |
| "Build a landing page that does not look like every other SaaS page" | `frontend-design` sets the palette, type scale and tokens first, then generates components, and runs its audit against the result rather than only producing the markup. |
| "Write these three claims into the report, then check them" | The draft pass runs first and `fact-check` runs after it as its own pass, flagging claims the cited sources do not support instead of hedging during generation. |
| "Turn this blog post into a narrated video" | `document-to-narration` cuts the piece into scenes, generates TTS audio and VTT with word level timestamps through its Deno and ffmpeg pipeline. |
| "I need a branded contract in Word and a one page PDF summary" | `docx-generator` fills a supplied template so branding holds, `pdf-generator` builds or merges the summary and can watermark it, and both run through Deno scripts. |
| "Make this funny, it is not landing" | `joke-engineering` treats the joke as a connection system, names where the setup and the punchline stop connecting, and rewrites for the specific gap. |

## Verification

The raw path below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} presentation-design\n" \
  https://raw.githubusercontent.com/jwynia/agent-skills/main/skills/general/communication/presentation-design/SKILL.md
```

Expect `200`. Read that file before installing a category, because the frontmatter is the whole routing contract: `name`, a `description` that names the trigger situations, a `license` line, and a `metadata` block with `type` and `mode`.

After an install, confirm the files landed and that the tree still matches the index:

```bash
find ~/.hermes/profiles/corpusiq/skills -name SKILL.md | wc -l
head -12 ~/.hermes/profiles/corpusiq/skills/presentation-design/SKILL.md
grep -rl "^license: MIT" --include=SKILL.md ~/.hermes/profiles/corpusiq/skills | wc -l
```

The first command should account for the skills you installed against the 119 in the repository. A good file shows `name: presentation-design`, the description and the `metadata:` block with `type: diagnostic` and `mode: diagnostic+assistive`. The licence count comes to 117 of 119 in a full copy, because two skills carry no frontmatter licence field.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| presentation-design | Pass | Pass | Pass |
| frontend-design | Pass | Pass | Warn |
| requirements-analysis | Pass | Pass | Pass |
| godot-best-practices | Pass | Pass | Pass |
| skill-maker | n/a | n/a | n/a |

One of the four sampled skills, `frontend-design`, carries a Snyk Warn, which means a dependency or code pattern in that skill was flagged and should be read before you install it into an agent with write access to a repository. Nothing in the sample is a Fail, Trust Hub and Socket returned Pass for all four audited skills, and `skill-maker` has no verdict at all on any of the three auditors, so its row says nothing either way.

The larger risk is legal rather than technical. The repository has no LICENSE file at its root and GitHub reports no license field, so the only grant is the `license: MIT` line inside 117 of the 119 `SKILL.md` files. Two skills, `npm-package` and `npx-cli`, have no licence field in their frontmatter at all, which leaves those files without a stated grant. For internal use that is a reasonable reading; for redistribution it is worth an explicit check.

Operationally, treat the suite as a supply of scripts as well as prompts. 48 skill directories ship a `scripts/` tree, several need Deno with read and write permissions, and the asset and search skills call paid third-party APIs with keys from the environment (`TAVILY_API_KEY`, `OPENAI_API_KEY`, `REPLICATE_API_TOKEN`, `FAL_KEY`). The review-oriented skills such as `presentation-design`, `story-coach` and `worldbuilding` are markdown only.

## Limitations

- Snapshot data, verified 2026-10-30: 65,356 combined installs across 119 indexed listings; 180 GitHub stars; no LICENSE file at the repository root; last pushed 2026-02-24. Counts drift over time.
- No repository licence. The root holds no LICENSE file and the GitHub licence field is empty, so the MIT grant rests on the `license: MIT` line in 117 of the 119 skills, and `npm-package` and `npx-cli` have no licence field in their frontmatter at all. Clear that with the author before redistributing or bundling.
- The repository is stale. Last push was 2026-02-24, roughly eight months before this guide, and the counts inside it have already drifted: the top-level README claims 112 skills and `skills/README.md` claims 114, while the tree holds 119 `SKILL.md` files. `web-search-brave` appears in neither README list.
- Install commands do not cover the whole tree. The three category commands in the README reach `creative`, `tech` and `general`, and two skills live in standalone `development` and `education` directories outside them, so a category install is not a full suite.
- Many skills need a runtime and keys. 48 skills ship scripts, most are Deno with read and write permissions, and the search and image skills require paid API keys, so a profile without Deno or those keys gets the advisory half of the suite only.
- Index names drift from the tree. Two listings, `competency-builder` and `skill-maker`, have no directory in the checkout, which instead holds `competency` and `react-pwa`, and `skills/research` mirrors two research skills as `references/` directories with no `SKILL.md` inside, so those paths look installable and are not.

## Related

- [Markdown Viewer Skills - Diagrams, Charts and Cards Setup](/hermes/skills/catalog/markdown-viewer-skills-setup)
- [Motion Design Skills - After Effects and Remotion Setup](/hermes/skills/catalog/motion-design-skills-setup)
- [Kami - PDF, PNG and Editable PPTX Layout Skill Setup](/hermes/skills/catalog/kami-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install by category, not all 119. `creative` alone is 57 skills and most profiles only want the review layer, so take `general` first for the document and research skills and add fiction on demand.
- Read the `type` field before installing. Diagnostic skills review, generator skills write, and orchestrators such as `chapter-drafter` will run several passes at once, which is a much larger token bill than a single review.
- Keep `fact-check` as its own turn. The skill states it cannot be reliably combined with generation in a single pass, and the failure looks like confident prose rather than an obvious error.
- `skill-builder` is the one to read if you plan to add to the collection. It documents the repository's own layout, a `SKILL.md` with `name`, `description`, `license` and a `metadata` block carrying `type` and `mode`, which is also the shape a Hermes profile will classify on.
- Pin what you install. With no root licence and a repository that has not moved since February, a copied directory is the durable record; the skills CLI will happily pull a different tree later.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
