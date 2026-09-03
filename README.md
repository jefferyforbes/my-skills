# AI-Skills

This repository serves as a centralized source of truth for AI agent capabilities, knowledge, workflows, and scripts. It is designed to be easily ingestible by various AI harnesses, such as Antigravity, Claude Code, Cursor, and GitHub Copilot/Codex.

## Structure

- `skills/`: Contains skill folders detailing how agents perform specific tasks.
- `knowledge/`: Contains markdown files representing what the agent should know (e.g., development workflows, architecture decisions).
- `workflows/`: Contains markdown files outlining how multiple skills should be sequenced together.
- `scripts/`: Contains utility scripts used by agents or for maintenance.

## Ingesting into AI Harnesses

### Antigravity
Antigravity automatically discovers skills and knowledge if they are placed in its configuration directory.

To ingest this repository into Antigravity, you can copy the contents of these directories directly into your Antigravity configuration directory (typically `~/.gemini/config/`).

Alternatively, for a more permanent setup, symlink the directories:
```bash
ln -s ~/Documents/Files/AI-Skills/skills ~/.gemini/config/skills
ln -s ~/Documents/Files/AI-Skills/workflows ~/.gemini/config/workflows
ln -s ~/Documents/Files/AI-Skills/knowledge ~/.gemini/config/knowledge
ln -s ~/Documents/Files/AI-Skills/scripts ~/.gemini/config/scripts
```
You can also use the `update-ai-data` skill to automate synchronization from the agent's memory to this repository.

### Claude Code
Claude Code doesn't use this exact directory structure natively, but you can feed this context to it.
- **Project Level:** Create a `.claude` configuration file or a `CLAUDE.md` in your project root that points Claude to this repository for guidelines.
- **Global Level:** You can copy relevant `knowledge/` markdown files into Claude's global instructions.

### Cursor & Codex
Cursor (and similar Copilot/Codex environments) can ingest this data through workspace rules.
1. Add this folder to your Cursor workspace.
2. Copy or symlink specific `knowledge/` files into your project's `.cursorrules` or `.cursor/rules/` directory so the agent automatically loads them as context.
3. For custom scripts, use Cursor's terminal features to run them from the `scripts/` directory.

### Other Agents
Most modern coding agents support reading markdown files for system prompts or custom instructions. You can point them to the `knowledge/` and `skills/` folders to align their behavior with your established workflows.
