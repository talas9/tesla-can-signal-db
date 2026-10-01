---
layout: default
title: "VCLEFT_thermalLogging10Hz (0x290) — Left body controller, Tesla Model Y 2025.20.8 ETH"
description: "Left body controller message: thermal logging10 hz. Ethernet-side message VCLEFT_thermalLogging10Hz of Left body controller for Tesla Model Y firmware 2025.20.8, 27 signals (VCLEFT_thermalLogging10HzIndex, VCLEFT_hvac2RLeftLateralVoltage, VCLEFT_hvac2RLeftVerticalVoltage, VCLEFT_hvac2RRightLateralVoltage and 23 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_thermalLogging10Hz (0x290) — Left body controller, Tesla Model Y 2025.20.8 ETH

Left body controller message: thermal logging10 hz. This page documents the 27 signals of VCLEFT_thermalLogging10Hz as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_thermalLogging10Hz` |
| Ethernet-side id | 0x290 (656) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 20 ms |
| Signals | 27 |

## Signals of VCLEFT_thermalLogging10Hz

Tesla Model Y CAN bus signals in `VCLEFT_thermalLogging10Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_thermalLogging10HzIndex` | selector | Left body controller: thermal logging10 hz index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HVAC_VARS`<br>1 = `HVAC_VARS2`<br>2 = `2R_HVAC_VOLTAGE_AND_STATUS`<br>3 = `MISC`<br>4 = `2R_HVAC_DUTY`<br>5 = `END` | plausible |
| `VCLEFT_hvac2RLeftLateralVoltage` | page 2 | Left body controller: hvac2 r left lateral voltage | 8\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCLEFT_hvac2RLeftVerticalVoltage` | page 2 | Left body controller: hvac2 r left vertical voltage | 16\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCLEFT_hvac2RRightLateralVoltage` | page 2 | Left body controller: hvac2 r right lateral voltage | 24\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCLEFT_hvac2RRightVerticalVoltage` | page 2 | Left body controller: hvac2 r right vertical voltage | 32\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCLEFT_hvac2RLeftLateralCalibrated` | page 2 | Left body controller: hvac2 r left lateral calibrated | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_CALIBRATED`<br>1 = `CALIBRATED` | plausible |
| `VCLEFT_hvac2RLeftVerticalCalibrated` | page 2 | Left body controller: hvac2 r left vertical calibrated | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_CALIBRATED`<br>1 = `CALIBRATED` | plausible |
| `VCLEFT_hvac2RRightLateralCalibrated` | page 2 | Left body controller: hvac2 r right lateral calibrated | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_CALIBRATED`<br>1 = `CALIBRATED` | plausible |
| `VCLEFT_hvac2RRightVerticalCalibrated` | page 2 | Left body controller: hvac2 r right vertical calibrated | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_CALIBRATED`<br>1 = `CALIBRATED` | plausible |
| `VCLEFT_hvac2RLeftLateralState` | page 2 | Left body controller: hvac2 r left lateral state | 44\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `HVAC_ACTUATOR_BRUSHED_STATE_INIT`<br>1 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_RUN`<br>2 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_STALL`<br>3 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_RUN`<br>4 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_STALL`<br>5 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING`<br>6 = `HVAC_ACTUATOR_BRUSHED_STATE_BRAKING`<br>7 = `HVAC_ACTUATOR_BRUSHED_STATE_FAULT`<br>8 = `HVAC_ACTUATOR_BRUSHED_STATE_CONTROL_DISABLED`<br>9 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_BACKOFF`<br>10 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_BACKOFF`<br>11 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING_OVERSHOOT` | plausible |
| `VCLEFT_hvac2RLeftVerticalState` | page 2 | Left body controller: hvac2 r left vertical state | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `HVAC_ACTUATOR_BRUSHED_STATE_INIT`<br>1 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_RUN`<br>2 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_STALL`<br>3 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_RUN`<br>4 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_STALL`<br>5 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING`<br>6 = `HVAC_ACTUATOR_BRUSHED_STATE_BRAKING`<br>7 = `HVAC_ACTUATOR_BRUSHED_STATE_FAULT`<br>8 = `HVAC_ACTUATOR_BRUSHED_STATE_CONTROL_DISABLED`<br>9 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_BACKOFF`<br>10 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_BACKOFF`<br>11 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING_OVERSHOOT` | plausible |
| `VCLEFT_hvac2RRightLateralState` | page 2 | Left body controller: hvac2 r right lateral state | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `HVAC_ACTUATOR_BRUSHED_STATE_INIT`<br>1 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_RUN`<br>2 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_STALL`<br>3 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_RUN`<br>4 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_STALL`<br>5 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING`<br>6 = `HVAC_ACTUATOR_BRUSHED_STATE_BRAKING`<br>7 = `HVAC_ACTUATOR_BRUSHED_STATE_FAULT`<br>8 = `HVAC_ACTUATOR_BRUSHED_STATE_CONTROL_DISABLED`<br>9 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_BACKOFF`<br>10 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_BACKOFF`<br>11 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING_OVERSHOOT` | plausible |
| `VCLEFT_hvac2RRightVerticalState` | page 2 | Left body controller: hvac2 r right vertical state | 56\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `HVAC_ACTUATOR_BRUSHED_STATE_INIT`<br>1 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_RUN`<br>2 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_STALL`<br>3 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_RUN`<br>4 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_STALL`<br>5 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING`<br>6 = `HVAC_ACTUATOR_BRUSHED_STATE_BRAKING`<br>7 = `HVAC_ACTUATOR_BRUSHED_STATE_FAULT`<br>8 = `HVAC_ACTUATOR_BRUSHED_STATE_CONTROL_DISABLED`<br>9 = `HVAC_ACTUATOR_BRUSHED_STATE_POSITIVE_BACKOFF`<br>10 = `HVAC_ACTUATOR_BRUSHED_STATE_NEGATIVE_BACKOFF`<br>11 = `HVAC_ACTUATOR_BRUSHED_STATE_RUNNING_OVERSHOOT` | plausible |
| `VCLEFT_hvacBlowerWindmillElecRpm` | page 3 | Left body controller: hvac blower windmill elec rpm | 8\|14 | little-endian | unsigned | 1 | 0 | RPM | 0 to 16383 |  | plausible |
| `VCLEFT_hvac2RRightVerticalVelocity` | page 3 | Left body controller: hvac2 r right vertical velocity | 24\|8 | little-endian | signed | 1 | 0 | deg/s | -100 to 100 |  | plausible |
| `VCLEFT_hvacBlowerWindmillBemf` | page 3 | Left body controller: hvac blower windmill bemf | 32\|14 | little-endian | unsigned | 4 | 0 | mV | 0 to 65532 |  | plausible |
| `VCLEFT_hvac2RLeftVerticalVelocity` | page 3 | Left body controller: hvac2 r left vertical velocity | 46\|8 | little-endian | signed | 1 | 0 | deg/s | -100 to 100 |  | plausible |
| `VCLEFT_hvac2RLeftLateralVelocity` | page 3 | Left body controller: hvac2 r left lateral velocity | 54\|8 | little-endian | signed | 1 | 0 | deg/s | -100 to 100 |  | plausible |
| `VCLEFT_vcusbLinSchedule` | page 3 | Left body controller: vcusb lin schedule | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VCUSB_LIN_SCHEDULE_OFF`<br>1 = `VCUSB_LIN_SCHEDULE_COMMAND_AND_RESPONSE`<br>2 = `VCUSB_LIN_SCHEDULE_DIAGNOSTIC`<br>3 = `VCUSB_LIN_SCHEDULE_COUNT` | plausible |
| `VCLEFT_hvac2RLeftLateralDuty` | page 4 | Left body controller: hvac2 r left lateral duty | 3\|8 | little-endian | signed | 1 | 0 | % | -100 to 100 |  | plausible |
| `VCLEFT_hvac2RLeftVerticalDuty` | page 4 | Left body controller: hvac2 r left vertical duty | 11\|8 | little-endian | signed | 1 | 0 | % | -100 to 100 |  | plausible |
| `VCLEFT_hvac2RRightLateralDuty` | page 4 | Left body controller: hvac2 r right lateral duty | 19\|8 | little-endian | signed | 1 | 0 | % | -100 to 100 |  | plausible |
| `VCLEFT_hvac2RRightVerticalDuty` | page 4 | Left body controller: hvac2 r right vertical duty | 27\|8 | little-endian | signed | 1 | 0 | % | -100 to 100 |  | plausible |
| `VCLEFT_hvacBlowerWindmilling` | page 4 | Left body controller: hvac blower windmilling | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCLEFT_hvac2RRightLateralVelocity` | page 4 | Left body controller: hvac2 r right lateral velocity | 36\|8 | little-endian | signed | 1 | 0 | deg/s | -100 to 100 |  | plausible |
| `VCLEFT_hvacBlower1msOverrunFrequency` | page 4 | Left body controller: hvac blower1ms overrun frequency | 44\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 |  | layout-only |
| `VCLEFT_hvacBlower10msOverrunFrequency` | page 4 | Left body controller: hvac blower10ms overrun frequency | 54\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | layout-only |

## Multiplexing

`VCLEFT_thermalLogging10HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 2 (12 signals), page 3 (6 signals), page 4 (8 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
