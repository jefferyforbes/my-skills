#!/bin/bash
DEST_DIR="/Users/jefferyforbes/Documents/Files/AI-Skills"
mkdir -p "$DEST_DIR/skills" "$DEST_DIR/workflows" "$DEST_DIR/knowledge" "$DEST_DIR/scripts"

echo "Synchronizing skills..."
find /Users/jefferyforbes/.gemini -name "SKILL.md" 2>/dev/null | while read -r skill_file; do
    skill_dir=$(dirname "$skill_file")
    skill_name=$(basename "$skill_dir")
    
    if [ -d "$DEST_DIR/skills/$skill_name" ]; then
        echo "Updating existing namespace: $skill_name"
    else
        echo "Adding new namespace: $skill_name"
    fi
    rsync -a "$skill_dir/" "$DEST_DIR/skills/$skill_name/"
done

echo "Synchronizing workflows..."
rsync -a ~/.gemini/config/workflows/ "$DEST_DIR/workflows/" 2>/dev/null || true

echo "Synchronizing knowledge..."
rsync -a ~/.gemini/config/knowledge/ "$DEST_DIR/knowledge/" 2>/dev/null || true

echo "Synchronizing scripts..."
rsync -a ~/.gemini/config/scripts/ "$DEST_DIR/scripts/" 2>/dev/null || true

echo "AI data synchronization complete."
