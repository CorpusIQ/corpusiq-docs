---
title: "Rapidly MCP - Idea Validation, Lean Canvas and Pretotyping"
description: "Hosted Rapidly MCP server that takes a business idea through a Lean Canvas, a riskiest-assumption hypothesis with a researched pass mark, and three to five Pretotyping experiments with a build prompt for the smallest test worth running. 21 tools for idea generation, evidence interpretation and portfolio scoring over bearer-token or OAuth HTTP."
category: Productivity
stars: 1
added: 2026-08-25
source: "mcp.so GitHub issue #3756"
relevance: ★★
tags: [mcp-server, lean-canvas, pretotyping, validation, strategy, product]
---

# Rapidly MCP

**Test the idea before you build it.** Rapidly works inside your AI agent: in about five minutes it takes an idea through a Lean Canvas, turns the riskiest assumption into a measurable hypothesis with a researched pass mark, and returns a build prompt for the smallest Pretotyping experiment worth running. The agent builds the test; real customers provide the evidence. Work is saved to your Rapidly team instead of disappearing in a chat thread.

```
Server type: Remote Streamable HTTP (hosted)
Endpoint: https://www.rapidly.co/mcp
Auth: one-time bearer token (RAPIDLY_MCP_TOKEN) for new teams, OAuth for existing teams
Tools: 21 (idea generation, Lean Canvas design, hypothesis and experiment design, evidence interpretation, portfolio scoring, team records)
Repo: github.com/Exponentially-Platform/Rapidly-MCP (MIT, 1 star)
Registry: co.rapidly/rapidly
Pricing: free trial with five new ideas; team plans by request
```

## Why This Matters for Operators

Asking a general model for a business plan produces something that looks reasonable and proves nothing. Rapidly encodes the method instead: Alberto Savoia's Pretotyping combined with the vendor's practice across 4,000+ client experiments and 200+ workshops. The core run builds a full Lean Canvas, converts the riskiest demand assumption into a market-engagement hypothesis with a researched pass threshold, then designs three to five named experiments and recommends the smallest useful one with a build prompt. The output includes GO/NO-GO rules, cited sources, and a test asset your agent can build immediately.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `independent_generate_ideas` | Generates grounded ideas from a company, problem, or brief with cited public sources |
| `independent_design_lean_canvas` | Builds a complete Lean Canvas, preserving the original customer, problem, and proposition |
| `independent_design_hypothesis` | Turns the riskiest assumption into a market engagement hypothesis with a researched pass threshold |
| `independent_design_experiments` | Creates three to five named Pretotyping experiments, recommends the smallest useful one, returns its build prompt |
| `design_hypothesis` | Designs a hypothesis and researched target from a saved idea or raw idea text |
| `design_experiments` | Designs three to five Pretotyping options for a saved idea |
| `interpret_results` | Turns recorded experiment evidence into an executive summary |
| `evaluate_idea` | Summarises the evidence and recommends what to do next |
| `score_portfolio` | Orders the team's ideas by stored value and effort, with confidence and experiment counts |
| `get_sprint_pack` | Combines the ranked portfolio, team knowledge, focus idea, hypothesis, and fresh experiment designs |
| `list_ideas` | Lists the team's idea portfolio |
| `get_idea` | Opens one idea and its current method work |
| `list_experiments` | Lists an idea's experiments, outcomes, and lessons |
| `get_team_knowledge` | Reads company context and lessons saved by the team |
| `save_idea` | Updates selected fields on an existing idea |
| `expand_idea` | Stages proposed Canvas, hypothesis, and experiment work for review |
| `save_experiment` | Saves a new experiment with the idea it tests |
| `save_team_knowledge` | Adds company context or a lesson to team knowledge |
| `create_idea_bundle` | Creates an idea with optional Canvas, hypothesis, and experiment records |
| `generate_ideas` | Generates grounded, de-duplicated ideas inside an existing team portfolio |
| `validate_idea` | Produces a quick Canvas, hypotheses, and a suggested first experiment without public-source grounding |

## Installation

Open rapidly.co/rapidly-mcp, enter a name, email, and team name. Rapidly creates the account and team, then shows the personal token once (no plan or password needed). The page provides copy-ready setup for Codex CLI and Claude Code.

## Configuration

- **New teams:** keep the bearer token in the RAPIDLY_MCP_TOKEN environment variable and register the endpoint https://www.rapidly.co/mcp with that header.
- **Existing teams:** connect with OAuth, choose the team, and approve access.
- Works with Claude, Codex, ChatGPT, and Hermes; any agent that supports remote MCP can connect.
- Rapidly checks team and access scoping on every request.

## Business Relevance

- **Pre-build validation:** a build prompt for the smallest experiment instead of a full product commitment.
- **Evidence-based decisions:** GO/NO-GO rules and pass thresholds reviewed by real customers.
- **Portfolio discipline:** `score_portfolio` ranks ideas by value and effort for funding conversations.
- **Institutional memory:** experiments, outcomes, and lessons stay in the team workspace.

## Integration with CorpusIQ

Rapidly's experiment evidence pairs with CorpusIQ connectors for the measurement side: validate demand with GA4 landing-page traffic, Shopify trial orders, or Stripe revenue during a Fake Door test, and log hypotheses and pass marks in Notion or Airtable so the validation record lives next to the operating data.

## Limitations

- Free trial caps at five new ideas; team plans require contacting the vendor.
- Generated facts, cited sources, and proposed targets need human review before use.
- Bearer token is shown once at creation - store it securely.
- Young repo (created Aug 24, 2026, 1 star); anonymous endpoint probes return 401 (liveness verified).

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Alpha Sophia MCP - US Healthcare Provider and Market Data](/hermes/mcp/servers/external/alpha-sophia-mcp)
- [LiveSend MCP - Share Client-Facing Content with Read Tracking](/hermes/mcp/servers/external/livesend-mcp)
