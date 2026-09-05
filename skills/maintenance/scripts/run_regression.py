#!/usr/bin/env python3
"""
Harness Regression Verification Suite
Automated regression tests derived from system audit findings:
1. all_internal_links_resolve
2. top_level_discoverable_skills
3. nested_capability_is_reachable
4. referenced_scripts_are_executable
"""

import os
import sys
import re
import py_compile
import subprocess

def find_skills_root():
    curr = os.path.abspath(__file__)
    return os.path.abspath(os.path.join(os.path.dirname(curr), "..", ".."))

def test_internal_links(root):
    print("Test 1: Verifying internal markdown link resolution...")
    broken_links = []
    total_links = 0
    link_pattern = re.compile(r"(?<!`)(?:\[([^\]]+)\]\(([^)]+)\))")

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for f in filenames:
            if f.endswith(".md"):
                fp = os.path.join(dirpath, f)
                with open(fp, "r", encoding="utf-8", errors="ignore") as fh:
                    content = fh.read()
                clean_content = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
                for m in link_pattern.finditer(clean_content):
                    target = m.group(2)
                    if target.startswith("http") or target.startswith("#") or target.startswith("mailto:"):
                        continue
                    total_links += 1
                    clean = target.split("#")[0]
                    if not clean:
                        continue
                    if clean.startswith("~/"):
                        resolved = os.path.expanduser(clean)
                    elif clean.startswith("/"):
                        resolved = clean
                    else:
                        resolved = os.path.normpath(os.path.join(dirpath, clean))
                    if not os.path.exists(resolved):
                        broken_links.append((os.path.relpath(fp, root), m.group(1), target, resolved))

    if broken_links:
        print(f"  [FAIL] {len(broken_links)} / {total_links} links broken:")
        for src, txt, tgt, res in broken_links:
            print(f"    - In {src}: [{txt}]({tgt}) -> {res} (NOT FOUND)")
        return False
    else:
        print(f"  [PASS] All {total_links} internal markdown links resolve cleanly.")
        return True

def test_top_level_skills(root):
    print("\nTest 2: Verifying top-level discoverable skills...")
    top_skills = []
    for d in os.listdir(root):
        dp = os.path.join(root, d)
        if os.path.isdir(dp) and not d.startswith(".") and os.path.exists(os.path.join(dp, "SKILL.md")):
            top_skills.append(d)

    print(f"  Found {len(top_skills)} discoverable root skills:")
    for s in sorted(top_skills):
        print(f"    ✓ {s}")
    return top_skills

def test_reachability(root, top_skills):
    print("\nTest 3: Verifying reachability from discoverable roots...")
    link_pattern = re.compile(r"(?<!`)(?:\[([^\]]+)\]\(([^)]+)\))")
    reachable = set()
    to_visit = [os.path.join(root, s, "SKILL.md") for s in top_skills]
    visited = set()

    while to_visit:
        curr = to_visit.pop(0)
        if curr in visited or not os.path.exists(curr):
            continue
        visited.add(curr)
        reachable.add(curr)
        with open(curr, "r", encoding="utf-8", errors="ignore") as fh:
            text = fh.read()
        clean_text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        for m in link_pattern.finditer(clean_text):
            target = m.group(2)
            if target.startswith("http") or target.startswith("#") or target.startswith("mailto:"):
                continue
            clean = target.split("#")[0]
            if not clean:
                continue
            if clean.startswith("~/"):
                resolved = os.path.expanduser(clean)
            elif clean.startswith("/"):
                resolved = clean
            else:
                resolved = os.path.normpath(os.path.join(os.path.dirname(curr), clean))
            if os.path.exists(resolved) and resolved.endswith((".md", ".txt")) and resolved not in visited:
                to_visit.append(resolved)

    all_md = set()
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for f in filenames:
            if f.endswith(".md"):
                all_md.add(os.path.normpath(os.path.join(dirpath, f)))

    unreachable = all_md - reachable
    if unreachable:
        print(f"  [FAIL] {len(unreachable)} unreachable documents found:")
        for u in sorted(unreachable):
            print(f"    - {os.path.relpath(u, root)}")
        return False
    else:
        print(f"  [PASS] 100% of markdown documents ({len(all_md)} total) are reachable from root hubs.")
        return True

def test_executable_scripts(root):
    print("\nTest 4: Verifying referenced scripts and syntax integrity...")
    errors = []
    script_count = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for f in filenames:
            p = os.path.join(dirpath, f)
            if f.endswith(".py"):
                script_count += 1
                try:
                    py_compile.compile(p, doraise=True)
                except Exception as e:
                    errors.append((os.path.relpath(p, root), str(e)))
            elif f.endswith(".sh"):
                script_count += 1
                r = subprocess.run(["bash", "-n", p], capture_output=True, text=True)
                if r.returncode != 0:
                    errors.append((os.path.relpath(p, root), r.stderr))

    if errors:
        print(f"  [FAIL] Script syntax errors in {len(errors)} files:")
        for f, err in errors:
            print(f"    - {f}: {err}")
        return False
    else:
        print(f"  [PASS] All {script_count} Python and shell scripts passed syntax compilation.")
        return True

def main():
    root = find_skills_root()
    print(f"=== Running Maintenance Regression Suite on: {root} ===\n")
    p1 = test_internal_links(root)
    top_skills = test_top_level_skills(root)
    p2 = len(top_skills) > 0
    p3 = test_reachability(root, top_skills)
    p4 = test_executable_scripts(root)

    print("\n=======================================================")
    if p1 and p2 and p3 and p4:
        print("  ALL REGRESSION TESTS PASSED (100% HEALTH)")
        print("=======================================================")
        sys.exit(0)
    else:
        print("  REGRESSION FAILURES DETECTED")
        print("=======================================================")
        sys.exit(1)

if __name__ == "__main__":
    main()
