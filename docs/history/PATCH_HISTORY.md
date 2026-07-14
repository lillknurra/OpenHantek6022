# Patch History

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
