---
title: "Webflow Skills - Site Building for Agents Setup"
description: "webflow/webflow-skills: 29.4K combined installs. Official Webflow MCP skills for CMS work, site audits, code components and safe publishing."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/webflow-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "webflow", "cms", "mcp"]
---

# Webflow Skills - Setup Guide

**Source:** [webflow/webflow-skills](https://www.skills.sh/webflow/webflow-skills) via skills.sh - 29.4K combined installs across 45 indexed listings; first documented November 3, 2026 (evening sweep)
**GitHub:** 135 stars, MIT, last pushed 2026-10-29, 33 SKILL.md directories
**Category:** Webflow for agents: CMS collections, components, accessibility audits and safe publishing through the Webflow MCP server
**Quality Tier:** 🟢 Green - MIT licence and no fail verdicts in the sample, though three of the five sampled listings have no verdict at all

This is Webflow's own skill collection, shipped as one plugin called webflow-skills and aimed at agents working on live Webflow sites rather than at people writing code. The 33 SKILL.md directories in the tree are spread across three surfaces: MCP skills that act on a site through the Webflow MCP server, Code Component skills that build and deploy components, and Webflow CLI skills that wrap the command line.

The install data is flatter than most packs of this size. The top listing holds 1,047 installs and the twentieth holds 857, which means the population is broad rather than concentrated around one flagship skill. The lowest listing in the pack sits at 22. Two prerequisites decide whether anything works: a Webflow MCP server configured in the agent, and Node.js plus the Webflow CLI for the Code Component and CLI workflows.

## Installation

The README's own path uses the skills CLI:

```bash
npx skills add https://github.com/webflow/webflow-skills
```

Claude Code users get a plugin marketplace instead:

```bash
claude plugin marketplace add webflow/webflow-skills
claude plugin install webflow-skills@webflow-skills
```

Both paths need the Webflow MCP server before the site facing skills do anything. Add it to your agent's MCP configuration, authenticate with a Webflow account when prompted, and confirm by listing your sites. The server details live at developers.webflow.com/mcp; the plugin path also exposes a Set up authentication button that runs the same flow. Code Component and CLI skills additionally need Node.js and the Webflow CLI installed.

Nothing in the repository mentions Hermes, but these are plain Markdown skills, so a profile skills directory takes the same tree:

```bash
git clone --depth 1 https://github.com/webflow/webflow-skills.git /tmp/webflow-skills
cp -R /tmp/webflow-skills/plugins/webflow-skills/skills/* ~/.hermes/profiles/corpusiq/skills/
```

The README's copy table lists the target directories other agents expect, including ~/.claude/skills/, ~/.cursor/skills/, ~/.config/opencode/skills/ and ~/.codex/skills/. A Hermes profile directory takes the same layout: one folder per skill, each holding a SKILL.md.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| webflow-cli:cloud | 1,047 | The Webflow Cloud command workflow: deploying and managing Cloud apps from the CLI. Indexed with the plugin prefix; the tree directory is webflow-cloud-command. |
| webflow-cli:code-component | 1,041 | Code Component work from the command line: creating and wiring components before they go through the deploy path. Tree directory code-component-command. |
| webflow-cli:designer-extension | 1,035 | Building and running Webflow Designer extensions locally. Tree directory designer-extension-command. |
| webflow-code-component:component-audit | 1,025 | Auditing an existing Code Component for structure, props and reusable patterns before it is converted or deployed. |
| webflow-cli:troubleshooter | 1,023 | Diagnosing Webflow CLI failures. Tree directory webflow-cli-troubleshooter. |
| webflow-code-component:component-scaffold | 1,014 | Scaffolding a new Code Component so it starts from the expected file layout rather than from a blank folder. |
| webflow-cli:devlink | 1,013 | The DevLink workflow for connecting a local development environment to a Webflow site. Tree directory devlink-command. |
| webflow-code-component:convert-component | 1,010 | Converting existing markup or a component into the Webflow Code Component format. |
| webflow-code-component:local-dev-setup | 1,005 | Setting up local development for Code Components, including the Node and Webflow CLI prerequisites. |
| webflow-code-component:pre-deploy-check | 1,003 | The checks to run against a Code Component immediately before it ships. |
| webflow-code-component:deploy-guide | 1,002 | The deploy path from a local Code Component build to a published site. |
| webflow-code-component:troubleshoot-deploy | 989 | Debugging a Code Component deploy that failed or produced the wrong output. |
| webflow-mcp:accessibility-audit | 906 | Accessibility audit of a Webflow site through the MCP server, reading the live site rather than the local source. |
| webflow-mcp:cms-best-practices | 893 | CMS architecture guidance. The README describes it as expert guidance on CMS architecture and optimization. |
| webflow-mcp:asset-audit | 888 | Auditing site assets for size and format problems before they reach a template. |
| webflow-mcp:site-audit | 879 | A site health audit across a Webflow site through the MCP server. |
| webflow-mcp:custom-code-management | 875 | Managing the custom code a site carries, rather than editing it by hand in the Designer. |
| webflow-mcp:link-checker | 872 | Checking the links across a site for broken targets. |
| webflow-mcp:cms-collection-setup | 858 | Creating CMS collections with custom fields and relationships; the README cites 16 field types. |
| webflow-mcp:designer-tools | 857 | Designer tools exposed through the MCP server, for work that would otherwise be a manual Designer session. |
| accessibility-audit | 486 | The plain-name listing of the same tree directory as webflow-mcp:accessibility-audit, shown here because it is the clearest example of the duplicate indexing described below. |

The remaining 25 indexed listings range from 22 to 851 installs.

One entry above sits below the threshold on purpose. The plain-name listing accessibility-audit at 486 is the same accessibility-audit directory as webflow-mcp:accessibility-audit at 906, so the pack's 45 listings map onto 33 directories, and twelve skills are indexed twice, once with a plugin prefix and once without. The other plain-name duplicates in the tail are cms-best-practices at 419, link-checker at 393, custom-code-management at 353, site-audit at 338, cms-collection-setup at 337, bulk-cms-update at 323, asset-audit at 318, safe-publish at 313, flowkit-naming at 304, designer-tools at 172 and site-activity at 83, each paired with a prefixed listing of the same skill. Every one of the 20 rows at or above the threshold has a SKILL.md directory under plugins/webflow-skills/skills/.

The names also shift between surfaces. Five CLI listings carry a different name in the tree than on skills.sh: webflow-cli:cloud ships as webflow-cloud-command, code-component as code-component-command, designer-extension as designer-extension-command, devlink as devlink-command, and troubleshooter as webflow-cli-troubleshooter. Install counts follow the listing, so a search for the directory name will not find the row with the traffic.

## Why This Matters for Hermes Agents

Most agent work on a website stops at generating files. This pack is interesting because the skills act on the site itself through the MCP server: they read the live site, audit it, and change it, which is a different risk class from writing a component to disk. The split between read-shaped skills such as site-audit, link-checker, asset-audit and accessibility-audit, and write-shaped skills such as bulk-cms-update and safe-publish, is the split an agent needs to plan a task safely.

The Code Component surface covers the full loop rather than one step of it. A component gets scaffolded, converted, developed locally, audited, checked before deploy, then deployed, with a troubleshooter for each half of the pipeline. That means an agent can be pointed at a broken component and find a skill that matches the stage it failed at, instead of being handed a single generic instruction.

The CMS skills are where the install counts concentrate, and the README says why: collections with custom fields and relationships, sixteen field types, batch create and update with validation and preview before anything is written. Validation and preview are the two properties that make an agent safe to point at a production CMS, because both give it a chance to see the change before it lands.

The naming quirks are the practical trap. A skill directory called webflow-cloud-command is indexed as webflow-cli:cloud, and a duplicate listing splits the install count in half. Reading the table as a popularity ranking will mislead you about which skills are actually used; reading it as a directory index, with the mapping above, will not.

## Usage

| You say | What happens |
|---|---|
| "Audit this Webflow site for broken links and heavy images" | link-checker and asset-audit read the live site through the MCP server and report broken targets and oversized assets. |
| "Set up a blog collection with author and category relationships" | cms-collection-setup creates the collection with custom fields and relationships, using the field types the README documents. |
| "Import these forty posts into the blog collection" | bulk-cms-update validates the batch and shows a preview before writing the items. |
| "Check whether this site is accessible" | accessibility-audit runs against the live site and reports the issues it finds. |
| "Scaffold a pricing table component and deploy it" | component-scaffold creates the layout, local-dev-setup covers the Node and CLI prerequisites, pre-deploy-check runs the checks, and deploy-guide walks the deploy. |
| "The component deploy failed, help me debug it" | troubleshoot-deploy diagnoses the failure and hands off to webflow-cli:troubleshooter when the problem is in the CLI rather than the component. |
| "Publish these changes but keep a way back" | safe-publish walks the publishing flow with the safety step the skill is named for. |

## Verification

Check the tree before copying, using the path the LAYOUT lists:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/webflow/webflow-skills/main/plugins/webflow-skills/skills/accessibility-audit/SKILL.md
```

That URL should print 200. The full skill root is plugins/webflow-skills/skills/ on branch main, and every directory named in the table sits directly under it with its own SKILL.md.

After the copy, count what landed and confirm the MCP connection separately, because the two fail differently:

```bash
find ~/.hermes/profiles/corpusiq/skills -maxdepth 2 -name SKILL.md | wc -l
```

The count should be 33 if the profile started empty. A skills failure shows up as an agent that does not know the workflow; an MCP failure shows up as a skill that loads and then cannot list your sites, so test the site listing before blaming the skill.

## Security

skills.sh verdicts for sampled skills (verified November 3, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| webflow-cli:cloud | ? | ? | ? |
| webflow-code-component:troubleshoot-deploy | ? | ? | ? |
| webflow-mcp:safe-publish | ? | ? | ? |
| cms-collection-setup | Pass | Pass | Pass |
| webflow-mcp:waf-rules | ? | ? | ? |

Only one of the five sampled listings carries a verdict: cms-collection-setup passes all three auditors. The other four show no result on any of the three, which is not the same as a pass. Treat an unrated skill as unverified, and read the SKILL.md before an agent runs it against a production site.

The write surface is the reason to be careful here. bulk-cms-update changes CMS items in batches, custom-code-management changes injected code, site-activity looks at who changed what, and safe-publish publishes. A skill that publishes is a skill that can publish a mistake, and the preview and validation steps the README describes are the only guardrail between an agent and a live site.

The credential is a Webflow account with site access, held by the MCP server rather than by the skill files, so the skills themselves are Markdown and carry no secrets. That also means revocation happens at the account or the token, not in the skill directory. Read the account scopes the MCP server requests before you connect it to a site with other people's content on it.

## Limitations

- Snapshot data, verified November 3, 2026: 29,425 combined installs across 45 indexed listings; 135 GitHub stars; MIT; last pushed 2026-10-29. Counts drift over time.
- Twenty five of the 45 listings sit below the 857 threshold, from 851 down to 22. Thirteen are distinct skills: bulk-cms-update, flowkit-naming, safe-publish, site-activity, review-comments, compress-cms-image, figma-to-webflow, interactions, cloud-apps, waf-rules and the three webflow-university entries. The other twelve are the plain-name duplicates.
- Twelve skills are indexed twice, once prefixed and once plain, so any per-listing install figure is roughly half the skill's real usage.
- Five CLI listing names do not match their tree directory names, which breaks a naive lookup by directory.
- Four of the five sampled skills have no security verdict on any of the three auditors.
- Site, CMS, audit, Designer and publishing skills need the Webflow MCP server configured and an authenticated Webflow account; Code Component and CLI skills also need Node.js and the Webflow CLI. Nothing works from the skill files alone.

## Related

- [WordPress Agent Skills - Official WP Development Setup](/hermes/skills/catalog/wordpress-agent-skills-setup)
- [Modern Web Guidance - Google Chrome Agent Skill Setup](/hermes/skills/catalog/googlechrome-modern-web-guidance-setup)
- [Interface Design Skill - Non-Templated Product UI Setup](/hermes/skills/catalog/interface-design-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Audit before you write. site-audit, link-checker, asset-audit and accessibility-audit are all read shaped, so run them first and let their findings decide what the agent changes.
- Use cms-collection-setup before bulk-cms-update. The field types and relationships have to exist before a batch can fill them, and getting the schema wrong is more expensive than the import.
- Run pre-deploy-check as a gate, not as advice. It exists to fail before deploy-guide runs, and an agent that treats it as optional is an agent that publishes broken components.
- Keep the MCP skills and the CLI skills in separate phases. Mixing a site read with a local CLI build in one step makes failures hard to attribute, and each has its own troubleshoot skill.
- Search by listing name, not directory name. webflow-cli:cloud, code-component, designer-extension, devlink and troubleshooter are all named differently in the tree.
- Start on a staging site with safe-publish. The skill is built for the careful version of publishing, and a first run is a poor place to find out what the careful version skips.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
