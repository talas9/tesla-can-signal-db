---
layout: default
title: "APP_boardTemperatures (0x3FC) — Driver assistance computer (primary), Tesla Model 3 2025.20.8 CH CAN"
description: "Driver assistance computer (primary) message: board temperatures. Tesla Model 3 CAN bus message APP_boardTemperatures (0x3FC) of Driver assistance computer (primary), firmware 2025.20.8, 7 signals (APP_decisionTemperature, APP_pascalTemperature, APP_parkerATemperature, APP_parkerBTemperature and 3 more). Bit layout, scaling, units and value tables."
---

# APP_boardTemperatures (0x3FC) — Driver assistance computer (primary), Tesla Model 3 2025.20.8 CH CAN

Driver assistance computer (primary) message: board temperatures; frame length from the layout, not yet observed on a vehicle bus. This page documents the 7 signals of APP_boardTemperatures as defined for Tesla Model 3 firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APP_boardTemperatures` |
| CAN id | 0x3FC (1020) |
| ECU | [Driver assistance computer (primary)](../../app.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | APP |
| Frame length | 7 bytes |
| Cycle time | 1000 ms |
| Signals | 7 |

## Signals of APP_boardTemperatures

Tesla Model 3 CAN bus signals in `APP_boardTemperatures`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APP_decisionTemperature` | Rolling average of Parker and Pascal temperature. | 0\|8 | little-endian | unsigned | 1 | -128 | C | -128 to 127 | 0 = `UNKNOWN` | plausible |
| `APP_pascalTemperature` | Temperature of Autopilot GPU | 8\|8 | little-endian | unsigned | 1 | -128 | C | -128 to 127 | 0 = `UNKNOWN` | plausible |
| `APP_parkerATemperature` | Temperature of Autopilot CPU(1) | 16\|8 | little-endian | unsigned | 1 | -128 | C | -128 to 127 | 0 = `UNKNOWN` | plausible |
| `APP_parkerBTemperature` | Temperature of Autopilot CPU(1) | 24\|8 | little-endian | unsigned | 1 | -128 | C | -128 to 127 | 0 = `UNKNOWN` | plausible |
| `APP_pascalExtTemperature` | External temperature of Autopilot GPU | 32\|8 | little-endian | unsigned | 1 | -128 | C | -128 to 127 | 0 = `UNKNOWN` | plausible |
| `APP_parkerExtTemperature` | External temperature of Parker | 40\|8 | little-endian | unsigned | 1 | -128 | C | -128 to 127 | 0 = `UNKNOWN` | plausible |
| `APP_pascalHeaterDecision` | Pascal heater descision on/off | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OFF`<br>1 = `ON` | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 CH DBC file](../../../../../dbc/Model3/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/CH.json)

## See also

- [All Driver assistance computer (primary) messages (APP)](../../app.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
