#!/usr/bin/env python3
"""Patch 003 - apply patch-history documentation.

Creates:
- docs/history/PATCH_HISTORY.md
- docs/history/PATCH_003.md

This script is documentation-only and idempotent. It refuses to overwrite a
different existing file.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_BRANCH = "project/patch-003-project-standardization"
PATCH_HISTORY = ROOT / "docs" / "history" / "PATCH_HISTORY.md"
PATCH_003 = ROOT / "docs" / "history" / "PATCH_003.md"

PATCH_HISTORY_CONTENT = r"""# Patch History

## Purpose

This document is the chronological index of accepted and in-progress project
patches for the OpenHantek6022 MSO research fork.

It records scope, evidence, limitations, and continuation points. Detailed
implementation notes belong in the individual patch record when one exists.

## Status vocabulary

- `ACCEPTED`: reviewed and retained as a project baseline.
- `IN PROGRESS`: implementation or documentation is still being completed.
- `PASS`: the stated validation scope passed.
- `FAIL`: the stated validation scope failed.
- `INCONCLUSIVE`: available evidence is insufficient.
- `MERGED`: integrated into its target branch.
- `UNMERGED`: still present only on its patch branch.

A build result, runtime result, USB result, and hardware result are separate
evidence categories and must not be treated as interchangeable.

## Patch 001 - Project governance baseline

**Status:** ACCEPTED on its project branch.

**Purpose**

Establish the repository-first project workflow, source-of-truth rules, safety
constraints, documentation structure, and patch-based development discipline.

**Result**

The project gained a durable governance baseline for continued engineering
work.

**Validation scope**

Documentation and repository-structure review only.

**Limitations**

No application runtime, USB device, firmware, packaging, or physical hardware
behavior was validated by this patch.

## Patch 002 - Apple Silicon macOS build baseline

**Status:** ACCEPTED as the technical baseline for Patch 003.

**Accepted baseline commit**

```text
501ffe7d352abe4eb01ce0afbd498f0cf4fb03ac
```

**Purpose**

Establish a reproducible local build baseline for the existing unmodified
OpenHantek6022 application on the recorded Apple Silicon macOS host.

**Verified evidence**

- Host environment was recorded as macOS 26.5.2 / Darwin 25.5.0 / arm64.
- Apple Command Line Tools and Apple Clang were used.
- CMake, Homebrew, Git, and Qt versions were recorded.
- Configuration and compilation reached:

```text
[100%] Built target OpenHantek
```

- The application bundle was produced at:

```text
build/openhantek/OpenHantek.app
```

- No runtime source change was required for the build baseline.

**Observed non-fatal warnings**

- libusb flexible or zero-length array warnings;
- ignored `nodiscard` result in
  `openhantek/src/usb/uploadFirmware.cpp`;
- missing `WrapVulkanHeaders`, treated as non-fatal for this build.

**Not verified**

- visible demo-mode operation;
- operation with physical Hantek hardware;
- USB acquisition behavior;
- firmware loading;
- packaging or distribution;
- measurement correctness.

A launch command returning without a terminal error is not sufficient evidence
to mark demo operation as `PASS`.

## Patch 003 - Project standardization

**Status:** IN PROGRESS / UNMERGED.

**Branch**

```text
project/patch-003-project-standardization
```

**Base branch**

```text
project/patch-002-macos-build-baseline
```

**Purpose**

Standardize architecture, design decisions, branching, release, validation,
history, handoff, and documentation ownership without changing OpenHantek
runtime behavior.

**Completed work**

- branching strategy documentation;
- release-process documentation;
- system architecture;
- durable design decisions `DD-001` through `DD-009`;
- requirement that every technical patch references applicable design
  decisions;
- reproducible architecture-document applicator and validator.

**Architecture commit**

```text
9a90ec76ec9ce1ecdd7cd0791f2a6204e2dc325f
Patch 003: add architecture documents
```

**Current validation result**

`PASS` for the completed architecture-document subset:

- required architecture files exist;
- required decision identifiers exist;
- no OpenHantek runtime or firmware files changed in that subset;
- whitespace validation passed.

**Current limitations**

Patch 003 is not yet complete, merged, tagged, or a runtime baseline.

No new runtime, USB, firmware, hardware, synchronization, packaging, or
measurement claim is introduced by Patch 003.

**Detailed record**

See `docs/history/PATCH_003.md`.

## Next history update rule

Update this file during the `LOCK` phase when a patch:

- becomes accepted;
- changes validation status;
- is merged or abandoned;
- creates a new durable continuation point;
- modifies or supersedes a design decision.
"""
PATCH_003_CONTENT = r"""# Patch 003 - Project Standardization

## Identity

**Title:** Project standardization  
**Branch:** `project/patch-003-project-standardization`  
**Base:** `project/patch-002-macos-build-baseline`  
**Status:** IN PROGRESS / UNMERGED  
**Patch type:** documentation and project infrastructure

## Purpose

Create a coherent, repository-owned engineering method for continued
OpenHantek6022 research and development.

Patch 003 standardizes:

- official document ownership and reading order;
- architecture boundaries;
- durable design decisions;
- patch planning and validation;
- branching and Git workflow;
- release discipline;
- patch history;
- handoff and current-state maintenance.

## Non-goals

Patch 003 does not:

- change OpenHantek runtime source;
- change USB behavior;
- change device firmware;
- claim mixed-signal synchronization;
- validate physical Hantek hardware;
- validate demo-mode user-visible operation;
- create a distributable release;
- merge itself into Patch 002 or `main`.

## Design decisions

**Implements:**

- `DD-002` - Evidence determines correctness.
- `DD-003` - Use small reversible patches.
- `DD-007` - Documentation owns durable project memory.
- `DD-008` - Separate infrastructure from runtime functionality.
- `DD-009` - Technical patches must reference design decisions.

