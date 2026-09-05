# Firecrawl Auth & Onboarding Workflows

## 1. Quick Onboarding CLI
To run full setup non-interactively with browser sign-in:
```bash
npx -y firecrawl-cli@latest init --all --browser
```

Flags:
- `--all`: Non-interactive initialization for all detected agent environments.
- `--browser`: Launch browser auth flow.
- `--skip-auth`, `--skip-install`, `--skip-skills`, `--agent <name>`.

---

## 2. Programmatic CLI Auth Flow (Path D)

When helping a human sign in without automatic browser launch:

### Step 1 — Generate Auth Parameters
```bash
SESSION_ID=$(openssl rand -hex 32)
CODE_VERIFIER=$(openssl rand -base64 32 | tr '+/' '-_' | tr -d '=\n' | head -c 43)
CODE_CHALLENGE=$(printf '%s' "$CODE_VERIFIER" | openssl dgst -sha256 -binary | openssl base64 -A | tr '+/' '-_' | tr -d '=')
```

### Step 2 — Human Authorization URL
Provide this URL to the human:
```text
https://www.firecrawl.dev/cli-auth?code_challenge=$CODE_CHALLENGE&source=coding-agent#session_id=$SESSION_ID
```

### Step 3 — Poll Status Endpoint
Poll every 3 seconds:
```bash
curl -X POST https://www.firecrawl.dev/api/auth/cli/status \
  -H "Content-Type: application/json" \
  -d "{\"session_id\": \"$SESSION_ID\", \"code_verifier\": \"$CODE_VERIFIER\"}"
```
- `{"status": "pending"}`: Keep polling.
- `{"status": "complete", "apiKey": "fc-...", "teamName": "..."}`: Done.

### Step 4 — Persist Key
```bash
echo "FIRECRAWL_API_KEY=fc-..." >> .env
```

---

## 3. Keyless Free Tier (Path F Fallback)

Used when no API key is available and the human cannot sign up immediately:
- **Available Features:** `search`, `scrape`, `interact`, `parse`, and `/search/research/*`.
- **Unavailable without Key:** `crawl`, `map`, `monitor`, `extract`, batch jobs, and autonomous agents.
- **MCP Endpoint:** `https://mcp.firecrawl.dev/v2/mcp`
- **Rate Limits:** Strictly throttled; switch to an account key as soon as possible.
