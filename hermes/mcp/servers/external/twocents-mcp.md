---
name: "twocents MCP"
description: "Human feedback for AI agents — share pages and collect structured feedback"
category: "Productivity"
source: "mcp.so"
discovered: "2026-07-23"
verified: true
repository: "https://github.com/twocents-page/twocents"
remote_endpoint: "https://twocents.page/mcp"
---

# twocents MCP — Human Feedback Loop for AI Agents

twocents gives AI agents a direct channel to request human feedback. Agents can share generated content, designs, or proposals via a simple web page, and humans can leave structured feedback that flows back into the agent's context.

## What It Does

- **Share pages** — Agent creates a simple, shareable web page with content for review
- **Collect feedback** — Humans leave comments, approvals, or revision requests
- **Structured feedback** — Feedback can be structured (approve/reject/revise) or freeform
- **Remote MCP** — Works as a remote endpoint, no local install needed

## Quick Start

```bash
# Remote endpoint — no local install
hermes mcp add twocents --url https://twocents.page/mcp

# Or Claude Code
claude mcp add twocents --url https://twocents.page/mcp
```

**Prerequisites:** None. The endpoint is open and requires no authentication.

## Key Tools

| Tool | Description |
|------|-------------|
| `share_page` | Create a shareable page with content for human review |
| `get_feedback` | Retrieve all feedback left on a shared page |
| `get_page_status` | Check if a page has been reviewed |
| `list_pages` | List all pages shared by this agent |

## Use Cases

- **Content review** — Agent drafts a blog post, shares it via twocents, PM reviews and approves
- **Design feedback** — Agent generates UI mockups → shares → designer leaves pixel-level feedback
- **Decision gates** — Agent proposes architecture decision → shares for team vote → proceeds on approval
- **Client review** — Agent drafts deliverables → shares with client → incorporates feedback in next iteration

## Hermes Agent Integration

```python
# Agent creates a review page
page = mcp_twocents_share_page(
    title="Q3 Content Calendar Draft",
    content=calendar_markdown,
    feedback_type="approve_or_revise"
)
# Later: check for feedback
feedback = mcp_twocents_get_feedback(page_id=page.id)
if feedback.status == "approved":
    print("Calendar approved — proceeding with scheduling")
```

---

*Discovered via [mcp.so](https://mcp.so) sweep. Listed in the [CorpusIQ MCP Catalog](https://corpusiq-docs/hermes/mcp/).*
