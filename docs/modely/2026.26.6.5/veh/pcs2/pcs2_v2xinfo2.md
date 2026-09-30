---
layout: default
title: "PCS2_v2xInfo2 (0x40F) — PCS2 ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "PCS2 ECU message: v2x info2. Tesla Model Y CAN bus message PCS2_v2xInfo2 (0x40F) of PCS2 ECU, firmware 2026.26.6.5, 3 signals (PCS2_v2xUserPower, PCS2_v2xDispatchableApparentPower, PCS2_v2xReadyApparentPower). Bit layout, scaling, units and value tables."
---

# PCS2_v2xInfo2 (0x40F) — PCS2 ECU, Tesla Model Y 2026.26.6.5 VEH CAN

PCS2 ECU message: v2x info2; frame length from the layout, not yet observed on a vehicle bus. This page documents the 3 signals of PCS2_v2xInfo2 as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PCS2_v2xInfo2` |
| CAN id | 0x40F (1039) |
| ECU | [PCS2 ECU](../../pcs2.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PCS2 |
| Frame length | 4 bytes |
| Cycle time | 100 ms |
| Signals | 3 |

## Signals of PCS2_v2xInfo2

Tesla Model Y CAN bus signals in `PCS2_v2xInfo2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PCS2_v2xUserPower` | Reports the present Power Conversion System 2 (PCS2) Vehicle-to-Everything (V2X) user-requested Alternating Current (AC) real power (positive polarity is battery discharging). | 0\|10 | little-endian | signed | 0.05 | 0 | kW | -20 to 20 |  | validated |
| `PCS2_v2xDispatchableApparentPower` | Reports the maximum apparent power Power Conversion System 2 (PCS2) is currently capable of for Vehicle-to-Everything (V2X) operations | 10\|9 | little-endian | unsigned | 0.05 | 0 | kVA | 0 to 20 |  | validated |
| `PCS2_v2xReadyApparentPower` | Reports the maximum apparent power Power Conversion System 2 (PCS2) is capable of for Vehicle-to-Everything (V2X) operations under nominal grid conditions | 19\|9 | little-endian | unsigned | 0.05 | 0 | kVA | 0 to 20 |  | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All PCS2 ECU messages (PCS2)](../../pcs2.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
