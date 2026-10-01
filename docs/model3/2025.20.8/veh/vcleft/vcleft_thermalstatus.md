---
layout: default
title: "VCLEFT_thermalStatus (0x182) — Left body controller, Tesla Model 3 2025.20.8 VEH CAN"
description: "Left body controller message: thermal status. Tesla Model 3 CAN bus message VCLEFT_thermalStatus (0x182) of Left body controller, firmware 2025.20.8, 8 signals (VCLEFT_hvac2RLeftLateralStatus, VCLEFT_hvac2RLeftVerticalStatus, VCLEFT_hvac2RRightLateralStatus, VCLEFT_hvac2RRightVerticalStatus and 4 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_thermalStatus (0x182) — Left body controller, Tesla Model 3 2025.20.8 VEH CAN

Left body controller message: thermal status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of VCLEFT_thermalStatus as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_thermalStatus` |
| CAN id | 0x182 (386) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 8 |

## Signals of VCLEFT_thermalStatus

Tesla Model 3 CAN bus signals in `VCLEFT_thermalStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_hvac2RLeftLateralStatus` | Left body controller: hvac2 r left lateral status | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_hvac2RLeftVerticalStatus` | Left body controller: hvac2 r left vertical status | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_hvac2RRightLateralStatus` | Left body controller: hvac2 r right lateral status | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_hvac2RRightVerticalStatus` | Left body controller: hvac2 r right vertical status | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCLEFT_hvac2RLeftLateralPosition` | Left body controller: hvac2 r left lateral position | 32\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | plausible |
| `VCLEFT_hvac2RLeftVerticalPosition` | Left body controller: hvac2 r left vertical position | 40\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | plausible |
| `VCLEFT_hvac2RRightLateralPosition` | Left body controller: hvac2 r right lateral position | 48\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | plausible |
| `VCLEFT_hvac2RRightVerticalPosition` | Left body controller: hvac2 r right vertical position | 56\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
