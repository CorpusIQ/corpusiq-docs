---
title: "Google Ads for Agencies: Manager Account Setup"
description: "Set up one Google Ads Manager Account and one agency-controlled Google identity so CorpusIQ can report across linked client accounts."
category: "Connector Guide"
tags: ["Google Ads agency setup", "Google Ads MCC", "manager account", "client accounts", "Google Ads connector"]
last_updated: "2026-08-11"
canonical: "https://www.corpusiq.io/docs/connectors/google-ads-for-agencies"
robots: "index,follow"
---

# Google Ads for agencies: one manager account, one connection

An agency should not create a different Google login for every client it manages.

The clean setup is:

```text
One agency-controlled Google identity
                  |
                  v
Google Ads Manager Account (MCC)
        |                    |
        v                    v
 Client account A       Sub-manager account
                              |
                              v
                       Client account B
```

Connect that agency identity to CorpusIQ once. CorpusIQ discovers the Google Ads accounts linked beneath the manager account, including accounts beneath sub-manager accounts.

## What the agency needs

Before connecting Google Ads to CorpusIQ, confirm all four requirements:

1. **A Google Ads Manager Account (MCC).** This is a separate Google Ads account built to manage multiple advertiser accounts. An ordinary advertiser account is not converted into an agency account.
2. **One designated, login-capable Google identity controlled by the agency.** A managed Google Workspace user such as `ads-reporting@youragency.com` is easier to retain when employees change. It must be a real user that can complete Google sign-in, not a Google Group, forwarding alias, or distribution list. Protect it with multifactor authentication and normal company access controls. Do not share its password broadly.
3. **Every client advertiser account linked to the manager hierarchy.** A client may sit directly beneath the agency's top-level manager account or beneath a linked sub-manager account.
4. **The designated identity has access at the manager level.** Google Ads roles inherit through the linked hierarchy. Read-only access is enough for CorpusIQ reporting; Standard or Admin access also works, but CorpusIQ still exposes read-only reporting tools.

A Google identity is not itself “configured as an agency.” The agency structure lives in the Google Ads Manager Account. The identity is the user that CorpusIQ authenticates.

## Recommended setup

| Use this | Avoid this |
|---|---|
| One Google Ads Manager Account for the agency | A pile of unrelated advertiser accounts with no manager account |
| One agency-controlled Google identity connected to CorpusIQ | One client email and password per advertiser account |
| Client accounts linked beneath the MCC | Logging out and reconnecting CorpusIQ as a different client every time |
| Individual staff keep their own Google users for normal Ads work | A shared password used by the whole agency |
| Clients retain their own access and control | Asking clients to hand the agency their Google credentials |

The client does not lose access when it links its advertiser account to an MCC. Its existing users continue signing in normally, and an account administrator can unlink the manager relationship later.

## Step 1: Create the manager account

If the agency does not already have an MCC:

1. Open Google's [Manager Account page](https://ads.google.com/home/tools/manager-accounts/).
2. Sign in with the designated agency Google identity.
3. Create a manager account and choose the option to manage other people's accounts.
4. Choose the agency's permanent country, time zone, and currency carefully. Google does not let you change some of these values later.

Google's detailed instructions are in [Create a Google Ads manager account](https://support.google.com/google-ads/answer/7459399).

## Step 2: Link each client account

From the manager account:

1. Open **Accounts** and then **Sub-account settings**.
2. Select **Link existing account**.
3. Enter the client's ten-digit Google Ads customer ID.
4. Send the request.
5. Ask an administrator on the client account to accept it under **Admin → Access and security → Managers**.

The account appears under the manager account after the client accepts. Repeat this for every client account the agency wants CorpusIQ to report on.

If the agency uses sub-manager accounts, link those beneath the top-level MCC. CorpusIQ supports nested manager hierarchies and resolves the correct manager context when it queries a leaf advertiser account.

Google's current click path is documented in [Link accounts to your manager account](https://support.google.com/google-ads/answer/7459601).

## Step 3: Verify the designated identity

Before opening CorpusIQ, sign in to Google Ads as the designated agency identity and verify that it can see:

- the top-level manager account;
- any linked sub-manager accounts;
- every client advertiser account the agency expects to query.

If an account is missing in Google Ads while using that identity, it will also be missing from CorpusIQ. Reconnecting OAuth cannot repair an unaccepted manager link or missing Google Ads access.

## Step 4: Connect Google Ads to CorpusIQ once

1. Open **Dashboard → Connectors** in CorpusIQ.
2. Select **Google Ads** and click **Connect**.
3. Sign in with the designated agency Google identity.
4. Approve the Google Ads access request.
5. Return to CorpusIQ and confirm that Google Ads shows as connected.

Do not reconnect once per client. The single OAuth connection represents the designated identity, and the MCC hierarchy supplies the client-account access beneath it.

## Step 5: Verify account discovery

Ask your connected AI client:

> Use CorpusIQ to list every Google Ads account I can access. Include customer ID, account name, whether it is a manager account, and its parent manager when available.

The result should include the top-level MCC, sub-manager accounts, and leaf advertiser accounts.

Then test one client:

> Show Google Ads account performance for client customer ID 123-456-7890 for the last 30 days.

CorpusIQ automatically resolves the manager account required for that child account. Advanced callers may pass `login_customer_id` explicitly, but normal agency users should not need to manage that field.

## What happens when the agency uses separate client logins

A CorpusIQ Google Ads connection authenticates one Google identity. It can only discover accounts that identity can access.

If Client A is available only through `client-a@example.com` and Client B only through `client-b@example.com`, connecting one of those users will not make both accounts visible. The agency should either:

- link both advertiser accounts to its MCC; or
- grant the designated agency identity direct access to the accounts.

If a client will not permit either option, contact [support@corpusiq.io](mailto:support@corpusiq.io) before onboarding that account. Do not send passwords or OAuth codes to support.

## Troubleshooting

### The MCC appears, but a child account does not

Check that the client accepted the link request and that the account appears in Google Ads when signed in as the same identity used for CorpusIQ. A pending invitation is not an active link.

### The account appears, but a query returns `USER_PERMISSION_DENIED`

Confirm the complete path from the top-level MCC through any sub-manager to the advertiser account. Then ask CorpusIQ to list accounts again before retrying the report. If the error remains, send support the manager and advertiser customer IDs, but no credentials.

### Reconnecting did not help

Repeated OAuth consent does not fix a missing MCC link or a Google Ads role problem. Repair the account hierarchy or user access in Google Ads first.

### A former employee owns the connected identity

Move the MCC access to an agency-controlled identity, then reconnect Google Ads in CorpusIQ with that identity. This is why a managed role address is preferable to one employee's personal account.

## What CorpusIQ can and cannot do

CorpusIQ can read account, campaign, ad group, ad, keyword, search-term, geographic, device, demographic, and performance data exposed by Google Ads.

CorpusIQ does not create campaigns, change bids or budgets, pause ads, accept manager links, or change Google Ads user permissions. Those actions remain in Google Ads.

## Official Google references

- [About Google Ads Manager Accounts](https://support.google.com/google-ads/answer/6139186)
- [Create a Manager Account](https://support.google.com/google-ads/answer/7459399)
- [Link Client Accounts](https://support.google.com/google-ads/answer/7459601)
- [Google Ads API access model](https://developers.google.com/google-ads/api/docs/oauth/access-model)
