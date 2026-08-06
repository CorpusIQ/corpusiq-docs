#!/usr/bin/env python3
"""
Inject JSON-LD structured data into built HTML pages for AEO/SEO.
Adds FAQPage, Article, BreadcrumbList, and Organization schema.
"""
import os, re, json, html as html_mod
from pathlib import Path

BUILD_DIR = os.path.expanduser("~/corpusiq-docs/site")
COUNT = {"faq": 0, "article": 0, "breadcrumb": 0}

def extract_faq_pairs(html_content):
    """Extract Q&A pairs from HTML FAQ sections."""
    pairs = []
    # MkDocs renders FAQ as: <p><strong>Q: question</strong><br />A: answer</p>
    pattern = r'<strong>Q:\s*(.*?)</strong>\s*<br\s*/?>\s*A:\s*(.*?)</p>'
    matches = re.findall(pattern, html_content, re.DOTALL)

    for question, answer in matches:
        q_clean = re.sub(r'<[^>]+>', '', question).strip()[:200]
        a_clean = re.sub(r'<[^>]+>', '', answer).strip()[:500]
        if q_clean and a_clean:
            pairs.append((q_clean, a_clean))

    # Also try alternative format: <strong>Question:</strong>
    if not pairs:
        pattern2 = r'<strong>Question:\s*(.*?)</strong>\s*<br\s*/?>\s*Answer:\s*(.*?)</p>'
        matches2 = re.findall(pattern2, html_content, re.DOTALL)
        for question, answer in matches2:
            q_clean = re.sub(r'<[^>]+>', '', question).strip()[:200]
            a_clean = re.sub(r'<[^>]+>', '', answer).strip()[:500]
            if q_clean and a_clean:
                pairs.append((q_clean, a_clean))

    return pairs

def extract_title(html_content):
    """Extract page title from H1 or title tag."""
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', html_content)
    if h1:
        return re.sub(r'<[^>]+>', '', h1.group(1)).strip()
    t = re.search(r'<title>(.*?)</title>', html_content)
    if t:
        return t.group(1).strip()
    return ""

def extract_description(html_content):
    """Extract meta description."""
    d = re.search(r'<meta[^>]+name="description"[^>]+content="([^"]+)"', html_content)
    if d:
        return d.group(1)[:300]
    return ""

def build_faq_schema(pairs, page_url):
    """Build FAQPage JSON-LD."""
    entities = []
    for q, a in pairs:
        entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })
    
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities
    }

def build_article_schema(title, description, page_url, date_published="2026-08-06"):
    """Build Article JSON-LD."""
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": description,
        "url": page_url,
        "datePublished": date_published,
        "dateModified": date_published,
        "publisher": {
            "@type": "Organization",
            "name": "CorpusIQ",
            "url": "https://www.corpusiq.io"
        }
    }

def build_breadcrumb_schema(path_parts, base_url="https://www.corpusiq.io"):
    """Build BreadcrumbList JSON-LD."""
    items = []
    url = base_url
    for i, part in enumerate(path_parts):
        name = part.replace('-', ' ').replace('.html', '').title()
        if name.lower() in ['docs', 'site', 'index']:
            continue
        url += '/' + part if not part.endswith('.html') else '/' + part.replace('.html', '')
        items.append({
            "@type": "ListItem",
            "position": len(items) + 1,
            "name": name,
            "item": url
        })
    
    if not items:
        return None
    
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items
    }

def inject_schema(html_path):
    """Inject structured data into an HTML file."""
    with open(html_path) as f:
        content = f.read()
    
    # Extract info
    faq_pairs = extract_faq_pairs(content)
    title = extract_title(content)
    description = extract_description(content)
    
    # Determine page URL
    rel_path = html_path.replace(BUILD_DIR, '').lstrip('/')
    page_url = f"https://www.corpusiq.io/{rel_path}"
    
    # Build schemas
    schemas = []
    
    if len(faq_pairs) >= 2:
        schemas.append(build_faq_schema(faq_pairs, page_url))
        COUNT["faq"] += 1
    
    if title:
        schemas.append(build_article_schema(title, description, page_url))
        COUNT["article"] += 1
    
    path_parts = [p for p in rel_path.split('/') if p]
    breadcrumb = build_breadcrumb_schema(path_parts)
    if breadcrumb:
        schemas.append(breadcrumb)
        COUNT["breadcrumb"] += 1
    
    if not schemas:
        return
    
    # Build injection block
    schema_html = ""
    for schema in schemas:
        schema_html += f'\n<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>'
    
    # Inject before </head>
    if '</head>' in content:
        content = content.replace('</head>', schema_html + '\n</head>')
    elif '<body' in content:
        # Inject after opening body tag
        content = re.sub(r'(<body[^>]*>)', r'\1' + schema_html, content)
    
    with open(html_path, 'w') as f:
        f.write(content)

# Walk the build directory
for root, dirs, files in os.walk(BUILD_DIR):
    for f in files:
        if f.endswith('.html') and not f.startswith('404'):
            try:
                inject_schema(os.path.join(root, f))
            except Exception as e:
                pass  # Skip problematic files

print(f"Structured data injected:")
print(f"  FAQPage: {COUNT['faq']} pages")
print(f"  Article: {COUNT['article']} pages")
print(f"  BreadcrumbList: {COUNT['breadcrumb']} pages")
