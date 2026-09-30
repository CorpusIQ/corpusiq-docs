---
title: "Sep 29, 2026 - Record Sweep: 64 New Publisher Clusters"
description: "Skills.sh sweep: 64 new publisher setup guides (GSAP 443K, Jeff Allan 395K, K-Skill 425K, Nature Skills 226K, OKX 223K, .NET 207K + 58 more) and 29 roster reconciles."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-sep29-2026-skills/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "skill marketplace", "skills.sh"]
---

# Sep 29, 2026 - Record Sweep: 64 New Publisher Clusters

**Discovered:** 64 new publisher clusters (~98,947 combined installs) · **Guides created:** 64 · **Roster reconciles:** 29

Daily sweep of the skills.sh REST API across 15 queries (`hermes`, `hermes agent`, `hermes skill`, `hermes automation`, `nousresearch/hermes-agent`, `aradotso/hermes-skills`, `garrytan/gbrain`, `plastic-labs/honcho`, `aradotso/devtools-skills`, `sickn33/antigravity-awesome-skills`, `kcchien/clawpilot`, `rethinking-studio/clawpilot-skills`, `varnan-tech/opendirectory`, `cosmicstack-labs/mercury-agent-skills` + publisher follow-up cluster sizing). 723 unique skills collected, 106 NEW / 234 PARTIAL after cross-reference. NEW >=100 installs: 66. Every candidate >=100 installs received a setup guide, grouped by publisher (64 clusters). 29 existing publisher guides received roster reconciles for missing skills.

**Infra note:** this sweep also fixed a silent failure in the sweep pipeline - ripgrep was missing on the Mac Mini worker, causing the official sweep script's grep fallback to run at O(skills x tree) (hours). ripgrep 14.1.1 installed at ~/bin/rg.

## New Publishers at a Glance (top 14 by combined installs)

