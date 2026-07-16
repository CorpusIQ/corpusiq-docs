---
title: openclaw-release-maintainer — Setup Guide
description: Automate OpenClaw skill releases with semantic versioning, changelog generation, tag creation, and GitHub release publishing. Part of the Clawdis ecosystem.
---

# openclaw-release-maintainer — Setup Guide

## Prerequisites
- **GitHub Personal Access Token** with `repo` scope
- **Hermes Agent** installed
- **Git 2.30+** configured with user name and email
- **Existing OpenClaw/Hermes skill repository** with semver tags

## Capabilities

| Capability | Description |
|-----------|-------------|
| **Semantic Version Bumping** | Increments major, minor, or patch versions based on commit analysis |
| **Auto-Generated Changelogs** | Parses conventional commits to produce release notes |
| **Git Tag Creation** | Creates and pushes annotated tags with release metadata |
| **GitHub Release Publishing** | Publishes release with changelog, assets, and release notes |
| **Pre-Release Checklist** | Verifies tests pass, builds succeed, and dependencies are current before publishing |

## Installation

```bash
npx skills add steipete/clawdis/openclaw-release-maintainer
```

## Configuration

Add your GitHub token to the Hermes environment:

```bash
export GITHUB_TOKEN="ghp_your-token-here"
```

Or configure in `~/.hermes/config.yaml`:

```yaml
skills:
  openclaw-release-maintainer:
    github_token: "${GITHUB_TOKEN}"
    default_bump: "patch"          # major | minor | patch
    changelog_format: "keepachangelog"
    push_tags: true
    create_release: true
```

## Usage

### Standard Release Workflow

```bash
# From your skill repository directory
cd ~/corpusiq-docs/hermes/skills/

# Bump version and release
npx skills run openclaw-release-maintainer --bump patch --message "fix: correct gateway token validation"
```

### Checking What Would Change (Dry Run)

```bash
npx skills run openclaw-release-maintainer --bump minor --dry-run
```

Output shows:
- Current version → new version
- Commits that will appear in changelog
- Tags that will be created
- Files that will be modified

### Major Release with Breaking Changes

```bash
npx skills run openclaw-release-maintainer --bump major --breaking "API: dropped support for legacy OAuth flow"
```

## How It Works

```
┌──────────┐     ┌──────────────────┐     ┌───────────┐
│  Hermes   │────▶│  Release          │────▶│  GitHub   │
│  Agent    │     │  Maintainer Skill │     │  API      │
└──────────┘     └──────────────────┘     └───────────┘
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
    ┌──────────┐ ┌──────────┐ ┌──────────┐
    │ Version  │ │ Changelog│ │ Release  │
    │ Bump     │ │ Generate │ │ Publish  │
    └──────────┘ └──────────┘ └──────────┘
```

The skill analyzes commits since the last tag using conventional commit conventions, determines the appropriate version bump, generates a KeepAChangelog-formatted changelog, creates an annotated Git tag, and publishes a GitHub Release with the full changelog as release notes.

## Commit Convention

The skill parses [Conventional Commits](https://www.conventionalcommits.org/) to determine the version bump:

| Commit Prefix | Bump Type | Example |
|--------------|-----------|---------|
| `fix:` | Patch (0.0.x) | `fix: resolve memory leak in recall module` |
| `feat:` | Minor (0.x.0) | `feat: add multi-agent skill delegation` |
| `BREAKING CHANGE:` or `!:` | Major (x.0.0) | `feat!: drop support for Node 16` |
| `docs:`, `chore:`, `style:`, `refactor:` | Patch | `docs: update setup instructions` |

## CorpusIQ Use Cases

1. **Skill Repository Publishing:** CorpusIQ maintains 133+ skills. Each skill update goes through: bump → changelog → tag → release. This skill automates that entire pipeline.

2. **Multi-Repository Coordination:** When a Hermes core update requires updates across multiple skill repos, batch-releases ensure consistent versioning and changelogs.

3. **Quality Gates:** The pre-release checklist ensures no skill is published with broken tests, missing dependencies, or stale documentation.

4. **Audit Trail:** Every release is tagged and published on GitHub with full changelogs — providing a complete history of what changed and why.

## Integration with CI/CD

For automated releases in GitHub Actions:

```yaml
name: Auto Release
on:
  push:
    branches: [main]
jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Auto-release
        run: |
          npx skills add steipete/clawdis/openclaw-release-maintainer
          npx skills run openclaw-release-maintainer --auto
```

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| "No conventional commits found" | Commits don't use conventional format | Use `fix:` or `feat:` prefixes |
| "Tag already exists" | Version already published | Bump to next version or use `--force` |
| "401 Bad credentials" | Invalid GitHub token | Verify `GITHUB_TOKEN` has `repo` scope |
| "No changes since last tag" | All commits already released | Verify with `git log --oneline $(git describe --tags --abbrev=0)..HEAD` |
| "Pre-release checks failed" | Tests or builds failing | Fix failing checks before releasing |
| "Protected branch" | Main branch has push protection | Use PR-based workflow or admin token |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
*↑ [Skills Home](/hermes/skills/)*

---

*Curated by CorpusIQ — one MCP endpoint, all your business tools.*
