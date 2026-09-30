---
layout: default
title: "PM_locState (0x1E5) — PM ECU, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "PM ECU message: loc state. Tesla Model 3 CAN bus message PM_locState (0x1E5) of PM ECU, firmware 2026.26.6.5, 18 signals (PM_cruiseFaultRequest, PM_shiftState, PM_cruiseState, PM_vehicleHoldRequest and 14 more). Bit layout, scaling, units and value tables."
---

# PM_locState (0x1E5) — PM ECU, Tesla Model 3 2026.26.6.5 VEH CAN

PM ECU message: loc state; frame length from the layout, not yet observed on a vehicle bus. This page documents the 18 signals of PM_locState as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PM_locState` |
| CAN id | 0x1E5 (485) |
| ECU | [PM ECU](../../pm.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PM |
| Frame length | 8 bytes |
| Cycle time | 10 ms |
| Signals | 18 |

## Signals of PM_locState

Tesla Model 3 CAN bus signals in `PM_locState`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PM_cruiseFaultRequest` | PM ECU: cruise fault request | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PM_shiftState` | PM ECU: shift state; raw 7 = signal not available (SNA) | 1\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `DI_GEAR_INVALID`<br>1 = `DI_GEAR_P`<br>2 = `DI_GEAR_R`<br>3 = `DI_GEAR_N`<br>4 = `DI_GEAR_D`<br>7 = `DI_GEAR_SNA` | validated |
| `PM_cruiseState` | PM ECU: cruise state | 4\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CRS_STATE_UNAVAILABLE`<br>1 = `CRS_STATE_STANDBY`<br>2 = `CRS_STATE_ENABLED`<br>3 = `CRS_STATE_STANDSTILL`<br>4 = `CRS_STATE_OVERRIDE`<br>5 = `CRS_STATE_FAULT`<br>6 = `CRS_STATE_PRE_FAULT`<br>7 = `CRS_STATE_PRE_CANCEL` | validated |
| `PM_vehicleHoldRequest` | PM ECU: vehicle hold request | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PM_NO_VHLD_REQUEST`<br>1 = `PM_VHLD_OFF_REQUEST` | validated |
| `PM_aebRequest` | PM ECU: aeb request | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PM_NO_AEB_REQUEST`<br>1 = `PM_AEB_OFF_REQUEST` | validated |
| `PM_torqueCmdState` | PM ECU: torque cmd state; raw 0 = signal not available (SNA) | 9\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `TorqueCmd_SNA`<br>6 = `TorqueCmd_Valid`<br>8 = `TorqueCmd_Invalid` | validated |
| `PM_btcCmdState` | PM ECU: btc cmd state | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `BTC_CMD_INVALID`<br>1 = `BTC_CMD_VALID` | validated |
| `PM_unparkAllowed` | PM ECU: unpark allowed | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PM_stationaryMode` | PM ECU: stationary mode | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PM_onePedalFaultRequest` | PM ECU: one pedal fault request | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PM_backfillDisableRequest` | PM ECU: backfill disable request | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PM_autoparkState` | PM ECU: autopark state; raw 15 = signal not available (SNA) | 18\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `DI_APC_UNAVAILABLE`<br>1 = `DI_APC_STANDBY`<br>2 = `DI_APC_STARTED`<br>3 = `DI_APC_ACTIVE`<br>4 = `DI_APC_COMPLETE`<br>5 = `DI_APC_PAUSED`<br>6 = `DI_APC_ABORTED`<br>7 = `DI_APC_RESUMED`<br>8 = `DI_APC_UNPARK_COMPLETE`<br>9 = `DI_APC_SELFPARK_STARTED`<br>15 = `DI_APC_SNA` | validated |
| `PM_regenBlendCmdQF` | PM ECU: regen blend cmd QF | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `BRAKE_COMMAND_INVALID`<br>1 = `BRAKE_COMMAND_VALID` | validated |
| `PM_brakePedalCmdQF` | PM ECU: brake pedal cmd QF | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `BRAKE_COMMAND_INVALID`<br>1 = `BRAKE_COMMAND_VALID` | validated |
| `PM_latentFaultCheckIntResponse` | PM ECU: latent fault check int response | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `PM_hvilSystemStatus` | HVIL system status; raw 3 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `DISABLED`<br>1 = `OPEN`<br>2 = `CLOSED`<br>3 = `SNA` | validated |
| `PM_locStateCounter` | PM ECU: loc state counter | 53\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | validated |
| `PM_locStateChecksum` | PM ECU: loc state checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All PM ECU messages (PM)](../../pm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
