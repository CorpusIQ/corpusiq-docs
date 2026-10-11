---
title: "Journalism Agent Skills - Media Workflows Setup"
description: "Setup guide for jamditis/claude-skills-journalism - 18.9K combined installs. Journalism, FOIA, verification, and data journalism skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-skills-journalism-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "journalism", "research", "media"]
---

# Journalism Agent Skills - Setup Guide

**Source:** [jamditis/claude-skills-journalism](https://www.skills.sh/jamditis/claude-skills-journalism) via skills.sh - 18.9K combined installs across 67 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [jamditis/claude-skills-journalism](https://github.com/jamditis/claude-skills-journalism) (416 stars, MIT license; active - pushed Oct 4, 2026; default branch `master`; 63 SKILL.md files across plugin packages and root-level skill packages)
**Category:** Journalism / Research / Media
**Quality Tier:** 🟡 Beta - 416-star MIT collection; docs site skills.amditis.tech; active Oct 2026; mixed sampled verdicts

James Amditis publishes one of the broadest journalism skill collections on skills.sh: 67 indexed listings covering verification, public records, data journalism, newsroom style, editorial workflow, crisis communications, academic writing, and media production. The same repository serves Claude Code and Codex, keeping Claude-only commands, agents, and hooks clearly labeled while shared skills follow the Agent Skills specification. Documentation lives at skills.amditis.tech, including setup guides and long-form workflow guides on autonomous dev work, multi-agent workflows, and persistent sessions.

The skills ship as plugin packages: journalism-core bundles 15 core skills (AP-style writing, source verification, FOIA and NJ OPRA requests, fact-checking, interview prep and transcription, story pitches, editorial workflow, crisis communications, newsletter publishing, photo metadata), research-toolkit adds six research and academic skills, dev-toolkit covers development work including ethical web scraping, security-toolkit handles defensive security, and smaller packages cover video, PDF design, project templates, and knowledge-base scaffolding. Root-level skill packages (okf-wiki, pdf-design, visual-explainer, web-design-picker) install on their own.

---

## Installation

Use one install path per client; during the Codex pilot, stick to a single Codex installation path per skill or package.

Claude Code plugins (recommended in the README) also add slash commands. Prerequisite: Claude Code installed (`claude --version` to check).

```text
/plugin marketplace add jamditis/claude-skills-journalism
/plugin install journalism-core@claude-skills-journalism
```

Codex can install the journalism-core package through the same marketplace metadata. Prerequisite: Codex CLI installed (`codex --version` to check).

```bash
codex plugin marketplace add jamditis/claude-skills-journalism
codex plugin add journalism-core@claude-skills-journalism
```

The skills CLI installs standards-based skills into the agent's skills directory. Codex example from the README:

```bash
npx skills@latest add https://github.com/jamditis/claude-skills-journalism/tree/master/journalism-core --skill '*' --agent codex --copy -g -y
```

To install a single skill instead:

```bash
npx skills@latest add jamditis/claude-skills-journalism --skill fact-check-workflow --agent codex --copy -g -y
```

Manual route: clone the repo and copy or symlink a skill directory into your agent's skills folder. Claude Code discovers skills at `~/.claude/skills/<skill-name>/SKILL.md`, one level deep:

```bash
git clone https://github.com/jamditis/claude-skills-journalism.git
cp -r claude-skills-journalism/dev-toolkit/skills/web-scraping ~/.claude/skills/
```

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| web-scraping | 6,063 | Ethical scraping patterns: Playwright, robots.txt, anti-bot defense, and terms-of-service discipline (dev-toolkit) |
| academic-writing | 2,859 | Research design, literature reviews, IMRaD structure, peer review responses, and grant proposals (research-toolkit) |
| page-monitoring | 596 | Change detection, RSS generation, webhook alerts, and automatic archiving when monitored pages change (research-toolkit) |
| fact-check-workflow | 545 | Claim extraction, evidence gathering, rating scales, and correction protocols (journalism-core) |

The remaining 63 indexed listings range from 5 to 484 installs.

## Why This Matters for Hermes Agents

Journalism is the discipline of checking things before publishing, which is exactly the discipline most agent workflows lack: sources get cited without verification, claims get repeated without extraction, and research trails go undocumented. This collection encodes the checking habit as skills - SIFT-based source verification, deepfake and C2PA checks, FOIA requests with current statutory citations, fact-check rating scales, and correction protocols - so an agent doing research work can follow a newsroom process instead of an improvisation. The scope reaches well beyond newsrooms: interview transcription pipelines, web archiving for evidence preservation, page-change monitoring, data analysis with chart and map generation, and academic writing all apply to any serious research task an agent runs. The repo also ships multi-agent workflow guides drawn from real newsroom practice (ICIJ, The Markup, Full Fact, Elicit) covering fan-out, pipeline, and adversarial-verify patterns. It is MIT licensed and maintained with a visible catalog control plane and validation scripts, and it serves Claude Code and Codex from one repository. For Hermes agents that research, monitor, and write, this is a strong verification layer to install alongside general-purpose content skills.

## Usage

| You say | What happens |
|---|---|
| "Draft a FOIA request for these records" | foia-requests writes a federal FOIA or NJ OPRA request with current citations, then plans tracking and appeals |
| "Verify this video before we publish it" | source-verification runs the SIFT method with image/video verification, deepfake checks, and C2PA Content Credentials |
| "Fact-check the claims in this draft" | fact-check-workflow extracts claims, gathers evidence, applies a rating scale, and proposes corrections |
| "Analyze this dataset for a story" | data-journalism handles dataset analysis, charts and maps, statistical reasoning, and story structure |
| "Rewrite this headline in AP style" | newsroom-style enforces AP Style, attribution rules, headline formatting, and number conventions |
| "Watch this government page for changes" | page-monitoring detects changes, generates RSS or webhook alerts, and archives the page automatically |
| "Transcribe and quote-check my interview" | interview-transcription runs Whisper/WhisperX pipelines with quote management and speaker diarization |

## Verification

```bash
# Claude Code: plugin skills land under the skills directory
ls ~/.claude/skills/ | grep -i -E "verification|foia|fact-check"

# Codex: user-level install target used by the skills CLI route
ls ~/.agents/skills | grep -i fact-check

# Review a skill file straight from GitHub before installing (default branch: master)
curl -s https://raw.githubusercontent.com/jamditis/claude-skills-journalism/master/dev-toolkit/skills/web-scraping/SKILL.md | head -20
```

The README also documents a clean-install canary that checks the exact global destination for the Codex route.

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| web-scraping | Pass | Pass | Warn |
| data-journalism | Pass | Pass | Pass |
| fact-checking | - | - | - |

## Limitations

- Mixed security profile: web-scraping carries a Snyk Warn in the sampled verdicts, and sampling is uneven across the collection (fact-checking returned no verdicts).
- The Codex package route exposes nested skills only - Claude commands, agents, hooks, and root-level skills are not converted into Codex components.
- Codex installs are pilot-stage: the README warns against mixing installation paths for the same skill identity because Codex does not deduplicate same-name skills across install roots.
- Default branch is master, so raw GitHub URLs and manual clone flows must use master rather than main.
- Skills cite statutes, platform APIs, and vendor behavior that change; the README recommends re-checking older skills against their sources, with last-changed dates on the docs site.
- Snapshot data, verified Oct 10, 2026: 18,912 combined installs across 67 indexed listings; 416 GitHub stars; MIT; last pushed Oct 4, 2026. Counts drift over time.

## Related

- [Academic Research Skills - Paper Pipeline for Agents Setup](/hermes/skills/catalog/academic-research-skills-setup) - adjacent research pipeline for long-form academic work
- [Bright Data Agent Skills - Web Scraping & Research Setup](/hermes/skills/catalog/brightdata-agent-skills-setup) - production-grade scraping to pair with the ethical-scraping skill
- [Research Paper Writing Pipeline - Academic ML/AI Paper Production Setup](/hermes/skills/catalog/research-paper-writing-setup) - writing pipeline for research outputs
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the journalism-core plugin: one install brings all 15 core skills, and the README treats it as the default entry point.
- Prefer the skills CLI route for single skills (for example `fact-check-workflow`) when you do not want an entire plugin package.
- Use one Codex installation path per skill: the repo warns that duplicate identities across install roots are not deduplicated.
- Do not clone the repository directly into `~/.claude/skills` as a nested folder; copy or symlink one level deep so Claude Code discovers each SKILL.md.
- Check the last-changed dates before relying on statutory or platform-citing skills, since the repo tracks changes by git history.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
