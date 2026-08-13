---
title: Canvas LMS — Full Setup Guide for Hermes Agents
description: Install, configure, and use the Canvas LMS skill from NousResearch. Read-only access to courses, assignments, and grades for student agents.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/canvas-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Canvas LMS — Setup Guide

**Source:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent) (227.9K⭐)
**Skill:** `nousresearch/hermes-agent@canvas`
**Installs:** 14
**Category:** Education / Productivity
**First Seen:** Apr 4, 2026

Read-only access to Canvas LMS for listing courses and assignments. Designed for student agents that need to track coursework, due dates, and grades without manual browser interaction.

---

## Installation

```bash
npx skills add nousresearch/hermes-agent@canvas
```

Or install from the Hermes Agent monorepo:

```bash
npx skills add https://github.com/nousresearch/hermes-agent --skill canvas
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Canvas LMS Account** | Any Canvas instance (university, school, or self-hosted) |
| **Canvas API Token** | Generated from Account → Settings → Approved Integrations |
| **Hermes Agent** | Any version |
| **Python 3** | For `canvas_api.py` script |

---

## Setup

### Step 1: Generate a Canvas API Token

1. Log in to your Canvas instance in a browser
2. Go to **Account → Settings** (click your profile icon, then Settings)
3. Scroll to **Approved Integrations** and click **+ New Access Token**
4. Name the token (e.g., "Hermes Agent"), set an optional expiry, and click **Generate Token**
5. Copy the token

### Step 2: Add Token to Hermes Environment

Add the token to `${HERMES_HOME:-~/.hermes}/.env`:

```bash
CANVAS_API_TOKEN=your_token_here
CANVAS_INSTANCE_URL=https://your-school.instructure.com
```

Or add it to your profile's `.env`:

```bash
echo 'CANVAS_API_TOKEN=your_token_here' >> ~/.hermes/.env
echo 'CANVAS_INSTANCE_URL=https://your-school.instructure.com' >> ~/.hermes/.env
```

### Step 3: Verify Connection

```bash
python3 <skill-dir>/scripts/canvas_api.py --check
```

---

## What It Provides

### Available Commands

| Command | Description |
|---|---|
| `list-courses` | List all active courses with IDs, names, and term info |
| `list-assignments` | List assignments for a specific course |
| `list-grades` | List grades for a specific course |
| `list-upcoming` | Show assignments due in the next N days |
| `course-info` | Detailed course metadata (syllabus, instructor, schedule) |
| `assignment-detail` | Full assignment details (description, rubric, submission status) |

### Script: `canvas_api.py`

The skill ships with `scripts/canvas_api.py` — a Python CLI that wraps the Canvas REST API. All commands use the token from the environment.

---

## Quick Start

```bash
# 1. Install
npx skills add nousresearch/hermes-agent@canvas

# 2. Configure environment
export CANVAS_API_TOKEN="your_token"
export CANVAS_INSTANCE_URL="https://canvas.yourschool.edu"

# 3. List your courses
python3 <skill-dir>/scripts/canvas_api.py list-courses

# 4. Check upcoming assignments
python3 <skill-dir>/scripts/canvas_api.py list-upcoming --days 7
```

---

## Limitations

- **Read-only:** This skill cannot submit assignments, post to discussions, or modify course content.
- **Token scope:** The token inherits the permissions of the Canvas user who generated it. Student tokens see only their own data.
- **Pagination:** Large courses with many assignments may require pagination. The script handles this automatically.

---

## Verification

After setup, run the check command:

```bash
python3 <skill-dir>/scripts/canvas_api.py --check
```

Expected output: `✓ Connected to Canvas LMS — 2 courses, 0 upcoming assignments due in 7 days`

---

## Security

- [Gen Agent Trust Hub: Pass](https://www.skills.sh/nousresearch/hermes-agent/canvas/security/agent-trust-hub)
- [Socket: Pass](https://www.skills.sh/nousresearch/hermes-agent/canvas/security/socket)
- [Snyk: Pass](https://www.skills.sh/nousresearch/hermes-agent/canvas/security/snyk)

---

**Related:** [google-workspace setup](google-workspace), [apple-calendar-setup.md](apple-calendar-setup.md)
