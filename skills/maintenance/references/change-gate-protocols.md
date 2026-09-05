# Maintenance Change Gate Protocols & Regression Standards

This reference details the formal 5-stage change gate governing modifications to the agent operating environment.

---

## 1. The Change Gate Criteria
1. **Defect Proving**: A proposed change must be captured by a failing baseline test in \`agent-testing\`.
2. **Atomic Modification**: Changes must be made in small, discrete steps following the "Fix Before You Delete" principle.
3. **Regression Validation**: 100% of links, discovery roots, and executable scripts must pass regression testing before changes are promoted to production.

---

## 2. Regression Runner Architecture
The test suite at \`maintenance/scripts/run_regression.py\` executes 4 automated tests:
- \`test_internal_links\`: Crawls all markdown files for valid target paths.
- \`test_top_level_skills\`: Verifies discoverable roots under \`skills/\`.
- \`test_reachability\`: Crawls outgoing links from discoverable roots to ensure zero orphaned documentation.
- \`test_executable_scripts\`: Compiles Python and validates bash syntax.
