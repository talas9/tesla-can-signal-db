---
layout: default
title: "DI_systemStatus (0x118) — Drive inverter, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Drive inverter message: system status. Tesla Model 3 / Model Y CAN bus message DI_systemStatus (0x118) of Drive inverter, firmware 2026.26.6.5, 21 signals (DI_systemStatusChecksum, DI_systemStatusCounter, DI_secondaryGearControlStatus, DI_immobilizerState and 17 more). Bit layout, scaling, units and value tables."
---

# DI_systemStatus (0x118) — Drive inverter, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Drive inverter message: system status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 21 signals of DI_systemStatus as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DI_systemStatus` |
| CAN id | 0x118 (280) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | DI |
| Frame length | 8 bytes |
| Cycle time | 10 ms |
| Signals | 21 |

## Signals of DI_systemStatus

Tesla Model 3 / Model Y CAN bus signals in `DI_systemStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_systemStatusChecksum` | Drive inverter: system status checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `DI_systemStatusCounter` | Drive inverter: system status counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `DI_secondaryGearControlStatus` | Indicates if gear control through PRND is being honored | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | validated |
| `DI_immobilizerState` | Detects state of the Drive Inverter (DI) immobilizer; raw 0 = signal not available (SNA) | 13\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `DI_IMM_STATE_INIT_SNA`<br>1 = `DI_IMM_STATE_REQUEST`<br>2 = `DI_IMM_STATE_AUTHENTICATING`<br>3 = `DI_IMM_STATE_DISARMED`<br>4 = `DI_IMM_STATE_IDLE`<br>5 = `DI_IMM_STATE_RESET`<br>6 = `DI_IMM_STATE_FAULT` | validated |
| `DI_systemState` | DI system state machine state. | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DI_SYS_UNAVAILABLE`<br>1 = `DI_SYS_IDLE`<br>2 = `DI_SYS_STANDBY`<br>3 = `DI_SYS_FAULT`<br>4 = `DI_SYS_ABORT`<br>5 = `DI_SYS_ENABLE` | validated |
| `DI_brakePedalState` | Brake pedal switch signal sensed at the drive inverter. | 19\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `ON`<br>2 = `INVALID` | validated |
| `DI_gear` | Detects the current operating gear reported by the drive inverter; raw 7 = signal not available (SNA) | 21\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `DI_GEAR_INVALID`<br>1 = `DI_GEAR_P`<br>2 = `DI_GEAR_R`<br>3 = `DI_GEAR_N`<br>4 = `DI_GEAR_D`<br>7 = `DI_GEAR_SNA` | validated |
| `DI_driveBlocked` | Reason drive unit is blocked from entering enable | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DRIVE_BLOCKED_NONE`<br>1 = `DRIVE_BLOCKED_FRUNK`<br>2 = `DRIVE_BLOCKED_PROX`<br>3 = `DRIVE_BLOCKED_FALCON`<br>4 = `DRIVE_BLOCKED_TRUNK` | validated |
| `DI_hvilSystemStatus` | Aggregated HVIL system status; raw 3 = signal not available (SNA) | 27\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `DISABLED`<br>1 = `OPEN`<br>2 = `CLOSED`<br>3 = `SNA` | validated |
| `DI_driveModeState` | System drive mode state | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DM_STATE_NONDRIVE`<br>1 = `DM_STATE_DRIVE` | validated |
| `DI_shiftRequestType` | Type of most recent shift request | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `GTW_SHIFT`<br>2 = `CCCM_SHIFT`<br>3 = `SMART_SHIFT` | validated |
| `DI_accelPedalPos` | Drive Inverter measured accelerator pedal position; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 | 255 = `SNA` | validated |
| `DI_tractionControlMode` | Active traction control mode as requested by the driver. | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `TC_NORMAL`<br>1 = `TC_SLIP_START`<br>2 = `TC_DEV_MODE_1`<br>3 = `TC_DEV_MODE_2`<br>4 = `TC_ROLLS_MODE`<br>5 = `TC_DYNO_MODE`<br>6 = `TC_OFFROAD_ASSIST`<br>7 = `TC_SLIPPERY_SURFACE` | validated |
| `DI_dynoModeAvailable` | Reports to the vehicle if the Drive Inverter (DI) will accept a request to enter dyno mode. | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_epbRequest` | Reports Electronic Parking Brake (EPB) requests. | 44\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DI_EPBREQUEST_NO_REQUEST`<br>1 = `DI_EPBREQUEST_PARK`<br>2 = `DI_EPBREQUEST_UNPARK` | validated |
| `DI_brakeSource` | Drive inverter: brake source | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DAS`<br>1 = `DI` | validated |
| `DI_keepDrivePowerStateRequest` | Reports that the Drive Inverter (DI) expects vehicle power state to remain in drive. | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NO_REQUEST`<br>1 = `KEEP_ALIVE` | validated |
| `DI_trackModeState` | Indicates state of Track mode | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TRACK_MODE_UNAVAILABLE`<br>1 = `TRACK_MODE_AVAILABLE`<br>2 = `TRACK_MODE_ON` | validated |
| `DI_autonomyControlActive` | Drive inverter: autonomy control active | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_regenLight` | Drive inverter: regen light | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_vehicleAcceleration` | Drive inverter: vehicle acceleration; raw 2048 = signal not available (SNA) | 52\|12 | little-endian | signed | 0.01 | 0 | m/s^2 | -20.47 to 20.47 | -2048 = `SNA` | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
