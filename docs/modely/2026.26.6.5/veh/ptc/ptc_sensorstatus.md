---
layout: default
title: "PTC_sensorStatus (0x287) — Cabin heater, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Cabin heater message: sensor status. Tesla Model Y CAN bus message PTC_sensorStatus (0x287) of Cabin heater, firmware 2026.26.6.5, 7 signals (PTC_leftTempIGBT, PTC_tempOCP, PTC_rightTempIGBT, PTC_tempPCB and 3 more). Bit layout, scaling, units and value tables."
---

# PTC_sensorStatus (0x287) — Cabin heater, Tesla Model Y 2026.26.6.5 VEH CAN

Cabin heater message: sensor status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 7 signals of PTC_sensorStatus as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PTC_sensorStatus` |
| CAN id | 0x287 (647) |
| ECU | [Cabin heater](../../ptc.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PTC |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 7 |

## Signals of PTC_sensorStatus

Tesla Model Y CAN bus signals in `PTC_sensorStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PTC_leftTempIGBT` | Heater left bank IGBT temperature | 0\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 200 |  | validated |
| `PTC_tempOCP` | Temperature measured near the over current protection circuit | 8\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 200 |  | validated |
| `PTC_rightTempIGBT` | Heater right bank IGBT temperature | 16\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 200 |  | validated |
| `PTC_tempPCB` | Heater printed circuit board temperature | 24\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 200 |  | validated |
| `PTC_voltageHV` | Heater high voltage input voltage | 32\|10 | little-endian | unsigned | 0.5 | 0 | V | 0 to 511.5 |  | validated |
| `PTC_leftCurrentHV` | Cabin heater: left current HV | 48\|8 | little-endian | unsigned | 0.2 | 0 | A | 0 to 50 |  | validated |
| `PTC_rightCurrentHV` | Cabin heater: right current HV | 56\|8 | little-endian | unsigned | 0.2 | 0 | A | 0 to 50 |  | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Cabin heater messages (PTC)](../../ptc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
