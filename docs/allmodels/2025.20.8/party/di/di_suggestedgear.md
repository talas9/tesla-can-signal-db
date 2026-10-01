---
layout: default
title: "DI_suggestedGear (0x255) — Drive inverter, Tesla Model 3 / Model Y 2025.20.8 PARTY CAN"
description: "Drive inverter message: suggested gear. Tesla Model 3 / Model Y CAN bus message DI_suggestedGear (0x255) of Drive inverter, firmware 2025.20.8, 10 signals (DI_lastQualifiedGear, DI_lastDrivingGear, DI_distDrivenInGear, DI_frontBlocked and 6 more). Bit layout, scaling, units and value tables."
---

# DI_suggestedGear (0x255) — Drive inverter, Tesla Model 3 / Model Y 2025.20.8 PARTY CAN

Drive inverter message: suggested gear; frame length from the layout, not yet observed on a vehicle bus. This page documents the 10 signals of DI_suggestedGear as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DI_suggestedGear` |
| CAN id | 0x255 (597) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | DI |
| Frame length | 4 bytes |
| Cycle time | 100 ms |
| Signals | 10 |

## Signals of DI_suggestedGear

Tesla Model 3 / Model Y CAN bus signals in `DI_suggestedGear`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_lastQualifiedGear` | Drive inverter: last qualified gear; raw 7 = signal not available (SNA) | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `DI_GEAR_INVALID`<br>1 = `DI_GEAR_P`<br>2 = `DI_GEAR_R`<br>3 = `DI_GEAR_N`<br>4 = `DI_GEAR_D`<br>7 = `DI_GEAR_SNA` | plausible |
| `DI_lastDrivingGear` | Drive inverter: last driving gear; raw 7 = signal not available (SNA) | 3\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `DI_GEAR_INVALID`<br>1 = `DI_GEAR_P`<br>2 = `DI_GEAR_R`<br>3 = `DI_GEAR_N`<br>4 = `DI_GEAR_D`<br>7 = `DI_GEAR_SNA` | plausible |
| `DI_distDrivenInGear` | Drive inverter: dist driven in gear | 8\|8 | little-endian | unsigned | 0.0235294122249 | 0 | m | 0 to 6 |  | plausible |
| `DI_frontBlocked` | Drive inverter: front blocked | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_rearBlocked` | Drive inverter: rear blocked | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_firstShiftOccurred` | Drive inverter: first shift occurred | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_suggestedGearReason` | Reason for the suggested gear | 19\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `REASON_RETRACE`<br>1 = `REASON_1ST_SHFT_PAR_PARK`<br>2 = `REASON_1ST_SHFT_FR_BLCK`<br>3 = `REASON_1ST_SHFT_RE_BLCK`<br>4 = `REASON_1ST_SHFT_FR_BLCK_PAR_PARK`<br>5 = `REASON_SUB_SHFT_RE_BLCK`<br>6 = `REASON_SUB_SHFT_RE_BLCK_PAR_PARK`<br>7 = `REASON_SUB_SHFT_PAR_PARK`<br>8 = `REASON_SUB_SHFT`<br>9 = `REASON_AP`<br>10 = `REASON_AP_NOT_CONFIDENT`<br>11 = `REASON_AP_MIA`<br>12 = `REASON_EEPROM`<br>13 = `REASON_AP_NOT_READY`<br>14 = `REASON_1ST_SHFT_PAR_PARK_NO_USS` | plausible |
| `DI_parallelParked` | Drive inverter: parallel parked | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_smartShiftGear` | Gear vehicle will shift into if smart shift occurs | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `DRIVE`<br>2 = `REVERSE` | plausible |
| `DI_smartShiftUnavailableReason` | Reports the reason why Smart Shift is unavailable; raw 0 = signal not available (SNA) | 26\|5 | little-endian | unsigned | 1 | 0 |  | 1 to 31 | 0 = `SMART_SHIFT_UNAVAILABLE_SNA`<br>1 = `SMART_SHIFT_UNAVAILABLE_NONE`<br>2 = `SMART_SHIFT_SILENT_UNAVAILABLE_UI_DISABLE`<br>3 = `SMART_SHIFT_SILENT_UNAVAILABLE_NON_STANDARD_MODE`<br>4 = `SMART_SHIFT_SILENT_UNAVAILABLE_DRIVER_BUCKLED_QF`<br>5 = `SMART_SHIFT_SILENT_UNAVAILABLE_CHARGE_CABLE_CONNECTED`<br>6 = `SMART_SHIFT_SILENT_UNAVAILABLE_CLOSURE_OPEN`<br>7 = `SMART_SHIFT_SILENT_UNAVAILABLE_SGS_ACTIVE`<br>8 = `SMART_SHIFT_SILENT_UNAVAILABLE_GTW_NOT_QUALIFIED`<br>9 = `SMART_SHIFT_SILENT_UNAVAILABLE_CRUISE_REGULATING`<br>10 = `SMART_SHIFT_SILENT_UNAVAILABLE_AEB_ACTIVE`<br>11 = `SMART_SHIFT_UNAVAILABLE_IBST_MIA`<br>12 = `SMART_SHIFT_UNAVAILABLE_BLS_UNKNOWN`<br>13 = `SMART_SHIFT_UNAVAILABLE_OPD_UNAVAILABLE`<br>14 = `SMART_SHIFT_UNAVAILABLE_VHLD_UNAVAILABLE`<br>15 = `SMART_SHIFT_UNAVAILABLE_VDC_UNAVAILABLE`<br>16 = `SMART_SHIFT_UNAVAILABLE_DISPLAY_ERROR`<br>17 = `SMART_SHIFT_UNAVAILABLE_DAS_NOT_CONFIDENT`<br>18 = `SMART_SHIFT_UNAVAILABLE_DAS_MIA` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 PARTY DBC file](../../../../../dbc/AllModels/2025.20.8/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/PARTY.json)

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
