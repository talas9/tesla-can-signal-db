---
layout: default
title: "DI_estimatedBrakeTemp (0x74A) — Drive inverter, Tesla Model 3 2025.20.8 ETH"
description: "Drive inverter message: estimated brake temp. Ethernet-side message DI_estimatedBrakeTemp of Drive inverter for Tesla Model 3 firmware 2025.20.8, 6 signals (DI_estimatedBrakeTempChecksum, DI_estimatedBrakeTempCounter, DI_brakeFLTemp, DI_brakeFRTemp and 2 more). Bit layout, scaling, units and value tables."
---

# DI_estimatedBrakeTemp (0x74A) — Drive inverter, Tesla Model 3 2025.20.8 ETH

Drive inverter message: estimated brake temp. This page documents the 6 signals of DI_estimatedBrakeTemp as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DI_estimatedBrakeTemp` |
| Ethernet-side id | 0x74A (1866) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DI |
| Frame length | 7 bytes |
| Cycle time | 1000 ms |
| Signals | 6 |

## Signals of DI_estimatedBrakeTemp

Tesla Model 3 CAN bus signals in `DI_estimatedBrakeTemp`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_estimatedBrakeTempChecksum` | Drive inverter: estimated brake temp checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `DI_estimatedBrakeTempCounter` | Drive inverter: estimated brake temp counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `DI_brakeFLTemp` | Drive inverter: brake FL temp; raw 1023 = signal not available (SNA) | 12\|10 | little-endian | unsigned | 1 | -40 | DegC | -40 to 982 | 1023 = `SNA` | plausible |
| `DI_brakeFRTemp` | Drive inverter: brake FR temp; raw 1023 = signal not available (SNA) | 22\|10 | little-endian | unsigned | 1 | -40 | DegC | -40 to 982 | 1023 = `SNA` | plausible |
| `DI_brakeRLTemp` | Drive inverter: brake RL temp; raw 1023 = signal not available (SNA) | 32\|10 | little-endian | unsigned | 1 | -40 | DegC | -40 to 982 | 1023 = `SNA` | plausible |
| `DI_brakeRRTemp` | Drive inverter: brake RR temp; raw 1023 = signal not available (SNA) | 42\|10 | little-endian | unsigned | 1 | -40 | DegC | -40 to 982 | 1023 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
