#!/usr/bin/env python3
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BRANCH = "project/patch-004-post-merge-state-lock"
BASE = "1ce5d559dce0e7d1f4fcd0c69f9fe1744cee10b8"

checks = {
    "GITHUB_WORKFLOW.md": [
        "gh pr ready PR_NUMBER",
        "gh pr merge PR_NUMBER --merge --delete-branch",
        "git fetch --prune",
    ],
    "docs/handoff/CURRENT_STATE.md": [
        "COMPLETE / MERGED",
        BASE,
        "Patch 005 - visible demo-mode runtime baseline",
    ],
    "docs/history/PATCH_003.md": ["COMPLETE / MERGED", "PR #2"],
    "docs/history/PATCH_004.md": ["# Patch 004", "DD-009"],
}

def run(*args):
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True)

def main():
    failures = []
    branch = run("git", "branch", "--show-current").stdout.strip()
    if branch == BRANCH:
        print(f"PASS: branch={branch}")
    else:
        failures.append(f"wrong branch: {branch}")

    for rel, markers in checks.items():
        path = ROOT / rel
        if not path.is_file():
            failures.append(f"missing {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                failures.append(f"{rel} missing {marker}")
        print(f"PASS: {rel}")

    changed = set()
    for cmd in (
        ("git", "diff", "--name-only", f"{BASE}...HEAD"),
        ("git", "diff", "--name-only"),
        ("git", "diff", "--cached", "--name-only"),
    ):
        changed.update(x for x in run(*cmd).stdout.splitlines() if x)
    for line in run("git", "status", "--porcelain", "--untracked-files=all").stdout.splitlines():
        if len(line) >= 4:
            changed.add(line[3:])

    runtime = sorted(x for x in changed if x.startswith(
        ("openhantek/", "libOpenHantek2xxx/", "firmware/")
    ))
    outside = sorted(x for x in changed if x != "GITHUB_WORKFLOW.md" and not x.startswith(
        ("docs/", "scripts/")
    ))
    if runtime:
        failures.append(f"runtime changes: {runtime}")
    else:
        print("PASS: no runtime or firmware changes")
    if outside:
        failures.append(f"outside boundary: {outside}")
    else:
        print("PASS: docs/scripts boundary")

    for cmd in (("git", "diff", "--check"), ("git", "diff", "--cached", "--check")):
        if run(*cmd).returncode:
            failures.append("whitespace check failed")

    print("\n=== VALIDATION SUMMARY ===")
    if failures:
        for item in failures:
            print(f"FAIL: {item}")
        print("FAIL: Patch 004 validator failed")
        return 1
    print("PASS: Patch 004 post-merge state lock validator complete")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
