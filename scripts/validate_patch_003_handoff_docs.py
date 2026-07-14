#!/usr/bin/env python3
"""Validate Patch 003 Commit C handoff synchronization."""

from __future__ import annotations

from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_BRANCH = "project/patch-003-project-standardization"
BASE = "project/patch-002-macos-build-baseline"

REQUIRED_FILES = [
    Path("docs/handoff/MASTER_INDEX.md"),
    Path("docs/handoff/CURRENT_STATE.md"),
    Path("docs/handoff/AI_MEMORY.md"),
    Path("docs/handoff/HANDOFF.md"),
]

REQUIRED_MARKERS = {
    Path("docs/handoff/MASTER_INDEX.md"): [
        "# Master Index",
        "## Authority",
        "sole canonical reading order",
        "CURRENT_STATE.md",
        "AI_MEMORY.md",
        "HANDOFF.md",
    ],
    Path("docs/handoff/CURRENT_STATE.md"): [
        "# Current State",
        "501ffe7d352abe4eb01ce0afbd498f0cf4fb03ac",
        "9a90ec76ec9ce1ecdd7cd0791f2a6204e2dc325f",
        "f7fbfdca6635fc0a0990767ae527b82e3adc5842",
        "## Unknown or unverified",
    ],
    Path("docs/handoff/AI_MEMORY.md"): [
        "# AI Memory",
        "No GitHub write operation in chat without a defined commit message first.",
        "DD-009",
        "~/GitHub/OpenHantek6022",
    ],
    Path("docs/handoff/HANDOFF.md"): [
        "# Handoff",
        "Patch 003: synchronize handoff documents",
        "## Validation requirements for Commit C",
        "## Next after Commit C",
    ],
}

RUNTIME_PREFIXES = ("openhantek/", "libOpenHantek2xxx/", "firmware/")
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

    print("\n=== PATCH 003 COMMIT C BRANCH ===")
    branch = run(["git", "branch", "--show-current"]).stdout.strip()
    if branch == EXPECTED_BRANCH:
        print(f"PASS: branch={branch}")
    else:
        failures.append(f"expected branch {EXPECTED_BRANCH}, current={branch}")
        print(f"FAIL: {failures[-1]}")

    print("\n=== DOCUMENT PRESENCE ===")
    for rel in REQUIRED_FILES:
        if (ROOT / rel).is_file():
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

    print("\n=== MASTER INDEX PATH SANITY ===")
    index_path = ROOT / "docs/handoff/MASTER_INDEX.md"
    if index_path.is_file():
        text = index_path.read_text(encoding="utf-8")
        refs = sorted(set(re.findall(r"`([^`]+\.(?:md|py|sh))`", text)))
        missing = []
        for ref in refs:
            target = (index_path.parent / ref).resolve()
            if not target.exists():
                missing.append(ref)
        if missing:
            failures.append(f"MASTER_INDEX missing paths: {missing}")
            print(f"FAIL: {failures[-1]}")
        else:
            print(f"PASS: MASTER_INDEX referenced paths exist count={len(refs)}")

    print("\n=== DESIGN DECISION REFERENCES ===")
    handoff_text = (ROOT / "docs/handoff/HANDOFF.md").read_text(encoding="utf-8")
    ids = sorted(set(re.findall(r"DD-[0-9]{3}", handoff_text)))
    expected = ["DD-002", "DD-003", "DD-007", "DD-008", "DD-009"]
    missing_ids = sorted(set(expected) - set(ids))
    if not missing_ids:
        print(
            "PASS: Commit C references all intended design decisions "
            f"(found={ids})"
        )
    else:
        failures.append(
            f"Commit C is missing intended design decisions: {missing_ids}; "
            f"found={ids}"
        )
        print(f"FAIL: {failures[-1]}")

    print("\n=== RUNTIME FILE CHECK ===")
    comparison = run(["git", "diff", "--name-only", f"{BASE}...HEAD"])
    if comparison.returncode != 0:
        failures.append("unable to compare Patch 003 against Patch 002")
        print(f"FAIL: {failures[-1]}")
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
        print("FAIL: Patch 003 Commit C handoff validator failed")
        return 1

    print("PASS: Patch 003 Commit C handoff validator complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
