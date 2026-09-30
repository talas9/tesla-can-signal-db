---
layout: default
title: "VCLEFT_liftgateLeaderRequest (0x124) — Left body controller, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Left body controller message: liftgate leader request. Tesla Model Y CAN bus message VCLEFT_liftgateLeaderRequest (0x124) of Left body controller, firmware 2026.26.6.5, 11 signals (VCLEFT_liftgateRequestAction, VCLEFT_liftgateRequestTargetDuty, VCLEFT_liftgateRequestTargetAngle, VCLEFT_liftgateRequestTargetParam and 7 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_liftgateLeaderRequest (0x124) — Left body controller, Tesla Model Y 2026.26.6.5 VEH CAN

Left body controller message: liftgate leader request; frame length from the layout, not yet observed on a vehicle bus. This page documents the 11 signals of VCLEFT_liftgateLeaderRequest as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_liftgateLeaderRequest` |
| CAN id | 0x124 (292) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 11 |

## Signals of VCLEFT_liftgateLeaderRequest

Tesla Model Y CAN bus signals in `VCLEFT_liftgateLeaderRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_liftgateRequestAction` | Action of dual strut PLG requested by the leader | 0\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `LIFTGATE_POSITION_ACTION_IDLE`<br>1 = `LIFTGATE_POSITION_ACTION_FIXED_DUTY_OPEN`<br>2 = `LIFTGATE_POSITION_ACTION_FIXED_DUTY_CLOSE`<br>3 = `LIFTGATE_POSITION_ACTION_RAMPED_DUTY_EOT`<br>4 = `LIFTGATE_POSITION_ACTION_RAMPED_DUTY_LATCH_EXIT`<br>5 = `LIFTGATE_POSITION_ACTION_RAMPED_DUTY_OFF`<br>6 = `LIFTGATE_POSITION_ACTION_OPENING`<br>7 = `LIFTGATE_POSITION_ACTION_OPENING_INIT_VEL`<br>8 = `LIFTGATE_POSITION_ACTION_OPENING_WHOOSH`<br>9 = `LIFTGATE_POSITION_ACTION_PARTY_OPENING`<br>10 = `LIFTGATE_POSITION_ACTION_CLOSING`<br>11 = `LIFTGATE_POSITION_ACTION_CLOSING_WHOOSH`<br>12 = `LIFTGATE_POSITION_ACTION_UNCAL_CLOSE`<br>13 = `LIFTGATE_POSITION_ACTION_FACTORY_CLOSE`<br>14 = `LIFTGATE_POSITION_ACTION_UPDATE_PARAM_CLOSING_SPEED`<br>15 = `LIFTGATE_POSITION_ACTION_OPENING_BACKOFF`<br>16 = `LIFTGATE_POSITION_ACTION_FIXED_DUTY_LATCH_CURRENT`<br>17 = `LIFTGATE_POSITION_ACTION_FIXED_DUTY_LATCH_CURRENT_SCALED`<br>18 = `LIFTGATE_POSITION_ACTION_COUNT` | validated |
| `VCLEFT_liftgateRequestTargetDuty` | Left body controller: liftgate request target duty | 5\|8 | little-endian | signed | 1 | 0 | % | -100 to 100 |  | validated |
| `VCLEFT_liftgateRequestTargetAngle` | Left body controller: liftgate request target angle | 13\|10 | little-endian | signed | 0.2 | 0 | deg | -100 to 100 |  | validated |
| `VCLEFT_liftgateRequestTargetParam` | Left body controller: liftgate request target param | 23\|8 | little-endian | signed | 1 | 0 |  | -100 to 100 |  | validated |
| `VCLEFT_adaptiveLiftgateControlModeActive` | Indicates if adaptive liftgate control mode is active | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_liftgateReqObsDetMode` | Pinch mode requrest by the PLG leader | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `PLG_OBSTACLE_DETECT_MODE_INACTIVE`<br>1 = `PLG_OBSTACLE_DETECT_MODE_OPENING`<br>2 = `PLG_OBSTACLE_DETECT_MODE_CLOSING`<br>3 = `PLG_OBSTACLE_DETECT_MODE_LATCH_ENTRY`<br>4 = `PLG_OBSTACLE_DETECT_MODE_LATCH_EXIT`<br>5 = `PLG_OBSTACLE_DETECT_MODE_PARTY_CLOSE` | validated |
| `VCLEFT_liftgateReqResetStrutCount` | Set strut count reset request from the leader | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_liftgateReqClearCal` | Request follower strut ro clear it calibration | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_liftgateTargetTerminalSpeed` | Left body controller: liftgate target terminal speed | 40\|8 | little-endian | signed | 0.08 | 10 | deg/s | 0 to 20 |  | validated |
| `VCLEFT_liftgateReqCoastPercent` | Reports the percentage of time to coast the strut. | 48\|5 | little-endian | unsigned | 4 | 0 | % | 0 to 100 |  | validated |
| `VCLEFT_liftgateReqDutyScale` | Reports the amount to scale duty from current value to ramp to for a LATCH_CURRENT_SCALED request | 53\|8 | little-endian | unsigned | 0.0125 | 0 | - | 0 to 3.15 |  | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