| # | Publisher | Top Skill | Combined Installs | Top Install | Setup Guide |
|---|-----------|-----------|-------------------|-------------|-------------|
| 1 | upstash/skills | upstash-redis-js | 14335 | 14335 | [guide](/docs/hermes/skills/catalog/upstash-skills-setup) |
| 2 | gargantuax/gemini-watermark-remover | gemini-watermark-remover | 12828 | 12828 | [guide](/docs/hermes/skills/catalog/gemini-watermark-remover-setup) |
| 3 | dotnet/skills | configuring-opentelemetry-dotnet | 5735 | 3467 | [guide](/docs/hermes/skills/catalog/dotnet-skills-setup) |
| 4 | ziniao-open/skills | ziniao-shared | 5268 | 5268 | [guide](/docs/hermes/skills/catalog/ziniao-open-skills-setup) |
| 5 | nomadamas/k-skill | k-dart | 5246 | 4476 | [guide](/docs/hermes/skills/catalog/k-skill-setup) |
| 6 | thedivergentai/gd-agentic-skills | godot-master | 3988 | 3988 | [guide](/docs/hermes/skills/catalog/gd-agentic-skills-setup) |
| 7 | muratcankoylan/agent-skills-for-context-engineering | context-engineering-collection | 3933 | 3933 | [guide](/docs/hermes/skills/catalog/context-engineering-skills-setup) |
| 8 | zc277584121/marketing-skills | chrome-automation | 3771 | 3771 | [guide](/docs/hermes/skills/catalog/zc277584121-marketing-skills-setup) |
| 9 | marimo-team/skills | marimo-batch | 3402 | 3402 | [guide](/docs/hermes/skills/catalog/marimo-skills-setup) |
| 10 | frames-engineering/skills | agentwallet | 2490 | 2490 | [guide](/docs/hermes/skills/catalog/frames-engineering-skills-setup) |
| 11 | aas-ee/open-websearch | open-websearch | 2097 | 2097 | [guide](/docs/hermes/skills/catalog/open-websearch-setup) |
| 12 | zaddy6/agent-email-skill | agent-email-cli | 2066 | 2066 | [guide](/docs/hermes/skills/catalog/agent-email-cli-setup) |
| 13 | daffy0208/ai-dev-standards | animation-designer | 1978 | 1807 | [guide](/docs/hermes/skills/catalog/ai-dev-standards-skills-setup) |
| 14 | dohooo/helmor | helmor-cli | 1968 | 1968 | [guide](/docs/hermes/skills/catalog/helmor-skills-setup) |
| 15 | mindrally/skills | selenium-automation | 1880 | 1204 | [guide](/docs/hermes/skills/catalog/mindrally-skills-setup) |
| 16 | celigo/ai | managing-on-premise-agents | 1698 | 1698 | [guide](/docs/hermes/skills/catalog/celigo-ai-skills-setup) |
| 17 | hugomrtz/skill-vetting-clawhub | clawhub-skill-vetting | 1656 | 1656 | [guide](/docs/hermes/skills/catalog/clawhub-skill-vetting-setup) |
| 18 | actionbook/rust-skills | core-dynamic-skills | 1523 | 1523 | [guide](/docs/hermes/skills/catalog/actionbook-rust-skills-setup) |
| 19 | bergside/awesome-design-skills | skeumorphism | 1471 | 1471 | [guide](/docs/hermes/skills/catalog/bergside-awesome-design-skills-setup) |
| 20 | ifuryst/open-codex-computer-use | open-computer-use | 1432 | 1432 | [guide](/docs/hermes/skills/catalog/open-computer-use-setup) |
| 21 | thesysdev/openui | openui | 1336 | 1336 | [guide](/docs/hermes/skills/catalog/openui-setup) |
| 22 | martinholovsky/claude-skills-generator | windows-ui-automation | 1291 | 1291 | [guide](/docs/hermes/skills/catalog/claude-skills-generator-setup) |
| 23 | microsoftdocs/mcp | microsoft-skill-creator | 1201 | 1201 | [guide](/docs/hermes/skills/catalog/microsoft-learn-mcp-skills-setup) |
| 24 | flightclaw/agents | flightclaw | 1082 | 1082 | [guide](/docs/hermes/skills/catalog/flightclaw-agents-setup) |
| 25 | codestable/codestable | cs-guide | 1073 | 1073 | [guide](/docs/hermes/skills/catalog/codestable-skills-setup) |
| 26 | manutej/luxor-claude-marketplace | expressjs-development | 1036 | 530 | [guide](/docs/hermes/skills/catalog/luxor-claude-marketplace-setup) |
| 27 | volcengine/openviking | openviking | 900 | 900 | [guide](/docs/hermes/skills/catalog/openviking-setup) |
| 28 | shaivpidadi/freeride | freeride | 784 | 784 | [guide](/docs/hermes/skills/catalog/freeride-setup) |
| 29 | aktsmm/agent-skills | skill-finder | 663 | 663 | [guide](/docs/hermes/skills/catalog/aktsmm-agent-skills-setup) |
| 30 | different-ai/openwork | opencode-bridge | 631 | 631 | [guide](/docs/hermes/skills/catalog/openwork-skills-setup) |
| 31 | joellewis/finance_skills | portfolio-management-systems | 631 | 631 | [guide](/docs/hermes/skills/catalog/joellewis-finance-skills-setup) |
| 32 | boshu2/agentops | pr-plan | 600 | 600 | [guide](/docs/hermes/skills/catalog/boshu2-agentops-setup) |
| 33 | tech-leads-club/agent-skills | technical-design-doc-creator | 565 | 565 | [guide](/docs/hermes/skills/catalog/tech-leads-club-skills-setup) |
| 34 | copilotkit/skills | copilotkit-self-update | 564 | 564 | [guide](/docs/hermes/skills/catalog/copilotkit-skills-setup) |
| 35 | mosif16/codex-skills | ios-ux-design | 526 | 526 | [guide](/docs/hermes/skills/catalog/mosif16-codex-skills-setup) |
| 36 | glittercowboy/taches-cc-resources | create-agent-skills | 502 | 502 | [guide](/docs/hermes/skills/catalog/taches-cc-resources-setup) |
| 37 | dylantarre/animation-principles | physics-intuition | 494 | 494 | [guide](/docs/hermes/skills/catalog/dylantarre-animation-principles-setup) |
| 38 | majiayu000/spellbook | harmonyos-app | 489 | 489 | [guide](/docs/hermes/skills/catalog/majiayu000-spellbook-setup) |
| 39 | ifuryst/open-browser-use | open-browser-use | 446 | 446 | [guide](/docs/hermes/skills/catalog/open-browser-use-setup) |
| 40 | openai/openai-agents-python | openai-knowledge | 439 | 439 | [guide](/docs/hermes/skills/catalog/openai-agents-python-skills-setup) |
| 41 | pluggyai/agent-skills | pluggy-open-finance | 434 | 434 | [guide](/docs/hermes/skills/catalog/pluggyai-agent-skills-setup) |
| 42 | spencerpauly/awesome-cursor-skills | building-skills-from-patterns | 416 | 416 | [guide](/docs/hermes/skills/catalog/awesome-cursor-skills-setup) |
| 43 | asif2bd/openclaw-token-optimizer | token-optimizer | 398 | 398 | [guide](/docs/hermes/skills/catalog/openclaw-token-optimizer-setup) |
| 44 | hedera-dev/hedera-skills | Hedera Hackathon Submission Validator | 390 | 198 | [guide](/docs/hermes/skills/catalog/hedera-skills-setup) |
| 45 | google-antigravity/antigravity-sdk-python | google-antigravity-sdk | 348 | 348 | [guide](/docs/hermes/skills/catalog/google-antigravity-sdk-setup) |
| 46 | mathruffian-dot/antigravity-lazy-pack | antigravity-lazy-packs | 310 | 176 | [guide](/docs/hermes/skills/catalog/antigravity-lazy-pack-setup) |
| 47 | bagelhole/devops-security-agent-skills | openclaw-local-mac-mini | 263 | 263 | [guide](/docs/hermes/skills/catalog/bagelhole-devops-security-skills-setup) |
| 48 | rysweet/amplihack | pm-architect | 245 | 245 | [guide](/docs/hermes/skills/catalog/amplihack-setup) |
| 49 | copilotkit/copilotkit | copilotkit-cli | 227 | 227 | [guide](/docs/hermes/skills/catalog/copilotkit-copilotkit-skills-setup) |
| 50 | travisjneuman/.claude | hr-talent | 214 | 214 | [guide](/docs/hermes/skills/catalog/travisjneuman-claude-toolkit-setup) |
| 51 | somasays/skill-creator | create-skills | 207 | 207 | [guide](/docs/hermes/skills/catalog/somasays-skill-creator-setup) |
| 52 | decentraland/sdk-skills | player-physics | 202 | 202 | [guide](/docs/hermes/skills/catalog/decentraland-sdk-skills-setup) |
| 53 | dzhng/skills | eval-skills | 201 | 201 | [guide](/docs/hermes/skills/catalog/dzhng-skills-setup) |
| 54 | coleam00/skills | skills-create | 198 | 198 | [guide](/docs/hermes/skills/catalog/coleam00-skills-setup) |
| 55 | manojbajaj95/claude-gtm-plugin | skill-navigator | 191 | 191 | [guide](/docs/hermes/skills/catalog/claude-gtm-plugin-setup) |
| 56 | eachlabs/skills | age-transformation | 182 | 182 | [guide](/docs/hermes/skills/catalog/eachlabs-skills-setup) |
| 57 | xbtlin/ai-berkshire | earnings-team | 175 | 175 | [guide](/docs/hermes/skills/catalog/ai-berkshire-setup) |
| 58 | zcyynl/claw-multi-agent | claw-multi-agent | 168 | 168 | [guide](/docs/hermes/skills/catalog/claw-multi-agent-setup) |
| 59 | yakoub-ai/phaser4-gamedev | phaser-physics | 160 | 160 | [guide](/docs/hermes/skills/catalog/phaser4-gamedev-setup) |
| 60 | aahl/skills |  | 0 | 0 | [guide](/docs/hermes/skills/catalog/aahl-skills-setup) |
| 61 | greensock/gsap-skills |  | 0 | 0 | [guide](/docs/hermes/skills/catalog/greensock-gsap-skills-setup) |
| 62 | jeffallan/claude-skills |  | 0 | 0 | [guide](/docs/hermes/skills/catalog/jeffallan-claude-skills-setup) |
| 63 | okx/onchainos-skills |  | 0 | 0 | [guide](/docs/hermes/skills/catalog/okx-onchainos-skills-setup) |
| 64 | yuan1z0825/nature-skills |  | 0 | 0 | [guide](/docs/hermes/skills/catalog/nature-skills-setup) |

