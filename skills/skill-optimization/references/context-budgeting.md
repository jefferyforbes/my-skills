# Context Budgeting & Token Optimization Reference

This reference provides formulas, word count benchmarks, and guidelines for managing agent prompt footprints.

---

## 1. Word Count Benchmarks

| Document Type | Ideal Word Count | Warning Ceiling | Hard Failure |
| :--- | :--- | :--- | :--- |
| **Top-Level Root Router (`SKILL.md`)** | 300 – 500 words | 700 words | >1,000 words |
| **Category Router (`<cat>/SKILL.md`)** | 200 – 400 words | 500 words | >700 words |
| **Specialist Router (`<cat>/<spec>/SKILL.md`)** | 300 – 550 words | 700 words | >1,000 words |
| **Reference File (`references/<file>.md`)** | Unconstrained | None | None |

---

## 2. Quick Measurement Script

Run this command to audit word counts across any target skill directory:
```bash
python3 -c "
import os, sys
p = sys.argv[1] if len(sys.argv) > 1 else '.'
for root, _, files in os.walk(p):
    for f in files:
        if f.endswith('.md'):
            fp = os.path.join(root, f)
            with open(fp) as fh:
                wc = len(fh.read().split())
            print(f'{wc:5} words | {os.path.relpath(fp, p)}')
"
```
