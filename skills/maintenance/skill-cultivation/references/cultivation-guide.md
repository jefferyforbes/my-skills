# Skill Cultivation & Pattern Mining Guide

This reference provides detailed instructions for querying the interaction ledger, clustering session topics, evaluating candidate skill viability, and conducting external frontier research with Firecrawl.

---

## 1. Querying the Interaction Ledger

The ledger is stored at `maintenance/skill-cultivation/ledger.jsonl`. Each entry contains:
- `session_id`: Unique conversation UUID.
- `created_at`: ISO timestamp.
- `primary_request`: User request snippet.
- `tools_used`: List of distinct tool names called.
- `artifacts`: List of generated markdown/image deliverables.

### Frequency Analysis Snippet
```bash
python3 -c "
import json
from collections import Counter
with open('ledger.jsonl') as f:
    records = [json.loads(l) for l in f if l.strip()]
print(f'Total Sessions: {len(records)}')
"
```

---

## 2. External Frontier Research with Firecrawl

When internal interaction artifacts are sparse or when exploring emergent engineering patterns, cultivate new skills and improve existing architectures by leveraging **Firecrawl** (see [`firecrawl`](../../../firecrawl/SKILL.md)):

1. **Academic & Engineering Papers**: Use `firecrawl research search-papers "<topic>"` to discover peer-reviewed agent architectures, context compression methods, or eval frameworks.
2. **Open-Source Agent Frameworks**: Use `firecrawl research search-github "<query>"` to inspect issues, PRs, and implementations across frontier agent libraries.
3. **Official Documentation & Technical Specs**: Use `firecrawl search` and `firecrawl scrape` to extract clean markdown from upstream framework documentation.
4. **Change Tracking on Specifications**: Use `firecrawl monitor create` to track evolving SDKs or library documentation for breaking changes.

---

## 3. Viability Evaluation Scoring

Before proposing a candidate skill, score it against the **Toil vs. Frequency Matrix**:

| Factor | High (3 pts) | Medium (2 pts) | Low (1 pt) |
| :--- | :--- | :--- | :--- |
| **Frequency** | Occurred >10 times | Occurred 4–9 times | Occurred 2–3 times |
| **Friction / Toil** | High manual setup, fragile config | Multi-step navigation | Simple one-liner |
| **Specialization** | Distinct domain rules & invariants | Reusable procedural steps | Generic coding task |

**Threshold**: A candidate must score $\ge 6$ points to warrant promotion or adoption into the global catalog.
