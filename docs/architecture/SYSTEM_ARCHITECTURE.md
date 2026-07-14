# System Architecture

## Purpose

This document defines the architectural boundaries for the OpenHantek6022 MSO research fork. It describes how the existing upstream application, host-side USB handling, device firmware, physical hardware, validation evidence, and project documentation relate to each other.

The document is intentionally conservative. It records verified boundaries and explicitly separates them from hypotheses that still require source inspection or physical measurement.

## Architectural principles

1. Preserve upstream oscilloscope behavior unless a patch explicitly changes it.
2. Separate generally useful upstream-compatible changes from 6022BL-specific experiments.
3. Treat analog acquisition, digital acquisition, synchronization, and user-interface integration as separate concerns until evidence supports combining them.
4. Keep hardware and firmware experiments reversible.
5. Do not infer timing guarantees from successful enumeration, device opening, or application builds.
6. Store durable decisions and evidence in the repository rather than only in chat.

## System layers

### 1. User interface and application layer

The upstream OpenHantek6022 application provides the desktop user interface, configuration flow, waveform presentation, and normal oscilloscope operation.

Responsibilities:

- device selection and configuration;
- acquisition controls;
- waveform rendering;
- application state and settings;
- user-visible diagnostics.

Patch work in this layer must not silently change ordinary 6022BE/BL behavior.

### 2. Acquisition and device abstraction layer

This layer translates application requests into device-specific acquisition operations.

Responsibilities:

- device discovery;
- capability reporting;
- configuration of sampling and trigger behavior;
- acquisition lifecycle management;
- transfer of acquired data into application-level structures.

Future mixed-signal work must not be introduced here until separate analog and digital acquisition behavior has been measured and documented.

### 3. Host USB transport layer

This layer owns communication between the macOS host and USB devices or USB functions.

Responsibilities:

- USB enumeration and descriptor inspection;
- opening and closing interfaces;
- claiming interfaces and endpoints;
- control transfers;
- bulk or interrupt transfers;
- timeout, disconnect, and recovery handling;
- transport-level logging suitable for validation.

A successful USB open proves only that the selected interface can be opened. It does not prove simultaneous operation, synchronization, sustained throughput, or data correctness.

### 4. Device firmware layer

The Hantek devices use firmware running on USB-connected controller hardware. Firmware identity, loading method, and persistence must be recorded for every experiment.

Responsibilities may include:

- USB descriptor presentation;
- endpoint behavior;
- acquisition control;
- sample transfer;
- coordination with analog or digital front-end logic.

Experimental firmware must remain RAM-loaded until recovery and rollback have been demonstrated. Persistent flashing requires a separate, explicitly approved patch and recovery plan.

### 5. Physical hardware layer

The physical Hantek 6022BL unit is the final source of truth for topology, revision, electrical behavior, timing, and synchronization capability.

The following remain separate evidence categories:

- external model and labeling;
- PCB revision and component population;
- internal USB topology;
- analog acquisition path;
- digital acquisition path;
- clock sources;
- shared or independent timing domains;
- measured offset, jitter, and drift.

Available schematics and third-party material are reference inputs, not proof that the purchased unit uses the same revision.

### 6. Validation and evidence layer

Validation is part of the architecture because correctness claims depend on reproducible evidence.

Evidence can include:

- build logs;
- toolchain reports;
- demo-mode behavior;
- USB descriptor captures;
- source inspection;
- firmware hashes;
- transfer logs;
- oscilloscope and logic measurements;
- explicit user confirmation.

Each result must be classified as `PASS`, `FAIL`, or `INCONCLUSIVE`, and claims must be labelled as verified, inferred, or unknown where applicable.

### 7. Project-control and documentation layer

The repository documentation controls the development process and preserves project knowledge.

Key ownership:

- `AGENTS.md`: agent behavior and safety rules;
- `PROJECT_INSTRUCTIONS.md`: project objectives and patch requirements;
- `docs/handoff/MASTER_INDEX.md`: official reading order;
- `docs/handoff/CURRENT_STATE.md`: current accepted baseline and next work;
- `docs/handoff/AI_MEMORY.md`: durable project context;
- `docs/history/PATCH_HISTORY.md`: chronological patch record;
- `docs/architecture/DESIGN_DECISIONS.md`: accepted architectural decisions and rationale.

## Dependency direction

The intended dependency direction is:

```text
User interface
    -> acquisition and device abstraction
        -> host USB transport
            -> device firmware
                -> physical hardware
```

Validation and documentation observe and govern all layers but must not be used as substitutes for runtime or hardware evidence.

## Current architectural baseline

Verified:

- the fork is based on OpenHantek6022 upstream;
- the unmodified application can be configured and built locally on the recorded Apple Silicon macOS host;
- no runtime source changes are required for that build baseline.

Inferred:

- available external material suggests that the 6022BL may contain distinct analog and digital acquisition functions behind an internal USB arrangement.

Unknown until physical inspection and measurement:

- the exact topology and PCB revision of the purchased unit;
- whether both acquisition functions enumerate and operate concurrently;
- whether they share a clock or have independent timing domains;
- achievable sustained throughput;
- relative offset, jitter, and drift;
- whether a maintainable mixed-signal integration is technically justified.

## Change rule

A patch that changes boundaries, ownership, public interfaces, firmware behavior, synchronization assumptions, or safety constraints must update this document or `DESIGN_DECISIONS.md` during the LOCK phase.