Full list: 64 guides, one per publisher cluster (all >=100 installs; verified against GitHub repos + skills.sh follow-up queries Sep 29, 2026).

## Roster Reconciles (29 guides updated)

Missing skill names added to existing publisher guides - highlights: taste-skill (804K), microsoft/azure-skills (443K), github/awesome-copilot (129K), wshobson/agents (101K), samber/cc-skills-golang (75K), affaan-m/ecc (56K), claude-office-skills (46K), langchain-ai (45K), addyosmani (38K), expo (33K), google/skills (32K), agentmemory (29K), googleworkspace (28K), deepline (12K), forcedotcom/sf-skills (10K), openclaw/carapace (7.9K), agentic-awesome (7K), openclaw/openclaw (5.1K), clawdirect (4.6K), nousresearch/hermes-agent (3.4K) + 9 more.

## Skipped / Parked (below-bar)

NEW skills under 100 installs (top 16 shown; 40 total parked):

| Publisher | Skill | Installs |
|-----------|-------|----------|
| velumkai/metacognition-skill | metacognition | 80 |
| gmh5225/awesome-skills | awesome-skills-overview | 64 |
| kingstar-omega/claude-token-optimizer | antigravity-protocol | 60 |
| sandraschi/advanced-memory-mcp | windsurf-ide-integration | 56 |
| latitude-dev/skills | latitude-telemetry | 55 |
| numman-ali/openskills | my-first-skill | 50 |
| mims-harvard/tooluniverse | tooluniverse-antigravity-plugin | 48 |
| wjgoarxiv/antigravity-swarm | antigravity-swarm | 47 |
| crazymsn/academic-skills | astropy | 36 |
| outfitter-dev/agents | hono-dev | 31 |
| ratacat/claude-skills | figma-design-sync | 29 |
| cocacha12/agent-skills | skill-antigravity | 28 |
| ada20204/antigravity-sync-mcp | antigravity-mcp | 27 |
| ratacat/claude-skills | data-integrity-guardian | 26 |
| drshailesh88/integrated_content_os | astropy | 26 |
| thegovind/claude-scientific-skills | astropy | 23 |

---

*← [Skills Marketplace](/docs/hermes/skills/marketplace) | [Skills Catalog](/docs/hermes/skills/catalog) →*
*Powered by CorpusIQ*
