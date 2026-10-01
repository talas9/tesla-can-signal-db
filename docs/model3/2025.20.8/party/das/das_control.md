---
layout: default
title: "DAS_control (0x2B9) — Driver assistance computer, Tesla Model 3 2025.20.8 PARTY CAN"
description: "Driver assistance computer message: control. Tesla Model 3 CAN bus message DAS_control (0x2B9) of Driver assistance computer, firmware 2025.20.8, 9 signals (DAS_setSpeed, DAS_accState, DAS_aebEvent, DAS_jerkMin and 5 more). Bit layout, scaling, units and value tables."
---

# DAS_control (0x2B9) — Driver assistance computer, Tesla Model 3 2025.20.8 PARTY CAN

Driver assistance computer message: control; frame length from the layout, not yet observed on a vehicle bus. This page documents the 9 signals of DAS_control as defined for Tesla Model 3 firmware 2025.20.8 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DAS_control` |
| CAN id | 0x2B9 (697) |
| ECU | [Driver assistance computer](../../das.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | DAS |
| Frame length | 8 bytes |
| Cycle time | 40 ms |
| Signals | 9 |

## Signals of DAS_control

Tesla Model 3 CAN bus signals in `DAS_control`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DAS_setSpeed` | Detects the commanded Traffic Aware Cruise Control (TACC) or Autopilot set speed for the Drive Inverter (DI); raw 4095 = signal not available (SNA) | 0\|12 | little-endian | unsigned | 0.1 | 0 | kph | 0 to 409.4 | 4095 = `SNA` | plausible |
| `DAS_accState` | Reports the state of Adaptive Cruise Control (ACC), Traffic-Aware Cruise Control (TACC), and Autopark / Summon; raw 15 = signal not available (SNA) | 12\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `ACC_CANCEL_GENERIC`<br>1 = `ACC_BACKWARD`<br>2 = `ACC_FORWARD`<br>3 = `ACC_HOLD`<br>4 = `ACC_ON`<br>5 = `APC_BACKWARD`<br>6 = `APC_FORWARD`<br>7 = `APC_COMPLETE`<br>8 = `APC_ABORT`<br>9 = `APC_PAUSE`<br>10 = `APC_UNPARK_COMPLETE`<br>11 = `APC_SELFPARK_START`<br>12 = `ACC_PARK`<br>13 = `ACC_CANCEL_GENERIC_SILENT`<br>15 = `FAULT_SNA` | plausible |
| `DAS_aebEvent` | Driver assistance computer: aeb event; raw 3 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `AEB_NOT_ACTIVE`<br>1 = `AEB_ACTIVE`<br>2 = `AEB_FAULT`<br>3 = `AEB_SNA` | plausible |
| `DAS_jerkMin` | Reports the minimum allowed jerk the Drive Inverter (DI) can generate to reach the commanded set speed; raw 511 = signal not available (SNA) | 18\|9 | little-endian | unsigned | 0.03 | -15.232 | m/s^3 | -15.232 to 0.068 | 511 = `SNA` | plausible |
| `DAS_jerkMax` | Reports the maximum allowed jerk the Drive Inverter (DI) can generate to reach the commanded set speed; raw 255 = signal not available (SNA) | 27\|8 | little-endian | unsigned | 0.059 | 0 | m/s^3 | 0 to 14.986 | 255 = `SNA` | plausible |
| `DAS_accelMin` | Reports the minimum acceleration the drive inverter can apply to reach the commanded set speed; raw 511 = signal not available (SNA) | 35\|9 | little-endian | unsigned | 0.04 | -15 | m/s^2 | -15 to 5.4 | 511 = `SNA` | plausible |
| `DAS_accelMax` | Reports the maximum acceleration the drive inverter can apply to reach the commanded set speed; raw 511 = signal not available (SNA) | 44\|9 | little-endian | unsigned | 0.04 | -15 | m/s^2 | -15 to 5.4 | 511 = `SNA` | plausible |
| `DAS_controlCounter` | Driver assistance computer: control counter | 53\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `DAS_controlChecksum` | Driver assistance computer: control checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 PARTY DBC file](../../../../../dbc/Model3/2025.20.8/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/PARTY.json)

## See also

- [All Driver assistance computer messages (DAS)](../../das.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
