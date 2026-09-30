---
layout: default
title: "TAS_dampingStates (0x576) — Air suspension controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Air suspension controller message: damping states. Tesla Model 3 / Model Y CAN bus message TAS_dampingStates (0x576) of Air suspension controller, firmware 2025.20.8, 23 signals (TAS_endstopState, TAS_continuousControlState, TAS_activeTireTune, TAS_roughnessRaiseReason and 19 more). Bit layout, scaling, units and value tables."
---

# TAS_dampingStates (0x576) — Air suspension controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Air suspension controller message: damping states; frame length from the layout, not yet observed on a vehicle bus. This page documents the 23 signals of TAS_dampingStates as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `TAS_dampingStates` |
| CAN id | 0x576 (1398) |
| ECU | [Air suspension controller](../../tas.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | TAS |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 23 |

## Signals of TAS_dampingStates

Tesla Model 3 / Model Y CAN bus signals in `TAS_dampingStates`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `TAS_endstopState` | Air suspension controller: endstop state | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TAS_DAMPING_STATE_STANDBY`<br>1 = `TAS_DAMPING_STATE_ACTIVE` | validated |
| `TAS_continuousControlState` | SW-237496 | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TAS_DAMPING_STATE_STANDBY`<br>1 = `TAS_DAMPING_STATE_ACTIVE` | validated |
| `TAS_activeTireTune` | Air suspension controller: active tire tune | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TAS_TIRE_TUNE_DEFAULT`<br>1 = `TAS_TIRE_TUNE_MICHELIN_SUMMER_21` | validated |
| `TAS_roughnessRaiseReason` | Air suspension controller: roughness raise reason | 3\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TAS_ROUGHNESS_RAISE_REASON_NONE`<br>1 = `TAS_ROUGHNESS_RAISE_REASON_LEGACY`<br>2 = `TAS_ROUGHNESS_RAISE_REASON_LOOKAHEAD` | validated |
| `TAS_frontMetricDrivesRear` | Air suspension controller: front metric drives rear | 5\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TAS_ACTION_DISABLED`<br>1 = `TAS_ACTION_STANDBY`<br>2 = `TAS_ACTION_ARMED`<br>3 = `TAS_ACTION_ACTIVE` | validated |
| `TAS_roadCondition` | Air suspension controller: road condition; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.005 | 0 | - | 0 to 1.27 | 255 = `SNA` | validated |
| `TAS_bellyProtect` | Air suspension controller: belly protect | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TAS_ACTION_DISABLED`<br>1 = `TAS_ACTION_STANDBY`<br>2 = `TAS_ACTION_ARMED`<br>3 = `TAS_ACTION_ACTIVE` | validated |
| `TAS_frontMetricDrivesFront` | Air suspension controller: front metric drives front | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TAS_ACTION_DISABLED`<br>1 = `TAS_ACTION_STANDBY`<br>2 = `TAS_ACTION_ARMED`<br>3 = `TAS_ACTION_ACTIVE` | validated |
| `TAS_speedBumpAxleFront` | Air suspension controller: speed bump axle front | 20\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `TAS_ACTION_DISABLED`<br>1 = `TAS_ACTION_STANDBY`<br>2 = `TAS_ACTION_ARMED`<br>3 = `TAS_ACTION_ACTIVE`<br>4 = `TAS_ACTION_CANCELED` | validated |
| `TAS_speedBumpAxleRear` | Air suspension controller: speed bump axle rear | 23\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `TAS_ACTION_DISABLED`<br>1 = `TAS_ACTION_STANDBY`<br>2 = `TAS_ACTION_ARMED`<br>3 = `TAS_ACTION_ACTIVE`<br>4 = `TAS_ACTION_CANCELED` | validated |
| `TAS_holeProtectFL` | Air suspension controller: hole protect FL | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TAS_ACTION_DISABLED`<br>1 = `TAS_ACTION_STANDBY`<br>2 = `TAS_ACTION_ARMED`<br>3 = `TAS_ACTION_ACTIVE` | validated |
| `TAS_holeProtectFR` | Air suspension controller: hole protect FR | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TAS_ACTION_DISABLED`<br>1 = `TAS_ACTION_STANDBY`<br>2 = `TAS_ACTION_ARMED`<br>3 = `TAS_ACTION_ACTIVE` | validated |
| `TAS_holeProtectRL` | Air suspension controller: hole protect RL | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TAS_ACTION_DISABLED`<br>1 = `TAS_ACTION_STANDBY`<br>2 = `TAS_ACTION_ARMED`<br>3 = `TAS_ACTION_ACTIVE` | validated |
| `TAS_holeProtectRR` | Air suspension controller: hole protect RR | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TAS_ACTION_DISABLED`<br>1 = `TAS_ACTION_STANDBY`<br>2 = `TAS_ACTION_ARMED`<br>3 = `TAS_ACTION_ACTIVE` | validated |
| `TAS_stepProtectFL` | Air suspension controller: step protect FL | 34\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TAS_ACTION_DISABLED`<br>1 = `TAS_ACTION_STANDBY`<br>2 = `TAS_ACTION_ARMED`<br>3 = `TAS_ACTION_ACTIVE` | validated |
| `TAS_stepProtectFR` | Air suspension controller: step protect FR | 36\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TAS_ACTION_DISABLED`<br>1 = `TAS_ACTION_STANDBY`<br>2 = `TAS_ACTION_ARMED`<br>3 = `TAS_ACTION_ACTIVE` | validated |
| `TAS_stepProtectRL` | Air suspension controller: step protect RL | 38\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TAS_ACTION_DISABLED`<br>1 = `TAS_ACTION_STANDBY`<br>2 = `TAS_ACTION_ARMED`<br>3 = `TAS_ACTION_ACTIVE` | validated |
| `TAS_stepProtectRR` | Air suspension controller: step protect RR | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TAS_ACTION_DISABLED`<br>1 = `TAS_ACTION_STANDBY`<br>2 = `TAS_ACTION_ARMED`<br>3 = `TAS_ACTION_ACTIVE` | validated |
| `TAS_FDUTorqueCorruptionScale` | Air suspension controller: FDU torque corruption scale; raw 15 = signal not available (SNA) | 42\|4 | little-endian | unsigned | 0.075 | 0 | - | 0 to 1.05 | 15 = `SNA` | validated |
| `TAS_sprungMassEstimate` | Air suspension controller: sprung mass estimate; raw 31 = signal not available (SNA) | 46\|5 | little-endian | unsigned | 64 | 1800 | kg | 1800 to 3720 | 31 = `SNA` | validated |
| `TAS_anyDamperActive` | Air suspension controller: any damper active | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TAS_dampingStatesCounter` | Air suspension controller: damping states counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `TAS_dampingStatesChecksum` | Air suspension controller: damping states checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Air suspension controller messages (TAS)](../../tas.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
