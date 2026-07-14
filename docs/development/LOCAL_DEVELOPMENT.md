# Local Development

## Repository location

Recommended local checkout:

```bash
mkdir -p ~/GitHub
cd ~/GitHub
git clone git@github.com:lillknurra/OpenHantek6022.git
cd OpenHantek6022
```

## Before each patch

Run from the repository root:

```bash
printf '\n=== STATUS ===\n'
git status -sb

printf '\n=== BRANCH ===\n'
git branch --show-current

printf '\n=== LAST COMMITS ===\n'
git log --oneline --decorate -5
```

Do not start implementation from a dirty working tree unless the pending changes are explicitly part of the patch.

## macOS prerequisites

Install the baseline toolchain with:

```bash
./scripts/macos/bootstrap.sh
```

The current Apple Silicon baseline uses Homebrew packages for Qt 6, FFTW, libusb, CMake, binutils, and create-dmg. Full Xcode is not currently required for the verified Debug build; Apple Command Line Tools were sufficient.

## Local build policy

- Build from a clean or deliberately reused build directory.
- Capture CMake and compiler output with `tee` when the result will become patch evidence.
- A successful build proves only buildability. It does not prove device operation, firmware behavior, acquisition accuracy, or mixed-signal synchronization.
- Do not commit generated build directories, local logs, app bundles, or DMG files unless a patch explicitly requires an artifact.

## Current verified build command

```bash
rm -rf build
mkdir build
cd build

cmake .. \
  -DCMAKE_BUILD_TYPE=Debug \
  -DCMAKE_PREFIX_PATH="$(brew --prefix qt@6)" \
  2>&1 | tee cmake-output.log

cmake --build . \
  --parallel "$(sysctl -n hw.ncpu)" \
  2>&1 | tee build-output.log
```

Expected build artifact:

```text
build/openhantek/OpenHantek.app
```

## Demo launch

```bash
open build/openhantek/OpenHantek.app --args --demoMode
```

Visual confirmation from the running application is required before demo mode is marked PASS.
