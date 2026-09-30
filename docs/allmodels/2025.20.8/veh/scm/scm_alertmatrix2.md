---
layout: default
title: "SCM_alertMatrix2 (0x54B) — SCM ECU, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "SCM ECU message: alert matrix2. Tesla Model 3 / Model Y CAN bus message SCM_alertMatrix2 (0x54B) of SCM ECU, firmware 2025.20.8, 4 signals (SCM_a074_isoVDiffHi, SCM_a076_bmsMIA, SCM_a078_voltageMatchTimeout, SCM_a091_voltageRiseDetection). Bit layout, scaling, units and value tables."
---

# SCM_alertMatrix2 (0x54B) — SCM ECU, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

SCM ECU message: alert matrix2; frame length from the layout, not yet observed on a vehicle bus. This page documents the 4 signals of SCM_alertMatrix2 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `SCM_alertMatrix2` |
| CAN id | 0x54B (1355) |
| ECU | [SCM ECU](../../scm.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | SCM |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 4 |

## Signals of SCM_alertMatrix2

Tesla Model 3 / Model Y CAN bus signals in `SCM_alertMatrix2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `SCM_a074_isoVDiffHi` | SCM ECU: a074 iso v diff hi | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCM_a076_bmsMIA` | SCM ECU: a076 bms MIA | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCM_a078_voltageMatchTimeout` | SCM ECU: a078 voltage match timeout | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCM_a091_voltageRiseDetection` | SCM ECU: a091 voltage rise detection | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All SCM ECU messages (SCM)](../../scm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
