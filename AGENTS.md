# AGENTS.md

# OpenHantek6022 MSO Research Fork

This repository is developed using conservative, evidence-driven, patch-based engineering.

The primary goal is to preserve a reproducible OpenHantek6022 baseline while investigating macOS support, Hantek 6022BL USB architecture, dual-device discovery, parallel analog/digital capture, and possible mixed-signal operation.

## Source of truth

The Git repository is authoritative. Documentation explains intent. Build logs, USB captures, measurements, and explicit user confirmation determine correctness.

Do not assume behavior that is not supported by source inspection, documentation, logs, captures, measurements, or user-confirmed evidence.

## Read first

Before non-trivial work:

1. Read `PROJECT_INSTRUCTIONS.md`.
2. Read `docs/handoff/MASTER_INDEX.md`.
3. Follow the reading order owned by `MASTER_INDEX.md`.
4. Read `docs/handoff/CURRENT_STATE.md` before changing code or hardware-facing behavior.

Do not duplicate the complete reading order here.

## Development philosophy

- Prefer small, reversible patches with one clear purpose.
- Audit before modifying behavior that is not fully understood.
- Avoid unrelated cleanup and speculative redesign.
- Preserve ordinary 6022BE/BL oscilloscope behavior unless a patch explicitly changes it.
- Keep general upstream-compatible fixes separate from experimental MSO work.
- Never claim synchronized mixed-signal operation until it has been measured on physical hardware.

## Official patch phases

```text
IMPLEMENT -> VALIDATE -> PUBLISH -> LOCK -> COMPLETE
```

- **IMPLEMENT:** make only scoped changes.
- **VALIDATE:** run the defined checks and collect evidence.
- **PUBLISH:** commit and push only intended files after PASS or an explicitly documented inconclusive result.
- **LOCK:** update the documents that own the new durable knowledge.
- **COMPLETE:** summarize status, evidence, commit, baseline, and next patch.

A successful build proves only that the build succeeded. It does not validate USB behavior, hardware operation, timing, synchronization, or measurement accuracy.

## Git rules

- `main` is the accepted fork baseline and must remain easy to synchronize with upstream.
- Patch branches use `project/patch-NNN-description`.
- Feature branches use `feature/short-description`.
- Hardware or firmware experiments use `experiment/short-description` until reproducible.
- Do not force-push, rewrite published history, or stage unrelated files.
- Prefer explicit file staging and one logical change per commit.

## Hardware and firmware safety

- The 6022BL has USB-referenced BNC grounds and is not an isolated mains oscilloscope.
- Test only SELV or otherwise reviewed low-voltage circuits.
- Experimental FX2 firmware must be RAM-loaded until recovery has been verified.
- Record device revision, firmware identity, host environment, wiring, commands, and raw evidence for hardware-facing experiments.

## Command standard

Whenever a next step requires a local command, include a complete copy/paste block in the same response. Follow `docs/handoff/COMMAND_OUTPUT_GUIDANCE.md`.

## Final rule

Small, documented, validated, reversible changes are preferred over large, clever, speculative changes.