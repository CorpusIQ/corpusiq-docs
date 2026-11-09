---
title: "Designlang Skill - Extract Any Site's Design System"
description: "manavarya09/design-extract on skills.sh: 3.3K combined installs; one skill that reads a site's design system into DTCG tokens, Tailwind and Figma."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/design-extract-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "design tokens", "tailwind", "figma", "wcag"]
---

# Designlang Skill - Setup Guide

**Source:** [manavarya09/design-extract](https://www.skills.sh/manavarya09/design-extract) via skills.sh - 3,334 installs across 1 indexed listing (3.3K combined); first seen 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 4,969 stars, MIT via LICENSE, `main` branch, last pushed 2026-11-05, one skill at `skills/extract-design/SKILL.md` and 24 further copies of that same file under `website/public/gallery/<site>/.claude/skills/designlang/SKILL.md`
**Category:** Design systems and tokens: reading a live site's palette, type scale, spacing, shadow, radius, motion and component patterns into DTCG tokens, Tailwind, Figma variables and CSS
**Quality Tier:** 🟡 Adequate - MIT license and a single indexed listing at 3,334 installs, with no Fail anywhere, but Trust Hub and Snyk both return Warn on a skill that drives a browser and writes files on every run.

designlang is a Node CLI that points a headless Chromium at a URL through Playwright and reads the design system off the live DOM rather than off the stylesheet. One command against a site produces the palette, type scale, spacing system, shadows, radii, breakpoint set, component inventory and a WCAG contrast score, then writes them out as files a project can adopt: DTCG design tokens, a Tailwind config, CSS custom properties, Figma variable JSON, a shadcn/ui theme, a React theme object, an HTML preview and a markdown summary written for an LLM to read.

This repository is the skill wrapper around that CLI, not the CLI alone. `skills/extract-design/SKILL.md` is 86 lines, declares `allowed-tools: Bash, Read, Write, Glob`, and describes the job as four steps: run the extraction, read the generated markdown, present the findings, offer the next step per output format. It is a short skill on purpose. The value is in the file it tells the agent to read next and in the eight formats it hands back, and both come from the CLI rather than from the instructions.

The install numbers are the odd part. 4,969 stars against 3,334 installs means the repository is being starred faster than it is being installed as a skill, which is the reverse of most listings in this catalog and a sign that most of the attention is on the CLI. Treat the skill as the agent-facing door to a tool that has its own, larger audience.

## Installation

The README's shortest route needs no install at all:

```bash
npx designlang https://stripe.com
```

The persistent route installs the CLI and then fetches the browser it drives:

```bash
npm i -g designlang
designlang install-browser
```

`npm install` no longer pulls a browser down, so the second line is the one that matters in a fresh container. `install-browser` fetches the Chromium build matching the bundled Playwright (add `--with-deps` on bare Linux); without it designlang falls back to an installed Google Chrome. Node 20 or later, no account and no API key are needed for the default path.

The skill itself comes through the skills CLI, which is what the skills.sh listing wraps:

```bash
npx skills add https://github.com/manavarya09/design-extract --skill extract-design
```

Claude Code gets a plugin instead, eleven slash commands wrapping the same CLI:

```text
/plugin marketplace add Manavarya09/design-extract
/plugin install designlang@designlang
```

An MCP route exists for agents that would rather call a tool than shell out. The server itself is `npx -y designlang mcp`, a stdio server that exposes an extraction as a job, and it is registered with the client's own `mcp add` command, which takes the server name followed by the command to run.

In that mode `extract_design(url)` returns a job id, which `get_job_status`, `get_tokens`, `get_colors`, `get_typography`, `get_components`, `get_findings`, `compute_drift` and `export` all consume by id. `export` takes the format as an argument: dtcg, tailwind, shadcn, figma, css or design-md.

## What It Provides

The threshold for this guide is zero installs, so the single indexed listing appears below:

| Skill | Installs | Use For |
|---|---|---|
| extract-design | 3,334 | Pulling a site's palette, type scale, spacing, shadows, components and WCAG contrast score into eight files: DTCG tokens, Tailwind config, CSS variables, Figma variables, shadcn theme, React theme, HTML preview and an LLM-ready markdown summary |

One row clears the threshold, and since the threshold is zero no rows fall below it.

The eight outputs are named in the skill body and each one has a stated consumer. `*-design-language.md` is the LLM context file. `*-preview.html` is the visual report with swatches, type scale, shadows and the accessibility result. `*-design-tokens.json` is W3C Design Tokens format. `*-tailwind.config.js`, `*-variables.css`, `*-figma-variables.json`, `*-theme.js` and `*-shadcn-theme.css` are drop-in artifacts for the five stacks the README calls out.

The command surface is wider than the skill body documents, and the README is the better source for it. Beyond plain extraction there is `slop` for a 0 to 100 genericity score with each AI-design tell named, `verify-ui` for checking a local page against a brand file at several widths and both themes, `site` for crawling canonical pages into one de-duplicated system, `fidelity` for scoring a clone against the original, `dna` for placing a design in a measured space, and `pack`, `brand`, `pair`, `remix`, `theme-swap`, `clone`, `grade` and `battle` for the rest. The skill routes to the first of those; the others are reachable with the same tool and are not described in `SKILL.md`.

## Why This Matters for Hermes Agents

An agent asked to match a brand or continue an existing product has no design vocabulary to reason with unless something extracts one. Given a URL, this skill converts the visual surface of a site into named tokens, and named tokens are the form a model can hold consistently across a long build. That is the difference between an agent that produces a purple gradient dashboard and one that produces the client's actual indigo, their actual radius scale and their actual type ramp.

The second fit is the file format. DTCG tokens, a Tailwind config and a Figma variable export are all diffable text. An agent can be told to use the extracted set as the only source of colour and spacing, and a reviewer can then check that instruction mechanically instead of by eye. Tokens extracted into a scratch directory and never imported into the project give none of that.

The third is the accessibility score. The skill reports contrast as part of the extraction, so the first artifact an agent hands back can carry a real WCAG number rather than an assurance. It is a score of the source site, not of the code the agent writes afterwards, and the distinction is worth keeping straight in a report.

The counterweight is that extraction is not design. A site's tokens describe what that site chose, including choices that fail contrast or collapse at 280px. Copying them wholesale reproduces the flaws along with the look, and nothing in this skill grades whether the source was any good.

## Usage

| You say | What happens |
|---|---|
| "Extract the design system from stripe.com" | Runs the CLI against the URL with screenshots, reads `*-design-language.md`, and reports palette, fonts, spacing base unit, WCAG score and component patterns |
| "What colours and fonts does this site use" | Answers from the extracted file rather than from a screenshot guess, with hex values and family names |
| "Turn this URL into design tokens" | Produces the DTCG JSON plus the Tailwind, CSS, Figma, shadcn and React variants in one run |
| "Make a Tailwind theme from this site" | Runs with `--framework react` or `--framework shadcn` to emit only the requested theme file, and points at the matching config |
| "Is our landing page generic" | Uses `slop` for a 0 to 100 genericity score with each detected AI-design tell and where it was measured |
| "Check our page against our brand" | Runs `verify-ui` against localhost at phone, tablet and desktop widths in both themes, and exits 1 on drift |
| "Score our clone against the original" | Runs `fidelity` with `--clone` and returns one number covering visual and motion halves, plus the correction plan |

## Verification

The skill sits under `skills/` in this repository, and this URL returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/manavarya09/design-extract/main/skills/extract-design/SKILL.md | head -6
```

It should open with YAML frontmatter holding `name: extract-design` and a `description` that lists the eight outputs and the trigger phrases, followed by `allowed-tools: Bash, Read, Write, Glob`. The body below it opens with `# Extract Design Language`. If the `allowed-tools` line is gone, the skill no longer declares what it will run and the file has been rewritten.

The README is the source for anything the 86-line body does not cover:

```bash
curl -fsSL https://raw.githubusercontent.com/manavarya09/design-extract/main/README.md | grep -n "designlang install-browser"
```

A hit there confirms the browser step is still the documented prerequisite. A miss means the install procedure moved and the commands above are stale.

After installing the CLI, check the local stack before the first extraction rather than after a failure:

```bash
designlang doctor
```

That one screen reports Node, playwright, the Chromium binary, the output directory and network reachability, and exits 1 if any of them is wrong. A silent success followed by an empty `design-extract-output/` is usually a missing browser rather than a blocked site.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| extract-design | Warn | Pass | Warn |

Two Warns against one Pass is the right shape for what this skill actually is. The instruction file is 86 lines of Markdown with no payload of its own, but it grants itself Bash, Read, Write and Glob, then shells out to a third-party npm package that opens a browser and writes into the working directory. A static scanner looking at a skill that executes an external CLI should not return a clean Pass, and two of the three did not.

The concrete surface is narrow and worth stating plainly. The extraction makes an outbound request to the URL you name, downloads roughly 150MB of Chromium on first use, and writes eight files to `./design-extract-output` or to `--out`. It holds no credentials and authenticates to nothing. What it does collect is a full picture of a page: computed colours, fonts, spacing, shadows, component structure and screenshots.

The data-egress path to know is `--smart`. That flag routes low-confidence classification to Atlas Cloud through an OpenAI-compatible chat API, using `ATLASCLOUD_API_KEY` and a model named in `ATLASCLOUD_MODEL`. With the flag off, extraction is local. A page behind a login, an unreleased product or anything under NDA should not be extracted with `--smart` set, and the README's sponsor section is why the option exists at all.

The last point is not a scanner finding but it belongs here: extracting a site copies its palette, its type choices and screenshots of its pages into your repository. That is a licensing question about the source, and the output is close enough to the original that it should be treated as derived work until someone decides otherwise.

## Limitations

- Snapshot data, verified 2026-11-09: 3,334 combined installs across 1 indexed listing; 4,969 GitHub stars; MIT license; last pushed 2026-11-05. Counts drift over time.
- One indexed listing means one install number and no second source to cross-check it. 3,334 installs against 4,969 stars also says most of the attention is on the CLI, not on the skill, so the adoption figure understates the tool's use.
- The skill body documents eight output files and a five-command surface. The README describes 17+ files and roughly twenty commands, including `slop`, `verify-ui`, `site`, `fidelity` and `dna`. The instructions trail the tool, so pin a commit or read the README before relying on a command the body never mentions.
- 25 of the 26 `SKILL.md` files in the tree are not extra skills. 24 are per-site copies under `website/public/gallery/` (cal-com, ramp-com, v0-dev and 21 others) and one is `marketplace/claude-code-skill.md`. The index has one listing because there is one skill; a directory count would mislead.
- Extraction depends on the rendered DOM. Client-side pages need `--wait <ms>` or they yield the shell instead of the design, and a page that blocks headless browsers yields nothing at all.
- Both Warns are consistent with a skill that executes an external CLI, and the security verdicts are a snapshot: re-check the skills.sh page before putting this in a pipeline.

## Related

- [Extract Design System - UI Token & Component Extraction Setup](/hermes/skills/catalog/extract-design-system-setup)
- [Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup)
- [Uizze UI Skills - Anti-UI-Slop Design Quality Setup](/hermes/skills/catalog/uizze-ui-skills-setup)
- [Bergside Design Skills - Design Systems Setup](/hermes/skills/catalog/bergside-awesome-design-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `designlang doctor` first, not after. It checks the five things that actually break (Node, playwright, the Chromium binary, the output directory, network) and exits 1 so a script can stop.
- Ask for the tokens, not the screenshots, when the goal is to build on a system. The DTCG JSON and the Tailwind config are what an agent can diff and a reviewer can check; the preview HTML is for a person.
- Add `--dark` on any site that ships two themes. A single-mode extraction hands the agent one palette and it will apply that palette to both modes without being told.
- `verify-ui` exits 1 on drift, which makes it the one command here that drops into CI without extra glue. The extraction itself has no pass or fail, only output.
- Extract into a scratch directory and read the markdown file before letting the agent write code from it. Eight files of plausible tokens are exactly the input that produces confident, wrong UI.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
