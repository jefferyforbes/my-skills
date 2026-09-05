# Shared Agent Principles & Knowledge

## Overview

The `shared/` directory houses cross-domain principles, architectural rules, and decision guidance shared across multiple skills.

Per the **Host Harness Discovery Contract**, `shared/` is retained as an **unmounted internal progressive-disclosure repository** rather than an independently discoverable top-level skill.

---

## Directory Structure

```text
shared/
├── README.md                 # This documentation
└── principles/
    ├── SKILL.md              # Internal progressive-disclosure router
    ├── skill-system.md       # Architecture & discovery contract
    ├── skill-authoring/
    │   └── SKILL.md          # Skill authoring guidelines
    └── learning/
        └── SKILL.md          # Decision explanation & teaching workflow
```

---

## Routing

Domain skills (such as `engineering`, `android`, or `maintenance`) access shared principles via the internal router:
- **[Shared Principles Router](./principles/SKILL.md)**
