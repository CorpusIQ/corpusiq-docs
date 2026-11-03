---
title: "Tons of Skills - Agent Skills Marketplace Platform"
description: "jeremylongshore/tons-of-skills-marketplace: 17.0K combined installs. A ccpi-backed skills marketplace with 137 listings, not one skill family."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/tons-of-skills-marketplace-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "marketplace", "ccpi", "plugin catalog", "package manager"]
---

# Tons of Skills - Setup Guide

**Source:** [jeremylongshore/tons-of-skills-marketplace](https://www.skills.sh/jeremylongshore/tons-of-skills-marketplace) via skills.sh - 17.0K combined installs across 137 indexed listings; first documented 2026-11-03 (nightly sweep)

**GitHub:** [jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace) - 2,894 stars, MIT, branch main, last pushed 2026-11-03; 5,758 skill directories in the tree across 19 plugin categories, with a duplicate-ish layer of numbered topic folders under `skills/` and an adapter layer under `.agents/skills/`

**Category:** Agent skills marketplace platform and package manager, not a single skill family

**Quality Tier:** 🟢 Green - all three sampled listings pass Gen Agent Trust Hub, Socket and Snyk, and the repository ships an MIT LICENSE

Tons of Skills is Jeremy Longshore's model-agnostic agent-skills platform, published under the Intent Solutions brand with the marketplace itself at tonsofskills.com. The README is careful about what that means: the canonical layer is harness-free by construction, Claude Code is currently the only verified-native harness, and other harnesses stay engineering candidates until their native-path integration is verified. Source research alone is never presented as public support.

This guide is different from the others in the catalog, and the difference matters before you install anything. The 137 indexed listings are not a family of related skills; they are individual entries drawn from a catalogue whose README labels 428 catalog plugins and 2,713 marketplace-visible skills. Installing "Tons of Skills" means installing a distribution platform plus the `ccpi` package manager that installs plugins from it. Rows in the table below are the specific skills you would pull out of that catalogue, not modules that ship together.

The repository is also large in a way that changes the install decision. It carries 5,758 skill directories, 19 plugin categories, 38 mirrored external plugins marked with a `.source.json` provenance file, and a 329 MB working tree. Nobody installs this by cloning and copying. You install the platform, then install one plugin or one skill at a time.

## Installation

Inside Claude Code, the README's one-command route registers the whole marketplace:

```bash
/plugin marketplace add jeremylongshore/claude-code-plugins
```

That slug is not a typo and should not be "fixed" to the repository name. The README labels it a frozen compatibility contract, hardcoded in the CLI, the website hero snippet and hundreds of downstream READMEs, with GitHub's redirect to the canonical repository name carrying the load.

The CLI route installs `ccpi`, then a plugin by name:

```bash
pnpm add -g @intentsolutionsio/ccpi
ccpi install devops-automation-pack

npx @intentsolutionsio/ccpi install <plugin-name>
npx @intentsolutionsio/ccpi list
npx @intentsolutionsio/ccpi doctor
```

The skills.sh route pulls the whole tree at full depth, which is what makes the per-skill tree reachable:

```bash
npx skills add jeremylongshore/tons-of-skills-marketplace --full-depth
```

The most careful route is the platform's own first-party installer, which copies committed Git bytes for one skill directory into a verified harness path and leaves a receipt behind:

```bash
tons skills install ./plugins/crypto/trading-strategy-backtester/skills/backtesting-trading-strategies \
  --harness claude-code --scope project
```

For a Hermes profile, prefer the narrow path: install the platform, then copy a single skill directory such as `skills/18-visual-content/svg-icon-generator` into `~/.hermes/profiles/corpusiq/skills/`. Copying the repository is not a realistic option at 329 MB, and copying a plugin directory wholesale drags in whatever else that plugin ships.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| backtesting-trading-strategies | 4,699 | Backtesting crypto and traditional trading strategies against historical data. |
| svg-icon-generator | 1,308 | SVG icon generation, an auto-activating entry in the visual content category. |
| mindmap-generator | 999 | Mindmap generation for visual content work. |
| performance-lighthouse-runner | 598 | Lighthouse performance runs for frontend development. |
| d2-diagram-creator | 346 | D2 diagram creation for visual content work. |
| tracking-crypto-prices | 339 | Real-time cryptocurrency prices across exchanges, with historical data and alerts. |
| n8n-workflow-generator | 262 | n8n workflow generation for business automation. |
| readme-generator | 244 | README generation for DevOps basics. |
| aggregating-crypto-news | 237 | Crypto news aggregation from configured RSS sources including CoinDesk, CoinTelegraph, The Block and Decrypt. |
| swagger-doc-creator | 225 | Swagger documentation work for API development. |
| pdf-parser | 222 | PDF parsing for business automation. |
| consul-service-discovery | 180 | Consul service discovery for advanced DevOps work. |
| mermaid-flowchart-generator | 173 | Mermaid flowchart generation. |
| forecasting-time-series-data | 172 | Forecasting future values from historical time series by analysing trends, seasonality and patterns. |
| plantuml-diagram-generator | 115 | PlantUML diagram generation. |
| ansible-playbook-generator | 113 | Ansible playbook generation for advanced DevOps work. |
| docker-compose-creator | 102 | Docker Compose file creation. |
| brand-strategy | 99 | A seven-part brand strategy covering identity, audience, positioning, messaging, visual principles, channels and measurement. |
| jmeter-test-plan-creator | 98 | JMeter test plan creation for performance testing. |
| gitignore-generator | 97 | gitignore generation for DevOps basics. |

The remaining 117 indexed listings range from 42 to 94 installs.

The shape of that table is the catalogue in miniature. The single largest listing is a backtesting skill at 4,699 installs, roughly nine times the twentieth entry, and the distribution is a long tail: 117 of the 137 indexed listings sit below 97 installs and the smallest is at 42. The top twenty also lean heavily on generated categories, where a listing exists to produce one artifact type (an icon, a mindmap, a Mermaid chart, a Dockerfile, a gitignore file) rather than to run a workflow.

Selection is the real work with a catalogue this size. Many entries share a templated description of the form "Generate X operations. Auto-activating skill for Y", which tells you the category but little about quality or depth. The entries that read like real specifications, such as `backtesting-trading-strategies`, `brand-strategy` or `forecasting-time-series-data`, describe an actual method and are the ones worth installing first.

## Why This Matters for Hermes Agents

A Hermes profile is only as capable as the skills it can reach, and hand-writing each one does not scale past a few dozen. This repository is the largest single source of prebuilt agent skills in the catalog: 2,713 marketplace-visible skills according to its own scale table, each one a directory with a `SKILL.md` that an agent can read and follow.

The more interesting contribution is the install plumbing. The `tons skills install` command refuses uncommitted, untracked, ignored, symlinked and mirrored sources, restricts allowed content to `SKILL.md`, `README.md`, licenses, eval specs and files under `assets/`, `examples/`, `references/`, `scripts/` or `templates/`, and writes a `.ccpi-portable-install.json` receipt binding file hashes to the source repository, commit, tree and harness. `tons skills doctor` then rehashes installed files and reports `verified`, `outdated`, `locally-modified`, `missing` or `unverifiable`.

That receipt model is worth copying in your own skill pipeline. It is also honest about its limits in a way most marketplaces are not: the README states that `verified` means byte identity only, and that quality remains `not-assessed`. A skill can be provably unmodified and still be a bad skill.

The provenance rules are explicit too. External plugins are hosted mirror-by-default, the contributor's repository stays the source of truth, every mirrored source is pinned in a content lockfile, and upstream credit (author, license, resolved commit) is recorded in the mirror. Where a plugin is somebody else's work, the improvement path is upstreaming, never a silent edit to the mirror.

## Usage

| You say | What happens |
|---|---|
| "Find me a skill that backtests a trading strategy" | Surfaces `backtesting-trading-strategies`, the catalogue's most installed listing at 4,699, and installs it on request. |
| "Install the visual content pack into this profile" | Resolves the numbered `skills/18-visual-content/` tree and copies the chosen skill directories, which is the narrow path for a Hermes profile. |
| "What is installed and is it intact?" | `tons skills doctor` rehashes installed files against their receipts and reports integrity per skill. |
| "Which plugins can this marketplace install?" | `ccpi search terraform` or `ccpi list`, both documented CLI commands, against the catalogue. |
| "Set up an n8n workflow for this intake form" | Routes to `n8n-workflow-generator` at 262 installs, a business automation entry. |
| "Generate a Mermaid flowchart of this process" | Routes to `mermaid-flowchart-generator` at 173 installs instead of pulling a diagram plugin. |
| "Write the brand brief for the new product line" | Routes to `brand-strategy` at 99 installs, which covers identity, audience, positioning, messaging, visual principles, channels and measurement. |

## Verification

The raw paths below returned 200 on branch main on 2026-11-03:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/jeremylongshore/tons-of-skills-marketplace/main/README.md
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/jeremylongshore/tons-of-skills-marketplace/main/skills/18-visual-content/svg-icon-generator/SKILL.md
```

After a full-depth install, confirm the tree really is a catalogue and that the CLI reads the same picture:

```bash
npx @intentsolutionsio/ccpi list
node -e "console.log(require('./.claude-plugin/marketplace.json').metadata.totalPlugins)"
ls -d skills/*/ | wc -l
```

The `list` command should print installed plugins rather than the whole catalogue. The manifest metadata should print 444 plugins with `skillsEnabled` at 2954, while the README's labeled scale table counts 428 catalog plugins and 2,713 marketplace-visible skills; these are different cohorts, which is exactly why the README prints the cohort and the reproduce command beside every number. The directory count should print 20, the numbered topic folders under `skills/`.

For a single installed skill, the receipt is the check that matters:

```bash
ls ~/.hermes/profiles/corpusiq/skills/svg-icon-generator
cat ~/.hermes/profiles/corpusiq/skills/svg-icon-generator/.ccpi-portable-install.json
```

If the receipt is present, the install went through the first-party path; if it is absent, you copied the directory yourself and none of the integrity guarantees apply.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-03) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| backtesting-trading-strategies | Pass | Pass | Pass |
| svg-icon-generator | Pass | Pass | Pass |
| mindmap-generator | Pass | Pass | Pass |

Three passes out of three is a good signal for those three listings and a weak signal for a catalogue of this size. The sampled skills are the top of the install distribution, which is exactly where a marketplace's own curation attention lands. Of the roughly 2,713 marketplace-visible skills, three were sampled.

The repository's own posture is unusually explicit about this. External plugins are mirrored, not vendored: 38 plugin directories carry a `.source.json` recording upstream author, license and pinned commit, and the contributor's repository remains the source of truth. Each plugin also carries its own license in its manifest, while the repository scaffold and first-party tooling are MIT. Installing a mirrored plugin means trusting its upstream author, not Jeremy Longshore.

Two guardrails are worth using as designed. The first-party installer refuses mirrored sources, along with uncommitted, untracked, ignored and symlinked ones, and restricts which file types it will copy, so it will not carry a key file, a database or build output into a skill directory. The doctor command is read-only by contract: it never fetches, checks out commits, refreshes the index, uploads content, writes reports or repairs a skill.

Finally, the README is direct that certification does not yet exist. The certification section renders "Not yet certified" from the absence of a report file, and says so honestly rather than cosmetically. Until that report exists, no artifact on the marketplace claims a tier.

## Limitations

- Snapshot data, verified 2026-11-03: 17,030 combined installs across 137 indexed listings; 2,894 GitHub stars; MIT; last pushed 2026-11-03. Counts drift over time.
- The install distribution is thin. 117 of the 137 indexed listings sit below 97 installs, and the smallest is 42, so the four-figure entries at the top are the exception rather than the norm.
- This is a platform install, not a skill install. You get a marketplace and the `ccpi` package manager, and you still have to choose a plugin or a skill before an agent gains any capability.
- The working tree is 329 MB with 5,758 skill directories, so a clone is a commitment and a full-depth skills.sh pull is larger than most profiles want in context.
- Claude Code is the only verified-native harness. The README states other harnesses remain engineering candidates until their native-path integration is verified, so a Hermes install is partly a manual copy rather than a supported path.
- Mirrored plugins keep their upstream license and provenance, and the catalogue's certification program has not shipped: the README renders "Not yet certified" from the absence of a report.
- Many listings share templated descriptions ("Generate X operations. Auto-activating skill for Y"), so names and install counts carry more selection signal than the descriptions do.

## Related

- [ClawHub Skill Vetting - Security Scanner Setup](/hermes/skills/catalog/clawhub-skill-vetting-setup)
- [Luxor Claude Marketplace Skills Setup](/hermes/skills/catalog/luxor-claude-marketplace-setup)
- [OpenCLI Skills - Agent CLI with Browser Automation Setup](/hermes/skills/catalog/opencli-skills-setup)
- [Qodo Skills - Code Review and Standards Suite](/hermes/skills/catalog/qodo-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Decide which install you are doing before you start. Installing the platform is one decision; installing a specific skill is another, and mixing the two is how a profile ends up with 300 unrelated skills competing for triggers.
- Use `tons skills install` rather than a directory copy when the skill matters. The receipt is cheap, the `doctor` command works against it, and it refuses file types that should never land in a skill folder.
- Read the scale table before quoting any number from this repository. It is the only part of the README that names the cohort and the reproduce command for each count, and it exists because unlabeled counts contradict each other.
- Prefer the entries that describe a method over the ones that describe an artifact type. "Backtest a strategy" is a workflow; "generate a gitignore" is a template with an install count.
- Keep the frozen `jeremylongshore/claude-code-plugins` slug in the plugin marketplace command. Renaming it to match the repository breaks the redirect the CLI depends on.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
