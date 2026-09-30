---
layout: default
title: "UI_tripPlanning5 (0x497) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 ETH"
description: "Touchscreen user interface computer message: trip planning5. Ethernet-side message UI_tripPlanning5 of Touchscreen user interface computer for Tesla Model 3 / Model Y firmware 2026.26.6.5, 2 signals (UI_battPreconditionOnNavTime, UI_maxBattPreconditionOnNavTime). Bit layout, scaling, units and value tables."
---

# UI_tripPlanning5 (0x497) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 ETH

Touchscreen user interface computer message: trip planning5. This page documents the 2 signals of UI_tripPlanning5 as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_tripPlanning5` |
| Ethernet-side id | 0x497 (1175) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 4 bytes |
| Cycle time | 1000 ms |
| Signals | 2 |

## Signals of UI_tripPlanning5

Tesla Model 3 / Model Y CAN bus signals in `UI_tripPlanning5`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_battPreconditionOnNavTime` | Touchscreen user interface computer: batt precondition on nav time; raw 65535 = signal not available (SNA) | 0\|16 | little-endian | unsigned | 1 | 0 | s | 0 to 65534 | 65534 = `MAXVAL`<br>65535 = `SNA` | plausible |
| `UI_maxBattPreconditionOnNavTime` | Touchscreen user interface computer: max batt precondition on nav time; raw 65535 = signal not available (SNA) | 16\|16 | little-endian | unsigned | 1 | 0 | s | 0 to 65534 | 65534 = `MAXVAL`<br>65535 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/AllModels/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
