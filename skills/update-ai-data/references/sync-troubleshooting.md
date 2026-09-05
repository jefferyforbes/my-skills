# AI Data Synchronization: Troubleshooting & Configuration Reference

This reference covers environment variables, directory mapping, and merge conflict resolution when synchronizing AI skills.

---

## 1. Environment Variables
- \`AI_SKILLS_DIR\`: Path to the centralized \`AI-Skills\` git repository (default: \`$HOME/Documents/Files/AI-Skills\`).
- \`AI_SYNC_SCRIPT\`: Path to the shell synchronization script (default: \`$HOME/.gemini/config/scripts/sync_ai_data.sh\`).

---

## 2. Resolving Git Sync Conflicts
If the target repository has divergent commits:
1. Run \`git status\` in \`$AI_SKILLS_DIR\`.
2. Stash local uncommitted changes: \`git stash\`.
3. Pull with rebase: \`git pull --rebase origin main\`.
4. Pop stash: \`git stash pop\` and commit the synchronized skills.
