---
layout: default
title: "DI_debug (0x7D7) — Drive inverter, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Drive inverter message: debug. Tesla Model Y CAN bus message DI_debug (0x7D7) of Drive inverter, firmware 2026.26.6.5, 8 signals (DI_debugSelector, DI_regenBackfillCmd, DI_regenBackfillUnavailableReason, DI_regenBackfillAbsSatState and 4 more). Bit layout, scaling, units and value tables."
---

# DI_debug (0x7D7) — Drive inverter, Tesla Model Y 2026.26.6.5 VEH CAN

Drive inverter message: debug; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of DI_debug as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DI_debug` |
| CAN id | 0x7D7 (2007) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | DI |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 8 |

## Signals of DI_debug

Tesla Model Y CAN bus signals in `DI_debug`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `DI_debugSelector` | selector | Drive inverter: debug selector | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 2 = `Mux2`<br>32 = `pwrSat`<br>33 = `Mux33`<br>34 = `sysPedal`<br>35 = `onePedalDriving1`<br>36 = `onePedalDriving2`<br>37 = `onePedalDriving3`<br>38 = `pedalTorque1`<br>39 = `regenBackfill`<br>45 = `aeb`<br>50 = `sysHeat`<br>53 = `Mux53`<br>65 = `Mux65`<br>66 = `Mux66`<br>67 = `Mux67`<br>68 = `Mux68`<br>69 = `Mux69`<br>75 = `longControl` | plausible |
| `DI_regenBackfillCmd` | page 39 | Drive inverter: regen backfill cmd | 8\|13 | little-endian | unsigned | 2 | 0 | Nm | 0 to 16382 |  | validated |
| `DI_regenBackfillUnavailableReason` | page 39 | Drive inverter: regen backfill unavailable reason | 21\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `NONE`<br>1 = `GTW_DISABLE`<br>2 = `UI_DISABLE`<br>3 = `EBR_UNAVAILABLE`<br>4 = `NON_DRIVE_GEAR`<br>5 = `SYSTEM_STATE`<br>6 = `UI_COASTDOWN_MODE`<br>7 = `ACTIVE_DAMPING_UNAVAILABLE`<br>8 = `TRACTION_CONTROL_UNAVAILABLE`<br>9 = `VELOCITY_ESTIMATOR_UNAVAILABLE`<br>10 = `TRACK_MODE_ACTIVE`<br>11 = `PM_DISABLE_REQUEST`<br>12 = `EBR_FAULT`<br>13 = `BRAKE_TEMP`<br>14 = `CARBON_CERAMIC_BRAKES`<br>15 = `PM_DISABLE_REQUEST_BLEND`<br>16 = `PM_DISABLE_REQUEST_BPED`<br>17 = `EBR_FULL_FAULT`<br>18 = `DI_LATENT_FAULT_TRIP` | validated |
| `DI_regenBackfillAbsSatState` | page 39 | Drive inverter: regen backfill abs sat state | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IDLE`<br>1 = `RAMP_OUT`<br>2 = `RAMP_IN` | validated |
| `DI_sysHeatPowerOptimal` | page 50 | Drive inverter: sys heat power optimal | 8\|8 | little-endian | unsigned | 0.08 | 0 | kW | 0 to 20 |  | validated |
| `DI_sysPostPedalMinTorque` | page 53 | Drive inverter: sys post pedal min torque | 8\|15 | little-endian | unsigned | 0.5 | -13000 | Nm | -13000 to 0 |  | validated |
| `DI_sysPostPedalMaxTorque` | page 53 | Drive inverter: sys post pedal max torque | 24\|15 | little-endian | unsigned | 0.5 | 0 | Nm | 0 to 13000 |  | validated |
| `DI_systemTorqueCommand` | page 53 | Drive inverter: system torque command | 40\|16 | little-endian | signed | 0.5 | 0 | Nm | -13000 to 13000 |  | validated |

## Multiplexing

`DI_debugSelector` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 39 (3 signals), page 50 (1 signals), page 53 (3 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
