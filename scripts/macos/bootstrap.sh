#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Darwin" ]]; then
  echo "Error: this script is intended for macOS." >&2
  exit 1
fi

if ! command -v brew >/dev/null 2>&1; then
  echo "Error: Homebrew is required. Install it from https://brew.sh and rerun." >&2
  exit 1
fi

brew update
brew install qt@6 fftw libusb cmake binutils create-dmg

echo
echo "Installed