# Skill Cultivation & Pattern Mining Guide

This reference provides detailed instructions for querying the interaction ledger, clustering session topics, and evaluating candidate skill viability.

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

## 2. Viability Evaluation Scoring

Before proposing a candidate skill, score it against the **Toil vs. Frequency Matrix**:

| Factor | High (3 pts) | Medium (2 pts) | Low (1 pt) |
| :--- | :--- | :--- | :--- |
| **Frequency** | Occurred >10 times | Occurred 4–9 times | Occurred 2–3 times |
| **Friction / Toil** | High manual setup, fragile config | Multi-step navigation | Simple one-liner |
| **Specialization** | Distinct domain rules & invariants | Reusable procedural steps | Generic coding task |

**Threshold**: A candidate must score $\ge 6$ points to warrant promotion or adoption into the global catalog.
