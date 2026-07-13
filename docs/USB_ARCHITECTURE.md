# USB Architecture

## Known upstream scope transport
OpenHantek6022 uses libusb and open FX2 firmware for ordinary 6022BE/BL oscilloscope acquisition.

## Working 6022BL hypothesis
The available schematic appears to show an internal hub with separate analog-scope and logic-analyzer USB functions. This must be verified from descriptors on the physical unit.

## Required descriptor inventory
Capture for every visible USB node:
- vendor and product ID;
- manufacturer, product, and serial strings;
- parent hub and port path;
- configurations and interfaces;
- alternate settings;
- endpoint address, direction, type, and packet size;
- state before and after firmware upload.

## Concurrency questions
1. Are two child devices present at the same time?
2. Can both be claimed by libusb concurrently?
3. Does firmware upload to one reset or detach the other?
4. Can both IN streams run without packet loss?
5. Is there a shared hardware trigger or clock path?

No answer is considered verified until raw descriptor and capture logs are stored.
