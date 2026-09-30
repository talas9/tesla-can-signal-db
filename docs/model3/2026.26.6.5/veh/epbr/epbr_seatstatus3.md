---
layout: default
title: "EPBR_seatStatus3 (0x2E6) — Right electric parking brake, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Right electric parking brake message: seat status3. Tesla Model 3 CAN bus message EPBR_seatStatus3 (0x2E6) of Right electric parking brake, firmware 2026.26.6.5, 7 signals (EPBR_frontSeatCushionFanCur, EPBR_frontSeatBackrestFanCur, EPBR_frontSeatCushionFanDuty, EPBR_frontSeatCushionFanEn and 3 more). Bit layout, scaling, units and value tables."
---

# EPBR_seatStatus3 (0x2E6) — Right electric parking brake, Tesla Model 3 2026.26.6.5 VEH CAN

Right electric parking brake message: seat status3; frame length from the layout, not yet observed on a vehicle bus. This page documents the 7 signals of EPBR_seatStatus3 as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `EPBR_seatStatus3` |
| CAN id | 0x2E6 (742) |
| ECU | [Right electric parking brake](../../epbr.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | EPBR |
| Frame length | 7 bytes |
| Cycle time | 1000 ms |
| Signals | 7 |

## Signals of EPBR_seatStatus3

Tesla Model 3 CAN bus signals in `EPBR_seatStatus3`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `EPBR_frontSeatCushionFanCur` | Right electric parking brake: front seat cushion fan cur | 0\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | validated |
| `EPBR_frontSeatBackrestFanCur` | Right electric parking brake: front seat backrest fan cur | 12\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | validated |
| `EPBR_frontSeatCushionFanDuty` | Right electric parking brake: front seat cushion fan duty | 24\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `EPBR_frontSeatCushionFanEn` | Right electric parking brake: front seat cushion fan en | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_frontSeatBackrestFanEn` | Right electric parking brake: front seat backrest fan en | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_frontSeatBackrestFanDuty` | Right electric parking brake: front seat backrest fan duty | 33\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `EPBR_seat2RControllerCurrent` | Right electric parking brake: seat2 r controller current | 40\|9 | little-endian | unsigned | 0.2 | 0 | A | 0 to 102 |  | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Right electric parking brake messages (EPBR)](../../epbr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
