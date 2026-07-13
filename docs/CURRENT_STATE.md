# Current State

## Baseline
- Fork: `lillknurra/OpenHantek6022`
- Upstream: `OpenHantek/OpenHantek6022`
- Upstream baseline commit: `4abdcce9be1319bdc83d9ff1b2c96edfcbb22506`
- Working branch: `project/patch-001-governance-baseline`

## Verified
- The fork exists and is writable.
- Upstream supports Hantek 6022BE/BL oscilloscope operation.
- The project is GPL-3.0 licensed.

## Inferred
- Available schematic material appears to show separate analog and logic subsystems behind an internal USB hub.
- Concurrent capture may therefore be possible, but synchronization quality is unknown.

## Unknown
- Exact USB topology of the ordered physical unit.
- PCB revision and whether it matches the available schematic.
- Whether both FX2 devices enumerate simultaneously.
- Whether both streams can run concurrently without loss.
- Relative clock offset, jitter, and drift.

## Next patch
Patch 002: reproduce an unmodified macOS build and record toolchain, demo-mode, packaging, and warnings. No device is required.
