---
layout: default
title: "CMPD_state (0x2A7) — CMPD ECU, Tesla Model 3 2025.20.8 VEH CAN"
description: "CMPD ECU message: state. Tesla Model 3 CAN bus message CMPD_state (0x2A7) of CMPD ECU, firmware 2025.20.8, 11 signals (CMPD_speedRPM, CMPD_speedDuty, CMPD_inputHVPower, CMPD_inputHVCurrent and 7 more). Bit layout, scaling, units and value tables."
---

# CMPD_state (0x2A7) — CMPD ECU, Tesla Model 3 2025.20.8 VEH CAN

CMPD ECU message: state; frame length from the layout, not yet observed on a vehicle bus. This page documents the 11 signals of CMPD_state as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `CMPD_state` |
| CAN id | 0x2A7 (679) |
| ECU | [CMPD ECU](../../cmpd.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | CMPD |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 11 |

## Signals of CMPD_state

Tesla Model 3 CAN bus signals in `CMPD_state`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `CMPD_speedRPM` | Reports compressor speed. | 0\|11 | little-endian | unsigned | 10 | 0 | RPM | 0 to 20000 |  | plausible |
| `CMPD_speedDuty` | Reports compressor speed duty cycle percentage. | 11\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 100 |  | plausible |
| `CMPD_inputHVPower` | Measures compressor input high voltage (HV) power consumption. | 21\|11 | little-endian | unsigned | 10 | 0 | W | 0 to 20000 |  | plausible |
| `CMPD_inputHVCurrent` | Measures compressor input high voltage (HV) current draw. | 32\|9 | little-endian | unsigned | 0.1 | 0 | A | 0 to 50 |  | plausible |
| `CMPD_inputHVVoltage` | Measures compressor input high voltage (HV) level. | 41\|11 | little-endian | unsigned | 0.5 | 0 | V | 0 to 1000 |  | plausible |
| `CMPD_2ShuntModeActive` | Indicates the compressor motor control is running using only two current shunt resistors instead of three. | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CMPD_powerLimitActive` | Indicates the compressor power limit is active. | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CMPD_state` | Reports compressor operational state; raw 15 = signal not available (SNA) | 56\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `CMPD_STATE_INIT`<br>1 = `CMPD_STATE_RUNNING`<br>2 = `CMPD_STATE_STANDBY`<br>3 = `CMPD_STATE_FAULT`<br>4 = `CMPD_STATE_IDLE`<br>15 = `CMPD_STATE_SNA` | plausible |
| `CMPD_wasteHeatState` | Reports compressor waste heat recovery state. | 60\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CMPD_WASTE_HEAT_STATE_OFF`<br>1 = `CMPD_WASTE_HEAT_STATE_ACTIVE`<br>2 = `CMPD_WASTE_HEAT_STATE_NOT_AVAILABLE`<br>3 = `CMPD_WASTE_HEAT_STATE_UNUSED` | plausible |
| `CMPD_powerLimitTooLowToStart` | Indicates the compressor power limit is too low to start the compressor. | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `CMPD_ready` | Indicates the compressor is ready to start. | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All CMPD ECU messages (CMPD)](../../cmpd.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
