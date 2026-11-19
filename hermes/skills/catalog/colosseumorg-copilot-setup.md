---
title: "Colosseum Copilot - Crypto Startup Research Setup"
description: "colosseumorg/colosseum-copilot: 4.5K combined installs across 1 listing; agent skill for crypto startup research, project histories, and tool guidance."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/colosseumorg-copilot-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "crypto", "startup research", "solana"]
---

# Colosseum Copilot - Setup Guide

**Source:** [colosseumorg/colosseum-copilot](https://www.skills.sh/colosseumorg/colosseum-copilot) via skills.sh - 4.5K combined installs across 1 indexed listing; first seen Nov 19, 2026 (Nov 19, 2026 morning sweep)
**GitHub:** 15 stars, no licence file (the skill declares Proprietary), `main` branch, last pushed 2026-11-17. One skill directory, skills/colosseum-copilot/, with a SKILL.md and 13 reference files.
**Category:** Crypto startup research and tool guidance
**Quality Tier:** 🟠 Orange - the sampled skill carries a Snyk Fail, and the repo has no open-source licence file.

Colosseum Copilot connects an agent to Colosseum's evidence base - project histories, crypto archives, and The Grid - so the agent can answer questions, weigh founder decisions, and choose tools for crypto or onchain startups. Solana is the deepest evidence base; other ecosystems have uneven coverage.

Protected evidence requires a Colosseum account, and installation uses Node.js 20 or later with npx. The single listing carries all 4,508 combined installs.

## Installation

```bash
npx skills add ColosseumOrg/colosseum-copilot -g
npx @colosseum-org/copilot-connect@0.2.3 login
npx @colosseum-org/copilot-connect@0.2.3 status
```

Installing globally replaces an older Copilot skill in place. If an older project copy exists, remove it with npx skills remove colosseum-copilot so it cannot load instead. For OpenClaw, add -a openclaw. Default login opens the browser with PKCE; use login --device for remote environments or blocked callbacks. Credentials stay in the helper's protected storage, so do not paste tokens into chat.

For tool picks from the same hub without signing in, the lighter colosseum-resources skill covers it (npx skills add ColosseumOrg/colosseum-resources).

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| colosseum-copilot | 4,508 | Research Colosseum project histories, competitors, ideas, program questions, and tool choices, and give feedback on your own crypto or onchain projects, drafts, submissions, and team. |

The single indexed listing clears the threshold and appears in the table above.

## Why This Matters for Hermes Agents

For a builder evaluating a crypto startup idea, the hard part is evidence: what did similar projects actually do, what happened after they launched, and which tools are still supported. Colosseum Copilot grounds those answers in project histories and primary sources instead of a model's memory.

The skill separates submission-time claims from later outcomes and cites dates, which is the discipline a research agent needs when the stakes are a funding decision. It also recommends tools for an existing stack, including offchain or existing-provider approaches when appropriate, rather than defaulting to the newest onchain option.

The connection helper keeps credentials in protected storage and sends Colosseum only the API queries it needs; it does not upload repositories, and sharing conversations is opt-in. The SKILL.md is plain text, but the real value is the authenticated evidence access behind it.

## Usage

| You say | What happens |
|---|---|
| "Compare two stablecoin payment project histories" | The agent separates submission-time claims from later outcomes and cites dates, flagging what remains unknown. |
| "Which payment tools should I evaluate for my stack?" | The agent checks current support and explains tradeoffs against your existing stack and customers. |
| "Give feedback on my hackathon draft" | The agent reviews the draft against Colosseum program context and prior projects. |
| "What should I know before choosing this tool?" | The agent pulls tool guidance from the shared hackathon tool hub. |

## Verification

Probe the skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/ColosseumOrg/colosseum-copilot/main/skills/colosseum-copilot/SKILL.md
```

Then run npx @colosseum-org/copilot-connect@0.2.3 status after login and confirm the connection shows as active.

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - the repo has no open-source licence file (the skill declares Proprietary). Re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| colosseum-copilot | Pass | Pass | Fail |

The single sampled skill carries a Snyk Fail; Gen Agent Trust Hub and Socket pass.

## Limitations

- Snapshot data, verified Nov 19, 2026: 4,508 combined installs across 1 indexed listing; 15 GitHub stars; no licence file; last pushed 2026-11-17. Counts drift over time.
- The skill is proprietary, copyright Colosseum, with no open-source licence; public visibility does not grant reuse rights.
- Protected evidence requires a Colosseum account; without it the skill is limited to public data.
- Solana has the deepest coverage; other ecosystems are uneven.
- v1 tokens stopped working at 00:00 UTC on October 28, 2026, so older setups must update the skill and sign in with the helper.

## Related

- [Solana Dev Skill - Blockchain Development Setup](/hermes/skills/catalog/solana-dev-skill-setup)
- [Coinbase Agentic Wallet - USDC Payments Skill](/hermes/skills/catalog/coinbase-agentic-wallet-setup)
- [GMGN Agent Skills - On-Chain Analytics and Trading Setup](/hermes/skills/catalog/gmgn-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use login --device in remote or headless environments where the PKCE browser callback is blocked.
- If you installed an older project copy, run npx skills remove colosseum-copilot in that project so the stale skill cannot load.
- Opt in to sharing only if you accept your questions and the agent's answers being retained for 12 months; the default is off.
- For read-only tool picks without an account, use the lighter colosseum-resources skill instead.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
