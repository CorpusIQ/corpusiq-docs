---
title: "Claude Blog - AI Blog Writing and SEO Plugin Setup"
description: "agricidaniel/claude-blog on skills.sh: 79.5K combined installs across 33 listings; 32 blog skills for research, writing, SEO and GEO."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-blog-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "blog writing", "seo", "geo"]
---

# Claude Blog - Setup Guide

**Source:** [agricidaniel/claude-blog](https://www.skills.sh/agricidaniel/claude-blog) via skills.sh - 79.5K combined installs across 33 indexed listings; first seen 2026-11-07 (Nov 7, 2026 evening sweep)
**GitHub:** 2,672 stars, MIT, last pushed 2026-11-03, 33 SKILL.md files: 32 skill directories under `skills/` plus the separate `brain/SKILL.md`, with 5 agent definitions in `agents/` and 30 `/blog` commands
**Category:** Blog production: research, drafting, SEO checks, fact-checking, GEO and AEO readiness, multilingual publishing
**Quality Tier:** 🟡 Yellow - MIT with a LICENSE file in the root, but all three sampled skills carry a Snyk warn and the plugin installs Python tooling that makes paid API calls.

This is a complete publishing pipeline dressed as a skill. The usual shape of a blog skill is a prompt that says "write a good post"; this one routes a request to one of 32 sub-skills, writes the article, scores it out of 100, sends it to an independent reviewer that can block delivery, and runs five gates before the file appears. The README describes the reviewer as scoring every post and refusing anything under 90 or with an unresolved P0.

The architecture is the interesting part for anyone building their own agent workflows. `blog` is an orchestrator that routes by intent, `blog-write` owns the long path from research to delivery, and the review skills (`blog-seo-check`, `blog-factcheck`, `blog-analyze`, `blog-geo`) are separate because they are useful on posts you did not write with the tool. That separation is why the install is worth it even if you never use the writing half.

## Installation

The documented route is the Claude Code plugin marketplace. Run these inside Claude Code, then restart it. Python 3.11 or newer is required:

```bash
/plugin marketplace add AgriciDaniel/claude-blog
/plugin install claude-blog@agricidaniel-blog
```

The analyzer's dependencies install separately, and rendering, screenshots and generated heroes need the optional presentation extra from `pyproject.toml`. Without a renderer, gate 3 blocks delivery rather than skipping it:

```bash
pip install -r requirements.txt
```

There is also a standalone installer for Unix, macOS and Windows. The README recommends cloning, reviewing the scripts, then installing a pinned revision:

```bash
git clone https://github.com/AgriciDaniel/claude-blog.git
cd claude-blog
git checkout <commit-sha-or-release-tag>
chmod +x install.sh
./install.sh
```

That installer writes the skills to `~/.claude/skills/` and the agents to `~/.claude/agents/`, according to its own header. It accepts a full commit SHA or a release tag from v2.3.0 on, and the header is explicit that a full SHA is preferred for pinning.

The README carries no skills CLI line. skills.sh indexes the repository, so the CLI route also works, but confirm the skill name in the current tree first:

```bash
npx skills add agricidaniel/claude-blog
npx skills add agricidaniel/claude-blog --skill blog-seo-check
```

Nothing in the repository documents a Hermes specific flag. The skills are plain folders with a `SKILL.md`, so the portable path is to copy the `skills/` tree into the agent skills directory, the same layout the installer uses.

## What It Provides

Seventeen listings clear the 2,600-install threshold, and the ordering reads like a single install that fans out:

| Skill | Installs | Use For |
|---|---|---|
| blog | 2,956 | Router for the set: sends a request to writing, rewriting, analysis, outlines, audits, schema or charts |
| blog-seo-check | 2,765 | Post-writing on-page checklist: title clarity, meta description, heading order, internal and external links |
| blog-factcheck | 2,726 | Fetches every cited URL and checks the claimed statistic actually appears on the page |
| blog-analyze | 2,712 | 100-point score across content quality, SEO, E-E-A-T, technical elements and AI citation readiness |
| blog-audit | 2,699 | Whole-blog health scan: quality scores, orphan pages, cannibalization, stale content |
| blog-brief | 2,694 | Content brief with keywords, search intent, template choice, SERP gaps and sourced statistics |
| blog-geo | 2,686 | AI citation readiness audit for one post, with per-surface notes for the answer engines |
| blog-calendar | 2,671 | Dated monthly or quarterly editorial calendar with content mix and a review queue |
| blog-chart | 2,659 | Internal SVG chart generation called by write and rewrite, not by the user directly |
| blog-write | 2,655 | New article from a topic through research, drafting, review and the five delivery gates |
| blog-image | 2,652 | Paid Gemini hero and inline images plus OG cards, with consent before the first paid call |
| blog-cannibalization | 2,646 | Finds posts competing for the same keyword and clusters the semantic overlap |
| blog-audio | 2,641 | Paid Gemini text to speech for a summary, a full read or a two-speaker dialogue |
| blog-outline | 2,639 | SERP-informed H2 and H3 outline with word targets and chart placement markers |
| blog-rewrite | 2,622 | Rewrites an existing post for Google SEO and AI citation visibility in one pass |
| blog-repurpose | 2,617 | Turns one post into X threads, LinkedIn posts, short video scripts and newsletter excerpts |
| blog-google | 2,605 | Credentialed Google calls: PageSpeed, CrUX, Search Console, GA4, NLP entities and Keyword Planner |

The remaining 16 indexed listings range from 233 to 2,598 installs.

Two of the tail entries are worth naming because they are easy to miss in a table cut at the threshold. `blog-schema` (2,598) generates the JSON-LD structured data, and `blog-persona` (2,594) builds the writing personas that the rest of the set reads. Both sit a few installs under the cut and both matter if you want the output to look like one publication.

## Why This Matters for Hermes Agents

The failure mode for an agent writing content is confident unsourced prose. A model asked for "a blog post about X" produces structure and cadence immediately, and the statistics in it are often plausible and unverifiable. The fact-check skill addresses that directly: it extracts the load-bearing claims, fetches each cited URL, and checks whether the number is on the page. That is a mechanical check, not a judgement call, which is why it works.

The second failure is a score with no meaning. Everyone has a "SEO score". This one is a five-category rubric with a deterministic analyzer underneath and a reviewer that can refuse delivery. Whether you agree with the rubric, the structure is auditable, and the delivery gates stop a weak post from being presented as done.

Third, the set treats Google ranking and AI citation as one discipline with two outputs. Answer-first structure, sourced passages, entity clarity and Schema.org markup serve both, and the GEO skill audits the second axis explicitly. For teams whose traffic now includes ChatGPT and AI Overviews, that is the gap most content tooling leaves open.

For a Hermes agent the useful split is between generation and inspection. The inspection skills run on any markdown file in a repository, including posts a human wrote, so they fit an existing site without adopting the whole writing pipeline.

The cost is weight. This is 32 skills, 5 agents, Python dependencies and paid APIs, which is a lot of machinery for a small site. Install it when the bottleneck is a publishing cadence, not when you need one post.

## Usage

| You say | What happens |
|---|---|
| "Write a post about best CRM for freelancers" | `/blog write` researches sources, drafts the article, runs the reviewer and the five gates, then renders markdown, HTML and PDF |
| "Is this post ready for AI answers?" | `/blog geo` audits one file for self-contained passages, entity clarity and crawler access, with per-surface notes |
| "Check every claim in this draft" | `/blog factcheck` extracts the claims, fetches each source and reports which ones the page does not support |
| "Score the posts we already have" | `/blog analyze` runs the 100-point rubric on one file or a folder, and `blog-audit` extends it to the whole blog |
| "Which posts compete for the same keyword?" | `/blog cannibalization` clusters titles and headings and flags the posts fighting for one search intent |
| "Plan next quarter" | `/blog calendar` builds a dated calendar with content mix and a material-change review queue |
| "Turn this post into LinkedIn and X copy" | `/blog repurpose` produces draft text per channel and saves it next to the source |

## Verification

Read the router before installing the set. This path returned HTTP 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-blog/main/skills/blog/SKILL.md | head -20
```

It should open with `name: blog` and a description that names the sub-skills, the 100-point scoring and the five agents, which is how you confirm you have the orchestrator and not a leftover file.

After install, confirm the skill count. The tree holds 32 skill directories besides the brain, so a `blog` prefix count of 32 is the expected shape:

```bash
ls ~/.claude/skills | grep -c '^blog'
```

Then run `/blog` in the session and check that the command list matches the README's six groups. If the command list is empty, the plugin installed but Claude Code has not restarted, and the skills are not loaded yet.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07). This is a snapshot, so re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| blog | Pass | Pass | Warn |
| blog-seo-check | Pass | Pass | Warn |
| blog-factcheck | Pass | Pass | Warn |

The warn is consistent across all three samples, which usually means one shared pattern rather than a defect in each skill. The shared surface here is Python: the analyzer runs `scripts/analyze_blog.py`, the renderer pulls Patchright, WeasyPrint and Pillow, and the installers run shell scripts that copy files into your home directory. Pin a commit before running `install.sh` and read it first, which is what the README recommends.

Two skills spend money. `blog-image` and `blog-audio` call the Gemini API and both ask for explicit consent before the first paid call, so the guard exists but the cost is real and lands on your key.

`blog-factcheck` and `blog-discourse` fetch external pages, and `blog-google` uses stored Google credentials for Search Console, GA4 and PageSpeed. That means the tool reads your analytics and sends queries out, so decide which credentials it may hold before you point it at a production property.

The licence is MIT with a `LICENSE` file in the root, and a `NOTICE` file sits beside it, which is unusual for a repo of this size and worth reading before redistribution.

## Limitations

- Snapshot data, verified 2026-11-07: 79,486 combined installs across 33 indexed listings; 2,672 GitHub stars; MIT; last pushed 2026-11-03. Counts drift over time.
- Python 3.11 or newer is required, and the presentation extra adds Patchright, WeasyPrint, Pillow and google-genai. Without a renderer, gate 3 blocks delivery instead of skipping that check, so a bare install can look broken rather than degraded.
- Two skills spend money per call. `blog-image` and `blog-audio` use Gemini's paid endpoints and ask for consent first, which is a guard rather than a budget.
- `blog-chart` is internal. Its own description says it is not user-invocable and is called by write and rewrite, so do not expect it to answer a direct request.
- The README describes 32 skills and 30 commands. The tree holds 33 `SKILL.md` files, because `brain/` is the separate `claude-blog-brain` scaffold at 233 installs, which sits below the table threshold.
- The reviewer is opinionated and the delivery gates are strict. A post that fails a gate is reported as failed, not softened, so budget time for a second pass on anything with an unsourced statistic.

## Related

- [Content Strategy - Full Planning Framework for Hermes](/hermes/skills/catalog/content-strategy-setup)
- [SEO GEO Claude Skills - 20-Skill SEO & Generative](/hermes/skills/catalog/seo-geo-claude-skills-setup)
- [Digital Marketing Pro - AI Marketing OS Setup](/hermes/skills/catalog/digital-marketing-pro-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `/blog analyze` on three posts you already published before writing anything new. The score distribution tells you whether the rubric agrees with your own judgement.
- Read the gate definitions in the plugin before trusting a delivery. Five gates that each block are only useful if you know which one fired.
- Keep the paid skills off until you need them. Set the API key only for the session that generates images or audio, and approve the cost each time.
- Use `blog-geo` on your best performing post first. If the audit finds nothing to fix there, the tool is telling you something about the rubric.
- The brief and outline skills are the cheap half. They cost a few minutes and prevent the expensive case, which is a well written post aimed at the wrong query.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
