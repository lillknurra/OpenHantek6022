# AGENTS.md

## Scope
This fork investigates Hantek 6022BL hardware, macOS support, dual-device discovery, parallel analog/digital capture, and possible mixed-signal operation.

## Upstream preservation
- Keep `main` aligned with `OpenHantek/OpenHantek6022`.
- Develop only on project or feature branches.
- Preserve GPL-3.0 licensing and upstream attribution.
- Separate generally useful fixes from experimental 6022BL work.

## Engineering rules
- Establish a reproducible baseline before changing runtime behavior.
- Record hardware revision, USB descriptors, firmware identity, OS, toolchain, and test wiring.
- Label statements as verified, inferred, or unknown.
- Never claim synchronized MSO operation until measured on physical hardware.
- Prefer small patches with explicit acceptance criteria and rollback notes.
- Do not perform mains-referenced measurements with the 6022BL.

## Required reading
Read in order:
1. `PROJECT_INSTRUCTIONS.md`
2. `docs/MASTER_INDEX.md`
3. `docs/ENGINEERING_METHOD.md`
4. `docs/CURRENT_STATE.md`
5. `docs/HARDWARE_BASELINE.md`
6. `docs/USB_ARCHITECTURE.md`
7. `docs/MSO_HYPOTHESES.md`
8. `docs/TEST_PLAN.md`
