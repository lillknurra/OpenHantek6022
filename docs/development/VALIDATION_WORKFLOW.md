# Validation Workflow

## Purpose

This document defines how OpenHantek6022 patches are validated and how evidence
may be described.

Validation must match the type of claim being made. Passing one evidence class
does not imply that another class passed.

## Evidence classes

### Documentation

Examples:

- required files and headings exist;
- internal references resolve;
- stated branch and commit identities are correct;
- `git diff --check` passes.

Documentation validation does not prove build, runtime, USB, firmware, hardware,
synchronization, packaging, or measurement behavior.

### Static and source inspection

Examples:

- source paths and symbols exist;
- call paths and ownership boundaries are understood;
- generated diffs match the patch plan;
- no prohibited files changed.

Static inspection does not prove compilation or runtime behavior.

### Build

Examples:

- configuration succeeds;
- compilation completes;
- expected binaries or bundles are produced;
- warnings are recorded.

A successful build proves only the tested build configuration.

### Runtime

Examples:

- the application launches visibly;
- the intended mode is selected;
- expected UI behavior is observed;
- logs show the expected runtime path.

A command returning without an error is not sufficient evidence of visible
runtime behavior.

### USB and firmware

Examples:

- devices enumerate with recorded identifiers;
- endpoints and interfaces are captured;
- firmware loading is observed;
- transfers are sustained for a defined duration;
- recovery is demonstrated.

Enumeration alone does not prove usable acquisition.

### Physical hardware

Examples:

- PCB revision is identified from the purchased unit;
- measured voltages and signals are recorded;
- analog and digital functions are tested separately;
- concurrent operation is tested.

External schematics and forum material remain references until confirmed on the
physical unit.

### Synchronization and measurement

Examples:

- common stimulus and acquisition conditions are documented;
- offset, jitter, and drift are measured;
- sample counts and timing windows are recorded;
- accuracy is compared with an appropriate reference.

Concurrent streams do not by themselves prove synchronization.

## Required validation plan

Before implementation, every patch records:

1. objective;
2. non-goals;
3. base branch and base commit;
4. expected changed files;
5. applicable design decisions;
6. required evidence classes;
7. commands or procedures;
8. pass criteria;
9. failure and inconclusive criteria;
10. rollback.

Use `Not applicable` rather than silently omitting an evidence class.

## Result vocabulary

- `PASS`: stated criteria passed with recorded evidence.
- `FAIL`: stated criteria failed.
- `INCONCLUSIVE`: evidence is insufficient or ambiguous.
- `NOT RUN`: planned validation was not executed.
- `NOT APPLICABLE`: the class does not apply to the patch.

Never convert `INCONCLUSIVE` or `NOT RUN` into `PASS`.

## Validation order

Run the cheapest relevant checks first:

1. repository and branch sanity;
2. intended-file check;
3. static and structural checks;
4. whitespace and formatting checks;
5. build;
6. runtime;
7. USB and firmware;
8. physical hardware;
9. synchronization and measurement.

Stop when a failed prerequisite makes later claims invalid, but record what was
not run.

## Documentation-only patch minimum

A documentation-only patch must verify:

```bash
git status -sb
git diff --check
git diff --stat
git diff --name-only
```

It must also verify:

- required files and markers;
- internal paths where practical;
- exact staged-file set;
- no runtime or firmware files changed relative to the patch base.

## Technical patch minimum

A technical patch must additionally record:

- build command and result;
- runtime test or explicit reason it was not run;
- design-decision references;
- affected hardware or firmware assumptions;
- rollback or recovery procedure.

Hardware-dependent claims remain `INCONCLUSIVE` or `NOT RUN` until the required
device evidence exists.

## Evidence capture

Store durable evidence in the repository when appropriate:

- commands and concise outputs in patch records;
- long logs in a dedicated evidence directory;
- screenshots only when visual behavior matters;
- measurements with equipment, setup, units, and uncertainty;
- hashes or commit IDs for baselines and generated artifacts.

Do not paste uncontrolled terminal output into canonical state documents.

## Validator requirements

Repository-local validators should:

- be deterministic;
- return non-zero on failure;
- print a short final PASS or FAIL summary;
- distinguish missing files from incorrect content;
- check current worktree changes as well as committed branch changes;
- avoid modifying the repository;
- avoid treating ignored build output as a patch change.

A validator passing proves only the checks implemented by that validator.

## Completion rule

A patch cannot be marked complete until:

- applicable criteria are recorded;
- validation results use the approved vocabulary;
- failures and limitations remain visible;
- durable documents are updated during `LOCK`;
- staged files match the commit plan;
- the published commit is verified after push.
