# Patch 003 - Project Standardization

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
