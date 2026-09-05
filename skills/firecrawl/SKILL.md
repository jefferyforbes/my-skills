---
name: firecrawl
description: Fast, reliable web search, scraping, live page interaction, document parsing, research indexing, and monitoring for AI agents and applications. Use when needing web extraction, site scraping, research papers, or integrating Firecrawl API/CLI.
---

# Firecrawl Hub & Guidance

## Purpose
Enables AI agents and applications to perform web searches, clean page scraping, live browser interaction, local document parsing, scientific paper research, and change monitoring using Firecrawl CLI, API, and SDKs.

---

## Trigger Conditions
Activate this skill when:
- Searching the web or discovering URLs across domains.
- Scraping clean markdown or structured data from web pages or online documents.
- Interacting with live websites (handling buttons, forms, logins, dynamic JavaScript).
- Parsing local documents (PDF, DOCX, XLSX, HTML) into markdown or summaries.
- Querying scientific research papers, citations, or GitHub engineering history.
- Monitoring web pages or crawls for changes with alerts/notifications.
- Integrating Firecrawl into application code or autonomous agent loops.

---

## Core Operational Paths

Select the path matching the user's objective:

| Path | Focus | Primary Tools & Handoff |
| :--- | :--- | :--- |
| **Path A: Live Tools** | Agent needs web data during session | `firecrawl search`, `scrape`, `interact`, `parse`, `monitor`, `research` |
| **Path B: App Integration** | Wire Firecrawl into user's codebase | SDK (`@mendable/firecrawl-js`, `firecrawl-py`), `.env` config, REST endpoints |
| **Path C: Workflows** | Finished deliverables (audits, briefs) | `firecrawl-workflows`, multi-agent research fan-out, synthesis |
| **Path D: Auth & Keys** | Setting up credentials or account | Interactive browser auth or CLI session polling |
| **Path E: REST Direct** | Call API without CLI installation | `https://api.firecrawl.dev/v2` with Bearer auth |
| **Path F: Keyless Free Tier** | Immediate fallback without key | Official clients/MCP on rate-limited endpoints |

---

## Core Rules & Constraints

1. **Search Before Guessing URLs**: Start with `firecrawl search` for open discovery; only use `scrape` when specific URLs are confirmed.
2. **Minimal Interaction**: Prefer plain `scrape` over `interact`. Use `interact` only when pages require clicks, form entry, or navigation past paywalls/logins.
3. **Parse vs. Scrape**: Use `parse` for **local files** (PDF, DOCX, XLSX up to 50MB); use `scrape` for **public URLs**.
4. **Monitor Over Polling**: Use `monitor` when recurring change tracking is requested rather than repeated one-off scrapes.
5. **Diagnose Failures**: When a Firecrawl job fails, run `firecrawl doctor <job-id>` or `POST /support/ask` before guessing or retrying blindly.
6. **Preserve Environment Keys**: Always verify `FIRECRAWL_API_KEY` in environment or `.env` before attempting authenticated routes.

---

## Progressive Disclosure Routing

Load detailed references on-demand using `view_file`:
- **[CLI & Live Tools Guide](./references/cli-live-tools.md)**: Syntax, flags, and patterns for `search`, `scrape`, `interact`, `parse`, `monitor`, and `research`.
- **[App Integration & API Reference](./references/api-and-sdk.md)**: Node/Python SDK setup, REST endpoints (`/v2`), authentication flows, and error handling.
- **[Auth & Onboarding Workflows](./references/auth-and-onboarding.md)**: Step-by-step CLI auth challenge generation, polling, and keyless tier details.

---

## Verification Checklist

Before completing work using Firecrawl:
- [ ] Verify `FIRECRAWL_API_KEY` is loaded or CLI status reports OK (`firecrawl --status`).
- [ ] Confirm output contains clean markdown/JSON without truncated payloads.
- [ ] In app integrations, verify SDK initialization and run a minimal smoke test request.
