---
title: "Hermes Agent Skill Marketplaces"
description: Navigate Hermes Agent skill marketplaces for discovering and publishing skills. Quality tiers, marketplace comparison, publishing guides, community standards, and how to find the best community-built AI agent skills.
category: skills
tags: [hermes-agent, skills, marketplace, publishing, quality-tiers, community, discovery, curation]
last_updated: "2026-10-30"
canonical: "https://www.corpusiq.io/docs/hermes/skills/skill-marketplaces/"
robots: "index,follow"

---

# Hermes Agent Skill Marketplaces  --  Discovery, Publishing & Quality

## Marketplace Overview

| Marketplace | Focus | Curation Level | Cost Model | Best For |
|------------|--------|---------------|------------|----------|
| [skills.sh](https://skills.sh) | Open community | Light moderation | Free | Broadest selection, diverse categories |
| [agentskills.io](https://agentskills.io) | Open skill standard | Public spec, no gatekeeping | Free | Portable, standard-compliant skills |
| [Official optional skills](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog) | Hermes repo catalog | Maintained by Nous Research | Free | Verified, Hermes-native |
| [skilldock.io](https://skilldock.io) | Enterprise focus | Strict review | Subscription | Compliance-ready, SLAs, support |
| GitHub (`hermes-skill-*`) | Open source | None (self-serve) | Free | Custom forks, bleeding edge, community |

## skills.sh

**Best for:** Discovering a wide variety of skills across every category. The largest open marketplace.

**Discovery:** Browse by category or search by keyword. The search supports natural-language queries like "show me skills for email automation." Each skill listing shows the quality tier, required connectors, last update date, and community rating.

**Publishing:** Create an account, verify your email, and submit your skill directory. Submissions go through light moderation (content check, no malware/viruses, basic documentation present) and are typically published within 24 hours. Your listing includes the skill name, description, tags, required connectors, version, and quality tier.

**Quality indicators to look for:**
- Community rating (4+ stars from 10+ ratings is a strong signal)
- Recency of last update (updated within 90 days)
- Number of installations (higher is generally better, but niche skills may be excellent with fewer installs)
- Author responsiveness in the discussion thread
- Quality tier badge (Production, Beta, Community)

**When to choose skills.sh:** You want maximum selection and are comfortable doing your own due diligence before installing.

## agentskills.io

**Best for:** Understanding the format your skill has to satisfy. agentskills.io publishes the open Agent Skills standard that Hermes skills are compatible with.

**Discovery:** The site is documentation, not a paid catalog: an overview, the specification, a client showcase, and authoring guidance (quickstart, best practices, optimizing descriptions, evaluating skills, using scripts). Read the [specification](https://agentskills.io/specification) before you write a SKILL.md, because the frontmatter and directory layout it defines are what Hermes and other clients parse.

**Publishing:** There is no submission queue. You publish by distributing a standard-compliant skill directory wherever you like (your own repo, a hub, or a direct URL), and any client that implements the standard can load it.

**Quality indicators to look for:**
- Conformance with the published specification (frontmatter, layout, references)
- Description quality, which the site documents as the single biggest lever on activation
- Documentation depth (example output, troubleshooting section)
- Evidence the author evaluated the skill against real tasks

**When to choose agentskills.io:** You are authoring a skill and want it to work across Hermes and other Agent Skills clients, not just one registry.

## Official optional skills (Hermes catalog)

**Best for:** Skills that integrate deeply with Hermes-specific features, maintained inside the Hermes repository itself. These install with built-in trust.

**Discovery:** The catalog ships with Hermes under `optional-skills/` in the repo and is browsable from the CLI:

```bash
hermes skills browse --source official
hermes skills install official/security/1password
```

**Publishing:** Contribute to the Hermes repository; the skills are reviewed and released with Hermes rather than through a separate submission queue.

**Quality indicators to look for:**
- Shipped in the official catalog (maintained alongside Hermes)
- Compatibility with your Hermes version, since the catalog is released with it
- Integration depth (uses Hermes-native features like memory, skills chaining, cron triggers)

**Note on hermeshub:** the registry previously linked from this section, `hermeshub.nousresearch.com`, no longer resolves (checked October 30, 2026). Hermes's own documentation lists the integrated sources as the official catalog, skills.sh, well-known `/.well-known/skills/index.json` endpoints, direct SKILL.md URLs, GitHub, ClawHub, lobehub, and browse.sh.

**When to choose the official catalog:** You want maximum compatibility with your Hermes setup and trust the maintainers' review process.

## skilldock.io

**Best for:** Enterprise teams with compliance requirements, SLAs, and support needs.

**Discovery:** Skills are organized by enterprise use case and compliance certification (SOC 2, HIPAA, GDPR-ready). Every skill has a support SLA, documented data handling practices, and a security review summary.

**Publishing:** Enterprise-grade review process including security audit, performance testing, and compliance verification. Publication timeline is typically 2-4 weeks. Revenue model is subscription-based with enterprise licensing.

**Quality indicators to look for:**
- Compliance certifications
- Support SLA (response time guarantee)
- Enterprise support contact available
- Data processing documentation (where does data go, how is it handled)

**When to choose skilldock.io:** You're deploying Hermes in a regulated environment (healthcare, finance, government contracting) and need compliance-ready skills.

## GitHub

**Best for:** Discovering bleeding-edge skills, custom forks, and skills from individual developers who prefer open-source distribution.

**Discovery:** Search for `hermes-skill-*` repositories or use topic tags `hermes-skill` and `hermes-plugin`. Each repository is a self-contained skill directory. Quality and documentation vary widely.

**Publishing:** Create a public GitHub repository, add the `hermes-skill` topic, and share the link. No review process, no formal listing  --  pure open source.

**Quality indicators to look for:**
- Stars and forks
- Recency of commits
- Open vs. closed issues ratio
- README completeness
- Test files present
- CI/CD badges (tests passing, lint passing)

**When to choose GitHub:** You want to fork and customize, contribute directly to skill development, or find skills too new for other marketplaces.

## How to Publish: Step-by-Step

Regardless of marketplace, the preparation is similar:

### 1. Prepare Your Skill Directory

```
my-skill/
├── SKILL.md              # Required: skill definition and documentation
├── README.md             # Optional but recommended: expanded documentation
├── CHANGELOG.md          # Version history
├── examples/             # Example inputs and expected outputs
│   └── sample-output.md
└── tests/                # Test cases (if applicable)
    └── test-scenarios.md
```

### 2. Remove Environment-Specific Data

Before publishing, scrub your skill of anything specific to your environment:
- Replace real email addresses with `user@example.com`
- Replace real API endpoints with `<your-api-endpoint>`
- Replace real company names with placeholder text
- Remove any hardcoded credentials or tokens
- Generalize configuration values (use environment variables or config sections)

### 3. Write for a Stranger

Your documentation should answer these questions for someone who has never met you:
- What problem does this solve?
- What do I need before I can use it?
- How do I install and configure it?
- What does successful execution look like?
- What can go wrong and how do I fix it?

### 4. Choose Your Marketplace

Match your skill to the right marketplace based on your goals:
- Maximum reach and community feedback → skills.sh
- Quality recognition and curation → agentskills.io (write to the spec)
- Hermes-native integration → the official optional skills catalog
- Enterprise/compliance focus → skilldock.io
- Open-source collaboration → GitHub

### 5. Submit and Engage

Submit your skill following the marketplace's process. After publication:
- Respond to questions and issues promptly
- Update when connectors change
- Add features based on community feedback
- Deprecate gracefully when the skill is no longer maintained

## How to Discover Skills Safely

Before installing any skill from any marketplace:

1. **Read the SKILL.md completely.** Not just the description  --  what connectors does it need? What does it write?

2. **Check the quality tier.** Match the tier to your risk tolerance. Production tier for automated workflows. Beta for supervised use. Community for learning.

3. **Review the permissions.** Does it request access to connectors or tools that don't align with its purpose? A "weather report" skill shouldn't need CRM access.

4. **Check for confirmation gates.** If the skill modifies data, does it ask for confirmation? Skills from open marketplaces should always have confirmation on write operations.

5. **Test in isolation.** Install in a test profile first. Run with limited data. Verify the output matches expectations.

6. **Check the update history.** Regularly updated skills are maintained. Skills untouched for 12+ months may have compatibility issues.

## Marketplace Comparison: Quality Signals

When comparing the same skill across marketplaces, weigh these signals differently:

| Signal | skills.sh | agentskills.io | official catalog | skilldock.io | GitHub |
|--------|-----------|----------------|-----------|-------------|--------|
| Community rating | High weight | High weight | Medium | Medium | Low |
| Curator review | Low | High | High | Highest | None |
| Update recency | High weight | Medium | Medium | Low (stability valued) | High weight |
| Install count | Medium | Medium | Low | N/A | Stars |
| Compatibility test | Self-reported | Curator-tested | Team-tested | Enterprise-tested | Self-reported |

## The Future of Skill Discovery

The skill ecosystem is evolving toward:

- **Inter-marketplace compatibility:** Skills published on one marketplace working on Hermes instances provisioned from another
- **Automated compatibility testing:** CI/CD pipelines that test skills against every Hermes release
- **Semantic skill search:** Find skills by describing your problem, not by guessing keywords
- **Skill composition:** Chaining multiple community skills into workflows without manual integration
- **Reputation systems:** Author reputation carrying across marketplaces

The marketplaces are complementary, not competitive. A skill published on skills.sh might later graduate into the official Hermes catalog. A skill you distribute standalone can still be fully spec-compliant on agentskills.io. Navigate them based on your needs, not marketplace loyalty.

One skill ecosystem, many entry points. Find what works, build what's missing, and share what you create.

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills)  --  133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
