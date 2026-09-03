# Agent Ecosystem Architecture

This repository uses a structured layout for agent customizations. Please adhere to the following directory structure when creating or modifying content:

- `skills/`: Contains all skill folders (how the agent performs a task). New skills must be placed inside this directory.
- `knowledge/`: Contains markdown files representing what the agent should know (e.g., development workflows, architecture decisions).
- `workflows/`: Contains markdown files outlining how multiple skills should be sequenced together.
- `scripts/`: Contains utility scripts (e.g., sync scripts).

**Constraint:** When creating, updating, or managing components in this repository, always place them in their respective directories. Do not place new skills, knowledge files, or workflows directly in the repository root.
