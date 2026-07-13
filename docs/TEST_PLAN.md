# Test Plan

## T0: Upstream build baseline
- Build unchanged source on macOS.
- Record hardware, macOS, Xcode/clang, CMake, Qt, FFTW, and libusb versions.
- Run demo mode and capture startup logs.

## T1: Original scope baseline
- Confirm CH1 and CH2 with the calibration output.
- Record sample rates, trigger modes, disconnect/reconnect behavior, and CPU load.

## T2: USB topology
- Capture `system_profiler`, `ioreg`, and libusb descriptor output before and after firmware upload.
- Identify hub and child-device paths.

## T3: Logic-analyzer baseline
- Verify all 16 channels with a known pattern source.
- Record supported rates, input thresholds, channel mapping, and decoder export.

## T4: Concurrent open and streaming
- Open both functions in one diagnostic process.
- Run fixed-duration captures at increasing rates.
- Count transfers, bytes, errors, timeouts, and dropped data.

## T5: Timeline alignment
- Feed one square wave to analog CH1 and digital D0.
- Measure start offset, edge jitter, and drift at multiple durations and sample rates.

## Acceptance for first mixed-signal prototype
- Existing scope behavior unchanged when MSO support is disabled.
- Analog and digital streams captured concurrently for 60 seconds.
- No unexplained USB resets.
- Timing uncertainty measured and displayed, not assumed.
