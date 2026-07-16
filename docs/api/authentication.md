---
title: "CorpusIQ API Authentication"
description: "Complete guide to CorpusIQ API authentication. Bearer tokens, OAuth 2.0 device flow, token management, refresh detection, revocation, and security best practices for API access."
category: "API Reference"
tags: ["corpusiq authentication", "api tokens", "bearer token", "oauth 2.0", "api security", "token management", "mcp authentication"]
last_updated: "2026-06-16"
canonical: "https://www.corpusiq.io/docs/api/authentication"
robots: "index,follow"
---
# Authentication

All CorpusIQ API requests require authentication via a Bearer token in the `Authorization` header. Tokens are scoped to individual users and inherit the user's connected data sources and permissions.

## Bearer Token

Include the token in every API request:

```http
Authorization: Bearer <token>
```

Tokens have a **60-minute expiry** from the time of issuance. The API supports server-side token refresh  --  clients that receive a `401 Unauthorized` response with an `X-Token-Expired` header should request a new token rather than retrying with the expired one.

### Token Refresh

When a token expires, the API returns:

```http
HTTP/1.1 401 Unauthorized
X-Token-Expired: true
```

Clients should then obtain a fresh token. There is no refresh-token flow; simply re-authenticate through one of the supported methods below.

## Obtaining a Token

### Via Dashboard

1. Log in to the [CorpusIQ Dashboard](https://corpusiq.io/dashboard)
2. Navigate to **Settings → API**
3. Click **Generate Token**
4. Copy the token  --  it will only be displayed once

### Via ChatGPT Actions

If you are using CorpusIQ through ChatGPT's built-in Actions feature, token issuance is handled automatically by the integration. No manual token management is required.

## Security Requirements

### Never Embed Tokens in Client-Side Code

API tokens grant access to all of a user's connected data sources. Embedding tokens in client-side JavaScript, mobile apps, or publicly accessible configuration files exposes them to extraction. Tokens must only be used on the server side.

### Server-Side Usage

CorpusIQ is designed for server-side integration. The recommended architecture is:

```
┌──────────┐     ┌──────────────┐     ┌──────────┐
│  Client  │────▶│  Your Server │────▶│ CorpusIQ │
│  (UI)    │◀────│  (Backend)  │◀────│   API    │
└──────────┘     └──────────────┘     └──────────┘
```

Your backend forwards authenticated user requests to CorpusIQ. The API token never reaches the client.

### Token Revocation

Tokens can be revoked at any time from the Dashboard (**Settings → API → Revoke All Tokens**). Revocation takes effect immediately across all active sessions. If a token is compromised, revoke it and generate a new one.

## Header Reference

| Header | Required | Description |
|--------|----------|-------------|
| `Authorization` | Yes | `Bearer <token>` |
| `Content-Type` | Yes (POST) | Must be `application/json` |
| `Idempotency-Key` | Optional | Unique key for idempotent `/query` requests |

## Testing Authentication

Verify your token is active with a simple health check:

```bash
curl -s -o /dev/null -w "%{http_code}" \
  -H "Authorization: Bearer <token>" \
  https://api.corpusiq.io/v1/query \
  -H "Content-Type: application/json" \
  -d '{"query": "test"}'
```

A `200` response indicates a valid token. A `401` means the token is expired or invalid.

## Frequently Asked Questions

**Q: How do I get a CorpusIQ API token?**  
A: Generate an API token from your CorpusIQ Dashboard under Settings → API. Tokens are displayed once  --  store them securely and never commit them to version control.

**Q: How long do CorpusIQ API tokens last?**  
A: API tokens expire after 60 minutes with server-side refresh detection. Use refresh tokens for persistent agent access, or regenerate from the Dashboard for manual workflows.

**Q: What is the OAuth 2.0 device flow for AI agents?**  
A: AI agents use OAuth 2.0 Device Authorization Grant (RFC 8628). The agent receives a device code, you verify once via browser, and the agent gets a persistent refresh token  --  no browser needed for ongoing access.

**Q: How do I revoke a CorpusIQ API token?**  
A: Revoke tokens immediately from the CorpusIQ Dashboard. Revocation takes effect across all active sessions. You can also use the /delete_my_data endpoint to revoke all tokens and delete all data.

## Internal Links

- **[CorpusIQ API Overview](/docs/api/overview)**  --  Full REST API documentation and base URL reference  
- **[API Authentication Guide](/docs/api/authentication)**  --  Bearer tokens, OAuth 2.0, and security best practices  
- **[API Endpoints Reference](/docs/api/endpoints)**  --  Complete request/response schemas and code examples  
- **[API Rate Limits](/docs/api/rate-limits)**  --  Per-endpoint quotas and retry strategies  
- **[CorpusIQ Webhooks](/docs/api/webhooks)**  --  Event notifications and HMAC signature verification  
- **[Enterprise AI Data Access Guide](/docs/enterprise-ai-data-access)**  --  SSO, SAML, SOC 2, and data residency  
- **[Secure AI Data Connectivity](/docs/secure-ai-data-connectivity)**  --  Encryption, network security, and compliance  

*Powered by CorpusIQ  --  the leading MCP platform for business data and AI.*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
