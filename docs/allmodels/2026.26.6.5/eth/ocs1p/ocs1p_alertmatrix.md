---
layout: default
title: "OCS1P_alertMatrix (0x2FF) — Occupant classification system, Tesla Model 3 / Model Y 2026.26.6.5 ETH"
description: "Occupant classification system message: alert matrix. Ethernet-side message OCS1P_alertMatrix of Occupant classification system for Tesla Model 3 / Model Y firmware 2026.26.6.5, 35 signals (OCS1P_matrixIndex, OCS1P_w015_NVMMAlert, OCS1P_w121_sandwichOpen, OCS1P_w122_sandwichLow and 31 more). Bit layout, scaling, units and value tables."
---

# OCS1P_alertMatrix (0x2FF) — Occupant classification system, Tesla Model 3 / Model Y 2026.26.6.5 ETH

Occupant classification system message: alert matrix. This page documents the 35 signals of OCS1P_alertMatrix as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `OCS1P_alertMatrix` |
| Ethernet-side id | 0x2FF (767) |
| ECU | [Occupant classification system](../../ocs1p.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | OCS1P |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 35 |

## Signals of OCS1P_alertMatrix

Tesla Model 3 / Model Y CAN bus signals in `OCS1P_alertMatrix`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `OCS1P_matrixIndex` | selector | Occupant classification system: matrix index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `AlertMatrix0`<br>2 = `AlertMatrix2` | plausible |
| `OCS1P_w015_NVMMAlert` | page 0 | Occupant classification system: w015 NVMM alert | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w121_sandwichOpen` | page 2 | Occupant classification system: w121 sandwich open | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w122_sandwichLow` | page 2 | Occupant classification system: w122 sandwich low | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w123_sandwichShort` | page 2 | Occupant classification system: w123 sandwich short | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w124_cushionSelfOpen` | page 2 | Occupant classification system: w124 cushion self open | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w125_cushionSelfLow` | page 2 | Occupant classification system: w125 cushion self low | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w126_cushionSelfShort` | page 2 | Occupant classification system: w126 cushion self short | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w127_seatbackSelfOpen` | page 2 | Occupant classification system: w127 seatback self open | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w128_seatbackSelfLow` | page 2 | Occupant classification system: w128 seatback self low | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w129_seatbackSelfShort` | page 2 | Occupant classification system: w129 seatback self short | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w130_sandwichNoCalib` | page 2 | Occupant classification system: w130 sandwich no calib | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w131_cushionSelfNoCalib` | page 2 | Occupant classification system: w131 cushion self no calib | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w132_seatbackSelfNoCalib` | page 2 | Occupant classification system: w132 seatback self no calib | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w133_sandwichBadCalib` | page 2 | Occupant classification system: w133 sandwich bad calib | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w134_uninitializedCalib` | page 2 | Occupant classification system: w134 uninitialized calib | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w135_tempNoCalib` | page 2 | Occupant classification system: w135 temp no calib | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w136_cushionSelfDutyLow` | page 2 | Occupant classification system: w136 cushion self duty low | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w137_cushionSelfDutyHigh` | page 2 | Occupant classification system: w137 cushion self duty high | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w138_seatbackSelfDutyLow` | page 2 | Occupant classification system: w138 seatback self duty low | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w139_seatbackSelfDutyHigh` | page 2 | Occupant classification system: w139 seatback self duty high | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w140_tempInvalidCalib` | page 2 | Occupant classification system: w140 temp invalid calib | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w141_humidityInvalidCalib` | page 2 | Occupant classification system: w141 humidity invalid calib | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w142_tempHumidityInvalid` | page 2 | Occupant classification system: w142 temp humidity invalid | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w143_mismatchPassAirbag` | page 2 | Occupant classification system: w143 mismatch pass airbag | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w144_mismatchCarRegion` | page 2 | Occupant classification system: w144 mismatch car region | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w145_rebaselineTriggered` | page 2 | Occupant classification system: w145 rebaseline triggered | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w148_classificationMismatch` | page 2 | Occupant classification system: w148 classification mismatch | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w150_rbEntryTriggered` | page 2 | Occupant classification system: w150 rb entry triggered | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w151_rbEntryExited` | page 2 | Occupant classification system: w151 rb entry exited | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w152_rbExit1Triggered` | page 2 | Occupant classification system: w152 rb exit1 triggered | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w153_rbExit1Exited` | page 2 | Occupant classification system: w153 rb exit1 exited | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w154_rbExit2Exited1` | page 2 | Occupant classification system: w154 rb exit2 exited1 | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w155_rbExit2Exited2` | page 2 | Occupant classification system: w155 rb exit2 exited2 | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_w156_seatbeltReminderUnavailable` | page 2 | Occupant classification system: w156 seatbelt reminder unavailable | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`OCS1P_matrixIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (1 signals), page 2 (33 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/AllModels/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Occupant classification system messages (OCS1P)](../../ocs1p.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
