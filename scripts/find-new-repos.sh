#!/bin/bash
# Daily ecosystem discovery — finds new repos to add to hermes/ecosystem.md
cd /tmp/corpusiq-docs

# Tracked repos
TRACKED=$(mktemp)
grep -oP 'github\.com/\K[^/)]+' hermes/ecosystem.md | sort -u > "$TRACKED"

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
