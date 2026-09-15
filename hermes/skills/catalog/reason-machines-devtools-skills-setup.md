---
title: Reason Machines DevTools Skills - CLI Skill Farm
description: Setup guide for reason-machines/devtools-skills, the ara.so auto-generated farm of 173 agent skills for trending developer tools - 42 skills at 100+ installs (9,850 combined). Install per-skill with npx skills add.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/reason-machines-devtools-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-15"
tags: ["hermes skill", "agent skill", "developer tools", "skill setup"]
---

# Reason Machines DevTools Skills - Setup Guide

**Source:** [reason-machines/devtools-skills](https://github.com/reason-machines/devtools-skills) (9,850+ installs across the 42 skills at 100+ installs)
**Category:** Developer Tools / CLI Automation
**Quality Tier:** 🟡 Unverified (no skills.sh Trust Hub / Socket / Snyk verdicts published)

`devtools-skills` is an auto-generated skill farm from [ara.so](https://ara.so) (the skills.sh platform operator): a bot scans GitHub every 30 minutes for trending developer-tools repos, ranks them by stars/day, and writes an installable `SKILL.md` for the top new project. 173 skills currently live in the repo. The publisher org was renamed `aradotso` → `reason-machines` on Sep 12, 2026 (GitHub 301 redirect; `reason-machines` is canonical). The repo's `hermes-client-web-ui` skill is documented separately in the catalog.

Provenance caveats, stated honestly: quality varies by source repo (auto-generated), the roster includes niche game-mod and automation skills, the repo carries a NOASSERTION license, 4★, and no skills.sh security audits are published. Cherry-pick production-relevant skills rather than bulk-installing.

---

## Installation

```bash
# Everything (173 skills)
npx skills add reason-machines/devtools-skills

# Single skill (recommended)
npx skills add reason-machines/devtools-skills --skill <skill-name>

# Browse before installing
npx skills add reason-machines/devtools-skills --list
```

Legacy `aradotso/devtools-skills` install paths still resolve via GitHub 301.

## Prerequisites

| Requirement | Details |
|---|---|
| Node.js 18+ | `npx skills` requirement |
| Per-skill tooling | Each SKILL.md wraps an external CLI - install the underlying tool (e.g. Chrome DevTools MCP, OpenAI CLI) as its docs require |
| API keys | Some skills (polymarket, wecom, twitter-cli) need their platform credentials |

## Roster - 42 Skills at 100+ Installs

| Skill | Installs | Wraps |
|---|---|---|
| cc-switch-cli | 316 | Claude Code provider switcher |
| wx-cli-wechat-local-data | 285 | WeChat local data CLI |
| chrome-devtools-mcp-automation | 263 | Chrome DevTools MCP |
| officecli-office-automation | 260 | Office document automation |
| cli-anything-agent-native-software | 257 | CLI-Anything (HKUDS, 43K★) |
| autocli-web-scraping | 257 | AutoCLI web scraping |
| opencli-universal-cli-hub | 256 | OpenCLI (jackwener) |
| op-auto-clicker | 255 | OPAutoClicker |
| polymarket-clob-client | 253 | Polymarket CLOB API |
| wecom-cli-enterprise-wechat | 248 | WeCom enterprise CLI |
| polymarket-clob-client-v2 | 247 | Polymarket CLOB v2 |
| fieldtheory-cli | 244 | FieldTheory CLI |
| deepcode-cli | 244 | DeepCode CLI |
| openai-cli | 242 | OpenAI terminal CLI |
| cli-printing-press-generator | 240 | Printing Press skill generator |
| subnautica-ii-deep-synergy-coop-mod | 238 | Subnautica II coop mod |
| subnautica-2-coop-mod-bepinex | 237 | Subnautica 2 coop mod |
| subnautica-ii-coop-deep-synergy-mod | 236 | Subnautica II coop mod |
| subnautica-ii-coop-multiplayer-mod | 235 | Subnautica II coop mod |
| subnautica-2-deep-synergy-multiplayer-mod | 234 | Subnautica 2 coop mod |
| subnautica-ii-deep-synergy-multiplayer-mod | 232 | Subnautica II coop mod |
| subnautica-ii-coop-bepinex-mod | 228 | Subnautica II coop mod |
| agent-browser-cli-control | 228 | Agent Browser CLI |
| clipify-video-clip-generator | 227 | Clipify video clips |
| claude-devtools-inspector | 227 | Claude DevTools inspector |
| twitter-cli-skill | 226 | Twitter CLI |
| subnautica-2-deep-synergy-coop-mod | 226 | Subnautica 2 coop mod |
| watch-cli-video-agent | 224 | Watch CLI video agent |
| dingtalk-workspace-cli | 224 | DingTalk workspace CLI |
| cliamp-terminal-music-player | 223 | CLIamp music player |
| mcp2cli-runtime-api-tooling | 222 | MCP ↔ CLI API tooling |
| mac-cleaner-cli-disk-cleanup | 220 | Mac disk cleanup CLI |
| github-copilot-cli | 219 | GitHub Copilot CLI |
| byterover-cli-memory-layer | 217 | ByteRover memory layer |
| clipsketch-ai-video-storyboard | 215 | ClipSketch storyboard |
| blur-autoclicker-automation | 214 | Blur autoclicker |
| gooserelayvpn-android-client | 212 | GooseRelay VPN client |
| devtools-hub-installer | 208 | DevTools hub installer |
| sigcli-auth-proxy | 207 | SigCLI auth proxy |
| subnautica-2-coop-mod | 205 | Subnautica 2 coop mod |
| subnautica-ii-coop-mod | 204 | Subnautica II coop mod |
| devtools-debugger-mcp-nodejs | 195 | Chrome DevTools MCP - Node.js debugging |

The remaining 131 skills sit below 100 installs and are excluded from this roster. Roster is the skills.sh API snapshot of Sep 15, 2026 - install counts move as the bot ships new skills.

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Browser automation & verification** | chrome-devtools-mcp-automation for headful verification of docs/social posts |
| **X automation companion** | twitter-cli-skill for post/engagement workflows |
| **API tooling** | mcp2cli-runtime-api-tooling for MCP ↔ CLI bridges |
| **Terminal model access** | openai-cli / github-copilot-cli / deepcode-cli for code + model tasks from the shell |
| **Video clip workflows** | clipify-video-clip-generator / watch-cli-video-agent for UGC clip extraction |
| **Document automation** | officecli-office-automation for Office doc generation |

## Honest Notes / Known Risks

- Auto-generated on a 30-minute cadence - SKILL.md freshness and accuracy vary by source repo
- 8 of the 42 are Subnautica II coop-mod skills - game-modding niche, low ops value
- Automation-adjacent skills present (op-auto-clicker, blur-autoclicker-automation, gooserelayvpn-android-client) - review before use
- NOASSERTION license, 4★, no skills.sh security audits published

## Verification

```bash
# Confirm the skill resolves before installing
npx skills add reason-machines/devtools-skills --list
```

## Security

| Audit | Status |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Hermes Client Web UI - Setup Guide](/docs/hermes/skills/catalog/hermes-client-web-ui-setup)
- [Hermes Labyrinth Observability - Setup Guide](/docs/hermes/skills/catalog/hermes-labyrinth-observability-setup)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
