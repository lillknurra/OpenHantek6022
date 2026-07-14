#!/usr/bin/env python3
"""Final structural validator for Patch 003."""

from __future__ import annotations

from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BRANCH = "project/patch-003-project-standardization"
BASE = "501ffe7d352abe4eb01ce0afbd498f0cf4fb03ac"

REQUIRED = [
    "AGENTS.md",
    "PROJECT_INSTRUCTIONS.md",
    "GITHUB_WORKFLOW.md",
    "docs/handoff/MASTER_INDEX.md",
    "docs/handoff/CURRENT_STATE.md",
    "docs/handoff/AI_MEMORY.md",
    "docs/handoff/HANDOFF.md",
    "docs/architecture/SYSTEM_ARCHITECTURE.md",
    "docs/architecture/DESIGN_DECISIONS.md",
    "docs/history/PATCH_HISTORY.md",
    "docs/history/PATCH_003.md",
    "docs/development/BRANCHING_STRATEGY.md",
    "docs/development/RELEASE_PROCESS.md",
    "docs/development/DEVELOPMENT_WORKFLOW.md",
    "docs/development/VALIDATION_WORKFLOW.md",
    "docs/build/MACOS_BUILD_BASELINE.md",
    "docs/HARDWARE_BASELINE.md",
    "docs/USB_ARCHITECTURE.md",
    "docs/MSO_HYPOTHESES.md",
    "docs/TEST_PLAN.md",
]

LEGACY = {
    "docs/MASTER_INDEX.md": "docs/handoff/MASTER_INDEX.md",
    "docs/CURRENT_STATE.md": "docs/handoff/CURRENT_STATE.md",
    "docs/AI_MEMORY.md": "docs/handoff/AI_MEMORY.md",
}

ALLOWED_PREFIXES = ("docs/", "scripts/")
ALLOWED_EXACT = {"GITHUB_WORKFLOW.md"}
RUNTIME_PREFIXES = ("openhantek/", "libOpenHantek2xxx/", "firmware/")
RUNTIME_EXACT = {"CMakeLists.txt"}


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(args), cwd=ROOT, text=True, capture_output=True, check=False
    )


def all_changed() -> set[str]:
    changed: set[str] = set()
    for args in (
        ("git", "diff", "--name-only", f"{BASE}...HEAD"),
        ("git", "diff", "--name-only"),
        ("git", "diff", "--cached", "--name-only"),
    ):
        result = run(*args)
        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip() or "git diff failed")
        changed.update(x for x in result.stdout.splitlines() if x)

    status = run("git", "status", "--porcelain", "--untracked-files=all")
    for line in status.stdout.splitlines():
        if len(line) >= 4:
            path = line[3:]
            if " -> " in path:
                path = path.split(" -> ", 1)[1]
            changed.add(path)
    return changed


def main() -> int:
    failures: list[str] = []

    print("\n=== BRANCH ===")
    branch = run("git", "branch", "--show-current").stdout.strip()
    if branch == BRANCH:
        print(f"PASS: branch={branch}")
    else:
        failures.append(f"expected branch {BRANCH}, current={branch}")
        print(f"FAIL: {failures[-1]}")

    print("\n=== REQUIRED STRUCTURE ===")
    for relative in REQUIRED:
        if (ROOT / relative).is_file():
            print(f"PASS: {relative}")
        else:
            failures.append(f"missing {relative}")
            print(f"FAIL: missing {relative}")

    print("\n=== LEGACY POINTERS ===")
    for relative, target in LEGACY.items():
        path = ROOT / relative
        text = path.read_text(encoding="utf-8") if path.is_file() else ""
        if "compatibility pointer" in text and target in text:
            print(f"PASS: {relative} -> {target}")
        else:
            failures.append(f"{relative} is not a valid legacy pointer")
            print(f"FAIL: {failures[-1]}")

    print("\n=== MASTER INDEX REFERENCES ===")
    index = ROOT / "docs/handoff/MASTER_INDEX.md"
    text = index.read_text(encoding="utf-8")
    refs = sorted(set(re.findall(r"`([^`]+\.(?:md|py|sh))`", text)))
    missing = [
        ref for ref in refs
        if not (index.parent / ref).resolve().exists()
    ]
    if missing:
        failures.append(f"missing MASTER_INDEX references: {missing}")
        print(f"FAIL: {failures[-1]}")
    else:
        print(f"PASS: canonical references resolve count={len(refs)}")

    print("\n=== DESIGN DECISIONS ===")
    decisions = (ROOT / "docs/architecture/DESIGN_DECISIONS.md").read_text(
        encoding="utf-8"
    )
    missing_dd = [
        f"DD-{n:03d}" for n in range(1, 10)
        if f"DD-{n:03d}" not in decisions
    ]
    if missing_dd:
        failures.append(f"missing design decisions: {missing_dd}")
        print(f"FAIL: {failures[-1]}")
    else:
        print("PASS: DD-001 through DD-009")

    print("\n=== PATCH 003 CHANGE BOUNDARY ===")
    try:
        changed = all_changed()
        runtime = sorted(
            p for p in changed
            if p in RUNTIME_EXACT or p.startswith(RUNTIME_PREFIXES)
        )
        outside = sorted(
            p for p in changed
            if p not in ALLOWED_EXACT and not p.startswith(ALLOWED_PREFIXES)
        )
        if runtime:
            failures.append(f"runtime or firmware files changed: {runtime}")
            print(f"FAIL: {failures[-1]}")
        else:
            print("PASS: no runtime or firmware files changed")
        if outside:
            failures.append(f"changes outside docs/scripts boundary: {outside}")
            print(f"FAIL: {failures[-1]}")
        else:
            print("PASS: all Patch 003 changes are documentation or scripts")
    except RuntimeError as exc:
        failures.append(str(exc))
        print(f"FAIL: {exc}")

    print("\n=== WHITESPACE ===")
    worktree = run("git", "diff", "--check")
    staged = run("git", "diff", "--cached", "--check")
    if worktree.returncode == 0 and staged.returncode == 0:
        print("PASS: worktree and staged whitespace checks")
    else:
        failures.append("whitespace check failed")
        print("FAIL: whitespace check failed")
        print(worktree.stdout + worktree.stderr + staged.stdout + staged.stderr)

    print("\n=== VALIDATION SUMMARY ===")
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print("FAIL: Patch 003 final structural validator failed")
        return 1

    print("PASS: Patch 003 final structural validator complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
