---
layout: default
title: "APS_sysHealth (0x5E6) — Driver assistance computer (secondary), Tesla Model 3 / Model Y 2025.20.8 CH CAN"
description: "Driver assistance computer (secondary) message: sys health. Tesla Model 3 / Model Y CAN bus message APS_sysHealth (0x5E6) of Driver assistance computer (secondary), firmware 2025.20.8, 6 signals (APS_A_cam12v0Voltage, APS_B_cam12v0Voltage, APS_A_turboMaxTemperature, APS_A_turboProbeType and 2 more). Bit layout, scaling, units and value tables."
---

# APS_sysHealth (0x5E6) — Driver assistance computer (secondary), Tesla Model 3 / Model Y 2025.20.8 CH CAN

Driver assistance computer (secondary) message: sys health; frame length from the layout, not yet observed on a vehicle bus. This page documents the 6 signals of APS_sysHealth as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APS_sysHealth` |
| CAN id | 0x5E6 (1510) |
| ECU | [Driver assistance computer (secondary)](../../aps.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | APS |
| Frame length | 7 bytes |
| Cycle time | 1000 ms |
| Signals | 6 |

## Signals of APS_sysHealth

Tesla Model 3 / Model Y CAN bus signals in `APS_sysHealth`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APS_A_cam12v0Voltage` | Measures the 12V camera power supply voltage for Autopilot Secondary Processor (APS) Turbo A; raw 4095 = signal not available (SNA) | 0\|12 | little-endian | unsigned | 0.0048 | 0 | V | 0 to 19.44 | 4095 = `SNA` | plausible |
| `APS_B_cam12v0Voltage` | Measures the 12V camera power supply voltage for Autopilot Secondary Processor (APS) Turbo B; raw 4095 = signal not available (SNA) | 12\|12 | little-endian | unsigned | 0.0048 | 0 | V | 0 to 19.44 | 4095 = `SNA` | plausible |
| `APS_A_turboMaxTemperature` | Reports the maximum temperature recorded by Autopilot Secondary Processor (APS) unit A; raw 128 = signal not available (SNA) | 24\|8 | little-endian | signed | 1 | 0 | degC | -128 to 127 | -128 = `SNA` | plausible |
| `APS_A_turboProbeType` | Driver assistance computer (secondary): a turbo probe type; raw 63 = signal not available (SNA) | 32\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 62 | 63 = `SNA` | plausible |
| `APS_B_turboMaxTemperature` | Reports the maximum temperature recorded by Autopilot Secondary Processor (APS) unit B; raw 128 = signal not available (SNA) | 38\|8 | little-endian | signed | 1 | 0 | degC | -128 to 127 | -128 = `SNA` | plausible |
| `APS_B_turboProbeType` | Driver assistance computer (secondary): b turbo probe type; raw 63 = signal not available (SNA) | 46\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 62 | 63 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 CH DBC file](../../../../../dbc/AllModels/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/CH.json)

## See also

- [All Driver assistance computer (secondary) messages (APS)](../../aps.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
