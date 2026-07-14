# Patch 005 - Visible Demo-Mode Runtime Baseline

## Identity

- Branch: `project/patch-005-demo-runtime-baseline`
- Base branch: `project/patch-002-macos-build-baseline`
- Base commit: `bd6d86b5f21bb07efc6c06b7432dde36d1214b34`
- Status: VALIDATED LOCALLY / UNMERGED
- Runtime result: `PASS`

## Purpose

Establish whether the existing Apple Silicon macOS build starts visibly and
operates responsively in OpenHantek demo mode without physical hardware.

## Command

```text
build/openhantek/OpenHantek.app/Contents/MacOS/<executable> -d
```

## Result

```text
PASS: User visually confirmed visible, updating, responsive demo mode
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
