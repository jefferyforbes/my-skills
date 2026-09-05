# Firecrawl CLI & Live Tools Guide

## Overview
Firecrawl CLI provides agents with direct terminal commands to scrape, search, interact with, parse, and monitor web resources during an active session.

Install or run on-demand:
```bash
npx -y firecrawl-cli@latest <command>
# Or install globally:
# npm install -g firecrawl-cli
```

---

## 1. Quick Status & Diagnostics
```bash
# Check CLI status and authentication
firecrawl --status

# Diagnose a failed job ID
firecrawl doctor <job-id>
```

---

## 2. Web Search (`firecrawl search`)
Use when you need to discover pages from a query before scraping.
```bash
# Search web and return top result URLs & snippets
firecrawl search "query"

# Search and output clean markdown results to file
firecrawl search "latest advancements in kotlin multiplatform" -o .firecrawl/search-results.md
```

---

## 3. Web Scraping (`firecrawl scrape`)
Extract clean markdown or structured data from a single public URL.
```bash
# Basic scrape to stdout
firecrawl scrape "https://example.com"

# Scrape to output markdown file
firecrawl scrape "https://firecrawl.dev" -o .firecrawl/install-check.md

# Public document URLs (PDFs, DOCX) can be scraped directly
firecrawl scrape "https://example.com/spec.pdf" -o .firecrawl/spec.md
```

---

## 4. Live Browser Interaction (`firecrawl interact`)
Use when content requires button clicks, dropdown selections, form submissions, or handling dynamic JavaScript.
```bash
# Interact with a page using plain language prompt
firecrawl interact "https://example.com/login" --prompt "Click login button and wait for dashboard"
```

---

## 5. Local Document Parsing (`firecrawl parse`)
Converts local documents (PDF, DOCX, DOC, ODT, RTF, XLSX, XLS, HTML up to 50 MB) into markdown.
```bash
# Convert local PDF to markdown
firecrawl parse ./report.pdf -o .firecrawl/report.md

# Generate an AI summary from a local doc
firecrawl parse ./spec.docx -S -o .firecrawl/summary.md

# Answer a specific question from a doc
firecrawl parse ./financials.xlsx -Q "What was the Q3 operating margin?"
```

---

## 6. Site Crawling & Mapping
```bash
# Discover URLs across a domain
firecrawl map "https://example.com"

# Bulk crawl an entire site / section
firecrawl crawl "https://example.com/docs"

# Download site or section for offline use (experimental)
firecrawl x download "https://example.com/docs" -o ./offline-docs
```

---

## 7. Change Monitoring (`firecrawl monitor`)
Set up recurring checks that diff snapshots and run an AI judge.
```bash
# Create monitor with schedule and natural language goal
firecrawl monitor create "https://example.com/pricing" \
  --schedule "every 30 minutes" \
  --goal "Alert if tier pricing or usage limits change" \
  --notify-email "team@example.com"
```

---

## 8. Research Index (`firecrawl research`)
Access scientific papers and GitHub history.
```bash
# Search scientific papers by topic
firecrawl research search-papers "attention mechanisms state space models"

# Inspect paper metadata and read key passages
firecrawl research inspect-paper <paper-id>
firecrawl research read-paper <paper-id> --query "computational complexity"

# Find citing, referenced, or similar papers
firecrawl research related-papers <paper-id>

# Search GitHub issues, PRs, and READMEs
firecrawl research search-github "firecrawl agent timeout"
```
