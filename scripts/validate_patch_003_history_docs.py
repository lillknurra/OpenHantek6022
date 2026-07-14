#!/usr/bin/env python3
"""Validate Patch 003 Commit B history documents."""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_BRANCH = "project/patch-003-project-standardization"
BASE = "project/patch-002-macos-build-baseline"

REQUIRED_FILES = [
    Path("docs/history/PATCH_HISTORY.md"),
    Path("docs/history/PATCH_003.md"),
]

REQUIRED_MARKERS = {
    Path("docs/history/PATCH_HISTORY.md"): [
        "# Patch History",
        "## Patch 001 - Project governance baseline",
        "## Patch 002 - Apple Silicon macOS build baseline",
        "## Patch 003 - Project standardization",
        "501ffe7d352abe4eb01ce0afbd498f0cf4fb03ac",
        "9a90ec76ec9ce1ecdd7cd0791f2a6204e2dc325f",
    ],
    Path("docs/history/PATCH_003.md"): [
        "# Patch 003 - Project Standardization",
        "## Design decisions",
        "DD-002",
        "DD-003",
        "DD-007",
        "DD-008",
        "DD-009",
        "## Rollback",
        "## Completion criteria",
        "Patch 003: add patch history",
    ],
}

RUNTIME_PREFIXES = (
    "openhantek/",
    "libOpenHantek2xxx/",
    "firmware/",
)
RUNTIME_EXACT = {"CMakeLists.txt"}


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def main() -> int:
    failures: list[str] = []

    print("\n=== PATCH 003 COMMIT B BRANCH ===")
    branch = run(["git", "branch", "--show-current"]).stdout.strip()
    if branch == EXPECTED_BRANCH:
        print(f"PASS: branch={branch}")
    else:
        failures.append(f"expected branch {EXPECTED_BRANCH}, current={branch}")
        print(f"FAIL: {failures[-1]}")

    print("\n=== DOCUMENT PRESENCE ===")
    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if path.is_file():
            print(f"PASS: {rel} exists")
        else:
            failures.append(f"missing {rel}")
            print(f"FAIL: missing {rel}")

    print("\n=== REQUIRED MARKERS ===")
    for rel, markers in REQUIRED_MARKERS.items():
        path = ROOT / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker in text:
                print(f"PASS: {rel} contains {marker}")
            else:
                failures.append(f"{rel} missing marker: {marker}")
                print(f"FAIL: {failures[-1]}")

    print("\n=== DESIGN DECISION REFERENCES ===")
    patch_text = (ROOT / "docs/history/PATCH_003.md").read_text(encoding="utf-8")
    ids = sorted(set(re.findall(r"DD-[0-9]{3}", patch_text)))
    expected_ids = [f"DD-{number:03d}" for number in range(1, 10)]
    if ids == expected_ids:
        print("PASS: PATCH_003 references DD-001 through DD-009")
    else:
        failures.append(f"design decision set differs: {ids}")
        print(f"FAIL: {failures[-1]}")

    print("\n=== RUNTIME FILE CHECK ===")
    comparison = run(["git", "diff", "--name-only", f"{BASE}...HEAD"])
    if comparison.returncode != 0:
        failures.append("unable to compare Patch 003 against Patch 002")
        print(f"FAIL: {failures[-1]}")
        if comparison.stderr:
            print(comparison.stderr.strip())
    else:
        changed = [line for line in comparison.stdout.splitlines() if line]
        runtime = [
            path for path in changed
            if path in RUNTIME_EXACT or path.startswith(RUNTIME_PREFIXES)
        ]
        if runtime:
            failures.append(f"runtime or firmware files changed: {runtime}")
            print(f"FAIL: {failures[-1]}")
        else:
            print("PASS: no OpenHantek runtime or firmware files changed")

    print("\n=== WHITESPACE CHECK ===")
    whitespace = run(["git", "diff", "--check"])
    if whitespace.returncode == 0:
        print("PASS: git diff --check")
    else:
        failures.append("git diff --check failed")
        print("FAIL: git diff --check")
        print(whitespace.stdout)
        print(whitespace.stderr)

    print("\n=== VALIDATION SUMMARY ===")
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print("FAIL: Patch 003 Commit B history validator failed")
        return 1

    print("PASS: Patch 003 Commit B history validator complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
