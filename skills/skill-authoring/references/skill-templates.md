# Skill Authoring Templates & Schemas

This reference provides standard structural scaffolds for creating new Antigravity skills following the Core Triad: **Well-Connected**, **Thorough**, and **Precise**.

---

## 1. Root Router Template (`SKILL.md`)

Target size: **300 – 500 words**.

```markdown
---
name: <skill-name>
description: <Concise, 1-2 sentence trigger criteria describing when the agent must activate this skill.>
---

# <Skill Name> Hub & Guidance

## Purpose
<Single sentence describing what capability this provides and the problem it solves.>

---

## Trigger Conditions
Activate this skill when:
- The user requests <explicit action or keywords>.
- The task requires <domain operation>.

---

## Core Rules & Constraints
1. **<Rule 1>**: <Actionable operational rule>.
2. **<Rule 2>**: <Actionable constraint or failure prevention>.

---

## Progressive Disclosure Routing
Load detailed references on-demand using \`view_file\`:
- **[Topic Guide](./references/topic-guide.md)**: Deep technical recipes, parameters, and patterns.
- **[Troubleshooting](./references/troubleshooting.md)**: Common failure modes and edge cases.

---

## Verification Checklist
Before completing work under this skill:
- [ ] <Verification Step 1>
- [ ] <Verification Step 2>
```

---

## 2. Reference Document Template (`references/<topic>.md`)

Target size: **Unconstrained** (loaded only on demand).

```markdown
# <Topic Name> Reference & Recipes

## Overview
<Contextual summary of this subsystem or framework.>

---

## Code Recipes & Patterns
\`\`\`<language>
// Minimal, production-ready, zero-fluff implementation snippet
\`\`\`

---

## Edge Cases & Failure Modes
- **<Edge Case 1>**: How to detect and remediate.
- **<Edge Case 2>**: Parameter boundaries.
```
