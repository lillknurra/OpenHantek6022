# Patch 001 Handoff — Governance and Upstream Baseline

## Status
Patch 001 establishes project governance and documentation only. It does not change OpenHantek6022 runtime behavior.

## Baseline
- Fork: `lillknurra/OpenHantek6022`
- Upstream: `OpenHantek/OpenHantek6022`
- Baseline commit: `4abdcce9be1319bdc83d9ff1b2c96edfcbb22506`
- Branch: `project/patch-001-governance-baseline`

## Added
- Agent and project instructions
- Project rules and GitHub workflow
- Master index, current state, engineering method, and AI memory
- Hardware and USB baseline notes
- MSO hypotheses and staged test plan
- New-chat start prompt
- macOS USB baseline collection script

## Verified
- Fork is writable.
- Branch is based directly on the recorded upstream baseline.
- Changes are documentation and diagnostics only.

## Not yet verified
- Local macOS build
- Demo-mode launch
- Packaging
- Physical 6022BL USB topology
- Parallel analog/digital operation

## Next patch
Patch 002 — macOS unmodified build baseline.

Acceptance criteria:
1. Record macOS, architecture, Xcode/clang, CMake, Qt, FFTW, and libusb versions.
2. Build unchanged application from the Patch 001 merged baseline.
3. Launch demo mode and record outcome.
4. Capture build warnings and packaging status.
5. Make no mixed-signal runtime changes.
