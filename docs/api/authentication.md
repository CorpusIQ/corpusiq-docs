# Authentication

All CorpusIQ API requests require authentication via a Bearer token in the `Authorization` header. Tokens are scoped to individual users and inherit the user's connected data sources and permissions.

## Bearer Token

Include the token in every API request:

```http
Authorization: Bearer <token>
```

Tokens have a **60-minute expiry** from the time of issuance. The API supports server-side token refresh — clients that receive a `401 Unauthorized` response with an `X-Token-Expired` header should request a new token rather than retrying with the expired one.

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
4. Copy the token — it will only be displayed once

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
