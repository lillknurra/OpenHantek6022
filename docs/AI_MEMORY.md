# AI Memory

## Project identity
- Fork: `lillknurra/OpenHantek6022`
- Upstream: `OpenHantek/OpenHantek6022`
- Primary target: Hantek 6022BL on macOS, including Apple Silicon.
- Long-term research goal: determine whether simultaneous analog and 16-channel digital acquisition can be implemented and synchronized.

## Known baseline
- Upstream baseline commit for Patch 001: `4abdcce9be1319bdc83d9ff1b2c96edfcbb22506`.
- Upstream actively supports the oscilloscope portion of 6022BE/BL.
- The separate `Ho-Ro/Hantek6022API` project contains open FX2 firmware for 6022BE and 6022BL.
- Available schematic material appears to show separate analog and logic acquisition subsystems behind an internal USB hub. This remains to be verified against the purchased unit.

## User environment
- User: Petter (`lillknurra`).
- Primary development computer: MacBook, macOS.
- Ordered hardware: Hantek 6022BL.
- Multimeter: UNI-T UT161D.
- Related embedded work includes ESP32-S3, SPI sensors, PDM microphones, and PCB diagnostics.

## Non-negotiable method
- Never present hypotheses as verified facts.
- Preserve upstream history and GPL-3.0 obligations.
- Baseline first, runtime changes later.
- Keep patches small and documented.
- Do not perform mains-referenced measurements with this USB oscilloscope.

## Immediate next work
Patch 002 should reproduce the unmodified macOS build, record the toolchain, run demo mode, and capture warnings before any runtime modification.
