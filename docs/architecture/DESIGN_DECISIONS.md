# Design Decisions

## Purpose

This document records durable architectural and engineering decisions for the
OpenHantek6022 MSO research fork.

It is inspired by Architecture Decision Records, but adapted to the project's
patch-based workflow. Each accepted decision has a stable identifier and must
remain traceable to the patch that introduced, modified, or superseded it.

## Status vocabulary

Each decision uses one of these states:

- `PROPOSED`: under discussion and not yet binding.
- `ACCEPTED`: active and binding for new work.
- `SUPERSEDED`: replaced by a newer decision.
- `REJECTED`: considered but explicitly not adopted.
- `DEFERRED`: intentionally postponed pending evidence.

## Patch traceability requirement

Every technical patch must contain a design-decision section.

The section must list one or more of:

```text
Implements:
DD-001
DD-004

Updates:
DD-007

Supersedes:
DD-003
```

If a technical patch does not depend on an existing decision, it must state:

```text
Design decisions:
None. This patch does not change or depend on an architectural decision.
```

Documentation-only housekeeping patches may omit the section only when they do
not introduce, modify, interpret, or supersede technical policy.

Every design decision must identify:

- the patch that introduced it;
- later patches that modified it;
- the decision that superseded it, if any.

## Accepted decisions

## DD-001 - Preserve upstream-compatible behavior

**Status:** ACCEPTED

**Decision**

Ordinary OpenHantek6022 oscilloscope behavior must be preserved unless a patch
explicitly changes it and provides appropriate validation evidence.

General upstream-compatible fixes must remain separate from experimental
6022BL mixed-signal work.

**Rationale**

The fork must remain understandable, reviewable, and easy to synchronize with
upstream.

**Introduced by:** Patch 003  
**Modified by:** None  
**Superseded by:** None

## DD-002 - Evidence determines correctness

**Status:** ACCEPTED

**Decision**

Source inspection, documentation, build logs, USB captures, measurements, and
explicit user confirmation determine what may be claimed as verified.

A successful build proves only that the build succeeded. It does not validate
USB behavior, hardware operation, timing, synchronization, or measurement
accuracy.

**Rationale**

The project combines software, firmware, USB transport, and physical hardware.
Correctness claims must therefore be tied to the relevant evidence type.

**Introduced by:** Patch 003  
**Modified by:** None  
**Superseded by:** None

## DD-003 - Use small reversible patches

**Status:** ACCEPTED

**Decision**

Each patch must have one narrow purpose, explicit non-goals, expected changed
files, a validation plan, completion criteria, and rollback notes.

Unrelated cleanup and speculative redesign are prohibited.

**Rationale**

Small patches are easier to validate, review, revert, and compare against known
baselines.

**Introduced by:** Patch 003  
**Modified by:** None  
**Superseded by:** None

## DD-004 - Physical hardware is the final source of truth

**Status:** ACCEPTED

**Decision**

Schematics, PCB photographs, forum posts, and third-party reverse engineering
are useful reference inputs, but they are not proof of the purchased unit's
revision, USB topology, timing behavior, or synchronization capability.

Claims about those properties remain inferred or unknown until verified on the
physical device.

**Rationale**

Commercial hardware revisions may differ from available external material.

**Introduced by:** Patch 003  
**Modified by:** None  
**Superseded by:** None

## DD-005 - Keep firmware experiments recoverable

**Status:** ACCEPTED

**Decision**

Experimental FX2 firmware must remain RAM-loaded until recovery and rollback
have been demonstrated.

Persistent flashing requires a separate explicitly approved patch with a
documented recovery procedure.

**Rationale**

Firmware experiments must not create unnecessary risk of leaving the device
unusable.

**Introduced by:** Patch 003  
**Modified by:** None  
**Superseded by:** None

## DD-006 - Prove USB behavior before mixed-signal design

**Status:** ACCEPTED

**Decision**

The project must first establish:

1. the physical unit's USB topology;
2. separate analog acquisition behavior;
3. separate digital acquisition behavior;
4. whether both functions can be opened concurrently;
5. whether both streams can operate concurrently and sustainably;
6. measured relative offset, jitter, and drift.

A unified mixed-signal API or synchronized timeline must not be designed as an
assumed requirement before this evidence exists.

**Rationale**

Enumeration or concurrent opening does not establish usable mixed-signal
operation.

**Introduced by:** Patch 003  
**Modified by:** None  
**Superseded by:** None

## DD-007 - Documentation owns durable project memory

**Status:** ACCEPTED

**Decision**

Durable project knowledge must be stored in the repository.

Ownership is divided as follows:

- `docs/MASTER_INDEX.md`: official reading order;
- `docs/CURRENT_STATE.md`: accepted baseline and immediate next work;
- `docs/AI_MEMORY.md`: durable context and lessons;
- `docs/history/PATCH_HISTORY.md`: chronological patch record;
- `docs/architecture/SYSTEM_ARCHITECTURE.md`: system boundaries;
- `docs/architecture/DESIGN_DECISIONS.md`: accepted decisions and rationale.

Chat history alone is not an accepted source of durable project state.

**Rationale**

The project must remain continuable across sessions, tools, and contributors.

**Introduced by:** Patch 003  
**Modified by:** None  
**Superseded by:** None

## DD-008 - Separate infrastructure from runtime functionality

**Status:** ACCEPTED

**Decision**

Project-method, documentation, build, and validation infrastructure changes
must remain distinguishable from runtime source changes.

A docs-only or infrastructure-only patch must explicitly verify that it did not
alter runtime behavior.

**Rationale**

This preserves clear baselines and prevents methodological changes from being
mistaken for functional validation.

**Introduced by:** Patch 003  
**Modified by:** None  
**Superseded by:** None

## DD-009 - Technical patches must reference design decisions

**Status:** ACCEPTED

**Decision**

Every technical patch must explicitly reference the design decisions it
implements, depends on, updates, or supersedes.

The reference belongs in the patch plan, handoff, or patch record and must be
reviewable before the patch is considered complete.

**Rationale**

This provides traceability between architectural intent, implementation,
validation evidence, and Git history.

**Introduced by:** Patch 003  
**Modified by:** None  
**Superseded by:** None

## Decision lifecycle

1. A decision is proposed in a scoped patch.
2. The patch records rationale, alternatives, and required evidence.
3. The decision becomes `ACCEPTED` only when the patch is accepted.
4. Later changes update the existing decision or add a new superseding decision.
5. Published decision history is not silently rewritten.

## Change rule

A patch that changes system boundaries, ownership, public interfaces, firmware
behavior, synchronization assumptions, safety constraints, or project-wide
technical policy must update this document during the `LOCK` phase.
