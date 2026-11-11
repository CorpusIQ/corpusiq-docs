---
title: "Self-Learning Skill - Agent Improvement Setup"
description: "Autonomous skill generator: 3.4K combined installs across 1 indexed listing, researching libraries on the web into a reusable SKILL.md"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/self-learning-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-10"
tags: ["hermes skill", "agent skill", "skill setup", "skill authoring", "self-improvement", "web research"]
---

# Self-Learning Skill - Setup Guide

**Source:** [philschmid/self-learning-skill](https://www.skills.sh/philschmid/self-learning-skill) via skills.sh - 3.4K combined installs across 1 indexed listing (3,432 exact); first seen Feb 6, 2026 (Nov 10, 2026 sweep)
**GitHub:** 97 stars, Apache-2.0 license, `main` branch, last pushed 2026-02-06, one `SKILL.md` at `skills/self-learning/SKILL.md`, with a single companion document at `skills/self-learning/references/skill_creation_guide.md`
**Category:** Agent self-improvement: turning corrections and session outcomes into durable learnings
**Quality Tier:** 🟠 Experimental - one listing from a single commit day, no updates since February, and all three scanners warn; take the procedure, not the plumbing.

This is the smallest possible shape of an agent that can teach itself a new library. The repository holds one skill, one reference document, a README and a license: no plugin, no CLI, no scripts. You invoke it as `/learn <topic>`, it searches the web for official documentation, pulls the installation, concept and API sections out of three to five pages, and writes a new `SKILL.md` into the agent's skills directory. The generated skill is then available like any other.

The author is Philipp Schmid, and the format is credited in the README to `hyperbrowserai/examples/skills`. Both the repository and the skills.sh listing first appear on 2026-02-06, the same date as the only push, which is why the repo reads as a published example of a technique rather than a maintained tool. That matters for how you adopt it: the value on offer is the numbered research procedure and its four rules against fabrication, and every path and tool name inside it belongs to a different agent runtime than Hermes.

The interesting part is the constraint set. Instead of asking an agent to write a skill about a library it half remembers, the skill forces source discovery first, caps the source count so the context stays readable, records a scrape date per source, and refuses to proceed when discovery fails. Those four rules are the difference between a skill grounded in documentation and a skill that confidently invents an API surface.

## Installation

The README has no CLI installer. It says to copy the `SKILL.md` and its `references/` folder into the agent's skills directory, and names two Antigravity locations: `.agent/skills/self-learning/` for a workspace-scoped install and `~/.gemini/antigravity/skills/self-learning/` for a global one.

That layout is the first thing to change for Hermes. Clone the repository and copy the whole skill directory, which already has the `SKILL.md` plus `references/` shape Hermes expects:

```bash
git clone https://github.com/philschmid/self-learning-skill
cp -R self-learning-skill/skills/self-learning ~/.hermes/profiles/corpusiq/skills/self-learning
```

Confirm the files landed:

```bash
ls ~/.hermes/profiles/corpusiq/skills/self-learning
ls ~/.hermes/profiles/corpusiq/skills/self-learning/references
```

The repository ships nothing else: a README, a license, the `SKILL.md` and one reference document. There is no plugin manifest, no `npx skills` instruction in the README, and no configuration step. If you would rather keep the skill inside a project, put the same directory under the project's own skills path instead of the profile one.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| self-learning | 3,432 | Autonomous skill generator that researches an unfamiliar library, framework or tool through web search and synthesizes the authoritative pages into a reusable `SKILL.md`. |

No indexed listings fall below the threshold.

The skill body is a numbered procedure. Topic intake normalizes the subject to kebab-case for filenames and asks a clarifying question when the name is ambiguous, with three worked examples in the file: `react` resolves to React for web, React Native or a specific library such as react-query; `apollo` to the GraphQL client, Server or Federation; `aws` to a named service. Discovery then runs four search patterns (official documentation, getting started, API reference, GitHub repository) and ranks results with official docs sites first, official GitHub repositories second, official blogs third, capped at three to five URLs. If nothing credible turns up, the skill asks you for a URL instead of improvising.

Extraction keeps five things per page (installation, core concepts, API reference, common patterns, version) and explicitly drops navigation, ads, login prompts, sidebars, comments and forums. Pages that fail to read because they are JavaScript-heavy route to a browser subagent with a fixed extraction prompt. Each source gets a scrape timestamp in `YYYY-MM-DD`. Generation reads `references/skill_creation_guide.md` first, then writes a description that states when to use the skill, a step-by-step workflow, and valid YAML frontmatter, with optional `scripts/`, `references/` and `assets/` directories. The file closes with four critical rules: never hallucinate documentation, never invent APIs, ask for URLs when discovery fails, and prefer official sources over third-party tutorials.

## Why This Matters for Hermes Agents

Every agent eventually meets a library it was not trained on, and the default failure is fluent and wrong: an import path that moved two versions ago, a config key that never existed, a method signature from a blog post written against the previous major. The cost is not the wrong answer itself, it is that the wrong answer was plausible enough to ship.

This skill attacks that at the source. By capping the research at three to five official URLs and requiring a scrape date, it makes the evidence set small enough to audit and old enough to notice. The instruction to ask for a URL when discovery fails is the part most agents skip, and it is the only one that reliably prevents a fabricated skill.

The output format is a real Hermes artifact. Hermes loads skills from directories holding `SKILL.md`, so a generated skill needs no conversion once the save path is corrected, and the trigger-description requirement matches how Hermes decides when a skill applies. That makes the procedure reusable as a template even if you never run the file as shipped.

The hard edge is portability. The skill calls `search_web`, `read_url_content`, `browser_subagent` and `write_to_file`, which are Antigravity tool names, and it saves to `.agent/skills/` or `~/.gemini/antigravity/skills/`. Hermes has none of those tools under those names and neither path. Run it unmodified and the likely outcome is an agent that narrates the steps and writes nothing, or writes into a directory nothing reads.

## Usage

| You say | What happens |
|---|---|
| "/learn drizzle-orm" | Runs the four discovery searches, picks up to five official pages, extracts installation and API sections, and writes `drizzle-orm/SKILL.md` with a trigger description and workflow |
| "/learn react" | Stops at intake to ask whether you mean React for web, React Native or a specific library such as react-query before any search runs |
| "/learn stripe" | Resolves the product name, pulls the official docs and API reference, and records a scrape date for each source it used |
| "/learn" with no topic | Prints the usage line instead of guessing a subject |
| "/learn some-internal-tool" | Finds no credible source, asks you for a URL, and refuses to synthesize from memory |
| "/learn next-auth" on a JavaScript-heavy docs site | Falls back to the browser subagent with the fixed extraction prompt covering installation, concepts and code examples |

## Verification

The skill lives one directory below the repository root. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/philschmid/self-learning-skill/main/skills/self-learning/SKILL.md | head -4
```

It should open with frontmatter holding `name: self-learning` and a quoted description beginning `Autonomous skill generator that learns new technologies from the web`, followed by the delimiter and the instruction body. The companion reference is a second fetch:

```bash
curl -fsSL https://raw.githubusercontent.com/philschmid/self-learning-skill/main/skills/self-learning/references/skill_creation_guide.md | head -5
```

After copying, confirm the install is a directory holding `SKILL.md` and a `references/` subdirectory, since the generation step reads that file by relative path and fails silently without it.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-10) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| self-learning | Warn | Warn | Warn |

All three scanners warn on the single listing, which is the reason the tier is orange rather than yellow. A Warn is not a malware finding. It means at least one scanner saw something it would not sign off without a human look, and on a skill like this the candidates are visible in the text: it is instructed to browse arbitrary pages, it writes files into a directory the agent later trusts, and its content is whatever a search engine returned. Three warns on one file is a prompt to read that file, not a reason to skip the install.

Three properties need your own review before production use. First, the write step turns scraped web content into standing instructions that the agent will load in future sessions, so a poisoned or simply wrong page becomes a durable belief rather than a bad answer. Second, the browser fallback hands a URL to a subagent with minimal scoping, which is the classic prompt-injection surface. Third, nothing in the skill validates the generated `SKILL.md` after writing it: no schema check, no diff review, no revert. Read every generated skill before it survives a session.

## Limitations

- Snapshot data, verified 2026-11-10: 3,432 combined installs across 1 indexed listing; 97 GitHub stars; Apache-2.0; last pushed 2026-02-06. Counts drift over time.
- The repository was created and last pushed on the same day, 2026-02-06, and has had no commits in the nine months since. The skills.sh listing carries the same first-seen date, so the install count is demand for an idea rather than adoption of a maintained tool.
- Written for Antigravity, not Hermes. Tool names (`search_web`, `read_url_content`, `browser_subagent`, `write_to_file`) and both save paths belong to that runtime; adopting it on Hermes means editing the body, and an unedited copy will stall or write where nothing reads.
- The published file's numbering starts at `### 2. Discover Sources` immediately after the usage block, so step 1 exists only as implied topic intake. Treat the list as a lightly edited draft and read the whole file before running it.
- A single research pass with three to five sources and no evaluation step. There is no test that the generated skill works, no check that the cited APIs still exist, and no re-scrape later, so the output is as good as the pages that happened to rank that day.
- One maintainer, no repository description and no packaging beyond the raw directory. There is no release process to notice a change in behaviour, so pin the copy you install.

## Related

- [Hermes Agent Skill Authoring - Official SKILL.md Writing Guide](/hermes/skills/catalog/hermes-agent-skill-authoring-setup)
- [Memory Hygiene Setup](/hermes/skills/catalog/memory-hygiene-setup)
- [Deep Research Skill - Citation-Tracked Research Setup](/hermes/skills/catalog/claude-deep-research-skill-setup)

## Pro Tips

- Copy the procedure, not the file. Rewrite the tool reference for your agent's search and fetch tools and change the two save paths to your Hermes profile skills directory, or the run stops at the first tool call.
- Ask for a narrow topic. `/learn drizzle-orm` produces a usable skill; `/learn databases` produces a summary of nothing, because the three-to-five source cap cannot cover a category.
- Keep the scrape timestamps in the generated file and add the version you targeted. Six months later that line is the only way to know whether the skill is describing the library you now run.
- Read the generated skill before the next session starts. It becomes trusted instruction immediately, and a wrong API written into it is worse than no skill at all.
- Pair it with a memory or research hygiene pass rather than using it alone. The self-learning loop decides what to write, not whether what it wrote is true.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
