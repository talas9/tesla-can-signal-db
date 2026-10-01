---
layout: default
title: "VCFRONT_okToUseHighPower (0x2D1) — Front body controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Front body controller message: ok to use high power. Tesla Model 3 / Model Y CAN bus message VCFRONT_okToUseHighPower (0x2D1) of Front body controller, firmware 2025.20.8, 9 signals (VCFRONT_vcleftOkToUseHighPower, VCFRONT_vcrightOkToUseHighPower, VCFRONT_das1OkToUseHighPower, VCFRONT_das2OkToUseHighPower and 5 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_okToUseHighPower (0x2D1) — Front body controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Front body controller message: ok to use high power; frame length observed on a vehicle bus. This page documents the 9 signals of VCFRONT_okToUseHighPower as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_okToUseHighPower` |
| CAN id | 0x2D1 (721) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT |
| Frame length | 2 bytes |
| Cycle time | 100 ms |
| Signals | 9 |

## Signals of VCFRONT_okToUseHighPower

Tesla Model 3 / Model Y CAN bus signals in `VCFRONT_okToUseHighPower`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_vcleftOkToUseHighPower` | Front body controller: vcleft ok to use high power | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_vcrightOkToUseHighPower` | Front body controller: vcright ok to use high power | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_das1OkToUseHighPower` | Front body controller: das1 ok to use high power | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_das2OkToUseHighPower` | Front body controller: das2 ok to use high power | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_MCULogicOkToUseHighPower` | Front body controller: MCU logic ok to use high power | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_MCUAudioOkToUseHighPower` | Front body controller: MCU audio ok to use high power | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_cpOkToUseHighPower` | Front body controller: cp ok to use high power | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_premAudioOkToUseHiPower` | Front body controller: prem audio ok to use hi power | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_tasOkToUseHighPower` | Front body controller: tas ok to use high power | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
