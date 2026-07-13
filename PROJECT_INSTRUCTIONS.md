# Project Instructions

## Objective
Determine whether Hantek 6022BL can support simultaneous analog and 16-channel digital acquisition, then implement the safest maintainable solution supported by measurements.

## Patch workflow
Each patch must include:
- purpose and non-goals;
- affected files;
- test procedure and captured evidence;
- result classified as pass, fail, or inconclusive;
- documentation update;
- rollback method.

## Branch policy
- `main`: upstream-tracking only.
- `project/patch-*`: governance, documentation, baseline, and integration patches.
- `feature/*`: isolated technical experiments.

## Initial phase gates
1. Build unmodified upstream on macOS.
2. Verify demo mode.
3. Verify ordinary 6022BL scope operation.
4. Inventory the internal USB topology.
5. Test logic-analyzer operation separately.
6. Prove or disprove that both USB functions can be opened concurrently.
7. Only then design a unified capture API and timeline.

## Safety
The 6022BL has USB-referenced grounds and is not an isolated mains oscilloscope. Project testing is limited to SELV/low-voltage circuits unless an appropriately rated isolated measurement method is reviewed and documented first.
