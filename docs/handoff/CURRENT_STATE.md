# Current State

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
