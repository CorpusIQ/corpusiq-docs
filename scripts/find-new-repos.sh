#!/bin/bash
# Daily ecosystem discovery - finds new repos to add to the ecosystem directory.
# Run from the docs repo root: cd /path/to/corpusiq-docs
#
# Set GITHUB_TOKEN before running (a classic PAT with public repo read is enough).

# Tracked repos: BOTH directory surfaces. The served page is ecosystem/index.md;
# ecosystem.md is its shadowed twin. Reading one and writing the other made every
# promoted repo look new again on the next run.
TRACKED=$(mktemp)
grep -hoP 'github\.com/\K[^/)]+' hermes/ecosystem.md hermes/ecosystem/index.md 2>/dev/null | sort -u > "$TRACKED"

for query in "hermes-agent+skill" "mcp+server+ai" "openclaw+skill" "agent+skill+code" "ai+employee+slack"; do
  curl -s "https://api.github.com/search/repositories?q=$query&sort=updated&per_page=10" \
    -H "Authorization: token $(cat /home/hermes/.hermes/profiles/corpusiq/secrets/github.token)" \
    | python3 -c "
import json,sys
for r in json.load(sys.stdin).get('items',[]):
    if r['stargazers_count'] < 30: continue
    print(f'{r[\"full_name\"]:50s} ⭐{r[\"stargazers_count\"]:6d} {r[\"description\"] or \"\"}'[:120])
" 2>/dev/null
done | sort -u
rm "$TRACKED"
