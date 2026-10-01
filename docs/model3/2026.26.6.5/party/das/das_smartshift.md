---
layout: default
title: "DAS_smartShift (0x12B) — Driver assistance computer, Tesla Model 3 2026.26.6.5 PARTY CAN"
description: "Driver assistance computer message: smart shift. Tesla Model 3 CAN bus message DAS_smartShift (0x12B) of Driver assistance computer, firmware 2026.26.6.5, 8 signals (DAS_smartShiftChecksum, DAS_smartShiftCounter, DAS_smartShiftTorqueDirection, DAS_smartShiftTorqueReason and 4 more). Bit layout, scaling, units and value tables."
---

# DAS_smartShift (0x12B) — Driver assistance computer, Tesla Model 3 2026.26.6.5 PARTY CAN

Driver assistance computer message: smart shift; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of DAS_smartShift as defined for Tesla Model 3 firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DAS_smartShift` |
| CAN id | 0x12B (299) |
| ECU | [Driver assistance computer](../../das.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | DAS |
| Frame length | 4 bytes |
| Cycle time | 100 ms |
| Signals | 8 |

## Signals of DAS_smartShift

Tesla Model 3 CAN bus signals in `DAS_smartShift`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DAS_smartShiftChecksum` | Driver assistance computer: smart shift checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `DAS_smartShiftCounter` | Driver assistance computer: smart shift counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `DAS_smartShiftTorqueDirection` | Reports Driver Assistance System (DAS) Smart Shift torque direction; raw 0 = signal not available (SNA) | 12\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `SUGGESTED_TORQUE_DIRECTION_SNA`<br>1 = `SUGGESTED_TORQUE_DIRECTION_NOT_CONFIDENT`<br>2 = `SUGGESTED_TORQUE_DIRECTION_REVERSE`<br>3 = `SUGGESTED_TORQUE_DIRECTION_FORWARD`<br>4 = `SUGGESTED_TORQUE_DIRECTION_NOT_READY` | plausible |
| `DAS_smartShiftTorqueReason` | Reports Driver Assistance System (DAS) Smart Shift torque direction reason; raw 0 = signal not available (SNA) | 15\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `SUGGESTED_TORQUE_REASON_SNA`<br>1 = `SUGGESTED_TORQUE_REASON_SMART_SHIFT_PLAN`<br>2 = `SUGGESTED_TORQUE_REASON_SMART_SUMMON_PLAN`<br>3 = `SUGGESTED_TORQUE_REASON_SMART_SUMMON_SHORT_PLAN`<br>4 = `SUGGESTED_TORQUE_REASON_ROAD_MARKING`<br>5 = `SUGGESTED_TORQUE_REASON_GATE`<br>6 = `SUGGESTED_TORQUE_REASON_CIPV`<br>7 = `SUGGESTED_TORQUE_REASON_PLL_TO_ROAD_1ST_SHFT`<br>8 = `SUGGESTED_TORQUE_REASON_PLL_TO_ROAD_SUBS_SHFT`<br>9 = `SUGGESTED_TORQUE_REASON_RETRACE`<br>10 = `SUGGESTED_TORQUE_REASON_CURB`<br>11 = `SUGGESTED_TORQUE_REASON_STATIC_OBSTACLE`<br>12 = `SUGGESTED_TORQUE_REASON_BLOCKING_VEHICLE`<br>13 = `SUGGESTED_TORQUE_REASON_PLL_PARKING`<br>14 = `SUGGESTED_TORQUE_REASON_PERP_PARKING`<br>15 = `SUGGESTED_TORQUE_REASON_FSD_E2E` | plausible |
| `DAS_autoshiftTorqueDirectionDbg` | Driver assistance computer: autoshift torque direction dbg; raw 0 = signal not available (SNA) | 19\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `SUGGESTED_TORQUE_DIRECTION_SNA`<br>1 = `SUGGESTED_TORQUE_DIRECTION_NOT_CONFIDENT`<br>2 = `SUGGESTED_TORQUE_DIRECTION_REVERSE`<br>3 = `SUGGESTED_TORQUE_DIRECTION_FORWARD`<br>4 = `SUGGESTED_TORQUE_DIRECTION_NOT_READY` | plausible |
| `DAS_autoshiftUpcomingDirection` | Reports the Driver Assistance System (DAS) upcoming torque direction; raw 3 = signal not available (SNA) | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `AUTOSHIFT_DIRECTION_NONE`<br>1 = `AUTOSHIFT_DIRECTION_REVERSE`<br>2 = `AUTOSHIFT_DIRECTION_DRIVE`<br>3 = `AUTOSHIFT_DIRECTION_SNA` | plausible |
| `DAS_autoshiftBrakeRequired` | Reports whether brake press is required for Autoshift Drive/Reverse (D/R). | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `DAS_autoshiftSteerRequest` | Reports the Driver Assistance System (DAS) steering angle direction requested for Autoshift Drive/Reverse (D/R). | 25\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `AUTOSHIFT_STEERING_DIRECTION_NONE`<br>1 = `AUTOSHIFT_STEERING_DIRECTION_ANY`<br>2 = `AUTOSHIFT_STEERING_DIRECTION_RIGHT`<br>3 = `AUTOSHIFT_STEERING_DIRECTION_LEFT` | plausible |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 PARTY DBC file](../../../../../dbc/Model3/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/PARTY.json)

## See also

- [All Driver assistance computer messages (DAS)](../../das.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
