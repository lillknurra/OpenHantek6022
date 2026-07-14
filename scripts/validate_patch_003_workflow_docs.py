#!/usr/bin/env python3
"""Validate Patch 003 Commit D workflow documentation."""

from __future__ import annotations

from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BRANCH = "project/patch-003-project-standardization"
BASE = "project/patch-002-macos-build-baseline"

FILES = {
    "docs/development/VALIDATION_WORKFLOW.md": [
        "# Validation Workflow",
        "## Evidence classes",
        "## Result vocabulary",
        "## Documentation-only patch minimum",
        "A validator passing proves only the checks implemented by that validator.",
    ],
    "docs/development/DEVELOPMENT_WORKFLOW.md": [
        "# Development Workflow",
        "IMPLEMENT -> VALIDATE -> PUBLISH -> LOCK -> COMPLETE",
        "## PUBLISH",
        "## LOCK",
        "## COMPLETE",
        "docs/development/VALIDATION_WORKFLOW.md",
    ],
    "GITHUB_WORKFLOW.md": [
        "# GitHub Workflow",
        "Define the commit message before any GitHub write operation.",
        "A stacked patch must target its actual accepted base branch",
        "project/patch-002-macos-build-baseline",
        "## GitHub write safety",
    ],
}

RUNTIME_PREFIXES = ("openhantek/", "libOpenHantek2xxx/", "firmware/")
RUNTIME_EXACT = {"CMakeLists.txt"}


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(args), cwd=ROOT, text=True, capture_output=True, check=False
    )


def changed_paths() -> set[str]:
    result: set[str] = set()

    committed = run("git", "diff", "--name-only", f"{BASE}...HEAD")
    if committed.returncode != 0:
        raise RuntimeError(committed.stderr.strip() or "base comparison failed")
    result.update(x for x in committed.stdout.splitlines() if x)

    worktree = run("git", "diff", "--name-only")
    result.update(x for x in worktree.stdout.splitlines() if x)

    staged = run("git", "diff", "--cached", "--name-only")
    result.update(x for x in staged.stdout.splitlines() if x)

    status = run("git", "status", "--porcelain", "--untracked-files=all")
    for line in status.stdout.splitlines():
        if len(line) >= 4:
            path = line[3:]
            if " -> " in path:
                path = path.split(" -> ", 1)[1]
            result.add(path)

    return result


def main() -> int:
    failures: list[str] = []

    print("\n=== BRANCH ===")
    branch = run("git", "branch", "--show-current").stdout.strip()
    if branch == BRANCH:
        print(f"PASS: branch={branch}")
    else:
        failures.append(f"expected branch {BRANCH}, current={branch}")
        print(f"FAIL: {failures[-1]}")

    print("\n=== FILES AND MARKERS ===")
    for rel, markers in FILES.items():
        path = ROOT / rel
        if not path.is_file():
            failures.append(f"missing {rel}")
            print(f"FAIL: missing {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        print(f"PASS: {rel} exists")
        for marker in markers:
            if marker not in text:
                failures.append(f"{rel} missing marker: {marker}")
                print(f"FAIL: {failures[-1]}")

    print("\n=== DESIGN DECISIONS ===")
    expected = {"DD-002", "DD-003", "DD-007", "DD-008", "DD-009"}
    handoff = (ROOT / "docs/handoff/HANDOFF.md").read_text(encoding="utf-8")
    found = {dd for dd in expected if dd in handoff}
    if found == expected:
        print("PASS: workflow work remains consistent with Commit C decision set")
    else:
        failures.append(f"missing design decisions in handoff: {sorted(expected-found)}")
        print(f"FAIL: {failures[-1]}")

    print("\n=== RUNTIME FILE CHECK ===")
    try:
        changed = changed_paths()
        runtime = sorted(
            path for path in changed
            if path in RUNTIME_EXACT or path.startswith(RUNTIME_PREFIXES)
        )
        if runtime:
            failures.append(f"runtime or firmware paths changed: {runtime}")
            print(f"FAIL: {failures[-1]}")
        else:
            print("PASS: no OpenHantek runtime or firmware files changed")
    except RuntimeError as exc:
        failures.append(str(exc))
        print(f"FAIL: {exc}")

    print("\n=== WHITESPACE CHECK ===")
    diff = run("git", "diff", "--check")
    cached = run("git", "diff", "--cached", "--check")
    if diff.returncode == 0 and cached.returncode == 0:
        print("PASS: worktree and staged whitespace checks")
    else:
        failures.append("whitespace check failed")
        print("FAIL: whitespace check failed")
        print(diff.stdout + diff.stderr + cached.stdout + cached.stderr)

    print("\n=== VALIDATION SUMMARY ===")
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print("FAIL: Patch 003 Commit D workflow validator failed")
        return 1

    print("PASS: Patch 003 Commit D workflow validator complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
