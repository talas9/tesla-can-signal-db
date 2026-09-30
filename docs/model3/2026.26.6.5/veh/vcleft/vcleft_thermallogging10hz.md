---
layout: default
title: "VCLEFT_thermalLogging10Hz (0x290) — Left body controller, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Left body controller message: thermal logging10 hz. Tesla Model 3 CAN bus message VCLEFT_thermalLogging10Hz (0x290) of Left body controller, firmware 2026.26.6.5, 29 signals (VCLEFT_thermalLogging10HzIndex, VCLEFT_hvac2RLeftLateralVoltage, VCLEFT_hvac2RLeftVerticalVoltage, VCLEFT_hvac2RRightLateralVoltage and 25 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_thermalLogging10Hz (0x290) — Left body controller, Tesla Model 3 2026.26.6.5 VEH CAN

Left body controller message: thermal logging10 hz; frame length from the layout, not yet observed on a vehicle bus. This page documents the 29 signals of VCLEFT_thermalLogging10Hz as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_thermalLogging10Hz` |
| CAN id | 0x290 (656) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 20 ms |
| Signals | 29 |

## Signals of VCLEFT_thermalLogging10Hz

Tesla Model 3 CAN bus signals in `VCLEFT_thermalLogging10Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_thermalLogging10HzIndex` | selector | Left body controller: thermal logging10 hz index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HVAC_VARS`<br>1 = `HVAC_VARS2`<br>2 = `2R_HVAC_VOLTAGE_AND_STATUS`<br>3 = `MISC`<br>4 = `2R_HVAC_DUTY`<br>5 = `END` | plausible |
| `VCLEFT_hvac2RLeftLateralVoltage` | page 2 | Left body controller: hvac2 r left lateral voltage | 8\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCLEFT_hvac2RLeftVerticalVoltage` | page 2 | Left body controller: hvac2 r left vertical voltage | 16\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCLEFT_hvac2RRightLateralVoltage` | page 2 | Left body controller: hvac2 r right lateral voltage | 24\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCLEFT_hvac2RRightVerticalVoltage` | page 2 | Left body controller: hvac2 r right vertical voltage | 32\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCLEFT_hvac2RLeftLateralCalibrated` | page 2 | Left body controller: hvac2 r left lateral calibrated | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_CALIBRATED`<br>1 = `CALIBRATED` | validated |
| `VCLEFT_hvac2RLeftVerticalCalibrated` | page 2 | Left body controller: hvac2 r left vertical calibrated | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_CALIBRATED`<br>1 = `CALIBRATED` | validated |
| `VCLEFT_hvac2RRightLateralCalibrated` | page 2 | Left body controller: hvac2 r right lateral calibrated | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_CALIBRATED`<br>1 = `CALIBRATED` | validated |
| `VCLEFT_hvac2RRightVerticalCalibrated` | page 2 | Left body controller: hvac2 r right vertical calibrated | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_CALIBRATED`<br>1 = `CALIBRATED` | validated |
| `VCLEFT_hvac2RLeftLateralState` | page 2 | Left body controller: hvac2 r left lateral state | 44\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `HVAC_ACTUATOR_BRUSHED_STATE_INIT`<br>1 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_RUN`<br>2 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_STALL`<br>3 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_RUN`<br>4 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_STALL`<br>5 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING`<br>6 = `HVAC_ACTUATOR_BRUSHED_STATE_BRAKING`<br>7 = `HVAC_ACTUATOR_BRUSHED_STATE_FAULT`<br>8 = `HVAC_ACTUATOR_BRUSHED_STATE_CONTROL_DISABLED`<br>9 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_BACKOFF`<br>10 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_BACKOFF`<br>11 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING_OVERSHOOT` | validated |
| `VCLEFT_hvac2RLeftVerticalState` | page 2 | Left body controller: hvac2 r left vertical state | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `HVAC_ACTUATOR_BRUSHED_STATE_INIT`<br>1 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_RUN`<br>2 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_STALL`<br>3 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_RUN`<br>4 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_STALL`<br>5 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING`<br>6 = `HVAC_ACTUATOR_BRUSHED_STATE_BRAKING`<br>7 = `HVAC_ACTUATOR_BRUSHED_STATE_FAULT`<br>8 = `HVAC_ACTUATOR_BRUSHED_STATE_CONTROL_DISABLED`<br>9 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_BACKOFF`<br>10 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_BACKOFF`<br>11 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING_OVERSHOOT` | validated |
| `VCLEFT_hvac2RRightLateralState` | page 2 | Left body controller: hvac2 r right lateral state | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `HVAC_ACTUATOR_BRUSHED_STATE_INIT`<br>1 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_RUN`<br>2 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_STALL`<br>3 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_RUN`<br>4 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_STALL`<br>5 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING`<br>6 = `HVAC_ACTUATOR_BRUSHED_STATE_BRAKING`<br>7 = `HVAC_ACTUATOR_BRUSHED_STATE_FAULT`<br>8 = `HVAC_ACTUATOR_BRUSHED_STATE_CONTROL_DISABLED`<br>9 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_BACKOFF`<br>10 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_BACKOFF`<br>11 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING_OVERSHOOT` | validated |
| `VCLEFT_hvac2RRightVerticalState` | page 2 | Left body controller: hvac2 r right vertical state | 56\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `HVAC_ACTUATOR_BRUSHED_STATE_INIT`<br>1 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_RUN`<br>2 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_STALL`<br>3 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_RUN`<br>4 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_STALL`<br>5 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING`<br>6 = `HVAC_ACTUATOR_BRUSHED_STATE_BRAKING`<br>7 = `HVAC_ACTUATOR_BRUSHED_STATE_FAULT`<br>8 = `HVAC_ACTUATOR_BRUSHED_STATE_CONTROL_DISABLED`<br>9 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_BACKOFF`<br>10 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_BACKOFF`<br>11 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING_OVERSHOOT` | validated |
| `VCLEFT_hvacBlowerWindmillElecRpm` | page 3 | Left body controller: hvac blower windmill elec rpm | 3\|14 | little-endian | unsigned | 1 | 0 | RPM | 0 to 16383 |  | validated |
| `VCLEFT_hvac2RRightVerticalVelocity` | page 3 | Left body controller: hvac2 r right vertical velocity | 17\|8 | little-endian | signed | 1 | 0 | deg/s | -100 to 100 |  | validated |
| `VCLEFT_hvacBlowerWindmillBemf` | page 3 | Left body controller: hvac blower windmill bemf | 25\|14 | little-endian | unsigned | 4 | 0 | mV | 0 to 65532 |  | validated |
| `VCLEFT_hvac2RLeftVerticalVelocity` | page 3 | Left body controller: hvac2 r left vertical velocity | 39\|8 | little-endian | signed | 1 | 0 | deg/s | -100 to 100 |  | validated |
| `VCLEFT_hvac2RLeftLateralVelocity` | page 3 | Left body controller: hvac2 r left lateral velocity | 47\|8 | little-endian | signed | 1 | 0 | deg/s | -100 to 100 |  | validated |
| `VCLEFT_vcusbLinSchedule` | page 3 | Left body controller: vcusb lin schedule | 55\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VCUSB_LIN_SCHEDULE_OFF`<br>1 = `VCUSB_LIN_SCHEDULE_COMMAND_AND_RESPONSE`<br>2 = `VCUSB_LIN_SCHEDULE_DIAGNOSTIC`<br>3 = `VCUSB_LIN_SCHEDULE_COUNT` | validated |
| `VCLEFT_hvacBlowerArbState` | page 3 | Left body controller: hvac blower arb state | 57\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ARBITRATOR_NOT_READY`<br>1 = `ARBITRATOR_READY`<br>2 = `ARBITRATOR_HIGH_FREQ_VOLT_INJECTION`<br>3 = `ARBITRATOR_WAIT_BEFORE_REQUEST`<br>4 = `ARBITRATOR_REQUEST_CURRENT`<br>5 = `ARBITRATOR_COMPLETED`<br>6 = `ARBITRATOR_FAULTED` | validated |
| `VCLEFT_hvacBlowerArbResult` | page 3 | Left body controller: hvac blower arb result | 60\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VC_MOTOR_ID_UNKNOWN`<br>1 = `VC_MOTOR_ID_DELTA`<br>2 = `VC_MOTOR_ID_BOSCH` | validated |
| `VCLEFT_hvac2RLeftLateralDuty` | page 4 | Left body controller: hvac2 r left lateral duty | 3\|8 | little-endian | signed | 1 | 0 | % | -100 to 100 |  | validated |
| `VCLEFT_hvac2RLeftVerticalDuty` | page 4 | Left body controller: hvac2 r left vertical duty | 11\|8 | little-endian | signed | 1 | 0 | % | -100 to 100 |  | validated |
| `VCLEFT_hvac2RRightLateralDuty` | page 4 | Left body controller: hvac2 r right lateral duty | 19\|8 | little-endian | signed | 1 | 0 | % | -100 to 100 |  | validated |
| `VCLEFT_hvac2RRightVerticalDuty` | page 4 | Left body controller: hvac2 r right vertical duty | 27\|8 | little-endian | signed | 1 | 0 | % | -100 to 100 |  | validated |
| `VCLEFT_hvacBlowerWindmilling` | page 4 | Left body controller: hvac blower windmilling | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_hvac2RRightLateralVelocity` | page 4 | Left body controller: hvac2 r right lateral velocity | 36\|8 | little-endian | signed | 1 | 0 | deg/s | -100 to 100 |  | validated |
| `VCLEFT_hvacBlower1msOverrunFrequency` | page 4 | Left body controller: hvac blower1ms overrun frequency | 44\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 |  | validated |
| `VCLEFT_hvacBlower10msOverrunFrequency` | page 4 | Left body controller: hvac blower10ms overrun frequency | 54\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | validated |

## Multiplexing

`VCLEFT_thermalLogging10HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 2 (12 signals), page 3 (8 signals), page 4 (8 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
