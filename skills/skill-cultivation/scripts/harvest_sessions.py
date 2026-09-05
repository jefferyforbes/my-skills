#!/usr/bin/env python3
"""
harvest_sessions.py

Scans recent Antigravity session brain directories (~/.gemini/antigravity/brain/),
extracts interaction summaries, tools used, artifacts produced, and user intents,
and writes them into a lightweight interaction ledger (ledger.jsonl).
"""

import os
import sys
import json
import glob
from datetime import datetime

DEFAULT_BRAIN_DIR = os.path.expanduser("~/.gemini/antigravity/brain")
DEFAULT_LEDGER_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "ledger.jsonl")

def harvest_session(session_dir):
    session_id = os.path.basename(session_dir)
    transcript_file = os.path.join(session_dir, ".system_generated", "logs", "transcript.jsonl")
    
    if not os.path.exists(transcript_file):
        return None

    user_requests = []
    tools_used = set()
    artifacts = []
    created_at = None

    # Identify artifacts
    for entry in os.listdir(session_dir):
        if entry.endswith(".md") and not entry.startswith("."):
            artifacts.append(entry)

    # Inspect transcript
    try:
        with open(transcript_file, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    data = json.loads(line)
                    if not created_at and "created_at" in data:
                        created_at = data["created_at"]
                    
                    if data.get("type") == "USER_INPUT":
                        content = data.get("content", "")
                        # Strip XML tags if present
                        if "<USER_REQUEST>" in content:
                            req = content.split("<USER_REQUEST>")[1].split("</USER_REQUEST>")[0].strip()
                        else:
                            req = content.strip()
                        if req and req not in user_requests:
                            user_requests.append(req[:300]) # Cap snippet length
                    
                    if "tool_calls" in data:
                        for tc in data["tool_calls"]:
                            name = tc.get("name")
                            if name:
                                tools_used.add(name)
                except Exception:
                    continue
    except Exception as e:
        return None

    if not user_requests:
        return None

    return {
        "session_id": session_id,
        "created_at": created_at or datetime.utcnow().isoformat() + "Z",
        "primary_request": user_requests[0] if user_requests else "",
        "request_count": len(user_requests),
        "tools_used": sorted(list(tools_used)),
        "artifacts": artifacts
    }

def main():
    brain_dir = os.environ.get("ANTIGRAVITY_BRAIN_DIR", DEFAULT_BRAIN_DIR)
    ledger_path = os.environ.get("CULTIVATION_LEDGER_PATH", DEFAULT_LEDGER_PATH)

    if not os.path.exists(brain_dir):
        print(f"[WARN] Brain directory not found: {brain_dir}")
        sys.exit(0)

    # Load existing session IDs from ledger to avoid duplicate entries
    recorded_sessions = set()
    if os.path.exists(ledger_path):
        try:
            with open(ledger_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        try:
                            rec = json.loads(line)
                            if "session_id" in rec:
                                recorded_sessions.add(rec["session_id"])
                        except Exception:
                            pass
        except Exception:
            pass

    print(f"Scanning brain sessions in: {brain_dir}...")
    new_entries = []
    
    session_dirs = [os.path.join(brain_dir, d) for d in os.listdir(brain_dir) if os.path.isdir(os.path.join(brain_dir, d)) and not d.startswith(".")]
    # Sort by mtime descending
    session_dirs.sort(key=lambda d: os.path.getmtime(d), reverse=True)

    for s_dir in session_dirs:
        s_id = os.path.basename(s_dir)
        if s_id in recorded_sessions:
            continue
        record = harvest_session(s_dir)
        if record:
            new_entries.append(record)

    if new_entries:
        with open(ledger_path, "a", encoding="utf-8") as f:
            for entry in new_entries:
                f.write(json.dumps(entry) + "\n")
        print(f"[SUCCESS] Recorded {len(new_entries)} new session(s) into lightweight ledger: {ledger_path}")
    else:
        print(f"[INFO] Ledger is up to date ({len(recorded_sessions)} existing records).")

if __name__ == "__main__":
    main()
