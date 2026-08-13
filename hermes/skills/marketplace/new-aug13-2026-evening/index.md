---
title: New Skills — August 13, 2026 (Evening)
description: "skills.sh sweep — 12 new publisher clusters, 244 skills, 3.5M+ installs: Emil Kowalski design engineering (694K), Convex backend (757K), UI/UX Pro Max (611K), Higgsfield AI video (577K), OSINT (286K), Wind financial (133K), Momentic QA (119K), Planning With Files (91K), Wonda CLI (75K), SquirrelScan (71K), Solana (58K), Genkit (57K)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-aug13-2026-evening/"
robots: "index,follow"
last_updated: "2026-08-13"
tags: ["hermes skill", "agent skill", "skill marketplace", "skills.sh"]
sweep_id: aug-13-2026-evening
new_publishers: 12
new_skills: 244
guides_drafted: 12
---

# New Skills — August 13, 2026 (Evening)

**Source:** [skills.sh](https://skills.sh) all-time + trending (24h) leaderboards
**Date:** August 13, 2026
**Result:** 12 new publisher clusters · 244 skills · 3.5M+ listed installs · 12 setup guides

The largest single-run sweep to date. Executed from the Spark node after the Mac Mini went offline (SSH timeout); the full leaderboard (top 600 all-time) was pulled, every publisher cross-referenced against the 413-entry catalog, and 12 undocumented clusters were guided. Headlined by Emil Kowalski's design-engineering suite (694K installs) and Convex's 46-skill backend platform pack (757K).

---

## New Publishers (12) — All with Setup Guides

| # | Publisher | Skills | Installs | Setup Guide |
|---|-----------|:------:|---------:|-------------|
| 1 | get-convex/agent-skills | 46 | 756.9K | [convex-agent-skills-setup](/hermes/skills/catalog/convex-agent-skills-setup/) ✍️ |
| 2 | emilkowalski/skills | 10 | 694.4K | [emilkowalski-skills-setup](/hermes/skills/catalog/emilkowalski-skills-setup/) ✍️ |
| 3 | nextlevelbuilder/ui-ux-pro-max-skill | 19 | 611.4K | [ui-ux-pro-max-setup](/hermes/skills/catalog/ui-ux-pro-max-setup/) ✍️ |
| 4 | higgsfield-ai/skills | 10 | 577.3K | [higgsfield-skills-setup](/hermes/skills/catalog/higgsfield-skills-setup/) ✍️ |
| 5 | useosint/osint-skills | 57 | 285.8K | [osint-skills-setup](/hermes/skills/catalog/osint-skills-setup/) ✍️ |
| 6 | wind-information-co-ltd/wind-skills | 82 | 132.6K | [wind-skills-setup](/hermes/skills/catalog/wind-skills-setup/) ✍️ |
| 7 | momentic-ai/skills | 5 | 118.9K | [momentic-skills-setup](/hermes/skills/catalog/momentic-skills-setup/) ✍️ |
| 8 | othmanadi/planning-with-files | 7 | 90.5K | [planning-with-files-setup](/hermes/skills/catalog/planning-with-files-setup/) ✍️ |
| 9 | degausai/wonda | 1 | 74.6K | [wonda-setup](/hermes/skills/catalog/wonda-setup/) ✍️ |
| 10 | squirrelscan/skills | 2 | 71.4K | [squirrelscan-skills-setup](/hermes/skills/catalog/squirrelscan-skills-setup/) ✍️ |
| 11 | solana-foundation/solana-dev-skill | 1 | 58.4K | [solana-dev-skill-setup](/hermes/skills/catalog/solana-dev-skill-setup/) ✍️ |
| 12 | genkit-ai/skills | 4 | 57.3K | [genkit-skills-setup](/hermes/skills/catalog/genkit-skills-setup/) ✍️ |

---

## Highlights

### Convex Agent Skills — 756.9K, 46 skills
The largest single-platform developer-experience cluster outside Microsoft Azure. Agents stand up a full TypeScript backend — schema, auth, crons, domains, billing, deploy guards — end to end. Twenty-nine expert sub-skills cover every lifecycle stage from `convex-quickstart` through `convex-self-heal` and `convex-launch-readiness`.

### Emil Kowalski Skills — 694.4K, 10 skills
The highest-signal design-quality layer on skills.sh, from the creator of Sonner. `emil-design-eng` (204K) plus a full motion-craft stack: review animations adversarially, improve them like a senior engineer, find where animation is missing, and pick the right UI library before writing code. The natural complement to `anti-ui-slop`.

### Wind Skills — 132.6K, 82 skills
China's Bloomberg-equivalent data terminal goes agent-native. `wind-mcp-skill` (93.8K) wires Wind's feeds into agents; 79 research workflows cover DCF models, valuation snapshots, backtests, earnings analysis, and investor-persona reasoning lenses (Buffett, Munger, Taleb, Naval). The strongest signal yet of institutional finance moving to agent-native tooling.

### OSINT Skills — 285.8K, 57 skills
The largest investigation cluster on skills.sh. Flagships verify media (`is-this-photo-real`, `find-the-original-image`) and audit personal exposure (`what-leaked-about-you`); the long tail covers domain recon, breach analysis, geolocation, crypto tracing, and intel-brief writing.

### Planning With Files — 90.5K, 7 skills
The ecosystem answer to context loss: persist task plans, findings, and decisions to disk so interrupted agents resume cleanly. Seven language editions including Simplified Chinese (16.8K) and a personal-intelligence variant.

---

## Still Pending (logged from prior sweeps)

- **fandhe-ai** and **novel-to-game** — not on current leaderboards; need direct publisher URL discovery
- **site/docs.stripe.com** — Stripe's site-registry skills (observed on the hot board: `connect-required-verification-information`); fetch `https://www.skills.sh/site/docs.stripe.com` next cycle
- **huaweicloud/huaweicloud-skills** — the full 82-skill cluster beyond the Flexus Hermes deployment guide already published
- Smaller zero-hit clusters not yet guided (install counts from all-time board): agentix-cloud (51.6K), huashu-design (42.6K), make-interfaces-feel-better (51K), momentic captured, nia (54.9K), pexo (39.4K), vue-best-practices (36.5K), fastify-best-practices (35K), hallmark (40.7K), design-doc-mermaid (33.4K), anysearch (~36K), hugmouse (35.5K), replicas (34.7K)

## Sweep Notes

- Mac Mini unreachable this cycle (SSH timeout); sweep ran fully from Spark with the local clone and token at `~/.hermes/profiles/corpusiq/secrets/github.token` — the documented fallback path
- Cross-reference method: extracted all 128 publisher slugs from the cached full leaderboard, grep-batched against `hermes/skills/`, zero-hit set then fetched in batches of 5
- Two publisher pages (squirrelscan, wonda) timed out on first fetch and succeeded on retry; Firecrawl 504s are transient
