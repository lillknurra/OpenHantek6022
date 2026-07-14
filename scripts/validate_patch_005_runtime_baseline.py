#!/usr/bin/env python3
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BRANCH = "project/patch-005-demo-runtime-baseline"
BASE = "bd6d86b5f21bb07efc6c06b7432dde36d1214b34"
EXPECTED = {
    "docs/evidence/patch_005/runtime.log",
    "docs/evidence/patch_005/runtime_result.env",
    "docs/evidence/patch_005/runtime_result.md",
    "docs/handoff/CURRENT_STATE.md",
    "docs/handoff/AI_MEMORY.md",
    "docs/handoff/HANDOFF.md",
    "docs/history/PATCH_004.md",
    "docs/history/PATCH_005.md",
    "docs/history/PATCH_HISTORY.md",
    "scripts/run_patch_005_demo_runtime.sh",
    "scripts/apply_patch_005_runtime_docs.py",
    "scripts/validate_patch_005_runtime_baseline.py",
}


def run(*args: str):
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True)


def main() -> int:
    failures: list[str] = []
    branch = run("git", "branch", "--show-current").stdout.strip()
    if branch == BRANCH:
        print(f"PASS: branch={branch}")
    else:
        failures.append(f"wrong branch: {branch}")

    result_file = ROOT / "docs/evidence/patch_005/runtime_result.env"
    result = ""
    if result_file.is_file():
        values = dict(
            line.split("=", 1) for line in result_file.read_text(encoding="utf-8").splitlines() if "=" in line
        )
        result = values.get("RESULT", "")
    if result in {"PASS", "FAIL", "INCONCLUSIVE"}:
        print(f"PASS: runtime result vocabulary={result}")
    else:
        failures.append("missing or invalid runtime result")

    for rel in EXPECTED:
        if not (ROOT / rel).is_file():
            failures.append(f"missing {rel}")

    changed: set[str] = set()
    for cmd in (
        ("git", "diff", "--name-only", f"{BASE}...HEAD"),
        ("git", "diff", "--name-only"),
        ("git", "diff", "--cached", "--name-only"),
    ):
        changed.update(x for x in run(*cmd).stdout.splitlines() if x)
    for line in run("git", "status", "--porcelain", "--untracked-files=all").stdout.splitlines():
        if len(line) >= 4:
            changed.add(line[3:])

    runtime = sorted(x for x in changed if x.startswith(("openhantek/", "libOpenHantek2xxx/", "firmware/")))
    outside = sorted(x for x in changed if x not in EXPECTED)
    if runtime:
        failures.append(f"runtime or firmware changes: {runtime}")
    else:
        print("PASS: no runtime or firmware source changes")
    if outside:
        failures.append(f"unexpected changed files: {outside}")
    else:
        print("PASS: exact Patch 005 file boundary")

    for cmd in (("git", "diff", "--check"), ("git", "diff", "--cached", "--check")):
        if run(*cmd).returncode:
            failures.append("whitespace check failed")

    print("\n=== VALIDATION SUMMARY ===")
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print("FAIL: Patch 005 validator failed")
        return 1
    print("PASS: Patch 005 visible demo-mode runtime validator complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
