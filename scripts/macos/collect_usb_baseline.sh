#!/usr/bin/env bash
set -euo pipefail

OUT_DIR="${1:-usb-baseline-$(date +%Y%m%d-%H%M%S)}"
mkdir -p "$OUT_DIR"

{
  echo "timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "host=$(hostname)"
  echo "arch=$(uname -m)"
  echo "kernel=$(uname -a)"
  echo "sw_vers_product=$(sw_vers -productVersion 2>/dev/null || true)"
} > "$OUT_DIR/environment.txt"

system_profiler SPUSBDataType > "$OUT_DIR/system_profiler_SPUSBDataType.txt" 2>&1 || true
ioreg -p IOUSB -l -w 0 > "$OUT_DIR/ioreg_IOUSB.txt" 2>&1 || true

if command -v python3 >/dev/null 2>&1; then
  python3 - <<'PY' > "$OUT_DIR/python_usb_note.txt"
print("Optional next step: add a libusb-based descriptor dumper after the macOS build baseline is established.")
PY
fi

cat > "$OUT_DIR/README.txt" <<'EOF'
USB baseline capture complete.

Run this script in each relevant state and rename the output directories clearly:
- device-unplugged
- device-original-firmware
- scope-firmware-loaded
- logic-firmware-loaded
- attempted-parallel-operation

Do not edit raw capture files. Add interpretation separately.
EOF

printf 'Wrote USB baseline to %s\n' "$OUT_DIR"
