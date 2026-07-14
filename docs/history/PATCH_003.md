# Patch 003 - Project Standardization

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
