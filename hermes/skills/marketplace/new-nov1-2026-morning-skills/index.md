---
title: "New Skills - November 1, 2026"
description: "Skills.sh sweep (Nov 1): 14 publisher guides for 179.8K combined installs across 476 indexed listings from the standing queue."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov1-2026-morning-skills/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 1, 2026 Morning Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window returned 885 unique skills with 0 failed queries: 85 NEW, 265 PARTIAL.

The standing window was silent above the 1,000-install trigger for the twenty-seventh consecutive fire, its top NEW row reading 316 installs, so this fire drained the queue the October 31 fires left behind: fourteen of the twenty-two undocumented sources still above the 5,000-install floor.

Every guide was built from a pre-verified pack holding the exact per-listing install figures, a depth-1 clone with its branch, licence and skill directories, and three-auditor verdicts sampled at the top of each index. Each draft was then checked with three gates: the format gate, the pack cross-check at a per-guide threshold, and the frontmatter audit. All 42 gate runs passed on the orchestrator re-run after an md5 comparison of the three canonical scripts.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 885 (0 failed queries) |
| NEW (not in catalog) | 85 |
| PARTIAL (source known, skill not cataloged) | 265 |
| Above-floor finds in the standing window | 0 (top row 316) |
| Undocumented above-floor sources in the queue | 22 |
| Guides published this fire | 14 |
| Combined installs documented | 179,773 |
| Indexed listings covered | 476 |

## Publisher Guides

| Guide | Repository | Installs | Listings | Stars | License |
|---|---|---|---|---|---|
| [Syncfusion Angular UI Skills - Vendor Component Pack](/hermes/skills/catalog/syncfusion-angular-ui-skills-setup) | [syncfusion/angular-ui-components-skills](https://github.com/syncfusion/angular-ui-components-skills) | 17,636 | 61 | 0 | no LICENSE file |
| [ChatGPT Skills - 12-Suite Deterministic Toolkit](/hermes/skills/catalog/chatgpt-skills-setup) | [dkyazzentwatwa/chatgpt-skills](https://github.com/dkyazzentwatwa/chatgpt-skills) | 16,721 | 106 | 126 | no LICENSE file |
| [Huashu Skills - 22-Skill Content Production Pack](/hermes/skills/catalog/huashu-skills-setup) | [alchaincyf/huashu-skills](https://github.com/alchaincyf/huashu-skills) | 16,023 | 37 | 2147 | MIT |
| [VectorBT Backtesting Skills - Quant Workflow Setup](/hermes/skills/catalog/vectorbt-backtesting-skills-setup) | [marketcalls/vectorbt-backtesting-skills](https://github.com/marketcalls/vectorbt-backtesting-skills) | 15,152 | 6 | 217 | no LICENSE file |
| [Slack Skills Plugin - MCP Plus Nine Slack Skills](/hermes/skills/catalog/slack-skills-plugin-setup) | [slackapi/slack-skills-plugin](https://github.com/slackapi/slack-skills-plugin) | 15,188 | 9 | 163 | MIT |
| [QwenCloud AI Skills - Multimodal Suite Setup](/hermes/skills/catalog/qwencloud-ai-setup) | [qwencloud/qwencloud-ai](https://github.com/qwencloud/qwencloud-ai) | 15,120 | 10 | 44 | Apache-2.0 |
| [Full Stack Skills - 788-Skill Catalog for Agents](/hermes/skills/catalog/full-stack-skills-setup) | [partme-ai/full-stack-skills](https://github.com/partme-ai/full-stack-skills) | 14,932 | 102 | 718 | Apache-2.0 |
| [Supabase Pentest Skills - 24-Skill Audit Suite](/hermes/skills/catalog/supabase-pentest-skills-setup) | [yoanbernabeu/supabase-pentest-skills](https://github.com/yoanbernabeu/supabase-pentest-skills) | 13,050 | 25 | 73 | NOASSERTION |
| [Startup OS Skills - Sales, Product and Video Pack](/hermes/skills/catalog/startup-os-skills-setup) | [ncklrs/startup-os-skills](https://github.com/ncklrs/startup-os-skills) | 12,860 | 53 | 53 | no LICENSE file |
| [AgentMail Skills - Agent Email Inbox Setup](/hermes/skills/catalog/agentmail-skills-setup) | [agentmail-to/agentmail-skills](https://github.com/agentmail-to/agentmail-skills) | 10,705 | 11 | 25 | no LICENSE file |
| [Awesome Android Agent Skills - Compose and Kotlin Setup](/hermes/skills/catalog/awesome-android-agent-skills-setup) | [new-silvermoon/awesome-android-agent-skills](https://github.com/new-silvermoon/awesome-android-agent-skills) | 9,948 | 18 | 998 | Apache-2.0 |
| [Shenzjd Skills - DevOps and AI Image Pack](/hermes/skills/catalog/shenzjd-skills-setup) | [wu529778790/shenzjd-skills](https://github.com/wu529778790/shenzjd-skills) | 7,887 | 16 | 4 | MIT |
| [Robust Skills - Architecture and Platform Suite](/hermes/skills/catalog/robust-skills-setup) | [ccheney/robust-skills](https://github.com/ccheney/robust-skills) | 7,780 | 12 | 61 | MIT |
| [Awesome Finance Skills - Market Analysis Pack](/hermes/skills/catalog/awesome-finance-skills-setup) | [rkiding/awesome-finance-skills](https://github.com/rkiding/awesome-finance-skills) | 6,771 | 10 | 3094 | Apache-2.0 |

## What The Batch Covers

Three of the fourteen are **official vendor packs** rather than community work: Slack's own plugin repository, which pairs a hosted Slack MCP server with nine skills, Syncfusion's Angular component skills, and QwenCloud's multimodal suite. Two more are large catalogues rather than single packs: partme-ai/full-stack-skills is a navigation hub for 788 skill entries across 51 separately installable packages, and alchaincyf/huashu-skills covers only the 22 built-in skills of a three-layer Chinese content catalogue.

The batch splits by domain: five are engineering suites (Angular components, full stack, Android, architecture, DevOps), four are data and analysis (vectorbt backtesting, QwenCloud multimodal, Supabase penetration testing, finance market analysis), three are business or product operating sets (startup OS, AgentMail, Slack) and two are document and content production (ChatGPT skills, Huashu).

One guide leads with a FAIL rather than a Warn: shenzjd-skills carries a Snyk E005 on the two skills that write executable workflow and hook files. Nine carry Warns on the skills that reach the network, fetch live documentation or run package installs, and in each case the guide names the code and describes the surface rather than interpreting what the code means. Two high-install sources are deliberately inventory-grade: partme-ai/full-stack-skills is a directory of separately installable packages, and dkyazzentwatwa/chatgpt-skills ships twelve directories behind 106 indexed listings, so ten of its above-threshold rows have nothing to install.

## Related

- [Skills Catalog](/hermes/skills/catalog)
- [Skills Marketplace](/hermes/skills/marketplace)
- [October 31, 2026 Evening Sweep](/hermes/skills/marketplace/new-oct31-2026-evening-skills)

---

*[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)*
*Powered by CorpusIQ*
