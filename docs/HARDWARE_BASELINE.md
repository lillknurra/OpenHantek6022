# Hardware Baseline

## Target device
Hantek 6022BL: two analog oscilloscope channels and a nominal 16-channel logic-analyzer function.

## Source-derived working model
The available schematic and PCB material suggest:
- a dual 8-bit ADC and analog front ends for CH1/CH2;
- an FX2-class USB controller for oscilloscope acquisition;
- a separate digital-input section and likely separate FX2-class controller;
- an internal USB hub joining both subsystems to one external USB cable.

This model is **inferred**, not yet verified on the ordered unit.

## Physical inspection checklist
When the device arrives, record before modification:
- enclosure and serial labels;
- PCB revision and both PCB sides;
- all major IC markings;
- USB hub and controller markings;
- connector pin numbering;
- continuity checks only after photographs and baseline functional tests.

## Safety boundary
The BNC grounds are USB/host referenced. Do not connect the instrument directly to mains-primary circuitry, non-isolated switch-mode power supplies, or other hazardous floating nodes.
