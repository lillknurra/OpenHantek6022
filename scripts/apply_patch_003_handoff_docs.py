#!/usr/bin/env python3
"""Patch 003 - synchronize canonical handoff documents.

Creates:
- docs/handoff/MASTER_INDEX.md
- docs/handoff/CURRENT_STATE.md
- docs/handoff/AI_MEMORY.md
- docs/handoff/HANDOFF.md

This script is documentation-only and idempotent. It refuses to overwrite a
different existing file.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_BRANCH = "project/patch-003-project-standardization"

FILES = {
    ROOT / "docs/handoff/MASTER_INDEX.md": r"""# Master Index

## Authority

This file is the sole canonical reading order for the OpenHantek6022 MSO
research fork.

Legacy top-level documents may remain temporarily for compatibility, but they
must not define a competing reading order. When legacy documents are converted
to pointers, this file remains authoritative.

## Required reading order

1. `../../AGENTS.md`
2. `../../PROJECT_INSTRUCTIONS.md`
3. `../development/DEVELOPMENT_WORKFLOW.md`
4. `CURRENT_STATE.md`
5. `AI_MEMORY.md`
6. `../history/PATCH_003.md`
7. `../architecture/SYSTEM_ARCHITECTURE.md`
8. `../architecture/DESIGN_DECISIONS.md`
9. `../build/MACOS_BUILD_BASELINE.md`
10. `../HARDWARE_BASELINE.md`
11. `../USB_ARCHITECTURE.md`
12. `../MSO_HYPOTHESES.md`
13. `../TEST_PLAN.md`
14. `HANDOFF.md`

## Document ownership

| Document | Ownership |
|---|---|
| `../../AGENTS.md` | Agent behavior, safety rules, and execution discipline |
| `../../PROJECT_INSTRUCTIONS.md` | Project purpose, scope, and patch requirements |
| `../development/DEVELOPMENT_WORKFLOW.md` | Complete patch lifecycle |
| `CURRENT_STATE.md` | Current accepted baseline, active branch, and next work |
| `AI_MEMORY.md` | Durable context and permanent lessons |
| `../history/PATCH_HISTORY.md` | Chronological patch record |
| `../history/PATCH_003.md` | Detailed current patch record |
| `../architecture/SYSTEM_ARCHITECTURE.md` | System boundaries and layer ownership |
| `../architecture/DESIGN_DECISIONS.md` | Accepted design decisions and rationale |
| `HANDOFF.md` | Exact continuation point for the next session |

## Reading rules

- Read in order unless the task is a narrowly scoped inspection.
- Confirm the active branch and baseline before proposing changes.
- Treat `Verified`, `Inferred`, and `Unknown` as distinct evidence classes.
- Do not infer runtime or hardware correctness from documentation or build
  success.
- Every technical patch must reference applicable design decisions.
- Update this index only when document ownership or reading order changes.

## Current patch

Patch 003 standardizes project architecture, history, handoff, validation, and
development workflow without changing OpenHantek runtime or firmware behavior.

Current branch:

```text
project/patch-003-project-standardization
```

Accepted technical base:

```text
project/patch-002-macos-build-baseline
501ffe7d352abe4eb01ce0afbd498f0cf4fb03ac
```
""",
    ROOT / "docs/handoff/CURRENT_STATE.md": r"""# Current State

Last updated: 2026-07-14

## Repository

- Fork: `lillknurra/OpenHantek6022`
- Upstream: `OpenHantek/OpenHantek6022`
- Local repository: `~/GitHub/OpenHantek6022`
- Active branch: `project/patch-003-project-standardization`
- Base branch: `project/patch-002-macos-build-baseline`

## Accepted technical baseline

Patch 003 is stacked on:

```text
501ffe7d352abe4eb01ce0afbd498f0cf4fb03ac
```

Patch 002 established a successful local Apple Silicon macOS build of the
unmodified OpenHantek6022 application.

Verified Patch 002 evidence:

- host: macOS 26.5.2 / Darwin 25.5.0 / arm64;
- Apple Command Line Tools and Apple Clang;
- CMake 4.3.4;
- Homebrew 6.0.5;
- Git 2.54.0;
- Qt 6.11.1;
- build completed with `[100%] Built target OpenHantek`;
- application bundle created at `build/openhantek/OpenHantek.app`;
- no runtime source change was required for the build baseline.

Observed non-fatal warnings:

- libusb flexible or zero-length arrays;
- ignored `nodiscard` result in
  `openhantek/src/usb/uploadFirmware.cpp`;
- missing `WrapVulkanHeaders`.

## Patch 003 status

**Status:** IN PROGRESS / UNMERGED.

Completed and pushed:

- branching strategy documentation;
- release process documentation;
- system architecture;
- design decisions `DD-001` through `DD-009`;
- technical-patch design-decision traceability rule;
- patch history;
- detailed Patch 003 record;
- reproducible applicators and validators for Commit A and Commit B.

