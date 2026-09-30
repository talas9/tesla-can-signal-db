---
layout: default
title: "VCFRONT_LVThermalMotors10Hz (0x2BC) — Front body controller, Tesla Model Y 2025.20.8 VEH CAN"
description: "Front body controller message: LV thermal motors10 hz. Tesla Model Y CAN bus message VCFRONT_LVThermalMotors10Hz (0x2BC) of Front body controller, firmware 2025.20.8, 11 signals (VCFRONT_LVThermalMotorsIndex, VCFRONT_radiatorFanState, VCFRONT_radiatorFanTorque, VCFRONT_radiatorFanIDc and 7 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_LVThermalMotors10Hz (0x2BC) — Front body controller, Tesla Model Y 2025.20.8 VEH CAN

Front body controller message: LV thermal motors10 hz; frame length from the layout, not yet observed on a vehicle bus. This page documents the 11 signals of VCFRONT_LVThermalMotors10Hz as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_LVThermalMotors10Hz` |
| CAN id | 0x2BC (700) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT |
| Frame length | 8 bytes |
| Cycle time | 8 ms |
| Signals | 11 |

## Signals of VCFRONT_LVThermalMotors10Hz

Tesla Model Y CAN bus signals in `VCFRONT_LVThermalMotors10Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_LVThermalMotorsIndex` | selector | Front body controller: LV thermal motors index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `RAD_FAN_0`<br>1 = `RAD_FAN_1`<br>2 = `RAD_FAN_2`<br>3 = `PUMP_PT_0`<br>4 = `PUMP_PT_1`<br>5 = `PUMP_PT_2`<br>6 = `PUMP_BATT_0`<br>7 = `PUMP_BATT_1`<br>8 = `PUMP_BATT_2`<br>9 = `WINDMILL_0`<br>10 = `WINDMILL_1`<br>11 = `COOLANT_FLOW_DIAGNOSTICS`<br>12 = `END` | plausible |
| `VCFRONT_radiatorFanState` | page 0 | Radiator Fan motor controller state | 4\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VC_mlxControllerState_IDLE`<br>1 = `VC_mlxControllerState_ENABLE`<br>2 = `VC_mlxControllerState_COLD_STARTUP`<br>3 = `VC_mlxControllerState_STANDBY`<br>4 = `VC_mlxControllerState_SELF_TEST`<br>5 = `VC_mlxControllerState_UV_TEST`<br>6 = `VC_mlxControllerState_FAULTED`<br>7 = `VC_mlxControllerState_MIA` | validated |
| `VCFRONT_radiatorFanTorque` | page 0 | Radiator Fan motor torque; raw 1023 = signal not available (SNA) | 8\|10 | little-endian | unsigned | 0.006 | -1.5 | Nm | -1.5 to 4.5 | 1023 = `SNA` | validated |
| `VCFRONT_radiatorFanIDc` | page 0 | Radiator Fan DC current; raw 127 = signal not available (SNA) | 24\|7 | little-endian | unsigned | 0.5 | 0 | A | 0 to 63 | 127 = `SNA` | validated |
| `VCFRONT_mlxLINCurrentSchedule` | page 0 | Currently set schedule for MLX LIN bus | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OFF`<br>1 = `NORMAL`<br>2 = `DIAGNOSTIC` | validated |
| `VCFRONT_pumpPowertrainState` | page 3 | Powertrain Pump motor controller state | 4\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VC_mlxControllerState_IDLE`<br>1 = `VC_mlxControllerState_ENABLE`<br>2 = `VC_mlxControllerState_COLD_STARTUP`<br>3 = `VC_mlxControllerState_STANDBY`<br>4 = `VC_mlxControllerState_SELF_TEST`<br>5 = `VC_mlxControllerState_UV_TEST`<br>6 = `VC_mlxControllerState_FAULTED`<br>7 = `VC_mlxControllerState_MIA` | validated |
| `VCFRONT_pumpPowertrainTorque` | page 3 | Powertrain Pump motor torque; raw 1023 = signal not available (SNA) | 8\|10 | little-endian | unsigned | 0.006 | -1.5 | Nm | -1.5 to 4.5 | 1023 = `SNA` | validated |
| `VCFRONT_pumpPowertrainIDc` | page 3 | Powertrain Pump DC current; raw 127 = signal not available (SNA) | 24\|7 | little-endian | unsigned | 0.5 | 0 | A | 0 to 63 | 127 = `SNA` | validated |
| `VCFRONT_pumpBatteryState` | page 6 | Battery Pump motor controller state | 4\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VC_mlxControllerState_IDLE`<br>1 = `VC_mlxControllerState_ENABLE`<br>2 = `VC_mlxControllerState_COLD_STARTUP`<br>3 = `VC_mlxControllerState_STANDBY`<br>4 = `VC_mlxControllerState_SELF_TEST`<br>5 = `VC_mlxControllerState_UV_TEST`<br>6 = `VC_mlxControllerState_FAULTED`<br>7 = `VC_mlxControllerState_MIA` | validated |
| `VCFRONT_pumpBatteryTorque` | page 6 | Battery Pump motor torque; raw 1023 = signal not available (SNA) | 8\|10 | little-endian | unsigned | 0.006 | -1.5 | Nm | -1.5 to 4.5 | 1023 = `SNA` | validated |
| `VCFRONT_pumpBatteryIDc` | page 6 | Battery Pump DC current; raw 127 = signal not available (SNA) | 24\|7 | little-endian | unsigned | 0.5 | 0 | A | 0 to 63 | 127 = `SNA` | validated |

## Multiplexing

`VCFRONT_LVThermalMotorsIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (4 signals), page 3 (3 signals), page 6 (3 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
