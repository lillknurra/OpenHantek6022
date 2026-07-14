# AI Memory

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
