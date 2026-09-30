---
layout: default
title: "EPBL_seatStatus3 (0x2E7) — Left electric parking brake, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Left electric parking brake message: seat status3. Tesla Model 3 CAN bus message EPBL_seatStatus3 (0x2E7) of Left electric parking brake, firmware 2026.26.6.5, 6 signals (EPBL_frontSeatCushionFanCur, EPBL_frontSeatBackrestFanCur, EPBL_frontSeatCushionFanDuty, EPBL_frontSeatCushionFanEn and 2 more). Bit layout, scaling, units and value tables."
---

# EPBL_seatStatus3 (0x2E7) — Left electric parking brake, Tesla Model 3 2026.26.6.5 VEH CAN

Left electric parking brake message: seat status3; frame length from the layout, not yet observed on a vehicle bus. This page documents the 6 signals of EPBL_seatStatus3 as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `EPBL_seatStatus3` |
| CAN id | 0x2E7 (743) |
| ECU | [Left electric parking brake](../../epbl.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | EPBL |
| Frame length | 5 bytes |
| Cycle time | 1000 ms |
| Signals | 6 |

## Signals of EPBL_seatStatus3

Tesla Model 3 CAN bus signals in `EPBL_seatStatus3`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `EPBL_frontSeatCushionFanCur` | Left electric parking brake: front seat cushion fan cur | 0\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | validated |
| `EPBL_frontSeatBackrestFanCur` | Left electric parking brake: front seat backrest fan cur | 12\|12 | little-endian | unsigned | 0.01 | 0 | A | 0 to 40.95 |  | validated |
| `EPBL_frontSeatCushionFanDuty` | Left electric parking brake: front seat cushion fan duty | 24\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `EPBL_frontSeatCushionFanEn` | Left electric parking brake: front seat cushion fan en | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBL_frontSeatBackrestFanEn` | Left electric parking brake: front seat backrest fan en | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBL_frontSeatBackrestFanDuty` | Left electric parking brake: front seat backrest fan duty | 33\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Left electric parking brake messages (EPBL)](../../epbl.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
