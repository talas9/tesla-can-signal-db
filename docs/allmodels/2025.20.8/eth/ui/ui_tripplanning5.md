---
layout: default
title: "UI_tripPlanning5 (0x497) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: trip planning5. Ethernet-side message UI_tripPlanning5 of Touchscreen user interface computer for Tesla Model 3 / Model Y firmware 2025.20.8, 3 signals (UI_battPreconditionOnNavTime, UI_maxBattPreconditionOnNavTime, UI_tripPlanChargingTargetPercent). Bit layout, scaling, units and value tables."
---

# UI_tripPlanning5 (0x497) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 ETH

Touchscreen user interface computer message: trip planning5. This page documents the 3 signals of UI_tripPlanning5 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_tripPlanning5` |
| Ethernet-side id | 0x497 (1175) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 6 bytes |
| Cycle time | 1000 ms |
| Signals | 3 |

## Signals of UI_tripPlanning5

Tesla Model 3 / Model Y CAN bus signals in `UI_tripPlanning5`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_battPreconditionOnNavTime` | Touchscreen user interface computer: batt precondition on nav time; raw 65535 = signal not available (SNA) | 0\|16 | little-endian | unsigned | 1 | 0 | s | 0 to 65534 | 65534 = `MAXVAL`<br>65535 = `SNA` | plausible |
| `UI_maxBattPreconditionOnNavTime` | Touchscreen user interface computer: max batt precondition on nav time; raw 65535 = signal not available (SNA) | 16\|16 | little-endian | unsigned | 1 | 0 | s | 0 to 65534 | 65534 = `MAXVAL`<br>65535 = `SNA` | plausible |
| `UI_tripPlanChargingTargetPercent` | Touchscreen user interface computer: trip plan charging target percent; raw 1023 = signal not available (SNA) | 32\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.2 | 1023 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
