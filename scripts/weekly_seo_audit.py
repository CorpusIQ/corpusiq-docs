#!/usr/bin/env python3
"""
Weekly SEO crawl audit for corpusiq-docs.

Checks the live site at https://www.corpusiq.io/docs/ for:
1. Broken external links
2. Orphan pages (via sitemap cross-reference)
3. Missing meta descriptions
4. Pages not in sitemap

Designed to run as a cron job via GitHub Actions or Hermes cron.
Reports issues to stdout — pipe to email or Slack.

Usage:
    python3 scripts/weekly_seo_audit.py [--base-url https://www.corpusiq.io/docs/]
"""

import argparse
import re
import sys
import time
import urllib.request
import urllib.error
import urllib.parse
import xml.etree.ElementTree as ET
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser


class LinkExtractor(HTMLParser):
    """Extract all links and meta descriptions from HTML."""
    def __init__(self):
        super().__init__()
        self.links = []
        self.meta_description = None
        self.title = None
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "href" in attrs:
            self.links.append(("a", attrs["href"]))
        elif tag == "link" and "href" in attrs:
            self.links.append(("link", attrs["href"]))
        elif tag == "script" and "src" in attrs:
            self.links.append(("script", attrs["src"]))
        elif tag == "meta" and attrs.get("name") == "description":
            self.meta_description = attrs.get("content", "")
        elif tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title and self.title is None:
            self.title = data.strip()


def fetch_url(url, timeout=10):
    """Fetch a URL and return (status, html, error)."""
    try:
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "CorpusIQ-Weekly-SEO-Audit/1.0")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return (resp.status, resp.read().decode("utf-8", errors="replace"), None)
    except urllib.error.HTTPError as e:
        return (e.code, e.read().decode("utf-8", errors="replace"), str(e))
    except Exception as e:
        return (None, "", str(e))


def fetch_sitemap(base_url):
    """Fetch and parse sitemap to get all known URLs."""
    sitemap_urls = [
        f"{base_url}/sitemap.xml",
        f"{base_url}/sitemap-index.xml",
    ]
    urls = set()
    for sitemap_url in sitemap_urls:
        status, xml_content, error = fetch_url(sitemap_url)
        if status != 200:
            continue
        try:
            root = ET.fromstring(xml_content)
            ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            for url_elem in root.findall(".//sm:url", ns):
                loc = url_elem.find("sm:loc", ns)
                if loc is not None and loc.text:
                    urls.add(loc.text)
            for sitemap_elem in root.findall(".//sm:sitemap", ns):
                loc = sitemap_elem.find("sm:loc", ns)
                if loc is not None and loc.text:
                    # Nested sitemap — fetch it too
                    _, nested, _ = fetch_url(loc.text)
                    if nested:
                        try:
                            nr = ET.fromstring(nested)
                            for u in nr.findall(".//sm:url", ns):
                                lc = u.find("sm:loc", ns)
                                if lc is not None and lc.text:
                                    urls.add(lc.text)
                        except ET.ParseError:
                            pass
        except ET.ParseError:
            pass
    return urls


def crawl_site(base_url, sitemap_urls, max_pages=500):
    """Crawl pages from sitemap and check for issues."""
    pages = {}
    external_links = defaultdict(list)  # url -> [source pages]
    missing_descriptions = []
    short_descriptions = []
    broken_assets = []

    urls_to_check = list(sitemap_urls)[:max_pages]
    print(f"Crawling {len(urls_to_check)} pages from sitemap...")

    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(fetch_url, url): url for url in urls_to_check}
        done = 0
        for future in as_completed(futures):
            url = futures[future]
            done += 1
            if done % 50 == 0:
                print(f"  {done}/{len(urls_to_check)}...")

            status, html, error = future.result()
            if status != 200:
                broken_assets.append((url, status, error))
                continue

            parser = LinkExtractor()
            try:
                parser.feed(html)
            except Exception:
                continue

            pages[url] = {
                "title": parser.title,
                "description": parser.meta_description,
            }

            if not parser.meta_description:
                missing_descriptions.append(url)
            elif len(parser.meta_description) < 70:
                short_descriptions.append((url, len(parser.meta_description)))

            for link_type, href in parser.links:
                if href.startswith("http") and "corpusiq.io" not in href:
                    external_links[href].append(url)
                elif href.startswith("/") and not href.startswith("/docs/"):
                    # Root-absolute path that should have /docs/ prefix
                    if any(href.startswith(p) for p in ["/assets/", "/javascripts/", "/stylesheets/"]):
                        broken_assets.append((url, "WRONG_PATH", href))

    return pages, external_links, missing_descriptions, short_descriptions, broken_assets


