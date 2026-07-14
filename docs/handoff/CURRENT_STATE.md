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
