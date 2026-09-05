# Firecrawl API & SDK Reference (Path B & E)

## Base Configuration
- **Base URL:** `https://api.firecrawl.dev/v2`
- **Auth Header:** `Authorization: Bearer fc-YOUR_API_KEY`

---

## 1. SDK Installation

### TypeScript / Node.js
```bash
npm install @mendable/firecrawl-js
```

### Python
```bash
pip install firecrawl-py
```

---

## 2. Code Patterns

### TypeScript Example
```typescript
import FirecrawlApp from '@mendable/firecrawl-js';

const app = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Scrape URL to clean markdown
async function runScrape(url: string) {
  const scrapeResponse = await app.scrapeUrl(url, {
    formats: ['markdown'],
  });

  if (!scrapeResponse.success) {
    throw new Error(`Failed to scrape: ${scrapeResponse.error}`);
  }
  return scrapeResponse.markdown;
}

// Search web
async function runSearch(query: string) {
  const searchResults = await app.search(query, {
    limit: 5,
  });
  return searchResults;
}
```

### Python Example
```python
import os
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key=os.environ.get("FIRECRAWL_API_KEY"))

# Scrape URL
scrape_result = app.scrape_url('https://firecrawl.dev', params={'formats': ['markdown']})
print(scrape_result['markdown'])

# Search
search_result = app.search('multi-agent systems 2026', params={'limit': 5})
```

---

## 3. Direct REST Endpoints (`/v2`)

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/v2/search` | Search query, returns pages and optional extracted content |
| `POST` | `/v2/scrape` | Extract markdown/JSON from a URL (supports web & online PDFs) |
| `POST` | `/v2/interact` | Standalone browser session for dynamic actions |
| `POST` | `/v2/scrape/{scrapeId}/interact` | Run clicks, forms, or nav against previously scraped page |
| `POST` | `/v2/parse` | Multipart upload for local docs (PDF, DOCX, XLSX up to 50MB) |
| `POST` | `/v2/monitor` | Create change monitoring job (scrape/crawl/search target) |
| `GET` | `/v2/monitor` | List existing monitors |
| `GET` | `/v2/monitor/{id}/checks` | Get page check history and diff evaluations |
| `GET` | `/v2/search/research/papers` | Query scientific paper index |
| `GET` | `/v2/search/research/papers/{id}` | Paper metadata & passage search |
| `GET` | `/v2/search/research/papers/{id}/similar` | Similar, citers, and reference expansions |
| `GET` | `/v2/search/research/github` | Search GitHub issues, PRs, and READMEs |
| `POST` | `/v2/support/ask` | AI diagnostic tool for failed jobs (pass `{ "question": "..." }`) |
| `POST` | `/v2/support/docs-search` | Official documentation query with source citations |
