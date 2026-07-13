# Engineering Method

## Evidence levels
- **Verified:** reproduced by measurement, source inspection, or captured USB data.
- **Inferred:** supported by evidence but not yet directly measured.
- **Unknown:** unresolved and explicitly tracked.

## Experiment record
Every hardware or USB experiment records:
- device and PCB revision;
- host model and OS version;
- software commit and firmware image;
- wiring and signal source;
- exact commands;
- raw output or capture files;
- conclusion and confidence.

## Change discipline
1. Freeze and identify the baseline.
2. Define one falsifiable question.
3. Add the smallest diagnostic needed.
4. Capture raw evidence before interpretation.
5. Update `CURRENT_STATE.md` and relevant technical documents.
6. Keep experimental code behind an explicit build or runtime option until stable.

## Upstream compatibility
General fixes should remain independently reviewable. Experimental mixed-signal work must not regress ordinary 6022BE/BL oscilloscope operation.
