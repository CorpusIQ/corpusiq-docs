---
title: "Adjfks Corner Skills - Xiaohongshu and Debug Skills Setup"
description: "adjfks/corner-skills: 4.9K combined installs across 4 listings; Xiaohongshu note writing plus MCP debugging, code review, and debug-mode skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/adjfks-corner-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "xiaohongshu", "mcp debugging", "code review"]
---

# Adjfks Corner Skills - Setup Guide

**Source:** [adjfks/corner-skills](https://www.skills.sh/adjfks/corner-skills) via skills.sh - 4.9K combined installs across 4 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 morning sweep)
**GitHub:** 5 stars, no licence file, `main` branch, last pushed 2026-06-02. Four skills are plain SKILL.md directories under skills/, and the repo README is empty.
**Category:** Xiaohongshu content publishing and developer debugging
**Quality Tier:** 🟠 Orange - no licence file; write-xiaohongshu carries 2 Warns (Socket, Snyk) among 4 sampled skills.

adjfks/corner-skills is a small four-skill collection with one content skill and three developer debugging aids. write-xiaohongshu researches and publishes Xiaohongshu notes, while the other three target hard-to-find bugs: stdio MCP server debugging in VS Code, a multi-agent code review council, and an interactive debug mode for Claude Code.

The install count is heavily skewed: write-xiaohongshu carries 4,810 of the 4,909 combined installs. The repo has no plugin manifest and an empty README, so each skill is installed by copying its directory into a skills path.

## Installation

The repo README is empty and there is no plugin manifest, so installation is a manual copy into a skills directory. The debug-mode skill documents the pattern, which applies to the other three skill directories the same way:

```bash
git clone https://github.com/adjfks/corner-skills.git
cp -r corner-skills/skills/debug-mode ~/.claude/skills/debug-mode
```

Use .claude/skills/ inside a repo for project scope, then restart Claude Code. debug-mode is entered with /debug-mode; write-xiaohongshu, debug-mcp-stdio, and code-review-council activate on their own triggers.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| write-xiaohongshu | 4,810 | Research top-performing Xiaohongshu image posts, analyze titles and comments for emotional patterns, then write and publish an XHS note with a title of 20 characters or fewer and a body of 1000 or fewer, via Firecrawl and Xiaohongshu MCP. |
| debug-mcp-stdio | 45 | Debug a Node.js stdio MCP server in VS Code by attaching to Node Inspector, producing a launch.json, an inspector command, and a prioritized troubleshooting checklist. |
| code-review-council | 35 | Run a multi-agent code review council that analyzes a code task from several roles in parallel, covering structure, bugs, library choice, and refactor impact, and cross-checks a single answer. |
| debug-mode | 19 | Drive a Cursor-style interactive debug mode: hypothesis, runtime instrumentation, log verification, and manual repro before fix, entered with /debug-mode in Claude Code. |

No indexed listings fall below the threshold; all 4 appear above.

## Why This Matters for Hermes Agents

For an agent that writes and publishes Xiaohongshu content, the difference between a note that lands and one that is ignored is research: which titles, formats, and emotional hooks already perform. write-xiaohongshu encodes that research step and hard output limits, so the agent does not produce an over-length note the platform trims or rejects.

The three debugging skills target bugs a single-pass answer misses. code-review-council runs several reviewer roles in parallel and cross-checks them, which catches errors a single perspective would not. debug-mcp-stdio turns a broken stdio MCP server into a reproducible VS Code attach workflow, and debug-mode forces a hypothesis-first loop with runtime instrumentation and log verification instead of guessing.

All four are plain SKILL.md files, so a harness that reads skill files, including Hermes, can load them directly. The only external dependencies are the two MCP servers write-xiaohongshu uses, which are separate installs.

## Usage

| You say | What happens |
|---|---|
| "Write a Xiaohongshu note about this product" | write-xiaohongshu researches top posts, then writes and publishes an XHS note within the 20-character title and 1000-character body limits. |
| "My stdio MCP server is not hitting breakpoints" | debug-mcp-stdio gives a launch.json, an inspector command, and a prioritized checklist for VS Code attach debugging. |
| "Review this code change from several angles" | code-review-council runs multiple reviewer roles in parallel and cross-checks the answer. |
| "/debug-mode this list does not refresh" | debug-mode lists hypotheses, adds runtime instrumentation, and waits for a manual repro before fixing. |
| "Is this library the right choice for this task?" | code-review-council evaluates API usage, version compatibility, and known pitfalls. |

## Verification

Probe one skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/adjfks/corner-skills/main/skills/write-xiaohongshu/SKILL.md
```

After copying, confirm the skill directory is present under ~/.claude/skills/ and that /debug-mode appears in Claude Code's command list.

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - the repo has no licence file. Re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| write-xiaohongshu | Pass | Warn | Warn |
| debug-mcp-stdio | Pass | Pass | Pass |
| code-review-council | Pass | Pass | Pass |
| debug-mode | Pass | Pass | Pass |

The sample covers all 4 indexed listings; write-xiaohongshu carries a Socket Warn and a Snyk Warn, and every other cell passes.

## Limitations

- Snapshot data, verified Nov 19, 2026: 4,909 combined installs across 4 indexed listings; 5 GitHub stars; no licence file; last pushed 2026-06-02. Counts drift over time.
- The repo README is empty and there is no plugin manifest or one-line installer, so setup is a manual copy of each skill directory.
- There is no licence file, so treat the repo as all-rights-reserved rather than open source.
- write-xiaohongshu depends on Firecrawl MCP and Xiaohongshu MCP, which are separate, unmanaged installs; the skill does not bundle them.
- debug-mcp-stdio assumes VS Code, and debug-mode assumes Claude Code and Node.js on the machine.

## Related

- [Xiaohongshu Skills - RED Content Operations](/hermes/skills/catalog/xiaohongshu-skills-setup)
- [Code Review Skill - 20+ Language Review Guides](/hermes/skills/catalog/code-review-skill-setup)
- [MCP Client - MCP Client Operations Setup](/hermes/skills/catalog/mcp-client-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install only what you need: most of the value here is write-xiaohongshu; the debugging skills are for VS Code and Claude Code users.
- Set up Firecrawl MCP and Xiaohongshu MCP before relying on write-xiaohongshu; the skill calls them at run time.
- Use debug-mode for state and async bugs, not typos; the skill itself says not to enable it for obvious one-line fixes.
- Keep the copy pattern identical for every skill directory so updating means re-copying the folder.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
