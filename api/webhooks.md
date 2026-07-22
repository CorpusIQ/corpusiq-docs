# Webhooks

CorpusIQ can send HTTP callbacks to your server when events happen in your account.

## Available Events

| Event | Description |
|-------|-------------|
| `connector.connected` | A new data source was connected |
| `connector.disconnected` | A data source was removed |
| `connector.sync_completed` | A connector finished syncing |
| `query.completed` | A query finished executing |
| `query.failed` | A query encountered an error |

## Setting Up Webhooks

1. Go to **Settings > Webhooks** in the dashboard
2. Enter your endpoint URL
3. Select which events to subscribe to
4. Copy the signing secret to verify payloads

## Payload Format

```json
{
  "event": "query.completed",
  "created_at": "2026-07-22T12:00:14Z",
  "data": {
    "query_id": "qry_xyz789",
    "status": "completed"
  }
}
```

## Verifying Payloads

Each webhook includes a `CorpusIQ-Signature` header. Verify it using your signing secret:

```python
import hmac, hashlib

def verify_signature(payload, signature, secret):
    expected = hmac.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature)
```
