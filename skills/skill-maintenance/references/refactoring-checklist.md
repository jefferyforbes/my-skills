# Skill Maintenance & Structural Refactoring Checklist

This reference provides concrete execution recipes for safely refactoring skills without breaking harness reachability or link resolution.

---

## 1. Relative Link Depth Formulas

When moving a document between directory depths, adjust relative links accordingly:

```text
From root level (depth 1: skills/<name>/SKILL.md):
  To peer skill:               ../<peer-name>/SKILL.md
  To own reference:            ./references/<ref>.md
  To nested specialist:        ./<subcat>/<specialist>/SKILL.md

From depth 2 (skills/<name>/<subcat>/SKILL.md):
  To parent root:              ../SKILL.md
  To peer subcat:              ../<peer-subcat>/SKILL.md
  To own reference:            ./references/<ref>.md

From depth 3 (skills/<name>/<subcat>/<specialist>/SKILL.md):
  To subcat router:            ../SKILL.md
  To grandparent root:         ../../SKILL.md
  To root peer skill:          ../../../<peer-skill>/SKILL.md
```

---

## 2. Pre-Flight & Post-Flight Refactor Checklist

- [ ] Run baseline: `python3 ~/.gemini/config/skills/maintenance/scripts/run_regression.py`.
- [ ] Ensure any newly created markdown document is reachable from a discoverable root.
- [ ] Ensure any moved script preserves executable permissions (`chmod +x`).
- [ ] Run regression suite and verify zero broken links.
