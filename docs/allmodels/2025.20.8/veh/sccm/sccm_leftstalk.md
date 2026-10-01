---
layout: default
title: "SCCM_leftStalk (0x249) — Steering column control module, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Steering column control module message: left stalk. Tesla Model 3 / Model Y CAN bus message SCCM_leftStalk (0x249) of Steering column control module, firmware 2025.20.8, 6 signals (SCCM_leftStalkCrc, SCCM_leftStalkCounter, SCCM_highBeamStalkStatus, SCCM_washWipeButtonStatus and 2 more). Bit layout, scaling, units and value tables."
---

# SCCM_leftStalk (0x249) — Steering column control module, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Steering column control module message: left stalk; frame length from the layout, not yet observed on a vehicle bus. This page documents the 6 signals of SCCM_leftStalk as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `SCCM_leftStalk` |
| CAN id | 0x249 (585) |
| ECU | [Steering column control module](../../sccm.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | SCCM |
| Frame length | 4 bytes |
| Cycle time | 50 ms |
| Signals | 6 |

## Signals of SCCM_leftStalk

Tesla Model 3 / Model Y CAN bus signals in `SCCM_leftStalk`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `SCCM_leftStalkCrc` | Steering column control module: left stalk crc | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `SCCM_leftStalkCounter` | Steering column control module: left stalk counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `SCCM_highBeamStalkStatus` | Active state of high beam push/pull stalk position; raw 3 = signal not available (SNA) | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `IDLE`<br>1 = `PULL`<br>2 = `PUSH`<br>3 = `SNA` | plausible |
| `SCCM_washWipeButtonStatus` | Active state of wash/wipe button on the turn signal stalk; raw 3 = signal not available (SNA) | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NOT_PRESSED`<br>1 = `1ST_DETENT`<br>2 = `2ND_DETENT`<br>3 = `SNA` | plausible |
| `SCCM_turnIndicatorStalkStatus` | Active state of turn indicator stalk position; raw 9 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `IDLE`<br>1 = `UP_0_5`<br>2 = `UP_1`<br>3 = `UP_1_5`<br>4 = `UP_2`<br>5 = `DOWN_0_5`<br>6 = `DOWN_1`<br>7 = `DOWN_1_5`<br>8 = `DOWN_2`<br>9 = `SNA` | plausible |
| `SCCM_turnIndicatorStalkAngle` | Measured angle of the turn signal stalk; raw 4095 = signal not available (SNA) | 20\|12 | little-endian | unsigned | 0.1 | -180 | deg | -180 to 180 | 4095 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Steering column control module messages (SCCM)](../../sccm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
