# Case Study: Ecommerce Operations

Ecommerce businesses run on tight margins, high transaction volumes, and relentless operational cadence. Hermes automation transforms reactive firefighting into proactive management across the entire commerce lifecycle.

## Inventory Synchronization

Multi-channel sellers face a constant challenge: keeping inventory accurate across their own store, Amazon, eBay, and wholesale channels. Manual reconciliation is slow, and overselling damages seller ratings and customer trust.

**The Hermes approach:** A scheduled cron runs every 15 minutes during business hours (every 60 minutes overnight), querying each channel's inventory API and comparing against the source-of-truth warehouse system. Discrepancies are triaged:

- **Confirmed stock-outs on a channel** with available warehouse inventory → automatic restock push
- **Warehouse stock below safety threshold** and channel still showing availability → alert with explicit "reduce quantity to X" recommendation
- **Cross-channel conflict** (same SKU sold on two channels simultaneously) → immediate alert with order details for manual resolution

A skill bundles the inventory health check into a single invocation: "Check inventory health" returns a dashboard of SKUs with negative available quantities, items below reorder point, and channels with the highest discrepancy rates. This skill runs as a cron at 8 AM daily so the operations team starts each day with a clear picture.

## Order Processing Pipeline

Orders flow in from multiple channels with different fulfillment requirements. Amazon FBA orders need different handling than Shopify direct-ship orders.

**The pipeline:** A cron monitors new orders across channels every 10 minutes. It enriches each order with customer history (repeat buyer? VIP tier?), flags high-value orders for priority handling, and routes to the appropriate fulfillment workflow:

- **FBA orders:** Verify the FBA shipment was created, log the order for reconciliation
- **Direct-ship orders:** Generate pick lists, check inventory allocation, flag items needing special packaging
- **Pre-order/backorder items:** Trigger customer notification with updated ETA

A "Daily order digest" skill provides the morning summary: orders received, average order value, fulfillment status breakdown, and any orders stuck in processing for more than 4 hours.

## Abandoned Cart Recovery

Cart abandonment costs ecommerce businesses billions annually. Hermes turns abandoned carts from lost revenue into recovery opportunities.

**The flow:** A cron checks for abandoned carts (items added, no purchase within 2 hours). It segments carts by value:

- **High-value carts** (>$200): Personal follow-up within 4 hours. A skill drafts a personalized email referencing the specific items and offering assistance.
- **Mid-value carts** ($50-$200): Automated recovery email at 4 hours, reminder at 24 hours
- **Low-value carts** (<$50): Single automated email at 24 hours

A "Cart recovery report" skill shows recovery rate by value tier, channel, and time window. This data feeds into optimization decisions — are high-value cart emails converting? Should the timing change?

## Multi-Channel Listing Management

Managing product listings across channels is tedious and error-prone. Prices, descriptions, images, and variants must stay consistent.

**The Hermes approach:** A "Listing audit" skill compares listings across channels:

- Price parity violations (same product, different prices across channels) trigger alerts
- Missing or broken images are flagged
- Inconsistent product titles or descriptions are surfaced
- Missing channels (product listed on Shopify but not Amazon) are identified

For businesses using MAP (Minimum Advertised Price) policies, a cron monitors marketplace prices daily and flags unauthorized discounters.

## Common Patterns and Anti-Patterns

**Works well:**
- Inventory crons at staggered intervals to avoid API rate limits
- Order enrichment as a separate step from order processing
- Recovery email sequences with clear opt-out mechanisms
- Multi-channel price monitoring with configurable tolerance thresholds

**Avoid:**
- Real-time inventory sync on every single order (use event-driven architecture instead of polling)
- Automated price changes without human review when margin impact exceeds 2%
- Sending recovery emails to customers who placed orders through another channel (check before sending)
- Hardcoding channel-specific logic (use a channel abstraction layer)

## Integration Patterns

Most ecommerce Hermes setups connect to:
- Ecommerce platform (Shopify, WooCommerce, Magento)
- Marketplaces (Amazon Seller Central, eBay, Walmart)
- Email marketing (Klaviyo, Mailchimp)
- Analytics (GA4)
- Accounting (QuickBooks, Xero)
- Shipping (ShipStation, EasyPost)

The value compounds with each integration. Inventory from the warehouse, orders from Shopify, customer segments from Klaviyo, and financials from QuickBooks give Hermes a complete picture that no single dashboard provides.