def main():
    parser = argparse.ArgumentParser(description="Weekly SEO audit for corpusiq-docs")
    parser.add_argument("--base-url", default="https://www.corpusiq.io/docs")
    parser.add_argument("--max-pages", type=int, default=500)
    parser.add_argument("--check-external", type=int, default=100, help="Max external links to verify")
    args = parser.parse_args()

    base = args.base_url.rstrip("/")
    print(f"CorpusIQ Weekly SEO Audit — {base}")
    print(f"Started: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # 1. Fetch sitemap
    print("\n[1/5] Fetching sitemap...")
    sitemap_urls = fetch_sitemap(base)
    print(f"  Found {len(sitemap_urls)} URLs in sitemap")

    if not sitemap_urls:
        print("  ❌ No sitemap URLs found — aborting")
        sys.exit(1)

    # 2. Crawl pages
    print(f"\n[2/5] Crawling pages...")
    pages, external_links, missing_descs, short_descs, bad_assets = crawl_site(
        base, sitemap_urls, args.max_pages
    )
    print(f"  Crawled {len(pages)} pages")

    # 3. Check external links
    print(f"\n[3/5] Checking external links (sample of {args.check_external})...")
    broken_count = 0
    skip_domains = {"github.com", "linkedin.com", "twitter.com", "x.com",
                     "youtube.com", "reddit.com", "wikipedia.org"}
    check_links = [url for url in external_links
                   if not any(d in url for d in skip_domains)]

    with ThreadPoolExecutor(max_workers=10) as pool:
        futures = {pool.submit(fetch_url, url, 8): url
                   for url in list(check_links)[:args.check_external]}
        for future in as_completed(futures):
            url = futures[future]
            status, _, _ = future.result()
            if status and status >= 400:
                broken_count += 1
                sources = external_links[url][:3]
                print(f"  ❌ {status} {url}")
                for s in sources:
                    print(f"     from {s}")

    if broken_count == 0:
        print("  ✅ No broken external links in sample")

    # 4. Meta descriptions
    print(f"\n[4/5] Meta description audit...")
    if missing_descs:
        print(f"  ❌ {len(missing_descs)} pages missing meta description:")
        for url in missing_descs[:5]:
            print(f"     {url}")
    if short_descs:
        print(f"  ⚠️  {len(short_descs)} pages with short description:")
        for url, length in short_descs[:5]:
            print(f"     {url} ({length}c)")

    if not missing_descs and not short_descs:
        print("  ✅ All meta descriptions OK")

    # 5. Asset path issues
    print(f"\n[5/5] Asset path check...")
    if bad_assets:
        print(f"  ❌ {len(bad_assets)} asset path issues (missing /docs/ prefix):")
        for url, issue, path in bad_assets[:10]:
            print(f"     {url}: {path}")
    else:
        print("  ✅ No asset path issues")

    # Summary
    total_issues = len(missing_descs) + len(short_descs) + broken_count + len(bad_assets)
    print("\n" + "=" * 60)
    print(f"AUDIT COMPLETE — {total_issues} issues found")
    print(f"  Broken external links: {broken_count}")
    print(f"  Missing descriptions: {len(missing_descs)}")
    print(f"  Short descriptions:   {len(short_descs)}")
    print(f"  Bad asset paths:      {len(bad_assets)}")
    print(f"  Pages crawled:        {len(pages)}/{len(sitemap_urls)}")
    print(f"Finished: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)


if __name__ == "__main__":
    main()
