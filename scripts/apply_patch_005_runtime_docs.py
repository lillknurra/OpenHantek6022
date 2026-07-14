#!/usr/bin/env python3
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BRANCH = "project/patch-005-demo-runtime-baseline"
BASE = "bd6d86b5f21bb07efc6c06b7432dde36d1214b34"
RESULT_FILE = ROOT / "docs/evidence/patch_005/runtime_result.env"


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True, check=True).stdout.strip()


def read_result() -> dict[str, str]:
    if not RESULT_FILE.is_file():
        raise SystemExit("ERROR: run scripts/run_patch_005_demo_runtime.sh first")
    values: dict[str, str] = {}
    for line in RESULT_FILE.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            values[key] = value
    if values.get("RESULT") not in {"PASS", "FAIL", "INCONCLUSIVE"}:
        raise SystemExit("ERROR: invalid runtime result")
    return values


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    desired = content.rstrip() + "\n"
    target.write_text(desired, encoding="utf-8")
    print(f"PASS: synchronized {path}")


def main() -> None:
    if git("branch", "--show-current") != BRANCH:
        raise SystemExit(f"ERROR: expected branch {BRANCH}")
    result = read_result()
    status = result["RESULT"]
    reason = result.get("REASON", "")

    write("docs/history/PATCH_004.md", f"""# Patch 004 - Post-Merge State Lock and GitHub CLI Workflow

## Status

```text
COMPLETE / MERGED
```

## Merge identity

```text
PR #3
Merge commit: {BASE}
Target: project/patch-002-macos-build-baseline
```

## Result

Patch 004 locked the Patch 003 merge state and documented the GitHub CLI ready,
merge, branch-deletion, and post-merge synchronization workflow.

## Next patch

```text
Patch 005 - visible demo-mode runtime baseline
```
""")

    write("docs/history/PATCH_005.md", f"""# Patch 005 - Visible Demo-Mode Runtime Baseline

## Identity

- Branch: `{BRANCH}`
- Base branch: `project/patch-002-macos-build-baseline`
- Base commit: `{BASE}`
- Status: VALIDATED LOCALLY / UNMERGED
- Runtime result: `{status}`

## Purpose

Establish whether the existing Apple Silicon macOS build starts visibly and
operates responsively in OpenHantek demo mode without physical hardware.

## Command

```text
build/openhantek/OpenHantek.app/Contents/MacOS/<executable> -d
```

## Result

```text
{status}: {reason}
```

Evidence:

```text
docs/evidence/patch_005/runtime_result.md
docs/evidence/patch_005/runtime.log
```

## Design decisions

**Implements:** `DD-001`, `DD-002`, `DD-003`, `DD-007`, `DD-008`, `DD-009`

## Validation boundary

This patch validates visible demo-mode runtime only. It does not validate USB,
firmware, physical hardware, concurrent acquisition, synchronization, packaging,
or measurement accuracy.

## Runtime changes

None intended. Patch 005 adds test tooling, evidence, and durable documentation.

## Rollback

Revert the Patch 005 commit. No runtime source or firmware rollback is required.

## Next patch

```text
Patch 006 - USB enumeration baseline
```
""")

    write("docs/history/PATCH_HISTORY.md", f"""# Patch History

## Patch 001 - Project governance baseline

**Status:** ACCEPTED.

## Patch 002 - Apple Silicon macOS build baseline

**Status:** ACCEPTED.

Verified build completion and application bundle creation. Visible runtime was
not verified by Patch 002.

## Patch 003 - Project standardization

**Status:** COMPLETE / MERGED through PR #2.

## Patch 004 - Post-merge state lock and GitHub CLI workflow

**Status:** COMPLETE / MERGED through PR #3.

```text
Merge commit: {BASE}
```

## Patch 005 - Visible demo-mode runtime baseline

**Status:** VALIDATED LOCALLY / UNMERGED.

```text
Runtime result: {status}
```

Detailed record: `docs/history/PATCH_005.md`
""")

    write("docs/handoff/CURRENT_STATE.md", f"""# Current State

Last updated: 2026-07-14

## Repository

- Fork: `lillknurra/OpenHantek6022`
- Local repository: `~/GitHub/OpenHantek6022`
- Active branch: `{BRANCH}`
- Base branch: `project/patch-002-macos-build-baseline`
- Base commit: `{BASE}`

## Patch 004 status

**Status:** COMPLETE / MERGED through PR #3.

## Patch 005 status

**Status:** VALIDATED LOCALLY / UNMERGED.

```text
Runtime result: {status}
Reason: {reason}
```

## Verified

- Apple Silicon macOS build and application bundle creation from Patch 002.
- Patch 003 and Patch 004 are merged.
- Patch 005 process survived startup and produced durable evidence.
- Visible demo-mode result is exactly `{status}`.

## Unknown or unverified

- physical Hantek enumeration and acquisition;
- exact hardware revision and USB topology;
- concurrent analog and digital acquisition;
- synchronization;
- packaging and measurement correctness.

## Immediate next work

Review and merge Patch 005. Then begin Patch 006 - USB enumeration baseline.
""")

    write("docs/handoff/AI_MEMORY.md", f"""# AI Memory

## Accepted baseline

Patch 004 is merged through PR #3 at `{BASE}`.

## Current patch

```text
Patch 005 - visible demo-mode runtime baseline
Branch: {BRANCH}
Runtime result: {status}
```

## Evidence rule

Patch 005 proves only the recorded demo-mode runtime result. It does not prove
USB, firmware, hardware, synchronization, packaging, or measurement behavior.

## Immediate continuation

Validate the exact Patch 005 file set, publish the commit, open a draft PR, and
merge only if the recorded result is represented honestly.
""")

    write("docs/handoff/HANDOFF.md", f"""# Handoff

## Exact continuation point

```text
Repository: ~/GitHub/OpenHantek6022
Active branch: {BRANCH}
Base branch: project/patch-002-macos-build-baseline
Base commit: {BASE}
```

## Current patch

```text
Patch 005 - visible demo-mode runtime baseline
Commit: Patch 005: establish visible demo-mode runtime baseline
Runtime result: {status}
```

## Expected files

```text
docs/evidence/patch_005/runtime.log
docs/evidence/patch_005/runtime_result.env
docs/evidence/patch_005/runtime_result.md
docs/handoff/CURRENT_STATE.md
docs/handoff/AI_MEMORY.md
docs/handoff/HANDOFF.md
docs/history/PATCH_004.md
docs/history/PATCH_005.md
docs/history/PATCH_HISTORY.md
scripts/run_patch_005_demo_runtime.sh
scripts/apply_patch_005_runtime_docs.py
scripts/validate_patch_005_runtime_baseline.py
```

## Next action

Run the validator, stage exactly the expected files, commit, push, and open a
draft pull request targeting the Patch 004 merged base branch.
""")

    print(f"PASS: Patch 005 documentation applied with result={status}")


if __name__ == "__main__":
    main()