**Depends on:**

- `DD-001` - Preserve upstream-compatible behavior.
- `DD-004` - Physical hardware is the final source of truth.
- `DD-005` - Keep firmware experiments recoverable.
- `DD-006` - Prove USB behavior before mixed-signal design.

**Updates:** None.  
**Supersedes:** None.

## Accepted starting baseline

Patch 003 is stacked on the accepted Patch 002 commit:

```text
501ffe7d352abe4eb01ce0afbd498f0cf4fb03ac
```

Patch 002 established a successful local Apple Silicon macOS build of the
unmodified application. It did not establish demo, USB, firmware, hardware,
packaging, synchronization, or measurement correctness.

## Planned document groups

### Commit A - Architecture documents

Commit message:

```text
Patch 003: add architecture documents
```

Scope:

- `docs/architecture/SYSTEM_ARCHITECTURE.md`
- `docs/architecture/DESIGN_DECISIONS.md`
- reproducible architecture applicator;
- architecture validator.

Status: COMPLETE / PUSHED.

Published commit:

```text
9a90ec76ec9ce1ecdd7cd0791f2a6204e2dc325f
```

Validation:

```text
PASS: branch=project/patch-003-project-standardization
PASS: architecture documents present
PASS: DD-001 through DD-009 present
PASS: technical-patch traceability requirement present
PASS: no OpenHantek runtime or firmware files changed
PASS: whitespace check
```

### Commit B - Patch history

Commit message:

```text
Patch 003: add patch history
```

Scope:

- `docs/history/PATCH_HISTORY.md`
- `docs/history/PATCH_003.md`
- reproducible history applicator;
- history validator.

Status: IN PROGRESS.

### Later Patch 003 groups

Planned later groups include:

- canonical handoff and current-state documents;
- validation workflow;
- completed development and Git workflow;
- compatibility pointers for legacy top-level documents;
- final structural validation and completion record.

Exact grouping may be refined, but scope must remain documentation and project
infrastructure only.

## Validation model

Patch 003 uses documentation-only validation.

Required checks include:

1. expected files exist;
2. required headings and markers exist;
3. internal repository paths are valid;
4. design-decision references are present where required;
5. no runtime or firmware files changed relative to Patch 002;
6. `git diff --check` passes;
7. staged files exactly match the commit plan.

A documentation validator passing does not validate application runtime or
hardware behavior.

## Evidence classification

### Verified

- Patch 003 branch exists and is based on Patch 002.
- Architecture documents have been created and pushed.
- `DD-001` through `DD-009` are recorded.
- Technical patches are required to reference design decisions.
- Commit A validator passed.
- Commit A did not alter OpenHantek runtime or firmware files.

### Inferred

- The standardized document structure should make future work easier to review
  and continue across conversations.

This remains an engineering-process inference, not runtime evidence.

### Unknown or unverified

- visible demo operation;
- physical Hantek enumeration and acquisition;
- internal USB topology of the purchased device;
- concurrent analog and digital operation;
- clock relationships;
- sustained throughput;
- offset, jitter, and drift;
- packaging and distribution.

## Rollback

Before merge, rollback consists of discarding or deleting the Patch 003 branch.

After merge, rollback consists of reverting the relevant Patch 003 commits.
Published history must not be rewritten.

Applicator scripts must refuse to overwrite differing existing documents
without explicit review.

## Completion criteria

Patch 003 is complete only when:

- canonical reading order is defined;
- current state and durable AI memory are synchronized;
- architecture and design decisions are recorded;
- branching, development, Git, release, and validation workflows are complete;
- patch history and Patch 003 record are complete;
- legacy duplicate documents are converted to non-authoritative pointers where
  required;
- structural validation passes;
- comparison against Patch 002 confirms no runtime or firmware changes;
- final handoff records limitations and the exact next patch;
- the user accepts the patch for review or merge.

## Current continuation point

Complete Commit B using the repository-local applicator and validator. Review
the diff, stage exactly the four intended files, commit with:

```text
Patch 003: add patch history
```

Then push to:

```text
origin/project/patch-003-project-standardization
```
"""


def current_branch() -> str:
    result = subprocess.run(
        ["git", "branch", "--show-current"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


def write_expected(path: Path, content: str) -> None:
    desired = content.rstrip() + "\n"
    if path.exists():
        existing = path.read_text(encoding="utf-8")
        if existing == desired:
            print(f"PASS: {path.relative_to(ROOT)} already has expected content")
            return
        raise SystemExit(
            f"ERROR: {path.relative_to(ROOT)} exists with different content; "
            "review it manually before overwriting"
        )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(desired, encoding="utf-8")
    print(f"PASS: created {path.relative_to(ROOT)}")


def main() -> None:
    if not (ROOT / ".git").exists():
        raise SystemExit(f"ERROR: not a Git repository: {ROOT}")

    branch = current_branch()
    if branch != EXPECTED_BRANCH:
        raise SystemExit(
            f"ERROR: expected branch {EXPECTED_BRANCH}, current branch is {branch}"
        )

    required = [
        ROOT / "docs" / "architecture" / "SYSTEM_ARCHITECTURE.md",
        ROOT / "docs" / "architecture" / "DESIGN_DECISIONS.md",
    ]
    for path in required:
        if not path.exists():
            raise SystemExit(f"ERROR: required file missing: {path.relative_to(ROOT)}")

    write_expected(PATCH_HISTORY, PATCH_HISTORY_CONTENT)
    write_expected(PATCH_003, PATCH_003_CONTENT)
    print("PASS: Patch 003 history apply complete")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        print(f"ERROR: command failed: {exc}", file=sys.stderr)
        raise SystemExit(exc.returncode)