Published commits:

```text
9a90ec76ec9ce1ecdd7cd0791f2a6204e2dc325f
Patch 003: add architecture documents

f7fbfdca6635fc0a0990767ae527b82e3adc5842
Patch 003: add patch history
```

Current work:

```text
Commit C
Patch 003: synchronize handoff documents
```

## Verified

- The Patch 003 branch exists and tracks origin.
- Commit A passed its architecture-document validator.
- Commit B passed its history-document validator.
- `DD-001` through `DD-009` are present.
- Every technical patch must reference applicable design decisions.
- No OpenHantek runtime or firmware changes were introduced by Commit A or
  Commit B.
- Patch history now distinguishes build, runtime, USB, firmware, hardware,
  packaging, synchronization, and measurement evidence.

## Inferred

- Available external material suggests that the 6022BL may contain separate
  analog and digital acquisition functions behind an internal USB arrangement.
- Standardized documentation should make future work easier to review and
  continue across sessions.

These remain inferences, not runtime or hardware evidence.

## Unknown or unverified

- visible demo-mode operation;
- physical Hantek device enumeration;
- exact PCB revision and internal USB topology;
- whether analog and digital functions can be opened concurrently;
- whether both streams can run concurrently without loss;
- clock relationships;
- sustained throughput;
- relative offset, jitter, and drift;
- mixed-signal synchronization feasibility;
- packaging and distribution;
- measurement correctness.

## Safety constraints

- Do not perform mains-referenced measurements with this USB oscilloscope.
- Keep experimental firmware RAM-loaded until recovery is demonstrated.
- Do not claim hardware behavior without physical evidence.
- Preserve upstream-compatible oscilloscope behavior unless a validated patch
  explicitly changes it.

## Immediate next work

Complete Patch 003 documentation standardization:

1. synchronize canonical handoff documents;
2. add the validation workflow;
3. complete development and Git workflow documents;
4. convert legacy duplicate documents to non-authoritative pointers;
5. run final structural comparison against Patch 002;
6. open a draft pull request targeting Patch 002.

No runtime change should begin before Patch 003 is reviewed and accepted.
""",
    ROOT / "docs/handoff/AI_MEMORY.md": r"""# AI Memory

## Project identity

- Repository: `lillknurra/OpenHantek6022`
- Upstream: `OpenHantek/OpenHantek6022`
- Local path: `~/GitHub/OpenHantek6022`
- Primary target: Hantek 6022BL on Apple Silicon macOS.
- Long-term goal: determine whether simultaneous analog and 16-channel digital
  acquisition can be implemented and synchronized maintainably.

## Source of truth

GitHub is the only source of truth.

Canonical reading order:

```text
docs/handoff/MASTER_INDEX.md
```

Do not treat chat history, old ZIP files, or unpushed local edits as accepted
project state.

## Current baseline

Active branch:

```text
project/patch-003-project-standardization
```

Patch 003 base:

```text
project/patch-002-macos-build-baseline
501ffe7d352abe4eb01ce0afbd498f0cf4fb03ac
```

Published Patch 003 commits:

```text
9a90ec76ec9ce1ecdd7cd0791f2a6204e2dc325f
Patch 003: add architecture documents

f7fbfdca6635fc0a0990767ae527b82e3adc5842
Patch 003: add patch history
```

## Verified build baseline

Patch 002 verified:

- Apple Silicon macOS build;
- Apple Command Line Tools and Apple Clang;
- Qt 6.11.1;
- `[100%] Built target OpenHantek`;
- bundle at `build/openhantek/OpenHantek.app`;
- no runtime source change required.

Patch 002 did not verify visible demo behavior, USB acquisition, hardware,
firmware, packaging, synchronization, or measurement correctness.

## Durable method

- One patch has one narrow purpose.
- Every patch defines expected files, validation, completion criteria, and
  rollback.
- Use `IMPLEMENT -> VALIDATE -> PUBLISH -> LOCK -> COMPLETE`.
- Prefer reproducible applicator and validator scripts for large document
  changes.
- Review the diff before staging.
- Stage exact files only.
- No GitHub write operation in chat without a defined commit message first.
- Every technical patch must reference the design decisions it implements,
  depends on, updates, or supersedes.
- Build success is not runtime validation.
- Runtime success is not hardware or synchronization validation.
- Never present hypotheses as verified facts.
- Preserve GPL-3.0 obligations and upstream history.
- Do not rewrite published history.
- Keep experiments reversible.

## Accepted design decisions

