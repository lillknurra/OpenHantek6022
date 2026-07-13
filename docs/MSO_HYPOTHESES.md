# MSO Hypotheses

## H1: Concurrent unsynchronized capture is possible
The analog and digital subsystems can enumerate, open, and stream simultaneously through the internal USB hub.

**Pass:** both streams run concurrently with bounded loss.
**Fail:** hardware, firmware, or USB topology permits only one active function.

## H2: Software alignment is sufficient for short captures
A common signal connected to analog CH1 and digital D0 can align independently captured streams with useful repeatability.

**Measure:** start offset, edge jitter, sampling-rate error, and drift over capture duration.

## H3: Clock drift can be corrected
Two or more common reference edges permit affine correction of the digital timeline against the analog timeline.

## H4: Hardware synchronization is possible
A shared trigger, GPIO, or reference-clock modification can reduce uncertainty beyond software alignment.

## Definition of MSO
The project will distinguish:
- concurrent display;
- software-aligned mixed-signal capture;
- hardware-triggered capture;
- genuinely clock-synchronous capture.

The user interface must state which level is active and its measured timing uncertainty.
