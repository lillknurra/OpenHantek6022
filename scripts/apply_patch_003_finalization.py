#!/usr/bin/env python3
"""Patch 003 Commit E - finalize pointers and canonical project state."""

from __future__ import annotations

from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BRANCH = "project/patch-003-project-standardization"

EXPECTED_SHAS = {'docs/MASTER_INDEX.md': '397ad278d241710739269123d8a02184e0a3cb9d', 'docs/CURRENT_STATE.md': '3762352b1031bb2b3c2aa0ecf65d6d74a2be2387', 'docs/AI_MEMORY.md': '0c7bbcba59f424b228f6505781b1a563361c0b84', 'docs/handoff/CURRENT_STATE.md': '3461962013987ef52cef871a3246101ac85b4f0d', 'docs/handoff/AI_MEMORY.md': '1d0a338a2f22f28391a07e45fba827f6b962e637'}

FILES = {
    "docs/MASTER_INDEX.md": r"""# Legacy Master Index

This file is retained only as a compatibility pointer.

The sole canonical reading order is:

```text
docs/handoff/MASTER_INDEX.md
```

Do not maintain project state or reading order in this legacy file.
""",
    "docs/CURRENT_STATE.md": r"""# Legacy Current State

This file is retained only as a compatibility pointer.

The canonical current project state is:

```text
docs/handoff/CURRENT_STATE.md
```

Do not update project status in this legacy file.
""",
    "docs/AI_MEMORY.md": r"""# Legacy AI Memory

This file is retained only as a compatibility pointer.

The canonical durable project memory is:

```text
docs/handoff/AI_MEMORY.md
```

Do not update durable project memory in this legacy file.
""",
    "docs/handoff/CURRENT_STATE.md": r"""# Current State

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

Patch 002 verified an Apple Silicon macOS build of the unmodified application,
including `[100%] Built target OpenHantek` and creation of
`build/openhantek/OpenHantek.app`.

Patch 002 did not verify visible demo behavior, USB acquisition, firmware,
physical hardware, packaging, synchronization, or measurement correctness.

## Patch 003 status

**Status:** FINAL STRUCTURAL VALIDATION IN PROGRESS / UNMERGED.

Published commits:

```text
9a90ec76ec9ce1ecdd7cd0791f2a6204e2dc325f
Patch 003: add architecture documents

f7fbfdca6635fc0a0990767ae527b82e3adc5842
Patch 003: add patch history

9200cbab1a7823693a5918c24df75cd44323c83f
Patch 003: synchronize handoff documents

bc3cad41da5a1630c936a21eb3e519dad6609294
Patch 003: add validation and development workflow
```

Current work:

```text
Commit E
Patch 003: finalize legacy pointers and structural validation
```

## Completed Patch 003 scope

- branching strategy;
- release process;
- system architecture;
- design decisions `DD-001` through `DD-009`;
- patch history;
- canonical handoff documents;
- validation workflow;
- complete development workflow;
- GitHub workflow and write-safety rules;
- repository-local applicators and validators;
- canonical ownership under `docs/handoff/`.

## Verified

- Commits A through D are published on the Patch 003 branch.
- Their local validators passed before publication.
- Canonical reading order is `docs/handoff/MASTER_INDEX.md`.
- Evidence classes distinguish documentation, build, runtime, USB, firmware,
  hardware, synchronization, packaging, and measurement claims.
- Technical patches must reference applicable design decisions.
- Patch 003 has introduced no intended OpenHantek runtime or firmware change.

## Inferred

The standardized repository structure should improve reviewability and
continuation across sessions. This is a process inference, not runtime evidence.

## Unknown or unverified

- visible demo-mode operation;
- physical Hantek device enumeration;
- exact PCB revision and USB topology;
- concurrent analog and digital operation;
- sustained transfer capacity;
- clock relationships;
- relative offset, jitter, and drift;
- mixed-signal synchronization feasibility;
- packaging and distribution;
- measurement correctness.

## Safety constraints

- Do not perform mains-referenced measurements with this USB oscilloscope.
- Keep experimental firmware RAM-loaded until recovery is demonstrated.
- Treat the purchased hardware as the final source of hardware truth.
- Preserve upstream-compatible behavior unless a validated patch changes it.

## Immediate next work

1. run Commit E final structural validation;
2. stage exactly the intended Commit E files;
3. publish Commit E;
4. verify the published commit;
5. open a draft pull request from Patch 003 to Patch 002.

No runtime, USB, firmware, or hardware modification should begin before Patch
003 is reviewed and accepted.
""",
    "docs/handoff/AI_MEMORY.md": r"""# AI Memory

## Project identity

- Repository: `lillknurra/OpenHantek6022`
- Upstream: `OpenHantek/OpenHantek6022`
- Local path: `~/GitHub/OpenHantek6022`
- Target: Hantek 6022BL on Apple Silicon macOS.
- Long-term goal: determine whether maintainable simultaneous analog and
  16-channel digital acquisition and synchronization are feasible.

## Source of truth

GitHub is the only accepted source of durable project state.

Canonical reading order:

```text
docs/handoff/MASTER_INDEX.md
```

The following files are legacy compatibility pointers only:

```text
docs/MASTER_INDEX.md
docs/CURRENT_STATE.md
docs/AI_MEMORY.md
```

## Current baseline

```text
project/patch-002-macos-build-baseline
501ffe7d352abe4eb01ce0afbd498f0cf4fb03ac
```

Active standardization branch:

```text
project/patch-003-project-standardization
```

Published Patch 003 commits:

```text
9a90ec76ec9ce1ecdd7cd0791f2a6204e2dc325f
f7fbfdca6635fc0a0990767ae527b82e3adc5842
9200cbab1a7823693a5918c24df75cd44323c83f
bc3cad41da5a1630c936a21eb3e519dad6609294
```

## Durable method

- One patch has one narrow purpose.
- Use `IMPLEMENT -> VALIDATE -> PUBLISH -> LOCK -> COMPLETE`.
- Define the commit message before a GitHub write.
- Stage exact files only.
- Review worktree and staged diffs.
- Prefer deterministic, repository-local applicators and validators.
- Applicators must be idempotent and reject unexpected existing content.
- Validators must return non-zero on failure and end with a short PASS/FAIL.
- Every technical patch references applicable design decisions.
- Build success is not runtime validation.
- Runtime success is not hardware or synchronization validation.
- Never promote `INCONCLUSIVE` or `NOT RUN` to `PASS`.
- Preserve GPL-3.0 obligations and upstream history.
- Do not rewrite published history.
- Keep firmware and hardware experiments reversible.

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
- Repositories normally live under `~/GitHub/`.
- OpenHantek6022 lives at `~/GitHub/OpenHantek6022`.
- Primary environment: MacBook / macOS.
- Multimeter: UNI-T UT161D.
- Related experience includes ESP32-S3, sensors, PDM, firmware validation, and
  PCB diagnostics.

## Current unknowns

- physical device revision;
- exact USB topology;
- separate and concurrent acquisition behavior;
- sustained throughput;
- clock relationships;
- offset, jitter, and drift;
- synchronization feasibility.

## Immediate continuation

Finish Commit E, verify the remote commit, and open a draft pull request
targeting `project/patch-002-macos-build-baseline`.
""",
    "docs/handoff/HANDOFF.md": r"""# Handoff

## Exact continuation point

Repository:

```text
~/GitHub/OpenHantek6022
```

Active branch:

```text
project/patch-003-project-standardization
```

Target branch:

```text
project/patch-002-macos-build-baseline
```

Base commit:

```text
501ffe7d352abe4eb01ce0afbd498f0cf4fb03ac
```

## Published Patch 003 commits

```text
9a90ec76ec9ce1ecdd7cd0791f2a6204e2dc325f
Patch 003: add architecture documents

f7fbfdca6635fc0a0990767ae527b82e3adc5842
Patch 003: add patch history

9200cbab1a7823693a5918c24df75cd44323c83f
Patch 003: synchronize handoff documents

bc3cad41da5a1630c936a21eb3e519dad6609294
Patch 003: add validation and development workflow
```

## Current work

Commit E:

```text
Patch 003: finalize legacy pointers and structural validation
```

Expected changed files:

```text
docs/MASTER_INDEX.md
docs/CURRENT_STATE.md
docs/AI_MEMORY.md
docs/handoff/CURRENT_STATE.md
docs/handoff/AI_MEMORY.md
docs/handoff/HANDOFF.md
docs/history/PATCH_HISTORY.md
docs/history/PATCH_003.md
scripts/apply_patch_003_finalization.py
scripts/validate_patch_003_final_structure.py
```

## Design decisions

```text
Implements:
DD-002
DD-003
DD-007
DD-008
DD-009
```

## Commit E validation

Commit E must verify:

- the three legacy documents are non-authoritative pointers;
- canonical handoff documents exist;
- required architecture, history, development, build, and technical-baseline
  documents exist;
- canonical references resolve;
- Patch 003 contains no runtime or firmware changes relative to Patch 002;
- only documentation and scripts changed;
- worktree and staged whitespace checks pass;
- the exact intended Commit E file set is staged before commit.

## Known limitations

Patch 003 does not validate application runtime, USB behavior, firmware,
physical hardware, synchronization, packaging, or measurement correctness.

## After Commit E

Verify the pushed commit and open a draft pull request:

```text
base: project/patch-002-macos-build-baseline
head: project/patch-003-project-standardization
```

Do not begin runtime or hardware work until Patch 003 is accepted.
""",
    "docs/history/PATCH_HISTORY.md": r"""# Patch History

## Purpose

Chronological index of accepted and in-progress OpenHantek6022 project patches.

Evidence categories are independent. Documentation or build success does not
prove runtime, USB, firmware, hardware, synchronization, packaging, or
measurement correctness.

## Patch 001 - Project governance baseline

**Status:** ACCEPTED on its project branch.

Established repository-first governance, safety constraints, source-of-truth
rules, and patch discipline. No runtime or hardware behavior was validated.

## Patch 002 - Apple Silicon macOS build baseline

**Status:** ACCEPTED technical base for Patch 003.

```text
501ffe7d352abe4eb01ce0afbd498f0cf4fb03ac
```

Verified configuration and compilation of the unmodified application through:

```text
[100%] Built target OpenHantek
```

and creation of:

```text
build/openhantek/OpenHantek.app
```

Visible demo behavior, USB, firmware, physical hardware, packaging,
synchronization, and measurement correctness remain unverified.

## Patch 003 - Project standardization

**Status:** FINAL STRUCTURAL VALIDATION IN PROGRESS / UNMERGED.

**Branch:** `project/patch-003-project-standardization`
**Base:** `project/patch-002-macos-build-baseline`

Published groups:

```text
9a90ec76ec9ce1ecdd7cd0791f2a6204e2dc325f
Patch 003: add architecture documents

f7fbfdca6635fc0a0990767ae527b82e3adc5842
Patch 003: add patch history

9200cbab1a7823693a5918c24df75cd44323c83f
Patch 003: synchronize handoff documents

bc3cad41da5a1630c936a21eb3e519dad6609294
Patch 003: add validation and development workflow
```

Commit E converts legacy duplicate documents to compatibility pointers,
synchronizes final handoff state, and runs structural comparison against Patch
002.

No runtime, USB, firmware, hardware, synchronization, packaging, or measurement
claim is introduced by Patch 003.

Detailed record:

```text
docs/history/PATCH_003.md
```

## History update rule

Update this file during `LOCK` when a patch is accepted, merged, abandoned,
changes validation state, or modifies a durable design decision.
""",
    "docs/history/PATCH_003.md": r"""# Patch 003 - Project Standardization

## Identity

**Branch:** `project/patch-003-project-standardization`
**Base:** `project/patch-002-macos-build-baseline`
**Base commit:** `501ffe7d352abe4eb01ce0afbd498f0cf4fb03ac`
**Status:** FINAL STRUCTURAL VALIDATION IN PROGRESS / UNMERGED
**Type:** documentation and project infrastructure

## Purpose

Create a coherent repository-owned engineering method for continued
OpenHantek6022 work without changing runtime or firmware behavior.

## Non-goals

Patch 003 does not validate or change:

- visible application runtime;
- USB acquisition;
- device firmware;
- physical hardware;
- simultaneous analog and digital capture;
- synchronization;
- packaging;
- measurement correctness.

## Design decisions

**Implements:** `DD-002`, `DD-003`, `DD-007`, `DD-008`, `DD-009`
**Depends on:** `DD-001`, `DD-004`, `DD-005`, `DD-006`
**Updates:** None
**Supersedes:** None

## Published commits

### Commit A

```text
9a90ec76ec9ce1ecdd7cd0791f2a6204e2dc325f
Patch 003: add architecture documents
```

Added system architecture, design decisions, and traceability requirements.

### Commit B

```text
f7fbfdca6635fc0a0990767ae527b82e3adc5842
Patch 003: add patch history
```

Added chronological and detailed patch records.

### Commit C

```text
9200cbab1a7823693a5918c24df75cd44323c83f
Patch 003: synchronize handoff documents
```

Established canonical handoff, state, memory, and reading order.

### Commit D

```text
bc3cad41da5a1630c936a21eb3e519dad6609294
Patch 003: add validation and development workflow
```

Completed validation, development, publication, and GitHub workflow rules.

### Commit E

```text
Patch 003: finalize legacy pointers and structural validation
```

Converts legacy documents to non-authoritative pointers, synchronizes final
handoff state, and verifies the complete Patch 003 structure against Patch 002.

## Final validation requirements

- canonical reading order exists;
- architecture and design decisions exist;
- patch history exists;
- validation and development workflows exist;
- legacy duplicate state documents are pointers only;
- internal canonical paths resolve;
- no runtime or firmware files changed relative to Patch 002;
- changed files are limited to documentation and scripts;
- worktree and staged whitespace checks pass;
- exact Commit E file set is staged.

## Rollback

Before merge, delete or abandon the Patch 003 branch.

After publication, revert the relevant commits. Do not rewrite published
history.

## Completion criteria

Patch 003 may be marked `COMPLETE / UNMERGED` after Commit E:

1. validator passes;
2. exact intended files are committed;
3. commit is pushed and verified;
4. branch is synchronized with origin.

The next action is a draft pull request targeting
`project/patch-002-macos-build-baseline`.
""",
}


