---
title: Development Skills
description: Software development workflows for Hermes agents — code review, GitHub PRs, testing, project management
---

# Development Skills

Development workflows for managing code, repositories, and CI/CD pipelines through Hermes agents.

## GitHub Operations
- Repository management (clone, create, fork)
- PR workflow (branch, commit, open, CI, merge)
- Code review with inline comments
- Issue management (create, triage, label, assign)
- Authentication setup (HTTPS, SSH, gh CLI)

## Code Quality
- Codebase inspection (pygount: LOC, languages, ratios)
- Parallel 3-agent cleanup of recent code changes
- Syntax checking on all file writes

## Project Management
- Monday.com integration for task tracking
- Notion workspace management
- Kanban board operations

## Execution

Development skills are loaded into Hermes sessions. The agent reads the skill, follows the numbered steps, and verifies each step completes. Errors trigger the reflexion loop for self-correction. Pipelining multiple skills enables full-stack workflows from PR creation through CI verification to merge.
