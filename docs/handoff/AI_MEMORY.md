# AI Memory

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
