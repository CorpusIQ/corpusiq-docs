---
title: "Mobbin Skills - UI Reference Research Setup"
description: "mobbin/skills: official Mobbin skills for UI reference research, screen redesign and plain-writing reports - 6.4K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/mobbin-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "ui design", "mobile design", "mcp"]
---

# Mobbin Skills - UI Reference Research Setup

**Source:** [mobbin/skills](https://www.skills.sh/mobbin/skills) via skills.sh - 6.4K combined installs across 5 indexed listings; first seen Nov 21, 2026 (Nov 21, 2026 morning sweep)
**GitHub:** [mobbin/skills](https://github.com/mobbin/skills) - 75 stars, MIT license, main branch, last pushed Nov 12, 2026; four skills under `skills/<name>/SKILL.md` plus plugin manifests for Antigravity, Claude, Codex, Cursor, Devin, Grok and Kimi.
**Category:** UI and UX Design Reference
**Quality Tier:** 🟡 Yellow - 5 of 5 sampled skills pass Gen Agent Trust Hub and Socket; 2 Snyk Warns, 0 Fails.

Mobbin publishes this skills package to help agents design and build UI against Mobbin, its subscription library of UI and UX design references from real mobile apps, web apps and websites. The package installs both the Mobbin skills and the Mobbin MCP server, which is how an agent queries the Mobbin library for screens, flows and sections.

Mobbin is a paid service: on first use your agent opens a browser to sign in, and you need a Pro, Team or Enterprise plan. The four skills are contextual and auto-load by conversation: best-practices explains what Mobbin can and cannot do, search improves every Mobbin query, redesign-screen rebuilds a screen from patterns real apps ship, and plain-writing rewrites Mobbin reports so they read like a person wrote them. First seen in the Nov 21, 2026 morning sweep.

## Installation

Use the native plugin where supported; it installs both the skills and the Mobbin MCP server:

```bash
codex plugin marketplace add mobbin/skills
codex plugin add mobbin@mobbin
```

```bash
claude plugin marketplace add mobbin/skills
claude plugin install mobbin@mobbin
```

Or from inside a Claude Code session:

```
/plugin marketplace add mobbin/skills
/plugin install mobbin@mobbin
```

Antigravity CLI:

```bash
agy plugin install https://github.com/mobbin/skills
```

If your agent only supports the Agent Skills standard, install the skills separately and add the MCP server to your config:

```bash
npx skills add mobbin/skills
```

```json
{
  "mcpServers": {
    "mobbin": {
      "url": "https://api.mobbin.com/mcp"
    }
  }
}
```

On first use your agent opens a browser to sign in to Mobbin; you need a Pro, Team or Enterprise plan.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| best-practices | 1,792 | what Mobbin and its MCP can and cannot do, and how the Mobbin skills work together |
| search | 1,790 | writing queries that return screens, flows and sections that match what you are building |
| redesign-screen | 1,041 | redesigning a screen, section or component from patterns real apps ship, with a before and after image and a short report |
| plain-writing | 980 | rewriting Mobbin reports so they read like a person wrote them, without changing a fact |
| mobbin-search | 777 | indexed listing with no matching directory in the current tree; the search skill covers Mobbin search |

All 5 indexed listings clear the 500-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

UI work is where an agent's lack of taste shows first: a generated screen can be technically correct and still look like a template. Mobbin gives the agent a ground truth of what real, shipped apps actually do for a given screen, so a redesign is anchored in evidence rather than in the model's guess about what design looks like. The search skill forces the agent to pick a mode, write an effective query and pull more results, which is the difference between a reference that matches the task and one that is merely adjacent.

The redesign-screen skill is the workhorse: it keeps whatever already works, explores directions grounded in Mobbin collections or saved screens, and returns a before and after image plus a short report, so a human can see the evidence behind each change. The plain-writing skill strips the tells of AI-generated prose from every Mobbin report, which matters because the report is the thing a client actually reads. Everything goes through the Mobbin MCP server, so the agent can only query the library for the account it is signed into, and Mobbin itself is a paid subscription service.

## Usage

| You say | What happens |
|---|---|
| How do real apps lay out an onboarding screen? | Searches Mobbin for matching screens, flows and sections from shipped apps |
| Redesign this signup screen but keep what works | Finds how apps handle the same screen and returns a before and after image plus a short report |
| Show me a few directions for this dashboard | Explores variations grounded in Mobbin collections or saved screens |
| Write up the redesign in plain language for the team | Rewrites the Mobbin report so it reads like a person wrote it |
| What can Mobbin actually do for me? | Explains what Mobbin and its MCP can and cannot do before any search runs |

## Verification

Confirm the MCP server is registered, then review the best-practices skill before installing, since it decides when Mobbin is the right tool:

```bash
ls ~/.claude/plugins/mobbin/skills 2>/dev/null || ls skills
```

```bash
curl -sL https://raw.githubusercontent.com/mobbin/skills/main/skills/best-practices/SKILL.md | head -40
```

On first use your agent opens a browser to sign in to Mobbin. Confirm the sign-in succeeds and the MCP server returns a search result before running a redesign.

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| best-practices | Pass | Pass | Pass |
| search | Pass | Pass | Warn |
| redesign-screen | Pass | Pass | Warn |
| plain-writing | Pass | Pass | Pass |
| mobbin-search | Pass | Pass | Pass |

The skills read from a paid Mobbin account through the MCP server, so scope the connected account to the workspace you intend to query. Read the skill instructions before granting access to a shared team account.

## Limitations

- Snapshot data, verified Nov 21, 2026: 6,380 combined installs across 5 indexed listings; 75 GitHub stars; MIT license; last pushed Nov 12, 2026. Counts drift over time.
- Mobbin is a paid subscription service: first use requires a Pro, Team or Enterprise plan and a browser sign-in.
- Index-versus-tree drift: mobbin-search carries an install count but has no matching directory in the current tree, which ships four skill directories against five indexed listings.
- The skills query the Mobbin library through the MCP server, so what an agent can retrieve depends on the server's tool surface, not on the skill files alone.
- Two of the five sampled skills carry Snyk Warn cells; read the skill instructions before pointing the agent at a shared team account.
- The plugin manifests target Antigravity, Claude, Codex, Cursor, Devin, Grok and Kimi; other agents install the skills and MCP server separately.

## Related

- [Mobile App UI Design Skill - Mobile Interface Setup](/hermes/skills/catalog/mobile-app-ui-design-skill-setup)
- [Appllama Skills - Mobile App Design Patterns Setup](/hermes/skills/catalog/appllama-skills-setup)
- [Sleek Design Mobile Apps - AI Mobile App Design Skill Setup](/hermes/skills/catalog/sleek-design-mobile-apps-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read best-practices before any Mobbin work: it is the only skill that tells the agent when Mobbin is the wrong tool for the job.
- Run search with an explicit mode and query; the skill exists to make references match the task rather than merely look adjacent.
- Keep redesign scope tight: the skill preserves what already works, so point it at one screen or section at a time.
- Let plain-writing finish every report before it reaches a client; it removes AI-writing tells without changing a fact.
- Save promising screens to a Mobbin collection so redesign-screen can ground variations in what you have already approved.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