- `DD-001`: preserve upstream-compatible behavior.
- `DD-002`: evidence determines correctness.
- `DD-003`: use small reversible patches.
- `DD-004`: physical hardware is the final source of truth.
- `DD-005`: keep firmware experiments recoverable.
- `DD-006`: prove USB behavior before mixed-signal design.
- `DD-007`: documentation owns durable project memory.
- `DD-008`: separate infrastructure from runtime functionality.
- `DD-009`: technical patches must reference design decisions.

## User environment

- User: Petter (`lillknurra`).
- Primary development environment: MacBook / macOS.
- Local repositories normally live under `~/GitHub/`.
- OpenHantek6022 now lives at `~/GitHub/OpenHantek6022`.
- Related experience includes ESP32-S3, SPI sensors, PDM microphones, firmware
  validation, and PCB diagnostics.
- Multimeter: UNI-T UT161D.
- Target hardware: Hantek 6022BL.

## Current unknowns

- physical device revision;
- exact USB topology;
- simultaneous enumeration and operation;
- separate acquisition behavior;
- sustained transfer capacity;
- clock relationships;
- offset, jitter, and drift;
- mixed-signal synchronization feasibility.

## Immediate continuation

Finish Patch 003 documentation and structural validation before any runtime,
USB, firmware, or hardware modification.
""",
    ROOT / "docs/handoff/HANDOFF.md": r"""# Handoff

## Purpose

This document is the exact continuation point for the next OpenHantek6022
development session.

## Repository state

Repository:

```text
lillknurra/OpenHantek6022
```

Local path:

```text
~/GitHub/OpenHantek6022
```

Active branch:

```text
project/patch-003-project-standardization
```

Base branch:

```text
project/patch-002-macos-build-baseline
```

Accepted technical base commit:

```text
501ffe7d352abe4eb01ce0afbd498f0cf4fb03ac
```

## Current patch

```text
Patch 003 - Project standardization
```

Patch type:

```text
documentation and project infrastructure only
```

No OpenHantek runtime or firmware change is intended.

## Completed and published

### Commit A

```text
9a90ec76ec9ce1ecdd7cd0791f2a6204e2dc325f
Patch 003: add architecture documents
```

Result:

- `SYSTEM_ARCHITECTURE.md` present;
- `DESIGN_DECISIONS.md` present;
- `DD-001` through `DD-009` present;
- technical-patch traceability requirement present;
- architecture validator passed;
- no runtime or firmware files changed.

### Commit B

```text
f7fbfdca6635fc0a0990767ae527b82e3adc5842
Patch 003: add patch history
```

Result:

- `PATCH_HISTORY.md` present;
- `PATCH_003.md` present;
- design-decision references present;
- history validator passed;
- no runtime or firmware files changed.

## Current work

Commit C:

```text
Patch 003: synchronize handoff documents
```

Expected files:

```text
docs/handoff/MASTER_INDEX.md
docs/handoff/CURRENT_STATE.md
docs/handoff/AI_MEMORY.md
docs/handoff/HANDOFF.md
scripts/apply_patch_003_handoff_docs.py
scripts/validate_patch_003_handoff_docs.py
```

Design decisions:

```text
Implements:
DD-002
DD-003
DD-007
DD-008
DD-009
```

## Validation requirements for Commit C

- all four handoff documents exist;
- `MASTER_INDEX.md` defines the sole canonical reading order;
- internal paths referenced by `MASTER_INDEX.md` exist;
- `CURRENT_STATE.md` records Patch 002 evidence and Patch 003 status honestly;
- `AI_MEMORY.md` records durable method and design decisions;
- `HANDOFF.md` records exact continuation;
- no runtime or firmware files changed relative to Patch 002;
- `git diff --check` passes;
- only the six intended files are staged.

## Known limitations

The following are not verified:

- visible demo-mode operation;
- Hantek hardware operation;
- USB acquisition;
- firmware behavior;
- simultaneous analog and digital capture;
- synchronization;
- packaging;
- measurement correctness.

## Rollback

Before merge, discard the Patch 003 branch or revert individual commits.

After merge, revert the relevant commits. Do not rewrite published history.

## Next after Commit C

Add the canonical validation workflow and finish the development/Git workflow
documents. Then convert legacy duplicate files to compatibility pointers and
run final Patch 003 structural validation.

Do not begin runtime or hardware work until Patch 003 is accepted.
""",
}


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
        ROOT / "docs/architecture/SYSTEM_ARCHITECTURE.md",
        ROOT / "docs/architecture/DESIGN_DECISIONS.md",
        ROOT / "docs/history/PATCH_HISTORY.md",
        ROOT / "docs/history/PATCH_003.md",
    ]
    for path in required:
        if not path.exists():
            raise SystemExit(f"ERROR: required file missing: {path.relative_to(ROOT)}")

    for path, content in FILES.items():
        write_expected(path, content)

    print("PASS: Patch 003 handoff synchronization complete")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        print(f"ERROR: command failed: {exc}", file=sys.stderr)
        raise SystemExit(exc.returncode)
