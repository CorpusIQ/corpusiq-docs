---
title: "Testiny MCP - Test Case Management from Your Agent"
description: "Create test cases, organize folders, run test suites and update results in Testiny from Claude, ChatGPT, Copilot or Cursor."
category: Development
stars: n/a (hosted platform, testiny.io)
added: 2026-10-07
source: "mcp.so /feed (Oct 7, 2026 midday sweep)"
relevance: ★★
tags: [test-management, qa, testing, test-cases, coverage, teams, api-key, remote-mcp]
---

# Testiny MCP

**Hosted MCP server (Streamable HTTP) for test management** - let Claude, ChatGPT, GitHub Copilot, Cursor or any MCP client work directly with your Testiny project: create and organize test cases, build test runs, update results, and use the test repository as context when generating new tests.

```
Server type: Hosted (Streamable HTTP, protocol 2025-06-18)
Auth: Bearer API key or OAuth (no key needed with OAuth)
Endpoint: https://app.testiny.io/api/v1/mcp-server
Tools: 15 across projects, folders, cases, runs and results
Pricing: Requires a Testiny paid or trial plan; agent access ships with the product
Built by: Mategra GmbH (testiny.io)
```

## Why This Matters for Operators

A test repository is quiet business documentation: cases carry business rules, edge cases and expected behavior that never make it into specs. The MCP server turns that knowledge into context an agent can use - generate API tests for a new feature from existing billing cases, compare incoming requirements against the regression suite and see what is missing, then create the resulting cases and a run without leaving the conversation.

## Tools & Capabilities

| Tool | What the agent can do |
|---|---|
| `listProjects` / `listTestCaseFolders` | Read projects and the folder structure |
| `listTestCases` / `listTestRuns` | Read cases and runs with keyword filtering; BDD cases return their Gherkin scenarios |
| `createFolder` / `editFolder` / `moveFolder` | Organize the case tree |
| `createTestCase` / `editTestCase` / `moveTestCases` | Write cases with preconditions, steps, expected results and custom fields |
| `createTestRun` | Set up a run for organizing execution |
| `setTestResult` / `setTestResultBatch` | Mark results passed, failed, blocked or skipped, one case or many |
| `getTestStatus` / `addTestResultComment` | Read current status in a run; comment on a result |

## Installation

VS Code with Copilot (mcp.json):

```json
{
  "servers": {
    "testiny": {
      "url": "https://app.testiny.io/api/v1/mcp-server",
      "type": "http",
      "headers": { "Authorization": "Bearer <your-api-key>" }
    }
  }
}
```

Claude (Code and Desktop), ChatGPT and other clients: add a remote MCP server with the same URL and header. Omit the Authorization header in an OAuth-capable client and it uses OAuth instead. API keys come from Testiny Settings - API Keys and inherit the permissions of the user who created them.

## Configuration

```json
{
  "mcpServers": {
    "testiny": {
      "url": "https://app.testiny.io/api/v1/mcp-server",
      "headers": { "Authorization": "Bearer <your-api-key>" }
    }
  }
}
```

## Business Relevance

- **QA teams:** create the next regression run and mark results from chat instead of re-keying into the tracker.
- **Product and engineering:** generate test cases straight from requirements or user stories, checked against the existing suite for gaps.
- **Compliance-sensitive teams:** the case repository carries the business rules; an agent reading it produces tests that respect the same rules.

## Integration with CorpusIQ

CorpusIQ reads your operational systems and answers questions with citations. Testiny holds what your product is supposed to do and whether it does it. Business results from CorpusIQ, product confidence from Testiny, both from the same chat.

## Limitations

- Requires a paid Testiny plan or trial; MCP access is part of the product, not a separate add-on.
- BDD test cases are read-only through MCP; edit Gherkin scenarios in the Testiny app.
- An API key inherits its creator's permissions - scope dedicated keys to the projects they need.
- Testiny Cloud and self-hosted Server instances differ; confirm the base URL for your instance.

## FAQ

### Do I need OAuth or an API key?

Either works. With no key, an OAuth-enabled client signs in. API keys suit automation and headless agents; OAuth must be enabled in the organization settings for the former.

### Can it generate tests from a ticket?

Yes - point the agent at requirements or user stories and it compares them to the existing suite, then creates new cases. Pair it with a Jira or GitLab MCP for richer context.

### Are results writable?

Yes: create a run, then set results one at a time or in batch, with comments on individual results.

### Which clients are supported?

Claude (Code and Desktop), VS Code with Copilot, ChatGPT, Cursor and any MCP-compatible client using protocol 2025-06-18.

## See Also

- [Uxia MCP - AI User Testing and UX Research](/hermes/mcp/servers/external/uxia-mcp)
- [Scribase MCP - Hosted Postgres for Agents](/hermes/mcp/servers/external/scribase-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
