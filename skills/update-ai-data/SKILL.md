---
name: update-ai-data
description: Syncs saved skills, workflows, knowledge, and scripts from the local Antigravity configuration directory into the AI-Skills repository.
---

# `update-ai-data` Skill

This skill synchronizes the user's Antigravity data (skills, workflows, knowledge, and scripts) into the `AI-Skills` repository to maintain a version-controlled, centralized source of truth.

## Usage

When the user asks to "update AI data" or sync their skills/knowledge, you should execute this skill.

## Execution Steps

1.  **Locate the source and destination:**
    *   Source (Antigravity Config): `~/.gemini/config/` (or `~/.gemini/antigravity/builtin/skills/` etc. based on the current environment).
    *   Destination: `/Users/jefferyforbes/Documents/Files/AI-Skills/`

2.  **Synchronize Data:**
    Use `rsync` or `cp` to copy the directories. Prefer `rsync -av` for efficient synchronization that doesn't overwrite newer files blindly if bidirectional sync is needed, but for a simple backup, `cp -R` or `rsync -av --delete` (if meant to exactly mirror) works.
    
    ```bash
    # Example sync commands (run these in the user's terminal)
    rsync -av ~/.gemini/config/skills/ /Users/jefferyforbes/Documents/Files/AI-Skills/skills/
    rsync -av ~/.gemini/config/workflows/ /Users/jefferyforbes/Documents/Files/AI-Skills/workflows/
    rsync -av ~/.gemini/config/knowledge/ /Users/jefferyforbes/Documents/Files/AI-Skills/knowledge/
    rsync -av ~/.gemini/config/scripts/ /Users/jefferyforbes/Documents/Files/AI-Skills/scripts/
    ```
    *(Note: adjust the source paths if the agent's configuration is stored elsewhere in the `~/.gemini/` directory).*

3.  **Git Commit (Optional):**
    If the `AI-Skills` directory is a git repository (has a `.git` folder), you may optionally offer to commit the changes for the user.
    ```bash
    cd /Users/jefferyforbes/Documents/Files/AI-Skills/
    git add .
    git commit -m "chore: update AI data and skills"
    git push
    ```

4.  **Completion:**
    Inform the user that the synchronization is complete and summarize any major changes if possible.
