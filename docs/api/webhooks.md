---
title: "CorpusIQ Webhooks  --  Event Notifications and HMAC Signature Verification"
description: "Complete CorpusIQ webhooks guide: event types (user.deleted), HMAC-SHA256 signature verification, retry with exponential backoff, payload format, and setup instructions."
category: "API Reference"
tags: ["corpusiq webhooks", "event notifications", "hmac signature", "webhook security", "user deleted event", "webhook setup", "api events"]
last_updated: "2026-06-16"
canonical: "https://www.corpusiq.io/docs/api/webhooks"
robots: "index,follow"
---
# Webhooks

CorpusIQ webhooks notify your application when specific events occur, such as user data deletion. Webhooks are delivered as HTTP POST requests to a URL you configure in the CorpusIQ Dashboard.

## Registering a Webhook

1. Log in to the [CorpusIQ Dashboard](https://corpusiq.io/dashboard)
2. Navigate to **Settings → Webhooks**
3. Enter your endpoint URL (must be HTTPS)
4. Copy the signing secret  --  it will only be displayed once

CorpusIQ sends a verification request to your endpoint during registration. Your server must respond with HTTP `200` to confirm the endpoint is reachable.

## Delivery

Each webhook delivery is an HTTP POST with `Content-Type: application/json`. The request body follows the [Webhook Event Schema](/docs/api/schemas#webhook-event).

### Headers

| Header | Description |
|--------|-------------|
| `Content-Type` | Always `application/json` |
| `CorpusIQ-Signature` | HMAC-SHA256 signature for payload verification |
| `CorpusIQ-Event-Id` | Unique event delivery ID |
| `CorpusIQ-Event-Type` | Event type (e.g., `user.deleted`) |

### Payload Example

```json
{
  "event_id": "evt_a1b2c3",
  "event_type": "user.deleted",
  "created_at": "2026-06-16T14:22:00Z",
  "data": {
    "user_id": "usr_x9y8z7",
    "details": {
      "oauth_tokens_revoked": 12,
      "archive_entries_removed": 847
    }
  }
}
```

## Signature Verification

Every webhook delivery includes a `CorpusIQ-Signature` header containing an HMAC-SHA256 signature. You must verify this signature to ensure the payload originated from CorpusIQ and has not been tampered with.

### How Verification Works

1. CorpusIQ computes `HMAC-SHA256(payload, secret)` using your webhook signing secret
2. The result is sent in the `CorpusIQ-Signature` header
3. Your server recomputes the HMAC using the raw request body and your stored secret
4. If the signatures match, the payload is authentic

### Verification Code

**Python**

```python
import hmac
import hashlib

def verify_signature(payload: bytes, signature: str, secret: str) -> bool:
    expected = hmac.new(
        secret.encode("utf-8"),
        payload,
        hashlib.sha256,
    ).hexdigest()
    return hmac.compare_digest(expected, signature)

# In your webhook handler:
raw_body = request.body
sig_header = request.headers.get("CorpusIQ-Signature", "")

if not verify_signature(raw_body, sig_header, WEBHOOK_SECRET):
    return 403, "Invalid signature"
```

**JavaScript (Node.js)**

```javascript
const crypto = require("crypto");

function verifySignature(payload, signature, secret) {
  const expected = crypto
    .createHmac("sha256", secret)
    .update(payload)
    .digest("hex");
  return crypto.timingSafeEqual(
    Buffer.from(expected),
    Buffer.from(signature)
  );
}

// In your Express route:
app.post("/webhooks/corpusiq", (req, res) => {
  const rawBody = req.rawBody; // Use raw body, not parsed JSON
  const sig = req.headers["corpusiq-signature"];

  if (!verifySignature(rawBody, sig, process.env.CORPUSIQ_WEBHOOK_SECRET)) {
    return res.status(403).send("Invalid signature");
  }

  const event = JSON.parse(rawBody);
  // Process event...
  res.status(200).send("OK");
});
```

**Important**: Always use the raw request body for signature verification, not a parsed JSON object. JSON serialization differences between libraries can cause mismatched signatures.

## Response Expectations

Your webhook endpoint must respond with an HTTP `2xx` status within 10 seconds. CorpusIQ retries failed deliveries with exponential backoff:

| Attempt | Delay |
|---------|-------|
| 1st retry | 60 seconds |
| 2nd retry | 5 minutes |
| 3rd retry | 15 minutes |
| 4th retry | 1 hour |

After 5 failed attempts, the delivery is dropped. Monitor the Dashboard for delivery failures.

## Supported Events

| Event Type | Trigger |
|------------|---------|
| `user.deleted` | A user permanently deletes their data via `/delete_my_data` |

Additional events will be documented here as they become available. Subscribe to the [Changelog](/docs/changelog) for updates.

## Security Considerations

- Always verify the `CorpusIQ-Signature` header before processing any webhook payload
- Store your webhook signing secret securely (environment variables, secrets manager)
- Use HTTPS for your webhook endpoint  --  CorpusIQ will not deliver to HTTP URLs
- Process webhooks idempotently using the `event_id` field to handle retries
- Respond with `200` before performing long-running processing to avoid timeouts

## Frequently Asked Questions

**Q: What events do CorpusIQ webhooks support?**  
A: Currently, CorpusIQ webhooks fire the user.deleted event when a user's data is permanently deleted via the /delete_my_data endpoint. Additional event types are on the roadmap.

**Q: How are webhook payloads secured?**  
A: All webhook deliveries are signed with HMAC-SHA256 using a per-endpoint signing secret. The signature is included in the CorpusIQ-Signature header for verification.

**Q: What happens when a webhook delivery fails?**  
A: Failed deliveries are retried with exponential backoff: 60s → 5min → 15min → 1hr. Configure your endpoint to handle duplicate deliveries by checking the event ID.

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
