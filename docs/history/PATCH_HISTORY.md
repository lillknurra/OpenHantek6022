# Patch History

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
