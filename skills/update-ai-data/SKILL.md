---
name: update-ai-data
description: Syncs saved skills, workflows, knowledge, and scripts from the local Antigravity configuration directory into the AI-Skills repository.
---

# `update-ai-data` Skill

This skill synchronizes the user's Antigravity data (skills, workflows, knowledge, and scripts) into the `AI-Skills` repository to maintain a version-controlled, centralized source of truth.

## Usage

When the user asks to "update AI data" or sync their skills/knowledge, you should execute this skill.

## Execution Steps

1.  **Locate and Synchronize Data:**
    The skills in Antigravity are spread across various plugin, built-in, and config directories. We need to find all skill namespaces and copy them to `/Users/jefferyforbes/Documents/Files/AI-Skills/skills/`.
    
    Execute the following script to perform the synchronization. It uses `find` to discover all `SKILL.md` locations and synchronizes them into the destination based on their namespace.

    ```bash
    DEST_DIR="/Users/jefferyforbes/Documents/Files/AI-Skills"
    mkdir -p "$DEST_DIR/skills" "$DEST_DIR/workflows" "$DEST_DIR/knowledge" "$DEST_DIR/scripts"

    # Synchronize Skills
    find /Users/jefferyforbes/.gemini -name "SKILL.md" 2>/dev/null | while read -r skill_file; do
        skill_dir=$(dirname "$skill_file")
        skill_name=$(basename "$skill_dir")
        rsync -a "$skill_dir/" "$DEST_DIR/skills/$skill_name/"
    done
    
    # Synchronize other data (workflows, knowledge, scripts) if they exist
    rsync -a ~/.gemini/config/workflows/ "$DEST_DIR/workflows/" 2>/dev/null || true
    rsync -a ~/.gemini/config/knowledge/ "$DEST_DIR/knowledge/" 2>/dev/null || true
    rsync -a ~/.gemini/config/scripts/ "$DEST_DIR/scripts/" 2>/dev/null || true
    ```

2.  **Git Commit (Optional):**
    If the `AI-Skills` directory is a git repository (has a `.git` folder), you may optionally offer to commit the changes for the user. Note that executing git operations outside the workspace might require `BypassSandbox: true`.
    ```bash
    cd /Users/jefferyforbes/Documents/Files/AI-Skills/
    git add .
    git commit -m "chore: update AI data and skills"
    git push
    ```

3.  **Completion:**
    Inform the user that the synchronization is complete and summarize any major changes if possible.
