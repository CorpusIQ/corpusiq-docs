# API Authentication

The CorpusIQ API uses API keys for authentication. All requests must include your API key in the `Authorization` header.

## Getting an API Key

1. Log in to your [CorpusIQ dashboard](https://corpusiq.io)
2. Go to **Settings > API**
3. Click **Generate API Key**
4. Copy the key — you won't be able to see it again

## Using Your API Key

Include the key in every request:

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
     https://api.corpusiq.io/v1/connectors
```

## Security Best Practices

- Never expose your API key in client-side code or public repositories
- Rotate keys regularly from the dashboard
- Use separate keys for development and production
- API keys have the same permissions as your user account

## Token Expiry

API keys do not expire automatically. You can revoke them at any time from the dashboard.