def run(*args: str) -> str:
    return subprocess.run(
        list(args), cwd=ROOT, text=True, capture_output=True, check=True
    ).stdout.strip()


def apply_file(relative: str, content: str) -> None:
    path = ROOT / relative
    desired = content.rstrip() + "\n"

    if path.exists() and path.read_text(encoding="utf-8") == desired:
        print(f"PASS: {relative} already synchronized")
        return

    expected = EXPECTED_SHAS.get(relative)
    if expected is not None:
        if not path.exists():
            raise SystemExit(f"ERROR: expected existing file missing: {relative}")
        actual = run("git", "hash-object", relative)
        if actual != expected:
            raise SystemExit(
                f"ERROR: unexpected baseline for {relative}: "
                f"actual={actual} expected={expected}"
            )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(desired, encoding="utf-8")
    print(f"PASS: synchronized {relative}")


def main() -> None:
    if not (ROOT / ".git").exists():
        raise SystemExit(f"ERROR: not a Git repository: {ROOT}")
    branch = run("git", "branch", "--show-current")
    if branch != BRANCH:
        raise SystemExit(f"ERROR: expected branch {BRANCH}, current={branch}")

    for relative, content in FILES.items():
        apply_file(relative, content)

    print("PASS: Patch 003 Commit E finalization apply complete")


if __name__ == "__main__":
    main()
