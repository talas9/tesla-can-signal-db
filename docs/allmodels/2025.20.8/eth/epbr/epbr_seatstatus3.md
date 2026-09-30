---
layout: default
title: "EPBR_seatStatus3 (0x2E6) — Right electric parking brake, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Right electric parking brake message: seat status3. Ethernet-side message EPBR_seatStatus3 of Right electric parking brake for Tesla Model 3 / Model Y firmware 2025.20.8, 6 signals (EPBR_frontSeatCushionFanCur, EPBR_frontSeatBackrestFanCur, EPBR_frontSeatCushionFanDuty, EPBR_frontSeatCushionFanEn and 2 more). Bit layout, scaling, units and value tables."
---

# EPBR_seatStatus3 (0x2E6) — Right electric parking brake, Tesla Model 3 / Model Y 2025.20.8 ETH

Right electric parking brake message: seat status3. This page documents the 6 signals of EPBR_seatStatus3 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `EPBR_seatStatus3` |
| Ethernet-side id | 0x2E6 (742) |
| ECU | [Right electric parking brake](../../epbr.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | EPBR |
| Frame length | 5 bytes |
| Cycle time | 1000 ms |
| Signals | 6 |

## Signals of EPBR_seatStatus3

Tesla Model 3 / Model Y CAN bus signals in `EPBR_seatStatus3`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `EPBR_frontSeatCushionFanCur` | Right electric parking brake: front seat cushion fan cur | 0\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | validated |
| `EPBR_frontSeatBackrestFanCur` | Right electric parking brake: front seat backrest fan cur | 12\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | validated |
| `EPBR_frontSeatCushionFanDuty` | Right electric parking brake: front seat cushion fan duty | 24\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `EPBR_frontSeatCushionFanEn` | Right electric parking brake: front seat cushion fan en | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_frontSeatBackrestFanEn` | Right electric parking brake: front seat backrest fan en | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_frontSeatBackrestFanDuty` | Right electric parking brake: front seat backrest fan duty | 33\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Right electric parking brake messages (EPBR)](../../epbr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
