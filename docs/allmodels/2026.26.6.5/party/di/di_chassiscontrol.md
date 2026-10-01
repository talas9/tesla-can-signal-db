---
layout: default
title: "DI_chassisControl (0x148) — Drive inverter, Tesla Model 3 / Model Y 2026.26.6.5 PARTY CAN"
description: "Drive inverter message: chassis control. Tesla Model 3 / Model Y CAN bus message DI_chassisControl (0x148) of Drive inverter, firmware 2026.26.6.5, 18 signals (DI_chassisControlChecksum, DI_chassisControlCounter, DI_imuOffsetLearnRequest, DI_brakeCommandType and 14 more). Bit layout, scaling, units and value tables."
---

# DI_chassisControl (0x148) — Drive inverter, Tesla Model 3 / Model Y 2026.26.6.5 PARTY CAN

Drive inverter message: chassis control; frame length from the layout, not yet observed on a vehicle bus. This page documents the 18 signals of DI_chassisControl as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DI_chassisControl` |
| CAN id | 0x148 (328) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | DI |
| Frame length | 8 bytes |
| Cycle time | 20 ms |
| Signals | 18 |

## Signals of DI_chassisControl

Tesla Model 3 / Model Y CAN bus signals in `DI_chassisControl`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_chassisControlChecksum` | Drive inverter: chassis control checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `DI_chassisControlCounter` | Drive inverter: chassis control counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `DI_imuOffsetLearnRequest` | Drive inverter: imu offset learn request | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IMU_OFFSET_LEARNING_OFF`<br>1 = `IMU_SLOW_LEARNING_DISTANCE`<br>2 = `IMU_FAST_LEARNING_TIME` | plausible |
| `DI_brakeCommandType` | Drive inverter: brake command type | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FAST`<br>1 = `QUIET` | plausible |
| `DI_brakeTorqueRequestActive` | Drive inverter: brake torque request active | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `INACTIVE`<br>1 = `ACTIVE` | plausible |
| `DI_brakeTorqueCommand` | Brake torque command to ESP | 16\|13 | little-endian | unsigned | 3 | 0 | Nm | 0 to 24573 |  | plausible |
| `DI_ptcStateGlobal` | Indicates state of Tesla traction control system; raw 3 = signal not available (SNA) | 29\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `GLOBAL_PTC_STATE_FAULTED`<br>1 = `GLOBAL_PTC_STATE_BACKUP`<br>2 = `GLOBAL_PTC_STATE_ON`<br>3 = `GLOBAL_PTC_STATE_SNA` | plausible |
| `DI_ptcActive` | TRUE when pedal-positive (drive) traction control is active | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `INACTIVE`<br>1 = `ACTIVE` | plausible |
| `DI_vdcState` | Status of VDC | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VDC_STATE_FAULTED`<br>1 = `VDC_STATE_BACKUP_A`<br>2 = `VDC_STATE_NORMAL`<br>3 = `VDC_STATE_STARTUP` | plausible |
| `DI_isAnyVdcControlActive` | Drive inverter: is any vdc control active | 34\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VDC_NO_CONTROL_ACTIVE`<br>1 = `VDC_CONTROL_ACTIVE`<br>2 = `UNUSED_VALUE` | plausible |
| `DI_vdcMode` | Indicates mode of VDC | 36\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VDC_MODE_OFF`<br>1 = `VDC_MODE_ON`<br>2 = `VDC_MODE_TRACK` | plausible |
| `DI_pedalAssistCurveSelect` | Drive inverter: pedal assist curve select | 38\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `PEDAL_ASSIST_CURVE_0`<br>3 = `PEDAL_ASSIST_CURVE_3`<br>6 = `PEDAL_ASSIST_CURVE_6`<br>8 = `PEDAL_ASSIST_CURVE_8`<br>11 = `PEDAL_ASSIST_CURVE_11`<br>12 = `PEDAL_ASSIST_CURVE_12`<br>15 = `PEDAL_ASSIST_CURVE_15` | plausible |
| `DI_isAnyTcActive` | TRUE when either drive or regen traction control is active | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `INACTIVE`<br>1 = `ACTIVE` | plausible |
| `DI_VehicleMuConfidence` | Confidence in surface mu estimate for development use only | 43\|6 | little-endian | unsigned | 0.02 | 0 | - | 0 to 1.26 |  | plausible |
| `DI_VehicleMu` | Learn-up estimate of surface mu for development use only | 49\|6 | little-endian | unsigned | 0.024 | 0 | - | 0 to 1.512 |  | plausible |
| `DI_trailerSwayIndex` | VDC trailer sway index | 55\|5 | little-endian | unsigned | 0.035 | 0 | - | 0 to 1 |  | plausible |
| `DI_vdcControlActive` | Type of VDC control while VDC is actuating | 60\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VDC_NOT_ACTIVE`<br>1 = `VDC_OVERSTEER_ACTIVE`<br>2 = `VDC_UNDERSTEER_ACTIVE`<br>3 = `VDC_TRAILER_SWAY_ACTIVE`<br>4 = `VDC_DECEL_ACTIVE` | plausible |
| `DI_treadDepthAlertSet` | Drive inverter: tread depth alert set | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FALSE`<br>1 = `TRUE` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 PARTY DBC file](../../../../../dbc/AllModels/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/PARTY.json)

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
