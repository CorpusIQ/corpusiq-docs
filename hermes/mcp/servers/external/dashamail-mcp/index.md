---
title: "DashaMail MCP"
description: "DashaMail email marketing MCP for AI agents."
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/dashamail-mcp/"
robots: "index,follow"
last_updated: "2026-09-17"
tags: [mcp server, model context protocol, hermes mcp, email, marketing]
---
# DashaMail MCP

DashaMail MCP gives AI agents programmatic access to DashaMail's email marketing platform. Manage campaigns, flows, metrics, and audience data through a unified MCP interface.

## Quick Start

```bash
# Add DashaMail MCP to Hermes
hermes mcp add dashamail -- url https://dasha-mcp.com/sse
```

## Available Tools

### Campaign Management

```bash
mcp_dashamail_connector(action="get_campaigns")
```

## Use Cases

### Automated Campaign Reporting

```python
dashamail = mcp_dashamail_connector()
```

## Configuration

### OAuth Setup

1. Run `hermes mcp add dashamail`
2. Visit the generated URL and authorize the application
3. Complete the OAuth flow in your browser
4. Token is stored automatically for future sessions

### API Key Alternative

# Generate API key from DashaMail dashboard
# Then add with key
hermes mcp add dashamail -- key YOUR_API_KEY_HERE

## Integration Notes

- **Rate Limits:** Default 100 requests/minute, adjustable per plan
- **Idempotency:** All write operations support idempotency keys
- **Error Handling:** MCP errors include error codes and messages for retry logic
- **Data Freshness:** Real-time for campaigns, 5-minute delayed for aggregate metrics

## Related Guides

- [Convert.Online MCP](/hermes/mcp/servers/external/convert-online-mcp) - File conversion companion
- [AurasPay Merchant MCP](/hermes/mcp/servers/external/auraspay-mcp) - Payment integration
- [Google Analytics 4](/hermes/mcp/servers/external/google-analytics-mcp) - Analytics correlation
