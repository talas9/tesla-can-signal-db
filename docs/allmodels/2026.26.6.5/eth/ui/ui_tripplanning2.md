---
layout: default
title: "UI_tripPlanning2 (0x8B) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 ETH"
description: "Touchscreen user interface computer message: trip planning2. Ethernet-side message UI_tripPlanning2 of Touchscreen user interface computer for Tesla Model 3 / Model Y firmware 2026.26.6.5, 3 signals (UI_maxSpeedToReachDestination, UI_remainingWeightedRMSSpeed, UI_timeToDestination). Bit layout, scaling, units and value tables."
---

# UI_tripPlanning2 (0x8B) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 ETH

Touchscreen user interface computer message: trip planning2. This page documents the 3 signals of UI_tripPlanning2 as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_tripPlanning2` |
| Ethernet-side id | 0x8B (139) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 6 bytes |
| Cycle time | 1000 ms |
| Signals | 3 |

## Signals of UI_tripPlanning2

Tesla Model 3 / Model Y CAN bus signals in `UI_tripPlanning2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_maxSpeedToReachDestination` | maximum speed to reach destination without significant risk of running out of energy; raw 65535 = signal not available (SNA) | 0\|16 | little-endian | unsigned | 0.01 | 0 | m/s | 0 to 655.34 | 65533 = `MAXVAL`<br>65534 = `UNREACHABLE`<br>65535 = `SNA` | validated |
| `UI_remainingWeightedRMSSpeed` | Touchscreen user interface computer: remaining weighted RMS speed; raw 65535 = signal not available (SNA) | 16\|16 | little-endian | unsigned | 0.01 | 0 | m/s | 0 to 655.34 | 65534 = `MAXVAL`<br>65535 = `SNA` | plausible |
| `UI_timeToDestination` | remaining time to reach destination; raw 65535 = signal not available (SNA) | 32\|16 | little-endian | unsigned | 1 | 0 | s | 0 to 65534 | 65534 = `MAXVAL`<br>65535 = `SNA` | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/AllModels/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
