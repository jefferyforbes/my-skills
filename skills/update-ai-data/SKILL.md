---
name: update-ai-data
description: Syncs saved skills, workflows, knowledge, and scripts from the local Antigravity configuration directory into the AI-Skills repository.
---

# `update-ai-data` Skill

This skill synchronizes the user's Antigravity data (skills, workflows, knowledge, and scripts) into the `AI-Skills` repository to maintain a version-controlled, centralized source of truth.

## Operating Contract

This skill operates under the root `AGENTS.md`.

Treat synchronization as a repository operation:

- establish the source and destination before changing files;
- preserve files unless the sync contract explicitly requires replacement/deletion;
- verify the resulting diff;
- do not commit or push unless explicitly requested or clearly authorised by the workflow.

## Usage

When the user asks to "update AI data" or sync their skills/knowledge, execute this skill.

## Execution Steps

1.  **Locate and Synchronize Data:**
    The skills in Antigravity are spread across various plugin, built-in, and config directories.
    
    Execute the global sync script to perform the synchronization. It uses `find` to discover all `SKILL.md` locations and synchronizes them, along with other AI data, into the destination based on their namespace.

    ```bash
    # Resolve sync script location from environment or standard config directory
    SYNC_SCRIPT="${AI_SYNC_SCRIPT:-$HOME/.gemini/config/scripts/sync_ai_data.sh}"
    if [ -x "$SYNC_SCRIPT" ]; then
        "$SYNC_SCRIPT"
    else
        echo "Error: AI data sync script not found or not executable at: $SYNC_SCRIPT"
        exit 1
    fi
    ```

2.  **Git Commit (Optional):**
    If the target repository is configured and tracked by git, optionally offer to commit the synchronized changes. Note that executing git operations outside the workspace may require `BypassSandbox: true`.
    ```bash
    # Resolve target repository path from environment or standard workspace directory
    TARGET_REPO="${AI_SKILLS_DIR:-$HOME/Documents/Files/AI-Skills}"
    if [ -d "$TARGET_REPO/.git" ]; then
        cd "$TARGET_REPO"
        git add .
        git commit -m "chore: update AI data and skills"
        git push
    else
        echo "Notice: Repository not found at $TARGET_REPO; verify AI_SKILLS_DIR configuration."
    fi
    ```

3.  **Completion:**
    Inform the user that the synchronization is complete and summarize any major changes if possible.
